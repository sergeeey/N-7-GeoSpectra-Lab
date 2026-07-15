---
claim_id: C-exact-chirality
round: 20260715-round-su3-index-map-audit
status: PROVED for ALL G2-invariant-connection-induced homogeneous twisted Dirac operators — symmetry-breaking extension OPEN
---

# Claim C — Exact-chirality obstruction (precisely scoped)

## Question Type
Mathematical / Formal.

## Why this claim needed re-scoping (the correction that drove this round)

The original phrasing ("SU(3)-equivariance ⟹ block-preserving, by Schur's
lemma") is too broad. Schur's lemma forbids a nonzero ZERO-ORDER intertwiner
V_i→V_j between inequivalent irreps. It does NOT forbid a general equivariant
FIRST-ORDER differential operator with symbol built from the tangent
representation, T*S^6⊗V_i→V_j, which can be nonzero even for i≠j whenever
T*S^6⊗V_i contains a copy of V_j. So "equivariant ⟹ block-preserving" is
false as a blanket statement; it is true only for a specific, standard
construction.

## Claim under test (precisely scoped)

For the STANDARD homogeneous twisted Dirac operator built from a
block-diagonal connection,

    ∇_E = ⊕_i ∇_{E_i},     D_E = c∘∇_E = ⊕_i D_{E_i}    (by construction),

a reducible bundle E=⊕E_i combining irreducible summands of mixed-sign index
cannot have exact kernel dimensions (dim ker D_E⁺, dim ker D_E⁻) = (3,0) (or
any exact realization of a small net index with zero mirror modes) — it
necessarily carries EXTRA paired zero modes from each summand's own index.

This holds by construction (direct sum of operators ⟹ direct sum of kernels),
not by an appeal to Schur's lemma on the full operator.

## Worked example: E = 6 ⊕ 3̄^⊕4

Using Claim A's values (I(6)=7, I(3̄)=-1, conditional on Claim A):

    D_E = D_6 ⊕ D_{3̄}^⊕4
    ind(D_6) = 7    ⟹  dim ker D_6⁺ ≥ 7  (assuming ind gives a lower bound on the larger side)
    ind(D_{3̄}) = -1 ⟹  dim ker D_{3̄}⁻ ≥ 1 per copy ⟹ dim ker D_{3̄^⊕4}⁻ ≥ 4

    ⟹ dim ker D_E⁺ ≥ 7,  dim ker D_E⁻ ≥ 4

Net index = 7 - 4 = 3 (matches the naive "net index 3" target), but the
actual kernel has at least 11 total zero modes, not an exact (3,0). This is
a strict FAIL for exact-chirality within the frozen standard-operator class.

## What does NOT refute this result

If a later construction introduces an off-diagonal background term,

    D_E → D_E + Φ,     Φ: pairing 4 positive-chirality with 4 negative-chirality modes,

this is NOT a counterexample to the claim above — it is a DIFFERENT operator,
outside the frozen standard block-diagonal class. Using it requires a
separate justification: origin of Φ, its symmetries, and its exact spectral
effect (does it really lift exactly 4+4 modes, leaving (3,0)? or does it
leave residual modes?). This is explicitly out of scope for Claim C and is
listed as the open extension below, not something this claim rules out or
rules in.

## Upgrade: block-diagonality is FORCED for every G2-invariant connection, not just the chosen one

The open extension above asked whether T*S^6⊗3̄ (≅ isotropy rep m*_ℂ⊗3̄, since
T*S^6 at a point is the complexified isotropy representation m*_ℂ of
SU(3)⊂G₂) contains a copy of 6 — i.e. whether Hom_{SU(3)}(m*_ℂ⊗3̄, 6) is
nonzero, which would allow an invariant off-diagonal connection component
mixing the 6 and 3̄^⊕4 blocks.

**Computed and independently re-verified this round** (via a from-scratch
GL(3) Pieri-rule implementation, not by trusting memorized SU(3) tables —
`certificates/claim_c_invariant_connection_cg.py`, exit 0):

    m*_ℂ ≅ 3 ⊕ 3̄   (standard fact for the nearly-Kähler isotropy rep)
    m*_ℂ ⊗ 3̄ = (3⊗3̄) ⊕ (3̄⊗3̄) = (8⊕1) ⊕ (6̄⊕3) = 1⊕3⊕6̄⊕8

    6=(2,0) does NOT appear (only 6̄=(0,2) does — a DIFFERENT, inequivalent
    irrep) ⟹ Hom_{SU(3)}(m*_ℂ⊗3̄, 6) = 0.

    Reverse direction, also checked: m*_ℂ⊗6 = (3⊗6)⊕(3̄⊗6) = (10⊕8)⊕(15⊕3)
    3̄=(0,1) does NOT appear ⟹ Hom_{SU(3)}(m*_ℂ⊗6, 3̄) = 0.

**Why this matters:** per Wang's theorem, a G₂-invariant connection on the
homogeneous bundle associated to E=6⊕3̄^⊕4 differs from the canonical
(reductive) connection by an SU(3)-equivariant map m_ℂ⊗E→E. The off-diagonal
piece of any such map mixing the 6 and 3̄^⊕4 blocks would have to be an
element of Hom_{SU(3)}(m*_ℂ⊗3̄, 6) ⊕ Hom_{SU(3)}(m*_ℂ⊗6, 3̄). Both vanish.
**No G2-invariant connection — canonical or otherwise — can mix these two
blocks.** Block-diagonality is forced, not chosen.

Mixing WITHIN the four identical copies of 3̄ (an internal GL(4,ℂ) flavor
rotation) remains possible and unconstrained by this argument, but it cannot
move modes between the 6-block (positive chirality) and the 3̄^⊕4-block
(negative chirality), so it does not touch the dim ker D_E⁺≥7,
dim ker D_E⁻≥4 bound.

## Remaining open extension (genuinely out of scope, not closed by the above)

The upgrade above only rules out MIXING VIA A G2-INVARIANT CONNECTION. It does
NOT rule out:
- A non-invariant background (explicit symmetry breaking).
- A Higgs/flux-type term added to the operator by hand.
- Any zero-order Clifford-odd term not arising from a connection at all.
- A more general Dirac-type operator not built from ANY connection on this
  bundle (e.g. a genuinely different differential operator construction).

Any of these must be introduced and justified as a NEW physical structure
(D_E → D_E + Φ, with Φ's origin, symmetries, and exact spectral effect
established separately) — not something this framework produces for free.

## Index-zero sectors (separate open gap, also flagged by the round)

ind(D_{E_0})=0 does NOT imply ker(D_{E_0})=0 in general (dim ker D⁺=dim ker D⁻=k
for any k≥0 is consistent with index 0). So the strongest currently-defensible
statement about any residual sector E_0 (e.g. after subtracting 3^⊕3 from a
larger construction) is:

    E ≅ 3^⊕3 ⊕ E_0,   with ker(D_{E_0}) STATUS UNKNOWN — requires a separate
    vanishing argument (explicit spectrum, or a Lichnerowicz/Weitzenböck-type
    lower bound as in G74A), not assumed.

The presence of E_0 may also enlarge the commutant / create additional
physical sectors even if its zero modes vanish — a further open question, not
addressed here.

## Status

`PROVED FOR ALL STANDARD HOMOGENEOUS TWISTED DIRAC OPERATORS INDUCED BY`
`G2-INVARIANT CONNECTIONS (block-diagonality is forced, not chosen — see`
`Clebsch-Gordan certificate above).`
`GENERAL SYMMETRY-BREAKING / NON-INVARIANT EXTENSIONS: OPEN.`
`INDEX-ZERO SECTORS: OPEN — requires vanishing test.`
