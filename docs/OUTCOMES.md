# GeoSpectra Lab — Outcome Map

**Purpose:** retrospective Outcome Cards for the 15 most load-bearing artefacts in this project, so a new reader (or future-Sergey) can answer in 10 minutes: *what does each artefact try to achieve, what is its current blocker, and how would we know it succeeded?*

**Methodology:** Thomas Gordon's Win-Win / No-Lose Method applied to code. Each card has 5 fields — desired outcome, current blocker, smallest useful next step, win-win constraint, success check.

**Scope of this map:** 15 artefacts out of ~200 in the project. The other 185 are intentionally not mapped — either they are derivative (run artefacts, paper drafts, audit follow-ups), or their outcome is fully captured by one of the 15 below.

**What this map is NOT:**
- Not a scientific verdict on any artefact
- Not a claim that listed outcomes have been achieved (status field is honest)
- Not a replacement for `docs/CLAIMS_AND_CAVEATS.md`, `reports/NULL_RESULTS.md`, or pre-registrations — those remain authoritative for what may/may not be communicated externally

**Date written:** 2026-05-27
**Project state at writing:** Gate 4B v0.1.21 interpretation frozen (S³ Dirac operator bug discovered and fixed in `093573b`); v0.1.24 corrected rerun attempted on Hetzner CPX42 and killed by OOM on 2026-05-25; no scientific verdict on v0.1.24.

---

## Section A — Scientific Core (operators and metrics)

### A1. `cc_toy_lab/spectral/dirac_s3.py` — S³ Dirac operator

**Desired outcome:** A finite-mode S³ Dirac operator whose spectrum matches the canonical form `λ = ±(k + 3/2) / R` from arXiv:1103.4097 §6, with correct dimension and Hermiticity, usable as the S³ factor inside the S³×S¹ product operator (Gate 4B).

**Current blocker:** Achieved — corrected version at commit `093573b` includes the negative `k=0` branch (`λ = −3/2`) that was missing in v0.1.21. Targeted unit tests in `tests/cc_toy_lab/spectral/test_dirac_s3_branches.py` pass 6/6.

**Smallest useful next step:** Use this operator in v0.1.24 rerun (blocked on hardware — see A2 / runner artefact).

**Win-win constraint:** Hermiticity must hold; eigenvalue formula must trace to arXiv source page-and-equation; dimension formula `total_dim = k0_neg_degeneracy + sum(dimensions)` must be exposed and testable, not hidden inside the operator builder.

**Success check:** `pytest tests/cc_toy_lab/spectral/test_dirac_s3_branches.py -v` → 6 passed. Eigenvalue list at `j_max=2` contains `[-4.5, -3.5, -2.5, -1.5, +1.5, +2.5, +3.5]` (unique values, with documented degeneracies). Dimension at `j_max ∈ {0,1,2}` equals `{10, 28, 60}`.

---

### A2. `cc_toy_lab/spectral/s3_s1_product_discretized.py` — Gate 4B product operator

**Desired outcome:** A discretized S³×S¹ Hamiltonian `H = kron(D_S³², I_S¹) + kron(I_S³, P_S¹)` parameterized by `(j_max, s1_size, alpha, mode, disorder_strength, seed, radius, s1_family)`, used as the unit of computation in the Gate 4B finite-size scaling grid.

**Current blocker:** Operator itself is constructed and runs correctly on small cases. End-to-end use of the corrected operator (after S³ fix `093573b`) at the heaviest grid point (`N=128, j_max=3`) is blocked by memory ceiling — peak RSS ≈ 10.5 GiB inside `scipy.linalg.eigh`, which exceeded available RAM on the 15 GiB Hetzner CPX42 host (incident 2026-05-25).

**Smallest useful next step:** Heavy smoke case in isolation on a ≥64 GiB host — N=128, j_max=3, seed=123, `spectral_circle` — to measure real peak RSS on the corrected operator before the full 216-case rerun. Detailed plan in `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`.

**Win-win constraint:** Operator parameters and the assembly formula must not change (the operator is what is being measured; mutating it invalidates the pre-registered protocol locked at commit `1f4173c`). No silent switch to sparse / k-top solvers — that is a separate, formally pre-registered alternative method.

**Success check:** A single heavy smoke case completes without OOM, writes a non-empty `metrics.json` with finite `true_ipr_mean`, and produces a peak RSS reading ≤ 50% of host RAM with documented thread settings.

---

### A3. `cc_toy_lab/spectral/dirac_monopole_s2.py` — S² monopole positive control

**Desired outcome:** Finite-mode S² Dirac monopole operator that reproduces the analytic index identity `index(D) = q` for monopole charge `q ∈ {-3, …, +3}`, serving as the project's *positive control* — the only artefact that gives a non-zero topological index in this codebase and demonstrates that the index-counting pipeline can detect a real topological signal when one exists.

**Current blocker:** None for its scoped purpose — full and quick scripts confirmed `index = n_plus − n_minus = q` for the documented charge set (`reports/CHIRALITY_INDEX_REPORT.md`, run `20260511-230305_dirac_monopole_s2_full`).

**Smallest useful next step:** Keep frozen as the positive-control reference. Any new chirality-related diagnostic in the project must cite this artefact as its calibration baseline.

**Win-win constraint:** Must remain a *finite-mode toy control*, not be reinterpreted as evidence for protected physical chiral fermions. The convention "q > 0 → positive-chirality zero modes" must remain explicit in the operator's docstring and report.

**Success check:** `python scripts/dirac_monopole_s2.py --full` produces the documented index table (rows for q = −3..+3 at cutoff 5) with `passed = yes` for every row.

---

### A4. `cc_toy_lab/spectral/metrics.py` — true IPR and r-statistic

**Desired outcome:** Reproducible implementations of (a) inverse participation ratio `IPR = Σ|ψᵢ|⁴ / (Σ|ψᵢ|²)²` operating on eigenvectors (1-D or 2-D matrix of columns) and (b) mean adjacent gap ratio `⟨r⟩` for level-spacing statistics, both with explicit zero-vector guards and documented sensitivity to unfolding.

**Current blocker:** Achieved. The current IPR is the *true* eigenvector-based form. The v0.1.20 metric (eigenvalue-mean stand-in) was identified as wrong, corrected in v0.1.21, and the correction is the reason the Gate 4B interpretation was rerun under the locked metric tag `v0.1.21_true_ipr_corrected_s3_dirac` (now extended to `v0.1.24_true_ipr_corrected_s3_dirac` for the corrected operator).

**Smallest useful next step:** Keep the metric pinned. Any change to either function must be accompanied by a metric version bump (currently tracked via `--ipr-metric-version` flag in the runner) and a pre-registration update.

**Win-win constraint:** Zero-vector and norm-below-tolerance cases must raise, not silently return NaN — a silent NaN in a downstream IPR aggregate is the failure mode that produced the v0.1.20 incident in the first place.

**Success check:** `pytest tests/test_spectral_metrics.py tests/test_ipr_metric.py -v` passes. Synthetic delocalized vector (uniform amplitude N=100) returns IPR ≈ 1/N within 1e-12; synthetic localized vector (single-site) returns IPR = 1.

---

## Section B — Validation Harness (the falsification machinery)

### B1. `cc_toy_lab/controls/negative_controls.py` — v0.1.22 specificity test

**Desired outcome:** Three controls (random Hermitian, scrambled geometry, broken Wilson term) which, when run through the Gate 4B pipeline, should *fail* to reproduce the v0.1.21 PASS pattern — thereby demonstrating that the harness can distinguish a geometry-coupled localization signal from generic random / artefact-driven contrast.

**Current blocker:** Two batches (random Hermitian, W=0 and W=20) completed locally — 18 of 54 cases. Remaining four batches (scrambled geometry × 2, broken Wilson × 2) paused: first blocked by local thermal limits, then by v0.1.24 operator fix (which restarts the upstream Gate 4B itself).

**Smallest useful next step:** Resume the remaining 36 cases on a memory-safe host *after* the corrected v0.1.24 Gate 4B rerun produces a verdict. Running controls before then would compare against a frozen-interpretation upstream.

**Win-win constraint:** Controls must remain falsification controls, not validation operators. A passing control = harness lacks specificity = problem. No silent reclassification of a passing control as "interesting positive result".

**Success check:** All three control families return aggregate contrast `< 2.0×` and/or weak/collapsing FSS trend across the full 54-case grid. The decision rules from the pre-registration document determine the verdict, not post-hoc interpretation.

---

### B2. `cc_toy_lab/spectral/random_matrix_controls.py` — synthetic r-statistic controls

**Desired outcome:** Validate the `mean_adjacent_gap_ratio` implementation independently of any Anderson / Dirac operator, by computing it on synthetic Poisson, GOE, and GUE level sequences with known analytic targets (0.3863 / 0.5307 / 0.5996).

**Current blocker:** Achieved. Full mode passes all three controls within tolerance (Poisson 0.3817 ± 0.0350, GOE 0.5309 ± 0.0400, GUE 0.5960 ± 0.0450) per the latest snapshot in `reports/SPECTRAL_REPORT.md`.

**Smallest useful next step:** None — this control is a regression backstop. Re-run only if the metric code in A4 changes.

**Win-win constraint:** Synthetic-control success must NOT be promoted into a claim about Anderson physics or about geometric localization. It validates the *statistic implementation* only.

**Success check:** `python scripts/r_stat_controls.py --full` reports all three ensembles with `passed = yes` and measured `⟨r⟩` within documented tolerance of the analytic target.

---

### B3. `cc_toy_lab/spectral/s1_discretizations.py` — S¹ family comparison

**Desired outcome:** Three independent S¹ discretization families (`spectral_circle`, `ring`, `wilson_ring`) so that any S²/S³ × S¹ result can be tested for *discretization sensitivity* — a positive signal that depends on which S¹ family was used is a discretization artefact, not a geometric signal.

**Current blocker:** Achieved as infrastructure. Known limitation documented: `ring` family at `alpha=0` on small lattices (`s1_size < 64`) shows kernel-only gate failures, which targeted follow-up (run `20260516-165729`) classified as a `SMALL_LATTICE_ARTIFACT` (failure rate drops from 6.6% at small sizes to 0.0% at `s1_size ≥ 64`).

**Smallest useful next step:** Use all three families in the v0.1.24 rerun. The cross-family consistency check is what keeps a future positive result from being a single-family artefact.

**Win-win constraint:** No family may be silently removed from the grid to "clean up" results. If `ring` produces sensitivity at small sizes, that is data, not noise — document and keep.

**Success check:** v0.1.21 already showed 3/3 family consistency at the locked grid sizes; the same check applied to v0.1.24 corrected operator after rerun is the natural next data point.

---

### B4. `scripts/run_gate4_batched.py` — batched FSS runner

**Desired outcome:** A single runner that executes the 216-case Gate 4B grid in 9 batches, with output-namespace isolation (so v0.1.21 and v0.1.24 runs cannot collide), explicit guardrails against grid/threshold changes, and parameterized `--output-base`, `--protocol-version`, `--ipr-metric-version` flags.

**Current blocker:** Two open requirements before the next full rerun:
1. *Per-case checkpointing* — currently persistence happens only at batch completion. The 2026-05-25 OOM lost 21 successful in-memory cases because batch 1 never closed.
2. *Resume behaviour* — runner must skip already-completed per-case artefacts on `--resume`, with atomic temp-rename writes.

**Smallest useful next step:** Implement per-case checkpointing (separate task, separate doc) before any rerun. No code change to operator or metric — only persistence boundary moves from batch-level to case-level.

**Win-win constraint:** Adding checkpointing must not change the numerical pipeline. The `eigh` call, metric computation, seed handling, and output content of each case must be byte-identical to a non-checkpointed run.

**Success check:** A simulated SIGKILL after case N completes leaves on disk N valid per-case artefacts; `--resume` on the same output namespace runs cases N+1..216 only. No double-counted or overwritten artefacts.

---

## Section C — Other science paths (separate from the S³×S¹ main thread)

### C1. `cc_toy_lab/radion/potentials.py` — toy radion stabilization

**Desired outcome:** A reproducible toy model in which four explicit potentials (`A: a/R²`, `B: a/R² + bR²`, `C: B + c/R⁴`, `D: B + toy-regularized KK tower`) have well-defined minima, with the B-potential minimum analytically matching `R₀_B = (a/b)^(1/4) ≈ 1.189207` and numerical computation matching it to ≤ 1e-6 relative error.

**Current blocker:** Achieved. Latest verified run reports `R₀_B = 1.189207`, MFG relative error `6.7e-4`, multitrajectory error `5.7e-5` (per `reports/RADION_REPORT.md`).

**Smallest useful next step:** Keep frozen as the radion baseline. The radion track is parallel to the main S³×S¹ FSS thread; the next radion-related decision (whether to expand the phase scan or freeze entirely) waits on the Gate 4B v0.1.24 outcome.

**Win-win constraint:** The phase-transition threshold `α_c = 1.345` is a *toy reproducibility target*, not a derived physical critical point. Any future tightening of that number must update `reports/ISSUES_SCIENTIFIC.md` to keep the toy framing explicit.

**Success check:** `python scripts/radion_stabilization.py` produces the dashboard PNG, prints `R₀_B ≈ 1.189207`, and the asserted checks in the script pass (minimum near `R₀_B`, positive curvature at the minimum, five stable trajectories converging, MFG self-consistency, alpha-threshold smoke).

---

### C2. `cc_toy_lab/geometry/analytic_spectra.py` — analytic ground truth

**Desired outcome:** Closed-form analytic spectra for the Laplace-Beltrami operator on `S²`, `S³`, `S⁶` (and product spaces via Minkowski sums), with degeneracies, scalar curvature, and radius scaling — usable as the ground truth against which any graph-Laplacian or finite-lattice approximation in the project is compared.

**Current blocker:** Achieved. Hardcoded reference eigenvalues for `ℓ = 0..4` on `S²/S³/S⁶`, plus radius scaling and product checks, are tested in `tests/test_analytic_spectra.py` with explicit *anti-circular-validation* comments (the test does not re-derive from the same helpers under test).

**Smallest useful next step:** None — this is a foundational module. New geometries added in the future must follow the same anti-circular pattern (hardcoded reference values, not re-derived).

**Win-win constraint:** Reproducing an analytic spectrum is NOT validation of physical compactification on that geometry. The module's docstring and `docs/CLAIMS_AND_CAVEATS.md` must keep this distinction explicit.

**Success check:** `pytest tests/test_analytic_spectra.py -v` passes — all hardcoded references match, radius scaling `λ ∝ 1/R²` holds, product spectra equal `λ(M₁) + λ(M₂)`, scalar curvature equals `n(n−1)/R²`.

---

## Section D — Critical tests

### D1. `tests/cc_toy_lab/spectral/test_dirac_s3_branches.py` — k=0 branch test

**Desired outcome:** A regression backstop that detects if the S³ Dirac operator ever loses the negative `k=0` branch again. Tests assert: (a) `λ = −3/2` appears in the spectrum at every `j_max ≥ 0`; (b) dimension at `j_max ∈ {0,1,2}` is `{10, 28, 60}`; (c) operator is Hermitian; (d) eigenvalues are real; (e) radius scaling `λ(R=2) = λ(R=1)/2` holds.

**Current blocker:** Achieved. 6/6 PASS at commit `093573b`. Tests are the formal contract between the source verification document (`reports/S3_DIRAC_SOURCE_VERIFICATION_v0.1.23.md`) and the runtime operator.

**Smallest useful next step:** Keep these tests in every CI run. If they ever fail, no further v0.1.24+ work proceeds until they pass again.

**Win-win constraint:** These tests must not be weakened to make a future operator change "pass cheaply". If a code change makes any of the six checks fail, the change is wrong, not the tests.

**Success check:** `pytest tests/cc_toy_lab/spectral/test_dirac_s3_branches.py -v` → 6 passed in the local working tree at the current operator commit.

---

## Section E — Critical reports and methodology

### E1. `reports/S3_S1_GATE4B_FSS_RESULTS_v0.1.21.md` — Gate 4B frozen verdict

**Desired outcome:** A complete record of what the v0.1.21 finite-size scaling campaign produced, with raw metrics, per-cell results, family contrasts, FSS trend, and the formal verdict — **frozen** so that any future communication about Gate 4B can cite a specific commit-tagged document rather than a moving interpretation.

**Current blocker:** Interpretation frozen after the S³ Dirac branch-indexing issue was discovered. The document remains the authoritative record of *what the run produced under the v0.1.21 operator*; it cannot be cited as "canonical S³ Dirac validation" until the v0.1.24 rerun produces a comparable result on the corrected operator.

**Smallest useful next step:** Do not edit this document to "soften" the verdict. Add a freeze banner at the top if not yet present, pointing to the incident report and the rerun plan. The comparison document `reports/GATE_4B_v0.1.24_COMPARISON_v0.1.21_vs_v0.1.24.md` will be written *after* the rerun, not by editing this one.

**Win-win constraint:** Raw computational outputs (216-case run artefacts) must not be deleted or overwritten. v0.1.24 outputs go to a separate namespace by design (commit `4b77684`).

**Success check:** `grep -i "frozen\|interpretation" reports/S3_S1_GATE4B_FSS_RESULTS_v0.1.21.md` returns a clearly visible status header. The document is referenced by `docs/CLAIMS_AND_CAVEATS.md` and `docs/ROADMAP.md` as the v0.1.21 record.

---

### E2. `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md` — failed rerun record

**Desired outcome:** A reproducible record of why the v0.1.24 rerun did not complete, with kernel-level evidence (journalctl OOM trace), root-cause analysis (`scipy.linalg.eigh` peak memory on the heaviest case), and an explicit non-scientific status disclaimer.

**Current blocker:** Achieved (this session). Document is complete: raw evidence, root cause, impact, lessons learned, options considered, recommendation, forbidden actions. Untracked, not yet committed (per user instruction).

**Smallest useful next step:** Commit this document when the user is ready, paired with `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`. No interpretation work follows from this incident — only infrastructure changes do.

**Win-win constraint:** The incident must not be cited as a scientific result. "OOM on heavy case" ≠ "signal weakened". The document's section 6 ("Non-Scientific Status") is the load-bearing disclaimer.

**Success check:** `grep -iE "validated|proven|verdict" reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md` returns only no-verdict contexts (e.g. "no scientific verdict can be made"). No positive scientific claim language.

---

### E3. `docs/CLAIMS_AND_CAVEATS.md` — claim boundary document

**Desired outcome:** A standing document that lists, side by side, what the project may publicly claim (`✅ What Can Claim`) and what it must never publicly claim (`❌ Cannot Claim`), with mandatory caveats attached to each allowed claim and a 7-point checklist before any external communication.

**Current blocker:** Achieved as infrastructure (last updated 2026-05-24). The Gate 4B section currently refers to the v0.1.21 result with all caveats; this section will need an update once v0.1.24 produces a verdict (preserved or weakened or disappeared).

**Smallest useful next step:** Treat this document as the single source of truth before any LinkedIn post, CAMP message, paper draft, or grant text. Update it *first*, then communicate — never the reverse.

**Win-win constraint:** The "Cannot Claim" list is monotonically growing in strictness, not shrinking. Removing an entry from `Cannot Claim` requires evidence that the corresponding claim has become provable — never editorial choice.

**Success check:** Every external communication artefact (`reports/TOM_MESSAGE_*`, `reports/LINKEDIN_*`, paper drafts) cites this document. `grep -l "CLAIMS_AND_CAVEATS" reports/` returns the expected set.

---

### E4. `docs/RESEARCH_CONTEXT.md` — independence + attribution statement

**Desired outcome:** A standing document that makes three things unambiguous to any external reader: (a) GeoSpectra Lab was independently developed by Sergey Boyko; (b) the inspiration from Tom Lawrence's public work is attributed but does not imply affiliation, endorsement, or review by him; (c) the project's narrow computational question is distinct from Tom Lawrence's conceptual programme on covariant compactification.

**Current blocker:** Achieved as infrastructure. Document lists Tom Lawrence's peer-reviewed papers (arXiv:2203.09473, 2211.07586, preprints 202303.0314, 202510.2222), his ORCID `0000-0002-2741-8226`, and the explicit Independence Statement.

**Smallest useful next step:** Update if Tom Lawrence (or anyone else) ever formally collaborates, reviews, or co-authors anything in the project — the document is currently structured to support transition from "independent + inspired" to a documented collaboration without ambiguity. Until then: do not edit.

**Win-win constraint:** No social-proof inflation. Even after a successful CAMP meeting (2026-05-26) or a Buckholtz contact, the Independence Statement must remain unless a formal collaboration agreement is recorded.

**Success check:** Every README mention of Tom Lawrence's name links back to this document. The `## Acknowledgements` section in `README.md` matches the wording in this document.

---

## Meta — How to extend this map

When a new artefact reaches the load-bearing threshold (i.e. removing it would invalidate a downstream result, or a new reader cannot reconstruct the project without it), add an Outcome Card here in the same format.

Threshold for inclusion:
- Code module: ≥ 1 test depends on it AND it produces a metric used in a Gate decision
- Report: cited as the basis for a forbidden / allowed claim in `docs/CLAIMS_AND_CAVEATS.md`
- Test: regression backstop for a previously-fixed bug OR contract for an external source
- Methodology doc: changes the rules of what can be communicated externally

Threshold for removal:
- Artefact is deleted from the codebase (rare — most are frozen, not deleted)
- Outcome is fully absorbed by another artefact's Outcome Card

Do not add Outcome Cards for:
- Run artefacts (`reports/RUNS/<timestamp>_*`)
- Draft paper sections (`PAPER_DRAFT_SECTION_*`)
- Audit follow-ups (`*_AUDIT_*`, `*_FOLLOWUP_*`) — these are derived from the artefacts already mapped above

---

**Last updated:** 2026-05-27
**Total cards:** 15
**Convention:** Thomas Gordon Win-Win Method (Outcome Card 5-field format)
