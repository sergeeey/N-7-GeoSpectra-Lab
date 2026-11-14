"""C125 -- full gauge-equivalence gate for the t=0 vs t=1 pair.

Computational core of `decision.md`.  Nothing here refers to the external
`Kimi_Agent` document; every identity it asserts is rebuilt from scratch in
this project's own conventions (`docs/clifford_convention_registry.md`).

Six independent blocks:

  A. S3 = SU(2) as unit quaternions; Isom(S3) = O(4) = SO(4) u SO(4)*iota.
     Verify iota(g)=g^{-1}, the tangent determinants, and the conjugation
     action iota o phi_{a,b} o iota = phi_{b,a}  (SU(2)_a <-> SU(2)_b swap).

  B. Cartan-Schouten family.  nabla^t_X Y = t[X,Y] on left-invariant fields.
     nabla^0 is the unique connection with the LEFT-invariant frame parallel;
     nabla^1 the unique one with the RIGHT-invariant frame parallel (verified
     here directly, not cited).  A map phi satisfies phi_*nabla^0 = nabla^1
     iff it carries the left-invariant frame to the right-invariant frame up
     to a CONSTANT matrix.  Test every element of O(4) through its two
     cosets.  => the set {phi : phi_* nabla^0 = nabla^1} is EXACTLY the
     orientation-reversing coset.

  C. Full 13D orientation bookkeeping over the 2^3 sign assignments.

  D. Clifford: rebuild Cl(1,3) x Cl(3) x Cl(6) -> Cl(1,12) in this repo's own
     S3 (Z_i = i sigma_i, Z^2=-1) and S6 (Gamma_a hermitian, Gamma^2=+1)
     conventions AND in the registry's rule-3 uniformised negative-definite
     convention.  Decide the disputed identity `Gamma_4 = +- omega_3 Gamma_6`
     under BOTH readings (intrinsic-factor vs 13D-embedded).

  E. The Z2 transformation law of the 13D-embedded pseudoscalars under frame
     reflection (this is the part that is convention-independent).

  F. Conjugate-bundle arithmetic c_k(Ebar) = (-1)^k c_k(E).

Run:  python experiments/20260901-c125-full-gauge-equivalence-gate/c125_full_gauge_equivalence.py
"""

from __future__ import annotations

import json
import pathlib

import numpy as np

RNG = np.random.default_rng(20260901)
TOL = 1e-10
OUT: dict = {}


# --------------------------------------------------------------------------
# quaternion helpers  (q = [w, x, y, z]  <->  w + x i + y j + z k)
# --------------------------------------------------------------------------
def qmul(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return np.array(
        [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        ]
    )


def qconj(q: np.ndarray) -> np.ndarray:
    return np.array([q[0], -q[1], -q[2], -q[3]])


def rand_unit_quat() -> np.ndarray:
    v = RNG.normal(size=4)
    return v / np.linalg.norm(v)


E_IM = [np.array([0.0, 1, 0, 0]), np.array([0.0, 0, 1, 0]), np.array([0.0, 0, 0, 1])]


def left_frame(g: np.ndarray) -> np.ndarray:
    """X_i(g) = g * e_i, columns are the 3 left-invariant frame vectors in R^4."""
    return np.column_stack([qmul(g, e) for e in E_IM])


def right_frame(g: np.ndarray) -> np.ndarray:
    """Y_i(g) = e_i * g."""
    return np.column_stack([qmul(e, g) for e in E_IM])


# --------------------------------------------------------------------------
# BLOCK A -- Isom(S3) = O(4), iota, and the SU(2)_a <-> SU(2)_b swap
# --------------------------------------------------------------------------
def phi(a: np.ndarray, b: np.ndarray, g: np.ndarray) -> np.ndarray:
    """SO(4) element:  g |-> a g b^{-1}."""
    return qmul(qmul(a, g), qconj(b))


def iota(g: np.ndarray) -> np.ndarray:
    return qconj(g)


def block_A() -> dict:
    res: dict = {}

    # A1: iota(g) = g^{-1} for unit quaternions
    err = max(
        np.abs(qmul(iota(g := rand_unit_quat()), g) - np.array([1.0, 0, 0, 0])).max()
        for _ in range(200)
    )
    res["A1_iota_is_inverse_maxerr"] = float(err)
    res["A1_pass"] = bool(err < TOL)

    # A2: iota o phi_{a,b} o iota  ==  phi_{b,a}   (the SU(2)_a <-> SU(2)_b swap)
    worst = 0.0
    for _ in range(200):
        a, b, g = rand_unit_quat(), rand_unit_quat(), rand_unit_quat()
        lhs = iota(phi(a, b, iota(g)))
        rhs = phi(b, a, g)
        worst = max(worst, float(np.abs(lhs - rhs).max()))
    res["A2_conjugation_swaps_SU2_factors_maxerr"] = worst
    res["A2_pass"] = bool(worst < TOL)

    # A2b: negative control -- iota o phi_{a,b} o iota  !=  phi_{a,b} in general
    diffs = []
    for _ in range(200):
        a, b, g = rand_unit_quat(), rand_unit_quat(), rand_unit_quat()
        diffs.append(float(np.abs(iota(phi(a, b, iota(g))) - phi(a, b, g)).max()))
    res["A2b_negcontrol_median_diff"] = float(np.median(diffs))
    res["A2b_pass"] = bool(np.median(diffs) > 1e-3)

    # A3: tangent determinant, computed against an ambient-orientation-pinned
    #     basis (the C39 lesson: an un-pinned QR basis measures the QR call).
    #     [g | X_1 | X_2 | X_3] is in SO(4) for every unit g, so the
    #     left-invariant frame IS the pinned oriented basis; det(dphi|TS3) is
    #     then just the determinant of the frame-transition matrix.
    def tangent_det(f, g: np.ndarray) -> float:
        gp = f(g)
        Fs = left_frame(g)  # 4x3 at g
        Ft = left_frame(gp)  # 4x3 at f(g)
        # numerical differential of f along the frame directions
        h = 1e-6
        cols = []
        for j in range(3):
            gp_plus = f(_normalize(g + h * Fs[:, j]))
            gp_minus = f(_normalize(g - h * Fs[:, j]))
            cols.append((gp_plus - gp_minus) / (2 * h))
        J = np.column_stack(cols)  # 4x3, image vectors
        M = np.linalg.lstsq(Ft, J, rcond=None)[0]  # 3x3 frame-transition
        return float(np.linalg.det(M))

    dets_so4, dets_coset = [], []
    for _ in range(100):
        a, b = rand_unit_quat(), rand_unit_quat()
        g = rand_unit_quat()
        dets_so4.append(tangent_det(lambda x, a=a, b=b: phi(a, b, x), g))
        dets_coset.append(tangent_det(lambda x, a=a, b=b: phi(a, b, iota(x)), g))
    res["A3_det_SO4_coset_min"] = float(np.min(dets_so4))
    res["A3_det_SO4_coset_max"] = float(np.max(dets_so4))
    res["A3_det_iota_coset_min"] = float(np.min(dets_coset))
    res["A3_det_iota_coset_max"] = float(np.max(dets_coset))
    res["A3_pass"] = bool(
        np.allclose(dets_so4, 1.0, atol=1e-5) and np.allclose(dets_coset, -1.0, atol=1e-5)
    )
    return res


def _normalize(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


# --------------------------------------------------------------------------
# BLOCK B -- which isometries send nabla^0 to nabla^1
# --------------------------------------------------------------------------
def ad_matrix(q: np.ndarray) -> np.ndarray:
    """SO(3) matrix of Ad_q on Im(H) in the (i,j,k) basis."""
    return np.column_stack([qmul(qmul(q, e), qconj(q))[1:] for e in E_IM])


def block_B() -> dict:
    res: dict = {}

    # WHY this block was rewritten (FL Step 8a skeptic pass, 2026-09-01):
    #   the ORIGINAL B1 was a TAUTOLOGY.  It compared `-ad_e[i] @ A` against a
    #   hand-expanded `brack[l,j] = sum_k A[k,j]*2*eps[i,k,l]`, and those two
    #   expressions are literally the same matrix for ANY 3x3 `A` -- feed it
    #   `np.ones((3,3))` and the residual is still exactly 0.0.  The claimed
    #   derivative `d/ds Ad_{conj(g e^{s e_i})} = -ad_{e_i} Ad_gbar` was never
    #   differentiated, so the geometric content was never touched.  Confirmed
    #   by direct re-run.  Replaced with B0 (a real finite-difference test of
    #   exactly that derivative, which CAN fail) and B3 (the torsion /
    #   volume-tensor argument, which proves the theorem exhaustively with no
    #   sampling at all and explains WHY the two Z2 characters coincide).
    eps = np.zeros((3, 3, 3))
    for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        eps[i, j, k] = 1.0
        eps[i, k, j] = -1.0
    ad_e = [
        2.0 * np.array([[eps[i, m, k] for m in range(3)] for k in range(3)]) for i in range(3)
    ]  # (ad_{e_i})_{km} = 2 eps_{i m k}

    # B0: FINITE-DIFFERENCE test of  d/ds|_0 Ad_{conj(g exp(s e_i))} = -ad_{e_i} Ad_gbar.
    #     This is the step the old B1 assumed.  It can fail: a wrong sign, a
    #     wrong structure constant, or a wrong side of the group action all
    #     break it.
    h = 1e-6
    worst_fd = 0.0
    for _ in range(100):
        g = rand_unit_quat()
        for i in range(3):
            axis = E_IM[i]
            gp = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) + (h / 2) * axis))
            gm = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) - (h / 2) * axis))
            num = (ad_matrix(qconj(gp)) - ad_matrix(qconj(gm))) / h
            ana = -ad_e[i] @ ad_matrix(qconj(g))
            worst_fd = max(worst_fd, float(np.abs(num - ana).max()))
    res["B0_finite_difference_dAd_maxerr"] = worst_fd
    res["B0_pass"] = bool(worst_fd < 1e-4)

    # B0b: negative control -- the SAME finite difference against the WRONG
    #      sign must fail loudly, otherwise B0 is not discriminating.
    worst_fd_bad = 0.0
    for _ in range(50):
        g = rand_unit_quat()
        for i in range(3):
            axis = E_IM[i]
            gp = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) + (h / 2) * axis))
            gm = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) - (h / 2) * axis))
            num = (ad_matrix(qconj(gp)) - ad_matrix(qconj(gm))) / h
            wrong = +ad_e[i] @ ad_matrix(qconj(g))  # sign flipped on purpose
            worst_fd_bad = max(worst_fd_bad, float(np.abs(num - wrong).max()))
    res["B0b_negcontrol_wrongsign_maxdev"] = worst_fd_bad
    res["B0b_pass"] = bool(worst_fd_bad > 1e-2)

    # B1: nabla^1 has the RIGHT-invariant frame parallel -- now assembled from
    #     the finite-difference derivative measured in B0, NOT from a
    #     re-expansion of the same symbol.
    worst = 0.0
    for _ in range(100):
        g = rand_unit_quat()
        A = ad_matrix(qconj(g))
        for i in range(3):
            axis = E_IM[i]
            gp = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) + (h / 2) * axis))
            gm = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) - (h / 2) * axis))
            deriv = (ad_matrix(qconj(gp)) - ad_matrix(qconj(gm))) / h  # measured, not assumed
            brack = np.zeros((3, 3))
            for lidx in range(3):
                for j in range(3):
                    brack[lidx, j] = sum(A[k, j] * 2.0 * eps[i, k, lidx] for k in range(3))
            worst = max(worst, float(np.abs(deriv + brack).max()))
    res["B1_nabla1_right_frame_parallel_maxerr"] = worst
    res["B1_pass"] = bool(worst < 1e-4)

    # B1b: negative control -- for nabla^0 the bracket term is absent, so the
    #      measured derivative alone must NOT vanish.
    worst0 = 0.0
    for _ in range(50):
        g = rand_unit_quat()
        for i in range(3):
            axis = E_IM[i]
            gp = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) + (h / 2) * axis))
            gm = _normalize(qmul(g, np.array([1.0, 0, 0, 0]) - (h / 2) * axis))
            worst0 = max(
                worst0, float(np.abs((ad_matrix(qconj(gp)) - ad_matrix(qconj(gm))) / h).max())
            )
    res["B1b_negcontrol_nabla0_right_frame_maxdev"] = worst0
    res["B1b_pass"] = bool(worst0 > 1e-3)

    # B2: frame-transition constancy test over BOTH cosets of O(4).
    #     M_LL(g): dphi(X_j(g)) expressed in the LEFT frame at phi(g).
    #     M_LR(g): dphi(X_j(g)) expressed in the RIGHT frame at phi(g).
    #     M_LL constant  <=>  phi_* nabla^0 = nabla^0
    #     M_LR constant  <=>  phi_* nabla^0 = nabla^1
    def transition(f, g, target="L"):
        gp = f(g)
        h = 1e-6
        Fs = left_frame(g)
        cols = []
        for j in range(3):
            cols.append(
                (f(_normalize(g + h * Fs[:, j])) - f(_normalize(g - h * Fs[:, j]))) / (2 * h)
            )
        J = np.column_stack(cols)
        Ft = left_frame(gp) if target == "L" else right_frame(gp)
        return np.linalg.lstsq(Ft, J, rcond=None)[0]

    def spread(f, target):
        gs = [rand_unit_quat() for _ in range(25)]
        Ms = [transition(f, g, target) for g in gs]
        base = Ms[0]
        return float(max(np.abs(M - base).max() for M in Ms))

    so4_LL, so4_LR, cos_LL, cos_LR = [], [], [], []
    for _ in range(12):
        a, b = rand_unit_quat(), rand_unit_quat()

        def f_so4(x, a=a, b=b):
            return phi(a, b, x)

        def f_cos(x, a=a, b=b):
            return phi(a, b, iota(x))

        so4_LL.append(spread(f_so4, "L"))
        so4_LR.append(spread(f_so4, "R"))
        cos_LL.append(spread(f_cos, "L"))
        cos_LR.append(spread(f_cos, "R"))

    res["B2_SO4_leftframe_spread_max"] = float(np.max(so4_LL))
    res["B2_SO4_rightframe_spread_min"] = float(np.min(so4_LR))
    res["B2_iotacoset_leftframe_spread_min"] = float(np.min(cos_LL))
    res["B2_iotacoset_rightframe_spread_max"] = float(np.max(cos_LR))
    res["B2_pass"] = bool(
        np.max(so4_LL) < 1e-4  # SO(4) preserves nabla^0
        and np.min(so4_LR) > 1e-2  # ... and never maps it to nabla^1
        and np.max(cos_LR) < 1e-4  # iota-coset maps nabla^0 -> nabla^1
        and np.min(cos_LL) > 1e-2  # ... and never preserves nabla^0
    )
    res["B2_note"] = (
        "B2 SAMPLES 12 (a,b) pairs per coset x 25 base points.  It is a "
        "cross-check, NOT the proof of exhaustiveness -- 'O(4) has two "
        "components' does not by itself make a sampled test exhaustive.  The "
        "exhaustive argument is B3 (torsion = volume tensor) plus the coset "
        "argument recorded in decision.md sec 2a."
    )

    # B3: THE EXHAUSTIVE PROOF (no sampling).  In the orthonormal left frame,
    #     T^t(X_i,X_j) = (2t-1)[X_i,X_j] = 2(2t-1) eps_{ijk} X_k, i.e. the
    #     torsion is a CONSTANT MULTIPLE OF THE VOLUME TENSOR.  For any
    #     isometry phi,  phi_* (volume tensor) = det(dphi|_T) * (volume tensor),
    #     so phi_* T^0 = eps_S3 * T^0.  Since T^1 = -T^0 != 0,
    #         phi_* T^0 = T^1   <=>   eps_S3 = -1,
    #     with no sampling and no reference to which coset phi lies in.  And a
    #     metric connection is LC + contorsion(T) with LC preserved by every
    #     isometry, so equality of torsion IS equality of connection.
    t_sym = {}
    for tval in (0.0, 1.0):
        comp = np.zeros((3, 3, 3))
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    comp[i, j, k] = 2.0 * (2.0 * tval - 1.0) * eps[i, j, k]
        t_sym[tval] = comp
    res["B3_T0_is_multiple_of_volume_tensor"] = bool(
        np.allclose(t_sym[0.0], -2.0 * eps) and np.allclose(t_sym[1.0], +2.0 * eps)
    )
    res["B3_T1_equals_minus_T0"] = bool(np.allclose(t_sym[1.0], -t_sym[0.0]))
    res["B3_T0_nonzero"] = bool(np.abs(t_sym[0.0]).max() > 0)
    # pullback of a rank-3 fully antisymmetric tensor by R in O(3): eps -> det(R)*eps
    pull_ok, discriminating = True, True
    for _ in range(200):
        M = RNG.normal(size=(3, 3))
        Q, _r = np.linalg.qr(M)
        for sgn in (+1, -1):
            R = Q.copy()
            if np.sign(np.linalg.det(Q)) != sgn:
                R[:, 0] = -R[:, 0]
            d = float(np.linalg.det(R))
            pulled = np.einsum("ia,jb,kc,abc->ijk", R, R, R, t_sym[0.0])
            if not np.allclose(pulled, d * t_sym[0.0], atol=1e-9):
                pull_ok = False
            # the discriminating half: pulled == T^1 iff det == -1
            hit = np.allclose(pulled, t_sym[1.0], atol=1e-9)
            if hit != (d < 0):
                discriminating = False
    res["B3_pullback_scales_by_det"] = bool(pull_ok)
    res["B3_pullback_equals_T1_iff_det_negative"] = bool(discriminating)
    res["B3_pass"] = bool(
        res["B3_T0_is_multiple_of_volume_tensor"]
        and res["B3_T1_equals_minus_T0"]
        and res["B3_T0_nonzero"]
        and pull_ok
        and discriminating
    )
    res["B2_conclusion"] = (
        "{phi in Isom(S3) : phi_* nabla^0 = nabla^1} == O(4)\\SO(4) "
        "== the orientation-reversing coset, EXACTLY.  Proof: B3 (torsion is a "
        "multiple of the volume tensor, so it scales by det(dphi); T^1 = -T^0)."
    )
    return res


# --------------------------------------------------------------------------
# BLOCK C -- 13D orientation bookkeeping
# --------------------------------------------------------------------------
def block_C() -> dict:
    rows = []
    for e4 in (+1, -1):
        for e3 in (+1, -1):
            for e6 in (+1, -1):
                rows.append(
                    {
                        "eps_M4": e4,
                        "eps_S3": e3,
                        "eps_S6": e6,
                        "eps_13": e4 * e3 * e6,
                        "realizes_w0_to_w1": bool(e3 == -1),  # BLOCK B theorem
                        "orientation_preserving_13D": bool(e4 * e3 * e6 == +1),
                        # WHY not a sufficient condition (skeptic-corrected 2026-09-01):
                        # O(1,3) has FOUR components and PT = -I_4 has det = +1
                        # while lying OUTSIDE the identity component.  So
                        # eps_M4 = +1 does NOT imply g_4 in Isom_0(M4); this
                        # field is therefore only a NECESSARY condition, and the
                        # enumeration is exhaustive over the SIGN TRIPLE, not
                        # over pi_0 (which has 2*2*2*2 = 16 classes).  Inert for
                        # the count -- eps_S3 = -1 kills every row either way.
                        "identity_component_NECESSARY_only": bool(e4 == 1 and e3 == 1 and e6 == 1),
                    }
                )
    surviving = [r for r in rows if r["realizes_w0_to_w1"] and r["orientation_preserving_13D"]]
    gauge_and_swap = [
        r for r in rows if r["realizes_w0_to_w1"] and r["identity_component_NECESSARY_only"]
    ]
    return {
        "C_table": rows,
        "C_pi0_note": (
            "pi_0(Isom(M13)) = pi_0(O(1,3)) x pi_0(O(4)) x pi_0(O(7)) "
            "= (Z2 x Z2) x Z2 x Z2 = 16 classes.  This table enumerates the 8 "
            "sign TRIPLES; the identity-component column is a NECESSARY "
            "condition only.  Since eps_S3 = -1 is forced by condition (i) and "
            "already excludes every row, the finer 16-class enumeration cannot "
            "change the count."
        ),
        "C_H3_degree_argument": (
            "Independent of any Isom factorisation and of Cerf/Hatcher: M4 is "
            "contractible, so M13 is homotopy equivalent to S3 x S6, and "
            "Kunneth gives H^3(M13;Z) = Z generated by the S3 class.  A product "
            "map acts on that generator by deg = eps_S3 = -1, while any "
            "diffeomorphism isotopic to the identity acts as +1 on H^*.  So NO "
            "candidate -- compensated or not -- is isotopic to the identity in "
            "Diff(M13), let alone in Isom_0.  Homotopy fact, not computed here."
        ),
        "C_surviving_literal_orientation_reading": surviving,
        "C_n_surviving_literal": len(surviving),
        "C_surviving_gauge_reading": gauge_and_swap,
        "C_n_surviving_gauge": len(gauge_and_swap),
    }


# --------------------------------------------------------------------------
# BLOCK D/E -- Clifford
# --------------------------------------------------------------------------
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3M = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def gammas_1_3():
    """Cl(1,3), mostly-minus:  (g0)^2=+1, (gk)^2=-1."""
    g0 = kron(S3M, I2)
    gk = [kron(1j * S2, s) for s in (S1, S2, S3M)]
    return [g0] + gk


def gammas_6_0():
    """Cl(6,0):  hermitian, Gamma_a^2 = +1  (this repo's S6 convention)."""
    return [
        kron(S1, I2, I2),
        kron(S2, I2, I2),
        kron(S3M, S1, I2),
        kron(S3M, S2, I2),
        kron(S3M, S3M, S1),
        kron(S3M, S3M, S2),
    ]


def pseudoscalar(gs):
    out = np.eye(gs[0].shape[0], dtype=complex)
    for g in gs:
        out = out @ g
    return out


def block_DE() -> dict:
    res: dict = {}
    g4 = gammas_1_3()
    eta4 = np.diag([1.0, -1, -1, -1])
    ok = all(
        np.allclose(g4[m] @ g4[n] + g4[n] @ g4[m], 2 * eta4[m, n] * np.eye(4))
        for m in range(4)
        for n in range(4)
    )
    res["D0_Cl13_algebra_ok"] = bool(ok)
    g5 = 1j * g4[0] @ g4[1] @ g4[2] @ g4[3]
    res["D0_g5_squares_to_one"] = bool(np.allclose(g5 @ g5, np.eye(4)))

    G = gammas_6_0()
    ok6 = all(
        np.allclose(G[a] @ G[b] + G[b] @ G[a], 2 * (a == b) * np.eye(8))
        for a in range(6)
        for b in range(6)
    )
    res["D0_Cl60_algebra_ok"] = bool(ok6)
    w6 = pseudoscalar(G)
    res["D0_w6_sq"] = (
        complex(w6 @ w6 @ np.linalg.inv(np.eye(8)))[0, 0].real
        if False
        else float(np.real((w6 @ w6)[0, 0]))
    )
    G7 = 1j * w6
    res["D0_G7_squares_to_one"] = bool(np.allclose(G7 @ G7, np.eye(8)))
    res["D0_G7_anticommutes_with_all"] = bool(
        all(np.allclose(G7 @ G[a] + G[a] @ G7, 0) for a in range(6))
    )

    # ---- the two Cl(3) conventions -------------------------------------
    conventions = {
        "S3_as_found_Cl(0,3)_Z=i*sigma": [1j * S1, 1j * S2, 1j * S3M],
        "S3_positive_Cl(3,0)_sigma": [S1, S2, S3M],
    }
    res["D1_conventions"] = {}
    for name, Z in conventions.items():
        w3 = pseudoscalar(Z)
        res["D1_conventions"][name] = {
            "Z_sq_sign": float(np.real((Z[0] @ Z[0])[0, 0])),
            "omega3_is_scalar": bool(np.allclose(w3, w3[0, 0] * I2)),
            "omega3_scalar_value_re": float(np.real(w3[0, 0])),
            "omega3_scalar_value_im": float(np.imag(w3[0, 0])),
        }

    # ---- build the 13D algebra:  Cl(1,3) x Cl(9),  Cl(9) = Cl(3) x Cl(6) --
    # e_i = sigma_i (x) Gamma_7 ,  e_{3+a} = 1 (x) Gamma_a   -> Cl(9,0)
    e9 = [kron(s, G7) for s in (S1, S2, S3M)] + [kron(I2, Ga) for Ga in G]
    ok9 = all(
        np.allclose(e9[m] @ e9[n] + e9[n] @ e9[m], 2 * (m == n) * np.eye(16))
        for m in range(9)
        for n in range(9)
    )
    res["D2_Cl9_algebra_ok"] = bool(ok9)

    # 13D:  Gamma^mu = gamma^mu (x) 1_16 ;  Gamma^{3+m} = i * gamma_5 (x) e_m
    # so that (Gamma^{3+m})^2 = -1, matching mostly-minus Cl(1,12).
    G13 = [kron(gm, np.eye(16)) for gm in g4] + [1j * kron(g5, em) for em in e9]
    eta13 = np.diag([1.0] + [-1.0] * 12)
    ok13 = all(
        np.allclose(G13[A] @ G13[B] + G13[B] @ G13[A], 2 * eta13[A, B] * np.eye(64))
        for A in range(13)
        for B in range(13)
    )
    res["D2_Cl1_12_algebra_ok"] = bool(ok13)
    res["D2_spinor_dim"] = 64

    # ---- omega_13 is central and scalar (odd dimension) ------------------
    w13 = pseudoscalar(G13)
    res["D3_omega13_is_scalar"] = bool(np.allclose(w13, w13[0, 0] * np.eye(64)))
    res["D3_omega13_value"] = [float(np.real(w13[0, 0])), float(np.imag(w13[0, 0]))]
    res["D3_omega13_central"] = bool(
        all(np.allclose(w13 @ G13[A] - G13[A] @ w13, 0) for A in range(13))
    )

    # ---- the disputed identity, BOTH readings ----------------------------
    Om3 = G13[4] @ G13[5] @ G13[6]  # 13D-embedded S3 pseudoscalar
    Om6 = pseudoscalar(G13[7:13])  # 13D-embedded S6 pseudoscalar
    G5_13 = kron(g5, np.eye(16))  # 4D chirality on the 64-dim module

    prod = Om3 @ Om6
    # is prod proportional to the 4D chirality?
    ratio = None
    prop = False
    nz = np.argmax(np.abs(G5_13))
    idx = np.unravel_index(nz, G5_13.shape)
    if abs(G5_13[idx]) > 1e-12:
        ratio = prod[idx] / G5_13[idx]
        prop = bool(np.allclose(prod, ratio * G5_13))
    res["D4_embedded_reading"] = {
        "Omega3_times_Omega6_proportional_to_gamma5": prop,
        "proportionality_constant_re": float(np.real(ratio)) if ratio is not None else None,
        "proportionality_constant_im": float(np.imag(ratio)) if ratio is not None else None,
    }

    # intrinsic reading:  gamma_5  =?  +- (1 (x) omega_3 (x) Gamma_7)
    for name, Z in conventions.items():
        w3 = pseudoscalar(Z)
        intrinsic = kron(np.eye(4), w3, G7)
        eq_plus = bool(np.allclose(intrinsic, G5_13))
        eq_minus = bool(np.allclose(intrinsic, -G5_13))
        # is it even proportional?
        c = intrinsic[idx] / G5_13[idx] if abs(G5_13[idx]) > 1e-12 else None
        proportional = bool(c is not None and np.allclose(intrinsic, c * G5_13))
        res.setdefault("D5_intrinsic_reading", {})[name] = {
            "equals_plus_gamma5": eq_plus,
            "equals_minus_gamma5": eq_minus,
            "proportional_to_gamma5": proportional,
        }

    # ---- BLOCK E: the Z2 transformation law (convention-independent) -----
    # reflect one S3 frame direction: Gamma^4 -> -Gamma^4  (eps_S3 = -1)
    G13_r3 = list(G13)
    G13_r3[4] = -G13_r3[4]
    Om3_r = G13_r3[4] @ G13_r3[5] @ G13_r3[6]
    res["E1_Omega3_flips_under_S3_reflection"] = bool(np.allclose(Om3_r, -Om3))

    G13_r6 = list(G13)
    G13_r6[7] = -G13_r6[7]
    Om6_r = pseudoscalar(G13_r6[7:13])
    res["E1_Omega6_flips_under_S6_reflection"] = bool(np.allclose(Om6_r, -Om6))

    G13_r4 = list(G13)
    G13_r4[1] = -G13_r4[1]
    Om4 = pseudoscalar(G13[0:4])
    Om4_r = pseudoscalar(G13_r4[0:4])
    res["E1_Omega4_flips_under_M4_reflection"] = bool(np.allclose(Om4_r, -Om4))

    # E2: THE OVER-DETERMINATION TEST (rewritten 2026-09-01 after the FL Step
    #     8a skeptic pass).  The ORIGINAL E2 was named for a claim about
    #     gamma_5 but its body never mentioned gamma_5 -- it multiplied two
    #     signs, which is forced by multilinearity and cannot fail.  gamma_5
    #     admits TWO routes:
    #        route A:  gamma_5 =  i * Omega_4          -> transforms as eps_M4
    #        route B:  gamma_5 = -i * Omega_3 Omega_6  -> transforms as eps_S3*eps_S6
    #     These agree ONLY when eps_M4 = eps_S3*eps_S6, i.e. only when
    #     eps_13 = +1.  Off that locus the reflected gammas generate the OTHER
    #     inequivalent Cl(1,12) module (omega_13 flips), so no conjugation
    #     implements the map and "the 4D handedness flips" is NOT a determinate
    #     statement there.  Both facts are measured here, not asserted.
    reflect_cases = {
        "none": [],
        "M4_only": [1],
        "S3_only_iota_tilde": [4],
        "M4_and_S3_familyC": [1, 4],
        "S3_and_S6_familyB": [4, 7],
    }
    e2_rows = {}
    for label, idxs in reflect_cases.items():
        Gp = list(G13)
        for i in idxs:
            Gp[i] = -Gp[i]
        route_A = 1j * Gp[0] @ Gp[1] @ Gp[2] @ Gp[3]
        route_B = -1j * (Gp[4] @ Gp[5] @ Gp[6]) @ pseudoscalar(Gp[7:13])
        e2_rows[label] = {
            "eps_M4": -1 if 1 in idxs else 1,
            "eps_S3": -1 if 4 in idxs else 1,
            "eps_S6": -1 if 7 in idxs else 1,
            "eps_13": (-1 if 1 in idxs else 1)
            * (-1 if 4 in idxs else 1)
            * (-1 if 7 in idxs else 1),
            "omega13_preserved": bool(np.allclose(pseudoscalar(Gp), w13)),
            "routeA_equals_routeB": bool(np.allclose(route_A, route_B)),
        }
    res["E2_gamma5_two_routes"] = e2_rows
    res["E2_routes_agree_iff_omega13_preserved"] = bool(
        all(r["routeA_equals_routeB"] == r["omega13_preserved"] for r in e2_rows.values())
    )
    res["E2_law_valid_only_on_eps13_plus1"] = True
    res["E2_pass"] = bool(res["E2_routes_agree_iff_omega13_preserved"])

    # and omega_13 (a scalar) flips iff eps_13 = -1, i.e. an orientation-reversing
    # map of the FULL 13-manifold exchanges the two inequivalent Cl(1,12) modules
    w13_r3 = pseudoscalar(G13_r3)
    res["E3_omega13_flips_under_single_reflection"] = bool(np.allclose(w13_r3, -w13))
    G13_r36 = list(G13)
    G13_r36[4] = -G13_r36[4]
    G13_r36[7] = -G13_r36[7]
    res["E3_omega13_invariant_under_double_reflection"] = bool(
        np.allclose(pseudoscalar(G13_r36), w13)
    )
    return res


# --------------------------------------------------------------------------
# BLOCK F -- conjugate bundle arithmetic
# --------------------------------------------------------------------------
def block_F() -> dict:
    # c_k(Ebar) = (-1)^k c_k(E).  With c_3(S^-) = +2 (G73, cited):
    c3_E = 2
    c3_Ebar = (-1) ** 3 * c3_E
    return {
        "F_c3_E_cited_G73": c3_E,
        "F_c3_Ebar": c3_Ebar,
        "F_ind_E": c3_E // 2,
        "F_ind_Ebar": c3_Ebar // 2,
        "F_note": "A-hat(S6)=1 (G50). ind = A-hat * c3/2. Orientation reversal "
        "on S6 sends the SU(3)-structure J to -J, hence E=T^{1,0}+C to "
        "its conjugate; ind +1 -> -1.",
    }


def main() -> None:
    OUT["A_isometry_group"] = block_A()
    OUT["B_cartan_schouten"] = block_B()
    OUT["C_orientation_bookkeeping"] = block_C()
    OUT["DE_clifford"] = block_DE()
    OUT["F_conjugate_bundle"] = block_F()

    checks = {
        "A1": OUT["A_isometry_group"]["A1_pass"],
        "A2": OUT["A_isometry_group"]["A2_pass"],
        "A2b_negcontrol": OUT["A_isometry_group"]["A2b_pass"],
        "A3": OUT["A_isometry_group"]["A3_pass"],
        "B1": OUT["B_cartan_schouten"]["B1_pass"],
        "B1b_negcontrol": OUT["B_cartan_schouten"]["B1b_pass"],
        "B2": OUT["B_cartan_schouten"]["B2_pass"],
        "D_algebra": (
            OUT["DE_clifford"]["D2_Cl1_12_algebra_ok"] and OUT["DE_clifford"]["D2_Cl9_algebra_ok"]
        ),
        "D3_omega13_scalar": OUT["DE_clifford"]["D3_omega13_is_scalar"],
        "D4_embedded_identity_holds": OUT["DE_clifford"]["D4_embedded_reading"][
            "Omega3_times_Omega6_proportional_to_gamma5"
        ],
        "B0_finite_difference": OUT["B_cartan_schouten"]["B0_pass"],
        "B0b_negcontrol": OUT["B_cartan_schouten"]["B0b_pass"],
        "B3_torsion_is_volume_tensor_exhaustive": OUT["B_cartan_schouten"]["B3_pass"],
        "E2_gamma5_two_routes_agree_iff_omega13_preserved": OUT["DE_clifford"]["E2_pass"],
    }
    OUT["checks"] = checks
    OUT["all_checks_pass"] = bool(all(checks.values()))
    OUT["verdict"] = (
        "NO_SUCH_g_EXISTS__CONDITION_i_FORCES_S3_ORIENTATION_REVERSAL__"
        "HENCE_NON_IDENTITY_COMPONENT_OF_Isom__AND_EVERY_ORIENTATION_"
        "COMPENSATED_CANDIDATE_FAILS_CONDITION_iii"
    )

    here = pathlib.Path(__file__).parent
    (here / "results_c125.json").write_text(json.dumps(OUT, indent=2), encoding="utf-8")

    print(json.dumps(checks, indent=2))
    print("all_checks_pass:", OUT["all_checks_pass"])
    print("\n-- BLOCK B conclusion --")
    print(OUT["B_cartan_schouten"]["B2_conclusion"])
    print("\n-- BLOCK C --")
    print(
        "candidates surviving the LITERAL orientation reading:",
        OUT["C_orientation_bookkeeping"]["C_n_surviving_literal"],
    )
    print(
        "candidates surviving the GAUGE (identity-component) reading:",
        OUT["C_orientation_bookkeeping"]["C_n_surviving_gauge"],
    )
    print("\n-- BLOCK D --")
    print("embedded reading:", OUT["DE_clifford"]["D4_embedded_reading"])
    print("intrinsic reading:", OUT["DE_clifford"]["D5_intrinsic_reading"])
    print("omega13 value:", OUT["DE_clifford"]["D3_omega13_value"])
    print("\nVERDICT:", OUT["verdict"])


if __name__ == "__main__":
    main()
