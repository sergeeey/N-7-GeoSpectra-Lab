# Round107 (Codex items 2+3) — Decision

**Date:** 2026-07-17
**Verdict:** `SU4_SINGLET_CONFIRMED__PATI_SALAM_INCOMPATIBLE__STRENGTHENS_ROUND92_RATHER_THAN_REPLACES_IT`
(two rounds of skeptic review, second pass WEAKENED→addressed with caveats
accepted, not dismissed)
**Go/no-go:** the physical twisted-kernel vector `k_vec` is a genuine
singlet under the FULL 15-generator `SO(6)=SU(4)` action, not merely
under the 8-generator `SU(3)_c` subalgebra (round92). Directly answers
Codex/round105's items 2+3 concern that the `G₂`-trivial kernel "cannot
by itself represent a Pati-Salam `4`... needs an explicit intertwiner" —
this round supplies the intertwiner-level check and confirms the concern
is correct, with an honest caveat on scope (below).

## What was computed [VERIFIED-tool: sympy, this round]

1. **Basis-conversion permutation `P`** built explicitly (qubit-kron-index
   → dolan-casimir `SUBSETS`-index, reusing round94's own bijection
   `g15_index_to_subset`).
2. **First sanity check** [VERIFIED-tool]: `P` correctly reproduces
   round94's own `B-L` result (`P·BmL_g15·P.T == BL_sigma`) — but this
   alone is a WEAK check (flagged by skeptic pass 1): `BmL` is diagonal
   with degenerate eigenvalue multiplicities `(1,3,3,1)`, so a permutation
   wrong WITHIN a degenerate eigenspace would still pass.
3. **Stronger sanity check, added after skeptic pass 1** [VERIFIED-tool]:
   cross-validated `P` against a genuinely NON-diagonal object — the 8
   `SU(3)_c` generators, permuted via `P` from `g10b_su3_explicit.
   su3_generators()`+`lift_to_spinor`, compared against round59's own,
   INDEPENDENTLY-built (different module, no kron/qubit convention at
   all) `su3_matrix_on_sigma(i)`. Individual generators do NOT match
   one-to-one (different labeling/normalization convention between the
   two modules — expected, both are valid `su(3)` bases) — but a SPAN
   check (rank of the flattened-generator matrix stack) confirms BOTH
   8-generator sets span the IDENTICAL 8-dimensional subspace of `Mat(8,8)`
   (`rank(permuted)=rank(reference)=rank(combined)=8`). Skeptic pass 2
   confirmed this span check is logically sufficient to validate `P` for
   the 9-dim `su(3)+u(1)` subalgebra specifically.
4. **Main computation** [VERIFIED-tool]: all 15 `so(6)` generators
   (round93's own `so6_spin_gens`, Leibniz-lifted to the 64-dim `Σ⊗Σ`
   fibre via round59/94's own `leibniz64`, correctly basis-converted via
   `P`) applied to `k_vec` (round94's own exact reconstruction) — **all
   15 give exactly zero.** `span{k_vec, G_1·k_vec,...,G_15·k_vec}` has
   rank **1**.

## Honest scope caveat [accepted from skeptic pass 2, not dismissed]

The independent (third-construction) validation of `P` covers the 9-dim
`su(3)+u(1)` subalgebra (8 `SU(3)` generators + `B-L`). **The remaining 6
"extra" `so(6)` generators (outside `su(3)+u(1)`) were NOT independently
cross-checked against a third construction** — their correctness under
`P` rests on `lift_to_spinor`'s INTERNAL CONSISTENCY (the same function
applied uniformly to all 15 `so(6)` vector-rep generators, round93's own
already-established construction), not an independent third source. This
is logically strong (a single, uniform, already-tool-verified function,
not 15 separately hand-built objects) but is explicitly weaker evidence
than the 9-generator piece's genuine triple-cross-validation. Reported
honestly, not smoothed over.

## Honest framing correction [accepted from skeptic, both passes]

**This does NOT establish Pati-Salam-incompatibility from scratch** —
round92 already showed `k_vec` is an `SU(3)_c` singlet (living in the
`G₂`-trivial isotypic component), which ALONE already rules out
identifying it with a Pati-Salam `4`/`4̄` (whose `SU(3)` restriction is
`3⊕1`, never a pure singlet). **What this round adds, precisely:** under
the standard `4⊗4̄=1⊕15` branching of `Σ⁺⊗Σ⁻`, restricted further to
`SU(3)`, the adjoint `15=8⊕3⊕3̄⊕1` ALSO contains an `SU(3)`-singlet piece
— so the known 2-dimensional `SU(3)`-trivial block that `k_vec` lives in
could a priori have been EITHER the genuine `SU(4)`-singlet "1", OR the
singlet-embedded-in-the-adjoint "1 ⊂ 15" (or a mixture). This round
determines WHICH: `k_vec` sits exactly along the pure `SU(4)`-singlet
direction, not the adjoint-embedded one. This **strengthens** round92's
conclusion (rules out even the SU(4)-adjoint-component possibility) but
does not, by itself, newly establish the headline Pati-Salam-
incompatibility — that was already implied.

## Applying the pre-registered criteria (claim.md Section 3)

**SU(4) SINGLET** confirmed, with the honest scope caveat (9/15
generators triple-validated, 6/15 resting on internal function
consistency) and the honest framing correction (strengthens, does not
solely establish, round92's conclusion) both applied per the skeptic
response matrix — neither dismissed nor allowed to inflate the claim.

## Kill Analysis

- **What this kills:** any remaining hope that the twisted kernel, viewed
  under the FULL `SU(4)` (not just its `SU(3)` shadow), might turn out to
  be an adjoint-component (still Pati-Salam-incompatible, but a
  structurally different possibility this round explicitly rules out).
- **What this does NOT kill:** round92's own `SU(3)_c`-singlet finding
  (reused, reconfirmed, not re-derived); `N_gen=3`; round93's own
  established `SU(4)` construction (`so6_spin_gens`) — reused unchanged.
- **What survives, sharper than before:** Codex/round105's item 3 concern
  is now answered with a concrete computation, not left as a flagged
  worry — the twisted kernel cannot represent Pati-Salam matter under
  ANY reading of `SU(4)` (singlet or adjoint-component), closing off the
  entire `4⊗4̄=1⊕15` branching as a possible rescue for the Pati-Salam/
  anomaly route's matter-content assumption.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Independently validate the remaining 6 "extra" `so(6)` generators against a third construction | A genuinely independent build of at least one of the 6 coset generators, not relying on `lift_to_spinor`'s uniformity — not attempted here |
| Determine whether this closes or merely narrows the round90 Pati-Salam-matter-content question | This round shows the SPECIFIC computed `dim ker=1` kernel is SU(4)-incompatible with Pati-Salam content in either branching piece — whether some OTHER, not-yet-considered zero mode of a modified construction could still work remains open |

## Assumptions carried, unresolved

- Round93's own `so6_spin_gens` construction (via `so6_generators()`+
  `lift_to_spinor`) — reused unchanged, itself resting on `g10_s6_so6_gauge.py`'s
  and `g11_block_generators.py`'s own established, prior-round-verified
  constructions.
- Round59/94's `k_vec`, `leibniz64`, `D_full`, `herm` — reused unchanged.

## What this does NOT mean

1. Does NOT reopen or resolve gate G97 (the geometric-realization
   question) — a logically separate question from "what representation
   does the computed kernel transform in, GIVEN an abstract `SU(4)`
   action already constructed" (round93's own framing, Part D).
2. Does NOT affect `N_gen=3` (G73/G74A/G74B, S⁶-only, independent of this
   entire torsion-escape-route/Pati-Salam program).
3. Does NOT affect `lambda=FREE_COUPLING_PARAMETER` or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round107-su4-orbit-of-twisted-kernel
python e30_su4_orbit_of_kernel.py
```
Expect: `P_is_permutation_matrix=True`,
`permutation_sanity_check_against_round94_BmL_ok=True`,
`stronger_offdiagonal_su3_sanity_check_ok=True` (via span-match, not
one-to-one — `per_generator_match=False` is EXPECTED, not an error),
`k_vec_confirmed_physical_kernel=True`, `span_dimension_of_su4_orbit=1`,
`k_vec_is_su4_singlet=True`.
