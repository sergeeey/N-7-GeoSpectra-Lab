# G70 Decision — NP Functional-Form Stress Test

**Date:** 2026-06-21

**Verdict:** PROMOTE as a bounded robustness result

**Evidence status:** [VERIFIED-SYNTHETIC]

## Question

Is the G66 result

\[
\kappa=\rho_{\min}/\rho_*\approx\sqrt{7/6}
\]

an artifact of choosing exactly \(\exp(-a/\rho^2)\)?

## Preregistered comparison

The generalized NP term is

\[
V_{\rm np}(\rho;p)=-A_{\rm np}\exp(-a_p/\rho^p),
\qquad
p\in\{1,1.5,2,2.5,3\}.
\]

The scan holds

\[
u_* = a_p/\rho_*^p
\]

fixed at the G62 value. Thus

\[
a_p=u_*\rho_*^p,\qquad A_{\rm np}=V_{\rm flux}e^{u_*},
\]

and every variant has the same NP strength and satisfies
\(V(\rho_*)=0\). This isolates the exponent shape from amplitude changes.

## Kill criterion

H4 in its narrow form is rejected if every variant satisfies

\[
\frac{|\kappa(p)-\sqrt{7/6}|}{\sqrt{7/6}}<0.5\%.
\]

## Result

| p | ρ_min | κ | Relative deviation from √(7/6) |
|---:|---:|---:|---:|
| 1.0 | 1.181827 | 1.084245 | 0.3816% |
| 1.5 | 1.180426 | 1.082959 | 0.2626% |
| 2.0 | 1.179060 | 1.081706 | 0.1465% |
| 2.5 | 1.177727 | 1.080484 | 0.0334% |
| 3.0 | 1.176431 | 1.079294 | 0.0768% |

All variants have an interior AdS minimum with positive coordinate-space
second derivative. The original \(p=2\) case reproduces G62.

The leading generalized formula is

\[
\kappa_0(p)=\left(1+\frac{p}{2n}\right)^{1/p},
\qquad n=6,
\]

and tracks the numerical scan to better than 0.3%.

## Conclusion

The claim that \(\kappa\approx1.08\) is a numerical accident caused solely by
choosing \(p=2\) is rejected for the tested family \(1\le p\le3\).

The supported statement is narrower:

> Within the Minkowski-anchored effective model with volume dilution
> \(\rho^{-12}\), the gap \(\kappa\approx1.08\) is robust to the tested
> power-law deformations of the NP exponent.

This does **not** establish independence from arbitrary NP sectors, racetrack
potentials, prefactors, uplift terms, or canonical-field corrections.
