# Test (c) — `ι` is PARITY, not gauge. The ill-posedness branch is dead.

**Date:** 2026-08-10
**Verdict:** `IOTA_IS_ORIENTATION_REVERSING__PARITY_NOT_GAUGE`
**Runs:** test (c) from the consortium run — *"does `ι` act trivially on all
observables?"* — reformulated to the sharper question that actually decides it.

## Why this test decides the consolidated question

C38 showed `ker(D_{S³},t=0) = (1,2)` and `ker(D_{S³},t=1) = (2,1)`, exchanged by
`ι`. C37/OB13 raised the branch that `ι` might be a **gauge** redundancy, making
"which `t`" ill-posed. **Those two readings conflict:**

- `ι` **gauge** → `(1,2)` and `(2,1)` are the same physical state, there is no
  4-dim spinor, and C38's reconciliation collapses;
- `ι` **discrete/parity** → the two halves are genuinely distinct states and C38
  stands.

One computation separates them. A gauge symmetry is connected to the identity,
hence **orientation-preserving**; a parity is **orientation-reversing**.

## Result [VERIFIED-numpy]

In quaternion coordinates `ι : (x₀, x⃗) ↦ (x₀, −x⃗)` — verified as
`g(x)⁻¹ = g(ι x)` at 200 random unit `x`, not assumed.

| check | result |
|---|---|
| det of the induced map on `T_x S³`, 200 sampled points | **−1.000 at every point** (min = max) |
| `\|det\| = 1` (is an isometry) | ✓ |
| **negative control:** left translation `g ↦ ag` | **+1 at all 100 points** ✓ |

**`ι` is an orientation-reversing isometry of `S³`. It is not gauge.**

## Consequences

1. **C37/OB13's "H1c may be ill-posed because `ι` is gauge" branch is DEAD.**
   Recorded as a killed branch, not left ambiguous.
2. **C38 stands.** `(1,2)` and `(2,1)` are genuinely distinct physical states,
   exchanged by **parity** — which is exactly how `SU(2)_L` and `SU(2)_R` relate
   in the Standard Model.
3. **C37 and this result are the same statement in two languages.** C37: a
   selector must be **odd** in `(t−½)`. Here: `t=0`/`t=1` are a **parity pair**.
   A parity-odd term is precisely what breaks a parity pair. The two arrived
   independently — one from polynomial parity of computed invariants, one from
   the orientation of a diffeomorphism — and agree.

So "which endpoint is realized" is **not** ill-posed; it is the question of what
breaks parity. In the SM parity *is* broken, so a selector is expected to exist
rather than being a category error.

## Two bugs in this file's own machinery, both caught by the negative control

Recorded because the control earned its place twice in one sitting:

1. **Wrong quaternion coordinate extraction.** The 4×4 matrix of left
   translation was built using `Re g[1,0] = −x₂` where `Re g[0,1] = +x₂` was
   meant. One flipped sign → determinant flipped → control failed. Fixed and a
   round-trip identity `coords(g_of(x)) == x` now pins it.
2. **Un-oriented QR bases.** `np.linalg.qr` returns a basis whose orientation
   depends on internal sign conventions, so comparing `det` between two
   independently-QR'd tangent bases measures the two QR calls, not the map.
   Fixed by pinning `det([normal | basis]) = +1`, tying every tangent basis to
   the same ambient orientation.

Both times the control failed **before** the headline claim was recorded. Had it
been omitted, this file would have confidently reported the right verdict from
broken machinery — which is worse than reporting the wrong one, because it would
never have been revisited.

## What this does NOT establish

1. Does **not** show that any particular term in an action selects an endpoint.
   That is `C11`, still OPEN, and still the live question.
2. Does **not** resolve `C27`. It removes one branch from the consolidated
   question, it does not answer it.
3. Does **not** identify the parity-odd term. It says one is needed and is
   *expected* on SM grounds — an expectation is not a construction.
4. Says nothing about the S⁶-side factor-8 mismatch (C38's open half).

## Check

```
python experiments/20260810-iota-gauge-or-parity/iota_test.py
```
Expect `VERDICT: IOTA_IS_ORIENTATION_REVERSING__PARITY_NOT_GAUGE`; tangent det
−1 at all 200 points; left-translation control +1 at all 100.
