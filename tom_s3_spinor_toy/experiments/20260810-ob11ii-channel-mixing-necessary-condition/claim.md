# OB11(ii), S⁶-restricted necessary condition — does a channel-mixing term have any algebraic room to exist?

**Experiment id:** `20260810-ob11ii-channel-mixing-necessary-condition`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C29/`20260803-ob11-internal-block-structure-check` (OB11 condition (i),
SUPPORTED), G102 (`Hom_su3` machinery, `restrict_to_subalgebra`), round124 (su(3)+centralizer
probe), round128 (Cartan-Weyl intertwiner `S`, unrelated object — see scope note)

---

## Why this, why now (user-directed pivot away from C11)

C11 (the S³ doubling / KO-tuple gauge-vs-real question) closed completely at C60. The user
explicitly redirected all further work toward the actual headline mechanism, `N_gen=3`, and
named **OB11(ii)+(iii)** — build the three-channel Dirac operator, test whether channel-mixing
terms `X_ij` vanish and whether triality acts purely as `1⊗t` — as the single most informative
next experiment: a binary fork that either strengthens `N_gen=3` past CONDITIONAL or identifies
exactly which mechanism is missing.

## Pre-work check (Adaptive Iteration Branch Rule)

`null_results/INDEX.md`'s `Round118-STRONG-reading` entry REJECTs a **different** claim (genuine
gauged SU(4) Pati-Salam content, closed by gate G97). This round targets the **WEAK** reading
(`H_matter` = already-realized SU(3)×SU(2)_L×SU(2)_R content, `generation` = 3-dim triality-channel
label) — OB11, not reopened, never rejected, `PARTIAL` as of 2026-08-03 (condition (i) SUPPORTED,
(ii) and (iii) explicitly OPEN, "not attempted"). Confirmed distinct branch, not a revival.

## Scope decision — why this round attempts a narrower question than the user's literal proposal

The user's own boxed formulation asks for the **full, differential-operator-level** channel-mixing
test using the real curvature-twisted `D_{S⁶,twisted}` (round59's actual Clifford/connection
construction, not the flat stand-in other rounds have used). Grounding this session found:

1. **No such object exists anywhere in the repo, even partially** — round59's operator acts on a
   *single* channel only (no triality/`8_v/8_s/8_c` structure in its construction); G73/G74A are
   index-theoretic bookkeeping, not matrix-level constructions.
2. The project's own most recent, considered judgment on this exact question
   (`20260803-ob11-internal-block-structure-check/decision.md:14-18`, same day OB11(i) closed):
   *"(ii) requires assembling a genuinely new channel-decomposed differential Dirac operator,
   entangled with the still-open OB1 — not a cheap extraction from existing data."* OB1 (physical
   selection of the S³ torsion parameter `t`) remains PARKED per C58, untouched by today's C57–C60
   closure (which resolved a different, KO-dimension question, not t-selection itself).

Building the full object first would violate this project's own Cheapest Differentiating Test
Protocol — expensive, and gated behind a PARKED blocker not resolved by attempting it directly.
**This round instead runs the cheapest real differentiating test available now: the pointwise
SU(3)-representation-theoretic *necessary condition* for a first-order mixing term to exist at
all**, reusing G102's already-verified `restrict_to_subalgebra`/`hom_dim` machinery without
modification — exactly the technique that closed the structurally analogous pearl #26 result
(`Hom_su3(m*⊗3̄,6)=0` and `Hom_su3(m*⊗6,3̄)=0`, for a *different* representation pair). If this
necessary condition already fails (Hom-space empty), `X_ij=0` is **proven**, full stop, without
ever needing OB1 or the full operator. If it does not fail, OB11(ii) stays open exactly where the
project's own note left it — but genuinely narrowed, and the S³/OB1 entanglement is honestly
preserved as a real limitation, not silently routed around.

**Condition (iii) (`τ=1⊗t`) is explicitly NOT attempted this round** — it needs a different,
separately-scoped object (an explicit triality generator, e.g. via the `S3⊂F4` construction
pearl #33 already found, realized as an operator on zero modes) — round128's intertwiner `S` is a
different object (matches `su3_v` to `su3_σ`, an S³-side spin-lift basis, not a triality generator
relating channels v/s/c to each other) and does not answer (iii) despite the superficial similarity.
One well-scoped claim this round, matching this session's own established discipline.

## The claim under test

> **C61.** The tangent/isotropy representation `m = g2/su3` (6-dim, complement of `su3` in `g2`),
> tensored with triality channel `i`, contains **no** SU(3)-equivariant map into channel `j` for
> any `i≠j` — i.e. `dim Hom_su3(m⊗channel_i, channel_j) = 0` for all six ordered off-diagonal
> pairs `(i,j) ∈ {v,s,c}², i≠j`.
>
> If TRUE: a first-order (Dirac-operator-shaped) channel-mixing term `X_ij` has **zero** algebraic
> room to exist, at any point of `S⁶`, under any G2-invariant connection — condition (ii) is
> **proven**, not merely unfalsified, and the WEAK-reading factorization strengthens materially.
> If FALSE: bare SU(3)-equivariance does not forbid mixing; OB11(ii) remains open, narrowed to a
> genuinely new question (does a specific G2-invariant *section* inside this nonzero Hom-space
> exist) that inherits the same OB1-entanglement the project already flagged.

**Falsifier, fixed in advance:** any off-diagonal pair with `Hom_su3(m⊗channel_i,channel_j) > 0`
refutes the strong form of the claim above.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P0 (setup sanity)** | `m` (orthogonal complement of `su3`'s 8 generators inside `g2`'s 14, via the standard Frobenius/trace inner product already used throughout this codebase) has dimension exactly **6** |
| **P1 (positive control)** | `m`, restricted to `su3`, decomposes with quadratic-Casimir spectrum matching **3⊕3̄** (2 clusters of 3 eigenvalues each, equal magnitude, matching the standard nearly-Kähler tangent representation) — reuses the exact Casimir technique C29 already validated |
| **P2 (harness sanity, load-bearing negative control on the computation itself)** | `dim Hom_su3(m⊗channel_i, channel_i)` (diagonal, i=j) is **nonzero** — round59's own already-built, already-verified single-channel Dirac operator is *itself* a nonzero element of exactly this Hom-space (Clifford multiplication contracts a tangent index with a spinor index). If P2 returns 0, the harness is broken, not the physics — do not accept the off-diagonal result without this passing first |
| **P3 (the actual question)** | Best guess, stated honestly before running: a rough Clebsch-Gordan hand-count of `(3⊕3̄)⊗(1⊕1⊕3⊕3̄)` shows the tensor product contains multiple copies of `1`, `3`, `3̄` — i.e. the *representation content* needed for a nonzero map into `channel_j=1⊕1⊕3⊕3̄` is generically present. **Predicted outcome: `Hom_su3(m⊗channel_i,channel_j) > 0` for the off-diagonal pairs too** — meaning this necessary condition will likely NOT by itself kill mixing. This prediction is stated to be genuinely falsifiable by the run, not to pre-decide it: the hand count uses only representation *content*, not the actual invariant tensor structure (built from the real octonion/G2 data), which could vanish for a reason the content-count alone can't see |

## kill_criterion

C61 (strong form) **survives** if all six off-diagonal `Hom_su3(m⊗channel_i,channel_j)` come out
exactly 0, with P0–P2 all passing as predicted (harness verified sound). C61 **fails** (OB11(ii)
stays open, narrowed as described above) if any off-diagonal Hom-space is nonzero. Either outcome
is informative; P3 is a stated guess, not the criterion — the computed dimensions decide it.

## What this cannot show

- Does **not** prove `X_ij≠0` even if P3's prediction holds (nonzero Hom-space is necessary, not
  sufficient, for a genuine G2-invariant mixing term to exist as an actual section) — only that the
  question stays open at the next, harder level (an explicit G2-invariant-section search, the same
  difficulty class the project already flagged as OB1-entangled).
- Does **not** attempt condition (iii) (`τ=1⊗t`) — separately scoped, not started here.
- Does **not** touch the S³ factor, `t`-selection, or OB1 in any way — this is deliberately an
  S⁶-only necessary-condition test, consistent with the user's own step-5 instruction that S³
  should supply geometry/spinor structure only, not act as a generation-multiplying mechanism.
- Does **not** build the actual curvature-twisted, channel-decomposed differential Dirac operator
  the user's literal proposal describes — that remains future work, now informed by whichever
  outcome this round produces.
- Nothing about `λ`, `ρ`, or any other open parameter — orthogonal to this question.
