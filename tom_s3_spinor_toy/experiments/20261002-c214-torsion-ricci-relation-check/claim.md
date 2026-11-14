# C214 Claim — torsion-Ricci relation check (C212 vs C213)

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: whether C212's torsion (`|T|^2`) and C213's Ricci relate
   via a derivable formula from Russo's theorem (`Ric_g=5*mu^2*g`,
   arXiv:2002.04673) and the `T^c<->mu` bridge shared by Agricola-
   Borowka-Friedrich (arXiv:1707.08591).
2. `decision.md`/`null_results` grep: 0 hits for "torsion-Ricci" /
   "ricci-torsion" anywhere in the project.
3. **Status:** [x] NEW.

---

## Estimand

**Population:** S6=G2/SU(3), G96/C210's certified complement basis.
**Intervention:** recompute BOTH torsion and Ricci in a SINGLE,
explicitly ambient-orthonormal basis (not C212's/C213's own, separately
normalized bases -- a critical finding of this round, see below), then
test the derived relation `Ric=(5/24)|T^c|^2`.
**Comparator:** the relation's own prediction vs. the directly
(re)computed Ricci value, both for the SAME metric.
**Endpoint:** relative error between predicted and computed Einstein
constant.
**Summary measure:** relative error (0% = confirmed).
**MCID:** n/a -- this is an exact-match check (a derived algebraic
identity either holds to numerical precision or it doesn't); a clean,
reproducible mismatch (not numerical noise) is itself the finding.

---

## Claim

**Critical prerequisite finding (not the main claim, but required
before any comparison is meaningful):** C212's tangent vectors
(`v_a=K_a@N`, G96's Frobenius-orthonormal complement generators pushed
through the orbit map) are NOT ambient-orthonormal -- `Gram(v_a,v_b)
=(1/3)*delta_ab`, checked directly. C212's `|T|^2=8/9` and C213's
Einstein-constant `5/6` (at `r=1`) were each computed in their OWN,
DIFFERENT normalization (neither is "the ambient unit-sphere metric"),
so comparing them directly, without first expressing both in the SAME
basis, would have been invalid regardless of any formula.

**Main claim (tested, FALSIFIED as stated):** the formula `Ric=(5/24)
|T^c|^2`, derived in this round from Russo's `Ric_g=5*mu^2*g` plus a
direct derivation of `|T^c|^2=24*mu^2` from Russo's own Lemma 3.1 and
the Agricola et al. `T^c` definition, does NOT match the independently,
directly (re)computed values in a single common ambient-orthonormal
basis: predicted `Ric=5.0`, directly computed `Ric=2.5` -- a clean,
exact factor-of-2 mismatch, not numerical noise (relative error 50.0%
exactly, not some small residual).

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| Predicted vs. directly-computed Ricci disagree beyond numerical precision | relative error `> 1e-6` -- met: 50% |

If FAIL (as happened) -> kills: the SPECIFIC derived bridging formula
`Ric=(5/24)|T^c|^2` as stated. Does NOT kill: C212's torsion computation
(passed its own Gray-antisymmetry positive control, unaffected by this
round); C213's Ricci computation (passed its own double N^010
calibration, unaffected -- this round only re-ran the SAME validated
code at a different, explicitly-justified `r`, confirming it still
produces a clean, Einstein-to-machine-precision result at the new
scale too: diag spread/off-diag both `~1e-15`).

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | Ambient Gram matrix of `v_a` is proportional to identity (isotropic, not some other shape) | if the complement generators were NOT isotropy-irreducible, this would show a non-uniform diagonal -- it doesn't, confirming G96's own established isotropy-irreducibility |
| T2 | Rescaled torsion equals EXACTLY `27 * (C212's own value)` | this is a pure scaling consistency check (torsion is degree-3, so `(sqrt(3))^3=3*sqrt(3)`, squared `=27`) -- confirms the rescaling itself was applied correctly, independent of whether the FINAL comparison to Russo holds |
| T3 | Rescaled Ricci is STILL Einstein (diag spread ~0) at the new `r` | confirms C213's code's correctness is not an artifact of `r=1` specifically |
| T4 [the real test] | Predicted Ricci (from torsion via the derived formula) matches directly-computed Ricci | FAILED -- factor of 2, see Kill Analysis |

---

## What this does NOT mean

1. Does NOT mean C212 or C213 are wrong -- both passed their OWN
   independent positive controls (Gray's theorem; double N^010
   calibration) again in this round, unaffected by the mismatch.
2. Does NOT mean nearly-Kahler manifolds don't satisfy SOME clean
   torsion-Ricci relation -- Russo's own `Ric=5*mu^2` theorem is a
   cited, trusted result; what failed is THIS ROUND'S OWN derivation
   of how `mu` relates to `|T^c|^2` via the Agricola et al. `T^c`
   definition, a bridge this round built itself, not something read
   directly from either paper.
3. Does NOT identify the exact source of the factor of 2 -- candidates
   named in Kill Analysis are hypotheses, not verified causes.
4. Does NOT relate to F6 directly -- this is an internal consistency
   check between two already-recorded F6-adjacent results, not a new
   F6 input itself.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**REJECT (bridging formula only)** -- clean, exact, reproducible
factor-of-2 mismatch between the derived relation and direct
computation. C212 and C213 both independently re-confirmed as correct
in the process.

**Evidence:** [VERIFIED-numpy] for all computed numbers;
[SELF-DERIVED, NOT FOUND IN A PRIMARY SOURCE] for the specific bridging
formula that failed.

**Status:** CLOSED REJECT (bridging formula) — see `decision.md` for
Kill Analysis and Relaxation Map.
