"""G12: Gauge anomaly cancellation for the S³×S⁶ 32-component spinor.

Verifies all 5 standard SM anomaly conditions for the one-generation fermion
content identified in G6/G11.  This is a NECESSARY CONDITION for mathematical
consistency — it does NOT prove the quantum numbers come from geometry.

Fermion content (one SM generation — 16 left-handed Weyl dof, 16 right = 32):

  Q_L = (3, 2)_{+1/6}   quark doublet        6 Weyl components
  u_R = (3, 1)_{+2/3}   right up quark       3 Weyl components
  d_R = (3, 1)_{-1/3}   right down quark     3 Weyl components
  L_L = (1, 2)_{-1/2}   lepton doublet       2 Weyl components
  e_R = (1, 1)_{-1}     right electron       1 Weyl component
  ν_R = (1, 1)_{0}      right neutrino       1 Weyl component  (sterile, Y=0)
  ─────────────────────────────────────────────
  Total left-handed Weyl: 6+3+3+2+1+1 = 16   ×2 CPT conjugates = 32 = G6 ✓

Connection to G11 quantum numbers:
  J₃ (SU(2)_L): ±1/2 → doublet vs singlet (from G11, 8+8+16 pattern)
  K₃ (SU(2)_R): ±1/2 → right-handed doublet vs singlet
  C_i (SU(3)_c): color, from G10-B→G11 spinor lift
  Y = T3R + (B−L)/2  (Pati-Salam decomposition; B−L not yet geometric)

Convention: work with LEFT-HANDED Weyl fermions.
  Chirality chi = +1 for left-handed, −1 for right-handed.
  Each right-handed fermion ψ_R counted as chi=−1.

Gates:
  T1  [SU(3)]³                   = 0   (QCD cubic, fermion-type counting)
  T2  [SU(2)]³                   = 0   (automatic: SU(2) pseudo-real)
  T3  [SU(2)]² × U(1)_Y          = 0
  T4  [SU(3)]² × U(1)_Y          = 0
  T5  [U(1)_Y]³                  = 0
  T6  [grav]²   × U(1)_Y         = 0
"""

import json
import os
import sys

import sympy as sp
from sympy import Rational as R

# ── Fermion table ─────────────────────────────────────────────────────────────
# Each entry: (name, SU3_dim, SU2_dim, Y, chi)
#   SU3_dim: 3 = fundamental, 1 = singlet
#   SU2_dim: 2 = doublet,     1 = singlet
#   Y:       U(1)_Y hypercharge (rational)
#   chi:     +1 left-handed, -1 right-handed

FERMIONS = [
    ("Q_L", 3, 2, R(1, 6), +1),
    ("u_R", 3, 1, R(2, 3), -1),
    ("d_R", 3, 1, R(-1, 3), -1),
    ("L_L", 1, 2, R(-1, 2), +1),
    ("e_R", 1, 1, R(-1, 1), -1),
    ("nu_R", 1, 1, R(0, 1), -1),
]

# Verify total Weyl component count = 16 (×2 CPT = 32)
WEYL_COUNT = sum(su3 * su2 for _, su3, su2, _, _ in FERMIONS)
assert WEYL_COUNT == 16, f"Expected 16 Weyl dof, got {WEYL_COUNT}"


# ── Anomaly coefficient functions ────────────────────────────────────────────
# Index of fundamental SU(N) representation: T(fund) = 1/2.


def A_su3_cubic() -> sp.Rational:
    """[SU(3)]³: chi × dim(SU2) × T(SU3) summed over SU(3) triplets."""
    return sum(chi * su2 * R(1, 2) for _, su3, su2, Y, chi in FERMIONS if su3 == 3)


def A_su2_cubic() -> int:
    """[SU(2)]³: automatic zero because SU(2) is pseudo-real (real reps)."""
    return 0


def A_su2_sq_u1() -> sp.Rational:
    """[SU(2)]² × U(1)_Y: chi × dim(SU3) × T(SU2) × Y, summed over SU(2) doublets."""
    return sum(chi * su3 * R(1, 2) * Y for _, su3, su2, Y, chi in FERMIONS if su2 == 2)


def A_su3_sq_u1() -> sp.Rational:
    """[SU(3)]² × U(1)_Y: chi × dim(SU2) × T(SU3) × Y, summed over SU(3) triplets."""
    return sum(chi * su2 * R(1, 2) * Y for _, su3, su2, Y, chi in FERMIONS if su3 == 3)


def A_u1_cubic() -> sp.Rational:
    """[U(1)_Y]³: chi × dim(SU3) × dim(SU2) × Y³."""
    return sum(chi * su3 * su2 * Y**3 for _, su3, su2, Y, chi in FERMIONS)


def A_grav_sq_u1() -> sp.Rational:
    """[grav]² × U(1)_Y: chi × dim(SU3) × dim(SU2) × Y."""
    return sum(chi * su3 * su2 * Y for _, su3, su2, Y, chi in FERMIONS)


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> bool:
    results = []
    passed = 0

    def chk(name: str, val: sp.Basic, desc: str) -> bool:
        nonlocal passed
        ok = bool(val == 0)
        results.append({"check": name, "value": str(val), "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}  [value = {val}]")
        if ok:
            passed += 1
        return ok

    print(f"Fermion table: {len(FERMIONS)} multiplets, {WEYL_COUNT} Weyl dof (×2 CPT = 32)\n")

    chk("T1_SU3_cubic", A_su3_cubic(), "[SU(3)]³ anomaly")
    chk("T2_SU2_cubic", A_su2_cubic(), "[SU(2)]³ anomaly (auto: pseudo-real)")
    chk("T3_SU2sq_U1", A_su2_sq_u1(), "[SU(2)]² × U(1)_Y anomaly")
    chk("T4_SU3sq_U1", A_su3_sq_u1(), "[SU(3)]² × U(1)_Y anomaly")
    chk("T5_U1_cubic", A_u1_cubic(), "[U(1)_Y]³ anomaly")
    chk("T6_grav_sq_U1", A_grav_sq_u1(), "[grav]² × U(1)_Y anomaly")

    total = len(results)
    verdict = "PASS_G12_ANOMALY_FREE" if passed == total else f"PARTIAL_{passed}_of_{total}"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "G12-ANOMALY-CHECK",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "weyl_count": WEYL_COUNT,
        "interpretation": (
            "All 5 SM gauge anomaly conditions satisfied for one-generation "
            "32-component spinor from G6/G11. NECESSARY CONDITION confirmed. "
            "Does NOT prove Y assignment is geometric."
        ),
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_g12.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
