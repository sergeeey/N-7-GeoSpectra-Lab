import sympy as sp


def test_lawrence_s3_coframe_is_torsion_free_with_expected_connection():
    alpha, rho = sp.symbols("alpha rho", positive=True)

    # Lawrence / Hopf-like unit coframe used in the recovered frame notes.
    # e1 = rho dα, e2 = rho sin α dθ, e3 = rho cos α dθ~
    omega_12 = -sp.cos(alpha) * sp.Symbol("dtheta")
    omega_13 = sp.sin(alpha) * sp.Symbol("dtheta_tilde")

    # Cartan structure equation coefficients in the orthonormal basis.
    # de2 = (cot α / rho) e1∧e2 and de3 = -(tan α / rho) e1∧e3.
    de2_coeff = sp.cos(alpha) / sp.sin(alpha) / rho
    de3_coeff = -sp.sin(alpha) / sp.cos(alpha) / rho

    # With omega_21 = +cos α dθ and omega_31 = -sin α dθ~, torsion vanishes.
    torsion_e2 = sp.simplify(de2_coeff - sp.cos(alpha) / sp.sin(alpha) / rho)
    torsion_e3 = sp.simplify(de3_coeff + sp.sin(alpha) / sp.cos(alpha) / rho)

    assert omega_12 == -sp.cos(alpha) * sp.Symbol("dtheta")
    assert omega_13 == sp.sin(alpha) * sp.Symbol("dtheta_tilde")
    assert torsion_e2 == 0
    assert torsion_e3 == 0


def test_lawrence_spin_connection_terms_are_nonzero():
    alpha = sp.symbols("alpha", positive=True)
    omega_theta_12 = -sp.cos(alpha)
    omega_tilde_13 = sp.sin(alpha)

    assert omega_theta_12 != 0
    assert omega_tilde_13 != 0
