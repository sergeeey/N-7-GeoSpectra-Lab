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

**FIXED (2026-07-17):** `_central_eigensystem` now derives the window
half-width from a Gershgorin spectral bound computed directly on the matrix
(`_gershgorin_half_width`), so the window definition no longer depends on
which eigensolver path was taken. The sparse path also requests a
margin-adjusted `k` (double the uniform-density estimate of eigenvalues
expected in the window) and falls back to dense if the window would still
reach the edge of what was computed. Re-ran the same size/W/seed grid as
this finding used originally: window population now scales smoothly across
the size=192 boundary (e.g. size=180→~87-91, 192→~90-98, 193→~90-98,
200→~93-105 — previously ~74-84 dense vs ~17-24 sparse, a 3-4x discontinuity).
Added two regression tests (`tests/test_anderson_benchmark.py`) that assert
the window population doesn't jump discontinuously across the solver switch
and that r/IPR statistics agree within noise on either side of it. Existing
test suite (5/5 in this file, 19/19 across all anderson-related tests
project-wide) still passes; `ruff check` clean.

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

**FIXED (2026-07-17):** `central_eigensystem` now selects eigenvalues by the
same criterion on both paths — nearest to value 0 by `|value|` — instead of
the dense path using index-centered selection. Re-ran the same L=7, W∈{4,24},
5-seed grid this finding used originally: eigenvalue-set overlap went from
62–96% to **48/48 (exact) in all 10 cases**, with r-statistic and IPR
matching to machine precision (<1e-6) rather than differing by up to ~9%.
Added two regression tests (`tests/test_anderson_3d.py`): one asserting
dense/sparse select identical eigenvalue sets at the project's own L=7
parameters, one asserting the dense branch alone picks nearest-to-zero
values rather than an index-centered slice. Existing test suite (5/5 →
7/7 in this file, 21/21 across all anderson-related tests project-wide)
still passes; `ruff check` clean.

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
2. ~~Finding 1 (`anderson.py`) is a genuine numerical bug...~~ **DONE (2026-07-17)**
   — see the "FIXED" note under Finding 1 above.
3. ~~Finding 2 (`anderson_3d.py`) does not require an urgent fix...~~ **DONE
   (2026-07-17)** — see the "FIXED" note under Finding 2 above. Both findings
   from this audit are now fixed with regression-test coverage; only the
   `ISSUES_SCIENTIFIC.md` bookkeeping update (item 1 above) remains open.

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
