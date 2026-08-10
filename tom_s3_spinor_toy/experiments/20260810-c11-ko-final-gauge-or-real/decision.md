# decision — KO tuple, finally: the KO-2/KO-4 split is real, not gauge

**Verdict:** `KO_SPLIT_IS_REAL_NOT_GAUGE__C57_CONFIRMED_AS_FINAL` → **C60 REFUTED**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_ko_final.json` persisted.

---

## The question

C57 found exactly two survivors of order-zero + `JD=ε'DJ` + `Jγ=ε''γJ`: `k=I` (KO-dim 4)
and `k=s3` (KO-dim 2), calling the choice *"internal to `J`, not geometric"* — but never
checked whether the two are secretly **the same triple in two descriptions**. C59 just
proved the analogous question for the `S³`-factor lift `J_M` (unique up to phase, Schur).
This round checks whether a sector-only change of basis relates `k=I` to `k=s3`.

## The transformation law, derived carefully

For `V = I_M ⊗ v` and `J = J_M ⊗ (k·conj)`:

```
(V J V⁻¹)(x⊗y) = J_M x ⊗ [v k v^T] conj(y)        so:  k' = v k v^T
```

*(not `v k v^†`* — the extra transpose comes from `J`'s antilinearity; written out
explicitly rather than guessed, exactly the kind of step C59 caught a sign error in.)

## Results, all [VERIFIED]

| step | finding |
|---|---|
| **G1** | the commutant of `s3` (`D_block`'s sector part) among general `2×2` `v` is **exactly** the 2 diagonal directions [VERIFIED-numpy, SVD null space] — any `V` preserving `D_block` exactly must be sector-diagonal |
| **G2** | for diagonal `v=diag(v1,v2)`, `v s1 v† ∝ s1` **iff** `v1=±v2` [VERIFIED-sympy+numpy] — generic phases fail |
| **G3/G4** | for **all** admissible `v = diag(e^{iα}, σe^{iα})`, `σ=±1`, at once (not spot-checked): `k=I`'s orbit stays **exactly** `{phase·I}`; `k=s3`'s orbit stays **exactly** `{phase·s3}` [VERIFIED-sympy] — `σ` cancels (`σ²=1`) from both |
| **G5, discriminator** | the same machinery correctly recovers the **known trivial** equivalence `k=I ∼ e^{iθ}I` (`α=θ/2` exactly) [VERIFIED] |

**Two orbits, each a 1-complex-dimensional ray (`phase·I` and `phase·s3`), and `I`, `s3`
are linearly independent — the rays never meet.**

## Two harness bugs, caught and fixed before accepting the verdict

1. **G3/G4** initially compared symbolic matrices containing a free `σ` via sympy's `==`,
   which doesn't know `σ²=1` unless told — the check returned `False` even though the
   underlying algebra was already correct. Fixed by substituting `σ=+1` and `σ=−1`
   explicitly and requiring **both** to match (a stronger check, not a weaker one).
2. **G5** initially grid-searched 2000 points over `[0,2π]` with tolerance `1e-6` — far
   tighter than the `~π/1000` grid spacing, so it could (and did) miss the exact solution
   `α=0.45`. `e^{2iα}=e^{iθ}` has the closed form `α=θ/2`; fixed by solving directly
   instead of searching.

Neither bug touched the mathematics (G1, G2 were correct on the first pass) — both were
in how the check was *evaluated*, caught before the verdict was written down.

---

## Kill Analysis

**Killed:** C60 (the "gauge artifact" hypothesis). **Confirmed, now as a proof rather than
an assertion:** C57's *"internal to `J`, not geometric"* is the final word within this
framework — a genuine, irreducible bifurcation, not a hidden relabelling.

**Residual, named not hidden:** only **sector-only** automorphisms (`V = I_M ⊗ v`) were
checked. A more general `V = V_M ⊗ v` mixing the `S³` factor too is **untested**. Given C59
already pins `V_M` to a phase (unique up to phase on each isotypic block, by Schur), such a
`V` could only rescale `k` by *another* overall phase — it has no room to supply new
sector-mixing freedom — but this is stated as the honest remaining gap, not assumed closed.

## Where this leaves the whole chain

The `S³`-factor lift is unique up to phase (C59); the sector factor now has **two**
genuinely inequivalent, phase-independent choices (`k=I`, `k=s3`), giving KO-dimension 4 or
2, with **nothing in `(A, H, D_block, γ)`** to select between them. That is the complete,
final characterization of the KO-dimension ambiguity for this construction.

## What this does NOT show

- **Zero consequence for whether the doubled triple is a geometry.** C49 (Poincaré duality
  fails) and C52 (orientability fails) already settled that, independent of KO-dimension.
  This is bookkeeping on bookkeeping on a non-geometry, and is scoped that way throughout.
- Does not search the full automorphism group (see residual, above).
- Nothing about `N_gen=3` — closed at C58, untouched here.
