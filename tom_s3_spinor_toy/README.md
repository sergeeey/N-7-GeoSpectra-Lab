# S³×S⁶ Spinor Toy — Geometric Origin of One SM Generation

**Status:** CSDR 5/5 · N_gen=3 EXACTLY (G73+G74A+G74B) · G76/G77/G82 local audit · 2748 tests collected · 2026-06-22

**Zenodo (parent repo):** [10.5281/zenodo.20252650](https://doi.org/10.5281/zenodo.20252650) (concept DOI)  
**Author:** Sergey Boyko · Independent researcher  
**Inspired by:** Tom Lawrence, *Product Manifolds as Realisations of General Linear Symmetries* (arXiv:2203.09473)

---

## ⚠️ Where to Start (for reviewers)

**The root `.py` files** (`alpha_dependence_comparison.py`, `reference_spinor_harmonics.py`,
`geometry_s3_hopf.py`, etc.) are **early geometric infrastructure** from the P5–P14 exploration
phase. The result described there (√sin(2α) = measure factor, not an eigenspinor) is a correct
transitional falsification — NOT the main result of this project.

**The main mathematical content is in `experiments/`:**

```
experiments/
├── 20260621-g67-octonion-triality/     ← SO(8) Z₃ triality → 3 independent channels
├── 20260621-g68-octonion-channels/     ← L/R inequivalence in Cl(7,0)
├── 20260621-g69-csdr-coset/            ← CSDR: 3+3̄+1+1 independent route
├── 20260621-g73-three-channel-dirac/   ← N_gen = 3 from Atiyah-Singer  ← START HERE
├── 20260621-g74a-lichnerowicz-gap/     ← dim ker = 1 exactly (not just ≥ 1)
└── 20260621-g74b-chirality-from-index/ ← SM left-handed excess from sign(ind)
```

Each directory: `*.py` (implementation, exact `fractions.Fraction`) + `decision.md` (FL Full-Ladder verdict).

Full narrative: [`RESEARCH_STATUS_REPORT.md`](RESEARCH_STATUS_REPORT.md) | Preprint: [`preprint_abstract.md`](preprint_abstract.md) | Theorem pack: [`THEOREM_PACK.md`](THEOREM_PACK.md)

---

## Main Result

The product geometry **S³ × S⁶** reproduces the complete fermion sector of the Standard Model
for **one generation** from pure geometry and representation theory, without postulating the
finite algebra A_F of Noncommutative Geometry.

| Derived | How |
|---------|-----|
| 32-component spinor = 1 SM generation | G6: SO(4)×SU(4)→SU(2)_L×SU(2)_R×SU(3)_c decomposition |
| Electric charge Q = T3L + Y | G17: S³ isometry (T3L) + S⁶ holonomy (Y) |
| Exactly 4 Yukawa parameters {Y_ν,Y_e,Y_u,Y_d} | G25: 256→16→4 geometric cascade |
| KO-dimension 6 of the finite spectral triple | G18: anticommutation relations of (γ_F, J_F, D_F) |
| Chirality = SU(2)_L vs SU(2)_R gauge sectors | G23: Witten index=0, representation asymmetry |
| B−L from K₃ on S⁶ | G16: Cartan generator of SO(6)⊃SU(3) |
| **N_gen = 3 EXACTLY** | **G73+G74A+G74B: Atiyah-Singer ind=1 per channel × 3 Z₃-triality channels** |
| **Left-handed chirality** | **G74B: sign(ind)=+1; orientation of S⁶ is the single Z₂ input** |

**Comparison with CCM 2006** (Connes-Chamseddine-Marcolli, arXiv:hep-th/0610241):

| CCM 2006 postulates | S³×S⁶ derives |
|---------------------|---------------|
| Algebra A_F = ℂ⊕ℍ⊕M₃(ℂ) | Not postulated — SM-like rep content from S³×S⁶ symmetry; full gauge group derivation NOT claimed |
| Exactly 4 Yukawa parameters | From product geometry + CPT (G25) |
| B−L via unimodularity | From K₃ on S⁶ (G16) |

**Nearest prior work:** Dolan-Nash 2002 (arXiv:hep-th/0207078) derived the same 1-generation
result from CP²×CP³ via the Atiyah-Singer index theorem. Our approach is independent:
different manifold (S³×S⁶), different method (NCG spectral triple), additional results (CCM comparison, Yukawa count).

---

## CSDR 5-Angle Plan — Complete (5/5)

| Angle | Gate | Result |
|-------|------|--------|
| 1 — Blind Spectrum | G24 | SO(4)×G₂ rep theory predicts SM content without coordinates |
| 2 — Extended Schur | G21 | S⁶ necessary for distinguishing all 8 fermion types |
| 3 — Literature | G26 | 3 CCM postulates → derived results; Dolan-Nash 2002 identified |
| 4 — Chirality | G23 | Witten=0; SM chirality from SU(2)_L vs SU(2)_R |
| 5 — Prediction | G25 | 4 Yukawa params from geometry; 256→16→4 cascade |

---

## Gate Chain (G6–G26)

| Gate | Claim | Verdict |
|------|-------|---------|
| G6 | 32-component spinor = 1 SM generation | PASS (32/32) |
| G7 | KK mass spectrum M²_{mn} = (m+3/2)²/ρ₃² + (n+3)²/ρ₆² | PASS |
| G8 | Chirality obstruction on round S³×S⁶ (Witten problem) | PASS |
| G9 | Coset chirality: S⁶≅G₂/SU(3) | PASS |
| G10 | S⁶ spin connection → SO(6) gauge field (Tom's s₂=6) | PASS (6/6) |
| G10b | Explicit SU(3) embedding in SO(6) via J-preserving subalgebra | PASS (5/5) |
| G11 | 32×32 block generators for SU(2)_L, SU(2)_R, SU(3) | PASS |
| G12 | All 5 SM gauge anomaly conditions cancel | PASS |
| G13 | Twisted Dirac index on S⁶: ind=1≠0 | PASS |
| G14 | Quark color triplet from S⁶ spinor; 3 colors combinatorial | PASS |
| G15 | Hypercharge Y from S⁶ geometry | PASS |
| G16 | Y = K₃ + (B−L)/2 fully geometric | PASS |
| G17 | Q = T3L + Y; 32 states; ΣQ=0 | PASS |
| G18 | NCG spectral triple (γ_F, J_F, D_F), KO-dim=6, 4 Yukawa | PASS |
| G19 | (2,2)₀ Higgs bidoublet from Yukawa quantum numbers | PASS |
| G20 | Yukawa intertwiner dim=4; 8→4 CPT reduction | PASS |
| G21 | dim=8 with B-L; S⁶ necessary for full distinguishability | PASS (5/5) |
| G22 | NCG first-order condition selects SU(3)×U(1)_{B-L} | PASS |
| G23 | Witten=0; SM chirality from SU(2)_L/R sectors | PASS |
| G24 | SO(4)×G₂ blind spectrum prediction | PASS (6/6) |
| G25 | 4 Yukawa parameters from 256→16→4 cascade | PASS (6/6) |
| G26 | CCM 2006 correspondence; 5/5 CSDR angles | PASS |
| G28 | Spectral action inner fluctuation → SM gauge kinetic terms | PASS |
| G29 | Coupling ratio g₂²/g₃² = 15/(16π) at equal radii (SM error +4.3%) | PASS |
| G67 | SO(8) triality Z₃: three channels 8_v, 8_s, 8_c with c₃=2 each | PASS (25/25) |
| G73 | ind(D_{S⁶}⊗S⁻) = Â(S⁶)·c₃/2 = 1 per channel; N_gen ≥ 3 | PROMOTE (29/29) |
| **G74A** | **Lichnerowicz gap 8/45≪1 + G₂-Schur: dim ker = 1 EXACTLY → N_gen = 3** | **PROMOTE (30/30)** |
| **G74B** | **sign(ind)=+1 → LEFT_HANDED_EXCESS; L=1, R=0 per channel** | **PROMOTE (31/31)** |

---

## Conditional Stabilization Predictions (G54–G82)

**Audit update (2026-06-22):** G76 and G82 show that this chain is not
parameter-free and the G62 mass ratio was not canonically normalized.

The compactification chain — UV-selection → NP stabilization → conditional
dimensionless observables — gives the following values under the stated inputs:

| Input | Value | Source |
|-------|-------|--------|
| λ (NP exponent) | **1/3** (candidate) | dimensional hypothesis `3/9`; `FREE` until derived microscopically |
| A_np | 0.3787 | `CONDITIONAL` on λ, normalization, and the G60 Minkowski condition |
| ρ₆\* | 1.090 | `CONDITIONAL` on the UV calculation and external `C_SM=0.986` |

| Observable | Value | Notes |
|-----------|-------|-------|
| ρ₆_min | **1.179** | AdS minimum position |
| V_min | **−2.53×10⁻⁶** | Shallow AdS (KKLT-like; uplift needed) |
| coordinate-curvature proxy | **2.02%** | `sqrt(V''(rho)/m_KK²)`; not canonical |
| canonical metric-only proxy | **0.252%** | conditional on the tested Einstein-frame metric and `M4=Ms=1` |

**On C = 0.986:** The SM constraint ρ₃ = C·ρ₆² uses C derived from PDG 2022 gauge couplings
(g₂²/g₃² at M_Z → C = 0.9865, deviation from natural C=1 is 1.4%). This is an observational
input, not a fit to the observables below. The equal-radius case C=1 predicts g₂/g₃ with 4.3%
error; C=0.986 closes this gap. All stabilization results (G57–G62) are independent of
adjusting C within [0.98, 1.00]. (G29, PROMOTE)

**Key structural finding:** UV-selection point (ρ₆\*=1.090, where Casimir divergence cancels)
and potential minimum (ρ₆\_min=1.179) are **distinct** — consistent with KKLT uplift structure.
The 8.2% separation is a conditional output of the implemented toy potential.

Casimir correction is sub-dominant for the tested coefficient range. A physical
modulus/KK mass ratio still requires the normalized reduced action, `M4/Ms`, and
the full two-field mass eigenproblem.

### G77 uplift schemes

- **Scheme A:** choose `p`, enforce `V=0` and `V'=0` at
  `rho6_star=1.090`, and solve for `A_np` and `D`.
- **Scheme B:** keep the previous `A_np=0.3787`, then solve for the shifted
  Minkowski minimum and `D`.

G77 is `PASS_ALGEBRAIC_TOY`: both schemes produce local minima in the tested
one-field potential. This is not a microscopic or string-theoretic derivation
of the uplift sector. The exponent `p` remains `FREE`.

The earlier `D` table used the convention `K=1`. The repository potential uses
`K_VOL=652.841994`, so repository-normalized values are
`D_repo=D_K1/K_VOL`.

**Stabilization gates (G54–G62):**

| Gate | Claim | Verdict |
|------|-------|---------|
| G54-A | V_flux = const on SM constraint ρ₃=Cρ₆² | PASS |
| G54-B/C | Casimir pole residue c_{1/2} at s=−1/2 | PASS |
| G54-D/E | ζ_FP Hadamard finite part; three radii ρ₆\_min<ρ₆\*<ρ₆\*\* | PASS |
| G54-F | 4D EH frame: Dine-Seiberg runaway without NP | PASS |
| G55 | Two-flux 2D: V\_flux\_min=q₃q₆=1 exact | PASS |
| G56+G57 | KKLT-like NP stabilization + UV-selection ρ₆\*=1.090 | PASS |
| G58–G59 | Curvature and FR charge-scaling: outside SM window | NULL |
| G60 | Minkowski uplift constraint → A\_np from geometry | PASS (pearl) |
| G61 | λ = 1/3 (dimensional) or π/9 (E7 gaugino) | WEAK PROMOTE |
| G62 | coordinate-space observables; 2.02% curvature proxy | REINTERPRETED BY G82 |
| G76 | parameter provenance registry | PASS |
| G77 | algebraic uplift at fixed radius or fixed amplitude | PASS_ALGEBRAIC_TOY |
| G82 | canonical radion mass audit | CONDITIONAL |

### Reproduce the local audit

```bash
python tom_s3_spinor_toy/experiments/20260622-g76-parameter-registry/g76_parameter_registry.py
python -m pytest tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q

python tom_s3_spinor_toy/experiments/20260622-g77-uplift-solver/g77_uplift_solver.py
python -m pytest tom_s3_spinor_toy/tests/test_g77_uplift_solver.py -q

python tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/g82_canonical_mass.py
python -m pytest tom_s3_spinor_toy/tests/test_g82_canonical_mass.py -q

python -m pytest tom_s3_spinor_toy/tests/test_markdown_claim_audit.py -q
```

---

## Three-Generation Investigation → RESOLVED by G73+G74A+G74B

**Result (updated 2026-06-21):** N_gen = 3 EXACTLY from twisted Atiyah-Singer index on S⁶.

**Mechanism:** ind(D_{S⁶}⊗S⁻) = Â(S⁶)·c₃(S⁻)/2 = 1 per channel × 3 Z₃-triality channels = **3**.
- c₃(S⁻) = χ(S⁶) = 2 (G33, Chern–Gauss–Bonnet)
- Â(S⁶) = 1 (G50, H⁴(S⁶;ℤ)=0)
- Three channels from G₂ = Fix(Z₃ ⊂ Aut(𝕆)) on SO(8) reps 8_v, 8_s, 8_c (G67)
- Count exact: |F_{S⁻}|/(R/4) = 8/45 ≪ 1 (G74A Lichnerowicz) + G₂-Schur → dim ker ≤ 1

**Why earlier NULL scan (G27–G38) did not find this:** Those 10 mechanisms tried single-bundle
selections with c₃=6. The χ-lemma (Proposition T1) correctly rules those out. The resolution uses
THREE bundles of c₃=2 each — c₃=2 is an asset (ind=1), not a limitation.

**Earlier NULL results (still valid for their respective classes):**

| Gate | Mechanism | Verdict |
|------|-----------|---------|
| G27-ℤ₃ | Z₃ orbifold on S⁶ | NULL — χ(S⁶)=2, Smith theory rules out free ℤ₃ |
| G30-G₂ | G₂-instanton index | NULL — G₂ symmetry forces index=0 always |
| G31-S³ | S³ adjoint bundle, j=1 | NULL — Lichnerowicz + parity block j=1 |
| G33-A1 | Euler class c₃(T^{1,0}S⁶)=χ(S⁶) | NULL — equals 2, not 6; A1 circular |
| G34-D1 | Flux quantization H⁶(S⁶;ℤ)=ℤ | WEAK — necessary not sufficient |
| G34-B3 | WZW SU(2)_k from spin connection | NULL — η(S³)=0 → k=0 → 1 primary |
| G34-A2 | Cobordism Ω^{Spin}_6=0 | NULL — no mod-k invariants on S⁶ |
| G35-C1 | NCG M₃(ℂ) = generation counter | NULL — rank(T^{1,0}S⁶)≠ind; color SU(3), not gen |
| G36-K1 | K-theory K̃(S⁶)=ℤ, Adams ψ^k | NULL — homogeneous group, Adams k³ same ∀n |
| G37-S1 | String tadpole on S³×S⁶ | NULL — dim=9≠6; χ=0; min tadpole at c₃=2 |
| G38-S2 | Spectral action minimum on bundle space | NULL — S_spec monotone, min at c₃=2 (= G33) |

null_results/INDEX.md: 24 entries (G27–G51, G58–G60 + earlier branches).

---

## Earlier Threads (pre-G6)

| Thread | Result |
|--------|--------|
| AV-2 | Angular/bilinear operator analysis; E1 STRONG_PASS: sin(2α)/2 exact |
| BG-H1 | S³×S¹ KK bridge: λ²=(n+3/2)²+(m/R)²; robust to disorder |
| Lambda-B5 | λ is non-identifiable from S³ alone (Fisher rank theorem); R=√2 λ-free ratio |
| V-RATIO | Rank-1 and rank-2 λ-free ratio families (closed forms) |
| S6-BRANCH-G0 | SU(4)→SU(3)×U(1): all charges ∈ ℚ; Pati-Salam conditions satisfied |

---

## Open Questions

1. **Three generations** — RESOLVED (G73+G74A+G74B). N_gen=3 exactly from twisted Atiyah-Singer index. Left-handed chirality from sign(ind)=+1. See gate chain above.
2. **Majorana mass** for right-handed neutrino — not yet explored
3. **Coupling λ** — free at S³ stage (G4 Fisher rank theorem); requires V-operator promotion

---

## Repository Structure

```
tom_s3_spinor_toy/
├── tests/                          # 2748 tests collected (pytest, 2026-06-22)
├── experiments/                    # FL-Standard experiment folders (G6-G38)
│   ├── 20260619-g26-ccm-comparison/  # claim.md + decision.md
│   └── ... (38 experiments total)
├── reports/                        # Analysis reports
├── null_results/                   # Falsified hypotheses
├── geometry_s3_hopf.py            # S³ metric and coframe
├── reference_spinor_harmonics.py  # Spinor harmonics reference
└── RESEARCH_STATUS_REPORT.md      # Full technical status
```

---

## Running the Tests

```bash
cd tom_s3_spinor_toy
python -m pytest tests/ -q
# Current collection: 2748 tests; full runtime depends on heavy numerical gates
```

---

## What This Is and Is NOT

**This is:**
- A falsification-first toy model study
- Representation-theory level (no quantum field theory)
- One generation of SM fermions from geometry

**This is NOT:**
- A proof of S³×S⁶ as the physical compactification space
- A derivation of the SM Lagrangian or coupling constants
- A bypass of the Witten index no-go (our result uses it, not bypasses it)
- Endorsed by Tom Lawrence or affiliated with his research group

---

## Attribution

Developed independently by Sergey Boyko. Inspired by Tom Lawrence's covariant
compactification framework and the NCG approach of Connes-Chamseddine-Marcolli.
All errors and interpretations are entirely my own.

Nearest prior work must be cited in any publication:  
- Dolan, Nash (2002) arXiv:hep-th/0207078  
- Connes, Chamseddine, Marcolli (2006) arXiv:hep-th/0610241
