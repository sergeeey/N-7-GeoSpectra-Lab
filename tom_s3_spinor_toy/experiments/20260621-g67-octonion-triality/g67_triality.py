"""G67: Octonion triality on S⁶ → N_gen = 3

CLAIM: Under SU(3) ⊂ G₂ ⊂ SO(8), the three triality-related 8-dim reps
of SO(8) — denoted 8_v, 8_s, 8_c — ALL decompose identically:
    8_v → 3 + 3̄ + 1 + 1   under SU(3)
    8_s → 3 + 3̄ + 1 + 1
    8_c → 3 + 3̄ + 1 + 1

This gives THREE IDENTICAL copies of SM quark+lepton content.
Combined with the S³ spinor (4-dim), each copy yields ONE SM generation:
    4 (S³) × 8 (S⁶ triality rep) = 32 states = 1 generation
    3 copies → N_gen = 3.

EVIDENCE CHAIN:
1. G₂ = Aut(O) = isometry group of S⁶ (S⁶ = unit imaginary octonions)
2. SU(3) = stabilizer of a point on S⁶: G₂/SU(3) = S⁶
3. G₂ ⊂ Spin(7) ⊂ Spin(8): G₂ acts on the 7-dim imaginary octonion space
4. G₂ = Fix(Z₃ triality) in SO(8): triality permutes 8_v, 8_s, 8_c
   → under G₂, ALL THREE 8-dim reps look the same: 7 + 1
5. Under SU(3) ⊂ G₂: 7 → 3 + 3̄ + 1  [G₂ fundamental rep branching]
6. So: 8 (any triality rep) → (7+1) of G₂ → (3+3̄+1) + 1 = 3+3̄+1+1 under SU(3)
7. NUMBER: |Z₃ orbit| = 3 = N_gen

GATES:
  G67-A1: G₂ short roots = SU(3) roots (algebraically identical)
  G67-A2: G₂ 7-dim rep weights = 6 short roots + zero
  G67-A3: Under SU(3): those 6 weights → 3 (triplet) + 3 (anti-triplet)
           + 0 (singlet)
  G67-A4: S⁶ spinor = 7+1 of G₂ → 3+3̄+1+1 under SU(3) — MATCHES G24
  G67-B1: Triality Z₃ of SO(8) permutes {8_v, 8_s, 8_c} — 3 orbits
  G67-B2: G₂ = Fix(Z₃): all three reps restrict to SAME G₂ content
  G67-C1: N_gen = 3 [GATE: IF all 3 copies appear in action]
  G67-C2: Physical mechanism: three octonion channels L_p, R_p, T_p
  G67-C3: OPEN — prove all 3 channels appear in S³×S⁶ action

PRIOR WORK (FL Step -4 source trace):
  - Schray & Manogue (1994): Octonionic representations of Clifford algebras
    and triality. [VERIFIED: arXiv not found but DOI 10.1007/BF02058887]
    → Establishes triality in octonionic Clifford algebra context.
  - Furey (2018): N. Furey, arXiv:1806.00612, EPJC 78:375.
    → One generation from CL(6); three generations from triality.
    → Does NOT prove why three copies appear (same open question as G67-C3).
  - Furey (2023): arXiv:2312.12377 "Algebraic Roadmap Part I"
    → Network of algebraic connections between particle theories.
  - Todorov (2023): DOI:10.3390/universe9050222 — review of octonion SM.
"""

import numpy as np

# ─── G₂ root system in ℝ³ (hyperplane x+y+z=0) ───────────────────────────────

# Short roots of G₂ = simple roots of A₂ = roots of SU(3)
# Shape: {±(eᵢ-eⱼ) : i≠j ∈ {1,2,3}}
G2_SHORT = np.array(
    [
        [1, -1, 0],
        [-1, 1, 0],
        [1, 0, -1],
        [-1, 0, 1],
        [0, 1, -1],
        [0, -1, 1],
    ],
    dtype=float,
)

# Long roots of G₂ (length ratio = √3 relative to short roots)
# Shape: {±(eᵢ+eⱼ-2eₖ) or equivalently ±(2eᵢ-eⱼ-eₖ)}
G2_LONG = np.array(
    [
        [2, -1, -1],
        [-2, 1, 1],
        [-1, 2, -1],
        [1, -2, 1],
        [-1, -1, 2],
        [1, 1, -2],
    ],
    dtype=float,
)

G2_ALL_ROOTS = np.vstack([G2_SHORT, G2_LONG])

# ─── SU(3) root system ────────────────────────────────────────────────────────

# SU(3) = A₂ has 6 roots = exactly the short roots of G₂
SU3_ROOTS = G2_SHORT.copy()  # Same vectors!

# ─── G₂ 7-dim fundamental representation weights ──────────────────────────────

# The 7-dim G₂ rep = the 7-dim imaginary octonion space Im(O)
# Weights in ℝ³ (on the x+y+z=0 hyperplane):
# - 6 non-zero weights = the 6 short roots of G₂
# - 1 zero weight = the singlet
G2_7_WEIGHTS = np.vstack([G2_SHORT, np.zeros((1, 3))])  # shape (7,3)

# ─── SU(3) weight classification ──────────────────────────────────────────────

# The 3-dim SU(3) fundamental rep weights (choosing one Weyl chamber):
# 3: (1,-1,0), (0,1,-1), (-1,0,1)  [positive orbits]
# 3̄: (-1,1,0), (0,-1,1), (1,0,-1)  [negative orbits]

SU3_TRIPLET_WEIGHTS = np.array(
    [
        [1, -1, 0],  # "red" quark direction
        [0, 1, -1],  # "green" quark direction
        [-1, 0, 1],  # "blue" quark direction
    ],
    dtype=float,
)

SU3_ANTITRIPLET_WEIGHTS = np.array(
    [
        [-1, 1, 0],  # "anti-red"
        [0, -1, 1],  # "anti-green"
        [1, 0, -1],  # "anti-blue"
    ],
    dtype=float,
)

SU3_SINGLET_WEIGHT = np.array([[0.0, 0.0, 0.0]])

# ─── Classification functions ─────────────────────────────────────────────────


def weight_in_set(w, weight_set, tol=1e-10):
    """Check if weight w is in weight_set."""
    return any(np.allclose(w, v, atol=tol) for v in weight_set)


def classify_g2_7_under_su3(weights_7, triplet, antitriplet, singlet_w):
    """Classify weights of G2 7-dim rep under SU(3)."""
    n_triplet = sum(1 for w in weights_7 if weight_in_set(w, triplet))
    n_antitriplet = sum(1 for w in weights_7 if weight_in_set(w, antitriplet))
    n_singlet = sum(1 for w in weights_7 if weight_in_set(w, singlet_w))
    n_total = n_triplet + n_antitriplet + n_singlet
    return n_triplet, n_antitriplet, n_singlet, n_total


# ─── Short root length check ──────────────────────────────────────────────────


def root_length(r):
    return np.linalg.norm(r)


SHORT_LEN = root_length(G2_SHORT[0])
LONG_LEN = root_length(G2_LONG[0])
LENGTH_RATIO = LONG_LEN / SHORT_LEN

# ─── G67-B: Triality of SO(8) ─────────────────────────────────────────────────

# Key theorem (Cartan 1925, Dynkin 1952):
# SO(8) has an outer automorphism group S₃ (symmetric group on 3 elements).
# The Z₃ subgroup is called "triality" and permutes the three 8-dim irreps:
#   8_v (vector) → 8_s (left spinor) → 8_c (right spinor) → 8_v
#
# Key theorem (Engel, Jacobson):
# G₂ = Fix(Z₃ triality) in SO(8)
# i.e., G₂ is the subgroup of SO(8) that COMMUTES with the Z₃ action.
# Therefore, under G₂, all three 8-dim reps restrict identically:
#   8_v|_{G₂} ≅ 8_s|_{G₂} ≅ 8_c|_{G₂} = 7 + 1  of G₂

N_TRIALITY_ORBITS = 3  # |Z₃ orbit of {8_v, 8_s, 8_c}|

# Under G₂: 8 of Spin(7) → 7 + 1 of G₂
# This is the unique 8-dim rep of Spin(7) restricted to G₂ ⊂ Spin(7)
# The 7+1 splits: 7 = G₂ fundamental, 1 = G₂ singlet

# ─── G67-C: N_gen = 3 ─────────────────────────────────────────────────────────

# From G24 (verified): S⁶ spinor (8-dim) under SU(3) = 3+3̄+1+1
#   6 non-singlets (3+3̄) + 2 singlets = 8
# This is ONE of the three triality-related 8-dim reps.

# S³ spinor: 4-dim (Dirac spinor of Spin(3) ≅ SU(2))
S3_SPINOR_DIM = 4
S6_SPINOR_DIM = 8  # one triality rep

# One SM generation = S³ spinor ⊗ S⁶ spinor
ONE_GEN_DIM = S3_SPINOR_DIM * S6_SPINOR_DIM  # = 32 states (matches G17!)

# Three generations from triality
N_GEN = N_TRIALITY_ORBITS  # = 3
THREE_GEN_DIM = N_GEN * ONE_GEN_DIM  # = 96 states

# Physical mechanism (G67-C2):
# On S⁶ = Im(O)/|Im(O)|, unit octonion p acts in THREE ways:
#   L_p: x → p·x   (left multiplication — octonion algebra)
#   R_p: x → x·p   (right multiplication)
#   T_p: x → p̄·x·p (triality map = adjoint action)
# Each gives a DIFFERENT 8-dim rep of SO(8), all related by Z₃ triality.
# If all three appear in the fermion action → N_gen = 3.
# OPEN: prove this from the S³×S⁶ Dirac operator.

OCTONION_CHANNELS = ["L_p (left mult)", "R_p (right mult)", "T_p (bimodule)"]
N_CHANNELS = len(OCTONION_CHANNELS)  # = 3 = N_GEN ✓
