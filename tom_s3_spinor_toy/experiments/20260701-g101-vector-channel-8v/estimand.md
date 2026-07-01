# Estimand — G101: explicit construction of the 8_v (vector) triality channel

**Date:** 2026-07-01
**FL tier:** Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

## Background

G67-C3 requires three geometrically distinct channels (8_v, 8_s=L, 8_c=R)
to appear in the S3xS6 Dirac action for G73's N_gen=3 arithmetic to be more
than conditional. G68 (2026-06-21) rigorously closed 2/3: L and R octonion
multiplication matrices are proven INEQUIVALENT Cl(0,7) representations via
the pseudoscalar invariant (Omega_L=+I8 != Omega_R=-I8). The third channel,
8_v (the "vector" representation of SO(8)/Spin(8) triality), was explicitly
left unconstructed: G68's own text says it "does NOT arise from left or
right O-multiplication by any standard construction" and defers to G72
(Tom Lawrence input, does not exist as a file in this repo).

## Estimand

**Population:** the real 8-dimensional octonion vector space O = R (x) Im(O)
(1 real + 7 imaginary units), with G2=Aut(O) acting by automorphism (the
STANDARD, defining action -- not left/right multiplication).

**Intervention:** construct this G2-action explicitly as 8x8 matrices
(reusing the G2 generator matrices already built in G67/G96's Fano-plane
derivation, extended from their 7x7 action on Im(O) to an 8x8 action on
O = R (+) Im(O) by acting trivially on the R factor), and test whether this
"vector" module is a genuine THIRD Clifford-adjacent module distinguishable
from L and R by an analogous invariant.

**Comparator:** G68's method (pseudoscalar Omega = product of 7 generators)
applied to L and R; does an analogous invariant exist and differ for the
vector construction, or does the vector construction fail to even admit a
comparable Clifford-module structure at all (a real possibility, since the
"vector" rep is not built from multiplication operators the way L/R are --
this may be a category mismatch, not a missing computation).

**Endpoint:** (a) does the extended 7-dim-to-8-dim G2 action even close into
a genuine Cl(0,7)-type algebra the way L/R do; (b) if so, is its
pseudoscalar-like invariant distinct from Omega_L and Omega_R.

**Summary measure:** ternary outcome -- {GENUINE_THIRD_CHANNEL (distinct
invariant found), CATEGORY_MISMATCH (vector rep is not a Cl(7)-module in
the relevant sense, so G68's method does not apply -- this would explain,
not fix, why G68 called it unconstructable "by any standard construction"),
CONSTRUCTION_FAILS (attempted matrices don't even satisfy basic consistency
checks)}.

**MCID:** distinguishing GENUINE_THIRD_CHANNEL from the other two outcomes
is the entire content of this claim -- there is no smaller/larger effect
size to calibrate.

## Intercurrent events (ICE)

None -- symbolic/exact algebraic computation (sympy/exact rationals),
no missing data, no stochastic sampling.

## What this result does NOT mean

1. Does NOT, even if GENUINE_THIRD_CHANNEL is found, prove the 8_v channel
   physically appears in the S3xS6 Dirac ACTION (a separate, harder
   question than mere existence of a consistent module -- existence of a
   module is necessary but not sufficient for G67-C3's full closure).
2. Does NOT change N_gen=3's arithmetic (G73) regardless of outcome -- G73
   already assumed algebraic c3-equality across channels; this experiment
   only tests whether a genuine geometric object backing the "vector"
   channel can be built at all, independent of the index arithmetic.
3. If CATEGORY_MISMATCH: does NOT mean G73/G67 are wrong -- it would mean
   G68's own honest statement ("vector rep does not arise from L/R
   multiplication by any standard construction") is confirmed and the right
   framing, not something this experiment failed to find a workaround for.
