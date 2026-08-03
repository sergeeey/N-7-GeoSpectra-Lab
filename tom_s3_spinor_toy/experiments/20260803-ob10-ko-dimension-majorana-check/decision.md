# OB10 Decision — geometric S³×S⁶ spinor bundle reality structure

## Verdict

`PASS_PSEUDOREAL_CONSISTENT_WITH_JF`

## What was checked and how

Reused, without modification, the two Clifford constructions already
established elsewhere in this repo:
- S³: `Z_i = i·σ_i`, Cl(0,3), `{Z_i,Z_j}=-2δ_ij`
  (`experiments/20260717-round67-e2-s3-torsion-deformation/e2_s3_torsion_deformation.py:93-107`)
- S⁶: `Γ_1..6`, Cl(6,0), `{Γ_a,Γ_b}=+2δ_ab`, hermitian 8×8
  (`experiments/20260615-s6-harm-g0/s6_harm_g0_clifford.py:38-46`)

and preprint.tex's own stated product formula (`preprint.tex:1467-1480`):
`Γ_full(e_j)=Z_j⊗Γ₇` (3 S³ directions), `Γ_full(f_i)=I₂⊗Γ_i` (6 S⁶
directions), giving a 16-dimensional module and 9 total generators.

All steps run and verified in `ob10_reality_structure.py`
[VERIFIED-sympy]:

**T1 (sanity gate):** re-confirmed both source Clifford algebras and
Γ₇'s properties exactly as coded upstream — all PASS.

**T2 (signature):** built the 9 product generators, verified the full
9×9 anticommutator table (all off-diagonal terms vanish — genuine
Clifford algebra). **Result: signature (p,q)=(6,3)**, i.e. `Cl(6,3)`,
not the uniform `Cl(9,0)`/`Cl(0,9)` that a naive `dim(S³)+dim(S⁶)=9`
count would assume. This is because the two ALREADY-ESTABLISHED
conventions in this codebase use opposite Clifford sign conventions
(`Cl(0,3)` for S³, `Cl(6,0)` for S⁶) — a real, previously-unnoticed
detail, not an error in either individual construction (each is
internally consistent and independently verified in its own prior
round).

**T3 (charge-conjugation search, adversarial-widened):** searched all
256 factorized candidates `B = b_A⊗b_B⊗b_C⊗b_D`, `b_X∈{I₂,σ₁,σ₂,σ₃}`,
for `B·Γ_a·B⁻¹ = η·conj(Γ_a)` holding for **all 9 generators
simultaneously** with **one shared sign η**. **Result: exactly one
candidate found:** `B = σ₂⊗σ₂⊗σ₁⊗σ₂`, `η=−1`, `B·conj(B) = −I₁₆` →
**PSEUDOREAL (quaternionic/symplectic-Majorana type)**, not real.

**T4 (sanity + no-collapse):** confirmed B is Hermitian and unitary
(`B=B†`, `B†B=I₁₆`). Rebuilt the S⁶ factor with an independent,
equally-legitimate Kronecker-factor ordering and re-ran the full
256-candidate search from scratch: **same result** — unique candidate,
`η=−1`, PSEUDOREAL. Reality TYPE (real/pseudo-real/complex) is a
basis-independent invariant of a Clifford-module representation, so
this match under an independent ordering is the expected no-collapse
outcome, not a coincidence, and rules out the result being an artifact
of one arbitrary choice of basis order.

## Interpretation

The geometric S³×S⁶ spinor bundle, built purely from this project's own
already-established, independently-verified gamma-matrix conventions,
**does carry a genuine charge-conjugation structure**, and it is of
**pseudo-real (quaternionic) type** — the same general type as the
finite algebra's own established `J_F²=−1` (also pseudo-real). The two
parts of the construction (geometric and finite/NCG) are therefore
**consistent in reality type**, not contradictory, even though the naive
"KO-dimension 9 mod 8 = 1" arithmetic that `OPEN_BLOCKERS.md`'s own OB10
text proposed as the resolution path turns out not to be the right
calculation — the mixed-signature `Cl(6,3)` product (not a uniform
`Cl(9,0)`/`Cl(0,9)`) is what this repo's own established conventions
actually produce, and it happens to still land in a pseudo-real regime
by direct construction, not by that formula.

## What this does NOT mean (repeated from claim.md, load-bearing)

- Does NOT check `[D_full,B]` or `{D_full,B}` — only the algebraic
  Clifford-module reality type, not a full NCG real-structure axiom on
  the differential operator.
- Does NOT construct a combined `J=B⊗J_F` reality structure for the full
  spectral triple.
- Does NOT touch OB1, OB2, OB4, OB11, or the `N_gen=3` headline — a
  free-standing algebraic classification (per `GLOBAL_RECOMPOSITION_
  AUDIT.md`'s own confirmation that OB10 doesn't feed `D2`'s counting).
- The `Cl(6,3)`-vs-naive-`Cl(9,0)` correction does NOT retroactively
  invalidate anything already established about S³ (`Cl(0,3)`, round67)
  or S⁶ (`Cl(6,0)`, round0/G13) individually — each remains exactly as
  verified in its own prior round; only their PRODUCT's signature was
  previously unstated.

## Next gate (optional follow-up, not required by this claim)

If a future round wants to go further: check whether B commutes or
anticommutes with an explicit differential `D_full` construction (would
require assembling the actual momentum/derivative operators, not just
the gamma matrices used here), and/or attempt an explicit combined
`J=B⊗J_F` and check its own `J²`, `{J,Γ_full⊗γ_F}`, `[D,J]` per standard
NCG real-structure axioms.

## Check (reproduces this derivation)

```
cd experiments/20260803-ob10-ko-dimension-majorana-check
python ob10_reality_structure.py
```
Expect: Cl(0,3)/Cl(6,0)/Γ₇ sanity checks all True; signature (6,3);
exactly 1 charge-conjugation candidate found, η=−1, PSEUDOREAL(-I);
B Hermitian+unitary confirmed; alt-ordering robustness check reproduces
the same PSEUDOREAL(-I), η=−1 result.
