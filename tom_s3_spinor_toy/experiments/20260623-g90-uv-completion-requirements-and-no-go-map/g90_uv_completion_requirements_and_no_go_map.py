"""G90: UV completion requirements and no-go map packaging note.

This is a falsification-first packaging gate. It does not derive new physics.
It consolidates the repository's current status into:

- supported claims
- unsupported claims
- no-go routes
- UV completion requirements
- a short external-facing note

The script is deterministic and writes two outputs:

- results_g90.json
- UV_COMPLETION_REQUIREMENTS_AND_NO_GO_MAP.md
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_DIR = Path(__file__).resolve().parent
RESULTS_PATH = EXPERIMENT_DIR / "results_g90.json"
NOTE_PATH = EXPERIMENT_DIR / "UV_COMPLETION_REQUIREMENTS_AND_NO_GO_MAP.md"


def _read(rel_path: str) -> str:
    return (PROJECT_ROOT / rel_path).read_text(encoding="utf-8", errors="replace")


def _evidence(rel_path: str, needle: str) -> str:
    text = _read(rel_path)
    if needle not in text:
        raise RuntimeError(f"Missing evidence needle in {rel_path!r}: {needle!r}")
    return f"{rel_path}: {needle}"


def build_result() -> dict[str, Any]:
    sources = {
        "readme": "README.md",
        "status": "RESEARCH_STATUS_REPORT.md",
        "alive": "ALIVE_BRANCHES.md",
        "null_index": "null_results/INDEX.md",
        "preprint": "preprint.tex",
        "g84a": "experiments/20260622-g84a-standard-gauge-reduction/decision.md",
        "g85a": "experiments/20260622-g85a-poisson-bessel-resummation-audit/decision.md",
        "g85b": "experiments/20260622-g85b-spectral-saddle/decision.md",
        "g86a": "experiments/20260622-g86a-dual-modulus/decision.md",
        "g86b": "experiments/20260622-g86b-warp-factor/decision.md",
        "g88f": "experiments/20260623-g88f-full-reduced-action-reconstruction/decision.md",
        "g89a": "experiments/20260623-g89a-majorana-gauge-invariance-selection-rules/decision.md",
        "g89b": "experiments/20260623-g89b-b-minus-l-breaking-operator-audit/decision.md",
    }

    evidence = {
        "lambda_free": [
            _evidence(sources["status"], "λ = FREE_COUPLING_PARAMETER"),
            _evidence(sources["alive"], "G85B"),
            _evidence(sources["null_index"], "G86B"),
        ],
        "mass_ratio_not_confirmed": [
            _evidence(sources["status"], "coordinate-curvature proxy, not a canonically normalized physical mass ratio"),
            _evidence(sources["readme"], "G82 | canonical radion mass audit | CONDITIONAL"),
            _evidence(sources["g88f"], "INSUFFICIENT_ACTION"),
        ],
        "dirac_only_neutrinos": [
            _evidence(sources["g89a"], "DIRAC_ONLY_ALLOWED"),
            _evidence(sources["g89b"], "DIRAC_ONLY_CONFIRMED"),
            _evidence(sources["g89b"], "The current model branch remains Dirac-only for neutrinos."),
        ],
    }

    supported_claims = [
        {
            "claim": "The repository supports a phenomenological spectral compactification toy model with derived SM-like structure.",
            "evidence": [
                _evidence(sources["readme"], "The product geometry"),
                _evidence(sources["readme"], "32-component spinor = 1 SM generation"),
                _evidence(sources["readme"], "N_gen = 3 EXACTLY"),
            ],
        },
        {
            "claim": "The lambda bottleneck is not derived internally and remains FREE_COUPLING_PARAMETER.",
            "evidence": evidence["lambda_free"],
        },
        {
            "claim": "The right-handed neutrino sector is Dirac-only in the current branch unless new B-L-breaking physics is added.",
            "evidence": evidence["dirac_only_neutrinos"],
        },
        {
            "claim": "The physical mass ratio is not confirmed; only proxy-level results are available.",
            "evidence": evidence["mass_ratio_not_confirmed"],
        },
    ]

    unsupported_claims = [
        {
            "claim": "lambda is derived from current repository geometry.",
            "reason": "Track B is exhausted; the geometric/spectral class closed without a derivation.",
            "evidence": [
                _evidence(sources["status"], "Track B result"),
                _evidence(sources["alive"], "G85A"),
                _evidence(sources["alive"], "G86B"),
            ],
        },
        {
            "claim": "The old 2.02% mass ratio is a confirmed physical prediction.",
            "reason": "G88D/G88E/G88F show proxy-level results plus missing action and frame map.",
            "evidence": [
                _evidence(sources["g88f"], "INSUFFICIENT_ACTION"),
                _evidence(sources["status"], "coordinate-curvature proxy"),
            ],
        },
        {
            "claim": "A bare Majorana mass term for nu_R is allowed in the current model branch.",
            "reason": "Exact B-L forbids it, and no B-L = +2 compensator exists.",
            "evidence": [
                _evidence(sources["g89a"], "DIRAC_ONLY_ALLOWED"),
                _evidence(sources["g89b"], "DIRAC_ONLY_CONFIRMED"),
            ],
        },
    ]

    no_go_routes = [
        {
            "route": "Standard gauge reduction",
            "checked_by": "G84A",
            "verdict": "FAIL_FOR_INVERSE_SQUARE",
            "why_failed": "Unwarped reduction yields positive powers (+12/+6), not 1/rho6^2.",
            "revive_needed": "A non-standard gauge kinetic function or additional dilaton/warp/duality prefactor.",
            "evidence": [_evidence(sources["g84a"], "DERIVED_POSITIVE_POWER_STANDARD_ANSATZ")],
        },
        {
            "route": "Spectral / proper-time",
            "checked_by": "G84B, G85A",
            "verdict": "FORMS_ONLY",
            "why_failed": "The inverse-square form appears only at integrand level; no final A*exp(-lambda/rho6^2) term is derived.",
            "revive_needed": "A determinant or resummation step that produces a fixed effective exponential coefficient.",
            "evidence": [
                _evidence(sources["g85a"], "POISSON_THETA_FORM_ONLY"),
                _evidence(sources["g88f"], "INSUFFICIENT_ACTION"),
            ],
        },
        {
            "route": "Poisson / theta resummation",
            "checked_by": "G85A",
            "verdict": "BRIDGE_MISSING",
            "why_failed": "A theta/Poisson identity exists, but it does not close the bridge to the inverse-square effective term.",
            "revive_needed": "A final identification of the resummed expression with a rho6-dependent effective potential term.",
            "evidence": [_evidence(sources["g85a"], "POISSON_THETA_FORM_ONLY")],
        },
        {
            "route": "Saddle / worldline",
            "checked_by": "G85B",
            "verdict": "NULL",
            "why_failed": "The saddle gives exp(-3)=const, not exp(-lambda/rho6^2).",
            "revive_needed": "A rho6-dependent saddle that survives integration and produces the target functional form.",
            "evidence": [_evidence(sources["g85b"], "constant instead")],
        },
        {
            "route": "Dual modulus",
            "checked_by": "G86A",
            "verdict": "STRUCTURAL_POWER_LAW_ONLY",
            "why_failed": "Power-law T(rho6) always integrates to a power law, never to the desired inverse-square exponential.",
            "revive_needed": "A non-power-law modulus relation or a different UV mechanism.",
            "evidence": [_evidence(sources["g86a"], "power-law T(ρ₆) gives power-law")],
        },
        {
            "route": "Warp factor",
            "checked_by": "G86B",
            "verdict": "TRIVIAL_OR_CIRCULAR",
            "why_failed": "Uniform warp is trivial; localized warp becomes power-law plus free Q; the target form is circular.",
            "revive_needed": "A derived warp/dilaton equation with a genuine rho6-dependent exponential source.",
            "evidence": [_evidence(sources["g86b"], "free Q")],
        },
        {
            "route": "Dimensional lambda gate",
            "checked_by": "META-C1 / G83-G86B",
            "verdict": "PROMOTE_FREE_PARAMETER",
            "why_failed": "Buckingham-Pi style reasoning shows geometric lambda collapses to rho6^2 along the trajectory.",
            "revive_needed": "A non-geometric source for lambda.",
            "evidence": [_evidence(sources["null_index"], "lambda-dimensional-obstruction")],
        },
        {
            "route": "Physical mass ratio / canonical normalization",
            "checked_by": "G88D, G88E, G88F",
            "verdict": "INSUFFICIENT_ACTION",
            "why_failed": "No full reduced 4D action, no same-frame KK map, and only proxy-level masses are available.",
            "revive_needed": "A full 4D Einstein-frame reduced action with canonical radion and consistent KK/Planck/string normalization.",
            "evidence": [
                _evidence(sources["g88f"], "INSUFFICIENT_ACTION"),
                _evidence(sources["g88f"], "same-frame `M4/Ms` map are missing"),
            ],
        },
        {
            "route": "Majorana mass / neutrino seesaw",
            "checked_by": "G89A, G89B",
            "verdict": "DIRAC_ONLY_CONFIRMED",
            "why_failed": "Exact B-L forbids a bare Majorana mass and no B-L=+2 compensator exists.",
            "revive_needed": "An explicit B-L breaking sector or new operator with charge +2.",
            "evidence": [
                _evidence(sources["g89a"], "DIRAC_ONLY_ALLOWED"),
                _evidence(sources["g89b"], "DIRAC_ONLY_CONFIRMED"),
            ],
        },
    ]

    conditional_routes = [
        {
            "route": "External non-perturbative lambda origin",
            "status": "OPEN",
            "note": "Only a UV completion can supply a genuine non-perturbative source for exp(-lambda/rho6^2).",
            "evidence": evidence["lambda_free"],
        },
        {
            "route": "Full reduced 4D action",
            "status": "OPEN",
            "note": "Needed to upgrade the mass ratio from a proxy to a physical observable.",
            "evidence": evidence["mass_ratio_not_confirmed"],
        },
        {
            "route": "B-L breaking sector",
            "status": "OPEN",
            "note": "Required if the model is to support Majorana or seesaw neutrinos.",
            "evidence": evidence["dirac_only_neutrinos"],
        },
    ]

    uv_requirements = [
        "A mechanism for exp(-lambda/rho6^2).",
        "A source for lambda.",
        "A hidden gauge / brane / instanton sector or comparable UV origin.",
        "A full 4D reduced action.",
        "Canonical radion normalization.",
        "Same-frame KK scale.",
        "A B-L breaking sector if Majorana/seesaw neutrinos are desired.",
        "Otherwise an explicit Dirac-only neutrino prediction.",
    ]

    missing_inputs = [
        "A microscopic non-perturbative origin for lambda.",
        "A full reduced 4D Einstein-frame action.",
        "A canonical radion field and consistent mass extraction.",
        "A same-frame KK/Planck/string normalization map.",
        "A B-L=+2 operator or scalar if Majorana neutrinos are desired.",
    ]

    return {
        "verdict": "NO_GO_MAP_COMPLETE",
        "supported_claims": supported_claims,
        "unsupported_claims": unsupported_claims,
        "no_go_routes": no_go_routes,
        "conditional_routes": conditional_routes,
        "uv_requirements": uv_requirements,
        "lambda_origin_status": {
            "status": "FREE_COUPLING_PARAMETER",
            "summary": "Track B is exhausted; lambda is not derived in the current repository.",
            "evidence": evidence["lambda_free"],
        },
        "mass_ratio_status": {
            "status": "INSUFFICIENT_ACTION",
            "summary": "2.02% is a coordinate-curvature proxy; ~0.252% is a canonical proxy, but not a confirmed physical ratio.",
            "evidence": evidence["mass_ratio_not_confirmed"],
            "commits": ["9752c93"],
        },
        "neutrino_status": {
            "status": "DIRAC_ONLY_CONFIRMED",
            "summary": "Bare Majorana mass is forbidden by exact B-L in the current branch; Dirac-only is the current prediction.",
            "evidence": evidence["dirac_only_neutrinos"],
            "commits": ["7792811"],
        },
        "missing_inputs": missing_inputs,
        "next_required_gate": "External UV/string completion specification, not another internal GeoSpectra derivation gate.",
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# UV Completion Requirements and No-Go Map")
    lines.append("")
    lines.append("## Executive summary")
    lines.append("")
    lines.append(
        "GeoSpectra currently supports a disciplined phenomenological toy model, "
        "not a fully closed first-principles UV completion. The internal geometry "
        "and spectral analysis have exhausted the lambda-origin route, the physical "
        "mass-ratio route, and the neutrino Majorana route."
    )
    lines.append("")
    lines.append(
        "The right boundary condition for external work is now explicit: a UV/string "
        "completion must provide a mechanism for exp(-lambda/rho6^2), a full reduced "
        "4D action, a canonical radion, a same-frame KK scale, and (if desired) a "
        "B-L breaking sector."
    )
    lines.append("")
    lines.append("## What the current repository supports")
    lines.append("")
    lines.append("- A phenomenological spectral compactification toy model.")
    lines.append("- A derived SM-like one-generation structure from S^3 × S^6.")
    lines.append("- Exact N_gen = 3 from the G73/G74A/G74B chain.")
    lines.append("- Exact Dirac-only status for the current right-handed neutrino branch.")
    lines.append("- Lambda is tracked as FREE_COUPLING_PARAMETER, not as a derived quantity.")
    lines.append("")
    lines.append("## What the current repository does not support")
    lines.append("")
    lines.append("- A derived lambda origin from internal geometry or spectral data.")
    lines.append("- A confirmed physical m_mod/m_KK ratio from a full reduced 4D action.")
    lines.append("- A bare Majorana mass for nu_R in the current branch.")
    lines.append("")
    lines.append("## No-go map")
    lines.append("")
    lines.append("| Route | Checked by | Verdict | Why failed | What is needed to revive it |")
    lines.append("|---|---|---|---|---|")
    for route in result["no_go_routes"]:
        lines.append(
            f"| {route['route']} | {route['checked_by']} | {route['verdict']} | "
            f"{route['why_failed']} | {route['revive_needed']} |"
        )
    lines.append("")
    lines.append("## UV completion requirements")
    lines.append("")
    for idx, req in enumerate(result["uv_requirements"], start=1):
        lines.append(f"{idx}. {req}")
    lines.append("")
    lines.append("## Status of the three bottlenecks")
    lines.append("")
    lines.append(
        f"- Lambda origin: `{result['lambda_origin_status']['status']}` — "
        f"{result['lambda_origin_status']['summary']}"
    )
    lines.append(
        f"- Physical mass ratio: `{result['mass_ratio_status']['status']}` — "
        f"{result['mass_ratio_status']['summary']}"
    )
    lines.append(
        f"- Right-handed neutrino Majorana mass: `{result['neutrino_status']['status']}` — "
        f"{result['neutrino_status']['summary']}"
    )
    lines.append("")
    lines.append("## What would count as success")
    lines.append("")
    lines.append("- Show a real non-perturbative mechanism for exp(-lambda/rho6^2).")
    lines.append("- Derive lambda from that mechanism, not by convention.")
    lines.append("- Reconstruct a reduced 4D action and canonically normalize the radion.")
    lines.append("- Define the KK scale in the same frame and normalization as the mass.")
    lines.append("- If Majorana neutrinos are desired, add explicit B-L breaking.")
    lines.append("- If no B-L breaking is added, state Dirac-only neutrinos as the prediction.")
    lines.append("")
    lines.append("## Commit anchors")
    lines.append("")
    lines.append("- `9752c93` — `test(audit): close physical mass ratio as insufficient action`")
    lines.append("- `7792811` — `test(audit): close neutrino Majorana channel as Dirac-only`")
    lines.append("")
    lines.append("## Bottom line")
    lines.append("")
    lines.append(
        "The repository is strong as a phenomenological spectral toy model, but the "
        "stronger claims remain blocked until an external UV completion supplies the "
        "missing action, normalization, and non-perturbative input."
    )
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    RESULTS_PATH.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    NOTE_PATH.write_text(render_markdown(result), encoding="utf-8", newline="\n")


def main() -> int:
    result = build_result()
    write_outputs(result)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
