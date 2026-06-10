"""Tests — AV-2 E1: Sparse reconstruction over mixed bilinear dictionary.

Gate: AV2-E1 (from claim_av2_angular.md, precondition: G2 PASS)
Report: experiments/20260610-spinor-geometry-pivot-v0.2.0/e1_sparse_reconstruction_report.md
Pre-registration: experiments/.../claim_e1_sparse_reconstruction.md

Key result: phi_{0,0}(a) = cos(a), g_{0,0}(a) = sin(a)
=> phi*g = cos(a)*sin(a) = sin(2a)/2 = EXACT 1-term reconstruction of target.

These regressions pin:
  1. The 1-term STRONG_PASS verdict
  2. The selected atom is phi_g(0,0)
  3. The analytical identity: 2*phi_{0,0}*g_{0,0} = sin(2a)
  4. The scope guards (no overclaiming)

Skeptic note: 0% residual is analytically provable (not validation theater).
See e1_sparse_reconstruction_report.md for full derivation.
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.av2_e1_sparse_reconstruction import (
    PREREGISTERED_MODES,
    STRONG_PASS_MAX_TERMS,
    STRONG_PASS_RESIDUAL,
    WEAK_PASS_MAX_TERMS,
    _build_dictionary,
    _greedy_matching_pursuit,
    e1_sparse_reconstruction_summary,
    run_e1_sparse_reconstruction,
)
from tom_s3_spinor_toy.discrete_radial_dirac_proxy import g_nl_hopf
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf


# --- Fixtures ---


@pytest.fixture(scope="module")
def e1_report():
    """Run the full E1 gate once; reuse across tests."""
    return run_e1_sparse_reconstruction()


@pytest.fixture(scope="module")
def alpha_grid():
    return np.linspace(0.01, np.pi / 2 - 0.001, 8001)


@pytest.fixture(scope="module")
def e1_summary():
    return e1_sparse_reconstruction_summary()


# --- Analytical identity (core: WHY 0% is not theater) ---


class TestAnalyticalIdentity:
    """Verify the exact identity phi_{0,0}*g_{0,0} = sin(2a)/2.

    This is the mathematical reason why E1 achieves 0% residual with 1 term.
    It follows from C-H eqs 3.25/3.27 with n=l=0 and Jacobi P_0 = 1.
    [VERIFIED_FROM_PDF in AV-2 G0]
    """

    def test_phi00_equals_cos(self, alpha_grid):
        """C-H eq 3.25: phi_{0,0}(a) = cos(a) exactly (Jacobi P_0 = 1)."""
        phi00 = phi_nl_hopf(0, 0, alpha_grid)
        max_err = float(np.max(np.abs(phi00 - np.cos(alpha_grid))))
        assert max_err == 0.0, f"max|phi_00 - cos(a)| = {max_err:.2e}, expected 0"

    def test_g00_equals_sin(self, alpha_grid):
        """C-H eq 3.27: g_{0,0}(a) = sin(a) exactly (Jacobi P_0 = 1)."""
        g00 = g_nl_hopf(0, 0, alpha_grid)
        max_err = float(np.max(np.abs(g00 - np.sin(alpha_grid))))
        assert max_err == 0.0, f"max|g_00 - sin(a)| = {max_err:.2e}, expected 0"

    def test_phi_g_product_equals_sin2a_half(self, alpha_grid):
        """phi_{0,0}(a) * g_{0,0}(a) = sin(2a)/2 to machine precision."""
        phi00 = phi_nl_hopf(0, 0, alpha_grid)
        g00 = g_nl_hopf(0, 0, alpha_grid)
        product = phi00 * g00
        target_half = np.sin(2.0 * alpha_grid) / 2.0
        max_err = float(np.max(np.abs(product - target_half)))
        assert max_err < 1e-14, f"max|phi_00*g_00 - sin(2a)/2| = {max_err:.2e}, expected < 1e-14"

    def test_two_times_product_reconstructs_target(self, alpha_grid):
        """2 * phi_{0,0} * g_{0,0} = sin(2a) to machine precision."""
        phi00 = phi_nl_hopf(0, 0, alpha_grid)
        g00 = g_nl_hopf(0, 0, alpha_grid)
        reconstruction = 2.0 * phi00 * g00
        target = np.sin(2.0 * alpha_grid)
        max_err = float(np.max(np.abs(reconstruction - target)))
        assert max_err < 1e-13, f"max|2*phi_00*g_00 - sin(2a)| = {max_err:.2e}, expected < 1e-13"


# --- Dictionary construction ---


class TestDictionaryConstruction:
    """Verify the dictionary is built as pre-registered."""

    def test_dictionary_size_reasonable(self, alpha_grid):
        """Dictionary should have ~40-60 atoms (pre-registered)."""
        atoms = _build_dictionary(alpha_grid)
        assert 30 <= len(atoms) <= 80, (
            f"Dictionary size {len(atoms)} outside expected range [30, 80]"
        )

    def test_phi_g_00_atom_in_dictionary(self, alpha_grid):
        """The key atom phi_g(0,0) must be in the dictionary."""
        atoms = _build_dictionary(alpha_grid)
        names = [a.name for a in atoms]
        assert "phi_g(0,0)" in names, f"Key atom 'phi_g(0,0)' not found. Available: {names[:10]}..."

    def test_all_atoms_normalized(self, alpha_grid):
        """All atoms must have unit L2 norm (normalization step)."""
        atoms = _build_dictionary(alpha_grid)
        for a in atoms:
            nrm = float(np.linalg.norm(a.values))
            assert abs(nrm - 1.0) < 1e-10, f"Atom '{a.name}' norm = {nrm:.6f}, expected 1.0"

    def test_preregistered_modes_covered(self, alpha_grid):
        """All pre-registered modes must produce at least phi_sq and g_sq atoms."""
        atoms = _build_dictionary(alpha_grid)
        names = [a.name for a in atoms]
        for n, l in PREREGISTERED_MODES:  # noqa: E741
            assert f"phi_sq({n},{l})" in names, f"Missing phi_sq({n},{l})"
            assert f"g_sq({n},{l})" in names, f"Missing g_sq({n},{l})"


# --- Greedy pursuit algorithm ---


class TestGreedyPursuit:
    """Test the greedy matching pursuit on analytical examples."""

    def test_exact_1_term_sin2a(self, alpha_grid):
        """Greedy pursuit finds 1-term exact reconstruction of sin(2a)."""
        from tom_s3_spinor_toy.av2_e1_sparse_reconstruction import _build_dictionary

        target = np.sin(2.0 * alpha_grid)
        atoms = _build_dictionary(alpha_grid)
        weight = np.ones_like(alpha_grid)

        steps, selected = _greedy_matching_pursuit(target, atoms, weight, max_steps=5)
        assert len(selected) >= 1
        # First selected atom should be phi_g(0,0)
        assert selected[0] == "phi_g(0,0)", (
            f"Expected first atom = 'phi_g(0,0)', got '{selected[0]}'"
        )

    def test_residual_after_step1_near_zero(self, alpha_grid):
        """After 1 step, residual should be < 1e-10 (machine precision)."""
        from tom_s3_spinor_toy.av2_e1_sparse_reconstruction import _build_dictionary

        target = np.sin(2.0 * alpha_grid)
        atoms = _build_dictionary(alpha_grid)
        weight = np.ones_like(alpha_grid)

        steps, _ = _greedy_matching_pursuit(target, atoms, weight, max_steps=1)
        assert steps[0].residual_unweighted < 1e-10, (
            f"Residual after 1 step = {steps[0].residual_unweighted:.2e}, expected < 1e-10"
        )


# --- Key E1 gate results ---


class TestE1GateResults:
    """Pin the key numerical results of the E1 gate."""

    def test_verdict_strong_pass(self, e1_report):
        """E1 verdict must be STRONG_PASS."""
        assert e1_report.verdict == "STRONG_PASS", (
            f"E1 verdict = {e1_report.verdict!r}, expected STRONG_PASS. "
            f"residual={e1_report.final_residual_unweighted:.4f}, "
            f"n_terms={e1_report.n_terms_used}"
        )

    def test_n_terms_within_strong_pass_threshold(self, e1_report):
        """Number of terms used must be <= pre-registered STRONG_PASS threshold (5)."""
        assert e1_report.n_terms_used <= STRONG_PASS_MAX_TERMS, (
            f"n_terms = {e1_report.n_terms_used} > STRONG_PASS_MAX_TERMS = {STRONG_PASS_MAX_TERMS}"
        )

    def test_residual_below_strong_pass_threshold(self, e1_report):
        """Both residuals must be < pre-registered STRONG_PASS threshold (5%)."""
        assert e1_report.final_residual_unweighted < STRONG_PASS_RESIDUAL, (
            f"Unweighted residual {e1_report.final_residual_unweighted:.4f} "
            f">= {STRONG_PASS_RESIDUAL}"
        )
        assert e1_report.final_residual_weighted < STRONG_PASS_RESIDUAL, (
            f"Weighted residual {e1_report.final_residual_weighted:.4f} >= {STRONG_PASS_RESIDUAL}"
        )

    def test_first_selected_atom_is_phi_g_00(self, e1_report):
        """The first (and in this case only) selected atom must be phi_g(0,0).

        This is the mixed l=0 bilinear that G2 predicted would dominate.
        """
        assert len(e1_report.selected_atoms) >= 1, "No atoms selected"
        assert e1_report.selected_atoms[0] == "phi_g(0,0)", (
            f"First atom = {e1_report.selected_atoms[0]!r}, expected 'phi_g(0,0)'"
        )

    def test_n_atoms_reasonable(self, e1_report):
        """Dictionary should contain atoms from all mode pairs."""
        assert e1_report.n_atoms >= 30, (
            f"n_atoms = {e1_report.n_atoms} < 30 — dictionary unexpectedly small"
        )


# --- item40 status cap (hard constraint) ---


class TestItem40StatusCap:
    """item40 must not exceed the E1-era maximum."""

    ALLOWED_E1_STATUSES = {
        "RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED",
        "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED",  # fallback on E1 FAIL
        "RADIAL + DICTIONARY_ROBUST",  # fallback
    }

    FORBIDDEN_SUBSTRINGS = [
        "ANGULAR_SINGLET",
        "ANGULAR_BILINEAR_SUPPORTED",  # requires E2
        "TOM_ANSATZ_SOLVED",
        "H_T1_PROMOTED",
        "LAMBDA_FIXED",
        "SAFE_FOR_RUNTIME",
    ]

    def test_item40_within_allowed_set(self, e1_report):
        assert e1_report.item40_max_status in self.ALLOWED_E1_STATUSES, (
            f"item40 = {e1_report.item40_max_status!r} is outside the allowed set"
        )

    def test_item40_no_forbidden_substrings(self, e1_report):
        status = e1_report.item40_max_status.upper()
        for substr in self.FORBIDDEN_SUBSTRINGS:
            assert substr not in status, (
                f"item40 = {e1_report.item40_max_status!r} contains forbidden substring {substr!r}"
            )

    def test_summary_item40_consistent(self, e1_summary):
        assert e1_summary["item40_status"] in self.ALLOWED_E1_STATUSES


# --- Scope integrity ---


class TestScopeIntegrity:
    """Forbidden claims must not appear anywhere in the report."""

    def test_forbidden_claims_not_empty(self, e1_report):
        assert len(e1_report.forbidden_claims) >= 4

    def test_tom_ansatz_solved_forbidden(self, e1_report):
        fc = [c.lower() for c in e1_report.forbidden_claims]
        assert any("tom ansatz" in c for c in fc)

    def test_lambda_fixed_forbidden(self, e1_report):
        fc = [c.lower() for c in e1_report.forbidden_claims]
        assert any("lambda" in c for c in fc)

    def test_scope_contains_no_angular(self, e1_report):
        scope_lower = e1_report.scope.lower()
        assert "no full angular" in scope_lower

    def test_scope_contains_no_h_t1(self, e1_report):
        scope_lower = e1_report.scope.lower()
        assert "no h-t1" in scope_lower


# --- Pre-registered mode set coverage ---


class TestPreregisteredModeSet:
    """Pre-registered modes must be present in the report."""

    def test_preregistered_modes_match(self, e1_report):
        assert set(map(tuple, e1_report.preregistered_modes)) == set(PREREGISTERED_MODES)

    def test_excluded_mode_not_in_report(self, e1_report):
        """Mode (3,2) was pre-registered as excluded."""
        atoms = e1_report.selected_atoms
        assert not any("(3,2)" in a for a in atoms), (
            "Mode (3,2) was excluded from pre-registration but appeared in selected atoms"
        )

    def test_weak_pass_threshold_not_exceeded(self, e1_report):
        """Even WEAK_PASS allows at most 8 terms."""
        assert e1_report.n_terms_used <= WEAK_PASS_MAX_TERMS, (
            f"n_terms = {e1_report.n_terms_used} > WEAK_PASS_MAX_TERMS = {WEAK_PASS_MAX_TERMS}"
        )
