"""TOM-CERT-01 negative controls: damaged copies of certificate.json must be rejected.

Each mutant is built from the valid certificate by a small edit that models one mistake
(wrong sign, permuted indices, broken closure, tiny perturbation, malformed literal, emptied or
truncated fields, a verifier that implements a different but self-consistent convention). The
verifier runs as a separate process. A control passes only if the exit code matches what was
declared here BEFORE running AND every declared check id is among the failing checks (a single
damage may legitimately trip further checks; those are printed as `also failed`, not hidden).
Exit-2 controls declare a regular expression that the MALFORMED message must match.

Positive controls: the unmodified certificate and a copy with all keys reversed are accepted.
Usage: python negative_controls.py [certificate.json]      exit 0 = every control behaved as declared
"""

import copy
import json
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "verifier.py"


def neg(pair):
    return [str(-F(pair[0])), str(-F(pair[1]))]


def conj(pair):
    return [pair[0], str(-F(pair[1]))]


def mats_map(mats, fn):
    return [[[fn(e) for e in row] for row in m] for m in mats]


def transpose(m):
    return [list(r) for r in zip(*m)]


def mutants(cert):
    out = []

    def add(
        name, fn, expect_exit, expect_fail=(), expect_msg=None, skip=None, note="", verifier=None
    ):
        c = copy.deepcopy(cert)
        c = fn(c) or c
        out.append((name, c, expect_exit, set(expect_fail), expect_msg, skip, note, verifier))

    def setter(path, value):
        def f(c):
            d = c
            for k in path[:-1]:
                d = d[k]
            d[path[-1]] = value

        return f

    add("P0_valid_certificate", lambda c: None, 0, note="positive control")
    add(
        "P1_keys_reversed",
        lambda c: dict(reversed(list(c.items()))),
        0,
        note="positive control (key order is irrelevant)",
    )

    add(
        "N1a_wrong_sign_dL",
        lambda c: c.__setitem__("dL", [mats_map([m], neg)[0] for m in c["dL"]]),
        1,
        ["V2b_dL_matrices", "V4_algebra"],
        note="sign of the left action flipped: also violates [X_a,X_b] = +eps X_c",
    )

    def swap_inverse(c):
        g = c["group_elements"]
        for i in range(0, len(g), 2):
            g[i]["L_matrix"], g[i + 1]["L_matrix"] = g[i + 1]["L_matrix"], g[i]["L_matrix"]

    add(
        "N1b_wrong_sign_group_L",
        swap_inverse,
        1,
        ["V3a_group_L", "V3e_convention_equivariance"],
        note="claims (L_h f)(x) = f(h x) instead of f(h^-1 x): h and h^-1 swapped",
    )
    add(
        "N2a_transposed_dR",
        lambda c: c.__setitem__("dR", [transpose(m) for m in c["dR"]]),
        1,
        ["V2c_dR_matrices"],
        note="indices of the right-action matrices permuted (M -> M^T)",
    )
    add(
        "N2b_rows_instead_of_columns",
        setter(["decomposition", "left_blocks"], [[0, 1], [2, 3]]),
        1,
        ["V5a_invariant_blocks"],
        note="left doublets claimed as fixed ROW span{g_a0,g_a1} instead of fixed column",
    )

    def swap_labels(c):
        c["basis"][1], c["basis"][2] = c["basis"][2], c["basis"][1]

    add(
        "N2c_swapped_basis_labels",
        swap_labels,
        1,
        ["V1_basis_definition"],
        note="g01 and g10 exchanged in the declared basis",
    )

    def swap_weights(c):
        w = c["decomposition"]["weights_J3L_J3R"]
        w[1], w[2] = w[2], w[1]

    add(
        "N2d_permuted_weights",
        swap_weights,
        1,
        ["V6_casimir_weights"],
        note="weights of g01, g10 exchanged",
    )

    def break_closure(c):
        c["basis"][3] = [[[1, 0, 1, 0], "1", "0"]]  # |x0|^2, quadratic: replaces g11

    add(
        "N3a_broken_closure_V1_skipped",
        break_closure,
        1,
        ["V2a_closure"],
        skip="V1_basis_definition",
        note="g11 replaced by |x0|^2; with V1 skipped, the closure check itself must catch it",
    )
    add(
        "N3b_broken_closure_full_run",
        break_closure,
        1,
        ["V1_basis_definition", "V2a_closure"],
        note="same damage, nothing skipped",
    )

    def tiny(c):
        c["dL"][0][0][0][0] = str(F(c["dL"][0][0][0][0]) + F(1, 10**30))

    add(
        "N4_perturbation_1e-30",
        tiny,
        1,
        ["V2b_dL_matrices"],
        note="one entry changed by 10^-30: exact arithmetic must still reject (a float test would not)",
    )
    add(
        "N5_wrong_casimir_claim",
        setter(["decomposition", "casimir_L"], "1/2"),
        1,
        ["V6_casimir_weights"],
        note="claims j(j+1) = 1/2",
    )
    add(
        "N6_decimal_literal",
        setter(["dL", 0, 0, 0, 0], "0.5"),
        2,
        expect_msg=r"not an exact rational literal",
        note="non-rational literal",
    )
    add(
        "N7_non_unit_quaternion",
        setter(["group_elements", 0, "quaternion"], [1, 1, 1, 1, 3]),
        2,
        expect_msg=r"not a unit rational quaternion",
        note="not an element of SU(2)",
    )

    # --- emptied / truncated / never-read fields (found by the independent skeptic review) ---
    def empty_group_mats(c):
        for e in c["group_elements"]:
            e["L_matrix"], e["R_matrix"] = [], []

    add(
        "M1_empty_group_matrices",
        empty_group_mats,
        1,
        ["V3a_group_L", "V3b_group_R"],
        note="claimed matrices []",
    )

    def trunc_group(c):
        for e in c["group_elements"]:
            e["L_matrix"] = e["L_matrix"][:1]

    add(
        "M1b_truncated_group_matrix",
        trunc_group,
        1,
        ["V3a_group_L"],
        note="only the first row of each L matrix",
    )
    add(
        "M2_no_group_elements",
        setter(["group_elements"], []),
        2,
        expect_msg=r"at least 6",
        note="group layer would be vacuous",
    )
    add(
        "M3_no_homomorphism_pairs",
        setter(["homomorphism_pairs"], []),
        2,
        expect_msg=r"at least 4",
        note="homomorphism layer would be vacuous",
    )
    add(
        "M4a_empty_weights",
        setter(["decomposition", "weights_J3L_J3R"], []),
        1,
        ["V6_casimir_weights"],
    )

    def extra_weight(c):
        c["decomposition"]["weights_J3L_J3R"].append(["7", "-9"])

    add("M4b_garbage_extra_weight", extra_weight, 1, ["V6_casimir_weights"])
    add("M5a_empty_gram", setter(["gram"], []), 1, ["V7_gram_unitarity"])
    add("M5b_one_entry_gram", setter(["gram"], [["1/2"]]), 1, ["V7_gram_unitarity"])
    add("M6_empty_generators", setter(["generators"], []), 1, ["V2gen_generators"])
    add(
        "M7_right_block_reordered",
        setter(["decomposition", "right_blocks"], [[0, 1], [3, 2]]),
        1,
        ["V5b_doublets_irreducible"],
        note="second right block listed in the wrong order",
    )

    def extra_block(c):
        c["decomposition"]["left_blocks"].append([])

    add("M8_extra_empty_block", extra_block, 1, ["V5a_invariant_blocks"])

    def bool_claims(c):
        d = c["decomposition"]["commutant_dim"]
        d["full_LR"], d["left_only"], d["right_only"] = True, 4.0, 4.0

    add(
        "M9_bool_float_commutant_claims",
        bool_claims,
        1,
        ["V5c_commutants"],
        note="True == 1 and 4.0 == 4 in Python",
    )

    def dup_monomial(c):
        c["basis"][0] = [[[1, 0, 0, 0], "5", "0"], [[1, 0, 0, 0], "1", "0"]]

    add("M10_duplicate_monomial", dup_monomial, 2, expect_msg=r"duplicate monomial")

    def pad_dL(c):
        c["dL"] = [[row + [["0", "0"]] for row in m] for m in c["dL"]]

    add("M11_matrix_padded_to_4x5", pad_dL, 2, expect_msg=r"4x4")
    add(
        "M12_decimal_quaternion",
        setter(["group_elements", 0, "quaternion"], ["0.6", "0.8", "0", "0", "1"]),
        2,
        expect_msg=r"not an integer",
    )
    add(
        "M13_zero_denominator",
        setter(["gram", 0, 0], "1/0"),
        1,
        ["V7_gram_unitarity"],
        note="no crash, no exit-1 ambiguity",
    )
    add("M14a_trailing_newline", setter(["gram", 0, 0], "1/2\n"), 1, ["V7_gram_unitarity"])
    add("M14b_arabic_digits", setter(["gram", 0, 0], "١/٢"), 1, ["V7_gram_unitarity"])
    add(
        "M15_negative_pair_index",
        setter(["homomorphism_pairs", 0], [-1, 0]),
        2,
        expect_msg=r"out of range",
    )
    add(
        "M17_false_conventions_text",
        setter(["conventions", "L"], "(L_h f)(x) = f(h x)"),
        1,
        ["V0_statement"],
        note="the declared conventions are part of the statement",
    )

    def conj_group(c):
        for e in c["group_elements"]:
            for key in ("L_matrix", "R_matrix"):
                e[key] = [[conj(x) for x in row] for row in e[key]]

    add(
        "N8_other_homomorphic_convention",
        conj_group,
        1,
        ["V3e_convention_equivariance"],
        verifier="swap",
        note=(
            "verifier modified to implement L_h f = f(h^T x), R_k f = f(x.conj(k)) (also homomorphisms); "
            "certificate group matrices conjugated to match; the homomorphism checks cannot tell, "
            "the closed-form/equivariance check must"
        ),
    )
    return out


def swapped_verifier_source():
    src = VERIFIER.read_text(encoding="utf-8")
    a = "sub = left_sub(mdag(h))"
    b = "sub = right_sub(k)"
    assert src.count(a) == 1 and src.count(b) == 1, "verifier source layout changed"
    src = src.replace(a, "sub = left_sub([[h[0][0], h[1][0]], [h[0][1], h[1][1]]])")
    return src.replace(b, "sub = right_sub(mconj(k))")


def run_verifier(verifier, path, skip):
    cmd = [sys.executable, str(verifier), str(path)]
    if skip:
        cmd += ["--skip-checks", skip]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    failed = set(re.findall(r"^FAIL (\S+):", p.stdout, re.M))
    return p.returncode, failed, p.stdout


def main(argv):
    cert_path = Path(argv[1]) if len(argv) > 1 else HERE / "certificate.json"
    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    bad = []
    with tempfile.TemporaryDirectory() as td:
        swapped = Path(td) / "verifier_swapped.py"
        swapped.write_text(swapped_verifier_source(), encoding="utf-8")
        for name, c, want_exit, want_fail, want_msg, skip, note, which in mutants(cert):
            p = Path(td) / f"{name}.json"
            p.write_text(json.dumps(c), encoding="utf-8")
            code, failed, out = run_verifier(swapped if which == "swap" else VERIFIER, p, skip)
            ok = code == want_exit and want_fail <= failed
            if want_exit == 0:
                ok = ok and not failed
            if want_msg:
                ok = ok and re.search(want_msg, out) is not None
            extra = sorted(failed - want_fail)
            print(
                f"{'OK  ' if ok else 'BAD '} {name}: exit {code} (declared {want_exit}); "
                f"declared={sorted(want_fail) or want_msg or '-'}; also failed={extra} -- {note}"
            )
            if not ok:
                bad.append(name)
    print(f"CONTROLS: {'ALL BEHAVED AS DECLARED' if not bad else 'MISBEHAVED: ' + ','.join(bad)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
