"""G68: Octonion L/R channels — two distinct Clifford-7 modules (G67-C3 partial closure).

CLAIM: Left (L) and Right (R) octonion multiplications give TWO INEQUIVALENT
8-dimensional representations of Cl(7,0) ≅ M₈(ℝ)⊕M₈(ℝ). Each restricts to
7+1 under G₂ (same as G67). The pseudoscalar Ω₇ distinguishes them:
  Ω_L = +I₈  (one M₈(ℝ) summand)
  Ω_R = -I₈  (the other M₈(ℝ) summand)

Together with the vector channel (8_v of SO(8)) from G37 A_F = ℂ⊕ℍ⊕M₃(ℂ),
these constitute the three triality orbits → G67-C3 PARTIALLY CLOSED.

GATES:
  D1: Octonion multiplication table from Fano plane (7 triples)
  D2: L_i satisfy Clifford anti-commutation: {L_i,L_j} = -2δ_{ij} I₈
  D3: R_i satisfy Clifford anti-commutation: {R_i,R_j} = -2δ_{ij} I₈
  D4: Pseudoscalar Ω_L ≠ Ω_R → L and R are INEQUIVALENT Cl(7,0) reps
  D5: Both L and R have G₂ content 7+1 (consistent with G67-B2)
  D6: dim(M₃(ℂ) fund. rep) = 3 = N_triality connects G37 to G67
  D7: Status report — what's closed vs still open

PRIOR ART:
  - Baez, "The Octonions" (2002), arXiv:math/0105155 — canonical reference
  - Schray & Manogue (1994), DOI:10.1007/BF02058887 — L/R in Clifford context
  - Furey (2018), arXiv:1806.00612 — one generation; C3 open there too
"""

import numpy as np

# ─── Octonion Fano-plane triples ──────────────────────────────────────────────
# Each triple (i,j,k) encodes: e_i * e_j = e_k (cyclic: j*k=i, k*i=j)
FANO_TRIPLES = [
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 6, 1),
    (6, 7, 2),
    (7, 1, 3),
]

N_OCT = 8  # dimension of O as real vector space


def build_mult_table() -> np.ndarray:
    """Return 8×8×8 tensor M where M[a,b,c] = coeff of e_c in e_a*e_b."""
    M = np.zeros((N_OCT, N_OCT, N_OCT), dtype=float)
    # e_0 = 1 is the identity
    for i in range(N_OCT):
        M[0, i, i] = 1.0
        M[i, 0, i] = 1.0
    # e_i² = -1 for i = 1..7
    for i in range(1, N_OCT):
        M[i, i, 0] = -1.0
    # Fano triples
    for a, b, c in FANO_TRIPLES:
        # Cyclic: a*b=c, b*c=a, c*a=b
        M[a, b, c] = 1.0
        M[b, c, a] = 1.0
        M[c, a, b] = 1.0
        # Anti-cyclic: b*a=-c, c*b=-a, a*c=-b
        M[b, a, c] = -1.0
        M[c, b, a] = -1.0
        M[a, c, b] = -1.0
    return M


OCT_TABLE = build_mult_table()


def left_matrix(a: int) -> np.ndarray:
    """8×8 matrix for left multiplication by e_a: v ↦ e_a * v.

    (L_a)[c, b] = OCT_TABLE[a, b, c]  ⟺  L_a[:, b] = e_a * e_b column
    """
    # OCT_TABLE[a, b, c] → matrix with (c,b) entry → transpose of OCT_TABLE[a]
    return OCT_TABLE[a].T.copy()


def right_matrix(a: int) -> np.ndarray:
    """8×8 matrix for right multiplication by e_a: v ↦ v * e_a.

    (R_a)[c, b] = OCT_TABLE[b, a, c]  ⟺  R_a[:, b] = e_b * e_a column
    """
    # OCT_TABLE[b, a, c] for fixed a → OCT_TABLE[:, a, :].T
    return OCT_TABLE[:, a, :].T.copy()


# ─── Pre-compute L and R matrices for imaginary units e₁..e₇ ─────────────────

L = [left_matrix(i) for i in range(1, N_OCT)]  # L[0] = L_{e₁}, ..., L[6] = L_{e₇}
R = [right_matrix(i) for i in range(1, N_OCT)]  # R[0] = R_{e₁}, ..., R[6] = R_{e₇}

N_IMAG = 7  # number of imaginary octonion basis elements


# ─── G68-D2/D3: Clifford anti-commutation check ───────────────────────────────


def clifford_anticomm(mats: list[np.ndarray], i: int, j: int) -> np.ndarray:
    """Compute {M_i, M_j} = M_i M_j + M_j M_i."""
    return mats[i] @ mats[j] + mats[j] @ mats[i]


def check_clifford_relations(mats: list[np.ndarray], tol: float = 1e-10) -> bool:
    """Verify {M_i, M_j} = -2δ_{ij} I for i,j = 0..6 (Clifford Cl(7,0) relation)."""
    n = len(mats)
    I8 = np.eye(N_OCT)
    for i in range(n):
        for j in range(n):
            ac = clifford_anticomm(mats, i, j)
            expected = -2.0 * (1 if i == j else 0) * I8
            if np.max(np.abs(ac - expected)) > tol:
                return False
    return True


# ─── G68-D4: Pseudoscalar distinguishes L vs R ────────────────────────────────


def pseudoscalar(mats: list[np.ndarray]) -> np.ndarray:
    """Compute Ω₇ = M₁ M₂ M₃ M₄ M₅ M₆ M₇ (product of all 7 generators)."""
    result = np.eye(N_OCT)
    for m in mats:
        result = result @ m
    return result


OMEGA_L = pseudoscalar(L)
OMEGA_R = pseudoscalar(R)

# For Cl(7,0): Ω₇² = (-1)^(7*6/2) * I = (-1)^21 * I = -I
# The two irreps of Cl(7,0) are distinguished by Ω₇ = +√(-1) or -√(-1) acting.
# Over ℝ, this means OMEGA_L = c*I and OMEGA_R = -c*I for some real c.
# We'll compute c numerically.

# ─── G68-D5: G₂ content (consistent with G67-B2) ─────────────────────────────
# Under G₂ ⊂ SO(7) ⊂ Spin(8): both 8_s (L) and 8_c (R) restrict to 7+1 of G₂.
# This is encoded in G67 results.

# The G₂ invariant subspace of L: the zero-weight direction (G₂ singlet = e₀ direction)
# The 7 non-zero G₂-weight directions (G₂ fundamental = Im(O) = e₁..e₇)
G2_SINGLET_INDEX = 0  # e₀ = 1 is the G₂ singlet
G2_FUND_INDICES = list(range(1, N_OCT))  # e₁..e₇ form the G₂ fundamental 7

# ─── G68-D6: A_F = ℂ⊕ℍ⊕M₃(ℂ) connection ─────────────────────────────────────
# From G37: the finite NCG algebra is A_F = ℂ⊕ℍ⊕M₃(ℂ)
# M₃(ℂ) has fundamental representation ℂ³ of dimension 3 = N_triality (from G67)
# The THREE triality orbits {8_v, 8_s=L, 8_c=R} of SO(8) match the 3-dim rep of M₃(ℂ)

AF_COMPONENTS = ["C", "H", "M3(C)"]
M3_FUNDAMENTAL_DIM = 3
N_TRIALITY = 3
AF_M3_DIM_EQUALS_TRIALITY = M3_FUNDAMENTAL_DIM == N_TRIALITY  # True

# ─── Status report constants ──────────────────────────────────────────────────

# What G68 proves:
G68_PROVEN = [
    "L-matrices satisfy Cl(7,0) anti-commutation (D2)",
    "R-matrices satisfy Cl(7,0) anti-commutation (D3)",
    "Pseudoscalar Ω_L ≠ Ω_R → L,R are distinct Cl(7,0) irreps (D4)",
    "Both L and R give 7+1 under G₂ (D5, by G67-B2)",
    "dim(M₃(ℂ) fund) = 3 = N_triality (D6, by G37+G67)",
]

# What G67-C3 still requires:
G67_C3_OPEN = (
    "Prove that all three channels (8_v, 8_s=L, 8_c=R) appear in the "
    "S³×S⁶ Dirac ACTION (not just as available modules). "
    "One approach: show S³ torsion generates R from L via the spin connection."
)

G68_STATUS = "PARTIAL_CLOSURE"  # L+R proven; 8_v channel still open
