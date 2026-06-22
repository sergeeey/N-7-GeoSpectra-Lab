# G76 Decision вЂ” PASS

**Date:** 2026-06-22
**Verdict:** `PASS` вЂ” registry complete and internally consistent

## Result

- 14 parameters audited
- 3 `fixed`
- 6 `conditional`
- 5 `free`
- 0 dangling dependencies
- `lambda_np` and `lambda_v_operator` are explicitly separate
- `C_SM` remains an external input
- `A_np` and uplift `D` are conditional outputs
- the physical mass scale remains unidentified

The exact status vocabulary is:

- `PASS`: the registry audit itself;
- `CONDITIONAL`: values derived after explicit assumptions or external inputs;
- `FREE`: parameters not identified by the implemented model;
- `OPEN`: a derivation route that has not yet been completed.

The machine-readable verdict is in `results_g76.json`.

Run:

```bash
python tom_s3_spinor_toy/experiments/20260622-g76-parameter-registry/g76_parameter_registry.py
python -m pytest tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q
python -m pytest tom_s3_spinor_toy/tests/test_markdown_claim_audit.py -q
```

All six gates pass.
