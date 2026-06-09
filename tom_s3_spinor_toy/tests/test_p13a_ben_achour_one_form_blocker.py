"""Readiness checks for the missing Ben Achour executable one-form layer."""

from __future__ import annotations

import s3_oneform_laplacian_numerical as oneform_audit


def test_current_one_form_file_is_not_ben_achour_e_modes() -> None:
    assert not hasattr(oneform_audit, "E_i")
    assert not hasattr(oneform_audit, "Eprime_i")
    assert not hasattr(oneform_audit, "E_prime_i")
    assert "safe diagnostic" in oneform_audit.compute_e_coframe_norm_numerical.__doc__


def test_current_one_form_file_scope_is_not_symbolic_basis() -> None:
    result = oneform_audit.compute_e_coframe_norm_numerical(n_points=8, k_neighbors=2)

    assert "not Ben Achour E/E' basis mapping" in result["claim_scope"]
    assert result["graph_laplacian_status"] == "not_implemented_by_design"
