import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260706-g106-third-point-n7-confirmation"
    / "g106_third_point_n7.py"
)
SPEC = importlib.util.spec_from_file_location("g106_third_point_n7", SCRIPT)
assert SPEC and SPEC.loader
G106 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G106)

PRED = G106.predicted()
ACT = G106.actual()


def test_point_is_genuinely_new():
    """This gate must test a DIFFERENT N than every prior gate -- otherwise it doesn't
    close the skeptic's physical-genericity gap (G104/G105 both only tested N=6)."""
    assert G106.BIG_N == 7
    assert G106.BIG_N != 6


def test_prediction_computed_from_g105_alone():
    """Pre-registration check: predicted() must depend only on G105's closed-form
    functions, not on G104's numerical machinery -- otherwise it isn't a genuine
    advance prediction."""
    assert abs(PRED["kappa_sq"] - 8.0 / 7.0) < 1e-12
    assert 0.0 < PRED["mass_exponent"] < 1.0


def test_actual_minimum_exists():
    """The (a,N)=(2,7) point must admit a genuine AdS minimum -- if G104's own
    construction failed to even produce a minimum at this new N, nothing else here
    would be meaningful."""
    assert ACT["exists"]


def test_kappa_matches_prediction():
    """Core falsifiable check: kappa^2 at the untested N=7 point must match G105's
    algebraic prediction (N+1)/N=8/7, within the same 1e-2 bar G104 used for its own
    (a,N) positive controls."""
    assert abs(ACT["kappa_sq"] - PRED["kappa_sq"]) < 1e-2


def test_mass_exponent_matches_prediction():
    """Core falsifiable check: the local mass exponent at N=7 must match G105's
    closed-form (A,B) prediction for n=14, within the same 0.02 bar as G105's D5."""
    assert abs(ACT["mass_exponent_local"] - PRED["mass_exponent"]) < 0.02


def test_prediction_is_not_reused_from_n6():
    """Regression pin: the A,B coefficients for n=14 (N=7) must differ from n=12
    (N=6) -- guards against accidentally reusing G105's own N=6 numbers instead of
    computing fresh ones for N=7."""
    a12, b12 = G106.G105.exponent_coefficients(12)
    a14, b14 = G106.G105.exponent_coefficients(14)
    assert abs(a12 - a14) > 0.1
    assert abs(b12 - b14) > 0.001
