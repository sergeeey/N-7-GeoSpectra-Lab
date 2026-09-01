# C121 claim -- eta(D^t) at general t, the candidate C120's own
skeptic pass surfaced

## Question type (EstimandOps L0)
**Descriptive.** Direct symbolic computation of a spectral invariant
(zeta-regularized eta invariant) as a function of the already-certified
torsion parameter `t`, using this project's own already-certified
spectrum. No causal or predictive claim.

## Background

C120's FL Step 8a skeptic pass surfaced `eta(D^t)` -- the eta-invariant
of the torsion-deformed S³ Dirac operator, related to the gravitational
Chern-Simons level `k_grav = eta(D)/2` this project already certified
as `k_grav=0` at the Levi-Civita point (`t=1/2`, gate G34-B3) but never
computed at other `t`. Structurally odd in `(t-1/2)` by C44's own
already-certified identity `spec(D^{1-t})=-spec(D^t)`; scale/radius-
independent by definition (immune to round115's volume-circularity).

## The certified spectrum being used (cited, not re-derived)

Round67 [VERIFIED-sympy, this project]: `D^t` on `S³` has spectrum
`lambda(n,sigma) = sigma*(n+3/2) + 3*(t-1/2)`, `n=0,1,2,...`,
`sigma=+-1`, each with eigenspace multiplicity `(n+1)(n+2)` (S³ Dirac
operator's own standard multiplicity, cited from this project's
established spectrum). The shift `h_H=3` acts as a SCALAR on the
entire spectrum (round67's key finding: Kostant's torsion element
collapses to a scalar on `S³` specifically), so this multiplicity
structure is unaffected by `t`.

## Falsifiable claim

Compute `eta(D^t)` via zeta-function regularization: with
`a = 3(t-1/2)`, `m = n+3/2`, on the open interval `t in (0,1)`
(equivalently `|a|<3/2`) where every eigenvalue has a definite,
`n`-independent sign pattern (`m+a>0` and `m-a>0` for all `n>=0`
whenever `|a|<3/2`, since the smallest `m=3/2` gives `m-|a|>0` strictly
there):

```
eta(s) = sum_n (m^2-1/4) * [(m+a)^(-s) - (m-a)^(-s)]
       = [zeta_H(s-2,3/2+a) - 2a*zeta_H(s-1,3/2+a) + (a^2-1/4)*zeta_H(s,3/2+a)]
         - [same with a -> -a]
```

evaluated at `s=0` via the standard `zeta_H(-n,q) = -B_{n+1}(q)/(n+1)`
identity (Bernoulli polynomials), giving a closed-form polynomial in
`a` (hence in `t`) on `(0,1)`.

**Pre-registered prediction:** `eta(t)` is a polynomial in `a=3(t-1/2)`
of degree <=3 (from the `s-2,s-1,s` structure above), ODD in `a` (by
construction of the `f(s,a)-f(s,-a)` difference).

## HONEST CORRECTION, made before running anything (self-caught while
deriving the formula above)

The two checks originally planned as independent verification --
"`eta(t=1/2)=0`" and "`eta(1-t)=-eta(t)`" -- are **NOT independent
tests of this construction**. Both are algebraically GUARANTEED by the
`eta(s)=f(s,a)-f(s,-a)` structure itself, regardless of whether the
underlying formula has an error: `a=0` trivially makes `f(s,0)-f(s,0)=0`,
and swapping `a->-a` trivially negates the difference. Relying on
these as "checks that would catch a wrong formula" would have been
circular. **Corrected verification plan below uses a genuinely
independent method.**

(Separately, honest note: `eta(t=1/2)=0` IS independently true as a
known mathematical fact -- the round `S³` Dirac spectrum is symmetric
under an orientation-reversing isometry at the Levi-Civita point, a
standard reason round spheres have vanishing eta invariant -- but this
is a fact about the LITERATURE, not a check on THIS round's own
algebra, and is not sufficient by itself to catch a sign or
coefficient error in the Bernoulli-polynomial expansion.)

## Corrected, genuinely independent verification plan

1. **Numerical regularized-sum cross-check.** Compute
   `eta(a) ~ sum_{n=0}^{N} (m^2-1/4)[sign(m+a)e^{-eps*(m+a)} -
   sign(m-a)e^{-eps*(m-a)}]` for a grid of `eps` values, extrapolate
   `eps->0` (standard heat-kernel-style regularization, independent of
   the zeta-function method), and compare against the closed-form
   polynomial at several sample `a` values. Agreement is genuine
   evidence the closed form is correct; disagreement means the
   Bernoulli-polynomial algebra has an error.
2. **Symbolic self-consistency:** verify the closed form is degree <=3
   and odd in `a` symbolically (sympy `Poly`, check even-degree
   coefficients are exactly zero) -- a real check on the ALGEBRA
   (did the expansion actually produce a degree-3 odd polynomial, or
   did a mistake produce something else), distinct from the vacuous
   "does it look odd" check above.
3. Report `eta(t=1/2)=0` and antisymmetry as confirmed literature-
   consistent facts, explicitly NOT claimed as this round's own
   independent verification.

## Pre-registered risk (the most likely boring outcome, named before
running, per this session's own established discipline)

The `eta(t)` closed form derived above is valid only on `t in (0,1)`
(`|a|<3/2`) because that is where every eigenvalue keeps one fixed
sign for all `n`. At `a=+-3/2` (i.e. `t=0,1`) the `n=0` term's
`m-a` or `m+a` factor hits exactly zero -- a genuine zero mode
crossing (round67's own finding). The SAME thing happens at
`a=+-5/2` (`t=-1/3,4/3`, round67's `n=1` crossing), `a=+-7/2`
(`t=-2/3,5/3`, `n=2`), etc. [CORRECTED post-hoc, FL Step 8a skeptic
pass on the result: originally misstated as `a=+-7/2,+-11/2` --
crossings occur at `a=+-(n+3/2)` for n=0,1,2,..., i.e. spacing 1 in
`a`, not 2. The t-values quoted were already correct; only the a-values
were wrong. Did not affect the computed result, which never used
these specific a-values, but would have misdirected anyone following
this section to integrate over the wrong interval.] -- **the closed-form formula above will
need a DIFFERENT branch on each interval between consecutive
crossings, and there is no reason from this construction alone to
expect the `t=0,1` interval's `eta` value to be distinguished from
any other interval's.** The most likely outcome, consistent with
round116's own already-documented finding that this whole family is
an "equivalent restatement" with no preference for `n=0` over any
other `n`: `eta(t)` on each interval is ALSO just a relabeled version
of the same formula, with no special integrality/quantization
distinguishing `t in (0,1)` from `t in (-1/3,0)` etc.

**Kill criterion:** if the computed `eta` values on the `(0,1)`
interval show no special integrality/quantization property not ALSO
shared by the neighboring intervals (`(-1/3,0)`, `(1,4/3)`), this
candidate is NULL for the same underlying reason round116 was --
distinguishes nothing about `n=0` specifically. This round explicitly
computes at least one neighboring interval to make this comparison
possible, not just the `(0,1)` interval alone.

## What this round does NOT show

- Does not compute `eta(D^t)` on the FULL S³xS⁶ background -- only the
  S³ factor, matching this whole `t`-selection line's own established
  scope (round67, round99, round111, round113, round116 are all
  S³-only; C119 already showed S³-only results don't automatically
  transfer to the frozen S³xS⁶ product).
- Does not establish a gravitational-Chern-Simons-level-quantization
  ARGUMENT connecting `eta` to a physical selection principle -- that
  is a SEPARATE F6 question, to be assessed only after the computation,
  not assumed going in (the mistake C120's own original draft made
  with the volume-product framing).
- Does not change N_gen=3's CONDITIONAL status; does not touch S6/
  triality/OB1's PARKED status by itself.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- `ruff check` clean.
- Full pytest suite before commit (new .py file).
- The two genuinely independent checks above (numerical regularized-
  sum cross-check; symbolic degree/parity self-consistency).
- Explicit computation of at least 2 intervals (`(0,1)` and one
  neighbor) to test the pre-registered risk directly, not just assume
  it away.
- FL Step 8a skeptic pass on the result, same discipline as C112-C120.
