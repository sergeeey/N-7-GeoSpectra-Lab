# Track A — Numerical Analyst Audit (2026-07-17)

**Scope:** a focused numerical-analyst-lens pass on `cc_toy_lab/` (Track A), NOT
a full re-run of the multi-round Project 360° design used for Track B. Track A
already carries an unusually mature self-audit trail (`reports/NULL_RESULTS.md`,
`reports/ISSUES_SCIENTIFIC.md`, `docs/CLAIMS_AND_CAVEATS.md`, the 5-level
specificity cascade in `README.md`) that has already exhaustively covered
window-selection sensitivity, boundary-condition sensitivity, finite-size
scaling (s1_size 8→128, lattice L 4→7), and seed-count sensitivity across
dozens of documented `RUNS/`. Re-deriving any of that would duplicate real
work for no new signal.

**What this pass targeted instead:** the one item the project's own
`ISSUES_SCIENTIFIC.md` named as needed but never confirmed as done —
*"dense/sparse eigensolver consistency"* (named explicitly at line ~30-31,
dated May 2026, never followed up anywhere in the subsequent record). This is
exactly the numerical-analyst lens's distinctive angle (conditioning, solver
choice, basis dependence) that the project's own extensive physics/statistics
red-teaming doesn't cover.

**Method:** read the actual solver code (not reports), then directly
tool-verified dense-vs-sparse consistency by running both paths on identical
Hamiltonians at the project's own parameters.

---

## Finding 1 — CONFIRMED: real dense/sparse window inconsistency in `anderson.py` (1D toy module)

`cc_toy_lab/spectral/anderson.py:_central_eigensystem` switches at `size <= 192`:
dense (`np.linalg.eigh`, full spectrum, then windows by **energy fraction**) vs
sparse (`eigsh(sigma=0, which="LM")`, computes only `k = min(max(48, size//4),
size-2)` eigenvalues, **then** applies the same energy-fraction window to that
already-truncated set).

**[VERIFIED-tool]** Built identical Hamiltonians (same size/disorder/seed) and
ran both paths directly. Result across sizes 150–300, W∈{4,20}, 3 seeds each:
the number of eigenvalues actually captured in the "central window" differs by
**2–4×** between dense and sparse (e.g. size=200, W=4, seed=2: dense window
has 76 eigenvalues, sparse has 18) — because the sparse path can never put more
than `k` eigenvalues in the window, while dense draws from the full spectrum.
Resulting r-statistic and IPR values differ beyond plausible realization noise
in the majority of tested cases (e.g. size=300, W=20, seed=3: IPR 0.663 dense
vs 0.724 sparse — an ~9% relative difference on a single realization, not
averaged over the seed count the project normally uses).

**Impact scope:** `anderson.py` is imported by `scripts/spectral_localization.py`
and `tests/test_anderson_benchmark.py` — a 1D diagnostic module, not the
flagship claim (see Finding 3).

## Finding 2 — MILDER, WORTH TRACKING: `anderson_3d.py`'s dense/sparse eigenvalue-set selection differs modestly at the project's own L=7 "final-size" parameters

`anderson_3d.py:central_eigensystem` is architecturally different from the 1D
module — it selects a **fixed count** (`eigen_count`, default 48) of
eigenvalues on both paths (dense: 48 nearest the spectrum's *index* center;
sparse: 48 nearest *value* 0 via shift-invert), not an energy-fraction window.
This avoids Finding 1's severe truncation-before-windowing pattern.

**[VERIFIED-tool]** Directly tested at L=7 (343 sites — above the module's
`size<=260` dense/sparse threshold, and the project's own documented
"final-size" lattice for its key 3D Anderson result, see `reports/NULL_RESULTS.md`
"Follow-up after the configured full 3D Anderson benchmark"). Across W∈{4,24},
5 seeds each: the two paths select overlapping but **not identical** eigenvalue
sets (30–46 of 48 shared, i.e. 62–96% overlap — index-centered and
value-nearest-zero selection are the same only when the spectrum is exactly
symmetric, which disorder breaks). Resulting r/IPR differences are mostly
within the realization-to-realization noise already visible in the project's
own documented per-seed variance, though a few individual cases exceed it
(e.g. W=24 seed=4: r 0.376 dense vs 0.354 sparse, IPR 0.319 vs 0.299).

**This is not a smoking-gun bug** the way Finding 1 is — it does not by itself
overturn the L=7 result, which was itself always described as one point in a
finite-size-scaling trend, not a standalone claim. It does mean the specific
"dense/sparse eigensolver consistency" check `ISSUES_SCIENTIFIC.md` called for
has still never been done systematically (multiple seeds, both boundary
conditions, both disorder regimes, averaged) — only spot-checked here.

## Finding 3 — CONFIRMED CLEAN: the flagship Gate 4B benchmark (7.07× headline claim) is not exposed to this issue at all

**[VERIFIED-tool via Read]** `scripts/benchmark_gate4b_true_ipr.py` — the
actual script behind the README's headline 7.07× IPR contrast and the 5-level
specificity cascade — uses `np.linalg.eigh(H)` **unconditionally**, full dense
diagonalization, no sparse branch, no truncated-k, no windowing-after-truncation
pattern anywhere. This is computationally expensive at the largest case (matches
the project's own documented OOM incident, `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`)
but numerically the safest possible choice — full spectrum, no truncation bias.
**The headline claim is unaffected by Findings 1 and 2.**

---

## Recommendation

1. Close the long-standing `ISSUES_SCIENTIFIC.md` item honestly: it currently
   reads as an open, unaddressed call from May 2026. Recommend updating it to
   record Findings 1–2 above (partially checked, one real issue found, one
   milder one flagged) rather than leaving it as a silent gap indefinitely.
2. Finding 1 (`anderson.py`) is a genuine numerical bug in the 1D toy module's
   window-then-truncate ordering — the fix is mechanical (compute the energy
   window's bounds from a coarse estimate first, or request enough sparse
   eigenvalues to guarantee the window is fully populated, then confirm
   equivalence). Low priority given this module isn't behind any currently-cited
   headline claim, but worth fixing before this module is reused for anything
   claim-bearing.
3. Finding 2 (`anderson_3d.py`) does not require an urgent fix, but the
   systematic multi-seed dense-vs-sparse check `ISSUES_SCIENTIFIC.md` asked for
   should actually be run before the L=7 "final-size" point is cited again as
   the strongest evidence in any future write-up — right now it rests on a
   solver choice that this audit found is not perfectly reproducible across
   methods, only spot-checked as "probably fine."

## What this pass did NOT do (explicit, not a silent scope cut)

- Did not re-run or re-verify any of the extensive existing window-selection /
  boundary-condition / finite-size-scaling diagnostics already documented in
  `NULL_RESULTS.md` / `ISSUES_SCIENTIFIC.md` — those are real, tool-verified
  work already, re-checking them would be redundant.
- Did not audit `cc_toy_lab/`'s other numerical-analyst-relevant angles in
  depth (basis dependence beyond what's already covered by the ring/spectral_circle/
  wilson_ring family comparison; floating-point summation order effects;
  random-number-generator quality/seed-collision risk across the ~200k+ realizations
  run over the project's history). These remain open if a deeper pass is wanted.
- Did not check Track A's own test suite (`tests/`) for whether it independently
  covers the dense/sparse consistency question — worth a quick look before
  treating Findings 1-2 as entirely unaddressed by any existing test.
