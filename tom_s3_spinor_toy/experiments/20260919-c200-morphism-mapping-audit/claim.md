# C200 Claim — run the 5-outcome "morphism mapping audit" prompt on every target we could think of, and measure what it is actually worth

**Date:** 2026-09-19
**FL tier:** [x] Standard (methodology/instrument-validation round, plus re-expression of already-closed physics results; no new physics claim is made)
**Question type:** [x] descriptive (formal classification of structure-preserving relations between pairs of explicit objects)

**Source of this idea:** user pasted "PHASE 2. MORPHISM MAPPING AUDIT" of a larger
prompt (Phase 1, which builds the graphs `G_A`, `G_B`, was NOT supplied) —
classify the relation between `G_A` and `G_B` as exactly one of
`EXACT_ISOMORPHISM / PARTIAL_ISOMORPHISM / HOMOMORPHISM / QUOTIENT_RELATION /
NO_STRUCTURAL_BRIDGE` — and asked what we could run it on. Earlier in this
session the user chose "go, everything in turn, then conclusions, a report, and
what it gives us."

---

## Prior Result Gate

1. **Exact claim under test:** the 5-outcome taxonomy, applied by an explicit,
   auditable classifier, (a) is a valid instrument (passes positive and negative
   controls on objects whose relation is independently known from this
   project's own verified computations), and (b) adds resolution beyond what
   this project already has for "is X the same as Y, or only similar?".
2. `null_results/INDEX.md` grep (`isomorph|morphism|homomorph|quotient|structural bridge|analog`):
   ONE hit, C173 (P4 items 2+3): a basis bridge from round59's SU(3)-indexed
   zero-mode index to the `{v,s,c}` triality-channel index is
   IMPOSSIBLE-BY-G44. **Consequence for scope:** the triality-channel target
   below is a RE-EXPRESSION of closed results (C72/C63/G102/C173,
   THEOREM.md §1-§3) in a new vocabulary; it cannot produce a new physics
   verdict and no physics verdict from it will be claimed.
3. Existing neighbours (read, not assumed): the project's 6-field Mechanism
   Transfer Gate (`FORMULA/OBJECT/ROLE/GENERATOR/SECTOR/OBSERVABLE` -> five
   verdicts `ANALOGY/BLOCKED/SCOPE-LIMITED/REFUTED/TRANSFERRED`, memory note
   2026-07-17, itself carrying a "STRUCTURE-PRESERVING MAP: explicit/absent"
   field); the global `boyko-bridge-ladder` skill (bridges BETWEEN LEVELS of ONE
   system, 8 bridge types — a different object from a map BETWEEN TWO systems);
   round86-89 (`BLOCKED / FAIL / FAIL / PARTIAL_OPPOSITE_SIGN_STRUCTURAL`).
4. Primary sources re-read directly this session: `g102_spin8_fiber.py`,
   `c72_g2_equivariance_test.py` (reusable, previously verified machinery),
   `docs/kernel_geometry_vs_dimension_pattern.md` (C198 pipeline),
   round89 `decision.md` (header), `~/.claude/rules/meta-loop.md` (MethodOps
   comparison), THEOREM.md §3 `E1` (rev 8) + C199's Lean-verified lemma.
5. **Status:** [x] NEW as an instrument-validation round; [x] REPHRASE for the
   physics content (declared above).

## Estimand

**Population:** the nine target pairs listed below (they are the whole
population; no generalisation to "all analogies" is claimed).
**Intervention/method:** the 5-outcome classifier defined in `c200_morphism_audit.py`
(explicit precedence, explicit signature, explicit null calibration — see below).
**Comparator:** (i) known ground truth on controls; (ii) the same pair under a
different declared signature; (iii) the project's existing verdict for the same
pair where one exists.
**Endpoint:** per pair, a table `signature -> {raw verdict, null-rate, calibrated verdict}`.
**Summary measure:** counts (controls passed / pairs whose verdict changes with
signature / pairs where the calibrated verdict differs from the raw one).
**MCID:** any single control failure invalidates the instrument (no partial credit).

*Natural-language statement:* "We report, for each of nine explicit object
pairs, the relation type (of five) that holds under each declared signature,
handling the choice of signature by reporting all declared ones and the
vacuity of a match by a same-size random-graph null, in order to decide whether
the taxonomy is a usable instrument and where it is not."

## Targets, in the order they will be run

**T0 — instrument controls (no physics content)**
- PC-M1 `g2` modules `8_v,8_s,8_c` pairwise -> EXACT (C72: explicit invertible intertwiner, `dim Hom = 2`)
- PC-M2 `su(3)` same triple -> EXACT (`dim Hom = 6`)
- PC-M3 `8_v|g2` vs a random basis change of itself -> EXACT
- NC-M1 `so(8)` modules `8_v` vs `8_s` -> NO_BRIDGE (`Hom = 0`)
- NC-M2 `8_v|g2` vs itself with the generator correspondence cyclically shifted -> NO_BRIDGE (an unfaithful operation map must NOT be accepted)
- PC-G1 weight graph of `8_v` vs a node-shuffled copy -> EXACT
- PC-G2 weight graphs `8_v,8_s,8_c` (edges labelled by simple roots `1..4`) pairwise -> not EXACT, QUOTIENT by a permutation of Dynkin labels `{1,3,4}` (= the outer automorphism S3 of D4)
- NC-G1 one label-preserving edge swap of the `8_v` graph -> not EXACT (sensitivity)
- NC-G2 300 random graphs with the same node count and per-label edge counts -> EXACT-or-QUOTIENT rate <= 1%

**T1 — computed targets (independent ground truth exists)**
- T1a the `g2 / su(3) / so(7)_v / so(7)_s / so(7)_c / so(8)` signature ladder on `{8_v,8_s,8_c}` (module level, explicit matrices)
- T1b `so(8)` weight graphs of the three channels (combinatorial level) — the same pair as T0 read as a target

**T2 — hand-encoded targets (verdict depends on MY encoding; flagged as such)**
- T2a triality channels `{v,s,c}` vs Standard-Model generations `{g1,g2,g3}` (declared signatures S1..S4)
- T2b C198 pipeline: circulant/Lovasz (`G_A`) vs Dirac-on-`S3xS6` kernel pipeline (`G_B`), at role level and attribute level
- T2c round89 Killing-constant structure vs the AHL2023 statement (2 nodes each)
- T2d MethodOps 8-stage proposal (`G_A`) vs this stack's `meta-loop.md` (`G_B`)

**Skipped, with reason (not silently dropped):** Tom Lawrence's vocabulary
(`local ket space = section`, `dragged = pullback`) — already settled by direct
reading of his own text on 2026-09-07/08, three terms carry no structure to
test, and contact must not be initiated.

## Pre-registered predictions (written BEFORE the script was run)

| Item | Prediction |
|---|---|
| PC-M1/M2/M3, PC-G1, PC-G2 | pass as stated above |
| NC-M1, NC-M2, NC-G1, NC-G2 | pass as stated above (if NC-M2 fails, the CHECK is malformed, not the instrument — audit the check first) |
| T1a | `su(3)`, `g2`: all three pairs EXACT. `so(7)_x`: exactly the pair NOT containing the singled-out channel `x` is EXACT (`dim Hom = 1`), the other two pairs NO_BRIDGE. `so(8)`: all three NO_BRIDGE. Stabiliser dims: `so(7)` = 21. |
| T1b | EXACT nowhere; QUOTIENT for every pair (by S3 on labels `{1,3,4}`); raw QUOTIENT is NOT vacuous (null-rate < 5%) |
| T2a | S1 (unbroken-group indistinguishability) and S2 (+ pairwise distinguishability, symmetric) -> EXACT but VACUOUS (null-rate = 1.0). S3 (cyclic triality action `v->s->c->v` vs transitive mass order `g1<g2<g3`) -> NO_BRIDGE (a 3-cycle tournament and a transitive tournament are not isomorphic and admit no homomorphism either way). Calibrated verdict of the union of signatures: NO_BRIDGE. |
| T2b | role level: QUOTIENT_RELATION (after forgetting node attributes), non-vacuous; attribute level: NO_BRIDGE (every attribute differs). The forgotten-attribute list is the informative output. |
| T2c | magnitude layer EXACT, sign-relation layer NO_BRIDGE -> combined PARTIAL (reproduces round89's own verdict `PARTIAL_OPPOSITE_SIGN_STRUCTURAL`) |
| T2d | PARTIAL, core 13 of 15 (the two ambiguous readings of the source's braces + the `REPLAN->CONTRACT` back-edge are the difference); flagged CIRCULAR (`G_B` was built from `G_A`'s vocabulary) |
| Taxonomy artefacts | (a) HOMOMORPHISM (surjective, non-injective) is structurally unavailable for equal-size pairs; (b) for semisimple modules PARTIAL and HOMOMORPHISM coincide; (c) raw verdicts without null calibration call at least one vacuous match "EXACT" |
| Main claim H_main | at least ONE target's verdict changes when the signature is changed or the null calibration is applied (else the two amendments to the prompt add nothing) |

## Kill criteria

| Condition | Consequence |
|---|---|
| Any of PC-M1/M2/M3, PC-G1, PC-G2 fails, OR NC-G2 EXACT-or-QUOTIENT rate > 1% | Instrument INVALID -> `ORACLE_INADEQUATE` (Step 2b). NO target verdict is recorded as a finding. Not a REJECT of anything. |
| NC-M2 or NC-M1 fails | audit the check first (`feedback-failing-check-audit-the-check-first`); only if the check is sound does the instrument fail |
| H_main false (no verdict changes with signature/calibration) | the prompt as written is adequate; the two proposed amendments are dropped |
| Verdict on T2a is used as a physics claim | forbidden — see "does NOT mean" |

**Adoption rule (decided before results):** adopt as an OPTIONAL pre-check for
cross-domain bridge claims only if (i) instrument valid, (ii) H_main true, and
(iii) at least one case where the taxonomy separates two situations the
existing Mechanism Transfer Gate verdicts collapse. Otherwise: archive as
vocabulary only.

## Independence rung (falsification-ladder.md ladder)

The classifier is independently-written code (mine, but running deterministic
combinatorics and linear algebra, verified against controls with known answers)
— NOT "same model, new prompt". The prose-derived encodings (T2) are NOT
independent of the author and are labelled `[ENCODING-CHOICE]` in the output.
A context-blind skeptic pass (claim + script + results only) is run before the
decision is written.

## What this does NOT mean

1. Does NOT produce a new physics verdict about triality/generations; T2a
   re-expresses closed results (C72, C63, G102, C173, THEOREM.md) and any
   agreement is by construction of the encoding for the hand-built layers.
2. Does NOT show that prose analogies can be classified reliably: for T2 the
   classifier is exact but the INPUT (which nodes, which edge types) is my
   choice; garbage in, exact garbage out.
3. Does NOT validate the prompt for domains other than the nine pairs run here.
4. Does NOT change any existing verdict (round86-89, C173, THEOREM.md).

## Fence

- `safe_for_runtime = False` (research/tooling round). No `lambda` symbol is
  introduced anywhere (project constraint).

## Verdict

**PARTIALLY_SUPPORTED — PROMOTE, narrow scope** (`decision.md`). Instrument valid
(19/19 controls; kill criteria did not fire); H_main TRUE (verdict depends on the
declared signature and on null calibration); adopt only the AMENDED protocol, only for
computed pairs; the raw five-outcome prompt is not adopted as a standalone gate; the
hand-encoded targets (T2a-T2d) are not findings. Independent skeptic pass: WEAKENED,
all findings answered in `decision.md` (fixes checked by a brute-force oracle, `verify_c200_bruteforce.py`, 0 mismatches; no second skeptic pass).
Three pre-registered predictions were NOT met (NC-M2 malformed check, T2b tautology,
T2c single-graph PARTIAL) and are recorded as such.

Status: CLOSED PROMOTE (narrow).
