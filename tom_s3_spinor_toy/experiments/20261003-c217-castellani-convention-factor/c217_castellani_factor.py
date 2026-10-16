"""C217: is C213's Castellani-formula code off from the standard Levi-Civita
curvature by a UNIFORM factor 1/2 (a convention factor), as the C216 skeptic
review suggested -- component-wise, not just via the Ricci trace?

Pre-registered prediction (claim.md, written before running): for BOTH the
symmetric control S6=SO(7)/SO(6) (only term2 active) AND the non-symmetric
S6=G2/SU(3) (terms 1,2,4 active), 2 * R_castellani(a,b,d,e) equals the
constant-curvature tensor of the unit round S6,
    R_round(a,b,d,e) = delta_ad delta_be - delta_ae delta_bd,
in the ambient-unit orthonormal frame, entry by entry (6^4 = 1296 entries).

Why G2/SU(3) is round: G2 <= SO(7) acts on Im(O)=R^7 by isometries and
transitively on the unit S6; the isotropy rep m is real-irreducible (C165), so
the G2-invariant metric is unique up to scale -- it is the round one. The frame
here is ambient-orthonormal (Gram check below), i.e. the unit sphere.

Negative controls: (i) the code as-is (x1) and (ii) doubling ONLY term2 must
FAIL the component-wise test on G2/SU(3) (they would pass only if the factor
were not uniform).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c217.json"

spec = importlib.util.spec_from_file_location(
    "c216",
    HERE.parent
    / "20261002-c216-kobayashi-nomizu-ricci-check"
    / "c216_kn_ricci_check.py",
)
c216 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c216)


def structure_constants(k, h):
    n_k, n_h = len(k), len(h)
    full = k + h
    ckkk = np.zeros((n_k, n_k, n_k))
    ckkh = np.zeros((n_h, n_k, n_k))
    chkk = np.zeros((n_k, n_h, n_k))
    for b in range(n_k):
        for c in range(n_k):
            if b != c:
                co, _ = c216.expand_in_basis(c216.commutator(k[b], k[c]), full)
                ckkk[:, b, c], ckkh[:, b, c] = co[:n_k], co[n_k:]
    for i in range(n_h):
        for b in range(n_k):
            co, _ = c216.expand_in_basis(c216.commutator(h[i], k[b]), full)
            chkk[b, i, :] = co[:n_k]
    return ckkk, ckkh, chkk


def castellani_riemann(ckkk, ckkh, chkk, r, mult=(1.0, 1.0, 1.0, 1.0)):
    """Full 4-index tensor R[a,b,d,e] of C213's riemann() closure (same four
    terms, same coefficients 1/4, 1/2, 1/8, -1/8), with optional per-term
    multipliers used only for the negative controls."""
    n_k, n_h = ckkk.shape[0], ckkh.shape[0]

    def cb(a, b, c):
        return (
            (r[b] * r[c] / r[a]) * ckkk[a, b, c]
            - (r[a] * r[c] / r[b]) * ckkk[b, a, c]
            - (r[a] * r[b] / r[c]) * ckkk[c, a, b]
        )

    out = np.zeros((n_k, n_k, n_k, n_k))
    for a in range(n_k):
        for b in range(n_k):
            for d in range(n_k):
                for e in range(n_k):
                    t1 = 0.25 * sum(
                        (r[d] * r[e] / r[c]) * cb(a, b, c) * ckkk[c, d, e]
                        for c in range(n_k)
                    )
                    t2 = (
                        0.5
                        * r[d]
                        * r[e]
                        * sum(-chkk[b, i, a] * ckkh[i, d, e] for i in range(n_h))
                    )
                    t3 = 0.125 * sum(cb(a, c, d) * cb(c, b, e) for c in range(n_k))
                    t4 = -0.125 * sum(cb(a, c, e) * cb(c, b, d) for c in range(n_k))
                    out[a, b, d, e] = (
                        mult[0] * t1 + mult[1] * t2 + mult[2] * t3 + mult[3] * t4
                    )
    return out


def round_tensor(n):
    eye = np.eye(n)
    return np.einsum("ad,be->abde", eye, eye) - np.einsum("ae,bd->abde", eye, eye)


def ricci(rt):
    return np.einsum("abad->bd", rt)


def run_space(label, k, h, scale):
    n = len(k)
    ckkk, ckkh, chkk = structure_constants(k, h)
    r = scale * np.ones(n)
    rnd = round_tensor(n)
    res = {"c_kkk_max_abs": float(np.max(np.abs(ckkk)))}
    variants = {
        "as_is_x1": (1.0, 1.0, 1.0, 1.0),
        "uniform_x2": (2.0, 2.0, 2.0, 2.0),
        "term2_only_x2": (1.0, 2.0, 1.0, 1.0),
    }
    print(
        f"\n--- {label} (scale={scale:.6f}, max|C_KKK|={res['c_kkk_max_abs']:.3f}) ---"
    )
    for name, mult in variants.items():
        rt = castellani_riemann(ckkk, ckkh, chkk, r, mult)
        err = float(np.max(np.abs(rt - rnd)))
        ric = ricci(rt)
        res[name] = {
            "max_abs_err_vs_round_riemann": err,
            "ricci_diag_mean": float(np.mean(np.diag(ric))),
        }
        print(
            f"  {name:14s}: max|R_code - R_round| = {err:.3e}   Ric diag mean = {np.mean(np.diag(ric)):.6f}"
        )
    # Independent route (no Castellani anywhere): KN canonical Ricci + torsion
    # correction (Friedrich-Ivanov), torsion from the BRACKET.
    riem_kn, tors, leak = c216.kn_curvature_torsion(k, h, scale)
    assert leak < 1e-8, f"KN curvature leaves m (not reductive): leak={leak:.2e}"
    ric_c = c216.ricci_from_riem(riem_kn)
    corr = c216.torsion_correction(tors)
    ric_lc_from_kn = ric_c + corr
    res["kn_plus_fi_ricci_diag_mean"] = float(np.mean(np.diag(ric_lc_from_kn)))
    res["kn_plus_fi_offdiag_max"] = float(
        np.max(np.abs(ric_lc_from_kn - np.diag(np.diag(ric_lc_from_kn))))
    )
    res["kn_plus_fi_vs_round_ricci_err"] = float(
        np.max(np.abs(ric_lc_from_kn - (n - 1) * np.eye(n)))
    )
    print(
        f"  KN + Friedrich-Ivanov (no Castellani): Ric^g = {res['kn_plus_fi_ricci_diag_mean']:.6f} "
        f"(round-sphere value n-1={n - 1}), max|Ric - 5*I| = {res['kn_plus_fi_vs_round_ricci_err']:.2e}"
    )
    return res


def main():
    print("\n=== C217: Castellani-formula convention factor, component-wise ===")
    k0, h0, s0 = c216.so7_control()
    ctrl = run_space("CONTROL SO(7)/SO(6)", k0, h0, s0)

    k1, h1, s1 = c216.g2su3_data()
    # Frame / isometry sanity for G2/SU(3): ambient orthonormality and G2 <= so(7).
    n_pt = np.zeros(7)
    n_pt[6] = 1.0
    tang = np.array([(s1 * g) @ n_pt for g in k1])
    gram_err = float(np.max(np.abs(tang @ tang.T - np.eye(len(k1)))))
    antisym = max(float(np.max(np.abs(m + m.T))) for m in k1 + h1)
    print(
        f"\nG2/SU(3): ambient-Gram error of unit tangent frame = {gram_err:.2e}; "
        f"max|G + G^T| over comp+su3 generators = {antisym:.2e}"
    )
    main_res = run_space("G2/SU(3), ambient-unit frame", k1, h1, s1)
    main_res["gram_err"] = gram_err
    main_res["generators_antisym_err"] = antisym

    tol = 1e-8
    uniform_ok = (
        ctrl["uniform_x2"]["max_abs_err_vs_round_riemann"] < tol
        and main_res["uniform_x2"]["max_abs_err_vs_round_riemann"] < tol
    )
    negctrl_ok = (
        main_res["as_is_x1"]["max_abs_err_vs_round_riemann"] > 1e-3
        and main_res["term2_only_x2"]["max_abs_err_vs_round_riemann"] > 1e-3
    )
    kn_fi_ok = (
        main_res["kn_plus_fi_vs_round_ricci_err"] < tol
        and ctrl["kn_plus_fi_vs_round_ricci_err"] < tol
    )
    verdict = (
        "UNIFORM_FACTOR_2_CONFIRMED"
        if (uniform_ok and negctrl_ok and kn_fi_ok)
        else "NOT_CONFIRMED"
    )
    print(f"\nuniform x2 matches round Riemann on both spaces (<{tol:g}): {uniform_ok}")
    print(
        f"negative controls (x1, term2-only x2) FAIL on G2/SU(3) as they must: {negctrl_ok}"
    )
    print(
        f"independent KN + Friedrich-Ivanov Ricci = round value on both spaces: {kn_fi_ok}"
    )
    print(f"[{verdict}]")
    RESULTS_PATH.write_text(
        json.dumps(
            {
                "control": ctrl,
                "g2su3": main_res,
                "uniform_ok": bool(uniform_ok),
                "negative_controls_fail_as_required": bool(negctrl_ok),
                "kn_fi_independent_ok": bool(kn_fi_ok),
                "verdict": verdict,
            },
            indent=2,
        )
    )
    print(f"-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
