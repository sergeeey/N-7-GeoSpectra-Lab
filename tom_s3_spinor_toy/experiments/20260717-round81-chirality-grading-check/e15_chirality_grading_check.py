r"""E15 (round81): does the natural S3 Clifford volume element / grading operator
split the 2-dimensional torsion-crossing zero-mode kernel found in E12
(experiments/20260717-round78-e12-multiplicity-gate/), giving a candidate
mechanism for reducing the doublet to a single physical state?

Context (see claim.md for full framing):
  - E12 (round78) tool-verified dim_C ker(D_{S3,t=0 or 1}) = 2 -- the FULL
    2-dimensional space of constant (t=0) / gbar-twisted-constant (t=1) spinors
    is the kernel, not a single vector. Combined with G74A's S6-side
    dim ker=1 per channel, this gives 6 total internal zero modes across the
    3 triality channels, vs the 3 needed for N_gen=3 -- the "excess factor 2"
    problem this round is trying to attack.
  - round80 (E14) showed a genuine geometric Z2 (group inversion iota) swaps
    t=0 and t=1 sectors, but explicitly showed (Section E "Reading 1") that
    WITHIN a single fixed t, the doublet is an IRREDUCIBLE SU(2) multiplet --
    no natural 1-dim invariant subspace exists under the manifest continuous
    symmetry.
  - This round asks a DIFFERENT, cheaper question: is there a natural
    DISCRETE grading/chirality operator (not a continuous symmetry) built
    from the Clifford structure of the tensor-product Dirac operator
    D_full = D_{S3,t} \otimes I_{S6} + Gamma_{S3} \otimes D_{S6,twisted}
    that splits the doublet into two 1-dim eigenspaces?

  The natural candidate, using this project's OWN already-established
  convention (E2's own script, experiments/20260717-round67-e2-s3-torsion-
  deformation/e2_s3_torsion_deformation.py, function
  compute_omega_and_check_scalar): the Cl(3) volume element
    omega := Z1 . Z2 . Z3,   Z_i = i*sigma_i  (E2/E9/E10/E12's own convention)
  E2 ALREADY computed (for a completely different purpose -- calibrating the
  Kostant cubic element H = (3c/2)*omega inside Agricola's D^t formula, NOT
  as a chirality operator) that omega is EXACTLY a scalar multiple of I2, and
  omega^2 = I2. This script:
  1. [VERIFIED-tool] Re-derives this INDEPENDENTLY, from scratch, framed
     explicitly as "is this a candidate grading/chirality operator" (not
     re-using E2's own framing or citing its result without re-computing).
  2. [VERIFIED-tool] Computes the EXACT eigenvalues/eigenvectors of omega via
     sympy .eigenvects(), not just checking "proportional to I2" as a binary
     flag -- to see explicitly whether there are one or two distinct
     eigenvalues.
  3. [VERIFIED-tool] Applies omega to the FULLY GENERIC t=0 kernel vector
     psi=(a,b) (symbolic a,b, not spot-checked at (1,0)/(0,1) alone -- same
     rigor standard E12 used) and checks whether omega*psi = lambda*psi for a
     SINGLE lambda valid for all (a,b), or whether the two components split
     under different eigenvalues.
  4. [VERIFIED-tool] Repeats the same check at t=1, using the gbar-twisted
     kernel basis from E12/E10 (psi(x) = gbar(x)*(a_,b_)), confirming that
     since omega is CONSTANT (does not depend on x, t, or the frame), the
     splitting-or-not verdict is frame/t-independent by construction -- this
     is checked directly, not merely asserted from omega's constancy.
  5. [DERIVED, standard Clifford-algebra fact, stated not just asserted]
     explains WHY this outcome (scalar or split) is forced by the structure
     of Cl(3): Cl(n)'s volume element e_1...e_n is CENTRAL iff n is odd (a
     standard fact for real/complex Clifford algebras), and for a specific
     2-dimensional IRREDUCIBLE representation (the Pauli/spinor
     representation used throughout this project), a central element must
     act as a scalar by Schur's lemma. This is checked here by direct
     computation (the centrality checks in step 1), not merely cited.
  6. [VERIFIED-tool] Explicitly checks the DEGENERATE alternative: does ANY
     linear combination alpha*Z1+beta*Z2+gamma*Z3 (a general Cl(3) DEGREE-1,
     i.e. "vector-type", element -- not a chirality/grading candidate, but
     checked here to be thorough and to make sure no other single natural
     Clifford element of low degree happens to split the doublet either)
     have two distinct eigenvalues on C^2? (Expected: yes, since these are
     just Pauli-type Hermitian traceless matrices -- but this does NOT make
     them "chirality operators": a chirality/grading operator must be built
     from the FULL-DIMENSIONAL volume element / commute appropriately with
     the connection, not be an arbitrary vector-type Clifford element that
     transforms non-trivially under the very SU(2) whose irreducibility E14
     already established. This is reported as a side-note, not conflated
     with the main omega question.)

Honesty ledger:
  - Step 1 (Clifford relations, omega scalar/central): [VERIFIED-tool], exact
    symbolic computation, independent re-derivation (not a citation of E2).
  - Step 2 (exact eigenvalues via sympy .eigenvects()): [VERIFIED-tool].
  - Steps 3-4 (action on the generic kernel bases at t=0 and t=1):
    [VERIFIED-tool], exact symbolic computation on fully generic (a,b).
  - Step 5 (Cl(3) centrality-in-odd-dimension + Schur's lemma argument):
    [DOCS/derivation] -- standard Clifford-algebra representation theory
    (Lawson-Michelsohn "Spin Geometry", already cited by this project's own
    E9/E10 scripts for the spin-connection formula), NOT independently
    re-derived from Clifford-algebra axioms in this script, but its
    APPLICATION to this specific case (n=3, this specific 2-dim irrep) is
    directly grounded in step 1's own centrality computation, not asserted
    by bare analogy.
  - Step 6 (vector-type elements as a side-note, NOT the main claim):
    [VERIFIED-tool] for the computation; the interpretive caveat (why this
    does not count as a chirality operator) is [ARGUED], not computed.
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
a, b, a_, b_ = sp.symbols("a b a_ b_")
alpha, beta, gamma = sp.symbols("alpha beta gamma", real=True)
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)


# ---------------------------------------------------------------------------
# Step 1: Cl(3) via Pauli matrices -- IDENTICAL convention to E2/E9/E10/E12
# (independently re-derived here, not imported/cited)
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i, giving {Z_i,Z_j} = -2 delta_ij (E2/E9/E10/E12's own
    convention, re-derived here independently)."""
    return [sp.I * s for s in pauli_matrices()]


def verify_clifford_relations(Z: list[sp.Matrix]) -> dict[str, object]:
    """[VERIFIED-tool] Re-check {Z_i,Z_j} = -2 delta_ij Id exactly, all 6 pairs."""
    results = {}
    ok = True
    for i in range(3):
        for j in range(i, 3):
            anticomm = sp.simplify(Z[i] * Z[j] + Z[j] * Z[i])
            expected = -2 * I2 if i == j else sp.zeros(2, 2)
            match = bool(sp.simplify(anticomm - expected) == sp.zeros(2, 2))
            results[f"Z{i + 1}Z{j + 1}"] = match
            ok &= match
    return {"pairwise": results, "all_ok": ok}


# ---------------------------------------------------------------------------
# Step 1 (continued) + Step 2: omega = Z1.Z2.Z3, scalarity, centrality, exact
# eigenstructure
# ---------------------------------------------------------------------------


def compute_omega(Z: list[sp.Matrix]) -> sp.Matrix:
    return sp.simplify(Z[0] * Z[1] * Z[2])


def check_scalar_and_central(omega: sp.Matrix, Z: list[sp.Matrix]) -> dict[str, object]:
    off_diag_zero = bool(sp.simplify(omega[0, 1]) == 0 and sp.simplify(omega[1, 0]) == 0)
    diag_equal = bool(sp.simplify(omega[0, 0] - omega[1, 1]) == 0)
    is_scalar = off_diag_zero and diag_equal
    scalar_value = sp.simplify(omega[0, 0]) if is_scalar else None

    centrality = {}
    all_central = True
    for i in range(3):
        comm = sp.simplify(omega * Z[i] - Z[i] * omega)
        c_ok = bool(comm == sp.zeros(2, 2))
        centrality[f"omega_commutes_Z{i + 1}"] = c_ok
        all_central &= c_ok

    omega_sq = sp.simplify(omega * omega)
    omega_sq_is_I = bool(sp.simplify(omega_sq - I2) == sp.zeros(2, 2))

    return {
        "omega_matrix": str(omega),
        "is_scalar_times_identity": is_scalar,
        "scalar_value": str(scalar_value),
        "off_diagonal_entries_zero": off_diag_zero,
        "diagonal_entries_equal": diag_equal,
        "centrality_checks": centrality,
        "all_central": bool(all_central),
        "omega_squared": str(omega_sq),
        "omega_squared_equals_identity": omega_sq_is_I,
    }


def exact_eigenstructure(M: sp.Matrix) -> dict[str, object]:
    """[VERIFIED-tool] Full eigenvalue/eigenvector decomposition via sympy's
    own .eigenvects(), the ground-truth structural check for "does this
    operator split C^2 into two 1-dim eigenspaces, or is the whole space one
    eigenspace"."""
    ev = M.eigenvects()
    n_distinct_eigenvalues = len(ev)
    report = []
    for eigval, mult, vecs in ev:
        report.append(
            {
                "eigenvalue": str(sp.simplify(eigval)),
                "algebraic_multiplicity": mult,
                "eigenvectors": [str(v.T) for v in vecs],
            }
        )
    return {
        "n_distinct_eigenvalues": n_distinct_eigenvalues,
        "eigen_report": report,
        "splits_into_two_1dim_eigenspaces": bool(n_distinct_eigenvalues == 2),
        "single_eigenspace_is_all_of_C2": bool(n_distinct_eigenvalues == 1),
    }


# ---------------------------------------------------------------------------
# Step 3: action of omega on the fully generic t=0 kernel vector (a,b), per
# E9/E12's own convention (constant left-invariant spinor)
# ---------------------------------------------------------------------------


def check_action_on_generic_kernel_t0(omega: sp.Matrix) -> dict[str, object]:
    psi = sp.Matrix([a, b])
    omega_psi = sp.expand(omega * psi)
    # Is omega*psi proportional to psi with a SINGLE, psi-independent scalar?
    # Extract candidate scalar from ratio of components where possible; a
    # true single-eigenvalue action requires omega_psi == lam*psi for some
    # constant lam, for ALL (a,b) simultaneously -- check this directly by
    # solving (omega - lam*I)*psi = 0 identically in a,b for a constant lam.
    lam = sp.symbols("lam")
    residual = sp.expand(omega * psi - lam * psi)
    # collect coefficients of a and b in each row; both must vanish for the
    # SAME lam for the action to be proportional to identity on all of C^2.
    coeffs_row0_a = residual[0].coeff(a)
    coeffs_row0_b = residual[0].coeff(b)
    coeffs_row1_a = residual[1].coeff(a)
    coeffs_row1_b = residual[1].coeff(b)
    sol = sp.solve(
        [
            sp.Eq(coeffs_row0_a, 0),
            sp.Eq(coeffs_row0_b, 0),
            sp.Eq(coeffs_row1_a, 0),
            sp.Eq(coeffs_row1_b, 0),
        ],
        [lam],
        dict=True,
    )
    single_lambda_works_for_all_ab = len(sol) >= 1
    lambda_value = str(sol[0][lam]) if single_lambda_works_for_all_ab else None

    return {
        "psi_generic": "(a, b)",
        "omega_psi": str(omega_psi.T),
        "single_lambda_solves_omega_psi_eq_lambda_psi_for_all_a_b": bool(
            single_lambda_works_for_all_ab
        ),
        "lambda_value": lambda_value,
        "verdict_kernel_is_single_eigenspace_at_t0": bool(single_lambda_works_for_all_ab),
    }


# ---------------------------------------------------------------------------
# Step 4: action of omega on the t=1 kernel, psi(x) = gbar(x)*(a_,b_), per
# E10/E12's own right-invariant-frame convention (c0=-2 concrete realization)
# ---------------------------------------------------------------------------


def group_conjugate(Z: list[sp.Matrix]) -> sp.Matrix:
    """gbar(x) = x0*I - x1*Z1 - x2*Z2 - x3*Z3 (E10's own convention, re-derived
    here for self-containment)."""
    return x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]


def check_action_on_generic_kernel_t1(omega: sp.Matrix, Z: list[sp.Matrix]) -> dict[str, object]:
    gbar = group_conjugate(Z)
    psi0 = sp.Matrix([a_, b_])
    psi_t1 = sp.expand(gbar * psi0)  # E10/E12's own t=1 kernel family

    omega_psi_t1 = sp.expand(omega * psi_t1)

    lam = sp.symbols("lam")
    residual = sp.expand(omega_psi_t1 - lam * psi_t1)
    # Collect against a_, b_ AND the x-coordinates -- since psi_t1's components
    # are themselves linear combinations of a_,b_ with x-dependent coefficients,
    # check the identity holds for generic x AND generic (a_,b_) simultaneously.
    poly_row0 = sp.Poly(residual[0], a_, b_)
    poly_row1 = sp.Poly(residual[1], a_, b_)
    eqs = list(poly_row0.coeffs()) + list(poly_row1.coeffs())
    eqs = [sp.simplify(e) for e in eqs]
    sol = sp.solve([sp.Eq(e, 0) for e in eqs], [lam], dict=True)
    single_lambda_works = len(sol) >= 1
    lambda_value = str(sol[0][lam]) if single_lambda_works else None

    return {
        "psi_t1_generic": "gbar(x)*(a_,b_)",
        "omega_psi_t1": str(omega_psi_t1.T),
        "single_lambda_solves_for_all_x_a_b": bool(single_lambda_works),
        "lambda_value": lambda_value,
        "verdict_kernel_is_single_eigenspace_at_t1": bool(single_lambda_works),
    }


# ---------------------------------------------------------------------------
# Step 6: side-note -- do generic vector-type (degree-1) Clifford elements
# split C^2? (Expected yes -- Pauli-type Hermitian traceless matrices always
# have 2 distinct eigenvalues generically -- but this is NOT a chirality/
# grading operator, flagged explicitly as a side-note.)
# ---------------------------------------------------------------------------


def side_note_vector_type_element(Z: list[sp.Matrix]) -> dict[str, object]:
    M = alpha * Z[0] + beta * Z[1] + gamma * Z[2]
    M_at_111 = M.subs({alpha: 1, beta: 1, gamma: 1})
    ev = M_at_111.eigenvects()
    n_distinct = len(ev)
    return {
        "M_generic": "alpha*Z1+beta*Z2+gamma*Z3",
        "M_at_alpha_beta_gamma_eq_1": str(M_at_111),
        "n_distinct_eigenvalues_at_111": n_distinct,
        "splits_generically": bool(n_distinct == 2),
        "caveat": (
            "This is a DEGREE-1 (vector-type) Clifford element, not a "
            "chirality/grading operator. It transforms as a vector under the "
            "SU(2) that E14/round80 already showed acts irreducibly on this "
            "same C^2 doublet -- i.e. 'splitting' here is basis-dependent and "
            "not a natural, SU(2)-invariant statement, unlike a genuine "
            "central grading operator. Included only for completeness, not "
            "as a candidate resolution."
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    clifford = verify_clifford_relations(Z)

    omega = compute_omega(Z)
    scalar_central = check_scalar_and_central(omega, Z)
    eigenstructure = exact_eigenstructure(omega)

    t0_check = check_action_on_generic_kernel_t0(omega)
    t1_check = check_action_on_generic_kernel_t1(omega, Z)

    side_note = side_note_vector_type_element(Z)

    omega_is_trivial_grading = bool(
        scalar_central["is_scalar_times_identity"]
        and scalar_central["all_central"]
        and eigenstructure["single_eigenspace_is_all_of_C2"]
    )

    doublet_splits = bool(
        (not t0_check["verdict_kernel_is_single_eigenspace_at_t0"])
        or (not t1_check["verdict_kernel_is_single_eigenspace_at_t1"])
    )

    if omega_is_trivial_grading and not doublet_splits:
        label = "NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE"
    elif doublet_splits:
        label = "PASS_OMEGA_SPLITS_DOUBLET__CANDIDATE_MECHANISM_FOUND"
    else:
        label = "INCONCLUSIVE__UNEXPECTED_COMBINATION"

    result = {
        "step1_clifford_relations": clifford,
        "step1_2_omega_scalar_and_central": scalar_central,
        "step2_exact_eigenstructure_of_omega": eigenstructure,
        "step3_action_on_generic_kernel_t0": t0_check,
        "step4_action_on_generic_kernel_t1": t1_check,
        "step6_side_note_vector_type_element": side_note,
        "verdict": {
            "clifford_ok": clifford["all_ok"],
            "omega_is_scalar_times_identity": scalar_central["is_scalar_times_identity"],
            "omega_all_central": scalar_central["all_central"],
            "omega_single_eigenspace": eigenstructure["single_eigenspace_is_all_of_C2"],
            "kernel_splits_at_t0_or_t1": doublet_splits,
            "omega_is_trivial_grading_on_C2": omega_is_trivial_grading,
            "label": label,
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e15.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
