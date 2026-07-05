import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260705-g103-kk-lambda-blindness"
    / "g103_kk_lambda_blindness.py"
)
SPEC = importlib.util.spec_from_file_location("g103_kk_lambda_blindness", SCRIPT)
assert SPEC and SPEC.loader
G103 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G103)

ROWS = G103.sweep()  # computed once; ~9 bounded minimizations, fast


def test_symbolic_tower_is_lambda_blind():
    """(S): no lambda_np symbol in any KK tower expression — direct dependence is zero."""
    assert G103.tower_is_lambda_blind()


def test_minimum_exists_across_full_sweep():
    """AdS minimum with positive curvature must exist for every lambda in the sweep."""
    assert len(ROWS) == len(G103.LAMBDA_SWEEP)


def test_positive_control_reproduces_ga1_reference():
    """(P): lambda=1/3 must reproduce GA1 verified numbers (rho6_min=1.1791, ratio=0.198%)."""
    ref = G103.run_for_lambda(1.0 / 3.0)
    assert ref is not None
    assert abs(ref["rho6_min"] - 1.1791) <= 0.002
    assert abs(ref["ratio_pct"] - 0.198) <= 0.02


def test_kk_spread_within_blindness_threshold():
    """(I): KK mass spread over the 4x lambda range stays below the 0.5% blindness bound."""
    spread = G103.spread_pct([r["m_kk"] for r in ROWS])
    assert spread <= G103.KK_SPREAD_PASS_PCT


def test_modulus_mass_scales_as_sqrt_lambda():
    """(M): d ln m_mod / d ln lambda in [0.40, 0.60] — the H1 sqrt-law, now fitted."""
    p = G103.fit_exponent(ROWS)
    assert G103.EXPONENT_PASS[0] <= p <= G103.EXPONENT_PASS[1]


def test_negative_control_has_discriminating_power():
    """(N): an injected lambda-dependent fake tower must violate the blindness bound
    by a wide margin — otherwise the blindness test is vacuous."""
    ctrl = G103.negative_control(ROWS)
    assert ctrl["caught"]
    assert ctrl["fake_spread_pct"] > 10 * G103.KK_SPREAD_PASS_PCT


def test_kk_lightest_mode_always_s3():
    """Structural GA1 result must persist: S3 gives the lightest KK mode at every lambda."""
    assert all(r["kk_source"] == "S3" for r in ROWS)
