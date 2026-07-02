import importlib.util
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260701-g102-cs3-dbrane-normalization"
    / "g102_cs3_gs.py"
)
SPEC = importlib.util.spec_from_file_location("g102_cs3_gs", SCRIPT)
assert SPEC and SPEC.loader
G102 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G102)


def test_tension_formula_matches_source_trace():
    """T_2 must equal 1/((2pi)^2 * l_s^3 * g_s) -- the source-traced Polchinski form."""
    expected = 1 / (4 * sp.pi**2 * G102.g_s * G102.l_s**3)
    assert sp.simplify(G102.T_2_in_ls - expected) == 0


def test_cs3_equals_one_over_two_gs():
    """Core symbolic result: c_S3 = 1/(2*g_s), independent of l_s."""
    assert sp.simplify(G102.c_s3_derived - sp.Rational(1, 2) / G102.g_s) == 0


def test_l_s_cancels_exactly():
    """c_S3 is dimensionless -- l_s must not survive in the final expression."""
    assert G102.l_s not in G102.c_s3_derived.free_symbols


def test_control_independent_of_planck_mass_convention():
    """GA2's dropped-2pi convention (Planck-mass relation) must not appear here --
    this derivation never references M_Pl or V_9 at all."""
    assert not any(str(s) in ("M_Pl", "V_9", "V9") for s in G102.c_s3_derived.free_symbols)


def test_implied_gs_range_matches_g94_empirical_window():
    """G94's empirical c_S3 window [0.248, 0.372] must map to g_s in [1.344, 2.016]
    under c_S3=1/(2*g_s)."""
    gs_lo = float(1 / (2 * G102.C_S3_MAX_EMPIRICAL))
    gs_hi = float(1 / (2 * G102.C_S3_MIN_EMPIRICAL))
    assert abs(gs_lo - 1.344) < 0.01
    assert abs(gs_hi - 2.016) < 0.01


def test_full_experiment_runs_and_confirms_strongly_coupled():
    import json

    G102.main()
    data = json.loads(G102.RESULTS_PATH.read_text())
    assert data["verdict"] == "STRUCTURAL_RELATION_CONFIRMED"
    assert data["strongly_coupled"] is True
