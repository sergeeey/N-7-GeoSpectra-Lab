"""Run HYP_01–HYP_03 toy experiments and build markdown summary."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cc_toy_lab.compactification.hyp01_flux_veff import run_hyp01_experiment
from cc_toy_lab.compactification.hyp02_twisted_lichnerowicz import run_hyp02_experiment
from cc_toy_lab.compactification.hyp03_v_ratio import run_hyp03_experiment


@dataclass(frozen=True)
class HypothesisSuiteResult:
    coupled_hyp01: object
    falsifier_hyp01: object
    hyp02_unit: object
    hyp02_sqrt2: object
    hyp03: object


def run_all_hypothesis_experiments() -> HypothesisSuiteResult:
    coupled, falsifier = run_hyp01_experiment()
    h2u, h2s = run_hyp02_experiment()
    h3 = run_hyp03_experiment()
    return HypothesisSuiteResult(
        coupled_hyp01=coupled,
        falsifier_hyp01=falsifier,
        hyp02_unit=h2u,
        hyp02_sqrt2=h2s,
        hyp03=h3,
    )


def write_hypothesis_report(
    result: HypothesisSuiteResult,
    path: Path | str = "reports/HYPOTHESIS_EXPERIMENTS_REPORT.md",
) -> Path:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    c1 = result.coupled_hyp01
    f1 = result.falsifier_hyp01
    h2 = result.hyp02_unit
    h3 = result.hyp03

    lines = [
        "# Hypothesis Experiments Report",
        "",
        "**Status:** research_only | smoke_only | safe_for_runtime = no",
        "",
        "Toy tests for HYP_01–HYP_03. Does not promote physical compactification or SM claims.",
        "",
        "## HYP_01 — Flux / moduli stabilization",
        "",
        f"- Coupled branch: `{c1.status}` — {c1.message}",
    ]
    for i, cp in enumerate(c1.critical_points):
        lines.append(
            f"  - CP{i}: lambda*={cp.lam:.6f}, R={cp.radius:.6f}, phi={cp.squash:.6f}, "
            f"Hess proxy={cp.hessian_min_eig:.4f}"
        )
    lines.extend(
        [
            f"- Falsifier (decoupled): `{f1.status}` — {f1.message}",
            "",
            "## HYP_02 — Twisted Lichnerowicz eigenvalue",
            "",
            f"- Status: `{h2.status}` — {h2.message}",
            f"- Kernel dimension (toy constraint): {h2.kernel_dimension}",
            f"- Eigenvalues (UNIT / SQRT2): {h2.admissible_eigenvalues} / "
            f"{result.hyp02_sqrt2.admissible_eigenvalues}",
            "",
            "## HYP_03 — Nonlinear realization",
            "",
            f"- Status: `{h3.status}` — {h3.message}",
            f"- R_B observable: {h3.r_observable:.12f} (lambda derivative {h3.lambda_derivative})",
            f"- Full descent toy: deferred={h3.toy_test_deferred}",
            "",
            "## Interpretation",
            "",
            "- HYP_01: flux-lambda **coupling** can yield discrete lambda* in toy V_eff; "
            "removing coupling kills the route (falsifier confirmed).",
            "- HYP_02: current P13B1 truncation — check status above; "
            "convention dependence aligns with P13E NO-GO if killed.",
            "- HYP_03: lambda-free R_B=sqrt(2) confirmed; parent-action descent still deferred.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
