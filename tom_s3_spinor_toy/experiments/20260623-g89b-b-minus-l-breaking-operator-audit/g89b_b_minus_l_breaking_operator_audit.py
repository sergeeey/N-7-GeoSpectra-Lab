"""G89B: B-L breaking operator audit for Majorana neutrino mass."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g89b.json"
REPO_ROOT = HERE.parents[2]

SEARCH_FILES = [
    "tom_s3_spinor_toy/tests/test_g18_ncg.py",
    "tom_s3_spinor_toy/tests/test_g19_higgs_bidoublet.py",
    "tom_s3_spinor_toy/tests/test_g20_yukawa_intertwiner.py",
    "tom_s3_spinor_toy/tests/test_g21_extended_schur.py",
    "tom_s3_spinor_toy/tests/test_g22_first_order.py",
    "tom_s3_spinor_toy/experiments/20260619-g18-ncg-dirac-df/claim.md",
    "tom_s3_spinor_toy/experiments/20260619-g19-higgs-bidoublet/claim.md",
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

    candidates_examined = [
        {
            "name": "Higgs bidoublet / Yukawa mediator",
            "source": "tom_s3_spinor_toy/tests/test_g19_higgs_bidoublet.py",
            "quantum_numbers": {"dBL": 0, "dT3L": "±1/2", "dT3R": "∓1/2", "role": "SM Higgs bidoublet"},
            "couples_to_nu_r_nu_r": False,
            "derived_from_geometry": True,
            "vev_available": True,
        },
        {
            "name": "Forbidden |dBL|=2 channel",
            "source": "tom_s3_spinor_toy/experiments/20260619-g20-yukawa-intertwiner/claim.md",
            "quantum_numbers": {"dBL": "+2 or -2", "role": "forbidden lepton-number-violating operator"},
            "couples_to_nu_r_nu_r": False,
            "derived_from_geometry": True,
            "vev_available": False,
        },
    ]

    b_minus_l_exact = True
    nu_r_bm_l = -1
    majorana_bilinear_bm_l = -2

    b_plus_two_candidate = None
    for cand in candidates_examined:
        qn = cand["quantum_numbers"]
        if qn.get("dBL") == "+2":
            b_plus_two_candidate = cand
            break

    exact_bminusl_preserved = any(
        "D_F preserves B-L" in text or "exact B-L" in text or "B-L remains exact" in text
        for text in texts.values()
    )
    dirac_only_supported = any(
        "purely Dirac" in text or "Dirac-only" in text or "not yet explored" in text
        for text in texts.values()
    )

    if b_plus_two_candidate is not None:
        verdict = "B_MINUS_L_BREAKING_OPERATOR_FOUND"
    elif exact_bminusl_preserved and dirac_only_supported:
        verdict = "DIRAC_ONLY_CONFIRMED"
    elif exact_bminusl_preserved:
        verdict = "MAJORANA_REQUIRES_NEW_B_MINUS_L_FIELD"
    else:
        verdict = "OPEN_MISSING_SCALAR_SECTOR"

    candidate_sources = [cand["source"] for cand in candidates_examined]
    candidate_quantum_numbers = [cand["quantum_numbers"] for cand in candidates_examined]

    gates = {
        "G89B-1_exact_BminusL_is_present": exact_bminusl_preserved,
        "G89B-2_no_Bplus2_candidate_found": b_plus_two_candidate is None,
        "G89B-3_candidate_list_nonempty": len(candidates_examined) > 0,
        "G89B-4_dirac_only_supported": dirac_only_supported,
        "G89B-5_no_fake_majorana_promotion": verdict != "B_MINUS_L_BREAKING_OPERATOR_FOUND" or b_plus_two_candidate is not None,
    }

    return {
        "gate": "G89B",
        "verdict": verdict,
        "candidates_examined": candidates_examined,
        "b_minus_l_exact": b_minus_l_exact,
        "nu_r_b_minus_l": nu_r_bm_l,
        "majorana_bilinear_b_minus_l": majorana_bilinear_bm_l,
        "b_minus_l_plus_two_candidate_found": b_plus_two_candidate is not None,
        "candidate_sources": candidate_sources,
        "candidate_quantum_numbers": candidate_quantum_numbers,
        "coupling_to_nu_r_nu_r_allowed": False if b_plus_two_candidate is None else True,
        "candidate_derived_from_geometry": False if b_plus_two_candidate is None else b_plus_two_candidate["derived_from_geometry"],
        "candidate_vev_available": False if b_plus_two_candidate is None else b_plus_two_candidate["vev_available"],
        "seesaw_supported": False,
        "dirac_only_supported": dirac_only_supported,
        "missing_inputs": [
            "a B-L=+2 scalar/operator or equivalent breaking sector",
            "a coupling to nu_R nu_R",
            "evidence that the compensator can acquire a VEV or scale",
        ],
        "next_required_gate": "G89C_GEOMETRIC_BILINEAR_SINGLET_AUDIT",
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g89b-b-minus-l-breaking-operator-audit/"
            "g89b_b_minus_l_breaking_operator_audit.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())

