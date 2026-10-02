# C217 Claim — is C213's Castellani-formula curvature a UNIFORM factor 1/2 off
# the standard Levi-Civita curvature? (resolution attempt for the C216 anomaly)

**Date:** 2026-10-03
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive (algebraic/numerical consistency of a code path; no empirical or causal claim)

---

## Prior Result Gate

1. Exact claim: `riemann()` inside C213's `riemann_ricci` (Castellani hep-th/9912277 eq 3.35-3.36 as coded) equals
   exactly 1/2 x the standard Riemann tensor, for ALL four terms together, component-wise.
2. Prior hits reviewed: C213 (PASS_CALIBRATED, absolute value 5/6 at r=1, 2.5 at r=sqrt3), C214 (REJECT of the
   Russo/Agricola bridge, comparison target was C213's 2.5), C215 (Ric^grad=1.5 derived from C213's 2.5), C216
   (KN route gives 4.0; Castellani gives 2.5 instead of 5.0 on the SO(7)/SO(6) control; independent skeptic pass
   NEEDS_WORK, suggested exactly this hypothesis and flagged that the "two refuted hypotheses" of C216 did not test a
   uniform all-term factor: the term2-only doubling was refuted, a uniform doubling of all four terms never was).
3. `null_results/` + `parked/`: no entry on this specific question. **Status:** [x] NEW (follow-up resolving C216).

---

## Estimand

**Population:** the two 6-dim cosets already built in C216: S6=SO(7)/SO(6) (symmetric control, only term2 active) and
S6=G2/SU(3) (non-symmetric, terms 1,2,4 active), both in the ambient-unit orthonormal frame.
**Intervention:** compute the full 4-index tensor of C213's four terms (not just the Ricci contraction), multiply all four
by 2, compare entry-by-entry (6^4=1296) to the unit round S6 tensor `R(a,b,d,e)=d_ad d_be - d_ae d_bd`.
**Comparator:** the code as-is (x1) and a term2-only doubling (the variant C216 already refuted at the Ricci level).
**Endpoint:** max |R_code_variant - R_round| over all entries.
**Summary measure:** max-abs error; threshold 1e-8.

## Why G2/SU(3) is expected to be the round sphere (stated, not assumed silently)

G2 <= SO(7) acts on Im(O)=R^7 by isometries, transitively on the unit S6; the isotropy representation on m is
real-irreducible (C165, Casimir spread 3e-15), so the G2-invariant metric is unique up to scale, i.e. the round one.
The script checks the two concrete facts this uses: (a) all comp+su3 generators are antisymmetric 7x7 matrices, (b) the
rescaled tangent frame is ambient-orthonormal.

## Claim (pre-registered before running)

2 x C213's full Castellani tensor equals the unit-round-S6 tensor entry by entry on BOTH spaces (the symmetric control and
the non-symmetric G2/SU(3)); the code as-is and the term2-only doubling do not.

## Kill criterion

| Kill condition | Threshold |
|---|---|
| 2 x R_code differs from R_round on either space | max-abs error > 1e-8 -> the factor is NOT a uniform convention factor; the C216 anomaly stays unresolved |
| x1 or term2-only x2 already matches R_round on G2/SU(3) | error <= 1e-3 -> the test cannot distinguish a uniform factor from alternatives (cannot-fail check) |
| independent KN + Friedrich-Ivanov Ricci (no Castellani code) differs from n-1=5 | > 1e-8 -> the independent route disagrees, conclusion not trustworthy |

If PASS: C213's absolute values (5/6 at r=1, 2.5 at r=sqrt3) are in a convention with a factor 1/2; the standard values
are 5/3 and 5.0. C215's `Ric^grad=1.5` is wrong (should be 4.0). C214's REJECT compared Russo's correct 5.0 against a
half-convention 2.5 and should be retracted.

## What this does NOT mean

1. Does NOT locate WHERE in Castellani's paper/eq 3.35-3.36 the factor 1/2 comes from (convention of the curvature 2-form,
   a missing 1/2 in code, or the paper's own definition) - that needs a primary-source read and is separate.
2. Does NOT re-verify the N^010 published value `R=12`: if the factor is uniform, the standard-convention value would be 24;
   that has not been checked against an independent N^010 computation.
3. Does NOT touch C212's torsion (independently confirmed by the bracket route in C216).

## Fence

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

## Verdict

**PASS (`UNIFORM_FACTOR_2_CONFIRMED`)** - see `decision.md`. Component-wise error 2.0e-15 on G2/SU(3) (1296 entries), negative
controls (x1, term2-only x2) fail as required, independent KN + Friedrich-Ivanov route gives Ric^g = 5.0 exactly.
Root cause located in the primary source: Castellani eq. (3.34) omits the standard 1/2.

**Evidence:** [VERIFIED-numpy] + [VERIFIED-source: arXiv hep-th/9912277 eq. 3.34 read directly].
**Status:** CLOSED PASS.
