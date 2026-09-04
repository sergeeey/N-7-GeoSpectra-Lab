r"""
C151 STAGE 1a -- pin the nearly-Kahler J on SU(3)/T^2 BY COMPUTATION, then
test the pre-committed failure mode. The connection coefficient c is STILL
not computed here.

WHY J MUST BE PINNED BY COMPUTATION, NOT ASSERTED
  On the flag manifold SU(3)/T^2 there are SEVERAL invariant almost-complex
  structures: one sign eps_i in {+1,-1} per positive-root plane, so 2^3 = 8
  of them. Some are integrable (Kahler), some are not; the NEARLY-KAHLER one
  is a NON-INTEGRABLE representative. The pre-registration's invalidation
  criterion #1 forbids choosing J after seeing c, so J is fixed here, before
  c exists, by an objective computation: the Nijenhuis tensor.

    N(X,Y) = [JX,JY] - J[JX,Y] - J[X,JY] - [X,Y]

  N == 0  <=>  integrable (Kahler candidate)
  N != 0  <=>  non-integrable (nearly-Kahler candidate)

  Brackets are the m-projections of the su(3) commutators (reductive
  decomposition su(3) = t^2 (+) m), computed here from 3x3 matrices directly.

THE PRE-COMMITTED FAILURE MODE THIS ALSO TESTS
  The restatement frozen in PREREGISTRATION.md states: if J does not map the
  admissible connection family into itself, the prediction is NOT WELL-POSED
  on this coset (BLOCKED-STRUCTURE) and that is the finding -- it must not be
  worked around by swapping J or the family until something matches. That
  check is run below.

BASIS (same as Stage 0, restated so this file is self-contained)
  m has real basis, per pair p<q:  X_pq = E_pq - E_qp,  Y_pq = i(E_pq + E_qp)
  ordered (X_12, Y_12, X_13, Y_13, X_23, Y_23).
  For an off-diagonal anti-Hermitian M:  M = Re(M_pq)*X_pq + Im(M_pq)*Y_pq.

Run:  python c151_stage1a_pin_J.py
"""

import importlib.util
import itertools
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C73B = load_module("c73b_torsion_family", C73B_PATH)

PAIRS_M = [(0, 1), (0, 2), (1, 2)]  # (p,q) for m_12, m_13, m_23


def basis_m() -> list[np.ndarray]:
    """The 6 real basis elements of m as 3x3 anti-Hermitian matrices."""
    out = []
    for p, q in PAIRS_M:
        X = np.zeros((3, 3), dtype=complex)
        X[p, q], X[q, p] = 1, -1
        Y = np.zeros((3, 3), dtype=complex)
        Y[p, q], Y[q, p] = 1j, 1j
        out.extend([X, Y])
    return out


M_BASIS = basis_m()


def to_m_coords(mat: np.ndarray) -> np.ndarray:
    """Project a 3x3 anti-Hermitian matrix onto m and return its 6 real coords."""
    c = np.zeros(6)
    for k, (p, q) in enumerate(PAIRS_M):
        c[2 * k] = mat[p, q].real
        c[2 * k + 1] = mat[p, q].imag
    return c


def bracket_m(i: int, j: int) -> np.ndarray:
    """m-projection of [e_i, e_j] in m-coordinates."""
    comm = M_BASIS[i] @ M_BASIS[j] - M_BASIS[j] @ M_BASIS[i]
    return to_m_coords(comm)


# sanity: the construction must be anti-Hermitian and traceless throughout
for b in M_BASIS:
    assert np.max(np.abs(b + b.conj().T)) < 1e-12, "m basis element not anti-Hermitian"
    assert abs(np.trace(b)) < 1e-12, "m basis element not traceless"
print("STEP 0  m basis: 6 anti-Hermitian traceless 3x3 matrices  [OK]")


def make_J(eps: tuple[int, int, int]) -> np.ndarray:
    """Invariant almost-complex structure with sign eps_k on root plane k."""
    J = np.zeros((6, 6))
    for k, e in enumerate(eps):
        J[2 * k, 2 * k + 1] = -e
        J[2 * k + 1, 2 * k] = e
    return J


def nijenhuis_norm(J: np.ndarray) -> float:
    """max |N(X,Y)| over basis pairs, N(X,Y)=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y]."""

    def br(u: np.ndarray, v: np.ndarray) -> np.ndarray:
        A = sum(u[i] * M_BASIS[i] for i in range(6))
        B = sum(v[i] * M_BASIS[i] for i in range(6))
        return to_m_coords(A @ B - B @ A)

    worst = 0.0
    for i, j in itertools.combinations(range(6), 2):
        x = np.zeros(6)
        x[i] = 1
        y = np.zeros(6)
        y[j] = 1
        n = br(J @ x, J @ y) - J @ br(J @ x, y) - J @ br(x, J @ y) - br(x, y)
        worst = max(worst, float(np.max(np.abs(n))))
    return worst


print()
print("=" * 78)
print("STEP 1  Classify all 8 invariant almost-complex structures by Nijenhuis")
print("=" * 78)
integrable, non_integrable = [], []
for eps in itertools.product((1, -1), repeat=3):
    J = make_J(eps)
    assert np.max(np.abs(J @ J + np.eye(6))) < 1e-12, f"J^2 != -1 for eps={eps}"
    n = nijenhuis_norm(J)
    tag = "INTEGRABLE (Kahler)" if n < 1e-10 else "non-integrable (NK candidate)"
    (integrable if n < 1e-10 else non_integrable).append(eps)
    print(f"  eps={eps}  product={np.prod(eps):+d}  max|N| = {n:.3e}   {tag}")

print()
print(f"  integrable     : {len(integrable)} of 8 -> {integrable}")
print(f"  non-integrable : {len(non_integrable)} of 8 -> {non_integrable}")

# ---------------------------------------------------------------------------
# STEP 2 -- pin J_NK. Choice rule stated BEFORE looking at any c.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 2  Pin J_NK (rule fixed before any c exists)")
print("=" * 78)
print("  RULE: J_NK is a non-integrable invariant a.c.s.; among those, take the")
print("  lexicographically first sign tuple. Any other non-integrable choice is")
print("  related to it by a Weyl/conjugation symmetry of the coset, so the rule")
print("  is a labelling convention, not a physical selection -- and it is fixed")
print("  here, with c uncomputed.")
assert non_integrable, "NO non-integrable a.c.s. found -- nearly-Kahler J does not exist here"
EPS_NK = min(non_integrable)
J_NK = make_J(EPS_NK)
print(f"  J_NK sign tuple = {EPS_NK}   (sign product {np.prod(EPS_NK):+d})")

# ---------------------------------------------------------------------------
# STEP 3 -- THE PRE-COMMITTED FAILURE MODE: does J preserve the family?
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 3  Does J_NK map the admissible connection family into itself?")
print("        (pre-committed: if NOT, verdict is BLOCKED-STRUCTURE)")
print("=" * 78)


def rot_block(w: float) -> np.ndarray:
    return np.array([[0.0, -w], [w, 0.0]])


def cartan_gen_on_m(h):
    w = (h[0] - h[1], h[0] - h[2], h[1] - h[2])
    out = np.zeros((6, 6), dtype=complex)
    for k in range(3):
        out[2 * k : 2 * k + 2, 2 * k : 2 * k + 2] = rot_block(w[k])
    return out


t2_gens = [cartan_gen_on_m((1.0, -1.0, 0.0)), cartan_gen_on_m((0.0, 1.0, -1.0))]
family = C73B.equivariant_torsion_basis(t2_gens)
dim_family = family.shape[1]
print(f"  dim of admissible family (Stage 0 regression) = {dim_family}  (expect 6)")
assert dim_family == 6

# A family element is T (a map m -> Lambda^2 m) stored as a flat 6*15 vector.
# Precomposition with J acts on the SOURCE index only: (T o J)(e_i) = T(J e_i).
n_pairs = len(C73B.PAIRS)
J_applied = np.zeros_like(family)
for col in range(dim_family):
    T = family[:, col].reshape(6, n_pairs)  # rows indexed by source e_i
    J_applied[:, col] = (J_NK.T @ T).reshape(-1)

# Is each J-image still inside the family's span?
proj_res = []
for col in range(dim_family):
    v = J_applied[:, col]
    coeffs, *_ = np.linalg.lstsq(family, v, rcond=None)
    proj_res.append(float(np.max(np.abs(family @ coeffs - v))))
worst_res = max(proj_res)
preserved = worst_res < 1e-8
print(f"  worst residual of J-image against family span = {worst_res:.3e}")
print(f"  J_NK PRESERVES the admissible family: {preserved}")

print()
print("=" * 78)
print("STAGE 1a VERDICT")
print("=" * 78)
if preserved:
    print("  J_NK maps the family into itself. The restated prediction")
    print("  c(J.nabla) = +-i c(nabla) is WELL-POSED on this coset, and Stage 1b")
    print("  (invariant-sector dimensions, still before c) may proceed.")
else:
    print("  J_NK does NOT preserve the family -> BLOCKED-STRUCTURE, exactly the")
    print("  failure mode frozen in the pre-registration. Per that commitment this")
    print("  is the FINDING and must NOT be worked around by swapping J or the")
    print("  family. c is not computed.")
print()
print("  c HAS STILL NOT BEEN COMPUTED anywhere in Stage 0 or Stage 1a.")
