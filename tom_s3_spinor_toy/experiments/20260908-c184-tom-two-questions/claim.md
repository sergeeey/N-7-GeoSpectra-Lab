---
# C184 — answering Tom's two questions of 2026-09-07 23:08, in his labels and
# his coordinates, plus the sting in the tail of the first one

**Date:** 2026-09-08
**FL tier:** [x] Full
**Question type:** [x] descriptive (statements about fixed, known objects; no
intervention, no counterfactual)

---

## The questions, verbatim

> **1)** For `S^2`, are you saying that it is possible to write `psi_{1/2}` and
> `psi_{-1/2}` as functions of the angular coordinates? If so, are these complex
> functions or quaternionic functions? If not, how do we express them — given
> that, if we take the outer product of a spinor and an adjoint spinor, we can
> project out a vector?
>
> **2)** For `S^3`, are you saying that it is possible to write `psi_{(1/2,0)}`,
> `psi_{(-1/2,0)}`, `psi_{(0,1/2)}` and `psi_{(0,-1/2)}`, as functions of the Hopf
> coordinates? If so, are these complex functions or quaternionic functions?

The clause after the dash in (1) is the load-bearing part and is easy to read
past. It is a consistency challenge, not a request for detail: **if the spinor
is not a function, how can a bilinear built out of two of them be one?** An
answer that does not resolve that has not answered the question.

## Reading of his labels (stated, because the whole round depends on it)

He clarified for `S^2`: "`psi` with a lower index of 1/2. That is, the harmonic
with `j=1/2, m=1/2`." So a single index is `m`, with `j=1/2` understood.

For `S^3` he writes pairs with one entry zero. Read as `(m_L, m_R)` under
`Spin(4) = SU(2)_L x SU(2)_R`, the four labels are the two states of `(j_L,j_R)
= (1/2,0)` and the two of `(0,1/2)` — the two Weyl spinors of the bispinor his
§2.2 uses at `n=3`. This reading is **assumed, not verified with him**, and if it
is wrong the labelling half of this round is answering a different question. It
is flagged as such in the reply.

---

## Prior Result Gate

1. `C180` (2026-09-07) computed the `S^3` spinor spectrum and eight explicit
   `k=1` eigenspinors — as `C^2`-valued linear polynomials in `x_0..x_3`, exact
   over `Q(i)`. **Not in Hopf coordinates, not labelled by `(j_L,j_R)`.**
2. `C182` (2026-09-07) did the `S^2` descent at the level of weight sectors and
   multiplicities (1,3,5 and 2,4,6) plus the fibre non-invariance argument.
   **No explicit `psi_{±1/2}(theta,phi)` anywhere.**
3. `C179` established the no-go itself.
4. `grep` for the bilinear-cancellation argument across the sent letter and the
   `2026-09-08` draft: **0 hits.** The sting has never been answered on paper.
5. `grep` for `spin-weighted` / `sYlm` formulas: term appears, formulas do not.
6. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for any of this.
7. **Status:** [x] NEW as to deliverables; the underlying mathematics is
   standard and this round claims no novelty in it.

---

## Mechanism Claim Gate (Step 0a)

Two sentences do justificatory work here and are checked, not asserted:

**M1.** "`L^2(S^3)` contains only `(j,j)` under `SU(2)_L x SU(2)_R`, so
`(1/2,0)` is not there at all." — Peter-Weyl. This is a **second, independent
proof of the no-go**, by direct decomposition rather than by the `2pi` argument.
Checked in Part C by explicit decomposition of levels `k=0..3`.

**M2.** "A section in the group trivialization transforms with a fibre rotation
under `SU(2)_R` but not under `SU(2)_L`, so the content is `⊕_j (j, j±1/2)`."
Checked in Part E against `C180`'s already-computed multiplicities: it predicts
`k=1` splits as `(1/2,0)` dim 2 and `(1/2,1)` dim 6 — which must match `C180`'s
`D_0` eigenvalues `+3` (mult 2) and `-1` (mult 6). A mismatch falsifies M2.

---

## Estimand

**Population:** the lowest spinor harmonics of `S^2` and `S^3`, and the
`Spin(4)` content of scalar and spinor function spaces on `S^3`.

**Intervention:** exact symbolic computation (sympy, exact rationals and
`Q(i)`), no floating point in any verdict.

**Comparator:** `C180`'s committed spectrum and multiplicities; the standard
`S^3` Dirac degeneracies `(k+1)(k+2)` and `k(k+1)`.

**Endpoint:** for each of the five deliverables, an explicit formula plus the
check that decides whether it is right.

**MCID:** not applicable — every endpoint is an exact identity.

---

## Pre-registered predictions (written BEFORE running)

| # | prediction | falsified if |
|---|---|---|
| P1 | `L^2(S^3)` level `k` decomposes as exactly `(k/2, k/2)`, nothing else | any off-diagonal `(j_L,j_R)` appears |
| P2 | spinor level `k=0` is `(0,1/2)`, `D_0 = 0`, dim 2 | different label, eigenvalue or dimension |
| P3 | spinor level `k=1` is `(1/2,0) ⊕ (1/2,1)`, with `D_0=+3` on the dim-2 piece and `D_0=-1` on the dim-6 piece | the `D_0` eigenvalue does not sort by irrep, or dims are not 2 and 6 |
| P4 | on `S^2`, `chi_± = e^{∓i phi/2} (cos(theta/2), sin(theta/2))` satisfy `chi(phi+2pi) = -chi(phi)` | the phase is not exactly `-1` |
| P5 | every bilinear `chi_a chi_b^*` is single-valued in `phi`, and `chi^† sigma chi` equals the unit vector `(sin th cos ph, sin th sin ph, cos th)` **exactly, all three components** | any component differs |
| P6 | `x^mu = (1/2) Tr(sigma_mu^† U)` returns `x_0..x_3` with the quaternionic basis `sigma_mu = (I, i s_1, i s_2, i s_3)`, and returns `(x_0, i x_1, i x_2, i x_3)` with the plain Pauli basis | either fails |

P3 is the sharp one: it is a prediction about **which** eigenvalue attaches to
**which** irrep, made from `M2` alone, tested against a number `C180` computed
seven weeks... one day earlier without reference to any of this.

---

## Floor and ceiling (Step 4a)

Most endpoints are exact identities, where the floor is not a score but a
question: **could the check have failed?** Each is therefore paired with an
injected-error control that must flip it.

The one place a real floor exists is P3. A criterion that assigned labels by
dimension alone would score 2 of 2 here by luck, because 2 and 6 happen to be
the only two dimensions available. So P3's floor is **not** "the dimensions
match" — it is that the `D_0` eigenvalue sorts by irrep, which dimension
matching does not supply. Stated so it is not later claimed as more than it is.

---

## Kill criteria

| outcome | verdict |
|---|---|
| all six predictions hold, all injected-error controls flip | **PROMOTE** — the five deliverables go into the reply |
| P1 or P2 fails | the no-go's second proof is wrong; STOP, this touches `C179`, escalate before writing anything to Tom |
| P3 fails | `M2` is wrong; the labelling half is withdrawn, `S^3` answered without `(j_L,j_R)` labels |
| P4 or P5 fails | the `S^2` construction is wrong; withdraw it, `S^2` answered only structurally as `C182` already does |
| any control fails to flip | `CRITERION_INVALID` for that item — report the check as incapable of failing, do not count it |

---

## What this does NOT mean

- Does **NOT** claim any new mathematics. Peter-Weyl, the `D^{1/2}` matrix
  elements and spin-weighted harmonics are textbook; the work here is getting
  them into his labels and his coordinates without error.
- Does **NOT** settle whether the `(m_L,m_R)` reading of his four labels is what
  he meant. That is an assumption, flagged above and in the reply.
- Does **NOT** produce the `S^2` Dirac operator or its eigenvalues `±(l+1)` —
  still not built, as the sent letter already says.
- Does **NOT** transport the harmonics into Riemann normal coordinates; that
  remains groundwork, as already stated to him.
- A constant in the group trivialization is **not** a constant in a coordinate
  frame. Any claim of the form "they are just constants" must carry the frame it
  is true in, or it is false.
