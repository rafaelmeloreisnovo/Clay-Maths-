# Autores / Authors: Rafael Melo Reis (Autor Principal) & GPT-5 (IA Coautora Técnica)
import numpy as np
from scipy.stats import median_abs_deviation
from numpy.linalg import inv

H0 = 0.001
OMEGA_DE = 0.7
LAMBDA = 0.1
TIMESTEPS = 500
N_FEATURES = 8
np.random.seed(42)

features = np.random.rand(TIMESTEPS, N_FEATURES)
dark_signal = np.sin(np.linspace(0, 20*np.pi, TIMESTEPS))*0.3
features[:,4] += dark_signal
features[:,5] += dark_signal

def robust_clip(x, k=3.5):
    m = np.median(x, axis=0)
    mad = median_abs_deviation(x, axis=0)
    return np.clip(x, m - k*mad, m + k*mad)

class Cluster:
    def __init__(self, x):
        self.mu = x.copy()
        self.Sigma = np.eye(len(x))*0.1
    def mahalanobis(self, x):
        diff = x - self.mu
        return np.sqrt(diff.T @ inv(self.Sigma) @ diff)
    def update(self, x):
        diff = x - self.mu
        self.mu = (1 - LAMBDA)*self.mu + LAMBDA*x
        self.Sigma = (1 - LAMBDA)*self.Sigma + LAMBDA*np.outer(diff, diff)

clusters = []
for t in range(TIMESTEPS):
    x_t = features[t]*(1+OMEGA_DE*(1 - np.exp(-H0*t)))
    x_t = robust_clip(x_t[np.newaxis,:])[0]
    if clusters:
        d = [c.mahalanobis(x_t) for c in clusters]
        idx = np.argmin(d)
        if d[idx]<3.0:
            clusters[idx].update(x_t)
        else:
            clusters.append(Cluster(x_t))
    else:
        clusters.append(Cluster(x_t))
