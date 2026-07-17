r"""
Round 72 (E7) -- H1 sub-question kill-test: is t=0 / t=1 (the exact n=0 zero-mode
crossings found by E2, experiments/20260717-round67-e2-s3-torsion-deformation/)
a stationary point / symmetry-distinguished point of some INDEPENDENTLY MOTIVATED
quantity, checked WITHOUT reference to the Dirac operator or its zero-mode condition?

Context: E2 found ker(D_S3(t)) != 0 at t in {-2/3,-1/3,0,1,4/3,5/3} (n=0,1,2). Both
E2 and E3 explicitly flagged that NO physical principle was known for selecting
t=0/t=1 over t=1/2 (Levi-Civita) -- picking t=0 *because* it kills KT-8 would be
exactly the FITTED-vs-DERIVED trap this project's CLAUDE.md warns against (the
G56/lambda=0.30 lesson). claim.md (this folder) freezes 4 rival hypotheses
(H1 Killing spinor / H2 EOM / H3 anomaly cancellation / H4 free parameter) BEFORE
running this script. This script tests ONLY the cheapest sub-question of H1:
does Agricola's OWN classification of the connection family Nabla^t (arXiv:math/0202094,
Section 2 -- established via curvature/Ricci-tensor computations, BEFORE the Dirac
operator is even introduced in Section 3) single out t=0 and t=1 for a reason that
has NOTHING to do with spinors or zero modes?

Two facts read directly from the PDF this session (see claim.md/decision.md for
full page citations):
  (a) t=0 is Agricola's "canonical connection" Nabla^0 -- by the Ambrose-Singer
      theorem, the UNIQUE metric connection on M with Nabla^0 T^0 = Nabla^0 R^0 = 0
      (torsion AND curvature parallel). [PDF p.3, Section 2, para after eq(1)]
  (b) t=1 is what Agricola calls the "anticanonical connection" -- she introduces
      this name specifically because it has the SAME Ricci tensor as the canonical
      connection (t=0). [PDF p.5, right after Lemma 2.2]
  (c) Remark 4.2 / Theorem 4.4 [PDF p.19-20]: for the general Ricci tensor
      Ric^t(X,Y) = (t-t^2)*beta(X,Y) + (2t^2-2t+1)*A(X,Y), "the coefficient of beta
      vanishes for t=0 and t=1, and is positive between these parameter values" --
      an explicit, PURELY ALGEBRAIC (t-t^2) factor, established from curvature
      alone, with zero reference to Dirac operators.

None of (a)-(c) mention spinors, Dirac operators, or zero modes anywhere in their
derivation. This script INDEPENDENTLY verifies, by direct symbolic computation on
S3 = SU(2)/{e} (H = {e} trivial -- the SAME presentation E2 used, m = g = su(2)),
that the FULL curvature tensor R^t (not just its trace/Ricci part) of the family
Nabla^t vanishes IDENTICALLY as an operator if and only if t(t-1) = 0, i.e.
t in {0,1} -- exactly and only these two values, for ANY nonzero structure
constant (any actual S3, not a coincidence of a particular normalization). This is
the sharper, stronger statement behind (a)-(c): t=0 and t=1 are not merely
"Ricci-distinguished" but are the exact Cartan-Schouten "+/- connections" -- the
two FLAT (R=0 identically, not just Ricci-flat) affine connections that exist on
any Lie group with a bi-invariant metric (Cartan & Schouten 1926; here re-derived
from Agricola's own curvature formula (Lemma 2.2) plus the Jacobi identity, not
assumed).

This script does NOT touch spinors, Clifford algebra, or the Dirac operator at
all -- by design (H1's sub-question requires an INDEPENDENT criterion). It reuses
this project's own established Lie-algebra convention for S3=SU(2)/{e} (m=g=su(2),
orthonormal basis Z1,Z2,Z3, single independent structure constant
c := <[Z1,Z2]_m,Z3> = 2, established in E2 via h_H=3=(3/2)*c calibrated against
this project's own [VERIFIED-sympy, G8/G4] n=0 eigenvalue 3/2) -- but the central
result (R^t=0 iff t(t-1)=0) is verified to hold for GENERIC symbolic c != 0, i.e.
it does not depend on that specific calibration at all.

Run:  python round72_t_selection_check.py
"""

from __future__ import annotations

import json

import sympy as sp

t, c = sp.symbols("t c")


# ---------------------------------------------------------------------------
# Step 0: su(2) structure constants (abstract Lie bracket on m = g, H = {e}
# trivial -- same presentation E2 used). [Zi,Zj]_m = c * epsilon_ijk * Zk.
# c is kept SYMBOLIC (generic nonzero) throughout the main derivation so the
# result is not an artifact of one particular metric normalization; the
# project's own established value c=2 (from E2's h_H=3=(3/2)*c) is plugged in
# only at the end as a concrete cross-check.
# ---------------------------------------------------------------------------


def eps(i: int, j: int, k: int) -> int:
    """Levi-Civita symbol, 1-indexed i,j,k in {1,2,3}."""
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    perm = p[:]
    n = 3
    for x in range(n):
        for y in range(n - 1 - x):
            if perm[y] > perm[y + 1]:
                perm[y], perm[y + 1] = perm[y + 1], perm[y]
                sign = -sign
    return sign


def bracket_m(X: sp.Matrix, Y: sp.Matrix) -> sp.Matrix:
    """[X,Y]_m for X,Y given as 3x1 coefficient vectors in the Z1,Z2,Z3 basis.
    Since H={e} is trivial, m=g and this IS the full Lie bracket -- there is no
    separate h-component to split off anywhere in this script (h=0 identically).
    """
    out = sp.zeros(3, 1)
    for i in range(3):
        xi = X[i]
        if xi == 0:
            continue
        for j in range(3):
            yj = Y[j]
            if yj == 0:
                continue
            coeff = xi * yj
            for k in range(3):
                e = eps(i + 1, j + 1, k + 1)
                if e:
                    out[k] += coeff * c * e
    return sp.simplify(out)


def basis_vec(i: int) -> sp.Matrix:
    v = sp.zeros(3, 1)
    v[i] = 1
    return v


Z = [basis_vec(i) for i in range(3)]


def jacobi_identity_check() -> bool:
    """Sanity control: [X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]] == 0 for ALL basis triples.
    This is a GENERAL Lie-algebra fact (must hold for ANY bracket built this way);
    if this control fails, the bracket_m() implementation itself is broken and
    nothing below can be trusted.
    """
    ok = True
    for i in range(3):
        for j in range(3):
            for k in range(3):
                X, Y, W = Z[i], Z[j], Z[k]
                jac = (
                    bracket_m(X, bracket_m(Y, W))
                    + bracket_m(Y, bracket_m(W, X))
                    + bracket_m(W, bracket_m(X, Y))
                )
                if sp.simplify(jac) != sp.zeros(3, 1):
                    ok = False
    return ok


# ---------------------------------------------------------------------------
# Step 1: curvature R^t(X,Y)Z of Nabla^t, specialized to H={e} trivial.
# Agricola Lemma 2.2 (general reductive case):
#   R^t(X,Y)Z = t^2[X,[Y,Z]_m]_m + t^2[Y,[Z,X]_m]_m + t[Z,[X,Y]_m]_m + [Z,[X,Y]_h]
# For H={e}: h=0 identically, so [X,Y]_h = 0 for EVERY X,Y and [.,.]_m = [.,.]
# (the full bracket, since m=g). This is what is coded below -- the [Z,[X,Y]_h]
# term is dropped because it is identically zero for this presentation, not
# because it is assumed small.
# ---------------------------------------------------------------------------


def curvature_Rt(X: sp.Matrix, Y: sp.Matrix, W: sp.Matrix) -> sp.Matrix:
    """R^t(X,Y)W, general symbolic t (h=0 case, so the Jac_h term is dropped
    exactly, not approximately)."""
    term1 = t**2 * bracket_m(X, bracket_m(Y, W))
    term2 = t**2 * bracket_m(Y, bracket_m(W, X))
    term3 = t * bracket_m(W, bracket_m(X, Y))
    return sp.simplify(term1 + term2 + term3)


def S_term(X: sp.Matrix, Y: sp.Matrix, W: sp.Matrix) -> sp.Matrix:
    """S(X,Y,Z) := [X,[Y,Z]] + [Y,[Z,X]] -- the coefficient that R^t(X,Y)Z
    reduces to once R^t is factored as t(t-1)*S(X,Y,Z) (derived below using the
    Jacobi identity to eliminate the linear-in-t term; NOT assumed, verified by
    direct comparison in the exhaustive check)."""
    return sp.simplify(bracket_m(X, bracket_m(Y, W)) + bracket_m(Y, bracket_m(W, X)))


def exhaustive_flatness_check() -> dict[str, object]:
    """For ALL 27 ordered basis triples (i,j,k), verify:
    (A) R^t(Zi,Zj)Zk == t*(t-1)*S(Zi,Zj,Zk) EXACTLY (symbolic identity in t,c)
    (B) hence R^t(Zi,Zj)Zk == 0 for t=0 and t=1, for EVERY triple, regardless of c
    (C) at least one triple has S(Zi,Zj,Zk) != 0 for c != 0 (i.e. the vanishing
        at t=0,1 is a genuine, non-vacuous constraint -- R^t is NOT identically
        zero for t outside {0,1})
    """
    factorization_holds = True
    vanishes_at_0_and_1 = True
    max_abs_S_at_generic_t: list[tuple[int, int, int, sp.Matrix]] = []
    nonzero_example = None
    per_triple: list[dict[str, object]] = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                X, Y, W = Z[i], Z[j], Z[k]
                Rt = curvature_Rt(X, Y, W)
                S = S_term(X, Y, W)
                predicted = sp.simplify(t * (t - 1) * S)
                matches = sp.simplify(Rt - predicted) == sp.zeros(3, 1)
                factorization_holds &= matches

                R_at_0 = sp.simplify(Rt.subs(t, 0))
                R_at_1 = sp.simplify(Rt.subs(t, 1))
                zero_at_endpoints = (R_at_0 == sp.zeros(3, 1)) and (R_at_1 == sp.zeros(3, 1))
                vanishes_at_0_and_1 &= zero_at_endpoints

                if S != sp.zeros(3, 1) and nonzero_example is None:
                    nonzero_example = {
                        "i": i + 1,
                        "j": j + 1,
                        "k": k + 1,
                        "S": str(S.T),
                    }
                    max_abs_S_at_generic_t.append((i, j, k, S))

                per_triple.append(
                    {
                        "i": i + 1,
                        "j": j + 1,
                        "k": k + 1,
                        "R_t_factorization_matches_t(t-1)S": bool(matches),
                        "R_vanishes_at_t=0_and_t=1": bool(zero_at_endpoints),
                        "S_nonzero": bool(S != sp.zeros(3, 1)),
                    }
                )

    return {
        "per_triple": per_triple,
        "factorization_holds_for_all_27_triples": bool(factorization_holds),
        "curvature_vanishes_at_t0_and_t1_for_all_27_triples": bool(vanishes_at_0_and_1),
        "nonzero_S_example": nonzero_example,
    }


def only_roots_are_0_and_1() -> dict[str, object]:
    """Confirm t(t-1)=0 has EXACTLY the roots {0,1} (trivial algebra, stated
    explicitly and checked with sympy.solve rather than asserted by eye)."""
    roots = sp.solve(sp.Eq(t * (t - 1), 0), t)
    roots_sorted = sorted(sp.nsimplify(r) for r in roots)
    return {
        "roots_of_t(t-1)=0": [str(r) for r in roots_sorted],
        "matches_{0,1}_exactly": roots_sorted == [sp.Integer(0), sp.Integer(1)],
    }


# ---------------------------------------------------------------------------
# Step 2: Ricci-tensor cross-check (Agricola Theorem 4.4 / Remark 4.2), h=0 case.
# Ric^t(X,Y) = Sum_i (t-t^2)<[X,Zi]_m,[Y,Zi]_m> + Qh(...)   [Qh term = 0 since h=0]
# This is the TRACE of the curvature over one slot; if the full curvature R^t
# already vanishes at t=0,1 (Step 1), its trace must too -- this is an internal
# consistency check, not a new independent fact, but it directly reproduces
# Agricola's own stated Remark 4.2 ("coefficient of beta vanishes for t=0,1").
# ---------------------------------------------------------------------------


def ricci_t(X: sp.Matrix, Y: sp.Matrix) -> sp.Expr:
    total = sp.Integer(0)
    for i in range(3):
        Zi = Z[i]
        total += bracket_m(X, Zi).dot(bracket_m(Y, Zi))
    return sp.simplify((t - t**2) * total)


def ricci_cross_check() -> dict[str, object]:
    results = []
    all_zero_at_endpoints = True
    for i in range(3):
        for j in range(3):
            expr = ricci_t(Z[i], Z[j])
            at0 = sp.simplify(expr.subs(t, 0))
            at1 = sp.simplify(expr.subs(t, 1))
            ok = (at0 == 0) and (at1 == 0)
            all_zero_at_endpoints &= ok
            results.append(
                {
                    "i": i + 1,
                    "j": j + 1,
                    "Ric^t(Zi,Zj)": str(sp.simplify(expr)),
                    "vanishes_at_t=0_and_t=1": bool(ok),
                }
            )
    # coefficient-of-beta form: factor out (t - t^2) explicitly for the (1,1) entry
    ric_11 = ricci_t(Z[0], Z[0])
    coeff_form = sp.factor(ric_11)
    return {
        "per_pair": results,
        "ricci_vanishes_at_t0_and_t1_for_all_pairs": bool(all_zero_at_endpoints),
        "Ric^t(Z1,Z1)_factored": str(coeff_form),
    }


# ---------------------------------------------------------------------------
# Step 3: numeric cross-check with the project's OWN established structure
# constant c=2 (derived from E2's h_H=3=(3/2)*c, NOT re-fit here) -- confirms
# the symbolic result is not an artifact of keeping c abstract.
# ---------------------------------------------------------------------------


def concrete_c_cross_check(c_value: int = 2) -> dict[str, object]:
    X, Y, W = Z[0], Z[1], Z[1]  # (Z1,Z2)Z2 component used in the walkthrough above
    Rt = curvature_Rt(X, Y, W).subs(c, c_value)
    R_at_half = sp.simplify(Rt.subs(t, sp.Rational(1, 2)))  # Levi-Civita: should be NONZERO
    R_at_0 = sp.simplify(Rt.subs(t, 0))
    R_at_1 = sp.simplify(Rt.subs(t, 1))
    return {
        "c_value_used": c_value,
        "R^t(Z1,Z2)Z2_as_function_of_t": str(sp.simplify(Rt)),
        "R_at_t=1/2_LeviCivita_nonzero_as_expected": bool(R_at_half != sp.zeros(3, 1)),
        "R_at_t=0": str(R_at_0.T),
        "R_at_t=1": str(R_at_1.T),
        "R_at_0_and_1_both_zero": bool(R_at_0 == sp.zeros(3, 1) and R_at_1 == sp.zeros(3, 1)),
    }


# ---------------------------------------------------------------------------
# Step 4: cross-reference against E2's already-computed, already-verified
# n=0 zero-mode crossings (read-only -- this script does not recompute or
# modify E2's result, only compares against it).
# ---------------------------------------------------------------------------


def cross_reference_e2_n0_crossings() -> dict[str, object]:
    import os

    e2_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "20260717-round67-e2-s3-torsion-deformation",
        "results_e2.json",
    )
    e2_path = os.path.normpath(e2_path)
    try:
        with open(e2_path, encoding="utf-8") as fh:
            e2 = json.load(fh)
    except FileNotFoundError:
        return {"e2_file_found": False, "path_tried": e2_path}

    n0_crossings = sorted(
        sp.nsimplify(row["t_star_exact"])
        for row in e2["step4_closed_form_crossings_sorted_by_t"]
        if row["n"] == 0
    )
    n1_or_n2_crossings = sorted(
        sp.nsimplify(row["t_star_exact"])
        for row in e2["step4_closed_form_crossings_sorted_by_t"]
        if row["n"] != 0
    )
    matches_flat_set = n0_crossings == [sp.Integer(0), sp.Integer(1)]
    higher_n_not_flat = all(v not in (sp.Integer(0), sp.Integer(1)) for v in n1_or_n2_crossings)

    return {
        "e2_file_found": True,
        "e2_n0_crossings": [str(v) for v in n0_crossings],
        "e2_higher_n_crossings_(n=1,2)": [str(v) for v in n1_or_n2_crossings],
        "n0_crossings_equal_flat_connection_set_{0,1}": bool(matches_flat_set),
        "higher_n_crossings_NOT_in_flat_connection_set": bool(higher_n_not_flat),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    jacobi_ok = jacobi_identity_check()
    flatness = exhaustive_flatness_check()
    root_check = only_roots_are_0_and_1()
    ricci = ricci_cross_check()
    concrete = concrete_c_cross_check(c_value=2)
    e2_cross_ref = cross_reference_e2_n0_crossings()

    h1_subquestion_pass = (
        jacobi_ok
        and flatness["factorization_holds_for_all_27_triples"]
        and flatness["curvature_vanishes_at_t0_and_t1_for_all_27_triples"]
        and flatness["nonzero_S_example"] is not None
        and root_check["matches_{0,1}_exactly"]
        and ricci["ricci_vanishes_at_t0_and_t1_for_all_pairs"]
        and concrete["R_at_0_and_1_both_zero"]
        and concrete["R_at_t=1/2_LeviCivita_nonzero_as_expected"]
    )

    e2_confirms_n0_matches_flat_set = bool(
        e2_cross_ref.get("e2_file_found")
        and e2_cross_ref.get("n0_crossings_equal_flat_connection_set_{0,1}")
    )

    result = {
        "step0_jacobi_identity_control_ok": jacobi_ok,
        "step1_exhaustive_flatness_check": flatness,
        "step1b_roots_of_t(t-1)=0": root_check,
        "step2_ricci_cross_check": ricci,
        "step3_concrete_c=2_cross_check": concrete,
        "step4_cross_reference_against_E2_results_e2_json": e2_cross_ref,
        "verdict": {
            "h1_subquestion_independent_geometric_criterion_found": bool(h1_subquestion_pass),
            "e2_n0_zero_mode_crossings_match_the_independent_flat_connection_set": (
                e2_confirms_n0_matches_flat_set
            ),
            "label": (
                "PASS_H1_SUBQUESTION_INDEPENDENT_CRITERION_FOUND"
                if (h1_subquestion_pass and e2_confirms_n0_matches_flat_set)
                else "FAIL_OR_NO_INDEPENDENT_CRITERION_FOUND"
            ),
            "scope_note": (
                "This PASS covers ONLY the n=0 crossing values {0,1}. The n=1,2 "
                "crossings found by E2 ({-1/3,4/3},{-2/3,5/3}) are explicitly NOT "
                "matched by this (or any found) independent geometric criterion -- "
                "see decision.md for the honest scope statement."
            ),
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e7.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
