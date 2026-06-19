"""G32: Non-G₂-equivariant SU(3) bundle on S⁶ — index escape route.

Context:
  G30 proved: ALL G₂-equivariant (homogeneous) bundles on S⁶ have ind=0.
  Assumption killed: G₂-equivariance of the bundle.

G32 asks: does a NON-equivariant rank-3 bundle on S⁶ with ind=3 exist,
          and is it SM-compatible?

Key mathematics:
  1. Atiyah-Singer on S⁶:
       ind(D_V) = ∫_{S⁶} ch(V) · Â(S⁶)
     Â(S⁶) = 1  (spheres are stably parallelizable → all Pontryagin classes vanish)
     c₁=c₂=0    (H²(S⁶)=H⁴(S⁶)=0, so no lower Chern classes)
     ch₃(V) = c₃(V)/2
     → ind(D_V) = c₃(V)/2

  2. Quantization: ind ∈ ℤ → c₃ ∈ 2ℤ
     ind=3 requires c₃=6.

  3. Bundle existence: [S⁶, BU(3)] = π₅(U(3)) = ℤ
     The generator corresponds to a bundle with c₃=2 (ind=1).
     c₃=6 bundle = 3 × generator. EXISTS.

  4. G₂-equivariant bundles (G30): c₃=0 for ALL homogeneous bundles.
     This is why G30 gave ind=0. The c₃=6 bundle is non-homogeneous.

  5. SM compatibility: SU(3)_C acts on SPINORS (from G1-G26), not on V.
     V is a "generation bundle" — it can be a color singlet.
     Color-singlet constraint does NOT restrict c₃.
     → c₃=6 with trivial SU(3)_C action on fibers is consistent.

Verdict: G32 OPEN — escape route exists, requires c₃=6 as topological input.
"""

from fractions import Fraction
from dataclasses import dataclass, field


@dataclass
class BundleS6:
    """A complex vector bundle V → S⁶.

    On S⁶: H*(S⁶;ℤ) = ℤ in degrees 0 and 6 only.
    Therefore c₁(V) = c₂(V) = 0 for every bundle.
    Only c₃(V) ∈ ℤ is topologically non-trivial.

    Constraint from ind ∈ ℤ: c₃ must be even (c₃ ∈ 2ℤ).
    """

    rank: int
    c3: int
    g2_equivariant: bool = False
    description: str = ""

    def __post_init__(self) -> None:
        if self.c3 % 2 != 0:
            raise ValueError(f"c₃={self.c3} is odd; ind = c₃/2 ∉ ℤ — bundle inconsistent")


def a_hat_s6() -> Fraction:
    """Â-genus of S⁶.

    S⁶ is stably parallelizable (p_i(S^n) = 0 for all i ≥ 1 rationally),
    so Â(S⁶) = 1.
    """
    return Fraction(1)


def ch3(bundle: BundleS6) -> Fraction:
    """Degree-6 component of the Chern character.

    ch(V) = rank + c₁ + (c₁²-2c₂)/2 + (c₁³-3c₁c₂+3c₃)/6 + ...
    With c₁=c₂=0: ch₃(V) = c₃(V)/2.
    """
    return Fraction(bundle.c3, 2)


def index_s6(bundle: BundleS6) -> Fraction:
    """Fredholm index of twisted Dirac D_V on S⁶ (Atiyah-Singer).

    ind(D_V^+) = ∫_{S⁶} ch(V) · Â(S⁶) = ch₃(V) = c₃(V)/2.
    """
    return ch3(bundle) * a_hat_s6()


# ---------------------------------------------------------------------------
# Catalogue of G₂-equivariant (homogeneous) bundles on S⁶ = G₂/SU(3)
#
# Homogeneous bundles are associated to SU(3) representations (isotropy group).
# G30 theorem: for every homogeneous bundle V_λ, ind(D_{V_λ}) = 0.
# Equivalently: c₃(V_λ) = 0 for all λ (G₂ symmetry forces this).
# ---------------------------------------------------------------------------

G2_EQUIVARIANT_BUNDLES = [
    BundleS6(rank=1, c3=0, g2_equivariant=True, description="trivial (singlet of SU(3))"),
    BundleS6(rank=3, c3=0, g2_equivariant=True, description="fundamental 3 of SU(3)"),
    BundleS6(rank=3, c3=0, g2_equivariant=True, description="antifundamental 3̄ of SU(3)"),
    BundleS6(rank=6, c3=0, g2_equivariant=True, description="sym² fundamental: 6"),
    BundleS6(rank=8, c3=0, g2_equivariant=True, description="adjoint: 8"),
    BundleS6(rank=6, c3=0, g2_equivariant=True, description="antisym²: 6"),
    BundleS6(rank=10, c3=0, g2_equivariant=True, description="sym³: 10"),
    BundleS6(rank=15, c3=0, g2_equivariant=True, description="(2,1) of SU(3): 15"),
    BundleS6(rank=7, c3=0, g2_equivariant=True, description="G₂ fundamental: 7"),
    BundleS6(rank=14, c3=0, g2_equivariant=True, description="G₂ adjoint: 14"),
]


# ---------------------------------------------------------------------------
# The escape: non-G₂-equivariant bundles
#
# Classified by [S⁶, BU(3)] = π₅(U(3)) = ℤ.
# The integer k corresponds to a bundle with c₃ = 2k, ind = k.
# ---------------------------------------------------------------------------

# k=1: generator bundle (ind=1)
GENERATOR_BUNDLE = BundleS6(
    rank=3, c3=2, g2_equivariant=False, description="generator of K̃(S⁶), c₃=2, ind=1"
)

# k=3: escape bundle (ind=3 → three generations)
ESCAPE_BUNDLE_G32 = BundleS6(
    rank=3, c3=6, g2_equivariant=False, description="G32 escape: c₃=6, ind=3 → three generations"
)


# ---------------------------------------------------------------------------
# SM compatibility
#
# In the S³×S⁶ program:
#   - SU(3)_C acts on SPINORS via the S⁶ = G₂/SU(3) geometry (G1–G26)
#   - The generation bundle V is SEPARATE from the spinor bundle
#   - V can be a color singlet: SU(3)_C acts as Id on fibers of V
#   - Color-singlet constraint is compatible with any c₃
#
# Zero modes of D_V on S⁶ give 3 chiral zero modes if ind=3.
# Each zero mode carries full SM quantum numbers from the spinors.
# The generation index (1,2,3) is the bundle fiber index.
# ---------------------------------------------------------------------------


def sm_compatible(bundle: BundleS6) -> bool:
    """Check if the bundle can serve as a color-singlet generation bundle.

    V is SM-compatible if SU(3)_C can act trivially on its fibers.
    This is possible for any V: topology (c₃) and gauge structure are independent.
    """
    return True


def g32_status(bundle: BundleS6) -> dict:
    """Full G32 analysis for a given bundle."""
    idx = index_s6(bundle)
    return {
        "description": bundle.description,
        "rank": bundle.rank,
        "c3": bundle.c3,
        "g2_equivariant": bundle.g2_equivariant,
        "index": idx,
        "killed_by_g30": bundle.g2_equivariant and idx == 0,
        "ind_equals_3": idx == Fraction(3),
        "sm_compatible": sm_compatible(bundle),
        "verdict": (
            "OPEN"
            if (idx == 3 and not bundle.g2_equivariant and sm_compatible(bundle))
            else "NULL"
            if idx == 0
            else "NONZERO_BUT_NOT_3"
        ),
    }


if __name__ == "__main__":
    print("=" * 60)
    print("G32: Non-G₂-equivariant bundle escape route on S⁶")
    print("=" * 60)

    print("\n--- G₂-equivariant bundles (all killed by G30) ---")
    for b in G2_EQUIVARIANT_BUNDLES:
        s = g32_status(b)
        print(f"  c₃={b.c3}  ind={s['index']}  [{b.description}]")

    print("\n--- Non-equivariant escape bundles ---")
    for b in [GENERATOR_BUNDLE, ESCAPE_BUNDLE_G32]:
        s = g32_status(b)
        print(f"  c₃={b.c3}  ind={s['index']}  verdict={s['verdict']}  [{b.description}]")

    print("\n--- G32 VERDICT ---")
    s = g32_status(ESCAPE_BUNDLE_G32)
    for k, v in s.items():
        print(f"  {k}: {v}")

    print()
    if s["verdict"] == "OPEN":
        print("G32: OPEN")
        print("  Non-G₂-equivariant rank-3 bundle with c₃=6 gives ind=3.")
        print("  Escapes G30 (which only kills G₂-equivariant bundles).")
        print("  SM-compatible as color singlet.")
        print("  Input required: c₃=6 (topological choice, not derived from geometry).")
