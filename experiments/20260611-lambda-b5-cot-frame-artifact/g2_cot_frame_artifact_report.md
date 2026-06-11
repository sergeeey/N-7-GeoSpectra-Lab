# LAMBDA-B5-G2 Report — cot(2α) Frame Artifact Confirmed

**Date:** 2026-06-11
**Verdict:** `PASS_FRAME_ARTIFACT_CONFIRMED`
**Evidence script:** `evidence_sympy_cot_frame.py` — 14/14 checks PASS, exit 0
**Pre-registration:** `claim_lambda_b5_g2.md` (written before this script ran)
**Machine-readable:** `results.json`

---

## Summary

cot(2α) is a Hopf-coordinate spin-connection frame artifact.
It disappears completely in the left-invariant (Maurer-Cartan) frame on S³.

**Answer to Tom's Q2:**
> *"cot(2α) — expected to vanish with correct SO(4) spinor basis?"*
>
> Yes — cot(2α) = (cotα − tanα)/2 is the Hopf-frame spin connection combination
> ω^1_2 − ω^1_3 = tanα − cotα = −2cot(2α). In the left-invariant frame,
> all spin connection coefficients are integers (ε_ijk structure constants),
> with no α-dependence. The cot(2α) obstruction is a frame artifact.

---

## Results by Check

| Check | Status | What was verified |
|---|---|---|
| C1_tan_minus_cot_eq_minus_2cot2a | **PASS** | tanα − cotα = −2cot(2α) [exact, expand_trig + simplify] |
| C2_frame_omega12_eq_tana | **PASS** | Hopf frame ω^1_2 frame-component = tanα |
| C2_frame_omega13_eq_neg_cota | **PASS** | Hopf frame ω^1_3 frame-component = −cotα |
| C2_hopf_combo_gives_neg2cot2a | **PASS** | tanα + (−cotα) + 2cot(2α) = 0 [exact] |
| C2_torsion_free_e1 | **PASS** | de¹ + ω^1_2 ∧ e² + ω^1_3 ∧ e³ = 0 |
| C2_torsion_free_e2 | **PASS** | de² + ω^2_1 ∧ e¹ = 0 |
| C2_torsion_free_e3 | **PASS** | de³ + ω^3_1 ∧ e¹ = 0 |
| C3_nomizu_connection_is_constant_rational | **PASS** | All Nomizu Γ_ij^k are rational integers |
| C3_no_trig_in_invariant_frame | **PASS** | No trigonometric functions in invariant-frame connection |
| C3_omega12_k3_coeff_equals_1 | **PASS** | Γ_{12}^3 = ε_{123} = 1 |
| C3_omega23_k1_coeff_equals_1 | **PASS** | Γ_{23}^1 = ε_{231} = 1 |
| C3_omega31_k2_coeff_equals_1 | **PASS** | Γ_{31}^2 = ε_{312} = 1 |
| CONTROL_S2_omega21_eq_cos_theta_dphi | **PASS** | S² positive control: ω^2_1 = cosθ dφ |
| CONTROL_S2_zero_connection_fails_torsion | **PASS** | Negative control: zero connection breaks torsion |

---

## Key Results

### C1 — Algebraic identity [VERIFIED-sympy]

```
tan(α) − cot(α) = −2·cot(2α)
```

Proof path: expand_trig converts cos(2α) → cos²α − sin²α, sin(2α) → 2 sin α cos α;
numerator (sin²α − cos²α) + (cos²α − sin²α) = 0.

### C2 — Hopf-frame spin connection [VERIFIED-sympy]

Vielbein: e¹ = dα, e² = cosα dθ, e³ = sinα dφ.
Torsion-free (Cartan structure eq) uniquely gives:

```
ω^1_2 = sin(α) dθ     [coordinate form]  =  tan(α) e²   [frame form]
ω^1_3 = −cos(α) dφ   [coordinate form]  = −cot(α) e³  [frame form]
ω^2_3 = 0
```

All three torsion equations verified symbolically (exact zero).

The spin-connection contraction entering the Dirac radial equation:

```
tan(α) − cot(α) = −2·cot(2α)
```

This is exactly the cot(2α) term in C-H eqs 3.29-3.30 (the ρ cot θ term with θ=2α,
ρ=1 for N=3).

### C3 — Left-invariant frame [VERIFIED-sympy via Nomizu]

On S³ = SU(2) with left-invariant forms σᵢ satisfying dσᵢ = −εᵢⱼₖ σⱼ∧σₖ,
the Nomizu formula gives spin connection coefficients:

```
Γ_{ij}^k = ε_{ijk}   (structure constants — pure integers, NO α-dependence)
```

The invariant-frame spin connection is ω_ij = εᵢⱼₖ σᵏ — constant multiples of
the invariant forms. No tanα, cotα, or cot(2α) anywhere.

---

## Mechanism

The cot(2α) in Tom's S³ Dirac operator arises because the Hopf vielbein
e² = cosα dθ has a varying prefactor cosα. When Cartan's structure equation
is solved, the spin connection inherits a tanα = sinα/cosα coefficient.
Similarly e³ = sinα dφ gives −cotα. Their sum = −2cot(2α) appears in the
radial Dirac equation.

In the left-invariant frame (constant structure constants), these prefactors
are absorbed into the frame itself, and the connection is coordinate-free
(purely algebraic, ε_{ijk}).

---

## What This Result Does NOT Mean

1. Does NOT mean "Tom's operator is wrong" — it may intentionally use Hopf frame.
2. Does NOT mean λ is fixed — this answers frame structure, not coupling.
3. Does NOT mean tom_ansatz = full mode — item 40 angular identification is separate.
4. Does NOT select spin structure (m∈ℤ vs m∈ℤ+1/2).
5. Does NOT claim the S³×S¹ problem is solved.

---

## Next Gates

| Gate | Status | Content |
|---|---|---|
| G2 (this) | **✅ PASS** | cot(2α) = frame artifact, invariant frame is clean |
| G1 | OPEN | Canonical Dirac in invariant frame → spectrum ±(n+3/2); E0 harness as positive control |
| G3 | OPEN | [D_a, D_b] curvature kill-test; su(2)_L ⊂ su(4) embedding (Dereli eq 4.12) |

Order: G2 (done) → G1 (cheap, uses existing E0 harness) → G3 (only if G1 clean).

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
promotion = NONE; safe_for_runtime = False.
Nothing written to Tom until he replies to 2026-06-09 message.
