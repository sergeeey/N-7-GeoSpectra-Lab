# E16 (round83) — Claim: does the 2-dim S³×S⁶ joint kernel decompose as
# one weak doublet, or as two independent family copies?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim, per project CLAUDE.md methodology
activation; this reconciles a real, unresolved defect flagged by E12/KT-13 in
the torsion-escape-route program)
**Question type:** [x] descriptive [ ] predictive [ ] causal

## Estimand (L0/L1, descriptive)

**Population:** the 2-dimensional complex joint kernel
`ker(D_{S³,t}) ⊗ ker(D_{S⁶,twisted})` (dimension 2×1=2), for ONE fixed triality
channel, at ONE fixed torsion crossing (`t=0` or `t=1` — pick whichever this
project's existing conventions make cleanest; used `t=0` as the primary case
below, since it is the value E9 originally constructed without any sign
ambiguity, with `t=1` under `c0=-2` checked as a cross-reference throughout).

**Intervention/comparator:** none — this is a pure classification/
reconciliation task against ALREADY-ESTABLISHED project bookkeeping (G6's
`chir_s3` table, E11/round77's SU(2)_L/R representation labels, G74A/G74B's
S⁶-side chirality/index results, E12's tensor-product kernel identity). No new
physics is computed; existing, already tool-verified facts are cross-referenced
and one small structural/logical consequence of them (Part 3 of the script) is
checked concretely.

**Endpoint:** classification of the 2 joint-kernel basis states into one of
three pre-registered categories (below), based on whether they carry the same
or different values of: `SU(3)_c`/triality-channel label, `B-L` charge (if
defined for this specific object anywhere in this project), S⁶-side
chirality/G74B's `sign(ind)=+1` result, and `SU(2)_L×SU(2)_R` quantum numbers
(`T3L`, `T3R`).

**Summary measure:** a three-way categorical verdict (PASS / FAIL / BLOCKED),
not a continuous quantity.

**ICE:** none — this is a closed-form, deterministic classification of a
finite-dimensional (2-dim) space against a finite set of already-established
quantum-number assignments. There is no missing-data or dropout structure.

**MCID:** not applicable to a categorical PASS/FAIL/BLOCKED verdict.

## Natural-language statement (written before re-reading the full evidence trail in decision.md)

*We classify, descriptively, whether the two basis states of the 2-dimensional
torsion-escape-route joint kernel (S³ factor × S⁶ factor, one fixed channel)
carry identical full gauge quantum numbers (in which case they are two
independent family copies — FAIL) or differ only in `T₃` while sharing every
S⁶-side-determined label (in which case they are the two components of one
weak-isospin doublet — PASS), using only quantum-number bookkeeping this
project has already established (G6, E11/round77, G74A/G74B, E12), and we
report BLOCKED, honestly, if that existing bookkeeping is not rich enough to
decide between the two readings.*

## What this result does NOT mean (written before re-deriving the verdict)

1. Will **not** establish a physical mechanism for why `t=0` (or `t=1`) is
   selected in the first place (H1c) — that remains exactly as open as
   E7/E9/E10/E11/E14 left it, regardless of this experiment's outcome.
2. Will **not** resolve KT-8 (whether ANY zero mode of the untwisted `D_full`
   exists at all) — untouched.
3. Will **not**, even under a PASS verdict, establish that the torsion-escape
   route supplies a COMPLETE single generation (this project's own
   `preprint.tex:292-298` convention requires BOTH an `SU(2)_L` doublet AND an
   `SU(2)_R` doublet — i.e. both `t=0` and `t=1` sectors — simultaneously,
   which is a separate, unresolved question already flagged by E12 Section E.2
   and E14 as requiring its own physical mechanism). A PASS verdict here only
   settles whether the observed multiplicity-2 excess, BY ITSELF, constitutes
   illegitimate family duplication or expected internal SU(2) structure — it
   does not by itself certify the escape route as complete or physically
   selected.
4. Will **not** re-derive or challenge G73/G74A/G74B's own S⁶-only
   `dim ker=1`/chirality results — reused here by citation, per round82's
   already-established finding that these are entirely independent of the S³
   factor.
5. A BLOCKED verdict, if reached, would **not** mean "this project's physics
   is wrong" — only that the specific bookkeeping needed to distinguish PASS
   from FAIL (an explicit quantum-number assignment for the twisted `S⁻`
   kernel state, or an explicit 13D parent-spinor decomposition) does not yet
   exist in this project's artifacts, and would need to be built, not merely
   inferred, before a confident PASS/FAIL call could be made.

## Pre-registered PASS / FAIL / BLOCKED criteria (frozen verbatim, per task instructions)

| Verdict | Condition |
|---|---|
| **PASS** ("one weak doublet") | The two basis states carry the SAME `SU(3)` triality-channel label, the SAME `B-L` charge (if defined anywhere in this project for this object), the SAME S⁶-side chirality/4D-chirality assignment, but DIFFERENT `T₃` eigenvalues under the same `SU(2)` factor — i.e. they are the two `T₃`-components of one weak-isospin doublet. |
| **FAIL** ("two independent family copies") | The two basis states carry IDENTICAL full gauge quantum numbers, including which `SU(2)` factor is the doublet — i.e. two literal copies of the same particle content. |
| **BLOCKED** | This project's own quantum-number bookkeeping does not assign `B-L`, `SU(3)`, and `SU(2)_L×SU(2)_R` labels to individual S³-side (or twisted-S⁶-side) basis states richly enough to distinguish PASS from FAIL — a full 13D parent-spinor decomposition would be needed to unblock it. |

## Method

1. Re-cite (not re-derive) E11/round77's tool-verified SU(2)_L/R
   representation labels for the two S³-side kernel states, E14/E15's
   tool-verified irreducibility of that doublet, and G74A/G74B/round82's
   tool-verified confirmation that the S⁶-side chirality/index result depends
   on nothing about the S³ factor.
2. Directly inspect (Read) G6's own `s3_states` dict fields
   (`experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`)
   to determine exactly which quantum numbers this project's own bookkeeping
   assigns to an S3-side state, and whether an SU(3)/B-L field exists there at
   all.
3. Directly inspect (Grep + Read) `preprint.tex` for any statement fixing
   whether the S³ factor carries its own triality/generation label, or whether
   this is purely an S⁶-side property.
4. Make the resulting "shared S⁶ factor ⟹ shared S⁶-only quantum number"
   argument concrete with a small, self-contained toy computation
   (`e16_joint_representation_check.py`) rather than asserting it as obvious
   linear algebra — verify the joint-kernel Kronecker-product structure
   directly, and verify that an S3-side weight operator DOES distinguish the
   two states while a toy S6-side-only operator does NOT.
5. Reach the verdict honestly from 1-4, without inventing new bookkeeping to
   force a PASS or FAIL the existing artifacts don't support.

## Kill criterion

If Part 1 of the script finds G6 (or any other artifact in this project)
DOES assign a triality/SU(3)/B-L label directly to an individual S3-side
state, AND that label differs between the two S3-side kernel basis states
in a way consistent with the project's own conventions, this would
FALSIFY the PASS reading in favor of FAIL. Kill signal:
`verdict.no_su3_or_bl_field_on_s3_side == False` combined with an explicit
differing assignment found by direct Read.

## Assumptions (status)

| Assumption | Status |
|---|---|
| `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (exact decoupling) | [INFERRED, inherited from E2/E12's own unverified caveat] — not re-examined here; this experiment's classification is conditional on this holding, exactly as E12's own multiplicity-2 finding is |
| G74A's `dim ker(D_{S6,twisted}) = 1` per channel | [VERIFIED-tool, PROMOTE, inherited, not re-derived] |
| E11/round77's SU(2)_L=left-translation convention | [WEAK] — imported, unstated in `preprint.tex`, reused here exactly as round77/E13 flagged it; does not affect PASS/FAIL (only affects which SU(2) factor is *called* L vs R), only affects terminology |
| E12 Section C's tensor-product kernel identity `ker(A²⊗I+I⊗B²)=ker(A)⊗ker(B)` | [VERIFIED-tool, inherited from E12, not re-derived, reused as the structural basis for Part 3 of this script] |

## Check
`python e16_joint_representation_check.py` →
`verdict.no_su3_or_bl_field_on_s3_side==True`,
`verdict.doublet_confirmed==True`,
`verdict.different_T3_eigenvalues==True`,
`verdict.same_S6_eigenvalue_on_both_joint_states==True`,
`verdict.label=="STRUCTURAL_SUPPORT_FOR_ONE_WEAK_DOUBLET"`.
