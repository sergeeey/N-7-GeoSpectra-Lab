# C151 Stages 0 / 1a / 1b — Decision (scoping complete; `c` deliberately NOT computed)

**Date:** 2026-09-04. **Type:** structure-only scoping for the pre-registered
`SU(3)/T²` test. **Status of `c`: NOT COMPUTED in any of these three stages.**

## Why staged at all

The pre-registration's invalidation criterion #4 requires the admissible
family's dimension to be stated *before* the predicted quantity is touched.
Running the whole test in one go would have made any restatement of the
prediction fittable to an answer already seen. So the work was split, with
each stage's output frozen before the next began.

## Stage 0 — the connection family (`c151_stage0_scoping.py`)

Reuses **C73b's own solver** (`equivariant_torsion_basis`) with `T²`
generators substituted for `su(3)` ones — same code, different input, so no
new transcription risk. The `su(3)` case is re-run first as a regression.

```
REGRESSION  dim Hom_su3(m, Λ²m)  [S⁶]        = 2   ← reproduces C73b exactly
RESULT      dim Hom_T2 (m, Λ²m)  [SU(3)/T²]  = 6   ← 3× larger
            commutant of isotropy on m:  su(3) → 2,  T² → 6
```

**Cause, structural and anticipated:** isotropy drops from `SU(3)` (dim 8,
acting on `m` as `3⊕3̄`) to `T²` (dim 2, **abelian**, splitting `m` into three
2-real-dim weight planes, one per positive root). Abelian equivariance is a
far weaker constraint.

**→ Criterion #4 fired.** The restatement was written into
`PREREGISTRATION.md` at this point, with `c` still uncomputed.

## Stage 1a — pinning `J` by computation (`c151_stage1a_pin_J.py`)

`J` could not be asserted: the flag manifold admits **8** invariant
almost-complex structures (one sign per root plane), and criterion #1 forbids
choosing `J` after seeing `c`. So `J` was pinned objectively, via the
Nijenhuis tensor `N(X,Y) = [JX,JY] − J[JX,Y] − J[X,JY] − [X,Y]`:

```
6 of 8 integrable (Kähler)      : max|N| = 0.000e+00
2 of 8 NON-integrable (NK)      : max|N| = 4.000e+00
                                  eps ∈ {(1,-1,1), (-1,1,-1)}  — a conjugate pair
```

Exactly 2 non-integrable structures, forming a conjugate pair — the textbook
answer for `SU(3)/T²`, reached here by computation rather than citation.
`J_NK` fixed to `(-1,1,-1)` by a stated rule (lexicographic among the
non-integrable ones; the other is its conjugate, so this is a labelling
convention, not a physical selection).

**An armchair guess was refuted in passing:** before computing, the
orchestrating session expected the discriminant to be "sign product = −1".
It is not — the two non-integrable tuples have products `−1` and `+1`. The
actual discriminant is the *pattern* (middle sign opposite the outer two).
Computing rather than asserting was the correct call.

### The pre-committed failure mode — WITHDRAWN as tautological (skeptic-caught)

The restatement added a new possible outcome: *if `J` does not map the
admissible family into itself, the prediction is not well-posed on this coset
(`BLOCKED-STRUCTURE`) and that is the finding.* Checked:

```
worst residual of J-image against family span = 4.782e-16
J_NK PRESERVES the admissible family: True
```

So the restated prediction **is** well-posed here.

## Stage 1b — invariant-sector dimensions (`c151_stage1b_sectors.py`)

Exact integer weight arithmetic, no floating point. `Σ = Λ•V` with `V` the
`(1,0)` space selected by the pinned `J_NK`; twist `W = m⊗C`, matching
C139/C147's own choice on `S⁶`.

```
Σ^{T²} inside Σ itself          = 2      (S⁶ also had 2 — both Killing spinors present)
T²-invariants inside W itself   = 0      (m has no zero weight — matches S⁶'s "m has no singlet")

domain  dim (Σ_odd  ⊗ W)^{T²}   = 3      (S⁶, same twist: 1)
target  dim (Σ_even ⊗ W)^{T²}   = 3      (S⁶, same twist: 1)
```

**→ `c` is MATRIX-VALUED (3×3) here, not a scalar** — exactly what
restatement consequence #1 pre-committed. Per that same commitment the
prediction will be tested **as matrices, entry-by-entry**, and explicitly not
weakened to norms or singular values.

Two structural matches with `S⁶` worth noting (they make the comparison
meaningful rather than apples-to-oranges): `Σ` has the same `4+4` split and
the same 2 isotropy-invariants, and the twist has no invariant of its own in
both cases. The `(3,3)` shape also coincides with C141's `m⊕2·1` case on
`S⁶` — where the operator turned out to decompose as a direct sum over
channels, which is a concrete thing to look for in Stage 2.

## Verdict: **scoping COMPLETE, prediction WELL-POSED, `c` untouched**

| pre-registered gate | outcome |
|---|---|
| criterion #4 (family dimension stated first) | **fired** — family is 6, not 2; restatement frozen before `c` |
| criterion #1 (`J` not chosen after seeing `c`) | **satisfied** — `J` pinned by Nijenhuis computation, rule stated in advance |
| ~~new failure mode (`J` must preserve the family)~~ | **WITHDRAWN — TAUTOLOGICAL** (skeptic-caught). `J_NK` is itself `T²`-equivariant, so `T∘J` is in `Hom_{T²}` by construction, for any family dimension. The `4.8e-16` residual is machine noise on a forced zero; it verifies that `J` was *built* equivariantly (plumbing), not a structural property. The pre-registration's claim that this "becomes live because the family is bigger" was wrong — it was equally tautological on `S⁶`. |
| consequence #1 (`c` may be matrix-valued) | **realised** — sectors `(3,3)`, so `c` is 3×3 |
| consequence #2 (sector dims before `c`) | **satisfied** — reported here, `c` uncomputed |

## What remains: Stage 2, and an honest cost statement

Stage 2 is the actual test: build the Levi-Civita/Nomizu connection for
`SU(3)/T²` under CH2016's normalisation, realise `Σ` concretely (not just as
weights), build the twisted Dirac operator, restrict to the `(3,3)` sector,
compute `c`, and compare `c(J·∇)` against `i·c(∇)` as matrices.

That is a construction comparable in scope to round59's original build — not
a re-run of C147's script. It is **not** started here, and the honest reason
is recorded rather than glossed: the scoping is a coherent, registerable
result on its own, and registering it first is what keeps the blindness
record clean — the restatement is now frozen, dated, and public *before* any
`c` exists.

---

# STAGE 2 — EXECUTED. Verdict: **VACUOUS (NO_HEADROOM), not a confirmation**

## Stage 2a — construction, calibration gate PASSED

Metric from CH2016's `B(X,Y) = −(1/12)Tr(ad X ad Y) = −½Tr(XY)`; the
`X_pq, Y_pq` basis is **exactly** `B`-orthonormal (`max|Gram − I| = 0`).
Levi-Civita Nomizu `Λ(X)Y = ½[X,Y]_m`, verified antisymmetric exactly.
round59's Clifford algebra reused unmodified. `J`-alignment: swapping `X↔Y`
on the `ε=−1` planes turns `J_NK` into the standard `J₀`, so no new Clifford
code was written.

**Gate (can fail, and pins the geometry independently of anything the test
wants to find):** 2 `T²`-invariant spinors (Stage 1b predicted 2), with
`D_Σ` eigenvalues **exactly `±3`** — nonzero and equal-and-opposite, the
signature CH2016 §2 proves for any homogeneous NK 6-manifold. **PASSED.**
Sector dims independently re-derived as `(3,3)`, matching Stage 1b's weight
arithmetic.

## Stage 2b — the test, and a FALSE ALARM I must record

The first run printed **"PREDICTION CONFIRMED"**. **It was wrong.** `c`
vanishes identically on all six family vectors, so `c(J∇) = i·c(∇)` reduced
to `0 = i·0` — satisfied trivially, at `4.9e-16`, carrying no information.
The script's own non-vacuity check reported `False`, but **I had not wired it
into the verdict**, so it printed a confirmation over a vacuum. This is
textbook validation theater, caught by reading my own output rather than by
any external review. The gate is now first and dominant; the false verdict
is recorded here rather than quietly overwritten.

## The vanishing is STRUCTURAL, not a bug — diagnosed before any verdict

| check | result |
|---|---|
| Levi-Civita connection lies in the family | **YES**, residual `3.3e-16` |
| the operator is nonzero at all | **YES**, `max|D| = 3.0`, 204/2304 nonzero entries |
| `D` on a random odd-block vector | `max|Dv| = 6.38`, rank 15 of 24 columns |
| `D` on the invariant domain | **`5.6e-17` — annihilated** |
| invariant domain inside `ker(D|odd)` | yes; that kernel is 9-dim of 24 |
| Term1 (`Σ`-side) on the domain | **0** |
| Term2 (twist-side) on the domain | **0** |
| do the two terms cancel each other? | **No — each vanishes separately** |

So on `SU(3)/T²` with `W = m`, the twisted Dirac operator's invariant-sector
block is identically zero for structural reasons. Both terms die
independently — the same *kind* of mechanism C146 proved for `Term1` on `S⁶`,
but here it takes out `Term2` as well, leaving no observable at all.

## Verdict against the frozen pre-registration

The pre-registration listed three outcomes. This is the **third**:

> *"The construction cannot be posed on `SU(3)/T²` at all → `BLOCKED-SUBSTRATE`,
> per this project's own Step-2a discipline. NOT evidence either way; must not
> be recorded as a failed prediction."*

with one upgrade: it is not "we could not run it." The test **ran**, the
geometry **passed** an independent calibration gate, and the observable was
then found to be **structurally absent**. That is `NO_HEADROOM` in this
project's own Floor–Ceiling vocabulary — *"the metric cannot separate
anything; whatever the run returns is noise."*

**The skeptic's Caveat 2 anticipated exactly this risk** — *"if Stage 2 hits
an inconvenient `c` value, an over-generous invocation of BLOCKED-SUBSTRATE
would be the way to launder it."* That caveat is why the diagnosis above was
run before the verdict was written: this is not an inconvenient nonzero value
being reclassified, it is the total absence of the quantity, established by
seven separate checks and by both terms vanishing independently.

## What this DOES establish (a genuine cross-space contrast)

| | `S⁶ = G₂/SU(3)` | `SU(3)/T²` |
|---|---|---|
| admissible family | 2-dim | 6-dim |
| invariant sectors | `(1,1)` → `c` scalar | `(3,3)` → `c` 3×3 |
| `c` on the family | **nonzero everywhere except `∇=0`** (C147, exact) | **identically zero** |
| kernel vs graded floor | `Δ_geo = 0` | kernel = 3 = the whole domain |

C143's Lemma 1 says the kernel exceeds the graded floor exactly when the
defining scalar vanishes. C147 proved that on `S⁶` this **cannot** happen
inside the admissible family. On `SU(3)/T²` it happens **identically, for the
entire family** — the Lemma-1 escape condition realised, but in the
degenerate direction (no signal), not the dynamical one.

**Therefore the pre-registered question does not get an answer here:** whether
`c`'s holomorphy is a nearly-Kähler universality remains **open**, because the
designated second test space turns out not to carry the coefficient at all.

## What this does NOT mean

1. Does **not** test the prediction. Nothing here bears on whether
   `c(J∇) = ±i·c(∇)` holds on `SU(3)/T²`.
2. Does **not** establish that `Σ = Λ•V` is the correct spinor module for
   this coset beyond CH2016's own isotropy-independent construction (as
   quoted by round65) — Stage 2 must verify it concretely, not inherit it.
3. Does **not** confirm the Killing-spinor normalisation. Stage 1b uses only
   weights, which are normalisation-independent; CH2016's `λ = 1/2` and
   `B(X,Y) = −(1/12)Tr(ad X ad Y)` become load-bearing only in Stage 2.
4. Does **not** change anything about `S⁶`, `N_gen=3`, or any registered value.

---

# ⚠️ RETRACTION — 2026-09-04, same day, by C152

**Everything under "STAGE 2 — EXECUTED. Verdict: VACUOUS" above is WITHDRAWN.**
It is kept in place, unedited, per this project discipline on self-caught and
skeptic-caught errors. Do not cite it.

## What was wrong

`c151_stage2_construct.py:205` builds the T2 generator on Sigma (x) W as

```python
gens48 = [np.kron(RHO_SIGMA[k], I6) + np.kron(I8, T2_M[k]) for k in range(2)]
```

with `+T2_M` in the W slot. But `spin_lift(L)` generates the vector action
`-L` (the scripts own sign gate measures exactly this: `SPIN_VS_VEC = -1`), so
the consistent pairing is `(spin_lift(L), -L)`. The S6 side always used it
(`C139.rho_vector = -bivec`); this file did not.

**The decisive, internal check** (C152 Step 6, no external constant needed):
the twisted Dirac operator must commute with the true generator.

```
[D,G] with +T2_M : 2.000e+00     <- D is NOT equivariant. This file's choice.
[D,G] with -T2_M : 0.000e+00     <- exact
same adjudicator on S6: +ADNU 3.333e-01 vs -ADNU 1.509e-17 (= C139/C145's choice)
```

## What that changes

```
this file's sector (+1): max|Term1| = 0.000e+00   max|Term2| = 0.000e+00
corrected sector   (-1): max|Term1| = 0.000e+00   max|Term2| = 1.000e+00
```

So `c` is NOT identically zero on SU(3)/T2. The whole "NO_HEADROOM / vacuous /
question stays OPEN" conclusion above rests on a sector built from a
non-equivariant action, and falls with it.

**Why no gate here caught it:** the sector comes out (3,3) for BOTH signs, so
every dimension check passed; and Stage 2a Killing-spinor calibration gate,
though genuine, never touches the W action at all — it is structurally blind
to this defect. The only sign-sensitive gate in the line was the C145
`1.154701` number, which exists only on the S6 side.

## What still stands from this file

Stages 0, 1a and 1b are **unaffected** — family dimension 6, `J_NK` pinned by
the Nijenhuis computation, sectors (3,3), the withdrawal of the tautological
"J preserves the family" failure mode. All are sign-independent. Stage 2a
construction and its calibration gate also stand; only its blindness is newly
documented.

## The question this file left OPEN is now ANSWERED

On the corrected sector, with the vacuity gate first and dominant and with
falsifiability controls run before reporting:

```
c(J.nabla) = +i . c(nabla)   EXACTLY, entrywise, on all 8 draws
holds for exactly 2 of 8 invariant a.c.s.: J_NK and its conjugate (dev 1.8e-31)
fails for the other six (dev 1.6-2.0), for 5 random J' (0/5), for 3 random
real-linear maps of the same shape (0/3); the old sector is vacuous (~1e-16)
```

**The pre-registered prediction is CONFIRMED.** See
`experiments/20260904-c152-term2-vanishing-mechanism/decision.md`.
