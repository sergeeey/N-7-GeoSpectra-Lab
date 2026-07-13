# Round56-ExceptionalSet Decision — closes the L4B higher-representation program

**Date:** 2026-07-13
**Verdict: PASS** — `E_nontrivial = {(1,0)} = {ρ=7}`, registered and
regression-tested. Closes the L4B-higher-reps growing-gap program
opened as a Round 48 shortlist candidate and carried through Rounds
52-56.

## Headline result

```
lambda^2_min(rho) >= C_2,Bourbaki(rho) - 3 - (2*sqrt(6)/3)*sqrt(C_2,Bourbaki(rho))
```

is positive for every nontrivial G₂ representation with
`C₂_Bourbaki(ρ) > C_* = (13+2√22)/3 ≈ 7.460`. Since the smallest
nontrivial value is `C₂(1,0)=4` (ρ=7) and the next is `C₂(0,1)=8`
(ρ=14, already above threshold), **the exceptional set is exactly
`{ρ=7}`** — every larger representation (14, 27, 64, 77, and beyond)
is certified positive by this ONE general bound, with no further
per-representation computation required (monotonicity: `f(C)` is
increasing for `C>K_cert²/4≈0.667`, and every nontrivial `C₂≥4`).

## The 6 steps, all PASS

1. **Equivalence of native/Bourbaki forms**: `K_N√C_N = K_B√C_B`
   verified symbolically as an identity (not just numerically).
2. **Final Bourbaki formula** fixed:
   `C_B - 3 - (2√6/3)√C_B`.
3. **`C_*` derived symbolically**: `(13+2√22)/3`, matching the
   reviewer's own closed form exactly.
4. **Enumeration**: only `(0,0)` [trivial] and `(1,0)` [ρ=7] have
   `C_B≤C_*`.
5. **Registration**: `E_nontrivial = {(1,0)}`.
6. **Regression assertions**: `f(4)=1-4√6/3≈-2.266<0` (ρ=7, correctly
   exceptional); `f(8)=5-8√3/3≈0.381>0` (ρ=14, correctly safe, small
   but strictly positive exact margin).

## Rejected branch (annotated, not deleted)

An earlier message in this same review chain proposed the larger set
`{7,14,27,64}`. **Root cause, confirmed by both parties**: the
native-to-Bourbaki conversion factor was applied **twice** — once
correctly inside `K_cert=K_native/√2` (Round 55, where it converts the
*bound's own coefficient* to Bourbaki units), and again, incorrectly,
when re-deriving the threshold directly on `C_B` (which had already
been converted). The decisive evidence resolving this was not the
Round 55 positive control (which cannot by itself distinguish tight
from loose normalization — a bound need not be saturated to pass a
sanity check) but the explicit `K_cert=K_native/√2` definition line in
Round 55's own script, cross-checked here (STEP 1) via the symbolic
identity `K_N√C_N=K_B√C_B`.

## Narrative arc (Round 52 → 56), for the record

- **Round 52**: proved `min C₂(G₂;ρ)=4` unconditionally (elementary
  algebra, all nontrivial ρ) — the "growing gap" premise's easy half.
- **Round 53**: read Agricola 2002's general theorem; found it does NOT
  directly cover this project's TWISTED operator (later corrected by
  Round 54) but established the right theoretical vocabulary.
- **Round 54**: direct code audit of Round 22's actual `torsion_cross_
  term`/`mixed_AB_term` found BOTH factor as `Σ_r B_r·w(ρ(e_r)v)`,
  giving a unified `O(√C₂(ρ))` structural bound — corrected Round 53's
  narrower claim.
- **Round 55**: certified `K_cert=2√6/3` via EXACT eigenvalues of
  `H_L=ΣB_rB_r†`, `H_R=ΣB_r†B_r` — not numerical estimates. Found
  (Step 0) the naive 14-generator Casimir sum on ρ=7 gives `2·I`, not
  Bourbaki `4·I` — diagnosed as a clean global `√2` rescale.
- **Round 55a**: an external review (9.5/10) demanded independent
  confirmation via a second representation. `ρ=14` gave the SAME ratio
  (`4→8`, ratio 2) — confirmed universal, not a `ρ=7` coincidence.
  `D64²` proven positive semi-definite (never a hidden penalty).
- **Round 55a.1**: confirmed the SU(3) fibre side of the normalization
  independently — direct computation gives `{0,4/3,10/3,3}`, exactly
  matching Bourbaki `su3_casimir`, no rescale needed. Flagged (not
  asserted) a discrepancy in the resulting exceptional set.
- **Round 56 (this round)**: the reviewer confirmed the flagged
  discrepancy was their own double-conversion error; formally
  registered the final, correct exceptional set `{7}`.

## What survives, permanently reusable

- The general bound formula and its exact `K_cert=2√6/3`.
- The exceptional set `{ρ=7}` — ρ=14 and all larger representations
  need no further per-representation Dirac-operator construction to
  rule out unwanted zero modes via this mechanism.
- ρ=7 itself remains governed by Round 22's own EXISTING, independent,
  explicit computation (established, Levi-Civita invertible) —
  unaffected by, and not dependent on, this general-bound program.

## Recommendation

1. **Branch status**: this closes `L4B-HIGHER-REPS` — recommend
   updating `parked/INDEX.md` to reflect CLOSED (not parked, not
   active-pending — resolved) with a pointer to this decision.
2. **preprint.tex**: a citation-only update to the L4B Open Problems
   entry (currently "remaining representations formally open... per
   the growing-Casimir-gap argument") would now more precisely read
   "...proven via a certified general bound (this work) for every
   representation except ρ=7 itself, which is separately established"
   — proposed as a future small round, not applied here without
   separate confirmation, per this project's own scope discipline.

## Scope discipline check

No Dirac-operator matrices built for any representation beyond what
Round 22 already had (ρ=7, ρ=14 checks were Casimir-only, reusing
already-built representation matrices). `preprint.tex` untouched.

## Files

- `claim.md` — this round's FL Standard-tier artifact
- `round56_exceptional_set.py` — script, all 6 steps + regression
  assertions, symbolic throughout
