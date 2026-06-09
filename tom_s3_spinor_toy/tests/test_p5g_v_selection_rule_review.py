"""P5G review test for the current V-selection rule status.

The purpose of this test is not to derive a new physical V operator. It only
locks the current engineering status so that the review layer cannot be
silently promoted above smoke-only without explicit follow-up work.
"""

from __future__ import annotations

from s3_coupling_v_option_b import build_v_symbolic, expand_spectral_basis_states
from s3_reduced_matrix_elements import reduced_element_metadata


def test_v_scaffold_is_hermitian_and_nonzero_in_current_smoke_convention() -> None:
    """The current V scaffold remains a Hermitian, nonzero engineering layer."""

    matrix = build_v_symbolic(k_max=1)
    assert matrix.shape[0] == matrix.shape[1]
    assert (matrix != 0).any()
    assert (matrix == matrix.conjugate().T).all()


def test_current_selection_rules_remain_the_working_cg_rules() -> None:
    """The current working selection rules stay tied to the reduced CG scaffold."""

    states = expand_spectral_basis_states(k_max=1)
    metadata = reduced_element_metadata()

    assert states
    assert metadata["J_L"] == 1.0
    assert metadata["J_R"] == 0.0
    assert metadata["final_ben_achour_normalization"] == "unresolved"
    assert metadata["claim_scope"] == "engineering smoke tests only; no quantitative physics claims"

    for source in states:
        for target in states:
            if source.index == target.index:
                continue
            if source.j_right != target.j_right:
                continue
            if source.m_right != target.m_right:
                continue
            if abs(target.j_left - source.j_left) > 1.0:
                continue
            q_left = target.m_left - source.m_left
            if q_left not in {-1.0, 0.0, 1.0}:
                continue
            assert not (source.j_left == 0.0 and target.j_left == 0.0)

