"""
G86A: Dual-modulus route — does T(rho6)=B*rho6^alpha with alpha!=6
give exp(-lambda/rho6^2) from the proper-time integral?

Analytic prediction (derived before numerics):
  I(rho6) = integral_0^inf dt t^{-d/2-1} exp(-T(rho6)/t)
           = Gamma(d/2) / T(rho6)^{d/2}
           = Gamma(d/2) / (B * rho6^alpha)^{d/2}
           ~ rho6^{-alpha*d/2}   [POWER LAW, not exponential]

For S6: d=6, so I(rho6) ~ rho6^{-3*alpha}

For exp(-lambda/rho6^2) to arise, we would need:
  I(rho6) ~ exp(-lambda/rho6^2)
  log I ~ -lambda/rho6^2

But log(rho6^{-3*alpha}) = -3*alpha * log(rho6) — logarithmic, not 1/rho6^2.

This is a STRUCTURAL result: Laplace-type integrals with power-law T(rho6)
ALWAYS give power-law I(rho6). The exponential exp(-lambda/rho6^2) is
incompatible with this mechanism for any finite alpha.

This gate confirms the analytic prediction numerically across alpha in [-4, 8].
"""

import numpy as np
from scipy import integrate

RHO6_VALS = np.linspace(0.7, 1.6, 60)
ALPHA_VALS = np.linspace(-4, 8, 25)  # sweep including alpha=6 (killed by G84A)
B = 1.0  # coupling constant (does not affect functional form)
D = 6  # dimension of S6


def proper_time_integral(rho6: float, alpha: float, d: int = D) -> float:
    """I(rho6) = integral_0^inf dt t^{-d/2-1} exp(-T/t), T=B*rho6^alpha"""
    T_val = B * rho6**alpha

    def integrand(t: float) -> float:
        if t < 1e-10:
            return 0.0
        return t ** (-d / 2 - 1) * np.exp(-T_val / t)

    result, _ = integrate.quad(integrand, 1e-6, 1e3, limit=200, epsabs=1e-10)
    return result


def analytic_integral(rho6: float, alpha: float, d: int = D) -> float:
    """Analytic: I = Gamma(d/2) / T^{d/2} = Gamma(d/2) / (B*rho6^alpha)^{d/2}"""
    from scipy.special import gamma

    T_val = B * rho6**alpha
    return gamma(d / 2) / T_val ** (d / 2)


# --- G1: Verify numeric = analytic for a few alpha values ---
print("=== G86A-G1: Numeric vs Analytic ===")
for alpha_test in [-2.0, 0.0, 2.0, 6.0]:
    num = proper_time_integral(1.09, alpha_test)
    ana = analytic_integral(1.09, alpha_test)
    print(
        f"  alpha={alpha_test:5.1f}: numeric={num:.4e}, analytic={ana:.4e}, ratio={num / ana:.4f}"
    )

# --- G2: For each alpha, compute I(rho6) and fit: power-law or exponential? ---
print("\n=== G86A-G2: Functional form of I(rho6) for each alpha ===")
print(f"  {'alpha':>6} | {'power_exp':>10} | {'exp_lambda':>12} | {'form':>12}")
print("  " + "-" * 50)

results = {}
for alpha in ALPHA_VALS:
    I_vals = np.array([analytic_integral(r, alpha) for r in RHO6_VALS])

    # Fit 1: power-law  log I = power_exp * log(rho6) + const
    log_rho6 = np.log(RHO6_VALS)
    log_I = np.log(np.abs(I_vals) + 1e-100)
    c_power = np.polyfit(log_rho6, log_I, 1)
    power_exp = c_power[0]

    # Fit 2: exponential  log I = -exp_lambda/rho6^2 + const
    inv_rho6_sq = 1.0 / RHO6_VALS**2
    c_exp = np.polyfit(inv_rho6_sq, log_I, 1)
    exp_lambda = -c_exp[0]

    # R^2 for both fits
    pred_power = np.polyval(c_power, log_rho6)
    pred_exp = np.polyval(c_exp, inv_rho6_sq)
    ss_tot = np.var(log_I)
    r2_power = 1 - np.var(log_I - pred_power) / ss_tot if ss_tot > 0 else 0
    r2_exp = 1 - np.var(log_I - pred_exp) / ss_tot if ss_tot > 0 else 0

    analytic_power = -3 * alpha  # expected from I ~ rho6^{-3*alpha}
    is_power_law = r2_power > 0.99
    is_exponential = r2_exp > 0.99 and abs(exp_lambda) > 0.05

    form = "EXP(-lam/rho6^2)" if is_exponential and not is_power_law else "POWER-LAW"
    results[alpha] = {
        "power_exp": power_exp,
        "analytic_power": analytic_power,
        "exp_lambda": exp_lambda,
        "r2_power": r2_power,
        "r2_exp": r2_exp,
        "form": form,
    }
    print(
        f"  {alpha:6.1f} | {power_exp:10.3f} | {exp_lambda:12.4f} | {form:>18}"
        f"  (R²_pow={r2_power:.4f}, analytic={analytic_power:.1f})"
    )

# --- G3: Summary — is there ANY alpha giving exp(-lambda/rho6^2)? ---
print("\n=== G86A-G3: Search for exp(-lambda/rho6^2) across all alpha ===")
exp_candidates = {a: v for a, v in results.items() if v["form"] == "EXP(-lam/rho6^2)"}
print(f"  Alpha values giving exp(-lambda/rho6^2): {len(exp_candidates)}")
if exp_candidates:
    for a, v in exp_candidates.items():
        print(f"    alpha={a:.2f}: lambda={v['exp_lambda']:.4f}, R2_exp={v['r2_exp']:.4f}")
else:
    print("  NONE — all alpha give power-law I(rho6) ~ rho6^{-3*alpha}")

# --- G4: Special case alpha=-2 (T~1/rho6^2 — "inverse modulus") ---
print("\n=== G86A-G4: Special case alpha=-2 (inverse modulus T ~ 1/rho6^2) ===")
alpha_inv = -2.0
I_inv = np.array([analytic_integral(r, alpha_inv) for r in RHO6_VALS])
analytic_inv = B ** (-3) * RHO6_VALS**6  # I ~ rho6^{+6} for alpha=-2
log_ratio = np.log(I_inv) - np.log(analytic_inv)
print(f"  I(rho6, alpha=-2) ~ rho6^{-3 * alpha_inv:.0f} = rho6^+6")
print(f"  Max deviation from analytic rho6^6: {np.max(np.abs(log_ratio)):.2e}")
print("  Conclusion: POWER LAW rho6^+6, not exp(-lambda/rho6^2)")

# --- VERDICT ---
print("\n=== VERDICT ===")
n_exp = len(exp_candidates)
print(f"  alpha values tested: {len(ALPHA_VALS)}")
print(f"  exp(-lambda/rho6^2) found: {n_exp}")
print()
if n_exp == 0:
    print("  => G86A: NULL")
    print("  STRUCTURAL RESULT: Laplace integral I = Gamma(d/2)/T^{d/2}")
    print("  T = B*rho6^alpha => I ~ rho6^{-3*alpha} (ALWAYS power-law)")
    print("  No alpha gives exp(-lambda/rho6^2) — incompatible mechanism.")
else:
    print("  => G86A: PROMOTE candidate — found exp(-lambda/rho6^2)")
