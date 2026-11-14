# C126 claim -- full fluctuation-operator stability of the Yang-Mills
extrema at t=0,1 (C123's Relaxation Map priority 3, after C124 closed
the CS/transgression route)

## Question type (EstimandOps L0)
**Descriptive.** Are `t=0,1` local minima of `S_YM[∇]=∫_{S³}|R^∇|²`
under the FULL space of connection perturbations `δω` on `S³=SU(2)`,
not merely along the 1-parameter family `∇^t`? No causal or predictive
claim.

## Background

Already established, cited not re-derived:
- (round99/C123) along the 1-parameter family alone,
  `E(t)=Ct²(1-t)²`, `E''(0)=E''(1)=2C>0` (stable), `E''(1/2)=-C<0`
  (unstable) -- Levi-Civita is a barrier top between two flat vacua,
  **but only checked in this 1D slice**.
- (C123's own scope note, `global value/minimum ≠ local fluctuation
  spectrum` -- these are genuinely different claims, only the first
  established).
- (C124) `S_YM` itself is a duplicate of `round99`'s curvature-norm
  toy at gate field F4 (selection) -- this round does NOT re-litigate
  that; it asks a DIFFERENT question (F6, stability), which C124
  explicitly did not assess and C123 explicitly scoped out.
- (C124) `S_YM` (a Hodge-star-based S³-internal functional) is outside
  the Lovelock-Cartan class C124 classified -- this round's own
  fluctuation analysis is independent of C124's findings.

## Falsifiable claim

The full second variation of `S_YM[∇^t]` around `t=0` and `t=1`,
`δ²S_YM[δω,δω]` for a GENERAL perturbation `δω ∈ Ω¹(S³,𝔰𝔲(2))` (not
restricted to the 1-parameter family direction `δω ∝ ∂_t ω^t`), is
positive semi-definite at both `t=0` and `t=1` (confirming they remain
local minima under all fluctuations, not just the 1D slice), OR it has
negative modes (meaning `t=0,1` are saddle points once the full
fluctuation space is considered, not genuine local minima).

**Kill criterion:** if the full fluctuation operator has ANY negative
eigenvalue at `t=0` or `t=1`, the 1D-slice stability claim from C123
does NOT extend to genuine local-minimum status, and the whole
Yang-Mills F4 "selects a stable pair" framing is weakened to "selects
a pair that is at best a saddle in the fuller theory." If new stable
homogeneous vacua appear OUTSIDE `{0,1}` under the full perturbation
space, that is a separate, still more significant finding, named but
not the primary target of this round.

## What this round does NOT show

- Does not resolve gate field F4 (selection) for Yang-Mills -- that
  status (`duplicate of round99`) is unchanged by whatever this round
  finds about F6 stability.
- Does not touch C124's own CS/transgression `STRUCTURAL_NO_GO` --
  independent question, independent math.
- Does not derive `S_YM` from a 13D parent action -- that gap (why
  should S³'s connection have its own Yang-Mills dynamics at all)
  remains exactly as open as it was before this round, regardless of
  the stability outcome.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Set up the second variation of `S_YM` on `S³=SU(2)` around the flat
  connections `∇^0`, `∇^1` explicitly, using the same Peter-Weyl /
  left-invariant-frame machinery already certified elsewhere in this
  project (round67, C85's Peter-Weyl apparatus) rather than building
  new infrastructure from scratch where avoidable.
- Symbolic/numeric computation, own derivation, tool-verified.
- FL Step 8a skeptic pass on the result before treating it as settled.
