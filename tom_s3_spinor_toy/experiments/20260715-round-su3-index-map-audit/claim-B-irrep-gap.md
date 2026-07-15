---
claim_id: B-irrep-gap
round: 20260715-round-su3-index-map-audit
status: PROVED — conditional on Claim A
---

# Claim B — Irreducible gap theorem

## Question Type
Mathematical / Formal.

## Claim under test

No irreducible SU(3) representation gives index exactly 3:

    I(p,q) > 0  ⟹  I(p,q) = 1  or  I(p,q) ≥ 7

hence I(p,q) ≠ 3 for all (p,q).

## Proof (analytic, per user's derivation — verified below, not re-derived from scratch by me)

Given the formula I(p,q) = (p-q)(p+1)(q+1)(p+q+2)(p+2q+3)(2p+q+3)/120, and
that all factors except (p-q) are strictly positive for p,q ≥ 0:

- I(p,q) > 0 ⟺ p > q.

**Case q=0:** I(p,0) = p(p+1)(p+2)(p+3)(2p+3)/120. At p=1: I=1. For p≥2 this
expression is strictly increasing in p (each factor grows), so
I(p,0) ≥ I(2,0) = 7 for all p≥2.

**Case q≥1:** then p≥q+1 (from p>q, both integers). All positive factors are
minimized at the boundary (p,q)=(2,1), giving I(2,1)=14 as the floor for this
branch.

Combining: I(p,q)>0 ⟹ I(p,q)=1 (only at (1,0)) or I(p,q)≥7 (q=0,p≥2 branch,
floor 7) or I(p,q)≥14 (q≥1 branch, floor 14) — i.e. I(p,q)=1 or I(p,q)≥7.
Since 3 is neither 1 nor ≥7, I(p,q)≠3 for all (p,q).

## Verification performed this round (certificate, not the proof itself)

`certificates/claim_b_gap_verification.py` (sympy):
1. Confirmed I(p,0) symbolically equals the claimed closed form
   p(p+1)(p+2)(p+3)(2p+3)/120.
2. Confirmed strict monotonic increase of I(p,0) for p=1..9 (exact sympy
   values: 1,7,27,77,182,378,714,1254,2079 — matches the "p≥2 increasing"
   step of the proof).
3. Searched q≥1, p≥q+1 branch over q=1..14, p up to q+14 (196 pairs): global
   minimum found is exactly I(2,1)=14, no value below 14 found — consistent
   with (not a substitute for) the claimed minimum-at-boundary argument.
4. Sign-structure sweep over (p,q)∈[0,15]²: I(p,q)>0 ⟺ p>q holds with zero
   exceptions (120 pairs checked in the p>q region, out of 256 total; the
   remaining 136 split as 120 p<q + 16 p=q, both correctly ≤0).

This is a wide numerical control, not a proof of the general monotonicity
argument for all p — but it is consistent with the proof step-by-step and
found no counterexample.

## What this does NOT mean

1. Does NOT independently prove Claim A (I(p,q) actually equals the
   geometric index) — Claim B is conditional on Claim A being true.
2. Does NOT rule out I(p,q)=3 through some OTHER bundle construction not of
   the form E_{p,q} for a single irrep (p,q) — e.g. a reducible bundle could
   still have net index 3, as the S⁻⊗T candidate almost does when combined
   with mirror-sign pieces (see Claim C).
3. Numerical sweep (168 + 210 pairs) is a control, not exhaustive — the
   proof's validity rests on the algebraic monotonicity argument, which
   holds for genuine mathematical reasons (product of strictly increasing
   positive factors), not on the sweep.

## Status

`ANALYTICALLY PROVED, CONDITIONAL ON CLAIM A`
