"""
G86B: Warp factor Omega(y) route — can Omega(y)!=1 in the metric
give exp(-lambda/rho6^2) in the 4D effective potential?

Physics setup (10D SUGRA warped ansatz):
  ds^2 = e^{2A(y)} eta_munu dx^mu dx^nu + g_mn(y) dy^m dy^n
  Warp equation: nabla^2_{S^6} e^{4A(y)} = |F(y)|^2 - <|F|^2>_{S^6}

Three exhaustive cases:
  Case 1: Uniform G2 flux -> |F|^2 = const -> source = 0 -> A = const
          (harmonic functions on compact S^6 are constants)
  Case 2: Localized source (D-brane charge Q at y0)
          e^{4A}(y) ~ 1 + Q*G_{S^6}(y,y0), G~1/r^4
          4D correction ~ rho6^2 (POWER-LAW), not exp(-lambda/rho6^2)
          AND new free parameter Q introduced -> FAIL condition
  Case 3: Postulated A = -lambda/(4*rho6^2)
          rho6 is a GLOBAL modulus -> A constant on S^6 -> nabla^2 = 0
          -> source must = 0 -> identical to Case 1 -> circular

FALSIFIER conditions (from ALIVE_BRANCHES.md):
  PASS: Omega-contribution gives exp(-const/rho6^2) WITHOUT new free parameters
  FAIL: Omega introduces a new free parameter, OR contribution is power-law
"""

import numpy as np
from scipy import integrate

RHO6_VALS = np.linspace(0.5, 2.0, 80)

# --- G1: Uniform flux -> trivial warp ---
print("=== G86B-G1: Uniform G2 flux on S^6 ===")
print("  Warp equation: nabla^2_{S^6} e^{4A} = |F|^2 - <|F|^2>_{S^6}")
print("  For G2-invariant uniform flux: |F|^2 = const everywhere on S^6")
print("  => RHS = const - const = 0 at every point")
print("  => nabla^2_{S^6} e^{4A} = 0 on compact S^6")
print("  => e^{4A} = const  [harmonic functions on connected compact Riemannian")
print("     manifold without boundary are constants — standard Hopf lemma]")
print("  => A = const  (trivial warp, absorbed into rho6 rescaling)")
print()
print("  RESULT: Uniform G2 flux => CONSTANT warp factor => NO exp(-lambda/rho6^2)")

# --- G2: Localized source -> Green function on S^6 -> polynomial correction ---
print()
print("=== G86B-G2: Localized D-brane source — charge Q at y0 on S^6 ===")
print("  Green function on S^6 (d=6): G(r) ~ C / r^{d-2} = C / r^4")
print("  Warp factor: e^{4A}(y) ~ 1 + Q * G(|y - y0|)")
print()
print("  4D Planck mass correction:")
print("  delta M_Pl^2 ~ int_{S^6} d^6y sqrt(g6) * e^{2A}")
print("  ~ Q/2 * int d^6y G(r) ~ Q/2 * Omega_5 * int_0^{rho6} r^5 * r^{-4} dr")
print("  = Q/2 * Omega_5 * int_0^{rho6} r dr = Q/2 * Omega_5 * rho6^2 / 2")
print("  => delta M_Pl^2 ~ Q * rho6^2  [POWER-LAW, not exp(-lambda/rho6^2)]")
print()


def correction_from_source(rho6: float, Q: float = 1.0, r_min: float = 0.03) -> float:
    """4D Planck mass correction from point source: integral of G(r)*r^5 dr * Omega_5"""
    omega5 = 2.0 * np.pi**3
    result, _ = integrate.quad(lambda r: omega5 * r**5 / r**4, r_min, rho6)
    return Q * result


corrections = np.array([correction_from_source(r) for r in RHO6_VALS])

# Fit: power-law vs exponential
log_rho6 = np.log(RHO6_VALS)
log_corr = np.log(corrections)
inv_rho6_sq = 1.0 / RHO6_VALS**2

c_pow = np.polyfit(log_rho6, log_corr, 1)
c_exp = np.polyfit(inv_rho6_sq, log_corr, 1)
pred_pow = np.polyval(c_pow, log_rho6)
pred_exp = np.polyval(c_exp, inv_rho6_sq)
ss_tot = np.var(log_corr)
r2_pow = 1 - np.var(log_corr - pred_pow) / ss_tot
r2_exp = 1 - np.var(log_corr - pred_exp) / ss_tot if ss_tot > 0 else 0.0

print("  Numerical fit:")
print(f"    Power-law rho6^p: p = {c_pow[0]:.4f}, R^2 = {r2_pow:.6f}")
print(f"    Exp(-lam/rho6^2): lam = {-c_exp[0]:.4f}, R^2 = {r2_exp:.6f}")
analytic_power = 2.0  # from int r dr ~ rho6^2
print(f"    Analytic exponent: p = {analytic_power:.1f}")
print()
print(f"  RESULT: POWER-LAW (R^2={r2_pow:.4f}) vs exp (R^2={r2_exp:.4f})")
print("  FAIL condition: new free parameter Q introduced + power-law form")

# --- G3: Postulated exp warp is y-independent -> trivial ---
print()
print("=== G86B-G3: Postulated e^{4A} = exp(-lambda/rho6^2) ===")
print("  rho6 is a GLOBAL modulus — it is the RADIUS of S^6.")
print("  It takes the same value at every point y in S^6.")
print("  => e^{4A} = exp(-lambda/rho6^2) is CONSTANT on S^6 as a function of y.")
print("  => nabla^2_{S^6}[exp(-lambda/rho6^2)] = 0")
print("  => Warp equation: 0 = source => source = 0")
print("  => Identical to Case 1 (trivial constant warp factor)")
print()
print("  This is CIRCULAR: postulating A ~ 1/rho6^2 does not DERIVE it.")
print("  It merely renames the Freund-Rubin vacuum energy as a 'warp factor'.")
print()
print("  RESULT: exp(-lambda/rho6^2) warp is trivial (constant on S6)")

# --- G4: Direct comparison of all three cases ---
print()
print("=== G86B-G4: V_eff(rho6) from each case at rho6_min = 1.09 ===")
print()
print(
    f"  {'rho6':>6} | {'Case1: const A':>14} | {'Case2: point src':>16} | {'Case3: postulate':>16}"
)
print("  " + "-" * 58)
for rho6 in [0.7, 0.9, 1.09, 1.18, 1.5]:
    v1 = rho6**6
    v2 = rho6**6 + correction_from_source(rho6)
    v3 = rho6**6  # identical to Case 1 — constant warp rescales into rho6
    print(f"  {rho6:6.2f} | {v1:14.4f} | {v2:16.4f} | {v3:16.4f}")

print()
print("  Case 1 == Case 3: IDENTICAL — postulated exp(-lambda/rho6^2)")
print("  is constant on S6 => absorbed into case 1 (trivial)")
print("  Case 2: polynomial deviation ~rho6^2, not exponential, + free Q")

# --- Verdict ---
print()
print("=== VERDICT ===")
print()
# PASS requires: exp form WITHOUT free params.
# Case 1: A=const (trivial) — no exp. Case 3: circular — no exp.
# Case 2: power-law (R^2_pow=1.0) >> exp (R^2_exp=0.88), plus free Q.
# All three cases fail PASS condition => NULL.
pow_wins = (r2_pow - r2_exp) > 0.05  # power-law clearly better
case2_has_free_param = True  # Q always introduced
trivial_cases = True  # cases 1 and 3 are trivially non-exp
verdict = "NULL" if (pow_wins and case2_has_free_param and trivial_cases) else "OPEN"
print(f"  G86B: {verdict}")
print()
print("  Falsifier result:")
print("    Case 1 gives exp(-lambda/rho6^2) without free params: NO (A=const)")
print(f"    Case 2 gives exp form: NO (power-law, R^2_pow={r2_pow:.4f})")
print("    Case 2 free param introduced: YES (Q) — FAIL condition met")
print("    Case 3 is non-trivial: NO (circular / trivial)")
print()
print("  STRUCTURAL CONCLUSION:")
print("  The warp factor on compact S^6 CANNOT generate exp(-lambda/rho6^2)")
print("  from 10D supergravity equations without a new free parameter.")
print()
print("  Lambda-map: G83 + G84A/B + G85A/B + G86A/B = ENTIRE spectral/geometric")
print("  class EXHAUSTED. exp(-lambda/rho6^2) is non-perturbative in origin.")
print("  lambda = FREE_COUPLING_PARAMETER (hard fence maintained).")
