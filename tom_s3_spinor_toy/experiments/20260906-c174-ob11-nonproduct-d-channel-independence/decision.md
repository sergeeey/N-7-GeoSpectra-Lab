# C174 — Decision

**Date:** 2026-09-06
**Verdict:** `ARTIFACT-STILL-PRESENT` (one of claim.md's own pre-registered
kill-criteria — genuinely fired, not a failure to reach a verdict).
`[VERIFIED-tool]` for what was computed; the question OB11 asks ("does
this non-product coupling distinguish channels?") is **not answered** by
this round — it hit the same structural obstacle C79 already diagnosed,
one level deeper.

---

## 0. Summary

Attempted to extend C79's non-product coupling test (`Z_i × so(4)_1`
self-dual triple, transported to round59's `Σ` via a channel-specific
bridge) to channels `s` and `c` (C79 only tried `v`), targeted at the one
physically-relevant vector (round59's own certified kernel vector, reused
from C172) rather than the raw 128-dim space C79 showed is dominated by a
36-dim non-physical artifact.

**Two methodological attempts, in order, both self-corrected before being
trusted:**

1. **First draft:** compress `D_joint(eps)` onto the 2-dim subspace
   `span(e1⊗v_round59, e2⊗v_round59)` and diagonalize the exact 2x2 block.
   Result: eigenvalues EXACTLY `[1.5, 1.5]` for all three channels, at
   every `eps` tested — a suspiciously perfect agreement.
   **Self-caught before trusting it:** `compressed_t_max_abs_entry` (the
   compressed coupling term's own magnitude) is `~1e-17` for all three
   channels — machine-epsilon zero. The "channel independence" was
   **vacuous**: `T`'s diagonal action within this narrow 2-dim subspace is
   zero for every channel, telling us nothing about whether the
   construction can distinguish channels. This is the same class of error
   flagged in C172 (a test that cannot fail is not a test) — caught here
   before being reported as a result, not after.
2. **Corrected approach:** diagonalize the FULL 128x128 `D_joint(eps)` at
   each `eps`, and track the eigenvalue(s) whose eigenvector has the
   largest overlap with the physical 2-dim subspace (proper handling of
   the fact that a genuine coupling term should move probability OUT of a
   narrow subspace, which a diagonal-block compression cannot see).
   **Result:** the tracked overlap is `1.63` (out of a possible `2.0`) at
   `eps=0` and collapses to `0.28-0.55` almost immediately for any nonzero
   `eps` (see table below) — the physically relevant vector loses most of
   its identity as soon as any coupling is turned on, because it sits
   inside a 36-dimensional degenerate subspace (round59's `D`'s own raw,
   unrestricted kernel — see C172 §"check3", C79's own "raw-kernel
   artifact" finding) that ANY generic perturbation mixes strongly. Tracked
   eigenvalues differ across channels (`max diff ~6.8`), but this
   difference is **not trustworthy** given the overlap has already
   collapsed below 0.5 — the "tracked" eigenvalue is not reliably the same
   physical state across the sweep, let alone across channels.

**This round's own pre-registered kill-criterion `ARTIFACT-STILL-PRESENT`
("restricting to `w⊗v_round59` does not actually avoid C79's raw-kernel
artifact... requires diagnosis, not immediate acceptance of either
channel-dependent or -independent readings") fires exactly as specified.**

---

## 1. What was computed, `c174_channel_independence_check.py`, `results_c174.json`

| Item | Result |
|---|---|
| Bridge sanity (`U_v`, `U_s`, `U_c` intertwining residuals) | all `<1e-14`, `[VERIFIED-tool]` — the channel-specific bridges themselves are sound |
| `v_round59` reused from C172, confirmed unit-norm kernel vector of `D` | `[VERIFIED-tool]`, residual 0 |
| First-draft 2x2 compression | vacuous (`compressed_t_max_abs_entry ~1e-17`) — reported, not hidden |
| Full diagonalization + overlap tracking | overlap collapses from `1.63/2.0` at `eps=0` to `0.28-0.55` by `\|eps\|=0.2-1.0`, for all three channels |
| Cross-channel eigenvalue difference | `max_diff ~6.82` — large, but computed on an untrustworthy (low-overlap) tracked state, so NOT informative either way |

---

## 2. Kill Analysis (Perelman/OSA discipline)

**What this round kills:** the specific, naive hope that comparing a
narrow 2-dim compression, or a simple highest-overlap eigenvalue track, on
round59's raw (unrestricted) kernel vector would give a clean,
artifact-free answer to channel-(in)dependence. Both attempts, tried in
order and each self-corrected before being trusted, ran into the SAME
underlying obstacle (36-dim raw-kernel degeneracy) C79 already named —
this round adds two concrete, reproducible demonstrations of exactly how
that obstacle defeats two different reasonable-looking analysis methods,
which is useful negative information for whoever attempts this next.

**What this round does NOT kill:**
1. C79's own NULL result for channel `v` specifically — untouched, cited,
   not re-litigated.
2. OB11's non-product door in general — this round shows two SPECIFIC
   analysis methods don't work cleanly on this SPECIFIC coupling; it does
   not show no non-product construction could ever be analyzed
   successfully.
3. C173's item-3 no-go (`su(3)`-representation data alone cannot encode
   triality) — untouched; this round was attempting to extend it
   empirically to non-invariant-generator constructions, and simply did
   not reach a trustworthy answer either way.
4. `N_gen=3`'s CONDITIONAL status — unaffected.

**Relaxation Map — the correctly-scoped next step, not attempted here:**
proper (not naive) degenerate perturbation theory within the FULL 36-dim
raw kernel of `D` (not just the 1-dim span of `v_round59` alone): project
`T` onto the entire 36-dim degenerate subspace (⊗ the 2-dim S³ factor,
so a 72-dim degenerate block), diagonalize `T`'s restriction there to find
the CORRECT zeroth-order eigenbasis (standard degenerate perturbation
theory), identify which corrected zeroth-order state has the largest
overlap with round59's own physically-selected direction, and track THAT
state's eigenvalue as `eps` varies. This is a substantially bigger
construction (proper degenerate PT machinery) than either attempt in this
round, and is the honest next step if this specific line is pursued
further — not yet built.

---

## 3. What this does NOT mean

1. Does NOT establish channel-independence or channel-dependence for this
   coupling — genuinely undetermined by this round.
2. Does NOT show OB11's non-product door is closed — only that two
   specific, reasonable analysis attempts on it did not reach a
   trustworthy conclusion.
3. Does NOT contradict or weaken C173's own item-3 result — that result
   concerned a different class of construction (pure `su(3)`-invariant
   data) and stands independently.
4. Does NOT change `N_gen=3`'s CONDITIONAL status.

---

## 4. Floor-Ceiling / Verification substrate note

The genuine obstacle here IS the floor-ceiling problem in a new guise:
the "floor" (a construction with the tested mechanism removed, i.e. `T=0`)
already has a massively degenerate (36-dim) kernel — meaning almost any
metric built on top of it (a compressed block, an overlap-tracked
eigenvalue) has no reliable room to separate "channel distinguished" from
"channel not distinguished" without first properly handling that
degeneracy. This round did not get past that step. Recorded explicitly so
a future attempt does not repeat the same two now-eliminated shortcuts.

---

## 5. Recommendation on independent skeptic pass

**Not run, and judged unnecessary for this specific outcome**, per this
project's own Response Matrix: this round's headline is a genuine
methodological dead-end (`ARTIFACT-STILL-PRESENT`), not a positive claim
about the world — the two self-corrections (vacuous compression caught;
overlap collapse reported honestly with numbers, not glossed over) were
made BEFORE trusting either result, and nothing here is being promoted or
asserted as a discovery. Per this project's own precedent (C171), a
skeptic pass is reserved for surprising positive claims or novel
constructions being promoted, neither of which applies to a
`BLOCKED`/`ARTIFACT` verdict reached honestly. If a future round builds
the proper degenerate-PT fix named above and gets a clean positive or
negative answer, THAT round should get the skeptic pass.

---

## 6. Status

`experiments/20260906-c174-ob11-nonproduct-d-channel-independence/` —
DONE, verdict `ARTIFACT-STILL-PRESENT`. OB11's non-product door remains
open, now with two eliminated shortcuts and a precisely-scoped next step
(proper degenerate perturbation theory within the 36-dim raw kernel).
Registry files not touched, no git operations run, per this session's
established scope-boundary convention.
