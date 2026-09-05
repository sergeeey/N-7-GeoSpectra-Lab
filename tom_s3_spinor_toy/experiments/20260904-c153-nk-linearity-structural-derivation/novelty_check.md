# C153 novelty check — run 2026-09-04, POST-hoc (before building C154, per user instruction)

**Why post-hoc, not pre-hoc (honest process note):** this project's own AI-Hypothesis
Pre-Gates (`falsification-ladder.md` Steps -4/-3) call for a novelty check BEFORE
building, not after promoting. It was not run before C153. The user caught this gap
explicitly: before authorizing a C154 build around "explain the per-plane law via
Weyl orbit", they asked for a literature check first — "если да, C154 надо
формулировать уже вокруг недостающего звена". Run via `skeptic-auditor`, WebSearch +
arXiv, no session context given beyond the two questions below.

## Verdict: NOT NEW, on both fronts

### Q1 — the 6-vs-2 / Weyl-orbit characterization of the 8 invariant a.c.s.

**Classical, three independent citations:**

- **Borel–Hirzebruch (1958), §13.7** (the origin). Invariant a.c.s. on `G/H` ↔ a
  sign `ε` per complementary root; integrable ⟺ some ordering of the Cartan
  coordinates makes the `ε`-selected roots positive and closed. For `SU(3)/T²`:
  integrable ⟺ `ε` lies in a Weyl chamber; the 2 all-agree patterns are exactly
  the ones no ordering realizes.
- **Burstall–Salamon, "Tournaments, flags and harmonic maps"**, Math. Ann. 277
  (1987) 249–265. Invariant a.c.s. on `F(n) = U(n)/T` ↔ tournaments on `n`
  vertices; integrable ⟺ the tournament is the canonical transitive one.
  Transitive tournaments on 3 vertices = `3! = 6 = |S₃| = |W(SU(3))|`; the
  remaining 2 (the 3-cycles) are the all-agree pair.
- **Explicit for `F₃`**: arXiv:2411.07767 §5.2 — "three of our almost-complex
  structures are integrable and one is not" (up to `J↔−J`, i.e. 6 vs 2), and
  "the Weyl group `S₃` of `sl₃` acts transitively on the set of bases for `Δ`,
  and hence on the set of covariant almost-complex structures."

The non-integrable pair being the canonical nearly-Kähler structure is
Wolf–Gray/Butruille (already used in C140), not new here either.

### Q2 — the per-plane multiplicative law `i^{eps_k}`

**Not new, and structurally forced, not a fact about our operator at all.**

1. The `±i`-per-root-space action is **the definition itself**: Borel–Hirzebruch's
   own parametrization assigns each complementary root `β_j` a sign according to
   whether the a.c.s. acts as `+i` or `−i` on `𝔤_{±β_j}`. Burstall–Salamon's
   tournament is defined the same way.
2. `m` for a full flag manifold decomposes into pairwise-**inequivalent**
   irreducible 2-dim `T`-summands (multiplicity one, one per positive root) —
   the standard fact behind every invariant-metric/Ricci computation on flag
   manifolds. **Schur's lemma then forces any `T²`-equivariant map to respect
   this splitting**, with no reference to Dirac operators, torsion, or
   nearly-Kähler geometry. `c` is `T²`-equivariant by construction (it lives on
   a `T²`-invariant sector), so the per-plane law was **guaranteed before any
   computation ran**.

No paper stating this specifically for a twisted-Dirac connection-coefficient
map was found — because none is needed; it follows from (1)+(2) alone.

**Searched, found nothing on point:** Dirac-operator-specific per-plane
phrasing; 3-symmetric-space/twistor literature (arXiv:math/0604394); Agricola's
naturally-reductive connection family (arXiv:math/0202094, `t=1/3` = Kostant
cubic Dirac) — relevant background, not this statement.

**Bibliographically located, text not read (not cited as verified):** San
Martin & Negreiros, *Invariant almost Hermitian structures on flag manifolds*,
Adv. Math. 178 (2003) 277–310; Arvanitoyeorgos, *Geometry of flag manifolds*,
IJGMMP 3 (2006) 957–974 — plausible textbook sources for Q2, not consulted.

## Consequence for C153's claim

Every clause of `claim.md` items 1–3 (the per-plane law, its 2-of-8
corollary, and the Nijenhuis correlation) is **entailed by standard
representation theory + a 1958/1987 classical theorem**, not discovered by
this round. C153's actual, still-real contribution shrinks to: an
**independent exact verification** that this specific operator conforms to
the generic pattern (a legitimate but much weaker claim than the "headline
structural discovery" the original `claim.md`/`decision.md` framed it as),
plus locating the references that make it expected rather than surprising.

This is the same *class* of correction as C144's ("algebraically forced by
total antisymmetry, so the real discriminating test was elsewhere") — kept
in place, corrected in place, per this project's discipline. See `claim.md`'s
appended correction and `CLAIM_LEDGER.yaml`'s updated `caveat` field.

## What remains genuinely open (candidate framing for what a real C154 would need)

NOT "why does the per-plane law hold" (answered: it doesn't need explaining).
What is NOT explained by any classical result found here: the actual
**values** `c(v_k)` — e.g. why `S⁶`'s coefficient is `-2√3/3` and
`SU(3)/T²`'s are the specific rationals found in C152/C153, and whether
there is a reason connecting the two beyond "both were computed exactly".
The generic equivariance argument says the SIGN factors per plane; it says
nothing about the MAGNITUDE, which is where any remaining physics/geometry
content would have to live.
