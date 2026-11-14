"""C214: check the torsion-Ricci relation for S6's nearly-Kahler structure,
bridging C212 (torsion, |T|^2=8/9 in G96's Frobenius-generator basis) and
C213 (Ricci, Einstein const=5/6, SAME basis, r=1) via a SINGLE common,
explicitly ambient-normalized basis -- rather than hand-deriving a rescaling
bridge after the fact (a first attempt at that, by hand, gave an unexplained
factor-of-2 discrepancy against Russo's theorem below; redoing it directly,
in code, is the safe fix, not further hand algebra).

Source for the exact relation (full text, not abstract): Russo,
"The Einstein condition on nearly Kahler six-manifolds", arXiv:2002.04673,
section 3-4: Ric_g = 5*mu^2*g (Theorem, their Prop 3.9 + section 4 proof),
with mu defined by Lemma 3.1: ||(grad_X J)Y||^2 = mu^2*(...).
Derived here (shown in this file's own docstring below) from Russo's own
definitions: ||T^c||^2 = 24*mu^2 for an ORTHONORMAL frame, giving
    Ric_g = (5/24) * ||T^c||^2        [BOTH sides for the SAME g-orthonormal frame]

Derivation of ||T^c||^2=24mu^2 (not restated from any source, worked out
directly from Russo's Lemma 3.1 + the T^c=<(grad_X J)(JY),Z> formula shared
by Agricola-Borowka-Friedrich -- both already read in full this session):
for X,Y ranging over an orthonormal basis, sum_Z T^c(X,Y,Z)^2 = ||(grad_X
J)(JY)||^2 = mu^2(||X||^2||Y||^2 - g(X,Y)^2 - sigma(X,Y)^2) [same formula,
Y->JY leaves the RHS invariant since g(X,JY)^2=sigma(X,Y)^2 and
sigma(X,JY)^2=g(X,Y)^2 for an orthogonal J]. Summing X,Y over an
orthonormal basis of dim 6: sum(1) - sum(delta_ij) - sum(sigma(e_i,e_j)^2)
= 36 - 6 - 6 = 24 (the last sum uses Parseval: sum_j sigma(e_i,e_j)^2 =
||J e_i||^2 = 1 for each i).

CRITICAL finding that motivated this round: G96's complement generators
K_a (Frobenius-orthonormal, i.e. Tr(K_a^T K_a)=1) do NOT give ambient-
orthonormal tangent vectors when pushed through the orbit map v_a=K_a@N --
checked directly: Gram(v_a,v_b)=(1/3)*delta_ab, not delta_ab. C212's |T|^2
and C213's Ricci (r=1) were each computed in their OWN basis (C212: the
v_a as given, norm^2=1/3 each; C213: K_a treated as unit per Castellani's
own g=delta_ab*V^aV^b convention) -- NEITHER is the ambient-orthonormal
frame Russo's theorem requires. This round recomputes BOTH quantities in
a single, explicitly ambient-orthonormal basis (r=sqrt(3) uniform
rescaling of the SAME G96 generators, chosen so that r*K_a@N has ambient
unit norm, verified numerically below before trusting anything downstream).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c214.json"


def load_module(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, HERE.parent / rel_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_g96_data():
    g96 = load_module("20260626-g96-s6-g2-su3/g96_g2_su3.py", "g96_g2_su3")
    phi = g96.build_phi()
    gens = g96.find_g2_generators(phi)
    e6 = np.zeros(7)
    e6[6] = 1.0
    A = np.column_stack([G @ e6 for G in gens])
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
    return phi, gens, su3, comp, e6


def octonion_cross(phi: np.ndarray, A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return np.einsum("ijk,i,j->k", phi, A, B)


def main() -> None:
    print("\n=== C214: torsion-Ricci relation check, single ambient-normalized basis ===\n")

    phi, _gens, su3, comp, N = build_g96_data()

    tangent_unit = np.array([G @ N for G in comp])
    gram = tangent_unit @ tangent_unit.T
    print("Step 1: Gram matrix of v_a=K_a@N under ambient R^7 dot product:")
    print(
        f"  diag={np.round(np.diag(gram), 6)}  off-diag max={np.max(np.abs(gram - np.diag(np.diag(gram)))):.2e}"
    )
    norm_sq = float(np.mean(np.diag(gram)))
    print(
        f"  -> ||v_a||^2 = {norm_sq:.6f} (expect 1/3) -- generators are NOT ambient-unit as given"
    )
    assert abs(norm_sq - 1.0 / 3.0) < 1e-8, (
        "Unexpected normalization -- re-check before trusting anything below"
    )

    rescale = 1.0 / np.sqrt(norm_sq)  # = sqrt(3)
    print(
        f"  Rescale factor to reach ambient-unit tangent vectors: {rescale:.6f} (expect sqrt(3)={np.sqrt(3):.6f})"
    )

    # === Torsion, recomputed directly in the ambient-orthonormal basis ===
    unit_tangent = tangent_unit * rescale
    gram_check = unit_tangent @ unit_tangent.T
    assert np.max(np.abs(gram_check - np.eye(6))) < 1e-8, "unit_tangent not ambient-orthonormal"
    print("Step 2: unit_tangent verified ambient-orthonormal (Gram=I to 1e-8)")

    T = np.zeros((6, 6, 6))
    for a in range(6):
        for b in range(6):
            cab = octonion_cross(phi, unit_tangent[a], unit_tangent[b])
            for c in range(6):
                T[a, b, c] = -float(np.dot(N, octonion_cross(phi, cab, unit_tangent[c])))
    asym_err = max(
        abs(T[a, b, c] + T[b, a, c]) for a in range(6) for b in range(6) for c in range(6)
    )
    norm_T_sq = float(np.sum(T**2))
    print(
        f"Step 3: torsion in ambient-orthonormal basis: |T|^2={norm_T_sq:.6f}, antisym err={asym_err:.2e}"
    )
    print(f"  (expect exactly 27x C212's value: 27 * 8/9 = {27 * 8 / 9:.6f} -- scaling check)")
    assert abs(norm_T_sq - 27 * 8 / 9) < 1e-8, (
        "Torsion rescaling does not match the predicted 27x factor"
    )

    # === Ricci, recomputed with the SAME rescaling applied to Castellani's r ===
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
                sum((r[d] * r[e] / r[c]) * cbold(a, b, c) * C_KKK[c, d, e] for c in range(n_K))
                * 0.25
            )
            t2 = sum(-C_HKK[b, i, a] * C_KKH[i, d, e] for i in range(n_H)) * 0.5 * r[d] * r[e]
            t3 = sum(cbold(a, c, d) * cbold(c, b, e) for c in range(n_K)) * 0.125
            t4 = -sum(cbold(a, c, e) * cbold(c, b, d) for c in range(n_K)) * 0.125
            return t1 + t2 + t3 + t4

        ricci = np.zeros((n_K, n_K))
        for b in range(n_K):
            for d in range(n_K):
                ricci[b, d] = sum(riemann(a, b, a, d) for a in range(n_K))
        return ricci

    C_KKK, C_KKH, C_HKK = build_structure_constants(comp, su3)
    r_ambient = rescale * np.ones(6)
    ricci_ambient = riemann_ricci(C_KKK, C_KKH, C_HKK, r_ambient)
    einstein_ambient = float(np.mean(np.diag(ricci_ambient)))
    off_diag = float(np.max(np.abs(ricci_ambient - np.diag(np.diag(ricci_ambient)))))
    print(f"\nStep 4: Ricci recomputed with r={rescale:.6f} (ambient-unit rescaling):")
    print(f"  Einstein constant = {einstein_ambient:.6f}  off-diag max={off_diag:.2e}")
    print(
        f"  (C213's r=1 value was 5/6={5 / 6:.6f}; expect this to scale by 1/rescale^2=1/3: "
        f"{(5 / 6) / (rescale**2):.6f})"
    )

    # === Final check: Russo's Ric=5mu^2, |T^c|^2=24mu^2  =>  Ric=(5/24)|T^c|^2 ===
    mu_sq_from_T = norm_T_sq / 24.0
    predicted_ricci = 5.0 * mu_sq_from_T
    print(f"\nStep 5 [THE CHECK]: mu^2 from |T^c|^2/24 = {mu_sq_from_T:.6f}")
    print(f"  Russo predicts Ric = 5*mu^2 = {predicted_ricci:.6f}")
    print(f"  This round's directly-computed Ricci (ambient basis) = {einstein_ambient:.6f}")
    rel_err = abs(predicted_ricci - einstein_ambient) / abs(predicted_ricci)
    print(f"  Relative error = {rel_err:.4%}")

    verdict = "CONFIRMED" if rel_err < 1e-6 else "MISMATCH"
    print(f"\n[{verdict}]")

    results = {
        "ambient_norm_sq_raw": norm_sq,
        "rescale_factor": rescale,
        "torsion_norm_sq_ambient": norm_T_sq,
        "torsion_antisym_err": asym_err,
        "ricci_einstein_const_ambient": einstein_ambient,
        "ricci_off_diag_max": off_diag,
        "mu_sq_from_torsion": mu_sq_from_T,
        "ricci_predicted_from_russo": predicted_ricci,
        "relative_error": rel_err,
        "verdict": verdict,
        "source": "Russo arXiv:2002.04673 (Ric=5mu^2) + derivation (this file) of |T^c|^2=24mu^2",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
