r"""E11 (round77): does psi^(0) (t=0, left-invariant-frame constant spinor, E9) and
psi^(1) (t=1, right-invariant-trivialization spinor psi(x)=gbar(x)*psi_0, round76 Part 4,
c0=-2 sign convention ONLY) transform as clean, definite representations of
SU(2)_L x SU(2)_R -- under THIS project's own "only geometrically natural" convention
that SU(2)_L acts on S^3=SU(2) by LEFT group translation (g -> h g) and SU(2)_R by
RIGHT group translation (g -> g h^{-1}) -- and if so, does the resulting labeling
connect to the ALREADY-FIXED "left-handed" convention from S^6 (preprint.tex:885-908)?

This is explicitly SPECULATIVE SYNTHESIS (see claim.md), building on:
  - experiments/20260717-round74-e10-chirality-sign-link/decision.md -- flagged the
    candidate correspondence, explicitly NOT verified there (out of scope).
  - experiments/20260717-round76-e9followup-right-invariant-frame/decision.md -- built
    explicit psi^(0), psi^(1) and the c0=-2 vs c=+2 sign caveat that MUST be carried
    forward here.

Method: rather than re-deriving E9/round76's connection/parallelism machinery (already
done and tool-verified there), this script checks a DIFFERENT, independent thing: how
the two ALREADY-CONSTRUCTED spinor profiles (psi^(0)=const, psi^(1)(x)=g(x)^{-1}*psi_0)
transform under the LEFT-translation action g->h*g and the RIGHT-translation action
g->g*h^{-1} of a generic group element h, using an explicit symbolic representation-
theory computation (matrix Lie group elements, sympy), not an appeal to abstract Lie
theory alone.

Key definitions (matching round76's own conventions exactly):
  - Z_i = i*sigma_i (E2/E9/round76's Clifford/Pauli-based generators)
  - g(x) = x0*I + x1*Z1 + x2*Z2 + x3*Z3 (generic group element, symbolic x0..x3)
  - h(y) = y0*I + y1*Z1 + y2*Z2 + y3*Z3 (SAME quaternion family, symbolic y0..y3,
    kept fully symbolic/independent of x -- a GENERIC member of this matrix algebra,
    not restricted to unit norm). Using a second GENERIC symbolic quaternion (rather
    than a trig-parametrized rotation angle) keeps every check below a PURE
    rational-function identity (no trig simplification needed at all): the algebraic
    identities under test -- (h^{-1}g)^{-1}=g^{-1}h and h(gh)^{-1}=g^{-1} -- are
    consequences of ordinary matrix-inverse/associativity algebra, valid for ANY
    invertible matrices, hence valid a fortiori when g,h are restricted to the unit
    sphere (i.e. genuine SU(2) elements) -- restricting to the unit sphere only
    removes solutions, it cannot break an identity that holds identically off it.

Two candidate group actions on C^2-valued (spinor) functions of a group-element
argument G, matching the standard theory of associated bundles over a Lie group
trivialized by the LEFT-invariant frame (see claim.md for the derivation of why the
compensating factor is present for one action and absent for the other):
  - ACTION_L(h, psi)(G) := psi(h^{-1} * G)          [pullback ONLY -- frame Z_i^L is
    itself invariant under left translation, no compensating target rotation needed]
  - ACTION_R(h, psi)(G) := h * psi(G * h)           [pullback PLUS compensating h on
    the C^2 target -- frame Z_i^L rotates by Ad(h) under right translation, and for
    spinors (fundamental rep of the double cover) the lift of Ad(h) is h itself]

For each of psi^(0) and psi^(1), and each of ACTION_L/ACTION_R, this script checks
whether the transformed spinor equals (a) the original exactly (SINGLET), or (b) a
nontrivial map that is NOT reducible to the identity for generic h (DOUBLET/
fundamental-rep candidate) -- and reports the pattern honestly, without assuming
which outcome will occur.
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
y0, y1, y2, y3 = sp.symbols("y0 y1 y2 y3")
a_, b_ = sp.symbols("a_ b_")


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i -- IDENTICAL to E2/E9/round76's own convention."""
    return [sp.I * s for s in pauli_matrices()]


def group_element(Z: list[sp.Matrix], coords) -> sp.Matrix:
    c0, c1, c2, c3 = coords
    return c0 * I2 + c1 * Z[0] + c2 * Z[1] + c3 * Z[2]


def group_conjugate(Z: list[sp.Matrix], coords) -> sp.Matrix:
    c0, c1, c2, c3 = coords
    return c0 * I2 - c1 * Z[0] - c2 * Z[1] - c3 * Z[2]


def run_part1_setup(Z: list[sp.Matrix]):
    """g(x), h(y): two GENERIC, independent members of the same quaternion matrix
    family (no unit-norm constraint imposed -- see module docstring for why this is
    valid: the identities under test hold for any invertible matrices in this
    algebra, hence for SU(2) elements in particular, which are the unit-norm
    subfamily). Verify the quaternion-norm identity generically (reused fact from
    round76, re-derived here for self-containment) for BOTH g and h."""
    g = group_element(Z, (x0, x1, x2, x3))
    gbar = group_conjugate(Z, (x0, x1, x2, x3))
    h = group_element(Z, (y0, y1, y2, y3))
    hbar = group_conjugate(Z, (y0, y1, y2, y3))

    g_norm_check = sp.expand(g * gbar - (x0**2 + x1**2 + x2**2 + x3**2) * I2)
    h_norm_check = sp.expand(h * hbar - (y0**2 + y1**2 + y2**2 + y3**2) * I2)

    return {
        "g": g,
        "h": h,
        "g_quaternion_norm_identity_holds": bool(g_norm_check == sp.zeros(2, 2)),
        "h_quaternion_norm_identity_holds": bool(h_norm_check == sp.zeros(2, 2)),
    }


# ---------------------------------------------------------------------------
# PART 2: transformation of psi^(0) = const under ACTION_L and ACTION_R.
# ---------------------------------------------------------------------------


def run_part2_psi0(h: sp.Matrix) -> dict[str, object]:
    psi0 = sp.Matrix([a_, b_])

    # ACTION_L: pullback only, psi^(0) has no g-dependence, so trivially unchanged.
    action_L_psi0 = psi0  # psi^(0)(h^{-1} g) = psi^(0) identically (no g-dependence)
    is_singlet_under_L = bool(sp.expand(action_L_psi0 - psi0) == sp.zeros(2, 1))

    # ACTION_R: h * psi^(0)(g h) = h * psi0 (still no g-dependence, but h now multiplies).
    action_R_psi0 = sp.expand(h * psi0)
    is_invariant_under_R = bool(sp.expand(action_R_psi0 - psi0) == sp.zeros(2, 1))

    # Confirm ACTION_R is NOT reducible to the identity for CONCRETE, generic
    # numeric h (rules out an accidental/universal singlet).
    concrete_subs = {y0: sp.Integer(3), y1: sp.Integer(1), y2: sp.Integer(2), y3: sp.Integer(-1)}
    diff_concrete = sp.expand((action_R_psi0 - psi0).subs(concrete_subs))
    nontrivial_at_concrete_h = diff_concrete != sp.zeros(2, 1)

    return {
        "action_L_psi0_equals_psi0_exactly": is_singlet_under_L,
        "action_R_psi0_equals_psi0_exactly_for_all_h": is_invariant_under_R,
        "action_R_psi0_minus_psi0_at_concrete_h": str(diff_concrete.T),
        "action_R_psi0_nontrivial_at_concrete_h": bool(nontrivial_at_concrete_h),
        "action_R_psi0_str": str(action_R_psi0.T),
        "verdict_psi0": (
            "SU(2)_L SINGLET (exact invariance under left-translation pullback), "
            "SU(2)_R DOUBLET/fundamental (h acts by left matrix multiplication, "
            "nontrivial for generic h, exact identity only at h=+-I)"
        ),
    }


# ---------------------------------------------------------------------------
# PART 3: transformation of psi^(1)(x) = g(x)^{-1} psi_0 under ACTION_L, ACTION_R.
# Pure algebraic identities: (AB)^{-1} = B^{-1} A^{-1}, checked directly by
# constructing the matrices explicitly and comparing to sympy's own .inv().
# ---------------------------------------------------------------------------


def run_part3_psi1(g: sp.Matrix, h: sp.Matrix) -> dict[str, object]:
    psi0 = sp.Matrix([a_, b_])
    g_inv = g.inv()
    h_inv = h.inv()

    psi1_at_g = sp.simplify(g_inv * psi0)  # psi^(1)(g) = g^{-1} psi0

    # ---- ACTION_L: psi^(1)(h^{-1} g) --------------------------------------
    # (h^{-1} g)^{-1} = g^{-1} h  -- pure associativity/inverse identity, verified
    # directly here (not assumed) by computing (hinv*g).inv() from scratch and
    # comparing to g_inv*h.
    G_L = h_inv * g
    G_L_inv_direct = sp.simplify(G_L.inv())
    G_L_inv_claimed = sp.simplify(g_inv * h)
    inverse_identity_L_holds = bool(sp.expand(G_L_inv_direct - G_L_inv_claimed) == sp.zeros(2, 2))

    psi1_action_L = sp.simplify(G_L_inv_direct * psi0)  # = (h^{-1}g)^{-1} psi0
    candidate_L_closed_form = sp.simplify(g_inv * (h * psi0))  # g^{-1} (h psi0)
    action_L_matches_closed_form = bool(
        sp.expand(psi1_action_L - candidate_L_closed_form) == sp.zeros(2, 1)
    )

    diff_from_original_L = sp.simplify(psi1_action_L - psi1_at_g)
    is_singlet_under_L = bool(sp.expand(diff_from_original_L) == sp.zeros(2, 1))

    concrete_subs = {y0: sp.Integer(3), y1: sp.Integer(1), y2: sp.Integer(2), y3: sp.Integer(-1)}
    diff_from_original_L_concrete = sp.simplify(diff_from_original_L.subs(concrete_subs))
    nontrivial_under_L_at_concrete_h = diff_from_original_L_concrete != sp.zeros(2, 1)

    # ---- ACTION_R: h * psi^(1)(g h) ---------------------------------------
    # h * (g h)^{-1} = h * h^{-1} * g^{-1} = g^{-1}  -- verified directly.
    G_R = g * h
    G_R_inv_direct = sp.simplify(G_R.inv())
    psi1_at_gh = sp.simplify(G_R_inv_direct * psi0)  # = (gh)^{-1} psi0
    psi1_action_R = sp.simplify(h * psi1_at_gh)  # = h (gh)^{-1} psi0

    is_singlet_under_R = bool(sp.expand(psi1_action_R - psi1_at_g) == sp.zeros(2, 1))

    return {
        "psi1_at_g_str": str(psi1_at_g.T),
        "action_L": {
            "inverse_identity_hinv_g_holds": inverse_identity_L_holds,
            "psi1_action_L_str": str(psi1_action_L.T),
            "matches_closed_form_g_inv_times_h_psi0": action_L_matches_closed_form,
            "is_singlet_exact_for_all_h": is_singlet_under_L,
            "diff_from_original_at_concrete_h": str(diff_from_original_L_concrete.T),
            "nontrivial_at_concrete_h": bool(nontrivial_under_L_at_concrete_h),
        },
        "action_R": {
            "psi1_action_R_str": str(psi1_action_R.T),
            "is_singlet_exact_for_all_h_and_all_x": is_singlet_under_R,
        },
        "verdict_psi1": (
            "SU(2)_L DOUBLET/fundamental (transforms via psi_0 -> h*psi_0 on the "
            "2-dim solution space, nontrivial for generic h), "
            "SU(2)_R SINGLET (EXACT invariance, h cancels identically via "
            "h*(gh)^{-1}=g^{-1})"
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    setup = run_part1_setup(Z)
    g, h = setup["g"], setup["h"]

    part1 = {
        "g_quaternion_norm_identity_holds": setup["g_quaternion_norm_identity_holds"],
        "h_quaternion_norm_identity_holds": setup["h_quaternion_norm_identity_holds"],
    }
    part2 = run_part2_psi0(h)
    part3 = run_part3_psi1(g, h)

    core_setup_ok = bool(
        part1["g_quaternion_norm_identity_holds"] and part1["h_quaternion_norm_identity_holds"]
    )

    psi0_is_L_singlet = part2["action_L_psi0_equals_psi0_exactly"]
    psi0_is_R_doublet_not_singlet = bool(
        (not part2["action_R_psi0_equals_psi0_exactly_for_all_h"])
        and part2["action_R_psi0_nontrivial_at_concrete_h"]
    )

    psi1_is_L_doublet_not_singlet = bool(
        part3["action_L"]["inverse_identity_hinv_g_holds"]
        and part3["action_L"]["matches_closed_form_g_inv_times_h_psi0"]
        and (not part3["action_L"]["is_singlet_exact_for_all_h"])
        and part3["action_L"]["nontrivial_at_concrete_h"]
    )
    psi1_is_R_singlet = part3["action_R"]["is_singlet_exact_for_all_h_and_all_x"]

    clean_complementary_pattern_found = bool(
        psi0_is_L_singlet
        and psi0_is_R_doublet_not_singlet
        and psi1_is_L_doublet_not_singlet
        and psi1_is_R_singlet
    )

    if not core_setup_ok:
        overall_label = "FAIL_CORE_SETUP"
    elif clean_complementary_pattern_found:
        overall_label = "CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT"
    else:
        overall_label = "NO_CLEAN_PATTERN_FOUND"

    result = {
        "part1_setup": part1,
        "part2_psi0_transformation": part2,
        "part3_psi1_transformation": part3,
        "verdict": {
            "core_setup_ok": core_setup_ok,
            "psi0_is_SU2L_singlet": psi0_is_L_singlet,
            "psi0_is_SU2R_doublet_not_singlet": psi0_is_R_doublet_not_singlet,
            "psi1_is_SU2L_doublet_not_singlet": psi1_is_L_doublet_not_singlet,
            "psi1_is_SU2R_singlet": psi1_is_R_singlet,
            "clean_complementary_rep_pattern_found": clean_complementary_pattern_found,
            "label": overall_label,
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    with open("results_e11.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print("\nSaved: results_e11.json")
