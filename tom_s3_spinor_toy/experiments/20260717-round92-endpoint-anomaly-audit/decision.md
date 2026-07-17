# E22 (round92) — Decision

**Date:** 2026-07-17
**Verdict:** `BLOCKED__U1Y-MIXED_ANOMALY_CONDITIONS_NOT_COMPUTABLE_BL_VALUE_OF_TWISTED_S6_KERNEL_UNESTABLISHED__SU3C_CUBED_CONDITION_COMPUTABLE_BUT_SHOWS_NO_FORCING__WITTEN_PARITY_COMPUTABLE_BUT_SHOWS_NO_UNION_CANCELLATION`

**Go/no-go:** This experiment reaches Step 2 (representation assignment)
cleanly for `SU(3)_c` — a first-principles group-theoretic derivation from
this project's own already-established facts shows BOTH endpoint kernels are
`SU(3)_c` SINGLETS. It does **not** reach Step 3 cleanly for the three
`U(1)_Y`-dependent anomaly conditions (`[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`,
`[grav]^2 U(1)_Y`) required by the task's own methodology, because this
project's text has never assigned a numeric `B-L`/hypercharge value to the
specific twisted S⁶-kernel object that carries System A's zero modes — a
gap explicitly flagged already by round83/E16, reconfirmed here, and
sharpened by a further, previously-unremarked finding this round: `preprint.tex`
itself carries **two distinct, unreconciled hypercharge formulas**
(`Y=K_3+(B{-}L)/2`, S⁶-side, used in the paper's own verified anomaly check;
`Y=T_{3R}+(B{-}L)/2`, S³-side, used only in the self-flagged-illustrative
Weinberg-angle section), neither of which is stated to apply to, or has ever
been evaluated on, System A's specific endpoint content. The ONE anomaly
condition that IS fully computable (`[SU(3)_c]^3`) shows **no forcing**: both
endpoints are already anomaly-free alone (singlet ⇒ zero cubic coefficient),
so there is nothing for the union to fix on that channel. The Witten
`SU(2)_L`/`SU(2)_R` parity computation (fully computable, reusing round91) is
similarly non-forcing: each endpoint is a total singlet under the OTHER `SU(2)`
factor, so the union changes neither factor's parity at all. **BLOCKED is the
honest verdict, precisely naming the missing assignment (numeric `B-L`/`Y`
for the twisted S⁶-kernel) as required by the pre-registered criterion** —
neither PASS (which needs the mixed conditions computed and forcing) nor a
clean FAIL (which would require the WHOLE test, not just one channel, to show
no forcing, or the endpoints to be identical) is supported.

---

## 1. Frozen `G_eff`, reconfirmed [VERIFIED-tool: direct `Read` this round]

Per `claim.md` Section 2, `G_eff = SU(3)_c×SU(2)_L×SU(2)_R` (Option (i)) was
chosen irrevocably before any computation. Re-reading `preprint.tex:280-285`
and `:420-424` directly this round (not trusting round90's paraphrase alone)
confirms the reasoning: "an internal check (gate G97, this work) finds no
`SU(4)` subgroup in `Iso(S³×S⁶)`" (`:283`) and "an internal check of the
isometry group `Iso(S³×S⁶)=SO(4)×SO(7)` (gate G97, this work) finds that
`SU(4)` itself is not present among the isometries at all — only
`SU(3)×SU(2)_L×SU(2)_R`... is realized this way" (`:421-424`). This choice
was **not** revisited after computing anomaly coefficients below.

---

## 2. Step 1 — Kernel content [VERIFIED-tool + DOCS, reused verbatim]

Reusing, not re-deriving (per `claim.md` Section 3 step 1):

- `dim ker(D_{S3,t=0})=2` unconditionally
  (`experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md:44-62`);
  `dim ker(D_{S3,t=1})=2` under `c0=-2` only
  (`CONVENTION_TABLE.md` row 5, `experiments/20260717-round76-e9followup-
  right-invariant-frame/decision.md:129-168`); both reused as a fixed total
  by `experiments/20260717-round78-e12-multiplicity-gate/decision.md:12-18`.
- `dim ker(D_{S6,twisted})=1` per triality channel — re-read this round
  directly at the CURRENT, authoritative source, `preprint.tex:806-831`
  (not the now-superseded `G74A` Schur's-lemma argument): "The trivial `G_2`-
  representation `(0,0)` appears with multiplicity `2` in `S^+⊗S^-`...
  `D^+` restricts to a linear map `D^+|_1: C^2→C^1`... `rank(D^+|_1)=1`...
  (internal verification, experiments `20260708-dolan-casimir-g2su3` and
  `20260714-round59-trivial-rank-certification`, this work). The result
  carries three mutually reinforcing certifications" (`:806-831`). This
  supersedes `G74A`'s own original "Schur's lemma pins `dim ker≤1`"
  argument, which `preprint.tex:815-819` itself now says is insufficient
  ("Schur's lemma only forces `D^+|_1` to be *some* linear map on this
  2-dimensional space — it does not fix which one"). The NUMBER (`dim
  ker=1`) is unaffected by this correction; only the derivation route
  changed, exactly as this project's own 2026-07-17 provenance note (cited
  by round90/round91) records.
- `n_triality_channels=3` (`experiments/20260621-g67-octonion-triality/
  decision.md:11-19`).
- Representation under `SU(2)_L×SU(2)_R`, Convention A
  (`CONVENTION_TABLE.md` row 6, convention-independent up to an overall
  `L`↔`R` relabel per `experiments/20260717-round85-e17-sector-coexistence-
  gate/decision.md` Section 1): `t=0`↔`(1,2)` (`SU(2)_L` singlet, `SU(2)_R`
  doublet); `t=1`↔`(2,1)` (`SU(2)_L` doublet, `SU(2)_R` singlet). The 2-dim
  joint kernel per channel is confirmed ONE irreducible doublet, not two
  copies (`experiments/20260717-round83-joint-representation-decomposition/
  decision.md`, criteria table).

**Result: 1 doublet per channel, 3 total per endpoint (3 triality
channels), for each of `t=0` and `t=1` separately.** Script
`e22_endpoint_anomaly_audit.py` Part 1, reproduces this arithmetic.

---

## 3. Step 2 — `G_eff` representation assignment: `SU(3)_c` DERIVED, `U(1)_Y` NOT [VERIFIED-tool + honest gap]

### 3a. `SU(3)_c`: derivable from established facts, both endpoints SINGLET

Two already-established facts combine into a direct, first-principles
group-theoretic consequence:

1. `preprint.tex:440-441` (read directly this round): "The six-sphere `S^6`
   carries a transitive action of `G_2` with isotropy subgroup `SU(3)`,
   realizing `S^6` as the coset space `G_2/SU(3)`." → `SU(3)_c` is a
   SUBGROUP of `G_2`.
2. `preprint.tex:806-831` (Section 2 above): the `dim ker=1` zero mode lives
   inside the `G_2`-trivial isotypic component of `S^+⊗S^-` — a 2-dimensional
   space on which `G_2` acts as the IDENTITY operator (multiplicity-2 trivial
   representation, `preprint.tex:806`, "The trivial `G_2`-representation
   `(0,0)` appears with multiplicity `2`"). Since `G_2` acts trivially
   (pointwise-fixed) on the FULL 2-dim ambient space, ANY subspace of it —
   including whichever specific 1-dim subspace the later rank-1 computation
   identifies as the actual kernel — is automatically ALSO fixed pointwise
   by `G_2`, regardless of which specific subspace it turns out to be.

**[INFERRED — standard restriction-of-trivial-representation argument: a
subgroup of a group acting trivially also acts trivially. Not an independent
new tool computation, but a direct consequence of two already-established,
directly re-read facts. Reuses the identical inference already used by
round91 (`decision.md` Section 1, "Direct group-theory consequence"),
independently re-verified this round by reading `preprint.tex:440-441` and
`:806-831` directly rather than trusting round91's paraphrase alone.]**

**Conclusion: the `dim ker=1` per-channel S⁶-side zero mode is an `SU(3)_c`
SINGLET, for BOTH `t=0` and `t=1`** — the S⁶ factor is `t`-independent under
the decoupling assumption `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12,
reused throughout E9-E21), so the SAME colorless S⁶-side kernel tensors with
either endpoint's S³-side content. **System A's content carries NO internal
color multiplicity at all**, confirming and independently re-deriving
round91's identical finding (`decision.md` Section 1).

### 3b. `U(1)_Y`/`B-L`: NOT derivable — a genuine, honestly-flagged gap

Unlike `SU(3)_c` (a pure subgroup-invariance fact, needing no numeric weight
data), assigning a `B-L`/hypercharge VALUE requires locating the specific
1-dim kernel vector within a numerically-labeled weight space — and this has
never been done in this project for the twisted kernel specifically. Two
independent problems compound this gap, one already known, one newly
surfaced this round:

**(i) Already flagged (reused, not re-derived):**
`experiments/20260717-round83-joint-representation-decomposition/
decision.md`, "Assumptions carried, unresolved," item 3 (quoted verbatim):
"No explicit numeric B-L/SU(3)-representation value has ever been assigned
in this project to the twisted `S⁻` kernel object specifically (as opposed
to G6's untwisted 8-weight bookkeeping)." `g6_spinor_decomposition.py`'s
`bl_charge()` function (lines 40-69, read directly this round) is a function
of an S⁶ WEIGHT VECTOR `(±1/2,±1/2,±1/2)` in the UNTWISTED 8-state
decomposition (`s6_states`, built at lines 108-121 from `all_weights`,
line 106) — it has never been evaluated on, or connected to, the specific
`G_2`-singlet vector that is the actual `dim ker(D_{S6,twisted})=1`
zero mode (a state of a DIFFERENT operator, `D_{S6,twisted}`, not G6's plain
weight-space operator). There is no stated map from "which 1-dim subspace of
the `G_2`-trivial isotypic component is the twisted kernel" to "which of
G6's 8 weight-labeled states (if any) it corresponds to."

**(ii) New this round — two distinct, unreconciled `Y`-formulas in
`preprint.tex` itself [VERIFIED-tool: direct `Read`]:**

| | Formula | Where used | Status |
|---|---|---|---|
| (a) | `Y = K_3 + (B{-}L)/2` | `preprint.tex:302`, `304-305`: `K_3` is "a `U(1)` quantum number from the `SU(3)`-harmonic decomposition of `S^6`" (an S⁶-SIDE quantity) | Used in the paper's OWN verified anomaly-cancellation computation, `preprint.tex:309-320` ("passes all gauge anomaly conditions per generation, verified symbolically") |
| (b) | `Y = T_{3R} + (B{-}L)/2` | `preprint.tex:408` (an S³-SIDE quantity — `T_{3R}` is exactly the quantum number E16/E17 use to label the `t=0`/`t=1` kernels) | Used ONLY in `§`Weinberg-angle-estimate, which `preprint.tex:420-431` itself calls: "The Weinberg-angle estimate above should accordingly be read as illustrative pending this input, not as a computation with a well-defined completion path" |

`preprint.tex` never states these two formulas are equal, or which one
governs the twisted-kernel/System-A content specifically. Confirmed by
direct `Read` of `g6_spinor_decomposition.py:20,163` this round: G6's own
script uses formula (b) (`Y = T3R + BL/2`), matching the Weinberg-section
formula — **not** the formula actually used in the paper's own verified
anomaly check (a). Round90's own decision.md (Section 4, "the electric-
charge formula uses `T3R` via `Y=T3R+(B-L)/2`, `preprint.tex:408`") cited
ONLY formula (b) and did not flag that a SEPARATE, differently-defined `Y`
formula (a) is the one actually used in the paper's own verified anomaly
computation — this is a genuine, previously-unremarked ambiguity this round
surfaces, not a re-litigation of round90's own (narrower, correctly-scoped)
citation.

**Even setting the formula-choice ambiguity aside**: formula (b)
(`Y=T3R+(B-L)/2`) is the more natural candidate for System A specifically,
since `T3R` is directly available for System A's endpoints (`0` or `±1/2`,
per E16/E17's own `T3` computation) — but this STILL requires a numeric
`B-L` value for the twisted S⁶-kernel, which (i) shows is not established.

**Conclusion for Step 2: `SU(3)_c` assignment is DERIVED (singlet, both
endpoints); `U(1)_Y`/`B-L` assignment is NOT DERIVABLE from anything this
project has established.** Script Part 2 encodes exactly this asymmetry
(`su3_derivation_is_established=True`,
`bl_value_of_s6_twisted_kernel_computable=False`).

---

## 4. Step 3 — Anomaly coefficients for `G_eff`'s generators [VERIFIED-tool: script Part 3]

- **`[SU(3)_c]^3`** — COMPUTABLE, using only the Step 2a `SU(3)_c`-singlet
  derivation (a representation-theoretic fact, needing no numeric weight
  data: the cubic anomaly/Dynkin coefficient of an `SU(3)` singlet is
  identically `0`, since a singlet contributes nothing to any `SU(3)` trace).
  Script result: `A([SU(3)_c]^3, t0_alone)=0`, `A([SU(3)_c]^3, t1_alone)=0`,
  `A([SU(3)_c]^3, union)=0`. **Both endpoints are ALREADY anomaly-free alone
  on this channel — there is nothing for the union to fix.** This is the
  FAIL disjunct ("each endpoint is separately anomaly-free already, no
  forcing"), for this ONE specific anomaly channel.
- **`[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`, `[grav]^2 U(1)_Y`** — NOT
  COMPUTABLE, per Section 3b: all three require the numeric `B-L`/`Y` value
  of the twisted S⁶-kernel, which is not established anywhere in this
  project. Script Part 3 explicitly marks these `NOT COMPUTABLE` rather than
  substituting an imported Standard Model value or a guess.

**This means 3 of the 4 anomaly conditions the task's own methodology
requires cannot be evaluated at all** — the pre-registered PASS bar ("across
the anomaly conditions that can be computed... `anomaly(t=0 alone)≠0`,
`anomaly(t=1 alone)≠0`, `anomaly(union)=0`") cannot be checked for the
majority of the required conditions, and the one condition that CAN be
checked shows no forcing.

---

## 5. Step 4/5 — Witten `SU(2)` parity, endpoint alone and union [VERIFIED-tool: script Part 4, reusing round91]

Reusing round91's already tool-verified counts
(`experiments/20260717-round91-su2r-doublet-parity-check/
e21_su2r_doublet_parity_count.py` verdict dict, re-confirmed by this round's
own script Part 4, independently re-run):

| Group | `t=0` alone | `t=1` alone | Union |
|---|---|---|---|
| `SU(2)_R` doublets | 3 (ODD) | 0 (EVEN — `t=1` is an `SU(2)_R` singlet) | 3 (ODD) |
| `SU(2)_L` doublets | 0 (EVEN — `t=0` is an `SU(2)_L` singlet) | 3 (ODD) | 3 (ODD) |

**Since each endpoint is a TOTAL SINGLET under the OTHER `SU(2)` factor
(Section 2's representation table), the union changes NEITHER factor's
parity at all** — `SU(2)_R`'s count is supplied entirely by `t=0` (unchanged
by adding `t=1`, which contributes 0); `SU(2)_L`'s count is supplied entirely
by `t=1` (unchanged by adding `t=0`). There is no cross-endpoint parity
cancellation available for this quantity, for either factor — a clean,
computable, NEGATIVE result. This is consistent with, and independently
reinforces from a different angle, round90's own correction (the ⚠️ note at
the top of `experiments/20260717-round90-pati-salam-gauge-completeness/
decision.md`) that Witten `SU(2)` parity was never the right forcing
mechanism for "why both sectors are needed" — this round shows concretely
that the union does not even supply a parity cancellation for the two `SU(2)`
factors it actually contains, reinforcing (not merely repeating) that
correction from the endpoint-anomaly angle specifically.

Per round90's own correction, this Witten-parity computation checks a
DIFFERENT quantity from the perturbative anomalies of Section 4 above — both
are reported here without conflating them, per `claim.md` Section 3 step 4's
own instruction.

---

## 6. Applying the pre-registered criteria (`claim.md` Section 4)

| Criterion | Finding |
|---|---|
| Can Step 1 (kernel content) be completed by citation alone? | **YES** — Section 2, fully reused |
| Can Step 2 (`G_eff` representation assignment) be completed for `SU(3)_c`? | **YES, DERIVED** — Section 3a: both endpoints `SU(3)_c` singlets, from `SU(3)⊂G_2` + the kernel's `G_2`-triviality |
| Can Step 2 be completed for `U(1)_Y`/`B-L`? | **NO** — Section 3b: no numeric `B-L` value has ever been assigned to the twisted S⁶-kernel; compounded by a newly-surfaced, unreconciled dual-`Y`-formula ambiguity in `preprint.tex` itself |
| Can Step 3 (`[SU(3)_c]^3`) be computed? | **YES** — Section 4: trivially `0` for both endpoints and the union (singlet content) — shows NO forcing |
| Can Step 3 (`[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`, `[grav]^2 U(1)_Y`) be computed? | **NO** — Section 4: blocked on the same `B-L`/`Y` gap as Step 2 |
| Can Step 4 (Witten parity) be computed? | **YES** — Section 5: computable for both `SU(2)_L` and `SU(2)_R`, both endpoints, and the union — shows NO cross-endpoint cancellation for either factor |

**PASS is not supported:** PASS requires `anomaly(t=0 alone)≠0`,
`anomaly(t=1 alone)≠0`, `anomaly(union)=0` across the anomaly conditions
that can be computed — but 3 of 4 required conditions cannot be computed at
all (Section 4), and the one that can be computed shows both endpoints
ALREADY zero (not `≠0`), the opposite of what PASS needs.

**FAIL is not supported as an OVERALL verdict**, despite one specific
channel (`[SU(3)_c]^3`) matching FAIL's "no forcing" disjunct exactly: FAIL,
as pre-registered, describes the outcome of the WHOLE test (`claim.md`
Section 4), and the majority of the required anomaly conditions cannot be
evaluated at all (BLOCKED disjunct), not merely evaluated-and-found-
non-forcing. Declaring an overall FAIL from one computable channel while
silently treating the other three as "presumably also non-forcing" would be
exactly the kind of unverified extrapolation this project's own
`audit-verification-gate` discipline exists to prevent. The two endpoints
also do NOT give identical representations (`(1,2)` vs `(2,1)`, genuinely
different under `SU(2)_L×SU(2)_R`) — so FAIL's other disjunct ("both
endpoints give the identical representation") does not apply either.

**BLOCKED is the honest verdict**, per the pre-registered criterion's first
disjunct exactly as worded: "the endpoint kernels' representations under
`G_eff` cannot be determined from what this project has already
established" — specifically, the `U(1)_Y`/`B-L` component of that
representation (not the `SU(3)_c` component, which IS determined) is
missing, and this missing piece blocks 3 of the 4 required anomaly
conditions. This is precisely the outcome `claim.md` Section 4's
pre-registered expectation anticipated before any computation was run.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the possibility that a clean, fully-computed
  PASS or FAIL verdict on the FULL set of task-specified anomaly conditions
  could be reached for the frozen `G_eff` using only this project's currently
  established text. It also kills, specifically, any temptation to read the
  `[SU(3)_c]^3` result (trivially zero, both endpoints) as evidence FOR a
  forcing pattern — it is direct evidence AGAINST one, on that channel.
- **What this result does NOT kill:** round90/round91's own findings
  (reused, unchanged); the possibility that a FUTURE, explicit assignment of
  a numeric `B-L`/hypercharge value to the twisted S⁶-kernel (resolving
  which of the two `Y`-formulas applies, and evaluating it on the actual
  `G_2`-singlet vector rather than G6's untwisted weight space) could close
  this specific gap and permit a genuine re-run of Steps 2-3; the
  `SU(3)_c`-singlet derivation itself (robust, confirmed independently this
  round by direct re-reading of `preprint.tex:440-441` and `:806-831`,
  not merely inherited from round91).
- **What survives, confirmed stronger than before:** round83's previously
  narrower-sounding caveat ("no explicit numeric B-L/SU(3)-representation
  value... assigned to the twisted S⁻ kernel object") is now shown to have
  a CONCRETE, specifically-locatable consequence for anomaly-cancellation
  testing (this experiment), and is compounded by a NEW, independently
  surfaced finding: `preprint.tex` itself carries two distinct, never-
  reconciled `Y`-formulas (S⁶-side `K_3`-based, used in its OWN verified
  anomaly check; S³-side `T_{3R}`-based, used only in a self-flagged-
  illustrative section) — narrowing future work from "assign a B-L value"
  (vague) to the sharper, two-part task: (a) decide which `Y`-formula
  governs System A's content (the `T_{3R}`-based one is the more natural
  candidate, since `T_{3R}` is directly available for `t=0`/`t=1`), and (b)
  locate the twisted kernel's actual numeric `B-L` charge within whatever
  weight-space formalism that formula requires.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Assign a numeric `B-L` value to the twisted S⁶-kernel | Locate the specific 1-dim `G_2`-singlet vector (established by `dolan-casimir-g2su3`/`round59`'s explicit computation) within a weight-labeled basis where `bl_charge()`-style assignment is meaningful — not attempted anywhere in this project |
| Reconcile `preprint.tex`'s two `Y`-formulas (`K_3`-based vs `T_{3R}`-based) | State explicitly whether `K_3` and `T_{3R}` are the same quantity under different names, or genuinely different, and which governs which sector — not stated anywhere in `preprint.tex` currently |
| Re-run this experiment's Step 3 once the above are resolved | The script here (`e22_endpoint_anomaly_audit.py`) is directly reusable — only Part 2's `bl_value_of_s6_twisted_kernel` and Part 3's mixed-`Y` conditions would need real numbers substituted for `None`/`NOT COMPUTABLE` |
| Resolve the System-A/System-B reconciliation gap (round91, reused) | A prerequisite for the above — if System B's color/B-L bookkeeping is ever shown to be the correct target for System A's twisted kernel, the `SU(3)_c`-SINGLET finding here (Section 3a) would need to be re-examined against that reconciliation, since System B assigns quarks (triplets), not just leptons (singlets) |

## Assumptions carried, unresolved

- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12's decoupling assumption) —
  presupposed throughout, exactly as every reused experiment presupposes it.
- `SU(2)_L`=left-translation (Convention A, `CONVENTION_TABLE.md` row 6) —
  the qualitative finding (each endpoint singlet under the OTHER `SU(2)`
  factor) is convention-independent (E17 Section 1), so this choice does
  not affect the BLOCKED verdict.
- `t=1`'s kernel exists only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged.
- The `dolan-casimir-g2su3`/`round59` `dim ker=1` computation itself was NOT
  independently re-verified this round (reused by citation only, exactly as
  round90/round91 also did not re-open it) — this experiment's `SU(3)_c`-
  singlet derivation depends on the ambient 2-dim space being correctly
  identified as the FULL `G_2`-trivial isotypic component (`preprint.tex:806`),
  which was read directly this round, but the specific rank-1 computation
  within it (`:825-831`) was reused, not re-run.
- Whether the System-A/System-B reconciliation (round91) would, if resolved
  in System B's favor, overturn the `SU(3)_c`-singlet finding here — flagged
  in the Relaxation Map, not resolved.

## What this does NOT mean

1. Does **not** establish PASS or FAIL for the task's own endpoint-anomaly
   question — BLOCKED, per Section 6.
2. Does **not** reopen or overturn round90 (E21)'s `BLOCKED` or round91
   (E21-followup)'s `BLOCKED` findings — this experiment reuses both by
   citation, and its own BLOCKED verdict is consistent with, not
   contradicting, either.
3. Does **not** claim the `SU(3)_c`-singlet finding (Section 3a) is somehow
   uncertain or provisional — it is a robust, directly re-verified
   group-theoretic consequence of two independently-confirmed
   `preprint.tex` facts, confirmed this round by direct `Read`, not merely
   inherited from round91's paraphrase.
4. Does **not** claim `preprint.tex`'s own anomaly-cancellation computation
   (`:309-320`, using `Y=K_3+(B-L)/2`) is wrong — only that it uses a
   DIFFERENT `Y`-formula and a DIFFERENT (untwisted, S6-harmonic) bookkeeping
   than what would be needed to check System A's specific `t=0`/`t=1`
   endpoint content, a distinction this project's text has never stated one
   way or the other.
5. Does **not** affect this project's `N_gen=3` headline claim, which rests
   on the independently-established `G73`/`G74A`/`G74B` `S⁶`-only
   triality/index/chirality chain — this experiment concerns only the
   separate, already-non-load-bearing `S³`-side torsion-escape-route
   program.
6. Does **not** re-derive or challenge any of E1-E21's own tool-verified
   results, or Witten's 1982 `SU(2)` global-anomaly theorem — all reused
   here purely by citation.
7. Does **not** claim the two-`Y`-formula finding (Section 3b(ii)) means
   `preprint.tex` contains an error requiring correction — only that, AS
   CURRENTLY WRITTEN, it does not state which formula governs which sector,
   a gap this experiment surfaces honestly rather than resolving by
   assumption.
8. Nothing in this experiment was submitted, posted, or sent anywhere
   external; this project's standing rules (no arXiv submission, no contact
   with Tom Lawrence, `lambda_v`/`lambda_np`=FREE_COUPLING_PARAMETER,
   `safe_for_runtime=False`) are unaffected and were not approached.
   No existing file was modified — only this new folder was created.

## Pearl-registry candidate

**Observation, concrete enough to flag:** `preprint.tex` carries two
distinct hypercharge formulas (`Y=K_3+(B-L)/2`, S⁶-harmonic-side, used in
the paper's own verified anomaly check at `:309-320`; `Y=T_{3R}+(B-L)/2`,
S³-side, used only in the self-flagged-illustrative Weinberg-angle section
at `:408`) that are never stated to be equal or to apply to the same
bookkeeping system — and this project's own concrete code artifact
(`g6_spinor_decomposition.py`) uses the SECOND (S³-side) formula, not the
first (the one actually used in the paper's verified anomaly-cancellation
computation). **Falsifiable prediction, if pursued:** any future attempt to
check anomaly cancellation for a SPECIFIC sub-content of this project's
fermion spectrum (as opposed to the full, already-verified 32-state "one
generation" package) must first determine which `Y`-formula applies to that
specific sub-content — assuming they agree without checking risks silently
importing the wrong hypercharge convention. **Impact score ~4** (narrow to
this project's own S³/S⁶ hypercharge bookkeeping and any future round that
tries to compute anomaly coefficients for a partial/sub-generation content
specifically; not registered to the global `pearl_registry/INDEX.md` —
project-internal, not cross-domain). `next_check`: before any future round
attempts a full anomaly-cancellation check using System A's specific
twisted-kernel content, re-verify whether the `K_3`/`T_{3R}` `Y`-formula
ambiguity has been resolved in the interim; if not, this same BLOCKED
reasoning applies to that channel too.

## Check (reproduces this decision)

```
cd experiments/20260717-round92-endpoint-anomaly-audit
python e22_endpoint_anomaly_audit.py
```

Expect (from the script's own `verdict` dict, printed at the end):
`su3_derivation_is_established=True`, `su3_rep_of_s6_kernel='SINGLET'`,
`bl_value_of_s6_twisted_kernel_computable=False`,
`y_formula_ambiguity_unreconciled=True`,
`A_SU3c_cubed_t0_alone=0`, `A_SU3c_cubed_t1_alone=0`,
`A_SU3c_cubed_union=0`, `su3c_cubed_forcing_pattern_present=False`,
`mixed_Y_conditions_computable=False`, `su2R_doublets_t0_alone=3`,
`su2R_doublets_union=3`, `su2L_doublets_t1_alone=3`,
`su2L_doublets_union=3`, `witten_parity_forcing_pattern_present=False`.
Every source number and citation is given in a comment immediately above its
assignment, tracing to a specific prior experiment's `decision.md`, or to
`preprint.tex`/`g6_spinor_decomposition.py`, each independently `Read` this
round (not from memory or paraphrase) at the exact line ranges cited in
Sections 1-5 above.
