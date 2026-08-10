# decision — C11 step 6: Poincaré duality via the index pairing

**Verdict:** `EVEN_INDEX_PAIRING_VANISHES_IDENTICALLY__PD_FAILS_FOR_THIS_TRIPLE` → **C49**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_step6.json` persisted.

---

## Why step 6 became cheap

The portfolio recorded step 6's cost as *"unknown until step 1"*. C48 settled it: `J`
forces `A` to be the **twisted diagonal**, acting **sector-diagonally** as
`diag(f, f∘ι)`. Poincaré duality is defined relative to `A`, and the cheapest necessary
condition is that the index pairing of the fundamental class with `K`-theory be
non-degenerate. For a sector-diagonal algebra that is a two-line computation.

## The result

| step | finding |
|---|---|
| **S1** | `ker(D^0)` is level `(n=0, σ=+1)`, dim 2; `ker(D^1)` is `(n=0, σ=−1)`, dim 2. `U_ι` sends `(n,σ) → (n,−σ)` and `s1` swaps sectors, so `γ` maps `ker(D^0)` **onto** `ker(D^1)`: `γ|ker` is purely **off-diagonal**. |
| **S2** | `γ|ker` has eigenvalues `+1,+1,−1,−1`; `Tr(γ|ker) = 0`, so **`ind(D_block) = 0`**. |
| **S3** | The pairing vanishes for **every** `p ∈ A`, and the test **discriminates** (below). |
| **S4** | One sector alone is an **odd** triple (no grading — C35/C43), pairing with `K₁` by spectral flow, and `spec(D^0) = {0,1,2,…} ∪ {−3,−4,…}` **is** asymmetric. |

> **C49.** The doubled even triple's index pairing vanishes identically. A necessary
> condition for Poincaré duality **fails**: the fundamental class this triple defines is
> trivial.

## The mechanism, and why it is not a coincidence

`γ` **must** be off-diagonal in the sector index — that is exactly what made it exist
(C45: both factors needed, `U_ι` flips `D^{1/2}` and `s1` flips `s3`). An off-diagonal
involution has zero trace on the kernel it permutes. **The grading and the vanishing
pairing are two faces of one structure.**

So the doubling does not merely fail to *earn* itself (C44/C45/C48) — on this probe it
**costs** something: the single sector's spectral asymmetry, which is precisely what an
odd triple pairs with, is cancelled by construction.

## A tautological test, caught and replaced

The first version of S3 sampled 200 random block-diagonal `diag(P,P)` against a purely
off-diagonal `γ|ker`. `Tr = 0` held **by shape alone**, for any algebra whatsoever — a
criterion that could not fail, exactly the disease this session's own pearl (2026-08-10,
C45) predicts recurring. Replaced by:

- (a) every `p ∈ A` is sector-block-diagonal **[C48]**;
- (b) `γ|ker` is purely sector-off-diagonal **[S1]**;
- (c) therefore `Tr(γp) = 0` — by (a)+(b), a one-line consequence, **not** a numerical
  discovery;
- (d) **the counter-case**: sector-**mixing** projections give
  `Tr(γp) = 0, 0.7788, 1.6829, 1.9271` — **non-zero**.

(d) is what gives (c) content: **the pairing vanishes *because* `J` forced the algebra to
be sector-diagonal.** The crossed product `T4`, which `J` excluded, would **not** have
vanished. Step 6 therefore does not stand alone — it is the price of C48's result.

---

## Kill Analysis

**Killed:** Poincaré duality for the doubled even triple as constructed. With C48, the
`PARENT_ACTION_GATE` line on Poincaré duality cannot be filled by this object.

**Not killed:** classical PD for `S³` itself (it holds, in the odd/KO-3 sense — this
triple is not `S³`'s). C42, C43 (amended), C44, C46, C47 untouched. C48 is *reinforced*:
its consequence is what produces this one.

**Relaxation Map:**

| Variant | Assumption relaxed | Status |
|---|---|---|
| X1 | escape **W1** — a `J` that does not factor as `J_M ⊗ j`, which could readmit a sector-mixing algebra and hence a non-zero pairing | **untested; still the highest-value open question** |
| X2 | keep the triple **odd** (one sector), accept no grading, pair with `K₁` | legal, and it is just the undoubled theory — i.e. abandoning C11's two-operator reading |
| X3 | accept a trivial fundamental class and drop PD from the requirements | possible, but PD is what makes the object a *geometry* rather than an algebra with an operator |

---

## PARENT_ACTION_GATE, final state for this portfolio

```
H        SUPPLIED
D        SUPPLIED
gamma    SUPPLIED   but GENERIC in t (C44) and non-unique (C45)
A        SUPPLIED   forced to the twisted diagonal by J (C48) -- sector-DIAGONAL
J        SUPPLIED   for T7/T6; NOT for the maximal algebra (C48)
PD       FAILS      index pairing identically zero (C49, this file)
physics  NOT        "why two copies at all" -- unanswered, and now with three
                    independent results saying nothing forces them
```

## What this does NOT show

- It does **not** say `S³` fails Poincaré duality. It does not; this triple is not `S³`.
- It says **nothing** about the `S⁶` index behind `N_gen = 3` — different operator,
  different manifold, and **step 7 remains untouched by agreement.**
- Vanishing of the index pairing is a **necessary** condition failing. It does not by
  itself characterise every way PD could fail or be repaired.
- Inherits **ASSUMPTION A1** and **ANSATZ J1** from C45/C48.
