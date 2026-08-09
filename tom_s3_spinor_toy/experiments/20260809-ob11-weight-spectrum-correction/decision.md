# OB11 (i) — C29's conclusion stands, its evidence was insufficient

**Date:** 2026-08-09
**Verdict:** `C29_CONCLUSION_STANDS__EVIDENCE_CORRECTED`

## The criticism, and it is correct

An external red-team audit flagged that C29's headline — "each channel
decomposes as `1⊕1⊕3⊕3̄` under `su(3)`" — does not follow from what C29
computed. C29 diagonalised the **quadratic** Casimir and found, per channel,
2 zero eigenvalues + 6 at one shared nonzero value.

Verified here as a control: `C₂(3) = C₂(3̄) = 4/3` exactly. So that spectrum
is equally consistent with `1⊕1⊕3⊕3̄`, `1⊕1⊕3⊕3`, and `1⊕1⊕3̄⊕3̄`. **The
criticism is right.** (C29's own `claim.md` did flag the limitation; its
`decision.md` headline nonetheless said "directly confirms", which overstates.)

## But the remedy was already in the repo

The audit's suggested fix was a cubic Casimir or full weight computation.
Neither is needed — the discriminating number has been sitting in this project
since **G102** (2026-07-05), and **round127 already used exactly this
argument**:

```
Hom(V,V) = sum over irreps of (multiplicity)^2
    1+1+3+3bar      ->  2^2 + 1^2 + 1^2  =  6
    1+1+3+3         ->  2^2 + 2^2        =  8
    1+1+3bar+3bar   ->  2^2 + 2^2        =  8
```

G102 S7 measured `Hom_su3 = 6` for all nine pairs, diagonal included —
reproduced here directly. `Hom = 6` excludes both `Hom = 8` alternatives.

**Negative control** (mandatory — a criterion that accepts everything proves
nothing): built `1⊕1⊕3⊕3̄` and `1⊕1⊕3⊕3` explicitly as 8×8 matrices and
measured their Hom dimensions with G102's own `hom_dim`. Got **6** and **8**
respectively, matching prediction. The criterion discriminates.

## Net effect

| | before | after |
|---|---|---|
| C29's **conclusion** | `1⊕1⊕3⊕3̄` | unchanged — **correct** |
| C29's **evidence** | quadratic Casimir | insufficient; replaced by `Hom = 6` |
| Anything recomputed | — | nothing; only re-cited |

C29 reached for the wrong tool when the right one was already computed. That
is a weaker failure than OB10's (which reached a wrong *answer*), but it is
the same underlying shape: a check that could not have distinguished the
claimed outcome from its alternatives was reported as if it had.

## Two of my own failed attempts, recorded rather than dropped

The first version of this file built a **weight negation-symmetry** test. It
**failed its own negative control**, for two stacked reasons:

1. **Vacuity.** G102's channel reps are *real antisymmetric* matrices. Their
   eigenvalues are purely imaginary and therefore **automatically** symmetric
   under negation — the test would have passed anything, including a genuinely
   non-self-conjugate rep.
2. **Apples-to-oranges.** The control matrices were built hermitian (real
   eigenvalues), so taking imaginary parts zeroed them, making the control
   trivially "symmetric" as well.

Both were caught by the negative control, which is the entire reason it was
written before trusting the result. Recorded here because "my discriminating
test was structurally incapable of discriminating" is exactly the failure this
round was convened to fix in someone else's work.

## What this does NOT mean

1. Does **NOT** resolve OB11. Only condition (i) is addressed; conditions
   (ii) (no channel-mixing in the Dirac operator) and (iii) (triality acting
   as `1⊗t`) remain open and are the expensive ones.
2. Does **NOT** establish the `H_matter⊗H_generation` factorization. Identical
   `su(3)` content across channels is necessary, not sufficient — the audit
   separately (and correctly) notes that a genuine tensor factorization is a
   **commutant** question: one needs `I_matter ⊗ M₃(ℂ)` inside the commutant
   of the full algebra, which nothing here tests.
3. Does **NOT** address the audit's triality-orbit alternative — that the
   three channels may form an orbit under the outer automorphism
   (`Spin(8)⋊S₃`) rather than three copies of one module. That is a genuine
   competing model and remains untested.

## Check

```
cd experiments/20260809-ob11-weight-spectrum-correction
python weight_spectrum_check.py
```
Expect `VERDICT: C29_CONCLUSION_STANDS__EVIDENCE_CORRECTED`; `C₂` control
confirms 4/3 = 4/3; measured `Hom` 6 on all nine pairs; negative control
returns 6 and 8 for the two explicit constructions.
