"""C111 follow-up, strategy switch: the full bivariate symbolic det(G(lam,t))
via Bareiss elimination (schur_symbolic.py) ran 3.5+ hours of sustained
~100% CPU with zero intermediate output and was killed -- classic
intermediate-expression-swell failure mode for fraction-free elimination on
a dense matrix with bivariate polynomial entries (degree <=3 in lam, <=2 in
t per entry -> det bound degree <=24 in lam, and the discriminant w.r.t. lam
could in the worst case run to degree ~46*8=368 in t^2, though almost
certainly far smaller in practice -- either way, an intractable target to
reconstruct exactly bottom-up).

New strategy: we don't actually need the full symbolic det(G) polynomial.
We already know t1..t4 numerically to double precision (C111's own
np.linalg.eigvals + bisection). What we want is their EXACT closed form.
Standard tool for exactly this situation: compute each threshold to VERY
HIGH precision (mpmath, arbitrary-precision eigenvalues + bisection -- cheap,
this is just numerics, not symbolic elimination) then use PSLQ (integer
relation detection) to find the low-degree polynomial relation each root
satisfies over the rationals. This is the standard way to "guess the closed
form of a numerically-known algebraic root" and sidesteps the intractable
bivariate elimination entirely.

Given the proven t<->-t symmetry (C111 decision.md), each threshold's
minimal polynomial should be a polynomial in t^2, so we search for integer
relations among [1, s, s^2, ..., s^k] where s = t^2, starting at low degree
k and increasing only if nothing is found (Occam order).

RESULT (see pearl_registry/INDEX.md's C111 row for the full writeup): this
attempt also fell short, informatively. mpmath's QR eigensolver failed to
converge very close to the degeneracy itself (t1/t2 only reached 13/3
accurate digits vs t3/t4's clean 33/32), and a robustness check (rerunning
PSLQ on the same value truncated to different digit counts) proved the
apparent "relations" PSLQ found up to degree 30 were numerical artifacts,
not real algebraic relations -- a different "relation" every time. Closed
form remains genuinely open.
"""

from __future__ import annotations

import importlib.util
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(
    r"E:\Проверка Гипотез\работаю над проверкой гипотез\N-7-GeoSpectra-Lab\tom_s3_spinor_toy"
)


def log(msg: str) -> None:
    print(msg, flush=True)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1, l2, l3, k):
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k):
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_M_ab(c85_mod, k, a, b):
    j1 = S(k) / 2
    j2 = S(1) / 2
    jt = j1 + S(1) / 2
    dim_k = k + 1
    dim_kp1 = k + 2
    m_q_k, m_p_k = magnetic_labels(c85_mod, k)
    m_q_kp1, m_p_kp1 = magnetic_labels(c85_mod, k + 1)
    qidx = {v: i for i, v in enumerate(m_q_kp1)}
    pidx = {v: i for i, v in enumerate(m_p_kp1)}
    M = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
    for q in range(dim_k):
        for p in range(dim_k):
            mqt = m_q_k[q] + a
            mpt = m_p_k[p] + b
            if mqt not in qidx or mpt not in pidx:
                continue
            Q = qidx[mqt]
            P = pidx[mpt]
            vq = CG(j1, m_q_k[q], j2, a, jt, mqt).doit()
            vp = CG(j1, m_p_k[p], j2, b, jt, mpt).doit()
            M[Q * dim_kp1 + P, q * dim_k + p] = sp.simplify(vq * vp)
    return M


def sympy_matrix_to_mpmath(M: sp.Matrix) -> mp.matrix:
    rows, cols = M.shape
    out = mp.matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            out[i, j] = mp.mpf(sp.nsimplify(M[i, j]).evalf(mp.mp.dps + 10))
    return out


def main() -> None:
    t0 = time.time()
    c85 = load_module(
        "c85_certification",
        HERE
        / "experiments"
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(k):
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D1 = dbar_full(1)
    D2 = dbar_full(2)
    half = S(1) / 2
    M_sum = (
        build_M_ab(c85, 1, half, half)
        + build_M_ab(c85, 1, half, -half)
        + build_M_ab(c85, 1, -half, half)
        + build_M_ab(c85, 1, -half, -half)
    )
    B = sp.Matrix(sp.kronecker_product(M_sum, sp.eye(2)))
    log(f"Exact rational matrices built, t={time.time() - t0:.2f}s")

    mp.mp.dps = 60  # 60 decimal digits -- plenty of headroom for PSLQ
    D1_mp = sympy_matrix_to_mpmath(D1)
    D2_mp = sympy_matrix_to_mpmath(D2)
    B_mp = sympy_matrix_to_mpmath(B)
    n1, n2 = D1.shape[0], D2.shape[0]
    nt = n1 + n2
    log(f"Converted to {mp.mp.dps}-digit mpmath matrices, t={time.time() - t0:.2f}s")

    def dpw_for_scale(t: mp.mpf) -> mp.matrix:
        DPW = mp.matrix(nt, nt)
        for i in range(n1):
            for j in range(n1):
                DPW[i, j] = D1_mp[i, j]
        for i in range(n2):
            for j in range(n2):
                DPW[n1 + i, n1 + j] = D2_mp[i, j]
        Bs = t * B_mp
        for i in range(n2):
            for j in range(n1):
                DPW[n1 + i, j] = Bs[i, j]
        BsT = Bs.transpose_conj()
        for i in range(n1):
            for j in range(n2):
                DPW[i, n1 + j] = BsT[i, j]
        return DPW

    def max_imag_for_scale(t: mp.mpf) -> mp.mpf:
        eigs = mp.eig(dpw_for_scale(t), left=False, right=False)
        return max(abs(mp.im(e)) for e in eigs)

    def max_imag_for_scale_safe(t: mp.mpf) -> mp.mpf | None:
        """None means QR didn't converge -- point is too close to the exact
        degeneracy for mpmath's unshifted-ish QR to resolve (the two
        colliding eigenvalues separate like sqrt(t-t*), so very small
        |t-t*| makes the matrix numerically indistinguishable from an exact
        repeated eigenvalue -- a hard case for ANY floating eigenvalue
        algorithm, not an mpmath-specific bug)."""
        try:
            return max_imag_for_scale(t)
        except RuntimeError:
            return None

    def bisect(lo: mp.mpf, hi: mp.mpf, real_at_lo: bool, iters: int = 110) -> tuple[mp.mpf, int]:
        # WHY iters=110 not 220: each iteration adds ~log10(2)=0.301 decimal
        # digits to the BRACKET width, but bisection was hitting QR
        # non-convergence around iteration ~150-200 (see module docstring) --
        # 110 iterations (~33 digits) stays well clear of that wall while
        # still giving ~2x the double-precision baseline, plenty for a
        # low-degree PSLQ search.
        thresh = mp.mpf(10) ** (-(mp.mp.dps - 10))
        done = 0
        for i in range(iters):
            mid = (lo + hi) / 2
            mi = max_imag_for_scale_safe(mid)
            if mi is None:
                # Too close to call -- stop here rather than crash; the
                # current [lo,hi] bracket is still our best answer.
                break
            is_real = mi < thresh
            if is_real == real_at_lo:
                lo = mid
            else:
                hi = mid
            done = i + 1
        return (lo + hi) / 2, done

    # Double-precision seeds from C111's own formal script (results_c111.json).
    seeds = {
        "t1": (mp.mpf("0.95"), mp.mpf("1.0"), True),
        "t2": (mp.mpf("2.85"), mp.mpf("2.89"), False),
        "t3": (mp.mpf("2.89"), mp.mpf("2.93"), True),
        "t4": (mp.mpf("6.8"), mp.mpf("6.9"), False),
    }

    # WHY track accurate_digits per threshold (not just assume mp.mp.dps):
    # `done` bisection steps give ~done*log10(2) TRUE accurate digits, but
    # mp.mp.dps=60 is only the WORKING precision -- if bisect stopped early
    # (QR non-convergence near the degeneracy, see bisect()'s own docstring),
    # digits beyond the accurate count are numerical noise from the last
    # midpoint, not signal. Reporting "60 digits" regardless of `done` would
    # be exactly the kind of unmarked-precision overclaim integrity.md warns
    # against.
    thresholds: dict[str, mp.mpf] = {}
    accurate_digits: dict[str, int] = {}
    for name, (lo, hi, real_at_lo) in seeds.items():
        t0b = time.time()
        val, done = bisect(lo, hi, real_at_lo)
        thresholds[name] = val
        accurate_digits[name] = max(1, int(done * mp.log10(2)))
        log(
            f"{name} = {mp.nstr(val, accurate_digits[name])}  "
            f"({done} bisection steps -> ~{accurate_digits[name]} accurate digits, "
            f"took {time.time() - t0b:.1f}s)"
        )

    log(f"\nAll 4 thresholds refined, t={time.time() - t0:.1f}s")

    # PSLQ: search for the minimal polynomial of s = t^2 over the rationals,
    # trying degree 1,2,...,MAX_DEGREE (Occam order -- stop at first hit).
    MAX_DEGREE = 10
    log("\n--- PSLQ minimal-polynomial search (on s = t^2) ---")
    results = {}
    for name, val in thresholds.items():
        s = val * val
        # WHY margin=8, not a fixed digit count: the verification residual
        # threshold must be looser than this specific threshold's OWN
        # accurate-digit count (accurate_digits[name]), not the shared
        # mp.mp.dps=60 working precision -- a threshold that only reached
        # ~25 accurate digits (early-stopped bisection) cannot be verified
        # to a 10^-45 residual; that would silently reject true relations.
        residual_bound = mp.mpf(10) ** (-(accurate_digits[name] - 8))
        found = None
        for deg in range(1, MAX_DEGREE + 1):
            basis = [s**k for k in range(deg + 1)]
            rel = mp.pslq(basis, maxsteps=2000)
            if rel is not None and any(c != 0 for c in rel):
                # Verify: does this relation actually hold to high precision,
                # not just a PSLQ near-miss from too few digits?
                check = sum(mp.mpf(c) * s**k for k, c in enumerate(rel))
                if abs(check) < residual_bound:
                    found = (deg, rel)
                    break
        if found:
            deg, rel = found
            poly_str = " + ".join(f"({c})*s^{k}" for k, c in enumerate(rel) if c != 0)
            log(f"{name}: degree-{deg} relation in s=t^2 found: {poly_str} = 0")
            results[name] = {"degree": deg, "coeffs": [int(c) for c in rel]}
        else:
            log(
                f"{name}: no relation found up to degree {MAX_DEGREE} "
                f"(~{accurate_digits[name]} accurate digits available)"
            )
            results[name] = None

    log(f"\nDone, total t={time.time() - t0:.1f}s")
    out_path = (
        HERE
        / "experiments"
        / "20260830-c111-exceptional-point-systematic-sweep"
        / "schur_pslq_results.json"
    )
    import json

    payload = {
        "thresholds": {
            k: {
                "value": mp.nstr(v, accurate_digits[k]),
                "accurate_digits": accurate_digits[k],
            }
            for k, v in thresholds.items()
        },
        "pslq_minimal_polynomials_in_s_eq_t_squared": results,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    log(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
