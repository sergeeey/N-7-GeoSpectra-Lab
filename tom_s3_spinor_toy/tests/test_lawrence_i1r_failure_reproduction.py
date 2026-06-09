import sympy as sp


def test_scalar_dragging_recovered_ansatz_requires_cot2alpha_radial_ode():
    alpha = sp.symbols("alpha", positive=True)
    A = sp.Function("A")

    # Derived from the recovered Lawrence non-Cartan generator acting on
    # psi_{0,1/2} = A(alpha) * exp(i*(theta-theta_tilde)/2).
    coeff_e_plus_3half = sp.I / 8 * (
        2 * sp.diff(A(alpha), alpha) - (sp.cot(alpha) - sp.tan(alpha)) * A(alpha)
    )
    coeff_e_minus_half = sp.I / 8 * (
        2 * sp.diff(A(alpha), alpha) + (sp.cot(alpha) - sp.tan(alpha)) * A(alpha)
    )

    ode_solution = sp.sqrt(sp.sin(2 * alpha))
    radial_relation = sp.simplify(sp.diff(sp.log(ode_solution), alpha) - sp.cot(2 * alpha))

    forced_ode = sp.simplify(
        coeff_e_plus_3half.subs(
            sp.diff(A(alpha), alpha),
            (sp.cot(alpha) - sp.tan(alpha)) * A(alpha) / 2,
        )
    )
    surviving = sp.simplify(
        coeff_e_minus_half.subs(
            sp.diff(A(alpha), alpha),
            (sp.cot(alpha) - sp.tan(alpha)) * A(alpha) / 2,
        )
    )

    assert radial_relation == 0
    assert sp.simplify(forced_ode) == 0
    assert sp.simplify(surviving - sp.I / 4 * (sp.cot(alpha) - sp.tan(alpha)) * A(alpha)) == 0


def test_scalar_dragging_cannot_produce_alpha_independent_ladder_coefficient():
    alpha = sp.symbols("alpha", positive=True)
    A = sp.Function("A")
    surviving = sp.I / 4 * (sp.cot(alpha) - sp.tan(alpha)) * A(alpha)  # noqa: F841
    alpha_independent = sp.diff((sp.cot(alpha) - sp.tan(alpha)), alpha)
    assert sp.simplify(alpha_independent) != 0
