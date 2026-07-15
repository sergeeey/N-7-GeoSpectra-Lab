# Round decision — SU(3) index map and exact-chirality audit

**Date:** 2026-07-15
**Depends on (cited, not reopened):** `../20260715-index-formula-s-tensor-t-candidate/`
(PRIOR RESULT: ind(D⊗(S⁻⊗T^{1,0}S^6))=7, REJECT verdict for that candidate)

## Final status per claim

| Claim | Status |
|---|---|
| A — general index-map identity | `SUPPORTED ON CONTROLS — GENERAL PROOF OPEN` (evidence is 1 geometric method checked at 3 points, not 2 independent derivations — see correction in claim-A) |
| B — irreducible gap theorem (I≠3) | `ANALYTICALLY PROVED, CONDITIONAL ON CLAIM A` (PROOF = case analysis + monotonicity, kept explicitly separate from the sympy sweep, which is a CONTROL only) |
| C — exact-chirality obstruction | `PROVED FOR ALL G2-INVARIANT-CONNECTION-INDUCED HOMOGENEOUS TWISTED DIRAC OPERATORS` (upgraded from "chosen block-diagonal connection" — Clebsch-Gordan certificate shows block-diagonality is FORCED, not chosen). `GENERAL SYMMETRY-BREAKING / NON-INVARIANT EXTENSIONS: OPEN.` `INDEX-ZERO SECTORS: OPEN.` |

## Why this is an independent strengthening of G102, not a duplicate

G102 exhausted the internal G₂-equivariant continuous-symmetry/centralizer
search space inside so(8) (dim c_so(8)(g₂)=0) — the "is there a hidden
Spin(8) symmetry acting on the geometry itself" route. This round closes a
DIFFERENT route: whether any single irreducible SU(3) representation-theoretic
twist, or any standard reducible combination of such twists, could realize a
clean index-3 (or exact (3,0)-kernel) construction by representation-ring
arithmetic alone. Claim B rules out the former for all (p,q). Claim C rules
out the latter for the standard operator class. Neither route was addressed
by G102's centralizer computation, which was about symmetries of the geometry,
not about index arithmetic over the representation ring.

## Kill Analysis (Anti-Overfitting Gate)

**What this kills:**
- Any hope that a SINGLE irreducible SU(3) twist realizes index exactly 3
  (Claim B, proved conditional on A).
- Any hope that a STANDARD (block-diagonal-connection) reducible bundle with
  mixed-sign irreducible summands realizes an exact (3,0) kernel without
  extra mirror zero modes (Claim C, proved for that operator class).

**What this does NOT kill:**
- The general index-map identity (Claim A) is not proved for all (p,q) —
  only supported by 3 exact points from ONE geometric method + sign-consistency
  sweeps. A future counterexample at some untested (p,q) would fully undercut
  this round. (Corrected this round: the earlier claim of "two independent
  derivations converging" was wrong — hand Chern-root calc and its sympy
  realization are one method, not two.)
- Claim C's upgrade only closes the G2-INVARIANT-CONNECTION route (block
  diagonality is forced for any such connection, proved via Clebsch-Gordan).
  A non-invariant/symmetry-breaking extension (explicit background field,
  Higgs-type coupling) is NOT ruled out and requires its own justification —
  this door was never claimed closed, and remains explicitly open.
- Index-zero residual sectors (E_0 in any E≅3^⊕3⊕E_0 decomposition) are not
  shown to have vanishing kernel — open.

**Relaxation map:**
- Claim A → close via the genuinely independent Path B: representation-ring
  route R(SU(3))→K^0(S^6)→ℤ (recursion 3⊗(p,q)=(p+1,q)⊕(p−1,q+1)⊕(p,q−1), or
  a direct-sum-of-weight-cubes construction), cross-checked against ≥2 more
  explicit geometric (Chern-root) constructions at NEW (p,q) points.
- Claim C's remaining open door (non-invariant extensions) → requires
  introducing and justifying an explicit symmetry-breaking term Φ (origin,
  symmetries, exact spectral effect) — a new physical structure, not a
  computation this round can close.
- Index-zero sectors → close via an explicit Lichnerowicz/Weitzenböck-type
  lower bound (method already used successfully in G74A for a related
  vanishing argument).

## Provenance

Claim structure (A/B/C split), the exact-chirality re-scoping (Schur's lemma
insufficient for first-order symbols), the analytic gap proof for Claim B,
the index-zero-sector caveat, the Clebsch-Gordan strengthening of Claim C
(m*_ℂ⊗3̄ and m*_ℂ⊗6 decompositions), and the Claim-A independence correction
were all proposed by the user, building on the external-analysis-derived
candidate closed in the prior experiment. This round's contribution:
independent verification of each sub-claim by a DIFFERENT computational route
than the one used to derive it —
sympy Chern-root/formula checks for Claim B's gap theorem and the Claim C
worked example, and a from-scratch GL(3) Pieri-rule implementation (not the
memorized SU(3) product tables) for the Clebsch-Gordan decompositions — none
of the user's algebra was re-derived by rote acceptance; every check found
zero counterexamples/mismatches.

## Pearl closure

The pearl logged in `pearl_registry/INDEX.md` (2026-07-15,
round-su3-index-map-audit) asked whether Hom_{SU(3)}(m*_ℂ⊗3̄, 6) vanishes.
Answer: yes, confirmed both directions (also Hom_{SU(3)}(m*_ℂ⊗6, 3̄)=0). Pearl
status updated from `pending` to `resolved` — see registry entry.

## Cost

~35 minutes total: two sympy certificate scripts (gap-theorem sub-checks,
worked-example kernel bound) plus one from-scratch GL(3)-Pieri combinatorial
implementation (Clebsch-Gordan certificate) — no new physical construction.

## Files

- `frozen-scope.md`, `assumptions.md` — shared scope/assumptions across A/B/C
- `claim-A-index-map.md`, `claim-B-irrep-gap.md`, `claim-C-exact-chirality.md`
- `certificates/claim_b_gap_verification.py` — exit 0, all asserts pass
- `certificates/claim_c_invariant_connection_cg.py` — exit 0, all asserts pass
- `controls/worked_example_6_plus_3bar4.py` — exit 0, all asserts pass
