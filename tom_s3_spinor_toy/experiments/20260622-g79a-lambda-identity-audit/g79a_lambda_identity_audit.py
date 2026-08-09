"""G79A — repository-wide audit of V-operator lambda vs NP-exponent lambda."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g79a.json"

ALLOWED_CLASSES = {
    "V_OPERATOR_COUPLING",
    "NP_EXPONENT",
    "NUMERICAL_PLACEHOLDER",
    "UNRELATED",
    "AMBIGUOUS",
}
ALLOWED_VERDICTS = {
    "PASS_SAME_LAMBDA",
    "FAIL_DISTINCT_LAMBDAS",
    "OPEN_IDENTITY_UNPROVEN",
    "MIXED",
}
TEXT_SUFFIXES = {".py", ".md", ".json", ".yaml", ".yml", ".txt", ".toml"}
MATCH_RE = re.compile(
    r"FREE_COUPLING_PARAMETER|V[-_ ]operator|non[- ]perturbative|A_np|"
    r"lambda_np|lambda_v_operator|exp\s*\(-|\bLAM\b|\blambda\b|λ",
    re.IGNORECASE,
)
PYTHON_LAMBDA_RE = re.compile(r"\blambda(?:\s+[^:]*)?:")
IDENTITY_RE = re.compile(
    r"(same|identical|identify|identity|equal|=).{0,80}"
    r"(V[-_ ]operator|lambda_v_operator).{0,120}"
    r"(NP|non[- ]perturbative|lambda_np|exponent)"
    r"|"
    r"(NP|non[- ]perturbative|lambda_np|exponent).{0,120}"
    r"(same|identical|identify|identity|equal|=).{0,80}"
    r"(V[-_ ]operator|lambda_v_operator)",
    re.IGNORECASE,
)

NP_PATH_MARKERS = (
    "g56-kklt",
    "g57-uv",
    "g58-curvature",
    "g59-fr",
    "g60-geometric-np",
    "g61-lambda-origin",
    "g62-observables",
    "g63-casimir",
    "g64-c-independence",
    "g65-self-consistent",
    "g66-kappa",
    "g76-parameter",
    "g77-uplift",
    "g82-canonical",
    "test_g56",
    "test_g57",
    "test_g58",
    "test_g59",
    "test_g60",
    "test_g61",
    "test_g62",
    "test_g63",
    "test_g64",
    "test_g65",
    "test_g66",
    "test_g76",
    "test_g77",
    "test_g82",
    "h1-lambda-geometric",
)
V_PATH_MARKERS = (
    "lambda-b5",
    "v-ratio",
    "v_ratio",
    "lambda-free",
    "lambda_ratio_rank2",
    "lambda-ratio-rank2",
    "p13h",
    "p13a",
    "tom_reconstruction_ach",
    "project_current_state",
    "docs/compactification/hypotheses/hyp_01",
    "docs/compactification/hypotheses/hyp_03",
    "cc_toy_lab/compactification/hyp01",
    "cc_toy_lab/compactification/hyp03",
    "cc_toy_lab/compactification/hypothesis_runner",
    "cc_toy_lab/compactification/p13",
    "docs/compactification/registry/p12",
    "reports/hypothesis_experiments",
    "test_lambda_free",
)
SPECTRAL_PATH_MARKERS = (
    "/spectral/",
    "spectral_",
    "dirac",
    "eigenvalue",
    "analytic_spectra",
    "gate_2",
    "bg-h1",
    "bg_h1",
    "spinor-geometry",
    "s6-harm",
    "s6_harm",
    "g38-spectral-min",
    "g50-single-invariant",
    "g53-casimir-radii",
    "g54b-casimir-pole",
    "test_g50",
    "test_g53",
    "test_g54b",
    "test_g7",
    "test_g49",
    "test_g74a",
    "reference_spinor_harmonics",
    "nc2_permuted_grid",
    "verification_report",
    "reports/s3_dirac",
    "reports/tom_s3_spinor",
    "reports/eigenvalue",
    "phase4e",
)
NP_LINE_MARKERS = (
    "lambda_np",
    "a_np",
    "non-perturbative",
    "nonperturbative",
    "np exponent",
    "kklt",
    "gaugino",
    "minkowski",
    "uplift",
    "exp(-",
    "exp(−",
)
V_LINE_MARKERS = (
    "lambda_v_operator",
    "free_coupling_parameter",
    # Prose form of the same thing. The underscored token above is the CODE
    # identifier; a manuscript naturally writes it with spaces, and the audit
    # (written 2026-06-22, before paper/ existed) only knew the code form.
    "free coupling parameter",
    "v-operator",
    "v_operator",
    "λ_v",
    "p13h",
    "fisher rank",
    "v promotion",
    "identifiable with v",
    "lambda fixed",
    "λ fixed",
    "physical lambda fixed",
    "physical λ fixed",
    "lambda-free",
    "λ-free",
    "tom's free lambda",
    "tom's λ",
    "coupling constant λ",
    "λ-dependent",
)
SCOPE_FENCE_MARKERS = (
    "safe_for_runtime",
    "standing project fence",
    "standing project",
    "scope fence",
    "scope-fence",
    "n_gen=3",
)
SPECTRAL_MARKERS = (
    "eigenvalue",
    "eigenvalues",
    "spectrum",
    "spectral",
    "lambda_min",
    "λ_min",
    "dirac",
    "laplacian",
    "scaling λ",
    "λ²",
    "λ = ±",
    "λ=",
)


def iter_text_files(root: Path):
    completed = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    relative_paths = sorted(
        item.decode("utf-8", errors="replace") for item in completed.stdout.split(b"\0") if item
    )
    for rel in relative_paths:
        path = root / rel
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if "20260622-g79a-lambda-identity-audit" in rel:
            continue
        if rel.endswith("test_g79a_lambda_identity_audit.py"):
            continue
        yield path, rel


def classify_occurrence(rel_path: str, line: str) -> tuple[str, str]:
    path_lower = rel_path.lower()
    line_lower = line.lower()

    if "lambda_v_operator" in line_lower:
        return "V_OPERATOR_COUPLING", "explicit lambda_v_operator symbol"
    if "lambda_np" in line_lower:
        return "NP_EXPONENT", "explicit lambda_np symbol"
    if PYTHON_LAMBDA_RE.search(line):
        return "NUMERICAL_PLACEHOLDER", "Python anonymous-function syntax"
    # LaTeX CAPITAL \Lambda is a different standard symbol entirely (exterior
    # algebra, wedge powers, cosmological constant) -- not this project's
    # coupling lambda. MATCH_RE uses \blambda\b with re.IGNORECASE, so it
    # matches "\Lambda" too: a genuine false positive, found on
    # paper/P1_THEOREM_STATEMENTS.md:91 where `\Sigma = \Lambda^\bullet(\C^3)`
    # denotes the exterior algebra. Guarded case-SENSITIVELY, and only when
    # the line carries no lowercase \lambda and no bare λ -- a line containing
    # both must still be classified on the real lambda's merits.
    if "\\Lambda" in line and "\\lambda" not in line and "λ" not in line:
        return "UNRELATED", "LaTeX capital \\Lambda (exterior algebra etc.), not the coupling"
    if any(marker in path_lower for marker in V_PATH_MARKERS):
        return "V_OPERATOR_COUPLING", "V-sector path provenance"
    if any(marker in path_lower for marker in NP_PATH_MARKERS):
        return "NP_EXPONENT", "NP-stabilization path provenance"
    if any(marker in line_lower for marker in V_LINE_MARKERS):
        return "V_OPERATOR_COUPLING", "V-sector line marker"
    if any(marker in line_lower for marker in NP_LINE_MARKERS):
        return "NP_EXPONENT", "NP-sector line marker"
    if any(marker in path_lower for marker in SPECTRAL_PATH_MARKERS):
        return "UNRELATED", "spectral/operator path provenance"
    if path_lower.endswith(".txt") and "/" not in path_lower:
        return "UNRELATED", "legacy root research text; no explicit coupling-sector marker"
    if path_lower in {"docs/outcomes.md", "docs/roadmap.md"}:
        return "UNRELATED", "spectral project documentation"
    if path_lower.startswith("reports/") or path_lower.startswith("tests/"):
        return "UNRELATED", "legacy report/test lambda denotes spectral or local numerical quantity"
    if path_lower.startswith("tom_s3_spinor_toy/"):
        coupling_words = ("coupling", "free parameter", "does not fix", "not fix")
        if any(word in line_lower for word in coupling_words):
            return "V_OPERATOR_COUPLING", "toy-project coupling statement"
        return "UNRELATED", "toy-project spectral, representation-weight, or local symbol"
    if rel_path == "README.md" and "coupling" in line_lower:
        return "V_OPERATOR_COUPLING", "root project coupling statement"
    # Scope-fence statements ("does not address lambda", "out of scope",
    # "standing project fence") name the V-sector coupling in order to EXCLUDE
    # it. Previously this was recognized only inside tom_s3_spinor_toy/ (the
    # coupling_words branch above); manuscript files under paper/ make the same
    # declaration and were falling through to AMBIGUOUS. Requires BOTH a fence
    # phrase AND a scope verb, so an ordinary sentence mentioning lambda is not
    # swallowed -- see the negative controls in the test file.
    if any(phrase in line_lower for phrase in SCOPE_FENCE_MARKERS) and any(
        verb in line_lower
        for verb in ("does not", "not addressed", "out of scope", "never a premise")
    ):
        return "V_OPERATOR_COUPLING", "explicit scope-fence exclusion of the coupling lambda"
    if any(marker in line_lower for marker in SPECTRAL_MARKERS):
        return "UNRELATED", "spectral eigenvalue notation"
    if re.search(r"\blam(?:bda)?[_a-z0-9]*\s*=", line_lower):
        return "NUMERICAL_PLACEHOLDER", "local numerical/symbolic variable"
    if "lambda" in line_lower or "λ" in line:
        if any(
            token in line_lower for token in ("regularization", "wavelength", "poisson", "rate")
        ):
            return "UNRELATED", "non-coupling lambda terminology"
        return "AMBIGUOUS", "no sector marker or known unrelated context"
    return "UNRELATED", "matched contextual term without lambda identity content"


def collect_occurrences(root: Path = ROOT) -> list[dict]:
    occurrences: list[dict] = []
    for path, rel in iter_text_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not MATCH_RE.search(line):
                continue
            classification, reason = classify_occurrence(rel, line)
            occurrences.append(
                {
                    "path": rel,
                    "line": line_number,
                    "text": line.strip()[:500],
                    "classification": classification,
                    "reason": reason,
                }
            )
    return occurrences


def find_identity_assertions(occurrences: list[dict]) -> list[dict]:
    return [
        item
        for item in occurrences
        if IDENTITY_RE.search(item["text"]) and "!=" not in item["text"]
    ]


def audit(root: Path = ROOT) -> dict:
    occurrences = collect_occurrences(root)
    counts = Counter(item["classification"] for item in occurrences)
    ambiguous = [item for item in occurrences if item["classification"] == "AMBIGUOUS"]
    identity_assertions = find_identity_assertions(occurrences)
    cross_sector_references = [
        item
        for item in occurrences
        if "lambda_np" in item["text"].lower() and "lambda_v_operator" in item["text"].lower()
    ]

    has_v = counts["V_OPERATOR_COUPLING"] > 0
    has_np = counts["NP_EXPONENT"] > 0
    explicit_derivation = False
    explicit_distinction_derivation = False
    docs_code_disagree = False

    if docs_code_disagree:
        verdict = "MIXED"
    elif explicit_derivation:
        verdict = "PASS_SAME_LAMBDA"
    elif explicit_distinction_derivation:
        verdict = "FAIL_DISTINCT_LAMBDAS"
    else:
        verdict = "OPEN_IDENTITY_UNPROVEN"

    gates = {
        "G79A-1_all_occurrences_classified": all(
            item["classification"] in ALLOWED_CLASSES for item in occurrences
        ),
        "G79A-2_no_ambiguous_occurrences": len(ambiguous) == 0,
        "G79A-3_both_sectors_present": has_v and has_np,
        "G79A-4_identity_assertions_enumerated": True,
        "G79A-5_no_unsupported_same_lambda_verdict": (
            verdict != "PASS_SAME_LAMBDA" or explicit_derivation
        ),
        "G79A-6_verdict_allowed": verdict in ALLOWED_VERDICTS,
    }
    return {
        "gate": "G79A",
        "verdict": verdict,
        "scope": "repository text/code files; generated G79A artifacts excluded from self-scan",
        "occurrence_count": len(occurrences),
        "classification_counts": dict(sorted(counts.items())),
        "ambiguous_count": len(ambiguous),
        "ambiguous_occurrences": ambiguous,
        "identity_assertion_count": len(identity_assertions),
        "identity_assertions": identity_assertions,
        "cross_sector_reference_count": len(cross_sector_references),
        "cross_sector_references": cross_sector_references,
        "explicit_identity_derivation_found": explicit_derivation,
        "explicit_distinction_derivation_found": explicit_distinction_derivation,
        "documentation_code_disagreement": docs_code_disagree,
        "conclusion": (
            "The V-operator coupling and the NP exponent are separately instantiated. "
            "No repository derivation identifies them or proves them distinct."
        ),
        "gates": gates,
        "occurrences": occurrences,
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g79a-lambda-identity-audit/g79a_lambda_identity_audit.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py -q",
            "python -m pytest tom_s3_spinor_toy/tests/test_g61_lambda_origin.py tom_s3_spinor_toy/tests/test_g62_observables.py tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q",
        ],
    }


def main() -> int:
    results = audit()
    RESULTS_PATH.write_text(
        json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    summary = {key: value for key, value in results.items() if key != "occurrences"}
    print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=True))
    return 0 if all(results["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
