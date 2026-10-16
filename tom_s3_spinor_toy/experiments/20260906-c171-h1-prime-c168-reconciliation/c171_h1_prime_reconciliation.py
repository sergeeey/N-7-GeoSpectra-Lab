r"""C171 -- reconcile C170's derived holonomy H_1'=zeta_p^{-1} against C168's
own H_1=zeta_p convention, per C170's own Relaxation Map (decision.md SS8):
"attempt ONLY the holonomy-convention reconciliation next (does
H_1'=zeta_p^{-1} reproduce a dim-2 invariant-subspace-with-all-channels
classification identical to C168's, by the SAME T7-style generality argument
-- plausible, since zeta_p^{-1} is also order-3 with the same eigenvalue set,
but not yet checked)".

WHY this is expected to pass cleanly (not a blind guess): C168's own T8
(character theory) proves V (x) tau = dim(V) copies of the regular rep of
Z3, for ANY representation V of Z3 -- so ANY order-3 SU(2) element dropped
in for H_1 must give the same classification. zeta_p^{-1} is order exactly
3 whenever zeta_p is (inverses in a finite cyclic group have the same
order). This script CHECKS that expectation concretely for this SPECIFIC
substitution, rather than merely asserting it from the abstract theorem --
per this project's own discipline (a concrete check can catch a convention
error in either C168's or C170's own code that the abstract argument alone
would not reveal).

Method: reuse C168's own invariant_subspace_report() function via
importlib (not reimplemented), so this round cannot silently introduce a
DIFFERENT computation under the same name. H_1' is built two independent
ways (T1: closed-form zeta_p^{-1} exponential; T3: sympy .inv() of C168's
own zeta3 object) and cross-checked for exact agreement before use.

Run: python c171_h1_prime_reconciliation.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import sympy as sp

IMAG = sp.I
pi = sp.pi

# ---------------------------------------------------------------------------
# Load C168's own script as a module, so its invariant_subspace_report()
# function (and its own zeta3, tau objects) are REUSED, not reimplemented.
# ---------------------------------------------------------------------------

C168_DIR = Path(__file__).resolve().parent.parent / "20260906-c168-p4-step2-triality-correlation"
C168_SCRIPT = C168_DIR / "c168_triality_correlation_check.py"

spec = importlib.util.spec_from_file_location("c168_module", str(C168_SCRIPT))
c168_module = importlib.util.module_from_spec(spec)
sys.modules["c168_module"] = c168_module
spec.loader.exec_module(c168_module)  # runs C168's script top-level (its own __main__ guard
# prevents it from re-writing results_c168.json; only module-level assignments execute)

# ---------------------------------------------------------------------------
# T1 -- build H_1' = zeta_p^{-1}, closed form, same construction as C170's
#       own Step 5 (theta = 2*pi/p, zeta = diag(e^{i theta}, e^{-i theta})).
# ---------------------------------------------------------------------------

p_value = 3
theta = 2 * pi / p_value
zeta_p_closed_form = sp.Matrix([[sp.exp(IMAG * theta), 0], [0, sp.exp(-IMAG * theta)]])
H1_prime_closed_form = sp.simplify(zeta_p_closed_form.inv())

H1_prime_cubed = sp.simplify(H1_prime_closed_form**3)
H1_prime_is_order_3 = (sp.simplify(H1_prime_cubed - sp.eye(2)) == sp.zeros(2, 2)) and (
    sp.simplify(H1_prime_closed_form - sp.eye(2)) != sp.zeros(2, 2)
)

# ---------------------------------------------------------------------------
# T3 (adversarial cross-check, run before T2 so a mismatch here invalidates
#     T2 rather than being silently glossed over) -- recompute H_1' directly
#     as C168's own zeta3 object inverted, confirm exact agreement with the
#     closed-form construction above. Also confirm this matches C170's own
#     already-reported zeta_p_inverse (transcribed from C170's results_c170.json
#     for cross-reference, not re-imported, since C170's script does not
#     expose it as a reusable module-level function).
# ---------------------------------------------------------------------------

H1_prime_from_c168_zeta3_inv = sp.simplify(c168_module.zeta3.inv())

cross_check_closed_form_vs_c168_zeta3_inv = sp.simplify(
    H1_prime_closed_form - H1_prime_from_c168_zeta3_inv
) == sp.zeros(2, 2)

# C170's own results_c170.json step5.zeta_p_inverse (string form, for
# human cross-reference only -- the load-bearing check is the symbolic
# equality above, not a string comparison).
c170_results_path = (
    Path(__file__).resolve().parent.parent
    / "20260906-c170-p4-step3-item1-explicit-ker-ds3"
    / "results_c170.json"
)
c170_reported_zeta_p_inverse_str = None
if c170_results_path.exists():
    with open(c170_results_path, encoding="utf-8") as fh:
        c170_results = json.load(fh)
    c170_reported_zeta_p_inverse_str = c170_results["step5_holonomy_vs_c168_convention"][
        "zeta_p_inverse"
    ]

# ---------------------------------------------------------------------------
# T2 -- the main check: substitute H_1' for C168's H_1 in C168's OWN reused
#       invariant_subspace_report() function, compare against C168's own
#       already-computed t=1 sector (H_1=zeta_p).
# ---------------------------------------------------------------------------

sector_t1_prime = c168_module.invariant_subspace_report(
    H1_prime_closed_form, c168_module.tau, "t=1 (H_1'=zeta_p^{-1}, C171 reconciliation)"
)

# C168's own already-computed t=1 sector (H_1=zeta_p), reused for comparison,
# not recomputed.
sector_t1_c168_original = c168_module.sector_t1

dimension_matches = (
    sector_t1_prime["dim_invariant_eigenvalue_1_subspace"]
    == sector_t1_c168_original["dim_invariant_eigenvalue_1_subspace"]
)
classification_matches = (
    sector_t1_prime["classification"] == sector_t1_c168_original["classification"]
)
classification_is_expected_nonexclusive = (
    sector_t1_prime["classification"] == "NON-EXCLUSIVE-ALL-THREE-PARTICIPATE"
)

# ---------------------------------------------------------------------------
# Kill-criterion evaluation (per claim.md)
# ---------------------------------------------------------------------------

h1_prime_malformed = not H1_prime_is_order_3
reconciliation_confirmed = (
    (not h1_prime_malformed)
    and dimension_matches
    and classification_matches
    and classification_is_expected_nonexclusive
    and cross_check_closed_form_vs_c168_zeta3_inv
)
reconciliation_failed = (not h1_prime_malformed) and (
    not dimension_matches or not classification_matches
)

if h1_prime_malformed:
    verdict = "AMBIGUOUS-OR-INCONCLUSIVE"
    verdict_reason = "H_1' failed its own order-exactly-3 sanity check -- substitution itself is malformed, not a physics finding."
elif not cross_check_closed_form_vs_c168_zeta3_inv:
    verdict = "AMBIGUOUS-OR-INCONCLUSIVE"
    verdict_reason = "Closed-form H_1' does not match C168's own zeta3.inv() -- the two constructions of 'zeta_p^{-1}' disagree, ambiguous which one C170 meant."
elif reconciliation_confirmed:
    verdict = "RECONCILIATION-CONFIRMED"
    verdict_reason = (
        "H_1'=zeta_p^{-1} reproduces C168's own dim-2, "
        "NON-EXCLUSIVE-ALL-THREE-PARTICIPATE classification exactly, "
        "as predicted by C168's own T8 character-theory theorem."
    )
elif reconciliation_failed:
    verdict = "RECONCILIATION-FAILED"
    verdict_reason = (
        "Dimension or classification MISMATCH found -- contradicts C168's "
        "own T8 theorem as applied to this concrete substitution; requires "
        "careful re-examination, likely a coding bug in one of the two "
        "reused functions rather than a new physics finding."
    )
else:
    verdict = "AMBIGUOUS-OR-INCONCLUSIVE"
    verdict_reason = "Neither CONFIRMED nor FAILED conditions cleanly met -- report raw results for manual review."

results = {
    "T1_H1_prime_construction": {
        "H1_prime_closed_form": str(H1_prime_closed_form),
        "H1_prime_cubed": str(H1_prime_cubed),
        "H1_prime_is_order_exactly_3": bool(H1_prime_is_order_3),
    },
    "T3_cross_check_two_constructions_of_H1_prime": {
        "H1_prime_from_c168_zeta3_inv": str(H1_prime_from_c168_zeta3_inv),
        "matches_closed_form_construction": bool(cross_check_closed_form_vs_c168_zeta3_inv),
        "c170_reported_zeta_p_inverse_string_for_reference": c170_reported_zeta_p_inverse_str,
    },
    "T2_reused_c168_invariant_subspace_report": {
        "sector_t1_prime_H1_is_zeta_p_inverse": sector_t1_prime,
        "sector_t1_c168_original_H1_is_zeta_p": sector_t1_c168_original,
        "dimension_matches": bool(dimension_matches),
        "classification_matches": bool(classification_matches),
        "classification_is_expected_NON_EXCLUSIVE_ALL_THREE_PARTICIPATE": bool(
            classification_is_expected_nonexclusive
        ),
    },
    "verdict": {
        "value": verdict,
        "reason": verdict_reason,
    },
}

if __name__ == "__main__":
    print(json.dumps(results, indent=2, default=str, ensure_ascii=False))
    with open("results_c171.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, default=str, ensure_ascii=False)
    print("\nSaved: results_c171.json")
