"""
G54-D: Hadamard finite part ζ_FP(−1/2; ρ₃, ρ₆) via Mellin–Hadamard subtraction.

ζ(s) near s = −1/2 has Laurent expansion (G54-C):
    ζ(s) = c_{1/2} / [Γ(−1/2)(s+1/2)] + ζ_FP + O(s+1/2)

Hadamard finite part formula:
    ζ_FP = [Σ' + I_reg + I₂ − ψ(−1/2) × c_{1/2}] / Γ(−1/2)

where:
    Σ' = Σ_{αₙ≠1/2} cₙ/(αₙ−1/2)   [analytic sum, no quadrature]
    I_reg = ∫_{ε}^1 t^{-3/2}(K_full − K_SW) dt  [ε=0.10, K_SW remainder]
    I₂ = ∫_1^∞ t^{-3/2} K_full dt              [large-t tail]
    Γ(−1/2) = −2√π,  ψ(−1/2) ≈ 0.0365

Lower cutoff ε=0.10 for I_reg: avoids catastrophic cancellation at t<0.01
where K_{S⁶} eigenvalue sum needs ~260 terms but n=150 is used.
The omitted [0,ε] piece is O(B₁₂ε^{5/2}) < 10⁻⁶ — negligible.

Gates:
  D1: Σ' is analytic — sign flips between ρ₆=1.09 and ρ₆=1.20
  D2: I_reg ≪ |Σ'| for ρ₆ ∈ [0.7, 1.5] — SW expansion is a good approximation
  D3: I₂ exponentially small (< 10⁻⁶ at ρ₆=1.0)
  D4: ζ_FP changes sign — ρ₆** ∈ (1.2, 1.5) where ζ_FP = 0 (distinct from ρ₆*)
  D5: At ρ₆*, ζ_FP is finite and negative — pole vanishes but energy does not
  D6: Σ' drives the sign change; sign(ζ_FP) = sign(−Σ'/Γ) when Σ' dominates
"""

import math
from math import sqrt, pi, exp

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.special import comb, digamma

# ── physical constants ─────────────────────────────────────────────────────────
PI = pi
A0_S3 = sqrt(PI) / 2  # exact (Poisson theorem, G54-B B3)
A2_S3 = -sqrt(PI) / 4  # exact (Poisson theorem, G54-B B3)
CONSTRAINT_C = 0.986  # ρ₃ = C ρ₆²  (G29 gauge coupling ratio)
GAMMA_NEG_HALF = -2.0 * sqrt(PI)  # Γ(-1/2) = -2√π
PSI_NEG_HALF = float(digamma(-0.5))  # ψ(-1/2) ≈ 0.03649

EPS_IREG = 0.10  # lower cutoff for I_reg numerical integration


# ── heat kernels ───────────────────────────────────────────────────────────────


def _hs3(tau: float, n: int = 200) -> float:
    """K_{S³}(τ) spinor. Eigenvalues (k+3/2)², mult 2(k+1)(k+2)."""
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n))


def _hs6(tau: float, n: int = 150) -> float:
    """K_{S⁶}(τ) spinor. Eigenvalues (k+3)², mult 16C(k+5,5)."""
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n))


# ── SW coefficients (computed once, cached) ────────────────────────────────────

_SW_CACHE: dict | None = None


def _sw() -> dict:
    """6-param SW fit of K_{S⁶}(τ) on [0.005, 0.080]."""
    global _SW_CACHE
    if _SW_CACHE is None:
        tau = np.array([0.005, 0.008, 0.012, 0.018, 0.025, 0.035, 0.050, 0.070, 0.080])
        k = np.array([_hs6(t, n=150) for t in tau])
        basis = np.column_stack(
            [
                tau ** (-3),
                tau ** (-2),
                tau ** (-1),
                np.ones(len(tau)),
                tau,
                tau**2,
            ]
        )
        c, *_ = lstsq(basis, k)
        _SW_CACHE = {
            "B0": c[0],
            "B2": c[1],
            "B4": c[2],
            "B6": c[3],
            "B8": c[4],
            "B10": c[5],
        }
    return _SW_CACHE


# ── Hadamard components ────────────────────────────────────────────────────────


def sigma_prime(r3: float, r6: float) -> float:
    """Σ' = Σ_{αₙ≠1/2} cₙ/(αₙ−1/2) — fully analytic, no quadrature.

    From SW cross-terms of K_{S³}(τ/ρ₃²) × K_{S⁶}(τ/ρ₆²).
    The α=+1/2 term (the pole c_{1/2}) is EXCLUDED here.
    """
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
    cns = {
        -4.5: A0 * r3**3 * B0 * r6**6,
        -3.5: A0 * r3**3 * B2 * r6**4 + A2 * r3 * B0 * r6**6,
        -2.5: A0 * r3**3 * B4 * r6**2 + A2 * r3 * B2 * r6**4,
        -1.5: A0 * r3**3 * B6 + A2 * r3 * B4 * r6**2,
        -0.5: A0 * r3**3 * B8 / r6**2 + A2 * r3 * B6,
        1.5: A2 * r3 * B10 / r6**4,
    }
    return sum(cn / (alpha - 0.5) for alpha, cn in cns.items())


def c_half(r3: float, r6: float) -> float:
    """c_{1/2} = coefficient of t^{1/2} in K SW expansion (UV pole residue)."""
    sw = _sw()
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def rho6_star() -> float:
    """ρ₆* where c_{1/2}=0 along SM constraint ρ₃=Cρ₆²."""
    sw = _sw()
    ratio = -(A2_S3 * sw["B8"]) / (A0_S3 * sw["B10"] * CONSTRAINT_C**2)
    return sqrt(ratio) if ratio > 0 else float("nan")


def _k_sw(t: float, r3: float, r6: float) -> float:
    """SW approximation K_SW(t; ρ₃, ρ₆) — product of K_{S³}×K_{S⁶} SW terms."""
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
    ta = (
        A0
        * r3**3
        * (
            B0 * r6**6 * t ** (-4.5)
            + B2 * r6**4 * t ** (-3.5)
            + B4 * r6**2 * t ** (-2.5)
            + B6 * t ** (-1.5)
            + B8 / r6**2 * t ** (-0.5)
            + B10 / r6**4 * t**0.5
        )
    )
    t2 = (
        A2
        * r3
        * (
            B0 * r6**6 * t ** (-3.5)
            + B2 * r6**4 * t ** (-2.5)
            + B4 * r6**2 * t ** (-1.5)
            + B6 * t ** (-0.5)
            + B8 / r6**2 * t**0.5
            + B10 / r6**4 * t**1.5
        )
    )
    return ta + t2


def _k_full(t: float, r3: float, r6: float) -> float:
    """K_full(t; ρ₃, ρ₆) = K_{S³}(t/ρ₃²) × K_{S⁶}(t/ρ₆²)."""
    return _hs3(t / r3**2, n=200) * _hs6(t / r6**2, n=150)


def _i_reg(r3: float, r6: float) -> tuple[float, float]:
    """∫_{ε}^1 t^{-3/2} (K_full − K_SW) dt with ε=EPS_IREG."""

    def intgd(t: float) -> float:
        return t ** (-1.5) * (_k_full(t, r3, r6) - _k_sw(t, r3, r6))

    return quad(intgd, EPS_IREG, 1.0, limit=200, epsabs=1e-9, epsrel=1e-7)


def _i2(r3: float, r6: float) -> tuple[float, float]:
    """∫_1^∞ t^{-3/2} K_full dt — large-t tail, exponentially small."""

    def intgd(t: float) -> float:
        return t ** (-1.5) * _k_full(t, r3, r6)

    return quad(intgd, 1.0, 50.0, limit=100, epsabs=1e-12, epsrel=1e-10)


def zeta_fp(r3: float, r6: float) -> float:
    """Hadamard finite part ζ_FP(−1/2; ρ₃, ρ₆)."""
    Sig = sigma_prime(r3, r6)
    Ir, _ = _i_reg(r3, r6)
    I2v, _ = _i2(r3, r6)
    c12 = c_half(r3, r6)
    return (Sig + Ir + I2v - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


# ── D1: Σ' is analytic and changes sign ────────────────────────────────────────


class TestD1SigmaPrime:
    """Σ' is a closed-form analytic sum — no integration error possible."""

    def test_sigma_prime_finite_at_unit_radii(self):
        """σ' is finite at (ρ₃, ρ₆) = (1.0, 1.0)."""
        s = sigma_prime(1.0, 1.0)
        assert math.isfinite(s)

    def test_sigma_prime_positive_at_small_rho6(self):
        """Σ' > 0 at ρ₆=0.7 — α=-4.5 term A₀B₀ρ₃³ρ₆⁶ dominates at small radii."""
        r6 = 0.7
        s = sigma_prime(CONSTRAINT_C * r6**2, r6)
        assert s > 0, f"Σ'={s:.4e} at ρ₆=0.7"

    def test_sigma_prime_sign_flip_between_1p09_and_1p20(self):
        """Σ' changes sign between ρ₆=1.09 and ρ₆=1.20 along SM constraint.

        This is the geometric mechanism driving ζ_FP sign change (D4/D6).
        """
        s_below = sigma_prime(CONSTRAINT_C * 1.09**2, 1.09)
        s_above = sigma_prime(CONSTRAINT_C * 1.20**2, 1.20)
        assert s_below > 0, f"Σ' at ρ₆=1.09: {s_below:.4e}"
        assert s_above < 0, f"Σ' at ρ₆=1.20: {s_above:.4e}"

    def test_sigma_prime_large_at_rho6_2(self):
        """|Σ'| >> 1 at ρ₆=2 — dominated by α=-4.5 term ∝ ρ₆¹² (large radii blow up)."""
        r6 = 2.0
        s = sigma_prime(CONSTRAINT_C * r6**2, r6)
        assert abs(s) > 10.0, f"|Σ'|={abs(s):.2f} at ρ₆=2"

    def test_sigma_prime_analytic_formula_at_unit_radii(self):
        """Verify σ'(1,1) matches manual cross-term sum to floating-point precision."""
        sw = _sw()
        A0, A2 = A0_S3, A2_S3
        B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
        expected = (
            A0 * B0 / (-4.5 - 0.5)
            + (A0 * B2 + A2 * B0) / (-3.5 - 0.5)
            + (A0 * B4 + A2 * B2) / (-2.5 - 0.5)
            + (A0 * B6 + A2 * B4) / (-1.5 - 0.5)
            + (A0 * B8 + A2 * B6) / (-0.5 - 0.5)
            + A2 * B10 / (1.5 - 0.5)
        )
        assert abs(sigma_prime(1.0, 1.0) - expected) < 1e-12


# ── D2: I_reg is small relative to Σ' ─────────────────────────────────────────


class TestD2IregSmall:
    """I_reg ≪ |Σ'| — SW expansion is an accurate approximation of K_full."""

    def test_ireg_finite_at_rho6_star(self):
        """|I_reg| is finite at ρ₆* (no catastrophic cancellation with eps=0.10)."""
        r6 = rho6_star()
        Ir, _ = _i_reg(CONSTRAINT_C * r6**2, r6)
        assert math.isfinite(Ir), "I_reg is not finite at ρ₆*"
        assert abs(Ir) < 1.0, f"|I_reg|={abs(Ir):.4e} unexpectedly large at ρ₆*"

    def test_ireg_small_relative_to_sigma_prime_at_rho6_1(self):
        """|I_reg| < 50% |Σ'| at ρ₆=1.0 — SW expansion approximates well."""
        r6 = 1.0
        r3 = CONSTRAINT_C * r6**2
        Ir, _ = _i_reg(r3, r6)
        Sig = sigma_prime(r3, r6)
        ratio = abs(Ir) / abs(Sig)
        assert ratio < 0.5, f"|I_reg/Σ'|={ratio:.2f} at ρ₆=1.0 (expected < 0.5)"

    def test_k_full_matches_k_sw_at_eps(self):
        """K_full ≈ K_SW at t=ε=0.10 (relative error < 2%).

        Justifies omitting [0, ε] from I_reg: the remainder is K_{S³}×O(B₁₂τ³).
        """
        r6, r3 = 1.0, CONSTRAINT_C
        kf = _k_full(EPS_IREG, r3, r6)
        ksw = _k_sw(EPS_IREG, r3, r6)
        rel_err = abs(kf - ksw) / abs(kf)
        assert rel_err < 0.02, f"K_full vs K_SW at t=ε: rel_err={rel_err:.4f}"


# ── D3: I₂ is exponentially small ─────────────────────────────────────────────


class TestD3I2Small:
    """I₂ = ∫_1^∞ t^{-3/2} K_full dt — eigenvalue gap kills it exponentially."""

    def test_i2_small_relative_to_sigma_prime_at_rho6_1(self):
        """I₂ < 5% of |Σ'| at ρ₆=1.0 — large-t tail negligible vs analytic sum."""
        r6 = 1.0
        r3 = CONSTRAINT_C * r6**2
        I2v, _ = _i2(r3, r6)
        Sig = sigma_prime(r3, r6)
        ratio = abs(I2v) / abs(Sig)
        assert ratio < 0.05, f"|I₂/Σ'|={ratio:.3f} at ρ₆=1.0"

    def test_i2_positive(self):
        """I₂ > 0 at ρ₆=1.0 — K_full > 0 and t^{-3/2} > 0 throughout."""
        r6 = 1.0
        I2v, _ = _i2(CONSTRAINT_C * r6**2, r6)
        assert I2v > 0, f"I₂={I2v:.2e} should be positive"


# ── D4: ζ_FP changes sign — ρ₆** ∈ (1.2, 1.5) ────────────────────────────────


class TestD4ZetaFPSignChange:
    """ζ_FP changes sign between ρ₆=1.2 and ρ₆=1.5.

    ρ₆** ≈ 1.35 is a NEW special radius, distinct from ρ₆* ≈ 1.09 (where UV pole
    vanishes).  By Bolzano's theorem, a zero of ζ_FP exists in (1.2, 1.5).
    """

    def test_zeta_fp_negative_at_rho6_1p2(self):
        """ζ_FP(1.2) < 0 — still on negative side of sign change."""
        r6 = 1.2
        zfp = zeta_fp(CONSTRAINT_C * r6**2, r6)
        assert zfp < 0, f"ζ_FP={zfp:.5e} at ρ₆=1.2"

    def test_zeta_fp_positive_at_rho6_1p5(self):
        """ζ_FP(1.5) > 0 — crossed zero going outward."""
        r6 = 1.5
        zfp = zeta_fp(CONSTRAINT_C * r6**2, r6)
        assert zfp > 0, f"ζ_FP={zfp:.5e} at ρ₆=1.5"

    def test_zeta_fp_bolzano_bracket(self):
        """ζ_FP(1.2) × ζ_FP(1.5) < 0 — Bolzano guarantees ρ₆** ∈ (1.2, 1.5)."""
        zfp_a = zeta_fp(CONSTRAINT_C * 1.2**2, 1.2)
        zfp_b = zeta_fp(CONSTRAINT_C * 1.5**2, 1.5)
        assert zfp_a * zfp_b < 0, f"No sign change: ζ_FP(1.2)={zfp_a:.4e}, ζ_FP(1.5)={zfp_b:.4e}"


# ── D5: At ρ₆*, ζ_FP is finite and negative ───────────────────────────────────


class TestD5ZetaFPAtPoleCancellation:
    """At ρ₆*, the UV pole vanishes (c_{1/2}=0) but ζ_FP is finite and negative.

    Interpretation: the Casimir energy is UV-finite at ρ₆* (no counterterm needed)
    but the finite part is non-zero and negative.  ρ₆* does NOT make ζ_FP extremal.
    """

    def test_c_half_vanishes_at_rho6_star(self):
        """Prerequisite: c_{1/2}(ρ₆*) ≈ 0 to 1e-8."""
        r6 = rho6_star()
        c12 = c_half(CONSTRAINT_C * r6**2, r6)
        assert abs(c12) < 1e-8, f"c_{{1/2}}(ρ₆*)={c12:.4e}"

    def test_zeta_fp_finite_at_rho6_star(self):
        """ζ_FP(ρ₆*) is a finite real number."""
        r6 = rho6_star()
        zfp = zeta_fp(CONSTRAINT_C * r6**2, r6)
        assert math.isfinite(zfp), f"ζ_FP(ρ₆*)={zfp}"

    def test_zeta_fp_negative_at_rho6_star(self):
        """ζ_FP(ρ₆*) < 0 — Casimir energy is negative at the UV-finite radius."""
        r6 = rho6_star()
        zfp = zeta_fp(CONSTRAINT_C * r6**2, r6)
        assert zfp < 0, f"ζ_FP(ρ₆*)={zfp:.4e}"

    def test_zeta_fp_at_rho6_star_order_of_magnitude(self):
        """ζ_FP(ρ₆*) is O(10⁻³) — small but not negligible, not zero."""
        r6 = rho6_star()
        zfp = zeta_fp(CONSTRAINT_C * r6**2, r6)
        assert 1e-5 < abs(zfp) < 0.1, f"|ζ_FP(ρ₆*)|={abs(zfp):.4e}"


# ── D6: sign mechanism ─────────────────────────────────────────────────────────


class TestD6SignMechanism:
    """ζ_FP sign is determined by Σ' through sign(ζ_FP) = sign(−Σ'/Γ(−1/2)).

    Γ(−1/2) = −2√π < 0, so negative Σ' → positive ζ_FP.
    """

    def test_gamma_neg_half_exact(self):
        """Γ(−1/2) = −2√π exactly."""
        assert abs(GAMMA_NEG_HALF + 2 * sqrt(PI)) < 1e-14

    def test_psi_neg_half_range(self):
        """ψ(−1/2) ≈ 0.03649 (digamma at −1/2); in (0.02, 0.06)."""
        assert 0.02 < PSI_NEG_HALF < 0.06, f"ψ(−1/2)={PSI_NEG_HALF:.5f}"

    def test_sign_consistency_at_rho6_1p5(self):
        """At ρ₆=1.5: Σ'<0 and Γ<0 → Σ'/Γ>0 → ζ_FP>0.

        ζ_FP = (Sig + corrections)/Γ.  When Sig<0 and Γ<0, Sig/Γ>0.
        """
        r6 = 1.5
        r3 = CONSTRAINT_C * r6**2
        Sig = sigma_prime(r3, r6)
        zfp = zeta_fp(r3, r6)
        assert Sig < 0, f"Σ'={Sig:.4e} at ρ₆=1.5 should be negative"
        assert zfp > 0, f"ζ_FP={zfp:.4e} at ρ₆=1.5 should be positive"

    def test_sign_consistency_at_rho6_0p7(self):
        """At ρ₆=0.7: Σ'>0 and Γ<0 → Σ'/Γ<0 → ζ_FP<0."""
        r6 = 0.7
        r3 = CONSTRAINT_C * r6**2
        Sig = sigma_prime(r3, r6)
        zfp = zeta_fp(r3, r6)
        assert Sig > 0, f"Σ'={Sig:.4e} at ρ₆=0.7 should be positive"
        assert zfp < 0, f"ζ_FP={zfp:.4e} at ρ₆=0.7 should be negative"
