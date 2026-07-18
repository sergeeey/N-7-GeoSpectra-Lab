# Round118 — Decision

**Date:** 2026-07-17
**Verdict:** `THREE_WAY_SPLIT__STRONG_SU4_READING_BLOCKED__WEAK_READING_NECESSARY_CONDITION_VERIFIED_SUFFICIENCY_UNVERIFIED`
(skeptic: two passes, both found real problems, both corrected — this is
the most heavily-revised decision of the whole gauge/Hilbert/triality
program so far)

**Go/no-go:** the user's own proposed hypothesis
(`H_physical=H_matter⊗H_generation`) splits into two genuinely different
readings with **opposite** outcomes, plus a sub-claim that needed an
actual grep (not an assertion) before it could be trusted. This is
reported as a three-way split, not collapsed into one label.

## What happened, honestly, across two skeptic passes

**First draft:** concluded the whole hypothesis is `BLOCKED_AT_
CONSTRUCTION_STAGE` — citing gate G97 (no `SU(4)` gauge realization) and
a dimension-counting argument (the 1-dim twisted kernel can't factor
nontrivially).

**Skeptic pass 1: `FALSIFIED` the severity.** Found the round (a) applied
G97 — a no-go specifically about **gauged `SU(4)` Pati-Salam
unification** — to a hypothesis that doesn't necessarily require genuine
gauged `SU(4)` at all (the actually-realized gauge group is
`SU(3)_c×SU(2)_L×SU(2)_R`, round90, untouched by G97); (b) attacked a
strawman reading of "the kernel lives in the generation factor" (reading
it as "`H_generation` IS the 1-dim kernel" rather than the more natural
"`H_generation` has one dimension per triality channel, dim 3, separate
from a larger `H_matter`"). **Recommended:** split into the STRONG
(genuine `SU(4)` Pati-Salam) and WEAK (already-realized
`SU(3)×SU(2)×SU(2)`) readings, since they have different outcomes.

**Revision (Part 3 added):** tested the WEAK reading directly — does
`H_physical=H_matter(32-dim, established gauge content)⊗H_generation
(3-dim, one triality-channel slot)` hold? Checked whether the charge
formula `Q=T₃L+Y` has any per-channel (`8_v/8_s/8_c`) index — **asserted
`False` in a code comment, without actually grepping preprint.tex in the
script**, then built the "already true" conclusion on that unverified
assertion.

**Skeptic pass 2: `FALSIFIED` this new sub-claim, on exactly the
project's own audit-verification-gate rule.** Found the comment literally
admitted "NOT independently re-derived or grepped in this script" and
flagged this as a genuine gate violation (an unverified claim used as
load-bearing evidence, exactly what `audit-verification-gate.md` exists
to catch). **Separately**, found a deeper, independent problem: even IF
the charge formula is channel-independent, this is **necessary but not
sufficient** for a genuine tensor-product factorization — also needing
(i) identical internal structure of the 3 32-dim blocks, not just
identical charges, (ii) no channel-mixing terms in the Dirac operator,
(iii) triality acting purely as `1⊗t` with no admixture on the matter
factor. **None of these three are checked anywhere in this project.**

## What was actually verified [VERIFIED-tool: grep, this round, AFTER the second skeptic pass]

Fixed the gate violation directly: `grep -n "8_v\|8_s\|8_c" preprint.tex |
grep "Q\s*=\|Y\s*=\|T_{3"` → **zero hits.** The charge formula
(`preprint.tex:300-301`, `Q=T₃L+Y`, `Y=K₃+(B-L)/2`) is stated exactly
once, with no channel-indexed variant anywhere in the paper. This specific
sub-claim (charges are channel-uniform) is now genuinely, freshly
verified — not asserted.

## Final honest verdict (three-way, per skeptic's own recommended fallback)

| Reading | Status |
|---|---|
| **STRONG** (genuine gauged `SU(4)` Pati-Salam `H_matter`, carrying real `(4,4̄)`) | `BLOCKED` — gate G97 (rounds 102/108/109) rules out any `SU(4)` gauge-algebra realization within the standard product-manifold framework. Not "not yet found" — actively ruled out for this specific route. |
| **WEAK, necessary condition** (charge assignment is channel-independent) | `VERIFIED` — freshly grepped, zero exceptions found. |
| **WEAK, full claim** (genuine tensor factorization `H_matter⊗H_generation`, gauge acting purely on one factor, triality purely on the other) | `UNVERIFIED` — charge-uniformity alone does not establish this; the deeper structural checks (identical internal block structure, absence of Dirac-operator channel-mixing terms, triality acting with no admixture on the matter factor) have not been done anywhere in this project. Genuinely open, not resolved by this round. |

**Overall: the hypothesis, as stated by the user, does NOT currently hold
as a derived fact in either reading** — the strong reading is blocked,
the weak reading has one verified necessary condition but the sufficient
conditions are untested. This is meaningfully different from the first
draft's blanket "BLOCKED, not constructible" — the weak reading remains a
live, only partially-checked candidate, not a dead end.

## Kill Analysis

- **What this kills:** the STRONG (genuine `SU(4)` Pati-Salam `H_matter`)
  reading specifically — for the same reason the whole Pati-Salam
  anomaly-forcing program (rounds 90-112) was already blocked by G97. Not
  a new no-go, an application of an existing one to a new hypothesis.
- **What this does NOT kill:** the WEAK reading — its necessary condition
  (charge uniformity) holds, and nothing here shows the full tensor-
  factorization claim is FALSE, only that it hasn't been checked.
- **What survives, as a genuinely scoped next step:** a concrete, cheap-
  to-state follow-up — check the Dirac operator's block structure across
  the 3 triality channels for cross-channel mixing terms (data likely
  extractable from round107/round110's own existing computations, not
  re-derived from scratch) before either promoting or rejecting the WEAK
  reading.

## Relaxation Map (future work, not attempted here)

| Option | What it would require |
|---|---|
| Verify no channel-mixing in the Dirac operator | Check round107/round110's own existing matrix computations for off-diagonal blocks between the 8_v/8_s/8_c sectors — may already be implicit in data already computed, not a new construction |
| Verify triality acts purely on the generation factor | Would need triality (G67's `Z₃` action) expressed explicitly as an operator on the combined 96-dim space and checked for admixture into the 32-dim matter factor |
| Resolve the STRONG reading differently | Would require abandoning gauged `SU(4)` Pati-Salam unification specifically and finding some other physical role for `(4,4̄)`-type content — a different research direction entirely, not a fix to this hypothesis |

## What this does NOT mean

1. Does NOT establish the WEAK reading is true — only that one necessary
   condition (charge uniformity) is verified; sufficiency remains open.
2. Does NOT reopen gate G97 — the STRONG reading's blockage is a
   consequence of an already-firmly-established no-go, not a new finding.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Does NOT re-derive round59/round73/round94/round107's own established
   results — reused by citation throughout.

## Standing lesson (new, from this round specifically)

**Asserting a claim in a code comment (even with an honest "not verified"
caveat attached) and then treating it as load-bearing anyway is its own
distinct failure mode** — different from simply forgetting to check
something. The comment's own honesty ("NOT independently re-derived or
grepped") should have been a stop sign to actually run the grep before
using the conclusion, not a license to proceed with the caveat attached.
Mandatory second-pass skeptic review caught this; it should not require a
second pass to catch in the future — check the claim the moment the
caveat is written, not after.

## Check (reproduces the arithmetic and the fresh grep)

```
cd experiments/20260717-round118-matter-generation-factorization-test
python e40_matter_generation_factorization_check.py
```
Expect: `nontrivial_factorization_of_1dim_kernel_exists=False`,
`STRONG_reading...g97_blocks_it=True`,
`WEAK_reading_necessary_condition_charge_uniformity_VERIFIED=True`,
`WEAK_reading_full_sufficiency_UNVERIFIED=True`, matching this decision's
three-way split exactly (script updated after the second skeptic pass).
```
grep -n "8_v\|8_s\|8_c" preprint.tex | grep "Q\s*=\|Y\s*=\|T_{3"
```
Expect: zero hits (confirms charge-formula channel-independence, fresh
verification for this decision).
