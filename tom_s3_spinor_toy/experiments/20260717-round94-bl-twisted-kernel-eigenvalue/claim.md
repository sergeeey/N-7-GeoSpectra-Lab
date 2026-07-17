# Round94 (E24) — claim.md

**Stakes:** internal-only (research experiment, no submission/publication, no
external contact; `safe_for_runtime=False` unaffected).
**Question type:** descriptive (does a specific already-constructed vector,
under a specific already-constructed operator, satisfy an eigenvector
equation — not a causal or predictive claim).

## Background (frozen before running the script)

- `experiments/20260717-round93-charge-operator-representation-lift/decision.md`
  (E23) established the sole remaining blocker in the round86-93 chain:
  `B-L` (`experiments/20260619-g15-hypercharge/g15_hypercharge.py`'s `BmL`
  matrix) has only ever been constructed on G6's **untwisted** 8-state S⁶
  weight space — never on the twisted kernel's own Hilbert space
  (`dim ker(D_{S6,twisted})=1` per channel, per
  `experiments/20260621-g74a-lichnerowicz-gap/decision.md`, Lemma B, now
  superseded in its proof route but not its number — see that file's
  2026-07-17 note pointing to
  `experiments/20260708-dolan-casimir-g2su3` +
  `experiments/20260714-round59-trivial-rank-certification` as the actual
  source of the `dim ker=1` number).

## Frozen question

`g15_hypercharge.py`'s `T8` test proves `BmL = (2i/3)·lift_to_spinor(J)`,
where `J` is the `u(1)` center of `su(3)⊕u(1) ⊂ so(6)` (`g15_hypercharge.py:
150-162`). Round59's kernel vector lives in a 2-dimensional
`SU(3)`-invariant ambient space inside `Σ⊗Σ` (`Σ = Λ•(ℂ³)`, 8-dim,
`experiments/20260708-dolan-casimir-g2su3/g2su3_explicit_clifford.py:24-32`),
and the physical `dim ker=1` twisted kernel is a 1-dim subspace of that
2-dim space (`round59_route_b_consistency.py:210-238`, `dim_a=2`; also
`preprint.tex:806-812`).

**Does the same `U(1)` generator that is proportional to `B-L` (`J`, i.e.
`BmL`), Leibniz-lifted to `Σ⊗Σ` the same way this project already lifts
`su(3)` generators to that space
(`round59_route_b_consistency.py:91-106`, `leibniz64`), act as a scalar on
round59's actual kernel vector — and if so, what scalar (what `B-L`
value)?**

## Steps (exactly as specified, in order)

1. **Structural compatibility check.** Is `Σ⊗Σ` (or the specific 2-dim
   `SU(3)`-invariant subspace of it round59's kernel lives in) the SAME
   vector space as G15's 8-dim weight space (so `BmL` can act on it
   directly, or via a cheap, explicit, already-reusable Leibniz lift), or a
   genuinely different space requiring new basis-conversion work?
2. **If comparable:** construct `J`/`BmL`'s Leibniz lift on `Σ⊗Σ` and apply
   it to round59's explicit kernel vector. Is it an eigenvector? What
   eigenvalue (what `B-L` value, via `BmL = (2i/3)·lift_to_spinor(J)` or the
   direct `BmL`-as-degree-operator identity `g15_hypercharge.py` T2
   establishes)?
3. **If NOT comparable:** state precisely what conversion work is missing,
   and whether it is cheap (buildable from this project's own code) or not
   attempted here.
4. **Risk-lens check (report regardless of steps 1-3's outcome):** does
   round59/dolan-casimir's actual construction of the twisted kernel (the
   Dirac operator `D`, not just the `SU(3)`-invariance classification of the
   ambient space) depend on `so(6)` structure OUTSIDE the `su(3)⊕u(1)`
   subalgebra `B-L` is built from (per
   `experiments/20260701-g98-bl-isometry-holonomy/decision.md`, which found
   `BmL` commutes with the 9-dim `su(3)⊕u(1)` subalgebra but not the full
   15-dim `so(6)`)? If so, does this make the eigenvalue claim in step 2
   doubtful, or can it be shown, by direct computation, not to matter for
   THIS specific claim?

## Pre-registered verdicts (exact wording, frozen before running the script)

- **PASS:** the round59 kernel vector(s) are shown, by direct computation on
  comparable/reconciled bases, to be an eigenvector of the `B-L`-proportional
  `U(1)` generator, and the risk-lens check (step 4) finds no incompatibility
  with `su(3)⊕u(1)` — a genuine, well-defined `B-L` charge is computed for
  the twisted kernel, resolving round93's remaining gap.
- **BLOCKED:** the vector spaces (step 1) are not directly comparable
  without new basis-conversion work not attempted here, or the risk-lens
  check (step 4) finds the round59 construction genuinely depends on
  `SO(6)` structure outside `su(3)⊕u(1)`, making a well-defined `B-L` charge
  doubtful without further work.
- **FAIL:** the comparison IS possible and IS attempted, but the kernel
  vector turns out NOT to be an eigenvector of the relevant `U(1)`
  generator (i.e. `B-L`, in whatever sense it can be applied here, does not
  preserve the twisted kernel) — a genuine, informative negative result
  distinct from BLOCKED.

## Assumptions carried in

- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12) — not touched here (this
  experiment is entirely S⁶-side).
- `dolan-casimir-g2su3`/round59's own `dim ker=1`, `dim_a=2`, `dim_b=1`,
  `a=-1`, `b=-√3` results are REUSED by citation, not independently
  re-derived in full — this experiment re-derives `a`, `b` in its own script
  (cheap, since `D_full`/`herm` are directly imported unchanged) as a
  spot-check, but does not re-run the full completeness search
  (`common_nullspace_in_block`) that established `dim_a=2`/`dim_b=1` in the
  first place.
- `BmL`'s own G15 gates (T1-T12, all PASS) are reused by citation, not
  re-derived, except T2 (the Hamming-weight formula), which is spot-checked
  here as part of the structural-compatibility argument.
- `lambda = FREE_COUPLING_PARAMETER` throughout; nothing here touches
  `lambda`. `safe_for_runtime=False` unaffected.

## What this does NOT mean (pre-registered)

1. A PASS here does not re-derive or re-audit round59/dolan-casimir's own
   `dim ker=1` claim — that is reused by citation.
2. A PASS here does not resolve round85/E17's `t=0`/`t=1` coexistence
   question, or the S³-side `T_{3L}`/`T_{3R}` census (E23 Part C) — this
   experiment is entirely about the S⁶-side twisted-kernel `B-L` value.
3. Neither PASS nor BLOCKED nor FAIL here affects this project's `N_gen=3`
   headline (G73/G74A/G74B chain) — that chain does not depend on the
   S³-side torsion-endpoint/hypercharge program this experiment belongs to.
