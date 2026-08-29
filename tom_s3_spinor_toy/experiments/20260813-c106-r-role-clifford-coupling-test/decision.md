# C106 decision -- r-untouched is not load-bearing for this candidate;
a genuinely new, non-generic real-spectrum result survives a proper
negative-control suite

**Verdict:** `R_COUPLED_CLIFFORD_ALTERNATIVE_ALSO_REAL__R_UNTOUCHED_NOT_LOAD_BEARING`
**Status:** RESOLVED -- clean positive result on a well-controlled test,
with a genuinely new open question surfaced (not resolved this round)

---

## Summary

Tested whether the "r-untouched" ansatz used throughout C101-C103/C105
(`B_1 = M_1 (x) I_r`) is load-bearing for the exactly-real coupled
spectrum, by building a physically-motivated alternative that DOES
touch r: `B_1^Gamma := sum_i M_1^{(i)} (x) rmult_i`, a Clifford-type
coupling built by exactly the same "vector-index contraction" pattern
D-bar itself uses (`D_k_bar = -sum_i l_{e_i}(k) (x) rmult_i`), applied
to an exact Cartesian decomposition of the multiplication operator
(built from C104's own 4 (a,b) CG components, no new fundamental
construction).

**All 6 predictions confirmed:**

| # | Prediction | Outcome |
|---|---|---|
| P0 | `L_i(1) = -rmult_i` exactly (identity transform) | **CONFIRMED** -- exact, all 3 generators, no basis change. |
| P1 | `B_gamma` shape matches r-untouched `B_plain` (18x8) | **CONFIRMED**. |
| P2 | `B_gamma != B_plain` (genuinely different object) | **CONFIRMED**. |
| P3 | Coupled D_PW with `B_gamma` has exactly real spectrum | **CONFIRMED** -- max\|Im\|=0.0 exactly. |
| P4 (neg. control) | Fully asymmetric random real coupling gives clearly non-real spectrum | **CONFIRMED** -- max\|Im\| in [2.57, 3.00] across 4 trials, unambiguous. |
| P5 (neg. control) | Random B/B.T-mirrored real couplings are only SOMETIMES real, not universal | **CONFIRMED** -- 3/8 trials exactly real (max\|Im\|=0.0), 5/8 clearly non-real (max\|Im\| in [0.08, 0.18]). |

## What this genuinely establishes

1. **A new exact algebraic fact**: the r-space Clifford generators used
   inside `build_dbar` (`rmult_i`) are literally `-L_i(1)` -- the
   negative of the certified q-space L-generators at level k=1, with the
   IDENTITY similarity transform (no basis change at all). This is a
   clean, reusable structural fact about what `r` actually "is" in this
   construction: not an independent auxiliary space, but (up to a global
   sign / orientation) the same 2-dimensional carrier as q at level 1.
2. **"r-untouched" is demonstrated NOT to be load-bearing for this
   specific candidate relaxation**: a physically well-motivated
   alternative that DOES couple the off-diagonal multiplication operator
   to r (mirroring D-bar's own vector-index-contraction pattern) ALSO
   produces an exactly real coupled spectrum. This directly answers the
   "r's role" question as posed by C105's own Relaxation Map: the
   real-spectrum property is not fragile to this relaxation.
3. **The negative-control suite (P4, P5) is the most important
   methodological result of this round.** An early, informal attempt at
   a negative control (not documented as a formal prediction, corrected
   during this round's own preparation) used `B.T` instead of `B.H` --
   this is accidentally IDENTICAL to the correct construction whenever
   `B` is a real matrix (which `B_gamma` is, confirmed entrywise), so it
   produced a false "still real" reading for the wrong reason. A second
   informal attempt (asymmetric 2x scaling of one off-diagonal block)
   also read as real, and only became genuinely informative once
   verified with a careful float64 pipeline and a confirmed-nonzero
   perturbed entry -- both still gave exactly real spectra even then.
   Given that history, P4/P5 were designed and run specifically to rule
   out "the eigensolver / the degenerate D1,D2 spectra trivially force
   reality for ANY coupling" -- and they do rule it out: fully
   asymmetric random coupling reliably breaks reality (P4), and even the
   more favorable B/B.T-mirrored random coupling is real in only 3 of 8
   trials (P5), not universally. This confirms both the r-untouched
   result (C101-C103) and this round's r-coupled result are genuine,
   non-generic findings tied to the actual CG/su(2) algebraic structure
   -- not artifacts of matrix size, degeneracy, or a broken test.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the hypothesis "the real-spectrum property specifically
requires r to be left untouched by the off-diagonal coupling." A
concrete, well-motivated, certified-machinery-only r-coupled alternative
was built and shown to also give an exactly real spectrum.

**NOT killed:** (a) the real-spectrum property itself -- still true,
now confirmed under a FOURTH distinct construction (C101 2-level,
C102 replication, C103 3-level indirect coupling, this round's
r-coupled 2-level); (b) the general mystery of WHY the property holds
across such a wide family of constructions -- if anything this round
sharpens rather than resolves that mystery, since it rules out one more
candidate explanation ("maybe it only works because r happens to be
untouched") without supplying the actual mechanism; (c) whether OTHER
r-coupled constructions (e.g. a different sign, a different vector-index
contraction, or coupling to r via a genuinely different generator set)
would also preserve reality -- only ONE specific, motivated candidate
was tested.

**Relaxation map (only one relaxation tested this round; two remain from
C105's own map, still untouched):**

| Assumption | Status after this round |
|---|---|
| `S` is block-diagonal across levels (C105) | Still killed (unchanged by this round). |
| Per-level freedom is a single scalar `c_k` (C105) | Still killed (unchanged by this round). |
| `r` is left untouched by the off-diagonal coupling | **This round's relaxation** -- tested and found NOT load-bearing (real spectrum survives touching r via the Clifford-type coupling). |

## New open question surfaced this round (Pearl candidate, not pursued further here)

During preparation, a single-entry perturbation of a CONFIRMED-nonzero
entry of `B_gamma` (breaking matrix symmetry, verified via
`np.allclose(...,...T)==False`) STILL produced an exactly real spectrum
(max\|Im\|=0.0), even though P5 shows generic real couplings with the
SAME mirrored structure are only real 3/8 of the time. This is
surprising local robustness that this round does not explain -- it may
indicate that small/low-rank perturbations of a coupling that is already
real-spectrum stay within some structured "still-real" region (an
"exceptional-point"-adjacent phenomenon), or it may indicate something
more specific to the CG-derived coupling's rank/sparsity structure. Not
formalized as a prediction in this round (found informally during
preparation, not blind-tested) -- flagged in pearl_registry/INDEX.md
for a future, properly-designed round (systematic perturbation-strength
sweep, not a single anecdotal data point) rather than asserted as an
established fact here.

## What this cannot show

- Does not identify a unique "correct" r-coupling -- Clifford-type is
  one natural candidate, not a derivation.
- Does not resolve the general real-spectrum mechanism.
- Does not test k=2,3 levels or the 3-level construction with the
  r-coupled alternative.
- Does not explain the single-entry-perturbation robustness noted above
  (flagged as a pearl, not resolved).
- Does not change N_gen=3's CONDITIONAL status.

## Verification

- `ruff check experiments/20260813-c106-r-role-clifford-coupling-test/`
  -- clean, 0 errors.
- P0-P3 computed exactly via sympy symbolic arithmetic (CG coefficients,
  exact rational/radical entries) before any floating-point conversion;
  P4/P5 are floating-point by necessity (random real matrices), with a
  fixed seed (42) for reproducibility.
- This round's formal script independently re-derives every number
  found during the disclosed scratch exploration (claim.md's
  Counterfactual Frame) from a clean script, including the corrected
  P4/P5 negative controls that superseded two informally-flawed earlier
  attempts (B.T-instead-of-B.H; an unverified single-entry pick that
  turned out to be a zero entry) -- both corrections are recorded here,
  not hidden, per this project's own integrity discipline.
