# Estimand — G98: B-L as isometry vs. holonomy charge

**Date:** 2026-07-01
**FL tier:** Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

## Background

G97 (2026-06-26) searched for a B-L generator inside the Cartan of
Iso(S3xS6) = SO(4) x SO(7) and found none, concluding the U(1)_Y gap is
"OPEN, needs Tom Part 4/5". G97's own text (Step 5) explicitly flags an
UNTESTED candidate: "B-L could come from U(1) subset SO(7)\G2" but never
computes it.

Separately, G15 (2026-06-19, part of the ORIGINAL NCG/spectral-triple route,
not the isometry route) already constructed an explicit B-L operator
BmL = -(1/3)(sigma3_1+sigma3_2+sigma3_3) on the 8-dim S6 spinor, built from
the SO(6)=SU(4) local spin/holonomy structure (via g10_s6_so6_gauge.py),
and verified (12/12 tests, PASS_G15_BL_GEOMETRIC_ORIGIN) that it reproduces
the correct SM hypercharge table.

These two facts look contradictory (B-L exists per G15, B-L absent per G97)
unless the two routes are checking DIFFERENT algebras: G97 checks the full
isometry algebra so(7) (dim 21); G15's B-L lives in so(6) subset so(7)
(dim 15), the ISOTROPY subalgebra at a point of S6, not the full isometry
algebra. This is a known CSDR distinction: gauge bosons come from ISOMETRY
generators; internal R-symmetry/holonomy charges (like B-L here) come from
the SPIN CONNECTION / structure group of the spinor bundle, which is only
the isotropy subgroup, not the full isometry group.

## Estimand

**Population:** the Lie algebra so(7) = Lie(Iso(S6)), acting on the 8-dim
real spinor representation via the Clifford construction already used in
G11/G15 (Gamma_1..Gamma_6 from G_so6, Gamma_7 = kron(s3,s3,s3)).

**Intervention:** split so(7) into so(6) (15 generators J_ab = [Gamma_a,Gamma_b]/4,
a,b in 1..6 -- the isotropy subalgebra already partially used by G15/G11) and
the coset so(7)/so(6) (6 generators K_a = [Gamma_a,Gamma_7]/4, a in 1..6 --
never constructed or tested before in this repo).

**Comparator:** G97's implicit assumption that "B-L generator" would have to
appear as a Cartan direction of the FULL so(7) (equivalently: must commute
with ALL 21 generators, not just the 15 isotropy ones).

**Endpoint:** for BmL (G15's operator), does [BmL, X] = 0 for X ranging over
(a) all 15 so(6) generators, and (b) all 6 coset generators K_a?

**Summary measure:** two booleans -- commutes_with_so6 (expected: True),
commutes_with_coset (the actual open question).

**MCID:** a single non-zero commutator [BmL, K_a] for any a is sufficient to
establish that BmL is NOT so(7)-invariant (only so(6)-invariant) -- this is
the whole content of the claim, there is no smaller/larger effect size to
calibrate against.

## Intercurrent events (ICE)

None applicable -- this is a pure algebraic/symbolic computation (sympy),
no missing data, no dropout, no stochastic sampling.

## Natural language statement

We estimate whether the B-L generator (G15) commutes with the isotropy
subalgebra so(6) subset so(7) (population: the 21-dim Lie algebra so(7) in
its 8-dim spinor rep), comparing the so(6) block against the so(7)/so(6)
coset block, with no ICE (deterministic symbolic algebra).

## What this result does NOT mean

1. Does NOT prove U(1)_Y is fully derived from geometry -- T3_R (SU(2)_R
   Cartan) + B-L (SO(6) holonomy charge) still requires an external
   combination rule (Pati-Salam Y=T3_R+(B-L)/2) that is itself not derived
   from the isometry+holonomy structure alone.
2. Does NOT reconcile the SU(4) vs SO(6) representation-theoretic mismatch
   noted in G97 Step 5 (Pati-Salam formally wants SU(4), we only have SO(6);
   SO(6)=SU(4) as groups, but the EMBEDDING into the fermion representation
   needs separate checking, not addressed here).
3. Does NOT change the sm_derivation_claimed=False status -- this experiment
   clarifies WHY G97 found no B-L in the isometry Cartan, it does not supply
   a new B-L-from-isometry mechanism.
