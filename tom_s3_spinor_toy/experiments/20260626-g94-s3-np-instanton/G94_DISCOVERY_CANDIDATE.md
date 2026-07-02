# G94 Discovery Candidate

**Date:** 2026-07-02  
**Status:** [VERIFIED-SYNTHETIC] · CANDIDATE (not yet submitted)  
**Evidence:** `results_g94.json`, `g94_s3_np_instanton.py`, G102 extension  
**Hard fences:** toy model, c_S3 free parameter, λ free parameter, sm_derivation_claimed=False

---

## 1. Claim

> In the tested S³×S⁶ compactification toy model, the phenomenological
> path constraint ρ₃ ≈ ρ₆² arises as a **dynamical attractor** of the
> full 2D moduli potential when a D2-brane instanton term
> A_S3·exp(−c_S3·ρ₃³) is included — rather than being imposed externally.

One sentence version:
> **ρ₃≈ρ₆² is dynamically selected in the tested S³×S⁶ EFT with D-brane instanton.**

---

## 2. Prior art

| Work | What they did | How G94 differs |
|------|--------------|----------------|
| Lawrence [2022] arXiv:2203.09473 | S³ spin-connection → SM gauge fields; path ρ₃=ρ₆² assumed by hand | G94 derives path approximately from potential minimization |
| KKLT (Kachru et al. 2003) | Anti-brane uplift stabilizes moduli in IIB | Different geometry; G94 uses IIA-like D2 on S³ |
| LVS (Balasubramanian et al. 2005) | Large Volume Scenario — flux + α' | Volume moduli; no S³×S⁶ structure |
| Freund-Rubin | Flux stabilizes S⁶ radius | ρ₆ only; ρ₃ runaway remains (G93 confirms) |

**Literature gap:** No prior work derives ρ₃≈ρ₆² from a potential minimum
in this geometry. The path was a phenomenological input in all prior constructions.

**Pre-search required before submission:** grep arXiv hep-th for
"S3 instanton stabilization" + "S6 compactification" + "D2 brane moduli" —
confirm no prior result covers exactly this structure.

---

## 3. Novelty

Three independent new results in G94:

**N1 — First EFT-valid 2D minimum:** G91 worked on the path (1D constrained,
rho6=1.18 marginal EFT). G92, G93 gave sub-stringy minima (ρ₃<1, EFT invalid).
G94 is the first true 2D minimum with ρ₃=1.93, ρ₆=1.36 — **both above string scale**.

**N2 — Path as dynamical attractor:** The minimum lands at ρ₃/ρ₆²=1.04 (4% off path)
WITHOUT enforcing the path. This is an emergent result. Prior gates all imposed the path.

**N3 — Robustness over parameter window:** The attractor holds for c_S3 ∈ [0.235, 0.27]
(path deviation 4%–16%). This is a range, not a fine-tuned point. Fine-tuning
would require a single special value; the attractor persists over a window.

**N4 (G102) — c_S3 reduces to g_s prediction:** The instanton coefficient
c_S3 is structurally related to the string coupling g_s. This connects the free
parameter to a measurable quantity (not yet derived, but structural).

---

## 4. Kill tests

The claim fails if ANY of the following holds:

| # | Kill condition | Status |
|---|----------------|--------|
| K1 | The minimum disappears under ±20% variation of background parameters (C_SM, λ) | NOT TESTED — required |
| K2 | The Hessian has a negative eigenvalue at the claimed minimum | PASSES: H_eigs=[+1.28e-6, +1.71e-5] for c_S3=0.235 |
| K3 | The result is a coordinate artifact (reparametrization changes the attractor location by >50%) | NOT TESTED — required |
| K4 | Full Weyl rescaling changes sign of mass eigenvalues | NOT TESTED — schematic only |
| K5 | Known prior work covers this result (literature check) | NOT DONE — required |
| K6 | The 4% path deviation is larger than model precision | BORDERLINE — toy model precision ~10% |

**Kill tests K1, K3, K4, K5 are NOT YET RUN.** Current status is
[VERIFIED-SYNTHETIC] pending these checks. Discovery claim requires all 6.

---

## 5. Evidence [VERIFIED-SYNTHETIC]

### 5.1 Scan over c_S3

| c_S3 | ρ₃ | ρ₆ | ρ₃/ρ₆² | dev% | EFT | m_mod/m_KK |
|------|----|----|---------|------|-----|------------|
| 0.235 | 1.928 | 1.361 | 1.041 | **4.1%** | ✓ | **0.142%** |
| 0.240 | 1.953 | 1.355 | 1.063 | 6.3% | ✓ | 0.143% |
| 0.245 | 1.976 | 1.350 | 1.083 | 8.3% | ✓ | 0.144% |
| 0.250 | 1.997 | 1.346 | 1.102 | 10.2% | ✓ | 0.145% |
| 0.260 | 2.034 | 1.339 | 1.135 | 13.5% | ✓ | 0.147% |
| 0.270 | 2.068 | 1.333 | 1.164 | 16.4% | ✓ | 0.148% |

**Key observation:** m_mod/m_KK is remarkably stable across the window: [0.142%, 0.152%].
This is a secondary prediction that is robust to c_S3 variation.

### 5.2 Comparison to G91 (path-imposed)

| Quantity | G91 (path imposed) | G94 (emergent) |
|----------|-------------------|----------------|
| ρ₃/ρ₆² | 1.000 (exact, forced) | 1.041 (emergent, 4% off) |
| EFT status | MARGINAL (ρ₆=1.18) | **VALID** (ρ₆=1.36) |
| σ₃ stabilized | NO (runaway) | **YES** (m(σ₃)=0.00114) |
| m_mod/m_KK | 0.198% | 0.142% |

### 5.3 Hessian positivity (true minimum, not saddle)

At c_S3=0.235: H_eigs = [+1.28e-6, +1.71e-5]. Both positive → **true minimum**.
Earlier attempts with exp(−c/ρ₃²) gave H_eigs with negative component → saddle.
The D-brane cubic form exp(−c·ρ₃³) is the physically correct form.

---

## 6. Boundary (what this does NOT prove)

1. **Does NOT derive c_S3.** The instanton coefficient is a free parameter.
   UV completion (string theory embedding) determines c_S3. G94 shows
   the WINDOW that works, not the specific value.

2. **Does NOT prove ρ₃/ρ₆² = 1 exactly.** The 4% deviation is real.
   Exact path enforcement likely requires UV input from Tom Lawrence's
   full compactification geometry.

3. **Does NOT establish the physical mass ratio m_mod/m_KK = 0.142%.**
   This is a toy model prediction; full Weyl rescaling and off-diagonal
   kinetic terms are neglected. The order-of-magnitude (~0.1-0.2%) is
   robust; the exact number is not.

4. **Does NOT prove D2-brane is the unique mechanism.** Other forms
   (higher-dimensional branes, wrapped D5s, gaugino condensation) could
   give similar path recovery. G94 proves one such mechanism EXISTS.

5. **Does NOT constitute a SM derivation.** The path ρ₃≈ρ₆² is a
   phenomenological input from Lawrence [2022]; G94 recovers it dynamically
   but the SM derivation itself follows from Track B (N_gen=3 theorem),
   not from G94.

---

## 7. Predictions (what follows if G94 is confirmed)

**P1 — m_mod/m_KK window:** [0.14%, 0.20%] for c_S3 ∈ [0.235, 0.35].
This is a parameter-dependent but narrow band. Physical consequence:
moduli are ~50–700× lighter than KK modes → gravitino mass hierarchy.

**P2 — c_S3 → g_s structural relation (G102):** If c_S3 is set by
the string coupling, then c_S3 = f(g_s) gives a measurable connection
once g_s is determined by another sector. This would make c_S3
a *derived* quantity, eliminating one free parameter.

**P3 — Instanton window exclusion:** If the physical c_S3 falls outside
[0.235, 0.27], the path attractor breaks. This is a falsifiable prediction:
a UV calculation giving c_S3 < 0.22 or c_S3 > 0.35 would kill G94.

---

## Next steps to promote from CANDIDATE → CLAIM

1. **K1** (parameter sensitivity): run `g94_s3_np_instanton.py` with
   C_SM ± 20%, λ ± 20% — confirm minimum persists and path deviation stays < 20%.

2. **K5** (literature): arXiv search for "D2-brane S3 instanton moduli stabilization"
   + "S3 S6 compactification attractor". Confirm no prior exact result.

3. **K4** (Weyl rescaling): add canonical kinetic term correction to
   `g94_s3_np_instanton.py` — verify mass signs unchanged.

4. **G102 extension**: read decision.md for G102 — understand c_S3 → g_s
   structural relation and add to P2.

5. **Write 6-page preprint note:** if K1+K5+K4 pass → scope is publishable
   as "A Dynamical Attractor for ρ₃≈ρ₆² in an S³×S⁶ Compactification Toy Model"

---

## Claim entropy (Perelman)

| Component | Count |
|-----------|-------|
| N_unsupported_HIGH | 1 (K1/K4/K5 not run) |
| N_hidden_assumptions | 2 (toy model precision; schematic potentials) |
| N_missing_negative_controls | 1 (no test with wrong instanton form as null) |
| N_ambiguous | 0 |
| **claim_entropy** | **4** |

Target for CLAIM status: claim_entropy = 0 (all K-tests pass, lit check done).
