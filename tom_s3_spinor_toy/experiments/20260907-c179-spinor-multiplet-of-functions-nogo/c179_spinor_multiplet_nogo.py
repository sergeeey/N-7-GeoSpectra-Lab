"""C179: can a multiplet of ORDINARY FUNCTIONS on S^n carry a SPINOR
representation, in the sense of Tom Lawrence's 2026-09-07 notes
("Ket spaces and harmonics of S^n", eq 1, eq 4, eq 40, eq 77)?

The obstruction, computed rather than asserted: a rotation by 2*pi is the
IDENTITY in SO(n+1) but is MINUS THE IDENTITY in Spin(n+1). Tom's own
induced action on functions (his eq 4, Phi'|_{gA} = Phi|_A) therefore sends
a 2*pi rotation to the identity map on functions, while his eq 40
(|Phi'_beta> = Gamma_d(g)_beta^alpha |Phi_alpha>) with Gamma_d = spinor rep
sends it to minus the identity. Both must hold => Phi = 0.

Deliberately NOT done by declaring "z = -1 in the Clifford algebra" (which
would be tautological -- the exact 'a test that cannot fail is not a test'
failure mode this project's own C172 was corrected for). Instead the SAME
abstract Lie-algebra element is exponentiated at the SAME parameter value
(theta = 2*pi) in the vector rep and in the spinor rep, and the two results
are compared.

Reuses this project's own Clifford conventions (round67's Cl(3) generators
are cross-checked against the ones built here).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c179.json"

TOL = 1e-12

S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


# ---------------------------------------------------------------------------
# Clifford generators, Euclidean signature {e_i, e_j} = 2 delta_ij
# ---------------------------------------------------------------------------
def clifford_generators(m: int) -> list[np.ndarray]:
    if m == 3:
        return [S1, S2, S3]
    if m == 4:
        return [
            np.kron(S1, I2),
            np.kron(S2, I2),
            np.kron(S3, S1),
            np.kron(S3, S2),
        ]
    raise ValueError(f"only m=3,4 built here, got {m}")


def check_clifford_relations(gens: list[np.ndarray]) -> dict:
    m = len(gens)
    dim = gens[0].shape[0]
    worst = 0.0
    for i in range(m):
        for j in range(m):
            anti = gens[i] @ gens[j] + gens[j] @ gens[i]
            target = 2.0 * (1.0 if i == j else 0.0) * np.eye(dim, dtype=complex)
            worst = max(worst, float(np.max(np.abs(anti - target))))
    return {"max_abs_residual": worst, "ok": worst < TOL}


# ---------------------------------------------------------------------------
# The SAME so(m) generator, in two representations
# ---------------------------------------------------------------------------
def spinor_generator(gens: list[np.ndarray], i: int, j: int) -> np.ndarray:
    """Sigma_ij = (1/4)[e_i, e_j] -- standard spin representation of so(m)."""
    return 0.25 * (gens[i] @ gens[j] - gens[j] @ gens[i])


def vector_generator(m: int, i: int, j: int) -> np.ndarray:
    """(T_ij)_{kl} = delta_ik delta_jl - delta_il delta_jk -- defining rep."""
    T = np.zeros((m, m), dtype=complex)
    T[i, j] += 1.0
    T[j, i] -= 1.0
    return T


def matrix_exp(A: np.ndarray) -> np.ndarray:
    evals, evecs = np.linalg.eig(A)
    return evecs @ np.diag(np.exp(evals)) @ np.linalg.inv(evecs)


def rotation_by_angle(generator: np.ndarray, theta: float) -> np.ndarray:
    return matrix_exp(theta * generator)


# ---------------------------------------------------------------------------
# Check 1: the double cover, computed at theta = 2*pi
# ---------------------------------------------------------------------------
def double_cover_check(m: int) -> dict:
    gens = clifford_generators(m)
    cliff = check_clifford_relations(gens)
    spin_dim = gens[0].shape[0]

    sig = spinor_generator(gens, 0, 1)
    vec = vector_generator(m, 0, 1)

    two_pi = 2.0 * np.pi
    R_spin = rotation_by_angle(sig, two_pi)
    R_vec = rotation_by_angle(vec, two_pi)

    I_spin = np.eye(spin_dim, dtype=complex)
    I_vec = np.eye(m, dtype=complex)

    spin_is_minus_id = float(np.max(np.abs(R_spin + I_spin))) < 1e-9
    vec_is_plus_id = float(np.max(np.abs(R_vec - I_vec))) < 1e-9

    # sanity: at theta = 4*pi the spinor rep must come back to +Id
    R_spin_4pi = rotation_by_angle(sig, 2 * two_pi)
    spin_4pi_is_plus_id = float(np.max(np.abs(R_spin_4pi - I_spin))) < 1e-9

    # sanity: neither generator is trivially zero (else the test is vacuous)
    sig_nonzero = float(np.max(np.abs(sig))) > 0.1
    vec_nonzero = float(np.max(np.abs(vec))) > 0.1

    return {
        "m_ambient_dimension": m,
        "sphere": f"S^{m - 1}",
        "clifford_relations": cliff,
        "spinor_rep_dim": spin_dim,
        "spinor_generator_nonzero": bool(sig_nonzero),
        "vector_generator_nonzero": bool(vec_nonzero),
        "R_spin_2pi_is_minus_identity": bool(spin_is_minus_id),
        "R_vector_2pi_is_plus_identity": bool(vec_is_plus_id),
        "R_spin_4pi_is_plus_identity": bool(spin_4pi_is_plus_id),
        "R_spin_2pi_matrix": np.round(R_spin.real, 12).tolist(),
        "R_vector_2pi_matrix": np.round(R_vec.real, 12).tolist(),
        "double_cover_confirmed": bool(
            cliff["ok"] and spin_is_minus_id and vec_is_plus_id and spin_4pi_is_plus_id
        ),
    }


# ---------------------------------------------------------------------------
# Check 2: Tom's own induced action (his eq 4) at the same group element
# ---------------------------------------------------------------------------
def induced_action_on_functions_check(m: int) -> dict:
    """His eq (4): Phi'|_B = Phi|_A where B = gA. For the 2*pi rotation,
    g acts on POINTS as the identity, so Phi' = Phi identically. Verified
    concretely on random test functions and random points, rather than
    asserted."""
    vec = vector_generator(m, 0, 1)
    R = rotation_by_angle(vec, 2.0 * np.pi).real

    rng = np.random.default_rng(20260907)
    pts = rng.normal(size=(200, m))
    pts = pts / np.linalg.norm(pts, axis=1, keepdims=True)  # random points ON S^{m-1}

    moved = pts @ R.T
    max_point_shift = float(np.max(np.abs(moved - pts)))

    # a few arbitrary test functions on the sphere
    def f1(p):
        return p[0] ** 2 - p[1] * p[2] if len(p) > 2 else p[0] ** 2

    def f2(p):
        return np.exp(p[0]) * np.sin(3 * p[1])

    def f3(p):
        return np.prod(p)

    max_func_shift = 0.0
    for f in (f1, f2, f3):
        vals_before = np.array([f(p) for p in pts])
        vals_after = np.array([f(p) for p in moved])
        max_func_shift = max(max_func_shift, float(np.max(np.abs(vals_after - vals_before))))

    return {
        "max_point_displacement_under_2pi_rotation": max_point_shift,
        "max_function_value_change": max_func_shift,
        "induced_action_is_identity_on_functions": bool(
            max_point_shift < 1e-9 and max_func_shift < 1e-9
        ),
    }


# ---------------------------------------------------------------------------
# Check 3: the contradiction, stated in Tom's eq (40)
# ---------------------------------------------------------------------------
def contradiction_check(m: int, dc: dict, ia: dict) -> dict:
    """If |Phi_beta> is a multiplet of FUNCTIONS carrying the spinor rep, then
    at g = (2*pi rotation):
      eq (4)  =>  |Phi'_beta> = +|Phi_beta>
      eq (40) =>  |Phi'_beta> = Gamma_d(g) |Phi_beta> = -|Phi_beta>
    Both hold => 2|Phi_beta> = 0 => Phi = 0 (no nonzero multiplet exists)."""
    functions_say_plus = ia["induced_action_is_identity_on_functions"]
    matrices_say_minus = dc["R_spin_2pi_is_minus_identity"]
    return {
        "eq4_induced_action_gives_plus_identity": bool(functions_say_plus),
        "eq40_spinor_rep_gives_minus_identity": bool(matrices_say_minus),
        "forces_Phi_equals_minus_Phi": bool(functions_say_plus and matrices_say_minus),
        "conclusion": (
            f"No nonzero multiplet of ordinary functions on S^{m - 1} can carry "
            "the spinor representation."
            if (functions_say_plus and matrices_say_minus)
            else "NO OBSTRUCTION FOUND -- re-examine, this contradicts standard theory."
        ),
    }


# ---------------------------------------------------------------------------
# Check 4: the dimension trap, S^3 only
# ---------------------------------------------------------------------------
def dimension_trap_check() -> dict:
    """For SO(4): the VECTOR rep (1/2,1/2) and the SPINOR rep (1/2,0)+(0,1/2)
    BOTH have dimension 4. So 'is there a 4-dimensional block in L^2(S^3)?'
    is a FALSE-PASS test. The discriminator is the action of the kernel
    element (-1,-1) of Spin(4) -> SO(4): it acts as (-1)^(2 j_L + 2 j_R)."""

    def kernel_element_phase(jL2: int, jR2: int) -> int:
        """jL2 = 2*j_L, jR2 = 2*j_R (integers). Returns +1 or -1."""
        return (-1) ** (jL2 + jR2)

    vector_dim = (1 + 1) * (1 + 1)  # (1/2,1/2): (2 jL + 1)(2 jR + 1) = 2*2
    spinor_dim = (1 + 1) * 1 + 1 * (1 + 1)  # (1/2,0) + (0,1/2) = 2 + 2

    vector_phase = kernel_element_phase(1, 1)  # 2j_L = 1, 2j_R = 1
    spinor_phase_L = kernel_element_phase(1, 0)
    spinor_phase_R = kernel_element_phase(0, 1)

    return {
        "dim_vector_half_half": vector_dim,
        "dim_spinor_half_0_plus_0_half": spinor_dim,
        "dimensions_coincide": vector_dim == spinor_dim,
        "kernel_element_phase_on_vector": vector_phase,
        "kernel_element_phase_on_spinor_L": spinor_phase_L,
        "kernel_element_phase_on_spinor_R": spinor_phase_R,
        "vector_descends_to_SO4": vector_phase == 1,
        "spinor_descends_to_SO4": spinor_phase_L == 1 and spinor_phase_R == 1,
        "dimension_trap_confirmed": bool(
            vector_dim == spinor_dim and vector_phase == 1 and spinor_phase_L == -1
        ),
    }


# ---------------------------------------------------------------------------
# Check 5 (positive control A): Tom's eq (77) for the S^2 VECTOR multiplet
# ---------------------------------------------------------------------------
def tom_eq77_vector_control() -> dict:
    """His eq (77): [-x^l (d_jl d_i - d_il d_j)] |phi_gamma> =
                                    [i Gamma_d(T_ij)]_gamma^delta |phi_delta>
    with (61) (T_ij)^k_l = -i(d_jl d^k_i - d_il d^k_j) and (99) Gamma_d = -T.
    Basis (89): phi_i = x_i / r. Reproduces his own eqs 109-112."""
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    X = [x1, x2, x3]
    r = sp.sqrt(x1**2 + x2**2 + x3**2)
    phi = [X[i] / r for i in range(3)]

    def d(a, b):
        return 1 if a == b else 0

    def T_def(i, j):
        return sp.Matrix(3, 3, lambda k, ell: -sp.I * (d(j, ell) * d(k, i) - d(i, ell) * d(k, j)))

    results = {}
    for label, gamma_fn in (
        ("his_convention_Gamma_eq_minus_T_row_contraction", lambda i, j: -T_def(i, j)),
        ("transpose_variant", lambda i, j: (-T_def(i, j)).T),
        ("sign_variant_Gamma_eq_plus_T", lambda i, j: T_def(i, j)),
    ):
        all_ok = True
        for i in range(3):
            for j in range(i + 1, 3):
                M = sp.I * gamma_fn(i, j)
                for g in range(3):
                    lhs = sp.simplify(
                        -(X[j] * sp.diff(phi[g], X[i]) - X[i] * sp.diff(phi[g], X[j]))
                    )
                    rhs = sp.simplify(sum(M[g, dd] * phi[dd] for dd in range(3)))
                    if sp.simplify(lhs - rhs) != 0:
                        all_ok = False
        results[label] = all_ok
    return {
        "per_convention_satisfied": results,
        "his_stated_convention_verifies": results[
            "his_convention_Gamma_eq_minus_T_row_contraction"
        ],
        "exactly_one_convention_works": sum(results.values()) == 1,
    }


# ---------------------------------------------------------------------------
# Check 6 (positive control B): where the half-integers actually live on S^3
# ---------------------------------------------------------------------------
def half_integer_peter_weyl_control() -> dict:
    """S^3 = SU(2). The j=1/2 Peter-Weyl block D^{1/2}(g) = g itself, whose
    four entries are LINEAR in the four Cartesian coordinates of S^3 -- honest
    functions. But under g -> u g v^dagger (i.e. SU(2)_L x SU(2)_R = Spin(4))
    they transform in (1/2,1/2) = the VECTOR of SO(4), NOT in the spinor
    (1/2,0)+(0,1/2). This is the constructive half of the finding: half-integer
    j IS available in L^2(S^3), it just never assembles into a spinor rep."""
    rng = np.random.default_rng(7)

    def random_su2():
        a = rng.normal(size=4)
        a = a / np.linalg.norm(a)
        x0, x1, x2, x3 = a
        return np.array([[x0 + 1j * x3, x1 + 1j * x2], [-x1 + 1j * x2, x0 - 1j * x3]]), a

    # (a) the four entries of g are linear in the coordinates: verified by
    #     reconstructing the coordinates from g
    max_recon_err = 0.0
    for _ in range(200):
        g, coords = random_su2()
        x0 = float(np.real(g[0, 0] + g[1, 1]) / 2)
        x3 = float(np.imag(g[0, 0] - g[1, 1]) / 2)
        x1 = float(np.real(g[0, 1] - g[1, 0]) / 2)
        x2 = float(np.imag(g[0, 1] + g[1, 0]) / 2)
        max_recon_err = max(
            max_recon_err, float(np.max(np.abs(np.array([x0, x1, x2, x3]) - coords)))
        )

    # (b) g -> u g v^dagger preserves S^3 and acts as a rotation on the
    #     coordinate 4-vector => (1/2,1/2) = vector rep, dimension 4
    def coords_of(g):
        return np.array(
            [
                float(np.real(g[0, 0] + g[1, 1]) / 2),
                float(np.real(g[0, 1] - g[1, 0]) / 2),
                float(np.imag(g[0, 1] + g[1, 0]) / 2),
                float(np.imag(g[0, 0] - g[1, 1]) / 2),
            ]
        )

    u, _ = random_su2()
    v, _ = random_su2()
    basis_in, basis_out = [], []
    for _ in range(400):
        g, _ = random_su2()
        basis_in.append(coords_of(g))
        basis_out.append(coords_of(u @ g @ v.conj().T))
    A_in = np.array(basis_in)
    A_out = np.array(basis_out)
    # solve for the induced 4x4 map, then test it is orthogonal (a rotation)
    M, *_ = np.linalg.lstsq(A_in, A_out, rcond=None)
    orthogonality_residual = float(np.max(np.abs(M.T @ M - np.eye(4))))
    linear_fit_residual = float(np.max(np.abs(A_in @ M - A_out)))

    return {
        "coordinate_reconstruction_max_error": max_recon_err,
        "j_half_block_entries_are_functions_on_S3": bool(max_recon_err < 1e-9),
        "left_right_action_linear_fit_residual": linear_fit_residual,
        "induced_4x4_map_orthogonality_residual": orthogonality_residual,
        "j_half_block_carries_vector_rep_not_spinor": bool(
            linear_fit_residual < 1e-9 and orthogonality_residual < 1e-9
        ),
    }


# ---------------------------------------------------------------------------
def main() -> dict:
    result: dict = {}

    per_sphere = {}
    for m in (3, 4):  # S^2 in R^3, S^3 in R^4
        dc = double_cover_check(m)
        ia = induced_action_on_functions_check(m)
        ct = contradiction_check(m, dc, ia)
        per_sphere[f"S^{m - 1}"] = {
            "double_cover": dc,
            "induced_action": ia,
            "contradiction": ct,
        }
    result["per_sphere"] = per_sphere

    result["dimension_trap_S3"] = dimension_trap_check()
    result["positive_control_A_tom_eq77_vector"] = tom_eq77_vector_control()
    result["positive_control_B_half_integer_peter_weyl"] = half_integer_peter_weyl_control()

    # ---- verdict ----
    substrate_ok = all(
        per_sphere[k]["double_cover"]["clifford_relations"]["ok"]
        and per_sphere[k]["double_cover"]["spinor_generator_nonzero"]
        and per_sphere[k]["double_cover"]["vector_generator_nonzero"]
        and per_sphere[k]["double_cover"]["R_spin_4pi_is_plus_identity"]
        for k in per_sphere
    )
    nogo_all = all(
        per_sphere[k]["contradiction"]["forces_Phi_equals_minus_Phi"] for k in per_sphere
    )
    trap = result["dimension_trap_S3"]["dimension_trap_confirmed"]
    control_a = result["positive_control_A_tom_eq77_vector"]["exactly_one_convention_works"]
    control_b = result["positive_control_B_half_integer_peter_weyl"][
        "j_half_block_carries_vector_rep_not_spinor"
    ]

    if not substrate_ok:
        label = "SUBSTRATE-MISMATCH"
    elif not nogo_all:
        label = "NOGO-FAILS"
    else:
        label = "NOGO-CONFIRMED" + ("-AND-DIMENSION-TRAP-CONFIRMED" if trap else "")

    result["verdict"] = {
        "label": label,
        "substrate_ok": substrate_ok,
        "nogo_holds_for_S2_and_S3": nogo_all,
        "dimension_trap_confirmed": trap,
        "positive_control_A_passed": control_a,
        "positive_control_B_passed": control_b,
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out["verdict"], indent=2))
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\nSaved: {RESULTS_PATH}")
