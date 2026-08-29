# C109 claim -- what exactly causes C108's k=1 reality-breaking anomaly
under M_k^sum?

## L0 gate (EstimandOps)

**Question type:** Descriptive (what structural property of the k=1
construction causes a specific, already-observed effect?). Not causal in
the EstimandOps population-intervention sense -- a mechanistic
diagnosis of one fixed mathematical object, not an experiment over a
population.

## Background -- why this round exists

C108 found that D_PW built from C104's `M_k^sum` (summed over all 4
`(a,b)` CG components) has a clearly non-real spectrum (`max|Im|=0.106`)
at k=1->2, but is exactly real at k=2->3, k=3->4, k=4->5. This was
flagged as an open pearl ("why is k=1 anomalous?") rather than resolved.
This round investigates directly, per the pearl's own falsifiable
prediction (targeted symbolic/structural diagnosis, not another numeric
sweep).

## Counterfactual Frame (exploratory round -- disclosed up front)

Cheap interactive scratch exploration (sympy/numpy) was run FIRST,
matching this project's established discipline. It found, in order:

1. **A structural coincidence unique to k=1**: the auxiliary CG coupling
   representation used throughout the whole multiplication-operator
   construction is fixed at `j2=1/2` (C99-C108's own convention). The
   source level's own representation is `j1=k/2`. Only at k=1 does
   `j1=j2=1/2` -- at every other tested k (2,3), `j1=k/2 != 1/2=j2`.
   `M_1^sum` has exactly one "fully-populated" row (all 4 columns
   nonzero, value 1/2 each) that `M_2^sum`, `M_3^sum` do not have.
2. **This specific row is NOT causally sufficient**: zeroing it out
   restores exact reality (`max|Im|=0.0`) -- but so does zeroing ANY
   other single row, and in fact zeroing ANY ONE of the 16 nonzero
   entries of `M_1^sum` restores exact reality. The effect is extremely
   fragile to any single perturbation.
3. **The sharp, precise characterization**: testing all 15 nonempty
   subsets of the 4 `(a,b)` components (sizes 1, 2, 3, 4) shows that
   EVERY subset of size 1, 2, or 3 gives an exactly real spectrum --
   ONLY the complete sum of all 4 components together produces the
   complex spectrum. This is the actual, precise trigger: not a specific
   row, not a specific entry, but the full 4-component interference,
   occurring only at k=1.

The formal script below independently re-derives all of the above from
scratch.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** `M_1^sum` and its 15 nonempty proper/full subsets of the 4
  `(a,b)` CG components, each used as the off-diagonal coupling in
  C101's own 2-level D_PW at k=1->2.
- **Falsifiable predicate:** exactly which subset(s) of the 4 components
  produce a non-real coupled spectrum.
- **Measurable outcome:** `max|Im(eig(D_PW))|` per subset, `np.linalg.eigvals`
  (certified convention), `1e-6` threshold.

## Predictions (stated before the formal script runs, though after the
disclosed scratch exploration above)

| # | Prediction |
|---|---|
| P0 | `j1=k/2` equals the fixed auxiliary `j2=1/2` only at k=1, confirmed at k=1,2,3. |
| P1 | `M_1^sum` has exactly one fully-populated row; `M_2^sum`, `M_3^sum` have zero such rows. |
| P2 | Zeroing any single one of the 16 nonzero entries of `M_1^sum` (individually, one at a time) restores an exactly real spectrum in every case. |
| P3 | All 11 proper subsets of size 1, 2, 3 (out of the 4 components) give an exactly real spectrum. |
| P4 | Only the full size-4 subset (all components) gives a non-real spectrum, matching C108's own `max\|Im\|=0.106`. |

## What this cannot show

- Does not derive a closed-form group-theoretic reason WHY the full
  4-component sum specifically interferes destructively only at k=1 --
  identifies the precise trigger (full interference, k=1-specific),
  not a first-principles proof of why.
- Does not test whether an analogous resonance (matching `j1=j2`) at a
  DIFFERENT auxiliary representation choice (e.g. testing `j2=1` at
  k=2) reproduces the same phenomenon -- a natural next test, not
  attempted this round.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P0-P4 all hold as predicted, this establishes a precise, sharp,
mechanistic characterization of C108's own open pearl: the k=1 anomaly
is caused by the full, simultaneous interference of all 4 CG components
together (not any single structural feature), occurring specifically at
k=1's j1=j2 coincidence. If instead the effect survives some subset
removal (contradicting P3) or the resonant-row hypothesis (P1) is not
actually unique to k=1, this round reports that instead -- also a real,
informative finding, just a different and less clean one.
