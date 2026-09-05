# C158 — `ker(M)` is `W(A_2)`-invariant, and splits as `2·standard`

**Question type (EstimandOps L0): DESCRIPTIVE.** Tier: FL Full.
**Mandate (standing):** autonomy over search/computation/hypothesis-switching;
NOT over declaring "discovery" — needs theorem + out-of-sample test + null
model + novelty audit + independent skeptic pass, ALL FIVE.

> ## ⚠️ MAJOR CORRECTION (2026-09-05, same session, after Steps 3-4 completed)
> **This file's own headline (G4 + isotypic decomposition) is retroactively
> FORCED by facts proven LATER in the same round (Steps 3-4, see
> `claim_step3_4.md`), not an independent structural discovery.**
>
> Verified directly: `Q_mu_plus(v):=||D_Sigma(v)psi_+||^2` and
> `Q_mu_minus(v):=||D_Sigma(v)psi_-||^2` are IDENTICAL as quadratic forms on
> the 6-dim family. Combined with Step 4's proven `S.M_+(v)=i*M_-(R.v)` and
> `S` unitary: `Q_+(R.v) = Q_-(R.v) = ||M_-(R.v)||^2 = ||S.M_+(v)||^2 =
> ||M_+(v)||^2 = Q_+(v)`. So `Q_mu` (hence `ker(M)`) is FORCED to be
> `W(A_2)`-invariant — this is the fifth documented instance in this project's
> history of the "forced not discovered" pattern (C144, C153, C154, C156),
> now happening WITHIN a single round's own two halves. See `novelty_check.md`
> for the full writeup and an independent skeptic pass currently attacking
> this exact forcing argument (checking it is not itself circular/vacuous).
>
> **The computation below is NOT wrong** — `ker(M)` really is invariant, the
> isotypic decomposition really is `2*standard`/`trivial+sign`, both verified
> exactly. What changed is the EPISTEMIC STATUS: this is a consistency check
> that had to come out this way, not new content beyond Steps 3-4.
>
> **Status: G4 PASSED, isotypic decomposition computed — but downgraded from
> "independent finding" to "forced consequence, useful as a corroborating
> computation." Novelty audit: FAILS on TWO counts (this forcing, AND Steps
> 3-4 reconstructing 100-year-old Pin-cover-of-Weyl-group theory — see
> `novelty_check.md`). Skeptic pass: in progress.**

## What was tested (fixed in `PREREGISTRATION.md` before any Weyl action was built)

Built the actual GEOMETRIC action of `W(A_2) = S_3` on `m = su(3)/t` via
genuine `SU(3)` conjugation (not abstract weight combinatorics): representatives
`g01`, `g12` for the two elementary transpositions, conjugating `M_BASIS`
(C153's exact generators) and re-expressing via `to_m`. Gate G4: does this
action, restricted to the 6-dim equivariant family `V_conn`, preserve C155's
exact kernel `ker(M) = {a0=a2-a4, a1=a3-a5}` (dim 4)?

**G4: PASSED.**

## Two self-corrections made during construction (both before G4 ran)

1. **Naive `R01^2 = I` on the ambient `m` is FALSE** — this is the standard
   `SU(n)`-Weyl-lift phenomenon: `N(T) -> W` does not split, so a block-embedded
   `SU(2)` reflection representative has order 4 in `SU(n)`, not 2.
   `g01^2 = diag(-1,-1,1)` is a genuine, nontrivial element of the torus `T`
   itself. The CORRECT gate: does `R01^2` act as the identity SPECIFICALLY on
   `family_sym` (already `T`-invariant by construction)? Verified: **yes**.
2. **The original pre-registration mis-stated `g12` as order 3.** `g12` is
   also a simple reflection (order 2 in `S_3`), like `g01`. The genuine order-3
   element is the PRODUCT `g01*g12` (a 3-cycle) — and 3-cycles, unlike
   reflections, lift HONESTLY (no torus ambiguity): `(R01*R12)^3 = I` literally
   on all of `m`, verified directly, no restriction to `family_sym` needed.

Both corrected in place in `PREREGISTRATION.md`/`c158_step1_weyl_action.py`
before proceeding, not silently fixed.

## Isotypic decomposition (character theory, exact, S_3: trivial/sign/standard)

| space | dim | decomposition |
|---|---|---|
| `V_conn` | 6 | `trivial(1) + sign(1) + standard(2)` |
| `ker(M)` | 4 | `2 * standard` |
| `V_conn / ker(M)` | 2 | `trivial(1) + sign(1)` |

**Not pre-registered which irrep the quotient is** — deliberately, to avoid the
kind of post-hoc fit this project's discipline forbids (stated explicitly in
`PREREGISTRATION.md` before this was computed). The result is the OPPOSITE of
the naively-guessed "quotient = standard": **`M`'s kernel is where BOTH copies
of the 2-dimensional standard representation live; `M`'s image (what `mu`
actually measures) lives entirely in the two 1-dimensional pieces.**

## What this does NOT establish

1. **Not yet shown that `M` itself is `S_3`-equivariant.** The decomposition of
   `ker(M)` and the quotient is consistent with `M` being an equivariant map
   onto a target carrying `trivial (+) sign`, but this has NOT been checked —
   it requires lifting the Weyl action to the SPINOR space `Sigma` (via
   `spin_lift`/Clifford), which carries its OWN potential Pin/Spin sign
   ambiguity (a DIFFERENT subtlety from the two already found and fixed here,
   related to why this project has separately tracked Pin-structure issues
   before). Concrete, well-defined next step — not attempted in this round.
2. Not novelty-audited. Isotypic decompositions of isotropy modules under Weyl
   symmetry are extremely standard in Lie theory; whether THIS specific
   observation (kernel of a Dirac-response map = full standard part) is
   already known is an open question for the next step, not assumed either way.
3. Not skeptic-reviewed.
4. Nothing about `N_gen=3`, `lambda`, triality, or any physical claim.
5. One homogeneous space (`SU(3)/T^2`), fixed conventions — not a general
   theorem for other `G/H`.

## Reproduce

```
python c158_step1_weyl_action.py          # gates G1(corrected)-G4, all pass
python c158_step2_isotypic_decomposition.py  # character decomposition
```
