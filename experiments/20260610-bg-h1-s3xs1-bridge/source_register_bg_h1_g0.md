# BG-H1-G0 — Source Register: Product Dirac Decomposition

**Gate:** BG-H1-G0 (source trace, FL Step -4)
**Date:** 2026-06-10
**Verdict:** PASS
**Status:** BG-H1 = SOURCE_TRACE_COMPLETE — BG-H1-G1 may proceed

---

## Summary

The formula λ²(S³×S¹) = (n+3/2)² + (m/R)² is confirmed from two independent
pillars: (i) the C-H paper provides the S³ eigenvalue formula and the N=4 Clifford
algebra that forces 4-component spinors and anticommuting gamma matrices; (ii)
the product metric structure guarantees commutativity of the S³ and S¹ Dirac
operators, so cross terms in D² vanish for TWO independent algebraic reasons.

**No hallucination risk remains for the quadrature formula itself.** The spin
structure fork (periodic vs antiperiodic on S¹) is a topological choice with
both options valid — this is pre-registered and not resolved here.

---

## Claim 1 — S³ Dirac eigenvalues

**Claim:** The squared Dirac eigenvalues on S³ are λ²_{n,3} = (n + 3/2)² for
n = 0, 1, 2, … with ∇ψ = ±i(n + 3/2)ψ.

| Source | Location | Content | Status |
|--------|----------|---------|--------|
| Camporesi & Higuchi, arXiv:gr-qc/9505009 | Section 3.1, eq. (3.26) | λ²_{n,N} = (n + N/2)², for N=3: λ² = (n+3/2)² | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | eq. (3.34) | ∇ψ^{(s)}_{±nlm} = ±i(n + N/2) ψ^{(s)}_{±nlm} — eigenvalue convention iλ | [VERIFIED_FROM_PDF] |
| v0.2.0 E0 gate (this project) | main branch, e0_eigenvalue.py | Numerical: E0 ≈ 3/2 + ε on discrete S³ grid, confirming n=0 ground state | [VERIFIED-pytest 2026-06-10] |

**Verdict:** SOURCED — S³ eigenvalues are unambiguous.

---

## Claim 2 — Spinor dimension: 4-component doubling S³ → S³×S¹

**Claim:** On S³×S¹ (total dimension 4, even) Dirac spinors have 4 components.
This is double the 2 components on S³ alone (dimension 3, odd). The extra factor
of 2 comes from the N=4 Clifford algebra enlarging the spinor space.

| Source | Location | Content | Status |
|--------|----------|---------|--------|
| Camporesi & Higuchi | Section 2, eq. (2.4) | For N=4 (even): Γ⁴ = (0,𝟏;𝟏,0) and Γʲ = (0,iΓ̃ʲ;-iΓ̃ʲ,0) — matrices are 4×4; Clifford algebra requires 2^{N/2} = 4 components | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | Section 2 text after (2.4) | "matrices of dimension 2^{[N/2]}" — for N=4: 2² = 4 | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | Section 3.1 Case 2 text (p.12) | For N=3 (odd): spinors are 2^{(N-1)/2} = 2^1 = 2-dimensional — confirming the S³-alone dimension | [VERIFIED_FROM_PDF] |

**Conclusion:** S³ alone: 2 components. S³×S¹ (4d total): 4 components.
**Spinor doubling 2 → 4 is confirmed.** [VERIFIED_FROM_PDF]

---

## Claim 3 — Product Dirac decomposition: cross terms vanish in D²

**Claim:** D²_{S³×S¹} = D²_{S³} ⊗ 1 + 1 ⊗ D²_{S¹}, i.e. no cross terms.

### 3a. Explicit formula for D_{S³×S¹}

Using the N=4 gamma matrices from C-H eq. (2.4), the Dirac operator on S³×S¹
with product metric (S³ of radius 1, S¹ of radius R) is:

```
D_{S³×S¹} = Γʲ ∇^{S³}_j + Γ⁴ (1/R) ∂_y
```

where j ∈ {1,2,3} label S³ frame directions and y is the S¹ coordinate.

In block-matrix form (each block is 2×2):
```
D_{S³×S¹} = (  0,       iD̃ + ∂_y/R  )
             ( -iD̃ + ∂_y/R,    0      )
```

where D̃ = Γ̃ʲ∇^{S³}_j is the 2×2 Dirac operator on S³ (C-H Section 3.1).

**Source:** C-H eq. (2.4) for gamma matrix structure + standard product metric
vielbein (flat S¹ → no S¹ spin connection). [INFERRED from C-H + product metric,
HIGH confidence — derivation is 3-line algebra from VERIFIED sources]

### 3b. Two independent reasons cross terms vanish in D²

D²_{S³×S¹} contains cross terms:

```
(cross) = iD̃·(∂_y/R) + (∂_y/R)·(-iD̃)
        = i(D̃ × ∂_y/R - ∂_y/R × D̃)
        = i [D̃, ∂_y/R]
```

**Reason 1 — commutativity of operators on independent spaces:**
D̃ acts on S³ coordinates (α, θ, φ). ∂_y acts on S¹ coordinate y.
These coordinates are independent → [D̃, ∂_y] = 0 exactly.
Source: standard product metric; no citation needed (tautology of coordinate
independence). [INFERRED, CERTAIN]

**Reason 2 — Clifford anticommutation {Γʲ, Γ⁴} = 0:**
By C-H eq. (2.1): {Γ^a, Γ^b} = 2δ^{ab}.
For j ∈ {1,2,3} and the S¹ index 4: {Γʲ, Γ⁴} = 2δ^{j4} = 0.
So the Clifford algebra ALSO forces cross terms to cancel in the abstract
tensor-product representation.
Source: Camporesi & Higuchi, eq. (2.1). [VERIFIED_FROM_PDF]

**Both mechanisms independently guarantee zero cross terms.**

### 3c. Result

```
D²_{S³×S¹} = D̃² ⊗ 1 + 1 ⊗ (∂_y/R)²
```

Eigenvalue of D̃² on C-H eigenspinor: −(n+3/2)²  [from eq. 3.26, 3.34]
Eigenvalue of (∂_y/R)²: −m²/R²  [m ∈ ℤ or ℤ+1/2 per spin structure]

→ λ²(S³×S¹) = (n + 3/2)² + (m/R)²   ✓

**Status:** [DERIVED — from VERIFIED_FROM_PDF sources C-H eqs. (2.1), (2.4),
(3.26), (3.34) + tautological coordinate independence]

---

## Claim 4 — Spin structures on S¹

**Claim:** S¹ admits exactly two spin structures, corresponding to periodic
(Ramond) and antiperiodic (Neveu-Schwarz) boundary conditions for spinors.

| Spin structure | BC | m-spectrum | m₁ (lowest |m|>0) | δ₁(R) |
|---|---|---|---|---|
| Periodic (Ramond) | ψ(y+2πR) = +ψ(y) | m ∈ ℤ | m₁ = 1 (m=0 allowed → δ=0 for n=0) | √(9/4 + 1/R²) − 3/2 |
| Antiperiodic (NS) | ψ(y+2πR) = −ψ(y) | m ∈ ℤ+1/2 | m₁ = 1/2 | √(9/4 + 1/(4R²)) − 3/2 |

**Note on periodic case:** m=0 is in the spectrum, so the n=0 ground state
has δ=0 (gap unshifted). The headline δ(R) = √(9/4+1/R²)−3/2 applies to
the **first excited KK mode** (n=0, m=1), not the ground state.

| Source | Content | Status |
|--------|---------|--------|
| Standard spin geometry (Lawson & Michelsohn "Spin Geometry" 1989, Ch. II §2) | S¹ has exactly two spin structures classified by π₁(S¹) = ℤ; the two lifts correspond to ±1 holonomy → periodic/antiperiodic | [WEAK — not PDF-verified in this session, standard math result] |
| Standard QFT/string theory (Polchinski "String Theory" Vol.2, §10.2) | R sector = periodic fermions; NS sector = antiperiodic; both valid compactification choices | [WEAK — not PDF-verified in this session, standard physics result] |

**Status:** [INFERRED/STANDARD — two valid spin structures are mathematically
well-established; choice is NOT made here per pre-registration constraint]

---

## Claim 5 — No source needed for ruling out cross-product corrections

**Claim:** There is no "Kaluza-Klein mixing term" in D²_{S³×S¹} from mixed
curvature between S³ and S¹.

For a Riemannian product metric g = g_{S³} ⊕ g_{S¹}:
- The Riemann tensor has no cross components R_{μνρσ} with mixed S³/S¹ indices
- The Ricci scalar is a sum: Scal = Scal_{S³} + Scal_{S¹} = 6 + 0 (S¹ is flat)
- The Lichnerowicz formula D² = ∇*∇ + Scal/4 applies per-factor for product metrics

No correction terms arise. [INFERRED from Riemannian product geometry, CERTAIN]

---

## Confirmed Formula (BG-H1 Hypothesis)

```
λ²(S³×S¹) = (n + 3/2)² + (m/R)²,   n = 0,1,2,...
                                       m ∈ ℤ   (periodic)
                                       m ∈ ℤ+½ (antiperiodic)
```

Primary endpoint:
```
δ₁(R) = √(9/4 + (m₁/R)²) − 3/2
```

with m₁ = 1 (periodic, first KK) or m₁ = 1/2 (antiperiodic ground state).

---

## Sources Index

| ID | Reference | Equations used | Status |
|----|-----------|----------------|--------|
| CH-95 | Camporesi & Higuchi, arXiv:gr-qc/9505009 (1995) | (2.1), (2.4), (3.26), (3.27), (3.34) | [VERIFIED_FROM_PDF] |
| LM-89 | Lawson & Michelsohn, "Spin Geometry", Princeton 1989 | Ch. II §2 (spin structures on S¹) | [WEAK — standard reference, not PDF-verified] |
| POL-98 | Polchinski, "String Theory" Vol.2, Cambridge 1998 | §10.2 (R/NS boundary conditions) | [WEAK — standard reference, not PDF-verified] |
| v020-E0 | This project, main branch, E0 gate | Numerical S³ spectrum E0 ≈ 3/2 | [VERIFIED-pytest 2026-06-10] |

---

## G0 Verdict

**PASS** — Product Dirac additivity is confirmed from primary sources.

| Item | Status |
|------|--------|
| S³ eigenvalues λ² = (n+3/2)² | [VERIFIED_FROM_PDF — CH-95 eq. 3.26] |
| 4-component spinor doubling (2→4) | [VERIFIED_FROM_PDF — CH-95 eq. 2.4] |
| {Γʲ, Γ⁴} = 0 (Clifford anticommutation) | [VERIFIED_FROM_PDF — CH-95 eq. 2.1] |
| [D_{S³}, D_{S¹}] = 0 (coordinate independence) | [INFERRED, CERTAIN] |
| D²_{S³×S¹} = D²_{S³} + D²_{S¹} | [DERIVED from above, HIGH confidence] |
| Spin structure fork (periodic / antiperiodic) | [STANDARD, WEAK — both options valid] |
| NO physical spin structure selection | [CONSTRAINT — per claim_bg_h1.md] |

**Kill condition NOT triggered** — product Dirac additivity IS confirmed from
cited sources. BG-H1-G1 (analytic cross-check on small basis) may proceed.

---

**Code:** none — this is a source trace only (FL Step -4). No lattice code written.
**Next gate:** BG-H1-G1 — analytic cross-check: assemble D² from C-H S³ blocks
+ Fourier S¹ blocks symbolically on small basis, verify quadrature to ≤1e-6.
