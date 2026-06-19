"""S6-HARM-G0: SO(6) Clifford algebra foundation for S⁶ harmonic analysis.

Parallel to Tom Lawrence's SO(4) construction on S³ (Part 3, rows 9-10):
  x^α σ_α → u(2) algebra → U(2)
  x^α γ_α → Clifford(SO(4)) → spinor rep of SO(4)

Here: Clifford(SO(6)) → spinor rep of SO(6) ≅ SU(4)
8-component Dirac spinor = 4 ⊕ 4̄ (two Weyl spinors).

Construction (hermitian gamma matrices):
  Γ₁ = σ₁⊗I₂⊗I₂
  Γ₂ = σ₂⊗I₂⊗I₂
  Γ₃ = σ₃⊗σ₁⊗I₂
  Γ₄ = σ₃⊗σ₂⊗I₂
  Γ₅ = σ₃⊗σ₃⊗σ₁
  Γ₆ = σ₃⊗σ₃⊗σ₂

Cartan generators:
  H₁ = J₁₂ = [Γ₁,Γ₂]/4 = (i/2)(σ₃⊗I⊗I)
  H₂ = J₃₄ = [Γ₃,Γ₄]/4 = (i/2)(I⊗σ₃⊗I)
  H₃ = J₅₆ = [Γ₅,Γ₆]/4 = (i/2)(I⊗I⊗σ₃)

Chirality: Γ₇ = σ₃⊗σ₃⊗σ₃  (eigenvalues ±1)
"""

import json
from pathlib import Path

import sympy as sp
from sympy import I, eye, zeros, Matrix, kronecker_product as kron, simplify

# ── Pauli matrices ──────────────────────────────────────────────────────────
s0 = eye(2)
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])

# ── 6D Gamma matrices (hermitian, 8×8) ──────────────────────────────────────
G = [
    kron(s1, s0, s0),  # Γ₁
    kron(s2, s0, s0),  # Γ₂
    kron(s3, s1, s0),  # Γ₃
    kron(s3, s2, s0),  # Γ₄
    kron(s3, s3, s1),  # Γ₅
    kron(s3, s3, s2),  # Γ₆
]
I8 = eye(8)

results: dict = {}


def chk(label: str, expr, expected=0):
    val = simplify(expr - expected)
    ok = val == zeros(*val.shape) if hasattr(val, "shape") else val == 0
    results[label] = "PASS" if ok else f"FAIL: residual={val}"
    return ok


# ── T1: Clifford relation {Γ_a, Γ_b} = 2δ_{ab}I₈ ──────────────────────────
all_cliff = True
for a in range(6):
    for b in range(a, 6):
        anti = G[a] * G[b] + G[b] * G[a]
        expected = 2 * I8 if a == b else zeros(8)
        ok = simplify(anti - expected) == zeros(8)
        if not ok:
            all_cliff = False
            results[f"T1_cliff_{a + 1}{b + 1}"] = f"FAIL"

results["T1_clifford_all_21_pairs"] = "PASS" if all_cliff else "FAIL"


# ── SO(6) generators J_{ab} = [Γ_a, Γ_b] / 4 ───────────────────────────────
def J(a: int, b: int) -> Matrix:
    """Generator J_{a,b} (1-indexed)."""
    return (G[a - 1] * G[b - 1] - G[b - 1] * G[a - 1]) / 4


# ── T2: so(6) Lie algebra — sample: [J₁₂, J₂₃] = J₁₃ ──────────────────────
# so(n): [J_{ab}, J_{cd}] = δ_{ad}J_{bc} - δ_{ac}J_{bd} + δ_{bc}J_{ad} - δ_{bd}J_{ac}
# [J₁₂, J₂₃]: a=1,b=2,c=2,d=3 → δ_{13}J_{22}-δ_{12}J_{23}+δ_{22}J_{13}-δ_{23}J_{12}
#            = 0 - 0 + J_{13} - 0 = J_{13}
comm_12_23 = J(1, 2) * J(2, 3) - J(2, 3) * J(1, 2)
chk("T2_so6_algebra_J12_J23_eq_J13", comm_12_23, J(1, 3))

# [J₁₂, J₃₄]: a=1,b=2,c=3,d=4 → all δ=0 → 0
comm_12_34 = J(1, 2) * J(3, 4) - J(3, 4) * J(1, 2)
chk("T2_so6_algebra_J12_J34_eq_0", comm_12_34, zeros(8))

# [J₁₃, J₃₅]: a=1,b=3,c=3,d=5 → δ_{35}J_{13}?
# = δ_{15}J_{33}-δ_{13}J_{35}+δ_{33}J_{15}-δ_{35}J_{13} = 0-0+J_{15}-0 = J_{15}
comm_13_35 = J(1, 3) * J(3, 5) - J(3, 5) * J(1, 3)
chk("T2_so6_algebra_J13_J35_eq_J15", comm_13_35, J(1, 5))

# ── T3: Cartan generators commute ──────────────────────────────────────────
H1 = J(1, 2)  # (i/2)(σ₃⊗I⊗I)
H2 = J(3, 4)  # (i/2)(I⊗σ₃⊗I)
H3 = J(5, 6)  # (i/2)(I⊗I⊗σ₃)

chk("T3_H1_H2_commute", H1 * H2 - H2 * H1, zeros(8))
chk("T3_H1_H3_commute", H1 * H3 - H3 * H1, zeros(8))
chk("T3_H2_H3_commute", H2 * H3 - H3 * H2, zeros(8))

# ── T4: Cartan eigenvalues = ±i/2 on all 8 basis states ───────────────────
# Expected: H_k eigenvalues are ±i/2 each
# H₁ = (i/2)diag(+1,+1,+1,+1,-1,-1,-1,-1)  (σ₃ acts on first factor)
H1_expected = (I / 2) * kron(s3, s0, s0)
H2_expected = (I / 2) * kron(s0, s3, s0)
H3_expected = (I / 2) * kron(s0, s0, s3)

chk("T4_H1_equals_i_half_s3_I_I", H1, H1_expected)
chk("T4_H2_equals_i_half_I_s3_I", H2, H2_expected)
chk("T4_H3_equals_i_half_I_I_s3", H3, H3_expected)

# ── T5: Chirality operator Γ₇ = σ₃⊗σ₃⊗σ₃, eigenvalues ±1 ────────────────
# Γ₇ = i·Γ₁Γ₂Γ₃Γ₄Γ₅Γ₆  (in 6D, Γ₂ₙ₊₁ = i^n Γ₁...Γ₂ₙ convention variant)
# We use: Γ₇ = σ₃⊗σ₃⊗σ₃  (hermitian, squares to I)
G7 = kron(s3, s3, s3)

chk("T5_G7_squares_to_I8", G7 * G7, I8)

# eigenvalues: ±1, each with multiplicity 4
eigs = list(G7.eigenvals().keys())
eigs_simplified = sorted([simplify(e) for e in eigs])
results["T5_G7_eigenvalues"] = str(eigs_simplified)
results["T5_G7_eigenvalues_are_pm1"] = (
    "PASS" if set(eigs_simplified) == {-1, 1} else f"FAIL: {eigs_simplified}"
)

# multiplicity: 4 each
mults = {simplify(e): m for e, m in G7.eigenvals().items()}
results["T5_G7_multiplicity_4_each"] = (
    "PASS" if mults.get(1) == 4 and mults.get(-1) == 4 else f"FAIL: {mults}"
)

# ── T6: Chiral split matches 4⊕4̄ spinor weights ──────────────────────────
# Γ₇=+1 states: |ε₁ε₂ε₃⟩ with ε₁ε₂ε₃=+1 (even minus signs)
# Γ₇=−1 states: |ε₁ε₂ε₃⟩ with ε₁ε₂ε₃=−1 (odd minus signs)
# Weights (H₁,H₂,H₃) eigenvalues on 8 basis states:
basis = [Matrix([0] * 8) for _ in range(8)]
for k in range(8):
    basis[k][k] = 1

chiral_plus = []
chiral_minus = []
for k, v in enumerate(basis):
    c = (G7 * v)[k]
    if c == 1:
        chiral_plus.append(k)
    elif c == -1:
        chiral_minus.append(k)

results["T6_chiral_plus_indices"] = chiral_plus  # should be 4 states
results["T6_chiral_minus_indices"] = chiral_minus  # should be 4 states
results["T6_chiral_split_4_4"] = (
    "PASS"
    if len(chiral_plus) == 4 and len(chiral_minus) == 4
    else f"FAIL: +={len(chiral_plus)}, -={len(chiral_minus)}"
)

# Verify weights of 4 representation: all have even number of − signs in (ε₁ε₂ε₃)
# Basis ordering: |000⟩,|001⟩,...,|111⟩ with 0→+eigenvalue, 1→−eigenvalue for σ₃
# σ₃|0⟩=|0⟩, σ₃|1⟩=−|1⟩ → ε_k = (-1)^{bit_k}
weights_4 = []
for k in chiral_plus:
    b = [(k >> (2 - i)) & 1 for i in range(3)]  # bits: factor 0,1,2
    w = tuple(sp.Rational(1 - 2 * bit, 2) for bit in b)  # +1/2 or -1/2
    weights_4.append(w)

weights_4bar = []
for k in chiral_minus:
    b = [(k >> (2 - i)) & 1 for i in range(3)]
    w = tuple(sp.Rational(1 - 2 * bit, 2) for bit in b)
    weights_4bar.append(w)

results["T6_weights_of_4"] = [str(w) for w in sorted(weights_4)]
results["T6_weights_of_4bar"] = [str(w) for w in sorted(weights_4bar)]

# 4 weights should have even number of −1/2 (= even parity in ε)
ok_4 = all(sum(1 for x in w if x < 0) % 2 == 0 for w in weights_4)
ok_4bar = all(sum(1 for x in w if x < 0) % 2 == 1 for w in weights_4bar)
results["T6_4_has_even_minus_weights"] = "PASS" if ok_4 else "FAIL"
results["T6_4bar_has_odd_minus_weights"] = "PASS" if ok_4bar else "FAIL"

# ── T7: SO(6) generators commute with Γ₇ (chirality preserved) ────────────
all_comm_ok = True
for a in range(1, 7):
    for b in range(a + 1, 7):
        gen = J(a, b)
        comm = gen * G7 - G7 * gen
        if simplify(comm) != zeros(8):
            all_comm_ok = False
            results[f"T7_J{a}{b}_commutes_G7"] = "FAIL"

results["T7_all_generators_commute_with_G7"] = "PASS" if all_comm_ok else "FAIL"

# ── Summary ─────────────────────────────────────────────────────────────────
pass_count = sum(1 for v in results.values() if str(v) == "PASS")
total = len(results)

verdict = (
    "PASS_SO6_CLIFFORD_FOUNDATION_CONFIRMED"
    if all(
        str(v) == "PASS"
        or k.endswith("_indices")
        or k.endswith("weights_of_4")
        or k.endswith("weights_of_4bar")
        or k.endswith("eigenvalues")
        for k, v in results.items()
    )
    else "FAIL"
)

output = {
    "gate": "S6-HARM-G0",
    "date": "2026-06-15",
    "verdict": verdict,
    "pass_count": pass_count,
    "total_checks": total,
    "gamma_matrices": "Γ_a hermitian 8×8 via σ₁/σ₂/σ₃ tensor products",
    "cartan_generators": "H₁=J₁₂=(i/2)(σ₃⊗I⊗I), H₂=J₃₄=(i/2)(I⊗σ₃⊗I), H₃=J₅₆=(i/2)(I⊗I⊗σ₃)",
    "chirality": "Γ₇=σ₃⊗σ₃⊗σ₃, eigenvalues ±1, splits 8=4⊕4̄",
    "results": results,
}

out_path = Path(__file__).parent / "results_s6_harm_g0.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, default=str)

print(f"Verdict: {verdict}")
print(f"Checks: {pass_count}/{total}")
for k, v in results.items():
    status = (
        "✓"
        if str(v) == "PASS"
        else ("·" if k.endswith("_indices") or "weights" in k or "eigenvalues" in k else "✗")
    )
    print(f"  {status} {k}: {v}")
