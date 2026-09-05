# Formula–Theorem Ledger — Seven Directions / X–Y–Z

**Date:** 2026-09-04  
**Status:** `RESEARCH_LEDGER_ACTIVE`  
**claim_allowed:** `false`

## Purpose

This ledger converts RAFAELIA mathematical claims into proof obligations. It is deliberately stricter than a conceptual map.

Each entry is represented by:

\[
\mathbb T_i=(S_i,A_i,P_i,C_i,N_i,E_i,R_i)
\]

where:

- `S`: statement;
- `A`: assumptions;
- `P`: proof or derivation;
- `C`: counterexample/falsifier;
- `N`: numerical reproduction;
- `E`: empirical mapping;
- `R`: repository/source authority.

The same object is scored in:

\[
\mathbf E_i=(X_i,Y_i,Z_i)
\]

with `X=mathematical validity`, `Y=physical/empirical support`, `Z=computational reproducibility`.

## Seven directions

1. Pure mathematics and proof.
2. Dynamical systems / graph theory / topology.
3. Physics / optics / thermodynamics.
4. Information theory / AI / adaptive search.
5. Qudits / BITRAF / quantum hardware requirements.
6. RLL epistemic classification.
7. Publication, theorem and Clay-problem proof obligations.

## Canonical initial entries

### T-001 — Equilateral-triangle ratio

Statement:

\[
q=\frac{\sqrt3}{2}=\cos30^\circ=\sin60^\circ.
\]

Assumptions: Euclidean geometry, equilateral triangle.

Proof: split an equilateral triangle of side `a` into two right triangles and apply Pythagoras:

\[
h^2+(a/2)^2=a^2\Rightarrow h=a\sqrt3/2.
\]

State: `EXACT_IDENTITY`.

Physical mapping: `TOKEN_VAZIO` unless a measured system independently identifies this ratio.

### T-002 — Affine Rafael recurrence

\[
F_{n+1}=qF_n+c.
\]

For constant `q != 1`:

\[
F_n=q^nF_0+c\frac{1-q^n}{1-q}.
\]

For `|q|<1`:

\[
F_n\to\frac{c}{1-q}.
\]

State: `VALID_DEFINITION`; convergence theorem under the stated assumptions.

Blocked equivalence: this is not the canonical Fibonacci recurrence.

### T-003 — Quadratic-map fixed-point stability

\[
f(z)=z^2+c,
\quad z^*=f(z^*)
\]

implies

\[
z^{*2}-z^*+c=0,
\qquad
z^*_\pm=\frac{1\pm\sqrt{1-4c}}2.
\]

Local asymptotic stability condition:

\[
|f'(z^*)|=|2z^*|<1.
\]

State: `EXACT_LOCAL_DYNAMICS`.

### T-004 — 42 hyperforms by Cartesian product

Given seven operational coordinates and six operators:

\[
|\mathcal H|=7\times6=42.
\]

State: `EXACT_COUNT_BY_DEFINITION`.

Blocked claim: `42` is not thereby a universal physical constant.

### T-005 — Spectrum of uniform K42

For the complete graph:

\[
L(K_{42})=42I-J.
\]

Therefore:

\[
\operatorname{spec}L=\{0,42^{(41)}\}.
\]

State: `EXACT_GRAPH_THEORY`.

Consequence: labels `6`, `7`, `14`, `21` are not privileged spectral modes of uniform K42.

### T-006 — Circulant 6/7 model

For weighted modular jumps `±6, ±7`:

\[
\lambda_k=2w_6+2w_7-2w_6\cos(2\pi6k/42)-2w_7\cos(2\pi7k/42).
\]

State: `VALID_MODEL_IF_GRAPH_DEFINED`.

Required falsifier: compare against degree-preserving null graphs and source-graph weights.

### T-007 — Recurrence with append-only memory

A bounded measure-preserving operational subsystem may satisfy Poincaré recurrence while an augmented append-only memory state does not return exactly:

\[
X_{n+p}\approx X_n,
\qquad
M_{n+p}\ne M_n.
\]

State: `VALID_DISTINCTION`; Poincaré theorem applies only after its measure-preserving hypotheses are demonstrated.

### T-008 — Normalized alignment

For nonzero compatible vectors:

\[
F_{align}=\frac{\langle a,b\rangle}{\|a\|\|b\|}
\]

satisfies

\[
-1\le F_{align}\le1
\]

by Cauchy–Schwarz.

State: `EXACT_WITH_NONZERO_NORMS`.

### T-009 — BITRAF as a 20-state mathematical system

A 20-level state can be represented in:

\[
\mathcal H_{20}=\mathbb C^{20}.
\]

State: `KNOWN_MATHEMATICAL_FORM`; authorial novelty must lie in gates, code, correction, physical implementation or other structure—not in dimensionality alone.

### T-010 — Physical BITRAF chip

Required object:

\[
\mathcal Q_{20}=(\mathcal H_{20},\mathcal G,\mathcal M,\mathcal N,\mathcal C).
\]

Required evidence includes state preparation, gate set, readout, noise characterization, coherence, multipartite operation and reproducible device records.

State: `TOKEN_VAZIO_PHYSICAL_IMPLEMENTATION`.

## Clay-problem rule

Any relation to a Clay Millennium Problem remains one of:

- `BACKGROUND_RELATION`;
- `HEURISTIC_CONNECTION`;
- `PARTIAL_LEMMA`;
- `NUMERICAL_EVIDENCE`;
- `PROOF_CANDIDATE`;
- `PROOF_EXTERNALLY_VERIFIED`.

No file title or symbolic analogy is sufficient to use `PROOF_EXTERNALLY_VERIFIED`.

## Adaptive prioritization

For open entries, define:

\[
Priority_i=
\alpha U_i+
\beta E_{contra,i}+
\gamma IG_i+
\delta I_{proof,i}+
\epsilon I_{dependency,i}.
\]

High priority means the next finite calculation or counterexample is expected to remove the most uncertainty.

## Immediate queue

1. Close exact proofs and known counterexamples first.
2. Extract the actual source graph for 42 hyperforms.
3. Run circulant-vs-null spectral comparisons.
4. Separate BITRAF classical multistate coding from qudit physics.
5. Require reproducible data for cosmology/cryptography/biology claims.
6. Keep every unresolved physical equivalence as `TOKEN_VAZIO`.

## Publication invariant

\[
\text{mathematical coherence}\neq\text{physical validation}\neq\text{independent proof}.
\]
