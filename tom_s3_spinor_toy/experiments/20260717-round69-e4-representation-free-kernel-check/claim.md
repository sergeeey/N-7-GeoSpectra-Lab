# Round69-E4 Claim — representation-theory-FREE verification attempt of dim ker(D_S6⊗S⁻)=1

**Date:** 2026-07-17
**FL tier:** [x] Full (this is a methodology-audit experiment auditing the
project's headline result; external-facing consequence if it had succeeded:
would upgrade the independence rung of the N_gen=3 kernel-dimension claim)
**Question type:** [x] descriptive

---

## Background / why this experiment exists

The project's headline result `dim ker(D_{S6}⊗S⁻) = 1` (per triality
channel, giving N_gen=3) is currently established by:

- `experiments/20260621-g73-three-channel-dirac/g73_dirac.py` — Atiyah-Singer
  index via Chern-class addition formula + SU(3)/G₂ triality argument
  (topological lower bound: dim ker ≥ 1).
- `experiments/20260621-g74a-lichnerowicz-gap/g74a_lichnerowicz.py` — exact
  count via TWO representation-theoretic ingredients: (Lemma A) a Lichnerowicz
  spectral-gap bound using the SU(3) **Casimir eigenvalue** C₂(3)=4/3 (looked
  up as a standard rep-theory fact, not derived from first principles here),
  and (Lemma B) **Schur's lemma** applied to the G₂-isotypic decomposition of
  the zero-mode space (dim ker ≤ multiplicity of the trivial G₂-rep = 1).
- `experiments/20260714-round59-trivial-rank-certification/` — three routes
  (from-scratch reimplementation, completeness audit, analytic anchor) that
  all explicitly search for the **SU(3)-invariant subspace** of the fibre via
  nullspace of Lie-algebra generator matrices — an explicit-linear-algebra
  computation, but one whose defining move ("find the invariants of a group
  action") is itself the core representation-theoretic operation (this is
  literally how one counts multiplicities via Schur/Peter-Weyl).

Per `reports/100_DIRECTIONS_BRAINSTORM_2026-07-17.md` item 82's correction:
three reimplementations that all bottom out in the same representation-
theoretic decomposition are not mathematically independent verifications of
that decomposition — they would all share the same error if the SU(3)/G₂
branching itself were wrong somewhere. **None of the existing passes
diagonalizes the actual twisted Dirac operator as an explicit matrix without
going through group-representation machinery at some point.**

## Counterfactual Frame

In what world is the headline claim (dim ker = 1, hence N_gen=3) FALSE while
everything currently checked (index=1, Casimir=4/3, Schur multiplicity=1)
stays true? Only if the SU(3)/G₂ branching rule S⁻ = 3⊕1 itself, or the
identification of S⁶'s isotropy representation, contains a shared systematic
error common to every existing check — because every existing check assumes
that branching is correct and reasons *within* it. A genuinely different
verification would need to reconstruct the kernel dimension **without**
assuming that branching, e.g. by diagonalizing an explicit operator matrix on
a concrete finite-dimensional model of the section space.

## Method attempted (see decision.md for full result)

**Route 1 (primary, this experiment): direct explicit construction.**
Build D_{S6}⊗S⁻ as an explicit matrix using:
1. Explicit Cl(6) gamma matrices (8×8, built via Kronecker products of Pauli
   matrices — a hard-coded numeric recipe, verified by direct anticommutator
   computation, not asserted).
2. The ambient Cl(7) trivialization of the spinor bundle of S⁶⊂ℝ⁷ (Γ(x) =
   Σxₐ Γₐ, verified Γ(x)²=|x|²I) — a standard, purely differential-geometric
   device (same "constant ambient spinor restricted to the sphere" trick
   that round59's own Route C used for the Killing-spinor eigenvalue, but
   used HERE as the entire trivialization mechanism, not just to name one
   special vector).
3. An explicit hypersurface (Gauss–Weingarten) spin-connection formula for
   S⁶⊂ℝ⁷ (shape operator = Id for the round sphere — pure Riemannian
   geometry, no group theory).
4. A raw (non-harmonic, non-irrep-labeled) degree≤1 monomial basis {1,
   x₁,…,x₇} tensored with the 8-dim Clifford fibre (64-dim truncation), with
   an EXACT closed-form sphere-moment Galerkin projection (a classical
   Gaussian-integral formula for moments of monomials on Sⁿ — calculus, not
   representation theory) used to project D's output back onto the
   truncation.
5. Direct numerical/symbolic diagonalization (numpy/sympy), no SU(3)/G₂
   label, character, or Casimir value entering anywhere in steps 1-4.

**Mandatory positive control (Perelman-audit no-collapse test) before
trusting this on the twisted operator:** reproduce the ALREADY-KNOWN,
already-cited closed-form spectrum of the UNTWISTED Dirac operator on S⁶
(±(k+n/2), n=6 — Bär 1996 / Camporesi-Higuchi 1996, the same formula G74A's
own script quotes and uses) using this from-scratch machinery, at the
smallest tractable truncation (degree≤1).

## Assumptions

| # | Assumption | Status |
|---|---|---|
| A1 | Ambient Cl(7) trivialization correctly represents S(S⁶) | [VERIFIED] — Clifford relations + Γ(x)²=\|x\|²I checked directly |
| A2 | Hypersurface connection formula ∇ψ=∂ψ+K·Γ(x)ψ (K a free constant standing in for the Weingarten/mean-curvature correction) is the correct formula up to the value of K | [UNVERIFIED — this is exactly what the experiment tests] |
| A3 | Degree≤1 raw-monomial truncation, Galerkin-projected via exact sphere moments, is a legitimate (if crude) finite-dim approximation scheme | [Standard numerical-PDE technique, but truncation error at this low order turned out to be severe — see decision.md] |

## Kill criteria (fixed before running)

| Kill condition | Verdict |
|---|---|
| Degree≤1 Galerkin matrix, for EVERY natural choice of the free coefficient K, fails to reproduce the known untwisted eigenvalue 3 (n/2) | **CALIBRATION FAILURE** — do not proceed to the twisted operator; report NULL, do not force a match |
| Twisted-operator construction cannot be completed/validated given a calibration failure on the untwisted control | **STOP, do not attempt** — an uncalibrated twisted computation would not be trustworthy evidence either way |
| Untwisted control succeeds cleanly, twisted extension gives dim ker ≠ 1 | **REFUTED (this method)** — would require resolving the discrepancy with the representation-theoretic result before either could be trusted |
| Untwisted control succeeds, twisted extension gives dim ker = 1 | **CONFIRMED-REAL, representation-theory-free** — the strong positive outcome |

## What this does NOT mean (pre-registered)

1. A NULL/inconclusive result here does NOT mean dim ker(D_S6⊗S⁻)=1 is false
   — it means this particular from-scratch construction did not reach a
   trustworthy quantitative calibration within the effort invested, which is
   a statement about this experiment's tooling, not about the target claim.
2. Does NOT mean a representation-theory-free verification is impossible in
   principle — only that it was not achieved tractably here; see decision.md
   for concrete next steps (fixing the connection-formula sign/normalization,
   or pursuing the octonion-structure-constant route instead).
3. Does NOT touch L3b (channel independence, external/Tom) or any other open
   conditionality of the N_gen=3 chain.
4. Does NOT constitute a critique of G73/G74A/round59's correctness — their
   representation-theoretic route is not shown wrong by anything here; this
   experiment only establishes that an *independent, non-representation-
   theoretic* confirmation is harder to obtain than it might look.

## Fence

- λ = FREE_COUPLING_PARAMETER (untouched, not referenced here)
- safe_for_runtime = False
- Tom Lawrence: no contact initiated
- Existing experiment folders (`20260621-g73-*`, `20260621-g74a-*`,
  `20260714-round59-*`) were read-only referenced, never modified.
