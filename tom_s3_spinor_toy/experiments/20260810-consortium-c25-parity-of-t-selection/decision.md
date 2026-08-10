# Consortium #3 — C25/H1c: we have been searching in the wrong parity sector

**Date:** 2026-08-10 · **Depth:** Глубокий (FL Standard)
**Verdict:** `SELECTION_REQUIRES_A_TORSION-ODD_TERM__ALL_INVARIANTS_TRIED_SO_FAR_ARE_EVEN`
**Target:** `C25_H1C_PHYSICAL_SELECTION_OPEN` — which of `t=0` / `t=1` is realized.

## L0 — question type: Causal

*What must be added to the action for one endpoint to be selected?* **Does NOT
mean:** (1) that a selector exists; (2) anything about C27 or OB4; (3) that the
term identified below is physically motivated — only that nothing else can work.

## The anomaly (mode: Аномалия), computed [VERIFIED-sympy]

Parity of every `t`-dependent invariant this project has computed, under the
substitution `t → 1−t`:

| quantity | source | form | parity in `(t−½)` |
|---|---|---|---|
| `Scal(t) = Scal_LC − 6(2t−1)²` | round111 | quadratic | **EVEN** |
| curvature-norm toy `V(t)` | round99 | quadratic | **EVEN** |
| Dirac family `D^t(n,σ) = σ(n+3/2) + (t−½)·h_H` | E2/round67 | linear shift | **ODD** |

## The invisible line

`t → 1−t` is `(t−½) → −(t−½)`. So **any quantity that is an even function of
`(t−½)` is identically blind to the `t=0` vs `t=1` question** — not "has not yet
distinguished them", but *cannot*, as a matter of parity.

Both curvature-based searches (round99, round111) are even. **Their null results
were structurally necessary and carry no information about whether a selector
exists.** They were never tests of H1c.

Round80/E14 makes this a symmetry statement rather than an algebraic accident:
the isometry `ι(g) = g⁻¹` pulls the *whole* Cartan–Schouten family `∇^t` back to
`∇^(1−t)` **exactly** — verdict `PASS_GEOMETRIC_Z2_CONFIRMED`. So `t ↔ 1−t` is a
genuine **symmetry of the geometry**, and a symmetry can only be broken by a term
**odd** under it.

**Consequence:** a selection principle, if one exists, must be **linear (odd) in
the torsion**, never quadratic. The Dirac spectral shift `(t−½)·h_H` is the one
odd object already in hand.

## Three worlds (mode: Инверсия — what is true if there is no selector?)

| # | world | positive prediction if true |
|---|---|---|
| M1 | a selector exists | it appears in a torsion-**odd** term: parity-odd / Chern–Simons-like, or a fermionic term linear in the Dirac shift |
| M2 | **the question is ill-posed** — `t=0` and `t=1` are gauge-equivalent via `ι` | no selector will ever be found, and looking for one is the error. `H1c` should be **closed as ill-posed**, not left OPEN |
| M3 | both are realized (this is the open fork `C11`) | needs the product-ansatz question answered first |

**M2 is the inversion branch and it is not currently represented in the ledger.**
`C25` is recorded as OPEN, which presupposes an answer exists. If `ι` is a genuine
gauge symmetry rather than a mere isometry, "which endpoint" is like asking which
gauge representative is physical — and every even-parity null result to date is
exactly what M2 predicts.

## Anti-confirmation

- 🔴 **Survivorship** — two searches failed, but both were in the blind (even)
  sector, so their failure is evidence about the *method*, not the *question*.
  Reading them as "selection is hard" is the error this round corrects.
- 🟡 **Goodhart** — "find the selector" has been the framing; M2 says the framing
  is the bug.
- 🟡 **Scope** — parity checked for **three** quantities, the ones this project
  actually computed. This is not a theorem that all conceivable invariants are
  even; it is a fact about what has been tried.

## Cheapest differentiating test — ONE

**Is `ι` a gauge symmetry or merely an isometry?** Concretely: does `ι` act
trivially on the physical observables (spectrum *and* the zero-mode content),
or does it move something measurable?

- Acts trivially on everything → **M2**: close `C25` as ill-posed; that is a
  result, not a failure, and it retires a long-standing OPEN item.
- Moves something → **M1**: the moved quantity is the selector, and by the parity
  argument it is necessarily torsion-odd. Look there and nowhere else.

Discriminating, non-circular, and reuses round80/E14's existing machinery.

## What this does NOT establish

1. Does **not** show a selector exists or does not exist.
2. Does **not** close `C25` — it identifies M2 as a live, unrepresented branch.
3. The parity fact covers the three quantities actually computed, not all
   possible invariants.
4. Does not touch `C11`'s product-ansatz fork, C27, or OB4.
