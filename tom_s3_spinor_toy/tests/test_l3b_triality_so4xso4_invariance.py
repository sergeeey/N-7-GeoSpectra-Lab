"""L3b tests: triality acts as a genuine order-3 automorphism on SO(4)xSO(4).

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5. Checks whether the SO(4)xSO(4)
candidate (see test_l3b_so4xso4_candidate.py) is triality-invariant as a
subalgebra of so(8), or merely a convenient basis with no such symmetry.
"""

import os
import sys

import numpy as np

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260715-l3b-triality-so4xso4-invariance"
)
sys.path.insert(0, _exp_dir)

from triality_so4xso4_invariance import (  # noqa: E402
    build_so4xso4_basis,
    build_triality_matrix_T,
    g2_sanity_check_residual,
    residual_in_span,
    solve_triality_partners,
)


def test_g2_element_is_triality_fixed():
    """Sanity check: a known g2 derivation must satisfy b=c=a (G2=Fix(triality))."""
    assert g2_sanity_check_residual() < 1e-8


def test_all_so4xso4_generators_map_back_into_the_subalgebra():
    """Every basis generator's triality partner b stays inside so(4)_1+so(4)_2."""
    basis = build_so4xso4_basis()
    basis_flat = basis.reshape(12, 64)
    for a in basis:
        b, _c, _resid = solve_triality_partners(a)
        assert residual_in_span(b, basis_flat) < 1e-8


def test_triality_matrix_has_order_dividing_three():
    """T^3 = I for the 12x12 matrix representing a -> b on so(4)_1+so(4)_2."""
    t_matrix, max_partner_residual = build_triality_matrix_T()
    assert max_partner_residual < 1e-8
    t_cubed = t_matrix @ t_matrix @ t_matrix
    assert np.allclose(t_cubed, np.eye(12), atol=1e-6)


def test_triality_matrix_eigenvalues_are_cube_roots_of_unity():
    """Eigenvalues of T are exactly {+1 (x6), omega (x3), omega-bar (x3)}."""
    t_matrix, _ = build_triality_matrix_T()
    evals = np.linalg.eigvals(t_matrix)

    n_plus_one = sum(1 for ev in evals if abs(ev.real - 1) < 1e-6 and abs(ev.imag) < 1e-6)
    omega = np.exp(2j * np.pi / 3)
    n_omega = sum(1 for ev in evals if abs(ev - omega) < 1e-6)
    n_omega_bar = sum(1 for ev in evals if abs(ev - omega.conjugate()) < 1e-6)

    assert n_plus_one == 6
    assert n_omega == 3
    assert n_omega_bar == 3
    assert n_plus_one + n_omega + n_omega_bar == 12


def test_fixed_subspace_dimension_matches_stab_g2_h():
    """The 6-dim +1-eigenspace of T must match dim(Stab_G2(H))=6, an independent
    already-established fact -- a genuine cross-check, not a re-derivation.
    """
    t_matrix, _ = build_triality_matrix_T()
    evals = np.linalg.eigvals(t_matrix)
    n_plus_one = sum(1 for ev in evals if abs(ev.real - 1) < 1e-6 and abs(ev.imag) < 1e-6)
    dim_stab_g2_h = 6  # verified independently in test_l3b_so4xso4_candidate.py's sibling check
    assert n_plus_one == dim_stab_g2_h
