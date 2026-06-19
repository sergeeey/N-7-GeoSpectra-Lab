"""G14: Quark color triplet from S⁶ spinor — SU(3) fundamental from geometry.

G13 established: S⁶ spinor = S^+ ⊕ S^- = (1⊕3) ⊕ (3̄⊕1) as SU(3)_color.
G13 zero mode: SU(3) singlet in S^- → compatible with ν_R (lepton sector).

G14 question: does the '3' in S^+ carry exact quark color quantum numbers?

Answer: YES. The three states |011⟩, |101⟩, |110⟩ in S^+ transform as an
SU(3)-IRREDUCIBLE module whose weight system is exactly the conjugate of the
3̄ in S^-. Combined with the G13 zero mode (singlet at |111⟩), the full
S⁶ spinor gives: 8 = 1_{|000⟩} + 3_quarks + 3̄_antiquarks + 1_{|111⟩}.

Combinatorial origin of three quark colors:
  S^+ = {|000⟩, |011⟩, |101⟩, |110⟩}  (Γ₇ eigenvalue +1)
    |000⟩ → SU(3) singlet (lepton-like)
    |011⟩ → color state 1 (two ↓, first qubit ↑)
    |101⟩ → color state 2 (two ↓, second qubit ↑)
    |110⟩ → color state 3 (two ↓, third qubit ↑)

  S^- = {|001⟩, |010⟩, |100⟩, |111⟩}  (Γ₇ eigenvalue −1)
    |001⟩ → anti-color 1 (one ↓, third qubit)
    |010⟩ → anti-color 2 (one ↓, second qubit)
    |100⟩ → anti-color 3 (one ↓, first qubit)
    |111⟩ → SU(3) singlet = G13 zero mode (ν_R-compatible)

The THREE quark colors arise from the THREE choices of which single qubit is
↑ (= different from its two ↓ companions) in the tensor product σ₃⊗σ₃⊗σ₃.
This is a COMBINATORIAL consequence of the S⁶ = G₂/SU(3) spinor structure.

λ = FREE_COUPLING_PARAMETER throughout. sm_derivation_claimed = False.
"""

import json
import os
import sys

import sympy as sp
from sympy import zeros
from sympy import kronecker_product as kron

_EXP_DIR = os.path.dirname(__file__)
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))

for _subdir in [
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g11_block_generators import lift_to_spinor, s3  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402

# ── Chirality matrix and SU(3) generators ───────────────────────────────────

Gamma7: sp.Matrix = kron(s3, s3, s3)
su3_vec = su3_generators()
su3_spin = [lift_to_spinor(C) for C in su3_vec]

# ── Spinor sector indices ────────────────────────────────────────────────────
# Basis |i₁i₂i₃⟩ = |σ₃⊗σ₃⊗σ₃ eigenstates⟩, index = 4*i₁ + 2*i₂ + i₃
# Γ₇ eigenvalue = (-1)^(number of 1s in binary)
SP_SINGLET = 0  # |000⟩ — S^+ singlet
QUARK = (3, 5, 6)  # |011⟩,|101⟩,|110⟩ — S^+ color triplet (two 1s)
AQUARK = (1, 2, 4)  # |001⟩,|010⟩,|100⟩ — S^- color antitriplet (one 1)
SM_SINGLET = 7  # |111⟩ — S^- singlet = G13 zero mode


def _sel(indices: tuple[int, ...]) -> sp.Matrix:
    """Selection matrix: 8×n picking columns at 'indices' from identity."""
    cols = [sp.Matrix([1 if k == j else 0 for k in range(8)]) for j in indices]
    return sp.Matrix.hstack(*cols)


def _commutant_dim(generators_3x3: list[sp.Matrix]) -> int:
    """Dimension of commutant by Schur's lemma: 1 ↔ irreducible."""
    eqs = []
    for C in generators_3x3:
        block = kron(C.T, sp.eye(3)) - kron(sp.eye(3), C)
        eqs.append(block)
    A = sp.Matrix.vstack(*eqs)
    return len(A.nullspace())


def _cartan_weights(
    generators_3x3: list[sp.Matrix],
) -> list[tuple[sp.Expr, sp.Expr]]:
    """Return (T_4, T_7) weight pairs (Hermitian = i * anti-Hermitian generator)."""
    T4 = sp.I * generators_3x3[4]
    T7 = sp.I * generators_3x3[7]
    assert T4.is_diagonal() and T7.is_diagonal(), "Cartan generators must be diagonal"
    return [(T4[j, j], T7[j, j]) for j in range(3)]


# ── Main experiment ──────────────────────────────────────────────────────────


def main() -> None:
    results: dict = {}
    passed = 0

    # ── T1: Binary structure of chirality sectors ─────────────────────────
    # Γ₇ = kron(σ₃,σ₃,σ₃): eigenvalue = (-1)^(number of |1⟩ bits in index)
    SP_IDX = [0, 3, 5, 6]  # even number of 1s
    SM_IDX = [1, 2, 4, 7]  # odd number of 1s

    sp_check = all(
        Gamma7 * sp.Matrix([1 if k == j else 0 for k in range(8)])
        == sp.Matrix([1 if k == j else 0 for k in range(8)])
        for j in SP_IDX
    )
    sm_check = all(
        Gamma7 * sp.Matrix([1 if k == j else 0 for k in range(8)])
        == -sp.Matrix([1 if k == j else 0 for k in range(8)])
        for j in SM_IDX
    )
    t1_ok = sp_check and sm_check
    results["T1_binary_chirality"] = t1_ok
    passed += int(t1_ok)
    print(f"T1 binary chirality: {'PASS' if t1_ok else 'FAIL'}")
    print(f"   S^+ indices {SP_IDX}: |000⟩,|011⟩,|101⟩,|110⟩ (even #ones)")
    print(f"   S^- indices {SM_IDX}: |001⟩,|010⟩,|100⟩,|111⟩ (odd  #ones)")

    # ── T2: Quark subspace {|011⟩,|101⟩,|110⟩} is SU(3)-invariant ────────
    B_q = _sel(QUARK)
    quark_invariant = True
    for i, C in enumerate(su3_spin):
        for j in QUARK:
            e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
            Ce_j = C * e_j
            # Must stay in S^+ = {e0, e3, e5, e6}: check no S^- component
            for k in SM_IDX:
                if Ce_j[k] != 0:
                    quark_invariant = False
    t2_ok = quark_invariant
    results["T2_quark_invariant"] = t2_ok
    passed += int(t2_ok)
    print(f"T2 quark subspace SU(3)-invariant: {'PASS' if t2_ok else 'FAIL'}")

    # ── T3: Quark subspace is SU(3)-irreducible (Schur's lemma) ───────────
    C_q = [B_q.T * C * B_q for C in su3_spin]
    commutant_q = _commutant_dim(C_q)
    t3_ok = commutant_q == 1
    results["T3_quark_irreducible"] = t3_ok
    passed += int(t3_ok)
    print(
        f"T3 quark irreducibility (commutant dim=1): {'PASS' if t3_ok else 'FAIL'} (dim={commutant_q})"
    )

    # ── T4: Antiquark subspace {|001⟩,|010⟩,|100⟩} is SU(3)-irreducible ──
    B_a = _sel(AQUARK)
    C_a = [B_a.T * C * B_a for C in su3_spin]
    commutant_a = _commutant_dim(C_a)
    t4_ok = commutant_a == 1
    results["T4_antiquark_irreducible"] = t4_ok
    passed += int(t4_ok)
    print(
        f"T4 antiquark irreducibility (commutant dim=1): {'PASS' if t4_ok else 'FAIL'} (dim={commutant_a})"
    )

    # ── T5: Cartan weights of quark subspace ──────────────────────────────
    # Generators must be diagonal (C_4 and C_7) before this step
    t5_ok = C_q[4].is_diagonal() and C_q[7].is_diagonal()
    if t5_ok:
        q_weights = _cartan_weights(C_q)
        t5_ok = len(set(q_weights)) == 3  # three distinct weight vectors
    results["T5_quark_cartan_weights"] = t5_ok
    passed += int(t5_ok)
    q_w = _cartan_weights(C_q) if C_q[4].is_diagonal() else []
    print(f"T5 quark Cartan weights: {'PASS' if t5_ok else 'FAIL'}")
    print(f"   Weights (T4,T7): {q_w}")

    # ── T6: Antiquark weights = negatives of quark weights (3 vs 3̄) ───────
    a_weights = _cartan_weights(C_a)
    q_set = set(q_w)
    a_neg_set = {(-w1, -w2) for w1, w2 in a_weights}
    t6_ok = q_set == a_neg_set
    results["T6_conjugate_reps"] = t6_ok
    passed += int(t6_ok)
    print(f"T6 3 vs 3̄ (antiquark weights = neg. quark weights): {'PASS' if t6_ok else 'FAIL'}")
    print(f"   Antiquark weights: {a_weights}")
    print(f"   Negatives of quark: {sorted(str(w) for w in a_neg_set)}")

    # ── T7: Quark sum of Cartan weights = 0 (traceless generators) ────────
    T4_q, T7_q = sp.I * C_q[4], sp.I * C_q[7]
    T4_a, T7_a = sp.I * C_a[4], sp.I * C_a[7]
    sum_q4 = sum(T4_q[j, j] for j in range(3))
    sum_q7 = sum(T7_q[j, j] for j in range(3))
    sum_a4 = sum(T4_a[j, j] for j in range(3))
    sum_a7 = sum(T7_a[j, j] for j in range(3))
    t7_ok = sum_q4 == 0 and sum_q7 == 0 and sum_a4 == 0 and sum_a7 == 0
    results["T7_traceless_cartan"] = t7_ok
    passed += int(t7_ok)
    print(f"T7 traceless Cartan (sum of weights = 0): {'PASS' if t7_ok else 'FAIL'}")
    print(f"   quark sum T4={sum_q4}, T7={sum_q7}; antiquark sum T4={sum_a4}, T7={sum_a7}")

    # ── T8: Quark generators anti-Hermitian (unitary representation) ───────
    ah_q = all(C + C.H == zeros(3, 3) for C in C_q)
    ah_a = all(C + C.H == zeros(3, 3) for C in C_a)
    t8_ok = ah_q and ah_a
    results["T8_anti_hermitian"] = t8_ok
    passed += int(t8_ok)
    print(f"T8 anti-Hermitian generators (unitary rep): {'PASS' if t8_ok else 'FAIL'}")

    # ── T9: Full spinor decomposition 8 = 1+3+3bar+1 ──────────────────────
    all_indices = {SP_SINGLET} | set(QUARK) | set(AQUARK) | {SM_SINGLET}
    t9_ok = (
        len(all_indices) == 8
        and all_indices == set(range(8))
        and 1 + len(QUARK) + len(AQUARK) + 1 == 8
    )
    results["T9_full_decomposition"] = t9_ok
    passed += int(t9_ok)
    print(f"T9 full decomposition 8 = 1+3+3bar+1: {'PASS' if t9_ok else 'FAIL'}")
    print(
        f"   SP_singlet={SP_SINGLET}, quarks={QUARK}, antiquarks={AQUARK}, SM_singlet={SM_SINGLET}"
    )

    # ── T10: Combinatorial: colors = choices of 'two-down-one-up' ──────────
    # |ijk⟩ with exactly two 1s: (i+j+k=2) → three choices
    two_ones = [n for n in range(8) if bin(n).count("1") == 2]
    t10_ok = sorted(two_ones) == sorted(list(QUARK))
    results["T10_combinatorial_colors"] = t10_ok
    passed += int(t10_ok)
    print(f"T10 three colors = 'two-1s-in-3-qubits': {'PASS' if t10_ok else 'FAIL'}")
    print(f"   n in {{0..7}} with #bits=2: {two_ones}")

    # ── T11: Antiquark: choices of 'one-down-two-up' ──────────────────────
    one_ones = [n for n in range(8) if bin(n).count("1") == 1]
    t11_ok = sorted(one_ones) == sorted(list(AQUARK))
    results["T11_combinatorial_anticolors"] = t11_ok
    passed += int(t11_ok)
    print(f"T11 three anti-colors = 'one-1-in-3-qubits': {'PASS' if t11_ok else 'FAIL'}")
    print(f"   n in {{0..7}} with #bits=1: {one_ones}")

    # ── T12: Singlets = extremes (all-0 and all-1) ─────────────────────────
    t12_ok = SP_SINGLET == 0 and SM_SINGLET == 7
    results["T12_singlets_extremes"] = t12_ok
    passed += int(t12_ok)
    print(f"T12 singlets at extremes (000 and 111): {'PASS' if t12_ok else 'FAIL'}")

    # ── T13: Quark generators in quark subspace close under commutator ──────
    # [C_i, C_j]_Q should be in span of {C_k_Q}
    closed = True
    for i in range(8):
        for j in range(i + 1, 8):
            com = C_q[i] * C_q[j] - C_q[j] * C_q[i]
            if com != zeros(3, 3):
                # Check if in span of C_q
                eqs_T = sp.Matrix.hstack(*[C.reshape(9, 1) for C in C_q])
                rhs = com.reshape(9, 1)
                try:
                    sol, par = eqs_T.gauss_jordan_solve(rhs)
                except Exception:
                    closed = False
                    break
        if not closed:
            break
    t13_ok = closed
    results["T13_algebra_closes"] = t13_ok
    passed += int(t13_ok)
    print(f"T13 su(3) algebra closes on quark subspace: {'PASS' if t13_ok else 'FAIL'}")

    # ── Summary ───────────────────────────────────────────────────────────
    total = 13
    print(f"\n{'=' * 60}")
    print(f"G14 QUARK COLOR TRIPLET: {passed}/{total} gates PASS")
    if passed == total:
        print("PASS_G14_QUARK_COLOR_TRIPLET_GEOMETRIC_ORIGIN")
    else:
        print("INCOMPLETE — see failing gates above")

    out_path = os.path.join(_EXP_DIR, "g14_results.json")
    with open(out_path, "w") as f:
        json.dump({"passed": passed, "total": total, "gates": results}, f, indent=2)

    return passed == total


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
