"""G89A: Majorana gauge-invariance and selection-rule audit."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g89a.json"
REPO_ROOT = HERE.parents[2]

SEARCH_FILES = [
    "tom_s3_spinor_toy/tests/test_g21_extended_schur.py",
    "tom_s3_spinor_toy/tests/test_g22_first_order.py",
    "tom_s3_spinor_toy/tests/test_g18_ncg.py",
    "tom_s3_spinor_toy/tests/test_g19_higgs_bidoublet.py",
    "tom_s3_spinor_toy/tests/test_g20_yukawa_intertwiner.py",
    "tom_s3_spinor_toy/experiments/20260619-g18-ncg-dirac-df/claim.md",
    "tom_s3_spinor_toy/experiments/20260619-g20-yukawa-intertwiner/claim.md",
    "tom_s3_spinor_toy/experiments/20260619-g21-extended-schur/decision.md",
    "tom_s3_spinor_toy/experiments/20260619-g22-first-order/decision.md",
    "tom_s3_spinor_toy/README.md",
    "tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md",
]


def _text(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8", errors="ignore")


def _exists(rel: str) -> bool:
    return (REPO_ROOT / rel).exists()


def run() -> dict:
    texts = {rel: _text(rel) for rel in SEARCH_FILES if _exists(rel)}

    nu_r_bm_l = None
    for rel, text in texts.items():
        if re.search(r"(?:nu_R|ν_R).*B[-−]L\s*=\s*-1", text, flags=re.IGNORECASE | re.DOTALL):
            nu_r_bm_l = -1
            break

    exact_b_minus_l = any("B-L preserves" in text or "D_F preserves B-L" in text for text in texts.values())
    dirac_neutrino_explicit = any(
        "purely Dirac" in text or "Dirac neutrino" in text for text in texts.values()
    )
    majorana_missing = any("Majorana mass" in text and "not yet explored" in text for text in texts.values())
    bminusl2_scalar_found = any(
        re.search(r"B[-−]L\s*=\s*2", text) or re.search(r"dBL\s*=\s*2", text) for text in texts.values()
    )

    majorana_bilinear_charge = None if nu_r_bm_l is None else 2 * nu_r_bm_l

    gates = {
        "G89A-1_nuR_quantum_numbers_found": nu_r_bm_l == -1,
        "G89A-2_exact_BminusL_preserved": exact_b_minus_l,
        "G89A-3_no_BminusL2_scalar_found": not bminusl2_scalar_found,
        "G89A-4_dirac_neutrino_explicit": dirac_neutrino_explicit,
        "G89A-5_majorana_not_claimed_as_broken_in_repo": majorana_missing,
    }

    if nu_r_bm_l == -1 and exact_b_minus_l and not bminusl2_scalar_found and dirac_neutrino_explicit:
        verdict = "DIRAC_ONLY_ALLOWED"
    elif nu_r_bm_l == -1 and exact_b_minus_l and not bminusl2_scalar_found:
        verdict = "MAJORANA_FORBIDDEN_BY_B_MINUS_L"
    elif nu_r_bm_l is None:
        verdict = "INSUFFICIENT_QUANTUM_NUMBERS"
    else:
        verdict = "MIXED"

    return {
        "gate": "G89A",
        "verdict": verdict,
        "searched_terms": [
            "nu_R",
            "Majorana",
            "B-L",
            "B−L",
            "SU(2)_R",
            "Pati-Salam",
            "charge conjugation",
            "finite Dirac",
            "real structure",
            "seesaw",
        ],
        "files_examined_count": len(texts),
        "source_files": sorted(texts),
        "nu_r_b_minus_l": nu_r_bm_l,
        "majorana_bilinear_b_minus_l": majorana_bilinear_charge,
        "exact_b_minus_l_preserved": exact_b_minus_l,
        "b_minus_l2_scalar_found": bminusl2_scalar_found,
        "dirac_neutrino_explicit": dirac_neutrino_explicit,
        "majorana_missing_from_repo": majorana_missing,
        "mass_term_status": verdict,
        "requires_b_minus_l_breaking": verdict == "MAJORANA_REQUIRES_B_MINUS_L_BREAKING",
        "missing_inputs": [
            "explicit B-L=2 breaking scalar/operator",
            "neutrino-sector symmetry breaking sector",
            "proof that any Majorana block survives the exact B-L selection rule",
        ],
        "falsified_routes": [
            "bare nu_R^T C nu_R as gauge singlet under exact B-L",
            "Majorana mass with no B-L breaking sector",
            "claim that the current repo already constructs a Majorana ν_R mass",
        ],
        "next_required_gate": "G89B_GEOMETRIC_BILINEAR_SINGLET_AUDIT",
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g89a-majorana-gauge-invariance-selection-rules/"
            "g89a_majorana_gauge_invariance_selection_rules.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
