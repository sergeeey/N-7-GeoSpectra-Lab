r"""
C152 STEP 5 -- is the cancellation caused by J (nearly-Kahler structure) or by
m being ROOT-type? Step 4 left this as a correlation on n=2 spaces, which is
exactly the kind of pattern-match this project's own rules refuse to promote.

THE DIRECT TEST
  On SU(3)/T^2 there are 8 invariant almost-complex structures (one sign per
  root plane; C151 Stage 1a: 6 integrable, 2 non-integrable). Each gives a
  DIFFERENT V, hence a different Sigma_even/Sigma_odd split, hence different
  invariant sectors -- but m itself is unchanged, still root-type.

    zero for ALL 8      -> J is irrelevant; the cause is a property of m
                           (supports the root-type explanation)
    zero only for NK J  -> the cause IS the nearly-Kahler structure
                           (refutes the root-type explanation)

  This discriminates the two readings on the SAME space, so it does not rest
  on comparing two different manifolds.

Run:  python c152_step5_j_scan.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)
E_sym = R59.build_clifford(conj=False)
E = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
PAIRS_M = [(0, 1), (0, 2), (1, 2)]
I6, I8 = np.eye(6), np.eye(8)


def spin_lift_np(L):
    out = np.zeros((8, 8), dtype=complex)
    for a in range(6):
        for b in range(a + 1, 6):
            if abs(L[a, b]) > 1e-14:
                out += L[a, b] * 0.5 * (E[a + 1] @ E[b + 1])
    return out


def build(eps):
    """C151 Stage 2a's construction, parametrised by the a.c.s. sign tuple."""
    basis = []
    for k, (p, q) in enumerate(PAIRS_M):
        X = np.zeros((3, 3), dtype=complex)
        X[p, q], X[q, p] = 1, -1
        Y = np.zeros((3, 3), dtype=complex)
        Y[p, q], Y[q, p] = 1j, 1j
        basis.extend([X, Y] if eps[k] > 0 else [Y, X])
    def killing_B(A, C):
        """CH2016's B(X,Y) = -(1/12)Tr(ad X ad Y) = -(1/2)Tr(XY) for su(3)."""
        return -0.5 * np.trace(A @ C)

    def to_m(M):
        """Coordinates of M in the (J-aligned) m basis."""
        return np.array([killing_B(M, b).real for b in basis])

    gram = np.array([[killing_B(a, b) for b in basis] for a in basis])
    assert np.max(np.abs(gram - I6)) < 1e-12, f"basis not B-orthonormal for eps={eps}"
    lam = {}
    for i in range(6):
        L = np.zeros((6, 6))
        for j in range(6):
            L[:, j] = 0.5 * to_m(basis[i] @ basis[j] - basis[j] @ basis[i])
        lam[i + 1] = L
    def cartan(h):
        A = 1j * np.diag(h).astype(complex)
        return np.array([to_m(A @ basis[j] - basis[j] @ A) for j in range(6)]).T
    t2 = [cartan((1.0, -1.0, 0.0)), cartan((0.0, 1.0, -1.0))]
    rho = [spin_lift_np(g) for g in t2]
    # C151 Stage 2a's own generator, VERBATIM: +t2, because cartan_on_m is
    # already the vector action (built from commutators), unlike S^6's ADNU
    # which is stored as a BIVECTOR and needs rho_vector = -bivec. Using -t2
    # here silently builds a different action -- it produced a false
    # "all 8 nonzero" scan before the C151 gate below caught it.
    gens = [np.kron(rho[a], I6) + np.kron(I8, t2[a]) for a in range(2)]

    # even/odd blocks of Sigma, read off from the SAME chirality operator
    # round59 uses, so the split is not re-chosen per eps
    def sector(rows):
        idx = [r * 6 + c for r in rows for c in range(6)]
        P = np.zeros((48, len(idx)))
        for k, j in enumerate(idx):
            P[j, k] = 1.0
        _, sv, vh = np.linalg.svd(np.vstack([P.T @ g @ P for g in gens]))
        pad = np.concatenate([sv, np.zeros(len(idx) - len(sv))])
        return P @ vh.conj().T[:, np.abs(pad) < 1e-8]

    d, t = sector(R59.ODD_IDX), sector(R59.EVEN_IDX)
    T1 = sum(np.kron(E[i] @ spin_lift_np(lam[i]), I6) for i in range(1, 7))
    T2 = sum(np.kron(E[i], -lam[i]) for i in range(1, 7))
    return d, t, t.conj().T @ T1 @ d, t.conj().T @ T2 @ d


# --- HARD GATE: the NK eps C151 actually used MUST reproduce its zero -------
_d, _t, _b1, _b2 = build((-1, 1, -1))
assert _d.shape[1] == 3 and _t.shape[1] == 3, f"sector dims wrong: {_d.shape[1]},{_t.shape[1]}"
print(f"GATE  eps=(-1,1,-1) [C151's own J]: max|Term1| = {np.max(np.abs(_b1)):.3e}, "
      f"max|Term2| = {np.max(np.abs(_b2)):.3e}")
assert np.max(np.abs(_b2)) < 1e-10, (
    "C151 REGRESSION FAILED: this rebuild does not reproduce C151's zero -- "
    "the construction is wrong, do NOT read the scan below")
print("GATE  C151 regression PASSED -- the rebuild is faithful")

print("=" * 78)
print("SCAN OVER ALL 8 INVARIANT ALMOST-COMPLEX STRUCTURES ON SU(3)/T^2")
print("=" * 78)
print(f"{'eps':>14}  {'kind':<16} {'dom':>4} {'tgt':>4}  {'max|Term1|':>12}  {'max|Term2|':>12}")
NON_INT = {(1, -1, 1), (-1, 1, -1)}  # C151 Stage 1a, pinned by Nijenhuis
rows = []
for e1 in (1, -1):
    for e2 in (1, -1):
        for e3 in (1, -1):
            eps = (e1, e2, e3)
            d, t, b1, b2 = build(eps)
            kind = "NON-INT (NK)" if eps in NON_INT else "integrable"
            v1, v2 = float(np.max(np.abs(b1))), float(np.max(np.abs(b2)))
            rows.append((eps, kind, v2))
            print(f"{eps!s:>14}  {kind:<16} {d.shape[1]:>4} {t.shape[1]:>4}  "
                  f"{v1:>12.3e}  {v2:>12.3e}")

nk_zero = all(v < 1e-10 for e, k, v in rows if e in NON_INT)
int_zero = all(v < 1e-10 for e, k, v in rows if e not in NON_INT)
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  Term2 block zero for the 2 NEARLY-KAHLER J : {nk_zero}")
print(f"  Term2 block zero for the 6 INTEGRABLE  J   : {int_zero}")
print()
if nk_zero and int_zero:
    print("  -> J IS IRRELEVANT. The Term2 block vanishes for every invariant")
    print("     almost-complex structure on SU(3)/T^2, integrable or not. So the")
    print("     cancellation is NOT a nearly-Kahler phenomenon; it is a property")
    print("     of m itself on this coset. This SUPPORTS the root-type reading")
    print("     and REMOVES the NK structure as the explanation.")
elif nk_zero and not int_zero:
    print("  -> J MATTERS. The zero is specific to the nearly-Kahler J, so the")
    print("     root-type explanation is REFUTED and the cause is the NK structure.")
else:
    print("  -> Mixed / unexpected pattern -- read the table, do not summarise it.")
