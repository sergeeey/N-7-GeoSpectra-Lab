"""
C161 -- does C136's already-certified joint generalized-Killing-spinor
construction, recombined with C133's own Phi = 1_F (x) (lambda_0 w_0 + lambda_1
w_1) coupling language (decision.md SS9, w_0/w_1 spanning the two S3
t-sectors), let "all->both" be DERIVED as a genuine nonzero, channel-equal
pair (lambda_0, lambda_1) -- rather than remaining "the assumed Pati-Salam
content" C133 SS8a explicitly declined to derive?

REUSES, does NOT modify, c136_joint_killing_spinor_check.py: imports its
module directly (mu_of, nabla_t_ops, solve_cell, channel_inputs, CHANNELS) and
calls only its already-certified functions. No new S3/S6 geometry is built
here -- see decision.md for why the "missing S6 twisted operator" (C136 SS8
assumption 6) turns out NOT to be the actual missing ingredient.

THE ACTUAL FINDING (see decision.md for the full argument): C133's abstract
Phi never states WHICH of C136's two S3 frames (left-invariant / right-
invariant) plays the role of "w_0" (the t=0 sector) versus "w_1" (the t=1
sector). C136's own SS5 table has TWO frame entries at EACH t, so there are
FOUR equally literal ways to pick (w_0, w_1) as a pair of C136 table cells,
and this file computes the (lambda_0, lambda_1) pair each of the four gives.
No principle establishing which pairing is the physically correct one exists
anywhere in this project's certified content (checked against C133, C136,
E-L3B and G73/G74A/G74B this session) -- inventing one now would be new
physics content, not a mechanical recombination of already-built artifacts.

Run:  python c161_lambda_recombination_scoping_check.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

TOL = 1e-9
CHECKS: list[dict] = []
DATA: dict[str, object] = {}


def _load_c136_module():
    """Import c136_joint_killing_spinor_check.py by path (sibling experiment
    directory, not a package) without a module-level import, so this stays
    ruff-clean (E402) regardless of which rule set a given invocation enables."""
    c136_dir = os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "20260902-c136-joint-killing-spinor-constraint",
        )
    )
    spec = importlib.util.spec_from_file_location(
        "c136_joint_killing_spinor_check",
        os.path.join(c136_dir, "c136_joint_killing_spinor_check.py"),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


c136 = _load_c136_module()


def check(name: str, cond, detail: str = "") -> bool:
    ok = bool(cond)
    CHECKS.append({"name": name, "ok": ok, "detail": detail})
    if not ok:
        print(f"  [FAIL] {name} :: {detail}")
    return ok


def is_zero(x: float, tol: float = TOL) -> bool:
    return abs(x) < tol


# --------------------------------------------------------------------------
# 1. Reading (i) -- C136's own "pairing law" (D2/D4/E3/F5): lambda(t) =
#    mu(t,rho,frame) * chi4 * chi6. This is the ONLY quantity in C136 that has
#    literally the same shape as C133's Phi (a scalar times channel/sector
#    data). Show lambda_0 := lambda(t=0) and lambda_1 := lambda(t=1) are
#    IDENTICALLY ZERO -- and, crucially, that this holds for EVERY chi4/chi6
#    value, not just +-1, so the still-unbuilt S6-side value cannot change it.
# --------------------------------------------------------------------------
def section_1_reading_i():
    print("1. Reading (i): lambda(t) = mu(t)*chi4*chi6, at t=0 and t=1")

    mu0_left = c136.mu_of(0.0, 1.0, +1)  # left-invariant frame, the one C5
    mu1_right = c136.mu_of(1.0, 1.0, -1)  # right-invariant frame, the one C6
    DATA["mu_at_t0_left"] = mu0_left
    DATA["mu_at_t1_right"] = mu1_right
    check(
        "1a_mu_vanishes_at_its_own_parallel_point",
        is_zero(mu0_left) and is_zero(mu1_right),
        "reproduces C136 C5/C6: mu(0, left) = mu(1, right) = 0 -- this is "
        "what 'parallel at that (t,frame)' MEANS, already certified in C136, "
        "not recomputed here.",
    )

    # Sweep chi4, chi6 over a wide range -- not just +-1 -- including a value
    # taken from this project's own already-computed S6 twisted-operator
    # output (dolan-casimir-g2su3 decision.md Round 4-5: "D(v_a) = D(v_b) =
    # -sqrt(3)*w exactly", a genuine nonzero constant this project's S6
    # twisted-Dirac-operator machinery has produced -- NOT literally C136's
    # chi6 variable, used here only to show the conclusion is insensitive to
    # ANY finite S6-side number, real machinery-derived or not).
    sqrt3 = 3.0**0.5
    chi6_values = [+1.0, -1.0, +2.5, -0.37, sqrt3, -sqrt3, 1000.0]
    chi4_values = [+1.0, -1.0]
    lambda_0_vals, lambda_1_vals = [], []
    for chi4 in chi4_values:
        for chi6 in chi6_values:
            lambda_0_vals.append(mu0_left * chi4 * chi6)
            lambda_1_vals.append(mu1_right * chi4 * chi6)
    DATA["reading_i_lambda_0_sweep_all_zero"] = all(is_zero(v) for v in lambda_0_vals)
    DATA["reading_i_lambda_1_sweep_all_zero"] = all(is_zero(v) for v in lambda_1_vals)
    check(
        "1b_lambda_0_and_lambda_1_are_zero_for_every_chi4_chi6_swept",
        all(is_zero(v) for v in lambda_0_vals) and all(is_zero(v) for v in lambda_1_vals),
        f"{len(chi4_values) * len(chi6_values)} (chi4,chi6) combinations, including "
        f"+-sqrt(3) (this project's own g2su3 twisted-operator output, cited not "
        f"recomputed) and a large 1000.0 -- lambda_0 = lambda_1 = 0 * chi4 * chi6 = 0 "
        "in every case. WHY: mu(t) itself, not chi4*chi6, is what vanishes at these "
        "two points, so the still-unbuilt S6-side value is ALGEBRAICALLY IRRELEVANT "
        "to this reading's answer -- 0 times anything finite is 0.",
    )
    check(
        "1c_reading_i_is_the_channel_uniform_null_route",
        c136.channels_uniform(),
        "reproduces C136 E1 directly (imported, not recomputed): the chi6 input is "
        "identical across all 3 channels regardless, so reading (i)'s "
        "lambda_0=lambda_1=0 conclusion is trivially the same for 8_v, 8_s, 8_c.",
    )


# --------------------------------------------------------------------------
# 2. Reading (ii) -- C136's own SS5 3x2 table (the one claim.md's Intervention
#    section literally cites as "already computed"). There are FOUR literal
#    ways to read off (lambda_0, lambda_1) as (alpha at t=0 sector, alpha at
#    t=1 sector), because EACH t has TWO frame entries in the table and
#    nothing in C133 or C136 states which frame is "w_0" / "w_1". Compute all
#    four and show they land in THREE different cells of claim.md's own
#    5-outcome kill-criterion table.
# --------------------------------------------------------------------------
def section_2_reading_ii_four_pairings():
    print("2. Reading (ii): the four literal (w_0, w_1) pairings from C136's own table")

    cells = {}
    for ch in c136.CHANNELS:
        cells[ch] = {
            (t, frame): c136.alpha_from_residual(t, sf, +1, c136.channel_inputs(ch)["chi6"])
            for t in (0.0, 1.0)
            for sf, frame in ((+1, "left"), (-1, "right"))
        }
    DATA["alpha_by_channel_t_frame"] = {
        ch: {f"t={t}|{frame}": v for (t, frame), v in d.items()} for ch, d in cells.items()
    }

    # Channel-uniformity check on the raw table itself (cheap, direct evidence
    # that whatever pairing we pick, the channel axis contributes nothing).
    ref = cells["8_v"]
    channel_uniform_table = all(
        all(is_zero(cells[ch][k] - ref[k]) for k in ref) for ch in c136.CHANNELS[1:]
    )
    check(
        "2a_raw_alpha_table_is_channel_uniform",
        channel_uniform_table,
        "all four (t,frame) cells agree across 8_v/8_s/8_c to within TOL -- so "
        "WHICHEVER of the four pairings below is picked, the channel axis is inert; "
        "the only live question is the FRAME-SELECTION axis, not the channel axis.",
    )

    pairings = {
        "A_natural_natural": (cells["8_v"][(0.0, "left")], cells["8_v"][(1.0, "right")]),
        "B_twisted_twisted": (cells["8_v"][(0.0, "right")], cells["8_v"][(1.0, "left")]),
        "C_natural_twisted": (cells["8_v"][(0.0, "left")], cells["8_v"][(1.0, "left")]),
        "D_twisted_natural": (cells["8_v"][(0.0, "right")], cells["8_v"][(1.0, "right")]),
    }
    DATA["four_pairings_lambda0_lambda1"] = {k: list(v) for k, v in pairings.items()}

    def classify(l0: float, l1: float) -> str:
        z0, z1 = is_zero(l0), is_zero(l1)
        if z0 and z1:
            return "NULL-DEGENERATE (both zero)"
        if z0 != z1:
            return "NULL-CONTRADICTS-LABEL (exactly one zero)"
        return "PROMOTE-AS-DERIVATION-shaped (both nonzero)"

    verdicts = {k: classify(*v) for k, v in pairings.items()}
    DATA["four_pairings_verdicts"] = verdicts
    n_distinct_verdicts = len(set(verdicts.values()))
    check(
        "2b_the_four_literal_pairings_span_multiple_kill_criterion_outcomes",
        n_distinct_verdicts >= 3,
        f"pairings and verdicts: {verdicts}. {n_distinct_verdicts} distinct outcomes "
        "from claim.md's own 5-row kill-criterion table, depending SOLELY on which "
        "frame is arbitrarily assigned to w_0 vs w_1 -- a choice neither C133 nor "
        "C136 makes. This is the file's central finding: the recombination is "
        "underdetermined by already-certified content, not merely unfinished.",
    )


# --------------------------------------------------------------------------
def main():
    print("=" * 74)
    print("C161 -- lambda_0/lambda_1 recombination scoping check")
    print("=" * 74)
    section_1_reading_i()
    section_2_reading_ii_four_pairings()

    n_ok = sum(1 for c in CHECKS if c["ok"])
    n = len(CHECKS)
    print("-" * 74)
    print(f"CHECKS: {n_ok}/{n} passed")
    print()
    print("MACHINE-SUPPORTED FINDING (interpretation in decision.md):")
    print("  Reading (i) [C136's named 'pairing law']: lambda_0 = lambda_1 = 0")
    print("  identically, for EVERY finite chi4/chi6 -- the missing S6 value is")
    print("  algebraically irrelevant to this reading.")
    print("  Reading (ii) [C136's own SS5 table]: FOUR literal (w_0,w_1) pairings")
    print("  exist (frame choice at each t is unstated by both C133 and C136), and")
    print("  they span >= 3 distinct outcomes of claim.md's kill-criterion table.")
    print("  VERDICT: INCOMPLETE-MACHINERY -- the missing ingredient is a frame-")
    print("  selection PRINCIPLE, not the S6 twisted operator (shown irrelevant in")
    print("  section 1).")

    out = {
        "checks_total": n,
        "checks_passed": n_ok,
        "all_passed": n_ok == n,
        "checks": CHECKS,
        "data": DATA,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_c161.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nwrote {path}")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
