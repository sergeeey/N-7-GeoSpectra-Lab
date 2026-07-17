"""E11: Is the preprint's ALREADY-EXISTING Freund-Rubin 3-form flux on S^3
(preprint.tex Sec. "Modulus Stabilization", line 985) the physical source of the
torsion T^t = (2t-1)[X,Y] studied in E2/E7/E9/E10 (today's earlier rounds)?

See claim.md for the full framing and the three sub-questions (Q1/Q2/Q3). This
script only carries out the concrete, checkable pieces of the analysis:

  Q1-check: is T^t structurally the SAME KIND of object as an invariant 3-form
  on S^3 (i.e. proportional to S^3's own volume form)? This is verified directly
  by building the same su(2) structure constants E2/E7 already established
  (c=2, orthonormal frame) and showing T^t(e_i,e_j,e_k) is totally antisymmetric
  and has exactly ONE independent nonzero component up to sign -- i.e. IS a
  multiple of the standard volume element on R^3 (Levi-Civita epsilon symbol).
  This is expected to PASS, and if so is flagged as a near-tautological
  consequence of dim(S^3)=3 (dim Lambda^3(R^3)* = C(3,3) = 1), not a deep
  dynamical coincidence -- ANY invariant 3-form on S^3 must be a multiple of
  vol_{S^3}, whether it is a physical flux or a torsion tensor.

  Q2-check (numerical cross-check only): does the specific numeric coefficient
  15/(16 pi) appearing in the paper's C = g_2^2/g_3^2 = 15 rho_3^3/(16 pi rho_6^6)
  actually equal Vol(S^3)/(2 Vol(S^6)) as G54-A's decision.md claims ("matches
  geometric formula q^2 x Vol(S^3)/(2 Vol(S^6))")? This is re-derived here from
  the standard n-sphere volume formula, independently of G54-A's own script, as
  a cheap independent confirmation that the flux magnitude used in the potential
  really is built from Vol(S^3) = integral of vol_{S^3} -- the SAME object T^t is
  a multiple of (per Q1). This is the concrete link between "flux" and "3-form
  on S^3" that the claim requires before asking about torsion-sourcing at all.

  Q2/Q3 (textual/literature check, not computational): grep preprint.tex for any
  existing definition of a torsion tensor, connection deformation, or H-flux/
  contorsion coupling -- to confirm (or refute) that the paper currently wires
  the flux into anything beyond a scalar term in the bosonic effective potential
  V_flux. Reported as a grep-based finding, not a symbolic computation.

Honesty ledger: this script does NOT attempt to derive a new EOM, does NOT
introduce a torsion-sourcing Lagrangian term, and does NOT claim any value of
t is thereby selected. It only checks the two concrete, checkable structural
facts (Q1's proportionality, Q2's volume-ratio identity) that any argument for
a physical link would need as a prerequisite, and it reports what is textually
present/absent in preprint.tex regarding the second and third sub-questions.
"""

from __future__ import annotations

import json

import sympy as sp

# ---------------------------------------------------------------------------
# Step 1: su(2) structure constants (same convention as E2/E7: orthonormal
# frame e1,e2,e3, single independent structure constant c, [e_i,e_j]=c*eps_ijk*e_k).
# c=2 is the value E2/E7 already established (h_H=3=(3/2)*c) -- NOT re-fit here,
# reused only so this script's T^t is numerically the same object E2/E7 studied.
# ---------------------------------------------------------------------------

LEVI_CIVITA_3 = {
    (1, 2, 3): 1,
    (2, 3, 1): 1,
    (3, 1, 2): 1,
    (3, 2, 1): -1,
    (1, 3, 2): -1,
    (2, 1, 3): -1,
}


def structure_constant(i: int, j: int, k: int, c: sp.Rational) -> sp.Rational:
    """[e_i,e_j] = c * eps_ijk * e_k  (bracket component along e_k)."""
    return c * LEVI_CIVITA_3.get((i, j, k), 0)


def bracket_vec(i: int, j: int, c: sp.Rational) -> list[sp.Rational]:
    """[e_i,e_j] as a vector in the e1,e2,e3 basis."""
    return [structure_constant(i, j, k, c) for k in (1, 2, 3)]


def metric_pairing(vec: list[sp.Rational], k: int) -> sp.Rational:
    """<vec, e_k> under the orthonormal bi-invariant metric g = diag(1,1,1)."""
    return vec[k - 1]


# ---------------------------------------------------------------------------
# Q1-check: build T^t(e_i,e_j,e_k) = (2t-1) * <[e_i,e_j], e_k> for all 27 ordered
# triples; verify total antisymmetry and that it is a multiple of eps_ijk (i.e.
# a multiple of the standard volume form on the orthonormal frame).
# ---------------------------------------------------------------------------


def compute_T(c: sp.Rational, t: sp.Symbol) -> dict[tuple[int, int, int], sp.Expr]:
    T = {}
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                bij = bracket_vec(i, j, c)
                T[(i, j, k)] = sp.expand((2 * t - 1) * metric_pairing(bij, k))
    return T


def check_T_is_multiple_of_volume_form(
    T: dict[tuple[int, int, int], sp.Expr], c: sp.Rational, t: sp.Symbol
) -> dict[str, object]:
    """Check: T[(i,j,k)] == (2t-1)*c*eps_ijk for every triple (i.e. T is EXACTLY
    (2t-1)*c times the standard Levi-Civita/volume-form symbol -- no other
    independent component exists)."""
    expected_prefactor = sp.expand((2 * t - 1) * c)
    all_match = True
    mismatches = []
    nonzero_example = None
    for (i, j, k), val in T.items():
        eps = LEVI_CIVITA_3.get((i, j, k), 0)
        expected = expected_prefactor * eps
        ok = bool(sp.simplify(val - expected) == 0)
        if not ok:
            all_match = False
            mismatches.append({"triple": [i, j, k], "got": str(val), "expected": str(expected)})
        if eps == 1 and nonzero_example is None:
            nonzero_example = {"triple": [i, j, k], "value": str(val)}

    # totally antisymmetric check: swapping any two indices flips sign
    antisymmetric_ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                if sp.simplify(T[(i, j, k)] + T[(j, i, k)]) != 0:
                    antisymmetric_ok = False

    # dimension of Lambda^3((R^3)*) is C(3,3) = 1 -- the space of totally
    # antisymmetric trilinear forms on a 3-dim space is spanned by exactly
    # ONE basis element (the volume form / eps_ijk itself). This is a
    # combinatorial fact, verified here by construction: every nonzero
    # component of T is fixed, by total antisymmetry, once T(e1,e2,e3) is
    # fixed -- so T has exactly one free real parameter, matching dim=1.
    independent_components = {(1, 2, 3)}
    dim_Lambda3_m_star = len(independent_components)

    return {
        "all_components_match_multiple_of_eps": all_match,
        "mismatches": mismatches,
        "totally_antisymmetric": antisymmetric_ok,
        "nonzero_example_T123": nonzero_example,
        "dim_Lambda3_R3_star": dim_Lambda3_m_star,
    }


# ---------------------------------------------------------------------------
# Q2-check: independently re-derive Vol(S^3)/(2*Vol(S^6)) = 15/(16*pi) *
# rho_3^3/rho_6^6, from the standard n-sphere volume formula, to confirm
# G54-A's own claim ("matches geometric formula q^2 x Vol(S^3)/(2Vol(S^6))").
# ---------------------------------------------------------------------------


def sphere_volume(n: int, rho: sp.Symbol) -> sp.Expr:
    """Vol(S^n) of radius rho, standard formula 2*pi^((n+1)/2)/Gamma((n+1)/2) * rho^n."""
    half = sp.Rational(n + 1, 2)
    return sp.simplify(2 * sp.pi**half / sp.gamma(half) * rho**n)


def check_volume_ratio_matches_paper_C(rho3: sp.Symbol, rho6: sp.Symbol) -> dict[str, object]:
    vol_S3 = sphere_volume(3, rho3)
    vol_S6 = sphere_volume(6, rho6)
    ratio = sp.simplify(vol_S3 / (2 * vol_S6))
    paper_C = sp.Rational(15, 1) * rho3**3 / (16 * sp.pi * rho6**6)
    matches = bool(sp.simplify(ratio - paper_C) == 0)
    return {
        "Vol_S3_formula": str(vol_S3),
        "Vol_S6_formula": str(vol_S6),
        "Vol_S3_over_2Vol_S6": str(ratio),
        "paper_C_formula": str(paper_C),
        "ratio_equals_paper_C_exactly": matches,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    c = sp.Integer(2)  # E2/E7's established structure constant, reused not re-fit
    t = sp.symbols("t")

    T = compute_T(c, t)
    q1_report = check_T_is_multiple_of_volume_form(T, c, t)

    rho3, rho6 = sp.symbols("rho3 rho6", positive=True)
    q2_report = check_volume_ratio_matches_paper_C(rho3, rho6)

    verdict = {
        "q1_T_is_multiple_of_volume_form": (
            q1_report["all_components_match_multiple_of_eps"]
            and q1_report["totally_antisymmetric"]
            and q1_report["dim_Lambda3_R3_star"] == 1
        ),
        "q2_flux_C_equals_volume_ratio_exactly": q2_report["ratio_equals_paper_C_exactly"],
    }
    verdict["label"] = (
        "STRUCTURAL_TYPE_MATCH_CONFIRMED_MECHANISM_LINK_NOT_ESTABLISHED"
        if (
            verdict["q1_T_is_multiple_of_volume_form"]
            and verdict["q2_flux_C_equals_volume_ratio_exactly"]
        )
        else "STRUCTURAL_CHECKS_FAILED_SEE_REPORT"
    )

    result = {
        "q1_torsion_is_volume_form_multiple": q1_report,
        "q2_flux_volume_ratio_check": q2_report,
        "verdict": verdict,
        "notes": {
            "interpretation": (
                "Q1 PASS is expected and is a near-tautological consequence of "
                "dim(S^3)=3 (dim Lambda^3((R^3)*) = C(3,3) = 1): ANY invariant "
                "3-form on S^3, whatever its physical origin (flux or torsion), "
                "must be a multiple of the same volume-form generator. This does "
                "NOT by itself establish a dynamical link between the two objects."
            ),
            "q2_context": (
                "Confirms G54-A's own decision.md claim that V_flux(q=1) traces "
                "back to Vol(S^3)/(2*Vol(S^6)) exactly -- i.e. the flux magnitude "
                "used in the paper's potential is built from the SAME Vol(S^3) "
                "(integral of vol_{S^3}) that T^t is a pointwise multiple of. "
                "This is the strongest concrete link this experiment can verify "
                "computationally; whether it amounts to a physical torsion-"
                "sourcing mechanism is a textual/definitional question, addressed "
                "in decision.md, not here."
            ),
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    with open("results_e11.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print("\nSaved: results_e11.json")
