r"""
C151 STAGE 0 -- SCOPING ONLY. The connection coefficient c is NOT computed
here, deliberately: the pre-registration's invalidation criterion #4 requires
the admissible family's DIMENSION to be stated BEFORE the predicted quantity
is touched, so that any restatement of the prediction cannot be fitted to an
answer already seen.

WHAT THIS ANSWERS
  For SU(3)/T^2 (the flag manifold F_{1,2,3}, the designated second
  nearly-Kahler test space):
    (a) dim Hom_{T^2}(m, Lambda^2 m)  -- the admissible invariant-connection
        family, i.e. the analogue of the 2-dimensional family C73b certified
        for S^6 = G2/SU(3);
    (b) the T^2-weight structure of m;
    (c) how the isotropy-invariant content differs from the SU(3) case.

WHY IT MATTERS
  On S^6 the isotropy is SU(3) (dim 8) and the family came out 2-dimensional.
  On SU(3)/T^2 the isotropy is T^2 -- 2-dimensional and ABELIAN -- so
  equivariance is a far weaker constraint and the family is expected to be
  larger. If it is, the prediction "c(J.nabla) = i c(nabla), an exact
  90-degree rotation in a 2-dim family" cannot be carried across verbatim:
  its S^6-specific phrasing must be restated in the form that survives any
  even dimension ("c is C-linear w.r.t. J"), and per criterion #4 that
  restatement must be frozen BEFORE c is computed.

METHOD -- deliberately reuses C73b's OWN solver
  equivariant_torsion_basis(m_gens) is called with the T^2 generators instead
  of the su(3) ones. Same code, different input: no new transcription risk,
  and the su(3) case is re-run first as a REGRESSION (must reproduce C73b's
  own certified answer of 2, or this script's plumbing is wrong).

CONSTRUCTION OF THE T^2 ACTION (elementary, stated so it can be checked)
  su(3) = traceless anti-Hermitian 3x3. Cartan = diagonal imaginary traceless.
  m = off-diagonal part, real basis per pair p<q:
        X_pq = E_pq - E_qp,      Y_pq = i(E_pq + E_qp)
  For H = i*diag(h1,h2,h3):  [H, X_pq] = (h_p - h_q) Y_pq
                             [H, Y_pq] = -(h_p - h_q) X_pq
  so ad(H)|m is block-diagonal with three 2x2 blocks [[0,-w],[w,0]],
  w_pq = h_p - h_q -- i.e. m is three 2-real-dimensional T^2-weight planes,
  one per positive root, exactly as root-space theory predicts.

Run:  python c151_stage0_scoping.py
"""

import importlib.util
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

# ---------------------------------------------------------------------------
# REGRESSION FIRST: reproduce C73b's own certified su(3) answer with its own
# solver, so a wrong number below cannot be blamed on plumbing.
# ---------------------------------------------------------------------------
su3_m_gens = C73B.m_generators()
su3_family = C73B.equivariant_torsion_basis(su3_m_gens)
print("REGRESSION (su(3) isotropy, S^6 = G2/SU(3))")
print(f"  n generators fed to solver          : {len(su3_m_gens)}  (expect 8)")
print(f"  dim Hom_su3(m, Lambda^2 m)          : {su3_family.shape[1]}  (C73b certified: 2)")
assert su3_family.shape[1] == 2, "plumbing broken -- su(3) regression does not reproduce 2"
print("  -> solver reproduces C73b exactly. Safe to feed it T^2 generators.")


# ---------------------------------------------------------------------------
# THE T^2 ACTION ON m FOR SU(3)/T^2
# ---------------------------------------------------------------------------
def rot_block(w: float) -> np.ndarray:
    return np.array([[0.0, -w], [w, 0.0]])


def cartan_gen_on_m(h: tuple[float, float, float]) -> np.ndarray:
    """ad(i*diag(h)) restricted to m, in the basis
    (X_12, Y_12, X_13, Y_13, X_23, Y_23)."""
    w12, w13, w23 = h[0] - h[1], h[0] - h[2], h[1] - h[2]
    out = np.zeros((6, 6), dtype=complex)
    out[0:2, 0:2] = rot_block(w12)
    out[2:4, 2:4] = rot_block(w13)
    out[4:6, 4:6] = rot_block(w23)
    return out


H1 = (1.0, -1.0, 0.0)  # i*diag(1,-1,0)
H2 = (0.0, 1.0, -1.0)  # i*diag(0,1,-1)
t2_m_gens = [cartan_gen_on_m(H1), cartan_gen_on_m(H2)]

print()
print("T^2 ACTION ON m  (SU(3)/T^2, the flag manifold F_{1,2,3})")
for lbl, h in (("H1 = i*diag(1,-1,0)", H1), ("H2 = i*diag(0,1,-1)", H2)):
    w = (h[0] - h[1], h[0] - h[2], h[1] - h[2])
    print(f"  {lbl}: weights on (m_12, m_13, m_23) = {w}")
print("  -> m is THREE 2-real-dim weight planes (one per positive root),")
print("     NOT the 3(+)3bar of the SU(3)-isotropy case.")

# sanity: generators must be real antisymmetric (genuine so(6) elements)
for k, g in enumerate(t2_m_gens, 1):
    assert np.max(np.abs(g.imag)) < 1e-12, f"T2 generator {k} not real"
    assert np.max(np.abs(g + g.T)) < 1e-12, f"T2 generator {k} not antisymmetric"
print("  sanity: both T^2 generators are real antisymmetric (valid so(6))  [OK]")

# ---------------------------------------------------------------------------
# (a) THE ADMISSIBLE CONNECTION FAMILY -- the criterion-#4 number
# ---------------------------------------------------------------------------
t2_family = C73B.equivariant_torsion_basis(t2_m_gens)
dim_t2 = t2_family.shape[1]

print()
print("=" * 78)
print("(a) ADMISSIBLE INVARIANT-CONNECTION FAMILY")
print("=" * 78)
print(f"  dim Hom_su3(m, Lambda^2 m)  [S^6, C73b certified]      = {su3_family.shape[1]}")
print(f"  dim Hom_T2 (m, Lambda^2 m)  [SU(3)/T^2, THIS ROUND]    = {dim_t2}")
print(f"  ratio                                                   = {dim_t2 / 2:.1f}x larger")


# ---------------------------------------------------------------------------
# (c) how much bigger is the invariant content generally?
# ---------------------------------------------------------------------------
def commutant_dim(gens: list[np.ndarray], dim: int) -> int:
    ident = np.eye(dim, dtype=complex)
    stacked = np.vstack([np.kron(g.T, ident) - np.kron(ident, g) for g in gens])
    _, sv, _ = np.linalg.svd(stacked)
    padded = np.concatenate([sv, np.zeros(dim * dim - len(sv))])
    return int(np.sum(np.abs(padded) < 1e-8))


print()
print("=" * 78)
print("(c) ISOTROPY-INVARIANT CONTENT, su(3) vs T^2")
print("=" * 78)
print(f"  dim commutant of isotropy on m   -- su(3) : {commutant_dim(su3_m_gens, 6)}")
print(f"  dim commutant of isotropy on m   -- T^2   : {commutant_dim(t2_m_gens, 6)}")
print("  (commutant dim counts inequivalent irreducible constituents;")
print("   a larger number means the isotropy separates m into more pieces)")

print()
print("=" * 78)
print("STAGE 0 VERDICT")
print("=" * 78)
if dim_t2 == 2:
    print("  Family is ALSO 2-dimensional. The S^6 phrasing carries across")
    print("  verbatim and NO restatement is needed under criterion #4.")
else:
    print(f"  Family is {dim_t2}-dimensional, NOT 2. Per the pre-registration's")
    print("  invalidation criterion #4, the prediction's S^6-specific phrasing")
    print("  ('exact 90-degree rotation in a 2-dim family') MUST NOT be carried")
    print("  across verbatim. It must be restated in the form that survives any")
    print("  even dimension -- 'c is C-linear with respect to J' -- and that")
    print("  restatement must be FROZEN BEFORE c is computed.")
    print()
    print("  c was NOT computed in this script. Nothing here can have been")
    print("  fitted to an answer, because no answer exists yet.")
