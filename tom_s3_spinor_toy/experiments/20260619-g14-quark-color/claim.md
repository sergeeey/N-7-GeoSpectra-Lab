# G14 — Claim: Quark color triplet from S⁶ spinor geometry

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The 8-dimensional S⁶ spinor decomposes under SU(3)_color as:

  S^+ ⊕ S^- = (1 ⊕ 3) ⊕ (3̄ ⊕ 1)

where:
  - The "3" in S^+ is an SU(3)-IRREDUCIBLE color triplet (quark sector)
  - The "3̄" in S^- is an SU(3)-IRREDUCIBLE color antitriplet (antiquark sector)
  - The "3" and "3̄" carry CONJUGATE weight systems: antiquark weights = -(quark weights)

The three quark colors arise COMBINATORIALLY from the Kronecker basis:
  quark states = {|011⟩, |101⟩, |110⟩} = "exactly two ↓ spins in σ₃⊗σ₃⊗σ₃"

## Gates summary

All 13/13 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | Binary chirality: S^+ = even #ones, S^- = odd #ones | PASS |
| T2 | Quark {|011⟩,|101⟩,|110⟩} SU(3)-invariant (no leakage to S^-) | PASS |
| T3 | Quark subspace irreducible: commutant dim=1 (Schur's lemma) | PASS |
| T4 | Antiquark subspace irreducible: commutant dim=1 | PASS |
| T5 | Quark Cartan weights: (1,1), (-1,0), (0,-1) — three distinct | PASS |
| T6 | Antiquark weights = negatives of quark weights (3 vs 3̄) | PASS |
| T7 | Sum of Cartan weights = 0 (traceless SU(3)) | PASS |
| T8 | All generators anti-Hermitian (unitary representation) | PASS |
| T9 | Full decomposition: 8 = 1 + 3 + 3̄ + 1 (all 8 indices covered) | PASS |
| T10 | Three quark colors = 3 choices of "two-1s-in-3-qubits" | PASS |
| T11 | Three anti-colors = 3 choices of "one-1-in-3-qubits" | PASS |
| T12 | Singlets at binary extremes: |000⟩ (S^+) and |111⟩ (S^-) | PASS |
| T13 | su(3) algebra closes on quark subspace | PASS |

## Combinatorial origin of three quark colors

The Clifford algebra SO(6) = SO(6) ⊃ SU(3) acts on the 8-dim spinor
via the tensor product kron(σ₃,σ₃,σ₃) = Γ₇ (chirality matrix). The
SU(3) basis states in the Kronecker basis |i₁i₂i₃⟩ organize by Hamming weight:

| Hamming weight | Indices | SU(3) rep | Sector |
|---------------|---------|-----------|--------|
| 0 | |000⟩ = 0 | 1 (singlet) | S^+ |
| 2 | |011⟩=3, |101⟩=5, |110⟩=6 | **3 (quark)** | S^+ |
| 1 | |001⟩=1, |010⟩=2, |100⟩=4 | 3̄ (antiquark) | S^- |
| 3 | |111⟩ = 7 | 1 (G13 zero mode) | S^- |

"Why three colors?" → C(3,2) = C(3,1) = 3: three ways to choose which qubit
is the "odd one out" in the Kronecker product of three σ₃ eigenstates.

## Connection to G13

G13 zero mode = |111⟩ (S^- singlet) → SU(3) = 1, color-neutral.
G14 quark triplet = {|011⟩,|101⟩,|110⟩} (S^+ subspace) → SU(3) = 3, color-charged.

These are DIFFERENT sectors: different chirality (Γ₇ eigenvalue: −1 vs +1)
and different color content (singlet vs triplet). The quark sector has NO
Dirac zero modes from G13's twisted Dirac (which selects the S^- singlet).
A DIFFERENT mechanism (different twist or boundary condition) would be needed
to give the quark triplet a zero mode.

## Check

`python g14_quark_color.py` → `PASS_G14_QUARK_COLOR_TRIPLET_GEOMETRIC_ORIGIN` (13/13)
`pytest tests/test_g14_quark_color.py` → 26 passed
`pytest tests/` → 827 passed, 2 skipped

## What this does NOT mean

1. Does NOT give zero modes for the quark sector — that requires a separate twist
   or mechanism beyond G13's ind=1. The quark triplet is present in the spinor
   but is NOT a Dirac zero mode of D_{T^{1,0}}.
2. Does NOT identify WHICH of {3, 3̄} is "quark" vs "antiquark" from first
   principles — the labeling follows the chirality convention (S^+ = quark-like).
3. Does NOT derive quark HYPERCHARGE Y — the color structure alone doesn't fix Y.
4. Does NOT fix λ — λ = FREE_COUPLING_PARAMETER throughout.
5. Does NOT prove the SM quark/lepton content is complete — this is one generation
   of color structure, not the full SM spectrum.
6. The "combinatorial" picture (Hamming weights) is a basis-dependent statement
   about the Kronecker product basis of kron(σ₃,σ₃,σ₃); it is not a claim about
   physical quark structure.

## Connection to prior gates

| Gate | Result | G14 connection |
|------|--------|----------------|
| G10-B | SU(3) ⊂ SO(6) explicit | Provides su3_generators() for the color action |
| G11 | Spinor lift: C_i^spin | Provides su3_spin, the 8×8 spinor generators |
| G12 | Anomaly cancellation | The full 3+3̄+1+1 = one generation is anomaly-free (G12 context) |
| G13 | ind=1, singlet at |111⟩ | G14 identifies the COMPLEMENTARY triplet at {|011⟩,|101⟩,|110⟩} |

**Status:** PASS_G14_QUARK_COLOR_TRIPLET_GEOMETRIC_ORIGIN
[VERIFIED-sympy, 2026-06-19, 13/13 gates, 26 tests]
