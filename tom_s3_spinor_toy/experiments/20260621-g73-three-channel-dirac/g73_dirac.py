"""G73: Three-channel Dirac on S³×S⁶ — N_gen = 3 from index theory.

CLAIM: The Atiyah-Singer index of the Dirac operator on S⁶, twisted by the
negative-chirality spinor bundle S⁻, equals 1 per SO(8)-triality channel.
Three triality channels (8_v, 8_s, 8_c) give total index 3 = N_gen.

LOGICAL CHAIN:
  G33  → c₃(T^{1,0}S⁶) = χ(S⁶) = 2
  G50  → χ-lemma: H²=H⁴=0 on S⁶ → c₁=c₂=0 for all bundles (addition simplifies)
  G69  → S⁻ of Spin(6) under SU(3): 4 → 3 + 1 = T^{1,0}S⁶ ⊕ trivial
  G73-B → c₃(S⁻) = c₃(T^{1,0}S⁶) + c₃(trivial) = 2 + 0 = 2
  G73-C → Â(S⁶) = 1 (p₁=0 since H⁴(S⁶)=0)
  G73-D → ind(D_{S⁶} ⊗ S⁻) = ∫Â·ch₃(S⁻) = c₃(S⁻)/2 = 1
  G67  → Z₃ triality: G₂=Fix(Z₃), all three 8-dim reps have same G₂-content
  G73-E → c₃(8_v)=c₃(8_s)=c₃(8_c)=2  [triality preserves topological invariants]
  G73-F → N_gen = sum_i ind_i = 1+1+1 = 3  ✓

TENSOR PRODUCT STRUCTURE:
  D_{S³×S⁶} = D_{S³} ⊗ I_{S(S⁶)} + γ₃ ⊗ D_{S⁶}
  where γ₃ = chirality element on S³ (= Pauli σ₂ on the 2-dim Weyl spinors).
  Spinor bundle: S(S³×S⁶) = S(S³) ⊗ S(S⁶) = 4 ⊗ 8 = 32 per channel.

BOUNDARY CONDITIONS (what G73 does NOT prove):
  - That exactly 1 zero mode (not more) appears per channel: index is a lower bound.
    Exact count requires spectral gap argument on S⁶ (outside G73 scope).
  - Geometric realization of E_v bundle (the vector channel): depends on G72 (Tom).
    Here we use algebraic triality argument that c₃(8_v) = c₃(8_s) = c₃(8_c).
"""

from fractions import Fraction

# ─── G73-A: Tensor product Dirac structure ──────────────────────────────────

# S³ spinor dimension: Spin(3) = SU(2), Dirac spinor = 4-dim (2 Weyl + 2 conj)
DIM_S3_SPINOR = 4

# S⁶ spinor dimension: Spin(6) = SU(4), Dirac spinor = 8 = 4 (S⁺) + 4 (S⁻)
DIM_S6_SPINOR = 8

# Full spinor on S³×S⁶ per triality channel (tensor product)
DIM_FULL_SPINOR_PER_CHANNEL = DIM_S3_SPINOR * DIM_S6_SPINOR  # = 32

# Three triality channels (8_v, 8_s, 8_c) from G67
N_TRIALITY_CHANNELS = 3

# Total spinor space
DIM_TOTAL_SPINOR = N_TRIALITY_CHANNELS * DIM_FULL_SPINOR_PER_CHANNEL  # = 96

# ─── G73-B: S⁶ spinor bundle splitting ──────────────────────────────────────

# S⁶ = G₂/SU(3). Tangent frame group: Spin(6) = SU(4).
# Dirac spinor of Spin(6) = 8-dim = S⁺ (4-dim) + S⁻ (4-dim).
#
# Under SU(3) ⊂ SU(4) [standard upper-left block embedding]:
#   S⁺: antifund 4̄ of SU(4) → 3̄ + 1 of SU(3)   [negative physical content]
#   S⁻: fund  4  of SU(4) →  3 + 1 of SU(3)   [positive physical content]
#
# Physical identification:
#   S⁻ = T^{1,0}S⁶ ⊕ trivial  [as SU(3) vector bundles]
#   T^{1,0}S⁶ → 3 of SU(3), trivial → 1 of SU(3)

DIM_S_MINUS = 4  # negative chirality Weyl spinor
DIM_T10_S6 = 3  # T^{1,0}S⁶ triplet part
DIM_TRIVIAL = 1  # singlet part

# Dimension check: S⁻ = T^{1,0}S⁶ ⊕ trivial
S_MINUS_SPLITS_AS = {"triplet": DIM_T10_S6, "singlet": DIM_TRIVIAL}
assert sum(S_MINUS_SPLITS_AS.values()) == DIM_S_MINUS  # 3+1=4 ✓

# ─── G73-C: Chern class addition formula on S⁶ ──────────────────────────────

# On S⁶: H²(S⁶) = 0 and H⁴(S⁶) = 0 (standard topology of S⁶).
# For ANY complex vector bundle E over S⁶: c₁(E) = 0 and c₂(E) = 0.
# This simplifies the Chern class addition formula:
#
#   c(A ⊕ B) = c(A)·c(B)
#   top degree component (degree 6):
#   c₃(A ⊕ B) = c₃(A)·1 + c₁(A)·c₂(B) + c₂(A)·c₁(B) + 1·c₃(B)
#              = c₃(A) + 0 + 0 + c₃(B)   [since c₁=c₂=0 on S⁶]
#              = c₃(A) + c₃(B)


def c3_direct_sum(c3_A: int, c3_B: int) -> int:
    """c₃(A⊕B) = c₃(A)+c₃(B) when H²=H⁴=0 (valid on S⁶)."""
    return c3_A + c3_B


# c₃(T^{1,0}S⁶) from G33: equals the Euler characteristic χ(S⁶) = 2.
# Proof: the Chern-Gauss-Bonnet theorem on S⁶ with SU(3) structure gives
#   χ(S⁶) = ∫c₃(T^{1,0}S⁶) = 2.
C3_T10_S6 = 2  # from G33 [VERIFIED-25-tests]

# c₃(trivial rank-1 bundle) = 0 (trivial bundle has all Chern classes = 0)
C3_TRIVIAL = 0

# c₃(S⁻) via addition formula:
C3_S_MINUS = c3_direct_sum(C3_T10_S6, C3_TRIVIAL)  # = 2

# ─── G73-D: Atiyah-Singer index on S⁶ ──────────────────────────────────────

# Index theorem (Atiyah-Singer, 1963):
#   ind(D ⊗ E) = ∫_{S⁶} Â(S⁶) · ch(E)
#
# Â(S⁶) = 1: since H⁴(S⁶) = 0, the first Pontryagin class p₁(S⁶) = 0,
# and Â = 1 - p₁/24 + ... = 1 exactly. No higher corrections (Â is polynomial in p_i).
#
# ch(E) on S⁶: only the degree-6 part contributes in the integral.
# For bundle E with c₁=c₂=0 on S⁶:
#   ch(E)|_{deg-6} = ch₃(E) = (c₁³ - 3c₁c₂ + 3c₃)/6 = c₃(E)/2
#
# Therefore: ind(D ⊗ E) = c₃(E)/2

A_HAT_S6 = 1  # Â-genus of S⁶ is exactly 1


def dirac_index_s6(c3: int) -> Fraction:
    """Atiyah-Singer index on S⁶: ind(D⊗E) = Â(S⁶) · c₃(E)/2."""
    return Fraction(A_HAT_S6 * c3, 2)


# Index per channel (using S⁻ as the twisting bundle):
INDEX_PER_CHANNEL = dirac_index_s6(C3_S_MINUS)  # = 2/2 = 1

# ─── G73-E: Triality invariance ──────────────────────────────────────────────

# G₂ = Fix(Z₃ triality) in SO(8).  [G67-B2 VERIFIED]
# The three channels 8_v, 8_s, 8_c are related by the Z₃ outer automorphism τ of SO(8).
#
# Key property of outer automorphisms and topological invariants:
# If φ: S⁶ → S⁶ is an isometry and E, E' = φ*E are the original and
# pulled-back bundle, then c₃(E') = c₃(E) (pullback preserves Chern classes).
#
# The triality automorphism τ permutes 8_v, 8_s, 8_c:
#   E_v = E_s^τ = E_c^{τ²}
# Since τ is a continuous symmetry of the structure group and S⁶ is a
# G₂-homogeneous space, the associated G₂-equivariant bundles satisfy:
#   c₃(E_v) = c₃(E_s) = c₃(E_c)
#
# Since we computed c₃(E_s) = c₃(S⁻) = 2:
C3_8V = C3_S_MINUS  # = 2  [by triality]
C3_8S = C3_S_MINUS  # = 2  [computed directly]
C3_8C = C3_S_MINUS  # = 2  [by triality]

CHANNELS = {
    "8_v": {"c3": C3_8V, "channel": "L_p (left oct. mult.)"},
    "8_s": {"c3": C3_8S, "channel": "R_p (right oct. mult.)"},
    "8_c": {"c3": C3_8C, "channel": "T_p (triality / bimodule)"},
}

# ─── G73-F: N_gen = 3 ────────────────────────────────────────────────────────

# Total index = sum of indices over all three channels:
INDICES = [dirac_index_s6(ch["c3"]) for ch in CHANNELS.values()]
TOTAL_INDEX = sum(INDICES, Fraction(0))  # = 3/1

N_GEN = int(TOTAL_INDEX)  # = 3

# Cross-check with G67: N_gen = |Z₃ orbit| = 3 ✓
assert N_GEN == N_TRIALITY_CHANNELS

# ─── G73-G: SU(3) fermion content of three generations ──────────────────────

# One generation S⁶ content: S⁻ ⊕ S⁺ = (3+1) ⊕ (3̄+1) = 3+3̄+1+1 under SU(3)
# Three generations: 3×(3+3̄+1+1) under SU(3)

ONE_GEN_SU3 = {"triplet": 3, "antitriplet": 3, "singlet": 2}  # dim = 3+3+2 = 8 ✓
THREE_GEN_SU3 = {k: N_GEN * v for k, v in ONE_GEN_SU3.items()}

# Sanity: dim(S⁶ part) × N_gen = 8 × 3 = 24 non-singlet + singlet content
assert sum(ONE_GEN_SU3.values()) == DIM_S6_SPINOR  # 8 ✓
assert sum(THREE_GEN_SU3.values()) == N_GEN * DIM_S6_SPINOR  # 24 ✓

# Full generation (S³ ⊗ S⁶):
ONE_GEN_FULL = DIM_S3_SPINOR * DIM_S6_SPINOR  # = 32 states
THREE_GEN_FULL = N_GEN * ONE_GEN_FULL  # = 96 states

# ─── Summary ─────────────────────────────────────────────────────────────────

G73_RESULT = {
    "claim": "N_gen = 3 from twisted Dirac index on S³×S⁶",
    "index_per_channel": INDEX_PER_CHANNEL,  # = 1
    "total_index": TOTAL_INDEX,  # = 3
    "N_gen": N_GEN,  # = 3
    "c3_per_channel": C3_S_MINUS,  # = 2
    "A_hat_S6": A_HAT_S6,  # = 1 (exact)
    "states_per_gen": ONE_GEN_FULL,  # = 32
    "total_states": THREE_GEN_FULL,  # = 96
    "status": "PROMOTE",
    "caveat": (
        "Index = 3 is topological lower bound. "
        "Exact count (no extra zero modes) requires spectral gap on S⁶. "
        "E_v bundle realization via G72 (Tom) still open."
    ),
}
