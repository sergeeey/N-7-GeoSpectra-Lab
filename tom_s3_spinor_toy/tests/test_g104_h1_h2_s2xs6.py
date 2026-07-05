import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT / "tom_s3_spinor_toy" / "experiments" / "20260705-g104-h1-h2-s2xs6" / "g104_h1_h2_s2xs6.py"
)
SPEC = importlib.util.spec_from_file_location("g104_h1_h2_s2xs6", SCRIPT)
assert SPEC and SPEC.loader
G104 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G104)

G103_RESULTS = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260705-g103-kk-lambda-blindness"
    / "results_g103.json"
)

CTRL = G104.run_for_lambda(3, 6, 1.0 / 3.0)  # positive control, (a,N)=(3,6)
LAM_H1 = 1.0 / 2  # H1 = 1/a, a=2
LAM_H2 = 2.0 / (2 + 6)  # H2 = a/(a+N)
RUN_H1 = G104.run_for_lambda(2, 6, LAM_H1)
RUN_H2 = G104.run_for_lambda(2, 6, LAM_H2)


def test_positive_control_reproduces_g66_kappa():
    """C1: (a,N)=(3,6), volume-power-2n path, lambda=1/3 must reproduce G66's
    verified kappa^2=7/6 -- within 1e-2 (G66 itself has a ~0.3%-level subleading
    correction beyond the pure analytic term, see G66 decision.md)."""
    assert CTRL is not None and CTRL["exists"]
    assert abs(CTRL["kappa_sq"] - 7.0 / 6.0) < 1e-2


def test_positive_control_full_signature_matches_prior_gates():
    """C1 (full signature, per claim.md): V_min sign (AdS) and rho_min order
    of magnitude must also match G62/G103's already-verified (3,6) numbers
    (rho6_min~1.179), not just kappa^2 alone."""
    assert CTRL["v_min"] < 0
    assert abs(CTRL["rho_min"] - 1.179) < 0.01


def test_volume_power_path_scaling_regression():
    """Regression pin for the path-mismatch bug found during design: an
    equal-radii trajectory (rho_a=rho_N) FAILED this same control
    (kappa^2=1.228 vs target 1.1667). The fix -- rho_a = rho_N^(N/a) -- must
    hold exactly for the (3,6) control point."""
    rho_n = CTRL["rho_min"]
    assert abs(CTRL["rho_a_min"] - rho_n ** (6 / 3)) < 1e-9


def test_both_h1_h2_admit_ads_minimum():
    """C2: a valid AdS minimum (V_min<0, V''>0 enforced inside run_for_lambda)
    exists for BOTH lambda=H1(0.5) and lambda=H2(0.25) on (a,N)=(2,6)."""
    assert RUN_H1 is not None and RUN_H1["exists"]
    assert RUN_H2 is not None and RUN_H2["exists"]


def test_kappa_matches_g66_target_for_both_hypotheses():
    """C3: kappa^2(a=2,N=6) matches G66's N-only prediction (N+1)/N=7/6 for
    BOTH lambda choices -- kappa depends on N only, per G66."""
    target = 7.0 / 6.0
    assert abs(RUN_H1["kappa_sq"] - target) < 1e-2
    assert abs(RUN_H2["kappa_sq"] - target) < 1e-2


def test_kappa_blind_uses_relative_not_absolute_tolerance():
    """Regression pin for the tolerance-miscalibration bug found during design:
    comparing H1/H2 kappa^2 with an absolute 1e-6 bound is far stricter than
    the established H1-pearl 'near-universal, 0.20% spread' precedent. The
    relative spread here must be well under the 0.5% bar the script uses."""
    rel_spread = abs(RUN_H1["kappa_sq"] - RUN_H2["kappa_sq"]) / RUN_H2["kappa_sq"]
    assert rel_spread < 0.005


def test_c4_ratios_are_computed_and_positive():
    """C4: descriptive ratios (V_min, m_mod) between the H1-run and H2-run --
    reported, not pre-judged. Must be positive finite numbers (same sign
    conventions on both runs)."""
    v_ratio = RUN_H1["v_min"] / RUN_H2["v_min"]
    m_ratio = RUN_H1["m_mod"] / RUN_H2["m_mod"]
    assert v_ratio > 0
    assert m_ratio > 0


def test_m_mod_ratio_matches_g103_power_law():
    """Post-hoc cross-check (NOT one of the pre-registered C1-C4 checks in
    claim.md): G103 fit m_mod ~ lambda^0.4928 from a sweep at fixed
    (a,N)=(3,6). That same exponent, applied to (lambda_h1/lambda_h2)=2.0 on a
    DIFFERENT (a,N)=(2,6) pair, predicts the m_mod ratio to within 0.1% of the
    actual G104 result -- suggestive the power law is a structural feature of
    the modulus sector, not an artifact of the (3,6) point. Single data point,
    not independent confirmation (same V_FLUX/RHO6_STAR machinery reused) --
    recorded as a pearl candidate, not a claim."""
    g103 = json.loads(G103_RESULTS.read_text())
    exponent = g103["checks"]["M_modulus_exponent"]
    predicted_ratio = (LAM_H1 / LAM_H2) ** exponent
    actual_ratio = RUN_H1["m_mod"] / RUN_H2["m_mod"]
    assert abs(actual_ratio - predicted_ratio) / predicted_ratio < 0.002
