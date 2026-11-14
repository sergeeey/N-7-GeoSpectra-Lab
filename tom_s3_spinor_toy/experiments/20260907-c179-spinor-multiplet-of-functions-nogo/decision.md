# C179 — Decision

**Date:** 2026-09-07
**Verdict:** `NOGO-CONFIRMED-AND-DIMENSION-TRAP-CONFIRMED`. `[VERIFIED-tool]`,
all checks exact or at machine precision. Matches this round's own
pre-registered expectation (claim.md, written before running).

---

## 0. Summary

**A multiplet of ordinary functions on `Sⁿ` cannot carry a spinor
representation** — for `S²` (`d=2`) and `S³` (`d=4`), the two cases Tom
Lawrence's 2026-09-07 notes §3.3 asks for. The obstruction is exhibited
inside his own formalism, using only his eq (4) and eq (40).

**The argument, in his notation:** take `g` = rotation by `2π` in the
`(1,2)`-plane.

| | acts as | computed |
|---|---|---|
| on points of `Sⁿ`, hence on functions (his eq 4, `Φ'\|_{gA} = Φ\|_A`) | `+Id` | max point displacement `3.3e-16`, max function-value change `1.8e-15` over 200 random points × 3 arbitrary test functions |
| on the spinor multiplet index (his eq 40, `Γ_d(g)`) | `−Id` | `R_spin(2π) = −Id` exactly, both `d=2` and `d=4` |

Both must hold simultaneously for a spinor multiplet of functions, giving
`Φ = −Φ`, i.e. `Φ = 0`. **No nonzero such multiplet exists.**

This is the resolution of the `[*check*]` marker Tom put on his own §2.2
claim that *"higher-dimensional field ket spaces can be constructed as
tensor products of those for the spinors"* — the fundamental spinors are
not available as multiplets of functions to build from.

---

## 1. Why this is a real computation and not a restatement

The obstruction could have been "shown" tautologically by declaring the
kernel element to be `−1` in the Clifford algebra. That would be exactly
the *"a test that cannot fail is not a test"* failure this project's own
C172 was corrected for. Instead:

- **The SAME abstract `so(m)` generator** (rotation in the `(1,2)`-plane)
  is exponentiated **at the SAME parameter value** `θ = 2π` in two
  representations built independently: the vector rep from
  `(T_ij)_{kl} = δ_ik δ_jl − δ_il δ_jk`, and the spinor rep from
  `Σ_ij = ¼[e_i, e_j]` with explicit Clifford generators.
- **Vacuity guards, both checked:** neither generator is zero
  (`spinor_generator_nonzero`, `vector_generator_nonzero` both True) — a
  zero generator would make both exponentials the identity and the test
  meaningless.
- **Periodicity control:** `R_spin(4π) = +Id` (True for both spheres) —
  confirms the spinor rep really is 2-valued and not simply broken.
- **Clifford relations verified exactly:** `{e_i,e_j} = 2δ_ij` residual
  `0.0` (exact zeros, not rounding) for both `Cl(3)` and `Cl(4)`.
- **The function side is measured, not assumed:** the `2π` rotation is
  applied as an actual matrix to 200 random points on the sphere and to
  three arbitrary test functions, confirming numerically that Tom's
  induced action is the identity map.

---

## 2. The `S³` dimension trap — the specific way a good-faith attempt fails

This is the part worth flagging hardest, because dimension counting is
the natural first check and it **gives a false pass**:

| object | dimension | kernel-element phase | descends to `SO(4)`? |
|---|---|---|---|
| vector `(½,½)` | **4** | `+1` | yes |
| spinor `(½,0)⊕(0,½)` | **4** | `−1` | **no** |

`dim = 4` for both. Asking *"is there a 4-dimensional block in `L²(S³)`?"*
answers **yes** — and that block is the vector multiplet (the four
Cartesian coordinates, Tom's own eq 83/89), not the spinor. Only the
action of the kernel element `(−1,−1)` of `Spin(4) → SO(4)`, which acts as
`(−1)^{2j_L + 2j_R}`, discriminates them. `dimension_trap_confirmed = True`.

---

## 3. Positive control A: our reading of Tom's conventions is correct

Before claiming an obstruction inside someone else's formalism, the
formalism must be read correctly. His eq (77) was tested for the case he
has already verified himself (his §3.2, eqs 109–112) — the `S²` vector
multiplet `|φ_i⟩ = x_i/r` — against **three** candidate index conventions:

| convention | satisfies eq (77)? |
|---|---|
| **his own** (`Γ_d = −T`, row-contraction, his eq 99) | **True** |
| transpose variant | False |
| sign variant (`Γ_d = +T`) | False |

**Exactly one works, and it is his.** `exactly_one_convention_works = True`.
This also answers his own bracketed worry on p.13 (*"we seem to have the
same expression for two matrices, which are the negatives of each other
... I don't like this – can it be dealt with in any way?"*): the two are
not interchangeable, and eq (77) itself fixes which is which. He asked
that bracketed notes be ignored, so this is offered, not pressed.

**Provenance note:** this is the same transpose/row-vs-column artifact
this project isolated on 2026-07-28 in
`experiments/20260728-tom-so3-harmonics-sign-check/TRANSPOSE_LEMMA.md`
(*"if comparison (2) reports agreement, the honestly-built matrix `M`
satisfies `M = T^T` ... NOT `M = T`"*), sent to Tom in the 3 August notes,
and named by him in his 2026-09-07 email as the correction he then made
(*"it's the dual representation ... the inverse (or equivalently, the
transpose)"*). The provenance chain closes.

---

## 4. Positive control B: where the half-integers actually live

The no-go could be misread as *"half-integer `j` is unavailable on `S³`"*.
It is not. `S³ = SU(2)`, and the `j=½` Peter–Weyl block `D^{½}(g) = g`
consists of honest functions on `S³`:

- reconstructing the four Cartesian coordinates from the entries of `g`:
  max error **`0.0`** (exact)
- under `g ↦ u g v†` (i.e. `SU(2)_L × SU(2)_R = Spin(4)`), the four
  coordinate functions transform by a `4×4` map that is a genuine
  rotation: linear-fit residual `1.3e-15`, orthogonality residual
  `1.9e-15`

So half-integer `j` **is** present in `L²(S³)` — but it assembles into
`(½,½)`, the **vector**, not into `(½,0)⊕(0,½)`, the spinor. Functions on
a group are acted on by both left and right translations, so they always
land in balanced `(j,j)` blocks; the spinor is unbalanced and therefore
unreachable.

---

## 5. Kill Analysis

**What this round kills:** the specific construction Tom's §3.3 asks for —
spinor harmonics as multiplets of global functions on `Sⁿ` in his §1.1
sense. Not "not yet found": provably nonexistent.

**What this round does NOT kill:**
1. **Spinor harmonics themselves.** They exist as sections of the spinor
   bundle. On `S³` that bundle is trivial (`S³` is parallelizable — the
   same fact this project uses for the `t=0`/`t=1` flat connections,
   round67), so spinor fields ARE 4-tuples of functions **in the group
   trivialization** — just not in the ambient-`ℝ⁴`-Cartesian sense his
   §2.1 uses for vectors. This is the constructive route and it is open.
2. **His §1–§2 general theory for tensor multiplets** — untouched, and
   positive control A actively confirms his conventions are self-consistent.
3. `N_gen=3`'s CONDITIONAL status, OB1, OB11, OB14 — unaffected; this
   round is collaboration-facing, not a claim about the compactification.

**Relaxation Map — what changes for the remaining plan items:** the order
Tom proposed (`S²` first, then `S³`) should be **inverted**. `S²` is not
parallelizable, its spinor bundle is non-trivial, and its spinor harmonics
(spin-weighted `_{±½}Y_{jm}`) are standardly obtained by descending from
`SU(2) = S³` at fixed `U(1)` weight. So `S³` is the tractable end and `S²`
follows from it, not the reverse. `[INFERRED]` from the structure
established here plus standard theory — flagged for the next round, not
computed in this one.

---

## 6. What this does NOT mean

1. Does NOT say Tom made an error he was unaware of — his footnote 1
   (p.3), footnote 2 (p.11) and his own `[*check*]` on §2.2 all flag this
   exact region. This round resolves a question he raised.
2. Does NOT provide the spinor harmonics — that is the next round.
3. Does NOT establish anything about `S⁶` or the project's own
   compactification content.
4. Does NOT constitute a submission. Anything sent to Tom must pass
   `integrity.md`'s Submission Gate separately (external-facing artifact).

---

## 7. Floor–Ceiling / verification substrate note

Exact algebra, not estimation. The discriminating scalar is
`s = max|R_spin(2π) − Id|` — how far the spinor rotation at `2π` sits from
the identity (the function side is pinned at the identity by check 2, so
`s` measures the entire obstruction).

- **FLOOR (mechanism removed) = `0`.** With the spinor generator set to
  zero — a construction with no spin content at all — `exp(2π·0) = +Id`
  and `s = 0` exactly. That is what a vacuous version of this test would
  return. Guarded explicitly: `spinor_generator_nonzero = True`,
  `vector_generator_nonzero = True`.
- **OBSERVED `s = 2`** (`R_spin(2π) = −Id`, so every diagonal entry
  differs from `1` by exactly `2`), for both `d=2` and `d=4`.
- **CEILING = `2`.** For any unitary representation, `|U_ij − δ_ij| ≤ 2`,
  attained only at `U = −Id`. So `2` is the largest value `s` can take.
- **efficiency = `(2 − 0)/(2 − 0)` = `1.000`** — the obstruction is at the
  maximum attainable strength, not marginal. Note this `efficiency ≈ 1`
  means "exact algebraic result at the attainable limit," NOT the
  statistical reading ("we are at the limit of what the world allows") —
  the distinction is stated explicitly so it is not misread.

Supporting residuals: Clifford relations `0.0` (exact zeros), function-side
`≤1.8e-15` (float64 limit).

READY, no blocked-infrastructure issue.

---

## 8. Independent skeptic pass (Step 8a) — RUN, verdict `CONFIRMED-REAL`

Run context-blind (given `claim.md`, the script and `results_c179.json`;
denied this `decision.md`), briefed that the stakes are raised because the
conclusion is destined for an external collaborator. Six attacks, none
broke the claim.

| # | Attack | Outcome |
|---|---|---|
| 1 | **The one that mattered:** could Tom simply declare `Γ_d` to be a `Spin(n+1)` rep and proceed? | **Does not rescue it.** His eq (4) defines the induced action via the literal point-map on the sphere — an honest pullback with no phase freedom. `Spin(n+1)` acts on points only *through* the covering map, so `g` and `−g` induce the *identical* `Φ'`. Requiring eq (4) and eq (40) to describe the same object is what forces the contradiction; it is not an avoidable convention. |
| 2 | Is "multiplet of functions" read too narrowly? | Correctly scoped — the round tests his eq (1)'s literal global single-valued functions and explicitly disclaims bundle sections. The skeptic noted this *explains* his own footnote 2 rather than contradicting his notes. |
| 3 | Are the computations doing what they claim? | **Verified independently by hand.** `Σ_01` recomputed directly: `(i/2)σ₃` for `m=3`, `diag(i/2,i/2,−i/2,−i/2)` for `m=4` — both already diagonal, so the eigendecomposition-based `matrix_exp` is exact, not an artifact. Confirmed by direct commutator computation that `Σ_ij` and `T_ij` obey **identical** `so(m)` structure constants, so it genuinely is the same abstract Lie-algebra element in two reps. Vacuity guards judged real, not decorative. |
| 4 | The kernel-phase rule `(−1)^{2j_L+2j_R}` | Verified analytically — the standard `SU(2)×SU(2)→SO(4)` kernel computation. |
| 5 | Positive control A (three conventions, exactly one works) | Internally bug-free (hand-recomputed `T_def(0,1)` and one LHS/RHS pair), **but the skeptic could not check fidelity to the source PDF, which it did not have** — flagged honestly as `[UNVERIFIED]` rather than waved through. |
| 6 | Positive control B | **Confirmed, and strengthened.** The skeptic supplied a *second, independent* proof for the `S³` case: Peter–Weyl says `L²(G)` decomposes for any compact `G` into diagonal `(j,j)` blocks only, so `(j,0)`/`(0,j)` cannot occur — an argument that does not use the double cover at all. |

**Gap #5 closed here (the skeptic could not, this session can):** the
transcription was made by direct read of the PDF, and the four equations
are on record — eq (61) `(T_ij)^k_l = −i(δ_jl δ^k_i − δ_il δ^k_j)` (p. 8),
eq (77) (p. 9), eq (89) `|φ_i⟩ = δ_ij √((n+1)/S) x^j/r` (p. 12), eq (99)
`Γ_d(T_ij) = −T_ij` (p. 13). Re-checked against the source after the
skeptic flagged it. **Still worth an independent human re-read before
sending**, since transcription fidelity is exactly the class of error a
self-check is weakest against.

**Net effect:** verdict unchanged and strengthened — the `S³` half of the
no-go now has two independent proofs (double cover; Peter–Weyl bimodule
structure), and attack #1, the most likely failure mode, was specifically
probed and did not break it.

---

## 9. Status

`experiments/20260907-c179-spinor-multiplet-of-functions-nogo/` — DONE,
INCLUDING independent skeptic pass. Verdict
`NOGO-CONFIRMED-AND-DIMENSION-TRAP-CONFIRMED`, both positive controls
passed, skeptic verdict `CONFIRMED-REAL` with the `S³` case now carrying
**two independent proofs** (§8). One residual risk named and not closed by
self-check alone: transcription fidelity of Tom's four equations, which
should get a human re-read before sending. Item 1 of the 5-item plan is
complete; C180 (items 2–3) follows and is also complete. Registry
(`OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`) not yet updated. No git
operations run.
