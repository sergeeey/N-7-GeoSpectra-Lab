# S³ Spinor Harmonics Sync Audit

**Date:** 2026-06-04
**Operator:** Sergey Boyko
**Trigger:** Sync gap between work PC / current PC / vault / repo after autonomous literature audit session
**Type:** Read-only verification + claim classification. No code changes, no commits.

---

## Purpose

Resolve sync/desync between the autonomous literature-audit session (which produced findings on S³ spinor harmonics, Camporesi-Higuchi 1996, Ben Achour 2016, and a code review of `cc_toy_lab/spectral/dirac_s3.py`) and the current machine state. Classify all claims by verification status before any of them inform downstream decisions (Tom letter, CLAIMS_AND_CAVEATS edit, new module).

---

## Repo State

```
Latest commit (HEAD):  f19d265   docs: add one-page PROJECT_SKETCH.md + Current Claim Boundary block in README
Branch:                main (tracking origin/main, in sync)
Other branches:        backup/unsafe-code-fixes-before-cleanup
                       feature/gate-4b-parameterize-runner
                       feature/gate4b-rerun-docs-2026-05-31

Working tree:          DIRTY
  Modified (tracked):   .claude/settings.local.json
                        reports/GATE_4B_v0.1.24_COMPARISON_TEMPLATE.md
                        reports/GATE_4B_v0.1.24_DOWNLOAD_SUMMARY.md
                        reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md
                        reports/NEXT_STEPS_2026-05-31.md
                        scripts/download_v0.1.24_results.sh
                        scripts/run_negative_controls_batches_3_6.sh
                        scripts/server_status_check.sh
  Untracked:            .claude/checkpoints/
                        reports/SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md
                        scripts/run_spectral_circle_extended_v0_1_22.py
```

**Note on expectation `116247a`:** The expected `latest commit = 116247a` was NOT met. `116247a` does not appear in `git log --oneline -30`. The current HEAD `f19d265` is the most recent commit on `origin/main`. No discrepancy with remote — the expectation appears to be from a different machine/branch context. Reporting as-is.

---

## Artifacts Found

| Artifact | Location | Tracked? | Size | Modified |
|---|---|---|---|---|
| `SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md` | `reports/` | ❌ untracked | 7463 B | 2026-06-05 13:51 |

**Other artifacts referenced in the autonomous session** (`knowledge/physics/spinor-harmonics-s3-literature-2026-06-04.md`, `correspondence/tom-letter-enrichment-draft-2026-06-04.md`, `daily/2026-06-04-autonomous-research-summary.md`) are reported to live in the Obsidian vault under `C:\Users\serge\.claude\memory\`, NOT in the repo. They are out of scope for this repo-side audit. They are NOT verified here.

---

## Code Audit: `cc_toy_lab/spectral/dirac_s3.py`

**File present:** yes. 143 lines. Read in full.

### What the file actually does (verbatim mechanism)

1. Defines `build_s3_dirac_operator(j_max, radius)` (lines 24-115).
2. Initializes `operator = np.zeros((total_dim, total_dim), dtype=complex)` — a square zero matrix (line 83).
3. Sets ONLY diagonal entries:
   - `k=0` negative-branch block: `operator[i,i] = -1.5/radius` (lines 87-91)
   - For each `k ∈ {1, ..., j_max+1}`: positive block `operator[i,i] = (k+0.5)/radius` and negative block `operator[i,i] = -(k+1.5)/radius` (lines 93-107)
4. Hermitizes via `0.5 * (operator + operator.conj().T)` (line 110) — trivial for a real diagonal matrix.
5. Returns `(operator, chirality)` where `chirality = np.ones(total_dim, dtype=float)` is a placeholder (line 113).
6. Defines `s3_dimension(j_max)` (lines 118-143) — pure arithmetic, returns dimension count from same degeneracy formula.

### Mockup vs differential operator — confirmation

The constructed matrix is **diagonal by construction**. Its eigenvalues are the hard-coded numbers `(k+0.5)/R` and `-(k+1.5)/R` with the correct multiplicities. Its eigenvectors are the standard basis vectors `{e_i}` of `C^total_dim` (this is automatic for any diagonal matrix).

- No spherical-harmonic functions are computed anywhere in the file.
- No coordinates (Hopf, geodesic-polar, or other) are used.
- No `(1/2) ω_{abc} Σ^{bc}` spin-connection term appears.
- No Γ-matrices, no Jacobi polynomials.
- The file's own docstrings call it "GATE 2 STATUS: FULL EIGENVALUE IMPLEMENTATION" (line 3) and cite arXiv:1103.4097 for the eigenvalue formula only.

### Exported symbols

- `build_s3_dirac_operator(j_max, radius=1.0) -> (operator, chirality)`
- `s3_dimension(j_max) -> int`

### Verification verdict on the "diagonal mockup" claim

**VERIFIED_FROM_CODE.** The file is a spectrum-only construction: correct eigenvalues placed on the diagonal of a zero matrix, with no spinor harmonic content. The autonomous session's characterization of the file matches the code at the line level.

---

## Literature Claims Classification

Each major claim in `SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md` is classified here.

| # | Claim | Class | Comment |
|---|---|---|---|
| C1 | "Tom's α-problem is fully solved in the literature" | **OVERCLAIM_RISK** / **NEEDS_EXTERNAL_SOURCE_CHECK** | "Fully solved" is a strong universal claim. Literature gives explicit S³ Dirac eigenspinors in geodesic-polar coords. Whether this constitutes a complete answer to Tom's specific α-problem in his coordinate-and-symmetry framework is for Tom to judge, not us. |
| C2 | "`dirac_s3.py` is a diagonal eigenvalue mockup, not a differential operator" | **VERIFIED_FROM_CODE** | Confirmed line-by-line above. |
| C3 | "S³ factor is architecturally passive in the Kronecker product `H = D² ⊗ I + I ⊗ P`" | **VERIFIED_FROM_CODE** (partial) | Kronecker structure verified in `s3_s1_product_discretized.py` line 88. The "passive" interpretation is mathematically correct for a diagonal `D²`. |
| C4 | "ALL DISCRETIZATION_SENSITIVE variation comes from the S¹ family" | **HYPOTHESIS** / **OVERCLAIM_RISK** | Logically follows from C3 in the ideal case, but not empirically verified by rerun on this machine. Safer phrasing: "the S¹ factor is the only source of family-to-family variation in the current construction." |
| C5 | Camporesi-Higuchi eq 3.9 = explicit spin connection | **NEEDS_EXTERNAL_SOURCE_CHECK** | Equation numbers cited from memory of an earlier read. Not independently verified on this machine. |
| C6 | Camporesi-Higuchi eq 3.25 = Jacobi-polynomial angular eigenfunction | **NEEDS_EXTERNAL_SOURCE_CHECK** | Same — quoted from memory. |
| C7 | "`√sin(2α)` is the measure factor `√g`, never an eigenfunction" | **HYPOTHESIS** (interpretive) | The identity `(1−cos2α) = 2sin²α` is correct. The conclusion that Tom's ansatz equals the measure factor is an interpretation of Tom's reasoning, not a quote from Tom. |
| C8 | "Tom omitted the spin-connection term in his Lie derivative" | **HYPOTHESIS** / **OVERCLAIM_RISK** | We have not inspected Tom's actual derivation in detail. We do not know which covariant derivative he uses. This is a guess about an expert's 21-year program. Strongest care needed. |
| C9 | "The lowest mode (S=0, D=0, n=0) gives Φ = const" | **VERIFIED_FROM_LOCAL_DOCS** (math) | Pure algebraic substitution; can be checked from the formula reported in the audit document itself. |
| C10 | "v0.1.24 verdict is correct, just now better understood" | **SAFE** | Does not change the verdict; only adds an interpretation layer. |
| C11 | "A future `dirac_s3_full.py` would address Tom's framework directly" | **SAFE** (recommendation, not claim) | Forward-looking, not a claim about current state. |

---

## Safe Findings

The following can be taken forward to manual review without additional verification:

1. **`dirac_s3.py` is a diagonal eigenvalue mockup.** Eigenvalues correct by construction (`±(k+3/2)/R` for `k=0`, `±(k+1/2)/R` and `±(k+3/2)/R` for `k≥1`), eigenvectors = standard basis. No spinor harmonic content. (C2)
2. **The Kronecker product `H = D²_S³ ⊗ I + I ⊗ P_S¹` makes the S³ factor a diagonal block-scaling.** (C3)
3. **The v0.1.24 `DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC` verdict remains valid** — this audit adds an interpretation layer; it does not change or contradict the verdict. (C10)
4. **One algebraic identity inside the document checks out** — `(1−cos 2α) = 2 sin²α` and `(1+cos 2α) = 2 cos²α`. (C9)

---

## Unsafe / Overclaim Findings

The following must NOT be transmitted externally (e.g. to Tom) or written into `docs/CLAIMS_AND_CAVEATS.md` without independent verification:

1. **"Tom's α-problem is fully solved in the literature."** (C1) — overclaim. Strongest defensible phrasing: "Two peer-reviewed references (Camporesi-Higuchi 1996; Ben Achour 2016) construct explicit S^N spinor / vector harmonics with Jacobi-polynomial angular dependence; whether they resolve Tom's specific question is for him to judge."
2. **"Tom omitted the spin-connection term."** (C8) — speculative claim about another researcher's derivation. We have not read Tom's actual derivation step-by-step.
3. **Camporesi-Higuchi equation numbers (3.9, 3.25, 3.26, 3.34) and formula quotations** (C5, C6) — cited from session memory, not from a local copy of the paper. Verify against the actual PDF before quoting in any external message.
4. **"√sin(2α) is the measure factor `√g`."** (C7) — interpretive claim that requires Tom's confirmation. We can show algebraically what `√g` is in his coordinates, but cannot assert what Tom's ansatz "is essentially."
5. **"ALL DISCRETIZATION_SENSITIVE variation comes from the S¹ family."** (C4) — too universal. Soften to "the S¹ factor is the only source of family-to-family variation in the current construction; the S³ factor enters only as a diagonal block scaling."

---

## Recommended Next Step

**MANUAL_REVIEW_REQUIRED** — proceed in this order:

1. **Manual review of the Camporesi-Higuchi 1996 PDF** (locate a clean copy of arXiv:gr-qc/9505009 on this machine or fetch it; verify eq 3.9 and eq 3.25 against the actual text). Until this step is done, claims C5 and C6 remain `NEEDS_EXTERNAL_SOURCE_CHECK`.
2. **Manual review of Ben Achour 2016** (already on disk per session log — verify eq 3 quotation).
3. **Soften the four overclaim-risk claims** (C1, C4, C7, C8) in any document that is forwarded to Tom or written into project docs. Use the safer phrasings listed in the table above.
4. **Hold all external communication and all `git add`/`commit` operations until steps 1–3 are done.**
5. Only after the above: decide whether to `git add reports/SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md` AND/OR add a paragraph to `docs/CLAIMS_AND_CAVEATS.md`. The CLAIMS_AND_CAVEATS edit should reflect only the SAFE findings list above, not the unsafe ones.

---

## What this audit did NOT do (explicit list)

- ❌ No compute, no rerun, no negative controls
- ❌ No code changes
- ❌ No README changes
- ❌ No `docs/CLAIMS_AND_CAVEATS.md` edits
- ❌ No Tom letter
- ❌ No `git add`, no commit, no push
- ❌ No external scientific claims
- ❌ No verification of the autonomous-session vault notes (`knowledge/`, `correspondence/`, `daily/`) — those are out of scope for repo-side audit

---

**Generated:** 2026-06-04 (sync audit session, read-only)
