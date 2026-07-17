# E23 (round93) — Claim: Charge-Operator Provenance + Representation Lift

## L0 gate (EstimandOps)

**Question type:** Descriptive / structural-consistency check of this
project's OWN existing constructions (not causal, not predictive of a new
external observable). We are asking whether a set of quantum-number labels
this project has already assigned to torsion-endpoint zero modes are
well-defined operators on a well-defined Hilbert space, and whether two
formulas this project's own text uses for hypercharge are the same object.

## Frozen claim

Torsion-product zero modes (`ker(D_{S3,t}) ⊗ ker(D_{S6,twisted})`, at
`t=0` and `t=1`) admit an unambiguous, factor-consistent map to a complete
set of independent left-handed 4D Weyl states with well-defined `K_3`,
`T_{3R}`, `B-L`, `Y`, and gauge representations.

## Motivating context (why this experiment, why now)

`experiments/20260717-round92-endpoint-anomaly-audit/decision.md` (E22)
reached `BLOCKED` on the mixed `U(1)_Y`-dependent anomaly conditions for
exactly two stated reasons: (i) no numeric `B-L` value has ever been
assigned to the twisted S⁶-kernel object, and (ii) `preprint.tex` appears
to carry two distinct, unreconciled hypercharge formulas — `Y = K_3 +
(B-L)/2` (`preprint.tex:302,309`, S⁶-side `K_3` per the prose at
`:304-305`) and `Y = T_{3R} + (B-L)/2` (`preprint.tex:408`, S³-side). The
user's own recalibration of that finding sharpens it: the real blocker is
the ABSENCE of an explicit map from torsion-endpoint zero modes to
independent 4D Weyl fields with well-defined charge OPERATORS (not just
labels), and reason (ii) above should be registered as
`HYPERCHARGE_DEFINITION: UNRECONCILED` rather than assumed resolved, pending
a direct check of whether `K_3 = T_{3R}` holds as an operator identity.

This experiment runs that direct check, and three more (operator
provenance for every generator in play, a full field census per
`t`-sector, and an `SU(4)` lift), using ONLY this project's own already-
existing constructions — no new physics is introduced.

## Four-part structure (exact instructions followed)

**Part A — Operator provenance.** For `T_{3L}`, `T_{3R}`, `K_3`, `B-L`,
`Y`: which geometric factor (`S³` or `S6`) each acts on, the EXPLICIT
operator (cited, not invented), and its spectrum on the already-established
torsion-endpoint kernel (reusing E9/E12/E16/E17, not re-deriving). Check
`[K_3,D]=0`, `[T_{3R},D]=0`, `[B-L,D]=0` for the appropriate `D` in each
case, and state honestly where this project has never defined an operator
(as opposed to a post-hoc label) for one of these quantities.

**Part B — Resolve the two `Y` formulas.** Determine which of exactly
three outcomes holds: (1) `K_3 = T_{3R}` is provably true as an operator
identity on the physical subspace; (2) one formula is simply wrong or
belongs to a different effective description; (3) they are genuinely
different `U(1)` generators, in which case check whether the paper's own
ALREADY-VERIFIED anomaly computation (`preprint.tex:305-320`) uses `K_3`
consistently or implicitly needs `T_{3R}` somewhere, creating an internal
inconsistency in the paper's own published claim.

**Part C — All-left-handed census, per `t`-sector.** For `t=0` and `t=1`:
independent field, `SU(3)_c` rep, `SU(2)_L` rep, `SU(2)_R` rep, `K_3`,
`B-L`, `Y`, CPT status — excluding charge-conjugate duplicates (reusing
`g6_spinor_decomposition.py`'s own CPT bookkeeping, per round83/E13).
Flag explicitly, cell by cell, what this project's own sources let us fill
in versus what is currently unfillable.

**Part D — `SU(4)` lift.** Either exhibit an explicit `SU(4)` action on
these states that closes into complete `SU(4)` representations, checking
honestly against `preprint.tex`'s own gate G97 (no `SU(4)` subgroup in
`Iso(S³×S⁶)`) whether some OTHER (non-isometry) route is available in this
project's text — or register `SU4_ANOMALY_ROUTE: NOT_APPLICABLE` if no such
action can be exhibited. Compute `[SU(4)]^3` ONLY if Part D reaches a
genuine PASS.

## Pre-registered verdicts (exact wording, do not improvise a different rubric)

- **PASS:** operators are defined (Part A), the two `Y` formulas are
  reconciled (Part B), the field table is unambiguous (Part C), and
  `SU(4)`-completion is either explicitly constructed or honestly, cleanly
  excluded (Part D) — not left dangling.
- **FAIL:** `K_3` and `T_{3R}` are shown to give genuinely different
  charges with no reconciliation possible, OR the anomaly-free table was
  assembled by manually assigning Standard-Model charges rather than
  deriving them from this project's own geometric construction, OR `B-L`
  is shown to be introduced ONLY to make the anomaly conditions come out
  right (a post-hoc fit, not a derived quantity).
- **BLOCKED:** no explicit 13D-to-4D field map exists, or the gauge
  provenance (which operators act where, whether they commute with the
  relevant Dirac operator) cannot be established from what this project
  has already written down.

## Assumptions carried, not re-litigated here

- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption) — presupposed throughout, exactly as every reused experiment
  presupposes it.
- `dim ker(D_{S3,t=0})=2` unconditional, `dim ker(D_{S3,t=1})=2` under
  `c0=-2` only (`CONVENTION_TABLE.md` row 5).
- `dim ker(D_{S6,twisted})=1` per triality channel, `n_triality_channels=3`
  (G73/G74A→dolan-casimir-g2su3/round59 provenance-corrected number).
- The `t=0`/`t=1` joint kernel per channel is one weak-isospin doublet, not
  two copies (round83/E16, PASS, reused verbatim).
- `t=0`/`t=1` representation-theoretic content is `(1,2)`/`(2,1)` under
  either `SU(2)_L`↔`SU(2)_R` labeling convention (round85/E17, reused).
- Whether `t=0` and `t=1` coexist simultaneously (as opposed to being
  mutually exclusive values of one connection parameter) is itself
  BLOCKED (round85/E17) — this experiment does not re-open that question;
  Part C's census is built and flagged accordingly (per-sector, and
  separately for the union, with the coexistence caveat carried forward).
- System A (E9-E17, topological zero-mode count) and System B
  (`g6_spinor_decomposition.py`, full color/B-L-carrying SM bookkeeping)
  are NOT established as the same object (round91) — this experiment does
  not attempt that reconciliation; it uses this fact to determine which
  cells of Part C's census are fillable from which system.

## Constraints (repo-level, carried from CLAUDE.md)

- `lambda = FREE_COUPLING_PARAMETER` — never claim derived/fixed.
- `safe_for_runtime = False` — research only.
- No existing file modified; only this new folder created.
- No contact with Tom Lawrence; nothing submitted externally.
