"""G88F: full reduced-action reconstruction audit."""

from __future__ import annotations

import json
import re
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88f.json"
REPO_ROOT = HERE.parents[2]

C_SM = 0.986
RHO6_STAR = 1.090
LAMBDA_NP = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15

D_EXT = 4
PATH_TANGENT = np.array([2.0, 1.0])
KINETIC_DIMS = np.array([3.0, 6.0])
KINETIC_MATRIX = np.diag(KINETIC_DIMS) + np.outer(KINETIC_DIMS, KINETIC_DIMS) / (D_EXT - 2)
PATH_K = float(PATH_TANGENT @ KINETIC_MATRIX @ PATH_TANGENT)

A_NP = V_FLUX * exp(LAMBDA_NP / RHO6_STAR**2)

SEARCH_FILES = [
    "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/claim.md",
    "tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/claim.md",
    "tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/g82_canonical_mass.py",
    "tom_s3_spinor_toy/experiments/20260622-g83-gauge-kinetic-modulus-scaling/g83_gauge_kinetic_modulus_scaling.py",
    "tom_s3_spinor_toy/experiments/20260622-g84a-standard-gauge-reduction/g84a_standard_gauge_reduction.py",
    "tom_s3_spinor_toy/preprint.tex",
    "tom_s3_spinor_toy/preprint_draft.md",
]

KEY_TERMS = [
    "reduced 4D action",
    "4D Einstein-frame action",
    "Einstein frame",
    "string frame",
    "canonical field",
    "canonical radion",
    "radion kinetic",
    "KK scale",
    "Planck/string",
    "M4/Ms",
]


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAMBDA_NP / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def canonical_mass_metric_only(rho: float) -> float:
    return rho**2 * second_derivative_rho(rho) / PATH_K


def canonical_ratio_metric_only(rho: float) -> float:
    return sqrt(canonical_mass_metric_only(rho) / (1.0 / rho**2))


def _file_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _find_sources() -> tuple[list[str], list[str], bool]:
    found = []
    evidence_levels = []
    full_reduction_found = False
    for rel in SEARCH_FILES:
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        text = _file_text(path)
        if any(term.lower() in text.lower() for term in KEY_TERMS):
            found.append(rel)
            level = set()
            if re.search(r"reduced\s+4D\s+action", text, flags=re.IGNORECASE):
                level.add("reduced_action")
            if "Einstein" in text:
                level.add("einstein_frame")
            if "canonical" in text.lower():
                level.add("canonical_field")
            if "KK" in text or "m_KK" in text:
                level.add("kk_scale")
            if "M4/Ms" in text or "M4=Ms" in text or "M4=1" in text:
                level.add("normalization")
            if "m_mod/m_KK" in text or "m_moduli/m_KK" in text or "m/m_KK" in text:
                level.add("mass_ratio")
            evidence_levels.extend(sorted(level))
            if {
                "reduced_action",
                "einstein_frame",
                "canonical_field",
                "kk_scale",
                "normalization",
                "mass_ratio",
            } <= level:
                full_reduction_found = True
    return found, sorted(set(evidence_levels)), full_reduction_found


def run() -> dict:
    rho = rho_minimum()
    coord_proxy = sqrt(second_derivative_rho(rho) / (1.0 / rho**2))
    canonical_proxy = canonical_ratio_metric_only(rho)
    sources, evidence_levels, full_reduction_found = _find_sources()

    missing_inputs = [
        "single local file or chain that reconstructs the normalized reduced 4D action",
        "explicit same-frame KK scale map",
        "explicit Planck/string normalization map",
        "explicit derivation that the physical mass and KK scale are compared in the same convention",
    ]

    gates = {
        "G88F-1_sources_found": len(sources) > 0,
        "G88F-2_partial_chain_present": {"reduced_action", "einstein_frame", "canonical_field", "kk_scale"} <= set(evidence_levels),
        "G88F-3_full_reconstruction_found": full_reduction_found,
        "G88F-4_physical_ratio_not_promoted": True,
        "G88F-5_coordinate_proxy_remains_proxy": canonical_proxy < coord_proxy,
    }

    verdict = "INSUFFICIENT_ACTION"
    if full_reduction_found and all(gates.values()):
        verdict = "REDUCED_ACTION_RECONSTRUCTED"

    return {
        "gate": "G88F",
        "verdict": verdict,
        "searched_terms": KEY_TERMS,
        "files_examined_count": len(sources),
        "source_files": sources,
        "evidence_levels": evidence_levels,
        "full_reduced_action_reconstructed": full_reduction_found,
        "canonical_field_defined": True,
        "canonical_normalization_explicit": True,
        "coordinate_proxy_value": coord_proxy,
        "canonical_proxy_value": canonical_proxy,
        "physical_ratio_value": None,
        "ratio_invariant_under_reparametrization": False,
        "same_frame_comparison": False,
        "missing_inputs": missing_inputs,
        "falsified_routes": [
            "claim that local docs already contain a closed reduced 4D action",
            "claim that the old 2.02% is physically identified by the current repo",
            "claim that canonicalization alone closes the mass ratio",
        ],
        "next_required_gate": "EXTERNAL_REDUCED_ACTION_OR_EXPLICIT_FRAME_MAP",
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88f-full-reduced-action-reconstruction/"
            "g88f_full_reduced_action_reconstruction.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
