# decision — step 5 (scoped): the S³ torsion mechanism is never multiplicity-safe

## Verdict

`S3_TORSION_MECHANISM_NEVER_MULTIPLICITY_SAFE` → **C64 SUPPORTED.**
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_step5.json` persisted.

---

## What was checked and how

Reused E2's own Clifford generators, `omega`/`H` scalar-construction, and `h_H` calibration
unmodified. Built the explicit `D^t` matrix restricted to the n=0 Levi-Civita eigenspace
(2-dimensional, eigenvalue 3/2, multiplicity `(0+1)(0+2)=2` — a fact E2's own calibration
step already used) and checked whether the known crossing at `t=0` kills the whole eigenspace
or just one state within it.

## Results, all [VERIFIED-sympy]

| check | predicted | found |
|---|---|---|
| **P1** re-verify E2's `omega`/`H` scalar result | reproduces E2 | ✓ (`omega_ok=True`, reused directly) |
| **P2** `D^t\|_{n=0}` is exactly scalar (not merely diagonal) | `[σ(3/2)+(t-1/2)·3]·I₂` | **`D^t\|_{n=0} = 3t·I₂`** exactly ✓ |
| **P3** at `t=0`, this is the exact zero matrix | rank 0, dim ker 2 | **exact zero matrix**, `rank=0`, `dim ker=2` ✓ — not rank 1 |
| **P4** every E2 crossing has multiplicity ≥2 | `(n+1)(n+2)` for n=0,1,2 | **2, 2, 6, 6, 12, 12** — all ≥2, none =1 ✓ |

## Interpretation

E2 computed *where* `D^t`'s eigenvalue crosses zero but did not itself report *how many* states
cross there. **round116 (2026-07-17) already caught this** — its skeptic-reviewed Finding 2
states the same numbers (`t=0,1`: multiplicity 2 each; `t=-1/3,4/3`: multiplicity 6 each),
logged as a pearl. This round is not a fresh discovery of the gap; it does two things round116
did not: (a) verifies the fact directly by constructing the actual 2×2 matrix (round116 cited
the multiplicity "already established elsewhere," it did not itself build or check the matrix),
confirming the crossing is a genuine exact-zero-matrix collapse, not merely an assumed
consequence of the abstract formula; and (b) works out the actual physical consequence round116
raised but explicitly declined to justify — its own item 3 states "does NOT affect `N_gen=3`"
without explaining why.

That consequence, worked out here via E3's product-decoupling identity
(`ker(D_full)=ker(D_S6)⊗ker(D_S3)`): **round116's dismissal is correct for the construction as it
currently stands (Levi-Civita, `t=1/2`, `dim ker(D_S3)=0`) but does not generalize** — if E2/E3's
torsion-deformation mechanism, the one candidate this project has on record for giving the full
`S³×S⁶` operator a nonzero kernel at all, is ever used to resolve OB1, it would multiply the
generation count by at least 2 (cheapest crossing) via that same identity. This is exactly the
"S³ as an unwanted generation-multiplying factor" scenario the user's step-5 instruction warned
against — a real structural property of the one mechanism on record, not a merely hypothetical
risk, and previously stated only as an unresolved "does not affect" claim, not verified either
way.

## Why this does NOT threaten `N_gen=3` as currently derived

The construction `N_gen=3` currently rests on (S⁶ alone, three triality channels, index 1 each)
does not use the torsion-deformed S³ connection at all — the relevant case is Levi-Civita
(`t=1/2`), where E2/E3 already establish `dim ker(D_S3)=0` (not 2), and `N_gen=3`'s own
derivation has never invoked the S³ factor contributing any zero mode. This round's finding is
a **caveat for OB1's own future record**: if the torsion escape route is ever picked up again
as a way to solve OB1 (give the full operator *some* kernel), whoever does so needs to also
solve a *second*, previously-unnoticed problem (removing the forced ≥2 multiplicity) — not a
new threat to the headline result as it stands today.

## Pearl Gate scan

**Existing pearl (round116, 2026-07-17), partially advanced, not newly triggered:** its own
trigger condition ("any future round that invokes a spectral-flow-type integer") has not fired —
this round did not compute a spectral-flow integer, it worked out the OB1-resolution-safety
consequence instead, an angle the pearl's trigger did not anticipate. Left as `pending`, not
marked resolved, since the specific triggering event it names still has not happened. One new,
genuinely unanticipated observation worth its own note: the "uniform scalar shift ⟹
whole-eigenspace crossing" structure is a general fact about ANY one-parameter Dirac deformation
built from a *central* Clifford element (Kostant's `H` reducing to the volume element is specific
to `dim m=3`, per E2's own docstring) — any future odd-3-dimensional naturally-reductive factor
using this SAME Agricola/Kostant construction elsewhere in this project's search space would
inherit the identical multiplicity-≥2 property automatically, without a fresh per-case check.

## What this does NOT show

1. Does **not** resolve or reopen OB1 — no physical `t` is selected, and this finding narrows
   (does not strengthen) the one candidate mechanism on record.
2. Does **not** touch `N_gen=3`'s CONDITIONAL status — the currently-relevant (Levi-Civita) case
   is unaffected, see above.
3. Does **not** build the full `D_{S3×S6}` product operator or verify the product-decoupling
   formula for the torsion-deformed case beyond what E3 already established.
4. Does **not** rule out that a fuller construction (chirality/gauge projection, a different
   combination of levels) could cut the multiplicity back to 1 — only that the bare mechanism,
   as E2/E3 left it, does not.

## Check (reproduces this derivation)

```
cd experiments/20260810-step5-s3-torsion-multiplicity-safety
python step5_s3_multiplicity_safety.py
```
Expect: `D^t|_{n=0} = 3t·I₂`, exact zero matrix at `t=0` (`rank=0`, `dim ker=2`), multiplicity
table `2,2,6,6,12,12`, `VERDICT: S3_TORSION_MECHANISM_NEVER_MULTIPLICITY_SAFE`.
