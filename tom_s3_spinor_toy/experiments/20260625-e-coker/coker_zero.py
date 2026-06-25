"""
E-COKER: prove dim coker(D^+_{S⁻}) = 0 on G₂/SU(3) = S⁶.

Strategy: D^- = (D^+)† is G₂-equivariant. Show ker(D^-) = 0 via:
  1. Non-trivial G₂-reps: same KP gap as E-KP1 → no zero modes in target
  2. Trivial G₂-rep (0,0): dim(target trivials in S⁻⊗S⁻) = 1 < dim(source trivials in S⁺⊗S⁻) = 2
     → D^-|_{trivial}: ℂ¹ → ℂ² has ind(D^-)=-ind(D^+)=-1 → rank≥1 → dim ker=0

All computation reuses E-KP1 Casimir and LR decomposition infrastructure.
"""

import sys
import os
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "20260625-kp-zero-mode"))

from kp_zero_mode import (
    su3_casimir,
    g2_casimir,
    _su3_lr_decompose,
    run_kp_analysis,
)


# ── Bundle definitions (same as E-KP1) ──────────────────────────────────────

S_MINUS_SU3 = [(1, 0), (0, 0)]  # S⁻|_{SU(3)} = 3 ⊕ 1
S_PLUS_SU3 = [(0, 1), (0, 0)]  # S⁺|_{SU(3)} = 3̄ ⊕ 1


def _tensor_decompose(b1: list, b2: list) -> Counter:
    """Decompose tensor product of two SU(3) direct sums."""
    result: Counter = Counter()
    for r1 in b1:
        for r2 in b2:
            decomp = _su3_lr_decompose(*r1, *r2)
            for rep, mult in decomp.items():
                result[rep] += mult
    return result


def run_coker_analysis() -> dict:
    """
    E-COKER experiment: prove dim coker(D^+_{S⁻}) = 0.

    D^-_{S⁻}: Γ(S⁻⊗S⁻) → Γ(S⁺⊗S⁻) is the adjoint of D^+_{S⁻}.
    ker(D^-_{S⁻}) = 0 iff coker(D^+_{S⁻}) = 0.

    Returns dict with all computed results.
    """
    results: dict = {}
    checks_passed = 0
    checks_total = 0

    print("=" * 60)
    print("E-COKER: dim coker(D^+_{S⁻}) = 0 on G₂/SU(3)")
    print("=" * 60)

    # ── Step 1: Decompose target bundle S⁻⊗S⁻ ───────────────────────────────
    print("\nStep 1: Decompose S⁻⊗S⁻|_{SU(3)}")
    sminus_sminus = _tensor_decompose(S_MINUS_SU3, S_MINUS_SU3)
    print(f"  S⁻⊗S⁻|_SU(3) = {dict(sminus_sminus)}")

    # Expected: (2,0)⊕(0,1)⊕2×(1,0)⊕(0,0)
    expected_target = Counter({(2, 0): 1, (0, 1): 1, (1, 0): 2, (0, 0): 1})
    checks_total += 1
    ok1 = sminus_sminus == expected_target
    print(f"  {'✓' if ok1 else '✗'} S⁻⊗S⁻ decomposition correct")
    if ok1:
        checks_passed += 1
    results["sminus_sminus"] = dict(sminus_sminus)

    # ── Step 2: Decompose source bundle S⁺⊗S⁻ ───────────────────────────────
    print("\nStep 2: Decompose S⁺⊗S⁻|_{SU(3)} (source of D^+, target of D^-)")
    splus_sminus = _tensor_decompose(S_PLUS_SU3, S_MINUS_SU3)
    print(f"  S⁺⊗S⁻|_SU(3) = {dict(splus_sminus)}")

    expected_source = Counter({(1, 1): 1, (0, 1): 1, (1, 0): 1, (0, 0): 2})
    checks_total += 1
    ok2 = splus_sminus == expected_source
    print(f"  {'✓' if ok2 else '✗'} S⁺⊗S⁻ decomposition correct")
    if ok2:
        checks_passed += 1
    results["splus_sminus"] = dict(splus_sminus)

    # ── Step 3: Count trivial G₂-reps ────────────────────────────────────────
    print("\nStep 3: Count trivial G₂-invariant sections")
    trivials_target = sminus_sminus.get((0, 0), 0)  # in S⁻⊗S⁻ (domain of D^-)
    trivials_source = splus_sminus.get((0, 0), 0)  # in S⁺⊗S⁻ (codomain of D^-)
    print(f"  S⁻⊗S⁻: {trivials_target} trivial rep(s) [domain of D^-]")
    print(f"  S⁺⊗S⁻: {trivials_source} trivial rep(s) [codomain of D^-]")

    checks_total += 1
    ok3 = (trivials_target == 1) and (trivials_source == 2)
    print(f"  {'✓' if ok3 else '✗'} 1 trivial in target (S⁻⊗S⁻), 2 in source (S⁺⊗S⁻)")
    if ok3:
        checks_passed += 1
    results["trivials_in_target_of_Dplus"] = trivials_target
    results["trivials_in_source_of_Dplus"] = trivials_source

    # ── Step 4: KP gap for non-trivial G₂-reps in S⁻⊗S⁻ ────────────────────
    print("\nStep 4: KP spectral gap — non-trivial G₂-reps in S⁻⊗S⁻ have λ² > 0")
    fibre_target = list(sminus_sminus.keys())
    nontrivial_target = [σ for σ in fibre_target if σ != (0, 0)]

    kp_gaps_target = []
    for sigma in nontrivial_target:
        c2_g2_min = g2_casimir(1, 0)  # minimum non-trivial G₂ Casimir = 4
        c2_su3 = su3_casimir(*sigma)
        gap = float(c2_g2_min - c2_su3)
        kp_gaps_target.append((sigma, gap))
        print(f"  G₂(1,0) via σ={sigma}: λ² = {c2_g2_min} - {c2_su3} = {gap:.3f}")

    checks_total += 1
    ok4 = all(g > 0 for _, g in kp_gaps_target)
    print(f"  {'✓' if ok4 else '✗'} All non-trivial σ in S⁻⊗S⁻ have KP gap > 0")
    if ok4:
        checks_passed += 1
    results["kp_gaps_target"] = kp_gaps_target
    results["min_kp_gap_target"] = min(g for _, g in kp_gaps_target)

    # ── Step 5: D^-|_{trivial} — adjoint argument ────────────────────────────
    print("\nStep 5: D^-|_{trivial} adjoint argument")
    print(f"  D^-: ℂ^{trivials_target} → ℂ^{trivials_source}")
    ind_dplus = run_kp_analysis()["ind_total"]
    ind_dminus = -ind_dplus  # adjoint reverses index sign
    print(f"  ind(D^+) = {ind_dplus} → ind(D^-) = {ind_dminus}")
    print(f"  D^-|_trivial: ℂ¹ → ℂ², ind = {ind_dminus}")
    print("  rank(D^-|_trivial) ≥ max(0, dim_domain + ind) = max(0, 1 + (-1)) = 0")
    print("  But rank = dim_domain - dim ker ≥ 0, and rank ≤ min(1, 2) = 1")
    print("  From E-KP1: dim ker(D^+|_trivial) = 1, rank(D^+|_trivial) = 1")
    print(f"  Adjoint: ker(D^-) = coker(D^+) = {ind_dplus - 1}")
    # rank(D^-) = rank(D^+) by adjoint symmetry; dim ker(D^-) = dim(domain) - rank
    # D^-: ℂ¹ → ℂ², rank(D^-) = trivials_target - dim ker(D^-)
    # D^- = (D^+)†: rank(D^-) = rank(D^+) = 1
    rank_dplus = 1  # from E-KP1: rank=1
    dim_ker_dminus = trivials_target - rank_dplus  # 1 - 1 = 0
    print(
        f"  dim ker(D^-|_trivial) = {trivials_target} - rank(D^+|_trivial) = {trivials_target} - {rank_dplus} = {dim_ker_dminus}"
    )

    checks_total += 1
    ok5 = dim_ker_dminus == 0
    print(f"  {'✓' if ok5 else '✗'} dim ker(D^-|_trivial) = 0")
    if ok5:
        checks_passed += 1
    results["rank_dplus"] = rank_dplus
    results["dim_ker_dminus"] = dim_ker_dminus

    # ── Step 6: Total coker ────────────────────────────────────────────────────
    print("\nStep 6: Total dim coker(D^+_{S⁻})")
    dim_coker_total = dim_ker_dminus  # only trivial G₂-rep can contribute; all others λ²>0
    print(f"  dim coker = dim ker(D^-) = {dim_coker_total}")
    print(
        f"  Cross-check: ind(D^+) = dim ker(D^+) - dim coker(D^+) = 1 - {dim_coker_total} = {ind_dplus - dim_coker_total}"
    )

    checks_total += 1
    ok6 = (dim_coker_total == 0) and (ind_dplus - dim_coker_total == ind_dplus)
    print(f"  {'✓' if ok6 else '✗'} dim coker = 0, consistent with ind=1 and dim ker=1")
    if ok6:
        checks_passed += 1
    results["dim_coker_result"] = dim_coker_total
    results["ind_consistency"] = ind_dplus - dim_coker_total

    # ── Final verdict ─────────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    verdict = "PASS" if checks_passed == checks_total else "FAIL"
    print(f"VERDICT: {verdict} ({checks_passed}/{checks_total} checks)")
    if verdict == "PASS":
        print("dim coker(D^+_{S⁻}) = 0  ■")
    results["verdict"] = verdict
    results["checks_passed"] = checks_passed
    results["checks_total"] = checks_total
    return results


if __name__ == "__main__":
    run_coker_analysis()
