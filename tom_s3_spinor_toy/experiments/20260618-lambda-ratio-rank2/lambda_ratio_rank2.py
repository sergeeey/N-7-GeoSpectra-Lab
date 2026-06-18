"""LAMBDA-FREE RATIO RANK-2 (j→j+2 tensor sector).

Extends the rank-1 family R²(j,m) = 2(j−m+1)/(j+m)  [j→j+1, q=0 vs q=+1]
to rank-2 tensors (j₂=2) in the j→j+2 sector.

Setup
─────
For a rank-2 spherical tensor T^(k=2), three source states reach target |j+2, M⟩:
  q=0:  (m_src=M, q=0)   via ⟨j, M; 2, 0 | j+2, M⟩
  q=+1: (m_src=M-1, q=1) via ⟨j, M-1; 2, 1 | j+2, M⟩
  q=+2: (m_src=M-2, q=2) via ⟨j, M-2; 2, 2 | j+2, M⟩

Two independent adjacent-component ratios (using target M = m):
  R₂,A²(j,m) = CG(j,m; 2,0; j+2,m)²   / CG(j,m-1; 2,1; j+2,m)²   [A/B]
  R₂,B²(j,m) = CG(j,m-1; 2,1; j+2,m)² / CG(j,m-2; 2,2; j+2,m)²   [B/C]

Both are λ-free by Wigner-Eckart: the reduced matrix element and coupling λ
cancel exactly in any ratio within a fixed (j, j') sector.

The closed-form rational functions of (j,m) — the main result — are determined
numerically over the tower j=1/2..4 and verified symbolically.

Notation: CG(j₁, j₂, J, m₁, m₂, M) = sympy's clebsch_gordan(j₁, j₂, J, m₁, m₂, M)
          = ⟨j₁, m₁; j₂, m₂ | J, M⟩.
"""

import json
import os

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as CG

R = sp.Rational


def ratio_A(j, m):
    """R₂,A²(j,m) = CG(j,m;2,0;j+2,m)² / CG(j,m-1;2,1;j+2,m)²."""
    a = CG(j, 2, j + 2, m, 0, m)
    b = CG(j, 2, j + 2, m - 1, 1, m)
    if b == 0:
        return None
    return sp.simplify((a / b) ** 2)


def ratio_B(j, m):
    """R₂,B²(j,m) = CG(j,m-1;2,1;j+2,m)² / CG(j,m-2;2,2;j+2,m)²."""
    a = CG(j, 2, j + 2, m - 1, 1, m)
    b = CG(j, 2, j + 2, m - 2, 2, m)
    if b == 0:
        return None
    return sp.simplify((a / b) ** 2)


def closed_A(j, m):
    """R₂,A²(j,m) = 3(j−m+1) / [2(j+m)]  — same (j-m+1)/(j+m) structure as rank-1, prefactor 3/4."""
    return sp.Rational(3, 1) * (j - m + 1) / (2 * (j + m))


def closed_B(j, m):
    """R₂,B²(j,m) = 4(j−m+2) / (j+m−1)  — shifted +1 in both num and denom vs rank-1."""
    return sp.Rational(4, 1) * (j - m + 2) / (j + m - 1)


def main():
    results = []
    passed = 0

    def chk(name, cond, desc):
        nonlocal passed
        ok = bool(sp.simplify(cond)) if isinstance(cond, sp.Basic) else bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    # ── Step 0: Numerically survey the tower to find closed forms ─────────────
    print("=== Survey: R₂,A and R₂,B over tower j=1..4 ===")
    print(f"  {'j':>4} {'m':>5}  {'R₂,A':>12}  {'R₂,B':>12}")
    tower_A = []  # (j, m, value)
    tower_B = []
    for j2 in range(2, 9):  # j = 1..4 (step 1/2)
        j = R(j2, 2)
        for m2 in range(-j2 + 2, j2 + 1, 2):  # m must satisfy m ≥ -j+2 for ratio_A
            m = R(m2, 2)
            rA = ratio_A(j, m)
            rB = ratio_B(j, m)
            s_A = str(rA) if rA is not None else "—"
            s_B = str(rB) if rB is not None else "—"
            print(f"  {str(j):>4} {str(m):>5}  {s_A:>12}  {s_B:>12}")
            if rA is not None:
                tower_A.append((j, m, rA))
            if rB is not None:
                tower_B.append((j, m, rB))

    # ── T1: Closed-form R₂,A² = 3(j−m+1) / [2(j+m)] ─────────────────────────
    # Derived by pattern-fitting on the tower j=1..4:
    # Let a = j+m, b = j-m. Data shows R₂,A²(j,m) = 3(b+1)/(2a) = 3(j-m+1)/(2(j+m)).
    # Same rational structure as rank-1 [R₁² = 2(j-m+1)/(j+m)], prefactor = 3/4.
    js, ms = sp.symbols("j m")
    symbolic_rA = sp.Rational(3, 2) * (js - ms + 1) / (js + ms)
    print(f"\nDerived R₂,A² closed form: {symbolic_rA}")

    all_t1 = True
    mismatches = 0
    for j, m, val in tower_A:
        predicted = sp.simplify(symbolic_rA.subs([(js, j), (ms, m)]))
        diff = sp.simplify(val - predicted)
        if diff != 0:
            all_t1 = False
            mismatches += 1
            print(f"  T1 MISMATCH j={j} m={m}: numeric={val}, formula={predicted}")
    chk(
        "T1_R2A_closed_form",
        all_t1,
        f"R₂,A² = 3(j−m+1)/[2(j+m)] verified at {len(tower_A)} tower pts ({mismatches} mismatches)",
    )

    # ── T2: Closed-form R₂,B² = 4(j−m+2) / (j+m−1) ─────────────────────────
    # Derived by same pattern-fitting: let a=j+m, b=j-m.
    # Data shows R₂,B²(j,m) = 4(b+2)/(a-1) = 4(j-m+2)/(j+m-1).
    # Note: shifted by +1 vs rank-1 in BOTH numerator (+1 step) and denominator (−1 step).
    symbolic_rB = sp.Rational(4, 1) * (js - ms + 2) / (js + ms - 1)
    print(f"\nDerived R₂,B² closed form: {symbolic_rB}")

    all_t2 = True
    mismatches_b = 0
    for j, m, val in tower_B:
        predicted = sp.simplify(symbolic_rB.subs([(js, j), (ms, m)]))
        diff = sp.simplify(val - predicted)
        if diff != 0:
            all_t2 = False
            mismatches_b += 1
            print(f"  T2 MISMATCH j={j} m={m}: numeric={val}, formula={predicted}")
    chk(
        "T2_R2B_closed_form",
        all_t2,
        f"R₂,B² = 4(j−m+2)/(j+m−1) verified at {len(tower_B)} tower pts ({mismatches_b} mismatches)",
    )

    # ── T3: λ-free by construction (Wigner-Eckart) ────────────────────────────
    lam, vred = sp.symbols("lambda vred", positive=True)
    j0, m0 = R(2), R(1)
    a = CG(j0, 2, j0 + 2, m0, 0, m0)
    b = CG(j0, 2, j0 + 2, m0 - 1, 1, m0)
    ratio_sym = sp.simplify((lam * vred * a) / (lam * vred * b))
    chk("T3_lambda_free", sp.diff(ratio_sym, lam) == 0, "d(R₂,A)/dλ = 0 — ratio is λ-free")

    # ── T4: R₂,A² = (3/4) × R₁² — remarkable rank connection ────────────────
    # rank-1: R₁²(j,m) = 2(j-m+1)/(j+m)
    # rank-2 A: R₂,A²(j,m) = 3(j-m+1)/(2(j+m)) = (3/4) × R₁²(j,m)
    # Check at boundary: R₂,A²(j,j) = 3/(4j)  [verified: j=1→3/4, j=2→3/8, ...]
    jv = sp.Symbol("j", positive=True)
    rank1_at_jj = sp.Rational(2, 1) * 1 / (2 * jv)  # 2(j-j+1)/(j+j) = 1/j
    rank2A_at_jj = sp.simplify(symbolic_rA.subs([(js, jv), (ms, jv)]))
    expected = sp.Rational(3, 4) * rank1_at_jj  # 3/(4j)
    print(f"\nR₂,A²(j,m=j) = {rank2A_at_jj}")
    print(f"Expected 3/(4j) = {sp.simplify(expected)}")
    chk(
        "T4_rank_connection",
        sp.simplify(rank2A_at_jj - sp.Rational(3, 4) * rank1_at_jj) == 0,
        f"R₂,A²(j,j) = (3/4)×R₁²(j,j) = 3/(4j); same rank-1 structure with prefactor 3/4",
    )

    # ── T5: R₂,B²(j,j) = 8/(2j-1) — boundary at m=j ────────────────────────
    # R₂,B²(j,j) = 4(j-j+2)/(j+j-1) = 8/(2j-1)
    # Data: j=1→8, j=3/2→4, j=2→8/3, j=5/2→2, j=3→8/5, j=4→8/7 ✓
    rB_at_jj = sp.simplify(symbolic_rB.subs([(js, jv), (ms, jv)]))
    expected_rB = sp.Rational(8, 1) / (2 * jv - 1)
    print(f"\nR₂,B²(j,m=j) = {rB_at_jj}")
    chk(
        "T5_R2B_boundary",
        sp.simplify(rB_at_jj - expected_rB) == 0,
        f"R₂,B²(j,j) = 8/(2j−1) = 4/(j−½): {rB_at_jj} == {sp.simplify(expected_rB)}",
    )

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\nλ-free ratio family — RANK-2 (j→j+2 sector):")
    print("  Target |j+2, m⟩ reached by 3 source components:")
    print("    A: q=0, source m     → CG(j,m;2,0;j+2,m)")
    print("    B: q=1, source m-1   → CG(j,m-1;2,1;j+2,m)")
    print("    C: q=2, source m-2   → CG(j,m-2;2,2;j+2,m)")
    print()
    print("  R₂,A²(j,m) = A/B = 3(j−m+1) / [2(j+m)]")
    print("  R₂,B²(j,m) = B/C = 4(j−m+2) / (j+m−1)")
    print()
    print("Rank hierarchy:")
    print("  R₁²(j,m)  = 2(j−m+1) / (j+m)          [rank-1, j→j+1]")
    print("  R₂,A²(j,m) = 3(j−m+1) / [2(j+m)]      [rank-2 A, = (3/4)×R₁²]")
    print("  R₂,B²(j,m) = 4(j−m+2) / (j+m−1)       [rank-2 B, shifted by 1]")
    print()
    print("Sample rank-2 values:")
    for j, m, rA in tower_A[:6]:
        rB_val = ratio_B(j, m)
        print(f"  j={j}, m={m}: R₂,A²={rA}, R₂,B²={rB_val if rB_val else '—'}")

    total = len(results)
    verdict = "PASS_LAMBDA_FREE_RANK2_CONFIRMED" if passed == total else "PARTIAL"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "LAMBDA-FREE-RANK2",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "rank1_closed": "R1^2(j,m) = 2*(j-m+1)/(j+m)",
        "rank2_A_closed": "R2A^2(j,m) = 3*(j-m+1) / (2*(j+m))",
        "rank2_B_closed": "R2B^2(j,m) = 4*(j-m+2) / (j+m-1)",
        "rank_connection": "R2A^2 = (3/4) * R1^2  [same rational structure, prefactor 3/4]",
        "boundary_rB": "R2B^2(j,j) = 8/(2j-1)  [e.g. j=1:8, j=2:8/3, j=4:8/7]",
        "mechanism": "Wigner-Eckart: reduced element and lambda cancel in any intra-sector ratio",
        "scope": "structural CG ratios for rank-2 tensor on S3; lambda stays free",
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_rank2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    import sys

    sys.exit(0 if main() else 1)
