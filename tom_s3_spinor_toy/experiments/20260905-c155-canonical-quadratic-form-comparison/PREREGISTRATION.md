# C155 — PRE-REGISTRATION (written BEFORE any number is computed)

**Date:** 2026-09-05. **Tier:** FL Full. **L0 (EstimandOps): DESCRIPTIVE.**

## Why this round exists (what C154 left, and what it forbade)

C154 REJECTED the framing "the S^6 family-wide ratio `|c|/mu = 2/3` is
independent evidence" — both quadratic forms there are forced conformal by
`<psi_+,psi_-> = 0` and C147b's `c_B = i*c_A`. This session sharpened WHY:

> The S^6 admissible family is **1-complex-dimensional** (via the nearly-Kahler
> `J`; C147b established `c(NOMIZU o J) = i * c(NOMIZU)` exactly). Any two
> nonzero **C-linear** functionals on a 1-dimensional complex space are
> automatically proportional. Nothing geometric is being tested on `S^6`.

**Consequence, pre-registered as a vacuity finding, not a result:** any test of
the form "define invariant `Q_c`, `Q_mu`, check that `S^6` reproduces `2/3`"
**cannot fail** and therefore carries zero information. It is not run here as
evidence; it IS run below only as a positive control (it must pass; if it
somehow failed, the machinery is broken).

## The genuinely open question

`SU(3)/T^2`'s admissible family is **6-real-dimensional** (C153), splitting into
3 root planes. There, proportionality of two quadratic forms is **20 independent
conditions**, not an identity — so it is falsifiable.

C154 Step B's own numbers already hint at the answer and are quoted here so the
prediction below cannot be retrofitted: the ratio `|c|/mu` came out **constant
`2*sqrt(2)` on each of the 6 family basis directions** but **`2*sqrt(6)` on
their sum** and **`2*sqrt(6)/3` on the actual Levi-Civita vector**. A genuinely
proportional pair of forms gives the SAME ratio on every vector including sums.
Differing on sums ⟹ the forms differ in their **cross terms**.

## The canonical objects (chosen to remove researcher degrees of freedom)

The C154 mistake to avoid: picking a matrix norm post hoc until `2/3` appears.
Fix instead the two **canonical Hermitian forms** on the family `V` (real dim 6):

    C : V -> Hom(dom, tgt)      C(v) = c(v)          [linear, exact]
    M : V -> Sigma              M(v) = D_Sigma(v) psi_+   [linear, exact]

    G_c[a][b] := tr( C(v_a)^dagger C(v_b) )     (Hilbert-Schmidt; canonical
                                                 given inner products on dom,tgt)
    G_mu[a][b] := < M(v_a), M(v_b) >            (canonical spinor inner product)

Both are 6x6 Gram matrices of **linear** maps — no norm is chosen, HS is the form
induced by the trace pairing. On `S^6` (`dom`,`tgt` 1-dimensional) `G_c` reduces
to `|c|^2` exactly, so this generalises the S^6 quantity rather than replacing it.

**Normalisation gap closed first (mandatory):** C153's `sector_basis_exact()`
returns raw `nullspace()` output with NO Gram-Schmidt, unlike `S^6`'s `c147b`.
Both Grams were found to be exactly `2*I_3` (fortunate accident). `dom`,`tgt`
are therefore orthonormalised here BEFORE `G_c` is computed; the raw-vs-corrected
factor is verified explicitly rather than assumed.

## Pre-registered predictions (stated before running)

| # | prediction | this is falsified by |
|---|---|---|
| **P1** | `G_c` and `G_mu` are NOT proportional on `SU(3)/T^2`: `G_c != k*G_mu` for every scalar `k` | exact proportionality holding |
| **P2** | the failure is concentrated in **cross-plane** entries: after orthonormalisation the DIAGONAL blocks (within one root plane) ARE proportional with one common `k`, the off-diagonal (plane-to-plane) blocks are not | diagonal blocks having different `k`, or off-diagonal blocks vanishing in both forms |
| **P3** | `S^6`'s `G_c = (4/9) G_mu` holds exactly — **positive control, vacuous by the C-linearity argument above, must pass** | failure ⟹ machinery broken, STOP |

**Honest statement of expectation:** I expect P1 to hold (i.e. NO universal
identity), based on C154 Step B's sums already disagreeing. P2 is the genuinely
uncertain one and is where any new structure would live.

## Kill criteria / what each outcome means

| outcome | verdict |
|---|---|
| P3 fails | `BLOCKED-INFRASTRUCTURE` — not evidence about the claim |
| P1 falsified (forms ARE proportional) with `k = 4/9` | candidate **cross-space identity** — proceed to adversarial stress-test, do NOT promote on this alone |
| P1 falsified with `k != 4/9` | proportionality is real but the CONSTANT is space-dependent ⟹ `2/3` is a normalisation of `S^6`, not universal |
| P1 holds AND P2 holds | structural finding about WHERE the forms differ (cross-plane), `2/3` downgraded to `S^6`-specific |
| P1 holds AND P2 fails | no clean structure; `2/3` downgraded to numerical coincidence, close the line |

## What this round does NOT claim, regardless of outcome

1. Nothing about `N_gen = 3` or any physical claim.
2. Nothing about `lambda` (FREE_COUPLING_PARAMETER, unchanged).
3. A proportionality found here would be a statement about THESE two specific
   homogeneous spaces with THESE conventions — not a theorem about all
   nearly-Kahler 6-manifolds, which would need a proof, not two data points.
