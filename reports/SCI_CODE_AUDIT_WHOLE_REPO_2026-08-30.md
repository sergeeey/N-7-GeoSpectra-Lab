# SCI_CODE_AUDIT — Whole N-7-GeoSpectra-Lab Repo — 2026-08-30

**Methodology:** `sci-code-audit` skill, 10-layer trust audit (companion to `gate-check` and
`code-materiality`). Scope: both active code tracks, per root `CLAUDE.md`.

**Auditor stance:** presumption of falsity per FL. Findings below are marked
`[VERIFIED-tool]` (confirmed this session with Read/Grep/Bash/pytest/independent sympy
re-derivation) vs `[DOCS]` (taken from the project's own documentation/decision.md, not
independently re-run) vs `[HYPOTHESIS]` (plausible concern, not tool-confirmed).

---

## Scope actually covered (materiality-first, not exhaustive)

Given 100+ Track B experiment scripts and a multi-gate Track A pipeline, full read-every-file
coverage was not attempted (Layer 0 discipline: declare scope rather than fake completeness).

**Track A (`cc_toy_lab/`, `scripts/`, `tests/`):**
- Entry point: `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md` verdict chain
- Core eigensolver: `cc_toy_lab/spectral/block_ipr_solver.py` (full read)
- Core metrics: `cc_toy_lab/spectral/metrics.py` (full read)
- `tests/test_block_ipr_solver.py`, `tests/test_ipr_metric.py`, `tests/test_random_matrix_controls.py` — executed live
- Silent-fallback grep across `cc_toy_lab/`, `scripts/`

**Track B (`tom_s3_spinor_toy/`):**
- Shared certified substrate: `experiments/20260812-c85-peter-weyl-representation-certification/c85_certification.py`
  — full read, plus an **independent from-scratch sympy re-derivation** of its central claim
  (Layer 6). Confirmed 22 files (`grep -rl "c85_certification"`) import it via `importlib.util`,
  spanning C86 (2026-08-12) through C111 (2026-08-30) — this is genuinely the highest-leverage
  single file in Track B.
- Spot-checked at full depth: C86, C87 (`decision.md`), C88 (docstring/provenance), plus grep
  sweep of `eigvalsh`/`eigvals`/`np.real`/`np.imag` usage across all `experiments/*/`.
- `tests/test_c85_certification.py` — executed live (12/12 pass)
- Docs-vs-code: `RESEARCH_STATUS_REPORT.md`, `docs/load_bearing_formulas.md` — read against
  `git log` and the actual experiment directory listing.

Not covered at depth (declared, not silently skipped): the remaining ~90 individual experiment
scripts; Track A's other gate scripts beyond the block solver (`run_gate4_batched.py`,
`aggregate_gate4b_results.py`, etc. — read only their names/role, not full logic).

---

## Layer-by-layer findings

### Layer 0 — Stop the Spread
No new claims extended, no Gate N+1 initiated during this audit. ✅

### Layer 1 — Active Pipeline Materiality
- **Track A:** `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md` is itself already a **null/negative**
  verdict (`DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC` — the harness distinguishes FFT vs
  lattice discretization, NOT S³×S¹ physics). `[DOCS]`. This materially lowers audit risk: the
  project is not currently resting a strong physics claim on Track A's numerics.
- **Track B:** no single entry point (100+ independent rounds). The correct Layer-1 object is
  the shared substrate `c85_certification.py`, confirmed by import-count to be load-bearing for
  22 of the most recent rounds (C86-C111). `[VERIFIED-grep]`

### Layer 2 — Silent Fallbacks
- Grep for `except.*pass|except.*continue` across `tom_s3_spinor_toy/experiments/202608*/*.py`
  (the C-series): **zero matches**. `[VERIFIED-grep]` — consistent with the project's documented
  discipline of asserting/raising rather than catching-and-continuing.
- Track A: one `np.nan_to_num(phase_scan.radius, nan=0.0)` in `cc_toy_lab/radion/dashboard.py:107`
  — confirmed to be inside a matplotlib `fill_between` plotting call, not the metrics/results
  pipeline. **Not material.** `[VERIFIED-read]`
- **Minor finding:** `experiments/20260811-c79-nonproduct-s3s6-coupling-attempt/c79_nonproduct_coupling.py`
  line 181-185 computes a per-eps Hermiticity residual inside the sweep loop and **prints** a
  `"!! Hermiticity check FAILED"` warning if it exceeds `1e-8` — but does not branch on it; line 182's
  `np.linalg.eigvalsh(d_joint)` call is unconditional regardless of the check's outcome. In this
  specific script the risk is low (the S3 factor is a scalar×identity by construction, so the
  joint operator should stay Hermitian by construction for all `eps`), but the pattern itself
  (detect-but-don't-gate) is the precursor to the actual bug found one day later in C87 (below).
  `[VERIFIED-read]`

### Layer 3 — Metrics & Normalization
- Track A: `inverse_participation_ratio()` in `cc_toy_lab/spectral/metrics.py` uses the standard
  `Σ|ψ|⁴/(Σ|ψ|²)²` definition and **raises** (does not silently return 0 or NaN) on a zero-norm
  vector. `mean_adjacent_gap_ratio()` correctly filters degenerate (near-zero) spacings before
  computing the min/max ratio. Both `[VERIFIED-read]`.
- Track B: no single shared metric layer (each round defines its own JSON output); not
  practical to audit uniformly at this scope.

### Layer 4 — Core Computation Stability (eigensolver regression — primary focus per task)

This is the **strongest finding of the audit**, and it is a positive one about process, with
one concrete, already-fixed historical bug and one still-open minor pattern.

1. **Track A, `block_ipr_solver.py` — clean.** The module's own docstring documents a *prior*
   regression precisely matching the project's known failure mode: `eigsh(which='SA', k=N//10)`
   was benchmarked and found to return **wrong IPR** (0.036 vs true 0.296) due to ARPACK
   non-convergence for a 10%-of-spectrum request, and was also 6× slower than dense `eigh`.
   The shipped solver uses dense `eigh` per-block (exact, not approximate), asserts the
   block-diagonal structure at runtime, and **raises** rather than silently returning a wrong
   answer if the assertion fails. `reports/BLOCK_SOLVER_VERIFICATION_v0.1.25.md` documents
   dense-vs-block equivalence to 1e-16. `[VERIFIED-read]` + `tests/test_block_ipr_solver.py`
   executed live: **31/31 passed** (including `test_ipr_metric.py`, `test_random_matrix_controls.py`).

2. **Track B — a real eigvalsh/eigvals regression, caught and fixed same-session (C87→C88).**
   `[VERIFIED-read, decision.md]`: C87's original script called `np.linalg.eigvalsh()` on
   `d_joint_base` at level k=2. `eigvalsh` silently reads only the Hermitian part of its input
   and does not error on non-Hermitian input. A direct check found the Hermiticity residual was
   **2.0** (not ~0) at k=2 — meaning C87's original "clean NULL" conclusion was reached via a
   computation that "could have produced ARBITRARY wrong eigenvalues, not merely imprecise
   ones" (their own wording). Root cause: Meier's `|p⟩` basis is not orthonormal, so the
   certified `l_{e3}` generator is genuinely non-anti-Hermitian for k≥2 (a structural feature,
   not a repair bug — confirmed independently below). The fix (`c86_full_k1_coupling.py`'s
   `_real_eigvals` helper, reused by C87 onward): detect non-Hermiticity via residual, fall back
   to the general `eigvals` solver, and **report the max imaginary part actually found** as an
   explicit diagnostic rather than silently discarding it. The corrected re-run reproduced the
   original (invalid) numbers exactly — the project's own decision.md explicitly flags this as
   "reassuring, but NOT knowable in advance," i.e. it does not retroactively excuse having
   trusted the original run.
   - **Propagation check:** `[VERIFIED-grep]` — every downstream round from C101 onward
     (C101, C102, C103, C106, C108, C109, C110, C111) defines/uses an `eigen_multiplicities_general`
     or equivalent helper that returns `(eigenvalues, max_imag)` and tracks `max_imag` explicitly
     in its output JSON, i.e. the fix was durably adopted as a house convention, not a one-off
     patch. C85 itself, and C86's own `build_full_level_d_s3`, still discard the imaginary part
     via bare `np.real()` without reporting `max_imag` in that specific function (though C86
     separately computes and reports `dbar_pr_hermiticity_residual` for the same matrix) —
     a residual, low-severity gap: no `assert`/gate on that residual before trusting the
     `np.real()` truncation. `[HYPOTHESIS — low severity]`: worth adding an explicit assert or
     max-imag report to `c85_certification.py`'s own `eigen_multiplicities()` for full
     consistency with the house convention it indirectly caused to be created.
   - No other `eigvalsh` call site found in the C-series (`grep -rn eigvalsh experiments/*/*.py`)
     shows evidence of the same un-gated risk **except** C79 (Layer 2 finding above), which is
     lower-risk by construction (scalar×identity S3 factor).

3. **Track A vs Track B, cross-track pattern match confirmed:** the task's stated concern
   ("documented history of exactly this failure mode") is independently verified **in both
   tracks**, via two textually distinct incidents (Track A: `eigsh` non-convergence; Track B:
   `eigvalsh` reading only the Hermitian part of a non-Hermitian matrix) — same root failure
   class (wrong-solver-for-input-structure), different manifestation, both caught before being
   published as a final claim, both now documented in-repo as a house lesson.

### Layer 5 — Data/Operator Invariants
- Track A block solver: runtime-asserted block-diagonal structure (raises `ValueError` on a
  single connected component or non-uniform block sizes) — `[VERIFIED-read]`.
- Track B C85: runtime `assert` on quaternion relations before proceeding (`i²=j²=k²=-1, ij=k`)
  and an explicit complex-linearity `assert` on the right-multiplication matrix construction —
  `[VERIFIED-read]`. Both are genuine invariant gates, not merely printed diagnostics.

### Layer 6 — Control / Baseline Validity (independent re-derivation)

**Re-derived C85's central claim from scratch** (own sympy script, different variable names,
not importing `c85_certification.py`): built `l_{e1,e2,e3}` for both the "literal" (as printed
in Meier's PDF) and "repaired" (p−k) coefficient variants, k=0..5, and checked the sp(1) bracket
relations `[l_i, l_j] = 2·l_k` (cyclic) directly.

```
k=0: literal_brackets_ok=True   repaired_brackets_ok=True
k=1: literal_brackets_ok=True   repaired_brackets_ok=True
k=2: literal_brackets_ok=False  repaired_brackets_ok=True
k=3: literal_brackets_ok=False  repaired_brackets_ok=True
k=4: literal_brackets_ok=False  repaired_brackets_ok=True
k=5: literal_brackets_ok=False  repaired_brackets_ok=True
```

This **exactly reproduces** the project's own claimed pattern ("literal passes k=0,1, fails
k≥2; repaired passes all tested k"). `[VERIFIED-REAL, independent sympy]` — this is the
strongest possible confirmation available short of a different reviewer/model: genuinely
independent code, same conclusion.

`tests/test_c85_certification.py` also executed live: **12/12 passed**. `[VERIFIED-pytest]`

Per this stack's own Independent Verification Strength Ladder, this re-derivation counts as
"independently-written code" (Strong), not "same model, new prompt" (Weak) — the check used a
fresh implementation, not a re-run of their function.

### Layer 7 — Data Provenance
Not deeply audited at this scope (no file-date/results-mixing check performed across the 100+
`results_c*.json` files). Declared gap, not silently skipped.

### Layer 8 — Statistical Interpretation
Track A's Gate 4B verdict is already the project's own negative/null finding
(`DISCRETIZATION_SENSITIVE`), so there is no "impressive metric" here needing extra scrutiny for
overclaiming. Track B's C85-C111 chain uses exact symbolic algebra (sympy Rationals/exact
brackets) for the load-bearing identities, not a statistical threshold — the main risk category
(p-value/threshold gaming) largely does not apply to this substrate.

### Layer 9 — Documentation/Code Mismatch

**Concrete, verified finding.** `[VERIFIED-git log + directory listing]`

- `tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md` (the project's own designated Track B entry
  point per root `CLAUDE.md`) was last content-modified **2026-08-26** (commit
  `docs(tom_s3_spinor_toy): fix stale status pointers (boyko-project-radar Chain 3)`). Its most
  recent "Status correction" box is dated **2026-08-12** and covers only through round C102.
- The experiment directory listing shows five more rounds landed after that correction box was
  written and even after the file's own last edit: **C106 (2026-08-13), C107 (2026-08-29), C108
  ("summed mixing operator breaks reality"), C109 (k=1 anomaly diagnosis), C110 (covariance
  hypothesis refuted), C111 (exceptional point confirmed)** — all through 2026-08-30, i.e. today.
  None of these five/six rounds, including two with names suggesting substantive negative/refuting
  results (C108, C110), are mentioned anywhere in `RESEARCH_STATUS_REPORT.md`.
- This is a known, self-diagnosed pattern in the project's own words (the 2026-08-12 correction
  box explicitly flags: *"each correction box itself goes stale... a `boyko-project-radar` scan
  recommended wiring an automated staleness check"*) — the mechanism was apparently never built,
  or was built and has already fallen behind again by 4 days / 5 rounds. A reader relying solely
  on the designated entry point would not learn about C108-C111 at all.
- `docs/load_bearing_formulas.md` is separately dated 2026-07-11 (last modified 2026-07-14) and
  **honestly self-scopes** as non-exhaustive ("Remaining known gaps... Do not treat this as
  exhaustive coverage"). However, its scope list of gaps (G76, G82-G93, Dolan-Casimir rounds
  24-46) predates the entire C-series naming scheme — the file does not merely have gaps *within*
  its own G-gate framework, it is silent on the C-series' existence altogether, including the
  now heavily-reused `c85_certification.py` substrate this audit identified as the single
  highest-leverage file in Track B. Not an overclaim (the file doesn't claim completeness), but
  a materially larger blind spot than its own gap list suggests.

**Recommendation (not executed — out of scope for an audit):** the staleness problem is
structural (correction-box chain requires a human/agent to remember to append a new box each
session) rather than a one-off oversight; a real fix would be closer to the "automated staleness
check" the project's own 2026-08-12 box already asked for and evidently did not get, e.g. a
pre-commit or session-end hook comparing the newest `experiments/*/decision.md` mtime against
`RESEARCH_STATUS_REPORT.md`'s last correction-box date.

### Layer 10 — Reproducibility
- `python -m pytest tests/test_block_ipr_solver.py tests/test_ipr_metric.py
  tests/test_random_matrix_controls.py -q` → **31 passed** (Track A). `[VERIFIED-pytest]`
- `python -m pytest tom_s3_spinor_toy/tests/test_c85_certification.py -q` → **12 passed**
  (Track B substrate). `[VERIFIED-pytest]`
- `python -m pytest tom_s3_spinor_toy/tests/ -q --collect-only` → **2528 tests collected**,
  roughly consistent with (and slightly grown from) `RESEARCH_STATUS_REPORT.md`'s own stated
  2516-2517 count as of 2026-07-15 — no red flag of mass test deletion or count drift.
  `[VERIFIED-pytest]`
- Full suite execution (2528 Track B tests + full Track A suite) was **not** run in this
  session — collection-only + targeted execution, given time budget. Declared gap.

---

## Overall Verdict

| Track | Verdict | Rationale |
|---|---|---|
| **Track A** (`cc_toy_lab/`, `scripts/`, `tests/`) | **HARDENED** (for the scope audited) | Core eigensolver (`block_ipr_solver.py`) has a documented, fixed prior regression (`eigsh` non-convergence), current code uses exact block-diagonalized `eigh` with runtime-asserted invariants, machine-precision equivalence report on file, live tests pass (31/31). The project's own headline verdict for this track is already a null/negative result (`DISCRETIZATION_SENSITIVE`), which removes most overclaiming risk. One cosmetic-only `nan_to_num` in a plotting function, not material. |
| **Track B** (`tom_s3_spinor_toy/`) — shared substrate | **HARDENED** (for `c85_certification.py` and its direct fix chain) | Central claim independently re-derived from scratch this session and confirmed exactly. A real `eigvalsh`-on-non-Hermitian-matrix regression (C87) was caught same-session, transparently documented (not smoothed over), fixed, and the fix propagated as a durable house convention through 8+ subsequent rounds. No `except:pass` silent-continue pattern found in the C-series. One minor un-gated Hermiticity-check-but-continue pattern found in an *earlier* (pre-fix) script (C79); one minor un-asserted residual in C85 itself. |
| **Track B** — documentation layer | **PROVISIONAL** | `RESEARCH_STATUS_REPORT.md`'s correction-box chain is 4 days / 5 rounds stale as of this audit, missing two named-as-refuting rounds (C108, C110) entirely — a real, verified gap, not hypothetical, in the project's own designated entry point. `load_bearing_formulas.md` is honestly self-scoped as partial but its blind spot (the entire C-series) is larger than its own stated gap list. This does not affect trust in the *code*, only in a reader's ability to get an accurate current-status picture from the two files this audit was specifically asked to check. |

**Most concerning finding overall:** not a code bug (both eigensolver regressions found in this
audit were already self-caught and fixed before this session started) — it is the **Layer 9
documentation staleness gap**: `RESEARCH_STATUS_REPORT.md`, the project's own designated entry
point, is silent on five rounds including two (C108 "breaks reality", C110 "covariance
hypothesis refuted") whose names suggest they may be materially relevant to current status, and
the project's own prior request for an automated staleness check appears unfulfilled.

## Rerun Policy Applied

No rerun triggered. No newly-found bug is in the active pipeline undetected — the two
eigensolver issues surfaced by this audit (Track A `eigsh`, Track B `eigvalsh`/C87) were both
already found, fixed, and documented by the project itself prior to this audit; this audit's
role was to *verify* those fixes are real, complete, and durable, which they were found to be
(Layers 4, 6, 10 above). Layer 9's documentation gap requires a docs update, not a code rerun.

## "Антистыдный" checklist

- [x] External audit request received and executed (this document)
- [x] Not ignored — full 10-layer pass attempted with declared scope limits
- [x] Materiality audit performed (Layer 1: identified `c85_certification.py` as the
      highest-leverage single file via import-count grep, not guessed)
- [x] Active-pipeline issues separated from legacy/historical ones (C87's bug is historical
      and fixed; documented as such, not re-reported as a live issue)
- [x] Independent re-derivation performed (Layer 6), not just narrative trust
- [x] Regression tests confirmed present and passing (31 + 12 + 2528-collected)
- [ ] Full 2528-test Track B suite execution — not run this session (declared gap)
- [x] Findings documented in this report with evidence markers
