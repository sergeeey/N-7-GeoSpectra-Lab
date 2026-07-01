# Tom's Reconstruction — Competing Hypotheses Matrix

**Purpose:** For each open node in Tom's construction, list competing hypotheses,
evidence that kills/supports each, surviving branches, and required discriminating tests.

**Rule:** Every evidence claim MUST cite a repo artifact (experiment folder, commit, file).
No memory-based assertions. [INFERRED] without artifact = not accepted.

**Kill target rule (Strong Inference):**
Every gate claim.md MUST include a `Kill target:` field — which hypothesis dies on FAIL.
Gates without kill target are not scheduled.

**Last updated:** 2026-06-11 (G4 PASS, commit dce2156+28b7e17)

---

## Status legend
- `KILLED` — falsified, do not retry without fundamentally different approach
- `LIVE` — not yet tested or not yet falsified
- `VERIFIED` — confirmed by sympy/pytest/PDF with artifact
- `OPEN` — evidence insufficient for any verdict
- `FORK` — two live hypotheses, discriminating test designed but not run

---

## Case 1 — sin(2α): What generates the radial-angular bilinear?

**Node:** item40 / eq.49 structure / sin(2α)/2 as the dominant term

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: scalar ansatz | sin(2α) ≈ φ·φ without g-component | `KILLED` | AV-1c′ (e5576d7): sparse φ·φ killed, null_results/20260610-ht1-sparse-bilinear.md |
| H2: sparse φφ bilinear (H-T1) | sparse fit reconstructs sin(2α) | `KILLED` | AV-1c′ (e5576d7): boundary exponent obstruction kills this route |
| H3: dense dictionary fit | sin(2α) = Σᵢ cᵢ φᵢ (many terms) | `DEMOTED` | AV-2 E1 (4025e79): 1-term exact identity found → dense fit unnecessary |
| H4: mixed φ·g spinor bilinear | φ₀₀(α)·g₀₀(α) = cosα·sinα = sin(2α)/2 | `VERIFIED` | AV-2 E1 (4025e79) STRONG_PASS: 1 term, 0% residual, exact |

**Surviving:** H4 only.

**Mechanism chain:**
```
AV-1c′ negative result → boundary exponent obstruction (AV-2 G2, 993981a)
→ two-component split required → mixed φ·g → exact identity
```

**Forbidden promotions from this node:**
- "sin(2α) reconstructed therefore full V-sector determined" — V-sector has independent unknowns (see Case 4)
- "sin(2α) exact therefore λ fixed" — λ multiplies V-coefficient separately (see Case 3)

**Next discriminating test:** None needed — VERIFIED. Archive.

---

## Case 2 — cot(2α): Physical singularity or frame artifact?

**Node:** Tom Q2 / spin connection term cot(2α) that appears in Hopf-coframe basis

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: physical singularity | cot(2α) survives in any frame; requires regularization | `KILLED` | G2 (fc30a28): invariant frame dσ₃/(σ₁∧σ₂)=2, cot(2α) absent |
| H2: convention/sign error | cot(2α) = typo or wrong sign in Tom's paper | `KILLED` | G2 (fc30a28) T6-T10: Hopf spin connection ω¹₂=+tanα e², ω¹₃=−cotα e³ confirmed |
| H3: Hopf-frame spin-connection artifact | tan(α)−cot(α)=−2cot(2α); vanishes in left-invariant frame | `VERIFIED` | G2 (fc30a28) 14/14: algebraic identity + frame comparison; dσ₃/(σ₁∧σ₂)=2 integer constant |

**Surviving:** H3 only. PASS_FRAME_ARTIFACT_CONFIRMED.

**Candidate answer to Tom Q2 (scoped):**
If Tom's "correct SO(4) spinor basis" = left-invariant frame, then cot(2α) vanishes automatically.
Awaiting Tom's confirmation of which frame he means.

**Forbidden promotions from this node:**
- "cot(2α) = artifact therefore all Hopf-basis terms are artifacts" — not proven beyond this specific term
- "frame artifact therefore geometry fully resolved" — λ and spin structure still open

**Next discriminating test:** Tom's reply to Q2. No code needed.

---

## Case 3 — λ_V: Is the coupling parameter fixed by the S³ geometry?

**Node:** P13H / V-operator coefficient / physical promotion gate

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: λ fixed by S³ alone | S³ Dirac + V-operator uniquely fixes λ | `KILLED` | G4 (dce2156): rank(J_phys)=2, λ-column=[0,0]ᵀ → structural non-identifiability proved [VERIFIED-sympy 7/7] |
| H2: λ fixed by background connection | spin connection sector determines λ independently | `OPEN` | G0 (ae05133): V = λ_geom·V_ω + Σcᵢ·Vmodes; λ_geom conditionally canonical (Tom Q3); G4 shows λ non-identifiable from S³-only observables |
| H3: λ free until external principle (S⁶, gauge, action) | S³-only invariants insufficient to fix λ | `VERIFIED_FORMAL_THEOREM` | G4 (dce2156) 7/7: rank(J_phys)=2 < 3 = \|θ\| — λ structurally non-identifiable. Identifiable IFF V promoted (rank(J_full)=3). λ=FREE_COUPLING_PARAMETER is a proved theorem. |

**Surviving:** H3 — VERIFIED_FORMAL_THEOREM. H1 formally killed by Jacobian rank. H2 open.

**Formal result (G4, [VERIFIED-sympy 7/7]):**
- `rank(J_phys) = 2`, `dim(θ) = 3` → λ-column of Jacobian identically zero — structural non-identifiability
- `rank(J_full) = 3` → λ identifiable IFF V observable promoted
- `det(J_full) = 32π²m₁²ρ / (15R²√(9R²+4m₁²))` — nonzero for all ρ,R,m₁>0
- Recovery formula: `λ = 15·V_obs / (16π²ρ³)` — linear, requires V promotion
- Corollary: V promotion is NECESSARY AND SUFFICIENT for λ identifiability

**Next discriminating test:** Tom's answer to Q3. After that: V-promotion decision.

---

## Case 4 — V-sector: Where do the V-operator modes come from?

**Node:** LAMBDA-B5 / E/E′ tower / background spin connection / mode decomposition

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: all V from E/E′ tower (Dereli-style) | V-modes = Σcᵢ^I Eᵢ/E′ᵢ, matchable by tuning cᵢ | `KILLED` | G0 (ae05133) 12/12: invariant one-forms ξ̃/ξ̃′ NOT in span(Eᵢ/E′ᵢ); E(L=0)≡0 exactly |
| H2: V = background + modes (structural split) | V = λ_geom·V_ω + Σcᵢ·Vmodes; two independent sectors | `LIVE` | G0 STRUCTURAL_SPLIT_REQUIRED: consistent with evidence, not yet fully parameterized |
| H3: pure phenomenological fit | V has no geometric structure; arbitrary coefficients | `DEMOTED` | sin(2α) exact bilinear (Case 1) contradicts pure phenomenology |

**Surviving:** H2 as working structure. H1 formally killed. H3 demoted.

**Forbidden promotions:**
- "structural split identified therefore V fully determined" — parameterization of split not complete
- "STRUCTURAL_SPLIT_REQUIRED therefore λ is geometric" — λ_geom is conditionally canonical (Tom Q3 open)

**Next discriminating test:** Tom's answer to Q3. After that, G4 identifiability.

---

## Case 5 — Dirac core on S³: Is the geometric Dirac structure sound?

**Node:** spectral fingerprint E₀~3/2, spin connection, curvature

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: Γ_a depends on frame/convention | spin connection not uniquely determined by S³ geometry | `KILLED` | G2 (fc30a28): invariant frame gives dσ₃/(σ₁∧σ₂)=2 (integer constant, frame-independent) |
| H2: spectrum ±(n+3/2) is convention artifact | physical operator is ambiguous | `KILLED` | G1 (afefbbe) 10/10: D_phys=−iγ^a∇_a uniquely defined; Lichnerowicz D²=9/4; T8 anti-Hermitian |
| H3: curvature does not generate su(2) | [∇_a,∇_b] ≠ (1/4)[γ_a,γ_b] | `KILLED` | G3 (afefbbe) 9/9: F_{ab}=(1/4)[γ_a,γ_b], Casimir=−(3/4)I, j=1/2 |
| H4: S³ Dirac core is sound and frame-independent | Γ_a=(i/2)γ^a, spectrum ±(n+3/2), su(2) curvature | `VERIFIED` | G1+G2+G3 combined; λ₀=3/2 matches k0_disc=1.4999999561 (BG-H1-E1) |

**Surviving:** H4. Fully verified. This is the strongest closed subgraph in the project.

**Key chain:**
```
G2: dσ₃/(σ₁∧σ₂)=2 (frame-invariant integer)
  → Γ_a = (i/2)γ^a
  → G1: D_phys spectrum ±(n+3/2), Lichnerowicz D²=9/4
  → G3: F_{ab}=(1/4)[γ_a,γ_b], su(2), j=1/2
  → BG-H1: λ²=(n+3/2)²+(m/R)² (S³×S¹ bridge)
```

**Forbidden promotions:**
- "Dirac core verified therefore full theory verified" — S⁶, hypercharge, chirality all OPEN
- "λ₀=3/2 matches numerics therefore geometry selected" — matching descriptive only (BG-H1 GEOMETRY_AGNOSTIC)

**Next discriminating test:** None for this node. VERIFIED closed subgraph.

---

## Case 6 — Spin structure: m∈ℤ (periodic) vs m∈ℤ+½ (anti-periodic)?

**Node:** KK spectrum on S¹ / BG-H1 fork / spin structure selection

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: m∈ℤ (periodic, P-spin structure) | ground state m=0 → δ₀=0 (zero mode present) | `LIVE` | BG-H1 (d3fee3a): δ(R,m=0)=0 analytically; fork reported, no selection |
| H2: m∈ℤ+½ (anti-periodic, AP-spin structure) | minimum m=½ → δ₀=δ(R,½)>0 (no zero mode) | `LIVE` | BG-H1 (d3fee3a): δ(R,½)=√(9/4+(1/2R)²)−3/2; fork reported, no selection |

**Status:** `FORK` — both live. No discriminating test run yet.

**Designed discriminating test (not yet run):**
Binary observable: **does the KK spectrum contain a zero mode δ₀=0?**
- P-spin (H1): YES, δ₀=0 always, regardless of R.
- AP-spin (H2): NO, minimum gap δ₀(R)=√(9/4+(1/2R)²)−3/2 > 0 for all finite R.
- Cost: pure analytic / sympy, no lattice. FL Standard.
- This test requires a physical context to apply: Tom's theory must specify which structure is expected.

**Kill target when designed gate runs:**
- FAIL H1 (no zero mode found): m∈ℤ killed → H2 surviving
- FAIL H2 (zero mode required): m∈ℤ+½ killed → H1 surviving

**Constraint:** Do not run selection gate until Tom answers Q1 (replacement basis correctness).

---

## Case 7 — N_gen=3: does triality genuinely give 3 distinct channels, or does G2 collapse them?

**Node:** G73's "N_gen=3 PROMOTE" verdict vs G44's "D4 triality on S3xS6 REJECT" verdict —
both rest on the SAME underlying fact (G2=Fix(Z3): 8_v|G2 = 8_s|G2 = 8_c|G2 = 7+1
identically) but reach apparently different conclusions. Added 2026-07-01 (G100 audit)
after this relationship was found to be absent from this matrix and from README.md.

| Hypothesis | Prediction | Verdict | Evidence |
|---|---|---|---|
| H1: G2-triality-collapse kills any 3-channel mechanism on S3xS6 | since G2 can't distinguish 8_v/8_s/8_c, no geometric construction using only G2 structure can give 3 distinct index contributions | `PARTIALLY_VERIFIED` | G44 (2026-06-20, REJECT): kills the specific "one bundle, index enhanced to 3 by triality symmetry" mechanism on exactly this basis |
| H2: 3 distinct physical channels (L_p, R_p, T_p octonion mult.) exist independently in the S3xS6 Dirac action, each individually ordinary (c3=2, index=1), summing to 3 | index=1 per channel is unaffected by G2 blindness (each channel's c3 is computed directly, not "enhanced" by symmetry); only the EXISTENCE of 3 separate channels in the action needs proof | `PARTIAL_CLOSURE (2/3)` | **G68 (2026-06-21, 28/28 tests):** L_i and R_i octonion multiplication matrices ARE rigorously distinct — both satisfy Cl(0,7) Clifford relations separately, but the pseudoscalar differs (Ω_L=+I₈ ≠ Ω_R=−I₈), an actual invariant, not a relabeling. 2 of 3 channels (8_s=L, 8_c=R) are genuinely, algebraically inequivalent representations. **Still open:** the third (8_v, vector) channel — G68 states explicitly it "does NOT arise from left or right O-multiplication by any standard construction"; its geometric realization on S3xS6 needs G72 (Tom input). G73 (2026-06-21, PROMOTE 29/29 on the ARITHMETIC given H2) uses the algebraic c3-equality argument for all 3, not G68's explicit construction. |

**Surviving:** Both, for different questions. H1 (G44) correctly kills a DIFFERENT mechanism
(single-bundle symmetry-enhancement) than H2 (G73) requires (three separate channels).
G73's PROMOTE verdict is conditional on H2, which is 2/3 rigorously closed (G68: L vs R
genuinely inequivalent Clifford reps) and 1/3 open (8_v vector channel, needs G72/Tom) —
this partial-closure state was honestly flagged in G67/G68's own text but was never
connected to G44's REJECT verdict at the summary-document level, and G68 itself was also
missing from README.md/RESEARCH_STATUS_REPORT.md before this update.

**Forbidden promotions from this node:**
- "N_gen=3 is fully geometrically derived" — conditional on G67-C3 (H2), still OPEN
- "G44's REJECT contradicts G73's PROMOTE" — they answer different questions (single-bundle
  enhancement vs three-separate-channels existence); not a logical contradiction, but the
  SHARED premise (G2 cannot distinguish the three reps) means H2 needs an INDEPENDENT
  geometric argument for why three channels appear, not just "triality says so"
- "the E_v/E_s/E_c bundles are geometrically distinct objects" — this is exactly what
  remains unproven; G73 uses their EQUALITY of G2-content (which G44 also uses) only to
  argue each would individually give c3=2 IF they exist as separate objects

**Next discriminating test:** Resolve G67-C3 — either construct L_p/R_p/T_p as genuinely
distinct bundles on S3xS6 (geometric), or find the G72 input from Tom that specifies which
mechanism realizes all three channels physically. Full record: `experiments/20260701-g100-ach-g44-g73-audit/`.

---

## Summary table

| Case | Node | Surviving | Status | Next action |
|---|---|---|---|---|
| 1 | sin(2α) | H4: mixed φ·g | VERIFIED | Archive |
| 2 | cot(2α) | H3: Hopf-frame artifact | VERIFIED | Await Tom Q2 reply |
| 3 | λ_V | H3: free until external | VERIFIED_FORMAL_THEOREM | Await Tom Q3; then V-promotion |
| 4 | V-sector | H2: structural split | LIVE | Await Tom Q3; then G4 |
| 5 | Dirac core | H4: verified geometry | VERIFIED | Closed subgraph |
| 6 | Spin structure | H1 / H2 both | FORK | Await Tom Q1 |
| 7 | N_gen=3 (G44 vs G73) | H1 (G44) + H2 (G73), different questions | PARTIAL (H2 = G67-C3: 2/3 closed by G68, 1/3 open) | Resolve 8_v channel; needs G72/Tom or new geometry |

## Forbidden promotions (consolidated)

These claims cannot be made regardless of future results unless the blocking dependency is resolved:

| Claim | Blocked by |
|---|---|
| "λ is fixed" | Case 3 H1 formally killed by G4 (rank proof); Tom Q3 open; V-promotion BLOCKED |
| "physical V promoted" | λ=FREE_COUPLING_PARAMETER; safe_for_runtime=False |
| "S³ geometry selects spin structure" | Case 6 FORK open; Tom Q1 unanswered |
| "SM generation derived from this" | S⁶ OPEN; hypercharge OPEN; chirality OPEN |
| "cot(2α) resolved → full spin-connection resolved" | Case 2 scope: one term only |
| "BG-H1 S³×S¹ bridge is physical" | GEOMETRY_AGNOSTIC; descriptive only |

---

*Every entry above cites a repo artifact. No memory-based claims.*
*To update: modify only cells with new experiment folder + commit reference.*
