"""G33: Chern-Gauss-Bonnet on S⁶ — A1 hypothesis test.

A1 hypothesis: dim_ℂ(S⁶)=3 → c₃(T^{1,0}S⁶)=6 → ind=3 (three generations).

Result: A1 is NULL.
  c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (ONE generation unit, not 6).
  ind(D_{T^{1,0}S⁶}) = 1 (one generation from holomorphic tangent).
  c₃=6 requires c₃ = N_gen × 2 → assumes N_gen=3 (circular, not a derivation).

Key mathematics:
  1. Chern-Gauss-Bonnet for almost complex manifolds (M²ⁿ, J):
       c_n(T^{1,0}M) = e(TM)  [top Chern class = Euler class]
       χ(M) = ∫_M e(TM) = ∫_M c_n(T^{1,0}M)

  2. Betti numbers of Sⁿ: b_k = 1 for k=0,n; 0 otherwise.
       χ(Sⁿ) = Σ_k (-1)^k b_k = 1 + (-1)^n

  3. S⁶: χ(S⁶) = 1 + (-1)⁶ = 2  →  c₃(T^{1,0}S⁶) = 2

  4. Atiyah-Singer on S⁶ (Â=1):
       ind(D_V) = c₃(V)/2
       ind(D_{T^{1,0}S⁶}) = 2/2 = 1  [ONE generation from T^{1,0}S⁶]

  5. Frobenius consistency (G30 Step 3):
       S⁺ = 3⊕1, S⁻ = 3̄⊕1 under SU(3) ⊂ SU(4) = Spin(6)
       ind(D ⊗ V_{fund.3}) = mult(3 in S⁺) - mult(3 in S⁻) = 1 - 0 = 1 ✓

  6. G₂-equivariant rank-3 bundles = SU(3)-reps of dim=3:
       {3 → c₃=2, 3̄ → c₃=-2, 1⊕1⊕1 → c₃=0}
       max|c₃| = 2  →  no G₂-equivariant rank-3 bundle has c₃=6.

Also corrects G32 catalogue error:
  G32 listed fundamental 3-rep of SU(3) with c₃=0 (incorrect).
  Correct: c₃(fundamental 3) = χ(S⁶) = 2; this bundle has ind=1.
  G30's KILL applies to G₂-IRREP bundles (7, 14, 27, ...),
  NOT to SU(3)-isotropy-rep bundles like the fundamental 3.

Positive result:
  T^{1,0}S⁶ (SU(3) fundamental rep) is G₂-equivariant with c₃=2, ind=1.
  This gives ONE generation from S⁶ geometry (not zero, not three).
  Three generations: c₃=6 = 3 × c₃(T^{1,0}S⁶) — non-equivariant (G32).
  The open question is WHY the factor is 3 (not 1 or 2).
"""

from fractions import Fraction


# ---------------------------------------------------------------------------
# 1. Euler characteristic of spheres
# ---------------------------------------------------------------------------


def chi_sphere(n: int) -> int:
    """Euler characteristic of Sⁿ via Betti numbers.

    H^k(Sⁿ;ℤ) = ℤ for k=0,n; 0 otherwise.
    χ = Σ_k (-1)^k rank(H^k) = 1 + (-1)^n.
    """
    if n < 0:
        raise ValueError(f"n={n} < 0: sphere undefined")
    return 1 + (-1) ** n


CHI_S6: int = chi_sphere(6)  # = 2


# ---------------------------------------------------------------------------
# 2. Chern-Gauss-Bonnet: c_n(T^{1,0}M) = e(TM) for almost complex manifolds
# ---------------------------------------------------------------------------


def c_top_t10_sphere(n: int) -> int:
    """Top Chern class of the holomorphic tangent bundle of an almost complex Sⁿ.

    For any almost complex manifold (M²ⁿ, J):
      c_n(T^{1,0}M) = e(TM)  as cohomology classes in H²ⁿ(M;ℤ).
      Integrating: ∫_M c_n = χ(M).

    Almost complex structures exist only on S², S⁶ (among spheres):
      S² = ℂP¹ (integrable, c₁=2)
      S⁶ = G₂/SU(3) (non-integrable, c₃=2)

    For n odd: no almost complex structure exists on Sⁿ → raises ValueError.
    """
    if n % 2 != 0:
        raise ValueError(f"S^{n}: no almost complex structure (n must be even)")
    return chi_sphere(n)


C3_T10_S6: int = c_top_t10_sphere(6)  # = 2


# ---------------------------------------------------------------------------
# 3. Index of the Dirac operator twisted by a bundle on S⁶
# ---------------------------------------------------------------------------


def index_from_c3(c3: int) -> Fraction:
    """Atiyah-Singer index of twisted Dirac on S⁶.

    ind(D_V^+) = ∫_{S⁶} ch(V) · Â(S⁶).
    Â(S⁶) = 1  (stably parallelizable: all Pontryagin classes vanish).
    c₁=c₂=0 on S⁶  (H²=H⁴=0).
    ch₃(V) = c₃(V)/2.
    → ind = c₃(V)/2.

    Requires c₃ even (ind ∈ ℤ).
    """
    if c3 % 2 != 0:
        raise ValueError(f"c₃={c3} is odd: ind = c₃/2 ∉ ℤ, bundle inconsistent on S⁶")
    return Fraction(c3, 2)


INDEX_T10_S6: Fraction = index_from_c3(C3_T10_S6)  # = 1


# ---------------------------------------------------------------------------
# 4. Frobenius reciprocity consistency check (imported logic from G30)
# ---------------------------------------------------------------------------

# Spinor decomposition under SU(3) ⊂ Spin(6) ≅ SU(4):
#   S⁺ (positive chirality spinors) = 4 of SU(4) → 3⊕1 under SU(3)
#   S⁻ (negative chirality spinors) = 4̄ of SU(4) → 3̄⊕1 under SU(3)
_S_PLUS: dict[str, int] = {"3": 1, "1": 1}  # multiplicities in S⁺
_S_MINUS: dict[str, int] = {"3bar": 1, "1": 1}  # multiplicities in S⁻


def frobenius_index(su3_irrep: str) -> int:
    """Frobenius index for an SU(3)-irrep bundle on S⁶ = G₂/SU(3).

    ind(D ⊗ V_ρ) = mult(ρ in S⁺) - mult(ρ in S⁻).
    Reproduces G30 Step 3 result.
    """
    return _S_PLUS.get(su3_irrep, 0) - _S_MINUS.get(su3_irrep, 0)


FROBENIUS_FUND: int = frobenius_index("3")  # = +1 (fundamental 3-rep)
FROBENIUS_ANTIFUND: int = frobenius_index("3bar")  # = -1 (antifundamental 3̄-rep)
FROBENIUS_TRIVIAL: int = frobenius_index("1")  # = 0 (trivial)


# ---------------------------------------------------------------------------
# 5. All SU(3)-representations of complex dimension 3
#    (= all G₂-equivariant rank-3 bundles on S⁶)
# ---------------------------------------------------------------------------

# SU(3) irreps with dim=3: exactly {3, 3̄}.
# Plus the reducible: 1⊕1⊕1 (three singlets), c₃=0.
SU3_RANK3_REPS: list[dict] = [
    {
        "name": "fundamental 3",
        "dim": 3,
        "c3": 2,  # = χ(S⁶) via Frobenius: ind=1 → c₃=2
        "ind": 1,
        "g2_equivariant": True,
        "comment": "= T^{1,0}S⁶; G₂-equivariant, NOT a G₂-irrep",
    },
    {
        "name": "antifundamental 3̄",
        "dim": 3,
        "c3": -2,  # conjugate: ind=-1 → c₃=-2
        "ind": -1,
        "g2_equivariant": True,
        "comment": "= T^{0,1}S⁶ (antiholomorphic tangent)",
    },
    {
        "name": "trivial 1⊕1⊕1",
        "dim": 3,
        "c3": 0,
        "ind": 0,
        "g2_equivariant": True,
        "comment": "three singlets; c₃=0, no generations",
    },
]

# Maximum |c₃| achievable by any G₂-equivariant rank-3 bundle:
MAX_ABS_C3_EQUIVARIANT_RANK3: int = max(abs(r["c3"]) for r in SU3_RANK3_REPS)  # = 2

# Maximum c₃ (positive):
MAX_C3_EQUIVARIANT_RANK3: int = max(r["c3"] for r in SU3_RANK3_REPS)  # = 2


# ---------------------------------------------------------------------------
# 6. A1 hypothesis analysis
# ---------------------------------------------------------------------------


def a1_analysis(n_gen: int) -> dict:
    """Test whether A1 (dim_ℂ(S⁶)=3) derives c₃=6 for n_gen generations.

    A1 hypothesis: dim_ℂ(S⁶)=3 → c₃(T^{1,0}S⁶)=6 → ind=3.

    Computation:
      c₃(T^{1,0}S⁶) = χ(S⁶) = 2  [the "generation unit"]
      For N generations: c₃ = N × 2  [requires N as input]
      Ratio: c₃_needed / c₃_unit = N_gen  [always circular]

    Verdict: A1 is NULL.
      A1 establishes the UNIT (c₃=2 per generation), not the COUNT (N_gen=3).
      c₃=6 ↔ N_gen=3 is a restatement, not a geometric derivation of N_gen.
    """
    c3_unit = C3_T10_S6  # = 2, from χ(S⁶)
    c3_needed = n_gen * c3_unit  # = 2 × N_gen
    ind_needed = n_gen  # = N_gen (by construction)

    return {
        "n_gen_input": n_gen,
        "c3_canonical_unit": c3_unit,
        "c3_needed": c3_needed,
        "ind_needed": ind_needed,
        "ratio_to_unit": n_gen,  # always = n_gen (circular)
        "is_circular": True,  # ratio = n_gen always
        "derives_n_gen_geometrically": False,
        "a1_confirmed": False,  # c₃(T^{1,0}) = 2 ≠ 6 (for n_gen=3)
        "verdict": "NULL",
        "reason": (
            f"c₃(T^{{1,0}}S⁶) = {c3_unit} = χ(S⁶); "
            f"c₃={c3_needed} requires N_gen={n_gen} as axiom (circular)"
        ),
    }


A1_THREE_GENERATIONS: dict = a1_analysis(3)


# ---------------------------------------------------------------------------
# 7. G32 catalogue correction
# ---------------------------------------------------------------------------

# G32 incorrectly assigned c₃=0 to the fundamental 3-rep of SU(3).
# G32's catalogue entry:
#   BundleS6(rank=3, c3=0, g2_equivariant=True, description="fundamental 3 of SU(3)")
#
# Correct value:
#   c₃(fundamental 3-rep) = χ(S⁶) = 2  [from Chern-Gauss-Bonnet + Frobenius]
#   ind(D_{fund.3}) = 1  [one generation]
#
# G30's KILL applies to G₂-IRREP bundles (7, 14, 27, ...) — NOT to SU(3)-isotropy reps.
# The fundamental 3-rep is a G₂-equivariant bundle (ind=1), NOT killed by G30.
#
# Impact on G32:
#   Main conclusion preserved: c₃=6 rank-3 bundle is non-equivariant.
#   Reason: all G₂-equivariant rank-3 bundles have c₃ ∈ {-2, 0, 2}.
#   No SU(3)-rep of dim=3 gives c₃=6.

G32_CATALOGUE_ERROR: dict = {
    "bundle": "fundamental 3-rep of SU(3)",
    "c3_in_g32": 0,  # what G32 wrote (wrong)
    "c3_correct": 2,  # what Chern-Gauss-Bonnet + Frobenius give
    "ind_correct": 1,  # one generation from this bundle
    "g30_kills_this": False,  # G30 kills G₂-irreps, not SU(3)-isotropy reps
    "g32_main_conclusion_preserved": True,  # c₃=6 is still non-equivariant
}


# ---------------------------------------------------------------------------
# 8. Complete picture (G30 + G33 + G32)
# ---------------------------------------------------------------------------

# Route to 0 generations: G₂-IRREP bundles (7, 14, 27, ...) — killed by G30.
# Route to 1 generation: T^{1,0}S⁶ (fundamental 3-rep) — G₂-equivariant, c₃=2.
# Route to 3 generations: G32 escape (c₃=6, non-equivariant).
# A1 verdict: does NOT derive N_gen=3; gives the unit c₃=2 only.

GENERATION_ROUTES: list[dict] = [
    {
        "n_gen": 0,
        "bundle": "G₂-IRREP bundles (7, 14, 27, ...)",
        "c3": 0,
        "equivariant": True,
        "status": "NULL (G30 kill)",
    },
    {
        "n_gen": 1,
        "bundle": "T^{1,0}S⁶ = fundamental 3-rep of SU(3)",
        "c3": 2,
        "equivariant": True,
        "status": "OPEN (G₂-equivariant, ind=1; but N_gen=1 ≠ 3)",
    },
    {
        "n_gen": 3,
        "bundle": "G32 escape: non-equivariant rank-3, c₃=6",
        "c3": 6,
        "equivariant": False,
        "status": "OPEN (G32); origin of factor 3 unknown",
    },
]


if __name__ == "__main__":
    print("=" * 65)
    print("G33: Chern-Gauss-Bonnet on S⁶ — A1 hypothesis test")
    print("=" * 65)

    print(f"\nStep 1: Euler characteristic")
    print(f"  χ(Sⁿ) = 1 + (-1)ⁿ  [Betti numbers]")
    print(f"  χ(S⁶) = {CHI_S6}")

    print(f"\nStep 2: Chern-Gauss-Bonnet")
    print(f"  c₃(T^{{1,0}}S⁶) = e(TS⁶) = χ(S⁶) = {C3_T10_S6}")

    print(f"\nStep 3: Index from canonical bundle")
    print(f"  ind(D_{{T^{{1,0}}}}) = c₃/2 = {INDEX_T10_S6}  [ONE generation]")

    print(f"\nStep 4: Frobenius consistency (G30 cross-check)")
    print(
        f"  su3_index('3') = {FROBENIUS_FUND} = ind ✓"
        if FROBENIUS_FUND == int(INDEX_T10_S6)
        else "  INCONSISTENCY!"
    )

    print(f"\nStep 5: G₂-equivariant rank-3 bundles")
    for r in SU3_RANK3_REPS:
        print(f"  {r['name']:20s}: c₃={r['c3']:3d}, ind={r['ind']:2d}  ({r['comment']})")
    print(f"  max c₃ = {MAX_C3_EQUIVARIANT_RANK3}  →  no equivariant rank-3 bundle has c₃=6")

    print(f"\nStep 6: A1 hypothesis analysis")
    d = A1_THREE_GENERATIONS
    print(f"  c₃(T^{{1,0}}S⁶) = {d['c3_canonical_unit']}  [generation unit]")
    print(f"  c₃ for N_gen=3:  {d['c3_needed']}  = 3 × {d['c3_canonical_unit']}")
    print(f"  A1 confirmed? {d['a1_confirmed']}  (requires N_gen=3 as input)")
    print(f"  A1 verdict: {d['verdict']}")
    print(f"  Reason: {d['reason']}")

    print(f"\nStep 7: G32 catalogue correction")
    e = G32_CATALOGUE_ERROR
    print(f"  Bundle: {e['bundle']}")
    print(f"  c₃ in G32: {e['c3_in_g32']}  (wrong)  →  correct: {e['c3_correct']}")
    print(f"  G30 kills this bundle: {e['g30_kills_this']}  (G30 kills G₂-irreps, not SU(3)-reps)")
    print(f"  G32 main conclusion preserved: {e['g32_main_conclusion_preserved']}")

    print(f"\nStep 8: Complete generation route map")
    for r in GENERATION_ROUTES:
        print(
            f"  N_gen={r['n_gen']}: {r['status']}  (c₃={r['c3']}, equivariant={r['equivariant']})"
        )

    print(f"\n{'=' * 65}")
    print("G33 VERDICT: A1 = NULL")
    print("  c₃(T^{1,0}S⁶) = 2, not 6 → A1 gives the generation UNIT, not the COUNT")
    print("  THREE generations need c₃=6 = 3×2 → N_gen=3 is still the open input")
    print("  G32 escape route (non-equivariant c₃=6) remains the only path to N_gen=3")
    print("  New positive result: T^{1,0}S⁶ gives ONE generation geometrically (ind=1)")
