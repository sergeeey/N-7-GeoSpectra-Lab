"""C129 -- deliberate-error injections, to show the gate of
`c129_pin_structure_mapping_torus.py` can actually FAIL.

C128's skeptic finding A1 was that a gate collected only keys ending `_ok` and
therefore could not fail on its own two headline items.  This file is the
standing answer: each injection corrupts exactly one load-bearing quantity, in a
scratch copy, and records which gate checks fire.

An injection that is NOT caught is reported as such -- it is a finding about the
gate, not about the mathematics.
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

SRC = pathlib.Path(__file__).resolve().parent / "c129_pin_structure_mapping_torus.py"

INJECTIONS = {
    # 1. the clutching function's sign: M_iota = +Ad instead of -Ad
    "clutching_sign_flipped": (
        "err_iota.append(np.linalg.norm(frame_transition(iota, x) + Ad(x)))",
        "err_iota.append(np.linalg.norm(frame_transition(iota, x) - Ad(x)))",
    ),
    # 2. the Pin^+ / Pin^- criteria swapped (exactly the error claim.md contains)
    "pin_criteria_swapped": (
        (
            '        "Pin_plus": bool(_f2_is_zero(w2)),\n'
            '        "Pin_minus": bool(_f2_is_zero(w2 + w1sq)),'
        ),
        (
            '        "Pin_plus": bool(_f2_is_zero(w2 + w1sq)),\n'
            '        "Pin_minus": bool(_f2_is_zero(w2)),'
        ),
    ),
    # 3. the mapping-torus builder loses the (f_# - id) term -> H_* becomes
    #    that of the PRODUCT X x S^1 for every monodromy
    "monodromy_term_dropped": (
        "M[t_a + i, j] = fdeg[n - 1][i, j] - (1 if i == j else 0)",
        "M[t_a + i, j] = 0",
    ),
    # 4. the F_2 rank routine always returns 0 -> every H_*(;F_2) inflates
    "f2_rank_always_zero": (
        "    rank, ncols = 0, (len(M[0]) if M else 0)",
        "    rank, ncols = 0, 0",
    ),
    # 5. the quaternion embedding sign is hard-coded again (the defect gate G28
    #    actually caught while this round was being written)
    "embedding_sign_hardcoded": (
        "S = spin_elt(x, e, s_ok if s_ok else +1)",
        "S = spin_elt(x, e, +1)",
    ),
    # 6. HEADLINE-MOVING injection.  Both FL Step 8a skeptic passes observed that
    #    injections 1-5 leave every VERDICT_INPUTS field byte-identical: they
    #    show the gate CAN fail, not that the gate GUARDS THE CONCLUSION.  The
    #    reason was that M_iota's minimal CW model has no 2-cells, so H_2 = 0
    #    survives any corruption of the linear algebra.  With the non-minimal
    #    model added, dropping the boundary of a 'b' generator changes the rank
    #    of D_2/D_3 and therefore moves H_2 itself.
    "boundary_of_b_generator_dropped": (
        "M[t_a + i, a_dim + j] = d[n][i, j]",
        "M[t_a + i, a_dim + j] = 0",
    ),
    # 7. the F_2 reduction in pin_verdict reverted to a plain integer expand --
    #    the bug the gate caught during this round's own repair (see _f2_reduce).
    "pin_verdict_forgets_mod2": (
        '        "Pin_minus": bool(_f2_is_zero(w2 + w1sq)),',
        '        "Pin_minus": bool(sp.expand(w2 + w1sq) == 0),',
    ),
    # 8. pin_verdict reverted to the ORIGINAL boolean form both passes rejected.
    "pin_verdict_boolean_form_restored": (
        '        "Pin_minus": bool(_f2_is_zero(w2 + w1sq)),',
        '        "Pin_minus": bool(_f2_is_zero(w2) == _f2_is_zero(w1sq)),',
    ),
}

# Fields whose corruption would change the ROUND'S ANSWER, not merely trip a gate.
HEADLINE_FIELDS = (
    "w2_zero",
    "w1_squared_zero",
    "Pin_plus_exists",
    "Pin_minus_exists",
    "H2_M_iota_F2_nonminimal_model",
)

base = SRC.read_text(encoding="utf-8")
report: dict[str, object] = {}

for name, (old, new) in INJECTIONS.items():
    assert old in base, f"injection anchor not found: {name}"
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "inj.py"
        p.write_text(base.replace(old, new, 1), encoding="utf-8")
        subprocess.run(
            [sys.executable, str(p)], capture_output=True, text=True, check=False
        )
        res = json.loads(
            (pathlib.Path(td) / "results_c129.json").read_text(encoding="utf-8")
        )
    failed = [k for k, v in res["GATE"].items() if not v]
    report[name] = {
        "gate": res["GATE_PASSED"],
        "ALL_OK": res["ALL_OK"],
        "caught": not res["ALL_OK"],
        "checks_that_fired": failed,
        "verdict_inputs_under_injection": res["VERDICT_INPUTS"],
        # recorded separately because "the gate fired" and "the ANSWER moved"
        # are different facts, and the first draft of this harness conflated them
        "headline_fields_moved": [],  # filled after the baseline is read
    }

# baseline: the uncorrupted run must pass
res0 = json.loads((SRC.parent / "results_c129.json").read_text(encoding="utf-8"))
base_v = res0["VERDICT_INPUTS"]
for name in INJECTIONS:
    v = report[name]["verdict_inputs_under_injection"]
    report[name]["headline_fields_moved"] = [
        f for f in HEADLINE_FIELDS if v.get(f) != base_v.get(f)
    ]

report["BASELINE_uncorrupted"] = {
    "gate": res0["GATE_PASSED"],
    "ALL_OK": res0["ALL_OK"],
    "VERDICT_INPUTS": base_v,
}
report["ALL_INJECTIONS_CAUGHT"] = all(
    v["caught"] for k, v in report.items() if k in INJECTIONS
)
# The stronger property both skeptic passes asked for: at least one injection
# must move an actual headline field, otherwise the suite only shows that the
# gate can fail, never that it guards the conclusion.
report["AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE"] = any(
    report[k]["headline_fields_moved"] for k in INJECTIONS
)
report["INJECTIONS_THAT_MOVE_THE_HEADLINE"] = {
    k: report[k]["headline_fields_moved"]
    for k in INJECTIONS
    if report[k]["headline_fields_moved"]
}

(SRC.parent / "results_c129_injections.json").write_text(
    json.dumps(report, indent=2), encoding="utf-8"
)
for k, v in report.items():
    print(f"{k}: {v}")
