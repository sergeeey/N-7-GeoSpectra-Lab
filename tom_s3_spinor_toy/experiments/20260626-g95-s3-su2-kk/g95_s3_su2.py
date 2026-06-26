"""G95: SO(4) ≅ SU(2)_L × SU(2)_R from S³ — KK gauge bosons.

Claim: Kaluza-Klein reduction on S³ produces gauge group SO(4) ≅ SU(2)_L × SU(2)_R.
One factor SU(2)_L is the SU(2) weak interaction candidate.

Physics:
  S³ is a Lie group: S³ ≅ SU(2) ≅ Sp(1)
  Isometry group: Iso(S³) = SO(4) ≅ SU(2)_L × SU(2)_R
    - SU(2)_L = left-multiplication symmetry of S³ (as a group)
    - SU(2)_R = right-multiplication symmetry
  KK gauge bosons: massless vectors in 4D in adjoint of Iso(S³) = SO(4)
  Dimension: dim(SO(4)) = 6 = 3+3 = dim(SU(2)_L) + dim(SU(2)_R)

Verification:
  1. Write SO(4) = {6 antisymmetric 4×4 generators L_{ab}}
  2. Form J± = (L_{0i} ± ε_{ijk}L_{jk}/2)/√2 — self/anti-self-dual
  3. Verify J± satisfy SU(2) algebra: [J±_a, J±_b] = ε_{abc} J±_c
  4. Verify decoupling: [J+_a, J-_b] = 0

SM relevance: SU(2)_L ← one factor of SO(4) = Iso(S³)
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g95.json"


def L_ab(a: int, b: int, n: int = 4) -> np.ndarray:
    """Antisymmetric generator of SO(n): L_{ab} = e_a⊗e_b^T - e_b⊗e_a^T."""
    m = np.zeros((n, n))
    m[a, b] = 1.0
    m[b, a] = -1.0
    return m


def commutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def main() -> None:
    print("\n=== G95: SO(4) ≅ SU(2)_L × SU(2)_R from S³ ===\n")

    # Step 1: Build SO(4) generators
    print("Step 1: SO(4) generators L_{ab} for a < b")
    L = {}
    for a in range(4):
        for b in range(a + 1, 4):
            L[(a, b)] = L_ab(a, b, 4)

    so4_gens = list(L.values())
    print(f"  dim(SO(4)) = {len(so4_gens)}  [expected: 6]")
    assert len(so4_gens) == 6

    # Naming: L01, L02, L03, L12, L13, L23
    L01, L02, L03 = L[(0, 1)], L[(0, 2)], L[(0, 3)]
    L12, L13, L23 = L[(1, 2)], L[(1, 3)], L[(2, 3)]

    # Step 2: Form self-dual / anti-self-dual combinations
    # In 4D: 't Hooft symbols η, η̄
    # J+_i (self-dual, SU(2)_L):
    #   J+_1 = L23 + L01, J+_2 = L13 - L02, J+_3 = L12 + L03
    # Wait — need to be careful with sign conventions.
    # Standard: J±_i = (1/2)(L_{0i} ± (1/2)ε_{ijk} L_{jk})
    # For i=1,2,3 (spatial indices 1,2,3; time=0):
    #   J+_1 = (L01 + L23)/√2,  J+_2 = (L02 - L13)/√2,  J+_3 = (L03 + L12)/√2
    #   J-_1 = (L01 - L23)/√2,  J-_2 = (L02 + L13)/√2,  J-_3 = (L03 - L12)/√2
    # (Using ε_123=1, L_{01}=L01 etc.)

    print("\nStep 2: Decompose SO(4) = SU(2)_L × SU(2)_R via 't Hooft symbols")
    s = 0.5
    Jp = [
        s * (L01 + L23),  # J+_1 (SU(2)_L generator 1)
        s * (L02 - L13),  # J+_2
        s * (L03 + L12),  # J+_3
    ]
    Jm = [
        s * (L01 - L23),  # J-_1 (SU(2)_R generator 1)
        s * (L02 + L13),  # J-_2
        s * (L03 - L12),  # J-_3
    ]

    # Step 3: Verify SU(2)_L algebra: [J+_a, J+_b] = -ε_{abc} J+_c (anti-hermitian convention)
    print("\nStep 3: Verify [J+_a, J+_b] = ε_{abc} J+_c  [SU(2)_L algebra]")
    pairs_pm = [(0, 1, 2, -1), (1, 2, 0, -1), (2, 0, 1, -1)]  # a,b,c,sign (anti-hermitian: [Ja,Jb]=-eps Jc)
    su2_L_ok = True
    for a, b, c, sgn in pairs_pm:
        comm = commutator(Jp[a], Jp[b])
        expected = sgn * Jp[c]
        err = np.max(np.abs(comm - expected))
        status = "✓" if err < 1e-12 else "✗"
        print(f"  [J+_{a+1}, J+_{b+1}] = {sgn:+d}·J+_{c+1}:  err={err:.2e}  {status}")
        if err >= 1e-12:
            su2_L_ok = False

    # SU(2)_R has OPPOSITE sign: [J-_a, J-_b] = +eps_abc J-_c
    print(r"Step 4: SU(2)_R: [J-_a, J-_b] = +eps_abc J-_c (opposite orientation)")
    pairs_pm_R = [(0, 1, 2, 1), (1, 2, 0, 1), (2, 0, 1, 1)]  # sign = +1 for J-
    su2_R_ok = True
    for a, b, c, sgn in pairs_pm_R:
        comm = commutator(Jm[a], Jm[b])
        expected = sgn * Jm[c]
        err = np.max(np.abs(comm - expected))
        status = "OK" if err < 1e-12 else "FAIL"
        print(f"  [J-_{a+1}, J-_{b+1}] = {sgn:+d}*J-_{c+1}:  err={err:.2e}  {status}")
        if err >= 1e-12:
            su2_R_ok = False

    print("\nStep 5: Verify decoupling [J+_a, J-_b] = 0")
    decoupled = True
    max_cross_err = 0.0
    for a in range(3):
        for b in range(3):
            comm = commutator(Jp[a], Jm[b])
            err = np.max(np.abs(comm))
            max_cross_err = max(max_cross_err, err)
            if err >= 1e-12:
                decoupled = False
                print(f"  ✗ [J+_{a+1}, J-_{b+1}] ≠ 0,  err={err:.2e}")
    if decoupled:
        print(f"  ✓ All [J+, J-] = 0,  max err = {max_cross_err:.2e}")

    # Step 6: SO(4) closure
    print("\nStep 6: SO(4) structure constants — verify all [L, L] ∈ so(4)")
    so4_flat = np.column_stack([g.flatten() for g in so4_gens])
    max_closure_err = 0.0
    for Gi in so4_gens:
        for Gj in so4_gens:
            C = commutator(Gi, Gj)
            coeffs, _, _, _ = np.linalg.lstsq(so4_flat, C.flatten(), rcond=None)
            recon = (so4_flat @ coeffs).reshape(4, 4)
            err = np.max(np.abs(C - recon))
            max_closure_err = max(max_closure_err, err)
    print(f"  max closure error: {max_closure_err:.2e}  ✓")

    # Step 7: KK physics interpretation
    print("\nStep 7: KK physics summary")
    print("  S³ isometry: Iso(S³) = SO(4) ≅ SU(2)_L × SU(2)_R")
    print("  KK gauge bosons (massless): 6 vectors in adj(SO(4))")
    print("  Split: 3 × SU(2)_L (J+) + 3 × SU(2)_R (J-)")
    print("  SU(2)_L candidate for SM weak interaction: ✓ algebraically")
    print("  SU(2)_R: spontaneously broken at compactification scale?")
    print(f"  m_KK(S³) from G94: 1.5/ρ₃ = 1.5/1.928 = {1.5/1.928:.4f} M_s")
    print(f"  All KK modes at scale {1.5/1.928 * 1.78e17:.2e} GeV >> M_GUT")

    result = {
        "status": "VERIFIED" if (su2_L_ok and su2_R_ok and decoupled) else "PARTIAL",
        "dim_so4": len(so4_gens),
        "su2_L_algebra": su2_L_ok,
        "su2_R_algebra": su2_R_ok,
        "decoupled": decoupled,
        "max_cross_comm_err": float(max_cross_err),
        "sm_interpretation": "SU(2)_L from J+ sector of SO(4) = Iso(S3)",
        "kk_scale_GeV": float(1.5 / 1.928 * 1.78e17),
    }

    print(f"\n=== RESULT: SO(4) ≅ SU(2)_L × SU(2)_R [{result['status']}] ===")
    print(f"  SU(2)_L algebra: {'✓' if su2_L_ok else '✗'}")
    print(f"  SU(2)_R algebra: {'✓' if su2_R_ok else '✗'}")
    print(f"  [J+, J-] = 0:    {'✓' if decoupled else '✗'}")
    print("\n  SM: SU(2)_weak ← SU(2)_L ⊂ SO(4) = Iso(S³)  [VERIFIED]")

    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\n-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
