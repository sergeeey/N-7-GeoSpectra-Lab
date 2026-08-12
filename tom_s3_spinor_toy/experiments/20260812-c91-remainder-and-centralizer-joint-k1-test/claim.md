# C91 -- C83's 9-dim so(8) remainder and C75's 2-dim centralizer, tested on the joint k=1 space

**Experiment id:** `20260812-c91-remainder-and-centralizer-joint-k1-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C86 (built the joint k=1 methodology), C89 (extended it to
so(4)_2). Named as the next step in C89's own decision.md and
`predictions_before_data.md`.

---

## Same-day correction to the framing (found while scoping this round)

C89's own decision.md named the next candidates as "C75's 10-dim
centralizer candidate and C83's 9-dim remainder groups." The "9-dim
remainder" (C83) is correct as stated. **"10-dim centralizer" is
imprecise** -- direct inspection of `c75_gate2_symmetry_check.py`
(`get_centralizer_generators_on_channel_v`) shows `centralizer_dim=2`
(`u1_a`, `u1_b`, abelian, `[u1_a,u1_b]` norm `1.62e-15`). The "10" comes
from the variable name `v_out_10` (a 10-dim ambient space C75 pulled the
centralizer generators out of, `v_out_10[8]` and `v_out_10[9]`), not from
the centralizer's own dimension. Corrected here before building anything
on the wrong premise, per this project's own audit-verification-gate.md
("agent's/self's own prior [VERIFIED] = this round's [INFERRED] until
re-checked"). `predictions_before_data.md`'s C89 entry will be corrected
to match.

## The claims under test

> **P1 (C83's remainder, 3 groups).** C83's own 9-dim genuinely-untested
> so(8) complement (SVD-derived, 3 groups of 3 generators) was tested at
> n=0's scalar approximation only. Does C86's joint k=1 methodology
> (n=0<->n=1 simultaneously, on the certified substrate) find a crossing
> for any of the 3 groups? Per C88's own finding, the S3-side channel is
> candidate-independent (always nonzero) -- what's genuinely open is
> whether these SPECIFIC (arbitrary, SVD-ordered, not expected to close
> into any known subalgebra) generator triples combine with it to produce
> one.

> **P2 (C75's centralizer, adapted construction).** C75's centralizer
> (`u1_a`, `u1_b`) has only 2 generators, not the 3 that
> `build_coupling_on_full_level` sums over (it pairs round67's `Z_1,Z_2,Z_3`
> with 3 S6-side generators). No natural 3rd generator exists for an
> abelian pair. Adapted construction: `triple = [u1_a, u1_b, zero_8x8]`,
> i.e. `T = Z_1(x)Leibniz(u1_a) + Z_2(x)Leibniz(u1_b)` (the `Z_3` term
> drops out since `Leibniz(0)=0`). This is a genuine deviation from the
> established 3-generator pattern, flagged explicitly, not silently
> normalized away. Tested the same way: does it produce a crossing on the
> joint k=1 space?

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | All 3 remainder groups: clean NULL (no crossing), matching the pattern of every so(8) candidate tested so far (C79-C83, C86, C89) | pending |
| **P2** | Adapted 2-generator centralizer coupling: clean NULL as well | pending |

## kill_criterion

Either P1 or P2 finding a genuine (raw-kernel-nonartifact) crossing would
be the FIRST positive signal anywhere in this project's so(8) candidate
search using this construction family -- would require the same extra
scrutiny as any unexpectedly positive result (per C83's own decision.md
language) before being trusted, not an automatic celebration.

## What this cannot show

- Does **not** test C83's remainder or C75's centralizer at k>=2.
- Does **not** validate the 2-generator adaptation as a generally
  meaningful construction beyond this specific exploratory check -- it is
  explicitly ad hoc (no 3rd generator exists), and a negative result here
  says less than a negative result for a genuine 3-generator triple.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
