# Round126 — Claim

**User-requested follow-up to round124:** "проверь физическую идентификацию
u(1)×u(1) зарядов против Q/Y/B-L" — check the physical identification of
round124's `su(3)⊕u(1)⊕u(1)` centralizer charges against this project's
own established `Q`/`Y`/`B-L` charge formulas. This is exactly round124's
own flagged Relaxation Map item ("Physical identification of the
`u(1)×u(1)` charges... a concrete, cheap next check").

## Prior Result Gate — a genuine basis-identification risk, flagged before
any computation

This project's established `B-L` formula (`experiments/20260619-g15-
hypercharge/g15_hypercharge.py`) is built on an 8-dimensional object
called "the `S⁶` spinor" (`Σ=Λ•(ℂ³)`, constructed via `σ₃⊗σ₃⊗σ₃` qubit
operators, dated 2026-06-19) — this predates the octonion-triality
formalism (`G67`+, dated 2026-06-21) that established `8_v,8_s,8_c` as
the `SO(8)` triality triple. **Checked directly (grep, this round): no
file anywhere in this project explicitly identifies G15's "`S⁶` spinor"
with `8_v`, `8_s`, or `8_c` specifically.** Both objects independently
decompose as `3⊕3̄⊕1⊕1` under `su(3)` (a standard, expected coincidence
given `G102`'s own established fact that ALL THREE of `8_v,8_s,8_c`
restrict this way) — but this is NOT the same as being numerically
identical matrices in a common basis.

**Consequence for this round's scope:** this round does NOT claim
round124's centralizer charges are literally G15's `B-L` matrix. It tests
a narrower, honest, structurally well-defined question instead (below),
explicitly flagging the basis-identification gap as unresolved.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Does round124's `su(3)`-centralizer
(2-dimensional, abelian) contain a direction whose charge assignment to
`8_v`'s own `su(3)`-isotypic pieces (`3`, `3̄`, and the 2 singlets)
reproduces the SAME qualitative RATIO/sign pattern as this project's
established `B-L` formula (`|singlet|:|triplet| = 3:1`, singlet pair
carrying opposite signs, triplet/antitriplet carrying opposite signs) —
a structural-pattern match, not a claim of literal matrix identity.

## Falsifiable claim

1. The 2-dim singlet subspace of `8_v` under `su(3)` alone (already
   confirmed 2-dimensional in round124) can be found explicitly as the
   nullspace of the stacked `su(3)` generators acting on the vector rep.
2. Restricting each of the 2 centralizer generators to this singlet
   subspace and to its 6-dim orthogonal complement (the `3⊕3̄` piece)
   gives well-defined eigenvalue magnitudes (charges) on each piece.
3. Scanning the full 1-parameter family of unit-norm linear combinations
   of the 2 centralizer generators, check whether any combination gives
   `|charge_singlet| / |charge_triplet| = 3` (matching `|−1|/|1/3|=3` from
   G15's `B-L`), with the correct relative sign structure.

## Pre-registered kill criteria

| Outcome | Verdict |
|---|---|
| No combination in the 1-parameter family gives ratio `3` (within numerical tolerance) | **NO_MATCH** — round124's centralizer does not contain a `B-L`-pattern direction; report honestly, do not force a match |
| A combination gives ratio `3` but with the WRONG sign structure (e.g. triplet and one singlet share sign when they should be opposite) | **PATTERN_MISMATCH** — numerically close but structurally different from `B-L`; do not round up to a match |
| A combination gives ratio `3` with correct sign structure | **PATTERN_MATCH_FOUND** — report the specific combination and its exact charges; explicitly still flagged as NOT proven identical to G15's literal matrix (different basis, not cross-checked) |
| The centralizer acts as a SINGLE eigenvalue across singlet+triplet with no free ratio to tune (e.g. proportional to identity on both pieces) | **DEGENERATE** — the 1-parameter family collapses, report why |

## What this does NOT mean (pre-registered)

1. Does NOT claim `8_v` (octonion vector rep) is literally the same
   object as G15's "`S⁶` spinor" — that identification is unresolved and
   explicitly flagged, not assumed.
2. Does NOT, even if `PATTERN_MATCH_FOUND`, prove this project's `B-L`
   formula is "derived from" round124's centralizer — a pattern match
   across two independently-built 8-dim `su(3)`-modules with the same
   abstract decomposition type is expected to some degree by
   representation theory; the interesting content is the SPECIFIC ratio
   and sign match, reported honestly as suggestive, not conclusive.
3. Does NOT resolve round124's own Gates 2-6 physical-realization
   obstruction (dynamical consistency, global action) even if a pattern
   match is found.
4. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
