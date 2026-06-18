#!/usr/bin/env python
"""P13H — S3 absolute normalization integral test (research_only)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cc_toy_lab.compactification.convention_registry import Classification, register_gate_result
from cc_toy_lab.compactification.p13h_integral import report_to_dict, run_p13h_integral_test
from cc_toy_lab.runs import to_jsonable, write_json, write_summary

REPORT_MD = Path("reports/P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST.md")


def main() -> int:
    report = run_p13h_integral_test(grid_n=24)
    register_gate_result("P13H", report.classification)

    payload = report_to_dict(report)
    run_dir = Path("reports/RUNS/p13h_s3_absolute_normalization_integral_test")
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(run_dir / "metrics.json", payload)

    md = _format_report(report, payload)
    REPORT_MD.write_text(md, encoding="utf-8")
    write_summary(
        run_dir / "summary.md",
        "P13H S3 Absolute Normalization Integral Test",
        [f"Classification: {report.classification.value}", f"lambda: {report.lambda_role}"],
    )

    print(f"P13H complete: {report.classification.value}")
    print(f"lambda_role: {report.lambda_role}")
    print(f"P13E preserved: {report.p13e_status_preserved}")
    print(f"report: {REPORT_MD}")
    return 0 if report.classification != Classification.FAILED else 1


def _format_report(report, payload: dict) -> str:
    return f"""# P13H — S3 Absolute Normalization Integral Test

**Gate:** P13H | **Status:** completed | **Runtime:** research_only

## Scope Fence

Single explicit low-mode S3 integral smoke. Does NOT verify physical V-selection,
coupling strength, fermion generations, SM, or runtime safety.

## Volume element

`{report.volume_element}`

## Primary pair (P13B1)

`{report.primary_pair}` — matrix element = `coefficient * lambda`

| Quantity | Value |
|----------|-------|
| coefficient (CONV_HAAR_UNIT) | `{report.primary_coefficient}` |
| |M_ij| | `{abs(report.primary_coefficient):.6e}` |
| P11 pattern compatible | `{report.p11_pattern_compatible}` |
| Hermiticity max error | `{report.hermiticity_max_error:.6e}` |

## Convention invariance (diagonal 1,1)

| Convention | coeff_11 |
|------------|----------|
| CONV_HAAR_UNIT | `{report.coeff_11_unit}` |
| CONV_HAAR_HARMONIC_SQRT2 | `{report.coeff_11_sqrt2}` |
| relative change | `{payload['details']['relative_diagonal_11_change']:.6f}` |
| invariant | `{report.convention_invariant_for_diagonal_11}` |

## Classification

**`{report.classification.value}`**

- lambda: `{report.lambda_role}`
- P13E/P13F NO_GO preserved: `{report.p13e_status_preserved}`
- promotion: `{report.promotion}`

## Frozen inputs (unchanged)

P13A–P13G statuses not modified. P13E remains `NORMALIZATION_DEPENDENT_NO_GO`.

## Raw metrics

```json
{json.dumps(to_jsonable(payload), indent=2)}
```
"""


if __name__ == "__main__":
    raise SystemExit(main())
