---
# C186 — the k ≥ 2 S³ eigenspinors, exactly, and with a basis that is not arbitrary

**Date:** 2026-09-09
**FL tier:** [x] Full
**Question type:** [x] descriptive

---

## Why this round exists

The letter drafted for Tom Lawrence says, in its own words
(`correspondence/DRAFT_REPLY_TO_TOM_2026-09-08.md`, "Three limits I want to be
explicit about"):

> I have carried the exact arithmetic through at `k = 0` and `k = 1` only. The
> dimensionalities quoted for `k = 2` and `k = 3` are computed, but the
> eigen-objects at those levels I have so far only in numerical form — and a
> numerical eigenvector inside a level that is degenerate is an arbitrary choice
> of basis rather than a meaningful object, so I am not sending those and calling
> them formulas. The same exact method gives them; I simply have not run it yet.

Two separate things are admitted there, and only one of them is about effort:

1. **Not run.** The exact arithmetic at `k = 2, 3` was never executed.
2. **Would not help if it were.** Even run exactly, an eigenvector inside a
   degenerate eigenspace is a choice, not an object. Tom made the same point in
   his reply of 2026-09-07 and he is right. Running item 1 alone produces a page
   of formulas whose only defect — arbitrariness — is untouched.

So this round does not just "run it". It removes the arbitrariness first, and
the exact `k = 2, 3` objects fall out as a consequence.

**The move:** `D₀` does not act alone. It commutes with a two-dimensional
Cartan, and simultaneously diagonalising the three operators labels every
eigenspinor by a weight `(m_L, m_R)`. If — and only if — the joint eigenspaces
are one-dimensional, that labelling *fixes* each eigenspinor up to a scalar, and
the arbitrariness is gone. Those labels are also the very thing Tom's four `S³`
labels are read as (`§7` of the second message: "as `(m_L, m_R)` with a zero in
one slot"), so this is his coordinate system, not a new one.

---

## Prior Result Gate

1. `C180` / `C184`: `D₀ = −i Σ_a σ_a X_a^R` built on `S³`, spectrum obtained at
   `k = 0, 1, 2` as exact finite matrices over `ℚ(i)` in a harmonic-polynomial
   basis. `k=0 → 0` (mult 2); `k=1 → −1` (6), `+3` (2); `k=2 → −2` (12), `+4` (6).
   **Eigenvalues only — no eigenvectors were extracted at any level above 1.**
2. `C184` Part C: `L²(S³)` carries only `(j, j)` — verified `k = 0..3`.
3. `C185`: the half-angle reduction, on `S²`. **Not used here** — see the
   scope note below, this matters and was nearly got wrong.
4. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for a weight-labelled
   `S³` eigenspinor basis. Never attempted, never killed.
5. **Status:** [x] NEW.

### Scope note — the method this round does NOT use, and why it is worth saying

The pearl filed 2026-09-09 (`next_check 2026-10-15`) proposed its own
falsification test in these words: *"Testable and cheap on a case this project
already wants: the k>=2 exact S^3 eigenspinors, currently unbuilt."*

**That test does not test that pearl.** The pearl is about the half-angle
reduction `s = sin(θ/2)`, `c = cos(θ/2)`, whose purpose is to turn a *radial
ODE system* into polynomial identities. The `k ≥ 2` `S³` eigenspinors are not an
ODE problem at all: `C184` already reduces `S³` to finite exact matrices via
harmonic polynomials and the group action, with no angle and no differential
equation anywhere. Running this round therefore says nothing whatever about
whether the half-angle reduction generalises — it exercises a different method.

This is recorded here rather than only in the registry because it is the third
instance of one failure mode in this project: a pearl closed by a statistic that
both branches would have produced. The registry row is corrected separately;
this round is not its test.

---

## Substrate note (Step 2a)

Conventions are substrate, not hypothesis: the quaternion multiplication table,
which Pauli matrix is `σ₃`, and the sign of each orbital generator. All are
fixed by construction and printed. In particular the **relative** sign between
the orbital and the spin part of `J^R` is not chosen by taste — see the
mechanism check below, where it is determined and where getting it wrong is
shown to be detectable.

Exact arithmetic over `ℚ(i)` throughout. No floating point enters any verdict.

---

## Step 0a — Mechanism Claim Gate  [RUN BEFORE THIS FILE WAS FINALISED]

The design rests on one sentence about behaviour:

> `J₃ᴸ` and the **total** right angular momentum `J₃ᴿ = orbital + spin` both
> commute with `D₀`, so simultaneously diagonalising the three gives a basis
> labelled by `(m_L, m_R)` instead of an arbitrary basis of a degenerate
> eigenspace.

Checked at `k = 1`, the smallest case that could break it, before any of the
above was written. `scratchpad/probe_c186.py`. Result:

```
su(2) closure, [J_a,J_b] = i eps J_c, for J = s*(i/2)X :
   R with J = +(i/2)X : closes = True        L with J = +(i/2)X : closes = False
   R with J = -(i/2)X : closes = False       L with J = -(i/2)X : closes = True

[D_0, J_3^L]                        = 0 ?  True
[D_0, J_3^R orbital only]           = 0 ?  False
[D_0, S_3 spin only]                = 0 ?  False
[D_0, J_3^R TOTAL = orbital + spin] = 0 ?  True
[D_0, J_3^R TOTAL = orbital - spin] = 0 ?  False
```

**Verdict: HOLDS**, and the check discriminates rather than merely passing:
neither the orbital part nor the spin part commutes with `D₀` on its own, only
their sum, and only with the two signs that actually close as `su(2)` — which
are *opposite* for left and right. A wrong relative sign fails visibly here.
This is deliberately aimed at `C184`'s recorded sign bug, where orbital
`−(i/2)X` was added to spin `+σ/2` and the sum was not a sum; a Casimir is
quadratic and could not see it, but a commutator can.

Joint eigenspaces at `k = 1`, same probe:

```
D_0 = -1 (mult 6) -> 6 weight cells, all dimension 1
   (m_L, m_R) = (±1/2, −1), (±1/2, 0), (±1/2, +1)
D_0 = +3 (mult 2) -> 2 weight cells, all dimension 1
   (m_L, m_R) = (±1/2, 0)
```

---

## Falsifiable claim

For `k = 2` and `k = 3` on `S³`:

**(a)** every joint eigenspace of `(D₀, J₃ᴸ, J₃ᴿ)` is **one-dimensional**, so
each eigenspinor is determined by its weight up to a scalar and the basis is
canonical rather than arbitrary; and

**(b)** the eigenspaces of `D₀` carry exactly the representation content

| `D₀` eigenvalue | `(j_L, j_R)` | multiplicity |
|---|---|---|
| `−k` | `(k/2, (k+1)/2)` | `(k+1)(k+2)` |
| `+(k+2)` | `(k/2, (k−1)/2)` | `k(k+1)` |

**Pre-registered numbers, fixed before running:**

| | `k = 2` | `k = 3` |
|---|---|---|
| harmonic basis dim | 9 | 16 |
| total spinor dim | 18 | 32 |
| `D₀ = −k` multiplicity | 12 | **20** |
| `D₀ = +(k+2)` multiplicity | 6 | **12** |
| `m_L` range at both levels | `−1 … +1` | `−3/2 … +3/2` |
| `m_R` range at `D₀ = −k` | `−3/2 … +3/2` | `−2 … +2` |
| `m_R` range at `D₀ = +(k+2)` | `−1/2 … +1/2` | `−1 … +1` |
| number of weight cells | 12 + 6 | 20 + 12 |
| dimension of every cell | 1 | 1 |

The `k = 2` multiplicities `12` and `6` are already known from `C184` and are
therefore a **control**, not a result. The `k = 3` numbers `20` and `12` have
never been computed in this project and are the actual prediction.

---

## Floor (Step 4a)

"Some basis of an eigenspace was produced" is free — `eigenvects()` always
returns one. The floor is therefore not "vectors were obtained" but the two
things that separate a canonical basis from an arbitrary one:

- **Floor construction:** take the raw `eigenvects()` output of `D₀` alone. It
  spans the same space and carries **no** weight labels; nothing distinguishes
  it from any other spanning set. This is what "running it exactly" without the
  Cartan would produce, and it is what the letter already declines to send.
- **The criterion above the floor:** every joint cell has dimension exactly 1.
  If any cell came out with dimension `> 1`, the labelling would fail to fix a
  basis inside that cell and the round would have produced the same arbitrary
  object more expensively.

**Ceiling:** the representation-theoretic answer is attainable in closed form —
`(k/2,(k+1)/2) ⊕ (k/2,(k−1)/2)` is what the Clebsch–Gordan decomposition of
`(k/2,k/2) ⊗ (0,1/2)` gives. So the ceiling is exact agreement, the floor is a
label-free basis, and the interval is not degenerate.

---

## Kill criterion

The claim is **REJECTED** if any of:

1. any joint `(D₀, J₃ᴸ, J₃ᴿ)` eigenspace at `k = 2` or `k = 3` has dimension
   `> 1`;
2. the `k = 3` multiplicities are not `20` and `12`;
3. any produced eigenspinor fails `D₀ ψ = λ ψ` verified exactly;
4. the weight labels are not the half-integers/integers tabulated above;
5. the `k = 2` control does not reproduce `C184`'s `12` and `6`.

## Negative control

The connection between spin and orbital is where the previous bug lived, so the
injected error is there: rebuild `J₃ᴿ` as `orbital − spin` instead of
`orbital + spin` and re-run the joint diagonalisation. Expected: it no longer
commutes with `D₀`, so the joint decomposition is not even well posed and the
cell structure must break. If the cells come out `1`-dimensional anyway, the
check is not measuring what it claims to and the round is `ORACLE_INADEQUATE`,
not a pass.

---

## What this will NOT establish

- **No novelty.** `(k/2,(k+1)/2) ⊕ (k/2,(k−1)/2)` is standard representation
  theory. What changes is that this project can produce the explicit exact
  eigenspinors in Tom's own labels rather than cite a decomposition.
- **Does NOT derive the `3/2`.** That remains matched, not derived, exactly as
  `§7` of the letter says.
- **Does NOT settle which `SU(2)` to call "left"** — still a convention.
- **Does NOT test the half-angle pearl.** See the scope note above.
- **Does not extend beyond `k = 3`.** The pattern will be verified at `k = 2, 3`
  against a `k = 1` control; that it continues is inference.
