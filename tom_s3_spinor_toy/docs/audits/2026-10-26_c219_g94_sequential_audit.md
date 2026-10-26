# C219 / G70–G94 sequential source audit (2026-10-26)

**Scope:** repository `sergeeey/N-7-GeoSpectra-Lab`, main at commit `40ae3f402bbc829c1bb4a53b5d71d122d7123bbc` (latest visible commit 2026-09-01). This is **evidence-only**: no physics source code, experiment gate verdict, or `main` file is changed by this document.

**Parameter caveat:** the proposed corrected `RHO6_STAR=1.1541` comes from an external C219 report and its original derivation is **not verified in this observed branch**. All alternate-radius numerical results below are conditional sensitivity calculations, **not** a proof of C219.

## Reproduced G104

Source: `tom_s3_spinor_toy/experiments/20260705-g104-h1-h2-s2xs6/g104_h1_h2_s2xs6.py` and `results_g104.json`. Independent SciPy minimization reproduces all original baseline values.

| Case | rho_star | rho_min | kappa² | V_min | m_mod (coordinate proxy) |
|---|---:|---:|---:|---:|---:|
| S3xS6 control | 1.0900 | 1.179060 | 1.170089 | -2.526864e-6 | .020248 |
| S3xS6 control | 1.1541 | 1.248196 | 1.169711 | -1.132878e-6 | .013583 |
| S2xS6 H1 (lambda=.5) | 1.0900 | 1.179954 | 1.171863 | -6.015595e-6 | .030964 |
| S2xS6 H1 | 1.1541 | 1.249034 | 1.171283 | -2.693904e-6 | .020781 |
| S2xS6 H2 (lambda=.25) | 1.0900 | 1.178621 | 1.169218 | -2.961698e-6 | .022018 |
| S2xS6 H2 | 1.1541 | 1.247783 | 1.168937 | -1.328576e-6 | .014768 |

The control `|V_min|` falls 55.17%, while `kappa²` moves just 0.0323% (approximately, **not exactly**, invariant). The H1/H2 V_min ratios are 2.03113 → 2.02766 and `m_mod` ratios are 1.40633 → 1.40721. These hypotheses cannot be *physically selected* without an external target, but they are *numerically distinguishable* on these observables. Current G104 tracker wording “H1≠H2 not distinguishable” overstates the NULL verdict. Baseline “kappa² exactly equals 7/6” is also false literally: 1.170089 ≠ 1.166667; it passes a declared tolerance.

## G70–G94 dependence triage

- **G70:** retested p=1,1.5,2,2.5,3; each kappa stays within the documented 0.5% tolerance, though numerical minima and potential depth change.
- **G82:** canonical metric-only ratio 0.25165% → 0.17872%; this remains a *proxy*, not a physical mass measurement.
- **G87:** along its **own** trajectory `rho3=kappa*rho6`, `15/(16pi)*(kappa/rho_min)^3=15/(16pi)/rho_star^3`; 0.23043 → 0.19413. Its trajectory is not the G91 `rho3=rho6^2` path.
- **G91 full-4D reduction:** constrained-path, metric-only `m_mod/m_KK` 0.1978% → 0.1487%; analytic runaway `dV/dln rho3=-3V` is unchanged. **Beware:** tracker “G91” is an unrelated lambda-origin hypothesis gate; two experiments reuse this identifier.
- **Need full two-variable reruns before revising numbers:** G92–G94; G77, G71 and the 1D mass descendants need reanchoring. Do not linearly rescale a minimum in two variables.
- **Radius does not automatically invalidate structural/index claims:** G72/G73/G74B/G75/G79A/B/G84A/G85A/G86A/B/G89A/B/G90. Separately audit numerical examples that hardcode 1.090.
- **G74A provenance:** its `experiments/20260621-g74a-lichnerowicz-gap/decision.md` has a retroactive 2026-07-17 **SUPERSEDED** note: both original proof lemmas are declared invalid/insufficient. The note cites later July work for the result `dim ker=1`. The tracker must *not* cite the original “safety 5.625 + Schur” proof as valid. This does not by itself disprove the later result.

## P0 confirmed error: G94 stationarity calibration

Published source: `tom_s3_spinor_toy/experiments/20260626-g94-s3-np-instanton/g94_s3_np_instanton.py`.

For
```
V(r3,r6) = [N0(r6)+ A3*exp(-c*r3**3)] / [K*r3**3*r6**6]
```
direct differentiation yields
```
dV/d(ln r3) = -3*[N0 + A3*exp(-c*r3**3)*(1+c*r3**3)]/(K*r3**3*r6**6).
A3_correct  = -N0/[exp(-c*r3**3)*(1+c*r3**3)].
A3_published =  N0/[exp(-c*r3**3)*(c*r3**3-1)].
```
The source formula follows from a sign error when solving the derivative equation. At original reference `r6=1.1790613418407443`, `r3=r6²`, `c=.235`:
- `A3_published=.0607370`, `dV/dln(r3)=-2.59685e-5` (verified analytically **and** by finite difference).
- `A3_correct=.0137238`, derivative numerically zero.

**Important limitation:** the published amplitude *does* admit a positive-Hessian **local** minimum near the reported `(r3,r6)=(1.9281,1.3607)`. The error invalidates its *claimed calibration*, not automatically the existence of that different local minimum. Whether near-path EFT-valid minima survive a corrected and fully reanchored scan is **OPEN**. Also G94 separately hardcodes `RHO3_STAR`, `RHO6_STAR_MIN`, and `V_MIN_G91`; all must be recomputed together with `RHO6_STAR`.

## Recommended follow-up in separate correction PR

1. G94 analytic-gradient regression test and corrected calibration; rederive references from one parameter source; redo full c-scan with Hessian and physical-domain checks before reasserting PATH_RECOVERED.
2. Add G74A superseded provenance, keep independent later result separate.
3. Narrow tracker G104: kappa near-blind; V_min/m_mod distinguishable in toy model; no real-world discriminator.
4. Validate C219 primary derivation and then update dependent numerical records. Avoid changing topological gate verdicts based only on a scale change.
5. Disambiguate duplicate G91 identifiers. Synchronize October-local spinor artifacts before calling them repository results.

**Execution provenance:** independent Python/NumPy/SciPy computations were performed outside the repository, against source-equivalent formulas. Original GitHub test suite was **not run**, the proposed C219 radius was **not derived**, and Tom's physical Dirac equation is still unavailable. Therefore this is a conditional model-audit, not a verified physical prediction or an approval to merge downstream changes.
