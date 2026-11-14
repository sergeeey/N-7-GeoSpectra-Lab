# C207 Claim — close F6 (metric EOM) for the ECSK/C134 candidate; F7 is moot

**Date:** 2026-09-24
**FL tier:** [x] Full (architecture-level: closes a named field of
`PARENT_ACTION_GATE.md`, the project's own OB1/OB2 program gate)
**Question type (EstimandOps L0):** Descriptive — does a specific,
already-frozen background satisfy a specific, already-named equation at
a specific, already-derived point?

## Why this round exists

`PARENT_ACTION_GATE.md` F6 names, in its own words, "the single largest
gap in the whole OB1 program": no equations of motion have been derived
for the full candidate background. C134 (2026-09-02) derived the
**torsion** half of ECSK's field equations and logged F6 as `PARTIAL, not
PASS` because the **metric** (vielbein) equation `R_{MN} - (1/2)g_{MN}R =
kappa_13 T_{MN}` was never derived or checked against the frozen
background — C134's own text: *"Not an assumption but a gap: the
vielbein EOM (§2), which the background violates"* (asserted, not
formally closed).

This round closes that specific gap — not by deriving a new stress
tensor from scratch, but by chaining three already-certified facts this
project already has on record, plus one standard (textbook, not
project-specific) fact about product manifolds.

## Prior Result Gate

1. Exact claim: at `t=1/2` — the unique point where C134's own torsion
   equation of motion is self-consistent, and where KT-8 guarantees zero
   fermion zero modes (so the fermion stress tensor vanishes identically,
   not approximately) — the frozen `M4xS3xS6` background's Ricci tensor
   is nonzero, because its `S3` block alone (round111's own already-
   published `Ricci^t(Z_a,Z_b)=8t(1-t)*delta_ab`) is nonzero at `t=1/2`,
   and the Ricci tensor of a Riemannian product is block-diagonal
   (standard fact — no cross terms between factors).
2. `grep` of `null_results/`, `parked/`, `experiments/` for prior direct
   closure of F6's metric sector: no hits beyond C134's own `PARTIAL`
   status and round111's `Scal(t)` computation (both reused here, not
   duplicated).
3. **Status:** [x] NEW (a synthesis of existing facts into a new,
   previously-unstated formal conclusion, not a restated existing claim).

## Estimand

**Population:** the ECSK gravitational action on the frozen `M4xS3xS6`
background, evaluated at `t=1/2` (the one torsion-equation-consistent,
fermion-condensate-free point per C134+KT-8).
**Intervention/method:** apply the standard product-manifold Ricci
block-diagonal decomposition to the already-certified `S3` Ricci tensor
(round111); check whether the resulting total Ricci tensor can vanish.
**Comparator:** C134's own `PARTIAL` (unaddressed) status for F6's metric
sector.
**Endpoint:** boolean — does `Ric(g)=0` hold on the frozen background at
`t=1/2`, yes or no.

**Natural-language statement:** "We ask whether the frozen M4×S3×S6
background, evaluated at the one point where ECSK's own torsion equation
of motion is self-consistent and where this project's own KT-8 result
guarantees no fermion condensate, satisfies the vacuum Einstein equation
Ric(g)=0 — using only already-certified project facts (C134, KT-8,
round111) plus one standard product-manifold identity, not a new
geometric derivation."

## Kill criterion

| Condition | Consequence |
|---|---|
| `Ric_S3` at `t=1/2`, reconstructed from round111's own `8t(1-t)` eigenvalue formula, is nonzero as a matrix (not just its trace) | Confirms the S3 block alone is enough to make the full Ric(g) nonzero — F6 closes to REJECT for this candidate |
| `Ric_S3` were found to vanish at `t=1/2` (it does not) | Would require checking the `S6` block separately before any conclusion — not needed here |
| The `8t(1-t)` eigenvalue formula's trace does not reproduce round111's independently published `Scal(t)=24t(1-t)` | Internal inconsistency between two already-published numbers — stop, do not proceed, flag as a project data-integrity issue |

If FAIL (inconsistency found) → kills: the reuse of round111's numbers as
stated; would require re-deriving from scratch before any conclusion.
If PASS → survives: F6 for the ECSK+C134+frozen-background candidate is
definitively closed to REJECT, and — as a free corollary — the
conclusion is radius-independent (no finite `rho_3` rescues it), meaning
this candidate cannot be rescued by adjusting the `S3` radius alone
either.

## What this does NOT mean

1. Does NOT claim the `S6` block's own curvature was computed or is
   zero — the argument is deliberately independent of it (a single
   nonzero block in a block-diagonal sum is sufficient).
2. Does NOT close F6 for the OB1/OB2 program as a whole — only for the
   specific ECSK-with-fermion-condensate-torsion candidate examined by
   C134. Other candidates (e.g. a flux-supported Freund-Rubin-type
   background, this project's own G54-G66 line) are untouched by this
   round and would need their own F6 assessment.
3. Does NOT touch OB1/N_gen=3's own S6-only chain (G73/G74A/G74B) —
   unrelated substrate.
4. Does NOT constitute a new geometric derivation of the S6 nearly-Kähler
   curvature — deliberately avoided, since it is not needed for this
   round's conclusion.

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced (uses `t`,
  `rho3`, matching this project's existing torsion-parameter convention).

## Verdict

**REJECT (for F6, ECSK/C134/frozen-background candidate).** The vacuum
Einstein equation is violated at the one point ECSK's own torsion sector
permits. F6 for this candidate closes from `PARTIAL` to `REJECT`. **F7
(stability) is MOOT for this candidate** — there is no self-consistent
fixed point to test the stability of, stated explicitly rather than
silently skipped, per this project's own Kill Analysis discipline.

**Evidence:** [VERIFIED-sympy 6/6 checks, all_pass=True] — internal
consistency of round111's own two published numbers confirmed exactly;
`Ric_S3` at `t=1/2` confirmed nonzero and positive-definite as a full
3x3 matrix, not just via its trace; radius-independence confirmed (no
finite `rho_3` root).

**Status:** CLOSED REJECT.
