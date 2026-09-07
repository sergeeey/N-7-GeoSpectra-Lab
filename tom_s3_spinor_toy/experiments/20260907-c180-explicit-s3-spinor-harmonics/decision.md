# C180 — Decision

**Date:** 2026-09-07
**Verdict:** `BOTH-CONFIRMED-PLUS-CONNECTION-CONSTANT`. `[VERIFIED-tool]`,
all structural residuals exactly `0.0`. Exceeds this round's own
pre-registered expectation (`BOTH-CONFIRMED`) by one unplanned result:
the spin-connection constant `3/2` came out of the data uniquely rather
than having to be supplied.

---

## 0. Summary

Built the object Tom Lawrence's §3.3 asks for — **explicit `S³` spinor
harmonics** — in the trivialization C179 identified as the one that works,
and verified his eq (77) for the `S³` VECTOR multiplet as a control.

| | result |
|---|---|
| **Item 2** — eq (77) for `S³` vector `\|φ_i⟩ = x_i/r`, `i=0..3` | his convention `Γ_d = −T` verifies; transpose variant fails; sign variant fails. **Exactly one of three works, and it is his.** Extends to `n=3` a check his own notes only carry out for `n=2` (his §3.2). |
| **Item 3** — explicit spinor harmonics on `S³` | constructed at levels `k=0,1,2,3`; eigenvalue/multiplicity structure reproduces this project's own established `S³` Dirac degeneracy exactly |
| **Unplanned** | the spin-connection constant `3/2` is **solved for**, uniquely, from 7 independent (eigenvalue, multiplicity) pairs |

---

## 1. The construction (what to actually send Tom)

`S³` = unit quaternions `q = x₀ + x₁i + x₂j + x₃k`. The six generators of
`so(4)` split as `su(2)_L ⊕ su(2)_R`, given explicitly by left and right
quaternion multiplication:

```
X₁^R : (x₀,x₁,x₂,x₃) ↦ (−x₁, x₀,  x₃, −x₂)
X₂^R : (x₀,x₁,x₂,x₃) ↦ (−x₂, −x₃, x₀,  x₁)
X₃^R : (x₀,x₁,x₂,x₃) ↦ (−x₃,  x₂, −x₁, x₀)
```

(and the mirror set `X^L` with the middle signs flipped). Spinor fields
are `C²`-valued functions (per Weyl half; `C⁴` for the full spinor), and

```
D₀ = −i Σ_a σ_a ⊗ X_a^R
```

acts on `C² ⊗ H_k`, where `H_k` = harmonic polynomials of degree `k` in
four variables restricted to `S³`, `dim H_k = (k+1)²`.

**Structural controls, all exact (`0.0`, not rounded):** every generator
antisymmetric; `[X_a^L, X_b^L] = 2ε_abc X_c^L`; `[X_a^R, X_b^R] = −2ε_abc X_c^R`;
**`[X_a^L, X_b^R] = 0` for all 9 pairs** (left and right multiplication
commute — the `su(2)⊕su(2)` structure, verified not assumed); and the six
fields span exactly the same 6-dimensional space as the coordinate
rotations `x_μ∂_ν − x_ν∂_μ` (rank 6, joint rank 6).

---

## 2. The spectrum, and the constant that was not fitted

| `k` | `dim H_k` | `dim(C²⊗H_k)` | eigenvalues of `D₀` (multiplicity) |
|---|---|---|---|
| 0 | 1 | 2 | `0` (2) |
| 1 | 4 | 8 | `−1` (6), `+3` (2) |
| 2 | 9 | 18 | `−2` (12), `+4` (6) |
| 3 | 16 | 32 | `−3` (20), `+5` (12) |

Multiplicities are exactly `(k+1)(k+2)` and `k(k+1)` at every level —
matching round67's own established `S³` Dirac degeneracy `(n+1)(n+2)`.
All eigenvalues real (max imaginary part `<1e-9`).

**The unplanned result.** `D₀` contains no spin-connection term by
construction. Asking whether a single additive constant `c` makes
`D₀ − c` equal the physical spectrum `±(n+3/2)` with multiplicity
`(n+1)(n+2)`: each `(eigenvalue, multiplicity)` pair fixes `n` from its
multiplicity and then admits exactly two candidates `c = val ∓ (n+3/2)`.
Intersecting over all seven pairs:

```
(0, 2)   → {−1.5, +1.5}
(−1, 6)  → {−3.5, +1.5}
(+3, 2)  → {+1.5, +4.5}
(−2, 12) → {−5.5, +1.5}
(+4, 6)  → {+1.5, +6.5}
(−3, 20) → {−7.5, +1.5}
(+5, 12) → {+1.5, +8.5}
                intersection = { +1.5 }   ← unique
```

**`c = 3/2` exactly, and uniquely.** The standard `S³` spin-connection
constant is recovered from the eigenvalue data alone — it was solved for,
not supplied, and no other value is consistent with even two of the pairs.

---

## 3. A bug this round caught in its own check

The first draft of §2's analysis estimated the constant as
`(max + min)/2` over all eigenvalues, giving `c = 1.0` and a **failing**
verdict (`connection_constant_emerges_as_three_halves: false`). That
heuristic is simply wrong — the extreme eigenvalues come from different
levels and do not pair with each other. The failure was **not** patched by
loosening a tolerance; the method was replaced with the per-pair
intersection above, which is both correct and strictly stronger (it
returns uniqueness, which the averaging heuristic could never establish).
Recorded here because a tolerance-loosening "fix" would have produced the
same green verdict with none of the content.

---

## 4. The explicit harmonics (the deliverable)

- **`k=0`:** `H_0 = span{1}`, so `C²⊗H_0` is the **two constant spinors**
  `(1,0)` and `(0,1)`. These exist as global objects precisely because
  `S³` is parallelizable — the concrete point where C179's obstruction is
  evaded. Eigenvalue `0` (i.e. `−3/2` after the connection shift), matching
  round67's lowest level and its multiplicity 2.
- **`k=1`:** eight explicit eigen-spinors, `C²`-valued linear polynomials
  in `(x₀,x₁,x₂,x₃)`, six at eigenvalue `−1` and two at `+3`, listed in
  `results_c180.json` under `explicit_lowest_harmonics`. Example at
  `λ=+3`: `(i·x₀ + x₃, −x₁ + i·x₂)`.

Higher levels are generated by the same code path; `k≤3` was computed to
keep the round bounded.

---

## 5. Kill Analysis

**What this round establishes:** the construction Tom asked for exists,
is explicit, and reproduces the independently-established spectrum
including its connection constant. Item 2 also confirms his eq (77)
extends from `n=2` to `n=3` under his own convention — so the formalism
he built does carry over; it is only the *spinor* case that needed the
trivialization.

**What this round does NOT establish:**
1. The `S⁴`-and-higher cases, or `S²` (per C179, `S²` should be obtained
   by descent from `S³`; not attempted here).
2. Item 4 (his `ψψ†` → gamma → vector check) and item 5 (Riemann normal
   coordinates) — deliberately deferred to the next round.
3. Anything about `S⁶`, `N_gen=3`, or any open blocker — this round is
   collaboration-facing only.

**Relaxation Map:** the natural next steps are exactly items 4 and 5, both
now cheap: the explicit harmonics needed for the `ψψ†` projection are in
hand, and the frame machinery for item 5 already exists in
`experiments/20260623-s3-spin-connection-to-tom-operators/`.

---

## 6. Floor–Ceiling

The discriminating quantity is the multiplicity pattern.
- **FLOOR = 0 correct levels out of 4.** With the mechanism removed — i.e.
  if `Σσ_a X_a^R` failed to couple the spinor index to the orbital index —
  the operator would be proportional to the identity on `C²⊗H_k`, giving
  ONE eigenvalue of multiplicity 18 at `k=2` (and 32 at `k=3`) instead of
  a split, so **0** of the 4 levels would match. That is what a vacuous
  version of this test returns.
- **OBSERVED = 4 correct levels out of 4**, with the two-branch splits
  `12 + 6` at `k=2` and `20 + 12` at `k=3`, matching the pre-stated
  `(k+1)(k+2)`, `k(k+1)`.
- **CEILING = 4 correct levels out of 4** — the maximum attainable on the
  4 levels computed; additionally the connection constant is pinned to the
  single value 1.5.
- **efficiency = `1.000`** (exact algebraic agreement, not a statistical
  limit — same caveat as C179 §7).

---

## 7. Independent skeptic pass (Step 8a) — RUN, verdict `WEAKENED`, all three findings now closed by computation

Run context-blind (claim.md + script + results only; `decision.md`
withheld). It had no Bash and said so explicitly, hand-deriving instead.
Verdict `WEAKENED` — no computational error found, but three concerns
raised. **All three are now resolved, two of them by new computation added
to the script.**

| # | Concern | Resolution |
|---|---|---|
| **1** | **The multiplicity check may be vacuous:** the pattern `(k+1)(k+2)`/`k(k+1)` is forced by ANY su(2) generator set with the right algebra, including `X^L` — so it does not certify that the *right*-invariant fields (the ones the parallelizability argument needs) were used. The round ran no negative control for `D₀` itself. | **Concern correct, and now answered.** Added `chirality_discrimination_check()`: built the whole construction a second time from `X^L`. Multiplicities are indeed **identical** (`{6,2}`, `{12,6}`, `{20,12}` — the skeptic was right). **But the connection constant is not:** `X^R → c = +1.5`, `X^L → c = −1.5`, exactly opposite sign. So the multiplicity check alone does not discriminate, while the round's *stronger* check does. The negative control now exists and passes. |
| **2** | **Citation is thin:** round67's `decision.md` does not actually state the multiplicity formula `(n+1)(n+2)`; the rigorous source is `c85_certification.py`. | **Correct — and worse than the skeptic could see.** Direct check: round67 states it in its **`claim.md` line 73**, marked `[INFERRED]` and explicitly *"not independently cross-checked against a second source."* So the round was citing an acknowledged-uncertain claim as if established. Two consequences: the citation is corrected to `c85_certification.py` as the rigorous source, and — the positive side — **C180 supplies exactly the independent cross-check round67 itself said it lacked**, via a completely different method (quaternionic vector fields on harmonic polynomials vs. Peter–Weyl matrix elements). |
| **3** | **Unrequested finding:** the raw operator matrix at `k=2` is *not* antisymmetric in the monomial-coefficient basis, and the code comment justifying Hermiticity via "orthonormal from SVD" does not obviously survive that. Flagged as likely benign but unresolved. | **Correct catch on the comment; the maths is fine.** The SVD basis is orthonormal in *coefficient* space, which is **not** the `L²(S³)` inner product — so the matrix should not be expected antisymmetric. The comment was misleading and is rewritten. Closed by explicit demonstration: `basis_independence_check()` recomputes the `k=2` spectrum in a deliberately non-orthonormal random basis (non-orthonormality `16.6`) and gets the same eigenvalues to `6.0e-14`. |

**A second self-caught bug, while closing concern 3.** The first version of
`basis_independence_check()` reported a spurious *failure* (eigenvalues
differing by `54.4`). Cause: it reused `vector_field_matrix()`, which
restricts via `bᵀ·full·b` — a **similarity** transform only when `b` is
orthonormal, and a **congruence** otherwise, which does not preserve
eigenvalues. Feeding it a deliberately non-orthonormal basis was therefore
testing the wrong thing. Fixed with the pseudo-inverse restriction
(`pinv(b)·full·b`), which is correct for any basis. Recorded because it is
the same shape as §3's bug in the sibling round C181: **a check that fails
is not automatically evidence against the claim — it is first evidence
about the check.**

**Net effect:** verdict upgraded from the skeptic's `WEAKENED` — the two
substantive gaps (no negative control; imprecise sourcing) are closed, and
closing the first one produced a *stronger* result than the round
originally claimed: the connection constant, not the multiplicities, is
what certifies the construction, and it does so by flipping sign under the
one substitution that mattered.

---

## 8. Status

`experiments/20260907-c180-explicit-s3-spinor-harmonics/` — DONE, INCLUDING
independent skeptic pass. Verdict `BOTH-CONFIRMED-PLUS-CONNECTION-CONSTANT`,
with all three of the skeptic's concerns closed by added computation (§7):
a real negative control now exists (opposite chirality → constant flips to
`−3/2`), the sourcing is corrected, and basis-independence is demonstrated
(`6.0e-14`). Two self-caught bugs recorded (§3 and §7). Items 2–3 of the
5-item plan complete. Notable side effect: this round supplies the
independent cross-check that round67's own `claim.md:73` explicitly stated
it lacked. Registry not yet updated. No git operations run.
