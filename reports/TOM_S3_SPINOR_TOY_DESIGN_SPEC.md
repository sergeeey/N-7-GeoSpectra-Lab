# Tom-compatible S³ Spinor-Harmonic Sanity Tester — Design Spec

> ⚠️ **DRAFT / DESIGN SPEC / NOT A RESULT.**
> This document proposes a future Tom-compatible S³ spinor-harmonic sanity tester.
> It does **not** claim to solve Tom's α-problem.
> It does **not** claim current GeoSpectra tests Tom's theory.
> Literature equation numbers and coordinate conventions require manual PDF verification
> before any claim is forwarded externally. See claim classification in
> `reports/S3_SPINOR_HARMONICS_SYNC_AUDIT_2026-06-04.md`.

**Date:** 2026-06-05  
**Status:** Phase 0 — design spec only. No code, no compute, no commits.  
**Author:** Sergey Boyko  
**Trigger:** Tom Lawrence's open α-problem on S³ spinor harmonics (CAMP 2026-05-26 followup)  
**Linked audit:** `reports/SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md`  
**Linked sync-check:** `reports/S3_SPINOR_HARMONICS_SYNC_AUDIT_2026-06-04.md`

---

## 1. Purpose

This instrument is NOT about Anderson localization, IPR, or disorder sweeps.
It answers a different question:

> **Can we build a minimal, literature-grounded S³ geometry tool
> that makes the differences between orbital and spinorial generators
> numerically visible — in a form Tom can inspect?**

Tom's α-problem (CAMP 2026-05-26, Part 3 video, slide 95) appears to concern the
α-dependence of spinor harmonics on S³. His open question may involve a `√sin(2α)`
ansatz. Based on unverified literature notes [HYPOTHESIS — requires PDF check],
the correct α-dependence in the Camporesi-Higuchi construction is a Jacobi polynomial,
not `√sin(2α)`. Whether this is actually Tom's issue is unknown — we have not read
his derivation step-by-step (Sync Audit C8: HYPOTHESIS/OVERCLAIM_RISK).
A sanity tester that makes both forms numerically visible could be a useful
conversation starter — not a solution.

---

## 2. Relationship to Current GeoSpectra Pipeline

### What this instrument IS NOT:
- Not a replacement for Gate 4B / Negative Controls
- Not a modification of `cc_toy_lab/spectral/s3_s1_product_discretized.py`
- Not a rerun of existing experiments
- Not a new version of `v0.1.22` or `v0.1.24`

### Why a separate instrument is needed:

Current `cc_toy_lab/spectral/dirac_s3.py` (143 lines, verified 2026-06-04) is a
**diagonal eigenvalue mockup**. It places correct eigenvalues
`λ = ±(k + 3/2)/R` on the diagonal of a zero matrix, giving correct degeneracies
from arXiv:1103.4097. It does NOT contain:

- Spinor harmonic functions ψ(α, φ, θ)
- Hopf or geodesic-polar coordinates
- Spin connection `(1/2) ω_{abc} Σ^{bc}`
- Γ-matrices or Pauli matrices in any coordinate basis
- Jacobi polynomial α-dependence

This is not a bug. For the Kronecker product
`H = D²_S³ ⊗ I_S¹ + I_S³ ⊗ P_S¹` the mockup is sufficient and correct —
in the current construction, the S³ factor enters as a diagonal block-scaling,
and [HYPOTHESIS — Sync Audit C4] the observed family-to-family variation in v0.1.24
appears to arise from the S¹ discretization family. This is not empirically verified
by rerun on current machine; the safer phrasing is: "the S¹ factor is the only
source of family-to-family variation in the current construction."

But for a conversation with Tom about his α-problem, the mockup is insufficient.

---

## 3. Non-Goals (explicit)

- ❌ Does NOT prove or disprove Tom Lawrence's covariant compactification theory
- ❌ Does NOT test S³×S⁶ or any product with S⁶
- ❌ Does NOT make any compactification claim
- ❌ Does NOT replace or modify the v0.1.24 Negative Controls pipeline
- ❌ Does NOT run Gate 4B or any existing benchmarks
- ❌ Does NOT claim Tom's α-problem is "fully solved" (that is an overclaim — see Sync Audit C1)
- ❌ Does NOT send anything to Tom without Sergey's explicit approval

---

## 4. Literature Foundation (already audited)

Two peer-reviewed sources identified in `SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md`:

### Camporesi & Higuchi 1996 — gr-qc/9505009

Core reference for S^N spinor harmonics.

| Eq. | Content | Relevance |
|---|---|---|
| 3.1 | `ds²_N = dθ² + sin²θ ds²_{N-1}` — geodesic-polar coordinates | metric on S³ |
| 3.5 | `ω_{ijk} = (1/sinθ) ω̃_{ijk}`, `ω_{iNk} = cosθ/sinθ δ_{ik}` | spin connection |
| **3.9** | `∇_a ψ = ∂_a ψ − (1/2) ω_{abc} Σ^{bc} ψ` | spin connection term [HYPOTHESIS: may be absent in orbital-only treatment] |
| 3.25 | `φ_{nl}(θ) = (cosθ/2)^{l+1} (sinθ/2)^l P^{(N/2+l-1, N/2+l)}_{n-l}(cosθ)` | Jacobi-polynomial α-eigenfunction |
| 3.26 | `λ²_{n,N} = (n + N/2)²` → S³: `λ = ±(n + 3/2)` | eigenvalue formula |
| 3.34 | `∇̸ ψ^{(s)}_{±nlm} = ±i(n + N/2) ψ^{(s)}_{±nlm}` | full first-order Dirac eq |

**Claim status [NEEDS_EXTERNAL_SOURCE_CHECK]:** Eq. numbers cited from autonomous
session memory — NOT verified against actual PDF on this machine.
MUST verify gr-qc/9505009 sections 3.1, 3.5, 3.9, 3.25, 3.26, 3.34 by reading
the actual paper before quoting in any external document.
See Sync Audit items C5, C6 → NEEDS_EXTERNAL_SOURCE_CHECK.

### Ben Achour et al 2016 — arXiv:1505.03426v2

**⚠️ CRITICAL SCOPE NOTE [VERIFIED_FROM_PDF — 2026-06-05]:**
This paper is titled *"Explicit **vector** spherical harmonics on the 3-sphere"*.
It constructs eigenmodes of the **Laplace-de Rahm operator on one-forms (vector harmonics)**,
NOT spinor harmonics. Scalar modes in Section II are used as building blocks for vector modes.
The Dirac operator does not appear. Camporesi-Higuchi remains the primary reference for
spinor harmonics. This paper is valid for Hopf coordinates and scalar mode structure only.

| Eq. | Content | Verification status |
|---|---|---|
| 1 | `x¹ = sinα cosφ`, `x² = sinα sinφ`, `x³ = cosα cosθ`, `x⁴ = cosα sinθ` | **[VERIFIED_FROM_PDF ✅]** |
|   | `ds² = dα² + cos²α dθ² + sin²α dφ²`, α ∈ [0, π/2] | **[VERIFIED_FROM_PDF ✅]** |
| 2 | `ΔΦᵢ = λᵢΦᵢ`, `λᵢ = −L(L+2)`, L ∈ ℕ | **[VERIFIED_FROM_PDF ✅]** |
| 3 | `Φ = C_{L,m₊,m₋} e^{i(Sφ+Dθ)} (1−x)^{S/2} (1+x)^{D/2} P^{(S,D)}_{L/2−m₊}(x)` | **[VERIFIED_FROM_PDF ✅]** |
|   | `x = cos(2α)`,  `S = m₊+m₋`,  `D = m₊−m₋` | **[VERIFIED_FROM_PDF ✅]** |

Key identity [VERIFIED]: `(1 − cos 2α) = 2 sin²α`, `(1 + cos 2α) = 2 cos²α`.

Lowest scalar mode (S=0, D=0, n=0): **`Φ = const`** [VERIFIED_FROM_PDF ✅].

`√sin(2α)` in the scalar sector [VERIFIED_FROM_PDF ✅]:
From eq (3): `(1−x)^{S/2} = 2^{S/2} sinˢα`. For integer quantum numbers (S,D),
the mode is always `sinˢα · cosᴰα · P^{(S,D)}_n(cos2α)`.
The form `√sin(2α) = √(2 sinα cosα)` does NOT appear for any (S,D,n)
in this scalar mode basis. This is now **verified from the PDF**, not from memory.

**Note on Tom's ansatz [HYPOTHESIS/interpretive — Sync Audit C7, unchanged]:**
This verification applies to **scalar modes** of the Laplace-Beltrami operator.
Tom's framework may involve spinor modes (Dirac operator) — a different space.
Whether the scalar result generalises to his spinor ansatz is for Tom to judge.
We cannot assert what his `√sin(2α)` represents without reading his derivation.

### Existing project reference: arXiv:1103.4097

Already cited in `cc_toy_lab/spectral/dirac_s3.py` (line 8).
Provides eigenvalue formula `λ = ±(n + 3/2)/R` and degeneracy structure.
This is what the current diagonal mockup reproduces correctly.

---

## 5. Core Physical Concepts to Implement

### 5.1 Hopf Coordinates on S³

S³ embedded in ℝ⁴:
```
x¹ = sinα cosφ
x² = sinα sinφ
x³ = cosα cosθ
x⁴ = cosα sinθ

α ∈ [0, π/2],  φ ∈ [0, 2π),  θ ∈ [0, 2π)
```

Metric:
```
ds² = dα² + sin²α dφ² + cos²α dθ²
```

Volume measure:
```
√g = sinα cosα = (1/2) sin(2α)
```

Key sanity check: `∫ √g dα dφ dθ = 2π²` (volume of unit S³).

### 5.2 Spin Connection

Geodesic-polar coordinates (Camporesi-Higuchi eq 3.5):
```
ω_{ijk} = (1/sinθ) ω̃_{ijk}   (tangential component)
ω_{iNk} = (cosθ/sinθ) δ_{ik}  (radial component)
```

The full covariant spinor derivative:
```
∇_a ψ = ∂_a ψ − (1/2) ω_{abc} Σ^{bc} ψ
```

where `Σ^{bc} = (1/4)[Γ^b, Γ^c]` are the spin generators.

**This is the term absent in a purely orbital (non-spinorial) Lie derivative.**
[HYPOTHESIS — Sync Audit C8]: whether Tom's specific generator omits this term
is unknown. We have not inspected his derivation. Do not state externally that
"Tom omitted the spin connection" without first reading his framework.

### 5.3 Orbital vs Spinorial Generator

| Generator type | Formula | Spin connection included |
|---|---|---|
| Orbital (Lie derivative, scalar) | `L_ξ ψ = ξ^a ∂_a ψ` | ❌ No |
| Kosmann/spinorial | `L^K_ξ ψ = ξ^a ∇_a ψ + (1/4)(∇_a ξ_b − ∇_b ξ_a) Γ^{ab} ψ` | ✅ Yes |
| Standard in Camporesi-Higuchi | `∇̸ = Γ^a ∇_a` | ✅ Yes |

Key insight for Tom: if one uses only the orbital part, the spin connection term
`(1/2) ω_{abc} Σ^{bc}` is missing, which changes the α-dependence of eigenmodes.

### 5.4 Pauli / Gamma Matrix Conventions (S³, N=3)

For S³ (3-dimensional), the Clifford algebra is generated by 2×2 Pauli matrices:
```
Γ¹ = σ₁,  Γ² = σ₂,  Γ³ = σ₃
```
or equivalently by the SU(2) generators. The spinor representation is 2-component.

Convention must be fixed before any calculation. Standard choice: Pauli matrices
in Cartesian embedding, then pull back to Hopf/geodesic-polar vielbeins.

### 5.5 Known S³ Spinor Harmonic Spectrum (Sanity Baseline)

From arXiv:1103.4097 + Camporesi-Higuchi 1996:

| Level k | λ_+ (positive) | deg_+ | λ_- (negative) | deg_- |
|---|---|---|---|---|
| 0 | — | — | -3/2 | 2 |
| 1 | +3/2 | 2 | -5/2 | 6 |
| 2 | +5/2 | 6 | -7/2 | 12 |
| 3 | +7/2 | 12 | -9/2 | 20 |
| k | +(k+1/2) | k(k+1) | -(k+3/2) | (k+2)(k+1) |

This table is what `dirac_s3.py` reproduces by construction (diagonal mockup).
The sanity tester would reproduce the SAME table, but via actual Jacobi polynomials.

---

## 6. Proposed Directory Structure

```
N-7-GeoSpectra-Lab/
└── tom_s3_spinor_toy/
    ├── README.md                          # Purpose, non-goals, literature refs
    ├── geometry_s3_hopf.py                # Hopf coordinates, metric, √g, volume check
    ├── gamma_matrices.py                  # Pauli/Clifford algebra, conventions
    ├── orbital_generators.py              # L_ξ (orbital only, no spin connection)
    ├── spin_connection.py                 # ω_{abc} components in geodesic-polar coords
    ├── kosmann_derivative.py              # L^K_ξ (orbital + spin connection term)
    ├── reference_spinor_harmonics.py      # Camporesi-Higuchi eq 3.25/3.32 construction
    ├── alpha_dependence_comparison.py     # Key deliverable: orbital vs full vs Tom ansatz
    ├── tests/
    │   ├── test_metric_volume.py          # Volume ∫√g = 2π²
    │   ├── test_algebra_sanity.py         # SO(4) ~ SU(2)_L × SU(2)_R algebra
    │   ├── test_generators.py             # Orbital vs spinorial commutators
    │   ├── test_eigenvalues.py            # Jacobi-polynomial → correct λ = ±(k+3/2)
    │   ├── test_alpha_ansatz.py           # √sin(2α) ≠ eigenfunction check
    │   └── test_overclaim_guards.py       # Assert no physical interpretation creeps in
    └── reports/
        ├── ALPHA_COMPARISON_NOTE.md       # Key result: what changes with spin connection
        └── NOTE_FOR_TOM.md               # Phase 3 deliverable (after Phase 2 complete)
```

---

## 7. Implementation Phases

### Phase 0 — Design Spec (current document)
**Status:** ✅ This document  
**Deliverable:** `reports/TOM_S3_SPINOR_TOY_DESIGN_SPEC.md`  
**Review:** Manual review by Sergey before Phase 1

### Phase 1 — Literature Verification (before any code)
**Goal:** Verify equation numbers and formula quotations against actual PDFs.

| Task | Source | Verification method |
|---|---|---|
| Verify Camporesi-Higuchi eq 3.9 (spin connection formula) | gr-qc/9505009 PDF | Read paper, locate equation |
| Verify Camporesi-Higuchi eq 3.25 (angular eigenfunction) | gr-qc/9505009 PDF | Read paper, check Jacobi indices |
| Verify Ben Achour eq 1 (Hopf coordinates) | arXiv:1505.03426 PDF | Read paper, check metric |
| Verify Ben Achour eq 3 (scalar mode) | arXiv:1505.03426 PDF | Read paper, verify (S,D,n) labeling |
| Establish Γ-matrix convention | Choose one, document source | Cross-check with spectral formula |

**Block:** Do NOT write Phase 2 code until Phase 1 verification complete.  
**Output:** Annotated equation list in `tom_s3_spinor_toy/README.md`.

### Phase 2 — Symbolic / Numeric Sanity Checks (light compute)
**Goal:** Verify geometry, algebra, and α-dependence numerically.

| Module | Key check | Pass condition |
|---|---|---|
| `geometry_s3_hopf.py` | Volume: `∫₀^{π/2} ∫₀^{2π} ∫₀^{2π} sinα cosα dα dφ dθ` | Result = 2π² ± 1e-10 |
| `gamma_matrices.py` | Clifford algebra: `{Γᵃ, Γᵇ} = 2δᵃᵇ I` | Anticommutator correct |
| `orbital_generators.py` | Commutator algebra on S³ scalar | `[L_i, L_j] = ε_{ijk} L_k` |
| `kosmann_derivative.py` | Difference vs orbital: `L^K - L_orb = spin-connection term` | Non-zero for spinors |
| `reference_spinor_harmonics.py` | Jacobi polynomial at lowest mode (k=0): `ψ ∝ const` on S³ | Not `∝ √sin(2α)` |
| `alpha_dependence_comparison.py` | Plot orbital vs full vs `√sin(2α)` on α ∈ [0, π/2] | Clear visual difference |

**Compute budget:** All checks run in < 1 second on laptop. No GPU, no heavy matrix.

### Phase 3 — Note for Tom (after Phase 2 complete and reviewed)
**Goal:** One-page technical note, honest and precise.

Format:
```
1. What the literature says about α-dependence on S³ (Jacobi polynomial, not √sin(2α))
2. What our sanity tester shows numerically (Phase 2 results)
3. What would change if spin connection is included
4. What we do NOT know (Tom's specific derivation steps — we haven't read them)
5. Invitation: "Does this match your framework? Where does it differ?"
```

**NOT a claim that Tom's problem is solved.** A conversation tool.

---

## 8. Tests

### Correctness gates (must pass before claiming anything)

1. **Metric/volume consistency** — S³ volume = 2π² in Hopf coordinates
2. **Clifford algebra** — `{Γᵃ, Γᵇ} = 2δᵃᵇ I` for chosen convention
3. **SO(4) algebra sanity** — `[J_{ab}, J_{cd}] = δ_{bc} J_{ad} − ...` structure correct
4. **Orbital vs spinorial difference** — Kosmann−orbital = spin-connection term, non-zero for spinors
5. **Jacobi eigenvalue** — lowest mode of full Dirac gives `λ = -3/2` with Jacobi polynomial

### Scientific non-claim guards (must run before Phase 3)

6. **No overclaim on Tom** — `NOTE_FOR_TOM.md` must not contain "Tom's problem is solved"
7. **No ansatz equation** — `√sin(2α)` is explicitly shown to NOT be an eigenmode
8. **No physical theory claim** — no statement connecting this to compactification
9. **No modification to Gate 4B** — assert `dirac_s3.py` is unchanged

---

## 9. Risk Register

| Risk | Level | Mitigation |
|---|---|---|
| Wrong Γ-matrix convention → wrong commutators | HIGH | Fix convention in Phase 1; document source explicitly |
| Confusing scalar / vector / spinor harmonics | HIGH | Each function has explicit docstring on which harmonic type |
| Overclaiming Tom's α-problem is "solved" | HIGH | Overclaim guard test; softened language protocol (Sync Audit C1) |
| Mismatch with Tom's coordinate notation | MEDIUM | Present our coordinates explicitly; invite Tom to map to his |
| Using literature formula without source verification | MEDIUM | Phase 1 PDF verification is blocking for Phase 2 |
| Contaminating current GeoSpectra pipeline | LOW | Separate directory; no imports from `cc_toy_lab` |
| Reuse of `dirac_s3.py` (diagonal mockup) in this tester | LOW | `reference_spinor_harmonics.py` built fresh from Camporesi-Higuchi, not from mockup |

---

## 10. Deliverables by Phase

| Phase | Deliverable | Completion signal |
|---|---|---|
| 0 | `reports/TOM_S3_SPINOR_TOY_DESIGN_SPEC.md` | ✅ This document |
| 1 | Verified equation list in `tom_s3_spinor_toy/README.md` | All 5 literature checks have PDF page+line citation |
| 2 | All 9 tests in `tom_s3_spinor_toy/tests/` pass, plots in `reports/` | `pytest tom_s3_spinor_toy/tests/ -v` → 9 passed, 0 failed |
| 3 | `tom_s3_spinor_toy/reports/NOTE_FOR_TOM.md` | Sergey review + explicit send approval |

---

## 11. Recommended Immediate Next Step

**Manual review of this design spec by Sergey.**

Questions to answer before Phase 1:

1. Is the directory `tom_s3_spinor_toy/` in this repo the right location,
   or a separate branch?
2. Is Phase 1 (PDF verification) blocked by server access, or can it run locally?
3. Does Tom's α-problem in Part 3 slide 95 use geodesic-polar or Hopf coordinates?
   (determines which literature source is primary)
4. Is the `NOTE_FOR_TOM.md` Phase 3 output intended for email or LinkedIn?

**Do NOT start Phase 1 code or any literature fetch without answers to the above.**

---

## 12. What This Spec Did NOT Do

- ❌ No compute
- ❌ No code written
- ❌ No existing files modified
- ❌ No `dirac_s3.py` changes
- ❌ No Gate 4B / Negative Controls touched
- ❌ No Tom message drafted
- ❌ No git add, no commit, no push
- ❌ No physical theory claim

---

**Generated:** 2026-06-05  
**Next action:** Sergey review → decide on Phase 1 trigger  
**Block on:** Answers to 4 questions in Section 11
