r"""
C147b -- closes BOTH skeptic caveats on C147, by upgrading the decisive
ratio from float64 to EXACT sympy AND identifying the complex structure
that makes the map C-linear, instead of merely observing a numerical
similarity in whatever basis an SVD happened to return.

SKEPTIC CAVEAT 1 (basis-dependence): C147 observed "c2 = i*c1, condition
number exactly 1" in C73b's SVD-produced basis.  That property is
invariant under SO(2) rotations of the basis but NOT under a general
GL(2,R) change -- so as stated it was a numerical observation about one
particular basis, with the representation-theoretic REASON ("m = 3+3bar
gives Hom_su3(m,Lambda^2 m) a natural complex structure") named as
plausible but unverified.

SKEPTIC CAVEAT 2 (numerical vs exact): C147 used float64 throughout while
sympy machinery was available (C139 uses it for the single NOMIZU point,
getting c_exact = -2*sqrt(3)/3 exactly).

THIS SCRIPT'S FIX -- one construction closes both:
  Take the nearly-Kahler almost-complex structure J on m, which is FIXED
  by AHL2023's own eq.(5) pairing convention (e_{2j-1}, e_{2j}) and is
  therefore exactly known, NOT fitted:
        J e_1 = e_2,  J e_2 = -e_1,   J e_3 = e_4,  J e_4 = -e_3,
        J e_5 = e_6,  J e_6 = -e_5.
  Define a SECOND connection by precomposition with J:
        T_B(e_i) := Lambda_NOMIZU(J e_i)
  i.e. simply a permutation-with-signs of NOMIZU's own already-exact data
  -- so T_B is exactly known too, with no numerics anywhere.

  Then verify, EXACTLY:
    (1) T_B lies in C73b's certified admissible family (numerically to
        machine precision against its basis -- the family itself is only
        available numerically, so this one bridge stays numerical and is
        labelled as such);
    (2) T_B is R-independent of NOMIZU;
    (3) c(T_B) / c(NOMIZU) = +-i  EXACTLY, in sympy, closing caveat 2;
    (4) hence the R-linear map is an EXACT similarity, and the complex
        structure making c "C-linear" is explicitly the nearly-Kahler J
        -- not an artifact of the SVD basis, closing caveat 1.

Run:  python c147b_exact_and_complex_structure.py
"""

import importlib.util
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
C139_PATH = (
    HERE.parent
    / "20260904-c139-twisted-s6-alternate-representation-negative-control"
    / "c139_twisted_s6_alternate_representation.py"
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
C139 = load_module("c139_twisted_s6_alternate_representation", C139_PATH)
C73B = load_module("c73b_torsion_family", C73B_PATH)

E_sym = C139.E_sym

# ---------------------------------------------------------------------------
# STEP 1 -- the nearly-Kahler J on m, fixed by AHL2023's own eq.(5) pairing.
# T_B := NOMIZU o J  is then a permutation-with-signs of NOMIZU's OWN exact
# bivector data -- exactly known, nothing fitted.
# ---------------------------------------------------------------------------
J_ON_INDEX = {1: (2, +1), 2: (1, -1), 3: (4, +1), 4: (3, -1), 5: (6, +1), 6: (5, -1)}

NOMIZU_A = dict(R59.NOMIZU)  # exact sympy bivector-term lists
NOMIZU_B = {}
for i in range(1, 7):
    src, sgn = J_ON_INDEX[i]
    NOMIZU_B[i] = [(sgn * cf, aa, bb) for (cf, aa, bb) in NOMIZU_A[src]]

print("STEP 1  T_B := NOMIZU o J built from NOMIZU's own exact data")
print(f"        J index action: {J_ON_INDEX}")

# ---------------------------------------------------------------------------
# STEP 2 -- is T_B in C73b's certified admissible family?  (This bridge is
# numerical because the family's own basis is only available numerically.)
# ---------------------------------------------------------------------------
m_gens = C73B.m_generators()
torsion_basis = C73B.equivariant_torsion_basis(m_gens)
vec_B = C73B.nomizu_to_vec(NOMIZU_B)
coeffs_B, *_ = np.linalg.lstsq(torsion_basis, vec_B, rcond=None)
resid_B = float(np.max(np.abs(torsion_basis @ coeffs_B - vec_B)))
vec_A = C73B.nomizu_to_vec(NOMIZU_A)
coeffs_A, *_ = np.linalg.lstsq(torsion_basis, vec_A, rcond=None)
resid_A = float(np.max(np.abs(torsion_basis @ coeffs_A - vec_A)))

print()
print("STEP 2  membership in C73b's admissible family [NUMERICAL bridge]")
print(f"        NOMIZU  reconstruction residual = {resid_A:.3e}")
print(f"        T_B     reconstruction residual = {resid_B:.3e}")
in_family = resid_B < 1e-8
print(f"        T_B IS in the admissible family: {in_family}")

# R-independence of the two connections, in the family's own coordinates
M_coords = np.array([[coeffs_A[0].real, coeffs_B[0].real], [coeffs_A[1].real, coeffs_B[1].real]])
det_coords = float(np.linalg.det(M_coords))
print(f"        coords(NOMIZU) = ({coeffs_A[0].real:.6f}, {coeffs_A[1].real:.6f})")
print(f"        coords(T_B)    = ({coeffs_B[0].real:.6f}, {coeffs_B[1].real:.6f})")
print(f"        det of the two coordinate vectors = {det_coords:.6f}  (nonzero => independent)")
independent = abs(det_coords) > 1e-8

# ---------------------------------------------------------------------------
# STEP 3 -- EXACT c at both connections (sympy, no floats), reusing C139's
# own exact machinery unmodified.
# ---------------------------------------------------------------------------
su3_ops_sym = C139.su3_ops_sym
rho_m_adnu_sym = {a: C139.rho_vector_sympy(R59.ADNU[a]) for a in range(1, 9)}
gens_leibniz_48_sym = [
    R59.kron(su3_ops_sym[a], sp.eye(6)) + R59.kron(sp.eye(8), rho_m_adnu_sym[a])
    for a in range(1, 9)
]
domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(6)), 6)
target_block = C139.block_global_gen(R59.EVEN_IDX, list(range(6)), 6)
domain_inv_sym = C139.common_nullspace_in_block_sym(gens_leibniz_48_sym, domain_block, 48)
target_inv_sym = C139.common_nullspace_in_block_sym(gens_leibniz_48_sym, target_block, 48)
assert len(domain_inv_sym) == 1 and len(target_inv_sym) == 1
u_hat = R59.gram_schmidt(domain_inv_sym)[0]
w_hat = R59.gram_schmidt(target_inv_sym)[0]


def c_exact_for(nomizu_dict):
    nab_sym = {i: R59.spin_lift(nomizu_dict[i], E_sym) for i in range(1, 7)}
    rho_m_sym = {i: C139.rho_vector_sympy(nomizu_dict[i]) for i in range(1, 7)}
    d_sym = C139.build_twisted_dirac_sympy(E_sym, nab_sym, 6, rho_m_sym)
    return sp.simplify(R59.hip(w_hat, d_sym * u_hat))


c_A = c_exact_for(NOMIZU_A)
c_B = c_exact_for(NOMIZU_B)
print()
print("STEP 3  EXACT c at both connections (sympy)")
print(f"        c(NOMIZU) = {sp.nsimplify(sp.radsimp(c_A))}")
print(f"        c(T_B)    = {sp.nsimplify(sp.radsimp(c_B))}")

matches_c139 = sp.simplify(sp.Abs(c_A) - 2 * sp.sqrt(3) / 3) == 0
print(f"        |c(NOMIZU)| == 2*sqrt(3)/3 (C139's own registered value): {matches_c139}")

# ---------------------------------------------------------------------------
# STEP 4 -- the decisive EXACT ratio.
# ---------------------------------------------------------------------------
ratio = sp.simplify(c_B / c_A) if sp.simplify(c_A) != 0 else None
print()
print("=" * 78)
print("STEP 4  EXACT ratio c(T_B)/c(NOMIZU)  -- the caveat-closing quantity")
print("=" * 78)
print(f"        c(T_B)/c(NOMIZU) = {sp.nsimplify(sp.radsimp(ratio))}")
is_pure_imag = sp.simplify(sp.re(ratio)) == 0 and sp.simplify(sp.Abs(ratio) - 1) == 0
print(f"        Re(ratio) == 0 exactly : {sp.simplify(sp.re(ratio)) == 0}")
print(f"        |ratio|   == 1 exactly : {sp.simplify(sp.Abs(ratio) - 1) == 0}")
print(f"        ratio == +-i EXACTLY (sympy, not float64): {is_pure_imag}")

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print(f"  T_B = NOMIZU o J is in the admissible family [numerical bridge] : {in_family}")
print(f"  T_B is R-independent of NOMIZU                                 : {independent}")
print(f"  |c(NOMIZU)| reproduces C139's own exact 2*sqrt(3)/3            : {matches_c139}")
print(f"  c(T_B)/c(NOMIZU) = +-i EXACTLY (closes the float64 caveat)     : {is_pure_imag}")
print()
if is_pure_imag and in_family and independent:
    print("  => the R-linear map is an EXACT similarity, and the complex structure")
    print("     making c 'C-linear' is explicitly the NEARLY-KAHLER J of AHL2023's")
    print("     own eq.(5) convention -- NOT an artifact of the SVD basis. Both")
    print("     skeptic caveats on C147 are closed: the property is now exact AND")
    print("     attached to a named geometric structure, not a numerical accident.")
else:
    print("  => at least one leg failed; C147's Claim 3 stays a numerical,")
    print("     basis-dependent observation and must be worded as such.")
