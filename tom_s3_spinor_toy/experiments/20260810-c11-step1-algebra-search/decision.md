# decision — C11 step 1: the algebra search

**Verdict:** `C45_FALSIFIED_AS_WORDED__ALGEBRA_DOES_NOT_EARN_DOUBLING`, with a
strictly weaker structural result promoted separately as **C46**.

**Date:** 2026-08-10 · **L0:** descriptive · ruff clean · `results_step1.json` persisted.

---

## The prediction that came true was the killing one

`claim.md` recorded **P5** before running: *"≥2 inequivalent typed candidates survive
⇒ RF4 fires ⇒ C45 falsified as stated."* It did. Three of seven typed candidates are
admissible — `T4` (crossed product), `T6` (`A+ ⊗ I`), `T7` (twisted diagonal) — and they
are **nested inside one another**, `T6 ⊂ T7 ⊂ T4`.

**Self-check on my own criterion, recorded rather than hidden:** RF4's firing is *near-
tautological*. Admissibility here means closed + unital + `γ`-even, and all three are
inherited by every unital subalgebra, so a maximal admissible algebra always drags a
chain of admissible subalgebras with it. RF4 as worded was a **weak criterion**. The
informative question it should have asked is the one asked below.

---

## P1 — the axiom that was supposed to constrain the sectors cannot see them

[VERIFIED-sympy] `D^t − D^{t'} = 3(t − t')` — independent of **both** `n` and `σ`. So

```
D^0 − D^1 = −3 · Identity          a BOUNDED operator
D_block   = D^{1/2} ⊗ I + (3/2) I ⊗ s3
```

and for any `a = Σ f_i ⊗ s_i`,

```
[D_block, a] = Σ [D^{1/2}, f_i] ⊗ s_i  +  (3/2) Σ f_i ⊗ [s3, s_i]
                     ^ bounded (Clifford·df)      ^ bounded for EVERY s_i
```

**The bounded-commutator axiom imposes zero constraint on the sector index.** This is
C42's own observation — the torsion shift is level-independent — turned around: the very
fact that made the one-operator reading impossible also makes the two-operator reading
invisible to the first axiom one would reach for. Only the grading constrains sectors.

## P2 / RF5 — `γ` is massively non-unique

At `N_MAX = 8`: block spectrum symmetric, `dim ker = 4`, 11 distinct positive eigenvalues,
and the grading moduli `Σ_{λ>0} d_λ²` = **54900** real dimensions (each `(λ, −λ)` pair
contributes a free `U(d_λ)`). **RF5 fires.** "The algebra selected by the grading" is not
even well-defined until one demands that `γ` be the *geometric* one.

## P3 — but `ι` is genuinely load-bearing (controls confirm it)

| `γ` | flips `D^{1/2}` | flips `s3` | anticommutes with `D_block` |
|---|---|---|---|
| `U_ι ⊗ s1` | yes | yes | **PASS** |
| `U_ι ⊗ s2` | yes | yes | **PASS** (positive control) |
| `I ⊗ s1` (control B — `ι` dropped) | no | yes | FAIL |
| `U_ι ⊗ I` (control C — swap dropped) | yes | no | FAIL |
| `U_ι ⊗ s3` (control D — wrong Pauli) | yes | no | FAIL |

**Both factors are needed**, and the three degenerate controls fail exactly where they
should. This is the first place C39's orientation-reversal does load-bearing work inside
an NCG axiom rather than as a geometric aside.

## P4 / C46 — what all admissible algebras agree on

`γ_geo = U_ι ⊗ s1`-even symbols: `{even⊗I, even⊗s1, odd⊗s2, odd⊗s3}`.
`γ_geo`-odd: `{even⊗s2, even⊗s3, odd⊗I, odd⊗s1}`.

**`odd ⊗ I` is forbidden** — an `ι`-odd function may *not* act as the same function on
both sectors. Checked across all three admissible candidates: the sector-diagonal part of
every one lies inside `span{even⊗I, odd⊗s3}` = `{diag(f, f∘ι)}`.

> **C46.** If the doubling is taken, it is a **parity doubling**: the second sector
> carries `f∘ι`, not a free second copy (`T2`, rejected) and not a duplicate (`T1`,
> rejected). Both of those *are* closed unital algebras — they fail on `γ`-evenness alone.

Sanity: `A+` and `A−` are both non-trivial (`x0` is `ι`-even, `x1` is `ι`-odd on 500
sampled points), so the crossed-product structure is not vacuous.

## The informative uniqueness question, and its answer

Not "is the admissible algebra unique?" (no, trivially) but **"is the *maximal* `γ`-even
algebra unique?"** For the geometric family `γ_θ = U_ι ⊗ (cos θ · s1 + sin θ · s2)`:
every `θ` gives a valid grading, and every `γ_θ` is conjugate to `γ_0` by the
**sector-preserving** unitary `V_φ = diag(1, e^{iφ})`. So **given maximality, the algebra
IS unique up to a unitary that respects the `t=0/t=1` split.**

**Maximality is therefore the single missing axiom — and NCG does not supply it.** In a
spectral triple the algebra is *input data*, not derived. That is why C45 fails: not
because no good algebra exists, but because nothing in the axioms forces the good one
over its subalgebras.

---

## Kill Analysis

**What was killed:** C45 as worded — *"a natural algebra exists AND its existence makes
the doubling structurally necessary."* The second conjunct fails.

**What was NOT killed:**
- the crossed product `C^∞(S³) ⋊_ι Z₂` as the maximal admissible algebra — it survives
  and is unique up to sector-preserving unitary;
- **C46** — the parity-doubling structure, which holds across *all* admissible candidates
  and does not depend on maximality;
- C42, C43 (as amended), C44, C38, C39 — untouched.

**Relaxation Map** (one assumption changed per variant, per the Minimal Relaxation Rule):

| Variant | Assumption relaxed | Cost | Status |
|---|---|---|---|
| V1 | add **maximality** as an explicit, declared axiom | free, but it is an assumption and must be labelled as one everywhere | available now |
| V2 | drop "natural" and ask instead which algebra `J` + first-order select (step 5) | one experiment | **next in the portfolio** |
| V3 | require the triple to be a *real* spectral triple and see whether `J` kills `T6`/`T7` | one experiment | folded into V2 |

V2/V3 are the live route: the first-order condition involves `J` and could in principle
exclude the small subalgebras, which would earn the maximal one **without** an axiom of
convenience. That is the correct next question and it is already step 5 of the portfolio.

---

## PARENT_ACTION_GATE after this round

```
H        SUPPLIED   L2(S3,S) (+) L2(S3,S)
D        SUPPLIED   D^0 (+) D^1, round67's closed form
gamma    SUPPLIED   exists -- but GENERICALLY in t (C44), and non-uniquely (RF5)
A        PARTIAL    maximal admissible = C^inf(S3) |x|_iota Z2, unique up to a
                    sector-preserving unitary GIVEN maximality; maximality is an
                    added assumption, not an axiom
J        NOT        step 5
physics  NOT        why two copies at all
```

**3.5 of 6.** The half is honest: an algebra exists and is essentially unique *given* one
extra assumption, and it constrains the doubling's *form* (parity) without forcing its
*existence*.

## What this does NOT show

- It does **not** show no algebra earns the doubling — only that no axiom *available at
  this stage* does. `J` + first-order (step 5) is untested.
- It does **not** re-derive **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), inherited
  from C39 + the standard orientation-reversal result. If A1 fails, P3–P4 and C46 are void.
- It leaves **OPEN** whether the Pin-lift gives `U_ι² = +1`, required for `γ† = γ`.
- It says nothing about `N_gen = 3` (step 7, explicitly deferred).
- Non-tensor gradings (the bulk of the 54900-dimensional moduli) are **not** analysable in
  the 8-symbol space at all; the claim that they fail to normalise the function algebra is
  plausible but **UNTESTED** here.
