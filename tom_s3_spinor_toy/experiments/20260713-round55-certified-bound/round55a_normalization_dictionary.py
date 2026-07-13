"""Round 55a (2026-07-13): narrow normalization-consistency audit, per
user's own 4-point scope (NOT the full mu_sigma program -- that is
explicitly deferred to a later round pending this one passing):
  1. Build a normalization dictionary (native vs Bourbaki units).
  2. Check a second representative (rho=14, adjoint) for the SAME
     native-vs-Bourbaki rescale factor found at rho=7.
  3. Cite (not re-derive) the full-operator reconstruction at one known
     point -- Round 22's own STEP 2 already proved this exactly.
  4. Confirm all downstream pieces (K_cert, D64^2) live in a consistent,
     correctly-tracked unit system.

Direct response to a reviewer's critique of Round 55: K_cert=2*sqrt(6)/3
is a genuine, standalone result (confirmed here, unchanged), but its
substitution into "C2(rho)-3-K*sqrt(C2(rho))" needed independent
verification that native and Bourbaki units are consistently tracked.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
G2SU3_DIR = HERE.parent / "20260708-dolan-casimir-g2su3"
sys.path.insert(0, str(G2SU3_DIR))

from g2su3_equivariance_check import build_D_matrix64  # noqa: E402
from g2su3_v14_adjoint_full_matrix import ad_gen_raw, verify_full_adjoint_self_consistent  # noqa: E402
from g2su3_v7_multiplicity_dirac import rho7_ep, rho7_nuk  # noqa: E402


def main() -> None:
    print("=" * 70)
    print("ITEM 1+4: normalization dictionary, rho=7 (recap from Round 55)")
    print("=" * 70)
    gens7 = [rho7_ep(p) for p in range(1, 7)] + [rho7_nuk(k) for k in range(1, 9)]
    M7 = sp.zeros(7, 7)
    for g in gens7:
        M7 += g * g
    M7 = sp.simplify(-M7)
    assert M7 == M7[0, 0] * sp.eye(7), "rho=7 naive Casimir not scalar -- STOP"
    native_c2_7 = M7[0, 0]
    bourbaki_c2_7 = sp.Integer(4)
    ratio_7 = bourbaki_c2_7 / native_c2_7
    print(
        f"  rho=7:  native C2 = {native_c2_7},  Bourbaki C2 = {bourbaki_c2_7},  ratio = {ratio_7}"
    )

    print()
    print("=" * 70)
    print("ITEM 2: SECOND REPRESENTATIVE -- rho=14 (adjoint), independent check")
    print("=" * 70)
    AD_RAW = {a: ad_gen_raw(a) for a in range(1, 15)}
    self_consistent = verify_full_adjoint_self_consistent(AD_RAW)
    print(f"  rho=14 representation self-consistency (structure constants): {self_consistent}")
    assert self_consistent, "rho=14 representation is not self-consistent -- STOP"

    M14 = sp.zeros(14, 14)
    for a in range(1, 15):
        M14 += AD_RAW[a] * AD_RAW[a]
    M14 = sp.simplify(-M14)
    is_scalar_14 = M14 == M14[0, 0] * sp.eye(14)
    print(f"  rho=14: -Sum_a ad(E_a)^2 scalar? {is_scalar_14}")
    assert is_scalar_14, "rho=14 naive Casimir not scalar -- STOP"
    native_c2_14 = M14[0, 0]
    bourbaki_c2_14 = sp.Integer(8)  # C_2(G2;(0,1))=8, established (kp_zero_mode.py, preprint.tex)
    ratio_14 = bourbaki_c2_14 / native_c2_14
    print(
        f"  rho=14: native C2 = {native_c2_14},  Bourbaki C2 = {bourbaki_c2_14},  ratio = {ratio_14}"
    )

    print()
    same_ratio = sp.simplify(ratio_7 - ratio_14) == 0
    print(f"  SAME rescale ratio at rho=7 and rho=14? {same_ratio}  (ratio = {ratio_7})")
    assert same_ratio, (
        "CRITICAL: rho=7 and rho=14 give DIFFERENT native/Bourbaki ratios -- "
        "the 'universal global rescale' hypothesis is FALSE, STOP and re-examine "
        "Round 55's K_cert conversion entirely"
    )
    print("  CONFIRMED: the native-to-Bourbaki rescale is a UNIVERSAL constant (ratio=2 in")
    print("  Casimir-squared units, i.e. generator rescale sqrt(2)), independently verified")
    print("  at TWO representations, not a rho=7-specific coincidence. This is expected on")
    print("  structural grounds (the ratio between two FIXED, rho-independent invariant")
    print("  inner products on g2 cannot itself depend on rho), but empirical confirmation")
    print("  at a second point catches any bookkeeping/implementation bug the structural")
    print("  argument alone would not.")

    print()
    print("=" * 70)
    print("ITEM 3: full-operator reconstruction at one known point")
    print("=" * 70)
    print("""
  NOT re-derived here -- ALREADY established, exactly, by Round 22's own
  STEP 2 (g2su3_nomizu_crossterms.py, decision.md:3386-3390):

    "sum of 5 pieces == D^2(singlet_1) EXACTLY, full 448-dim? True"
    (CASIMIR + D64-SQUARED + SU3-CURVATURE + TORSION + MIXED_AB
     = d7_apply(d7_apply(w_s1, D64), D64), verified symbolically, exact)

  This IS the "collect D_full^2 = Casimir + F_sigma + Q and reproduce
  the known spectrum" check -- it was already done, 3 days before this
  round, and PASSES. Citing, not repeating: re-running it here would
  add no new information (same functions, same test vector, same
  ground truth).
""")

    print("=" * 70)
    print("BONUS (cheap, directly resolves the B_0-vs-mu_sigma framing")
    print("question for the D64^2 piece specifically): D64's OWN global")
    print("spectrum -- is it ever negative anywhere, for ANY rho?")
    print("=" * 70)
    D64 = build_D_matrix64()
    D64sq = sp.simplify(D64 * D64)
    herm = sp.simplify(D64 - D64.H) == sp.zeros(64, 64)
    print(f"  D64 Hermitian? {herm}")
    assert herm, "D64 not Hermitian -- STOP"
    ev = D64sq.eigenvals()
    print(f"  D64^2 exact eigenvalues: {ev}")
    min_ev = min(sp.re(sp.nsimplify(v)) for v in ev.keys())
    print("  Global minimum eigenvalue of D64^2 (over the FULL 64-dim fibre,")
    print("  independent of rho since D64 itself has zero rho-dependence,")
    print(f"  confirmed Round 54): {min_ev}")
    assert min_ev >= 0, (
        "D64^2 has a NEGATIVE eigenvalue somewhere -- STOP, B_0 could be a real deficit"
    )
    print("""
  RESULT: D64^2 is POSITIVE SEMI-DEFINITE (min eigenvalue = 0 exactly,
  multiplicity 36; confirmed Hermitian, all 4 distinct eigenvalues
  {0, 2/3, 10/3, 4} are >= 0). This is a FIXED, universal fact about
  D64 alone -- true for every rho, since D64 does not depend on rho.

  This resolves the B_0-vs-mu_sigma question CONSERVATIVELY but
  CLEANLY: D64^2's contribution to the total operator can NEVER be
  negative, for ANY rho, on ANY input vector -- so dropping it from the
  lower bound (B_0=0) is always SAFE (a valid, if not maximally tight,
  choice), never a hidden deficit. The optimistic reading (+mu_sigma
  strengthens the bound using D64^2's specific nonzero value on a
  particular test vector, e.g. +4 as seen on singlet_1) is NOT
  universally licensed -- the global minimum is 0, not 4; singlet_1's
  own value of 4 was that vector's own eigenvalue in a higher
  eigenspace, not the guaranteed worst case across all rho and all
  sigma-blocks. The SAFE, certified statement is B_0>=0 (never
  negative), not a specific positive mu_sigma applicable to every case.
""")

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"""
  1. Normalization dictionary: native quantities relate to Bourbaki
     quantities used in Round 52-54 via a UNIVERSAL rescale, confirmed
     at TWO independent representations (rho=7: {native_c2_7}->{bourbaki_c2_7},
     rho=14: {native_c2_14}->{bourbaki_c2_14}, SAME ratio {ratio_7} both times).
  2. K_cert=2*sqrt(6)/3 (Round 55) used this SAME, now double-confirmed,
     conversion -- its derivation stands, unchanged.
  3. The full-operator reconstruction check the reviewer asked for was
     already done (Round 22 STEP 2, exact, 3 days prior) -- cited, not
     repeated.
  4. D64^2 (the piece behind Round 55's open B_0 question) is PROVEN
     positive semi-definite -- can NEVER be a hidden negative penalty,
     for any rho. Safe, certified choice: B_0=0 (a valid lower bound,
     though not necessarily the tightest one -- the tightest bound
     would require the sigma-block-specific minimum, deferred as the
     reviewer's own "compute mu_sigma" next step, NOT attempted in this
     narrow round).
""")


if __name__ == "__main__":
    main()
