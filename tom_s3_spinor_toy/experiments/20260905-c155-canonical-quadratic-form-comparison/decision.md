# C155 — Decision

**Date:** 2026-09-05. **Tier:** FL Full. **L0:** descriptive.
**Verdict: REJECT the `|c| = (2/3) mu` universal-identity hypothesis, with a
structural mechanism — plus three surviving positive statements about
`SU(3)/T^2`.**

## Pre-registered predictions vs outcome

| # | pre-registered | outcome |
|---|---|---|
| **P1** | `Q_c` and `Q_mu` NOT proportional on `SU(3)/T^2` | **HELD** — and more strongly than predicted: they have different RANKS (6 vs 2), so no normalisation can relate them |
| **P2** | failure concentrated in cross-plane entries; diagonal blocks proportional with a common `k` | **HELD in substance** — per-direction diagonal ratios are all equal (2), and the whole difference sits in the off-diagonal structure: `Re(G_c)` has NO off-diagonal, `Re(G_mu)` has 12 nonzero off-diagonal entries |
| **P3** | `S^6` control passes (vacuous) | **HELD after a test correction** — see below |

Predictions were written before any number was computed and are unedited.

## What was found (all exact sympy, no floats)

In a genuinely `V`-orthonormal basis (`Gram(family_sym) = 4*I_6`, so the family
basis was already orthogonal with equal norms):

    S^6         : Q_c = (4/9) Q_mu        both rank 2 of 2   -- FORCED, vacuous
    SU(3)/T^2   : Q_c = 2 * ||v||^2       rank 6 of 6   (isotropic, injective)
                  Q_mu                    rank 2 of 6   (kernel 4-dimensional)

1. **No universal identity exists.** Two quadratic forms of different rank
   cannot be proportional. The `2/3` value is an artifact of `S^6`'s family
   being 1-complex-dimensional, where any two `C`-linear maps are automatically
   proportional. This closes the line opened in C147 and left INCONCLUSIVE by C154.
2. **A 4-dimensional space of admissible `T^2`-equivariant connections
   annihilates the invariant spinor**: `D_Sigma(v) psi_+ = 0` verified as an
   exact 8-component vector identity for a kernel basis AND for a random
   rational combination outside it. The same connections have `||c||^2 != 0`.
3. **`c` is injective** on the admissible family — its zero locus on
   `SU(3)/T^2` is exactly `{0}`. (C147 asked this question on `S^6`.)
4. **Mechanism, directly tested rather than narrated**: the three root planes
   are mutually **HS-orthogonal** for `c` (all cross-block pairings exactly 0)
   but map onto **one common real 2-plane** for `mu` (signs `(+,-,+)`, verified
   separately on even and odd directions).

## Three of my own sub-hypotheses were falsified during the round

Recorded because they were mine, not an opponent's:

| # | sub-hypothesis | how it died |
|---|---|---|
| 1 | compare full **Hermitian** Gram matrices | `S^6` positive control FAILED. `V` is a real vector space, so only `Re(G)` enters the quadratic form. Test corrected; `Im(G)` now reported separately (nonzero for `c`, identically zero for `mu`) |
| 2 | `M` is `C`-linear per block, image is a **complex line** | Step 4: `M(dir1)` is not a complex multiple of `M(dir0)`; `rank([M0 M1 | i*M0]) = 3`, so the shared 2-plane is NOT closed under `i`. Wording withdrawn; the rank-2 result never depended on it |
| 3 | the sign pattern `(+,-,+)` is the **`A_2` root relation** | Step 5: weights are `(-2,1), (1,1), (1,-2)`; the vanishing relation is `(1,1,1)`, but the `mu` coefficient functional is `(1,-1,1)`. They differ by a sign on one plane. A single orientation flip would reconcile them — which is exactly why this is NOT claimed: re-labelling until it fits is the forbidden move. **FALSIFIED as stated; open question** |

Sub-hypothesis 3 was the one that would have generalised (a prediction for other
flag manifolds). Its death is the main reason this round is a settlement rather
than a discovery.

## Novelty check (Step -3, run before writing this)

* The dimension of the space of invariant spinors on maximal flag manifolds is
  **published**: Artacho–Semmelmann, *Invariant Spinors on Flag Manifolds*
  (arXiv:2407.08493), Theorem 6(1) gives a lower bound `2^floor(n/2)`, i.e. 2 for
  `A_2` — matching the 2 computed here. **Not new.**
* Standard nearly-Kahler background used and NOT claimed as new: Kirichenko
  (characteristic torsion is parallel), Friedrich–Ivanov (`NK^6` Dirac
  eigenvalues `∓||T|| = ∓sqrt(2 Scal/15)`).
* That same paper does **not** treat the Dirac operator on invariant spinors,
  nor which invariant connections annihilate one. The rank/kernel statement
  above was not found in the nearest literature checked — but "not found in the
  papers I checked" is `[WEAK]` evidence of novelty, not a novelty claim.

## Honest assessment of significance

This is a **decisive negative result with a verified mechanism**, plus three
small positive structural facts about one homogeneous space. It is **not** a
discovery of new mathematics: both structures look symmetry-forced (weight
orthogonality, Weyl `S_3`, and the `C`-linearity already registered in C153),
and the one hypothesis that would have generalised was falsified in Step 5.

Its value is that it **ends** a question this project pursued across C147, C154
and C155 — and ends it structurally (different ranks) rather than numerically
(numbers failed to match), so it cannot be revived by a different choice of norm.

## What this does NOT establish

1. Nothing about `N_gen = 3` or any physical claim.
2. Nothing about `lambda` — still `FREE_COUPLING_PARAMETER`.
3. Not a theorem for all nearly-Kahler 6-manifolds: two homogeneous examples in
   fixed conventions. The dimensional-artifact argument is general; the
   computations are not a proof for arbitrary `G/H`.
4. The `S^6` positive control is vacuous by construction and its passing is not
   evidence for anything.

## Reproduce

```
python c155_step1_gram_forms.py          # the two canonical forms, both spaces
python c155_step2_kernel_and_forcing.py  # explicit kernel, verified as identities
python c155_step3_basis_independence.py  # isotropy is not a basis artifact
python c155_step4_mechanism_test.py      # mechanism; falsifies sub-hypothesis 2
python c155_step4b_addendum.py           # corrected mechanism statement
python c155_step5_root_structure.py      # falsifies sub-hypothesis 3
```

## Skeptic (FL Step 8a) — Response Matrix

Context-blind pass, given claim.md + code only, no session history. It reported
honestly that **it had no runnable Python** and derived everything by reading.
Under `audit-verification-gate.md` its `[CONFIRMED-REAL]` is only `[HYPOTHESIS]`
here, so every actionable point was re-checked with a tool (`c155_step6`).

| # | skeptic point | my tool verification | response |
|---|---|---|---|
| A1 | central rank claim survives; but the union map `v -> (D(v)psi_+, D(v)psi_-)` was **never run** — it predicted rank **4** "by chirality" | **RAN IT: rank = 2, not 4.** The skeptic's prediction is **wrong** | **Concern resolved, result STRENGTHENED** — see below |
| A2 | `D8_of` is the full untwisted Dirac, identical to C154 Step B's | matches by inspection; `mu(LC)=3` gate passes | Accepted |
| A3 | `C` injective since `Re(G_c)` positive definite | re-verified `Re(G_c)=2I` in a V-orthonormal basis | Accepted |
| A4 | hand-derived `Q_mu = 4(a0-a2+a4)^2 + 4(a1-a3+a5)^2` | **VERIFIED EXACTLY** in sympy on a symbolic 6-parameter connection | **Accepted and adopted as a headline result** |
| A5 | family really is the full 6-dim equivariant space | argument accepted; independent regression is C153's own LC-in-family check | Accepted |
| A6 | `-T2_M` sign convention almost certainly right, `[WEAKENED]` (could not run) | three internal gates (`sector dims 3,3`, `mu(LC)=3`, C152's `[D,G]=0`) all pass | Accepted as correct |
| **F1** | the log line printed `sqrt(6)/3` annotated `(2/3)` — misleading | **valid defect, confirmed** | **FIXED** — the line now states `sqrt(6)/3 = 0.816.. is NOT 2/3`, and separately reports the squared-form ratio |
| **F2** | Step 3 only rescales a `Gram=4I` basis, so it cannot tell "isotropic" from "already diagonal" | **DISMISSED WITH EVIDENCE**: conjugated `Q_c` by an exact rational orthogonal matrix that genuinely mixes planes A-B and B-C; `Re(G_c)` is **still exactly `2*I`** | Concern is mathematically unfounded (equal diagonal in an ORTHONORMAL basis *is* isotropy) but now settled by direct test rather than by argument |
| **F3** | "no universal identity" is scoped to the REAL parts; `Im(G_c) != 0` while `Im(G_mu) = 0` is unused information | correct as stated | **Accepted as a scope limitation**, added to "does NOT establish" |

**No concern dismissed without evidence. One skeptic prediction falsified.**

### The strengthening that came out of the test the skeptic could not run

`rank(v -> (D(v)psi_+, D(v)psi_-)) = 2`, the same as for `psi_+` alone. So the
collapse is **not per-spinor**: the **same 4-dimensional family of connections
annihilates the ENTIRE space of `T^2`-invariant spinors simultaneously**, not
just the chosen Killing eigenvector. This is a cleaner statement than the one in
claim.md's first version and does not depend on which invariant spinor is called
`psi_+` — which was precisely the skeptic's Attack 1 worry, now closed.

### Closed form (verified, adopted)

    Q_mu(v) = 4 (a_0 - a_2 + a_4)^2 + 4 (a_1 - a_3 + a_5)^2      [rank 2]
    Q_c(v)  = 8 (a_0^2 + a_1^2 + a_2^2 + a_3^2 + a_4^2 + a_5^2)  [rank 6]

in the raw family basis. The rank gap is now visible by inspection, and the
kernel `{a_0 = a_2 - a_4, a_1 = a_3 - a_5}` is exactly the 4-dimensional space
exhibited and verified in Step 2.
