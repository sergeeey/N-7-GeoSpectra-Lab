"""G10: S⁶ spin connection → SO(6) gauge field — Tom's mechanism at s₂=6.

Tom (PMs Section 7) shows the spin connection ω̊_μX^Y of the compact factor is a
gauge field of the ORTHOGONAL group O(s₂) of that factor. His worked examples:
  s₂ = 2  → U(1)   (electromagnetism, his eq 109)
  s₂ = 3  → SU(2)  (his eq 118)  ← this is Sergey's verified S³ result.
This gate is the direct next entry of that table:
  s₂ = 6  → SO(6)  (S⁶).

What this gate VERIFIES (sympy):
  1. so(6): 15 antisymmetric generators, closed under commutator (the gauge algebra).
  2. dim so(6) = 15 = dim su(4), both rank 3  (the local iso so(6) ≅ su(4)).
  3. A complex structure J (J²=−I) on ℝ⁶ has commutant u(3) ⊂ so(6) (dim 9);
     its traceless part is su(3) (dim 8). → SU(3)×U(1) sits inside SO(6) as the
     J-preserving subgroup.
  4. J splits the vector 6 of SO(6) into eigenspaces ±i (3 each): 6 = 3 ⊕ 3̄.
     This is the SAME 3 ⊕ 3̄ as the S⁶ tangent space in G9.

THE OPEN STEP (Tom's own words, PMs p.29):
  "the gauge groups of the standard model are special unitary groups... Further work
   is needed to understand the relation between the unitary transformations and the
   orthogonal ones... and how to couple fermions directly to this model."
  → Whether the SO(6) GAUGE FIELD actually reduces to the SU(3) preserving J (giving
    color) is the orthogonal→unitary gap. This gate sets up the structure and NAMES
    the gap. It does NOT claim S⁶ → SU(3)_color.
"""

import json
import os
import sys

import sympy as sp


def so6_generators():
    """15 antisymmetric 6×6 generators M_{ab} (a<b): (M)_{ab}=+1, (M)_{ba}=−1."""
    gens = []
    for a in range(6):
        for b in range(a + 1, 6):
            M = sp.zeros(6, 6)
            M[a, b] = 1
            M[b, a] = -1
            gens.append(((a, b), M))
    return gens


def complex_structure():
    """J on ℝ⁶ pairing (0,1),(2,3),(4,5); J = M01+M23+M45, J²=−I."""
    J = sp.zeros(6, 6)
    for k in range(0, 6, 2):
        J[k, k + 1] = 1
        J[k + 1, k] = -1
    return J


def main():
    results: list[dict] = []
    passed = 0

    def chk(name, cond, desc):
        nonlocal passed
        ok = bool(sp.simplify(cond)) if isinstance(cond, sp.Basic) else bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    gens = so6_generators()
    mats = [M for _, M in gens]

    # T1: 15 antisymmetric generators
    chk(
        "T1_so6_generators",
        len(gens) == 15 and all(M.T == -M for M in mats),
        f"{len(gens)} antisymmetric so(6) generators (expect 15)",
    )

    # T2: closure — every commutator is antisymmetric (stays in so(6))
    closed = all((A * B - B * A).T == -(A * B - B * A) for A in mats for B in mats)
    chk("T2_closure", closed, "all [M_a,M_b] antisymmetric → algebra closes in so(6)")

    # T3: so(6) ≅ su(4): dim 15=15, rank 3=3
    chk(
        "T3_so6_iso_su4",
        len(gens) == 4**2 - 1,
        f"dim so(6)={len(gens)} = dim su(4)={4**2 - 1}; both rank 3 → so(6)≅su(4) [DOCS]",
    )

    # T4: complex structure J, J²=−I, J = M01+M23+M45
    J = complex_structure()
    idx = {ab: M for ab, M in gens}  # locate M01, M23, M45 explicitly
    J_combo = idx[(0, 1)] + idx[(2, 3)] + idx[(4, 5)]
    chk(
        "T4_complex_structure",
        J * J == -sp.eye(6) and sp.simplify(J - J_combo) == sp.zeros(6, 6),
        "J²=−I and J = M01+M23+M45 (the U(1) generator)",
    )

    # T5: commutant of J in so(6) = u(3) (dim 9); su(3) part = 8
    cs = sp.symbols("c0:15")
    X = sp.zeros(6, 6)
    for c, M in zip(cs, mats):
        X += c * M
    comm = X * J - J * X
    A = sp.Matrix([[sp.diff(comm[i, j], c) for c in cs] for i in range(6) for j in range(6)])
    dim_commutant = 15 - A.rank()
    chk(
        "T5_u3_commutant",
        dim_commutant == 9,
        f"dim{{X∈so(6):[X,J]=0}} = {dim_commutant} = u(3); su(3) = {dim_commutant - 1} (=8) + u(1)",
    )

    # T6: J eigenvalues ±i (×3 each) → vector 6 splits 3 ⊕ 3̄
    ev = J.eigenvals()
    n_plus = ev.get(sp.I, 0)
    n_minus = ev.get(-sp.I, 0)
    chk(
        "T6_6_to_3_3bar",
        n_plus == 3 and n_minus == 3,
        f"J eigenvalues +i×{n_plus}, −i×{n_minus} → 6 = 3 ⊕ 3̄ (matches G9 S⁶ tangent)",
    )

    # ── Mechanism parallel (Tom's table) ─────────────────────────────────────
    print("\nTom's mechanism — orthogonal gauge group from the compact-space spin connection:")
    print(f"  {'s₂':>3} {'compact':>9} {'gauge group':>14} {'# generators':>13}")
    print(f"  {'2':>3} {'2D':>9} {'U(1)':>14} {'1':>13}   (Tom eq 109, EM)")
    print(f"  {'3':>3} {'S³':>9} {'SU(2)≅SO(3)':>14} {'3':>13}   (Tom eq 118 = Sergey's S³)")
    print(f"  {'6':>3} {'S⁶':>9} {'SO(6)':>14} {'15':>13}   ← THIS GATE")

    print("\n  J-reduction (the bridge to color, OPEN per Tom p.29):")
    print("    SO(6) ⊃ U(3) = SU(3)×U(1)  (J-preserving subgroup, dim 9 = 8+1) [VERIFIED]")
    print("    vector 6 → 3 ⊕ 3̄ under that SU(3) [VERIFIED, = G9 S⁶ tangent]")
    print("    [DOCS]    J on S⁶ = its nearly-Kähler almost-complex structure (S⁶=G₂/SU(3))")
    print("    [OPEN]    does the SO(6) GAUGE FIELD reduce to this SU(3)? = orthogonal→unitary")
    print("              gap Tom names himself. NOT claimed here.")

    total = len(results)
    verdict = "PASS_G10_S6_SO6_GAUGE_STRUCTURE" if passed == total else "PARTIAL"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")
    print("  S⁶ → SO(6) gauge field (Tom's mechanism, s₂=6 analog of his SU(2) at s₂=3).")
    print("  SU(3)_color = J-reduction of SO(6); the gauge-field reduction is Tom's OPEN problem.")

    out = {
        "gate": "G10-S6-SO6-GAUGE",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "mechanism": "Tom PMs Sec 7: compact-space spin connection = O(s2) gauge field",
        "table": {"s2=2": "U(1)", "s2=3": "SU(2) (S3, Sergey)", "s2=6": "SO(6) (S6, this gate)"},
        "so6_iso_su4": "dim 15=15, rank 3=3",
        "J_commutant_dim": "9 = u(3) = su(3)(8) + u(1)(1)",
        "vector6_branch": "6 = 3 + 3bar under J-preserving SU(3) (matches G9 S6 tangent)",
        "OPEN_per_Tom": "orthogonal SO(6) -> special-unitary SU(3) reduction + fermion coupling (PMs p.29)",
        "scope": "structure setup only; does NOT claim S6 gauge field gives SU(3) color",
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_g10.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
