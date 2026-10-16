"""C130 injection tests -- deliberately corrupt the machinery and check that
(a) the gate fires, and (b) for at least some corruptions, a HEADLINE field
actually moves.

This distinction is C129's own deepest process finding (its skeptic passes A4 /
C3 / C6): `ALL_INJECTIONS_CAUGHT = True` only shows the gate CAN fail, never
that it GUARDS THE CONCLUSION.  So this harness records, per injection, exactly
which `VERDICT_INPUTS` fields changed, and reports a separate top-level flag
`AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE`.
"""

from __future__ import annotations

import json
import os

import c130_twisted_pin_obstruction as m

BASE = m.main()
BASE_GATES = BASE["GATES"]
BASE_VERDICT = BASE["VERDICT_INPUTS"]


def _identity_chain_map(f: dict) -> dict:
    return {
        k: [[1 if i == j else 0 for j in range(len(v[0]))] for i in range(len(v))]
        for k, v in f.items()
    }


def inj_smith_returns_empty():
    """The integer Smith-normal-form routine always reports no elementary
    divisors -- i.e. every boundary map looks like zero over Z."""
    orig = m._smith_normal_form

    def broken(mat):
        return []

    m._smith_normal_form = broken
    return orig, "_smith_normal_form"


def inj_rank_mod_p_zero():
    """The mod-p rank routine always returns 0."""
    orig = m._rank_mod_p

    def broken(mat, p):
        return 0

    m._rank_mod_p = broken
    return orig, "_rank_mod_p"


def inj_drop_monodromy_term():
    """Drop the `(f - id)` monodromy term from the mapping-torus differential.

    Implemented by forcing the chain self-map passed to the construction to be
    the identity, which makes `(f - id) = 0` in every degree -- exactly the
    corruption, with no duplicated code.
    """
    orig = m.mapping_torus_complex

    def broken(c, f):
        return orig(c, _identity_chain_map(f))

    m.mapping_torus_complex = broken
    return orig, "mapping_torus_complex"


def inj_ext_of_free_is_nonzero():
    """Break the universal-coefficient theorem: report Ext^1(Z, A) = A instead
    of 0.  This is the classic UCT sign-of-life error and it directly
    manufactures a nonzero H^2."""
    orig = m.ext_into

    def broken(g, coeff):
        base = orig(g, coeff)
        if coeff == 0:
            return m.FGAb(base.free_rank + g.free_rank, base.torsion)
        return m.FGAb(base.free_rank, base.torsion + [coeff] * g.free_rank)

    m.ext_into = broken
    return orig, "ext_into"


def inj_pin_verdict_ignores_twist():
    """`pin_verdict` silently drops the twist class -- i.e. it computes the
    UNTWISTED answer and reports it as the twisted one.

    This is the injection that directly probes `claim.md`'s trap: if the
    controls could not tell the twisted question from the untwisted one, the
    round's central discharge would be vacuous."""
    orig = m.pin_verdict

    def broken(ring, w1, w2, twist_c2):
        return orig(ring, w1, w2, ring.zero())

    m.pin_verdict = broken
    return orig, "pin_verdict"


def inj_nonminimal_boundary_zeroed():
    """Zero out `d_2` in the NON-minimal CW model of S^3, so its two 2-cells
    stop being killed and H_2 of the mapping torus becomes nonzero."""
    orig = m.s3_nonminimal_complex

    def broken():
        return m.ChainComplex([1, 1, 1, 1], {2: [[0]], 1: [[0]], 3: [[0]]})

    m.s3_nonminimal_complex = broken
    return orig, "s3_nonminimal_complex"


def inj_pin_criteria_swapped():
    """Swap the Pin^+ / Pin^- existence criteria -- the exact error C129 found
    in C128 Sec.6c and in its own claim.md."""
    orig = m.pin_verdict

    def broken(ring, w1, w2, twist_c2):
        obs_plus = ring.add(w2, ring.mul(w1, w1), twist_c2)
        obs_minus = ring.add(w2, twist_c2)
        return {
            "obstruction_pin_plus": ring.show(obs_plus),
            "obstruction_pin_minus": ring.show(obs_minus),
            "pin_plus_exists": ring.is_zero(obs_plus),
            "pin_minus_exists": ring.is_zero(obs_minus),
        }

    m.pin_verdict = broken
    return orig, "pin_verdict"


def inj_pairing_always_zero():
    """The commutator-pairing routine always reports "they commute"."""
    orig = m.commutator_pairing

    def broken(lift1, lift2, kernel_gen):
        return 0

    m.commutator_pairing = broken
    return orig, "commutator_pairing"


def inj_local_coefficient_monodromy_neutered():
    """Force the local-coefficient routine to use the TRIVIAL monodromy.

    Supplied by FL Step 8a skeptic pass 2 as a corruption that the FIRST
    version of the suite let through completely (34/34, headline unmoved),
    while destroying the one computation specific to this background.  It is
    included here because it slipped through, not because it was designed to
    be caught.
    """
    orig = m.mapping_torus_local_coeff_betti_f2

    def broken(c, f, rho):
        k = len(rho)
        triv = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
        return orig(c, f, triv)

    m.mapping_torus_local_coeff_betti_f2 = broken
    return orig, "mapping_torus_local_coeff_betti_f2"


def inj_su2_to_so3_returns_identity():
    """`su2_to_so3` always returns the identity -- i.e. the double cover is
    reported as trivial."""
    orig = m.su2_to_so3

    def broken(q):
        import numpy as np

        return np.eye(3)

    m.su2_to_so3 = broken
    return orig, "su2_to_so3"


def inj_twisted_adjoint_transposed():
    """Transpose the twisted-adjoint representation matrix."""
    orig = m.twisted_adjoint

    def broken(x, gens, parity):
        return orig(x, gens, parity).T

    m.twisted_adjoint = broken
    return orig, "twisted_adjoint"


INJECTIONS = [
    ("smith_normal_form_returns_empty", inj_smith_returns_empty),
    ("rank_mod_p_returns_zero", inj_rank_mod_p_zero),
    ("monodromy_term_dropped", inj_drop_monodromy_term),
    ("UCT_Ext_of_free_group_nonzero", inj_ext_of_free_is_nonzero),
    ("pin_verdict_ignores_the_twist", inj_pin_verdict_ignores_twist),
    ("nonminimal_model_d2_zeroed", inj_nonminimal_boundary_zeroed),
    ("pin_plus_minus_criteria_swapped", inj_pin_criteria_swapped),
    ("commutator_pairing_always_zero", inj_pairing_always_zero),
    ("local_coefficient_monodromy_neutered", inj_local_coefficient_monodromy_neutered),
    ("su2_to_so3_returns_identity", inj_su2_to_so3_returns_identity),
    ("twisted_adjoint_transposed", inj_twisted_adjoint_transposed),
]


def run() -> dict:
    report: dict = {
        "baseline_gates_passed": BASE["GATE_SUMMARY"]["passed"],
        "baseline_gates_total": BASE["GATE_SUMMARY"]["total"],
        "injections": {},
    }
    any_moves = False
    all_caught = True
    for name, setup in INJECTIONS:
        orig, attr = setup()
        try:
            res = m.main()
            gates = res["GATES"]
            verdict = res["VERDICT_INPUTS"]
            fired = sorted(k for k, v in gates.items() if not v and BASE_GATES.get(k))
            moved = sorted(k for k, v in verdict.items() if BASE_VERDICT.get(k) != v)
            caught = bool(fired) or not res["GATE_SUMMARY"]["ALL_OK"]
            crashed = False
        # WHY blind: an injection may break the machinery in any way at all;
        # a crash is a legitimate (if crude) form of "caught", and must be
        # recorded as such rather than aborting the whole suite.
        except Exception as exc:  # noqa: BLE001
            fired = [f"EXCEPTION: {type(exc).__name__}"]
            moved = []
            caught = True
            crashed = True
            res = None
        finally:
            setattr(m, attr, orig)
        all_caught = all_caught and caught
        any_moves = any_moves or bool(moved)
        report["injections"][name] = {
            "gates_that_fired": fired,
            "gates_passed": (res["GATE_SUMMARY"]["passed"] if res else None),
            "gates_total": (res["GATE_SUMMARY"]["total"] if res else None),
            "caught": caught,
            "caught_by_crash": crashed,
            "headline_fields_moved": moved,
        }
    report["ALL_INJECTIONS_CAUGHT"] = all_caught
    report["AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE"] = any_moves
    report["N_INJECTIONS_MOVING_THE_HEADLINE"] = sum(
        1 for v in report["injections"].values() if v["headline_fields_moved"]
    )
    return report


if __name__ == "__main__":
    rep = run()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(
        os.path.join(here, "results_c130_injections.json"), "w", encoding="utf-8"
    ) as fh:
        json.dump(rep, fh, indent=2, sort_keys=True)
    print(f"ALL_INJECTIONS_CAUGHT = {rep['ALL_INJECTIONS_CAUGHT']}")
    print(
        "AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE = "
        f"{rep['AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE']} "
        f"({rep['N_INJECTIONS_MOVING_THE_HEADLINE']} of {len(INJECTIONS)})"
    )
    for name, info in rep["injections"].items():
        tag = "MOVES HEADLINE" if info["headline_fields_moved"] else "caught only"
        gp, gt = info["gates_passed"], info["gates_total"]
        shown = f"{gp}/{gt}" if gp is not None else "crash"
        print(f"  {name:38s} {shown:>7s}  {tag}")
        for f in info["headline_fields_moved"]:
            print(f"        moved: {f}")
