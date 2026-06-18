"""LAMBDA-FREE RATIO FAMILY (generalises V-RATIO-G0's single √2).

V-RATIO-G0 showed ONE λ-free ratio: R = √2 in the sector (j_L=1/2→3/2, m_tgt=1/2).
Mechanism (Wigner-Eckart): within a fixed irreducible vector-operator sector, every
matrix element is (reduced element) × (geometric factor) × (Clebsch-Gordan), so any
RATIO of two elements = ratio of CG coefficients — the coupling λ and the reduced
element cancel exactly.

This gate computes the CLOSED FORM of the whole family, of which √2 is one entry.

For the vector-operator (rank-1) raising sector j → j+1, fixed target m, the two
sources reaching m are (m_src=m, q=0) and (m_src=m−1, q=+1). Their ratio is:

        R²(j, m) = 2 (j − m + 1) / (j + m)            [closed form, derived below]

Derivation (standard CG for j→j+1):
    <j,m;1,0|j+1,m>²   = ((j+1)²−m²) / [(j+1)(2j+1)]
    <j,m−1;1,1|j+1,m>² = (j+m)(j+m+1) / [(2j+1)(2j+2)]
    ratio² = 2((j+1)²−m²) / [(j+m)(j+m+1)] = 2(j−m+1)/(j+m)   (since (j+1+m)=(j+m+1))

Verified two independent ways below: (1) symbolic proof for general (j,m);
(2) numeric match against sympy's clebsch_gordan over the whole tower j=1/2..3.
"""

import json
import os
import sys

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as CG

R = sp.Rational


def R2_closed(j, m):
    """Closed-form λ-free ratio² for the j→j+1 vector sector at target m."""
    return sp.simplify(2 * (j - m + 1) / (j + m))


def R2_from_cg(j, m):
    """Same ratio² computed directly from Clebsch-Gordan coefficients."""
    a = CG(j, 1, j + 1, m, 0, m)  # <j,m; 1,0 | j+1,m>
    b = CG(j, 1, j + 1, m - 1, 1, m)  # <j,m-1; 1,1 | j+1,m>
    if b == 0:
        return None
    return sp.simplify((a / b) ** 2)


def main():
    results: list[dict] = []
    passed = 0

    def chk(name: str, cond: object, desc: str) -> bool:
        nonlocal passed
        ok = bool(sp.simplify(cond)) if isinstance(cond, sp.Basic) else bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    # ── T1: symbolic proof for general (j,m) ─────────────────────────────────
    js, ms = sp.symbols("j m", positive=True)
    cgA2 = ((js + 1) ** 2 - ms**2) / ((js + 1) * (2 * js + 1))  # <j,m;1,0|j+1,m>²
    cgB2 = ((js + ms) * (js + ms + 1)) / ((2 * js + 1) * (2 * js + 2))  # <j,m-1;1,1|j+1,m>²
    symbolic_ratio = sp.simplify(cgA2 / cgB2)
    chk(
        "T1_symbolic",
        sp.simplify(symbolic_ratio - 2 * (js - ms + 1) / (js + ms)) == 0,
        f"general (j,m): CG-ratio² = {symbolic_ratio} = 2(j−m+1)/(j+m)",
    )

    # ── T2: numeric match against clebsch_gordan over the whole tower ─────────
    checked = 0
    mismatches = 0
    for j2 in range(1, 7):  # j = 1/2 .. 3
        j = R(j2, 2)
        for m2 in range(-j2, j2 + 1, 2):
            m = R(m2, 2)
            cg = R2_from_cg(j, m)
            if cg is None:
                continue
            checked += 1
            if sp.simplify(cg - R2_closed(j, m)) != 0:
                mismatches += 1
                print(f"  MISMATCH j={j} m={m}: CG={cg} closed={R2_closed(j, m)}")
    chk(
        "T2_numeric",
        mismatches == 0,
        f"closed form matches CG at all {checked} tower points (0 mismatches)",
    )

    # ── T3: √2 special case (consistency with V-RATIO-G0) ─────────────────────
    r2_half = R2_closed(R(1, 2), R(1, 2))
    chk("T3_sqrt2", sp.Eq(r2_half, 2), f"R²(1/2,1/2) = {r2_half} → R = √2 (recovers V-RATIO-G0)")

    # ── T4: ratios are λ-free by construction ─────────────────────────────────
    lam, vred, geom = sp.symbols("lambda vred geom", positive=True)
    j0, m0 = R(3, 2), R(1, 2)
    a = CG(j0, 1, j0 + 1, m0, 0, m0)
    b = CG(j0, 1, j0 + 1, m0 - 1, 1, m0)
    ratio = sp.simplify((lam * vred * geom * a) / (lam * vred * geom * b))
    chk("T4_lambda_free", sp.diff(ratio, lam) == 0, "d(M_a/M_b)/dλ = 0 — ratio is λ-free")

    # ── T5: ≥3 NON-TRIVIAL new ratios (R ≠ 1) beyond √2 ───────────────────────
    predictions = []
    for j, m in [(R(1), R(0)), (R(3, 2), R(3, 2)), (R(2), R(0)), (R(2), R(-1))]:
        r2 = R2_closed(j, m)
        predictions.append((j, m, r2, sp.sqrt(r2)))
    nontrivial = [p for p in predictions if sp.simplify(p[2] - 1) != 0]
    chk(
        "T5_new_predictions",
        len(nontrivial) >= 3,
        f"{len(nontrivial)} non-trivial NEW λ-free ratios (R≠1)",
    )

    # ── Report ────────────────────────────────────────────────────────────────
    print("\nλ-free ratio family  R²(j,m) = 2(j−m+1)/(j+m):")
    print(f"  {'j':>4} {'m':>5} {'R²':>8} {'R':>12}")
    print(f"  {'1/2':>4} {'1/2':>5} {'2':>8} {'√2':>12}   ← V-RATIO-G0 (known)")
    for j, m, r2, r in predictions:
        tag = "  (trivial)" if sp.simplify(r2 - 1) == 0 else "   ← NEW"
        print(f"  {str(j):>4} {str(m):>5} {str(r2):>8} {str(r):>12}{tag}")

    total = len(results)
    verdict = "PASS_LAMBDA_FREE_RATIO_FAMILY_CONFIRMED" if passed == total else "PARTIAL"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "LAMBDA-FREE-RATIO-FAMILY",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "closed_form": "R^2(j,m) = 2*(j-m+1)/(j+m)",
        "generalises": "V-RATIO-G0 single ratio R=sqrt(2) = R(j=1/2,m=1/2)",
        "new_predictions": {
            f"j={str(j)},m={str(m)}": str(sp.sqrt(r2)) for j, m, r2, _ in predictions
        },
        "lambda_status": "FREE_COUPLING_PARAMETER — cancels in every ratio (Wigner-Eckart)",
        "scope": "structural ratios of S3 vector-operator matrix elements; λ-free; NOT a coupling/observable prediction",
        "checks": results,
    }
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "results_lambda_free_family.json"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
