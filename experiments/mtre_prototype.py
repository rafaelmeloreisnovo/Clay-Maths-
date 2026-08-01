#!/usr/bin/env python3
"""MTRE V1: deterministic routed views over immutable bytes.

Standard-library-only proof of concept. It creates:
  payload.bin, routes.bin, anchors.bin, ledger.bin
and validates routed reconstruction with SHA-256.
"""
from __future__ import annotations

import hashlib
import json
import os
import struct
import time
from pathlib import Path

CHUNK = 4096
ROUTE_REC = struct.Struct("<II")  # chunk_index, byte_count


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def append_ledger(path: Path, event: dict) -> None:
    with path.open("ab") as fp:
        fp.write(json.dumps(event, sort_keys=True, separators=(",", ":")).encode() + b"\n")


def build(out: Path, size: int = 2 * 1024 * 1024) -> None:
    out.mkdir(parents=True, exist_ok=True)
    payload = bytes((i * 131 + (i >> 7) + 17) & 0xFF for i in range(size))
    payload_path = out / "payload.bin"
    routes_path = out / "routes.bin"
    anchors_path = out / "anchors.bin"
    ledger_path = out / "ledger.bin"
    payload_path.write_bytes(payload)

    chunks = (len(payload) + CHUNK - 1) // CHUNK
    # Deterministic non-linear route: evens then odds. No payload duplication.
    order = list(range(0, chunks, 2)) + list(range(1, chunks, 2))
    with routes_path.open("wb") as fp:
        for idx in order:
            count = min(CHUNK, len(payload) - idx * CHUNK)
            fp.write(ROUTE_REC.pack(idx, count))

    anchors = {
        "format": "MTRE-V1",
        "chunk_size": CHUNK,
        "route": "even_chunks_then_odd_chunks",
        "payload_sha256": sha256(payload),
        "source_size": len(payload),
        "reversible": True,
        "claim_allowed": False,
    }
    anchors_path.write_text(json.dumps(anchors, indent=2, sort_keys=True), encoding="utf-8")
    append_ledger(ledger_path, {"event": "BUILD", **anchors, "time_ns": time.time_ns()})


def read_route(routes_path: Path) -> list[tuple[int, int]]:
    raw = routes_path.read_bytes()
    if len(raw) % ROUTE_REC.size:
        raise ValueError("routes.bin has a truncated record")
    return [ROUTE_REC.unpack_from(raw, off) for off in range(0, len(raw), ROUTE_REC.size)]


def routed_view(payload: bytes, route: list[tuple[int, int]]) -> bytes:
    return b"".join(payload[idx * CHUNK : idx * CHUNK + count] for idx, count in route)


def reverse_route(view: bytes, route: list[tuple[int, int]], source_size: int) -> bytes:
    restored = bytearray(source_size)
    cursor = 0
    for idx, count in route:
        restored[idx * CHUNK : idx * CHUNK + count] = view[cursor : cursor + count]
        cursor += count
    if cursor != len(view):
        raise ValueError("route/view length mismatch")
    return bytes(restored)


def benchmark(out: Path, repeats: int = 9) -> dict:
    payload_path = out / "payload.bin"
    routes_path = out / "routes.bin"
    anchors_path = out / "anchors.bin"
    ledger_path = out / "ledger.bin"
    anchors = json.loads(anchors_path.read_text(encoding="utf-8"))
    route = read_route(routes_path)
    linear_ns, routed_ns = [], []
    restored_digest = ""

    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        payload = payload_path.read_bytes()
        linear_ns.append(time.perf_counter_ns() - t0)

        t0 = time.perf_counter_ns()
        view = routed_view(payload, route)
        restored = reverse_route(view, route, anchors["source_size"])
        routed_ns.append(time.perf_counter_ns() - t0)
        restored_digest = sha256(restored)
        if restored_digest != anchors["payload_sha256"]:
            append_ledger(ledger_path, {"event": "FAIL", "reason": "digest_mismatch", "time_ns": time.time_ns()})
            raise SystemExit("FAIL: reconstruction digest mismatch")

    linear_sorted = sorted(linear_ns)
    routed_sorted = sorted(routed_ns)
    p95_index = max(0, min(repeats - 1, int(0.95 * repeats) - 1))
    result = {
        "event": "BENCHMARK_PASS",
        "repeats": repeats,
        "payload_bytes": payload_path.stat().st_size,
        "routes_bytes": routes_path.stat().st_size,
        "anchors_bytes": anchors_path.stat().st_size,
        "ledger_bytes_before_append": ledger_path.stat().st_size,
        "linear_median_ns": linear_sorted[repeats // 2],
        "linear_p95_ns": linear_sorted[p95_index],
        "route_reconstruct_median_ns": routed_sorted[repeats // 2],
        "route_reconstruct_p95_ns": routed_sorted[p95_index],
        "source_sha256": anchors["payload_sha256"],
        "restored_sha256": restored_digest,
        "bit_exact": True,
        "time_ns": time.time_ns(),
    }
    append_ledger(ledger_path, result)
    return result


def main() -> None:
    out = Path(os.environ.get("MTRE_OUT", "mtre_run"))
    build(out)
    result = benchmark(out)
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"ARTIFACTS={out.resolve()}")


if __name__ == "__main__":
    main()
