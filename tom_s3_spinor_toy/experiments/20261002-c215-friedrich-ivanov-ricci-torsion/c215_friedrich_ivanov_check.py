"""C215: check the Friedrich-Ivanov Ricci/torsion formula component-wise
(not just the scalar trace by hand) on S6=G2/SU(3), reusing C213's Ricci
(r=sqrt(3), ambient-orthonormal) and C214's torsion (same basis) -- both
already independently calibrated/verified.

Source (full text, not abstract): Friedrich & Ivanov, "Parallel spinors
and connections with skew-symmetric torsion in string theory",
arXiv:math/0102142, section 2 (general, for ANY metric connection with
totally skew torsion -- NOT nearly-Kahler-specific, no T^c, no Russo-
style mu bridge):

    Ric^g(X,Y) = Ric^grad(X,Y) + (1/2)*delta^g(T)(X,Y)
                 - (1/4)*sum_i g(T(e_i,X),T(Y,e_i))

For nearly-Kahler, T is parallel w.r.t. the characteristic connection
grad (Kirichenko's theorem -- a standard, single structural fact, not a
bridge between two papers' own bespoke constructs), so delta^g(T)=0 and

    Ric^g(X,Y) = Ric^grad(X,Y) - (1/4)*sum_i g(T(e_i,X),T(Y,e_i))

This script computes the SECOND term directly (component-wise, 6x6,
not just its trace) from C214's own verified torsion tensor, subtracts
it from C213's own verified Ricci (recomputed here at the SAME r=sqrt(3)
ambient-orthonormal scale as C214, reusing the exact calibrated code),
and checks whether the result (interpreted as Ric^grad) is isotropic
(proportional to delta_bd) -- REQUIRED by Schur's lemma since the
complement is SU(3)-irreducible (G96 Step 5b), and NOT assumed anywhere
in this script's own arithmetic. If it comes out isotropic, that is a
genuine, independent component-level consistency check of the formula's
correct application here (not merely "solving for one unknown" at the
level of a single scalar).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c215.json"


def load_module(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, HERE.parent / rel_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def commutator(A, B):
    return A @ B - B @ A


def expand_in_basis(target, basis):
    basis_flat = np.column_stack([b.flatten() for b in basis])
    target_flat = target.flatten()
    coeffs, _, _, _ = np.linalg.lstsq(basis_flat, target_flat, rcond=None)
    residual = float(np.linalg.norm(target_flat - basis_flat @ coeffs))
    max_imag = float(np.max(np.abs(coeffs.imag))) if np.iscomplexobj(coeffs) else 0.0
    assert max_imag < 1e-8
    return coeffs.real, residual


def build_structure_constants(K, H):
    n_K, n_H = len(K), len(H)
    full = K + H
    C_KKK = np.zeros((n_K, n_K, n_K))
    C_KKH = np.zeros((n_H, n_K, n_K))
    C_HKK = np.zeros((n_K, n_H, n_K))
    for b in range(n_K):
        for c in range(n_K):
            if b == c:
                continue
            coeffs, _ = expand_in_basis(commutator(K[b], K[c]), full)
            C_KKK[:, b, c] = coeffs[:n_K]
            C_KKH[:, b, c] = coeffs[n_K:]
    for i in range(n_H):
        for b in range(n_K):
            coeffs, _ = expand_in_basis(commutator(H[i], K[b]), full)
            C_HKK[b, i, :] = coeffs[:n_K]
    return C_KKK, C_KKH, C_HKK


def riemann_ricci(C_KKK, C_KKH, C_HKK, r):
    n_K, n_H = C_KKK.shape[0], C_KKH.shape[0]

    def cbold(a, b, c):
        return (
            (r[b] * r[c] / r[a]) * C_KKK[a, b, c]
            - (r[a] * r[c] / r[b]) * C_KKK[b, a, c]
            - (r[a] * r[b] / r[c]) * C_KKK[c, a, b]
        )

    def riemann(a, b, d, e):
        t1 = (
            sum(
                (r[d] * r[e] / r[c]) * cbold(a, b, c) * C_KKK[c, d, e]
                for c in range(n_K)
            )
            * 0.25
        )
        t2 = (
            sum(-C_HKK[b, i, a] * C_KKH[i, d, e] for i in range(n_H))
            * 0.5
            * r[d]
            * r[e]
        )
        t3 = sum(cbold(a, c, d) * cbold(c, b, e) for c in range(n_K)) * 0.125
        t4 = -sum(cbold(a, c, e) * cbold(c, b, d) for c in range(n_K)) * 0.125
        return t1 + t2 + t3 + t4

    ricci = np.zeros((n_K, n_K))
    for b in range(n_K):
        for d in range(n_K):
            ricci[b, d] = sum(riemann(a, b, a, d) for a in range(n_K))
    return ricci


def octonion_cross(phi, A, B):
    return np.einsum("ijk,i,j->k", phi, A, B)


def main() -> None:
    print(
        "\n=== C215: Friedrich-Ivanov Ric^g/Ric^grad/T formula, component check ===\n"
    )

    g96 = load_module("20260626-g96-s6-g2-su3/g96_g2_su3.py", "g96_g2_su3")
    phi = g96.build_phi()
    gens = g96.find_g2_generators(phi)
    N = np.zeros(7)
    N[6] = 1.0
    A = np.column_stack([G @ N for G in gens])
    _, sv, Vt = np.linalg.svd(A, full_matrices=True)
    rank = int(np.sum(sv > 1e-10))
    null = Vt[rank:]
    gm = np.array([G.flatten() for G in gens])
    su3 = [row.reshape(7, 7) for row in (null @ gm)]
    Qsu3, _ = np.linalg.qr(np.column_stack([g.flatten() for g in su3]), mode="reduced")
    comp_vecs = []
    for G in gens:
        gf = G.flatten()
        res = gf - Qsu3 @ (Qsu3.T @ gf)
        if np.linalg.norm(res) > 1e-10:
            comp_vecs.append(res)
    Qc, Rc = np.linalg.qr(np.column_stack(comp_vecs), mode="reduced")
    ncomp = int(np.sum(np.abs(np.diag(Rc)) > 1e-10))
    comp = [Qc[:, k].reshape(7, 7) for k in range(ncomp)]
    print(f"Step 1: reused G96 data, dim(su3)={len(su3)}, dim(comp)={len(comp)} [OK]")

    tangent = np.array([G @ N for G in comp])
    norm_sq = float(np.mean(np.diag(tangent @ tangent.T)))
    rescale = 1.0 / np.sqrt(norm_sq)
    unit_tangent = tangent * rescale
    assert np.max(np.abs(unit_tangent @ unit_tangent.T - np.eye(6))) < 1e-8
    print(f"Step 2: ambient-unit tangent basis confirmed (rescale={rescale:.6f})")

    # Ric^g: SAME validated Castellani code, SAME r=rescale as C214.
    C_KKK, C_KKH, C_HKK = build_structure_constants(comp, su3)
    r_ambient = rescale * np.ones(6)
    ricci_g = riemann_ricci(C_KKK, C_KKH, C_HKK, r_ambient)
    einstein_g = float(np.mean(np.diag(ricci_g)))
    print(f"Step 3: Ric^g recomputed (= C214's value): Einstein const={einstein_g:.6f}")
    assert abs(einstein_g - 2.5) < 1e-6, (
        "Mismatch with C214's own Ricci -- stop, re-check"
    )

    # Torsion T_abc in the SAME ambient-unit basis (= C214's own tensor).
    T = np.zeros((6, 6, 6))
    for a in range(6):
        for b in range(6):
            cab = octonion_cross(phi, unit_tangent[a], unit_tangent[b])
            for c in range(6):
                T[a, b, c] = -float(
                    np.dot(N, octonion_cross(phi, cab, unit_tangent[c]))
                )
    norm_T_sq = float(np.sum(T**2))
    print(f"Step 4: torsion recomputed (= C214's value): |T|^2={norm_T_sq:.6f}")
    assert abs(norm_T_sq - 24.0) < 1e-6, (
        "Mismatch with C214's own torsion -- stop, re-check"
    )

    # Friedrich-Ivanov's correction term, COMPONENT-WISE (not just the trace):
    # corr(X,Y) := -(1/4) * sum_i g(T(e_i,X),T(Y,e_i))
    #            = -(1/4) * sum_{i,k} T(e_i,X,e_k) * T(Y,e_i,e_k)
    corr = np.zeros((6, 6))
    for b in range(6):
        for d in range(6):
            corr[b, d] = -0.25 * sum(
                T[i, b, k] * T[d, i, k] for i in range(6) for k in range(6)
            )
    print(
        "\nStep 5: Friedrich-Ivanov correction term -(1/4)*sum_i g(T(e_i,X),T(Y,e_i)):"
    )
    print(f"  diag(corr) = {np.round(np.diag(corr), 6)}")
    print(f"  off-diag max = {np.max(np.abs(corr - np.diag(np.diag(corr)))):.2e}")
    trace_corr = float(np.trace(corr))
    print(
        f"  trace(corr) = {trace_corr:.6f}  (hand-derivation predicted +|T|^2/4={norm_T_sq / 4:.6f})"
    )

    # Ric^grad := Ric^g - corr  (Friedrich-Ivanov's formula, rearranged)
    ricci_grad = ricci_g - corr
    einstein_grad = float(np.mean(np.diag(ricci_grad)))
    off_diag_grad = float(np.max(np.abs(ricci_grad - np.diag(np.diag(ricci_grad)))))
    diag_spread_grad = float(np.max(np.abs(np.diag(ricci_grad) - einstein_grad)))
    print("\nStep 6: Ric^grad = Ric^g - corr (Friedrich-Ivanov's formula applied):")
    print(f"  diag(Ric^grad) = {np.round(np.diag(ricci_grad), 6)}")
    print(f"  Einstein-like constant = {einstein_grad:.6f}")
    print(
        f"  off-diagonal max = {off_diag_grad:.2e}  diag spread = {diag_spread_grad:.2e}"
    )
    print(
        "  [Schur's lemma REQUIRES both ~0 since SU(3) acts irreducibly on this 6-dim space --"
    )
    print(
        "   this is NOT assumed by this script's arithmetic, it is a genuine consistency check]"
    )

    verdict = (
        "ISOTROPIC_CONFIRMED"
        if (off_diag_grad < 1e-8 and diag_spread_grad < 1e-8)
        else "NOT_ISOTROPIC"
    )
    print(f"\n[{verdict}]")

    results = {
        "ricci_g_einstein_const": einstein_g,
        "torsion_norm_sq": norm_T_sq,
        "correction_trace": trace_corr,
        "ricci_grad_diag": np.diag(ricci_grad).tolist(),
        "ricci_grad_einstein_like_const": einstein_grad,
        "ricci_grad_off_diag_max": off_diag_grad,
        "ricci_grad_diag_spread": diag_spread_grad,
        "verdict": verdict,
        "source": "Friedrich-Ivanov arXiv:math/0102142 section 2, Ric^g=Ric^grad+(1/2)delta(T)-(1/4)sum g(T(e_i,X),T(Y,e_i))",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
