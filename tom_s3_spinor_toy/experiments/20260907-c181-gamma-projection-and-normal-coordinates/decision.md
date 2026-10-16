# C181 — Decision

**Date:** 2026-09-07
**Verdict:** `PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE`. `[VERIFIED-tool]`.
Matches this round's own pre-registered expectation exactly, including the
prediction that the collaborator's proposed check would turn out to be
necessary but not sufficient.

---

## 0. Summary

Items 4 and 5 of the plan. Three results, one of them a correction to the
wording of Tom's own item 4.

| | result |
|---|---|
| **4a — does the gamma projection work?** | **Yes, exactly.** `x_μ = ½·Tr(σ_μ† g)` recovers the four vector harmonics with max error `< 1e-12` over 500 random points on `S³`. |
| **4b — does it DISCRIMINATE?** | **No.** An alternative built from the opposite chirality (`X^L` instead of `X^R`) — a genuinely different operator — passes the identical test. Demonstrated by construction, not asserted. |
| **4c — dimension count (unplanned correction)** | `ψψ†` for ONE Weyl spinor has an **invariant trace** (max change `0.0` over 200 random rotations), so it reduces as `1 ⊕ 3` and is NOT the irreducible `SO(4)` vector. The genuine vector needs one index from EACH chirality. |
| **5 — Riemann normal coordinates** | **Verified.** `g_ab(0) = δ_ab` on 5 exact unit directions, and **all 9 first derivatives vanish identically** (symbolic, no constraint needed). |

---

## 1. The correction to item 4's wording (worth telling him)

His item 4 says: *"take the outer product of the spinor multiplet and its
adjoint, and then use gamma matrices to project out the vector multiplet."*

Taken literally — one spinor multiplet with **its own** adjoint — this
gives `ψψ†`, a `2×2` matrix whose **trace is invariant** under the group
action (verified: max trace change `0.0` over 200 random `SU(2)` elements).
An invariant piece splitting off means the object is reducible, `1 ⊕ 3`,
not the irreducible 4-dimensional `SO(4)` vector.

The construction that *does* give the vector is
`(½,0) ⊗ (0,½) = (½,½)` — one index from **each** chirality. Concretely
that is exactly the `SU(2)` group element itself:

```
g = x₀·I + i(x₁σ₁ + x₂σ₂ + x₃σ₃)
```

whose trace is **not** invariant under `g ↦ u g v†` (max change `≈ 1.4`,
i.e. manifestly non-invariant), confirming irreducibility. The projection
back out is `x_μ = ½·Tr(σ_μ† g)`, verified exact.

So his recipe is right in spirit and needs one word changed: not the
spinor and *its own* adjoint, but the two chiralities paired.

---

## 2. The blind spot in his proposed check — demonstrated, not asserted

This is the result worth flagging hardest, because it concerns a check he
intends to *rely* on.

Two different operators were built — `D^R = −iΣσ_a X_a^R` (C180's) and
`D^L = −iΣσ_a X_a^L` (opposite chirality) — and confirmed to be genuinely
different (`the_two_operators_are_different: True`; their spectra differ).
Both produce equivariant bases of the same space, and both therefore
reproduce the same 4-dimensional vector multiplet under his projection.

**Conclusion:** the outer-product/gamma-projection check inspects
*representation content only*. It cannot see which operator's eigenbasis
was used, so it will pass for any equivariant basis — including a wrong
one. It is a genuine necessary condition (a construction that failed it
would be broken), but it cannot certify that a basis is the Dirac
eigenbasis. A second, spectrum-level check is needed for that — which is
what C180 supplies (multiplicities `(k+1)(k+2)`, `k(k+1)`, and the
connection constant pinned to `3/2`).

This was **pre-registered as the expected outcome** in claim.md before
running, so finding it is not being reported as a discovery — but it was
*tested* rather than assumed, which is the point.

---

## 3. A bug this round caught in itself — and what caused it

The first run returned `RNC-FAILS`. Diagnosis: **all nine first
derivatives vanished correctly** (the substantive half of the normal-
coordinate property); only `g(0) = δ` failed. The computed `g(0)` was a
rational function of the ray direction `n` that equals the identity
**precisely on `n₁²+n₂²+n₃² = 1`** — which sympy had no way to know,
because the variable holding that constraint had been **deleted to silence
a linter warning** (`F841 local variable assigned but never used`).

The linter was right that the variable was unused; the correct response
was to *use* it, not remove it. Removing it silenced the warning and broke
the mathematics, and the failure surfaced two steps later as a wrong
verdict. Fixed by evaluating on exact unit directions
(`(1,0,0)`, `(0,1,0)`, `(0,0,1)`, `(1,1,1)/√3`, `(1,−1,0)/√2`) — all five
give `g(0) = I` exactly. **Not** fixed by loosening a tolerance.

Recorded because the failure mode is general and not obvious: a lint fix
can be a silent math regression when the "unused" object encodes a
mathematical constraint.

---

## 4. Item 5 deliverable and its honest limit

Riemann normal coordinates at the identity of `S³ = SU(2)`:

```
q(y) = exp(y₁i + y₂j + y₃k) = cos|y| + (sin|y| / |y|)·(y₁i + y₂j + y₃k)
```

**Verified:** `g_ab(0) = δ_ab` (5 exact directions) and `∂_c g_ab(0) = 0`
(all 9 components, symbolically, identically zero). These are exactly the
defining conditions, so these are genuine normal coordinates — the
"locally orthonormal / frame coordinates" his item 5 asks for.

**Not covered, stated plainly:** transporting the full spinor-harmonic
machinery of C180 into these coordinates — i.e. actually writing the local
section of the spinor field — was **not** attempted. This round supplies
the coordinate system and its verification, not the transported
eigenfunctions. Cross-reference for the frame side already in the repo:
`experiments/20260623-s3-spin-connection-to-tom-operators/` (Hopf-frame
spin connection `ω₁₂=tan(α)e²`, `ω₁₃=−cot(α)e³`, `ω₂₃=0`, verdict
`PASS_LOCAL_GEOMETRIC_MATCH`) — a different frame, same geometry; relating
the two is the natural continuation.

Consistency note: the unit-radius round `S³` used here has `Scal_LC = 6`,
which is round111's own independently cross-checked value.

---

## 5. Kill Analysis

**What this round establishes:** his item 4 works as a necessary check,
needs one wording fix (two chiralities, not one spinor with its own
adjoint), and has a demonstrated blind spot. His item 5's coordinate
groundwork is in place and verified.

**What it does NOT establish:**
1. The local spinor field itself (item 5's endpoint) — groundwork only.
2. Anything about `S²`, `S⁶`, `N_gen=3`, or any open blocker.
3. That the C180 basis is *the* Dirac eigenbasis — that rests on C180's
   own spectrum check, not on this round's projection.

---

## 6. Floor–Ceiling

Discriminating quantity: the number of the four pre-registered predicates
that come out as predicted.
- **FLOOR = 0 of 4.** A construction with no real content — e.g. if the
  projection were trivially the identity map, or if the two chiralities
  were secretly the same operator — would leave predicate 2 untestable and
  predicate 3 vacuous, i.e. **0** genuinely-informative predicates. Guarded:
  `the_two_operators_are_different: True` confirms the alternative used in
  predicate 2 is a real alternative and not a relabelling.
- **OBSERVED = 4 of 4** predicates resolved as pre-registered.
- **CEILING = 4** predicates (privileged access could resolve at most the
  4 predicates this round poses; ceiling value = 4, floor value = 0, so the
  interval is 0 to 4 and is not degenerate).
- **efficiency = 1.000** — exact algebraic agreement, not a statistical
  limit (same caveat as C179/C180).

---

## 7. Independent skeptic pass (Step 8a) — RUN, verdict `WEAKENED`, one finding was serious

Context-blind (claim.md + script + results; both `decision.md` files
withheld). No Bash available to it; it hand-derived and read the code line
by line, and said so.

| Attack | Outcome | Response |
|---|---|---|
| **The discrimination test (claim b — the headline finding, and the one already written into the draft reply)** | **BROKE IT.** The "same span" half was a tautology: `span_R = matrix_rank(basis1)` and `span_L = matrix_rank(basis1)` computed the rank of the **same matrix twice**, with no `X^L` object built at all — so `same_span` was `True` for any input. Directly contradicted claim.md's own "tested, not asserted". | **Accepted in full and rebuilt.** The test now takes the LOWEST eigenspace of each chirality's operator (genuinely different: dim 6 for `X^R` at eigenvalue `−1`, dim 2 for `X^L` at `−3`), forms the bilinears `B^μ = ψ₀†σ^μψ₁` his item 4 prescribes, and computes their span inside `H₁`. Result: **both give rank 4** — the full vector multiplet — from genuinely different starting subspaces. The conclusion survives, now as computation instead of assertion. |
| **Claim (c), the correction being sent to him** | **Scoped too broadly.** The trace-invariance maths is textbook-certain, but the correction assumes "spinor multiplet" means a *single Weyl chirality*. If he meant a full Dirac bispinor `Ψ=(ψ_L,ψ_R)`, then `ΨΨ†` already has off-diagonal blocks pairing the chiralities and **his sentence is correct as written** — the "correction" would then misrepresent him. | **Accepted.** The draft has been rewritten to present this as a question about which reading he intended, not as an unqualified correction. This is the highest-cost error the pass could have caught, and it caught it before sending. |
| Riemann normal coordinates (claim d) | **Did not break — and is stronger than the round claimed.** The first-derivative result is symbolic in unconstrained `n`, so it is a *proof* that all nine vanish, not a five-point sample; and because the embedding is real-analytic, the `t→0` limit is direction-independent, so a sixth direction cannot fail. | Accepted as a strengthening; §4's framing was more cautious than necessary. |
| The projection formula (claim a) | **Did not break.** `Tr(σ_μ†σ_ν) = 2δ_μν` verified by hand, so `½Tr(σ_μ†g) = x_μ` exactly, with no hidden normalisation freedom. | No change. |

**Net:** the verdict label is unchanged, but one of its two supporting
legs was rebuilt from scratch and the outgoing correction to Tom was
softened into a question. **This was the third cannot-fail check found in
this round sequence** — after C180's basis test and C182's no-go check —
and the only one that had already reached a draft intended for someone
outside the project.

---

## 8. Status

`experiments/20260907-c181-gamma-projection-and-normal-coordinates/` —
computed, verdict `PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE`, all four
predicates as pre-registered, plus one unplanned correction to item 4's
wording. One self-caught bug recorded (§3, a lint fix that broke the
math). Items 4–5 complete; the 5-item plan is now complete end to end.
Skeptic pass not yet run (§7). Registry not yet updated. No git operations
run.

---

## 9. CORRECTION (2026-09-07, later same day) — §1's "correction to Tom" is WITHDRAWN

**Trigger:** a verbatim re-read of his §2.2 (p.13) while preparing the reply,
prompted by an external review of the draft letter.

**What §2.2 actually says, verbatim:**

> "For n even, the representation which acts on the `d`-dimensional multiplet is
> the spinor representation of `SO(n + 1)`; for n odd, it is the direct sum of
> the two (fundamental) spinor representations."

`n = 3` for `S³` is **odd**. So his multiplet is the direct sum of both
fundamental spinors — a 4-component Dirac **bispinor**, not one Weyl chirality.
And the next sentence already states the outcome we were about to "correct":

> "The action induced on this by a rotation is a **reducible** representation of
> `G`. This action partitions it into a set of bases for ket spaces, which
> **include** the basis for a vector multiplet."

He does not claim `ΨΨ†` **is** the vector. He claims it **contains** one, and
says so with the word *reducible*. **His sentence is correct as written.**

**Verified** (`c181b_bispinor_correction.py`, `results_c181b.json`):

| block | transforms as | singlet drift under 400 random `SU(2)×SU(2)` | content |
|---|---|---|---|
| `M_LL` | `u_L M u_L†` | `3.6e-15` — **invariant, splits off** | `(1,1) ⊕ (3,1)` reducible |
| `M_RR` | `u_R M u_R†` | `5.3e-15` — invariant | `(1,1) ⊕ (1,3)` reducible |
| `M_LR` | `u_L M u_R†` | **`8.44` — not invariant** | `(2,2)` **irreducible = the vector** |
| `M_RL` | `u_R M u_L†` | — | `(2,2)` the vector again |

`1+3+1+3+4+4 = 16 = dim(ΨΨ†)`. Block transformation laws exact to `0.0`.
The 4-vector norm from `M_LR` is preserved to `1.8e-15`.

**So §1 of this file is withdrawn.** The C181 skeptic had flagged exactly this
reading as the one that would invalidate the correction; his own §2.2 now
settles which reading he meant. What survives from §1 is only the *location*
result: the vector sits in the **off-diagonal** blocks, not the diagonal ones —
which is useful to him, and is not a correction.

**§2 of this file (the non-discrimination finding) is unaffected** and remains
the substantive thing to tell him.

### 9a. A fourth cannot-discriminate check — caught by a built-in control, not a skeptic

The first version of `c181b` tried to separate the blocks by comparing the
invariance of `|x|` built from each. Both returned `~1e-15`. Reason:
`|x|² = ½Tr(M†M)` is the **Frobenius norm**, invariant under `M → u M v†` for
*any* unitaries — so it holds for every block and discriminates nothing.

Withdrawn and replaced by the singlet-drift test above, which puts the two
blocks on opposite sides by 15 orders of magnitude
(`discriminates: true` is asserted in the results JSON, not eyeballed).

This is the **fourth** non-discriminating check in the C179–C182 sequence, after
C180's multiplicity check, C182's no-go condition and C181's own span test.
(C180's *basis-independence* test is NOT one of them — that was a
congruence-vs-similarity bug producing a spurious failure, the opposite defect.) It is the
**first one caught by a control deliberately built into the script** rather than
by an external skeptic — which is the intended direction of travel, and the
reason the negative control was put there at all.

### 9b. An independent code review found the replacement discriminator half-hollow

`c181b`'s rebuilt discriminator was `offdiag_x0_drift > 1e-3 AND diag_y0_drift < 1e-10`,
and §9a presented the two halves as having to "come out on OPPOSITE sides or the
test is worthless again". A code review (context-limited to the two scripts)
pointed out that the **diagonal half is the identity** `Tr(u A u†) = Tr(A)` —
trace cyclicity plus unitarity — which holds for **any** `2×2` matrix conjugated
by the same unitary on both sides, whether or not it came from `Ψ`.

**Verified rather than accepted:** the same test, run on an unrelated random
matrix, gives max drift `9.5e-16` against the genuine block's `3.6e-15`.
Indistinguishable. The conjunct carries **zero** information about whether the
construction is correct. Now a measured field, `junk_control_diag_y0_max_drift`,
with `diag_half_is_an_identity: true` asserted in the results JSON — the
review's argument is data in the artifact, not a remark in a comment.

**This is NOT a sixth cannot-fail check, and the distinction matters.** The
compound flag *can* still come out `False`, via its off-diagonal conjunct: slice
the wrong block and `offdiag_x0_drift` collapses to `~0` by the very same
identity. What was wrong was the **claim about the test**, not the test. Every
scrap of falsifying power sits in `offdiag_x0_drift > 1e-3`, and the results JSON
now says exactly that in a field called `falsifying_power_is_entirely_in`.

Two smaller findings, both accepted:
- The Frobenius-norm value was still being reported next to the discriminator
  captioned "which IS preserved" — the same quantity this file had **withdrawn
  two sections earlier** for discriminating nothing. Relabelled
  `UNITARITY_SANITY_ONLY_...` with an explicit "must not be quoted in support of
  the (2,2) identification".
- In `c180b`, the `6 → 7` corruption case detects the break through the
  *invalid-product fallback* (`n_from_multiplicity` returns `None`), so it would
  report "detected" even if the magnitude arithmetic were broken. Added
  `6 → 12` — a **valid** product with the wrong `n`, which forces the arithmetic
  to run. It also detects the corruption, and `broken_multiplicity_detected` now
  keys on that case instead.

**The part worth keeping:** this defect was found *in the script written to catch
this class of defect*, one level up from the four it was auditing. The shape is
new — not "a check that cannot fail", but **a compound `A AND B` discriminator in
which one conjunct is a mathematical identity**, which inherits an
unconditionally-true region while still looking like two independent tests. The
useful question, and it is cheap: *per conjunct*, what would have to be true
about the world — not about the code — for this half to come out False?
