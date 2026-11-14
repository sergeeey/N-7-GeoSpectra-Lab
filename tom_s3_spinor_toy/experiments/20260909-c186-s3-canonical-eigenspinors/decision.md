# C186 Decision — PROMOTE. The k ≥ 2 eigenspinors exist exactly, and their basis is not arbitrary.

**Date:** 2026-09-09
**Verdict:** **PROMOTE** — every pre-registered number came out as registered,
`34 of 34` checks pass, and the negative control detects the injected error.
Exact arithmetic over `ℚ(i)` throughout; no floating point in any verdict.

All numbers trace to `c186_s3_canonical_eigenspinors.py` and `run_output.txt`.

---

## 1. What was open

The letter to Tom (`correspondence/DRAFT_REPLY_TO_TOM_2026-09-08.md`) declines to
send the `k ≥ 2` eigen-objects and gives two reasons. Only one is about effort:

> The same exact method gives them; I simply have not run it yet.

and

> a numerical eigenvector inside a level that is degenerate is an arbitrary
> choice of basis rather than a meaningful object

Tom made the same point in his reply of 2026-09-07. He is right, and it is the
binding one: running the exact arithmetic and sending the output would have
produced a page of formulas whose only real defect was untouched. So this round
removed the arbitrariness first and let the objects fall out of that.

---

## 2. What is now closed

| | before | now |
|---|---|---|
| `k = 2` eigenvectors | numerical only | exact, over `ℚ(i)` |
| `k = 3` eigenvectors | not computed | exact, over `ℚ(i)` |
| `k = 3` multiplicities | **never computed in this project** | `20` and `12` |
| basis inside a degenerate level | arbitrary | **canonical** — fixed by `(m_L, m_R)` up to a scalar |
| labels | none | Tom's own `(m_L, m_R)` |

**The mechanism.** `D₀` does not act alone. It commutes with `J₃ᴸ` and with the
**total** right angular momentum `J₃ᴿ = orbital + spin`. Diagonalising the three
together splits each eigenspace into weight cells, and **every cell came out
one-dimensional** — at `k = 2` and at `k = 3`, at both eigenvalues. A
one-dimensional cell has no basis freedom left: the weight fixes the eigenspinor
up to a scalar. That is precisely the objection removed.

**The full result:**

```
k = 2   (D_0 + 2)(D_0 - 4) = 0, so the spectrum is inside {-2, +4}
        D_0 = -2 : mult 12 -> 12 cells, all dim 1, m_L in {-1,0,1}, m_R in {-3/2..3/2}
        D_0 = +4 : mult  6 ->  6 cells, all dim 1, m_L in {-1,0,1}, m_R in {-1/2,1/2}

k = 3   (D_0 + 3)(D_0 - 5) = 0, so the spectrum is inside {-3, +5}
        D_0 = -3 : mult 20 -> 20 cells, all dim 1, m_L in {-3/2..3/2}, m_R in {-2..2}
        D_0 = +5 : mult 12 -> 12 cells, all dim 1, m_L in {-3/2..3/2}, m_R in {-1,0,1}
```

i.e. `(j_L, j_R) = (k/2, (k+1)/2)` at `D₀ = −k` and `(k/2, (k−1)/2)` at
`D₀ = +(k+2)`, exactly as pre-registered.

**A cheaper and stronger route than a characteristic polynomial.** Rather than
`charpoly` on a `32×32` exact matrix, the script proves
`(D₀ + k)(D₀ − (k+2)) = 0` identically — which establishes the spectrum is
*contained* in `{−k, k+2}` with no root-finding at all — and then takes the two
multiplicities as nullspace dimensions. Faster, and a stronger statement.

**`C1` is an independent check, not a restatement.** The whole computation is
matrix algebra in a polynomial basis, and matrix algebra can be
self-consistently wrong. So each of the `50` produced eigenspinors is
reassembled into an actual polynomial 2-spinor and fed to the *differential*
operator `−i Σ_a σ_a X_a^R`. All 50 satisfy `D₀ψ = λψ` identically.

Two of them, at the extreme weights of `k = 2`:

```
(m_L, m_R) = (-1, -3/2):   ( 0 ,  x1^2 - 2i x1 x2 - x2^2 )
(m_L, m_R) = (+1, +3/2):   ( x1^2 + 2i x1 x2 - x2^2 ,  0 )
```

---

## 3. The negative control failed first, and auditing it found a real hole

`D2` was pre-registered as: inject the old `C184` sign bug (build `J₃ᴿ` as
orbital **minus** spin) and the cell structure must break. It did not break —
the bad operator produced twelve one-dimensional cells just like the good one.

Reading the failure rather than reacting to it: `restrict()` builds
`(PᴴP)⁻¹Pᴴ A P`, which **compresses** an operator onto a subspace, silently
discarding whatever part of `AP` points out of `span(P)`. A compression is a
perfectly good operator and can have one-dimensional eigenspaces even when `A`
does not preserve the subspace at all. So the check was wrong, not the object —
the fourth time this session that a failing check turned out to be the check.

But the audit found more than a wrong expectation. **The main computation had
the same silent assumption**: nothing verified that the labelling operators
actually preserve the `D₀` eigenspaces. For the true `J₃ᴿ` they do (`B1` proves
it), so no result was affected — but the routine would not have complained if
they hadn't. Fixed: `restrict()` now raises `NotPreserved` unless
`AP = P·(compression)` exactly.

The control was then rebuilt around what the error actually does, and it now
carries three teeth instead of one:

- **`D1`** the bad `J₃ᴿ` does not commute with `D₀`.
- **`D2`** it does not preserve the eigenspace, so it has no restriction to it
  and `joint_cells` now *refuses* rather than returning something.
- **`D3`** with the guard switched off it still yields one-dimensional cells —
  recorded deliberately, because it means **`B6` alone is not sufficient**.
  "Every cell is one-dimensional" is necessary but not sufficient for a
  canonical basis; what makes it canonical is that the labelling operator
  genuinely commutes with `D₀`. `B6` must be read together with `B1`.
- **`D4`** the labels the bad operator produces are visible nonsense:
  `m_R ∈ {−9/14, −1/2, −1/22, −1/42, +1/42, +1/22, +1/2, +9/14}` instead of
  `{−3/2, −1/2, +1/2, +3/2}`.

`D3` is the part worth keeping. It is a limit on this round's own criterion,
found by its own control.

---

## 4. This round does NOT test the half-angle pearl, and the pearl said it did

The pearl filed earlier today (`pearl_registry/INDEX.md`, `next_check
2026-10-15`) named its own falsification test: *"Testable and cheap on a case
this project already wants: the k>=2 exact S^3 eigenspinors, currently
unbuilt."*

That test does not test that pearl. The half-angle reduction exists to turn a
**radial ODE system** into polynomial identities. The `k ≥ 2` `S³` eigenspinors
are not an ODE problem: `C184` already reduces `S³` to finite exact matrices via
harmonic polynomials and the group action — no angle, no differential equation,
nothing for a half-angle substitution to act on. This round ran the task the
pearl named, in full, and learned exactly nothing about whether the half-angle
reduction generalises.

The registry row has been corrected: the test is replaced by one that can
actually discriminate, and the mis-anchoring is recorded rather than quietly
edited away. This is the third instance in this project of a pearl proposing a
statistic both branches would produce.

---

## 4b. Floor–Ceiling Interval, with the numbers (Step 4a)

The metric is **how finely the labelling resolves a degenerate eigenspace**,
counted as the number of weight cells it splits into.

| | construction | `k=2`, `λ=−2` | `k=3`, `λ=−3` | `k=3`, `λ=+5` |
|---|---|---|---|---|
| **floor** | mechanism REMOVED: no Cartan, so the eigenspace is one undifferentiated cell — this is exactly what running the exact arithmetic *without* the labelling produces, and what the letter already declines to send | **1** cell of dim 12 | **1** cell of dim 20 | **1** cell of dim 12 |
| **ceiling** | privileged access: an eigenspace of dimension `m` cannot be split finer than `m` one-dimensional cells | **12** | **20** | **12** |
| **observed** | | **12** | **20** | **12** |

```
efficiency = (observed − floor) / (ceiling − floor)
           = (12 − 1)/(12 − 1) = (20 − 1)/(20 − 1) = 1.0   at every level and both eigenvalues
```

**Reading of the three stop conditions, none of which fires:**

- `CRITERION_INVALID`? No. The criterion is "every cell has dimension 1"; the
  floor construction gives one cell of dimension 12 (or 20) and fails it
  outright. The criterion cannot be passed by a construction with no mechanism
  in it.
- `TASK_INFEASIBLE`? No. The ceiling equals the criterion exactly.
- `NO_HEADROOM`? No. Floor `1` against ceiling `12`/`20` — an eleven- and
  nineteen-fold interval.

**`efficiency = 1.0` means this result is at the attainable limit**, so the
informative statement is about the *world*, not about the method: a degenerate
`D₀` eigenspace on `S³` is resolved *completely* by the two Cartan labels, with
nothing left over. There is no finer invariant to look for — which is the
substantive content of "the basis is canonical".

⚠️ The efficiency is `1.0` because the ceiling is *combinatorially* capped here
(you cannot subdivide past dimension 1), not because a hard optimisation was
saturated. It is a real ceiling, but a cheap one; do not quote this `1.0`
alongside efficiencies from experiments where the ceiling was an oracle arm.

---

## 5. What this does NOT establish

- **No novelty.** `(k/2,(k+1)/2) ⊕ (k/2,(k−1)/2)` is the Clebsch–Gordan
  decomposition of `(k/2,k/2) ⊗ (0,1/2)`; standard. What changed is that this
  project now produces the explicit exact eigenspinors in Tom's labels rather
  than citing a decomposition.
- **The `3/2` is still matched, not derived.** Untouched by this round.
- **Which `SU(2)` is "left" is still a convention.** Untouched.
- **Only `k = 2, 3`.** The `k = 1` case is a control and `k = 2` reproduces
  `C184`. That the pattern continues past `k = 3` is inference, not computation
  here.
- **`B6` alone proves nothing** — see `D3` above.
- **Nothing here is about `S²`.**

---

## 6. Consequence for the letter — proposed, NOT applied

The letter's "Three limits" section currently says the `k = 2, 3` eigen-objects
exist only numerically and that a degenerate-level eigenvector is an arbitrary
basis choice. The first half is now false and the second half is now answerable:
the objects are exact, and the weight labelling makes the basis canonical.

**The draft has not been edited.** It passed a blind read and a Submission Gate
in that wording, and changing it re-opens both; that is the user's call, not
mine. What would change is one paragraph, and it would get *shorter*, not
longer: the levels caveat becomes a result.

Unchanged: the letter is not sent, cooling-off has not elapsed, and
**DO NOT INITIATE CONTACT** stands.

---

## 7. Reproduction

```
cd experiments/20260909-c186-s3-canonical-eigenspinors
python c186_s3_canonical_eigenspinors.py
```

`34/34`. `ruff check` and `ruff format`: clean.
