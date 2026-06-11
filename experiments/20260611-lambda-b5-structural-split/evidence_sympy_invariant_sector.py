"""LAMBDA-B5-G0 evidence: the invariant one-form sector is annihilated by the
Ben Achour E/E' combination at the constant seed (L = 0).

Claim verified here (see claim.md in this folder):
    For Phi = 1 (constant scalar seed, L = 0):
        B  = *d(Phi xi~)  = -2 xi~     C  = *d B  = +4 xi~     E  = (L+2)B + C  == 0
        B' = *d(Phi xi~') = +2 xi~'    C' = *d B' = +4 xi~'    E' = (L+2)B' - C' == 0
    Hence the invariant (Killing) one-forms lie OUTSIDE the E/E' tower and a
    Dereli-style spin-connection sector cannot be reached by tuning c_i^I.

Conventions (pinned to preserve-branch code, ben_achour_one_form_modes.py + test_p13a1):
    Metric       ds^2 = dalpha^2 + cos^2(alpha) dtheta^2 + sin^2(alpha) dphi^2
    Orientation  vol  = + sin(alpha) cos(alpha) dalpha ^ dtheta ^ dphi
    Seeds (code killing_one_form, coordinate components in (alpha, theta, phi)):
        xi~  = ( 0,  cos^2 a,  sin^2 a )   dual of  d_phi + d_theta
        xi~' = ( 0, -cos^2 a,  sin^2 a )   dual of  d_phi - d_theta
    Seed eigenvalues (code test convention): *d xi~ = -2 xi~ ,  *d xi~' = +2 xi~'

Standalone: requires only sympy. Run from this folder:
    python evidence_sympy_invariant_sector.py
Exit code 0 = all checks pass. Writes results.json next to this file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

a, t, p = sp.symbols("alpha theta phi", real=True)

METRIC = sp.diag(1, sp.cos(a) ** 2, sp.sin(a) ** 2)  # coordinate basis (alpha, theta, phi)
SQRT_G = sp.sin(a) * sp.cos(a)  # orientation: vol = +sqrt(g) da^dt^dp


def d_one_form(w: tuple) -> tuple:
    """Exterior derivative: 1-form (w_a, w_t, w_p) -> 2-form (F_at, F_ap, F_tp)."""
    w_a, w_t, w_p = w
    return (
        sp.diff(w_t, a) - sp.diff(w_a, t),
        sp.diff(w_p, a) - sp.diff(w_a, p),
        sp.diff(w_p, t) - sp.diff(w_t, p),
    )


def star_two_form(F: tuple) -> tuple:
    """Hodge star 2-form -> 1-form under vol = +sqrt(g) da^dt^dp.

    Derived via the orthonormal coframe e1=da, e2=cos(a)dt, e3=sin(a)dp with
    *(e1^e2)=e3, *(e2^e3)=e1, *(e3^e1)=e2.
    """
    F_at, F_ap, F_tp = F
    return (
        F_tp / SQRT_G,
        -F_ap * sp.cos(a) / sp.sin(a),
        F_at * sp.sin(a) / sp.cos(a),
    )


def star_d(w: tuple) -> tuple:
    return tuple(sp.simplify(c) for c in star_two_form(d_one_form(w)))


def is_zero(w: tuple) -> bool:
    return all(sp.simplify(c) == 0 for c in w)


def lin(w: tuple, k) -> tuple:
    return tuple(k * c for c in w)


def add(u: tuple, w: tuple) -> tuple:
    return tuple(x + y for x, y in zip(u, w))


XI = (sp.Integer(0), sp.cos(a) ** 2, sp.sin(a) ** 2)  # xi~
XIP = (sp.Integer(0), -(sp.cos(a) ** 2), sp.sin(a) ** 2)  # xi~' (code sign convention)

checks: dict[str, bool] = {}

# --- 1. Seeds are the metric duals of the Killing vectors -------------------
v_xi = sp.Matrix([0, 1, 1])  # d_phi + d_theta in (alpha, theta, phi) ordering
v_xip = sp.Matrix([0, -1, 1])  # d_phi - d_theta
dual_xi = tuple((METRIC * v_xi)[i] for i in range(3))
dual_xip = tuple((METRIC * v_xip)[i] for i in range(3))
checks["dual_of_xi_equals_seed_xi"] = all(sp.simplify(x - y) == 0 for x, y in zip(dual_xi, XI))
checks["dual_of_xi_prime_equals_seed_xi_prime"] = all(
    sp.simplify(x - y) == 0 for x, y in zip(dual_xip, XIP)
)

# --- 2. Seed *d eigenvalues (pin to preserve-branch test convention) --------
checks["star_d_xi_eq_minus_2_xi"] = is_zero(add(star_d(XI), lin(XI, 2)))
checks["star_d_xi_prime_eq_plus_2_xi_prime"] = is_zero(add(star_d(XIP), lin(XIP, -2)))

# --- 3. MAIN RESULT: constant seed Phi = 1 (L = 0) annihilated --------------
L0 = 0
B0 = star_d(XI)  # Phi = 1
C0 = star_d(B0)
E0 = add(lin(B0, L0 + 2), C0)  # E = (L+2)B + C
checks["B0_eq_minus_2_xi"] = is_zero(add(B0, lin(XI, 2)))
checks["C0_eq_plus_4_xi"] = is_zero(add(C0, lin(XI, -4)))
checks["E_at_L0_vanishes_identically"] = is_zero(E0)

B0p = star_d(XIP)
C0p = star_d(B0p)
E0p = add(lin(B0p, L0 + 2), lin(C0p, -1))  # E' = (L+2)B' - C'
checks["B0_prime_eq_plus_2_xi_prime"] = is_zero(add(B0p, lin(XIP, -2)))
checks["C0_prime_eq_plus_4_xi_prime"] = is_zero(add(C0p, lin(XIP, -4)))
checks["E_prime_at_L0_vanishes_identically"] = is_zero(E0p)

# --- 4. POSITIVE CONTROL: L = 2 scalar mode produces a NONZERO E mode -------
PHI2 = sp.cos(2 * a)
laplacian = -sp.simplify(sp.diff(SQRT_G * sp.diff(PHI2, a), a) / SQRT_G)
checks["phi2_is_L2_scalar_eigenmode_ev_8"] = sp.simplify(laplacian - 8 * PHI2) == 0
B2 = star_d(tuple(PHI2 * c for c in XI))
C2 = star_d(B2)
E2 = add(lin(B2, 2 + 2), C2)  # L = 2
checks["E_at_L2_is_nonzero"] = not is_zero(E2)

# --- Report ------------------------------------------------------------------
all_pass = all(checks.values())
print("LAMBDA-B5-G0 evidence checks")
print("=" * 60)
for name, ok in checks.items():
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print("=" * 60)
print(f"E (L=0)  components: {[sp.simplify(c) for c in E0]}")
print(f"E'(L=0)  components: {[sp.simplify(c) for c in E0p]}")
print(f"E (L=2)  theta-component (nonzero): {sp.simplify(E2[1])}")
print(f"OVERALL: {'ALL PASS' if all_pass else 'FAILURES PRESENT'}")

results = {
    "gate": "LAMBDA-B5-G0",
    "verdict": "STRUCTURAL_SPLIT_REQUIRED" if all_pass else "EVIDENCE_SCRIPT_FAILED",
    "date": "2026-06-11",
    "conventions": {
        "metric": "dalpha^2 + cos^2(alpha) dtheta^2 + sin^2(alpha) dphi^2",
        "orientation": "vol = +sin(alpha)cos(alpha) dalpha^dtheta^dphi",
        "seed_xi": "(0, cos^2 a, sin^2 a)",
        "seed_xi_prime": "(0, -cos^2 a, sin^2 a)",
        "E_formula": "E = (L+2)*B + C;  E' = (L+2)*B' - C'",
    },
    "checks": checks,
    "primary_result": {
        "B_L0": "-2 xi~",
        "C_L0": "+4 xi~",
        "E_L0": "0 (identically)",
        "B_prime_L0": "+2 xi~'",
        "C_prime_L0": "+4 xi~'",
        "E_prime_L0": "0 (identically)",
    },
    "positive_control": {
        "seed": "Phi = cos(2 alpha), L = 2 scalar eigenmode (Delta eigenvalue 8)",
        "E_L2_nonzero": bool(checks["E_at_L2_is_nonzero"]),
    },
    "lambda_status": {
        "lambda_total": "NOT fixed (P14 no-go intact for the mode sector)",
        "lambda_geom": "conditionally canonical IF V_omega identified with geometric "
        "Dirac spin-connection term (modeling choice - Tom Q3)",
        "mode_coefficients": "free",
    },
}

out = Path(__file__).resolve().parent / "results.json"
out.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(f"results written: {out}")

sys.exit(0 if all_pass else 1)
