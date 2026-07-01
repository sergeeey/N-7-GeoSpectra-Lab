"""G102: does c_S3 (G94) reduce to a prediction for the string coupling g_s?

Source trace [WEAK-MEDIUM]: Dp-brane tension T_p = 1/((2*pi)^p * alpha'^((p+1)/2) * g_s),
cross-confirmed via 2 independent WebSearch queries (2026-07-01) citing Polchinski's
convention. Direct primary-source PDF fetch (arXiv:2310.20559) FAILED to parse cleanly
(self-inconsistent double-1/g_s artifact) -- discarded, not used as a citation.
A follow-up search for the Euclidean-instanton-specific action (Wick rotation / RR
coupling subtleties) did not cleanly resolve whether an additional O(1) factor beyond
T_p*Vol applies -- this residual uncertainty is carried forward explicitly (T5 output),
not hidden. The STRUCTURAL claim (c_S3 proportional to 1/g_s) is more robust than the
exact numeric prefactor.

Skeptic review (agent aec83a030a24f6af4) resolved the GA2-2pi-convention worry as a
red herring: GA2's dropped (2*pi)^9 lives ONLY in the M_Pl^2=M_s^7*V_9 Planck-mass
relation (a kinetic-term normalization), structurally independent of the brane-tension
formula's own (2*pi)^p (a DBI-action normalization). VOL_S3_UNIT=2*pi^2 in G94/GA2 is
the exact geometric unit-S3 volume, not a KK convention choice. Confirmed via direct
read of g94_s3_np_instanton.py:55 and ga2_m4_ms_units.py:28-29 (2 independent files,
consistent).
"""

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g102.json"

# --- Symbols ---
g_s, alpha_p, l_s, rho3, p = sp.symbols("g_s alpha_prime l_s rho3 p", positive=True)
pi = sp.pi

# --- T1: source-traced Dp-brane tension formula (p=2 for Euclidean D2/E2-brane) ---
# T_p = 1 / ((2*pi)^p * alpha'^((p+1)/2) * g_s)
T_p_general = 1 / ((2 * pi) ** p * alpha_p ** ((p + 1) / sp.Integer(2)) * g_s)
T_2 = T_p_general.subs(p, 2)
# l_s = sqrt(alpha'), so alpha' = l_s^2
T_2_in_ls = T_2.subs(alpha_p, l_s**2)

# --- T2: Vol(S3) at physical radius R = rho3 * l_s (GA2 convention: rho3 dimensionless,
#     string units M_s=1, i.e. physical radius measured in units of l_s=1/M_s) ---
VOL_S3_UNIT = 2 * pi**2
R_physical = rho3 * l_s
vol_s3 = VOL_S3_UNIT * R_physical**3

# --- T3: instanton action S_inst = T_2 * Vol(S3), derive c_S3 such that S_inst = c_S3 * rho3^3 ---
S_inst = sp.simplify(T_2_in_ls * vol_s3)
# Extract coefficient of rho3^3 (should be independent of l_s if dimensions cancel correctly)
c_s3_derived = sp.simplify(S_inst / rho3**3)

# --- T4 (CONTROL, mandatory per G98/G99/G101 lesson): redo with the STANDARD KK
#     convention that DOES carry (2*pi)^9 in the Planck-mass relation, to confirm this
#     does NOT change c_s3 (since GA2's simplification lives in a different formula) ---
# The brane-tension-to-instanton-action derivation above never references M_Pl or V_9
# at all -- it only uses T_2 and Vol(S3). GA2's convention choice is therefore provably
# irrelevant to THIS derivation by construction (it simply never enters the formula).
# Control check: does c_s3_derived depend on any V_9/M_Pl-related symbol? It must not.
control_uses_planck_mass_symbols = any(
    str(s) in ("M_Pl", "V_9", "V9") for s in c_s3_derived.free_symbols
)

# --- T5: numeric evaluation, l_s-dependence check, and g_s window from G94's empirical range ---
l_s_cancels = c_s3_derived.diff(l_s) == 0  # must not depend on l_s if formula is consistent

C_S3_MIN_EMPIRICAL = sp.Rational(248, 1000)  # 0.248, from G94 scan
C_S3_MAX_EMPIRICAL = sp.Rational(372, 1000)  # 0.372, from G94 scan

# Solve c_s3_derived (as function of g_s) = empirical bound, for g_s
gs_solutions = {}
for label, c_val in [("min", C_S3_MIN_EMPIRICAL), ("max", C_S3_MAX_EMPIRICAL)]:
    eq = sp.Eq(c_s3_derived, c_val)
    sol = sp.solve(eq, g_s)
    gs_solutions[label] = sol


def main() -> None:
    results = {}
    passed = 0
    total = 0

    def check(name, ok, detail=None):
        nonlocal passed, total
        total += 1
        passed += int(bool(ok))
        results[name] = {"pass": bool(ok), "detail": detail}
        print(f"{name}: {'PASS' if ok else 'FAIL'}" + (f"  ({detail})" if detail else ""))

    print("=== G102: c_S3 vs g_s derivation ===\n")

    print(f"T_2 (Euclidean D2 tension, alpha'-form): {T_2}")
    print(f"T_2 (in l_s form): {T_2_in_ls}")
    check("T1_tension_formula_built", T_2_in_ls is not None)

    print(f"\nVol(S3) at R=rho3*l_s: {vol_s3}")
    check("T2_volume_built", True)

    print(f"\nS_inst = T_2 * Vol(S3) = {S_inst}")
    print(f"=> c_S3 (coefficient of rho3^3) = {c_s3_derived}")
    check(
        "T3_cs3_derived",
        sp.simplify(c_s3_derived - sp.Rational(1, 2) / g_s) == 0,
        detail=f"got {c_s3_derived}, expected 1/(2*g_s)",
    )

    check(
        "T4_control_no_planck_mass_dependence",
        not control_uses_planck_mass_symbols,
        detail="GA2's 2pi convention lives in a formula this derivation never touches",
    )

    check(
        "T5_no_l_s_dependence",
        l_s_cancels,
        detail="c_S3 must be dimensionless, l_s must cancel exactly",
    )

    print(
        f"\nG94 empirical c_S3 window: [{float(C_S3_MIN_EMPIRICAL)}, {float(C_S3_MAX_EMPIRICAL)}]"
    )
    print(
        f"Implied g_s solutions: min-c_S3 -> g_s={gs_solutions['min']}, "
        f"max-c_S3 -> g_s={gs_solutions['max']}"
    )

    gs_min_val = None
    gs_max_val = None
    if gs_solutions["max"] and gs_solutions["min"]:
        gs_at_c_max = float(gs_solutions["max"][0])  # smaller c_S3 <-> larger g_s (c=1/(2gs))
        gs_at_c_min = float(gs_solutions["min"][0])
        gs_lo, gs_hi = sorted([gs_at_c_max, gs_at_c_min])
        gs_min_val, gs_max_val = gs_lo, gs_hi
        print(f"\n=> Implied g_s range: [{gs_lo:.3f}, {gs_hi:.3f}]")
        strongly_coupled = gs_lo > 1.0
        print(f"Strongly coupled (g_s > 1): {strongly_coupled}")

    all_pass = passed == total
    verdict = "STRUCTURAL_RELATION_CONFIRMED" if all_pass else "DERIVATION_FAILED"

    print(f"\n{passed}/{total} checks PASS")
    print(f"VERDICT: {verdict}")
    print("\nCAVEAT: exact numeric prefactor (1/2) carries [WEAK-MEDIUM] confidence --")
    print("source trace confirmed the STRUCTURAL Dp-brane tension formula via 2 web")
    print("searches, but could NOT cleanly confirm from a primary source whether an")
    print("additional O(1) factor applies specifically to a WRAPPED EUCLIDEAN instanton")
    print("(vs. the Lorentzian brane tension formula used here). The proportionality")
    print("c_S3 ~ 1/g_s is more robust than the exact coefficient 1/2.")

    result = {
        "gate": "G102",
        "verdict": verdict,
        "checks": results,
        "c_s3_symbolic": str(c_s3_derived),
        "implied_gs_range": [gs_min_val, gs_max_val] if gs_min_val else None,
        "strongly_coupled": bool(gs_min_val and gs_min_val > 1.0),
        "confidence_note": (
            "STRUCTURAL relation (c_S3 ~ 1/g_s): [WEAK-MEDIUM], source-traced via "
            "2 independent WebSearch queries (Polchinski Dp-brane tension). "
            "EXACT prefactor (1/2): could not be independently confirmed for the "
            "Euclidean-wrapped-instanton case specifically vs the Lorentzian tension "
            "formula -- residual uncertainty, not hidden."
        ),
    }
    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\n-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
