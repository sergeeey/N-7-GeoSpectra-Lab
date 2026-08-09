# Majorana vs C27's multiplicity-2 — NO, and this corrects my own C32

**Date:** 2026-08-10
**Verdict:** `MAJORANA_DOES_NOT_RESOLVE_MULTIPLICITY_2__C32_OVERCORRECTED`
**Corrects:** `C32` (`experiments/20260809-ob10-convention-correction/`)

## Three statements, and where each was right

| claim | said | verdict |
|---|---|---|
| **C31** (08-06) | Majorana row CLOSED, *because the relevant factor is pseudo-real* | **conclusion right, reasoning wrong** — it cited the 9-dim product's type, taken from C28, which was itself a convention artifact |
| **C32** (08-09) | C31 INVERTED — the condition exists and halves the module, row is **OPEN** | **over-correction** — true of the 16-dim *module*, false of the *zero mode* |
| **this round** | the condition does not restrict to the zero mode as a real structure | row is **CLOSED**, for a reason neither earlier claim gave |

I corrected an error and, in correcting it, introduced a new one in the
opposite direction. The follow-through caught it. Recorded plainly.

## The computation [VERIFIED-numpy]

C27's zero mode is not the whole module:

```
ker(D_full) = ker(D_S3) (x) ker(D_S6,twisted) = C^2 (x) (1-dim)
```

Under the uniform convention the 16-dim module is REAL — but that reality is
a product of **two quaternionic factors**:

```
B_S3 conj(B_S3) = -I    (S3 factor, quaternionic)
B_S6 conj(B_S6) = -I    (S6 factor, quaternionic)
product          = +I    REAL, because (-1)*(-1) = +1
```

Restricting to `ℂ² ⊗ span(k)` collapses the S⁶ factor to a **scalar** `λ`,
and a scalar cannot supply the second minus sign. The induced antilinear map
on the zero mode is `ψ ↦ λ·B_S3·conj(ψ)`, whose square is
`|λ|²·B_S3 conj(B_S3) = −|λ|²·I` — quaternionic again.

A quaternionic structure has no fixed vector:
`ψ = Jψ ⟹ ψ = J²ψ = −cψ ⟹ (1+c)ψ = 0 ⟹ ψ = 0` for `c > 0`.

Tested over nine values of `λ` spanning phase and scale (`1, −1, ±i, 2.5,
0.3+0.7i, −1.4i, 0.01, 100`): **solution dimension 0 in every case.**

**The conclusion does not depend on the unknown `k`** — deliberately, because
no explicit S⁶ kernel vector exists in this project (see scope). Both
branches agree:

- If `B_S6` **preserves** `span(k)` → induced structure is quaternionic → no solutions.
- If `B_S6` **does not** preserve it → `B` maps the zero mode out of itself →
  the condition cannot be imposed on `ker(D_full)` at all.

Either way: **no halving**.

**Negative control:** the same solver on a genuinely real structure (`B=σ₁`,
`B conj(B)=+I`) returns dimension **2**, not 0 — the machinery is not
vacuously returning zero.

## Consequence

**C27's multiplicity-2 blocker is unchanged: 6 internal modes across 3
channels, not the needed 3.** The Majorana row of its Relaxation Map is
closed. Two rows remain open — an S³-specific projection, and the 32-state
reconciliation that round78 itself named as the thing to tackle first.

**Net effect of the whole OB10 episode on C27: zero.** The reality type was
corrected (a real gain in understanding, and it exposed a genuine codebase
inconsistency), but the blocker it briefly appeared to unlock never actually
moved.

## Scope — what this does NOT establish

1. **The S⁶ kernel is index-theoretic, not explicit.** `dim ker(D_{S⁶}⊗S⁻)=1`
   is established by Dolan-Casimir + round59's trivial-rank certification, not
   by an explicit vector in a concrete module. The argument above is
   deliberately `k`-independent for exactly that reason, but it does assume the
   kernel is **1-dimensional** — which is what those rounds establish.
2. **The genuine zero mode lives in a TWISTED bundle** (`D_{S⁶}⊗S⁻`), while
   OB10's 16-dim module is the **untwisted** product spinor module. The
   analysis here uses the untwisted module as a proxy. The load-bearing step —
   that the S³ factor is quaternionic and a scalar cannot flip a sign — is
   untouched by the twist (which acts on the S⁶ side), but a fully rigorous
   version would work in the twisted bundle directly.
3. **One loophole, named:** the argument assumes the full charge conjugation
   **factorizes** as (S³ part) ⊗ (S⁶/twist part). It does for the `B` found
   here. A non-factorizing antilinear structure on the twisted bundle is not
   excluded and would need separate treatment.
4. Does **NOT** affect C32's other content: the reality type of the module is
   REAL (correct), the Cl(6,3) signature was an artifact (correct), and the
   codebase-level convention inconsistency is real (correct). Only C32's
   claim about the *Relaxation Map row* is corrected.

## Check

```
cd experiments/20260810-majorana-vs-multiplicity2
python majorana_zero_mode.py
```
Expect `VERDICT: MAJORANA_DOES_NOT_RESOLVE_MULTIPLICITY_2__C32_OVERCORRECTED`;
solution dimension 0 for all nine λ; negative control returns 2.
