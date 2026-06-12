"""LAMBDA-B5-V-RATIO-G0: λ-free ratio gate.

Within a fixed sector (j_L_in, j_L_out, j_R) of the S³ V-operator (J_L=1, J_R=0),
all matrix elements share the same reduced element vred and the same geometric factor.
The ratio M_a/M_b = CG_a/CG_b — λ cancels exactly.

For the (j_L=1/2→j_L=3/2) sector, the ratio equals √2 — a structural prediction
that requires neither λ nor V-normalization to state.

Standalone: uses only sympy (no preserve-branch imports).
"""

import json
import os
import sys

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

# ── Symbols ──────────────────────────────────────────────────────────────────
lam = sp.Symbol("lambda", positive=True)
vred = sp.Symbol("vred", positive=True)  # shared reduced matrix element (sector-invariant)
pi = sp.pi

results: list[dict] = []
_passed = 0


def chk(name: str, cond: object, desc: str) -> bool:
    global _passed
    if isinstance(cond, sp.Basic):
        ok = bool(sp.simplify(cond))
    else:
        ok = bool(cond)
    results.append({"check": name, "pass": ok, "desc": desc})
    status = "PASS" if ok else "FAIL"
    print(f"{status} {name}: {desc}")
    if ok:
        _passed += 1
    return ok


def _cg(j1, j2, j3, m1, m2, m3) -> sp.Expr:
    """Wrapper: clebsch_gordan(j1, j2, j3, m1, m2, m3) = <j1,m1;j2,m2|j3,m3>."""
    return clebsch_gordan(
        sp.Rational(int(round(2 * j1)), 2),
        sp.Rational(int(round(2 * j2)), 2),
        sp.Rational(int(round(2 * j3)), 2),
        sp.Rational(int(round(2 * m1)), 2),
        sp.Rational(int(round(2 * m2)), 2),
        sp.Rational(int(round(2 * m3)), 2),
    )


def geom_factor(j_src: float, j_tgt: float, j_R_src: float, j_R_tgt: float) -> sp.Expr:
    """Geometric prefactor from P11 oracle: sqrt((2*j_src+1)*3/(2*j_tgt+1)) × sqrt((2*j_R_src+1)/(2*j_R_tgt+1))."""
    left = sp.sqrt(
        sp.Rational(int(round(2 * j_src)) + 1, 1) * 3 / sp.Rational(int(round(2 * j_tgt)) + 1, 1)
    )
    right = sp.sqrt(
        sp.Rational(int(round(2 * j_R_src)) + 1, 1) / sp.Rational(int(round(2 * j_R_tgt)) + 1, 1)
    )
    return sp.simplify(left * right)


def sector_elements(j_in: float, j_out: float, j_R: float) -> list[tuple[float, float, sp.Expr]]:
    """Return all (m_in, m_out, CG) for a sector with nonzero CG."""
    elements = []
    for m_in_2 in range(int(-2 * j_in), int(2 * j_in) + 1):
        m_in = m_in_2 / 2.0
        for q in (-1, 0, 1):
            m_out = m_in + q
            if abs(m_out) <= j_out + 1e-9:
                cg_val = _cg(j_in, 1, j_out, m_in, q, m_out)
                if cg_val != 0:
                    elements.append((m_in, m_out, cg_val))
    return elements


# ═══════════════════════════════════════════════════════════════════════════
# SECTOR A: j_L_in=1, j_L_out=1, j_R=1/2  (within k=1 positive branch)
# ═══════════════════════════════════════════════════════════════════════════
print("\n── SECTOR A: j_L = 1→1, j_R = 1/2 ──")
A_elements = sector_elements(j_in=1.0, j_out=1.0, j_R=0.5)
A_geom = geom_factor(j_src=1.0, j_tgt=1.0, j_R_src=0.5, j_R_tgt=0.5)
print(f"Geometric factor (sector A): {A_geom}")
print(f"Nonzero CG elements in sector A: {len(A_elements)}")
for m_in, m_out, cg_val in A_elements:
    M_sym = lam * vred * A_geom * cg_val
    print(f"  M({m_in:+.1f}→{m_out:+.1f}) = λ·vred·{A_geom}·{cg_val} = {sp.simplify(M_sym)}")

# ── T1: ≥2 nonzero CG elements in sector A ──────────────────────────────────
chk("T1", len(A_elements) >= 2, f"Sector A: {len(A_elements)} nonzero CG elements (≥2 required)")

# ── T2: Ratio in sector A = CG_a/CG_b (pure number) ─────────────────────────
# Take first two elements
cg_A1, cg_A2 = A_elements[0][2], A_elements[1][2]
M_A1 = lam * vred * A_geom * cg_A1
M_A2 = lam * vred * A_geom * cg_A2
R_A = sp.simplify(M_A1 / M_A2)
R_A_from_cg = sp.simplify(cg_A1 / cg_A2)
print(f"\nSector A ratio R = M_A1/M_A2 = {R_A}")
print(f"CG_a/CG_b = {R_A_from_cg}")
chk("T2", sp.Eq(R_A, R_A_from_cg), f"R = M_a/M_b = CG_a/CG_b = {R_A} (λ·vred·geom cancel)")

# ── T3: dR/dλ = 0 (λ-free) ───────────────────────────────────────────────────
dR_A_dlam = sp.diff(R_A, lam)
chk("T3", sp.Eq(dR_A_dlam, 0), "dR_A/dλ = 0 — sector A ratio is λ-free")

# ═══════════════════════════════════════════════════════════════════════════
# SECTOR B: j_L_in=1/2, j_L_out=3/2, j_R=1  (k=1 neg → k=2 pos)
# Non-trivial ratio: CG values are not all equal magnitude
# ═══════════════════════════════════════════════════════════════════════════
print("\n── SECTOR B: j_L = 1/2→3/2, j_R = 1 ──")
B_elements = sector_elements(j_in=0.5, j_out=1.5, j_R=1.0)
B_geom = geom_factor(j_src=0.5, j_tgt=1.5, j_R_src=1.0, j_R_tgt=1.0)
print(f"Geometric factor (sector B): {B_geom}")
print(f"Nonzero CG elements in sector B: {len(B_elements)}")
for m_in, m_out, cg_val in B_elements:
    M_sym = lam * vred * B_geom * cg_val
    print(f"  M({m_in:+.1f}→{m_out:+.1f}) = λ·vred·{B_geom}·{cg_val}")

# Filter to fixed target m_out = 1/2 (two source rows reach this column)
B_col_half = [
    (m_in, m_out, cg_val) for m_in, m_out, cg_val in B_elements if abs(m_out - 0.5) < 1e-9
]
print(f"\nFixed m_tgt=1/2 column in sector B: {len(B_col_half)} elements")
for m_in, m_out, cg_val in B_col_half:
    print(f"  CG({m_in:+.1f}→+0.5) = {cg_val}")

# ── T4: ≥2 nonzero CG in sector B column m_tgt=1/2 ──────────────────────────
chk(
    "T4",
    len(B_col_half) >= 2,
    f"Sector B m_tgt=1/2 column: {len(B_col_half)} elements (≥2 required)",
)

# ── T5: Ratio = √2 exactly ────────────────────────────────────────────────────
# The LARGER CG is for (m_src=+1/2, q=0): diagonal-type, <1/2,+1/2;1,0|3/2,1/2> = sqrt(6)/3
# The SMALLER CG is for (m_src=-1/2, q=1): raising,      <1/2,-1/2;1,1|3/2,1/2> = sqrt(3)/3
# R = larger/smaller = CG(m_src=+1/2) / CG(m_src=-1/2) = sqrt(6)/3 / (sqrt(3)/3) = sqrt(2)
cg_B_m_neg = _cg(0.5, 1, 1.5, -0.5, 1, 0.5)  # <1/2,-1/2;1,1|3/2,1/2> = sqrt(3)/3 (smaller)
cg_B_m_pos = _cg(0.5, 1, 1.5, 0.5, 0, 0.5)  # <1/2,+1/2;1,0|3/2,1/2> = sqrt(6)/3 (larger)
print(f"\ncg_B(m_src=-1/2→m_tgt=+1/2) = {cg_B_m_neg}  [smaller]")
print(f"cg_B(m_src=+1/2→m_tgt=+1/2) = {cg_B_m_pos}  [larger]")
R_B = sp.simplify(cg_B_m_pos / cg_B_m_neg)  # larger/smaller = sqrt(2)
print(f"Ratio R = CG_larger/CG_smaller = {cg_B_m_pos}/{cg_B_m_neg} = {R_B}")
chk("T5", sp.Eq(R_B**2, 2), f"R² = (CG_larger/CG_smaller)² = 2 → R = √2 exactly (got R = {R_B})")

# ── T6: R ≠ ±1 (non-trivial structural prediction) ───────────────────────────
chk(
    "T6",
    sp.Ne(R_B**2, 1),
    f"Sector B ratio R = {R_B} ≠ ±1 — non-trivial structural prediction",
)

# ── T7: dR/dλ = 0 for sector B ratio (R is pure CG ratio, λ-free) ─────────────
M_B1 = lam * vred * B_geom * cg_B_m_pos  # M for larger CG (m_src=+1/2)
M_B2 = lam * vred * B_geom * cg_B_m_neg  # M for smaller CG (m_src=-1/2)
R_B_full = sp.simplify(M_B1 / M_B2)  # = sqrt(2) after λ·vred·geom cancel
dR_B_dlam = sp.diff(R_B_full, lam)
chk("T7", sp.Eq(dR_B_dlam, 0), f"dR_B/dλ = 0 — sector B ratio {R_B_full} is λ-free")

# ── Summary ──────────────────────────────────────────────────────────────────
total = len(results)
print(f"\n{_passed}/{total} checks passed")

verdict = "PASS_LAMBDA_FREE_RATIO_CONFIRMED" if _passed == total else "PARTIAL"

# Additional structural info
print("\nKey structural ratios:")
print(f"  Sector A (j=1→1, j_R=1/2): CG ratio = {sp.simplify(cg_A1 / cg_A2)} (trivial ±1)")
print(f"  Sector B (j=1/2→3/2, j_R=1): CG ratio (m_tgt=1/2) = {R_B} = √2 (NON-TRIVIAL)")
print(f"  Sector B geom factor = {B_geom}")
print(f"  CG_B(m_src=-1/2→m_tgt=1/2) = {cg_B_m_neg}")
print(f"  CG_B(m_src=+1/2→m_tgt=1/2) = {cg_B_m_pos}")

out = {
    "gate": "LAMBDA-B5-V-RATIO-G0",
    "verdict": verdict,
    "passed": _passed,
    "total": total,
    "sector_A": {
        "j_L_in": 1.0,
        "j_L_out": 1.0,
        "j_R": 0.5,
        "nonzero_elements": len(A_elements),
        "geom_factor": str(A_geom),
        "representative_ratio": str(sp.simplify(cg_A1 / cg_A2)),
    },
    "sector_B": {
        "j_L_in": 0.5,
        "j_L_out": 1.5,
        "j_R": 1.0,
        "nonzero_elements": len(B_elements),
        "col_m_tgt_half": len(B_col_half),
        "geom_factor": str(B_geom),
        "cg_m_neg": str(cg_B_m_neg),
        "cg_m_pos": str(cg_B_m_pos),
        "ratio": str(R_B),
        "ratio_squared": str(sp.simplify(R_B**2)),
    },
    "key_result": (
        "R = CG_a/CG_b — λ cancels in ratio. "
        "Sector B: R(m_tgt=1/2) = √2 — non-trivial structural prediction independent of λ."
    ),
    "lambda_status": "FREE_COUPLING_PARAMETER — confirmed free in ratio (dR/dλ=0)",
    "GEOMETRY_AGNOSTIC": True,
    "safe_for_runtime": False,
    "checks": results,
}

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_v_ratio_g0.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

print(f"\nVerdict: {verdict}")
print(f"Saved: {out_path}")
sys.exit(0 if _passed == total else 1)
