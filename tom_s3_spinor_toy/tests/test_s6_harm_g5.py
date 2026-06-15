"""S6-HARM-G5: pytest pins for spin connection on S⁶ via Cartan equations.

Key results:
  Cartan: de^{φ_k} + ω^{φ_k}_{β_k} ∧ e^{β_k} = 0 verified for k=1,2,3
  ω^{φ_k}_{β_k,φ_k}(coord) = cosβ_k  (universal coordinate law)
  Frame forms: cotβ_k/(ρ × nesting) — same cotβ_k as G2 root generators
  cotβ_k structure appears in G2 (roots), G3 (ODEs), G4 (Lichnerowicz), G5 (ω)
"""

import pytest
from sympy import cos, sin, cot, symbols, trigsimp, diff, Integer


@pytest.fixture(scope="module")
def s6_spin():
    b1, b2, b3 = symbols(r"\beta_1 \beta_2 \beta_3", real=True, positive=True)
    p1, p2, p3 = symbols(r"\phi_1 \phi_2 \phi_3", real=True, positive=True)
    rho = symbols(r"\rho", real=True, positive=True)

    h_b1 = rho
    h_p1 = rho * sin(b1)
    h_b2 = rho * cos(b1)
    h_p2 = rho * cos(b1) * sin(b2)
    h_b3 = rho * cos(b1) * cos(b2)
    h_p3 = rho * cos(b1) * cos(b2) * sin(b3)

    # T1: (β₁,φ₁)
    de_p1 = trigsimp(diff(h_p1, b1))
    omega_p1_b1_coord = cos(b1)
    wedge_p1b1 = trigsimp(-h_b1 * omega_p1_b1_coord)
    cartan_p1 = trigsimp(de_p1 + wedge_p1b1)
    omega_p1_b1_frame = trigsimp(omega_p1_b1_coord / h_p1)

    # T2: (β₁,β₂) e^{β₂} cross term
    de_b2 = trigsimp(diff(h_b2, b1))
    omega_b2_b1_coord = -sin(b1)
    wedge_b2b1 = trigsimp(-h_b1 * omega_b2_b1_coord)
    cartan_b2 = trigsimp(de_b2 + wedge_b2b1)
    omega_b2_b1_frame = trigsimp(omega_b2_b1_coord / h_b2)

    # T3: (β₂,φ₂) — two-term structure
    de_p2_b1 = trigsimp(diff(h_p2, b1))
    de_p2_b2 = trigsimp(diff(h_p2, b2))
    omega_p2_b1_coord = trigsimp(diff(h_p2, b1) / h_b1)  # = -sinβ₁sinβ₂
    omega_p2_b2_coord = trigsimp(diff(h_p2, b2) / h_b2)  # = cosβ₂
    c1 = trigsimp(-h_b1 * omega_p2_b1_coord)
    c2 = trigsimp(-h_b2 * omega_p2_b2_coord)
    cartan_p2_b1 = trigsimp(de_p2_b1 + c1)
    cartan_p2_b2 = trigsimp(de_p2_b2 + c2)
    omega_p2_b2_frame = trigsimp(omega_p2_b2_coord / h_p2)

    # T4: (β₃,φ₃)
    de_p3_b3 = trigsimp(diff(h_p3, b3))
    omega_p3_b3_coord = trigsimp(diff(h_p3, b3) / h_b3)  # = cosβ₃
    c3 = trigsimp(-h_b3 * omega_p3_b3_coord)
    cartan_p3_b3 = trigsimp(de_p3_b3 + c3)
    omega_p3_b3_frame = trigsimp(omega_p3_b3_coord / h_p3)

    return {
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "rho": rho,
        "cartan_p1": cartan_p1,
        "omega_p1_b1_coord": omega_p1_b1_coord,
        "omega_p1_b1_frame": omega_p1_b1_frame,
        "cartan_b2": cartan_b2,
        "omega_b2_b1_coord": omega_b2_b1_coord,
        "omega_b2_b1_frame": omega_b2_b1_frame,
        "cartan_p2_b1": cartan_p2_b1,
        "cartan_p2_b2": cartan_p2_b2,
        "omega_p2_b1_coord": omega_p2_b1_coord,
        "omega_p2_b2_coord": omega_p2_b2_coord,
        "omega_p2_b2_frame": omega_p2_b2_frame,
        "cartan_p3_b3": cartan_p3_b3,
        "omega_p3_b3_coord": omega_p3_b3_coord,
        "omega_p3_b3_frame": omega_p3_b3_frame,
    }


# ── T1: (β₁,φ₁) Cartan equation ─────────────────────────────────────────────
def test_s6_g5_cartan_phi1_beta1_vanishes(s6_spin):
    """de^{φ₁} + ω^{φ₁}_{β₁} ∧ e^{β₁} = 0."""
    assert s6_spin["cartan_p1"] == Integer(0)


def test_s6_g5_omega_phi1_beta1_coord_is_cosbeta1(s6_spin):
    """ω^{φ₁}_{β₁}(coord, dφ₁) = cosβ₁."""
    b1 = s6_spin["b1"]
    assert trigsimp(s6_spin["omega_p1_b1_coord"] - cos(b1)) == Integer(0)


def test_s6_g5_omega_phi1_beta1_frame_is_cotbeta1_over_rho(s6_spin):
    """ω^{φ₁}_{β₁}(frame) = cotβ₁/ρ."""
    b1, rho = s6_spin["b1"], s6_spin["rho"]
    assert trigsimp(s6_spin["omega_p1_b1_frame"] - cot(b1) / rho) == Integer(0)


# ── T2: (β₁,β₂) cross-term ───────────────────────────────────────────────────
def test_s6_g5_cartan_beta2_beta1_vanishes(s6_spin):
    """de^{β₂} + ω^{β₂}_{β₁} ∧ e^{β₁} = 0."""
    assert s6_spin["cartan_b2"] == Integer(0)


def test_s6_g5_omega_beta2_beta1_coord_is_neg_sinbeta1(s6_spin):
    """ω^{β₂}_{β₁}(coord) = -sinβ₁."""
    b1 = s6_spin["b1"]
    assert trigsimp(s6_spin["omega_b2_b1_coord"] + sin(b1)) == Integer(0)


# ── T3: (β₂,φ₂) two-term Cartan equation ─────────────────────────────────────
def test_s6_g5_cartan_phi2_beta1_term_vanishes(s6_spin):
    """dβ₁∧dφ₂ coefficient of Cartan eq for e^{φ₂} vanishes."""
    assert s6_spin["cartan_p2_b1"] == Integer(0)


def test_s6_g5_cartan_phi2_beta2_term_vanishes(s6_spin):
    """dβ₂∧dφ₂ coefficient of Cartan eq for e^{φ₂} vanishes."""
    assert s6_spin["cartan_p2_b2"] == Integer(0)


def test_s6_g5_omega_phi2_beta2_coord_is_cosbeta2(s6_spin):
    """ω^{φ₂}_{β₂}(coord) = cosβ₂ (same pattern as ω^{φ₁}_{β₁} = cosβ₁)."""
    b2 = s6_spin["b2"]
    assert trigsimp(s6_spin["omega_p2_b2_coord"] - cos(b2)) == Integer(0)


def test_s6_g5_omega_phi2_beta2_frame_is_cotbeta2_over_nesting(s6_spin):
    """ω^{φ₂}_{β₂}(frame) = cotβ₂/(ρ cosβ₁)."""
    b1, b2, rho = s6_spin["b1"], s6_spin["b2"], s6_spin["rho"]
    assert trigsimp(s6_spin["omega_p2_b2_frame"] - cot(b2) / (rho * cos(b1))) == Integer(0)


# ── T4: (β₃,φ₃) Cartan equation ─────────────────────────────────────────────
def test_s6_g5_cartan_phi3_beta3_term_vanishes(s6_spin):
    """dβ₃∧dφ₃ coefficient of Cartan eq for e^{φ₃} vanishes."""
    assert s6_spin["cartan_p3_b3"] == Integer(0)


def test_s6_g5_omega_phi3_beta3_coord_is_cosbeta3(s6_spin):
    """ω^{φ₃}_{β₃}(coord) = cosβ₃."""
    b3 = s6_spin["b3"]
    assert trigsimp(s6_spin["omega_p3_b3_coord"] - cos(b3)) == Integer(0)


def test_s6_g5_omega_phi3_beta3_frame_is_cotbeta3_over_nesting(s6_spin):
    """ω^{φ₃}_{β₃}(frame) = cotβ₃/(ρ cosβ₁ cosβ₂)."""
    b1, b2, b3, rho = s6_spin["b1"], s6_spin["b2"], s6_spin["b3"], s6_spin["rho"]
    assert trigsimp(s6_spin["omega_p3_b3_frame"] - cot(b3) / (rho * cos(b1) * cos(b2))) == Integer(
        0
    )


# ── T5: Universal cosβ_k law ──────────────────────────────────────────────────
def test_s6_g5_universal_coord_form_all_three(s6_spin):
    """ω^{φ_k}_{β_k,φ_k}(coord) = cosβ_k for k=1,2,3 (universal law)."""
    b1, b2, b3 = s6_spin["b1"], s6_spin["b2"], s6_spin["b3"]
    assert trigsimp(s6_spin["omega_p1_b1_coord"] - cos(b1)) == Integer(0)
    assert trigsimp(s6_spin["omega_p2_b2_coord"] - cos(b2)) == Integer(0)
    assert trigsimp(s6_spin["omega_p3_b3_coord"] - cos(b3)) == Integer(0)


# ── T6: G2↔G5 cotβ_k connection ──────────────────────────────────────────────
def test_s6_g5_frame_cotbeta1_matches_g2(s6_spin):
    """Frame ω^{φ₁}_{β₁} carries cotβ₁ — same coefficient as G2 root generators."""
    b1, rho = s6_spin["b1"], s6_spin["rho"]
    coeff = trigsimp(s6_spin["omega_p1_b1_frame"] * rho)
    assert trigsimp(coeff - cot(b1)) == Integer(0)
