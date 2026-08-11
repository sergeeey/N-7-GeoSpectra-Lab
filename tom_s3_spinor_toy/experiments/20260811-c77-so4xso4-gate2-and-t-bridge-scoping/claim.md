# C77 -- SO(4)xSO(4) Gate 2 test + honest scoping of the actual T-to-D bridge

**Experiment id:** `20260811-c77-so4xso4-gate2-and-t-bridge-scoping`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C76 (named this as the concrete next lead); C75 (Gate 2
methodology, established here for round124's candidate); round119
(`SO(4)xSO(4)` candidate + its own triality matrix `T`, both cited not
rebuilt); round125 (verified `SO(4)xSO(4)` and `su(3)+u(1)+u(1)` share only
a 3-dim abelian core -- genuinely different candidates); C70 (verified
intertwiner `U_v`)

---

## Why this round is scoped the way it is (read before trusting the result)

C76's decision.md named `TRIALITY_DISTINGUISHABILITY_GATE.md`'s `SO(4)x
SO(4)` transport matrix `T` as "the most concrete, unattempted lead" for
attacking the channel-redundancy question, but flagged it as "real,
nontrivial construction work... not a quick follow-up." **This round
verifies that flag was correct, precisely, before doing any speculative
construction.**

Reading `triality_so4xso4_invariance.py` directly (not from memory) shows
`T` is a **12x12 matrix acting on the COORDINATES of the `so(4)+so(4)`
LIE ALGEBRA itself** (`build_triality_matrix_T()`), not a representation-
space intertwiner like C70's `U_v`. It encodes: given a generator `a`
(coordinates in the 12-dim `so(4)+so(4)` basis) acting on the vector
representation `8_v`, `T` returns the coordinates of its triality partner
`b`, which acts on the spinor representation `8_s` -- **assuming the same
12-dim coordinate basis describes the algebra's action on all three
representations**, which is exactly the open question round119's own
follow-up diagnostic (`triality_so4xso4_invariance.py` lines 289-311)
found NOT yet established: transporting `so(4)_1`'s generators via `T`
gives an algebra with a DIFFERENT commutant/Casimir structure than the
original -- "the transported algebra does NOT preserve the same block
split... vector-rep and spinor-rep `SO(4)xSO(4)` constructions are not yet
shown to be the same embedding." **This is a real, pre-existing,
documented gap in round119's own construction, not something this round
introduces.**

Using `T` to build a genuine channel-permuting operator on round59's real
`D` would additionally require an `SO(4)xSO(4)`-equivariant identification
of Sigma with `8_s` AND `8_c` specifically (not the su(3)-based `U_s`/`U_c`
C70/C71 already built, which are a different embedding, per round125:
only 3 shared abelian dimensions). **No such identification exists
anywhere in this codebase.** Building one from scratch is comparable in
scope to C70's own bridge-construction round, not a same-round add-on.

**What this round does instead, honestly re-scoped:** (1) the direct,
well-motivated, cheap extension of C75's Gate 2 methodology to round119's
`SO(4)xSO(4)` candidate specifically (transported via the ALREADY-verified
`U_v`, reusing C75's machinery almost unchanged) -- genuinely new
information regardless of outcome, since C75 only tested round124's
candidate; (2) a precise, written scoping of exactly what remains missing
for the actual `T`-based channel-permuting construction, so a future round
does not have to re-derive this analysis from scratch.

## The claim under test

> **C77 (working).** round119's `SO(4)xSO(4)` candidate (a genuinely
> different 12-dim subalgebra than round124's 10-dim `su(3)+u(1)+u(1)`,
> per round125) is tested against Gate 2 for the first time, using the
> same methodology as C75. **Whatever the result, this does NOT constitute
> a "T-to-D bridge"** -- that requires additionally resolving round119's
> own open vector-vs-spinor-rep consistency gap and building a genuinely
> new `SO(4)xSO(4)`-equivariant per-channel identification, neither
> attempted here.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (basis compatibility sanity)** | `build_so4xso4_basis()`'s 12 generators, stacked with G102's own su(3) generators on `channel_v`, reproduce round125's already-published `dim(A)=12, dim(A∩su3-centralizer)=3` result exactly -- confirms this round is combining the two constructions in the same convention round125 already verified, not silently introducing a NEW convention mismatch | pending |
| **P2 (bridge sanity)** | C70's `U_v` reproduces its own already-verified intertwining property for the su(3) generators (residual near machine precision) -- reused, not re-solved | pending |
| **P3 (positive control)** | `[D, Leibniz(M_k)]=0` for all 8 genuine su(3) generators, matching C75's exact result | pending |
| **P4 (Gate 2 test, SO(4)xSO(4))** | `[D, Leibniz(g_i)]` for each of the 12 transported `so(4)+so(4)` generators is nonzero and large -- per G74A's Lemma B (a GENERAL argument about breaking G2, not specific to round124's construction), expected to fail cleanly, consistent with C75's result for the other candidate | pending |

## kill_criterion

P1 fails if the stacked-rank computation disagrees with round125's own
published numbers -- would indicate a genuine convention mismatch between
the two source modules, a serious and immediately-blocking finding
requiring the whole test to stop and be re-scoped. P2/P3 fail if they
disagree with C70/C75's own already-established results. P4's outcome is
recorded either way: if `SO(4)xSO(4)` (unlike round124's candidate) DOES
commute with `D`, that would be a genuine surprise contradicting the
generality of G74A's Lemma B and would need immediate, careful
re-examination rather than being accepted at face value.

## What this cannot show

- Does **not** build the actual `T`-based channel-permuting operator --
  explicitly scoped as out of reach this round, for the specific reasons
  given above (round119's own unresolved vector/spinor consistency gap;
  no `SO(4)xSO(4)`-equivariant `U_s`/`U_c` analogue exists).
- Does **not** resolve the channel-redundancy/permutation question --
  orthogonal to Gate 2, exactly as C75 already noted for the other
  candidate.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** retroactively correct or re-run round119's own diagnostic
  finding (transported `so(4)_1` losing its commutant/Casimir structure)
  -- cited, not re-verified independently in this round.
