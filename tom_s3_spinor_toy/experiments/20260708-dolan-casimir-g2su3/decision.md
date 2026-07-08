---
experiment_id: 20260708-dolan-casimir-g2su3
date: 2026-07-08
status: PARKED (not REJECT, not PROMOTE — see below)
---

# decision.md

## Convergent finding (2 independent skeptic rounds, mode=artifact, context-asymmetric)

**Round 1 (on preprint.tex's original argument):** CONFIRMED, HIGH confidence.
"index=1 ⟹ rank 1" at kp_zero_mode.py:426 is a non-sequitur — index of any
linear map C^2→C^1 is automatically dim(domain)-dim(codomain)=1 regardless of
rank (0 or 1). Both scenarios are equally compatible with everything the
preprint actually establishes.

**Round 2 (on the escalated hypothesis that D^2 might be identically zero,
forcing rank=0):** WEAKENED. The "sum of eigenvalue-0 eigenvectors is
eigenvalue-0" linear algebra step is valid, but G-equivariance + Schur's
lemma only forces D^2 to act as Id_{V_rho}⊗M for SOME operator M on the
2-dim multiplicity space — it does NOT force M to be diagonal in the
V_a/V_b split (V_a = singlet in (0,1)⊗(1,0), V_b = singlet in (0,0)⊗(0,0)).
Diagonality of the naive per-summand Casimir formula lambda^2=C2(G)-C2(H)
is a THEOREM for symmetric spaces and for Kostant's cubic Dirac operator on
reductive G/H — but S^6=G2/SU(3) is naturally reductive, NOT symmetric, and
the physically relevant operator is the Levi-Civita Dirac D^g, which differs
from the cubic/characteristic-connection Dirac D^c by a TORSION term
(Clifford multiplication by the G2-invariant associative 3-form). This
torsion term could produce a non-zero off-diagonal coupling M_{ab} between
V_a and V_b that the naive Casimir-difference argument does not see either
way (it neither proves nor disproves the coupling).

## Kill Analysis (per Anti-Overfitting Gate / OSA)

**What was killed:** The claim that "L4B is proved" via the argument given in
kp_zero_mode.py / preprint.tex §4.2 as currently written. Neither rank=0 nor
rank=1 is established by the stated argument (global index + KP gap on
non-trivial components + naive per-summand Casimir diagonality assumption).

**What was NOT killed:** The possibility that rank=1 (the paper's claim) is
actually correct — it may well be, but for a DIFFERENT reason than currently
stated (an explicit non-vanishing torsion cross-term, or an explicit
non-degeneracy of the relevant spinor pairing), not yet computed.

**Relaxation map:** the crux question has been narrowed from "is dim ker
1 or 2, for unspecified reasons" (Round 1) to the single, well-posed,
computable question: "does Clifford multiplication by the G2-invariant
3-form T produce a non-zero matrix element between the V_a-derived and
V_b-derived basis vectors of the 2-dim trivial multiplicity space?" This is
a concrete, finite computation (not a fishing expedition) — it requires the
explicit torsion tensor / associative 3-form on G2/SU(3) (already used
elsewhere in this project's KP-formula infrastructure, e.g. Agricola 2002
cited in kp_zero_mode.py) and explicit spinor harmonic representatives for
V_a and V_b.

## Why PARKED, not pursued further today

This computation requires real differential-geometric care (explicit
torsion 3-form action on specific Clifford-module elements) beyond what can
be responsibly rushed in one sitting without risking a THIRD layer of
unverified claims stacked on the first two. Cost/benefit: the preprint's
public-facing claim can and should be fixed NOW (downgrade "L4B, proved" to
explicitly open, matching the honesty standard already applied to L3b/L4A
today) independent of whether the deeper torsion computation ultimately
vindicates rank=1 or not.

## Revival condition
Resume when: (a) explicit torsion/Clifford-multiplication formulas for
G2/SU(3) spinor harmonics are set up carefully (dedicated session, not a
rushed addendum), or (b) Dolan's Casimir-operator method (already cited in
preprint.tex as untried for G2/SU(3)) is implemented as a full independent
cross-check, whichever is cheaper once scoped properly.

## Pearl
observation: the paper's own pre-existing "torsion correction" open item
(E-KP1 claim.md) was more consequential than its own author (this project,
in a past session) realized — it is not a minor correction to an established
result, it is the actual open crux determining whether the central kernel
count is 1 or 2.
falsifiable_prediction: an explicit torsion cross-term computation will
either (a) vanish, vindicating rank=1 as claimed, or (b) be non-zero,
forcing dim ker(D+)=2 and requiring re-derivation of the "one zero mode per
triality channel" picture underlying N_gen=3's whole framing.
trigger_condition: next dedicated session on this specific computation.
next_check: before any further public claim building on L4B's current
"proved" status.
