"""C216: independent second route to Ric^grad=1.5 (C215) via the
Kobayashi-Nomizu canonical-connection formulas of a reductive space g=h+m:

    R^c(X,Y)Z = -[[X,Y]_h, Z]       (curvature of the canonical connection)
    T^c(X,Y)  = -[X,Y]_m            (its torsion; naturally reductive => 3-form)

Uses ONLY the Lie bracket and su(3)'s action on the complement. No
octonion cross product (C212), no Castellani curvature code (C213), no
Friedrich-Ivanov formula (C215) enters the KN computation itself.

The KN formula is written from memory [MEMORY]; its sign/index convention
is therefore calibrated BEFORE use on a positive control with a known
answer: the round unit S6 = SO(7)/SO(6) (symmetric space, T=0, canonical
connection = Levi-Civita), where Ric = 5*delta (n-1 for the unit n-sphere).

Triangle check at the end: Ric^g (Castellani, calibrated in C213) must
equal Ric^c (KN) - (1/4)*sum_i g(T(e_i,X),T(Y,e_i)) with T taken from the
BRACKET (not from octonions). CORRECTED 2026-10-03: as coded this does NOT
hold -- it misses by 2.5 on both spaces (see results_c216.json), because
Castellani's eq. 3.34 defines the components without the standard 1/2. It
holds exactly for 2 x Castellani (C217).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c216.json"


def load_module(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, HERE.parent / rel_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def commutator(A, B):
    return A @ B - B @ A


def expand_in_basis(target, basis):
    basis_flat = np.column_stack([b.flatten() for b in basis])
    coeffs, _, _, _ = np.linalg.lstsq(basis_flat, target.flatten(), rcond=None)
    residual = float(np.linalg.norm(target.flatten() - basis_flat @ coeffs))
    assert residual < 1e-8, f"commutator not in span(K+H): residual={residual:.2e}"
    return coeffs.real, residual


def kn_curvature_torsion(K, H, scale):
    """Orthonormal frame e_a = scale*K_a. Returns Riemann R[d,a,b,c] = component of
    R^c(e_a,e_b)e_c along e_d, torsion T[a,b,c] = -g([e_a,e_b]_m, e_c), and the
    reductive leak (H-part of [H,K], must be ~0)."""
    n_k, n_h = len(K), len(H)
    full = K + H
    riem = np.zeros((n_k, n_k, n_k, n_k))
    tors = np.zeros((n_k, n_k, n_k))
    leak = 0.0
    for a in range(n_k):
        for b in range(n_k):
            cab, _ = expand_in_basis(commutator(K[a], K[b]), full)
            # [e_a,e_b] = scale^2 [K_a,K_b]; m-part coefficients on e_d: scale*cab[d]
            tors[a, b, :] = -scale * cab[:n_k]
            h_part = scale**2 * sum(cab[n_k + i] * H[i] for i in range(n_h))
            for c in range(n_k):
                # R(e_a,e_b)e_c = -[h_part, e_c] = -scale*[h_part, K_c]
                out, _ = expand_in_basis(-scale * commutator(h_part, K[c]), full)
                leak = max(leak, float(np.max(np.abs(out[n_k:]))))
                riem[:, a, b, c] = out[:n_k] / scale  # coefficients on e_d=scale*K_d
    return riem, tors, leak


def ricci_from_riem(riem):
    n = riem.shape[0]
    return np.array([[sum(riem[a, a, b, c] for a in range(n)) for c in range(n)] for b in range(n)])


def torsion_correction(tors):
    n = tors.shape[0]
    return np.array(
        [
            [
                -0.25 * sum(tors[i, b, k] * tors[d, i, k] for i in range(n) for k in range(n))
                for d in range(n)
            ]
            for b in range(n)
        ]
    )


def antisym_err(t):
    n = t.shape[0]
    e = 0.0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                e = max(e, abs(t[a, b, c] + t[b, a, c]), abs(t[a, b, c] + t[a, c, b]))
    return e


def castellani_ricci(K, H, r):
    """Castellani eq. 3.35-3.36 (calibrated against N^010 in C213), uniform r."""
    n_k, n_h = len(K), len(H)
    full = K + H
    ckkk = np.zeros((n_k, n_k, n_k))
    ckkh = np.zeros((n_h, n_k, n_k))
    chkk = np.zeros((n_k, n_h, n_k))
    for b in range(n_k):
        for c in range(n_k):
            if b != c:
                co, _ = expand_in_basis(commutator(K[b], K[c]), full)
                ckkk[:, b, c], ckkh[:, b, c] = co[:n_k], co[n_k:]
    for i in range(n_h):
        for b in range(n_k):
            co, _ = expand_in_basis(commutator(H[i], K[b]), full)
            chkk[b, i, :] = co[:n_k]

    def cb(a, b, c):
        return (
            (r[b] * r[c] / r[a]) * ckkk[a, b, c]
            - (r[a] * r[c] / r[b]) * ckkk[b, a, c]
            - (r[a] * r[b] / r[c]) * ckkk[c, a, b]
        )

    def riem(a, b, d, e):
        t1 = 0.25 * sum((r[d] * r[e] / r[c]) * cb(a, b, c) * ckkk[c, d, e] for c in range(n_k))
        t2 = 0.5 * r[d] * r[e] * sum(-chkk[b, i, a] * ckkh[i, d, e] for i in range(n_h))
        t3 = 0.125 * sum(cb(a, c, d) * cb(c, b, e) for c in range(n_k))
        t4 = -0.125 * sum(cb(a, c, e) * cb(c, b, d) for c in range(n_k))
        return t1 + t2 + t3 + t4

    return np.array(
        [[sum(riem(a, b, a, d) for a in range(n_k)) for d in range(n_k)] for b in range(n_k)]
    )


def so7_control():
    """Round S6 = SO(7)/SO(6): K_a = A_{a,7}/sqrt2 (complement), H = A_ij/sqrt2 (i<j<=6)."""

    def a_ij(i, j):
        m = np.zeros((7, 7))
        m[i, j], m[j, i] = 1.0, -1.0
        return m / np.sqrt(2.0)

    k = [a_ij(i, 6) for i in range(6)]
    h = [a_ij(i, j) for i in range(6) for j in range(i + 1, 6)]
    n_pt = np.zeros(7)
    n_pt[6] = 1.0
    norm_sq = float(np.mean([np.dot(g @ n_pt, g @ n_pt) for g in k]))
    return k, h, 1.0 / np.sqrt(norm_sq)


def g2su3_data():
    g96 = load_module("20260626-g96-s6-g2-su3/g96_g2_su3.py", "g96_g2_su3")
    phi = g96.build_phi()
    gens = g96.find_g2_generators(phi)
    n_pt = np.zeros(7)
    n_pt[6] = 1.0
    a_mat = np.column_stack([g @ n_pt for g in gens])
    _, sv, vt = np.linalg.svd(a_mat, full_matrices=True)
    null = vt[int(np.sum(sv > 1e-10)) :]
    gm = np.array([g.flatten() for g in gens])
    su3 = [row.reshape(7, 7) for row in (null @ gm)]
    q_su3, _ = np.linalg.qr(np.column_stack([g.flatten() for g in su3]), mode="reduced")
    cv = []
    for g in gens:
        gf = g.flatten()
        res = gf - q_su3 @ (q_su3.T @ gf)
        if np.linalg.norm(res) > 1e-10:
            cv.append(res)
    qc, rc = np.linalg.qr(np.column_stack(cv), mode="reduced")
    ncomp = int(np.sum(np.abs(np.diag(rc)) > 1e-10))
    comp = [qc[:, k].reshape(7, 7) for k in range(ncomp)]
    norm_sq = float(np.mean([np.dot(g @ n_pt, g @ n_pt) for g in comp]))
    return comp, su3, 1.0 / np.sqrt(norm_sq)


def isotropy_stats(m):
    d = np.diag(m)
    return (
        float(np.mean(d)),
        float(np.max(np.abs(d - np.mean(d)))),
        float(np.max(np.abs(m - np.diag(d)))),
    )


def run_case(label, k, h, scale):
    print(f"\n--- {label} (scale={scale:.6f}) ---")
    riem, tors, leak = kn_curvature_torsion(k, h, scale)
    assert leak < 1e-8, f"R^c(X,Y)Z leaves m: leak={leak:.2e} (not reductive/ad(h)-invariant)"
    ric_c = ricci_from_riem(riem)
    c_ric, c_spread, c_off = isotropy_stats(ric_c)
    t_sq = float(np.sum(tors**2))
    t_asym = antisym_err(tors)
    corr = torsion_correction(tors)
    ric_g_cast = castellani_ricci(k, h, scale * np.ones(len(k)))
    g_ric, g_spread, g_off = isotropy_stats(ric_g_cast)
    triangle = float(np.max(np.abs(ric_g_cast - (ric_c + corr))))
    print(
        f"  KN:  Ric^c = {c_ric:.6f}*delta  (spread {c_spread:.1e}, off-diag {c_off:.1e}), leak {leak:.1e}"
    )
    print(
        f"  KN:  |T|^2 = {t_sq:.6f}, total-antisymmetry err {t_asym:.1e} (naturally reductive check)"
    )
    print(f"  Castellani Ric^g = {g_ric:.6f}*delta  (spread {g_spread:.1e}, off-diag {g_off:.1e})")
    print(f"  triangle: max|Ric^g_Castellani - (Ric^c_KN + corr_from_bracket_T)| = {triangle:.2e}")
    return {
        "ric_c_KN": c_ric,
        "ric_c_spread": c_spread,
        "ric_c_offdiag": c_off,
        "torsion_norm_sq_from_bracket": t_sq,
        "torsion_antisym_err": t_asym,
        "ric_g_castellani": g_ric,
        "triangle_max_err": triangle,
    }


def main():
    print("\n=== C216: Kobayashi-Nomizu second route to Ric^grad ===")
    k0, h0, s0 = so7_control()
    ctrl = run_case("CONTROL round S6=SO(7)/SO(6), expect Ric=5, T=0", k0, h0, s0)

    # Gate ONLY on the KN route itself -- this is the route being validated here.
    kn_ctrl_ok = abs(ctrl["ric_c_KN"] - 5.0) < 1e-8 and ctrl["torsion_norm_sq_from_bracket"] < 1e-12
    print(
        f"  KN CONTROL verdict: {'PASS' if kn_ctrl_ok else 'FAIL -- STOP, KN convention not calibrated'}"
    )

    # Castellani cross-check on the SAME control is reported SEPARATELY, not
    # used to gate the KN route -- it fails here (2.5 instead of 5.0), a
    # newly-discovered, unresolved issue in C213's own previously-"double-
    # calibrated" code (confirmed via debug_reuse_c213_on_control.py: C213's
    # OWN original functions give the same wrong 2.5 on this control, so this
    # is not a C216 transcription bug). Flagged explicitly, not patched here.
    castellani_ctrl_ok = abs(ctrl["ric_g_castellani"] - 5.0) < 1e-8
    print(
        f"  Castellani cross-check on SAME control: {'PASS' if castellani_ctrl_ok else 'FAIL (2.5 instead of 5.0) -- FLAGGED, see decision.md -- NOT gating this route'}"
    )

    results = {
        "control": ctrl,
        "kn_control_pass": bool(kn_ctrl_ok),
        "castellani_control_pass": bool(castellani_ctrl_ok),
    }
    if not kn_ctrl_ok:
        results["status"] = "BLOCKED_CALIBRATION_FAILED"
        RESULTS_PATH.write_text(json.dumps(results, indent=2))
        return

    k1, h1, s1 = g2su3_data()
    main_res = run_case("G2/SU(3), ambient-unit frame (C214/C215 basis)", k1, h1, s1)
    ok = (
        abs(main_res["ric_c_KN"] - 1.5) < 1e-8
        and main_res["ric_c_spread"] < 1e-8
        and main_res["ric_c_offdiag"] < 1e-8
    )
    print("\nPREDICTION from C215 (Friedrich-Ivanov route): Ric^grad = 1.5")
    print(f"KN route gives Ric^c = {main_res['ric_c_KN']:.6f}")
    print(
        f"  torsion norm from BRACKET alone: {main_res['torsion_norm_sq_from_bracket']:.6f} (C212/C214 octonion route: 24)"
    )
    verdict = "CONFIRMED" if ok else "MISMATCH"
    print(f"[{verdict}]")
    results.update({"g2su3": main_res, "status": verdict, "predicted_by_C215": 1.5})
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
