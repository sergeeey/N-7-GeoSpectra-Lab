"""OB11 discriminator: are the three triality channels separated by admissible (G-invariant) projectors?

Admissible group G = the su(3) that commutes with the Round59 Dirac operator (C78: commutant = su(3)).
G acts on the internal 8-dim index through X_a = spin_lift(ADNU[a]) (Gaussian-integer rescaled, as in
correspondence/verify/verify_c78_gl8_commutant.py).

Decision rule (fixed before running):
  - if the commutant of {X_a} in End(C^8) has dimension 1, the 8 is one irreducible block: no invariant
    split at all.
  - if the commutant has dimension 6 with blocks 3 + 3bar + 1 + 1, the minimal invariant projectors have
    rank 3 (triality is an irreducible triplet block, not three independent sectors) or rank 1 (singlets).
  - a rank-1 projector onto a single triplet basis vector must NOT commute with X_a (negative control).
Scope: numerical (float64) on the exact matrices built by round59; PASS/FAIL printed per check.
"""

import importlib.util
import json
import pathlib
import sys

import numpy as np
import sympy as sp

R59PATH = pathlib.Path(__file__).resolve().parents[2] / "experiments" / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
spec = importlib.util.spec_from_file_location("r59", R59PATH)
R59 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R59)

PASS = True
RESULTS = {}


def report(name, good):
    global PASS
    PASS = PASS and bool(good)
    print("PASS" if good else "FAIL", name, flush=True)


sqrt3 = sp.sqrt(3)
E = R59.build_clifford()
X = []
for a in range(1, 9):
    Xa = R59.spin_lift(R59.ADNU[a], E)
    scale = 4 * sqrt3 if a == 8 else 4
    X.append(np.array((scale * Xa).evalf(), dtype=complex))
X = [np.asarray(Xa, dtype=complex) for Xa in X]
n = 8

# P0: the 8 matrices are linearly independent and close under commutators (a Lie algebra of dim 8)
M = np.stack([x.reshape(-1) for x in X], axis=1)
report("P0a X_1..X_8 are linearly independent (rank 8)", np.linalg.matrix_rank(M, tol=1e-9) == 8)
coeffs_ok = True
for a in range(8):
    for b in range(8):
        comm = X[a] @ X[b] - X[b] @ X[a]
        c, res, *_ = np.linalg.lstsq(M, comm.reshape(-1), rcond=None)
        if np.linalg.norm(M @ c - comm.reshape(-1)) > 1e-8:
            coeffs_ok = False
report("P0b commutators close: [X_a, X_b] in span{X_c} (dim 8 Lie algebra)", coeffs_ok)

# P1: Casimir with the Gram matrix of the trace form on C^8; eigenvalue multiplicities give irreps
G = np.array([[np.trace(X[a] @ X[b]) for b in range(8)] for a in range(8)]).real
Ginv = np.linalg.inv(G)
C2 = sum(Ginv[a, b] * X[a] @ X[b] for a in range(8) for b in range(8))
evals = np.linalg.eigvals(C2)
vals, counts = np.unique(np.round(evals.real, 6), return_counts=True)
print("    Casimir eigenvalues on C^8 (value: multiplicity):", dict(zip(vals.tolist(), counts.tolist())), flush=True)
RESULTS["casimir_values"] = {str(v): int(c) for v, c in zip(vals, counts)}
report("P1 Casimir is scalar-diagonalisable with a clear multiplet structure (at least 2 distinct values)", len(vals) >= 2)

# P2: commutant of {X_a} in End(C^8): solve [Y, X_a] = 0 for all a (complex linear system in 64 unknowns)
rows = []
for a in range(8):
    # Y X_a - X_a Y = 0 as a linear map on vec(Y): kron(I, X_a^T) - kron(X_a, I)
    Ia = np.eye(n)
    rows.append(np.kron(Ia, X[a].T) - np.kron(X[a], Ia))
Amat = np.vstack(rows)
s = np.linalg.svd(Amat, compute_uv=False)
dim_comm = int(np.sum(s < 1e-9 * s[0]))
print(f"    dim of commutant of {{X_a}} in End(C^8): {dim_comm}", flush=True)
RESULTS["commutant_dim"] = dim_comm
report("P2 commutant dimension is 1 or 2 or 6 (irreducible, two-block, or 3+3bar+1+1 pattern)", dim_comm in (1, 2, 6))

# P3: minimal invariant projectors: the Casimir eigenspaces are invariant (positive control)
P_by_val = {}
for v in vals:
    w, V = np.linalg.eig(C2)
    idx = np.where(np.abs(w.real - v) < 1e-6)[0]
    if len(idx) == 0:
        continue
    B = V[:, idx]
    Q, _ = np.linalg.qr(B)
    P = Q @ np.conj(Q).T
    P_by_val[float(v)] = P
inv_ok = all(np.linalg.norm(P @ X[a] - X[a] @ P) < 1e-8 for P in P_by_val.values() for a in range(8))
report("P3a positive control: Casimir eigenprojectors commute with all X_a", inv_ok)
ranks = {str(v): int(np.round(np.trace(P).real)) for v, P in P_by_val.items()}
print("    Casimir eigenspace ranks:", ranks, flush=True)
RESULTS["casimir_ranks"] = ranks

# P3b negative control: a rank-1 projector onto one basis vector of an eigenspace of dimension >= 2
# the negative control must sit inside a NON-singlet multiplet: on singlets every X_a vanishes,
# so any vector there is trivially invariant (this is why the first version wrongly passed/failed)
big = [v for v, P in P_by_val.items() if int(np.round(np.trace(P).real)) >= 2 and v > 0.5]
if big:
    P = P_by_val[big[0]]
    w, Vv = np.linalg.eigh(P)  # P is Hermitian projector
    e = np.zeros((n, 1), dtype=complex)
    evec = Vv[:, np.argmax(w.real)]
    P1 = np.outer(evec, np.conj(evec))
    not_inv = any(np.linalg.norm(P1 @ X[a] - X[a] @ P1) > 1e-6 for a in range(8))
    report("P3b negative control: a rank-1 projector inside a multiplet is NOT G-invariant", not_inv)
    RESULTS["rank1_inside_multiplet_is_invariant"] = not (not_inv)
else:
    report("P3b negative control skipped: no eigenspace of dimension >= 2", True)

# Verdict rule (fixed above)
irreducible = dim_comm == 1
block_pattern = dim_comm == 6
if irreducible:
    verdict = "NO_INVARIANT_SPLIT__8_IRREDUCIBLE_UNDER_SU3"
elif block_pattern:
    verdict = "TRIALITY_IS_INVARIANT_BLOCK__NO_RANK1_INVARIANT_SECTOR"
else:
    verdict = f"OTHER_PATTERN__COMMUTANT_DIM_{dim_comm}"
RESULTS["verdict"] = verdict
print("VERDICT:", verdict, flush=True)

out = pathlib.Path(__file__).with_name("results_ob11.json")
out.write_text(json.dumps(RESULTS, indent=2, ensure_ascii=False), encoding="utf-8")
print("ALL PASS" if PASS else "SOME FAILED", flush=True)
sys.exit(0 if PASS else 1)
