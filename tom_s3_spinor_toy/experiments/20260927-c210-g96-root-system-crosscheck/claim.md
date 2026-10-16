# C210 Claim — cross-check G96's G2 realization against the standard root system

**Date:** 2026-09-27
**FL tier:** [x] Standard (verification round against this project's own
prior result, G96; no new physics claim)
**Question type (EstimandOps L0):** Descriptive — does a specific
algebraic construction (G96's octonion-derivation basis for g2) reproduce
a specific, already-known invariant (the abstract G2 root system)?

## Why this round exists

User asked to cross-check this project's own G96 (`experiments/20260626-
g96-s6-g2-su3/`) against a MathOverflow question found via the Stack
Exchange API ("Reference Request: Structure constants for G2", Q322858).
Its answers (Smolensky, McNamara, Humphreys) point to Chevalley-basis
structure constants `C_{alpha,beta,i,j}`, indexed by an ORDERED root
system (Carter's book table after Sec 12.4; Vavilov-Plotkin Table IV;
Humphreys GTM 9 Sec 19.3) -- see `mathoverflow-g2-structure-constants-
reference.md` for the full verbatim record.

**G96 never computed anything root-indexed.** It built 14 generators as
an arbitrary SVD null-space basis of octonion derivations, and verified
only Lie-bracket CLOSURE (via least-squares reconstruction residuals),
Jacobi, and the SU(3)-stabilizer decomposition -- no Cartan subalgebra,
no roots, no structure-constant table were ever extracted. A naive
number-for-number comparison against the MO-cited Chevalley tables would
therefore compare two DIFFERENT mathematical objects in two unrelated
bases and mean nothing.

## Prior Result Gate

1. Exact claim: G96's own 14-generator basis for g2 (built from the
   Fano-plane octonion-derivation condition), when its Cartan subalgebra
   and root system are extracted via the ambient trace form (basis-
   independent), reproduces the standard G2 root system exactly: 12
   roots, 6 short + 6 long in norm-squared ratio 3 (length ratio
   sqrt(3)), consecutive angular spacing 30 degrees.
2. `grep` of `experiments/` for any prior Cartan/root extraction from
   G96's basis: no hits -- G96 itself never did this, and no later round
   revisits it.
3. **Status:** [x] NEW.

## Estimand

**Population:** the 14-dimensional Lie algebra g2, realized as G96's own
explicit basis of 7x7 real antisymmetric matrices (octonion derivations).
**Intervention/method:** pick a generic Cartan element H1 (random real
combination of the 14 generators), extract the 2-dim kernel of ad(H1) as
the Cartan subalgebra {H1,H2}, extract the 6 positive-root eigenvectors
of ad(H1) on the complexified adjoint representation, read off each
root's second coordinate via [H2,E_k]=i*phi_k*E_k, convert (theta_k,phi_k)
into an actual Cartan ELEMENT H_{alpha_k} via the trace-form Gram matrix,
then measure lengths/angles using the SAME trace form on an orthonormal
basis (Gram-Schmidt), not the raw (theta,phi) coordinates.
**Comparator:** the standard, textbook G2 root system (6 short + 6 long
roots, ratio sqrt(3), 30-degree spacing) -- confirmed via WebSearch before
use, not from memory alone.
**Endpoint:** exact numerical match (to machine precision) of norm-ratio
and angular spacing.

## Kill criterion

| Condition | Consequence |
|---|---|
| `ad(H1)` does not have exactly a 2-dim zero-eigenspace and 6 nonzero conjugate pairs | G96's basis is not actually rank-2 / does not have 12 nonzero roots -- something is wrong with G96's own construction, report explicitly |
| The 12 norms-squared do not split cleanly into two clusters, or the ratio is not close to 3 | The realization does not have the standard G2 root-length structure -- a real finding, not swept under a tolerance |
| Angle gaps (using the CORRECT orthonormalized trace-form coordinates, not raw (theta,phi)) are not all ~30 degrees | Root system does not match G2's known angular structure |

If FAIL → kills: the claim that G96's basis is a faithful realization of
g2 at the level of its root system (would be a genuine, reportable
finding about G96, not previously known).
If PASS → survives: independent, basis-free confirmation that G96's
construction is the genuine G2 Lie algebra, not just "14 antisymmetric
matrices that happen to close under commutation."

## A self-caught bug before the final check

The first version of the angle check used the raw `(theta_k, phi_k)`
eigenvalue coordinates directly (`atan2(phi,theta)`) to sort and measure
angular gaps between roots. This FAILED (gaps of 6.3, 22.6, 122.0, 18.6,
5.9, 4.5 degrees, not 30) -- not because the root system is wrong, but
because `{H1,H2}` is not generally an ORTHONORMAL pair under the trace
form (their raw coordinate axes can be skewed/unequally scaled relative
to each other), so angles measured in that raw coordinate system are not
the true geometric angles. Fixed by Gram-Schmidt orthonormalizing
`{H1,H2}` into `{e1,e2}` under the SAME trace form already used (correctly)
for the length/ratio check, then projecting each root element onto
`{e1,e2}` before computing angles. Confirmed orthonormal
(`trace_form(e1,e1)=1.0`, `trace_form(e2,e2)=1.0`, `trace_form(e1,e2)~0`)
before trusting the corrected angles.

## What this does NOT mean

1. Does NOT independently verify the SPECIFIC numerical tables cited in
   the MO answers (Carter Sec 12.4; Vavilov-Plotkin Table IV) -- those
   are in a Chevalley/root-subgroup basis this round does not construct,
   and neither book was opened.
2. Does NOT touch this project's own OB1/N_gen=3/G2-SU(3)-on-S6 physics
   claims -- purely an internal-consistency check on G96's own algebra.
3. Does NOT redo G96's own closure/Jacobi/SU(3)-stabilizer verification
   -- those stand independently, unaffected.

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced.

## Verdict

**PROMOTE.** G96's own 14-generator basis, when its Cartan subalgebra
and root system are extracted via the ambient trace form, reproduces the
exact standard G2 root system: norm-squared ratio exactly 3.0 (length
ratio sqrt(3)), all 12 consecutive angular gaps exactly 30.0 degrees.
This is independent, basis-free confirmation (not previously done) that
G96's octonion-derivation construction is a genuine, faithful realization
of g2 -- not just a 14-dimensional space that happens to close under
commutation.

**Evidence:** [VERIFIED-numpy, 6/6 structural checks, all_pass=True]
(rank-2 Cartan, 12 nonzero roots, H1/H2 commute, 6 root pairs extracted,
exact ratio 3.0, exact 30-degree spacing) + [VERIFIED-WebSearch] (the G2
root system's own 6+6/sqrt(3)/30-degree structure, checked before use,
not assumed from memory).

**Status:** CLOSED PROMOTE.
