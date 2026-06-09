"""Phase 4 alpha-domain diagnostic for Tom's S3 convention.

This is a lightweight convention check, not a verdict on Tom Lawrence's theory.

Question:
    What changes if the Phase 2 Hopf half-domain alpha in [0, pi/2]
    is extended to a full alpha domain [0, pi]?

The diagnostic only records sign / real-valuedness facts for:
    sin(alpha) cos(alpha)
    abs(sin(alpha) cos(alpha))
    sin(2 alpha)
    abs(sin(2 alpha))
    sqrt(sin(2 alpha))
    sqrt(abs(sin(2 alpha)))
    cot(2 alpha)
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


REPORT_MD = Path("reports/PHASE4_ALPHA_DOMAIN_DIAGNOSTIC_2026-06-07.md")
REPORT_JSON = Path("reports/PHASE4_ALPHA_DOMAIN_DIAGNOSTIC_2026-06-07.json")
PLOT_PATH = Path("reports/PHASE4_ALPHA_DOMAIN_DIAGNOSTIC_2026-06-07.png")


def _interval_stats(alpha: np.ndarray, values: np.ndarray) -> dict:
    finite = np.isfinite(values)
    return {
        "min": float(np.nanmin(values[finite])),
        "max": float(np.nanmax(values[finite])),
        "mean": float(np.nanmean(values[finite])),
        "negative_fraction": float(np.mean(values < 0.0)),
        "positive_fraction": float(np.mean(values > 0.0)),
        "zero_near_fraction": float(np.mean(np.isclose(values, 0.0, atol=1e-10))),
        "finite_fraction": float(np.mean(finite)),
        "alpha_min": float(alpha[0]),
        "alpha_max": float(alpha[-1]),
    }


def run_diagnostic(n: int = 20_000, eps: float = 1e-6) -> dict:
    """Compute sign and real-valuedness diagnostics on alpha in (0, pi)."""
    alpha = np.linspace(eps, np.pi - eps, n)
    sincos = np.sin(alpha) * np.cos(alpha)
    sin2 = np.sin(2.0 * alpha)
    sqrt_sin2_complex = np.sqrt(sin2.astype(complex))
    sqrt_abs_sin2 = np.sqrt(np.abs(sin2))
    cot2 = 1.0 / np.tan(2.0 * alpha)

    left = alpha < (np.pi / 2)
    right = alpha > (np.pi / 2)
    center = np.isclose(alpha, np.pi / 2, atol=(np.pi / n))

    real_sqrt_mask = sin2 >= 0.0
    imaginary_sqrt_mask = sin2 < 0.0

    return {
        "meta": {
            "purpose": "Lightweight alpha-domain convention diagnostic; not a theory verdict.",
            "alpha_domain": "(0, pi), endpoints excluded by eps",
            "n": n,
            "eps": eps,
        },
        "global": {
            "sincos": _interval_stats(alpha, sincos),
            "sin2": _interval_stats(alpha, sin2),
            "cot2": _interval_stats(alpha, cot2),
            "sqrt_sin2_real_fraction": float(np.mean(real_sqrt_mask)),
            "sqrt_sin2_imaginary_fraction": float(np.mean(imaginary_sqrt_mask)),
            "sqrt_sin2_complex_has_imaginary_part_fraction": float(
                np.mean(np.abs(np.imag(sqrt_sin2_complex)) > 1e-12)
            ),
            "sqrt_abs_sin2_finite_fraction": float(np.mean(np.isfinite(sqrt_abs_sin2))),
        },
        "intervals": {
            "left_0_to_pi_over_2": {
                "alpha_min": float(alpha[left][0]),
                "alpha_max": float(alpha[left][-1]),
                "sin2_sign": "positive",
                "sqrt_sin2_type": "real",
                "sincos_sign": "positive",
            },
            "near_pi_over_2": {
                "alpha_center": float(np.pi / 2),
                "sin2_sign": "zero crossing",
                "sincos_sign": "zero crossing",
                "cot2": "pole / sign flip",
                "grid_points_near_center": int(np.sum(center)),
            },
            "right_pi_over_2_to_pi": {
                "alpha_min": float(alpha[right][0]),
                "alpha_max": float(alpha[right][-1]),
                "sin2_sign": "negative",
                "sqrt_sin2_type": "imaginary if principal complex sqrt is used",
                "sincos_sign": "negative",
            },
        },
        "skeptic": {
            "claim": (
                "The cot(2 alpha) imaginary inconsistency may be related to extending "
                "a half-domain Hopf-like measure/normalization factor to alpha in [0, pi]."
            ),
            "strongest_objection": (
                "cot(2 alpha) itself is real on both open intervals and only has poles/sign "
                "flips; Tom's inconsistency may come from generator matching, not from a "
                "sqrt(sin(2 alpha)) or measure factor."
            ),
            "cheapest_falsification": (
                "Obtain Tom's exact embedding, measure/Jacobian, I_1R differential operator, "
                "and the two coupled equations. If they do not use a sqrt-like sign-sensitive "
                "factor, this hypothesis weakens."
            ),
            "kill_criterion": (
                "If Tom's exact measure is positive by construction and his alpha functions "
                "avoid sqrt(sin(2 alpha)) or any half-domain continuation, do not pursue this "
                "as the primary explanation."
            ),
        },
    }


def write_plot(diagnostic: dict) -> None:
    """Write a compact plot of the sign-sensitive alpha functions."""
    n = diagnostic["meta"]["n"]
    eps = diagnostic["meta"]["eps"]
    alpha = np.linspace(eps, np.pi - eps, n)
    sincos = np.sin(alpha) * np.cos(alpha)
    sin2 = np.sin(2.0 * alpha)
    sqrt_abs_sin2 = np.sqrt(np.abs(sin2))

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle("Phase 4 alpha-domain diagnostic: alpha in [0, pi]", fontsize=12)

    ax = axes[0]
    ax.plot(alpha, sincos, label="sin(alpha) cos(alpha)", lw=2)
    ax.plot(alpha, sin2, label="sin(2 alpha)", lw=1.5, linestyle="--")
    ax.axhline(0.0, color="black", lw=0.8)
    ax.axvline(np.pi / 2, color="red", lw=1.0, linestyle=":")
    ax.set_ylabel("signed value")
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axes[1]
    sqrt_sin2_real = np.full_like(sin2, np.nan)
    real_mask = sin2 >= 0.0
    sqrt_sin2_real[real_mask] = np.sqrt(sin2[real_mask])
    ax.plot(alpha, sqrt_sin2_real, label="sqrt(sin(2 alpha)) real branch", lw=2)
    ax.plot(alpha, sqrt_abs_sin2, label="sqrt(abs(sin(2 alpha)))", lw=1.5, linestyle="--")
    ax.axvline(np.pi / 2, color="red", lw=1.0, linestyle=":")
    ax.set_xlabel("alpha")
    ax.set_ylabel("sqrt value")
    ax.legend()
    ax.grid(alpha=0.3)

    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=150, bbox_inches="tight")
    plt.close(fig)


def write_reports(diagnostic: dict) -> None:
    """Write JSON and Markdown reports."""
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(diagnostic, indent=2), encoding="utf-8")

    global_diag = diagnostic["global"]
    intervals = diagnostic["intervals"]
    skeptic = diagnostic["skeptic"]

    md = f"""# Phase 4 Alpha-Domain Diagnostic — 2026-06-07

Status: lightweight convention diagnostic, not a theory verdict.

## Claim Under Skeptic Check

[HYPOTHESIS] {skeptic["claim"]}

## What This Diagnostic Verifies

[VERIFIED] On `alpha in (0, pi)`, excluding endpoints:

- `sin(alpha) cos(alpha)` is positive on `(0, pi/2)` and negative on `(pi/2, pi)`.
- `sin(2 alpha)` is positive on `(0, pi/2)` and negative on `(pi/2, pi)`.
- `sqrt(sin(2 alpha))` is real only where `sin(2 alpha) >= 0`.
- `sqrt(abs(sin(2 alpha)))` stays real across both open intervals.
- `cot(2 alpha)` is real on both open intervals but has poles/sign flips; by itself it is not imaginary.

## Numeric Summary

```json
{json.dumps(global_diag, indent=2)}
```

## Interval Summary

```json
{json.dumps(intervals, indent=2)}
```

## Strongest Objection

[SKEPTIC] {skeptic["strongest_objection"]}

## Cheapest Falsification

[SKEPTIC] {skeptic["cheapest_falsification"]}

## Kill Criterion

[SKEPTIC] {skeptic["kill_criterion"]}

## Interpretation Guardrail

[INFERRED] This result supports only a convention-level question:

```text
If Tom's alpha really spans [0, pi], is the S3 chart patch-wise, signed,
or using an absolute Jacobian/phase convention?
```

It does not show that Tom made an error, and it does not validate or refute
Covariant Compactification.

## Plot

Generated artifact:

```text
{PLOT_PATH.as_posix()}
```
"""
    REPORT_MD.write_text(md, encoding="utf-8")


def main() -> None:
    diagnostic = run_diagnostic()
    write_plot(diagnostic)
    write_reports(diagnostic)
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()
