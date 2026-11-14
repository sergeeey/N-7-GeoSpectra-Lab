r"""
C146 -- WHY does C139's Term1 (Kostant's D_Sigma tensor Id_W part) vanish
identically on the su(3)-invariant sector, while Term2 (E_W, the twist
bundle's own connection) carries the entire physical signal?  C145 found
this is TRUE (symbolically, exactly, skeptic-confirmed). This round asks
whether it is FORCED, by a general Schur's-lemma argument from
already-certified branching data alone -- not a numerical accident
specific to m -- and whether it generalizes.

CLAIM (stated before computing): Sigma_odd = 3 (+) 1, Sigma_even = 1 (+)
  3bar.  EVEN_IDX/ODD_IDX (which COLUMNS are "even"/"odd") ARE certified
  in round59/C139's own code; module TYPE ("3+1", "1+3bar") is certified
  in C139's own Clebsch-Gordan check (Section 4).  The SPECIFIC assignment
  used below -- y1,y2,y3 = the "3", y123 = the "1" -- is standard
  Lagrangian-spinor representation theory (Lambda^1 L' = the fundamental
  3 by construction, Lambda^3 L' = det = the trivial 1 for SU(3)), NOT
  itself pulled from a prior in-repo certificate for this specific
  column-level assignment.  Skeptic-flagged (C146 pass) as a citation
  precision issue, not a mathematical one: Check 2 below verifies the
  matrix CONSEQUENCE directly, so even if this standard-textbook
  assignment were doubted, Check 2's result stands on its own.

D_Sigma (round59's own untwisted operator) is SU(3)-equivariant (it
commutes with the diagonal su(3) action on Sigma -- this is implicit
throughout round59/C139/C141's entire machinery but not, as far as this
project's registry shows, EXPLICITLY verified as a standalone fact
before now). If so, Schur's lemma forces D_Sigma to annihilate
Sigma_odd's "3" piece entirely: a nonzero SU(3)-equivariant map 3 -> Y
requires Y to contain a "3" constituent, and Sigma_even = 1(+)3bar has
none (3 and 3bar are INEQUIVALENT su(3) irreps). So D_Sigma's "3-block"
(Sigma_odd's 3-part -> Sigma_even) must be the zero matrix -- forced,
not fitted.

Any twist bundle W with NO su(3) singlet forces every domain-invariant
vector in (Sigma_odd (x) W)^SU(3) to have ZERO component along
Sigma_odd's OWN "1"-part (that "1" can only pair with a "1" in W to
build an invariant, and W has none) -- so the invariant lives entirely
in the "3"-part of Sigma_odd, where D_Sigma vanishes by the paragraph
above. CONSEQUENCE: Term1 (Kostant, = D_Sigma (x) Id_W restricted to
this sector) is forced to be EXACTLY ZERO for ANY such W, not merely for
W=m specifically -- C139's own finding was an instance of a general fact,
not a numerical coincidence about m.

This script verifies, symbolically:
  (1) D_Sigma commutes with all 8 su(3) generators on Sigma (equivariance)
  (2) D_Sigma's matrix elements from Sigma_odd's "3"-part (y1,y2,y3) into
      Sigma_even are ALL exactly zero (the forced vanishing, directly)
  (3) C139's own domain-invariant vector u_hat has EXACTLY ZERO component
      along Sigma_odd's "1"-part (y123) -- confirming the mechanism that
      forces Term1 to see only the (already-vanishing) "3"-block
  (4) as a cross-check of the OTHER branch of the theorem: for a genuine
      SINGLET twist (W=trivial, zero connection, E_W automatically 0),
      D_Sigma's "1-block" (Sigma_odd's 1-part -> Sigma_even) reproduces
      round59's own certified b-channel value -sqrt(3) exactly -- the
      complementary case, already implicit in C141's own Section 8 direct
      -sum decomposition, re-verified here directly from D_Sigma alone.

Reuses round59_route_a_independent.py's Clifford/Nomizu/ADNU machinery
and C139's own domain-invariant computation, unmodified.

Run:  python c146_schur_forced_vanishing.py
"""

import importlib.util
from pathlib import Path

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


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)
C139 = load_module("c139_twisted_s6_alternate_representation", C139_PATH)

E = R59.build_clifford(conj=False)
NAB = {i: R59.spin_lift(R59.NOMIZU[i], E) for i in range(1, 7)}
RHO_SIGMA = {a: R59.spin_lift(R59.ADNU[a], E) for a in range(1, 9)}  # su(3) on Sigma

calib_ok, _ = R59.run_calibration(E, R59.NOMIZU)
assert calib_ok
print("STEP 0  round59 machinery imported, calibration re-verified  [OK]")

D_SIGMA = sp.simplify(sum((E[i] * NAB[i] for i in range(1, 7)), sp.zeros(8, 8)))

# ---------------------------------------------------------------------------
# CHECK 1 -- is D_Sigma SU(3)-equivariant?  [D_Sigma, rho_Sigma(a)] == 0
# for all a=1..8, NOT assumed anywhere in this project's registry before
# now as an explicit standalone check.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("CHECK 1  D_Sigma SU(3)-equivariance:  [D_Sigma, rho_Sigma(a)] == 0 ?")
print("=" * 78)
equivariant_all = True
for a in range(1, 9):
    comm = sp.simplify(D_SIGMA * RHO_SIGMA[a] - RHO_SIGMA[a] * D_SIGMA)
    ok = comm == sp.zeros(8, 8)
    equivariant_all &= ok
    print(f"  a={a}: [D_Sigma, rho_Sigma({a})] == 0 : {ok}")
print(f"  ALL 8 generators commute with D_Sigma: {equivariant_all}")
assert equivariant_all, "D_Sigma is NOT SU(3)-equivariant -- the whole argument below collapses"

# ---------------------------------------------------------------------------
# CHECK 2 -- the "3-block" of D_Sigma (Sigma_odd's y1,y2,y3 columns, ALL
# 8 rows) is exactly zero -- the forced vanishing, checked directly on
# the matrix, not merely inferred from Check 1 + Schur's lemma (belt and
# braces: Schur's lemma predicts it, this confirms the prediction).
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("CHECK 2  D_Sigma's 'y1,y2,y3 columns' (Sigma_odd's su(3)-3-part) are")
print("         EXACTLY ZERO in every row (forced by Check 1 + branching)")
print("=" * 78)
print("  NOTE (skeptic-flagged precision): rows {0,4,5,6} (Sigma_even) are")
print("  zero because of SCHUR's lemma (no '3' in Sigma_even); rows {1,2,3,7}")
print("  (Sigma_odd) are zero for a SEPARATE, automatic reason -- D_Sigma is")
print("  strictly parity-FLIPPING (Clifford x spin-lift = odd<->even only),")
print("  so odd->odd is zero regardless of any su(3) argument. Both subsets")
print("  are checked together below; only the first 4 rows are the genuinely")
print("  Schur-forced content this round's theorem rests on.")
# BASIS index convention (R59.SUBSETS): 0=(),1=(1,),2=(2,),3=(3,),
# 4=(1,2),5=(1,3),6=(2,3),7=(1,2,3).  Sigma_odd = {1,2,3,7} (ODD_IDX);
# its su(3)-"3" part is span{y1,y2,y3} = columns {1,2,3}; its su(3)-"1"
# part is span{y123} = column 7 (already-certified branching, cited not
# re-derived: EVEN_IDX=1(+)3bar, ODD_IDX=3(+)1).
Y_3PART_COLS = [1, 2, 3]
Y_1PART_COL = 7
three_block_zero = all(
    sp.simplify(D_SIGMA[row, col]) == 0 for row in range(8) for col in Y_3PART_COLS
)
print(f"  D_Sigma[:, {{1,2,3}}] (the y1,y2,y3 columns) all zero: {three_block_zero}")
if not three_block_zero:
    nz = [
        (r, c, sp.simplify(D_SIGMA[r, c]))
        for r in range(8)
        for c in Y_3PART_COLS
        if sp.simplify(D_SIGMA[r, c]) != 0
    ]
    print(f"    nonzero entries found (theorem FALSIFIED): {nz}")

# ---------------------------------------------------------------------------
# CHECK 3 -- C139's own domain-invariant vector (Sigma_odd (x) m)^{SU(3)}
# has EXACTLY ZERO component along Sigma_odd's "1"-part (y123).
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("CHECK 3  C139's own domain invariant has zero y123-component")
print("=" * 78)
E_sym = C139.E_sym
NAB_sym_local = {i: R59.spin_lift(R59.NOMIZU[i], E_sym) for i in range(1, 7)}
su3_ops_sym = C139.su3_ops_sym
rho_m_adnu_sym = {a: C139.rho_vector_sympy(R59.ADNU[a]) for a in range(1, 9)}
gens_leibniz_48_sym = [
    R59.kron(su3_ops_sym[a], sp.eye(6)) + R59.kron(sp.eye(8), rho_m_adnu_sym[a])
    for a in range(1, 9)
]
domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(6)), 6)
domain_inv_sym = C139.common_nullspace_in_block_sym(gens_leibniz_48_sym, domain_block, 48)
print(f"  domain_inv dimension (exact): {len(domain_inv_sym)}  (expect 1)")
assert len(domain_inv_sym) == 1

u_hat = domain_inv_sym[0]
# u_hat is a 48-vector (8*6); extract the block corresponding to Sigma
# index 7 (y123, Sigma_odd's own "1"-part) across all 6 W-components.
IDX_Y123 = 7
y123_block = [u_hat[IDX_Y123 * 6 + w, 0] for w in range(6)]
y123_block_zero = all(sp.simplify(v) == 0 for v in y123_block)
print(f"  u_hat's y123-block (6 components, one per W-index): {y123_block}")
print(f"  ALL exactly zero (confirms the mechanism): {y123_block_zero}")

# ---------------------------------------------------------------------------
# CHECK 4 -- the complementary branch: D_Sigma's "1-block" (Sigma_odd's
# y123 column) reproduces round59's own certified b-channel value
# -sqrt(3) -- the value ANY singlet-twist channel inherits directly.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("CHECK 4  D_Sigma's y123-column reproduces round59's own b=-sqrt(3)")
print("=" * 78)
# round59's own b-channel: <w=1(x)1 (Sigma_even's own '1'-part, index 0),
# D_Sigma . y123> -- i.e. D_SIGMA[0, 7].
b_channel = sp.simplify(D_SIGMA[0, Y_1PART_COL])
print(f"  D_Sigma[row=0 ('1' in Sigma_even), col=7 (y123)] = {b_channel}")
matches_round59_b = sp.simplify(b_channel + sp.sqrt(3)) == 0
print(f"  matches round59's own certified b=-sqrt(3): {matches_round59_b}")

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
all_ok = equivariant_all and three_block_zero and y123_block_zero and matches_round59_b
print(f"  D_Sigma SU(3)-equivariant                         : {equivariant_all}")
print(f"  D_Sigma's Sigma_odd-3-block -> Sigma_even is zero  : {three_block_zero}")
print(f"  C139's domain invariant avoids Sigma_odd's 1-part  : {y123_block_zero}")
print(f"  D_Sigma's Sigma_odd-1-block matches round59's b    : {matches_round59_b}")
print(f"  ALL FOUR (the theorem, fully verified)             : {all_ok}")
