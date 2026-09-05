# C162 decision -- tool-verification of claim.md's hand-derived Steps 1-6:
# Delta_dyn=0 is FORCED for the ONLY currently-buildable instantiation of
# W_cand=3(+)3bar(+)3bar (m (+) a decoupled extra 3bar), regardless of that
# extra summand's own connection -- ALL SIX STEPS CONFIRMED by direct,
# cross-validated computation, no arithmetic error found.

**Date:** 2026-09-06
**Experiment:** `20260906-c162-ob14-w-cand-scoping`
**Script:** `c162_w_cand_delta_dyn_verification.py` -- **Results:**
`results_c162.json` (15/15 checks passed)
**Type:** Tool-verification round, executing the "future round" claim.md's
own Kill Criterion table anticipated. Not a new construction -- reuses
`round59_route_a_independent.py`, `c139_twisted_s6_alternate_representation.py`
(C139), and `c141_matched_singlet_twist.py` (C141) unmodified, plus a fresh
9-dimensional concrete instantiation of `W_cand` built from their already-
certified pieces. C146's Term1-vanishing theorem is cited, not re-imported
as code (this round independently re-derives an analogous result on a
different domain-invariant vector).

## Verdict

```
PROMOTE-AS-NECESSARY-CONDITION
  ALL SIX STEPS OF CLAIM.MD'S HAND-DERIVED ARGUMENT CONFIRMED, 15/15 CHECKS PASS
  STEP4_LOAD_BEARING_BRANCHING_CLAIM_VERIFIED_TWO_INDEPENDENT_WAYS_AGREE
  D_M_MATCHES_C139S_OWN_CERTIFIED_C_EXACTLY_NOT_JUST_IN_MAGNITUDE
  D_EXTRA_FORCED_ZERO_AT_NATURAL_CONNECTION_AND_SYMBOLICALLY_FOR_ARBITRARY_T
  DELTA_DYN_EQUALS_ZERO__RANK_1__KERNEL_1__FLOOR_1
  SELF_ADVERSARIAL_PASS_FOUND_TWO_REAL_SCOPE_LIMITATIONS_BOTH_ADDRESSED_NOT_FATAL
  RECOMMEND_INDEPENDENT_SKEPTIC_PASS_BEFORE_ANY_REGISTRY_ACTION
  UPDATE_2026_09_06__INDEPENDENT_SKEPTIC_PASS_RUN__VERDICT_CONFIRMED_REAL__SEE_SECTION_11
```

**One line:** claim.md's entire hand-derived (`[INFERRED]`, pen-and-paper)
six-step argument is now `[VERIFIED-tool]`: for `W_cand=m (+) 3bar_extra`
(the only instantiation buildable with this project's existing content,
per C139 Section 17 / C142's own exhaustive search), the graded-floor
diagnostic `Delta_dyn` is forced to exactly `0` -- not merely at the
natural zero-connection choice, but (via a genericity probe plus a
structural argument, both below) for any block-diagonal (decoupled)
connection `3bar_extra` might carry.

---

## 0. What this round did (per the orchestrating session's explicit
   instruction to tool-verify claim.md's Steps 1-6, not merely re-read them)

Read in full, this session, from primary sources (not summaries):
`experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`
(1030 lines, esp. Section 6 lines 317-338 for `c=-2*sqrt(3)/3`, Section 17
lines 951-1030 for the "decoupled is the only buildable option" reasoning),
`experiments/20260904-c141-matched-singlet-count-twist-m-plus-2singlets/decision.md`
(Section 2 lines 142-218, esp. F7 lines 206-218) and its script
`c141_matched_singlet_twist.py` (`trivial_mult()` lines 158-161, `SU3_DUAL`
line 155, `EVEN_IDX_MODULE`/`ODD_IDX_MODULE` lines 164-165, F7's own
brute-force loop lines 306-326),
`experiments/20260904-c142-graded-floor-candidate-scan/decision.md`
(confirmed C142's own `BLOCKED-INTERNAL` verdict and "no independently-
sourced second 3bar exists in this project's current content" finding,
lines 3-11, 102-110, 167-173 -- matches claim.md's own citation, not taken
on faith),
`experiments/20260904-c143-graded-floor-equality-theorem/decision.md`
(`Delta_dyn` definition, Section 4 lines 191-217; Lemma 2's genuinely-open
Hom-dim->=2 case and its toy illustration, Section 3 lines 150-179),
`experiments/20260904-c146-schur-forced-vanishing-theorem/decision.md` and
its script `c146_schur_forced_vanishing.py` (Term1-vanishing theorem, the
four checks, lines 1-213),
`PARENT_ACTION_GATE.md` lines 193-210 (C147's holomorphy quote, confirmed
verbatim match to claim.md's citation).

Wrote and ran `c162_w_cand_delta_dyn_verification.py`, importing
`round59_route_a_independent.py`, C139's, and C141's own scripts by path
(`importlib.util.spec_from_file_location`, the same pattern C161's own
`c161_lambda_recombination_scoping_check.py` and C146's own
`c146_schur_forced_vanishing.py` already use) and reusing their
already-built functions directly, not re-typing formulas.

## 1. Step 1 -- domain/target shape re-derivation, `[VERIFIED-tool]`

Using C141's own `trivial_mult()` (script lines 158-161, Frobenius
reciprocity via `SU3_DUAL`), applied to `W_cand` module
`(mult_1,mult_3,mult_3bar)=(0,1,2)`:

```
domain = trivial_mult(ODD_IDX_MODULE, W_cand)  = 2
target = trivial_mult(EVEN_IDX_MODULE, W_cand) = 1
```

Matches C141's own F7 exhaustive-search finding exactly (decision.md
Section 2, lines 206-218: "`(mult_1,mult_3,mult_3bar)` solutions for
`(domain,target)=(2,1)` ... `(0,1,2)` is a DIFFERENT, not-yet-tried module
type"). `check: step1_domain_target_matches_c141_f7_solution` -- PASS.

## 2. Step 2 -- W_cand built concretely as `m (+) 3bar_extra`, decoupling
   confirmed directly on the matrix, `[VERIFIED-tool]`

`3bar_extra` is realized as an independent copy of the su(3) `3bar` irrep:
`su3_ops_sym[a]` restricted to indices `{4,5,6}` (Sigma_even's own `3bar`
sub-block; C139 Section 3a already established `spin_lift` preserves
Sigma's even/odd parity, so this restriction is itself a valid su(3)
sub-representation, not an invented structure).

`W_cand`'s 9x9 su(3) action is built as `diag(rho_m_su3, rho_3bar_extra)`
and its Dirac connection as `diag(conn_m, extra_conn_scale * shape)`.
`check: step2_wcand_su3_action_block_diagonal` -- PASS: all 8 generators
have exactly zero cross-blocks between `m` (rows/cols 0-5) and
`3bar_extra` (rows/cols 6-8), confirmed directly, not assumed.

**Scope note, stated honestly (see Section 6, self-adversarial pass):**
C139 Section 17's own "no NOMIZU-derived data, so the only buildable
option is decoupled" quote is about `m(+)2*1`'s two extra SINGLETS, not
about an extra 3bar-type summand. This round transfers that reasoning by
direct analogy (absence of coupling data forces block-diagonality,
independent of which irrep the added summand carries) -- addressed in
Section 6, not silently assumed identical.

## 3. Step 4 (load-bearing) -- explicit branching computation,
   `[VERIFIED-tool]`, two independent methods agree

Built CONCRETE matrix representations (not abstract CG citation) for
`Sigma_even (x) 3bar_extra` (12-dim) and `Sigma_odd (x) 3bar_extra`
(12-dim), using C139's own `common_nullspace_in_block_sym` (the identical
invariant-subspace method C139 uses for its own `domain_inv`/`target_inv`):

```
dim su(3)-invariants, Sigma_even (x) 3bar_extra = 0   (claim.md predicted 0)
dim su(3)-invariants, Sigma_odd  (x) 3bar_extra = 1   (claim.md predicted 1)
```

Cross-validated against C141's own `trivial_mult(EVEN_IDX_MODULE,
{"3bar":1})=0` and `trivial_mult(ODD_IDX_MODULE, {"3bar":1})=1` -- two
independent methods (concrete nullspace computation vs. abstract
Frobenius-reciprocity counting) agree exactly. `checks:
step4_load_bearing_no_singlet_in_sigma_even_tensor_3bar_extra`,
`step4_sigma_odd_tensor_3bar_extra_has_exactly_one_singlet`,
`step4_cross_validation_trivial_mult_matches_explicit_nullspace` -- all
PASS.

**This is the load-bearing result claim.md's argument depends on**: no
su(3)-invariant target vector exists in `Sigma_even (x) 3bar_extra` for a
decoupled `3bar_extra` connection to map into.

## 4. Step 3 -- target_inv's location, `[VERIFIED-tool]`

Built the full 9-dim `W_cand`'s 72-dim Leibniz generators, computed
`domain_inv` (dim 2, matches Step 1) and `target_inv` (dim 1, matches Step
1). `check: step3_target_inv_avoids_3bar_extras_own_block` -- PASS:
`target_inv`'s basis vector has exactly zero components in `3bar_extra`'s
own 3-dim W-slot, confirming `target_inv` is entirely `m`'s own channel
(identical to C139's own already-certified `target_inv`).

## 5. Step 5 -- the 1x2 matrix, `[VERIFIED-tool]`

The 2 `domain_inv` basis vectors decouple cleanly into a pure-`m`-channel
vector and a pure-`3bar_extra`-channel vector (`check:
domain_on_splits_cleanly_into_m_channel_and_extra_channel` -- PASS,
checked directly via block norms, not assumed).

```
d_m     = -2*sqrt(3)/3     (EXACT match, not just |match|, to C139's own
                            c_exact -- target_inv here is literally the
                            same 1-dim invariant C139 already computed)
d_extra = 0                (at the natural, zero-connection instantiation)
```

`checks: step5_d_extra_is_zero_at_the_natural_zero_connection`,
`step5_d_m_matches_c139s_own_certified_c_magnitude` -- both PASS.

**Genericity probe (Step 4b, beyond claim.md's literal minimum):** rebuilt
`W_cand`'s connection with a SYMBOLIC nonzero scale `t` on `3bar_extra`'s
own block (an arbitrary fixed antisymmetric 3x3 shape). `d_extra(t)`
simplifies to literally `0` for ALL `t`, not merely at `t=0`; `d_m(t)` is
independent of `t` entirely (`d(d_m)/dt = 0`). `checks:
step4b_d_extra_vanishes_identically_for_arbitrary_nonzero_connection`,
`step4b_d_m_is_independent_of_3bar_extras_own_connection_t` -- both PASS.

**Why this generalizes beyond the one-parameter family tested (a
structural argument, not just the computed check):** `D'(eta (x) w) =
sum_i (E_i.nabla^Sigma_i eta)(x)w + (E_i.eta)(x)(nabla^W_i w)`. For a
domain vector `u_extra` supported ENTIRELY in `3bar_extra`'s own W-slot:
the first term leaves `w` (hence the W-slot) untouched; the second term
applies `nabla^W_i`, which -- for ANY block-diagonal (decoupled)
connection, regardless of its specific values -- maps the extra block to
itself, never into `m`'s block. So `D'(u_extra)` is supported ENTIRELY in
`3bar_extra`'s own W-slot, for any decoupled connection whatsoever, not
just the one-parameter family actually computed. Since `target_inv` has
zero component there (Step 3), `<target_inv, D'(u_extra)>=0` follows as a
general linear-algebra fact, independent of the connection's value. The
symbolic check above is a concrete confirmation of this argument on a
representative family, not the argument's only support.

## 6. Step 6 -- Delta_dyn, `[VERIFIED-tool]`

```
matrix (d_m, d_extra) = (-2*sqrt(3)/3, 0)
rank = 1, domain = 2, target = 1, floor = max(0,2-1) = 1
kernel = domain - rank = 2 - 1 = 1
Delta_dyn = kernel - floor = 1 - 1 = 0
```

`checks: step6_rank_is_exactly_1`, `step6_delta_dyn_is_forced_zero` --
both PASS. **Exactly matches claim.md's own Step 6 arithmetic, entry for
entry.**

## 7. Self-adversarial pass (per FL Step 8a's "pre-answered concerns"
   allowance, run before finalizing)

**Concern A -- is the "decoupled is the only buildable instantiation"
assumption (Step 2) really forced, or transferred too loosely from a
different case?** C139 Section 17's own quote ("no NOMIZU-derived data
... the only natural way to build a connection ... is to leave them
decoupled") was written about `m(+)2*1`'s two extra SINGLETS, not about an
extra `3bar`-type summand. Claim.md (and this round) transfer that
reasoning to `W_cand`'s extra `3bar` by direct analogy. **Assessed: the
transfer is sound, not merely convenient.** The underlying fact C139
Section 17 actually rests on is representation-type-independent: absent
any geometric (`NOMIZU`-derived) datum specifying HOW a new summand's
connection couples to `m`'s own, the ONLY connection buildable without
inventing new structure is block-diagonal -- this holds regardless of
whether the new summand is a singlet or a `3bar`. C142's own exhaustive
search (decision.md lines 3-11, 102-110) independently confirms no
geometric source for a second `3bar` exists in this project's current
content at all, coupled or otherwise -- so "decoupled" is not merely the
easiest option, it is the only one with ANY content behind it. **Not
fatal, but flagged as a real, if well-founded, analogy-transfer, not a
literal re-citation** -- this is exactly the distinction claim.md's own
kill-criterion row `ASSUMPTION_NARROWER_THAN_STATED` exists to catch, and
it does not fire here because C142's own search (a separate, independent
citation) closes the gap C139 Section 17 alone would have left open.

**Concern B -- is the su(3) branching computation (Step 4) genuinely
independent, or does it just re-assert Clebsch-Gordan symbolically?**
Two methods were used and cross-checked: (1) `trivial_mult()`, which IS an
algebraic application of Frobenius reciprocity (a restatement, though a
computed one, of standard CG); (2) the concrete nullspace/invariant-
subspace computation on ACTUAL 4x4/3x3 matrices (sub-blocks of
`su3_ops_sym`, which is itself built from `ADNU`'s own already-certified
structure constants, not invented). Method (2) does not presuppose the
branching rule -- it computes the invariant-subspace dimension directly
from concrete matrices satisfying the su(3) Lie algebra, and would have
returned a DIFFERENT number had the branching claim been wrong. The two
methods agreeing exactly (0 and 1, both ways) is a genuine cross-
validation, not a restatement of the same formula twice. **Assessed: not
fatal, methods are genuinely independent.**

**Concern C -- does the genericity probe (Step 4b) actually establish
"regardless of connection," or only for a narrow 1-parameter family?**
Addressed directly in Section 5 above: a short structural argument (not
merely the symbolic check) shows `d_extra=0` for ANY block-diagonal
connection, because Term1 never touches the W-connection and Term2 stays
within whatever W-block the input vector occupies for ANY connection
value, given block-diagonality. The 1-parameter symbolic check is a
concrete instance of this general fact, not its sole support. **Not
fatal.**

**Net assessment:** no arithmetic error found; the one real scope
question (Concern A) is addressed by an independent citation (C142's own
search) rather than resting on C139 Section 17 alone, and is disclosed
explicitly rather than smoothed over.

## 8. Kill criterion classification

Per claim.md's own table: **Steps 1-6 all confirmed by direct
computation** (branching counts match exactly; `d_extra=0` both at the
natural connection and symbolically for an arbitrary nonzero one; `d_m`
matches C139's own certified value EXACTLY, not just in magnitude) =>
**`PROMOTE-AS-NECESSARY-CONDITION`** -- the sharpened OB14 framing
claim.md's "Claim" section proposes (two sub-paths, (i') avoid `m`
entirely, or (ii') couple a new summand to `m`'s own tangent bundle,
replacing the single undifferentiated "second copy of `3bar`" framing) is
correct and should be folded into `OPEN_BLOCKERS.md` OB14 **by the
orchestrating session**, not by this file.

## 9. What this does NOT mean (carried forward from claim.md, not
   overclaimed beyond what Steps 1-6 establish)

- Does NOT itself constitute new physics beyond claim.md's own scope --
  this round verifies claim.md's hand-derived argument was correct, it
  does not extend the argument's reach.
- Does NOT claim `W_cand` can NEVER show `Delta_dyn>0` -- only that the
  ONE currently-buildable (decoupled) instantiation cannot, for any
  connection value on the decoupled piece.
- Does NOT resolve OB14 -- `Sigma` remains unexplained as the physically
  preferred twist; this narrows what KIND of future construction could
  matter, per claim.md's own "Claim" section (sub-paths (i')/(ii')).
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT edit `OPEN_BLOCKERS.md`, `PARENT_ACTION_GATE.md`,
  `pearl_registry/INDEX.md`, `CLAIM_LEDGER.yaml`, or `preprint.tex` --
  registry updates are the orchestrating session's, per C124-C161
  precedent.
- Does NOT proceed to sub-path (i') or (ii') -- per claim.md's explicit
  escape route, this round STOPS here.
- Does NOT solicit Tom Lawrence's Part 5.

## 10. Recommendation on an independent skeptic pass

**Recommend: YES, run an independent `Agent(skeptic)` pass (claim.md +
this decision.md + script, no session history) before any registry
action**, for three concrete reasons, not a reflexive default:

1. This is Full-Ladder tier and touches OB14's central blocker --
   exactly the case this project's own Paraphrase-Sensitivity Probe
   guidance names as warranting the extra check (a wrong PROMOTE here is
   expensive: it would misdirect whatever expensive construction round
   comes next).
2. Concern A (Section 7) is a genuine, if well-founded, analogy transfer
   -- an independent context-blind reviewer is well-suited to stress-test
   exactly this kind of "is the cited precedent actually about the same
   case" question, which this round's own self-check cannot fully rule
   out being too charitable to itself.
3. This round's own verification code was written by the same process
   that is now asking whether it should be trusted -- per this project's
   Context Asymmetry Rule, an independent pass with no visibility into
   this round's reasoning chain is the appropriate check before the
   sharpened OB14 framing is folded into any registry file.

**Not run in this round** -- per the task's explicit instruction to
recommend rather than execute, and to avoid combining Steps 1-6's
verification with a skeptic invocation in the same round.

---

## 11. Update -- independent context-blind skeptic pass (orchestrating
    session, 2026-09-06)

Per Section 10's own recommendation, ran an independent `Agent(skeptic)`
pass: claim.md + this decision.md + script + results_c162.json, plus
C139/C141/C142's cited decision.md files for background -- no session
history, no reasoning chain. Explicitly tasked with stress-testing
Concern A (Section 7) and independently sanity-checking the load-bearing
branching claim.

**Verdict: `CONFIRMED-REAL`.**

- **Concern A (analogy transfer):** confirmed sound. C139 Section 17's
  actual load-bearing premise ("absent NOMIZU-derived coupling data,
  block-diagonal is the only construction with any content behind it")
  is representation-type-independent -- a statement about missing input
  data, not about the summand's irrep type. The residual loophole ("some
  non-geometric coupling C139 Section 17 doesn't cover") is real but is
  exactly what this round's own scoping ("only currently-buildable
  instantiation") and OB14 sub-path (ii') already carve out -- not a
  fatal transfer.
- **Load-bearing branching claim, independently re-derived by hand**
  (standard su(3) CG, not merely re-running the code): `Sigma_even (x)
  3bar = (1(+)3bar)(x)3bar = 3bar (+) 3 (+) 6bar` -> 0 singlets;
  `Sigma_odd (x) 3bar = (3(+)1)(x)3bar = 1(+)8(+)3bar` -> 1 singlet.
  Matches Step 4 exactly, via a route independent of this round's own
  code.
- **Scope of "PROMOTE-AS-NECESSARY-CONDITION":** confirmed honestly
  bounded -- claim.md's and this file's own "what this does NOT mean"
  sections already state the conclusion applies only to the one
  buildable instantiation, not to `W_cand` in general.
- Three other angles checked (genericity-probe scope, alternative
  realizations of `3bar_extra` via Schur, sign/index conventions) --
  none fatal, all already disclosed in Section 7/9 above.

**No corrections to the verdict required.** `PROMOTE-AS-NECESSARY-
CONDITION` stands as written in Section 0/8. Proceeding to registry
action (`OPEN_BLOCKERS.md` OB14, `pearl_registry/INDEX.md`) per this
update.
