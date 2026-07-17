# E21-followup (round91) — Decision

> **⚠️ CORRECTION (2026-07-17, added retroactively after user review):**
> this experiment's own motivating question — "does completing an
> otherwise-odd Witten `SU(2)_R` doublet count force `t=0`'s content" —
> is now known to rest on a REFUTED premise: round90's own use of Witten's
> `SU(2)` anomaly as the forcing mechanism was wrong (see the correction
> note added to `experiments/20260717-round90-pati-salam-gauge-
> completeness/decision.md`); each Pati-Salam multiplet already has an
> EVEN (4) doublet count on its own, so Witten-anomaly parity was never the
> right quantity to check for "why both sectors." **This does NOT
> invalidate this experiment's own System-A-vs-System-B bookkeeping
> finding below**, which stands as an independent, still-valid result (two
> unreconciled fermion-counting schemes in this project) — but the SPECIFIC
> framing "checking SU(2)_R doublet parity for Witten-anomaly purposes" is
> superseded. The correct quantity to check, per the round90 correction, is
> the perturbative `SU(4)^3` cubic anomaly (or its `SU(3)_c`/`U(1)_{B-L}`
> descendants after symmetry breaking) — a DIFFERENT computation, not
> attempted here, pursued instead in round92.

**Date:** 2026-07-17
**Verdict:** `BLOCKED__ONLY_T-INDEXED_METHODOLOGY_GIVES_ODD_COUNT_BUT_FAILS_ITS_OWN_SU2L_CROSSCHECK__RIVAL_BOOKKEEPING_GIVES_EVEN_BUT_IS_NOT_ESTABLISHED_AS_APPLICABLE`

**Go/no-go:** This is a well-argued `BLOCKED`, not a forced `PASS` or `FAIL`.
This project contains exactly ONE bookkeeping system that is actually indexed
by the connection parameter `t` (the E9-E17 zero-mode-kernel chain), and
applying it gives `t=0` alone → **1 `SU(2)_R` doublet per triality channel,
3 total across channels — ODD**. But this same methodology, applied
identically to the `SU(2)_L`/`t=1` sector as a required consistency
cross-check, ALSO gives an odd count (3) — which contradicts the
independently well-established fact (external physics + this project's own
separate `G6` bookkeeping) that the real Standard Model's `SU(2)_L` doublet
content is EVEN (12, from 3 generations × 4 color/lepton doublets). A
counting methodology that gives a wrong answer on the one case where the
true answer is already known cannot be trusted to give a right answer on the
case where it is not. The rival bookkeeping that WOULD give a self-consistent
even count (`G6`'s pre-existing, color-carrying SM-content scheme) is not
established anywhere in this project as applying to the `t=0`/`t=1`
zero-mode split — this exact linkage is the reconciliation gap E12/E17
already flagged as open, now shown to have concrete consequences for THIS
specific question. **BLOCKED, per the pre-registered kill criterion.**

---

## 1. The only established `t`-indexed count: System A [VERIFIED-tool, reused + one direct group-theory inference]

`experiments/20260717-round91-su2r-doublet-parity-check/
e21_su2r_doublet_parity_count.py`, Parts 0-1, run this round
(`python e21_su2r_doublet_parity_count.py`):

- `dim ker(D_{S3,t}) = 2` — established for `t=0` unconditionally
  (`experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md:44-62`)
  and for `t=1` under `c0=-2` only (`CONVENTION_TABLE.md` row 5,
  `experiments/20260717-round76-e9followup-right-invariant-frame/
  decision.md:129-168`); reused as a fixed total by
  `experiments/20260717-round78-e12-multiplicity-gate/decision.md:12-18`
  ("Section D — total count").
- `dim ker(D_{S6,twisted}) = 1` EXACTLY, per triality channel —
  `experiments/20260621-g74a-lichnerowicz-gap/decision.md:57-66` (Lemma B:
  "`G₂`-rep content of `S⁻`: exactly one `G₂`-singlet per triality channel →
  `dim ker ≤ 1` per channel"), combined with `G73`'s `ind=1` (`≥1`) to give
  `=1` exactly (`decision.md:68-75`, "Combined conclusion"). **Provenance
  note, reused verbatim from this project's own correction:** `G74A`'s file
  itself now carries a 2026-07-17 superseded-note stating its ORIGINAL two
  lemmas are insufficient as literally stated, but "the `dim ker=1` NUMBER
  this file concludes is still correct... established by later, independent
  work (`experiments/20260708-dolan-casimir-g2su3` +
  `experiments/20260714-round59-trivial-rank-certification`)" — this round
  cites the NUMBER, correctly attributed, not the superseded lemma-derivation.
- **3 independent triality channels** — `experiments/20260621-g67-octonion-
  triality/decision.md:11-19` (`8_v`, `8_s`, `8_c`, related by `Z3` outer
  automorphism, identical `c₃=2` each); reused by `experiments/20260621-g73-
  three-channel-dirac/decision.md:8-9,20-21` ("Three channels (G67) →
  `N_gen=3×1=3`").
- **The 2-dim joint kernel per channel is one doublet, not two copies** —
  `experiments/20260717-round83-joint-representation-decomposition/
  decision.md:26-30` (bottom line) and the criteria table (`decision.md:193-
  204`): `PASS__ONE_WEAK_ISOSPIN_DOUBLET__NARROW_SCOPE`, tool-verified via
  `e16_joint_representation_check.py` (different `T3` eigenvalues, same
  S6-side/channel/B-L-type quantum numbers on both basis vectors).

**Direct group-theory consequence, drawn this round [INFERRED — standard
representation-theory fact, not independently re-derived by a new tool
computation]:** `G74A` Lemma B's "`G₂`-singlet" characterization of the
1-dim kernel has an immediate consequence: since `SU(3)_c ⊂ G₂` (`S⁶=G₂/
SU(3)`, established by `G9`), a vector invariant under the FULL `G₂` action
is automatically invariant under the SU(3) subgroup too — i.e. this
1-dimensional zero mode is an **`SU(3)_c`-SINGLET** (colorless). This means
**System A's per-channel content carries NO internal color multiplicity at
all** — there is no "3 colors" factor hiding inside `dim ker=1`; it is
literally one complex dimension, full stop.

**Count:** `t=0`'s joint-kernel dimension per channel = `2×1=2` → **1
`SU(2)_R` doublet per channel**. Across `3` channels: **3 total — ODD**.

`preprint.tex:317` ("All four conditions are satisfied with each generation
separately anomaly-free; no inter-generation cancellation is required") is
this project's OWN stated convention for how anomaly-type conditions are
checked in this framework — per generation, not summed. Under that
convention the relevant number is **1 per generation, itself already odd** —
aggregating across 3 generations does not change the parity finding either
way (`3` is odd regardless of whether checked per-channel or summed).

---

## 2. Cross-check: does the SAME methodology give the right answer for `SU(2)_L`? [VERIFIED-tool, this round's script Part 2 — decisive negative]

Per the task's own instruction (point 3) and this round's pre-registered
kill criterion, the identical System-A methodology was applied to the
`t=1`/`SU(2)_L` sector: `dim ker(D_{S3,t=1})=2` (same source as above, under
`c0=-2`), tensored with the SAME 1-dim, colorless, per-channel `S⁶`-twisted
kernel (the decoupling assumption `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²`,
E2/E12, means the `S⁶` factor does not depend on `t` at all — the identical
1-dim kernel tensors with either `t`-sector's 2-dim S3 kernel). Result: **1
`SU(2)_L` doublet per channel, 3 total — ODD.**

**This is independently known to be the WRONG answer.** The real Standard
Model's `SU(2)_L` doublet content is well-established, externally, to be
EVEN: 3 generations × (3 color quark doublets `(u,d)_L` + 1 lepton doublet
`(ν,e)_L`) = 3×4=12. This project's OWN separate bookkeeping
(`g6_spinor_decomposition.py`, `SM_TABLE` dict lines 134-153, and
`preprint.tex:289-298`'s "Standard Model fermion content for one
generation" section) reproduces this SAME even, color-explicit structure —
it is not merely a textbook fact imported from outside, it is this
project's own stated target for what "one generation" should contain.

**Consequence [VERIFIED-tool, this round's script `verdict` dict,
`system_A_su2L_crosscheck_matches_known_truth = False`]:** System A's
counting methodology (`dim ker=1`/channel, colorless, no multiplicity)
systematically UNDER-COUNTS relative to what "one generation's worth of
`SU(2)`-doublet matter" is independently known to require. It fails this
project's own pre-registered kill criterion. **A methodology that gives a
demonstrably wrong parity on the one case where the true answer is already
known (`SU(2)_L`) cannot be trusted to certify a right parity on the case
where it is not (`SU(2)_R`).**

---

## 3. Why System A under-counts: it is not the same object as "one generation" [DOCS + CODE, this round's synthesis of already-established facts]

Two genuinely distinct bookkeeping systems coexist in this project, and this
round's cross-check failure traces directly to conflating them:

- **System A** (E9-E17): a **topological zero-mode count** of a specific
  twisted Dirac operator. Its "1 per channel" is an index/kernel dimension,
  established to be a `G₂`/`SU(3)`-singlet (Section 1). It says nothing
  about, and structurally cannot represent, quark color content — it is a
  single colorless mode.
- **System B** (`g6_spinor_decomposition.py`, dated 2026-06-15 — **predates
  the entire `t`-parameter torsion-escape-route program**, which E2/round67
  introduces no earlier than 2026-06-22): the FULL, un-twisted, 4-component
  S3 Dirac spinor (`s3_states`, lines 29-36) tensored with the FULL 8-
  component S6 Dirac spinor (`s6_states`, built from `su3_label()`/
  `bl_charge()`, lines 40-102), explicitly carrying color (3-fold) and
  lepton (1-fold) structure. `g6_spinor_decomposition.py` has **no `t`
  variable anywhere in the file** — it is agnostic to which (if any)
  torsion-deformed operator's zero modes it is meant to describe.

`experiments/20260717-round85-e17-sector-coexistence-gate/decision.md:96-
152` (Section 2) already tool-verified that System B's 4 `s3_states` map
EXACTLY onto the union `{ker D^{t=0}} ∪ {ker D^{t=1}}` (2+2=4) — i.e. each
INDIVIDUAL `t`-sector supplies HALF of System B's s3-side content. But
`experiments/20260717-round78-e12-multiplicity-gate/decision.md:110-128`
(Section E.2) and E17's own Section 2 (`decision.md:137-152`) BOTH
explicitly flag, as still open, whether System B's SEPARATE, color-carrying
8-state `S⁶`-side bookkeeping is even the correct target for the
torsion-escape-route's `S⁶`-side zero-mode construction (System A's `dim
ker=1`, `G74A`) to match — "two logically separate bookkeeping exercises
this project has never reconciled" (E17 `decision.md:144`, reused verbatim).

**This round's contribution:** this exact, previously somewhat abstractly-
stated reconciliation gap is what DIRECTLY blocks the SU(2)_R-doublet-parity
question. It is not an aesthetic tidying-up issue — it has concrete teeth
here: System A (the only bookkeeping actually tied to `t`) gives an
answer that is independently falsifiable via the `SU(2)_L` cross-check and
fails; System B (the only bookkeeping that would give a self-consistent,
even, SM-matching answer) is not established as applying to `t` at all.

For completeness, this round's script Part 3 computes what System B WOULD
give if (unestablished) it could stand in for System A: `t=0`'s
`chir_s3="-"` states (`g6_spinor_decomposition.py:34-35`, `T3L=0,T3R=±1/2`
— matching `SU(2)_R` doublet content under Convention A, per the docstring
lines 9-10 and `CONVENTION_TABLE.md` row 6/E17 Section 1's labeling),
tensored with all 8 `s6_states`, gives 8 doublets per generation counting
particle+CPT-conjugate content separately (`preprint.tex:296-298`, "32 =
one generation... plus their CPT conjugates"; E13/round79 established this
CPT-doubling is carried entirely by the S6 factor's B-L sign) or 4 doublets
per generation counting only independent degrees of freedom. Both give EVEN
totals across 3 channels (24 or 12 respectively) — but, per the paragraph
above, this substitution is exactly the move this project's own text has
never licensed.

---

## Applying the pre-registered criteria

| Criterion | Finding |
|---|---|
| Does the ONLY `t`-indexed bookkeeping (System A) give a determinate parity for `t=0`'s `SU(2)_R` doublet count? | **YES, mechanically — 1/channel, 3 total, ODD** (Section 1) |
| Does that SAME methodology pass the required `SU(2)_L` self-consistency cross-check? | **NO — gives 3/ODD where the true, independently-known answer is 12/EVEN** (Section 2) — pre-registered kill criterion triggers |
| Is there a rival bookkeeping (System B) that WOULD give a self-consistent even count? | **YES (8 or 4 doublets/generation, both EVEN totals) — but its applicability to the `t=0`/`t=1` split is explicitly unestablished, per E12 Section E.2 / E17 Section 2** (Section 3) |
| Does this project's own text currently specify enough to determine, with confidence, whether `t=0`'s `SU(2)_R` doublet count is EVEN or ODD? | **NO** |

**PASS is not supported:** the pre-registered PASS criterion required the
System-A methodology to ALSO reproduce the known-true EVEN answer on the
`SU(2)_L` cross-check — it does not (Section 2).

**FAIL is not supported:** the count is not already even without `t=0`
under the only established `t`-indexed methodology (System A gives ODD, not
EVEN, with or without `t=0` specifically identified as the source) — and
`SU(2)_R` clearly does carry doublet content (Section 1's E16 citation), so
the "no doublet content at all" FAIL disjunct also does not apply.

**BLOCKED is the honest verdict**, exactly per the pre-registered kill
criterion: the one methodology directly tied to `t` fails its own
consistency check, and the methodology that would pass is not established
to apply to `t` at all.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the possibility of directly promoting round90's
  Relaxation-Map item ("check whether the narrower `SU(2)_R`-only
  Witten-anomaly argument suffices... using ONLY this project's own
  already-established fermion content") to a clean PASS. It specifically
  kills the naive move of reading `G74A`'s `dim ker=1`/channel as "one full
  generation's worth of `SU(2)_R`-doublet matter" — Section 2's cross-check
  shows this reading is demonstrably too coarse (fails on the case with a
  known-true answer).
- **What this result does NOT kill:** round90's own finding that `SU(2)_R`
  is genuinely gauged (Section 1 of round90, untouched, reused here); E16's
  `PASS` (the 2-dim joint kernel per channel IS one doublet, not two copies
  — this round's Section 1 reuses, not challenges, that finding); the
  possibility that a FUTURE, explicit reconciliation of System A and System
  B (the open item E12/E17 already flagged) could resolve this cleanly in
  either direction — this round does not attempt that reconciliation, only
  shows precisely where it is needed and why skipping it is not safe.
- **What survives, confirmed stronger than before:** the previously somewhat
  abstract-sounding "System A/System B not reconciled" gap (E12 Section E.2,
  E17 Section 2) is now shown to have a CONCRETE, falsifiable consequence:
  it is the specific reason round90's cheapest-next-step Relaxation-Map item
  cannot currently be closed. This narrows future work from "reconcile the
  bookkeeping systems in general" to the sharper, motivated question:
  "does `G74A`'s 1-dim, colorless zero mode represent ONE full SM
  multiplet's worth of matter (lepton-only, per its singlet character), or
  is it a topological placeholder standing in for a richer, yet-unbuilt
  physical spectrum that a real parent action would need to supply?" —
  precisely the kind of question KT-1/E18's missing-parent-action gap
  already names as the root issue.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Explicitly reconcile System A and System B | State, and justify, exactly how `G74A`'s 1-dim colorless `S⁶`-twisted kernel relates to `G6`'s 8-state, color-explicit `S⁶` bookkeeping — e.g. is the twisted kernel meant to be tensored with a further, not-yet-constructed color/family structure, or is "one channel = one generation" meant literally as a single colorless lepton-like mode? Neither is stated anywhere in this project. |
| Supply the missing parent action (KT-1/E18, reused) | Still the deepest form of the same gap: a stated 13D Lagrangian would fix how many independent fields exist and how they carry color/generation indices, which is exactly what is missing here. |
| Directly test whether `G74A`'s zero mode is meant to be a lepton (colorless) or must be embedded in a larger color-carrying multiplet | Would require an explicit statement (not found anywhere in this project) of how `dim ker(D_{S6,twisted})=1` per channel is supposed to reproduce a full generation's quark content, given that Section 1 shows it is manifestly an `SU(3)_c` singlet. |
| Re-run this exact cross-check once/if the reconciliation above is resolved | If a future round establishes System B (or an amended version of it) IS the correct target, re-apply this round's Part 1/2 counting using the reconciled numbers — the script here is directly reusable for that. |

## Assumptions carried, unresolved

- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption) — presupposed throughout, exactly as every reused experiment
  presupposes it.
- `SU(2)_L`=left-translation (Convention A, `CONVENTION_TABLE.md` row 6) —
  adopted per round90/E17's own citation; the qualitative "never two
  copies of the same piece" finding is convention-independent (E17 Section
  1), so this choice does not affect which methodology fails the
  cross-check, only which sector is labeled `L` vs `R`.
- `t=1`'s kernel exists only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged; the cross-check in Section 2 inherits this
  caveat exactly as E12/E17 do.
- The `G74A`→`dolan-casimir-g2su3`/`round59` provenance correction (the
  `dim ker=1` NUMBER, not the original two lemmas) — reused per the
  project's own 2026-07-17 correction note; not independently re-verified
  by reading the (390KB, over this session's file-size limit)
  `dolan-casimir-g2su3/decision.md` directly this round. This is a genuine
  gap in this round's own verification: the specific NUMBER (`dim ker=1`)
  was reused from `G74A`'s own already-superseded-but-number-preserved
  citation trail, not independently re-confirmed against the newer file's
  full text this round.

## What this does NOT mean

1. Does **not** overturn round90 (E21)'s own `BLOCKED` finding, or its
   positive sub-finding that `SU(2)_R` is genuinely gauged — this round
   supplies a MORE SPECIFIC reason the narrower Relaxation-Map item cannot
   yet be closed, consistent with (not contradicting) round90's own verdict.
2. Does **not** resolve E17 (round85)'s own coexistence `BLOCKED` (whether
   `t=0` and `t=1` are ever simultaneously physically realized) — untouched;
   if anything, this round shows that even IF coexistence were established,
   the doublet-PARITY argument for why it would be needed is itself not yet
   determinate.
3. Does **not** claim `G74A`'s `dim ker=1` result, or E16's doublet-PASS
   finding, is wrong — both are reused here exactly as established; this
   round's finding is about what `dim ker=1` licenses concluding about
   FULL-generation multiplicity, not about the number itself.
4. Does **not** affect this project's `N_gen=3` headline claim (the
   independently-established `G73`/`G74A`/`G74B` `S⁶`-only triality/index/
   chirality chain) — this round concerns only the separate, already-
   non-load-bearing `S³`-side torsion-escape-route program.
5. Does **not** claim the real Standard Model's `SU(2)_L` anomaly-freedom is
   in doubt — that is a well-established external fact, used here purely as
   a known-true reference point to stress-test this project's OWN counting
   methodology, not as a claim requiring independent verification this
   round.
6. Does **not** re-derive or challenge Witten's 1982 `SU(2)` global-anomaly
   theorem itself, or round90's bibliographic sourcing of it — reused here
   purely by citation.
7. Nothing in this experiment was submitted, posted, or sent anywhere
   external; this project's standing rules (no arXiv submission, no contact
   with Tom Lawrence, `lambda=FREE_COUPLING_PARAMETER`,
   `safe_for_runtime=False`) are unaffected and were not approached.

## Pearl-registry candidate

**Observation, concrete enough to flag:** a topological zero-mode COUNT
(index-theorem `dim ker`) and a PHYSICAL MULTIPLICITY count (how many
color/family copies of an SM-type multiplet exist) are logically distinct
quantities that can trivially disagree in magnitude — and this project's own
two bookkeeping systems (System A: topological, colorless, dim=1/channel;
System B: physical, color-explicit, dim=8/generation) are a clean, concrete
instance of exactly this distinction, previously only flagged in the
abstract (E12 Section E.2). **Falsifiable prediction, if pursued:** any
future attempt to use a Dirac-index/kernel-dimension result from this
project's `S⁶`-side constructions (`G73`/`G74A`/`G74B` or successors) to
answer an anomaly-cancellation or multiplicity question should FIRST check
whether the object in question is a `G2`/`SU(3)`-singlet (as `G74A`
establishes it is here) before assuming it carries the color/family
structure a full physical generation would need. **Impact score ~4** (narrow
to this project's own `S⁶`-side index-theorem outputs and any future round
that tries to read physical multiplicity directly off a topological index;
not registered to the global `pearl_registry/INDEX.md` — project-internal).
`next_check`: before any future round attempts a full anomaly-cancellation
check using this project's `S⁶`-side twisted-kernel content specifically
(as opposed to `G6`'s separate SM-content table), re-verify whether System A
and System B have been reconciled in the interim; if not, this same
BLOCKED reasoning applies.

## Check (reproduces this decision)

```
cd experiments/20260717-round91-su2r-doublet-parity-check
python e21_su2r_doublet_parity_count.py
```

Expect (from the script's own `verdict` dict, printed at the end):
`system_A_doublets_from_t0_total=3` (ODD), `system_A_su2L_crosscheck_total=3`
(ODD), `system_A_su2L_crosscheck_matches_known_truth=False`,
`system_B_doublets_incl_cpt_total=24` (EVEN),
`system_B_doublets_excl_cpt_total=12` (EVEN),
`system_A_and_system_B_reconciled_in_project_text=False`. Every source
number used by the script is cited in a comment immediately above its
assignment, tracing to a specific prior experiment's `decision.md` or to
`g6_spinor_decomposition.py`/`preprint.tex`, each independently `Read` this
round (not from memory or paraphrase) at the line ranges cited in Sections
1-3 above.
