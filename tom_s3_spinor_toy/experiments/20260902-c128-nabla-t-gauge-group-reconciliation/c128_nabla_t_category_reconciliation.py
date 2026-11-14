"""C128 -- which mathematical category is `nabla^t`?

Reconciles C125 (metric AFFINE connection on the soldered frame bundle of S^3)
with C126 (Yang-Mills SO(3) connection, an abstract so(3)-valued 1-form).

The Zero-Signal-Gate predicate this script answers numerically:

    Is C126's winding-(-1) large gauge transformation  g = Ad : S^3 -> SO(3)
    realizable as `df` for a diffeomorphism f of S^3 ?

The answer is obtained by CLASSIFYING the frame-transition function

    M_f(x)  defined by   df_x( X_j(x) )  =  M_f(x)^i_j  X_i( f(x) )

over Isom(S^3) = O(4), where {X_i} is the left-invariant orthonormal frame.

METHODOLOGICAL NOTE (deliberate, not incidental).  Every M_f below is obtained
by CENTRAL FINITE DIFFERENCES of the actual map f on the group -- never by
re-expanding the closed form it is then compared against.  The C125 FL Step 8a
skeptic pass caught exactly that defect in that round's B1 (and partially B3):
a check that constructs its own expected value from the same symbol it then
verifies cannot fail.  Every check here carries a negative control that is
reported alongside it, and several of them are designed to fail if a sign,
an index order, or a convention is wrong.

Conventions (C126's, so the comparison is like-for-like):
    T_a = -i sigma_a / 2 ,  [T_i,T_j] = eps_ijk T_k
    X_i(x) = x T_i        (left-invariant),   [X_i,X_j] = eps_ijk X_k
    Y_i(x) = T_i x        (right-invariant),  [Y_i,Y_j] = -eps_ijk Y_k
    <A,B> := -2 tr(AB)    (so <T_i,T_j> = delta_ij ; {X_i} orthonormal)
    Ad(x)_{ij} defined by  x T_j x^{-1} = Ad(x)_{ij} T_i
    nabla^t_{X_i} X_j = t eps_ijk X_k , i.e. A^t_i = t ad(T_i)

Run:  python c128_nabla_t_category_reconciliation.py
"""

from __future__ import annotations

import json
import pathlib

import numpy as np

RNG = np.random.default_rng(20260902)
HERE = pathlib.Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# PART 0 -- su(2)/SU(2) machinery, with its own self-tests
# --------------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
SIGMA = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
T = [-0.5j * s for s in SIGMA]

EPS = np.zeros((3, 3, 3))
for _i, _j, _k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    EPS[_i, _j, _k] = 1.0
    EPS[_j, _i, _k] = -1.0

# ad(T_i) as a 3x3 real matrix on coefficient vectors: (ad T_i)^k_j = eps_ijk
AD_T = [
    np.array([[EPS[i, j, k] for j in range(3)] for k in range(3)]) for i in range(3)
]


def ip(a: np.ndarray, b: np.ndarray) -> float:
    """<A,B> = -2 tr(AB); real on su(2)."""
    return float(np.real(-2.0 * np.trace(a @ b)))


def coeffs(v: np.ndarray) -> np.ndarray:
    """Coefficient vector of v in su(2) w.r.t. {T_a}."""
    return np.array([ip(T[a], v) for a in range(3)])


def su2_exp(vec: np.ndarray) -> np.ndarray:
    """exp(sum_a vec[a] T_a)."""
    n = float(np.linalg.norm(vec))
    if n < 1e-15:
        return I2.copy()
    v = sum(vec[a] * T[a] for a in range(3))
    return np.cos(n / 2) * I2 + (2 * np.sin(n / 2) / n) * v


def rand_su2(rng: np.random.Generator) -> np.ndarray:
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return q[0] * I2 + 2 * (q[1] * T[0] + q[2] * T[1] + q[3] * T[2])


def inv(x: np.ndarray) -> np.ndarray:
    return x.conj().T


def Ad(x: np.ndarray) -> np.ndarray:
    """Ad(x)_{ij} : x T_j x^{-1} = Ad(x)_{ij} T_i."""
    out = np.zeros((3, 3))
    xi = inv(x)
    for j in range(3):
        out[:, j] = coeffs(x @ T[j] @ xi)
    return out


def _p0_self_tests() -> dict:
    res = {}
    # bracket law, with wrong-sign negative control
    err, ctrl = 0.0, 0.0
    for i in range(3):
        for j in range(3):
            br = T[i] @ T[j] - T[j] @ T[i]
            tgt = sum(EPS[i, j, k] * T[k] for k in range(3))
            err = max(err, float(np.max(np.abs(br - tgt))))
            ctrl = max(ctrl, float(np.max(np.abs(br + tgt))))
    res["bracket_err"] = err
    res["bracket_wrong_sign_control"] = ctrl
    res["bracket_ok"] = bool(err < 1e-13 and ctrl > 0.4)

    # inner-product normalisation <T_i,T_j> = delta_ij
    gram = np.array([[ip(T[i], T[j]) for j in range(3)] for i in range(3)])
    res["gram_err"] = float(np.max(np.abs(gram - np.eye(3))))

    # Ad in SO(3), with a random-matrix negative control
    o_err, d_err = 0.0, 0.0
    for _ in range(200):
        x = rand_su2(RNG)
        a = Ad(x)
        o_err = max(o_err, float(np.max(np.abs(a.T @ a - np.eye(3)))))
        d_err = max(d_err, abs(np.linalg.det(a) - 1.0))
    fake = RNG.normal(size=(3, 3))
    res["Ad_orthogonality_err"] = o_err
    res["Ad_det_minus_one_err"] = d_err
    res["Ad_control_random_matrix_orth_err"] = float(
        np.max(np.abs(fake.T @ fake - np.eye(3)))
    )
    res["Ad_ok"] = bool(o_err < 1e-12 and d_err < 1e-12)

    # ad(T_i) really is the adjoint action in coefficients
    ad_err = 0.0
    for i in range(3):
        for j in range(3):
            br = coeffs(T[i] @ T[j] - T[j] @ T[i])
            ad_err = max(ad_err, float(np.max(np.abs(AD_T[i][:, j] - br))))
    res["ad_matrix_err"] = ad_err
    return res


# --------------------------------------------------------------------------
# PART 1 -- the frame-transition function M_f, by FINITE DIFFERENCES
# --------------------------------------------------------------------------


def frame_transition(f, x: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """M_f(x)_{ij} from df_x(X_j(x)) = M_f(x)_{ij} X_i(f(x)).

    Central finite difference of the ACTUAL map f along the group curve
    s -> x exp(s T_j).  No closed form for f is used anywhere.
    """
    fx = f(x)
    fxi = inv(fx)
    out = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3)
        e[j] = h
        dv = (f(x @ su2_exp(e)) - f(x @ su2_exp(-e))) / (2 * h)
        out[:, j] = coeffs(fxi @ dv)
    return out


def iota(x: np.ndarray) -> np.ndarray:
    return inv(x)


def make_fab(a: np.ndarray, b: np.ndarray):
    bi = inv(b)

    def f(x: np.ndarray) -> np.ndarray:
        return a @ x @ bi

    return f


def make_fab_iota(a: np.ndarray, b: np.ndarray):
    bi = inv(b)

    def f(x: np.ndarray) -> np.ndarray:
        return a @ inv(x) @ bi

    return f


def make_nonisometric(lam: float):
    """f(x) = x exp(phi(x) T_3), phi(x) = lam * Re tr(x)/2.

    A C^1-small perturbation of the identity for small lam, hence a
    diffeomorphism; it is NOT an isometry of the bi-invariant metric.
    """

    def f(x: np.ndarray) -> np.ndarray:
        phi = lam * float(np.real(np.trace(x))) / 2.0
        return x @ su2_exp(np.array([0.0, 0.0, phi]))

    return f


def _p1_frame_transitions() -> dict:
    res = {}

    # (C1) M_iota(x) = -Ad(x), with the +Ad(x) negative control
    err, ctrl = 0.0, np.inf
    for _ in range(200):
        x = rand_su2(RNG)
        m = frame_transition(iota, x)
        err = max(err, float(np.max(np.abs(m + Ad(x)))))
        ctrl = min(ctrl, float(np.max(np.abs(m - Ad(x)))))
    res["C1_M_iota_equals_minus_Ad_err"] = err
    res["C1_control_vs_plus_Ad_min_dev"] = float(ctrl)
    res["C1_ok"] = bool(err < 1e-8 and ctrl > 0.5)

    # (C2) M_{f_{a,b}} = Ad(b), constant in x; control: compare against Ad(a)
    # WHY the control statistic is a MEDIAN, not a MIN: Ad(a) and Ad(b) coincide
    # exactly when a = +-b, and are close whenever a is close to +-b, which
    # happens for some fraction of random draws BY CONSTRUCTION.  A min over
    # draws therefore measures how unlucky the draw was, not how discriminating
    # the check is.  Both statistics are reported; only the median is gated.
    err, spread_so4 = 0.0, 0.0
    ctrl_vals = []
    for _ in range(60):
        a, b = rand_su2(RNG), rand_su2(RNG)
        f = make_fab(a, b)
        ms = [frame_transition(f, rand_su2(RNG)) for _ in range(6)]
        for m in ms:
            err = max(err, float(np.max(np.abs(m - Ad(b)))))
            ctrl_vals.append(float(np.max(np.abs(m - Ad(a)))))
        stack = np.stack(ms)
        spread_so4 = max(spread_so4, float(np.max(stack.max(0) - stack.min(0))))
    res["C2_M_fab_equals_Ad_b_err"] = err
    res["C2_control_vs_Ad_a_median_dev"] = float(np.median(ctrl_vals))
    res["C2_control_vs_Ad_a_min_dev"] = float(np.min(ctrl_vals))
    res["C2_max_spread_over_x_SO4"] = spread_so4
    res["C2_ok"] = bool(
        err < 1e-8 and float(np.median(ctrl_vals)) > 0.3 and spread_so4 < 1e-8
    )

    # (C3) M_{f_{a,b} o iota}(x) = -Ad(b x); control: -Ad(x b).
    # Same median-vs-min point as C2: Ad(bx) = Ad(xb) exactly when [b,x] = 0,
    # so a min over random draws is dominated by near-commuting pairs and is
    # NOT a measure of the check's discriminating power.
    err, spread_rev = 0.0, np.inf
    ctrl_vals = []
    for _ in range(60):
        a, b = rand_su2(RNG), rand_su2(RNG)
        f = make_fab_iota(a, b)
        ms = []
        for _ in range(6):
            x = rand_su2(RNG)
            m = frame_transition(f, x)
            ms.append(m)
            err = max(err, float(np.max(np.abs(m + Ad(b @ x)))))
            ctrl_vals.append(float(np.max(np.abs(m + Ad(x @ b)))))
        stack = np.stack(ms)
        spread_rev = min(spread_rev, float(np.max(stack.max(0) - stack.min(0))))
    res["C3_M_fab_iota_equals_minus_Ad_bx_err"] = err
    res["C3_control_vs_minus_Ad_xb_median_dev"] = float(np.median(ctrl_vals))
    res["C3_control_vs_minus_Ad_xb_min_dev"] = float(np.min(ctrl_vals))
    res["C3_min_spread_over_x_reversing_coset"] = float(spread_rev)
    res["C3_ok"] = bool(
        err < 1e-8 and float(np.median(ctrl_vals)) > 0.3 and spread_rev > 0.3
    )
    return res


# --------------------------------------------------------------------------
# PART 2 -- the det <-> winding LOCK on the geometric image
# --------------------------------------------------------------------------


def _p2_lock(n_maps: int = 500, n_pts: int = 12) -> dict:
    """Over random isometries of BOTH cosets, record (sign det M_f, is M_f constant).

    WHAT THIS CAN AND CANNOT SHOW -- corrected after BOTH FL Step 8a skeptic
    passes independently made the same point.  The draws come from exactly the
    two parametric families already solved in closed form by C1/C2/C3, chosen
    by `k % 2`, so the 250/250 split is BY CONSTRUCTION and the sample cannot
    contain a third family.  This is therefore a CONSISTENCY RE-RUN of the
    closed forms at random points -- it confirms no drift in det or in
    constancy -- and NOT a completeness test of the classification.
    Completeness is inherited from the [CITED] enumeration
    O(4) = SO(4) u SO(4).iota, which is not tested here.
    """
    table = {"pp_const": 0, "pp_nonconst": 0, "mm_const": 0, "mm_nonconst": 0}
    dets, spreads = [], []
    for k in range(n_maps):
        a, b = rand_su2(RNG), rand_su2(RNG)
        f = make_fab(a, b) if k % 2 == 0 else make_fab_iota(a, b)
        ms = np.stack([frame_transition(f, rand_su2(RNG)) for _ in range(n_pts)])
        d = float(np.mean([np.linalg.det(m) for m in ms]))
        spread = float(np.max(ms.max(0) - ms.min(0)))
        dets.append(d)
        spreads.append(spread)
        const = spread < 1e-7
        if d > 0:
            table["pp_const" if const else "pp_nonconst"] += 1
        else:
            table["mm_const" if const else "mm_nonconst"] += 1
    return {
        "P2_counts": table,
        "P2_det_abs_dev_from_one": float(np.max(np.abs(np.abs(dets) - 1.0))),
        "P2_min_spread_nonconstant_branch": float(
            min(s for s, d in zip(spreads, dets) if d < 0)
        ),
        "P2_max_spread_constant_branch": float(
            max(s for s, d in zip(spreads, dets) if d > 0)
        ),
        # RENAMED from P2_lock_holds to P2_ok: the gate collects keys ending in
        # "_ok", so under the old name THE HEADLINE LOCK WAS NOT GATED AT ALL --
        # it could have broken while the script still printed ALL_OK = True.
        # Caught independently by both FL Step 8a skeptic passes.
        "P2_ok": bool(table["pp_nonconst"] == 0 and table["mm_const"] == 0),
    }


# --------------------------------------------------------------------------
# PART 3 -- "M_f is O(3)-valued  =>  f is an isometry", with a falsifier
# --------------------------------------------------------------------------


def _p3_orthogonality_lemma() -> dict:
    res = {}
    # isometries: M^T M = I
    err = 0.0
    for k in range(80):
        a, b = rand_su2(RNG), rand_su2(RNG)
        f = make_fab(a, b) if k % 2 == 0 else make_fab_iota(a, b)
        m = frame_transition(f, rand_su2(RNG))
        err = max(err, float(np.max(np.abs(m.T @ m - np.eye(3)))))
    res["P3_isometry_MtM_minus_I_err"] = err

    # FALSIFIER: a genuine non-isometric diffeomorphism must break orthogonality
    worst = {}
    for lam in (0.05, 0.2, 0.5):
        f = make_nonisometric(lam)
        dev, dets = 0.0, []
        for _ in range(60):
            m = frame_transition(f, rand_su2(RNG))
            dev = max(dev, float(np.max(np.abs(m.T @ m - np.eye(3)))))
            dets.append(float(np.linalg.det(m)))
        worst[f"lam_{lam}"] = {
            "max_MtM_minus_I": dev,
            "det_range": [min(dets), max(dets)],
        }
    res["P3_nonisometric_falsifier"] = worst
    res["P3_ok"] = bool(err < 1e-8 and worst["lam_0.05"]["max_MtM_minus_I"] > 1e-3)
    return res


# --------------------------------------------------------------------------
# PART 4 -- C126's gauge transformation, reproduced independently
# --------------------------------------------------------------------------


def _p4_c126_gauge() -> dict:
    res = {}
    # (C6) Ad(x)^{-1} X_i(Ad)(x) = ad(T_i), finite differences; wrong-sign control
    h = 1e-5
    err, ctrl = 0.0, np.inf
    for _ in range(200):
        x = rand_su2(RNG)
        ai = np.linalg.inv(Ad(x))
        for i in range(3):
            e = np.zeros(3)
            e[i] = h
            d = (Ad(x @ su2_exp(e)) - Ad(x @ su2_exp(-e))) / (2 * h)
            got = ai @ d
            err = max(err, float(np.max(np.abs(got - AD_T[i]))))
            ctrl = min(ctrl, float(np.max(np.abs(got + AD_T[i]))))
    res["C6_Adinv_dAd_equals_ad_T_err"] = err
    res["C6_control_wrong_sign_min_dev"] = float(ctrl)
    res["C6_ok"] = bool(err < 1e-7 and ctrl > 0.5)

    # (C7) det Ad = +1 everywhere: C126's g is det-preserving, unlike M_iota
    d_g = [float(np.linalg.det(Ad(rand_su2(RNG)))) for _ in range(200)]
    d_m = [
        float(np.linalg.det(frame_transition(iota, rand_su2(RNG)))) for _ in range(50)
    ]
    res["C7_det_g_range"] = [min(d_g), max(d_g)]
    res["C7_det_M_iota_range"] = [min(d_m), max(d_m)]

    # (C8) M_iota = (-I) . g exactly -- the factorisation, checked pointwise
    fac = 0.0
    for _ in range(200):
        x = rand_su2(RNG)
        fac = max(
            fac,
            float(np.max(np.abs(frame_transition(iota, x) - (-np.eye(3)) @ Ad(x)))),
        )
    res["C8_M_iota_equals_minusI_times_g_err"] = fac

    # (C9) winding algebra: sum_ijk eps_ijk tr(T_i T_j T_k) = -3/2 (C126 PART 6b)
    s = sum(
        EPS[i, j, k] * np.trace(T[i] @ T[j] @ T[k])
        for i in range(3)
        for j in range(3)
        for k in range(3)
    )
    res["C9_eps_tr_TTT"] = [float(np.real(s)), float(np.imag(s))]
    # K = 1/4 for the bi-invariant metric with |[X_1,X_2]| = 1  =>  R = 2, Vol = 16 pi^2
    k_sec = 0.25 * float(np.linalg.norm(coeffs(T[0] @ T[1] - T[1] @ T[0]))) ** 2
    radius = 1.0 / np.sqrt(k_sec)
    vol = 2 * np.pi**2 * radius**3
    res["C9_sectional_curvature"] = k_sec
    res["C9_radius"] = radius
    res["C9_volume_over_pi2"] = vol / np.pi**2
    res["C9_winding_n"] = float(np.real(s)) * vol / (24 * np.pi**2)
    res["C9_ok"] = bool(abs(res["C9_winding_n"] + 1.0) < 1e-12)
    return res


# --------------------------------------------------------------------------
# PART 5 -- the gauge transformation MOVES the vielbein
# --------------------------------------------------------------------------


def _p5_vielbein_moves() -> dict:
    """Gauge-rotated frame  e~_j = Ad(x)^k_j X_k(x)  =  x^2 T_j x^{-1}."""
    res = {}
    form_err, diff, orth = 0.0, [], 0.0
    for _ in range(200):
        x = rand_su2(RNG)
        a = Ad(x)
        for j in range(3):
            et = sum(a[k, j] * (x @ T[k]) for k in range(3))
            form_err = max(form_err, float(np.max(np.abs(et - x @ x @ T[j] @ inv(x)))))
            diff.append(float(np.max(np.abs(et - x @ T[j]))))
        # e~ is still orthonormal (Ad in SO(3))
        gram = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                ei = inv(x) @ sum(a[k, i] * (x @ T[k]) for k in range(3))
                ej = inv(x) @ sum(a[k, j] * (x @ T[k]) for k in range(3))
                gram[i, j] = ip(ei, ej)
        orth = max(orth, float(np.max(np.abs(gram - np.eye(3)))))
    res["P5_etilde_closed_form_err"] = form_err
    res["P5_etilde_minus_e_median"] = float(np.median(diff))

    # WHY THIS WAS REWRITTEN: the previous version of the next check read
    #     max_j | sum_k eye(3)[k,j] T_k  -  T_j |
    # which is identically |T_j - T_j| = 0.  It contained no x, no Ad, and no
    # e~ construction whatsoever, so it was 0.0 for ANY implementation -- a
    # tautology of exactly the species this module's own docstring says it was
    # written to avoid, and the same shape as the B1 defect C125's second
    # skeptic pass caught.  BOTH FL Step 8a skeptic passes flagged it
    # independently.  It is now evaluated THROUGH the real machinery at the two
    # central points, and paired with a nearby NON-central point so the pair
    # discriminates: central must give 0, non-central must not.
    def etilde_minus_e(x: np.ndarray) -> float:
        a = Ad(x)
        return float(
            max(
                np.max(np.abs(sum(a[k, j] * (x @ T[k]) for k in range(3)) - x @ T[j]))
                for j in range(3)
            )
        )

    res["P5_etilde_minus_e_at_center_plus"] = etilde_minus_e(I2)
    res["P5_etilde_minus_e_at_center_minus"] = etilde_minus_e(-I2)
    res["P5_etilde_minus_e_near_center_control"] = float(
        min(
            etilde_minus_e(su2_exp(np.array([eta, 0.0, 0.0])))
            for eta in (0.2, 0.5, 1.0)
        )
    )
    res["P5_center_test_discriminates"] = bool(
        max(
            res["P5_etilde_minus_e_at_center_plus"],
            res["P5_etilde_minus_e_at_center_minus"],
        )
        < 1e-14
        and res["P5_etilde_minus_e_near_center_control"] > 1e-2
    )
    res["P5_etilde_orthonormality_err"] = orth
    res["P5_ok"] = bool(
        form_err < 1e-12
        and float(np.median(diff)) > 0.1
        and orth < 1e-12
        and res["P5_center_test_discriminates"]
    )
    return res


# --------------------------------------------------------------------------
# PART 6 -- eps is SO(3)-invariant: no local Lorentz rotation flips the torsion
# --------------------------------------------------------------------------


def _p6_eps_character() -> dict:
    """Torsion components T^t_{ij}{}^k = (2t-1) eps_ijk.

    Under a frame rotation R the components go to det(R) eps.  So a
    det=+1 (local Lorentz / small OR large gauge) rotation cannot send
    T^0 = -eps to T^1 = +eps; only a det=-1 one can.
    """
    res = {}

    def rot_eps(r: np.ndarray) -> np.ndarray:
        out = np.einsum("ia,jb,kc,ijk->abc", r, r, np.linalg.inv(r).T, EPS)
        return out

    plus, minus = [], []
    for _ in range(200):
        r = Ad(rand_su2(RNG))  # generic SO(3)
        plus.append(float(np.max(np.abs(rot_eps(r) - EPS))))
        rm = -r  # generic O(3) minus-coset element
        minus.append(float(np.max(np.abs(rot_eps(rm) + EPS))))
    res["P6_SO3_leaves_eps_fixed_err"] = float(max(plus))
    res["P6_O3minus_sends_eps_to_minus_eps_err"] = float(max(minus))
    res["P6_control_SO3_vs_minus_eps_min_dev"] = float(
        min(float(np.max(np.abs(rot_eps(Ad(rand_su2(RNG))) + EPS))) for _ in range(50))
    )
    res["P6_ok"] = bool(max(plus) < 1e-10 and max(minus) < 1e-10)
    return res


# --------------------------------------------------------------------------
# PART 7 -- NEW THEOREM: any diffeomorphism carrying nabla^0 to nabla^1 is an
#           orientation-reversing ISOMETRY (no Cerf/Hatcher, no (0a) needed)
# --------------------------------------------------------------------------


def _p7_parallel_frames() -> dict:
    """Structure constants of the two parallel frames, by finite differences,
    plus a numerical root-find of the constraint the transition matrix c obeys.
    """
    res = {}
    h = 1e-5

    def lie_bracket(u, v, x):
        """[U,V](x) for ambient-matrix-valued vector fields on SU(2)."""

        def dirderiv(field, w, at):
            a = coeffs(inv(at) @ w)
            return (field(at @ su2_exp(h * a)) - field(at @ su2_exp(-h * a))) / (2 * h)

        return dirderiv(v, u(x), x) - dirderiv(u, v(x), x)

    def X(i):
        return lambda x: x @ T[i]

    def Y(i):
        return lambda x: T[i] @ x

    ex, ey = 0.0, 0.0
    for _ in range(50):
        x = rand_su2(RNG)
        for i in range(3):
            for j in range(3):
                bx = coeffs(inv(x) @ lie_bracket(X(i), X(j), x))
                by = coeffs(lie_bracket(Y(i), Y(j), x) @ inv(x))
                ex = max(ex, float(np.max(np.abs(bx - EPS[i, j]))))
                ey = max(ey, float(np.max(np.abs(by + EPS[i, j]))))
    res["P7_left_structure_constants_plus_eps_err"] = ex
    res["P7_right_structure_constants_minus_eps_err"] = ey

    # nabla^1 makes the RIGHT-invariant frame parallel:
    # Y_j = Ad(x^{-1})^k_j X_k , and  X_i(Ad^{-1}) + Ad^{-1} composed with A^1 cancels.
    par = 0.0
    for _ in range(100):
        x = rand_su2(RNG)
        c = Ad(inv(x))
        for i in range(3):
            e = np.zeros(3)
            e[i] = h
            dc = (Ad(inv(x @ su2_exp(e))) - Ad(inv(x @ su2_exp(-e)))) / (2 * h)
            par = max(par, float(np.max(np.abs(dc + AD_T[i] @ c))))
    # d/dX_i c = -ad(T_i) c   <=>   nabla^1_{X_i} Y_j = (dc + A^1_i c)_{kj} X_k = 0
    res["P7_nabla1_right_frame_parallel_err"] = par

    # The constraint on the constant transition matrix c:  phi_* X_i = c_{ai} Y_a
    #   -eps_abm c_ai c_bj  =  eps_ijk c_mk        (for all i,j,m)
    def residual(cv: np.ndarray) -> np.ndarray:
        c = cv.reshape(3, 3)
        lhs = -np.einsum("abm,ai,bj->ijm", EPS, c, c)
        rhs = np.einsum("ijk,mk->ijm", EPS, c)
        return (lhs - rhs).ravel()

    def gauss_newton(c0: np.ndarray, iters: int = 200) -> np.ndarray:
        c = c0.copy()
        for _ in range(iters):
            r = residual(c)
            if np.linalg.norm(r) < 1e-13:
                break
            jac = np.zeros((r.size, 9))
            for k in range(9):
                d = np.zeros(9)
                d[k] = 1e-6
                jac[:, k] = (residual(c + d) - residual(c - d)) / 2e-6
            step, *_ = np.linalg.lstsq(jac, -r, rcond=None)
            c = c + step
        return c

    sols, bad = [], 0
    for _ in range(200):
        c = gauss_newton(RNG.normal(size=9))
        if np.linalg.norm(residual(c)) > 1e-9:
            continue
        cm = c.reshape(3, 3)
        if abs(np.linalg.det(cm)) < 0.1:  # discard the degenerate c = 0 root
            continue
        sols.append(cm)
        if np.max(np.abs(cm.T @ cm - np.eye(3))) > 1e-6 or np.linalg.det(cm) > 0:
            bad += 1
    res["P7_rootfind_n_nondegenerate_solutions"] = len(sols)
    res["P7_rootfind_n_violating_O3minus"] = bad
    res["P7_rootfind_det_range"] = (
        [
            float(min(np.linalg.det(c) for c in sols)),
            float(max(np.linalg.det(c) for c in sols)),
        ]
        if sols
        else []
    )
    res["P7_rootfind_max_orthogonality_dev"] = (
        float(max(np.max(np.abs(c.T @ c - np.eye(3))) for c in sols)) if sols else None
    )
    # named checks: c = -I solves it, c = +I does NOT (identity does not swap)
    res["P7_c_minus_I_residual"] = float(np.linalg.norm(residual(-np.eye(3).ravel())))
    res["P7_c_plus_I_residual"] = float(np.linalg.norm(residual(np.eye(3).ravel())))
    # and iota realises c = -I:  iota_* X_i = -Y_i
    err = 0.0
    for _ in range(100):
        x = rand_su2(RNG)
        for i in range(3):
            e = np.zeros(3)
            e[i] = h
            dv = (iota(x @ su2_exp(e)) - iota(x @ su2_exp(-e))) / (2 * h)
            err = max(err, float(np.max(np.abs(dv + T[i] @ inv(x)))))
    res["P7_iota_pushforward_X_equals_minus_Y_err"] = err
    res["P7_ok"] = bool(
        ex < 1e-7
        and ey < 1e-7
        and par < 1e-7
        and len(sols) > 20
        and bad == 0
        and res["P7_c_minus_I_residual"] < 1e-12
        and res["P7_c_plus_I_residual"] > 1.0
        and err < 1e-8
    )
    return res


# --------------------------------------------------------------------------
# PART 8 -- the MINIMAL-HYPOTHESIS route:  det M_f = -1 with no use of O(4)
# --------------------------------------------------------------------------


def _p8_minimal_route() -> dict:
    """M_f(x) = Ad(f(x)^{-1}) . c   whenever  f_* X_i = c_{ai} Y_a .

    WHY this matters: combined with PART 7's theorem (c is forced into O(3)^-),
    it gives  det M_f = det(Ad) det(c) = -1  for EVERY diffeomorphism carrying
    nabla^0 to nabla^1, using only (i) parallel frames of a flat connection on a
    simply-connected base differ by a constant, (ii) the structure-constant
    equation, and (iii) Y_a(y) = Ad(y^{-1})_{ka} X_k(y).  It uses NO knowledge
    of Isom(S^3) = O(4), no Cerf/Hatcher, no de Rham splitting, no H^3 degree
    argument, and no torsion-equals-volume-tensor identity.  C126's g = Ad has
    det = +1 pointwise, so it is excluded by this alone.
    """
    res = {}
    h = 1e-5

    # (a) Y_a(y) = Ad(y^{-1})_{ka} X_k(y), with a wrong-inverse negative control.
    # WHY the control statistic is a MEDIAN, not a MIN (third instance of the
    # same point in this file, and it is a real methodological trap): Ad(y) and
    # Ad(y^{-1}) = Ad(y)^T coincide exactly whenever Ad(y) is symmetric, i.e.
    # y near-central or a pi-rotation.  Those draws occur with positive
    # probability, so a MIN over draws measures how unlucky the sample was, not
    # whether the check discriminates.  Both are reported; only the median gates.
    err = 0.0
    ctrl_vals = []
    for _ in range(200):
        y = rand_su2(RNG)
        c = Ad(inv(y))
        for a in range(3):
            got = sum(c[k, a] * (y @ T[k]) for k in range(3))
            err = max(err, float(np.max(np.abs(got - T[a] @ y))))
            wrong = sum(Ad(y)[k, a] * (y @ T[k]) for k in range(3))
            ctrl_vals.append(float(np.max(np.abs(wrong - T[a] @ y))))
    ctrl = float(np.median(ctrl_vals))
    res["P8_Y_in_X_frame_err"] = err
    res["P8_control_wrong_inverse_median_dev"] = ctrl
    res["P8_control_wrong_inverse_min_dev"] = float(np.min(ctrl_vals))

    # (b) for reversing isometries: c is CONSTANT, lies in O(3)^-, and
    #     M_f(x) = Ad(f(x)^{-1}) c.  Read c off by finite differences.
    c_spread, in_o3m, form_err, dets = 0.0, 0, 0.0, []
    for _ in range(60):
        a, b = rand_su2(RNG), rand_su2(RNG)
        f = make_fab_iota(a, b)
        cs = []
        for _ in range(6):
            x = rand_su2(RNG)
            fx = f(x)
            cmat = np.zeros((3, 3))
            for i in range(3):
                e = np.zeros(3)
                e[i] = h
                dv = (f(x @ su2_exp(e)) - f(x @ su2_exp(-e))) / (2 * h)
                cmat[:, i] = coeffs(dv @ inv(fx))  # coefficients in the Y frame
            cs.append(cmat)
            form_err = max(
                form_err,
                float(np.max(np.abs(frame_transition(f, x) - Ad(inv(fx)) @ cmat))),
            )
        stack = np.stack(cs)
        c_spread = max(c_spread, float(np.max(stack.max(0) - stack.min(0))))
        cm = cs[0]
        dets.append(float(np.linalg.det(cm)))
        if np.max(np.abs(cm.T @ cm - np.eye(3))) < 1e-7 and np.linalg.det(cm) < 0:
            in_o3m += 1
    res["P8_c_max_spread_over_x"] = c_spread
    res["P8_c_in_O3minus_count"] = in_o3m
    res["P8_c_det_range"] = [min(dets), max(dets)]
    res["P8_M_equals_Ad_finv_times_c_err"] = form_err
    res["P8_ok"] = bool(
        err < 1e-12
        and ctrl > 0.3
        and c_spread < 1e-8
        and in_o3m == 60
        and form_err < 1e-8
    )
    return res


# --------------------------------------------------------------------------
# PART 9 -- MAURER-CARTAN OBSTRUCTION: the strongest form of the answer
# --------------------------------------------------------------------------


def _p9_maurer_cartan() -> dict:
    """No SMOOTH MAP AT ALL -- local or global, diffeomorphism or not -- has
    M_f = +Ad, while M_f = -Ad is integrable.

    ROUTE (supplied by the FL Step 8a skeptic pass, adopted and credited).
    M_f = Phi is equivalent to f^*theta = Phi, where theta is the Maurer-Cartan
    form.  Pullback preserves the MC identity, so d(Phi) + Phi ^ Phi = 0 is
    NECESSARY.  For Phi_lambda(X_j) := lambda * x T_j x^{-1},

        d(Phi)(X_i,X_j)        = lambda   * eps_ijk x T_k x^{-1}
        (Phi ^ Phi)(X_i,X_j)   = lambda^2 * eps_ijk x T_k x^{-1}
        sum                    = lambda(1+lambda) * eps_ijk x T_k x^{-1}

    which vanishes iff lambda in {0,-1}.  lambda=-1 is M_iota (integrable, and
    realised by iota); lambda=+1 is C126's g = Ad (NOT integrable).

    WHY THIS IS BETTER than the route it replaces: it needs no classification
    of Isom(S^3), no Isom(S^3) = O(4), no Cerf/Hatcher, and not even that f be
    a diffeomorphism or globally defined.  Both skeptic passes independently
    found that the previous section 2b argument proved a statement about
    Isom while the headline claimed Diff, with the bridging lemma never stated.

    The lambda sweep is genuinely DISCRIMINATING: the residual is a known
    closed form |lambda(1+lambda)|/2, so the check has a predicted value at
    every lambda and fails loudly at lambda = +1.
    """
    res = {}
    h = 1e-5

    def mc_residual(lam: float, x: np.ndarray) -> float:
        def phi(y: np.ndarray, j: int) -> np.ndarray:
            m = lam * Ad(y)
            return sum(m[i, j] * T[i] for i in range(3))

        worst = 0.0
        for i in range(3):
            for j in range(3):
                ei, ej = np.zeros(3), np.zeros(3)
                ei[i] = h
                ej[j] = h
                d_i = (phi(x @ su2_exp(ei), j) - phi(x @ su2_exp(-ei), j)) / (2 * h)
                d_j = (phi(x @ su2_exp(ej), i) - phi(x @ su2_exp(-ej), i)) / (2 * h)
                brk = sum(EPS[i, j, k] * phi(x, k) for k in range(3))
                wedge = phi(x, i) @ phi(x, j) - phi(x, j) @ phi(x, i)
                worst = max(worst, float(np.max(np.abs(d_i - d_j - brk + wedge))))
        return worst

    # The residual is |lambda(1+lambda)| * base(x), where
    #     base(x) := max_k max-entry| x T_k x^{-1} |
    # is x-DEPENDENT, ranging over roughly [0.354, 0.5].  A first version of
    # this check compared against the SUPREMUM 0.5 and therefore mis-predicted
    # by up to 1.4e-2 -- a defect in my own prediction formula, not in the
    # mathematics.  Recorded rather than absorbed into a looser threshold:
    # this is the THIRD time in this file that a comparison statistic, not a
    # result, was the thing that was wrong (see the median-vs-min note in
    # decision.md section 10).  The fix evaluates base(x) at the SAME x.
    pts = [rand_su2(RNG) for _ in range(4)]

    def base(x: np.ndarray) -> float:
        return max(float(np.max(np.abs(x @ T[k] @ inv(x)))) for k in range(3))

    sweep = {}
    max_rel_err = 0.0
    for lam in (-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0):
        got, pred = 0.0, 0.0
        for x in pts:
            r = mc_residual(lam, x)
            p = abs(lam * (1.0 + lam)) * base(x)
            max_rel_err = max(max_rel_err, abs(r - p))
            if r > got:
                got, pred = r, p
        sweep[f"lam={lam:+.1f}"] = {"residual": got, "predicted": pred}
    res["P9_lambda_sweep"] = sweep
    res["P9_max_deviation_from_closed_form"] = max_rel_err
    res["P9_residual_at_minus_Ad_is_iota"] = sweep["lam=-1.0"]["residual"]
    res["P9_residual_at_plus_Ad_is_C126_g"] = sweep["lam=+1.0"]["residual"]
    res["P9_ok"] = bool(
        max_rel_err < 1e-6
        and sweep["lam=-1.0"]["residual"] < 1e-7
        and sweep["lam=+1.0"]["residual"] > 0.5
    )
    return res


# --------------------------------------------------------------------------
# PART 10 -- does section 4's theorem prove TOO MUCH?  The nabla^0 -> nabla^0
#            variant must give SO(3), not O(3)^-.
# --------------------------------------------------------------------------


def _p10_not_too_much() -> dict:
    """Same argument applied to f_* nabla^0 = nabla^0 (parallel frame {X} to
    itself) gives +eps_abm c_ai c_bj = eps_ijk c_mk, hence c^T c = +det(c) I,
    hence c in SO(3) -- i.e. Aut(nabla^0) is orientation-PRESERVING.

    If the section 4 machinery returned O(3)^- here too, it would be proving
    too much and the theorem would be worthless.  It does not.
    """
    res = {}

    def residual(cv: np.ndarray, sign: float) -> np.ndarray:
        c = cv.reshape(3, 3)
        lhs = sign * np.einsum("abm,ai,bj->ijm", EPS, c, c)
        rhs = np.einsum("ijk,mk->ijm", EPS, c)
        return (lhs - rhs).ravel()

    def gauss_newton(c0: np.ndarray, sign: float, iters: int = 200) -> np.ndarray:
        c = c0.copy()
        for _ in range(iters):
            r = residual(c, sign)
            if np.linalg.norm(r) < 1e-13:
                break
            jac = np.zeros((r.size, 9))
            for k in range(9):
                d = np.zeros(9)
                d[k] = 1e-6
                jac[:, k] = (residual(c + d, sign) - residual(c - d, sign)) / 2e-6
            step, *_ = np.linalg.lstsq(jac, -r, rcond=None)
            c = c + step
        return c

    for label, sign in (("swap_nabla0_to_nabla1", -1.0), ("preserve_nabla0", +1.0)):
        dets, bad = [], 0
        for _ in range(120):
            c = gauss_newton(RNG.normal(size=9), sign)
            if np.linalg.norm(residual(c, sign)) > 1e-9:
                continue
            cm = c.reshape(3, 3)
            if abs(np.linalg.det(cm)) < 0.1:
                continue
            dets.append(float(np.linalg.det(cm)))
            if np.max(np.abs(cm.T @ cm - np.eye(3))) > 1e-6:
                bad += 1
        res[f"P10_{label}_n_solutions"] = len(dets)
        res[f"P10_{label}_det_range"] = [min(dets), max(dets)] if dets else []
        res[f"P10_{label}_n_nonorthogonal"] = bad
    res["P10_ok"] = bool(
        res["P10_swap_nabla0_to_nabla1_det_range"][1] < -0.99
        and res["P10_preserve_nabla0_det_range"][0] > 0.99
        and res["P10_swap_nabla0_to_nabla1_n_nonorthogonal"] == 0
        and res["P10_preserve_nabla0_n_nonorthogonal"] == 0
    )
    return res


# --------------------------------------------------------------------------


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("C128 -- nabla^t category reconciliation (C125 affine vs C126 Yang-Mills)")
    print("=" * 78)

    for name, fn in [
        ("PART 0  su(2)/SU(2) self-tests", _p0_self_tests),
        (
            "PART 1  frame-transition functions M_f (finite differences)",
            _p1_frame_transitions,
        ),
        ("PART 2  det <-> winding LOCK on the geometric image", _p2_lock),
        (
            "PART 3  O(3)-valued M_f => isometry, with falsifier",
            _p3_orthogonality_lemma,
        ),
        ("PART 4  C126's g = Ad reproduced; M_iota = (-I).g; winding", _p4_c126_gauge),
        ("PART 5  the gauge transformation moves the vielbein", _p5_vielbein_moves),
        (
            "PART 6  eps is SO(3)-invariant => torsion sign needs det = -1",
            _p6_eps_character,
        ),
        (
            "PART 7  NEW: any diffeo with nabla^0 -> nabla^1 is an orient.-rev. isometry",
            _p7_parallel_frames,
        ),
        (
            "PART 8  minimal route: det M_f = -1 without using Isom(S^3) = O(4)",
            _p8_minimal_route,
        ),
        (
            "PART 9  Maurer-Cartan: NO smooth map has M_f = +Ad (lambda sweep)",
            _p9_maurer_cartan,
        ),
        (
            "PART 10 does section 4 prove too much?  nabla^0 -> nabla^0 gives SO(3)",
            _p10_not_too_much,
        ),
    ]:
        print(f"\n--- {name} ---")
        r = fn()
        out.update(r)
        for k, v in r.items():
            print(f"  {k:52s} = {v}")

    # WHY THIS IS NOW COMPUTED, NOT WRITTEN: the previous version of this block
    # was a dict of hard-coded literals (False / True / a prose string) that
    # consulted NOTHING in `out`, while decision.md's reproduce-instruction told
    # the reader to verify the round's conclusion against them.  Corrupting the
    # underlying measurements left every printed verdict field unchanged.  Both
    # FL Step 8a skeptic passes found this independently and rated it HIGH.
    # Every field below is now derived from a measured, gated quantity.
    verdict = {
        # Maurer-Cartan: +Ad is not integrable, -Ad is.  Independent of Isom(S^3).
        "g_equals_Ad_is_realizable_as_df": bool(
            out["P9_residual_at_plus_Ad_is_C126_g"] < 1e-7
        ),
        "minus_Ad_IS_realizable_and_is_M_iota": bool(
            out["P9_residual_at_minus_Ad_is_iota"] < 1e-7
            and out["C1_M_iota_equals_minus_Ad_err"] < 1e-8
        ),
        # This is C1 restated with g := Ad substituted -- NOT an extra measurement.
        "M_iota_equals_minus_I_times_g": bool(out["C1_ok"]),
        "det_M_f_is_minus_one_for_every_relating_diffeo": bool(
            out["P10_swap_nabla0_to_nabla1_det_range"][1] < -0.99
        ),
        "theorem_does_not_prove_too_much": bool(
            out["P10_preserve_nabla0_det_range"][0] > 0.99
        ),
        "geometric_image_det_plus_one_part_is_constant": bool(out["P2_ok"]),
        "reason": (
            "Maurer-Cartan: d(Phi)+Phi^Phi = lambda(1+lambda)*eps != 0 at "
            "lambda=+1, so NO smooth map has M_f = +Ad; = 0 at lambda=-1, "
            "which is M_iota.  The operative obstruction is det (C125's Z2), "
            "NOT winding -- see PART 6."
        ),
    }
    out["VERDICT_INPUTS"] = verdict
    ok_keys = [k for k in out if k.endswith("_ok")]
    out["ALL_OK"] = bool(all(out[k] for k in ok_keys))
    print("\n--- VERDICT INPUTS ---")
    for k, v in verdict.items():
        print(f"  {k:52s} = {v}")
    print(
        f"\n  gate checks passing: {sum(bool(out[k]) for k in ok_keys)} / {len(ok_keys)}"
    )
    print(f"  ALL_OK = {out['ALL_OK']}")

    (HERE / "results_c128.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nwrote {HERE / 'results_c128.json'}")


if __name__ == "__main__":
    main()
