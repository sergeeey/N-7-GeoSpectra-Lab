# BG-H1-G0 — Source Register: Product Dirac Decomposition

**Gate:** BG-H1-G0 (source trace, FL Step -4)
**Date:** 2026-06-10 (v1.1 — corrected after adversarial re-audit, see Audit Trail)
**Gate verdict:** BG-H1-G0 = PASS (partial-evidence on item iii, see Claim 4)
**Overall status:** BG-H1 = IN_PROGRESS — only the source trace is complete.
G1 (analytic), E1 (lattice), E2 (disorder) have NOT run. The quadrature formula
is **source-traced, NOT verified**.

---

## Summary

The formula λ²(S³×S¹) = (n+3/2)² + (m/R)² is source-traced via: (i) the C-H paper
provides the S³ eigenvalue formula and the N=4 Clifford algebra that forces
4-component spinors; (ii) the cross terms in D² vanish through the JOINT action
of Clifford anticommutation {Γʲ,Γ⁴}=0 and product-structure commutativity
[∇ⱼ,∂_y]=0 — **neither alone suffices** (see Claim 3b); (iii) C-H's own warped
construction (eqs 3.46–3.48) shows in-source exactly when a cross term survives
(warp factor f′≠0) and why it vanishes for a true product (f=const).

Source-level hallucination risk for the quadrature formula is closed.
Analytic verification (G1) and lattice verification (E1) remain — the formula
can still fail at those gates. The spin-structure fork (periodic vs antiperiodic
on S¹) is a topological choice with both options valid — pre-registered, not
resolved here.

---

## Claim 1 — S³ Dirac eigenvalues

**Claim:** The squared Dirac eigenvalues on S³ are λ²_{n,3} = (n + 3/2)² for
n = 0, 1, 2, … with ∇ψ = ±i(n + 3/2)ψ.

| Source | Location | Content | Status |
|--------|----------|---------|--------|
| Camporesi & Higuchi, arXiv:gr-qc/9505009 | Section 3.1, eq. (3.26), p.9 | λ²_{n,N} = (n + N/2)², for N=3: λ² = (n+3/2)² | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | eq. (3.34), p.9 | ∇ψ^{(s)}_{±nlm} = ±i(n + N/2) ψ^{(s)}_{±nlm} — eigenvalue convention iλ | [VERIFIED_FROM_PDF] |
| v0.2.0 E0 gate (this project) | main branch, `tom_s3_spinor_toy/spectral_fingerprint_proxy.py` + `tests/test_spectral_fingerprint_proxy.py` | Numerical: E0 ≈ 3/2 + ε on discrete S³ grid, confirming n=0 ground state | [VERIFIED-pytest 2026-06-10] |

**Verdict:** SOURCED — S³ eigenvalues are unambiguous.

*(v1.1 correction: the previous revision cited a phantom file `e0_eigenvalue.py`;
the actual E0 artifacts are named above — confirmed via git ls-files.)*

---

## Claim 2 — Spinor dimension: 4-component doubling S³ → S³×S¹

**Claim:** On S³×S¹ (total dimension 4, even) Dirac spinors have 4 components.
This is double the 2 components on S³ alone (dimension 3, odd). The extra factor
of 2 comes from the N=4 Clifford algebra enlarging the spinor space.

| Source | Location | Content | Status |
|--------|----------|---------|--------|
| Camporesi & Higuchi | Section 2, eq. (2.4), p.3 | For N=4 (even): Γ⁴ = (0,𝟏;𝟏,0) and Γʲ = (0,iΓ̃ʲ;-iΓ̃ʲ,0) — 4×4 matrices, with Γ̃ʲ the N=3 Clifford set | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | Section 2, text after eq. (2.1), p.3 | "(2.1) can be satisfied by matrices of dimension 2^{[N/2]}" — for N=4: 2² = 4 | [VERIFIED_FROM_PDF] |
| Camporesi & Higuchi | Section 3.1 Case 2 (N odd) text, p.11 | For N odd: "the dimension of the Γ-matrices is 2^{(N−1)/2}" — for N=3: 2¹ = 2, confirming the S³-alone dimension | [VERIFIED_FROM_PDF] |

**Conclusion:** S³ alone: 2 components. S³×S¹ (4d total): 4 components.
**Spinor doubling 2 → 4 is confirmed** — from eqs (2.1)/(2.4) and the Case-2
dimension statement, locations as cited above.

---

## Claim 3 — Product Dirac decomposition: cross terms vanish in D²

**Claim:** D²_{S³×S¹} = D²_{S³} ⊗ 1 + 1 ⊗ D²_{S¹}, i.e. no cross terms.

### 3a. Explicit form of D_{S³×S¹}

Using the N=4 gamma matrices from C-H eq. (2.4), the Dirac operator on S³×S¹
with product metric (S³ of radius 1, S¹ of radius R) is:

```
D_{S³×S¹} = Γʲ ∇^{S³}_j + Γ⁴ (1/R) ∂_y
```

where j ∈ {1,2,3} label S³ frame directions and y ∈ [0, 2π) is the S¹ angle.

The spin connection enters only through the S³ part: −(1/2)ω_{jbc}Σ^{bc} with
b,c ∈ {1,2,3} (a product metric has no mixed connection components, and S¹ is
flat). By C-H eqs (2.12)–(2.13), Σ^{jk} for j,k ≤ 3 is block-diagonal with both
2×2 blocks equal to the S³ generator Σ̃^{jk} — so ∇_j acts identically on the
upper and lower 2-component blocks. In block form (each block 2×2):

```
D_{S³×S¹} = (  0,            iD̃ + ∂_y/R  )
             ( -iD̃ + ∂_y/R,       0       )
```

where D̃ = Γ̃ʲ∇^{S³}_j is the 2×2 Dirac operator on S³ (C-H Section 3.1).

**Source:** C-H eqs (2.4), (2.12), (2.13) for the gamma/generator structure +
standard product-metric vielbein. [INFERRED from VERIFIED_FROM_PDF sources —
3-line algebra]

### 3b. Why cross terms vanish: a JOINT mechanism (not two independent ones)

D² contains the cross term X = Γʲ∇ⱼ·Γ⁴P + Γ⁴P·Γʲ∇ⱼ, where P = (1/R)∂_y.

**Lemma (required first):** Γ⁴ commutes with the S³ spin connection:
by C-H eq. (2.10), [Σ^{bc}, Γ⁴] = δ^{c4}Γᵇ − δ^{b4}Γᶜ = 0 for b,c ∈ {1,2,3}.
This allows Γ⁴ to be pulled through ∇ⱼ. [VERIFIED_FROM_PDF — eq. 2.10]

After the lemma, the cross term obeys the exact identity:

```
X = ½ {Γʲ,Γ⁴} {∇ⱼ, P}  +  ½ [Γʲ,Γ⁴] [∇ⱼ, P]
```

- **Clifford anticommutation** {Γʲ,Γ⁴} = 2δ^{j4} = 0 (C-H eq. 2.1, p.3)
  kills the FIRST half only. [VERIFIED_FROM_PDF]
- **Product-structure commutativity** [∇ⱼ, ∂_y] = 0 (S³ metric and spin
  connection are y-independent; coordinates independent) kills the SECOND
  half only. [INFERRED, CERTAIN]

**Neither mechanism alone suffices:**
- Commutativity alone: residue {Γʲ,Γ⁴}∇ⱼP survives (if [A,B]=0 the cross
  term is 2AB ≠ 0 — a commutator argument can never kill an anticommutator).
- Anticommutation alone (e.g. warped product, [∇ⱼ,P]≠0): residue ΓʲΓ⁴[∇ⱼ,P]
  survives — this is exactly C-H's own warped cross term, see 3d.

Numerical falsification check (adversarial agent, 2026-06-10): joint case
|X| = 0.0 exactly; commutativity-only counterexample |X| ≈ 13.9;
anticommutation-only counterexample |X| ≈ 22.1; the decomposition identity
holds to 3.6e-15; dropping the lemma (mixed Σ^{14} connection) gives |X| ≈ 3.4
even with both headline mechanisms intact. [VERIFIED-INLINE]

*(v1.1 correction: the previous revision claimed "both mechanisms independently
guarantee zero cross terms" — falsified by the identity above. The two
mechanisms are complementary and jointly necessary.)*

### 3c. Result, with the sign convention made explicit

```
D²_{S³×S¹} = D̃² ⊗ 1 + 1 ⊗ (∂_y/R)²
```

Eigenvalue of D̃² on a C-H eigenspinor: −(n+3/2)²  [eqs 3.26, 3.34]
Eigenvalue of (∂_y/R)² on e^{imy}: −m²/R²  [m per spin structure]

**Convention step (C-H eq. 3.16, p.7):** ∇²ψ = −λ²ψ, i.e. λ² ≡ −(eigenvalue
of D²). Summing the negative eigenvalues and flipping sign per (3.16):

```
λ²(S³×S¹) = (n + 3/2)² + (m/R)²   ✓
```

[DERIVED — from VERIFIED_FROM_PDF eqs (2.1), (2.4), (2.10), (2.12), (2.13),
(3.16), (3.26), (3.34) + product-structure commutativity]

### 3d. In-source precedent: C-H eqs (3.46)–(3.48) show exactly when a cross term survives

For S^N as a *warped* product over S^{N−1} (f(θ) = sinθ), C-H derive (p.11):

- eq (3.46): ∇ψ = (∂_θ + ρcotθ)Γᴺψ + (1/sinθ)∇̃ψ
- eq (3.47): Γᴺ∇̃ + ∇̃Γᴺ = 0  (anticommutation holds!)
- eq (3.48): ∇²ψ = (∂_θ + ρcotθ)²ψ + (1/sin²θ)∇̃²ψ − (cosθ/sin²θ)Γᴺ∇̃ψ

The surviving cross term has coefficient −cosθ/sin²θ = −f′(θ)/f(θ)² —
**proportional to the derivative of the warp factor**, despite (3.47)
anticommutation. For a true product (f = const, as in S³×S¹ with both radii
fixed) this term vanishes identically, leaving clean additivity.
[VERIFIED_FROM_PDF — p.11, read this session]

This is the strongest in-source confirmation: C-H themselves display the only
obstruction to additivity, and it is absent for a product metric.

### 3e. Inline numerical verification (sanity only — G1 is the real analytic gate)

Gamma algebra per C-H eq. (2.4) built explicitly in numpy [VERIFIED-INLINE]:

| Check | Result |
|---|---|
| 4d Clifford {Γᵃ,Γᵇ} = 2δᵃᵇ·I₄ | exact (0.0 deviation) |
| {Γʲ,Γ⁴} = 0, j=1,2,3 | exact |
| [Σ^{jk},Γ⁴] = 0, j,k ≤ 3 | exact |
| Block additivity D4² = blockdiag(D̃²+p², D̃²+p²) | max err 3.6e-15 |
| Eigenvalue quadrature \|eig\| = √(k²+p²), k=(n+3/2), p=m/R | max err 1.8e-15 |

**⚠ G1 implementation warning (convention caveat found by the check):** when
assembling the block form, the factor i goes on EITHER the 2×2 S³ Dirac block
OR on the S¹ symbol — not both. Applying the literal template
[[0, iD̃+p],[−iD̃+p, 0]] to an *already anti-Hermitian* D̃ = i·diag(k)
double-counts the i and yields √(k²−p²) instead of √(k²+p²). The consistent
assembly (Hermitian k-block with explicit i, or anti-Hermitian block without)
reproduces the quadrature to 1.8e-15. BG-H1-G1 MUST pin this convention with a
test before measuring anything.

---

## Claim 4 — Spin structures on S¹ (partial-evidence item)

**Claim:** S¹ admits exactly two spin structures, giving periodic (Ramond) and
antiperiodic (Neveu-Schwarz) boundary conditions for spinors.

| Spin structure | BC | m-spectrum | Ground-state shift δ₀(R) | First excited KK δ₁(R) |
|---|---|---|---|---|
| Periodic (Ramond) | ψ(y+2π) = +ψ | m ∈ ℤ | **0 for all R** (m=0 in spectrum — gap unshifted) | m₁=1: √(9/4 + 1/R²) − 3/2 |
| Antiperiodic (NS) | ψ(y+2π) = −ψ | m ∈ ℤ+1/2 | m₁=1/2: √(9/4 + 1/(4R²)) − 3/2 (R-sensitive) | same as δ₀ (lowest \|m\| is already 1/2) |

*(Table aligned with the claim_bg_h1.md fork table: that table's "δ(R)
prediction" column is the GROUND-STATE shift δ₀; the headline closed form
√(9/4+1/R²)−3/2 is the periodic-structure FIRST-EXCITED level. For the
antiperiodic structure the ground state itself is R-sensitive.)*

Evidence split:

| Sub-claim | Source | Status |
|---|---|---|
| Exactly two spin structures on S¹ (classified by π₁(S¹)=ℤ → ℤ₂ choices) | Lawson & Michelsohn, "Spin Geometry", Princeton 1989, Ch. II §2 | [WEAK — standard math result, NOT PDF-verified this session] |
| R/NS sectors both physically admissible | Polchinski, "String Theory" Vol.2, §10.2 | [WEAK — standard physics result, NOT PDF-verified this session] |
| Given periodic BC: m ∈ ℤ; given antiperiodic BC: m ∈ ℤ+1/2 | Fourier analysis: e^{imy} with e^{2πim} = ±1 | [INFERRED, CERTAIN — elementary] |

**Partial-evidence note (v1.1):** the pre-registered gate item (iii) asked for
the m-spectrum per spin structure "from primary literature". Delivered evidence:
the m-sets *given* a boundary condition are elementary Fourier analysis
[INFERRED, CERTAIN]; the *existence of exactly two* spin structures rests on
standard references cited from memory [WEAK]. The G0 kill condition covers only
the additivity claim (item i), which is fully [VERIFIED_FROM_PDF] — so the gate
PASSES, but with this evidence gap flagged. Mitigation: E1 computes BOTH
branches unconditionally; no result depends on which structures exist beyond
these two, and no branch choice is made.

---

## Claim 5 — No cross-curvature corrections on a product

**Claim:** No mixed-curvature term appears in D²_{S³×S¹}.

For a Riemannian product metric g = g_{S³} ⊕ g_{S¹}:
- The Riemann tensor of a product has no mixed components (R_{μνρσ} with
  indices from both factors vanishes).
- Scal(S³×S¹) = Scal(S³) + Scal(S¹) = 6 + 0 (unit S³: N(N−1) = 6; S¹ flat).
- The Lichnerowicz formula D² = ∇*∇ + Scal/4 holds globally on the product
  with this total Scal; since the Riemann tensor has no mixed components,
  no cross-curvature term can arise.

[INFERRED from Riemannian product geometry, CERTAIN]

---

## Source-Traced Formula (BG-H1 Hypothesis — G0 only, NOT yet verified)

```
λ²(S³×S¹) = (n + 3/2)² + (m/R)²,   n = 0,1,2,...
                                       m ∈ ℤ   (periodic)
                                       m ∈ ℤ+½ (antiperiodic)
```

Primary endpoint:
```
δ₁(R) = √(9/4 + (m₁/R)²) − 3/2
```

with m₁ = 1 (periodic, first excited KK) or m₁ = 1/2 (antiperiodic ground state).

Per the pre-registered verdict rules (claim_bg_h1.md): no "SUPPORTED" status
until G0+G1+E1 all pass. This section records what the source trace yields,
nothing more.

---

## Sources Index

| ID | Reference | Equations used | Status |
|----|-----------|----------------|--------|
| CH-95 | Camporesi & Higuchi, arXiv:gr-qc/9505009 (1995) | (2.1), (2.4), (2.10), (2.12), (2.13), (3.16), (3.26), (3.34), (3.46)–(3.48) | [VERIFIED_FROM_PDF] |
| LM-89 | Lawson & Michelsohn, "Spin Geometry", Princeton 1989 | Ch. II §2 (spin structures on S¹) | [WEAK — standard reference, not PDF-verified] |
| POL-98 | Polchinski, "String Theory" Vol.2, Cambridge 1998 | §10.2 (R/NS boundary conditions) | [WEAK — standard reference, not PDF-verified] |
| v020-E0 | This project, main branch: `tom_s3_spinor_toy/spectral_fingerprint_proxy.py`, `tests/test_spectral_fingerprint_proxy.py` | Numerical S³ spectrum E0 ≈ 3/2 | [VERIFIED-pytest 2026-06-10] |

---

## G0 Verdict

**BG-H1-G0 = PASS** (partial-evidence on spin-structure existence, see Claim 4).

| Item | Status |
|------|--------|
| S³ eigenvalues λ² = (n+3/2)² | [VERIFIED_FROM_PDF — CH-95 eqs 3.26, 3.34] |
| 4-component spinor doubling (2→4) | [VERIFIED_FROM_PDF — CH-95 eqs 2.1, 2.4 + Case-2 text p.11] |
| Cross-term cancellation: {Γʲ,Γ⁴}=0 ∧ [∇ⱼ,∂_y]=0 JOINTLY + lemma [Σ^{bc},Γ⁴]=0 | [VERIFIED_FROM_PDF eqs 2.1, 2.10 + INFERRED-CERTAIN + VERIFIED-INLINE] |
| In-source precedent: warped cross term ∝ f′ (eq 3.48), vanishes for product | [VERIFIED_FROM_PDF — CH-95 eqs 3.46–3.48, p.11] |
| Sign convention λ² = −eig(D²) | [VERIFIED_FROM_PDF — CH-95 eq 3.16] |
| Eigenvalue quadrature (matrix-algebra sanity) | [VERIFIED-INLINE — 1.8e-15] |
| Spin structure fork (two structures exist) | [WEAK — standard refs from memory; m-sets given BC: INFERRED-CERTAIN] |
| NO physical spin structure selection | [CONSTRAINT — per claim_bg_h1.md, respected] |

**Kill condition NOT triggered** — product Dirac additivity IS confirmed from
cited sources. BG-H1-G1 (analytic cross-check on small basis) may proceed,
and MUST pin the i-placement convention (see 3e warning) before measuring.

---

## Audit Trail

**v1.0 → v1.1 (2026-06-10):** corrected after adversarial re-audit (4
independent verifiers: falsification algebra, PDF citation check, numeric
gamma-algebra check, cross-file consistency check). Changes:

1. "Two independent mechanisms" → JOINT mechanism with exact identity
   X = ½{Γʲ,Γ⁴}{∇ⱼ,P} + ½[Γʲ,Γ⁴][∇ⱼ,P]; added required lemma [Σ^{bc},Γ⁴]=0
   (C-H eq 2.10). Original claim falsified numerically (counterexamples
   |X|≈13.9 / 22.1).
2. Phantom file citation `e0_eigenvalue.py` → actual artifacts
   `spectral_fingerprint_proxy.py` + test (verified via git ls-files).
3. "Status: SOURCE_TRACE_COMPLETE" → overall BG-H1 = IN_PROGRESS;
   "Confirmed Formula" → "Source-Traced Formula"; removed "no hallucination
   risk remains" overclaim.
4. Added missing sign-convention step (C-H eq 3.16) in Claim 3c.
5. Added in-source precedent C-H eqs (3.46)–(3.48) as Claim 3d.
6. Added inline numerics (3e) incl. the i-placement convention warning for G1.
7. Claim 2 citation locations fixed (text after eq 2.1 p.3; Case-2 text p.11).
8. Claim 4 table aligned with claim_bg_h1.md fork table (δ₀ vs δ₁ columns);
   evidence split into [WEAK] existence + [INFERRED-CERTAIN] m-sets;
   partial-evidence pass noted explicitly.
9. Sources Index: removed uncited eq (3.27) (copy-paste from AV-2 register);
   added (2.10), (2.12), (2.13), (3.16), (3.46)–(3.48).
10. Claim 5 Lichnerowicz phrasing fixed ("applies per-factor" → global formula
    with no mixed Riemann components).

The pre-registration claim_bg_h1.md was NOT edited (frozen per FL protocol).

---

**Code:** none — this is a source trace only (FL Step -4). No lattice code written.
**Next gate:** BG-H1-G1 — analytic cross-check: assemble D² from C-H S³ blocks
+ Fourier S¹ blocks on a small basis, verify quadrature to ≤1e-6, with the
i-placement convention pinned by a dedicated test.
