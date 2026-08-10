# decision — W1: does a non-factorizing `J` readmit a sector-mixing algebra?

**Verdict:** `W1_CLOSED__NO_J_ADMITS_A_SECTOR_MIXING_ALGEBRA` → **C50 REFUTED**, and
**C48/C49 upgraded from ansatz-limited to ansatz-free**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_w1.json` persisted.

---

## What was at stake

C48 and C49 both carried **ANSATZ J1** (`J = J_M ⊗ j` factorizes), flagged when written.
If a non-factorizing `J` readmitted the crossed product, C48's result 2 would have been
an artifact of my own ansatz **and** C49's failure of Poincaré duality would have been
lifted with it — the sector-mixing projection `p = (1+u)/2` gives index pairing **2**,
which C49 had already computed as its non-zero counter-case.

**The naive expectation was that W1 succeeds:** the crossed product's Tomita–Takesaki
conjugation *is* non-factorizing (it carries `U_ι` in one sector block only) and satisfies
order-zero automatically. That expectation is recorded in `claim.md` and it turned out
to be wrong for a reason that has nothing to do with order-zero.

## The argument

| step | content | status |
|---|---|---|
| **W1a** | `A'`'s sector-off-diagonal blocks all factor as `m·U_ι` (they must satisfy `T₀₁(f∘ι) = f T₀₁`) | [VERIFIED-numpy] on the finite model — commutant computed by SVD, checked against 8 random `f` per basis element |
| **W1b** | `[D_M, m U_ι] = {D_M, m}U_ι = ([D_M,m] + 2mD_M)U_ι` — **unbounded** unless `m = 0` | identity [VERIFIED-numpy] exactly; linear norm growth (ratio → 2.00) [VERIFIED-numpy]; **order-counting [INFERRED-analytic]**, see below |
| **W1c** | `[D,u] = −3i(I⊗s2)` is **bounded**, so `[D, JuJ⁻¹]` is bounded, so **`JuJ⁻¹` is sector-DIAGONAL** `= h⊗I` | [VERIFIED-numpy] — **and this step uses boundedness alone, never a factorization assumption** |
| **W1d** | `J(I⊗s2)J⁻¹ ∝ [D_M,h]⊗I` must be a unitary involution, so `[D_M,h]` is **invertible** | structural |
| **W1e** | but `[D_M,h]` bounded ⇒ `h` commutes with all Clifford multiplication ⇒ `h` scalar ⇒ `h = ±I` ⇒ `[D_M,h] = 0` — **not invertible. CONTRADICTION.** | Clifford commutant is 1-dimensional and scalar, [VERIFIED-numpy] |

> **C50 is REFUTED.** No antiunitary `J` with `JD = ±DJ` admits a sector-mixing algebra
> containing the sector swap — **factorizing or not**.

**W1c is the load-bearing step and it is ansatz-free.** That is the whole point: C48's
version of this conclusion came from restricting `J`'s sector action to `k m^T k⁻¹`;
this one comes from the boundedness of `[D,u]` and nothing else.

## Discrimination — the argument must not prove too much

Step 5 exhibited a `J` for the sector-**diagonal** algebra `T7`. An argument that also
killed `T7` would be wrong. It does not: the chain enters at W1c through `[D,u]` for a
sector-**off-diagonal** `u`, and `T7`'s sector parts are `{I, s3}`, both diagonal.
*(Structural observation, immediate from the symbol lists — recorded as such, not dressed
up as a numerical finding.)*

**Control:** the same code reproduces C48's factorizing no-go (`admissible k = NONE` for
`T4`), so the machinery is shown to recover the known result before being trusted on the
new one.

## Two of my own weak checks, caught and replaced

Both were versions of the failure this session already has a pearl about — a criterion
that cannot fail.

1. **W1b, v1** printed `2·max(n+3/2)` for rising truncations. That grows *by
   construction*.
2. **W1b, v2** compared it against `‖[D_M,m]‖` for a level-preserving `m` — which came
   out **exactly 0**, because such an `m` commutes with `D_M` in the toy. The "bounded"
   side was degenerate, so the comparison still could not fail.

**Final version splits what is verified from what is not.** The toy has no locality
structure and therefore *cannot* represent a bundle endomorphism's
`[D_M, m] = Clifford·dm`. So: the identity and the linear norm growth are
`[VERIFIED-numpy]`; the order-counting (`{D_M,m}` is order one, `[D_M,m]` is order zero)
is `[INFERRED-analytic]` — a fact about differential operators, **marked, not smuggled**.

---

## Kill Analysis

**Killed:** C50; escape route W1; and with it the last exit the C11 two-operator reading
had inside this framework.

**Upgraded rather than killed:** C48's result 2 and C49 — both were true but scoped by
ANSATZ J1, and are now **ansatz-free**. This is the payoff of having flagged the ansatz
at the time instead of quietly assuming it.

**Not killed:** C46 (parity doubling), C47 (isolated kernel), the sector-**diagonal**
triple `T7` with its `J`, and everything upstream (C42–C44).

**Relaxation Map — what actually remains:**

| Variant | Assumption relaxed | Honest assessment |
|---|---|---|
| Y1 | a sector-mixing algebra with **no** sector-swap unitary | a sliver: the argument enters through `u`, so this is untested — but it is not the crossed product, and the portfolio produced no such candidate |
| Y2 | `A`'s diagonal part **smaller** than the full twisted diagonal (enlarging `A'`) | a sliver; also makes the "geometry" less than `S³` (cf. `T6`, where the algebra is only `ι`-even functions) |
| Y3 | drop `JD = ±DJ` — i.e. abandon `J` as a real structure in the standard sense | legal, but then it is not a real spectral triple and Poincaré duality is not on the table anyway |

None of these is a route back to the crossed product.

## Bottom line for C11

The `t=0/t=1` doubling is **unearned from four directions now**, the last of them
ansatz-free: C44 (the grading is generic in `t`), C45 (no algebra forces it), C48+W1 (no
`J`, factorizing or not, admits a sector-mixing algebra), C49 (Poincaré duality fails).
What survives is C46 — *if* the doubling is taken, it is a **parity** doubling — and C47
— the 4-dim kernel is isolated, and C48 made that isolation a **selection**.

## What this does NOT show

- It does **not** show the doubling is *wrong*. It shows nothing in this framework
  *requires* it, which is a weaker and different statement.
- Inherits **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), still not re-derived.
- The finite model has 4 points and a 2-dim spinor fibre; it captures the *algebraic*
  structure of the `ι`-action, not the analysis. Where analysis is needed (W1b step iii)
  that is marked `[INFERRED-analytic]`.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
