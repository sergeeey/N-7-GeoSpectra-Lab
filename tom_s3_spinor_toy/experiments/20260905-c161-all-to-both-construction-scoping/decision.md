# C161 — Decision (convergent-mode, FL Full-Ladder)

**Date:** 2026-09-06
**Experiment:** `20260905-c161-all-to-both-construction-scoping`
**Question type (EstimandOps L0):** Descriptive — does a specific recombination of two
already-certified constructions derive a specific coefficient pair, or not. Explicitly
**not** causal, **not** predictive.
**Script:** `c161_lambda_recombination_scoping_check.py` (imports, does not modify,
`c136_joint_killing_spinor_check.py`) · **Results:** `results_c161.json`

## Verdict

```text
INCOMPLETE_MACHINERY_OR_ILL_POSED__CORRECTED_2026-09-06_AFTER_SKEPTIC_PASS
  __THE_MISSING_INGREDIENT_IS_NOT_THE_S6_TWISTED_OPERATOR__SECTION_1
  __READING_I_LAMBDA0_LAMBDA1_FORCED_ZERO_FOR_EVERY_FINITE_CHI4_CHI6
  __SO_THE_STILL_UNBUILT_S6_VALUE_IS_ALGEBRAICALLY_IRRELEVANT_TO_THAT_READING
  __READING_II_C136S_OWN_SS5_TABLE_HAS_FOUR_LITERAL_W0_W1_PAIRINGS__SECTION_2
  __ARITHMETIC_INDEPENDENTLY_RECONFIRMED_BY_SKEPTIC__CONFIRMED_REAL
  __THEY_SPAN_3_OF_5_ROWS_OF_CLAIM_MDS_OWN_KILL_CRITERION_TABLE
  __CHANNEL_AXIS_CONFIRMED_INERT_ACROSS_ALL_FOUR_PAIRINGS__CHECK_2A
  __BUT_SKEPTIC_FOUND_THE_VERDICT_LANGUAGE_ITSELF_TOO_OPTIMISTIC__SECTION_9
  __C133S_OWN_SS9_TEXT_CALLS_LAMBDA0_LAMBDA1_A_FREE_2_PARAMETER_CONTINUUM
  __A_HOM_SPACE_DIMENSION_COUNT_NOT_A_COMPUTED_SPECTRAL_QUANTITY
  __MAPPING_A_FREE_PARAMETER_ONTO_C136S_COMPUTED_ALPHA_EIGENVALUES_MAY_BE_A
  __TYPE_MISMATCH__NOT_MERELY_A_MISSING_SELECTION_RULE
  __PRACTICAL_UPSHOT_CORRECTED__DO_NOT_SPAWN_A_FUTURE_ROUND_TO_FIND_A
  __FRAME_SELECTION_PRINCIPLE__FIRST_AUDIT_WHETHER_THE_RECOMBINATION_ITSELF
  __WAS_EVER_A_LEGITIMATE_OPERATION__SECTION_9
  __STOPPING_HERE_EITHER_WAY__NOT_INVENTING_A_SELECTION_RULE
  __5_CHECKS_0_FAILURES
```

**One line.** C136's already-computed data does not need a new S6 twisted operator to
answer this file's question. Whether it CAN answer it at all is now itself in question
— C133's abstract `Φ = 1_F ⊗ (λ₀w₀ + λ₁w₁)` never states which of C136's two S3 frames
plays `w₀` versus `w₁` (four literal choices give three different verdicts), **and**,
per an independent skeptic pass (Section 9, added 2026-09-06), C133's own text treats
`λ₀,λ₁` as free moduli of an abstract `Hom`-space dimension count, not as spectral
eigenvalues of any operator — meaning the entire recombination may be a category error,
not merely an underdetermined one. Both readings stop this round from proceeding; they
differ only in what a *future* round should do next (see Section 9).

---

## Prior Result Gate — everything read from the primary this session

`claim.md` (full, this experiment) · `experiments/20260902-c136-joint-killing-spinor-
constraint/decision.md` (full) and `c136_joint_killing_spinor_check.py` (full) ·
`experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md` §§8–11 (lines
548–658, read this session) · `experiments/20260625-l3b-bundle-obstruction/decision.md`
(full) · `experiments/20260708-dolan-casimir-g2su3/decision.md` lines 200–300 (grepped
and read; file is 390.8 KB, too large to read whole — see §2 below for what this means
for the audit) · `experiments/20260714-round59-trivial-rank-certification/` (file list
only, not read in full — see §5). All `[VERIFIED-tool]` unless marked otherwise.

`git log --all -S"all->both"`, `-S"all_to_both"`, `-S"all→both"`, `-G"lambda_0.*lambda_1"`
run this session (claim.md item 3, marked `[ ]` there, now closed): hits confined to
C123–C137 pipeline commits, the C159 commit, and one status-report sync commit. **Zero
hits** combining `lambda_0` and `lambda_1` in the same commit anywhere in history. **The
specific recombination this file attempts has never been touched.** `ALREADY-KNOWN` is
therefore ruled out.

---

## 1. What C136 actually offers, and what claim.md's Intervention section pointed at

C136 leaves the S6 side `[UNKNOWN]` (its own §8 assumption 6: *"the twisted `S⁶`
operator was NOT built"*) but computes the **S3 side twice**, in two readings:

* **Reading (i)** — `c136_joint_killing_spinor_check.py:526-542` (`pairing_law_holds`),
  a single scalar `lambda = mu(t,ρ,frame) · χ₄ · χ₆` (D2). This is the only quantity in
  C136 with the same *scalar × channel/sector data* shape as C133's `Φ`.
* **Reading (ii)** — `c136_joint_killing_spinor_check.py:640-675` (`solve_cell`), the
  block-scalar `A = diag(0, α·1₃, β·1₆)` used to fill C136 §5's `3×2` table
  (`E_table_3x2`, `results_c136.json`). claim.md's own Intervention section names this
  table explicitly: *"the S3 half's alpha values ARE already computed in C136 SS5's 3x2
  table."*

Both are genuinely already built. Neither needs the S6 twisted operator to answer THIS
file's question — see §3.

---

## 2. Reading (i): the S6 value turns out to be algebraically irrelevant

`c136.mu_of(0.0, 1.0, +1)` (left-invariant frame, C136 check `C5`) and
`c136.mu_of(1.0, 1.0, -1)` (right-invariant frame, `C6`) are **both exactly `0`** —
reproduced here (`c161_lambda_recombination_scoping_check.py` §1, checks `1a`/`1b`),
not recomputed from scratch. This is not a numerical coincidence to verify against
tolerance; it is the literal *definition* of "parallel at that `(t,frame)`" that C136
already certified.

Identifying `λ₀ := λ(t=0)` and `λ₁ := λ(t=1)` under reading (i) therefore gives
`λ₀ = λ₁ = 0 · χ₄ · χ₆ = 0` **for every finite `χ₄, χ₆`** — swept over 14 combinations
in the script including `±√3` (cited, not recomputed, from
`experiments/20260708-dolan-casimir-g2su3/decision.md:283`: *"Decisive computation:
`D(v_a) = D(v_b) = -sqrt(3)*w` exactly"* — a genuine nonzero constant this project's S6
twisted-Dirac-operator machinery has actually produced, used here only to instantiate
the sweep with a real computed number, not asserted to literally equal C136's `χ₆`) and
a deliberately large `1000.0`. `check 1b` passes for all 14.

**Consequence: under reading (i), building the missing S6 twisted operator would not
change the answer.** `0 × (anything finite) = 0` is an algebraic fact about the M4/S3
sector alone (`mu(t)` is a function of `t, ρ, frame` only — see
`nabla_t_ops`/`mu_of`, lines 375–401 — it never receives `χ₆` as an argument). Whatever
number a genuinely-built S6 operator would produce, reading (i)'s `(λ₀,λ₁) = (0,0)` is
unaffected. **NULL-DEGENERATE**, if reading (i) is the correct identification — see §4
for why this file does not simply assert that.

---

## 3. Reading (ii): C136's own table has four literal `(w₀,w₁)` pairings, not one

`c136.solve_cell` returns **two frame entries per `t`** (left-invariant and
right-invariant), for both `t=0` and `t=1`. Re-imported directly, not re-derived
(`c161...py` §2), the four cells for every channel are:

| | `t=0` | `t=1` |
|---|---|---|
| **left-invariant** | `α = 0` | `α = −1` |
| **right-invariant** | `α = +1` | `α = 0` |

— identical for `8_v`, `8_s`, `8_c` to within `1e-9` (`check 2a`), confirming C136's
own `E1`/E-L3B result directly: **the channel axis is inert.** But C133's `Φ = 1_F ⊗
(λ₀w₀+λ₁w₁)` never states which frame plays `w₀` (nominally "the t=0 sector") versus
`w₁` ("the t=1 sector") — C136's SS5 table itself has TWO entries at each `t`, one per
frame, and nothing in either C133's decision.md (read in full this session — the
sector labels `w₀,w₁` are introduced at C133 `decision.md:586`, cited to C38, with no
further specification) or C136 assigns one of the two frames at each `t` to the role
`Φ`'s basis vectors need.

There are exactly four literal ways to pick one cell per `t`:

| pairing | `(λ₀, λ₁)` | claim.md kill-table row |
|---|---|---|
| **A** — natural@`t=0`, natural@`t=1` (each `t`'s own parallel frame, C5/C6) | `(0, 0)` | **NULL-DEGENERATE** |
| **B** — twisted@`t=0`, twisted@`t=1` (the *other* frame at each `t`) | `(+1, −1)` | **PROMOTE-AS-DERIVATION**-shaped (both nonzero, channel-equal per `2a`) |
| **C** — natural@`t=0`, twisted@`t=1` | `(0, −1)` | **NULL-CONTRADICTS-LABEL** (exactly one zero) |
| **D** — twisted@`t=0`, natural@`t=1` | `(+1, 0)` | **NULL-CONTRADICTS-LABEL** (exactly one zero) |

`check 2b`: **3 of claim.md's 5 possible outcomes are all reachable from the same
already-certified table, by frame choice alone.** No channel-dependent input changes
any of the four — `2a` already showed the channel axis contributes nothing.

**This table is the file's central finding.** It is not that the recombination is
partially done and needs one more ingredient (the S6 operator, per claim.md's original
framing) — it is that the recombination's OUTPUT depends entirely on an unstated
choice, and picking one of the four without justification would be exactly the kind of
silent modeling decision this project's `research-methodology.md` Type-1 classifier
(symbol overload — one symbol standing for two objects) and the FL Perelman-audit's
"hidden assumptions" check both exist to catch.

**A second, unquantified axis of the same gap, noted but not scripted:** C136's own
frame labels are printed as `"left-invariant (1,2)"` / `"right-invariant (2,1)"`
(`c136_joint_killing_spinor_check.py:653`), citing C38's `SU(2)_L×SU(2)_R`
representation labels — a DIFFERENT labeling scheme than "the two S3 `t`-sectors"
C133 SS9 uses for `w₀,w₁`. If `w₀,w₁` are meant to track the `(1,2)`/`(2,1)` labels
(fixed per frame, not per `t`) rather than "sector realized at `t=0`" versus "at
`t=1`" (which frame varies with `t`, per the table above), a THIRD axis of freedom
opens (which `t` to evaluate a frame-fixed sector at) that the four-pairing table does
not even enumerate. This is flagged, not resolved — resolving it would require the
same kind of unstated physical input the four-pairing table already shows is missing,
and doing so is out of this file's scope per its own Cost Estimate.

---

## 4. Why this is INCOMPLETE-MACHINERY, not a forced pick of pairing A or B

claim.md's escape route: *"if the coefficient computation resolves cleanly (any of the
first three outcomes) within one session… STOP… if [the missing S6 piece] requires a
genuinely new, expensive sub-derivation… INCOMPLETE-MACHINERY — STOP, name the specific
missing ingredient."* Section 2 shows the anticipated missing ingredient (a genuinely
built S6 twisted operator) is **not actually what blocks a clean resolution** — §2's
algebraic argument holds regardless of what that operator would return. What blocks a
clean resolution is a **different, unanticipated ingredient**: a stated principle for
which S3 frame is "the" `t=0`/`t=1` sector in C133's sense. That principle does not
exist in this project — not in C133 (which introduces `w₀,w₁` without specifying them
beyond "spanning the two S³ `t`-sectors"), not in C136 (which computes both frames at
every `t` without privileging either for this purpose), not in E-L3B, not in
`dolan-casimir-g2su3`/`round59` (which concern the S6 side only and, per §5, do not
bear on this specific S3-side ambiguity at all).

Inventing such a principle now — e.g., asserting "the physically realized sector at
each `t` is the one requiring zero extra torsion-coupling" (pairing A) or "the one
requiring nonzero coupling is where the actual physics lives" (pairing B) — would be a
genuine, new physical modeling choice, not a mechanical accounting step gluing together
already-built artifacts. That is exactly the class of work claim.md's escape route says
to name and stop at, rather than silently resolve by picking whichever pairing looks
more interesting. **This file does not pick one.**

---

## 5. Why G73/G74A/G74B and E-L3B do not change this verdict

Per the task's own instruction, this round checked whether `experiments/20260708-
dolan-casimir-g2su3/` and `experiments/20260714-round59-trivial-rank-certification/`
supply reusable machinery that would resolve §3's ambiguity rather than §2's (now shown
moot) S6-operator question.

* **E-L3B** (`experiments/20260625-l3b-bundle-obstruction/decision.md:17-31`,
  `[VERIFIED-tool]`, read in full): proves, by pure `SU(3)`-representation-restriction
  argument (Schur's lemma, no numerical computation), that `E_v ≅ E_s ≅ E_c` as
  `G₂`-equivariant bundles **with identical canonical connections** — *"the twisted
  Dirac operators … are THE SAME OPERATOR."* This is exactly why C136's `χ₆` is
  citable as `+1` for all three channels without building anything (C136 §8
  assumption 6) — and it is a **theorem**, not a computation this file could improve
  on. Building the operator numerically (as `dolan-casimir-g2su3` round 4-5 partially
  does, for a related but distinct question — see next) could only ever reproduce
  channel-uniformity, never break it. It has no bearing on §3's frame-selection
  ambiguity, which is an S3-side question entirely.
* **`dolan-casimir-g2su3`** (`decision.md:204-300`, grepped and read in the relevant
  range — the file is 390.8 KB, too large to read in full this session, a limitation
  recorded honestly here rather than silently worked around): its Round 4–5 machinery
  (`g2su3_explicit_clifford.py`, `g2su3_twisted_kernel.py`, `g2su3_find_invariant.py`)
  computes a **kernel-dimension / eigenvalue question for the trivial `SU(3)`-isotypic
  component of ONE twisted Dirac operator** (`D(v_a) = D(v_b) = -√3·w`, decisive for
  L4B's `dim ker = 1` result) — a genuinely different question (how big is the kernel,
  for the single operator E-L3B already proved is shared by all three channels) than
  "which S3 frame is `w₀` versus `w₁`." Cited in §2 as a real, computed nonzero
  constant to instantiate the sweep; **not** a source of a frame-selection principle,
  because it does not address the S3 side at all.
* **`round59-trivial-rank-certification`**: file list only (`claim.md`,
  `decision.md`, `round59_route_{a,b,c}*.py`) — not read in full this session, given
  §1–§4 already established that the S6 side is not the live gap. Naming this
  explicitly rather than silently treating "not read" as "checked and irrelevant":
  if a future round revisits this file's question and finds round59 IS relevant after
  all, that finding would need to explain why the frame-selection ambiguity (an S3-side
  question, §3) would be resolved by S6-side content — which would itself be
  surprising and worth a fresh Prior Result Gate.

**Conclusion: no already-built machinery in this project, on either side of the
`S³×S⁶` split, supplies the missing frame-selection principle.** This is consistent
with, not contradicted by, the S6-side machinery being real and reusable — the gap is
simply on the other side of the split from where claim.md's Intervention section
expected it.

---

## 6. Kill Analysis (Anti-Overfitting Gate)

**What this round KILLS.** The specific framing in claim.md's Intervention section —
that the one missing ingredient blocking `(λ₀,λ₁)` is a not-yet-built S6 twisted
operator — is **factually corrected**: §2 shows that ingredient, once built, cannot
change reading (i)'s answer, and §3 shows reading (ii)'s ambiguity is entirely on the
S3 side. **Nothing about the physical world is killed** — no candidate mechanism
(`P2`, `P3`, `P4`, `P5`, `P13`, `P14`, etc.) is newly ruled in or out by this file.

**What this round does NOT kill.** `all->both`'s status as "assumed, not derived"
(C133 SS8a) is **unchanged** — this file neither derives it (no pairing was picked)
nor refutes it (pairing B remains a live, if unprivileged, candidate reading under
which `all->both` WOULD be literally realized, `(λ₀,λ₁)=(+1,-1)`, both nonzero,
channel-equal). Does not touch `P4`, `P5`, `P13`, `P1`, `P6`-`P12` (C132's Relaxation
Map, still untried). Does not change `N_gen=3`'s CONDITIONAL status, `lambda =
FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or `safe_for_runtime =
False`.

**Relaxation Map** (one assumption per variant; none attempted here):

| variant | changed assumption | status |
|---|---|---|
| **R1** | State a frame-selection principle from an energy/ground-state argument (which frame minimizes some action functional at each `t`) | Would require an action/Lagrangian this project's Killing-spinor construction does not have (C136 §12: "poses no action and extremises nothing") — new physics content, not scoped here |
| **R2** | State a frame-selection principle from the `(1,2)`/`(2,1)` `SU(2)_L×SU(2)_R` labels directly, bypassing `t` | Opens the third, unquantified axis noted in §3's closing paragraph; not scoped here |
| **R3** | Ask Tom Lawrence which frame is physically realized | Falls under the project's existing `DO NOT INITIATE CONTACT` constraint (CLAUDE.md) — not actionable this round |
| **R4** | Treat `w₀,w₁` as literally spanning BOTH frames per `t` (i.e., `Φ` acts on a 4-, not 2-, dimensional sector space) | Would contradict C133's own explicit "2-parameter continuum" / `dim W = 2` accounting (decision.md:599, rung 3 table) — would need to revise C133, not extend C136; out of scope |

---

## 7. Self-adversarial pass (FL Step 8a "pre-answered" allowance)

The task instructions require a documented self-adversarial pass whenever the verdict
is PROMOTE-AS-DERIVATION or NULL-CONTRADICTS-LABEL. This file's verdict is
INCOMPLETE-MACHINERY (a scoping stop, not a promoted claim), so that trigger does not
strictly fire — but given the significance named in the task (OB1's central blocker),
one pass is run anyway, against this file's own central claim (§3's four-pairing
table).

**Attack 1 — "you only tried 4 pairings; is there a 5th, more natural one that
resolves the ambiguity?"** Considered: averaging the two frames per `t`
(`(0+1)/2=0.5` at `t=0`, `(−1+0)/2=−0.5` at `t=1`) — gives `(λ₀,λ₁)=(0.5,-0.5)`, both
nonzero, channel-equal, landing in the same "PROMOTE-shaped" bucket as pairing B. This
does not refute the finding — it adds a 5th candidate, strengthening rather than
weakening the point that the choice is unstated and consequential, not narrowing it to
a single answer. **Not a counterargument; folded in as further support.**

**Attack 2 — "maybe C133's `w₀,w₁` were never meant to be read off C136's table at
all, making this whole exercise a category error, not a genuine ambiguity."** This is
the strongest available objection, and it cannot be fully dismissed: C133's `Φ` is
introduced purely to COUNT support patterns in an abstract `Hom`-space (decision.md
§9's own framing: *"a Schur computation yields a dimension, not a finite set, unless a
support convention is imposed"* — never as a physically computed coupling). If that
reading is correct, this file's whole recombination attempt is answering a question
C133 never posed. **Response:** claim.md's own Intervention section (written by the
orchestrating session, not this file) explicitly authorized treating C136's alpha
table as the S3-side content of `λ₀,λ₁` — this file follows that authorization rather
than re-litigating it, but flags here that the authorization itself rests on an
identification neither C133 nor C136 make explicit. This is the same gap named in §4,
approached from the other direction — it does not change the verdict, it reinforces
it.

**Attack 3 — "is reading (i)'s `mu(t)=0` claim actually a tautology, since t=0/t=1
were chosen as exactly the points where a frame IS parallel — so of course the
'extra' coupling is zero there; you've smuggled the answer in via the choice of
evaluation points."** Correct, and stated plainly rather than hidden: `t∈{0,1}` are
not this file's choice — they are C133's own stated domain (`w₀,w₁` "spanning the two
`S³` `t`-sectors," i.e., specifically `t=0` and `t=1`, cited to C38) and C136's own
established survival set (`E3`, forced by flat-`M4` integrability `D4`, independent of
this file). This file evaluates `λ` at the two points the recombination itself
specifies, not points chosen to produce a null. The **tautological** character noted
is honest: reading (i)'s null is a restatement of C136's own `F5` (*"reading (i)'s
`t∈{0,1}` restates round72 H1b"*), which C136 itself already flagged as adding no new
physics. This file's contribution is not reading (i)'s null (already known) but §3's
four-pairing table under reading (ii) (genuinely new, per the git-pickaxe check).

**Recommendation to the orchestrator.** Given (a) the verdict is a scoping STOP, not a
promoted physical claim, (b) the central finding (§3's four-pairing table) is a
direct, mechanical computation from already-certified data with no interpretive step
inside the computation itself (only in what the four numbers are USED to conclude),
and (c) Attack 2 above is a real, unresolved objection this file could not fully
close — **a light, context-blind skeptic pass on §3 and §4 specifically (not the
whole file) is worth the cost before this recombination-ambiguity finding is written
into `pearl_registry` or cited elsewhere**, but is not mandatory before this decision.md
itself is considered complete, since no claim beyond "the recombination is
underdetermined by existing content" is being promoted.

---

## 8. What this does NOT mean

(Carried directly from claim.md, confirmed still accurate after this round's result.)

* Does NOT itself claim `all->both` is or is not physically realized — pairing B
  above shows it CAN be instantiated as a nonzero, channel-equal pair from
  already-certified data, but no principle picked pairing B over A, C, or D.
* Does NOT mean the cheap test's outcome closes H1c or OB1 — even under the most
  favorable reading (pairing B, PROMOTE-shaped), C136's own F7 precedent means any
  resulting derivation would be RESTATEMENT-tier, not a new physical mechanism, and
  not a parent action satisfying `PARENT_ACTION_GATE` F4/F6. This file does not even
  reach that stage, since no pairing was selected.
* Does NOT mean the untried Relaxation Map candidates (`P4`, `P13`, `P8`, `P1`, `P6`,
  `P7`, `P10`, `P12`) are ruled out or deprioritized.
* Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  or `safe_for_runtime = False`.
* Does NOT touch OB4, OB11, OB12, OB13, OB14, or the C144-C158 methodology thread.
* Does NOT edit `OPEN_BLOCKERS.md`, `PARENT_ACTION_GATE.md`, `pearl_registry/INDEX.md`,
  or `preprint.tex` — registry updates are the orchestrating session's, per C124-C159
  precedent. C136's own files were not modified.
* Does NOT solicit Tom Lawrence's Part 5.
* Does NOT commit to any further round regardless of outcome.

---

## 9. Independent skeptic pass (2026-09-06, context-blind, focused on §§3-4 per §7's
own recommendation) — verdict `WEAKENED`

**Arithmetic: CONFIRMED-REAL.** The skeptic independently re-derived the four-pairing
table directly from `c136_joint_killing_spinor_check.py:375-402` (`nabla_t_ops`,
`mu_of`) and `:640-675` (`solve_cell`), reproducing `(0,0), (+1,-1), (0,-1), (+1,0)`
exactly, and confirmed `check 2a`'s channel-inertness is a genuine reproduction of
C136's E1/E-L3B result, not a hidden equalization. No arithmetic defect found.

**Verdict language: found to be more optimistic than the evidence supports.** The
skeptic independently re-read `experiments/20260902-c133-symmetry-ladder-pairing-space/
decision.md:584-616` and found two clauses this file's own §7 Attack 2 already flagged
but did not follow to its conclusion: C133 itself states the coupling `Φ` lives in "a
2-parameter continuum" and that "a Schur computation yields a dimension, not a finite
set, unless a support convention is imposed" — i.e., in C133's own accounting, `λ₀,λ₁`
are **free moduli of an abstract `Hom`-space**, never spectral outputs of any operator.
C136's `α` values, by contrast, are Killing constants **solved** from a 64-dimensional
residual — computed eigenvalues of a specific operator. Identifying `λᵢ := α` at some
`(t,frame)` therefore risks a **type mismatch** (free parameter vs. computed
eigenvalue), not merely an unresolved choice of which computed value to use. Free
parameters are gauge-fixed or physically chosen; they are not "derived from" a
spectral computation.

**Corrected disposition.** The two readings differ in what follow-up they license, and
this file's original wording implicitly favored the more actionable one without
justification (the skeptic names this an unresolved AOG-3 "did the revision produce a
new prediction, or just pick the more convenient reading?" gap):

| Reading | Verdict | Licensed follow-up |
|---|---|---|
| `λᵢ := α(tᵢ, frameᵢ)` is a legitimate identification | `INCOMPLETE-MACHINERY` | Motivates a future round to find/build a frame-selection principle |
| C133 §9's own "free 2-parameter continuum" language is taken literally | `ILL-POSED` (category error) | **Forbids** spawning a round to "find a selection principle" — there is nothing to select, because `λ₀,λ₁` were never spectral quantities to begin with |

**This file does not adjudicate between the two** (neither this round nor the
skeptic pass had grounds to prefer one over the other — Attack 2, §7, was already
honest that it could not close this). **What changes, corrected here, is the
practical recommendation**: a future round picking this up should NOT be scoped as
"build a frame-selection principle" (which presupposes the INCOMPLETE-MACHINERY
reading without justification) — it should first audit, as its own Prior-Result-Gate
question, whether C133's `Φ` was ever meant to be identified with C136's specific
`α`-table at all, i.e. resolve the reading-ambiguity itself before attempting either a
construction or a further recombination. Also independently found by the skeptic
(Test 4): a fifth candidate pairing exists (the `t=1/2` simultaneous-Killing-constant
point, `(∓1/2,±1/2)`, `[VERIFIED, C136 C7 citing AHL2023 §6 case II]`) and a sixth
(identifying `w₀,w₁` with the `(1,2)`/`(2,1)` rep-labels rather than the `t=0`/`t=1`
sectors) — both **add** further candidate outcomes rather than resolving the
ambiguity, reinforcing rather than weakening §3's central finding.

No further correction to §§1-6 or the Kill Analysis (§6) was required — the skeptic
found those sections' own mathematics and scope-limits accurate as stated.

---

## Check

* Prior Result Gate item 3 (git pickaxe), left `[ ]` in claim.md, was run this session
  and closed — §"Prior Result Gate" above.
* The escape route (claim.md: "if resolution needs a genuinely new, expensive
  sub-derivation, STOP") was followed: no frame-selection principle was invented; the
  gap is named precisely (§4) rather than silently resolved.
* Every numeric claim in §§2–3 traces to `results_c161.json`, produced by a script run
  this session, not hand-typed.
* C136's own script and `results_c136.json` were not modified — `c161...py` only
  imports and calls C136's already-certified functions.
* `python -m ruff check` clean on the new script.
* The self-adversarial pass (§7) surfaced one objection (Attack 2) this file could not
  fully close, and says so rather than hiding it.

---

## Evidence tier of the central conclusion

**Central conclusion:** *the specific recombination claim.md scoped — mapping C133's
`Φ = 1_F ⊗ (λ₀w₀+λ₁w₁)` onto C136's already-certified Killing-spinor solution data —
is underdetermined by content already in this project, on the S3 side (which frame is
`w₀`/`w₁`), not on the S6 side (which was the anticipated gap and is shown moot).*

**Tier: `[VERIFIED-tool]` for the mathematics (both readings' numbers, the
channel-uniformity check, the 4-pairing enumeration) — all five checks pass, traced to
`results_c161.json`, confidence HIGH.**

**Tier of the INTERPRETIVE finding (that no selection principle exists in this
project): `[WEAKENED, per independent skeptic pass §9, 2026-09-06]`** — not because
the negative claim itself was refuted (it wasn't: no already-built machinery resolves
either reading), but because "no selection principle exists" presupposes the
INCOMPLETE-MACHINERY reading is the right one, when C133's own text is at least as
consistent with ILL-POSED (nothing to select — `λ₀,λ₁` were never spectral quantities).
Confidence on the underlying arithmetic remains HIGH (independently reconfirmed by the
skeptic); confidence on which of the two dispositions is correct is LOW — genuinely
undetermined by this project's current content, not merely under-evidenced.

**Marker on the whole round: this is a scoping-tier finding, not a promoted physical
claim** — no PROMOTE, REJECT, or ARCHIVE registry action is proposed; the orchestrating
session decides whether/how to record the recombination-ambiguity finding.
