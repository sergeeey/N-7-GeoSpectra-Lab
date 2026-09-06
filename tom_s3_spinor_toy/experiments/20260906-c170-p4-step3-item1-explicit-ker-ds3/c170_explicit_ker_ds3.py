r"""
C170 -- P4 Step 3 escalation item 1: explicit ker(D_S3(t)) vector at t=0,1.

Context: C169's decision.md Section 5 named item 1 of the genuine escalation
path as "ker(D_S3(t)) built as an explicit vector, not merely 'an eigenvalue
of 0 exists'". round72/E7's H1b proof established EXISTENCE of a globally
Nabla^t-parallel spinor at t=0,1 via an abstract holonomy argument (flatness +
simple-connectedness), without exhibiting the vector. round67/E2 established
the CLOSED-FORM EIGENVALUE crossings (t=0,1 for n=0) via Agricola's eq(5)
D^t psi = sum_i Z_i.Z_i(psi) + t.H.psi, with H = (3c/2)*omega and omega =
Z1.Z2.Z3 = EXACTLY the 2x2 identity (E2's own [VERIFIED-tool] result,
re-verified here for self-containment, Step 1).

This script attempts the EXPLICIT construction, self-contained and checked
at every step (no step is asserted without a symbolic verification):

Step 1: Rebuild E2's Clifford generators Z_i=i*sigma_i (Cl(3) via Pauli
        matrices) and re-verify omega = Z1 Z2 Z3 is exactly I2 (reproduces
        E2's own already-published result, done here fresh, not copied).

Step 2: Derive the SPIN CONNECTION matrices M_i(t) implied by Agricola's own
        Nabla^t_X Y = t[X,Y]_m (the connection coefficients Gamma^t_{ijk} =
        t*c*eps_ijk, general formula for a metric connection on an
        orthonormal frame), via the standard formula
            Nabla^t_{Z_i} psi = Z_i(psi) + (1/4) sum_{j,k} Gamma^t_{ijk} gamma_j gamma_k psi
        This is NEW to this project (not built anywhere before this round,
        confirmed by grep -- E2/round72 only ever used the eigenvalue-level
        formula eq(5), never the connection-matrix M_i(t) itself). The
        self-consistency check: does sum_i gamma_i . M_i(t) equal t*H
        (Agricola's own eq(5) H-term)? If this FAILS, the M_i(t) derivation
        is wrong and nothing below can be trusted (Substrate Gate for this
        script's own internal machinery).

Step 3: t=0 kernel. M_i(0)=0 identically (M_i(t) is linear in t) =>
        Nabla^0_{Z_i} psi = Z_i(psi) => the parallel-spinor condition at t=0
        is simply "psi is a CONSTANT function on SU(2)" -- ANY vector in C^2
        qualifies, a 2-dimensional kernel, with ZERO further derivation
        needed beyond M_i(0)=0. This reuses nothing new -- it is a direct,
        elementary reading of eq(5) at t=0 (D^0(constant psi) = 0.H.psi = 0
        for ANY constant psi), independent of the connection-matrix
        machinery above (cross-checked against it as a consistency test).

Step 4: t=1 kernel -- CANDIDATE construction, explicitly flagged as
        candidate, not certified. Ansatz: psi_1(g) := g^{-1} . psi_0 (matrix
        inverse of g in SU(2), acting on a fixed psi_0 in C^2), i.e. "the
        defining SU(2) representation composed with group inversion". This
        requires identifying the ABSTRACT structure-constant generator Z_i
        (bracket [Z_i,Z_j]=c*eps_ijk*Z_k, c=2, E2's own calibrated value)
        with a CONCRETE matrix e_i in su(2) such that [e_i,e_j] matches the
        SAME bracket at c=2 -- checked directly below for e_i := -i*sigma_i
        (NOT +i*sigma_i = Z_i itself; the sign is forced by c=+2, not a free
        choice -- checked both ways below, only one survives).

        Given that identification, d/ds|_0 (g.exp(s Z_i))^{-1} = -e_i . g^{-1}
        (elementary calculus of the matrix inverse -- no representation-
        theoretic assumption beyond the e_i identification), so
        Z_i(psi_1) = -e_i . psi_1 identically. This is checked directly
        against the REQUIRED condition from Step 2's M_i(1) (the parallel
        condition Nabla^1_{Z_i}psi=0 <=> Z_i(psi) = -M_i(1).psi).

Step 5: Holonomy check against C167/C168's own H_1 := zeta_3 convention.
        psi_1(g) = g^{-1}.psi_0 is a 2-parameter family (psi_0 in C^2); its
        value transforms under the deck map g -> zeta_p . g as
        psi_1(zeta_p g) = g^{-1} . zeta_p^{-1} . psi_0 = psi_1[zeta_p^{-1}
        psi_0](g) -- i.e. the family maps to itself with psi_0 -> zeta_p^{-1}
        psi_0. Evaluated at the basepoint g=e, this gives the holonomy
        H_1_derived := zeta_p^{-1}, NOT zeta_p as C168 assumed. This is
        reported honestly as a FOUND discrepancy (candidate vs C168's
        modeling choice), not silently resolved -- see decision.md.

All load-bearing claims are checked by direct sympy computation, exact
(not floating point unless explicitly marked "numeric sanity only").

Run: python c170_explicit_ker_ds3.py
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
IMAG = sp.I


# ---------------------------------------------------------------------------
# Step 1: E2's own Clifford generators, re-verified fresh.
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -IMAG], [IMAG, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i (E2's own convention, {Z_i,Z_j} = -2 delta_ij)."""
    return [IMAG * s for s in pauli_matrices()]


def eps(i: int, j: int, k: int) -> int:
    """Levi-Civita symbol, 1-indexed."""
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    perm = p[:]
    for x in range(3):
        for y in range(3 - 1 - x):
            if perm[y] > perm[y + 1]:
                perm[y], perm[y + 1] = perm[y + 1], perm[y]
                sign = -sign
    return sign


def step1_omega_check(Z: list[sp.Matrix]) -> dict:
    omega = sp.simplify(Z[0] * Z[1] * Z[2])
    is_I2 = sp.simplify(omega - I2) == sp.zeros(2, 2)
    return {"omega": str(omega), "omega_equals_I2_exactly": bool(is_I2)}


# ---------------------------------------------------------------------------
# Step 2: connection matrices M_i(t), self-consistency vs eq(5)'s t*H term.
# ---------------------------------------------------------------------------

t, c = sp.symbols("t c")


def connection_matrices(Z: list[sp.Matrix]) -> list[sp.Matrix]:
    """M_i(t) := (1/4) sum_{j,k} Gamma^t_{ijk} Z_j Z_k, Gamma^t_{ijk}=t*c*eps_ijk."""
    Ms = []
    for i in range(3):
        M = sp.zeros(2, 2)
        for j in range(3):
            for k in range(3):
                e = eps(i + 1, j + 1, k + 1)
                if e:
                    M += sp.Rational(1, 4) * t * c * e * (Z[j] * Z[k])
        Ms.append(sp.simplify(M))
    return Ms


def step2_self_consistency(Z: list[sp.Matrix], Ms: list[sp.Matrix]) -> dict:
    """Check sum_i Z_i . M_i(t) == t * H, H = (3c/2)*omega = (3c/2)*I2 (Step1)."""
    total = sp.zeros(2, 2)
    for i in range(3):
        total += Z[i] * Ms[i]
    total = sp.simplify(total)
    H_term_expected = sp.simplify(t * sp.Rational(3, 2) * c * I2)
    matches = sp.simplify(total - H_term_expected) == sp.zeros(2, 2)
    M_i_formula = [str(sp.simplify(M / (t * c)) if (t * c) != 0 else str(M)) for M in Ms]
    return {
        "sum_i_Zi_Mi(t)": str(total),
        "expected_t_times_H": str(H_term_expected),
        "matches_eq5_H_term": bool(matches),
        "M_i(t)_as_coefficient_of_(t*c)": M_i_formula,
    }


# ---------------------------------------------------------------------------
# Step 3: t=0 kernel -- trivial, direct.
# ---------------------------------------------------------------------------


def step3_t0_kernel(Ms: list[sp.Matrix]) -> dict:
    Ms_at_0 = [sp.simplify(M.subs(t, 0)) for M in Ms]
    all_zero = all(M == sp.zeros(2, 2) for M in Ms_at_0)
    return {
        "M_i(t=0)_all_zero": bool(all_zero),
        "conclusion": (
            "Nabla^0_{Z_i}psi = Z_i(psi) for all i => parallel condition is "
            "psi = CONSTANT function on SU(2). ANY vector in C^2 is a valid "
            "kernel vector; e.g. psi_0_A=(1,0)^T, psi_0_B=(0,1)^T span the "
            "full 2-dim kernel."
        )
        if all_zero
        else "FAILED -- M_i(0) not zero, something is wrong upstream.",
    }


# ---------------------------------------------------------------------------
# Step 4: t=1 candidate construction via e_i identification + matrix-inverse
#         calculus.
# ---------------------------------------------------------------------------


def step4_ei_identification_check(c_value: int = 2) -> dict:
    """Check which sign of e_i := +-i*sigma_i reproduces [e_i,e_j]=c*eps_ijk*e_k
    at c=c_value (E2's calibrated value). Both signs tested explicitly."""
    sigmas = pauli_matrices()
    results = {}
    for sign_label, sign in [("e_i = -i*sigma_i", -1), ("e_i = +i*sigma_i", +1)]:
        e = [sign * IMAG * s for s in sigmas]
        # check [e_1,e_2] = c_value * eps_123 * e_3 = c_value * e_3
        lhs = sp.simplify(e[0] * e[1] - e[1] * e[0])
        rhs = sp.simplify(c_value * e[2])
        matches = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
        results[sign_label] = {
            "[e1,e2]": str(lhs),
            "c_value*e3": str(rhs),
            "matches": bool(matches),
        }
    return results


def step4_parallel_condition_check(Ms: list[sp.Matrix], c_value: int = 2) -> dict:
    """Verify Z_i(psi_1) = -e_i . psi_1 (from calculus of g^{-1}, e_i=-i*sigma_i)
    matches the REQUIRED condition Z_i(psi) = -M_i(1).psi (parallel condition
    Nabla^1_{Z_i}psi=0 <=> Z_i(psi)=-M_i(1)psi), i.e. checks
        -e_i  ==  -M_i(1)|_{c=c_value}   as matrices, for each i.
    """
    sigmas = pauli_matrices()
    e = [-IMAG * s for s in sigmas]  # the identification forced by Step 4a (c=+2)
    Ms_at_1 = [sp.simplify(M.subs({t: 1, c: c_value})) for M in Ms]
    per_i = []
    all_match = True
    for i in range(3):
        required = sp.simplify(-Ms_at_1[i])  # Z_i(psi) = -M_i(1) psi required
        candidate = sp.simplify(-e[i])  # Z_i(psi) = -e_i psi from g^{-1} calculus
        ok = sp.simplify(required - candidate) == sp.zeros(2, 2)
        all_match &= ok
        per_i.append(
            {
                "i": i + 1,
                "minus_M_i(1)_required": str(required),
                "minus_e_i_from_ginverse_calculus": str(candidate),
                "matches": bool(ok),
            }
        )
    return {"per_i": per_i, "all_i_match": bool(all_match)}


def step5_holonomy_vs_c168(p_value: int = 3) -> dict:
    """Compute zeta_p and zeta_p^{-1} explicitly (C167/C168's own convention),
    and report the derived holonomy zeta_p^{-1} vs C168's assumed H_1=zeta_p."""
    theta = 2 * sp.pi / p_value
    zeta = sp.Matrix([[sp.exp(IMAG * theta), 0], [0, sp.exp(-IMAG * theta)]])
    zeta_inv = sp.simplify(zeta.inv())
    same_as_zeta = sp.simplify(zeta_inv - zeta) == sp.zeros(2, 2)

    def sort_key(v: sp.Expr) -> tuple[float, float]:
        n = complex(sp.N(v))
        return (n.real, n.imag)

    eigs_zeta = sorted((sp.N(v) for v in zeta.eigenvals()), key=sort_key)
    eigs_zeta_inv = sorted((sp.N(v) for v in zeta_inv.eigenvals()), key=sort_key)
    return {
        "zeta_p": str(zeta),
        "zeta_p_inverse": str(zeta_inv),
        "zeta_p_inverse_equals_zeta_p": bool(same_as_zeta),
        "eigenvalues_as_a_set_match": str(eigs_zeta) == str(eigs_zeta_inv),
        "conclusion": (
            "C170's derived holonomy for psi_1(g)=g^{-1}psi_0 is zeta_p^{-1}, "
            "NOT zeta_p as C168 modeled it. zeta_p^{-1} != zeta_p as MATRICES "
            "(swapped diagonal), though {eigenvalues} match as a SET. This "
            "means the SPECIFIC eigenvector-of-H_1 computation C168 did "
            "cannot be reused as-is for this candidate; it would need to be "
            "redone with H_1'=zeta_p^{-1} (or the psi_1 ansatz itself "
            "re-derived to target zeta_p directly, e.g. psi_1(g)=g.psi_0 "
            "instead of g^{-1}.psi_0 -- NOT attempted this round)."
        ),
    }


def step6_ht_alone_eigenvalue_1_check(p_value: int = 3) -> dict:
    """Task item 4, read at the level the explicit vectors actually live in:
    is psi_0 (t=0) / psi_1(e)=psi_0 (t=1) an eigenvector of H_t ALONE (not
    H_t (x) tau) with eigenvalue exactly 1? This is well-posed and answerable
    independently of the Step 5 holonomy-convention ambiguity, because it
    only needs H_t's own SPECTRUM, not which specific eigenvector attaches
    to which specific psi_0.
    """
    H0 = sp.eye(2)
    theta = 2 * sp.pi / p_value
    H1 = sp.Matrix([[sp.exp(IMAG * theta), 0], [0, sp.exp(-IMAG * theta)]])  # C168's H_1=zeta_p

    H0_eigs = list(H0.eigenvals().keys())
    H1_eigs = [sp.simplify(v) for v in H1.eigenvals()]

    H0_has_eig_1 = any(sp.simplify(v - 1) == 0 for v in H0_eigs)
    H1_has_eig_1 = any(sp.simplify(v - 1) == 0 for v in H1_eigs)

    return {
        "H0_eigenvalues": [str(v) for v in H0_eigs],
        "H0_has_eigenvalue_1": bool(H0_has_eig_1),
        "H0_conclusion": (
            "H0=I2 (C168's own MODELING ASSUMPTION), so EVERY vector, "
            "including psi_0 (any nonzero element of C^2, the t=0 kernel) "
            "is trivially an eigenvalue-1 eigenvector. Vacuous: this holds "
            "for ANY vector, not specifically because psi_0 is a kernel "
            "vector of D_S3(0)."
        ),
        "H1_eigenvalues": [str(v) for v in H1_eigs],
        "H1_has_eigenvalue_1": bool(H1_has_eig_1),
        "H1_conclusion": (
            "H1=zeta_3 has eigenvalues {omega,omega^2} (primitive cube "
            "roots of unity), NEITHER equal to 1. Consequence: NO nonzero "
            "vector in C^2 -- regardless of which specific psi_1 candidate "
            "is used, and REGARDLESS of the Step 5 holonomy-convention "
            "ambiguity (zeta_3^{-1} has the SAME eigenvalue set) -- can ever "
            "be an eigenvalue-1 eigenvector of H_1 ALONE. This is a clean, "
            "convention-independent NO for the H_t-alone reading of task "
            "item 4 at t=1."
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    step1 = step1_omega_check(Z)

    Ms = connection_matrices(Z)
    step2 = step2_self_consistency(Z, Ms)

    step3 = step3_t0_kernel(Ms)

    step4a = step4_ei_identification_check(c_value=2)
    step4b = step4_parallel_condition_check(Ms, c_value=2)

    step5 = step5_holonomy_vs_c168(p_value=3)
    step6 = step6_ht_alone_eigenvalue_1_check(p_value=3)

    result = {
        "step1_omega_recheck": step1,
        "step2_connection_self_consistency": step2,
        "step3_t0_kernel": step3,
        "step4a_ei_identification_sign_check": step4a,
        "step4b_t1_parallel_condition_check": step4b,
        "step5_holonomy_vs_c168_convention": step5,
        "step6_ht_alone_eigenvalue_1_check": step6,
        "verdict": {
            "t0_kernel_certified": bool(step3["M_i(t=0)_all_zero"]),
            "connection_formula_self_consistent": bool(step2["matches_eq5_H_term"]),
            "t1_candidate_satisfies_parallel_PDE": bool(step4b["all_i_match"]),
            # BUG FIX (caught on first run): the derived holonomy for
            # psi_1(g)=g^{-1}.psi_0 IS zeta_p^{-1} (Step 5). This matches
            # C168's assumed H_1=zeta_p directly iff zeta_p^{-1}==zeta_p,
            # i.e. iff step5's own "zeta_p_inverse_equals_zeta_p" is TRUE
            # -- NOT its negation. The original line here had the polarity
            # backwards (silently asserting a match where none exists);
            # fixed to read the flag directly, no negation.
            "t1_candidate_matches_c168_H1_convention_directly": bool(
                step5["zeta_p_inverse_equals_zeta_p"]
            ),
            "t0_survives_Ht_alone_eigenvalue_1": bool(step6["H0_has_eigenvalue_1"]),
            "t1_survives_Ht_alone_eigenvalue_1": bool(step6["H1_has_eigenvalue_1"]),
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    with open("results_c170.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print("\nSaved: results_c170.json")
