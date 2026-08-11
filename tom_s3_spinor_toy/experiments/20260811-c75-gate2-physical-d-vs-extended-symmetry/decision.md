# decision -- Gate 2 CLOSED for round124's candidate (NO), full redundancy question stays open

## Verdict

`GATE2_TESTED_DIRECTLY_NO__CANDIDATE_SYMMETRY_NOT_RESPECTED_BY_PHYSICAL_D__REDUNDANCY_QUESTION_STILL_OPEN`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED (positive control clean). P4
CONFIRMED: large, unambiguous, well-controlled violation.**
**Date:** 2026-08-11 · L0: descriptive · script:
`c75_gate2_symmetry_check.py`, results: `results_c75.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** centralizer sanity | abelian, centralizes su(3) on `channel_v` | **CONFIRMED** -- `centralizer_dim=2`, `abelian=True`, `[u1_a,u1_b]` commutator norm `1.62e-15` (~0); `u1_a` centralizes all 8 su(3) generators on `channel_v`, max commutator `2.78e-16` (~0). Matches round124's own already-established result, reused unmodified. | [VERIFIED-numpy, cited] |
| **P2** bridge sanity | `U_v` reproduces its own intertwining property | **CONFIRMED** -- `U_v` det `0.0692...` (same value as C70/C71/C74's own `U_v`, confirming the SAME bridge object is being reused, not a re-solved different one); intertwining residual `4.44e-16` (machine precision). | [VERIFIED-numpy, cited] |
| **P3** positive control | `[D, Leibniz(M_k)]=0` for genuine su(3) generators | **CONFIRMED, exact** -- max commutator over all 8 su(3) generators: `2.776e-17` (machine-precision zero). This confirms the commutator-test machinery itself is sound, so a nonzero result for P4 cannot be attributed to a bug in the test itself. | [VERIFIED-numpy] |
| **P4** Gate 2 test | large, clean nonzero violation (per G74A Lemma B) | **CONFIRMED** -- `[D, Leibniz(u1_a_sigma)]`: max abs entry `1.039`, Frobenius norm `5.241`; `[D, Leibniz(u1_b_sigma)]`: max abs entry `5.527`, Frobenius norm `28.187`. Against `|D|_F=8.000` (for scale): relative violation `u1_a` ~65.5%, `u1_b` ~352%. Both are many orders of magnitude above P3's machine-precision noise floor (`~1e-17`) -- an unambiguous, well-controlled NO. | [VERIFIED-numpy] |

## What this means, stated carefully

1. **Gate 2 of `TRIALITY_DISTINGUISHABILITY_GATE.md` is now tested directly
   for the first time**, for the specific `su(3)+u(1)+u(1)` candidate
   (round124). Previously this gate was marked "Undetermined... the source's
   own tooling says it cannot be checked this way at all" because no prior
   round had both a real physical `D` and a verified bridge into its
   representation space simultaneously. This round had both (via C73/C73b
   and C70 respectively) and ran the test: **the answer is NO, the physical
   `D` does not respect this extended symmetry.**
2. **This computationally confirms G74A's Lemma B prediction**, which was
   previously only an abstract argument ("does not degrade gradually with
   perturbation size; it simply no longer applies, at any nonzero
   perturbation"). The magnitude here (65%-352% relative violation, not a
   small perturbative effect) is fully consistent with that "simply no
   longer applies" character rather than a graceful degradation.
3. **This does NOT resolve the channel-permutation/redundancy question.**
   `predictions_before_data.md`'s own C75 concretization asked for a
   commutant test using genuine channel-PERMUTING operators (something that
   maps `channel_v -> channel_s -> channel_c`), not channel-preserving
   extended generators. No such permuting operator exists in this codebase
   (C71's tautology finding blocks the natural construction) and none is
   built here. The redundancy question is therefore **still fully open**,
   not answered by this round in either direction.
4. **The asymmetry between `u1_a` (65.5%) and `u1_b` (352%) is unexplained**
   -- no structural argument is offered here for why one centralizer
   generator's violation is ~5.4x larger than the other's. Logged as a
   pearl candidate, not investigated further this round.

## Kill Analysis

**Not killed:** any of C70-C74's own established results, round124's
centralizer construction, or G74A's Lemma B -- all reused/confirmed by
citation, and this round's result is a direct computational confirmation of
Lemma B's prediction, not a contradiction of it.

**Killed (for this specific candidate):** the possibility that round124's
`su(3)+u(1)+u(1)` extension is a genuine symmetry of the physical Dirac
operator -- ruled out directly, not just by abstract argument.

**What survives, as a genuinely scoped next step:** the full
`predictions_before_data.md` C75 redundancy/commutant attack remains
unattempted -- it needs a genuine channel-permuting operator, which this
project does not currently have a non-tautological way to construct. This is
either a future round's target (would need a fundamentally different
construction than anything tried in C70-C75) or an explicitly-acknowledged
open question to carry into C76's synthesis.

## What this does NOT show

1. Does **not** complete `predictions_before_data.md`'s own C75
   concretization (the channel-permutation/redundancy commutant test) --
   that remains open, see Kill Analysis above.
2. Does **not** resolve whether the three triality channels are physically
   redundant or genuinely distinct -- orthogonal to what this round tests.
3. Does **not** explain the `u1_a`/`u1_b` magnitude asymmetry -- flagged as
   an open pearl, not investigated.
4. Does **not** change `N_gen=3`'s CONDITIONAL status -- C75 carries no
   pre-commitment in `predictions_before_data.md`'s P1-P5 table.

## Reproduction

```
python experiments/20260811-c75-gate2-physical-d-vs-extended-symmetry/c75_gate2_symmetry_check.py
```
Reuses round124's `G102.centralizer_dim`/`restrict_to_subalgebra`, C70's
`run_direct_solve`/`hom_basis`/`search_nonzero_intertwiner`, and round59's
`build_clifford`/`leibniz`/`NOMIZU`, plus C73's `build_numeric_dirac`, all
unmodified.
