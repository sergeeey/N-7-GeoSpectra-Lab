"""
C136 -- does a joint generalized-Killing-spinor constraint on M4 x S3 x S6,
decomposed as eps = eps4 (x) eta3 (x) eta6, pair an S3 t-sector with an S6
triality channel asymmetrically?

Conventions follow C125 (`results_c125.json` D0-D5) and are REBUILT here from
scratch, not imported:

    Cl(6):    Gamma_a (a = 1..6), Gamma_a^2 = +1,  Gamma_7 = s * i * Gamma_1...Gamma_6
    Cl(9):    e_i     = sigma_i (x) Gamma_7        (i = 1,2,3  -- the S3 legs)
              e_{3+a} = 1_2     (x) Gamma_a        (a = 1..6   -- the S6 legs)
    Cl(1,12): Gamma^mu    = gamma^mu   (x) 1_16    (mu = 0..3)
              Gamma^{3+m} = i gamma_5  (x) e_m     (m = 1..9)

Module: C^4 (x) C^2 (x) C^8 = C^64.

`s = +1` reproduces C125's module (omega_13 = +1, Omega_3 Omega_6 = +i gamma_5).
`s = -1` is the OTHER inequivalent Cl(1,12) module (omega_13 = -1). Every
load-bearing conclusion below is run in BOTH and required to agree; a first
draft of this file silently used `s = -1` and was caught by check A7 against
C125's certified value.

S3 geometry (radius rho3, bi-invariant metric, left-invariant orthonormal
frame X_i):   [X_i, X_j] = (2/rho3) eps_ijk X_k
              T^t_ijk    = (2(2t-1)/rho3) eps_ijk    (C125 section 2a, at rho3 = 1)
              nabla^t    = nabla^LC + (1/4)(X . T^t) (Agricola 2002 Thm 4.2 cross-check)

ROUND114 TRAP BATTERY (section F) is mandatory and is why this file has this
shape. Round114 was FALSIFIED because a computed quantity collapsed to -tr(A)
independently of every input. Section F reproduces that exact collapse, then
partitions THIS round's own outputs into data-dependent and
construction-generic by actually varying the inputs.

Run:  python c136_joint_killing_spinor_check.py
"""

from __future__ import annotations

import ast
import inspect
import json
import os
import sys
from types import SimpleNamespace

import numpy as np

TOL = 1e-10
CHECKS: list[dict] = []
DATA: dict[str, object] = {}


# --------------------------------------------------------------------------
# AST self-audit (carried over from C134): a check() whose condition is a
# literal constant cannot fail and is therefore not a check.
# --------------------------------------------------------------------------
def _ast_self_audit() -> int:
    src = inspect.getsource(sys.modules[__name__])
    tree = ast.parse(src)
    n = 0
    for node in ast.walk(tree):
        is_check_call = (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
        )
        if not is_check_call:
            continue
        n += 1
        if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
            raise SystemExit(
                f"AST SELF-AUDIT FAILED: check() at line {node.lineno} "
                f"is passed a literal constant and cannot fail."
            )
    return n


def check(name: str, cond, detail: str = "") -> bool:
    ok = bool(cond)
    CHECKS.append({"name": name, "ok": ok, "detail": detail})
    if not ok:
        print(f"  [FAIL] {name} :: {detail}")
    return ok


def close(a, b, tol=TOL) -> bool:
    return bool(np.max(np.abs(np.asarray(a) - np.asarray(b))) < tol)


def is_zero(a, tol=TOL) -> bool:
    return bool(np.max(np.abs(np.asarray(a))) < tol)


def maxabs(a) -> float:
    return float(np.max(np.abs(np.asarray(a))))


# --------------------------------------------------------------------------
# A. Clifford algebras, built from scratch
# --------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [SX, SY, SZ]

EPS = np.zeros((3, 3, 3))
for _i in range(3):
    for _j in range(3):
        for _k in range(3):
            EPS[_i, _j, _k] = (_i - _j) * (_j - _k) * (_k - _i) / 2.0

Z3 = [1j * SIG[i] for i in range(3)]  # intrinsic S3 Clifford, Cl(0,3): Z_i^2 = -1

IDX_M4 = list(range(4))
IDX_S3 = list(range(4, 7))
IDX_S6 = list(range(7, 13))
ETA13 = np.diag([1.0] + [-1.0] * 12)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = np.kron(out, m)
    return out


def build_rep(gam7_sign: int = +1) -> SimpleNamespace:
    """Build the whole Cl(1,12) representation; gam7_sign picks the module."""
    G6 = [
        kron(SX, I2, I2),
        kron(SY, I2, I2),
        kron(SZ, SX, I2),
        kron(SZ, SY, I2),
        kron(SZ, SZ, SX),
        kron(SZ, SZ, SY),
    ]
    prod = np.eye(8, dtype=complex)
    for g in G6:
        prod = prod @ g
    G7 = gam7_sign * 1j * prod

    g0 = kron(SZ, I2)
    G4 = [g0] + [kron(1j * SY, SIG[k]) for k in range(3)]
    g5 = 1j * G4[0] @ G4[1] @ G4[2] @ G4[3]

    E9 = [kron(SIG[i], G7) for i in range(3)] + [kron(I2, G6[a]) for a in range(6)]
    G13 = [kron(G4[mu], np.eye(16, dtype=complex)) for mu in range(4)]
    G13 += [kron(1j * g5, E9[m]) for m in range(9)]

    return SimpleNamespace(
        sign=gam7_sign,
        G6=G6,
        G7=G7,
        G4=G4,
        g5=g5,
        E9=E9,
        G13=G13,
        g5_13=kron(g5, np.eye(16, dtype=complex)),
        g7_13=kron(np.eye(4, dtype=complex), kron(I2, G7)),
    )


R = build_rep(+1)  # C125's module
RFLIP = build_rep(-1)  # the other inequivalent module


def omega13(rep) -> np.ndarray:
    om = np.eye(64, dtype=complex)
    for M in range(13):
        om = om @ rep.G13[M]
    return om


def section_A():
    print("A. Clifford algebra Cl(1,12), built from scratch")
    DATA["ast_audit_check_call_sites"] = _ast_self_audit()

    ok = all(
        close(R.G6[a] @ R.G6[b] + R.G6[b] @ R.G6[a], 2 * (a == b) * np.eye(8))
        for a in range(6)
        for b in range(6)
    )
    check("A1_cl6_anticommutators", ok, "36 pairs, {Gamma_a,Gamma_b} = 2 delta_ab")
    check("A2_gamma7_involution", close(R.G7 @ R.G7, np.eye(8)), "Gamma_7^2 = 1")
    check(
        "A3_gamma7_anticommutes_with_all_cl6",
        all(is_zero(R.G7 @ g + g @ R.G7) for g in R.G6),
        "Gamma_7 is the Z2 GRADING of Cl(6) -- exists because dim S6 = 6 is EVEN",
    )
    check(
        "A4_gamma7_is_NOT_scalar",
        not (close(R.G7, np.eye(8)) or close(R.G7, -np.eye(8))),
        "an even-dimensional Clifford factor has a non-central volume element",
    )

    ok9 = all(
        close(R.E9[m] @ R.E9[n] + R.E9[n] @ R.E9[m], 2 * (m == n) * np.eye(16))
        for m in range(9)
        for n in range(9)
    )
    check("A5_cl9_anticommutators", ok9, "81 pairs")

    bad, worst = 0, 0.0
    for M in range(13):
        for N in range(13):
            r = (
                R.G13[M] @ R.G13[N]
                + R.G13[N] @ R.G13[M]
                - 2 * ETA13[M, N] * np.eye(64, dtype=complex)
            )
            worst = max(worst, maxabs(r))
            bad += 0 if is_zero(r) else 1
    DATA["A_cl13_worst_anticommutator_residual"] = worst
    check(
        "A6_cl13_all_169_anticommutators",
        bad == 0,
        f"{bad} failures, worst residual {worst:.3e}, eta = diag(+,-,...,-)",
    )

    om = omega13(R)
    DATA["A_omega13_scalar_value"] = complex(om[0, 0])
    check(
        "A7_omega13_scalar_plus_one",
        close(om, np.eye(64)),
        f"omega_13 = {om[0, 0]:.4f} * 1 -- reproduces C125 E3. A first draft of this "
        f"file used gam7_sign = -1 and this check CAUGHT it (it returned -1).",
    )
    check(
        "A8_omega13_flips_in_the_other_module",
        close(omega13(RFLIP), -np.eye(64)),
        "gam7_sign = -1 gives omega_13 = -1, i.e. the OTHER inequivalent Cl(1,12) "
        "module (C125 section 1b). Both are carried through section H.",
    )

    Om3 = R.G13[4] @ R.G13[5] @ R.G13[6]
    check(
        "A9_Omega3_equals_g5_x_1_x_Gamma7",
        close(Om3, kron(R.g5, kron(I2, R.G7))),
        "C134 section 5a item 1 reproduced independently: Omega_3 has NO S3 content",
    )

    Om6 = np.eye(64, dtype=complex)
    for M in IDX_S6:
        Om6 = Om6 @ R.G13[M]
    prod = Om3 @ Om6
    c = complex(np.trace(prod @ R.g5_13) / 64.0)
    DATA["A_Omega3_Omega6_over_gamma5"] = c
    check(
        "A10_Omega3_Omega6_equals_i_gamma5",
        close(prod, c * R.g5_13) and abs(c - 1j) < TOL,
        f"measured {c:.4f}, C125 D4 = 0+1i. C125's OWN DOWNGRADE IS CARRIED FORWARD: "
        f"this is forced in every irrep of Cl(1,12) and is NOT a discovery about the split.",
    )

    om3 = Z3[0] @ Z3[1] @ Z3[2]
    DATA["A_omega3_intrinsic"] = complex(om3[0, 0])
    check(
        "A11_omega3_intrinsic_is_scalar_plus_one",
        close(om3, I2),
        "C125 section 4: an ODD-dimensional Clifford factor has a CENTRAL, SCALAR "
        "volume element -- it cannot be a grading. General reason, not convention.",
    )


# --------------------------------------------------------------------------
# B. The Clifford-parity theorem.
# --------------------------------------------------------------------------
def parity_facts(rep) -> dict:
    """The two load-bearing (anti)commutation facts, computed for a given rep."""
    even_ok, odd_ok, worst = True, True, 0.0
    for i in IDX_S3:
        for a in IDX_S6:
            odd_ok &= is_zero(rep.G13[i] @ rep.G13[a] + rep.G13[a] @ rep.G13[i])
            for j in IDX_S3:
                r = rep.G13[i] @ rep.G13[j] @ rep.G13[a] - rep.G13[a] @ rep.G13[i] @ rep.G13[j]
                worst = max(worst, maxabs(r))
                even_ok &= is_zero(r)
    s6_vs_even_s3 = all(
        is_zero(rep.G13[a] @ (rep.G13[i] @ rep.G13[j]) - (rep.G13[i] @ rep.G13[j]) @ rep.G13[a])
        for a in IDX_S6
        for i in IDX_S3
        for j in IDX_S3
    )
    return {
        "even_commutes": even_ok,
        "odd_anticommutes": odd_ok,
        "s6_blind_to_even_s3": s6_vs_even_s3,
        "worst": worst,
    }


def section_B():
    print("B. Clifford-parity theorem (even part factorises, odd part does not)")
    f = parity_facts(R)
    DATA["B_worst_even_commutator"] = f["worst"]

    check(
        "B1_even_S3_elements_commute_with_S6_vectors",
        f["even_commutes"],
        f"[Gamma^i Gamma^j, Gamma^a] = 0 on all 3*3*6 = 54 triples, worst {f['worst']:.2e}. "
        "REPRESENTATION-INDEPENDENT: follows from {Gamma^i, Gamma^a} = 0 alone.",
    )
    check(
        "B2_odd_S3_elements_ANTIcommute_with_S6_vectors",
        f["odd_anticommutes"],
        "{Gamma^i, Gamma^a} = 0, so an odd S3 element cannot commute with Cl(6) and "
        "therefore cannot act as (S3 operator) (x) 1 on the module.",
    )

    ok = all(
        close(
            R.G13[4 + i] @ R.G13[4 + j],
            kron(np.eye(4), kron(Z3[i] @ Z3[j], np.eye(8))),
        )
        for i in range(3)
        for j in range(3)
    )
    check(
        "B3_S3_two_forms_are_1_x_M2_x_1",
        ok,
        "Gamma^{3+i}Gamma^{3+j} = 1_4 (x) Z_i Z_j (x) 1_8. BOTH the S3 spin connection "
        "AND the S3 torsion term live here, so BOTH factorise exactly.",
    )
    ok = all(
        close(R.G13[7 + a] @ R.G13[7 + b], kron(np.eye(4), kron(I2, -R.G6[a] @ R.G6[b])))
        for a in range(6)
        for b in range(6)
    )
    check("B4_S6_two_forms_are_1_x_1_x_M8", ok, "same statement for the S6 factor")

    check(
        "B5_S3_vector_carries_gamma5_AND_Gamma7",
        all(close(R.G13[4 + i], kron(1j * R.g5, kron(SIG[i], R.G7))) for i in range(3)),
        "Gamma^{3+i} = (i gamma_5) (x) sigma_i (x) Gamma_7 -- the ONLY cross-factor "
        "operators appearing are the two GRADINGS, each Z2-valued.",
    )
    check(
        "B6_S6_vector_carries_identity_on_the_S3_slot",
        all(close(R.G13[7 + a], kron(1j * R.g5, kron(I2, R.G6[a]))) for a in range(6)),
        "Gamma^{6+a} = (i gamma_5) (x) 1_2 (x) Gamma_a -- NO S3 operator appears. "
        "One-directional, forced by dim S3 = 3 ODD (omega_3 central, check A11).",
    )
    check(
        "B7_S6_vectors_commute_with_the_whole_even_S3_algebra",
        f["s6_blind_to_even_s3"],
        "so the S6 equation cannot see any S3 datum beyond a scalar",
    )
    check(
        "B8_the_two_carriers_are_involutions",
        close(R.g5_13 @ R.g5_13, np.eye(64)) and close(R.g7_13 @ R.g7_13, np.eye(64)),
        "gamma_5^2 = Gamma_7^2 = 1 -- each carrier transmits exactly ONE BIT",
    )
    check(
        "B9_the_two_carriers_commute",
        is_zero(R.g5_13 @ R.g7_13 - R.g7_13 @ R.g5_13),
        "they generate (Z2)^2, a group of order 4. A Z3 channel label cannot be "
        "transmitted through scalars valued in {+1,-1}.",
    )


# --------------------------------------------------------------------------
# C. S3 geometry: nabla^t on invariant spinors, from the structure constants.
# --------------------------------------------------------------------------
def su2_structure_constants_verified() -> bool:
    """E_i = -(i/2) sigma_i  =>  [E_i,E_j] = eps_ijk E_k. Verified, not asserted."""
    E = [-0.5j * SIG[i] for i in range(3)]
    return all(
        close(E[i] @ E[j] - E[j] @ E[i], sum(EPS[i, j, k] * E[k] for k in range(3)))
        for i in range(3)
        for j in range(3)
    )


def nabla_t_ops(t, rho, sign_frame, c_struct=2.0, torsion_norm=2.0):
    """
    O_i with nabla^t_{X_i} eta = O_i eta for a frame-constant spinor:

      omega_{i;jk} = sign_frame * (c_struct/2)/rho * eps_ijk     (Levi-Civita)
      T_ijk        = torsion_norm*(2t-1)/rho * eps_ijk           (volume tensor)
      nabla^t      = d + (1/4) omega_{i;jk} Z_j Z_k + (1/8) T_ijk Z_j Z_k

    sign_frame = +1 left-invariant frame, -1 right-invariant frame.
    c_struct / torsion_norm are exposed ONLY so section F can vary them.
    """
    ops = []
    for i in range(3):
        acc = np.zeros((2, 2), dtype=complex)
        for j in range(3):
            for k in range(3):
                w = sign_frame * (c_struct / 2.0) / rho * EPS[i, j, k]
                T = torsion_norm * (2 * t - 1) / rho * EPS[i, j, k]
                acc += (0.25 * w + 0.125 * T) * (Z3[j] @ Z3[k])
        ops.append(acc)
    return ops


def mu_of(t, rho, sign_frame, c_struct=2.0, torsion_norm=2.0) -> float:
    """The scalar mu in nabla^t_X eta = mu X . eta (extracted, not assumed)."""
    o = nabla_t_ops(t, rho, sign_frame, c_struct, torsion_norm)[0]
    return float(np.real(np.trace(o @ np.linalg.inv(Z3[0])) / 2.0))


def section_C():
    print("C. S3 geometry -- nabla^t on invariant spinors")
    check(
        "C1_su2_structure_constants_verified",
        su2_structure_constants_verified(),
        "[E_i,E_j] = eps_ijk E_k from explicit 2x2 matrices",
    )
    # WHY C2 IS GONE: it read
    #     check(..., abs(1.5*(2/rho)**2 - 6/rho**2) < TOL, ...)
    # which is the identity 6 = 6 for every rho -- no curvature computed, c = 2/rho
    # hard-coded on both sides, and the formula Scal = (3/2)c^2 merely asserted in the
    # detail string. BOTH FL Step 8a skeptic passes caught it independently. It is
    # DELETED rather than repaired, because a check that cannot fail is not a check.
    # Note the AST self-audit does NOT catch this shape: `abs(x) < TOL` is a Compare
    # node, not an ast.Constant. That limitation is now stated in decision.md rather
    # than left implicit.

    ok_L, ok_R = True, True
    for t in (0.0, 0.25, 0.5, 1.0, 1.7):
        for rho in (1.0, 1.6):
            oL, oR = nabla_t_ops(t, rho, +1), nabla_t_ops(t, rho, -1)
            for i in range(3):
                ok_L &= close(oL[i], -(t / rho) * Z3[i])
                ok_R &= close(oR[i], +((1 - t) / rho) * Z3[i])
    check(
        "C3_left_invariant_law",
        ok_L,
        "nabla^t_X eta_L = -(t/rho3) X . eta_L, 10 (t,rho) points x 3 directions",
    )
    check("C4_right_invariant_law", ok_R, "nabla^t_Y eta_R = +((1-t)/rho3) Y . eta_R")

    check(
        "C5_t0_left_invariant_spinor_is_parallel",
        all(is_zero(o) for o in nabla_t_ops(0.0, 1.0, +1)),
        "reproduces round72 H1b at t = 0 (left-invariant, (-)-connection)",
    )
    check(
        "C6_t1_right_invariant_spinor_is_parallel",
        all(is_zero(o) for o in nabla_t_ops(1.0, 1.0, -1)),
        "reproduces round72 H1b at t = 1 (right-invariant, (+)-connection)",
    )
    check(
        "C7_LC_killing_constants_are_minus_half_and_plus_half",
        close(nabla_t_ops(0.5, 1.0, +1)[0], -0.5 * Z3[0])
        and close(nabla_t_ops(0.5, 1.0, -1)[0], +0.5 * Z3[0]),
        "at t = 1/2 the invariant spinors are Killing with constants -1/2 and +1/2 -- "
        "AHL2023 section 6 case (II): 'a pair of invariant Killing spinors for the "
        "constant 1/2, BUT NO INVARIANT GENERALIZED KILLING SPINORS' [CITED, pdftotext "
        "this round, FULL sentence -- a previous draft truncated it at the comma. The "
        "dropped clause CLOSES Relaxation-Map variant V2: a non-scalar A_3 against "
        "nabla^t is exactly a non-scalar symmetric A against nabla^LC, which AHL2023 "
        "states does not exist for invariant spinors on the round S3 = SU(2).]",
    )
    DATA["C_killing_constant_law"] = {"left": "-t/rho3", "right": "+(1-t)/rho3"}

    # C8/C9 -- the strongest available corroboration that section C is not
    # round114 again: feed the SAME operators into the Dirac operator
    # D^t eta = sum_i Z_i . nabla^t_{X_i} eta and check the n=0 eigenvalues
    # against TWO independently certified project values.
    ok8, ok9, vals = True, True, {}
    for t in (0.0, 0.25, 0.5, 1.0, 1.3):
        for sf, pred, key in ((+1, 3 * t, "left"), (-1, 3 * t - 3, "right")):
            ops = nabla_t_ops(t, 1.0, sf)
            D = sum(Z3[i] @ ops[i] for i in range(3))
            good = close(D, pred * I2)
            vals[f"t={t}|{key}"] = float(np.real(D[0, 0]))
            if sf > 0:
                ok8 &= good
            else:
                ok9 &= good
    DATA["C_Dirac_n0_eigenvalues"] = vals
    check(
        "C8_Dirac_n0_left_branch_equals_3t",
        ok8,
        "D^t(n=0) = 3t * I_2 on the left-invariant spinors -- reproduces C64's own "
        "certified value at 5 t-points",
    )
    check(
        "C9_Dirac_n0_right_branch_equals_3t_minus_3",
        ok9,
        "D^t(n=0) = (3t-3) * I_2 on the right-invariant spinors -- reproduces round67's "
        "other branch, quoted verbatim by C107: 'the two n=0 branches are 3t and 3t-3; "
        "zero at t=0 and t=1 respectively, never simultaneously'. At t=1/2 these give "
        "+-3/2, the classical Friedrich-1980 constant -- but here it falls out of the "
        "FULL first-order operator WITH its whole t-dependence, not from round114's "
        "trace collapse.",
    )


# --------------------------------------------------------------------------
# D. The decomposed joint system, as a 64x64 operator equation.
# --------------------------------------------------------------------------
def weyl4(rep, chi4: int) -> np.ndarray:
    P = 0.5 * (np.eye(4, dtype=complex) + chi4 * rep.g5)
    for col in range(4):
        v = P[:, col]
        if np.linalg.norm(v) > 1e-8:
            return v / np.linalg.norm(v)
    raise RuntimeError("no Weyl vector")


def chiral6(rep, chi6: int, which: int = 0) -> np.ndarray:
    P = 0.5 * (np.eye(8, dtype=complex) + chi6 * rep.G7)
    cols = [P[:, c] for c in range(8) if np.linalg.norm(P[:, c]) > 1e-8]
    v = cols[which % len(cols)]
    return v / np.linalg.norm(v)


def s3_spinor(kind: int = 0) -> np.ndarray:
    v = np.zeros(2, dtype=complex)
    v[kind % 2] = 1.0
    return v


def s3_residual(rep, t, rho, sign_frame, lam, chi4, chi6, i, s3kind=0):
    """Residual of ( nabla^t_{X_i} - lam Gamma^{3+i} ) eps = 0 as a 64-vector."""
    ops = nabla_t_ops(t, rho, sign_frame)
    lhs = kron(np.eye(4), kron(ops[i], np.eye(8)))
    eps = np.kron(weyl4(rep, chi4), np.kron(s3_spinor(s3kind), chiral6(rep, chi6)))
    return (lhs - lam * rep.G13[4 + i]) @ eps


def pairing_law_holds(rep) -> bool:
    """lambda = mu * chi4 * chi6 solves the S3 equation, and a wrong lambda does not."""
    ok = True
    for t in (0.0, 0.3, 1.0):
        for chi4 in (+1, -1):
            for chi6 in (+1, -1):
                for sf in (+1, -1):
                    mu = mu_of(t, 1.0, sf)
                    lam = mu * chi4 * chi6
                    ok &= all(
                        is_zero(s3_residual(rep, t, 1.0, sf, lam, chi4, chi6, i)) for i in range(3)
                    )
                    ok &= any(
                        not is_zero(s3_residual(rep, t, 1.0, sf, lam + 0.37, chi4, chi6, i))
                        for i in range(3)
                    )
    return ok


def section_D():
    print("D. The decomposed joint system")
    ok = all(
        close(R.G13[4 + j] @ R.G13[4 + k], kron(np.eye(4), kron(Z3[j] @ Z3[k], np.eye(8))))
        for j in range(3)
        for k in range(3)
    )
    check(
        "D1_13D_S3_spin_connection_reduces_to_the_intrinsic_one",
        ok,
        "the block used below is the restriction of the genuine 13D operator, not an ansatz",
    )

    check(
        "D2_S3_equation_fixes_lambda_equals_mu_chi4_chi6",
        pairing_law_holds(R),
        "24 configurations: lambda = mu*chi4*chi6 solves it, lambda + 0.37 does not. "
        "THIS is the only cross-factor coupling the constraint produces.",
    )
    DATA["D_pairing_law"] = "lambda = mu(t,rho3,frame) * chi4 * chi6"

    ok = True
    for a in range(6):
        for kind in (0, 1):
            eps = np.kron(weyl4(R, +1), np.kron(s3_spinor(kind), chiral6(R, +1)))
            pred = 1j * np.kron(weyl4(R, +1), np.kron(s3_spinor(kind), R.G6[a] @ chiral6(R, +1)))
            ok &= close(R.G13[7 + a] @ eps, pred)
    check(
        "D3_S6_equation_carries_no_S3_datum",
        ok,
        "the S6 equation's only cross-factor input is chi4; the S3 slot is exactly 1_2",
    )

    comm = R.G13[0] @ R.G13[1] - R.G13[1] @ R.G13[0]
    eps = np.kron(weyl4(R, +1), np.kron(s3_spinor(0), chiral6(R, +1)))
    check(
        "D4_flat_M4_integrability_forces_lambda_zero",
        not is_zero(comm @ eps),
        "[Gamma_0,Gamma_1] eps != 0, so d_mu eps = lam Gamma_mu eps has no solution on "
        "flat M4 unless lam = 0 (single-constant ansatz A = lam * 1_13)",
    )


# --------------------------------------------------------------------------
# E. The 3 x 2 table (channel x t-sector), filled explicitly.
# --------------------------------------------------------------------------
CHANNELS = ["8_v", "8_s", "8_c"]


def channel_inputs(channel: str, fake: bool = False) -> dict:
    """
    Every input the constraint can see from the S6 side.

    E-L3B (experiments/20260625-l3b-bundle-obstruction/decision.md, Theorem +
    Corollary, read this round): E_v ~ E_s ~ E_c as G2-equivariant bundles WITH
    IDENTICAL canonical connections; the twisted Dirac operators "are THE SAME
    OPERATOR". L5/G74B: sign(ind) = +1 for all three -> the same S6 chirality.

    So the honest encoding is: identical inputs for all three channels.
    `fake` exists only for section F's positive control on the detector.
    """
    base = {
        "chi6": +1,
        "connection_id": "canonical_G2_equivariant",
        "bundle_iso_class": "3 + 3bar + 1 + 1 as SU(3)-module",
        "S6_killing_const": 0.0,
    }
    if fake:
        base["chi6"] = {"8_v": +1, "8_s": -1, "8_c": +1}[channel]
        base["connection_id"] = f"canonical_{channel}"
    return base


def alpha_from_residual(t: float, sf: int, chi4: int, chi6: int) -> float:
    """
    SOLVE the 64-dim S3 equation for the Killing constant, rather than substituting
    the closed form. Both sides are proportional to (1 (x) Z_i (x) 1) eps, so the
    equation is affine in alpha and least squares recovers it exactly:

        alpha* = <Gamma eps, Op eps> / <Gamma eps, Gamma eps>

    WHY THIS EXISTS: the first draft hard-coded `lam = 0.0` in solve_cell, which
    ANNIHILATED chi6 (it entered only as `lam * chi6`). Both FL Step 8a skeptic
    passes independently found that this made check E1 unable to return False for
    ANY input, fake included -- so the round's headline was a dict compared with
    itself and F4 tested only the comparator. This routes the cell content through
    the actual solver so chi6 reaches it.
    """
    ops = nabla_t_ops(t, 1.0, sf)
    lhs = kron(np.eye(4), kron(ops[0], np.eye(8)))
    eps = np.kron(weyl4(R, chi4), np.kron(s3_spinor(0), chiral6(R, chi6)))
    a, b = lhs @ eps, R.G13[4] @ eps
    return float(np.real(np.vdot(b, a) / np.vdot(b, b)))


def solve_cell(channel: str, t: float, fake: bool = False, chi4: int = +1) -> dict:
    """
    Reading (ii) -- the STANDARD generalized-Killing form (AHL2023: A a symmetric
    endomorphism, not necessarily a multiple of the identity). alpha is free, so both
    invariant frames always solve; the cell's CONTENT is the alpha each one requires,
    and that is a genuine function of chi6.

    Reading (i) (a single lam = 0 forced by flat M4, check D4) is reported separately
    by E3 -- it is NOT used to fill the table, precisely because lam = 0 removes all
    cross-factor content by arithmetic (skeptic finding, accepted).
    """
    inp = channel_inputs(channel, fake)
    frames = []
    for sf, label in ((+1, "left-invariant (1,2)"), (-1, "right-invariant (2,1)")):
        alpha = alpha_from_residual(t, sf, chi4, inp["chi6"])
        frames.append(f"{label}: alpha = {alpha:+.6f}")
    return {
        "channel": channel,
        "t": t,
        "reading": "(ii) block-scalar A; alpha SOLVED from the 64-dim residual",
        "chi6": inp["chi6"],
        "S3_solution_space": frames,
        "S3_dim_C": 2 * len(frames),
        # WHY: self-caught overclaim. The first draft wrote "NK canonical spinor,
        # dim_C 1" here and multiplied it into a total. The S6 solution space was
        # NEVER COMPUTED in this round -- the script builds no S6 spin connection,
        # no NK torsion and no twist bundle E (same limitation C134 section 7
        # disclosed for itself). Worse, if eps is a section of S(M13) (x) E then
        # E|_SU(3) = 3+3bar+1+1 has TWO trivial summands, so "dim 1" is not even a
        # safe guess. The kill does not need it: whatever the S6 solution space is,
        # it is the SAME for all three channels because the INPUTS are (E-L3B).
        "S6_solution": "[UNKNOWN] -- NOT COMPUTED this round; identical across the "
        "three channels because the inputs are (E-L3B), which is all the kill needs",
        "M4_solution": "constant spinor, dim_C 4",
        "S6_connection_id": inp["connection_id"],
    }


def cells_agree(a: dict, b: dict) -> bool:
    return (
        a["S3_solution_space"] == b["S3_solution_space"]
        and a["S3_dim_C"] == b["S3_dim_C"]
        and a["chi6"] == b["chi6"]
        and a["S6_connection_id"] == b["S6_connection_id"]
    )


def channels_uniform(fake: bool = False) -> bool:
    for t in (0.0, 1.0):
        ref = solve_cell("8_v", t, fake)
        for ch in CHANNELS[1:]:
            if not cells_agree(solve_cell(ch, t, fake), ref):
                return False
    return True


def section_E():
    print("E. The 3 x 2 table -- (S6 channel) x (S3 t-sector)")
    DATA["E_table_3x2"] = {
        f"{ch}|t={t:.0f}": solve_cell(ch, t) for ch in CHANNELS for t in (0.0, 1.0)
    }

    check(
        "E1_solution_set_is_UNIFORM_across_the_three_channels",
        channels_uniform(),
        "KILL BRANCH (b) FIRES: no channel-selectivity, hence no pairing information. "
        "The cell content is now the alpha SOLVED from the 64-dim residual, which "
        "depends on chi6 -- so this check CAN return False (F4 shows it does). But see "
        "F7: it is still a RESTATEMENT of E-L3B, not independent evidence.",
    )

    c0, c1 = solve_cell("8_v", 0.0), solve_cell("8_v", 1.0)
    check(
        "E2_t_sectors_carry_different_alpha_neither_preferred",
        c0["S3_solution_space"] != c1["S3_solution_space"] and c0["S3_dim_C"] == c1["S3_dim_C"],
        "t=0 and t=1 require different alpha on the two invariant frames, with equal "
        "dimension -> NO sector SELECTION. The (1,2)/(2,1) rep LABELS are hard-coded "
        "strings cited to C38, NOT computed here (skeptic finding, accepted); only the "
        "frame/alpha content is computed.",
    )

    surv = sorted(
        {
            round(float(t), 6)
            for t in np.linspace(-0.5, 1.5, 41)
            if abs(mu_of(float(t), 1.0, +1)) < TOL or abs(mu_of(float(t), 1.0, -1)) < TOL
        }
    )
    DATA["E_surviving_t_on_grid"] = surv
    check(
        "E3_reading_i_single_constant_only_t_in_0_1_survives",
        surv == [0.0, 1.0],
        f"reading (i), A = lam*1_13 with lam = 0 forced by flat M4 (check D4): "
        f"surviving t = {surv}. NOT used to fill the table -- lam = 0 annihilates chi6, "
        "so reading (i) has zero cross-factor content by arithmetic (skeptic finding, "
        "accepted). And see F5: it restates round72 H1b.",
    )

    # Reading (ii): the STANDARD generalized-Killing form, A a symmetric endomorphism
    # that need not be a multiple of the identity (AHL2023's own definition allows
    # several distinct eigenvalues). Take A = diag(0_4, alpha*1_3, beta*1_6). Then
    # alpha is free, so the S3 equation is solvable at EVERY t by choosing
    # alpha = mu(t)*chi4*chi6 -- and the constraint has NO t-selection content at all.
    surv_ii = []
    for t in np.linspace(-0.5, 1.5, 41):
        alpha = mu_of(float(t), 1.0, +1) * (+1) * (+1)
        if all(is_zero(s3_residual(R, float(t), 1.0, +1, alpha, +1, +1, i)) for i in range(3)):
            surv_ii.append(round(float(t), 6))
    DATA["E_surviving_t_reading_ii_count"] = len(surv_ii)
    check(
        "E4_reading_ii_block_scalar_A_every_t_survives",
        len(surv_ii) == 41,
        f"{len(surv_ii)}/41 grid points admit a solution with a free alpha -> in the "
        "STANDARD generalized-Killing reading the constraint has ZERO t-selection "
        "content. Both readings agree on E1 (channel uniformity), which is the kill.",
    )

    # E5 -- WITHDRAWN AND REPLACED BY ITS OWN REFUTATION.
    #
    # A previous draft claimed a "second, independent kill route" that needed no
    # E-L3B: the only cross-factor carrier is chi6 in Z2, a Z2 carrier can 2-colour
    # three channels but never 3-colour them, therefore no asymmetric pairing.
    #
    # BOTH FL Step 8a skeptic passes refuted this, and the refutation is correct:
    # claim.md's predicate is "NOT every channel pairs equally with every sector".
    # A 2+1 SPLIT SATISFIES THAT. So a Z2 carrier is entirely sufficient to produce
    # the asymmetry claim.md asks for -- the cardinality argument never delivered the
    # conclusion. (E-L3B's own level table has exactly such a row: SO(7) separates
    # 8_v from {8_s, 8_c}.) The argument is withdrawn, not narrowed.
    #
    # The check below now DEMONSTRATES the refutation instead of asserting the
    # refuted claim: with a hypothetical 2+1 chi6 assignment the solver really does
    # return a channel-asymmetric table. So what kills P14 is NOT the bandwidth
    # count -- it is that chi6 is CONSTANT across the three channels (L5/G74B,
    # sign(ind) = +1), which is prior art, not this round's finding.
    two_plus_one = channels_uniform(fake=True)
    DATA["E5_two_plus_one_split_would_satisfy_the_predicate"] = not two_plus_one
    check(
        "E5_a_Z2_carrier_CAN_produce_the_asymmetry__bandwidth_argument_withdrawn",
        not two_plus_one,
        "with a 2+1 chi6 assignment the table IS channel-asymmetric, which satisfies "
        "claim.md's predicate. So 'a Z3 label cannot pass through a Z2 carrier' never "
        "entailed the kill -- WITHDRAWN. The operative fact is chi6's CONSTANCY "
        "(L5/G74B), not the bandwidth count.",
    )


# --------------------------------------------------------------------------
# F. ROUND114 TRAP BATTERY -- mandatory.
# --------------------------------------------------------------------------
def section_F():
    print("F. round114 tautology-trap battery")
    rng = np.random.default_rng(20260902)

    collapse_ok = True
    for _ in range(20):
        a = rng.normal(size=3)
        Dop = sum(a[i] * R.G13[4 + i] @ R.G13[4 + i] for i in range(3))
        collapse_ok &= close(Dop, -float(a.sum()) * np.eye(64))
    DATA["F1_round114_collapse_reproduced"] = collapse_ok
    check(
        "F1_round114_collapse_reproduced_explicitly",
        collapse_ok,
        "sum_i Gamma^i A(e_i) = -tr(A) * 1 for 20 random diagonal A -- the EXACT "
        "round114 failure mode. NO quantity of this shape is used as evidence "
        "anywhere in this round; sections D/E use the FULL first-order equation.",
    )

    base = {"t": 0.3, "rho": 1.0, "sf": +1, "chi4": +1, "chi6": +1, "c": 2.0, "tn": 2.0}

    def lam_for(**kw):
        p = dict(base)
        p.update(kw)
        return mu_of(p["t"], p["rho"], p["sf"], p["c"], p["tn"]) * p["chi4"] * p["chi6"]

    lam0 = lam_for()
    sens = {
        "t": lam_for(t=0.8) - lam0,
        "rho3": lam_for(rho=2.0) - lam0,
        "chi4": lam_for(chi4=-1) - lam0,
        "chi6": lam_for(chi6=-1) - lam0,
        "frame_L_vs_R": lam_for(sf=-1) - lam0,
        "structure_constant": lam_for(c=3.0) - lam0,
        "torsion_normalisation": lam_for(tn=5.0) - lam0,
    }
    DATA["F_lambda_baseline"] = float(lam0)
    DATA["F_lambda_sensitivity"] = {k: float(v) for k, v in sens.items()}
    check(
        "F2_output_depends_on_every_input_varied",
        all(abs(v) > 1e-8 for v in sens.values()),
        f"lambda moves under all 7 perturbations: {DATA['F_lambda_sensitivity']}. "
        "CORRECTED FRAMING (both skeptic passes, accepted): a previous draft said "
        "'round114's -tr(A) moved under NONE of its analogous inputs'. THAT IS FALSE -- "
        "round114 computed D^s = s/2 - 3/2, which moves under s and has a zero crossing "
        "at s=3 (round114 decision.md:23-26). Input-dependence was never round114's "
        "failure criterion; ONE-LINE DERIVABILITY FROM THE SOURCE was. F2 therefore "
        "shows only that lambda is a non-constant function of its own arguments. The "
        "real round114 test is F7.",
    )

    generic = True
    for _ in range(5):
        A = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
        Q, _ = np.linalg.qr(A)
        rep = build_rep(+1)
        rep.G6 = [Q @ g @ Q.conj().T for g in rep.G6]
        rep.G7 = Q @ rep.G7 @ Q.conj().T
        rep.E9 = [kron(SIG[i], rep.G7) for i in range(3)] + [kron(I2, rep.G6[a]) for a in range(6)]
        rep.G13 = [kron(rep.G4[mu], np.eye(16)) for mu in range(4)] + [
            kron(1j * rep.g5, rep.E9[m]) for m in range(9)
        ]
        f = parity_facts(rep)
        generic &= f["even_commutes"] and f["odd_anticommutes"] and f["s6_blind_to_even_s3"]
    check(
        "F3_parity_theorem_is_representation_generic",
        generic,
        "the section-B parity theorem survives 5 random Cl(6) basis changes. DECLARED "
        "LIMITATION, not a claim: it is a fact about dim 3 ODD / dim 6 EVEN, true for "
        "ANY M3 x M6, and carries NO information about THIS background.",
    )

    # F4 -- REAL positive control on the SOLVER, not just the comparator.
    # The first draft's version injected chi6 while lam was hard-coded to 0, so the
    # injection could not reach the solution set and F4 established only that two
    # different dicts are different. Both skeptic passes caught this. solve_cell now
    # solves for alpha from the 64-dim residual, so an injected chi6 propagates into
    # the reported alpha. Verified below by comparing the SOLVED alphas, not metadata.
    real_alphas = {ch: solve_cell(ch, 0.0)["S3_solution_space"] for ch in CHANNELS}
    fake_alphas = {ch: solve_cell(ch, 0.0, fake=True)["S3_solution_space"] for ch in CHANNELS}
    DATA["F4_real_alphas_distinct"] = len({str(v) for v in real_alphas.values()})
    DATA["F4_fake_alphas_distinct"] = len({str(v) for v in fake_alphas.values()})
    check(
        "F4_detector_positive_control_on_the_SOLVER",
        len({str(v) for v in real_alphas.values()}) == 1
        and len({str(v) for v in fake_alphas.values()}) == 2,
        f"real inputs -> {DATA['F4_real_alphas_distinct']} distinct SOLVED alpha set; "
        f"injected channel-dependent chi6 -> {DATA['F4_fake_alphas_distinct']}. The "
        "injection now reaches the solution set, so E1 is a check that CAN fail.",
    )

    check(
        "F5_t_selection_is_a_restatement_of_round72_H1b",
        all(is_zero(o) for o in nabla_t_ops(0.0, 1.0, +1))
        and all(is_zero(o) for o in nabla_t_ops(1.0, 1.0, -1)),
        "lambda = 0 turns the joint constraint into 'a nabla^t-parallel spinor exists', "
        "which round72 H1b already PROVED holds exactly at t = 0,1. The 13D apparatus "
        "adds NOTHING to that half. Flagged, not claimed as new.",
    )

    worst, ok = 0.0, True
    for _ in range(10):
        S = rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
        Si = np.linalg.inv(S)
        scale = max(1.0, np.linalg.norm(S) * np.linalg.norm(Si))
        Gp = [S @ g @ Si for g in R.G13]
        for i in IDX_S3:
            for a in IDX_S6:
                r = maxabs(Gp[i] @ Gp[a] + Gp[a] @ Gp[i]) / scale
                worst = max(worst, r)
                ok &= r < 1e-6
    DATA["F_worst_similarity_residual"] = worst
    check(
        "F6_anticommutation_survives_general_GL64_similarity",
        ok,
        f"10 GL(64,C) similarities, worst scaled residual {worst:.2e}. SCOPE (skeptic "
        "finding, accepted): F3 and F6 re-check only parity_facts (B1/B2/B7) and "
        "anticommutation -- they do NOT re-check B5/B6, on which the bandwidth count "
        "rested. Since that count is withdrawn (E5), nothing now depends on the gap.",
    )

    # F7 -- round114's ACTUAL criterion, applied to THIS round's own headline.
    # round114 decision.md:108-112, verbatim: "before claiming 'independent
    # confirmation,' check whether the computation's OWN output is derivable in one
    # line directly from the source's stated theorem, with no intermediate step adding
    # information not already in that one citation -- if so, it is a restatement."
    #
    # E-L3B's Corollary: E_v ~ E_s ~ E_c with IDENTICAL canonical connections, the
    # twisted Dirac operators "are THE SAME OPERATOR". L5/G74B: sign(ind) = +1 for all
    # three. One line: identical inputs => identical solution sets.
    #
    # The test is implemented as: does the verdict survive DELETING everything this
    # round computed, keeping only the cited inputs? If yes, the round added encoding,
    # not evidence. Both skeptic passes found this and the first draft failed to apply
    # its own F5 audit to its own conclusion.
    inputs_identical = len({str(channel_inputs(ch)) for ch in CHANNELS}) == 1
    DATA["F7_verdict_is_one_line_derivable_from_EL3B"] = inputs_identical
    check(
        "F7_headline_is_a_RESTATEMENT_of_EL3B_not_independent_evidence",
        inputs_identical,
        "the three S6 input dicts are literally equal, so 'the columns are identical' "
        "follows in one line from E-L3B + L5 with NOTHING this round computed. By "
        "round114's own stated criterion the headline is a RESTATEMENT. Prior art "
        "saying the same: null_results G44-B1 ('S6 blind to tau'), GAP-4 ('no S3 "
        "quantum number to mix, structurally not just empirically'), Round81 "
        "('omega=Z1Z2Z3=I2 is central'), pearl rows 22 and 36. The round's positive "
        "content is section G, not this.",
    )


# --------------------------------------------------------------------------
# G. C134 section 8's non-transfer claim, verified rather than assumed.
# --------------------------------------------------------------------------
def section_G():
    print("G. C134 route-2 non-transfer, verified rather than assumed")
    Om3 = R.G13[4] @ R.G13[5] @ R.G13[6]
    PL = 0.5 * (np.eye(64) - R.g5_13)
    PR = 0.5 * (np.eye(64) + R.g5_13)
    G0 = R.G13[0]

    check(
        "G1_C134_bilinear_vanishes_on_chiral_content",
        is_zero(PL @ G0 @ Om3 @ PL) and is_zero(PR @ G0 @ Om3 @ PR),
        "P_L Gamma^0 Omega_3 P_L = P_R Gamma^0 Omega_3 P_R = 0 -- C134 route 2 reproduced",
    )
    check(
        "G2_linear_operator_does_NOT_vanish_on_chiral_content",
        (not is_zero(PL @ Om3 @ PL)) and (not is_zero(PR @ Om3 @ PR)),
        "P_L Omega_3 P_L != 0: Omega_3 COMMUTES with gamma_5, so it preserves 4D "
        "chirality. G1's vanishing comes entirely from the Gamma^0 insertion of the "
        "Dirac adjoint, which a linear-in-spinor constraint does not have.",
    )
    check(
        "G3_Omega3_commutes_with_gamma5",
        is_zero(Om3 @ R.g5_13 - R.g5_13 @ Om3),
        "the structural reason for G2",
    )
    check(
        "G4_Gamma0_anticommutes_with_gamma5",
        is_zero(G0 @ R.g5_13 + R.g5_13 @ G0),
        "the structural reason for G1",
    )
    check(
        "G5_S3_torsion_two_forms_preserve_4D_chirality",
        all(
            is_zero(R.G13[4 + i] @ R.G13[4 + j] @ R.g5_13 - R.g5_13 @ R.G13[4 + i] @ R.G13[4 + j])
            for i in range(3)
            for j in range(3)
        ),
        "so C134's chirality-flip kill cannot fire on this round's construction. "
        "C134 section 8's assertion VERIFIED, not assumed.",
    )


# --------------------------------------------------------------------------
# H. Both inequivalent Cl(1,12) modules give the same conclusions.
# --------------------------------------------------------------------------
def section_H():
    print("H. Module-independence (omega_13 = +1 and omega_13 = -1)")
    f = parity_facts(RFLIP)
    check(
        "H1_parity_theorem_holds_in_the_other_module",
        f["even_commutes"] and f["odd_anticommutes"] and f["s6_blind_to_even_s3"],
        "sections B1/B2/B7 unchanged for gam7_sign = -1",
    )
    check(
        "H2_pairing_law_holds_in_the_other_module",
        pairing_law_holds(RFLIP),
        "section D2 unchanged: lambda = mu * chi4 * chi6 in both modules",
    )
    Om3f = RFLIP.G13[4] @ RFLIP.G13[5] @ RFLIP.G13[6]
    PLf = 0.5 * (np.eye(64) - RFLIP.g5_13)
    check(
        "H3_route2_non_transfer_holds_in_the_other_module",
        is_zero(PLf @ RFLIP.G13[0] @ Om3f @ PLf) and (not is_zero(PLf @ Om3f @ PLf)),
        "section G unchanged: the bilinear dies, the linear operator does not",
    )
    # H4 DELETED. It read `check("H4_channel_uniformity_is_module_independent",
    # channels_uniform(), ...)` -- but channels_uniform() takes no representation
    # argument and never touches RFLIP, so it was a byte-for-byte re-run of E1 in
    # NEITHER module. Both skeptic passes caught it independently. The verdict
    # string's "both modules agree" token now covers H1/H2/H3 only, which do use
    # RFLIP. Deleted rather than renamed: the claim it made was not testable by the
    # call it made.


# --------------------------------------------------------------------------
# I. The ALGEBRAIC half of the type-II system, which sections D/E did NOT impose.
#
# Agricola 2002 section 4.1 [CITED, pdftotext this round] gives the common
# sector of type II string theory as FOUR equations; with constant dilaton they
# reduce to  Ric^nabla = 0,  delta(T) = 0,  nabla psi = 0,  T . psi = 0.
# Sections D/E impose only the THIRD (a parallel/generalized-Killing spinor).
# The fourth is ALGEBRAIC and is computed here, because leaving it unexamined
# would be exactly the kind of unstated scope gap this project keeps catching.
#
# Agricola's Theorem 4.1 (attributed to Alexandrov, from FI01): on a COMPACT
# manifold, all four together force T = 0 and nabla = Levi-Civita. M13 is NOT
# compact and the S6 factor's Ric^nabla is not zero, so the theorem's hypotheses
# are NOT met here -- it is recorded as context, not applied.
# --------------------------------------------------------------------------
def section_I():
    print("I. The algebraic (dilatino) condition T . eps = 0, not imposed above")
    Om3 = R.G13[4] @ R.G13[5] @ R.G13[6]

    ok, vals = True, {}
    for chi4 in (+1, -1):
        for chi6 in (+1, -1):
            eps = np.kron(weyl4(R, chi4), np.kron(s3_spinor(0), chiral6(R, chi6)))
            out = Om3 @ eps
            ok &= close(out, chi4 * chi6 * eps)
            vals[f"chi4={chi4:+d},chi6={chi6:+d}"] = chi4 * chi6
    DATA["I_Omega3_eigenvalue_on_factorised_eps"] = vals
    check(
        "I1_Omega3_acts_as_chi4_chi6_on_the_factorised_ansatz",
        ok,
        "Omega_3 eps = chi4*chi6*eps exactly, all 4 chirality combinations",
    )

    # T_3 as a Clifford element is T_123 * Omega_3 with T_123 = 2(2t-1)/rho3.
    zero_at = [
        round(float(t), 6)
        for t in np.linspace(-0.5, 1.5, 41)
        if abs(2 * (2 * float(t) - 1) / 1.0) < TOL
    ]
    DATA["I_dilatino_zero_at"] = zero_at
    check(
        "I2_dilatino_condition_on_the_S3_leg_forces_t_one_half",
        zero_at == [0.5],
        "T_3 . eps = (2(2t-1)/rho3) * chi4*chi6 * eps, which vanishes ONLY at t = 1/2 "
        "(41-point grid). So the ALGEBRAIC half of the type-II system, if imposed with "
        "the S6 torsion switched off, reproduces C134's kill from a completely different "
        "direction. NOT imposed in sections D/E; recorded so the scope gap is explicit.",
    )
    check(
        "I3_dilatino_condition_is_also_channel_blind",
        len({v for v in vals.values()}) == 2 and all(abs(v) == 1 for v in vals.values()),
        "its only cross-factor content is the SAME chi4*chi6 pair of Z2 carriers, so it "
        "adds no bandwidth and cannot revive P14. With the S6 torsion restored the "
        "condition becomes a relation between t and S6 data -- a genuine cross-factor "
        "t-selection candidate (Relaxation Map), still channel-blind. The NK torsion "
        "coefficient c_6 is [UNKNOWN] here and is deliberately NOT invented.",
    )


# --------------------------------------------------------------------------
# J. TWO COUNTEREXAMPLES that repair section 2's theorem.
#
# Both FL Step 8a skeptic passes found that the theorem as first stated ("the
# cross-factor operators an odd S3 term can carry are exactly gamma_5 and Gamma_7")
# is FALSE under its own stated hypotheses, and that the pearl built on it would be
# a wrong forward pre-filter. Both counterexamples are reproduced here rather than
# conceded in prose, because a refuted claim that is only described tends to come
# back.
# --------------------------------------------------------------------------
def section_J():
    print("J. Counterexamples repairing the section-2 theorem")

    # J1 -- OFF-BLOCK A. AHL2023's definition (quoted in section 1) requires only
    # that A be SYMMETRIC. Nothing in it makes A block-diagonal across TS3 (+) TS6.
    # With A_{ia} != 0 the S3 equation acquires sum_a A_{ia} Gamma^{6+a}, a full
    # Cl(6) VECTOR acting on eta6 -- six operators, not one grading bit.
    v = sum(R.G13[7 + a] for a in range(6))  # a generic off-block contribution
    in_grading_span = is_zero(v - np.trace(v @ R.g7_13) / 64.0 * R.g7_13) and is_zero(
        v - np.trace(v) / 64.0 * np.eye(64)
    )
    check(
        "J1_off_block_A_carries_a_full_Cl6_vector_not_a_grading_bit",
        not in_grading_span,
        "sum_a Gamma^{6+a} is NOT in span{1, Gamma_7}: an off-block symmetric A puts a "
        "Cl(6) vector into the S3 equation, so the '(Z2)^2 bandwidth' claim is FALSE "
        "without an extra hypothesis. REPAIR: the theorem now requires A to have no "
        "off-block component. That IS forced by G2-invariance -- SU(3) acts on "
        "T_p S6 = R^6 = 3 + 3bar with NO trivial summand, so an SU(3)-invariant vector "
        "is 0 -- but it must be ARGUED, and a non-G2-invariant A is exactly route (b).",
    )

    # J2 -- CHANNEL-DEPENDENT S6 DATA. The sharper counterexample: the pairing need
    # not pass through a Clifford carrier at all. In reading (i) a SINGLE shared
    # lambda couples the factor equations, so channel-dependent S6 data beta_alpha
    # gives lambda = beta_alpha AND lambda = mu(t) chi4 chi6, hence mu(t) = beta_alpha
    # chi4 chi6, hence t = t(alpha): a channel-selective t-sector with NO Z2 bottleneck.
    # C132 section 7 finding 1 establishes that G2-equivariance permits exactly this.
    betas = {"8_v": -0.10, "8_s": -0.35, "8_c": -0.80}
    t_of_channel = {}
    for ch, beta in betas.items():
        hits = [
            round(float(t), 6)
            for t in np.linspace(-0.5, 1.5, 2001)
            if abs(mu_of(float(t), 1.0, +1) * (+1) * (+1) - beta) < 1e-6
        ]
        t_of_channel[ch] = hits[0] if hits else None
    DATA["J2_t_of_channel_under_hypothetical_beta"] = t_of_channel
    check(
        "J2_channel_dependent_S6_data_pairs_t_to_the_channel_with_no_Z2_bottleneck",
        len({v for v in t_of_channel.values() if v is not None}) == 3,
        f"hypothetical beta_alpha -> three DISTINCT t values {t_of_channel}: a genuine "
        "3-way channel-selective pairing, obtained through the shared scalar lambda and "
        "NOT through any Z2 carrier. So the bandwidth bound never bounded the pairing. "
        "The binding constraint is E-L3B (all beta_alpha equal), i.e. prior art -- which "
        "is the honest statement of what kills P14.",
    )


# --------------------------------------------------------------------------
def main():
    print("=" * 74)
    print("C136 -- joint generalized-Killing-spinor constraint on M4 x S3 x S6")
    print("=" * 74)
    for s in (
        section_A,
        section_B,
        section_C,
        section_D,
        section_E,
        section_F,
        section_G,
        section_H,
        section_I,
        section_J,
    ):
        s()

    n_ok = sum(1 for c in CHECKS if c["ok"])
    n = len(CHECKS)
    print("-" * 74)
    print(
        f"CHECKS: {n_ok}/{n} passed  (AST self-audit: "
        f"{DATA['ast_audit_check_call_sites']} check() call sites, none constant)"
    )
    print(f"DATA values recorded separately, NOT counted as checks: {len(DATA)}")
    print()
    print("MACHINE-SUPPORTED VERDICT (interpretation in decision.md):")
    print("  UNIFORM_NO_PAIRING -- kill branch (b). The three channel columns of the")
    print("  3x2 table are identical. P14 is dead.")
    print("  BUT (F7, and both FL Step 8a skeptic passes): that conclusion is ONE-LINE")
    print("  DERIVABLE from E-L3B + L5 with nothing this round computed, so by")
    print("  round114's own criterion it is a RESTATEMENT, not independent evidence.")
    print("  The 'a Z3 label cannot pass a Z2 carrier' argument is WITHDRAWN (E5, J2):")
    print("  a 2+1 split would satisfy claim.md's predicate, and channel-dependent S6")
    print("  data pairs t to the channel through the shared scalar with no Z2 involved.")
    print("  The round's genuine positive content is section G (C134 route-2")
    print("  non-transfer, verified not assumed) and section J's two counterexamples.")

    out = {
        "checks_total": n,
        "checks_passed": n_ok,
        "all_passed": n_ok == n,
        "checks": CHECKS,
        "data": DATA,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_c136.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nwrote {path}")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
