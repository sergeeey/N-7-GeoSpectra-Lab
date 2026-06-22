"""
G85B: Spectral saddle in proper-time integral — does it give exp(-lambda/rho6^2)?

Strategy:
1. Build heat kernel K(t, rho6) for twisted Dirac on S6 (spectral sum)
2. Find stationary point t* where dK/dt = 0 (or d(K/t)/dt = 0)
3. Evaluate K(t*, rho6) and check if form ~ A*exp(-const/rho6^2)

S6 Dirac eigenvalues (untwisted): lambda_l = +(l+3) or -(l+3), l=0,1,2,...
Degeneracy: d_l = 2 * C(l+5,5) [approx, exact from spinor bundle]
Twisted by G2 bundle: lowest eigenvalue shifted by Lichnerowicz gap (G74A: |F|/(R/4) = 8/45)
R = 30/rho6^2 for S6, so R/4 = 7.5/rho6^2
Shift: delta = |F| = (8/45) * R/4 = (8/45) * 7.5/rho6^2 = 4/3 / rho6^2
"""

import numpy as np
from fractions import Fraction

RHO6 = 1.090  # UV pole position from G57

# --- Eigenvalues of D^2 on S6 (twisted) ---
# Untwisted: lambda_l = (l+3)^2 / rho6^2,  l=0,1,2,...
# Twisting shifts the zero modes UP by delta = (8/45)*(R/4) = (8/45)*(7.5/rho6^2)
DELTA_EXACT = Fraction(8, 45) * Fraction(15, 2)  # = 8/45 * 7.5 = 4/3
print(f"Lichnerowicz shift delta = {DELTA_EXACT} = {float(DELTA_EXACT):.6f} (in units 1/rho6^2)")

L_MAX = 30  # truncate spectral sum


def degeneracy(level: int) -> int:
    """Spinor degeneracy on S6 for level-th level (approximate: full spinor bundle)."""
    from math import comb

    return 4 * comb(level + 5, 5)


def eigenvalues_sq(level: int, rho6: float, delta: float = float(DELTA_EXACT)) -> float:
    """D^2 eigenvalue for given level, including G2 twist shift at level=0."""
    base = (level + 3) ** 2 / rho6**2
    if level == 0:
        # index=3 means dim ker(D^-)=3 zero modes; for D^2 these give lambda=0
        return 0.0
    return base


def heat_kernel(t: float, rho6: float, l_max: int = L_MAX) -> float:
    """K(t, rho6) = Tr[exp(-t D^2)] = sum_level d_level * exp(-lambda_level * t)"""
    K = 0.0
    for level in range(l_max + 1):
        lam = eigenvalues_sq(level, rho6)
        d = degeneracy(level)
        K += d * np.exp(-lam * t)
    return K


def dK_dt(t: float, rho6: float, l_max: int = L_MAX) -> float:
    """dK/dt = -sum_level d_level * lambda_level * exp(-lambda_level * t)"""
    dK = 0.0
    for level in range(l_max + 1):
        lam = eigenvalues_sq(level, rho6)
        d = degeneracy(level)
        dK += d * (-lam) * np.exp(-lam * t)
    return dK


# --- G1: Is K(t) monotonic? ---
print("\n=== G85B-G1: Monotonicity of K(t) ===")
t_vals = np.logspace(-3, 3, 200)
K_vals = np.array([heat_kernel(t, RHO6) for t in t_vals])
dK_vals = np.array([dK_dt(t, RHO6) for t in t_vals])

zero_crossings = np.where(np.diff(np.sign(dK_vals)))[0]
print(f"  dK/dt sign changes: {len(zero_crossings)}")
print(f"  K(t->0+):  {K_vals[0]:.2e}")
print(f"  K(t->inf): {K_vals[-1]:.2e}  (should = N_zero_modes = {degeneracy(0)})")
print(f"  K monotonically decreasing: {len(zero_crossings) == 0}")

# --- G2: Poisson-resummed form — saddle in K_resummed(t) ---
print("\n=== G85B-G2: Poisson-resummed saddle ===")
# After Poisson resummation of geodesic winding modes on S6:
# K_resummed ~ (rho6^2/t)^3 * sum_m exp(-m^2 * rho6^2 / t)  [schematic, 6D]
# Dominant m=1 term: f(t) = (rho6^2/t)^3 * exp(-rho6^2/t)


def f_resummed(t, rho6):
    """Leading Poisson-resummed contribution (m=1 winding mode)."""
    return (rho6**2 / t) ** 3 * np.exp(-(rho6**2) / t)


def df_dt(t, rho6):
    """df/dt for leading resummed term."""
    prefactor = rho6**6
    # f = prefactor * t^{-3} * exp(-rho6^2/t)
    # df/dt = prefactor * exp(-rho6^2/t) * [-3*t^{-4} + t^{-3} * rho6^2/t^2]
    #       = prefactor * t^{-4} * exp(-rho6^2/t) * [-3 + rho6^2/t]
    return prefactor * t ** (-4) * np.exp(-(rho6**2) / t) * (-3 + rho6**2 / t)


# Saddle: df/dt = 0 => -3 + rho6^2/t = 0 => t* = rho6^2/3
t_star = RHO6**2 / 3
f_star = f_resummed(t_star, RHO6)
print(f"  Saddle t* = rho6^2/3 = {t_star:.4f}")
print(f"  f_resummed(t*) = {f_star:.4e} > 0: {f_star > 0}")

# At the saddle, what is the exponential factor?
exp_at_saddle = np.exp(-(RHO6**2) / t_star)
print(f"  exp(-rho6^2/t*) at saddle = exp(-3) = {exp_at_saddle:.4f}")
print("  This is a CONSTANT (exp(-3)), NOT exp(-lambda/rho6^2)")

# --- G3: Does f(t*) depend on rho6 as exp(-const/rho6^2)? ---
print("\n=== G85B-G3: rho6-dependence at the saddle ===")
rho6_vals = np.linspace(0.8, 1.5, 50)
t_stars = rho6_vals**2 / 3
f_stars = np.array([f_resummed(ts, r) for ts, r in zip(t_stars, rho6_vals)])

# Fit log(f_star) vs 1/rho6^2
inv_rho6_sq = 1.0 / rho6_vals**2
log_f_stars = np.log(f_stars)
coeffs = np.polyfit(inv_rho6_sq, log_f_stars, 1)
lambda_fit = -coeffs[0]
print(f"  Fit: log f(t*) = {coeffs[0]:.4f}/rho6^2 + {coeffs[1]:.4f}")
print(f"  Fitted lambda (coeff of -1/rho6^2): {lambda_fit:.4f}")
print("  Expected for exp(-lambda/rho6^2): lambda > 0")
print("  Actual form: f(t*) ~ rho6^0 * exp(-3) = CONSTANT * rho6^-0")

# The polynomial dependence
coeffs_poly = np.polyfit(np.log(rho6_vals), np.log(f_stars), 1)
print(f"  Power-law fit: f(t*) ~ rho6^{coeffs_poly[0]:.2f} (NOT exponential in 1/rho6^2)")

# --- G4: Saddle of full effective action integrand K(t)/t^(1+p) ---
print("\n=== G85B-G4: Saddle of effective action integrand K(t)/t ===")
integrand = K_vals / t_vals
d_integrand = np.diff(integrand)
crossings_integrand = np.where(np.diff(np.sign(d_integrand)))[0]
print(f"  d(K/t)/dt sign changes: {len(crossings_integrand)}")
if len(crossings_integrand) > 0:
    t_saddle = t_vals[crossings_integrand[0]]
    K_saddle = heat_kernel(t_saddle, RHO6)
    print(f"  Saddle at t* ~ {t_saddle:.4f}, K(t*) = {K_saddle:.4e}")
else:
    print("  K(t)/t is monotonically decreasing — no interior saddle")

# --- VERDICT ---
print("\n=== VERDICT ===")
saddle_exists = t_star > 0 and f_star > 0
bridge_to_exp = abs(lambda_fit) > 0.01  # Would need lambda >> 0 for exp(-lambda/rho6^2)
# The fit lambda_fit should be near 0 since f(t*) ~ rho6^0 * const
print(f"  Saddle t* exists: {saddle_exists} (t* = rho6^2/3)")
print(f"  K(t*) > 0: {f_star > 0}")
print(f"  Form is exp(-lambda/rho6^2): {bridge_to_exp}")
print()

# Check claim conditions
if saddle_exists and f_star > 0:
    print("  PASS condition: saddle exists, K(t*)>0 ✓")
else:
    print("  FAIL condition: no saddle")

if not bridge_to_exp or abs(lambda_fit) < 0.1:
    print("  BRIDGE MISSING: saddle gives exp(-3)=const, NOT exp(-lambda/rho6^2)")
    print("  => G85B: NULL — saddle exists but wrong functional form")
    print("     Same conclusion as G85A via different language")
else:
    print("  Bridge found: PROMOTE candidate")
