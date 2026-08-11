"""C85 -- certified Peter-Weyl representation for S3's Dirac operator at
general level k, built from Meier (2011, arXiv:1103.4097, "Eigenspaces of
the Spin Dirac operator over S^3"), NOT from round67's own uncited
"Sire & Xu" attribution (see decision.md for the provenance correction --
Sire & Xu arXiv:2005.01448 is genuinely the source for the general product-
manifold Clifford-decoupling identity round67/round68 use elsewhere, but
contains NO S3-specific spectrum content at all; that citation had been
silently extended to also cover the multiplicity formula, which it does
not support).

Meier's construction (his eqs 6.1-6.4, verified directly against the PDF
this session, not from memory):
  - l_{e_i}: (k+1)x(k+1) matrices on basis |p>, p=0..k (the domain/orbital
    action, "Z_i(psi)" in Agricola's language):
      l_{e1}|p> = i(2p-k)|p>                                       (6.1)
      l_{e2}|p> = (p-k)|p+1> + p|p-1>                               (6.2)
      l_{e3}|p> = (p-1)i|p+1> - p*i|p-1>   ["literal", as printed]  (6.3)
    with |-1>=|k+1>=0.
  - "D-bar" = -sum_i l_{e_i} . e_i, where ". e_i" is RIGHT quaternion
    multiplication on the value factor (Delta_m).
  - Eq 6.4: (D-bar+k)(D-bar-(k+2)) = 0 -- eigenvalues -k (per-copy
    multiplicity k+2) and k+2 (per-copy multiplicity k); across all k+1
    "q"-copies (a trivial outer multiplicity space D-bar doesn't touch),
    totals become (k+1)(k+2) and k(k+1).
  - D = D-bar - 3/2 (eq 1.2).

SOURCE-VS-STRUCTURE ADJUDICATION (this round's core question, posed by an
external reviewer after the literal transcription failed structural
self-consistency checks starting at k=2): l as transcribed must be a
genuine sp(1)-representation, so [l_{e_i},l_{e_j}] = l_{[e_i,e_j]} =
2*l_{e_k} (cyclic) is a HARD, basis-independent algebraic requirement --
not optional. The literal (6.3) satisfies this at k=0,1 but fails at
k>=2. Hypothesis: the printed "(p-1)" coefficient is a transcription
error for "(p-k)" (matching (6.2)'s own "(p-k)" pattern) -- at k=1 these
are numerically IDENTICAL (p-1=p-k when k=1), which is exactly why k=1
passed every check "by accident" while k=2+ exposed the discrepancy. This
script tests literal vs repaired side by side for k=0..10, with bracket
residuals, the Casimir identity (Lemma 6.1), eq 6.4, and eigenvalue/
multiplicity matches -- plus a negative control that perturbs the
REPAIRED coefficient by a nonzero delta, to confirm the invariants break
immediately when they should (not just "any change looks fine").

Re-indexing to round67's own "n, sigma" labels (worked out in C85, not
previously established anywhere in this codebase): the sigma=-1 branch at
physical n is level k=n DIRECTLY (D=-(n+3/2), per-copy mult k+2=n+2,
total (n+1)(n+2)); the sigma=+1 branch at physical n is level k=n+1's
"+1/2" eigenvalue (D=(n+1)+1/2=n+3/2, per-copy mult k=n+1, total
(n+1)(n+2)). This is a genuinely new structural finding -- NEITHER of
C84's two candidate pictures (one combined space split in two, or two
independent scalar*I2 mirror copies) was correct; sigma selects between
ADJACENT Laplacian levels.

Quaternion multiplication is implemented from the raw Hamilton product
(4-real-component), not hand-derived -- the resulting 2x2 complex
matrices for right-multiplication by e1,e2,e3 are extracted
programmatically and cross-checked against i^2=j^2=k^2=-1, ij=k before use.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c85.json"


# ---------------------------------------------------------------------------
# Step 0: quaternion algebra, built from the raw Hamilton product (not by
# hand) -- right multiplication by e1=i, e2=j, e3=k, as 2x2 complex matrices
# acting on (a,b) in C^2 where q = a + b*j (a,b in C, "a"=w+x*i, "b"=y+z*i).
# ---------------------------------------------------------------------------


def hamilton_product(p: tuple, q: tuple) -> tuple:
    """(w,x,y,z) Hamilton product, exact via sympy Rationals/symbols."""
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return (w, x, y, z)


def verify_quaternion_relations() -> dict:
    """[VERIFIED-sympy] i^2=j^2=k^2=-1, ij=k, ji=-k."""
    i, j, k = (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
    neg_one = (-1, 0, 0, 0)
    checks = {
        "i_sq_eq_neg1": hamilton_product(i, i) == neg_one,
        "j_sq_eq_neg1": hamilton_product(j, j) == neg_one,
        "k_sq_eq_neg1": hamilton_product(k, k) == neg_one,
        "ij_eq_k": hamilton_product(i, j) == k,
        "ji_eq_negk": hamilton_product(j, i) == (0, 0, 0, -1),
    }
    checks["all_match"] = all(checks.values())
    return checks


def right_mult_matrix_on_ab(unit: tuple) -> sp.Matrix:
    """2x2 complex matrix for RIGHT multiplication by `unit`, extracted
    programmatically from the raw Hamilton product (no hand-derived
    coefficients), with an explicit complex-linearity check."""
    I_UNIT = sp.I
    aw, ax, bw, bx = sp.symbols("aw ax bw bx", real=True)
    q = (aw, ax, bw, bx)
    result = hamilton_product(q, unit)
    w, x, y, z = result
    a_prime = sp.expand(w + x * I_UNIT)
    b_prime = sp.expand(y + z * I_UNIT)
    m00 = sp.diff(a_prime, aw)
    m01 = sp.diff(a_prime, bw)
    m10 = sp.diff(b_prime, aw)
    m11 = sp.diff(b_prime, bw)
    M = sp.Matrix([[m00, m01], [m10, m11]])
    check_a = sp.expand((m00 * (aw + I_UNIT * ax) + m01 * (bw + I_UNIT * bx)) - a_prime)
    check_b = sp.expand((m10 * (aw + I_UNIT * ax) + m11 * (bw + I_UNIT * bx)) - b_prime)
    assert check_a == 0 and check_b == 0, (
        "right-mult map is not complex-linear -- construction error"
    )
    return sp.simplify(M)


# ---------------------------------------------------------------------------
# Step 1: l_{e_i} matrices, general k -- literal vs repaired (6.3)
# ---------------------------------------------------------------------------


def build_l_matrices(k: int, variant: str, delta: sp.Rational | int = 0) -> list[sp.Matrix]:
    """(k+1)x(k+1) matrices on basis |p>, p=0..k.

    variant "literal": l_{e3}'s |p+1> coefficient is (p-1), exactly as
      printed in the source PDF (verified character-for-character).
    variant "repaired": l_{e3}'s |p+1> coefficient is (p-k)+delta -- the
      Lie-bracket-consistent hypothesis; delta!=0 is the negative control.
    """
    dim = k + 1
    I_UNIT = sp.I
    l1 = sp.zeros(dim, dim)
    l2 = sp.zeros(dim, dim)
    l3 = sp.zeros(dim, dim)
    for p in range(dim):
        l1[p, p] = I_UNIT * (2 * p - k)  # eq 6.1
        if variant == "literal":
            l3_p1_coeff = p - 1
        elif variant == "repaired":
            l3_p1_coeff = (p - k) + delta
        else:
            raise ValueError(f"unknown variant: {variant}")
        if p + 1 <= k:
            l2[p + 1, p] += p - k  # eq 6.2, |p+1> coefficient
            l3[p + 1, p] += l3_p1_coeff * I_UNIT
        if p - 1 >= 0:
            l2[p - 1, p] += p  # eq 6.2, |p-1> coefficient
            l3[p - 1, p] += -p * I_UNIT  # eq 6.3, |p-1> coefficient (unchanged either variant)
    return [l1, l2, l3]


def bracket_residuals(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix) -> dict:
    """[l_{e1},l_{e2}]=2*l_{e3} (cyclic) -- hard requirement for a genuine
    sp(1)-representation, basis-independent."""
    r12 = sp.simplify(l1 * l2 - l2 * l1 - 2 * l3)
    r23 = sp.simplify(l2 * l3 - l3 * l2 - 2 * l1)
    r31 = sp.simplify(l3 * l1 - l1 * l3 - 2 * l2)
    dim = l1.shape[0]
    zero = sp.zeros(dim, dim)
    return {
        "bracket_12_holds": r12 == zero,
        "bracket_23_holds": r23 == zero,
        "bracket_31_holds": r31 == zero,
        "all_brackets_hold": (r12 == zero) and (r23 == zero) and (r31 == zero),
    }


def casimir_residual(k: int, l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix) -> dict:
    """Lemma 6.1: -(l1^2+l2^2+l3^2) = k(k+2)*Id."""
    dim = l1.shape[0]
    lhs = sp.simplify(-(l1 * l1) - (l2 * l2) - (l3 * l3))
    target = k * (k + 2) * sp.eye(dim)
    holds = sp.simplify(lhs - target) == sp.zeros(dim, dim)
    return {"casimir_holds_exactly": bool(holds)}


def build_dbar(l_mats: list[sp.Matrix], right_mult: list[sp.Matrix]) -> sp.Matrix:
    """D-bar = -sum_i l_{e_i} (x) (right mult by e_i), on the (p,r) basis."""
    dim_p = l_mats[0].shape[0]
    dbar = sp.zeros(2 * dim_p, 2 * dim_p)
    for l_mat, rmult in zip(l_mats, right_mult):
        dbar += sp.Matrix(sp.kronecker_product(l_mat, rmult))
    return -dbar


def verify_eq64(k: int, dbar: sp.Matrix) -> dict:
    """(D-bar+k)(D-bar-(k+2)) = 0 exactly (eq 6.4)."""
    dim = dbar.shape[0]
    lhs = (dbar + k * sp.eye(dim)) * (dbar - (k + 2) * sp.eye(dim))
    residual = sp.simplify(lhs)
    return {"eq64_holds_exactly": bool(residual == sp.zeros(dim, dim))}


def eigen_multiplicities(matrix_numeric: np.ndarray) -> list[tuple[float, int]]:
    eigvals = np.linalg.eigvals(matrix_numeric)
    rounded = sorted(float(np.real(v)) for v in eigvals)
    grouped: list[list[float | int]] = []
    for v in rounded:
        if grouped and abs(grouped[-1][0] - v) < 1e-6:
            grouped[-1][1] += 1
        else:
            grouped.append([v, 1])
    return [(v, m) for v, m in grouped]


def certify_level(
    k: int, right_mult: list[sp.Matrix], variant: str, delta: sp.Rational | int = 0
) -> dict:
    l1, l2, l3 = build_l_matrices(k, variant, delta=delta)
    brackets = bracket_residuals(l1, l2, l3)
    casimir = casimir_residual(k, l1, l2, l3)
    dbar = build_dbar([l1, l2, l3], right_mult)
    eq64 = verify_eq64(k, dbar)

    dbar_numeric = np.array(dbar.evalf().tolist(), dtype=complex)
    dbar_eigs = eigen_multiplicities(dbar_numeric)
    found = {round(v, 4): m for v, m in dbar_eigs}
    target_neg_k_mult = k + 2  # per-copy multiplicity (this script builds ONE q-copy)
    target_pos_k2_mult = k  # per-copy multiplicity
    neg_k_match = found.get(round(float(-k), 4)) == target_neg_k_mult
    pos_k2_match = found.get(round(float(k + 2), 4)) == target_pos_k2_mult if k > 0 else True

    certified = bool(
        brackets["all_brackets_hold"]
        and casimir["casimir_holds_exactly"]
        and eq64["eq64_holds_exactly"]
        and neg_k_match
        and pos_k2_match
    )
    return {
        "k": k,
        "variant": variant,
        "delta": str(delta),
        "dim": dbar.shape[0],
        "bracket_relations": brackets,
        "casimir": casimir,
        "eq64": eq64,
        "dbar_eigenvalues_with_multiplicity": dbar_eigs,
        "target_neg_k_multiplicity_per_copy": target_neg_k_mult,
        "target_pos_k2_multiplicity_per_copy": target_pos_k2_mult,
        "neg_k_multiplicity_matches": bool(neg_k_match),
        "pos_k2_multiplicity_matches": bool(pos_k2_match),
        "certification_passes": certified,
    }


def main() -> None:
    print("=== Step 0: quaternion relations, verified from raw Hamilton product ===")
    quat_check = verify_quaternion_relations()
    print(quat_check)
    assert quat_check["all_match"], "quaternion relations failed -- stop"

    right_mult = [right_mult_matrix_on_ab(u) for u in [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
    print("right-mult matrices (e1,e2,e3):", [m.tolist() for m in right_mult])

    K_RANGE = range(11)

    print("\n=== Step 1: LITERAL (6.3) as printed, k=0..10 ===")
    literal_results = {}
    for k in K_RANGE:
        r = certify_level(k, right_mult, "literal")
        literal_results[str(k)] = r
        print(
            f"  k={k}: brackets={r['bracket_relations']['all_brackets_hold']}, "
            f"casimir={r['casimir']['casimir_holds_exactly']}, eq64={r['eq64']['eq64_holds_exactly']}, "
            f"PASSES={r['certification_passes']}"
        )

    print("\n=== Step 2: REPAIRED (p-k) hypothesis, k=0..10 ===")
    repaired_results = {}
    for k in K_RANGE:
        r = certify_level(k, right_mult, "repaired", delta=0)
        repaired_results[str(k)] = r
        print(
            f"  k={k}: brackets={r['bracket_relations']['all_brackets_hold']}, "
            f"casimir={r['casimir']['casimir_holds_exactly']}, eq64={r['eq64']['eq64_holds_exactly']}, "
            f"PASSES={r['certification_passes']}"
        )

    print("\n=== Step 3: NEGATIVE CONTROL -- perturb repaired coeff by delta=1/2, k=1..5 ===")
    negative_control_results = {}
    for k in range(1, 6):
        r = certify_level(k, right_mult, "repaired", delta=sp.Rational(1, 2))
        negative_control_results[str(k)] = r
        print(
            f"  k={k} (delta=1/2): brackets={r['bracket_relations']['all_brackets_hold']}, "
            f"casimir={r['casimir']['casimir_holds_exactly']}, "
            f"PASSES={r['certification_passes']} (expect False)"
        )

    print("\n=== Step 4: round67 target crosscheck, from ACTUAL repaired-matrix eigenvalues ===")
    round67_check = {}
    for n in range(8):
        k_minus, k_plus = n, n + 1
        r_minus = repaired_results.get(str(k_minus)) or certify_level(
            k_minus, right_mult, "repaired"
        )
        r_plus = repaired_results.get(str(k_plus)) or certify_level(k_plus, right_mult, "repaired")
        target = n + 1.5
        found_minus = {round(v, 4): m for v, m in r_minus["dbar_eigenvalues_with_multiplicity"]}
        found_plus = {round(v, 4): m for v, m in r_plus["dbar_eigenvalues_with_multiplicity"]}
        # D = D-bar - 3/2; D-bar eigenvalue -k_minus -> D = -(n+3/2); D-bar eigenvalue k_plus+2 -> D = +(n+3/2)
        minus_dbar_eig = round(float(-k_minus), 4)
        plus_dbar_eig = round(float(k_plus + 2), 4)
        minus_mult_per_copy = found_minus.get(minus_dbar_eig)
        plus_mult_per_copy = found_plus.get(plus_dbar_eig)
        # TOTAL multiplicity = per-copy multiplicity * (k+1) q-copies (D-bar
        # is built on ONE q-copy here; q is a trivial multiplicity label
        # D-bar never touches, so the total scales linearly with copy count).
        minus_mult_total = (
            minus_mult_per_copy * (k_minus + 1) if minus_mult_per_copy is not None else None
        )
        plus_mult_total = (
            plus_mult_per_copy * (k_plus + 1) if plus_mult_per_copy is not None else None
        )
        target_mult = (n + 1) * (n + 2)
        matches = (
            minus_mult_total == target_mult
            and plus_mult_total == target_mult
            and (minus_dbar_eig - 1.5 == round(-target, 4))
            and (plus_dbar_eig - 1.5 == round(target, 4))
        )
        round67_check[str(n)] = {
            "n": n,
            "sigma_minus_D": minus_dbar_eig - 1.5,
            "sigma_minus_mult_per_copy": minus_mult_per_copy,
            "sigma_minus_mult_total": minus_mult_total,
            "sigma_plus_D": plus_dbar_eig - 1.5,
            "sigma_plus_mult_per_copy": plus_mult_per_copy,
            "sigma_plus_mult_total": plus_mult_total,
            "target_mult_n1n2": target_mult,
            "matches": bool(matches),
        }
        print(
            f"  n={n}: sigma=-1 D={minus_dbar_eig - 1.5} (total mult {minus_mult_total}), "
            f"sigma=+1 D={plus_dbar_eig - 1.5} (total mult {plus_mult_total}), "
            f"target_mult={target_mult}, matches={matches}"
        )

    all_repaired_pass = all(r["certification_passes"] for r in repaired_results.values())
    all_negative_rejected = all(
        not r["certification_passes"] for r in negative_control_results.values()
    )
    all_round67_match = all(r["matches"] for r in round67_check.values())
    literal_breaks_at_k2_plus = all(
        not literal_results[str(k)]["certification_passes"] for k in range(2, 11)
    )
    literal_passes_k01 = all(literal_results[str(k)]["certification_passes"] for k in (0, 1))

    print("\n=== Summary ===")
    print(f"literal (6.3) passes k=0,1: {literal_passes_k01}")
    print(f"literal (6.3) fails all k=2..10: {literal_breaks_at_k2_plus}")
    print(f"repaired (p-k) passes ALL k=0..10: {all_repaired_pass}")
    print(
        f"negative control (delta=1/2) correctly rejected for all tested k: {all_negative_rejected}"
    )
    print(f"round67 target eigenvalue/multiplicity matches confirmed n=0..7: {all_round67_match}")

    adjudication = (
        "REPAIR_CONFIRMED_LITERAL_IS_TRANSCRIPTION_ERROR"
        if (
            literal_passes_k01
            and literal_breaks_at_k2_plus
            and all_repaired_pass
            and all_negative_rejected
            and all_round67_match
        )
        else "ADJUDICATION_INCONCLUSIVE_DO_NOT_TRUST_EITHER_VARIANT"
    )

    results = {
        "quaternion_relations": quat_check,
        "literal_results": literal_results,
        "repaired_results": repaired_results,
        "negative_control_results": negative_control_results,
        "round67_crosscheck": round67_check,
        "literal_passes_k01": literal_passes_k01,
        "literal_breaks_at_k2_plus": literal_breaks_at_k2_plus,
        "all_repaired_pass": all_repaired_pass,
        "all_negative_rejected": all_negative_rejected,
        "all_round67_match": all_round67_match,
        "adjudication_verdict": adjudication,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nADJUDICATION VERDICT: {adjudication}")


if __name__ == "__main__":
    main()
