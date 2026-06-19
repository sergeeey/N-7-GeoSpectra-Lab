# S³×S⁶ Spinor Toy — Geometric Origin of One SM Generation

**Status:** CSDR 5/5 complete · 1067 tests · 2026-06-19  
**Zenodo (parent repo):** [10.5281/zenodo.20252650](https://doi.org/10.5281/zenodo.20252650) (concept DOI)  
**Author:** Sergey Boyko · Independent researcher  
**Inspired by:** Tom Lawrence, *Product Manifolds as Realisations of General Linear Symmetries* (arXiv:2203.09473)

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

**Comparison with CCM 2006** (Connes-Chamseddine-Marcolli, arXiv:hep-th/0610241):

| CCM 2006 postulates | S³×S⁶ derives |
|---------------------|---------------|
| Algebra A_F = ℂ⊕ℍ⊕M₃(ℂ) | Bypassed — gauge group from S³×S⁶ isometry |
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

1. **Three generations** (main open problem): G2 triality, S⁶/ℤ₃ orbifold, or G₂-instanton with index 3
2. **Majorana mass** for right-handed neutrino
3. **Spectral action** Tr f(D/Λ²) → SM Lagrangian
4. **Coupling λ** — free parameter at S³ stage; fixed only if V-operator is promoted to physical status

---

## Repository Structure

```
tom_s3_spinor_toy/
├── tests/                          # 1067 tests (pytest)
├── experiments/                    # FL-Standard experiment folders (G6-G26)
│   ├── 20260619-g26-ccm-comparison/  # claim.md + decision.md
│   └── ... (31 experiments total)
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
# Expected: 1067 passed, 2 skipped
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
- A bypass of known no-go theorems (Witten, Lichnerowicz)
- Endorsed by Tom Lawrence or affiliated with his research group

---

## Attribution

Developed independently by Sergey Boyko. Inspired by Tom Lawrence's covariant
compactification framework and the NCG approach of Connes-Chamseddine-Marcolli.
All errors and interpretations are entirely my own.

Nearest prior work must be cited in any publication:  
- Dolan, Nash (2002) arXiv:hep-th/0207078  
- Connes, Chamseddine, Marcolli (2006) arXiv:hep-th/0610241
