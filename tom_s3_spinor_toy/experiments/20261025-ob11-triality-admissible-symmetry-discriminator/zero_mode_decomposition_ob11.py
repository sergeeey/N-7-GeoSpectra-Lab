"""OB11 follow-up: where do the zero modes of the Round59 algebraic Dirac matrix sit under G = su(3)?

Fibre = C^8 (x) C^8 (64-dim), G acts by the Leibniz lift L(X) = X (x) I + I (x) X (commutes with D, C78 E2b).
Steps:
  Z1  L(X_a) commute with D (exact check to float tolerance)
  Z2  G-isotypic decomposition of the fibre via the Casimir of L (eigenspaces)
  Z3  dim ker(D restricted to each isotypic eigenspace)  -> zero modes sit in which G-block?
  Z4  for each block: is the zero-mode subspace G-invariant? (a non-trivial G-multiplet of zero modes
      would make the multiplicity G-related; an invariant zero mode is a G-singlet)
Scope: float64. Descriptive (L0). Algebraic matrix D, same object as C78 and round59 fibre analysis.
"""

import importlib.util
import json
import pathlib

import numpy as np
import sympy as sp

R59PATH = pathlib.Path(__file__).resolve().parents[2] / "experiments" / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
spec = importlib.util.spec_from_file_location("r59", R59PATH)
R59 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R59)

sqrt3 = sp.sqrt(3)
E = R59.build_clifford()
D = np.array(R59.build_dirac(E, R59.NOMIZU).evalf(), dtype=complex)
X = []
for a in range(1, 9):
    Xa = R59.spin_lift(R59.ADNU[a], E)
    scale = 4 * sqrt3 if a == 8 else 4
    X.append(np.array((scale * Xa).evalf(), dtype=complex))
I8 = np.eye(8)
L = [np.kron(x, I8) + np.kron(I8, x) for x in X]
PASS = True
out = {}


def report(name, good):
    global PASS
    PASS = PASS and bool(good)
    print("PASS" if good else "FAIL", name, flush=True)


# Z1
z1 = max(np.linalg.norm(D @ Lm - Lm @ D) for Lm in L)
print(f"    max |[D, L(X_a)]| = {z1:.2e}", flush=True)
report("Z1 [D, L(X_a)] = 0 for all a (G commutes with D)", z1 < 1e-8)

# Casimir of L with the trace-form Gram matrix on C^8
G8 = np.array([[np.trace(X[a] @ X[b]) for b in range(8)] for a in range(8)]).real
Ginv = np.linalg.inv(G8)
C64 = sum(Ginv[a, b] * L[a] @ L[b] for a in range(8) for b in range(8))
w, V = np.linalg.eig(C64)
vals = np.unique(np.round(w.real, 6))
blocks = {}
for v in vals:
    idx = np.where(np.abs(w - v) < 1e-5)[0]
    Q, _ = np.linalg.qr(V[:, idx])
    blocks[float(v)] = Q
print("    Casimir values on the fibre (value: dim):", {float(v): int(b.shape[1]) for v, b in blocks.items()}, flush=True)
out["casimir_dims"] = {str(v): int(b.shape[1]) for v, b in blocks.items()}
report("Z2 fibre splits into Casimir eigenspaces (at least 3 distinct values)", len(blocks) >= 3)

# Z3: kernel of D inside each isotypic block (D preserves each block by Z1)
kernel_by_block = {}
for v, Q in blocks.items():
    M = Q.conj().T @ D @ Q  # D restricted to the block (block is D-invariant)
    res = np.linalg.norm(D @ Q - Q @ M)
    assert res < 1e-7, f"block not D-invariant at Casimir {v}: {res}"
    s = np.linalg.svd(M, compute_uv=False)
    k = int(np.sum(s < 1e-8 * max(1.0, s[0])))
    kernel_by_block[v] = k
    print(f"    block Casimir {v:.4f} dim {Q.shape[1]}: dim ker D|block = {k}", flush=True)
out["kernel_by_block"] = {str(v): k for v, k in kernel_by_block.items()}
total = sum(kernel_by_block.values())
print("    total dim ker D on fibre:", total, flush=True)
report("Z3 zero modes are located in the isotypic blocks (total kernel computed)", True)

# Z4: which blocks carry zero modes, and is that G-invariant?
carrying = {str(v): k for v, k in kernel_by_block.items() if k > 0}
print("    blocks carrying zero modes:", carrying, flush=True)
trivial_only = all(abs(v) < 1e-6 for v in kernel_by_block if kernel_by_block[v] > 0)
verdict = ("ZERO_MODES_IN_G_SINGLET_BLOCK_ONLY" if trivial_only else "ZERO_MODES_IN_NON_SINGLET_BLOCK")
out["verdict"] = verdict
out["zero_mode_blocks"] = carrying
print("VERDICT:", verdict, flush=True)
report("Z4 classification recorded (verdict above)", True)

pathlib.Path(__file__).with_name("results_zero_modes_ob11.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print("ALL PASS" if PASS else "SOME FAILED", flush=True)
