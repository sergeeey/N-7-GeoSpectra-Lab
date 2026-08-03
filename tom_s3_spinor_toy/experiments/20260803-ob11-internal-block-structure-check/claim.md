# OB11 (condition i) Claim — internal block structure across triality channels

**Date:** 2026-08-03
**FL tier:** [x] Standard (single self-contained algebraic computation, reuses established machinery)
**Question type:** [x] descriptive (representation-theoretic classification)

---

## Prior Result Gate

1. Exact claim: is the internal `SU(3)_c×SU(2)_L×SU(2)_R` representation
   content of `H_matter` identical across the three triality channels
   `8_v/8_s/8_c` (OB11's sufficiency condition (i))?
2. `decision.md` grep: [x] done — `round118`, `round119`, `round124`
   discuss the hypothesis and `SU(3)_c` `Hom`-dimension counts, but none
   diagonalizes a Casimir or explicitly states the per-channel
   decomposition. No hit for this exact check.
3. `round*_claim.md`/scripts grep: [x] done — `g102_spin8_fiber.py`'s own
   `S7` computes `Hom_su3(a,b)=6` for all pairs (a dimension count, not a
   decomposition), round127's `decision.md:72-83` gives the algebraic
   argument `Hom(V,V)=4+a²+b²=6⟹a=b=1` but never runs it per-channel.
4. `null_results/`+`parked/` grep: [x] done, 0 hits for this exact
   question (pre-check on submit matched `G39-B1`/`G102`/`S-T-cand` —
   all confirmed unrelated topics on inspection, see below).
5. Prior source re-read: [x] done — read `g102_spin8_fiber.py` in full
   (own tool: `restrict_to_subalgebra`, `stabilizer_basis`), plus an
   Explore-agent grounding pass over round119/124/127/128 and round90 /
   `preprint.tex:292-310` for `H_matter`'s actual construction.
6. **Status:** [x] NEW.

**Null-results pre-check matched, confirmed unrelated:** `G39-B1`
(Spin(6)≅SU(4) Chern-class mismatch, unrelated construction), `G102`
(this claim's own prerequisite, not a duplicate — reused, not repeated),
`S-T-cand` (a different bundle's index formula).

**Scope-clarifying finding from the grounding pass (load-bearing for this
claim):** `SU(2)_L×SU(2)_R` lives entirely on the S³ factor
(`preprint.tex:292-310`; round90) and **never acts on the S⁶-side
octonion fiber where `8_v/8_s/8_c` live at all** — round119 explicitly
corrected an earlier draft's false claim that `SU(3)×SU(2)×SU(2)` embeds
in `SO(6)`. This means OB11's condition (i), as originally worded (full
`SU(3)_c×SU(2)_L×SU(2)_R)` block structure), only has non-trivial content
for the `SU(3)_c` part — the `SU(2)_L×SU(2)_R` part is **vacuously**
satisfied (the S³-side 4-dim spinor factor of `H_matter` is identical
for every channel by construction, since the channel label only ever
attaches to the S⁶ side).

---

## Estimand

**Population:** the three S⁶-side triality-channel representations
`8_v, 8_s, 8_c` of `su(3)_c` (the holonomy subalgebra, `stabilizer_basis`
in G102's own code), already constructed and dimension-counted (G102 S7).
**Intervention:** none (descriptive classification).
**Comparator:** the three channels compared pairwise against each other.
**Endpoint:** quadratic Casimir eigenvalue spectrum (multiplicities and
values) of each channel's `su(3)_c` representation.
**Summary measure:** categorical match/mismatch of the 3 spectra.
**MCID:** not applicable — exact algebraic classification.

---

## Claim

Each of the three channels `8_v, 8_s, 8_c` decomposes as `1⊕1⊕3⊕3̄` under
`su(3)_c`, with an IDENTICAL quadratic-Casimir spectrum across all three
— confirming condition (i)'s only non-trivial part directly, by
diagonalization, not by dimension-count inference alone.

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| Any channel's Casimir spectrum ≠ 2 zero + 6 equal-nonzero eigenvalues | pattern_ok[channel] = False |
| The three channels' nonzero Casimir eigenvalues differ from each other | cross_channel_identical = False |

If FAIL → kills: condition (i) for the `SU(3)_c` part specifically —
would mean round127's dimension-count argument (`a=b=1`) was not in fact
realized, or the three channels are not honestly isomorphic as `su(3)`
reps despite equal `Hom`-dimension (a genuinely informative negative,
since equal-dimension `Hom` spaces do not by themselves guarantee
identical Casimir spectra).
If PASS → survives: condition (i) [SU(3)_c part] verified; the WEAK
reading of `H_physical=H_matter⊗H_generation` gains one more of its three
open sufficiency conditions.

---

## Checks planned

- T1: reconfirm `su(3)` generator count = 8 (sanity gate, reconfirms G102 S2).
- T2: compute the quadratic Casimir for each channel's `su(3)` action,
  using the SAME 8 generators (`stabilizer_basis` output) fed into
  `restrict_to_subalgebra` for all three channels — this makes the
  cross-channel comparison basis-independent even though the absolute
  Casimir eigenvalue itself would change under a different (but internally
  consistent) choice of `su(3)` basis.
- T3 (adversarial): verify the exact multiplicity pattern (2 zero + 6
  nonzero-and-equal), not just "some structure exists" — a partial match
  (e.g. 2 zero + 6 at two DIFFERENT nonzero values) would still fail this
  check even though it superficially "has 8 dimensions."

---

## What this does NOT mean

1. Does NOT resolve OB11 in full — conditions (ii) (no channel-mixing in
   the Dirac operator) and (iii) (triality acting purely as `1⊗t`) remain
   open, and per the 2026-07-19 substrate-check, resolving them requires
   assembling a genuinely new channel-decomposed differential Dirac
   operator, entangled with the still-open OB1 — not attempted here.
2. Does NOT distinguish `3` from `3̄` within each channel — the quadratic
   Casimir cannot tell them apart (they share the same Casimir eigenvalue
   by construction); only the OVERALL multiplicity pattern is checked.
   round128's own explicit intertwiner already settled this finer
   question for `8_v` specifically (matched to Σ, `iso_residual~1e-15`);
   the analogous fine-grained match for `8_s`/`8_c` is not attempted here.
3. Does NOT re-derive G102's own `su(3)` construction or `Hom`-dimension
   counts — reused by import, not recomputed from scratch.
4. Does NOT affect `N_gen=3`, `λ=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.

---

## Fence

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS_CONDITION_I_SU3_PART_VERIFIED**

**Evidence:** [VERIFIED-numpy 3/3] (T1-T3 all pass, see
`ob11_internal_block_structure.py` output, `decision.md`).

**Status:** CLOSED PASS_CONDITION_I_SU3_PART_VERIFIED (OB11 overall
remains OPEN — conditions (ii)/(iii) untouched)
