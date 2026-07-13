# Round52-GrowingGap Decision — premise audit result

**Date:** 2026-07-13
**Verdict: SPLIT** — sub-claim (A) PROVEN, sub-claim (B) genuinely
UNRESOLVED (neither PASS nor FAIL by the user's own criteria)

## Summary

The user's frozen claim decomposes cleanly into two independent parts,
and they resolve very differently:

**(A) Casimir gap growth — PROVEN, unconditionally, for every
representation, not just a scanned range.** `C₂(G₂;m,n) ≥ 4` for all
`(m,n)≠(0,0)`, with equality only at `(1,0)` (ρ=7). Proof: every term
in `C₂(m,n)=(2m²+6mn+6n²+10m+18n)/3` is non-negative for `m,n≥0`; if
`m≥1` the m-only terms alone already give `≥4`; if `m=0,n≥1` the
n-only terms give `≥8`. Since the fixed S⁺⊗S⁻ fibre's max SU(3)
Casimir is 3 (already-calibrated, `kp_zero_mode.py`), the **bare**
(cubic-operator) KP gap is `≥1>0` for literally every nontrivial G₂
representation, with zero exceptions, requiring no case-by-case check
at all. This resolves — completely, cheaply, without any new matrix —
the part of "Round 6"'s premise that is actually about representation
theory.

**(B) Torsion-correction boundedness — NOT resolved, and NOT cheaply
resolvable.** This is the part Round 48 actually meant by "unverified,"
and it remains exactly that. No file anywhere in this project computes
or bounds how the torsion-correction operator (the term needed to go
from the bare cubic-operator KP formula to the physical Levi-Civita
operator, per `preprint.tex:699-708`) scales with ρ. The only concrete
torsion computation that exists (Round 22, `decision.md:3317+`) is a
closed, one-off, ρ=7-specific 448-dimensional construction with no
generalizable formula. There is no cheap test for this — establishing
it would require building an analogous explicit torsion construction
for a new ρ, which is precisely the expensive per-representation work
this audit exists to gate before committing to.

## Per the user's own PASS/FAIL framework

Neither condition is cleanly met:
- **Not PASS**: PASS requires one of (1) strict monotone lower bound,
  (2) rep-theoretic inequality, (3) finite exceptional set beyond which
  positivity is automatic, or (4) proof torsion grows slower than
  Casimir — for the WHOLE premise. Only the Casimir-side inequality (2)
  is established; (4) (the actually load-bearing condition, since it's
  what would let the growing Casimir side matter) is not.
- **Not FAIL**: FAIL requires a genuine counterexample (gap non-
  monotonic, cross-terms same order, cancellation, sign change,
  block-dependence). None was found — because sub-claim (A) genuinely
  holds and no computation of the torsion side (positive or negative)
  was performed at all.

**Practical resolution, honestly stated**: the premise cannot currently
be licensed to support the L4B higher-reps sweep, not because it was
falsified, but because half of it (the actually hard half) has zero
supporting evidence and no cheap path to acquiring any. Functionally,
for the purpose of deciding whether to proceed to ρ=27/64/77
computations, this has the same practical consequence as the user's own
FAIL branch — the higher-reps sweep is not currently justified — but
the reason is "insufficient evidence, cost of acquiring it is what we
were trying to avoid," not "found broken."

## Also resolved: the ρ=77 ambiguity

Round 48's shortlist item "L4B remaining reps (ρ=27,64,77...)" is
itself under-specified: 27=(2,0) and 64=(1,1) are unambiguous, but
**dimension 77 names two inequivalent G₂ irreps**, (0,2) [C₂=20] and
(3,0) [C₂=16]. Any future attempt at this program must first decide
which — this was never done and is a small, standalone documentation
gap independent of the growing-gap question itself.

## Recommendation

Per the user's own decision tree, treat "L4B remaining reps
(ρ=27,64,77...)" as **PARKED**, with an explicit, falsifiable revival
condition (not "more time" — per this project's own Parked Pearl
discipline):

**Revival condition**: a general bound (or a concrete disproof) on how
the torsion-correction operator's norm scales with G₂ representation
size ρ — derived either analytically (e.g. from the fixed structure
constants of the G₂-invariant 3-form, contracted against a growing
multiplicity space, evaluated via a general representation-theoretic
argument rather than an explicit matrix) or via a second explicit
per-ρ construction (e.g. ρ=27) that either confirms boundedness or
finds growth comparable to the Casimir gap. Until then, the higher-reps
sweep is not licensed to proceed on the growing-gap premise's authority.

**What survives, reusable regardless of outcome**: the min-C₂=4 proof
(sub-claim A) is a permanent, general result — any future attempt at
this program does not need to re-derive it. The ρ=77 label disambiguation
is likewise permanently resolved.

## Scope discipline check

No Dirac-operator matrices built for ρ=27, 64, or 77 (per explicit user
constraint). No new experiment beyond premise audit. `preprint.tex` not
touched (this round doesn't change any preprint claim — the preprint's
own L4B Open Problems entry already correctly says "remaining
representations formally open," which this audit neither strengthens
nor weakens).

## Files

- `claim.md` — this round's FL Standard-tier artifact
- `round52_growing_gap_audit.py` — script, positive control + T2-T4 inline
- `results_round52.json` — full numeric output
