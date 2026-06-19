"""G10-B: Explicit SU(3) ↪ SO(6) — the J-preserving traceless subalgebra.

G10 recap: the compact-space spin connection of S⁶ is an SO(6) gauge field.
SO(6) contains a 9-dim J-preserving subalgebra u(3) = su(3) ⊕ u(1).
u(1) generator = J = M_{01}+M_{23}+M_{45}.
su(3) = traceless part of u(3), dim 8.

Tom's open problem (PMs p.29): "Further work is needed to understand the relation
between the unitary transformations and the orthogonal ones."

This gate constructs the 8 su(3) generators EXPLICITLY as 6×6 real antisymmetric
matrices and verifies they form su(3):
  T1 — dim = 8                              [VERIFIED-sympy]
  T2 — algebra closes in su(3)              [VERIFIED-sympy]
  T3 — J ∉ span(su3): u(1) ∩ su(3) = 0     [VERIFIED-sympy]
  T4 — Tr(Tₐ^T T_b) negative definite      [VERIFIED-numpy]
  T5 — rank = 2: Cartan dim = 2             [VERIFIED-sympy]

Scope: algebraic embedding only. Whether the SO(6) gauge FIELD reduces to this
SU(3) — the physical orthogonal→unitary step — remains Tom's open problem.
"""

import json
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "20260617-g10-s6-so6-gauge"),
)
from g10_s6_so6_gauge import complex_structure, so6_generators  # noqa: E402


def frob(A, B):
    """Frobenius inner product (1/2) Tr(A^T B)."""
    return sp.Rational(1, 2) * sp.trace(A.T * B)


def su3_generators():
    """8 explicit su(3) generators: null space of [·,J]=0 AND ⟨·,J⟩=0.

    su(3) = {X ∈ so(6) : [X,J]=0 AND Tr(X^T J)/2 = 0}
    The second constraint removes the u(1)=span{J} direction from u(3).
    Result: exactly 8 linearly independent 6×6 rational antisymmetric matrices.
    """
    mats = [M for _, M in so6_generators()]
    J = complex_structure()
    cs = sp.symbols("c0:15")
    X = sp.zeros(6, 6)
    for c, M in zip(cs, mats):
        X += c * M

    # Constraint 1: [X,J] = 0 (36 equations, from u(3))
    comm = X * J - J * X
    rows_comm = [[sp.diff(comm[i, j], c) for c in cs] for i in range(6) for j in range(6)]

    # Constraint 2: ⟨X,J⟩ = Tr(X^T J)/2 = 0 (removes u(1) from u(3) → su(3))
    frob_XJ = sp.Rational(1, 2) * sp.trace(X.T * J)
    row_frob = [[sp.diff(frob_XJ, c) for c in cs]]

    A = sp.Matrix(rows_comm + row_frob)
    null_vecs = A.nullspace()
    return [
        sp.simplify(sum((v[k] * mats[k] for k in range(15)), start=sp.zeros(6, 6)))
        for v in null_vecs
    ]


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

    su3 = su3_generators()
    J = complex_structure()
    mats = [M for _, M in so6_generators()]

    # T1: exactly 8 generators
    chk("T1_dim8", len(su3) == 8, f"dim su(3) = {len(su3)} (expect 8 = dim su(3))")

    # T2: algebra closes — every [T_a,T_b] commutes with J and is J-traceless
    # Equivalent to [T_a,T_b] ∈ su(3) ⊂ so(6)
    bad_pairs = 0
    for Ta in su3:
        for Tb in su3:
            comm = Ta * Tb - Tb * Ta
            in_u3 = sp.simplify(comm * J - J * comm) == sp.zeros(6, 6)
            traceless = sp.simplify(frob(comm, J)) == 0
            if not (in_u3 and traceless):
                bad_pairs += 1
    chk("T2_closure", bad_pairs == 0, f"all [Tₐ,T_b] ∈ su(3) ({bad_pairs} violations)")

    # T3: J has nonzero residual after projecting onto su3 span
    # i.e. J ∉ span(su3) — u(1) and su(3) are linearly independent
    J_proj_components = [frob(J, T) / frob(T, T) for T in su3]
    J_residual = sp.simplify(
        J - sum((c * T for c, T in zip(J_proj_components, su3)), start=sp.zeros(6, 6))
    )
    chk(
        "T3_J_not_in_su3",
        J_residual != sp.zeros(6, 6),
        "J ∉ span(su3) — u(1) factor is linearly independent of su(3)",
    )

    # T4: Gram matrix G_{ab} = Tr(Tₐ Tᵦ) negative definite → compact Lie algebra
    # For antisymmetric Tₐ: Tr(Tₐ Tᵦ) = -⟨Tₐ,Tᵦ⟩_F ≤ 0; negative definite confirms compactness.
    G_sym = sp.Matrix(8, 8, lambda a, b: sp.trace(su3[a] * su3[b]))
    G_np = np.array([[float(G_sym[a, b]) for b in range(8)] for a in range(8)], dtype=float)
    eigs = np.linalg.eigvalsh(G_np)
    eig_min, eig_max = float(eigs.min()), float(eigs.max())
    chk(
        "T4_compact",
        bool(np.all(eigs < 0)),
        f"Gram Tr(TₐTᵦ) neg-def: eigs in [{eig_min:.4f}, {eig_max:.4f}] < 0",
    )

    # T5: rank = 2 — Cartan subalgebra has dim 2
    # Use a GENERIC Cartan element (all pairwise different coefficients, sum=0):
    #   H_gen = 3*M_{01} - 1*M_{23} - 2*M_{45}  (a=3,b=-1,c=-2, all distinct, a+b+c=0)
    # Avoids Weyl walls where b=c (non-generic H1 gave dim 4).
    M_01 = mats[0]  # pair (0,1)
    M_23 = mats[9]  # pair (2,3)
    M_45 = mats[14]  # pair (4,5)
    H_gen = 3 * M_01 - M_23 - 2 * M_45  # a+b+c=3-1-2=0 ✓, all different ✓

    # Centralizer of H_gen in su(3): {X = sum ci Ti : [H_gen, X] = 0}
    cs = sp.symbols("x0:8")
    X_gen = sp.zeros(6, 6)
    for c, T in zip(cs, su3):
        X_gen += c * T
    comm_H1X = H_gen * X_gen - X_gen * H_gen
    B = sp.Matrix([[sp.diff(comm_H1X[i, j], c) for c in cs] for i in range(6) for j in range(6)])
    centralizer_dim = 8 - B.rank()
    chk(
        "T5_rank2",
        centralizer_dim == 2,
        f"centralizer of generic H ∈ Cartan has dim {centralizer_dim} (expect 2 = rank su(3))",
    )

    # ── Summary table ────────────────────────────────────────────────────────
    print("\nExplicit SU(3) ↪ SO(6) via J-preserving traceless generators:")
    print("  u(3) = su(3) ⊕ u(1)  where  u(1) = span{J = M₀₁+M₂₃+M₄₅}")
    print(f"  dim su(3) = {len(su3)},  rank = {centralizer_dim}")
    print("  Gram matrix negative definite → su(3) is COMPACT")
    print("  Cartan generators: H₁ = (2/3)M₀₁ − (1/3)M₂₃ − (1/3)M₄₅")
    print("                     H₂ = −(1/3)M₀₁ + (2/3)M₂₃ − (1/3)M₄₅")
    print("\nTom's gap (OPEN — not claimed here):")
    print("  Algebraic: su(3) ⊂ so(6)  [VERIFIED-sympy]")
    print("  Physical:  does SO(6) gauge field on S⁶ reduce to this SU(3)?  [OPEN per Tom p.29]")

    total = len(results)
    verdict = "PASS_G10B_SU3_EXPLICIT_EMBEDDING" if passed == total else "PARTIAL"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "G10-B-SU3-EXPLICIT",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "dim_su3": len(su3),
        "rank_su3": centralizer_dim,
        "gram_eigs": {"min": eig_min, "max": eig_max, "all_negative": bool(np.all(eigs < 0))},
        "cartan_H_generic": "3*M_01 - M_23 - 2*M_45 (all-different coefficients, generic)",
        "cartan_H_lambda3": "M_01 - M_23 (analogue of Gell-Mann lambda_3/2)",
        "cartan_H_lambda8": "M_01 + M_23 - 2*M_45 (analogue of lambda_8/sqrt3)",
        "scope": "algebraic embedding su(3) ↪ so(6); gauge-field reduction is Tom's open problem",
        "open_per_tom": "orthogonal SO(6) gauge field -> special-unitary SU(3) color (PMs p.29)",
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_g10b.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
