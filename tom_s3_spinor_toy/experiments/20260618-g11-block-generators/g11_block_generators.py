"""G11: Explicit 32×32 block generators J, K, C_i on Ψ = ψ_{S³}(4D) ⊗ ψ_{S⁶}(8D).

Item 2 resolution: construct the three families of operators acting on the
32-component S³×S⁶ spinor as explicit 32×32 matrices.

  J_i (i=1,2,3): SU(2)_L  — S³ spinor sector, trivial on S⁶
  K_i (i=1,2,3): SU(2)_R  — S³ spinor sector, trivial on S⁶
  C_i (i=1..8):  SU(3)_color — trivial on S³, S⁶ spinor sector

Strategy
────────
1. S³ block (4×4): SU(2)_L and SU(2)_R as block-diagonal matrices
   Basis: {|L,↑⟩, |L,↓⟩, |R,↑⟩, |R,↓⟩}
   J_i = block_diag(σ_i/2, 0₂)   K_i = block_diag(0₂, σ_i/2)

2. S⁶ block (8×8): Lift G10-B's SU(3) generators from vector→spinor rep.
   G10-B constructs 8 generators C_k^vec as 6×6 antisymmetric matrices (vector rep).
   The spinor lift: C_k^spin = Σ_{a<b} C_k^vec[a,b] × J_{ab}^spin
   where J_{ab}^spin = [Γ_a, Γ_b] / 4  (from G0 Clifford construction).
   This is a Lie algebra homomorphism: φ(M_{ab}) = J_{ab}^spin.

3. 32×32: J_i^{32} = kron(J_i^4, I₈),  K_i^{32} = kron(K_i^4, I₈),
          C_i^{32} = kron(I₄, C_i^8)

Gates
─────
T1  [J_a,J_b] = iε_{abc}J_c          su(2)_L algebra closes (4×4)
T2  [K_a,K_b] = iε_{abc}K_c          su(2)_R algebra closes (4×4)
T3  [J_i, K_j] = 0                   L and R sectors decouple (4×4)
T4  φ([C₁,C₂]^vec) = [C₁,C₂]^spin   spinor lift is Lie algebra homomorphism
T5  φ([Cᵢ,Cⱼ]^vec) = [Cᵢ,Cⱼ]^spin  hom. for all 64 pairs → su(3) closes in spinor rep
T6  J₃^{32} diagonal: 8×(½) + 8×(-½) + 16×(0)  matches G6 T3L structure
"""

import json
import os
import sys

import sympy as sp
from sympy import I, eye, zeros, kronecker_product as kron

# ── Pauli matrices ─────────────────────────────────────────────────────────────
s0 = eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])

# ── SO(6) Clifford gamma matrices (hermitian 8×8) — identical to G0 ────────────
G_so6 = [
    kron(s1, s0, s0),  # Γ₁
    kron(s2, s0, s0),  # Γ₂
    kron(s3, s1, s0),  # Γ₃
    kron(s3, s2, s0),  # Γ₄
    kron(s3, s3, s1),  # Γ₅
    kron(s3, s3, s2),  # Γ₆
]
I8 = eye(8)
I4 = eye(4)


def J_spinor(a: int, b: int) -> sp.Matrix:
    """SO(6) spinor generator J_{ab} = [Γ_a, Γ_b] / 4  (1-indexed a,b ∈ {1..6})."""
    Ga, Gb = G_so6[a - 1], G_so6[b - 1]
    return (Ga * Gb - Gb * Ga) / 4


# ── Import G10-B SU(3) generators (vector rep, 6×6) ──────────────────────────
_g10_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "20260617-g10-s6-so6-gauge"
)
_g10b_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "20260618-g10b-su3-in-so6"
)
sys.path.insert(0, _g10_dir)
sys.path.insert(0, _g10b_dir)
from g10b_su3_explicit import su3_generators  # noqa: E402


def lift_to_spinor(C_vec: sp.Matrix) -> sp.Matrix:
    """Lift 6×6 so(6) vector-rep element to 8×8 spinor rep.

    C_vec = Σ_{a<b} C_vec[a,b] × M_{ab}  (M_{ab} has +1 at [a,b], -1 at [b,a])
    C_spin = Σ_{a<b} C_vec[a,b] × J_spinor(a+1, b+1)
    """
    result = zeros(8, 8)
    for a in range(6):
        for b in range(a + 1, 6):
            c = C_vec[a, b]
            if c != 0:
                result = result + c * J_spinor(a + 1, b + 1)
    return result


# ── S³ spinor space: SU(2)_L and SU(2)_R (4×4 block-diagonal) ────────────────
# Basis: {|L,↑⟩, |L,↓⟩, |R,↑⟩, |R,↓⟩}
half = sp.Rational(1, 2)

J_S3 = [  # SU(2)_L — σ_i/2 in upper-left (L) block, 0 in lower-right (R) block
    sp.Matrix([[0, half, 0, 0], [half, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
    sp.Matrix([[0, -I * half, 0, 0], [I * half, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
    sp.Matrix([[half, 0, 0, 0], [0, -half, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
]

K_S3 = [  # SU(2)_R — 0 in upper-left (L) block, σ_i/2 in lower-right (R) block
    sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, half], [0, 0, half, 0]]),
    sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -I * half], [0, 0, I * half, 0]]),
    sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, half, 0], [0, 0, 0, -half]]),
]


def _eps3(a: int, b: int, c: int) -> int:
    """Levi-Civita ε_{abc} for a,b,c ∈ {0,1,2}."""
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    if (a, b, c) in {(0, 2, 1), (2, 1, 0), (1, 0, 2)}:
        return -1
    return 0


def main():
    results: list[dict] = []
    passed = 0

    def chk(name: str, cond: bool, desc: str) -> bool:
        nonlocal passed
        ok = bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    # ── Build S⁶ SU(3) generators in spinor rep ──────────────────────────────
    print("Loading G10-B SU(3) generators (vector rep)...")
    su3_vec = su3_generators()
    print(f"  {len(su3_vec)} generators loaded  →  lifting to spinor rep...")
    su3_spin = [lift_to_spinor(C) for C in su3_vec]
    print(f"  Done. {len(su3_spin)} generators in 8×8 spinor rep.")

    # ── T1: [J_a, J_b] = i ε_{abc} J_c  (SU(2)_L, 4×4) ─────────────────────
    t1_ok = True
    for a in range(3):
        for b in range(3):
            comm = J_S3[a] * J_S3[b] - J_S3[b] * J_S3[a]
            expected = sum((I * _eps3(a, b, c) * J_S3[c] for c in range(3)), zeros(4))
            if comm - expected != zeros(4):
                t1_ok = False
    chk("T1_su2L_algebra", t1_ok, "[J_a,J_b] = iε_{abc}J_c  SU(2)_L  (9 commutators, 4×4)")

    # ── T2: [K_a, K_b] = i ε_{abc} K_c  (SU(2)_R, 4×4) ─────────────────────
    t2_ok = True
    for a in range(3):
        for b in range(3):
            comm = K_S3[a] * K_S3[b] - K_S3[b] * K_S3[a]
            expected = sum((I * _eps3(a, b, c) * K_S3[c] for c in range(3)), zeros(4))
            if comm - expected != zeros(4):
                t2_ok = False
    chk("T2_su2R_algebra", t2_ok, "[K_a,K_b] = iε_{abc}K_c  SU(2)_R  (9 commutators, 4×4)")

    # ── T3: [J_L, K_R] = 0  (4×4, block-diagonal → trivially 0) ─────────────
    t3_ok = all(
        J_S3[a] * K_S3[b] - K_S3[b] * J_S3[a] == zeros(4) for a in range(3) for b in range(3)
    )
    chk("T3_JL_KR_commute", t3_ok, "[J_L, K_R] = 0  (9 pairs, L⊕R block structure)")

    # ── T4: φ([C₁,C₂]^vec) = [C₁,C₂]^spin  (Lie algebra homomorphism check) ──
    # The spinor lift φ: M_{ab} → J_{ab}^spin is a Lie algebra representation.
    # Test: φ maps commutators in vector rep to commutators in spinor rep.
    comm_12_vec = su3_vec[0] * su3_vec[1] - su3_vec[1] * su3_vec[0]
    comm_12_via_lift = lift_to_spinor(comm_12_vec)  # φ([C₁,C₂]^vec)
    comm_12_of_spin = su3_spin[0] * su3_spin[1] - su3_spin[1] * su3_spin[0]  # [φ(C₁),φ(C₂)]
    chk(
        "T4_spinor_hom_C1C2",
        comm_12_via_lift - comm_12_of_spin == zeros(8),
        "φ([C₁,C₂]^vec) = [C₁,C₂]^spin  (spinor lift is Lie algebra hom.)",
    )

    # ── T5: φ([Cᵢ,Cⱼ]) = [φ(Cᵢ),φ(Cⱼ)] for all 64 pairs → su(3) closes ─────
    t5_ok = True
    bad_pairs = 0
    for i in range(8):
        for j in range(8):
            comm_vec = su3_vec[i] * su3_vec[j] - su3_vec[j] * su3_vec[i]
            lhs = lift_to_spinor(comm_vec)
            rhs = su3_spin[i] * su3_spin[j] - su3_spin[j] * su3_spin[i]
            if lhs - rhs != zeros(8):
                t5_ok = False
                bad_pairs += 1
    chk(
        "T5_su3_all_pairs_hom",
        t5_ok,
        f"φ([Cᵢ,Cⱼ]) = [φ(Cᵢ),φ(Cⱼ)] for all 64 pairs ({bad_pairs} violations) → su(3) closes in spinor rep",
    )

    # ── T6: J₃^{32} diagonal structure matches G6 T3L eigenvalues ─────────────
    J3_32 = kron(J_S3[2], I8)
    diag = [J3_32[i, i] for i in range(32)]
    cnt_pos = sum(1 for v in diag if v == half)
    cnt_neg = sum(1 for v in diag if v == -half)
    cnt_zer = sum(1 for v in diag if v == 0)
    chk(
        "T6_J3_32_eigenvalues",
        cnt_pos == 8 and cnt_neg == 8 and cnt_zer == 16,
        f"J₃^{{32}} diagonal: {cnt_pos}×(½) + {cnt_neg}×(−½) + {cnt_zer}×(0)  [G6: T3L=½ for |L↑⟩⊗S⁶, etc.]",
    )

    # ── Summary ────────────────────────────────────────────────────────────────
    print("\n32×32 block generator structure confirmed:")
    print("  J_i^{32} = kron(block_diag(σ_i/2, 0₂),  I₈)   SU(2)_L  on S³ × trivial on S⁶")
    print("  K_i^{32} = kron(block_diag(0₂, σ_i/2),  I₈)   SU(2)_R  on S³ × trivial on S⁶")
    print("  C_i^{32} = kron(I₄,  C_i^{spin}_{8×8})         trivial on S³ × SU(3) on S⁶ spinor")
    print()
    print("Lift formula: C^spin = Σ_{a<b} C^vec[a,b] × [Γ_a,Γ_b]/4  (φ: M_{ab}→J_{ab}^spin)")
    print("Commutativity: [J_i^{32}, C_j^{32}] = 0  (trivial by tensor product structure)")

    total = len(results)
    verdict = "PASS_G11_BLOCK_GENERATORS" if passed == total else f"PARTIAL_{passed}_of_{total}"
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "G11-BLOCK-GENERATORS",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "J_32x32": "kron(block_diag(sigma_i/2, 0), I8)  — SU(2)_L on S3 spinor",
        "K_32x32": "kron(block_diag(0, sigma_i/2), I8)  — SU(2)_R on S3 spinor",
        "C_32x32": "kron(I4, C_i^spin_8x8)  — SU(3) on S6 spinor",
        "lift_method": "C^spin = sum_{a<b} C^vec[a,b] * [Gamma_a,Gamma_b]/4",
        "J3_eigenvalues": {"1/2": cnt_pos, "-1/2": cnt_neg, "0": cnt_zer},
        "checks": results,
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_g11.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
