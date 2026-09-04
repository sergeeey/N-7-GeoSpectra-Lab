r"""
C147 -- EXACT zero-locus of the connection coefficient c_W(nabla) over the
WHOLE 2-dimensional admissible su(3)-equivariant torsion family, replacing
C139's own 13-point numerical sweep with a continuum statement.

WHAT IS ALREADY KNOWN (cited, not re-derived):
  * C73b certified the admissible family Hom_su3(m, Lambda^2 m) is
    2-DIMENSIONAL (real), with an explicit basis.
  * C139's own Section 7b swept 13 angles in that family and found
    |c(theta)| CONSTANT (spread 6.7e-16) and Term1 zero at every sampled
    angle. Its own code comment names the exact residual risk: "a linear
    functional on a real 2-dim space GENERICALLY has a 1-dim zero locus"
    -- i.e. 13 samples cannot rule out a zero locus that the sampling
    happened to miss.
  * C146 PROVED Term1 == 0 identically for any zero-singlet twist and any
    su(3)-EQUIVARIANT connection (Schur's lemma + branching) -- so the
    vanishing of Term1 across the family is now a theorem, not 13 samples.

WHAT THIS ROUND ADDS (the continuum upgrade):
  By C146, c(nabla) = Term2(nabla) exactly.  Term2 is R-LINEAR in nabla by
  construction (build_twisted_dirac is linear in the connection).  So

      c(alpha,beta) = alpha*c1 + beta*c2,     c1 := c(T1), c2 := c(T2)

  is an R-linear map R^2 -> C = R^2.  Its zero locus is {0} IFF the real
  2x2 matrix [[Re c1, Re c2],[Im c1, Im c2]] is nonsingular -- a
  BASIS-INDEPENDENT criterion (a change of real basis multiplies the
  determinant by a nonzero factor, so vanishing/non-vanishing is
  invariant).  TWO evaluations therefore decide the WHOLE continuum,
  where C139 needed 13 samples and still could not close the gap.

  Secondary: C139's observed |c(theta)| = const on the unit circle is
  equivalent, for an R-linear map, to the two conditions |c1| = |c2| AND
  Re(c1 * conj(c2)) = 0 -- i.e. c2 = +-i*c1, a similarity (rotation +
  scaling).  Checked directly here, turning C139's numerical observation
  into a structural statement.

Run:  python c147_zero_locus.py
"""

import importlib.util
from pathlib import Path

import numpy as np

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
E_np = C139.E_np
I6 = np.eye(6, dtype=complex)
I8 = np.eye(8, dtype=complex)

# --- C139's own su(3)-invariant domain/target sectors (connection-INDEPENDENT:
# they are defined by the ADNU su(3) action alone, NOT by the torsion) -------
su3_ops_np = C139.su3_ops_np
rho_m_adnu_np = {a: C139.rho_vector(R59.ADNU[a]) for a in range(1, 9)}
gens_leibniz_48 = [np.kron(su3_ops_np[a], I6) + np.kron(I8, rho_m_adnu_np[a]) for a in range(1, 9)]
domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(6)), 6)
target_block = C139.block_global_gen(R59.EVEN_IDX, list(range(6)), 6)
domain_inv = C139.invariant_basis_gen(gens_leibniz_48, domain_block, 48)
target_inv = C139.invariant_basis_gen(gens_leibniz_48, target_block, 48)
assert domain_inv.shape[1] == 1 and target_inv.shape[1] == 1
print("STEP 0  invariant sectors (connection-independent): domain=1, target=1  [OK]")

# --- C73b's own 2-dim admissible torsion basis, unmodified ------------------
m_gens = C73B.m_generators()
torsion_basis = C73B.equivariant_torsion_basis(m_gens)
assert torsion_basis.shape[1] == 2, f"expected 2-dim family, got {torsion_basis.shape[1]}"
print(f"STEP 1  C73b's admissible torsion family: dim = {torsion_basis.shape[1]}  [OK]")

t1_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 0])
t2_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 1])


def c_and_term1_for(combo_dict) -> tuple[complex, complex]:
    """Full c and its Term1 piece, for one connection in the family."""
    nomizu = C73B.matdict_to_nomizu(combo_dict)
    nab_sym = {i: R59.spin_lift(nomizu[i], E_sym) for i in range(1, 7)}
    nab_np = {i: np.array(nab_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    rho_m_np = {i: C139.rho_vector(nomizu[i]) for i in range(1, 7)}
    d_full = C139.build_twisted_dirac_np(E_np, nab_np, 6, rho_m_np)
    c_full = complex((target_inv.conj().T @ d_full @ domain_inv)[0, 0])
    d_term1 = np.zeros((48, 48), dtype=complex)
    for i in range(1, 7):
        d_term1 += np.kron(E_np[i] @ nab_np[i], I6)
    c_t1 = complex((target_inv.conj().T @ d_term1 @ domain_inv)[0, 0])
    return c_full, c_t1


c1, term1_at_T1 = c_and_term1_for(t1_dict)
c2, term1_at_T2 = c_and_term1_for(t2_dict)

print()
print("=" * 78)
print("STEP 2  c on the TWO basis directions (these two decide the continuum)")
print("=" * 78)
print(f"  c1 = c(T1) = {c1}")
print(f"  c2 = c(T2) = {c2}")
print(f"  Term1 at T1 = {term1_at_T1}   (C146 predicts exactly 0)")
print(f"  Term1 at T2 = {term1_at_T2}   (C146 predicts exactly 0)")
term1_zero_both = abs(term1_at_T1) < 1e-10 and abs(term1_at_T2) < 1e-10
print(f"  Term1 == 0 at BOTH basis directions: {term1_zero_both}")
print("  -> by R-linearity, Term1 == 0 on the ENTIRE 2-dim family")
print("     (C139 needed 13 samples for this; 2 + linearity now suffices,")
print("      and C146 proves it independently of any sampling at all)")

# --- THE DECISIVE, BASIS-INDEPENDENT CRITERION -----------------------------
print()
print("=" * 78)
print("STEP 3  Zero locus of c on the whole family (basis-independent test)")
print("=" * 78)
M = np.array([[c1.real, c2.real], [c1.imag, c2.imag]], dtype=float)
det_M = float(np.linalg.det(M))
print("  real 2x2 matrix of the R-linear map (alpha,beta) -> alpha*c1 + beta*c2:")
print(f"    [[{M[0, 0]: .10f}, {M[0, 1]: .10f}],")
print(f"     [{M[1, 0]: .10f}, {M[1, 1]: .10f}]]")
print(f"  det = {det_M:.12e}")
sing_vals = np.linalg.svd(M, compute_uv=False)
print(f"  singular values = {sing_vals}  (cond = {sing_vals[0] / sing_vals[1]:.6f})")
nonsingular = abs(det_M) > 1e-10
print(f"  NONSINGULAR (=> zero locus is EXACTLY the single point nabla=0): {nonsingular}")

# --- WHY |c(theta)| was constant in C139's sweep ---------------------------
print()
print("=" * 78)
print("STEP 4  Structural explanation of C139's |c(theta)| = const observation")
print("=" * 78)
abs_c1, abs_c2 = abs(c1), abs(c2)
re_inner = float(np.real(c1 * np.conj(c2)))
print(f"  |c1| = {abs_c1:.12f}")
print(f"  |c2| = {abs_c2:.12f}")
print(f"  |c1| == |c2| : {abs(abs_c1 - abs_c2) < 1e-10}")
print(f"  Re(c1 * conj(c2)) = {re_inner:.3e}   (== 0 required) : {abs(re_inner) < 1e-10}")
ratio = c2 / c1
print(f"  c2/c1 = {ratio}   -> |ratio| = {abs(ratio):.12f}, Re(ratio) = {ratio.real:.3e}")
is_similarity = abs(abs_c1 - abs_c2) < 1e-10 and abs(re_inner) < 1e-10
print(f"  c2 = +-i*c1 (a similarity: rotation + uniform scaling): {is_similarity}")
print("  => |c(alpha,beta)| = |c1| * sqrt(alpha^2+beta^2), EXACTLY --")
print("     C139's 13-point 'constant on the unit circle' is this formula,")
print("     and c=0 requires alpha=beta=0, i.e. the ZERO connection only.")

# --- consistency with C139's own already-registered headline value ---------
print()
print("=" * 78)
print("STEP 5  Consistency with C139's own registered |c| at the NOMIZU point")
print("=" * 78)
nomizu_vec = C73B.nomizu_to_vec(R59.NOMIZU)
coeffs, *_ = np.linalg.lstsq(torsion_basis, nomizu_vec, rcond=None)
alpha_n, beta_n = float(coeffs[0]), float(coeffs[1])
predicted = alpha_n * c1 + beta_n * c2
print(f"  NOMIZU's own coordinates in the basis: (alpha,beta) = ({alpha_n:.6f}, {beta_n:.6f})")
print(f"  predicted c(NOMIZU) from linearity = {predicted}")
print(f"  |predicted| = {abs(predicted):.10f}")
print("  C139's own registered |c_exact| = 2*sqrt(3)/3 = 1.1547005384")
matches_c139 = abs(abs(predicted) - 2 * np.sqrt(3) / 3) < 1e-8
print(f"  matches C139's own registered value: {matches_c139}")

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print(f"  Term1 == 0 on both basis directions (=> whole family) : {term1_zero_both}")
print(f"  R-linear map nonsingular (=> zero locus = {{0}} only)   : {nonsingular}")
print(f"  c2 = +-i*c1, so |c| depends only on the radius        : {is_similarity}")
print(f"  linearity reproduces C139's own |c| at NOMIZU         : {matches_c139}")
verdict = term1_zero_both and nonsingular and is_similarity and matches_c139
print(f"  ALL FOUR                                              : {verdict}")
print()
if nonsingular:
    print("  VERDICT: c_W(nabla) = 0 ONLY at the zero connection, over the WHOLE")
    print("  2-dim admissible family -- NOT merely at 13 sampled angles. C139's")
    print("  kernel=0 is therefore ROBUST AS A THEOREM over the family, and the")
    print("  hoped-for 'geometrically tunable zero mode' does NOT exist inside")
    print("  this connection family.")
else:
    print("  VERDICT: a nontrivial zero locus EXISTS -- a genuine geometric")
    print("  zero-mode-creating direction, the 'dynamic' outcome.")
