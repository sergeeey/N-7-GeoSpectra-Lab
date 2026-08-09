# OB10 → C27 — Decision: the Majorana branch of C27's Relaxation Map is CLOSED

**Date:** 2026-08-06
**Verdict:** `MAJORANA_BRANCH_CLOSED__OTHER_TWO_ROWS_UNTOUCHED`

## What question this answers

C27/round78 established `dim ker(D_{S³,t=0}) = 2` (complex), giving 2 internal
zero modes per triality channel — **6 total instead of the needed 3**. Its
Relaxation Map lists three escape routes. Round78 examined the first one
("new reality/Majorana condition") and reported only an **absence**: it
grepped `preprint.tex` for "Majorana"/"reality condition"/"Weyl condition",
found nothing, and concluded no such condition *is currently imposed*.

**It never asked whether one COULD be imposed.** This round asks that.

## What was newly computed [VERIFIED-sympy, `ob10_c27_majorana_halving.py`]

**1. OB10's `B` factorizes cleanly along the S³/S⁶ split.** OB10's unique
charge-conjugation operator `B = σ₂⊗σ₂⊗σ₁⊗σ₂` on the 16-dim module equals
`B_{S³} ⊗ B_{S⁶}` exactly, with `B_{S³}=σ₂` (the 2-dim S³ spinor slot, per
OB10's own construction where `E=[kron(Z_j,Γ₇)]`, `F=[kron(I₂,G6_i)]`).
This was not assumed — it could have mixed the factors, and was checked.

**2. The pseudo-reality comes ENTIRELY from the S³ factor:**

| factor | `B·conj(B)` | type |
|---|---|---|
| S³ (2-dim) | `−I₂` | **PSEUDO-REAL** |
| S⁶ (8-dim) | `+I₈` | REAL |
| product (16-dim) | `−I₁₆` | PSEUDO-REAL (= (−1)·(+1)) |

**This is the load-bearing coincidence:** C27's excess factor of 2 lives in
the *same* factor (`dim ker(D_{S³})=2` vs `dim ker(D_{S⁶})=1` per channel).
The no-go bites exactly where the problem is.

**3. The Majorana condition has only the trivial solution.** Solving
`ψ = B_{S³}·conj(ψ)` for a fully generic `ψ ∈ ℂ²` (split into real and
imaginary parts, so `conj` is handled honestly rather than by symbolic
`conjugate()` on free symbols): **0 free real parameters** → only `ψ=0`.

**4. No other antilinear structure rescues it — EXHAUSTIVE.** Step 3 alone
would only rule out OB10's *particular* `B`. Searched *all* antilinear
`J = M∘conj` for fully generic complex 2×2 `M`, imposing compatibility with
the S³ Clifford action (`M·conj(Z_i) = η·Z_i·M`, shared sign `η=±1`):
- `η=−1`: only the trivial `M=0` — no structure at all.
- `η=+1`: the solution family gives `M·conj(M) = −(mr₂²+mi₂²)·I₂` — **minus an
  explicit sum of squares**, hence strictly negative for any nonzero `M`.

**Every** compatible antilinear structure on this space is pseudo-real. No
real one exists. This upgrades the finding from "OB10's B doesn't work" to a
property of the 2-dim Cl(0,3) module itself.

**5. A phase does not rescue it.** For `ψ = λ·B·conj(ψ)`, iterating twice
gives `ψ = |λ|²·(B·conj(B))·ψ = −|λ|²·ψ`, requiring `−|λ|² = 1` — impossible
for a real modulus.

**6. It survives to `t=1`.** The `t=1` zero mode is `ψ(x)=ḡ(x)·ψ₀`, an
x-dependent family. Verified the identity `B_{S³}·conj(ḡ(x)) = ḡ(x)·B_{S³}`
holds *identically in x*, so the condition reduces exactly to the `t=0` case
already tested. Both endpoints, same answer.

**7. The standard workaround is separately blocked.** For a pseudo-real
structure the textbook fix is a *symplectic*-Majorana condition pairing an
**even** number of flavors (`ψ^A = B·conj(ψ^B)·ε_AB`). This project has
**three** triality channels (G67/G73), and 3 is odd — no symmetric pairing
exists. Pairing two and leaving one out would break the equal geometric
status of the three channels, which is precisely what `C_G67C3` and the
`N_gen=3` claim rest on.

## Negative control [MANDATORY, per this project's Gate 3 discipline]

A test that cannot distinguish a real from a pseudo-real structure is not a
test. Ran the identical solver on `B=σ₁` (genuinely real, `B·conj(B)=+I₂`):
**4 free real parameters** — solutions found, as they must be.
`0 vs 4` — the test discriminates.

## Honest scoping — what is standard and what is not

**The core algebraic fact is textbook:** the SU(2) fundamental / 2-dim
Cl(0,3) module is quaternionic, and quaternionic ⟹ no Majorana condition.
Anyone with the relevant background can state that in one line.

Per this project's own **one-line-reducibility test** (`pearl_registry`, added
after round114 was falsified for exactly this failure mode — a "cross-check"
that collapsed into restating the source's own theorem), this round is
explicitly checked against that trap. What is **not** reducible to citing the
textbook fact:

1. that OB10's independently-derived `B` factorizes so the textbook fact
   applies to *this* construction (it could have mixed the two factors);
2. that C27's excess lives in exactly that factor (needed round78's
   decomposition — the two results were produced 20 days apart and were never
   connected);
3. that `t=1` reduces to `t=0` (needed the `ḡ(x)` intertwining identity);
4. the odd-channel-count obstruction to the symplectic workaround, which is
   specific to *this* project's 3-channel structure and appears in no textbook.

**The contribution is the connection and the closure of a specific listed
escape route — not a new mathematical fact.** Stated plainly so no future
reader mistakes this for more than it is.

## Consequence for C27 / OB9

C27's Relaxation Map had three rows. **One is now closed:**

| Row | Status after this round |
|---|---|
| New reality/Majorana condition | **CLOSED** — structurally impossible, not merely absent |
| New projection specific to the S³ factor | **OPEN**, untouched |
| Reconcile the 32-state and zero-mode-kernel frameworks | **OPEN**, untouched |

Round78's own recommendation — that the 32-state reconciliation is "the FIRST
question to resolve" — is *strengthened*, not weakened: with the Majorana row
eliminated, the remaining option space narrows to two, and the 32-state
reconciliation is the one round78 already flagged as most likely load-bearing.

## What this does NOT mean

1. Does **NOT** resolve C27. The multiplicity-2 problem is fully intact; this
   removes one candidate solution, it does not supply one. **The excess factor
   of 2 remains exactly as unresolved as before.**
2. Does **NOT** weaken `N_gen=3` further — that claim's status is unchanged
   (it was already CONDITIONAL on this same gap).
3. Does **NOT** touch OB1/KT-8 (no zero mode for the full operator), H1c
   (which of t=0/t=1 is selected), or OB4.
4. Does **NOT** claim the symplectic-Majorana route is impossible in
   principle — only that no *channel-symmetric* version exists with 3
   channels. A construction that doubles the space first (6 channels) is not
   examined here and is not obviously available.
5. Does **NOT** revisit whether `D_full² = D_{S³,t}²⊗I + I⊗D_{S⁶}²` holds for
   the torsion-deformed S³ factor — round78's own carried assumption, still
   `[INFERRED]`, still unverified.

## Check (reproduces this decision)

```
cd experiments/20260806-ob10-c27-majorana-halving
python ob10_c27_majorana_halving.py
```
Expect: `B_factorizes_S3_tensor_S6=True`, `S3_factor_pseudoreal=True`,
`S6_factor_real=True`, `S3_majorana_free_params=0`,
`no_real_structure_exists_on_S3_factor=True`,
`control_majorana_free_params=4` (control discriminates),
`phase_cannot_rescue=True`, `t1_reduces_to_t0=True`,
`verdict="MAJORANA_BRANCH_CLOSED"`.

## Methodological note (a real bug caught in this round's own check)

The first version of the exhaustive search flagged
`no_real_structure_exists=True` **by accident**: it tested
`not scal.is_positive`, and sympy returns `None` (undecidable) for the
symbolic expression `−mi₂²−mr₂²`, so `not None` evaluated True. The flag
passed without proving anything. Caught on the first run and replaced with an
exact check that the coefficient is *minus an explicit sum of squares* (all
monomials even-powered with positive coefficients) — a statement that is
decidable and was decided. Logged here because "the guard passed for the
wrong reason" is a distinct and more dangerous failure than "the guard
failed."
