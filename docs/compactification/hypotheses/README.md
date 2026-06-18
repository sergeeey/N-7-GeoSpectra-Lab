# Compactification Hypotheses

Research-only hypothesis cards for post-P13E routes. **Not validated physics.**

| ID | File | Toy module |
|----|------|------------|
| HYP_01 | [HYP_01_FLUX_STABILIZATION.md](HYP_01_FLUX_STABILIZATION.md) | `cc_toy_lab/compactification/hyp01_flux_veff.py` |
| HYP_02 | [HYP_02_TWISTED_LICHNEROWICZ.md](HYP_02_TWISTED_LICHNEROWICZ.md) | `cc_toy_lab/compactification/hyp02_twisted_lichnerowicz.py` |
| HYP_03 | [HYP_03_NONLINEAR_REALIZATION.md](HYP_03_NONLINEAR_REALIZATION.md) | `cc_toy_lab/compactification/hyp03_v_ratio.py` |

Run: `python scripts/run_hypothesis_experiments.py`  
Tests: `pytest tests/test_hypothesis_experiments.py -q`

Report: `reports/HYPOTHESIS_EXPERIMENTS_REPORT.md`

**Hard constraints:** `lambda = FREE_COUPLING_PARAMETER`, `safe_for_runtime = no`, `research_only`.
