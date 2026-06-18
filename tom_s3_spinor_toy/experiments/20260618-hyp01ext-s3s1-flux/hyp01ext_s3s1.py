"""HYP_01-EXT: S³×S¹ flux V_eff with volume-constrained compactification modulus.

HYP_01 (origin/main) used an ad-hoc coupling κ to get a discrete λ*.
HYP_01-EXT derives the coupling from S³×S¹ topology: the volume conservation
constraint R_S3³ · R_S1 = const forces the two KK kinetic terms to compete
in a 1:(-3) ratio of φ-exponents, generating a discrete minimum without any
free parameter.

Setup
─────
S³×S¹ compact space. Volume constraint: R_S3³ · R_S1 = V_0 = const.
Parametrize with compactification modulus φ (units V_0^{1/4} = 1):
  R_S3(φ) = exp(+φ/4)
  R_S1(φ) = exp(−3φ/4)    ← from V_0 conservation (exponents in 1:−3 ratio)

KK energy (lowest modes, l=1 on S³, n=1 on S¹):
  E²_S3 = l(l+2)/R_S3² = 3 · exp(−φ/2)    [eigenvalue 1·3 = 3]
  E²_S1 = n²/R_S1²    = 1 · exp(+3φ/2)

Effective flux potential:
  V_eff(φ; N_S3, N_S1) = 3·N_S3² · exp(−φ/2)  +  N_S1² · exp(+3φ/2)

Analytic minimum (∂V/∂φ = 0):
  φ* = ln(N_S3 / N_S1)     [closed-form, no free parameter]

NOTE: φ is the compactification modulus of S³×S¹, NOT Tom's free coupling
parameter λ. They live in separate sectors. This experiment tests whether
the topology ALONE can prefer a modulus value — it can.

Scope: toy KK kinetic energy only; no dilaton, curvature, or backreaction.
"""

import json
import os

import numpy as np
from scipy.optimize import minimize_scalar


def v_eff(phi, n_s3, n_s1):
    """V_eff(φ) = 3*N_S3² exp(-φ/2) + N_S1² exp(3φ/2)."""
    return 3.0 * n_s3**2 * np.exp(-0.5 * phi) + n_s1**2 * np.exp(1.5 * phi)


def phi_star(n_s3, n_s1):
    """Analytic minimum: φ* = ln(N_S3 / N_S1)."""
    return np.log(n_s3 / n_s1)


def dv_dphi(phi, n_s3, n_s1):
    """∂V/∂φ = −3/2 · N_S3² exp(−φ/2)  +  3/2 · N_S1² exp(3φ/2)."""
    return -1.5 * n_s3**2 * np.exp(-0.5 * phi) + 1.5 * n_s1**2 * np.exp(1.5 * phi)


def d2v_dphi2(phi, n_s3, n_s1):
    """∂²V/∂φ² = 3/4 · N_S3² exp(−φ/2)  +  9/4 · N_S1² exp(3φ/2)."""
    return 0.75 * n_s3**2 * np.exp(-0.5 * phi) + 2.25 * n_s1**2 * np.exp(1.5 * phi)


def main():
    results = []
    passed = 0

    def chk(name, cond, desc):
        nonlocal passed
        ok = bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    cases = [
        (1.0, 1.0, "symmetric  N_S3=N_S1=1"),
        (2.0, 1.0, "N_S3>N_S1  2:1"),
        (1.0, 2.0, "N_S3<N_S1  1:2"),
        (3.0, 1.0, "large ratio 3:1"),
        (0.5, 2.0, "small ratio 0.5:2"),
    ]

    # ── C1: analytic φ* = ln(N_S3/N_S1) matches numeric minimizer ─────────────
    all_c1 = True
    c1_details = []
    for n_s3, n_s1, label in cases:
        phi_a = phi_star(n_s3, n_s1)
        res = minimize_scalar(v_eff, bounds=(-8, 8), method="bounded", args=(n_s3, n_s1))
        phi_n = res.x
        err = abs(phi_a - phi_n)
        c1_details.append(
            f"  {label}: φ*_analytic={phi_a:.5f}, φ*_numeric={phi_n:.5f}, err={err:.2e}"
        )
        if err > 1e-5:
            all_c1 = False
    for d in c1_details:
        print(d)
    chk(
        "C1_analytic_exact",
        all_c1,
        "φ* = ln(N_S3/N_S1) matches scipy.minimize_scalar to ≤1e-5 (5/5 cases)",
    )

    # ── C2: ∂V/∂φ = 0 at φ* and V'' > 0 (genuine minimum) ────────────────────
    all_c2 = True
    for n_s3, n_s1, label in cases:
        ps = phi_star(n_s3, n_s1)
        grad_at_min = dv_dphi(ps, n_s3, n_s1)
        v2_at_min = d2v_dphi2(ps, n_s3, n_s1)
        if abs(grad_at_min) > 1e-10 or v2_at_min <= 0:
            all_c2 = False
            print(f"  C2 FAIL {label}: grad={grad_at_min:.2e}, V''={v2_at_min:.4f}")
    chk(
        "C2_genuine_minimum",
        all_c2,
        "∂V/∂φ ≈ 0 and V'' > 0 at φ* for all 5 cases → genuine minimum",
    )

    # ── C3: falsifier — decouple S¹ (R_S1 = const) → dV/dφ < 0 everywhere ────
    # Decoupled V = 3N_S3² exp(-φ/2) + N_S1²  (S1 term constant)
    # dV/dφ = -3/2 N_S3² exp(-φ/2) < 0 for all φ → no interior minimum
    all_c3 = True
    phi_grid = np.linspace(-5, 5, 200)
    for n_s3, n_s1, label in cases:
        # Gradient of decoupled V:  only the S³ term contributes
        grad_decoupled = -1.5 * n_s3**2 * np.exp(-0.5 * phi_grid)
        if not np.all(grad_decoupled < 0):
            all_c3 = False
            print(f"  C3 FAIL {label}: decoupled gradient not always negative")
    chk(
        "C3_falsifier_decoupled",
        all_c3,
        "decouple S¹ (V_S1=const) → dV/dφ < 0 everywhere → no interior min (5/5)",
    )

    # ── C4: φ* = 0 at the symmetric point N_S3 = N_S1 ────────────────────────
    ps_symmetric = phi_star(1.0, 1.0)
    chk(
        "C4_symmetric_point",
        abs(ps_symmetric) < 1e-12,
        f"φ*(N_S3=N_S1=1) = {ps_symmetric:.2e} ≈ 0 (equal fluxes → equal radii)",
    )

    # ── C5: equipartition at φ* — V_S3/V_S1 = 3 for ALL (N_S3, N_S1) ─────────
    # Proof: V_S3(φ*)=3N_S3²(N_S1/N_S3)^{1/2}·... let's just compute:
    #   at φ* = ln(N_S3/N_S1):
    #   V_S3 = 3N_S3² exp(-φ*/2) = 3N_S3²(N_S1/N_S3)^{1/2}
    #   V_S1 = N_S1² exp(3φ*/2)  = N_S1²(N_S3/N_S1)^{3/2}
    #   V_S3/V_S1 = 3N_S3²(N_S1/N_S3)^{1/2} / [N_S1²(N_S3/N_S1)^{3/2}]
    #             = 3 · N_S3² · N_S1^{1/2}/N_S3^{1/2} · N_S1^{3/2}/N_S3^{3/2} / N_S1²
    #             = 3 · N_S3^{2-1/2-3/2} · N_S1^{1/2+3/2-2} = 3 · N_S3^0 · N_S1^0 = 3
    all_c5 = True
    ratios = []
    for n_s3, n_s1, label in cases:
        ps = phi_star(n_s3, n_s1)
        v_s3 = 3 * n_s3**2 * np.exp(-0.5 * ps)
        v_s1 = n_s1**2 * np.exp(1.5 * ps)
        r = v_s3 / v_s1
        ratios.append(r)
        if abs(r - 3.0) > 1e-9:
            all_c5 = False
            print(f"  C5 FAIL {label}: V_S3/V_S1 = {r:.6f} ≠ 3")
    chk(
        "C5_equipartition",
        all_c5,
        f"V_S3/V_S1 = {ratios[0]:.1f} at φ* for all cases (3:1 from S³ l=1 eigenvalue 1·3=3)",
    )

    # ── Summary ─────────────────────────────────────────────────────────────
    print("\nHYP_01-EXT — S³×S¹ volume-constrained flux modulus:")
    print("  Constraint: R_S3³ · R_S1 = const → exponents -φ/2 and +3φ/2 (ratio 1:−3)")
    print("  V_eff(φ) = 3·N_S3² exp(−φ/2)  +  N_S1² exp(+3φ/2)")
    print("  φ*       = ln(N_S3 / N_S1)   [closed-form, no free κ]")
    print("  V_S3/V_S1 at φ* = 3  (S³ eigenvalue 1·3=3 vs S¹ eigenvalue 1·1=1)")
    print("\nImprovement over HYP_01:")
    print("  HYP_01:    V_eff = κ N₁ N₂ f(λ) + ... (ad-hoc κ, numeric λ*≈−0.303)")
    print("  HYP_01-EXT: V_eff from volume conservation alone (closed-form φ* = ln ratio)")
    print("\nFalsifier: decouple S¹ (R_S1=const) → dV/dφ monotone → no interior min")
    print("\nScope: φ ≠ Tom's λ. This explores compactification geometry; λ stays free.")

    total = len(results)
    verdict = "PASS_HYP01EXT_S3S1_FLUX_MODULUS" if passed == total else "PARTIAL"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "HYP01EXT-S3S1-FLUX",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "v_eff": "3*N_S3^2*exp(-phi/2) + N_S1^2*exp(3*phi/2)",
        "phi_star": "ln(N_S3 / N_S1)",
        "coupling_mechanism": "S3xS1 volume conservation R_S3^3*R_S1=const (no free kappa)",
        "falsifier": "decouple S1 -> dV/dphi = -3/2*N_S3^2*exp(-phi/2) < 0 everywhere -> no minimum",
        "equipartition": "V_S3/V_S1 = 3 at phi* for all (N_S3,N_S1) [from l=1 eigenvalue 3]",
        "vs_HYP01": "HYP01 had ad-hoc kappa; HYP01-EXT derives coupling from topology alone",
        "scope": "toy KK kinetic energy; phi=compactification modulus, NOT Tom's free lambda",
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_hyp01ext.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    import sys

    sys.exit(0 if main() else 1)
