"""C135 -- does C133's explicit triality Z3 cyclically permute the
(Gamma_A, Gamma_B) sign patterns of 8_v, 8_s, 8_c?

Closes pearl_registry/INDEX.md row 40's own `next_check`.

Two sides are compared, each rebuilt from its OWN primary source:

  SIDE 1 (C133 / J3(O) / octonion-covariance).  C133's script is exec'd
  verbatim from a hash-checked temp copy, so `sigma`, `U24`, the octonion
  multiplication table and the 28 so(8) triples are literally the objects
  C133 computed -- not a re-derivation.  The temp copy exists only so that
  importing C133 cannot overwrite `results_c133.json`.

  SIDE 2 (round119 / L3B_SPIN8_INTERFACE_SPEC.md SS1.5 / Clifford).  Gamma_A,
  Gamma_B are rebuilt from that document's own recipe: 8 anticommuting
  16x16 gammas, Gamma_A = G1G2G3G4, Gamma_B = G5G6G7G8.  All three channels
  (V via the conjugation action on span(Gamma_i), S+ and S- via restriction
  to the Gamma_9 eigenspaces) come out of that ONE algebra, so no
  intertwiner is needed to compare them with each other.

Every block below is paired with a control that CAN fail.  Blocks whose
result is entailed by construction are labelled ENTAILED and are not counted
as evidence (C133's two skeptic passes made exactly that complaint).
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
import shutil
import tempfile

import numpy as np

TOL = 1e-9
HERE = os.path.dirname(os.path.abspath(__file__))
C133 = os.path.normpath(
    os.path.join(
        HERE, "..", "20260902-c133-symmetry-ladder-pairing-space", "c133_symmetry_ladder.py"
    )
)

OUT: dict = {}


# ==========================================================================
# 0.  Reuse C133 verbatim.
# ==========================================================================
def load_c133() -> dict:
    """Exec C133's script from a hash-verified copy in a temp dir.

    # WHY the copy: C133's script writes results_c133.json next to its own
    # __file__ at module level.  Importing it in place would silently
    # overwrite a committed artifact of a different experiment.  Copying
    # first redirects that write into a temp dir; the sha256 check proves the
    # code executed is byte-identical to C133's committed code.
    """
    with open(C133, "rb") as fh:
        raw = fh.read()
    digest = hashlib.sha256(raw).hexdigest()

    tmp = tempfile.mkdtemp(prefix="c135_c133_")
    try:
        dst = os.path.join(tmp, "c133_symmetry_ladder.py")
        shutil.copyfile(C133, dst)
        ns: dict = {"__file__": dst, "__name__": "c133_reused"}
        # C133 prints its whole JSON to stdout at import; swallow it.
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(raw, dst, "exec"), ns)  # noqa: S102
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    ns["_sha256"] = digest
    return ns


C = load_c133()

OUT["step0_reused_from_c133"] = {
    "source_file": os.path.relpath(C133, HERE).replace("\\", "/"),
    "sha256": C["_sha256"],
    "reused_objects": [
        "T_O / C_O (Cayley-Dickson octonion table + conjugation)",
        "to_matrix / from_matrix / jordan_prod (J3(O))",
        "sigma  (the explicit triality Z3, C133 SS3c)",
        "U24    (its 24x24 channel realisation, c133 script lines 637-642)",
        "TRIPLES / RHO (the 28 so(8) triality triples)",
    ],
    # Re-reported here to prove the objects in hand are C133's, not a re-derivation.
    "sigma_cubed_is_identity_max_err": C["OUT"]["step2b_sigma"]["sigma_cubed_is_identity_max_err"],
    "sigma_acts_as_xyz_to_zxy_max_err": C["OUT"]["step2b_sigma"][
        "sigma_acts_as_xyz_to_zxy_max_err"
    ],
    "sigma_is_jordan_automorphism_max_err": C["OUT"]["step2b_sigma"][
        "sigma_is_jordan_automorphism_max_err"
    ],
    "U_normalises_the_so8_image_rel_resid": C["OUT"][
        "step5e_U_is_a_legitimate_symmetry_only_where_claimed"
    ]["real_case_(rho1,rho2,rho3)_U_normalises_rel_resid"],
    "n_so8_generators": C["OUT"]["step2d_so8"]["n_generators"],
}

omulf = C["omulf"]
jordan_prod = C["jordan_prod"]
U24 = C["U24"]
RHO = C["RHO"]
RNG = np.random.default_rng(20260902)

D_A = np.diag([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0])


# ==========================================================================
# 1.  Is the H / H-ell block split an OCTONION AUTOMORPHISM?
#     (L3b SS1.5: H = span(e0..e3), H-ell = span(e4..e7).)
# ==========================================================================
def is_subalgebra(idx: list[int]) -> float:
    """Max leakage of e_i * e_j outside span(e_k : k in idx)."""
    worst = 0.0
    comp = [k for k in range(8) if k not in idx]
    for i, j in itertools.product(idx, repeat=2):
        u, v = np.eye(8)[i], np.eye(8)[j]
        p = omulf(u, v)
        worst = max(worst, float(np.max(np.abs(p[comp]))))
    return worst


def aut_residual(M: np.ndarray) -> float:
    """Max |M(uv) - M(u)M(v)| over random octonion pairs."""
    worst = 0.0
    for _ in range(200):
        u, v = RNG.normal(size=8), RNG.normal(size=8)
        worst = max(worst, float(np.max(np.abs(M @ omulf(u, v) - omulf(M @ u, M @ v)))))
    return worst


def sign_op(neg: list[int]) -> np.ndarray:
    """Diagonal +/-1 operator negating exactly the basis directions in `neg`."""
    d = np.ones(8)
    d[neg] = -1.0
    return np.diag(d)


# WHY this is chosen programmatically and not hard-coded: the FIRST version of
# this script used D = diag(1,1,-1,-1,1,1,-1,-1) as the "not an automorphism"
# control.  It returned residual 0.0 -- because span(e0,e1,e4,e5) is ALSO a
# quaternion subalgebra, so that operator is a SECOND G2 involution, not a
# negative control.  A control that cannot fail is not a control.  We now
# search for a genuine one and record how many 4-subsets actually qualify.
quaternionic, nonquaternionic = [], []
for trio in itertools.combinations(range(1, 8), 3):
    idx = [0, *trio]
    (quaternionic if is_subalgebra(idx) < TOL else nonquaternionic).append(idx)

D_A2 = sign_op([k for k in range(8) if k not in quaternionic[1]])  # a 2nd G2 involution
D_BAD4 = sign_op([k for k in range(8) if k not in nonquaternionic[0]])  # genuine control
D_BAD1 = sign_op([0])  # negates the unit 1 -- cannot be an automorphism
Q_RAND = np.linalg.qr(RNG.normal(size=(8, 8)))[0]

OUT["step1_block_split_is_an_octonion_automorphism"] = {
    "H_span_e0_e3_is_a_subalgebra_leakage": is_subalgebra([0, 1, 2, 3]),
    "CONTROL_span_e0_e1_e2_is_NOT_a_subalgebra_leakage": is_subalgebra([0, 1, 2]),
    "n_quaternionic_4_subsets_through_e0": len(quaternionic),
    "matches_7_Fano_lines": len(quaternionic) == 7,
    "D_A_is_an_octonion_automorphism_resid": aut_residual(D_A),
    "SECOND_G2_involution_also_resid_0": {
        "fixed_subalgebra": quaternionic[1],
        "resid": aut_residual(D_A2),
    },
    "CONTROL_nonquaternionic_4_4_split_resid": {
        "fixed_subspace": nonquaternionic[0],
        "resid": aut_residual(D_BAD4),
    },
    "CONTROL_negate_the_unit_resid": aut_residual(D_BAD1),
    "CONTROL_random_orthogonal_resid": aut_residual(Q_RAND),
    "reading": (
        "D_A (fix H, negate H-ell) IS an automorphism of O, hence lies in "
        "G2 = Aut(O) = Fix(triality).  Exactly 7 of the 35 four-subsets "
        "through e0 are quaternion subalgebras -- the 7 Fano lines -- so the "
        "H/H-ell split is one of a G2-orbit of equivalent choices, not a "
        "distinguished one.  The three controls (a NON-quaternionic 4+4 "
        "split, negating the unit, a random rotation) all fail by O(1), so "
        "the test genuinely can fail."
    ),
}


# ==========================================================================
# 2.  Which diagonal sign triples on (x, y, z) are J3(O) automorphisms?
#     This is the group-level center of Spin(8) in C133's own language.
# ==========================================================================
def slot_sign_map(eps: tuple[int, int, int], base: np.ndarray | None = None) -> np.ndarray:
    """27x27: identity on the three diagonal reals, eps_i * base on slot i."""
    B = np.eye(8) if base is None else base
    M = np.zeros((27, 27))
    M[:3, :3] = np.eye(3)
    for k, e in enumerate(eps):
        M[3 + 8 * k : 11 + 8 * k, 3 + 8 * k : 11 + 8 * k] = e * B
    return M


def jordan_aut_residual27(M: np.ndarray) -> float:
    worst = 0.0
    for _ in range(60):
        u, v = RNG.normal(size=27), RNG.normal(size=27)
        worst = max(worst, float(np.max(np.abs(M @ jordan_prod(u, v) - jordan_prod(M @ u, M @ v)))))
    return worst


sign_scan = {}
for eps in itertools.product([1, -1], repeat=3):
    r = jordan_aut_residual27(slot_sign_map(eps))
    sign_scan["".join("+" if e > 0 else "-" for e in eps)] = {
        "product_of_signs": int(np.prod(eps)),
        "jordan_automorphism_resid": r,
        "is_automorphism": bool(r < TOL),
    }

passing = sorted(k for k, v in sign_scan.items() if v["is_automorphism"])
OUT["step2_center_of_Spin8_as_slot_sign_triples"] = {
    "scan": sign_scan,
    "passing": passing,
    "n_passing": len(passing),
    "matches_Klein_four_group": sorted(passing) == sorted(["+++", "+--", "-+-", "--+"]),
    "reading": (
        "Exactly the four sign triples with product +1 are automorphisms; the "
        "other four fail by O(1).  These four are the center Z2 x Z2 of "
        "Spin(8).  EVERY nontrivial one has exactly ONE '+' and TWO '-'."
    ),
}


# ==========================================================================
# 3.  How the triality Z3 acts on those central elements  (ENTAILED in form,
#     but the ORBIT STRUCTURE is the content).
# ==========================================================================
def conj_by_U(eps: tuple[int, int, int]) -> tuple[int, ...]:
    M24 = slot_sign_map(eps)[3:, 3:]
    R = U24 @ M24 @ U24.T
    return tuple(round(R[8 * k, 8 * k]) for k in range(3))


orbit = {}
for eps in [(1, -1, -1), (-1, 1, -1), (-1, -1, 1), (1, 1, 1)]:
    key = "".join("+" if e > 0 else "-" for e in eps)
    img = conj_by_U(eps)
    orbit[key] = {
        "image_under_U_conjugation": "".join("+" if e > 0 else "-" for e in img),
        "is_fixed": img == eps,
    }

OUT["step3_Z3_orbit_on_the_center"] = {
    "orbit": orbit,
    "three_nontrivial_elements_form_one_3_cycle": (
        orbit["+--"]["image_under_U_conjugation"] == "-+-"
        and orbit["-+-"]["image_under_U_conjugation"] == "--+"
        and orbit["--+"]["image_under_U_conjugation"] == "+--"
    ),
    "identity_element_is_fixed": orbit["+++"]["is_fixed"],
}


# ==========================================================================
# 4.  D_A itself under triality:  diag(D_A, D_A, D_A) legitimate + U-invariant?
# ==========================================================================
G_B_27 = slot_sign_map((1, 1, 1), base=D_A)
G_B_24 = G_B_27[3:, 3:]
bad_mixed = slot_sign_map((1, 1, 1), base=None).copy()
bad_mixed[3:11, 3:11] = D_A
bad_mixed[11:19, 11:19] = D_A
bad_mixed[19:27, 19:27] = Q_RAND

OUT["step4_D_A_is_triality_fixed"] = {
    "diag_DA_DA_DA_is_a_J3O_automorphism_resid": jordan_aut_residual27(G_B_27),
    "CONTROL_diag_DA_DA_randomSO8_resid": jordan_aut_residual27(bad_mixed),
    "CONTROL_diag_nonquaternionic_split_x3_resid": jordan_aut_residual27(
        slot_sign_map((1, 1, 1), base=D_BAD4)
    ),
    "commutator_with_U24_max_abs": float(np.max(np.abs(U24 @ G_B_24 - G_B_24 @ U24))),
    "reading": (
        "The SAME matrix D_A in all three slots is a J3(O) automorphism and "
        "commutes with the triality U exactly -- i.e. D_A is triality-FIXED. "
        "Replacing one slot by a random SO(8) element, or D_A by a 4+4 sign "
        "operator whose fixed subspace is NOT a quaternion subalgebra, "
        "breaks it by O(1)."
    ),
}


# ==========================================================================
# 5.  so(4)+so(4) = centralizer of D_A, and its triality image
#     (independent replication of pearl row 41, different code path).
# ==========================================================================
def centralizer_basis(D: np.ndarray) -> np.ndarray:
    """Basis of {A in so(8) (slot-1 image) : [A, D] = 0}, as coefficient vectors."""
    A28 = np.array([RHO[0][k].flatten() for k in range(28)])  # 28 x 64
    rows = []
    for k in range(28):
        M = RHO[0][k]
        rows.append((M @ D - D @ M).flatten())
    Cmat = np.array(rows).T  # 64 x 28
    _u, s, vt = np.linalg.svd(Cmat)
    tol = max(Cmat.shape) * np.finfo(float).eps * (s[0] if s.size else 1.0) * 1e3
    null = vt[np.sum(s > tol) :]
    return null, A28


def triality_image_stays_inside(D: np.ndarray) -> dict:
    null, _ = centralizer_basis(D)
    dim = int(null.shape[0])
    # slot-1 and slot-2 matrices for each basis element of the centralizer
    m1 = [sum(c * RHO[0][k] for k, c in enumerate(vec)) for vec in null]
    m2 = [sum(c * RHO[1][k] for k, c in enumerate(vec)) for vec in null]
    B = np.array([M.flatten() for M in m1]).T
    Qb, _ = np.linalg.qr(B)
    worst = 0.0
    for M in m2:
        v = M.flatten()
        worst = max(
            worst, float(np.linalg.norm(v - Qb @ (Qb.T @ v)) / max(np.linalg.norm(v), 1e-30))
        )
    # T : slot-1 coords -> slot-1 coords of the slot-2 partner
    T = np.linalg.lstsq(B, np.array([M.flatten() for M in m2]).T, rcond=None)[0]
    ev = np.linalg.eigvals(T)
    return {
        "dim_centralizer": dim,
        "triality_image_stays_in_the_same_subalgebra_rel_resid": worst,
        "T_cubed_minus_I_max_abs": float(
            np.max(np.abs(np.linalg.matrix_power(T, 3) - np.eye(dim)))
        ),
        "T_eigenvalue_multiplicities": {
            "plus_1": int(np.sum(np.abs(ev - 1) < 1e-6)),
            "omega": int(np.sum(np.abs(ev - np.exp(2j * np.pi / 3)) < 1e-6)),
            "omega_bar": int(np.sum(np.abs(ev - np.exp(-2j * np.pi / 3)) < 1e-6)),
        },
    }


real_case = triality_image_stays_inside(D_A)
control_case = triality_image_stays_inside(D_BAD4)
second_g2 = triality_image_stays_inside(D_A2)

OUT["step5_so4_so4_is_the_centralizer_of_D_A"] = {
    "D_A_centralizer": real_case,
    "CONTROL_nonquaternionic_split_centralizer": control_case,
    "SECOND_G2_involution_centralizer": second_g2,
    "reading": (
        "so(4)+so(4) IS the centralizer of D_A in so(8) (dim 12 = 6+6).  Its "
        "triality image lands back inside itself, and T has eigenvalue "
        "multiplicities {+1 x6, omega x3, omega-bar x3} with T^3 = I -- "
        "independently replicating pearl row 41 through C133's triples "
        "instead of row 41's own covariance solve.  This is EXPLAINED, not "
        "just observed: D_A is triality-fixed (step 4), so its centralizer "
        "must be triality-invariant.  The control is a 4+4 sign operator "
        "whose fixed subspace is NOT a quaternion subalgebra: same dim-12 "
        "centralizer, but its triality image does NOT stay inside -- so the "
        "test discriminates on quaternionicity, not on dimension counting."
    ),
}


# ==========================================================================
# 6.  SIDE 2: rebuild (Gamma_A, Gamma_B) from L3b SS1.5's own recipe.
# ==========================================================================
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
i2 = np.eye(2, dtype=complex)


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


G = [
    kron(s1, i2, i2, i2),
    kron(s2, i2, i2, i2),
    kron(s3, s1, i2, i2),
    kron(s3, s2, i2, i2),
    kron(s3, s3, s1, i2),
    kron(s3, s3, s2, i2),
    kron(s3, s3, s3, s1),
    kron(s3, s3, s3, s2),
]

cliff = float(
    max(
        np.max(np.abs(G[i] @ G[j] + G[j] @ G[i] - 2 * (i == j) * np.eye(16)))
        for i in range(8)
        for j in range(8)
    )
)

GA = G[0] @ G[1] @ G[2] @ G[3]
GB = G[4] @ G[5] @ G[6] @ G[7]
G9 = GA @ GB

OUT["step6_clifford_side_reconstruction"] = {
    "anticommutator_max_err": cliff,
    "Gamma_A_squared_minus_I": float(np.max(np.abs(GA @ GA - np.eye(16)))),
    "Gamma_B_squared_minus_I": float(np.max(np.abs(GB @ GB - np.eye(16)))),
    "Gamma_A_Gamma_B_commutator": float(np.max(np.abs(GA @ GB - GB @ GA))),
    "Gamma_9_squared_minus_I": float(np.max(np.abs(G9 @ G9 - np.eye(16)))),
    "Gamma_9_equals_product_of_all_eight": float(
        np.max(np.abs(G9 - G[0] @ G[1] @ G[2] @ G[3] @ G[4] @ G[5] @ G[6] @ G[7]))
    ),
    "reproduces_L3b_relations": (
        "Gamma_A Gamma_B = Gamma_9 and [Gamma_A, Gamma_B] = 0 -- both stated "
        "as VERIFIED in L3B_SPIN8_INTERFACE_SPEC.md SS1.5, reproduced here."
    ),
}


def rho_v(g: np.ndarray) -> np.ndarray:
    """Vector-rep action: g Gamma_a g^-1 = sum_b V[b,a] Gamma_b."""
    gi = np.linalg.inv(g)
    V = np.zeros((8, 8))
    for a in range(8):
        X = g @ G[a] @ gi
        for b in range(8):
            V[b, a] = float(np.real(np.trace(G[b] @ X) / 16.0))
    return V


# S+ / S- : eigenspaces of Gamma_9
w, Vg = np.linalg.eigh(G9)
Sp = Vg[:, np.abs(w - 1) < 1e-8]
Sm = Vg[:, np.abs(w + 1) < 1e-8]


def restrict(g: np.ndarray, basis: np.ndarray) -> np.ndarray:
    return basis.conj().T @ g @ basis


chan = {
    "8_v": (rho_v(GA), rho_v(GB)),
    "8_s": (np.real(restrict(GA, Sp)), np.real(restrict(GB, Sp))),
    "8_c": (np.real(restrict(GA, Sm)), np.real(restrict(GB, Sm))),
}

sign_table = {}
for name, (a, b) in chan.items():
    same = float(np.max(np.abs(a - b)))
    opp = float(np.max(np.abs(a + b)))
    ratio = a @ np.linalg.inv(b)
    eps = round(float(np.real(np.trace(ratio))) / 8.0)
    sign_table[name] = {
        "dim_S_plus_or_minus": int(a.shape[0]),
        "Gamma_A_minus_Gamma_B_max_abs": same,
        "Gamma_A_plus_Gamma_B_max_abs": opp,
        "relation": "Gamma_A = +Gamma_B" if same < TOL else "Gamma_A = -Gamma_B",
        "epsilon_rho_X_of_Gamma_9": eps,
        # WHY not "Gamma_B == D_A" in all three channels: on S+/S- that
        # identification needs L3b's P,Q intertwiners and is basis-dependent.
        # The basis-INDEPENDENT content is the eigenvalue signature, so that
        # is what is reported.  (A first version compared |Gamma_B| to |D_A|,
        # which is nearly vacuous -- both are all-ones in absolute value.)
        "Gamma_B_eigenvalue_multiplicities_+1_-1": [
            int(np.sum(np.abs(np.linalg.eigvalsh(b) - 1) < 1e-8)),
            int(np.sum(np.abs(np.linalg.eigvalsh(b) + 1) < 1e-8)),
        ],
        "vector_channel_only_rho_v_Gamma_B_equals_D_A": (
            float(np.max(np.abs(b - D_A))) if name == "8_v" else None
        ),
    }

eps_triple = tuple(sign_table[k]["epsilon_rho_X_of_Gamma_9"] for k in ["8_v", "8_s", "8_c"])
OUT["step6b_the_three_sign_patterns"] = {
    "per_channel": sign_table,
    "epsilon_triple_(v,s,c)": list(eps_triple),
    "n_DISTINCT_sign_patterns_across_the_three_channels": len(set(eps_triple)),
    "reading": (
        "The relative sign of (Gamma_A, Gamma_B) is rho_X(Gamma_9), a CENTRAL "
        "element -- so it is a Z2-valued statistic.  8_s is the odd one out; "
        "8_v and 8_c carry the SAME relation Gamma_A = -Gamma_B."
    ),
}


# ==========================================================================
# 7.  THE DECISIVE TEST.  Can a Z3 cyclically permute those patterns?
# ==========================================================================
perms = list(itertools.permutations(range(3)))
stab = [p for p in perms if tuple(eps_triple[p[i]] for i in range(3)) == eps_triple]
three_cycles = [p for p in perms if all(p[i] != i for i in range(3))]

OUT["step7_DECISIVE"] = {
    "epsilon_triple": list(eps_triple),
    "n_distinct_values": len(set(eps_triple)),
    "stabiliser_of_the_pattern_in_S3_order": len(stab),
    "stabiliser_elements": [list(p) for p in stab],
    "any_3_cycle_fixes_the_pattern": any(p in stab for p in three_cycles),
    "channels_sharing_a_pattern": [
        [k for k in ["8_v", "8_s", "8_c"] if sign_table[k]["epsilon_rho_X_of_Gamma_9"] == val]
        for val in sorted(set(eps_triple))
    ],
    "VERDICT_z3_cyclically_permutes_the_sign_patterns": len(set(eps_triple)) == 3,
    "THIS_TEST_IS_ONE_SIDED": (
        "DISCLOSED, not hidden.  Once Gamma_A Gamma_B = Gamma_9 is a "
        "NONTRIVIAL CENTRAL element (step 6, verified), the sign triple is "
        "forced by step 2 to have exactly one '+' -- so n_distinct_values "
        "could never have been 3.  The test therefore has kill power but no "
        "rescue power: it could fire and did, but could not have confirmed. "
        "The informative content is the REASON (the statistic is the image "
        "of a central element), which is contingent on round119's specific "
        "choice of the two half-volume operators -- step 8 exhibits a "
        "different statistic on the SAME construction that does take three "
        "distinct values."
    ),
    "reading": (
        "A consistent single-symmetry cyclic permutation of THREE sign "
        "patterns requires three DISTINCT patterns.  There are only two.  "
        "The stabiliser of the pattern inside the triality S3 is the Z2 "
        "swapping the two channels that share it -- so the fixed pair "
        "(Gamma_A, Gamma_B) manifestly breaks S3 to Z2, and no Z3 fixes it."
    ),
}


# ==========================================================================
# 8.  Reading 2: what the Z3 DOES cyclically permute -- the su(2)^4 pairings.
# ==========================================================================
def sigma_gen(i: int, j: int) -> np.ndarray:
    return 0.25 * (G[i] @ G[j] - G[j] @ G[i])


def su2_triples(block: list[int]) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Self-dual / anti-self-dual split of so(4) on a 4-index block."""
    a, b, c, d = block
    eps3 = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    loc = [a, b, c]
    plus, minus = [], []
    for k in range(3):
        dual = np.zeros((16, 16), dtype=complex)
        for lm, sgn in eps3.items():
            if lm[0] == k:
                dual = dual + sgn * sigma_gen(loc[lm[1]], loc[lm[2]])
        base = sigma_gen(loc[k], d)
        plus.append(0.5 * (base + 0.5 * dual))
        minus.append(0.5 * (base - 0.5 * dual))
    return plus, minus


f1p, f1m = su2_triples([0, 1, 2, 3])
f2p, f2m = su2_triples([4, 5, 6, 7])
FACTORS = {"su2_1": f1p, "su2_2": f1m, "su2_3": f2p, "su2_4": f2m}

commute_check = float(max(np.max(np.abs(x @ y - y @ x)) for x in f1p for y in f1m))


def summand_pairing(
    basis16: np.ndarray | None,
    split_op: np.ndarray,
    vector: bool,
    factors: dict | None = None,
) -> list[list[str]]:
    """For each +/-1 eigenspace of split_op, which su(2) factors act nontrivially."""
    fac = FACTORS if factors is None else factors
    out = []
    for sgn in (+1, -1):
        if vector:
            w2, V2 = np.linalg.eigh(split_op)
            P = V2[:, np.abs(w2 - sgn) < 1e-8]
            act = []
            for name, gens in fac.items():
                nrm = max(float(np.linalg.norm(P.conj().T @ rho_v_alg(g) @ P)) for g in gens)
                if nrm > 1e-8:
                    act.append(name)
        else:
            R = basis16
            # WHY not np.real(op): op is complex Hermitian, and taking only
            # its real part is NOT the same operator.  It happened to be
            # harmless on the quaternionic path (the compression came out
            # real) but silently emptied the eigenspaces on the step-8b
            # control, which would have been reported as a finding.
            op = R.conj().T @ split_op @ R
            w2, V2 = np.linalg.eigh(op)
            P = R @ V2[:, np.abs(w2 - sgn) < 1e-8]
            act = []
            for name, gens in fac.items():
                nrm = max(float(np.linalg.norm(P.conj().T @ g @ P)) for g in gens)
                if nrm > 1e-8:
                    act.append(name)
        out.append(sorted(act))
    return out


def rho_v_alg(g: np.ndarray) -> np.ndarray:
    """Vector-rep image of a Lie-algebra element: [g, Gamma_a] = sum_b M[b,a] Gamma_b."""
    M = np.zeros((8, 8), dtype=complex)
    for a in range(8):
        X = g @ G[a] - G[a] @ g
        for b in range(8):
            M[b, a] = np.trace(G[b] @ X) / 16.0
    return M


pairings = {
    "8_v": summand_pairing(None, rho_v(GB), vector=True),
    "8_s": summand_pairing(Sp, GB, vector=False),
    "8_c": summand_pairing(Sm, GB, vector=False),
}
pairing_keys = {k: sorted(tuple(sorted(p)) for p in v) for k, v in pairings.items()}
distinct = len({str(v) for v in pairing_keys.values()})

# Each su(2) factor must actually BE an su(2): 3-dimensional and closed.
LABELS = ["su2_1", "su2_2", "su2_3", "su2_4"]
su2_sanity = {}
for name, gens in FACTORS.items():
    B = np.array([g.flatten() for g in gens]).T
    Qb, _ = np.linalg.qr(B)
    worst = 0.0
    for p, q in itertools.combinations(range(3), 2):
        v = (gens[p] @ gens[q] - gens[q] @ gens[p]).flatten()
        if np.linalg.norm(v) > 1e-12:
            worst = max(
                worst, float(np.linalg.norm(v - Qb @ (Qb.conj().T @ v)) / np.linalg.norm(v))
            )
    su2_sanity[name] = {
        "dim": int(np.linalg.matrix_rank(B.T, tol=1e-9)),
        "bracket_closure_rel_resid": worst,
    }

# Brute force: which permutations of the FOUR su(2) labels induce a 3-cycle of
# the three channel pairings, and what is the dimension of their fixed subspace?
as_sets = {k: {frozenset(p) for p in v} for k, v in pairings.items()}
chan_order = ["8_v", "8_s", "8_c"]
factor_perm_scan = []
for pi in itertools.permutations(range(4)):
    sub = {LABELS[i]: LABELS[pi[i]] for i in range(4)}
    img = {}
    for ch in chan_order:
        img[ch] = {frozenset(sub[x] for x in p) for p in as_sets[ch]}
    # which channel does each channel's pairing map onto?
    dest = []
    for ch in chan_order:
        hit = [d for d in chan_order if img[ch] == as_sets[d]]
        dest.append(hit[0] if len(hit) == 1 else None)
    order = 1
    cur = list(pi)
    while cur != [0, 1, 2, 3] and order < 5:
        cur = [pi[c] for c in cur]
        order += 1
    if None in dest:
        continue
    is_3cyc = all(dest[i] != chan_order[i] for i in range(3)) and len(set(dest)) == 3
    fixed_dim = 3 * sum(1 for i in range(4) if pi[i] == i) + 3 * (
        1 if order == 3 else 0
    )  # fixed factors contribute 3 each; a 3-cycle contributes its diagonal
    factor_perm_scan.append(
        {
            "perm_of_su2_labels": list(pi),
            "order": order,
            "channel_map": dict(zip(chan_order, dest, strict=True)),
            "induces_a_3_cycle_of_channels": is_3cyc,
            "predicted_fixed_subalgebra_dim": fixed_dim,
        }
    )

three_cyc_rows = [r for r in factor_perm_scan if r["induces_a_3_cycle_of_channels"]]

OUT["step8_what_the_Z3_DOES_permute"] = {
    "su2_factors_of_so4_1_commute_max_err": commute_check,
    "su2_factor_sanity": su2_sanity,
    "pairings_per_channel": pairings,
    "n_distinct_pairings": distinct,
    "all_three_pairings_distinct": distinct == 3,
    "n_su2_label_permutations_inducing_a_channel_3_cycle": len(three_cyc_rows),
    "all_such_permutations_have_order_3": all(r["order"] == 3 for r in three_cyc_rows),
    "all_such_permutations_predict_fixed_dim_6": all(
        r["predicted_fixed_subalgebra_dim"] == 6 for r in three_cyc_rows
    ),
    # WHY renamed: `predicted_fixed_subalgebra_dim` is HARD-CODED arithmetic
    # (3*fixed + 3*[order==3]); every order-3 permutation of 4 labels has
    # exactly one fixed point, so it returns 6 unconditionally.  It is an
    # arithmetic expectation, NOT a corroborating measurement.  The measured
    # number it is compared against lives in step 5.
    "NOTE_fixed_dim_6_is_arithmetic_not_measured": True,
    "step5_MEASURED_plus1_multiplicity": real_case["T_eigenvalue_multiplicities"]["plus_1"],
    "example_3_cycle_rows": three_cyc_rows[:2],
    "reading": (
        "Under so(4)+so(4) = su(2)^4 each channel splits into two 4-dim "
        "pieces, and each piece is a doublet of exactly TWO of the four "
        "su(2) factors.  The three channels realise the three DISTINCT ways "
        "to pair up {1,2,3,4}.  Triality permutes the channels cyclically "
        "(step 0: U^3 = I, U normalises the algebra), hence it cyclically "
        "permutes these three pairings.  THAT is the genuine Z3 structure -- "
        "and it is exactly the 3-cycle of the four su(2) factors whose fixed "
        "subalgebra is 3 + 3 = 6-dimensional, matching step 5's measured "
        "{+1 x6, omega x3, omega-bar x3}."
    ),
}


# ==========================================================================
# 8b. CONTROLS for step 8 -- added because step 8 as first written had NONE.
#     The control quoted alongside it (0.903) belongs to step 5 and does not
#     touch the pairing computation at all.
# ==========================================================================
# T4a -- degeneracy check: can the "3 distinct pairings" counter ever report
# anything but 3?  Collapse the four su(2) labels onto two.
FACTORS_DEGEN = {"a": f1p, "b": f1p, "c": f2p, "d": f2p}
pair_degen = {
    "8_v": summand_pairing(None, rho_v(GB), vector=True, factors=FACTORS_DEGEN),
    "8_s": summand_pairing(Sp, GB, vector=False, factors=FACTORS_DEGEN),
    "8_c": summand_pairing(Sm, GB, vector=False, factors=FACTORS_DEGEN),
}
degen_distinct = len({str(sorted(tuple(sorted(p)) for p in v)) for v in pair_degen.values()})


# T4b -- the real control: redo the whole pairing computation for a
# NON-quaternionic 4+4 split of the eight gamma indices.  If "three distinct
# pairings" survives this, then distinctness is generic to ANY 4+4 split and
# says nothing about the octonionic H/H-ell structure.
def pairings_for_split(blk_a: list[int], blk_b: list[int]) -> dict:
    ga = G[blk_a[0]] @ G[blk_a[1]] @ G[blk_a[2]] @ G[blk_a[3]]
    gb = G[blk_b[0]] @ G[blk_b[1]] @ G[blk_b[2]] @ G[blk_b[3]]
    g9 = ga @ gb
    ww, VV = np.linalg.eigh(g9)
    sp, sm = VV[:, np.abs(ww - 1) < 1e-8], VV[:, np.abs(ww + 1) < 1e-8]
    p1, m1 = su2_triples(blk_a)
    p2, m2 = su2_triples(blk_b)
    fac = {"su2_1": p1, "su2_2": m1, "su2_3": p2, "su2_4": m2}
    pr = {
        "8_v": summand_pairing(None, rho_v(gb), vector=True, factors=fac),
        "8_s": summand_pairing(sp, gb, vector=False, factors=fac),
        "8_c": summand_pairing(sm, gb, vector=False, factors=fac),
    }
    nd = len({str(sorted(tuple(sorted(p)) for p in v)) for v in pr.values()})
    return {"pairings": pr, "n_distinct": nd}


nonquat_split = pairings_for_split([0, 1, 2, 4], [3, 5, 6, 7])

OUT["step8b_CONTROLS_for_the_pairing_claim"] = {
    "T4a_degenerate_labels_n_distinct": degen_distinct,
    "T4a_counter_CAN_report_less_than_3": degen_distinct < 3,
    "T4b_nonquaternionic_split_n_distinct": nonquat_split["n_distinct"],
    "T4b_pairings": nonquat_split["pairings"],
    "T4b_distinctness_survives_a_NON_quaternionic_split": nonquat_split["n_distinct"] == 3,
    "reading": (
        "T4a: the counter is not stuck at 3 -- collapsing the four su(2) "
        "labels onto two makes it drop, so it can report a failure. "
        "T4b, THE IMPORTANT ONE: three distinct pairings ALSO appear for a "
        "4+4 split of the gamma indices whose fixed subspace is NOT a "
        "quaternion subalgebra.  So distinctness of the three pairings is "
        "GENERIC to any 4+4 split and is NOT evidence about the octonionic "
        "H/H-ell structure.  What IS special to the quaternionic split is "
        "step 5: only there does the resulting so(4)+so(4) stay inside "
        "itself under triality (2.24e-15 vs the control's 0.903).  The "
        "correct claim is therefore: distinctness is generic; TRIALITY-"
        "COVARIANCE of the three pairings is not."
    ),
}


# ==========================================================================
# 9.  Kill criterion, evaluated.
# ==========================================================================
OUT["step9_kill_criterion"] = {
    "criterion_a_BLOCKED_no_basis_identification": False,
    "criterion_a_note": (
        "NOT blocked.  Both sides live on O = R^8 and the identification was "
        "already built and machine-verified in this project's own record "
        "(the P,Q intertwiners, pearl row 43).  Moreover the decisive facts "
        "used here -- Gamma_A Gamma_B = Gamma_9 central, the center being "
        "Z2 x Z2 with one '+' per nontrivial element, and triality permuting "
        "those three cyclically -- are basis-INDEPENDENT, so any residual "
        "mismatch between the two octonion realisations cannot change them."
    ),
    "criterion_b_FIRES_sigma_does_not_cyclically_permute_the_patterns": bool(
        len(set(eps_triple)) != 3
    ),
    "claim_as_preregistered_is": "FALSE" if len(set(eps_triple)) != 3 else "TRUE",
}

with open(os.path.join(HERE, "results_c135.json"), "w", encoding="utf-8") as fh:
    json.dump(OUT, fh, indent=2, default=str)

print(json.dumps(OUT, indent=2, default=str))
