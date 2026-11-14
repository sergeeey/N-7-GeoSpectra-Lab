# C198 Claim — does the kernel LINE of D(θ) rotate across C73b's torsion-angle family even though dim ker stays fixed at 1?

**Date:** 2026-09-17
**FL tier:** [x] Standard
**Question type:** [x] descriptive (NOT causal — no intervention on a population, just "what is the value of this quantity across this fixed family")

**Source of this idea:** user-forwarded cross-domain analogy from an external
paper on random circulant graphs / Lovász number (Fourier-basis reduction of
an SDP to a kernel/null-space problem, then studying the null-space's
*geometry* — e.g. `‖x‖₂ ≤ (log²n/√n)‖x‖₁` — not just its dimension). The
transferred methodological point: this project's own `Δ_geo = dim ker D − F_graded`
diagnostic (C148) only asks "did an extra dimension appear?" It has never
asked "even when the dimension doesn't change, does the kernel's *orientation*
inside the ambient space still move?" Two operators can have `dim ker=1` each
with completely different unit zero-mode vectors — `Δ_geo=0` in both, but not
obviously "the same information."

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. **Exact claim:** the unit kernel vector of `D(θ)` (in the 2-dim
   `domain_inv` coordinates already established by C73/C73b) is NOT constant
   (up to overall phase) as `θ` varies across C73b's own 2-parameter
   `Hom_su(3)(m, Λ²m)` torsion-angle family.
2. `decision.md` grep (formula/synonyms: "projector", "principal angle",
   "kernel geometry", "P_ker", "zero mode overlap", "subspace"): **done, via
   a dedicated Explore-agent search of the whole repo** (this session,
   2026-09-17) — 0 real hits. Two adjacent-but-distinct precedents exist and
   are cited, not duplicated: `experiments/20260718-round125-.../decision.md`
   (principal angles between two STATIC Lie-subalgebra spans, not a Dirac
   kernel, not a family) and `experiments/20260812-c86-.../c86_full_k1_coupling.py:222`
   (a single FIXED kernel projector used as a reference to test overlap of
   OTHER eigenvectors against it, never two kernels from two different
   connections compared to each other).
3. `round*_claim.md` + scripts grep: **done**, same search — C139 §8c and
   C147's own swept families have `dim ker D(∇)=0` identically throughout (no
   nontrivial kernel to compare at any two points); round59's own nonzero
   kernel (`dim=1`) is a single, unswept point. C73b (this round's own
   substrate) is the ONLY place in the repo where a genuinely different
   (non-scalar-rescaled) connection family gives `dim ker=1` at more than one
   point — confirmed via a second, targeted Explore-agent search specifically
   hunting for any other independent nonzero-kernel data point on this same
   Σ space; none exists.
4. `null_results/` + `parked/` grep: **done**, 0 hits for any of the search
   terms above.
5. `git log -S`/`-G` pickaxe: not run (the two Explore-agent searches above
   already establish 0 hits at the file-content level across the CURRENT
   tree; a historical pickaxe would only matter if something had been
   deleted, which is not suspected here and is not worth the extra cost for
   a Standard-tier round).
6. Primary source re-read (not from memory): **done** — read
   `experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/c73b_torsion_family.py`
   in full directly, myself, not via agent summary. Confirmed: `test_torsion_sweep`
   computes `block = target_inv.conj().T @ d_theta @ domain_inv` (a `1×2`
   row vector `[a(θ), b(θ)]`, since `target_inv` is 1-dim, `domain_inv` is
   2-dim — `c73_dirac_battery.py:71-83`), and saves ONLY `b=block[0,1]` and
   `kernel_dim` to `results_c73b.json` — `a=block[0,0]` and the actual kernel
   DIRECTION are never saved. This experiment's own script re-derives both
   from the same, unmodified upstream functions.
7. **Status:** [x] NEW

---

## Estimand

**Population:** the 13-angle sweep already fixed by C73b (`θ ∈
{0°,22.5°,...,337.5°}` minus the ones not swept — actually C73b's own 13
points: `0,22.5,45,...,270` in 22.5° steps), PLUS the exact point
reconstructing round59's own NOMIZU connection (via C73b's own computed
`(t1,t2)` coefficients, not a sampled angle) as a labeled reference.
**Intervention:** none — this is not an intervention/comparator design, it
is a structural/descriptive characterization of one fixed mathematical
object (the null-space map) across one fixed, already-defined 2-parameter
family.
**Endpoint:** for each pair of angles `(θ,θ')`, the OVERLAP of their
(normalized) kernel vectors in the shared 2-dim `domain_inv` coordinate
space: `overlap(θ,θ') = |v(θ)† v(θ')|` where `v(θ) = (b(θ), -a(θ)) /
‖(b(θ),-a(θ))‖` is the unit null vector of the row `[a(θ),b(θ)]`.
**Summary measure:** `overlap(θ, θ_NOMIZU)` for every swept `θ` against the
NOMIZU reference point, plus `overlap(θ,θ+180°)` as a built-in positive
control (see below).
**MCID:** none in the usual causal-effect sense (descriptive question) — the
practically important threshold is binary-ish: `overlap ≈ 1` (say `>0.999`)
for ALL pairs means "kernel orientation is fixed across the whole family,"
`overlap` varying substantially (say ranging below `~0.9` somewhere in the
sweep) means "kernel orientation genuinely moves."

## Claim

**Pre-registered prediction, stated BEFORE running (per the user's own
explicit framing — both outcomes are informative, this is not a claim I
expect to fail):** my own best guess, based on the algebra alone (before
computing anything): `block(θ) = cos(θ)·Block_{t1} + sin(θ)·Block_{t2}` is
a genuine 2-real-parameter LINEAR PENCIL of `1×2` row vectors (since
`build_numeric_dirac` is exactly linear in the connection, already
established by C73/C73b), and there is no a priori algebraic reason for
`Block_{t1}` and `Block_{t2}` to be proportional to each other (they come
from two independent basis vectors of a genuine 2-dim `Hom_su(3)(m,Λ²m)`
space). A generic linear pencil's null direction rotates as the
combination coefficient changes. **My prediction: the kernel direction
WILL move non-trivially across the family (`overlap` will drop
measurably below 1 for at least some pairs), i.e. `Δ_geo=0` will coexist
with nonzero geometric information in the kernel's orientation.** Stated
explicitly so this is falsifiable, not fitted after the fact.

Supporting sub-claims:
1. `overlap(θ,θ+180°) ≈ 1` for all `θ` (POSITIVE CONTROL — negating the
   defining row vector by an overall sign, which is what `θ→θ+180°` does to
   `cos,sin` simultaneously... actually `cos(θ+180)=-cos(θ)`,
   `sin(θ+180)=-sin(θ)`, so `block(θ+180)=-block(θ)` exactly — a global sign
   flip of the functional, which cannot change its null line). If this
   FAILS, the methodology itself (not the physics) is broken and the round
   stops here.
2. The kernel-dimension values (`kernel_dim=1` at all 13 original angles)
   reproduce C73b's own `results_c73b.json` EXACTLY, as a positive control
   that this round's re-derivation of `block` uses the identical
   `domain_inv`/`target_inv`/`build_numeric_dirac` calls, not a subtly
   different setup.
3. `overlap(θ, θ_NOMIZU)` is reported for every swept angle, honestly, with
   NO claim of physical relevance — every one of C73b's 13 angles, and every
   other point on this family besides NOMIZU's own, already FAILS
   calibration (`results_c73b.json`, `calibration_passes: false`
   everywhere except possibly exactly at NOMIZU's own angle, which was never
   itself swept as a discrete point). This experiment is therefore a
   statement about the MATHEMATICAL structure of the abstract
   `Hom_su(3)(m,Λ²m)` family, not a physically-realized geometry — exactly
   the same honest framing C73b's own decision.md already uses for this
   family.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Sub-claim 1 (positive control) fails | `overlap(θ,θ+180°) < 0.999` for any swept `θ` — kills the METHOD, not the physics; stop and debug before reporting anything else |
| Sub-claim 2 (reproduction control) fails | any `kernel_dim` computed here ≠ C73b's own saved value at the same angle — same as above, a methodology failure |
| Main claim FALSE | `overlap(θ,θ_NOMIZU) > 0.999` for EVERY swept `θ` — i.e. the kernel direction does NOT move at all across the family — this would mean `Δ_geo=0` really does correspond to zero geometric information here, at least for this specific family |

If FAIL (main claim false) → kills the specific hypothesis "kernel
orientation carries information `Δ_geo` misses" FOR THIS FAMILY — does not
kill the general cross-domain idea (a different family, or a genuinely
admissible/calibration-passing one, could still show movement).
If PASS (main claim true, positive controls hold) → establishes, for the
first time in this project, a concrete example where `Δ_geo=0` coexists
with a moving kernel subspace — strengthens the case that `dim ker` alone
under-describes the kernel, though ONLY at the level of this abstract
family (see "What this does NOT mean").

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | `kernel_dim` at C73b's 13 angles matches `results_c73b.json` exactly | if it doesn't match, the reproduction itself is broken — this IS the negative control (a mismatch must be caught, not silently accepted) |
| T2 | `overlap(θ,θ+180°) ≈ 1` for all 13 angles | an intentionally WRONG overlap formula (e.g. comparing `v(θ)` to `v(θ)` rotated by a random unrelated phase) should NOT give 1 — sanity-checked by also computing `overlap(θ,θ)` (must be exactly 1, trivially) as a second, simpler control |
| T3 | `overlap(θ,θ_NOMIZU)` computed via the (b,-a) 2-vector must equal the overlap computed by embedding both kernel vectors into the FULL 64-dim space via `domain_inv @ v` and taking the inner product there (an adversarial/independent-method cross-check, since `domain_inv`'s columns are orthonormal by SVD construction, the two must agree to machine precision) | if they disagree, either `domain_inv` is not orthonormal (a real bug to find) or the reduced-coordinate shortcut is invalid |

---

## What this does NOT mean

1. Does NOT bear on the physical `N_gen=3` question directly — every point
   on this family except (possibly) NOMIZU's own exact angle fails
   calibration; this is a statement about an abstract Hom-space's structure.
2. Does NOT generalize to claim `Δ_geo` is useless — it may still be exactly
   the right diagnostic for OTHER questions (whether an extra dimension
   appears); this only tests whether it's the WHOLE story.
3. Does NOT retest or revise C73b's own admissibility/calibration verdict —
   that stays exactly as C73b left it (`PARTIAL`, `CLAIM_LEDGER.yaml:1619-1628`).
4. Does NOT establish that kernel orientation movement, if found, has any
   downstream physical consequence — that would be a separate, later
   question if this round's main claim survives.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**REJECT (main claim FALSE).** My own pre-registered prediction (kernel
direction would rotate) did not survive: `overlap(θ,θ_NOMIZU)=1.000000`
exactly at all 13 swept angles, and — found along the way, not assumed —
`block(θ)=exp(−iθ)·Block_t1` EXACTLY, an exact algebraic mechanism
(`Block_t2=−i·Block_t1`) that makes the kernel line's rigidity a provable
fact on this family, not a numerical coincidence. All 3 planned checks plus
one added mechanism check (T1, T1b, T2, T3) PASS. Full result and honest
scope caveats (this family fails calibration everywhere) in `decision.md`.

**Evidence:** [VERIFIED-numpy 4/4] (T1, T1b, T2, T3 all PASS; cross-checked
against C73b's own independently-saved `results_c73b.json` magnitudes)

**Status:** CLOSED REJECT — see `decision.md` §6 Kill Analysis for what
survives (the general cross-domain idea) vs. what's killed (this specific
family's ability to test it).
