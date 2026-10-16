# PRE-REGISTRATION — C151: is `c(J∇) = i·c(∇)` a nearly-Kähler universality or a `G2/SU(3)` accident?

**Registered:** 2026-09-04, **BEFORE any computation of THIS prediction's own
quantity on a second coset.**

> ### ⚠️ CORRECTION, same day, found by autonomous audit — read before the rest
>
> The original text of this line read: *"Status at registration time: NOTHING
> COMPUTED. **No `SU(3)/T²` construction exists in this project.**"*
> **That second sentence was FALSE, and it was my error.** An audit of open
> blockers and prior rounds found
> `experiments/20260715-round65-su3t2-killing-spinor-test/` — a **PROMOTE**
> round from 2026-07-15 which already re-derived round59's rank-forcing
> argument for `SU(3)/T²`'s own Killing-spinor data and `T²` representation
> theory.
>
> **What this changes, and what it does not:**
> - It does **not** compromise the blindness of THIS prediction. Round65
>   tested the *Killing-spinor / rank-forcing* argument. It did **not**
>   compute the connection coefficient `c`, nor its behaviour under `J` —
>   which is the entire content predicted here. The predicted quantity
>   remains uncomputed on any second coset.
> - It makes the test **cheaper than assumed**, and it **strengthens** the
>   anti-retrofit guarantees below. Round65's own source is
>   **Charbonneau–Harland 2016** (`Charbonneau_Harland_2016_NK_instantons.pdf`,
>   in the repo), which covers **all four** homogeneous nearly-Kähler
>   6-manifolds under a **single uniform** metric normalisation
>   (`B(X,Y) = −(1/12)·Tr(ad X ad Y)`) and a single Killing-constant
>   convention (`λ = 1/2`), and whose spinor/`SU(3)`-structure machinery is
>   built from an *abstract* Killing spinor on a general `(V,g)` without
>   reference to any specific isotropy group.
> - **Consequence for invalidation criterion 1 below:** the almost-complex
>   structure `J` and the metric normalisation for `SU(3)/T²` are therefore
>   fixed by an EXTERNAL source that predates this prediction and covers all
>   four spaces uniformly — they are not mine to choose after seeing an
>   answer. This is a stronger guarantee than the one originally written.
>
> Recorded rather than silently edited, per this project's own discipline on
> self-caught errors.

**Status at registration time (corrected):** the predicted quantity —
the connection coefficient `c` and its behaviour under `J` — has **not**
been computed on any coset other than `S⁶ = G₂/SU(3)`. Prior `SU(3)/T²`
work exists (round65) but concerns a different quantity. This file exists
so the prediction cannot be retro-fitted to whatever the computation
returns.

## Why this file exists at all

C147b found, on `S⁶ = G2/SU(3)`, that the nearly-Kähler almost-complex
structure `J` acts on C73b's 2-dimensional admissible torsion family as an
exact 90° rotation, and that the connection coefficient is `C`-linear with
respect to it:

```
c(NOMIZU)     = -2*sqrt(3)/3        [EXACT sympy]
c(NOMIZU o J) = -2*sqrt(3)*I/3      [EXACT sympy]
ratio         = I                   [EXACT]
```

The user (consortium message, 2026-09-04) proposed — correctly, and BEFORE
this was tested anywhere else — that this may not be a fact about
`G2/SU(3)` at all, but a consequence of nearly-Kähler `SU(3)`-structure in
general. That is a genuinely blind, falsifiable, cross-space prediction,
and it is only worth what it is worth if written down first.

## THE PREDICTION (frozen)

For a homogeneous nearly-Kähler coset other than `S⁶`, with its own
invariant-connection family `A_inv` carrying its own nearly-Kähler `J`, and
its own analogue of the twisted-Dirac invariant-sector coefficient `c`:

> **`c` is `C`-linear with respect to `J`:  `c(J∇) = ± i · c(∇)`.**

Equivalently: `A_inv` is naturally a complex vector space under `J`, and `c`
is a complex-linear functional on it — so `|c|` depends only on the `J`-radius,
and the zero locus of `c` is a complex subspace (in the rank-one case,
exactly `{0}`).

**Designated test space: `SU(3)/T²`.**

Chosen for a reason already established in this project, not picked now to
suit the prediction: C140 (design-only round, 2026-09-04) verified the
Butruille/Wolf classification of the four homogeneous nearly-Kähler
6-manifolds (`S⁶`, `S³×S³`, `CP³`, `SU(3)/T²`) and found that this project's
own construction is **ILL-POSED on `CP³` and `S³×S³`** but clean on
`SU(3)/T²`. So `SU(3)/T²` is the only available independent test space, and
it was designated as such BEFORE this prediction existed.

---

# RESTATEMENT under invalidation criterion #4 — FROZEN 2026-09-04, BEFORE `c` was computed

**Trigger:** Stage 0 scoping
(`experiments/20260904-c151-stage0-su3t2-scoping/`) measured the admissible
invariant-connection family for `SU(3)/T²` and found it **6-real-dimensional,
not 2**:

```
REGRESSION  dim Hom_su3(m, Lambda^2 m)  [S^6]        = 2   (reproduces C73b exactly)
RESULT      dim Hom_T2 (m, Lambda^2 m)  [SU(3)/T^2]  = 6
            commutant of isotropy on m:  su(3) -> 2,  T^2 -> 6
```

Reason, structural and expected: the isotropy drops from `SU(3)` (dim 8,
acting on `m` as `3⊕3̄`) to `T²` (dim 2, **abelian**, splitting `m` into three
2-real-dimensional weight planes, one per positive root). Equivariance under
an abelian group is a far weaker constraint, so the family is larger.

**`c` WAS NOT COMPUTED before this restatement was written.** The Stage 0
script computes only dimensions and prints an explicit statement to that
effect. Nothing below can have been fitted to an answer, because no answer
existed yet.

## The restated prediction (this is what C151 now tests)

The `S⁶` phrasing — *"`J` acts as an exact 90° rotation in a 2-dimensional
family"* — is **retired as `S⁶`-specific** and must not be carried across.
What survives, and what is hereby frozen as the prediction, is the
dimension-independent content:

> **`c(J·∇) = ± i · c(∇)`** — the connection coefficient is `C`-linear with
> respect to the coset's own canonical nearly-Kähler almost-complex
> structure `J`, acting on the admissible family by precomposition (exactly
> as `NOMIZU∘J` was formed for `S⁶` in C147b).

Three consequences of the higher dimension, pre-committed now:

1. **`c` may be matrix-valued, not scalar.** On `S⁶` both invariant sectors
   were 1-dimensional, so `c` was a single number. Under `T²` the invariant
   sectors are expected to be larger (weight-zero subspaces are more
   plentiful for an abelian isotropy). If so, the identity above is asserted
   **as matrices**, entry-by-entry — not weakened to a statement about
   norms.
2. **The invariant-sector dimensions must be reported BEFORE `c`**, in the
   same way this restatement reports the family dimension before `c`.
3. **`J` must be pinned before use.** On the flag manifold there are several
   invariant almost-complex structures (sign choices on the three root
   planes); the nearly-Kähler one is the **non-integrable** representative.
   The exact sign convention used will be stated explicitly and justified
   from its standard characterisation — not selected after seeing `c`.

## Additional pre-committed failure mode (new, forced by the larger family)

> **If `J` does not map the admissible family into itself**, the prediction
> is not merely false — it is **not well-posed on this coset**, and that is
> the finding. It must be reported as such (`BLOCKED-STRUCTURE`), not worked
> around by substituting a different `J` or a different family until
> something maps correctly.

> ### ⚠️ CORRECTION (2026-09-04, forced by the FL Step 8a skeptic pass on Stages 0/1)
>
> The paragraph originally continuing here read: *"This failure mode did not
> exist for `S⁶`... It becomes live here precisely because the family is
> bigger and `J`'s action on it is no longer a near-tautology."*
> **That was wrong, and the "failure mode" is TAUTOLOGICAL — it cannot fire.**
>
> `J_NK` is itself `T²`-equivariant (it is block-diagonal with a rotation in
> each root plane, and the `T²` generators are rotations in those same
> planes — rotations in a common 2-plane commute). For any equivariant `J`
> and any `T ∈ Hom_{T²}(m,Λ²m)`, the composition `T∘J` is automatically
> equivariant:
> `t·(T∘J)(v) = T(J·t v) = (T∘J)(t v)`. So `T∘J` lies in the family **by
> construction**, whatever the family's dimension.
>
> The same was true on `S⁶` for exactly the same reason (`J` there is
> `SU(3)`-invariant, `NOMIZU ∈ Hom_{SU(3)}`), so the claim that the bigger
> family makes this "live" is doubly wrong.
>
> **What the check actually verifies:** that `J` was *constructed*
> equivariantly — a plumbing check, not a structural one. The `4.782e-16`
> residual is machine noise on a mathematically forced zero. It must not be
> reported as a passed physics gate, and this "failure mode" is withdrawn as
> a pre-committed outcome.
>
> Recorded rather than deleted, per this project's discipline on self-caught
> and skeptic-caught errors.

---

## Outcomes, both pre-committed as informative

| Outcome | What it means | Consequence |
|---|---|---|
| `c(J∇) = ±i·c(∇)` holds on `SU(3)/T²` | The `C`-linearity is a nearly-Kähler phenomenon, not a `G2/SU(3)` accident | C147 becomes a special case of a general structure; substantially raises the value of the whole `E_W`/connection-coefficient line |
| It FAILS on `SU(3)/T²` | The `C`-linearity is specific to `G2/SU(3)` | Equally informative: localizes C147's structure precisely, and tells us the `G2` case has something the generic nearly-Kähler case does not — which is itself a lead |
| The construction cannot be posed on `SU(3)/T²` at all | `BLOCKED-SUBSTRATE`, per this project's own Step-2a discipline | NOT evidence either way; must not be recorded as a failed prediction |

## What would make this test INVALID (named in advance)

1. Choosing a different `J` on `SU(3)/T²` after seeing the answer. The `J`
   must be the canonical nearly-Kähler almost-complex structure of that
   coset, fixed by its own standard construction, exactly as `S⁶`'s was
   fixed by AHL2023's eq.(5) convention — not selected to make the ratio
   come out to `i`.
   **(Strengthened by the correction above:** Charbonneau–Harland 2016 fixes
   the metric normalisation and Killing-constant convention **uniformly
   across all four** homogeneous nearly-Kähler 6-manifolds, and round65
   already used it for `SU(3)/T²` on 2026-07-15 — i.e. before this
   prediction existed. So the convention is externally and pre-emptively
   fixed, not chosen by me. Any deviation from CH2016's own normalisation
   in the eventual execution must be flagged loudly and justified.**)**
2. Choosing which invariant-connection family to use after seeing the
   answer. It must be the analogue of `Hom_H(m, Λ²m)` for that coset's own
   isotropy `H = T²`, whatever dimension that turns out to be.
3. Reporting `|ratio| ≈ 1` without reporting `Re(ratio)`. Both are required;
   `C`-linearity needs `Re(ratio) = 0`, not merely unit modulus.
4. If the family turns out to have dimension ≠ 2, silently reinterpreting
   the prediction. State the dimension first; the prediction is about
   `J`-compatibility, which is meaningful in any even dimension, but the
   "exact 90° rotation in a 2-dim family" phrasing is `S⁶`-specific and must
   not be smuggled across.

## What this pre-registration does NOT claim

- Does NOT claim the prediction is likely true. It is a genuine blind test;
  the `G2/SU(3)`-specific outcome is fully live.
- Does NOT claim `SU(3)/T²` is easy — C140's own assessment was that it is
  the cleanest of the three alternatives, not that it is cheap.
- Does NOT commit this project to running C151 at all. If the cost turns out
  to be large, the honest action is to leave this pre-registration standing
  and unexecuted, not to run a weakened version of it.

## Provenance

Prediction proposed by the user, 2026-09-04, in direct response to C147b's
result, and explicitly flagged by them as needing registration before
computation. Registered here unmodified. No computation on any second coset
had been performed by this project at registration time.
---

# ✅ OUTCOME — 2026-09-04. Prediction CONFIRMED (after a retracted first execution)

**First execution (C151 Stage 2b): retracted.** It reported the third outcome
("cannot be posed / vacuous"). That rested on an invariant sector built with a
non-equivariant generator; see the RETRACTION appended to
`../20260904-c151-stage0-su3t2-scoping/decision.md`.

**Second execution (C152 Steps 6-8), on the corrected sector:** the FIRST
outcome in the table above.

```
c(J.nabla) = +i . c(nabla)   exactly, as matrices entry by entry, 8/8 draws
```

Blindness was preserved across the correction: the prediction was frozen here
before any `c` existed, and the corrected `c` had never been computed by
anyone at the time it was run. Invalidation criteria 1-3 were all satisfied
(`J` pinned by Nijenhuis in Stage 1a; the family is the coset own
`Hom_{T^2}(m, Lambda^2 m)`; the identity is reported entrywise, and
`Re(ratio) = 0` holds exactly, not merely `|ratio| = 1`). Criterion 4 had
already fired and was answered by the frozen restatement.

**Consequence, per this file own outcome table:** the C-linearity is a
nearly-Kahler phenomenon, not a `G2/SU(3)` accident. C147 becomes a special
case of a more general structure.
