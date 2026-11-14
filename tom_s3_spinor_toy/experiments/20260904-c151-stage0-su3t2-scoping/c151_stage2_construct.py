r"""
C151 STAGE 2a -- CONSTRUCTION ONLY, with a hard calibration gate.
Builds the SU(3)/T^2 geometry and verifies it against an INDEPENDENT
criterion (the Killing-spinor equation) BEFORE any coefficient is extracted.
c is still NOT computed in this file.

WHY A SEPARATE CONSTRUCTION FILE
  round59's own discipline: its Route-C script calibrates the Nomizu
  operators against AHL2023 Theorem 5.1 and REFUSES to proceed if that gate
  fails ("This gate CAN fail; it pins the spin-connection independently").
  The same discipline is applied here. If SU(3)/T^2's construction does not
  reproduce a genuine Killing spinor, the geometry is wrong and no
  coefficient computed from it would mean anything.

DESIGN DECISIONS, fixed here and stated so they can be checked
  * METRIC. CH2016 (round65's own source) normalises the nearly-Kahler metric
    on all four homogeneous NK 6-manifolds from B(X,Y) = -(1/12)Tr(ad X ad Y).
    For su(3), Tr(ad X ad Y) = 6 Tr(XY), so B(X,Y) = -(1/2)Tr(XY).
    The basis X_pq = E_pq - E_qp, Y_pq = i(E_pq + E_qp) is then ORTHONORMAL
    -- verified below, not assumed.
  * CONNECTION. For a naturally reductive homogeneous space the Levi-Civita
    Nomizu map is Lambda(X)Y = (1/2)[X,Y]_m. This is the same relation whose
    S^6 instance carried the 1/(2 sqrt3) prefactor (the 1/2 from this formula,
    the 1/sqrt3 from that metric's radius).
  * J-ALIGNMENT. round59's Clifford construction carries the STANDARD complex
    structure J_0 on each index pair (e_{2j-1}, e_{2j}), whereas Stage 1a
    pinned J_NK = eps with eps = (-1,1,-1). Swapping X<->Y inside a plane
    flips J_0 -> -J_0 there, so reordering the basis by eps turns J_NK into
    the standard J_0 and lets round59's build_clifford/spin_lift be reused
    UNMODIFIED. No new Clifford code is written.

THE GATE
  With the invariant spinors of Sigma (Stage 1b predicted exactly 2), the
  untwisted Dirac operator must act as D psi = mu psi with mu real and
  nonzero, and the two invariant spinors must carry opposite eigenvalues --
  the structural signature CH2016 Sec.2 proves for ANY homogeneous NK
  6-manifold (psi and Vol_g.psi are Killing with eigenvalues +-lambda).
  If that fails, this script raises and Stage 2b is not reached.

Run:  python c151_stage2_construct.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
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


R59 = load_module("round59_route_a_independent", R59_PATH)
C73B = load_module("c73b_torsion_family", C73B_PATH)

EPS_NK = (-1, 1, -1)  # pinned in Stage 1a by the Nijenhuis computation
PAIRS_M = [(0, 1), (0, 2), (1, 2)]  # root planes m_12, m_13, m_23


# ---------------------------------------------------------------------------
# 1. m basis, J-ALIGNED so that J_NK becomes the standard J_0 on each pair
# ---------------------------------------------------------------------------
def raw_plane(p: int, q: int) -> tuple[np.ndarray, np.ndarray]:
    X = np.zeros((3, 3), dtype=complex)
    X[p, q], X[q, p] = 1, -1
    Y = np.zeros((3, 3), dtype=complex)
    Y[p, q], Y[q, p] = 1j, 1j
    return X, Y


M_BASIS: list[np.ndarray] = []
for k, (p, q) in enumerate(PAIRS_M):
    X, Y = raw_plane(p, q)
    # eps=+1 -> (X,Y) keeps J_0 ; eps=-1 -> (Y,X) flips it, so J_NK becomes J_0
    M_BASIS.extend([X, Y] if EPS_NK[k] > 0 else [Y, X])

print("STEP 1  J-aligned m basis built (X<->Y swapped on planes with eps=-1)")
print(f"        EPS_NK = {EPS_NK}  ->  J_NK is the STANDARD J_0 in this basis")


def killing_B(A: np.ndarray, Bm: np.ndarray) -> complex:
    """CH2016's B(X,Y) = -(1/12)Tr(ad X ad Y) = -(1/2)Tr(XY) for su(3)."""
    return -0.5 * np.trace(A @ Bm)


gram = np.array([[killing_B(a, b) for b in M_BASIS] for a in M_BASIS])
orthonormal = np.max(np.abs(gram - np.eye(6))) < 1e-12
print(
    f"STEP 1  basis is B-ORTHONORMAL: {orthonormal}   max|Gram - I| = "
    f"{np.max(np.abs(gram - np.eye(6))):.3e}"
)
assert orthonormal, "basis not orthonormal under CH2016's B -- metric convention wrong"


def to_m(mat: np.ndarray) -> np.ndarray:
    """Coordinates of the m-part of a 3x3 anti-Hermitian matrix, in M_BASIS."""
    return np.array([killing_B(mat, b).real for b in M_BASIS])


# ---------------------------------------------------------------------------
# 2. Levi-Civita Nomizu operators  Lambda(e_i) = (1/2) ad(e_i)|_m
# ---------------------------------------------------------------------------
NOMIZU_LC: dict[int, np.ndarray] = {}
for i in range(6):
    L = np.zeros((6, 6))
    for j in range(6):
        comm = M_BASIS[i] @ M_BASIS[j] - M_BASIS[j] @ M_BASIS[i]
        L[:, j] = 0.5 * to_m(comm)
    NOMIZU_LC[i + 1] = L

antisym = max(float(np.max(np.abs(NOMIZU_LC[i] + NOMIZU_LC[i].T))) for i in range(1, 7))
print(f"STEP 2  Nomizu Lambda(e_i) = (1/2)[e_i,.]_m built; max|L + L^T| = {antisym:.3e}")
assert antisym < 1e-12, "Nomizu operators not antisymmetric -- not metric connections"

# ---------------------------------------------------------------------------
# 3. Clifford + spin lift, REUSED from round59 unmodified
# ---------------------------------------------------------------------------
E_sym = R59.build_clifford(conj=False)
E = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
for i in range(1, 7):
    assert np.max(np.abs(E[i] @ E[i] + np.eye(8))) < 1e-12, "Clifford convention broken"
print("STEP 3  round59's Clifford algebra reused unmodified (e_i^2 = -1 verified)")


def spin_lift_np(L: np.ndarray) -> np.ndarray:
    """(1/2) sum_{a<b} L_ab e_a e_b -- round59's own lift, numpy form."""
    out = np.zeros((8, 8), dtype=complex)
    for a in range(6):
        for b in range(a + 1, 6):
            if abs(L[a, b]) > 1e-14:
                out += L[a, b] * 0.5 * (E[a + 1] @ E[b + 1])
    return out


NAB = {i: spin_lift_np(NOMIZU_LC[i]) for i in range(1, 7)}
D_SIGMA = sum((E[i] @ NAB[i] for i in range(1, 7)), np.zeros((8, 8), dtype=complex))

# ---------------------------------------------------------------------------
# 4. THE CALIBRATION GATE -- independent of anything this test wants to find
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 4  CALIBRATION GATE (this gate CAN fail; it pins the geometry)")
print("=" * 78)


# T^2 action on Sigma, to locate the invariant spinors
def cartan_on_m(h) -> np.ndarray:
    """ad(i*diag(h))|m in the J-ALIGNED basis (weights follow the same swap)."""
    A = 1j * np.diag(h).astype(complex)
    out = np.zeros((6, 6))
    for j in range(6):
        comm = A @ M_BASIS[j] - M_BASIS[j] @ A
        out[:, j] = to_m(comm)
    return out


T2_M = [cartan_on_m((1.0, -1.0, 0.0)), cartan_on_m((0.0, 1.0, -1.0))]
RHO_SIGMA = [spin_lift_np(g) for g in T2_M]

stacked = np.vstack(RHO_SIGMA)
_, sv, vh = np.linalg.svd(stacked)
padded = np.concatenate([sv, np.zeros(8 - len(sv))])
inv_sigma = vh.conj().T[:, np.abs(padded) < 1e-8]
n_inv = inv_sigma.shape[1]
print(f"  T^2-invariant spinors in Sigma : {n_inv}   (Stage 1b predicted 2)")
assert n_inv == 2, f"expected 2 invariant spinors, got {n_inv} -- construction inconsistent"

block = inv_sigma.conj().T @ D_SIGMA @ inv_sigma
eigs = np.linalg.eigvals(block)
print(f"  D_Sigma on the invariant 2-plane, eigenvalues: {np.round(eigs, 8)}")
nonzero = np.all(np.abs(eigs) > 1e-8)
opposite = abs(eigs[0] + eigs[1]) < 1e-8
print(f"  both eigenvalues nonzero        : {nonzero}")
print(
    f"  eigenvalues equal and opposite  : {opposite}   (CH2016 Sec.2: psi, Vol.psi carry +-lambda)"
)
assert nonzero and opposite, "CALIBRATION FAILED -- geometry does not carry a Killing spinor pair"
mu = float(np.real(eigs[np.argmax(np.real(eigs))]))
print(f"  => CALIBRATION PASSED. |D-eigenvalue| on invariant spinors = {mu:.8f}")
print(f"     (S^6's own certified value under its normalisation was sqrt(3) = {np.sqrt(3):.8f})")

# ---------------------------------------------------------------------------
# 5. Twist W = m, and the invariant sectors -- cross-check against Stage 1b
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 5  Invariant sectors of Sigma (x) W  -- cross-check of Stage 1b")
print("=" * 78)
I6, I8 = np.eye(6), np.eye(8)
gens48 = [np.kron(RHO_SIGMA[k], I6) + np.kron(I8, T2_M[k]) for k in range(2)]

EVEN, ODD = R59.EVEN_IDX, R59.ODD_IDX


def sector_basis(first_idx) -> np.ndarray:
    block_idx = [i * 6 + j for i in first_idx for j in range(6)]
    proj = np.zeros((48, len(block_idx)))
    for col, g in enumerate(block_idx):
        proj[g, col] = 1
    st = np.vstack([proj.T @ g @ proj for g in gens48])
    _, s, vt = np.linalg.svd(st)
    pad = np.concatenate([s, np.zeros(len(block_idx) - len(s))])
    return proj @ vt.conj().T[:, np.abs(pad) < 1e-8]


dom = sector_basis(ODD)
tgt = sector_basis(EVEN)
print(f"  domain dim (Sigma_odd  (x) W)^T2 = {dom.shape[1]}   (Stage 1b predicted 3)")
print(f"  target dim (Sigma_even (x) W)^T2 = {tgt.shape[1]}   (Stage 1b predicted 3)")
match = dom.shape[1] == 3 and tgt.shape[1] == 3
print(f"  MATCHES Stage 1b's weight-arithmetic prediction: {match}")

print()
print("=" * 78)
print("STAGE 2a VERDICT")
print("=" * 78)
print(f"  metric/basis orthonormal under CH2016's B   : {orthonormal}")
print(f"  Nomizu operators are metric connections     : {antisym < 1e-12}")
print(f"  Killing-spinor calibration gate             : PASSED (|mu| = {mu:.6f})")
print(f"  sector dims reproduce Stage 1b's prediction : {match}")
print()
print("  Geometry is built and independently calibrated. c is STILL NOT")
print("  COMPUTED -- extracting it is Stage 2b, a separate file.")
