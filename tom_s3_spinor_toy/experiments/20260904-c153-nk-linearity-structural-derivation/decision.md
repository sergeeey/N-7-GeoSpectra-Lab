# C153 — Decision. Verdict: **PROMOTE, WEAKENED, THEN DOWNGRADED BY NOVELTY CHECK**

**Date:** 2026-09-04. **Tier:** FL Full. **L0:** descriptive.
**Skeptic (Step 8a, context-blind): WEAKENED. Novelty check (post-hoc,
run before authorizing C154): NOT NEW on both fronts.**

## ⚠️ CORRECTION, same day, run per user instruction before authorizing C154

Before greenlighting a C154 built around "explain the per-plane law via the
Weyl-group orbit", the user asked for a literature check first. Result
(`novelty_check.md`, `skeptic-auditor` + WebSearch, full detail there):

1. **The 6-vs-2 Weyl-orbit split is Borel–Hirzebruch (1958) §13.7 and
   Burstall–Salamon (1987, Math. Ann. 277)**, stated explicitly for the `F₃`
   flag manifold in arXiv:2411.07767 §5.2. This round's own `claim.md` item
   1 named this as an unverified "candidate C154" — it did not need
   verifying by a new round; it is 40-to-65-year-old classical geometry.
2. **The per-plane law is entailed by Schur's lemma**, not a fact about this
   operator: `m` splits into pairwise-inequivalent root-plane summands
   (multiplicity one), the `±i`-per-plane action is Borel–Hirzebruch's own
   *definition* of an invariant a.c.s., and any `T²`-equivariant map — `c`
   is one, by construction — is therefore forced to respect the splitting,
   before any of this round's computation ran.

**Consequence:** this round's headline ("a genuinely surprising structural
discovery") is downgraded to "an independent exact verification that a
specific operator conforms to a generic, already-known pattern." The
arithmetic below is unaffected — every number is still exactly correct —
but the evidentiary WEIGHT the original framing claimed was wrong, in the
same way, and for the same reason, C144's "algebraically forced by total
antisymmetry" correction downgraded that round. See `claim.md`'s own
correction for the reader-facing version; this file is left otherwise
intact below, per this project's discipline of correcting in place.

**What remains open, per the user's own framing ("если да, C154 надо
формулировать вокруг недостающего звена"):** not "why does the sign factor
per plane" (answered — it doesn't need explaining) but why the *values*
`c(v_k)` (not just their `T²`-transformation signs) come out the way they
do, and whether `S⁶` and `SU(3)/T²`'s coefficients are connected by
anything beyond both having been computed exactly. No classical result
found here addresses magnitude, only the sign/eigenvalue structure.

---

## What was asked

The user's own ranked low-hanging fruit, items #1+#2 combined: why does
`c(J∇) = i·c(∇)` hold, and why exactly for 2 of the 8 invariant
almost-complex structures on `SU(3)/T²`?

## Step 1 — Nijenhuis correlation, WITHDRAWN as tautological

Reused C152 Step 8 and C151 Stage 1a, relabelled the raw-basis
non-integrable set by `eps_NK`, and reported a match against the aligned
C-linear set. **The skeptic found this test is vacuous**: for *any*
conjugate pair `{b,−b}`, relabelling by `b` itself always produces
`{(1,1,1),(−1,−1,−1)}`, regardless of what `b` actually is — verified
directly on four different pairs, all giving the same relabelled result.
The `assert`s guarding the raw and aligned sets also make the printed
"FALSIFIED" branch dead code (an `AssertionError` fires before it could be
reached). **Response: FIX, not dismiss** — see Step 2g below, which
recomputes Nijenhuis directly in the aligned basis with no relabelling step
at all, closing the gap the skeptic identified. Step 1's script is kept
in place with a correction appended (see its own file); its arithmetic was
correct throughout, only the inference drawn from it was wrong.

## Step 2 — exact rational reconstruction

**First attempt failed, honestly, and was not patched around.** Rationalised
already-computed numeric `dom`/`tgt`/family vectors via `sympy.nsimplify`.
Honesty-check residual `2.1e-4`, far above the `1e-9` noise floor — SVD
orthonormalisation of a rational null space generically introduces
irrational entries into the *chosen basis vectors* even though the *span*
is exactly rational. Fixed the method, not the bound: rebuilt the entire
geometry from scratch in exact `sympy` — basis, Killing form, Nomizu
connection, `T²` Cartan generator, invariant sectors (`Matrix.nullspace()`),
6-dim connection family (same method, replacing C73b's SVD).

```
gram - I exactly zero                          : True
Nomizu operators exactly antisymmetric         : True
exact sector dims                              : (3, 3)   (Stage 1b: 3,3)
exact family dimension                         : 6         (Stage 0: 6)
Levi-Civita connection lies exactly in family   : True
```

**Skeptic correction, applied:** `(3,3)` and "LC ∈ family" are **not**
sensitive to the `T²`-generator sign choice — proven algebraically
(conjugation by `diag(1,−1,1,−1,1,−1)` maps the `+T2_M` construction to the
`−T2_M` one exactly, so both give `(3,3)`), and this is *already* visible
in the repo's own record: C151's original wrong-sign construction (`+T2_M`)
and C152/C153's corrected construction (`−T2_M`) both independently found
`(3,3)`. These are retained as code-correctness regressions; they are
explicitly **removed from the kill-criterion's sign-sensitive claims**
in `claim.md`.

**A real sign bug, self-caught before the skeptic pass.** The first version
of the decisive test checked only `c(J·v) − i·c(v) = 0`, found `(1,1,1)`
zero but wrongly flagged `(−1,−1,−1)` as failing — the pre-registration
says `±i`, only `+i` had been implemented. Fixed to check both signs:

```
eps=( 1, 1, 1)  EXACTLY ZERO (sign +i)
eps=(-1,-1,-1)  EXACTLY ZERO (sign -i)
matches C152 Step 8's floating-point 2-of-8 pattern: True
```

## Step 3 — per-plane law: real, but its evidentiary weight was inflated

Printing the sign per family direction (not just pass/fail) for the 6
"failing" `eps` showed a 3-pair grouping matching `i^{eps_k}` per plane — an
unregistered, stronger pattern. Built a targeted test: fix two plane signs,
vary the third. **First run used the wrong column-to-plane mapping**
(family column `k` against a.c.s. position `k`, when Step 2's own printout
grouped columns `(0,1)(2,3)(4,5)`) — self-caught before reporting, fixed to
column `2k`.

**Skeptic finding on the fixed version, verified directly and CORRECT:**
the "24 direct tests" claim was itself an overclaim. Computed independently
(not taking the skeptic's word for it):

```
family_sym column support:  col0,1 -> rows{0,1}   col2,3 -> rows{2,3}   col4,5 -> rows{4,5}
acs_from_eps(eps) == -acs_from_eps(-eps) EXACTLY : True
```

Both structures are exactly block-diagonal by construction, so a plane-`k`
-local family vector's response under `J_eps` **cannot** depend on the other
two planes' signs — this is forced, not measured — and the `eps_k=−1` case
follows from `eps_k=+1` by linearity, not an independent computation. **24
tests collapse to 3 genuinely independent facts**, one per plane. `claim.md`
revised accordingly; the script's docstring corrected in place.

## Step 2g (added after the skeptic pass) — the real, non-tautological Nijenhuis test

Computes the Nijenhuis tensor **directly in the aligned basis** (`M_BASIS`,
the same basis Stage 2a and this file's own Step 2 use), with **no
relabelling step** — closing exactly the gap the skeptic identified in
Step 1.

```
aligned eps=(1, 1, 1)     Nijenhuis = -4   non-integrable
aligned eps=(-1,-1,-1)    Nijenhuis = -4   non-integrable
the other 6               Nijenhuis =  0   integrable

aligned non-integrable set (direct, no relabelling) : {(1,1,1),(-1,-1,-1)}
aligned C-linear set (Step 2f, independent)         : {(1,1,1),(-1,-1,-1)}
DIRECT MATCH: True
```

**CONFIRMED, non-tautologically.** This is the version of item 3 that
survives — computed in the same coordinate system with no relabelling
step, so it genuinely could have disagreed and did not.

## FL Step 8a Response Matrix

| skeptic concern | verdict | response |
|---|---|---|
| Step 1's relabelling test is vacuous for any conjugate pair | **CONFIRMED** (verified directly, 4 different pairs) | **Fixed** — Step 2g, direct aligned-basis Nijenhuis, no relabelling |
| Step 1's `assert`s make the FALSIFIED branch dead code | **CONFIRMED** (read the code) | **Accepted as a code-quality note** — the asserts are legitimate regressions against known values; the *comparison test* was the vacuous part, now replaced |
| "24 direct tests" is inflated; really ~3 independent facts | **CONFIRMED** (verified: block-locality of family columns + block-diagonality of `acs_from_eps` + linearity) | **Fixed** — `claim.md` restated as 3 facts + 2 structural (non-computational) arguments |
| `(3,3)` sector dims and "LC ∈ family" are sign-blind, not sign-sensitive gates | **CONFIRMED** (algebraic proof + cross-check against C151's own wrong-sign result) | **Fixed** — removed from sign-sensitive kill-criterion, kept as code-correctness checks only |
| decision.md quoted stale/paraphrased script output not matching real branches | **CONFIRMED** (an earlier draft of this file did) | **Fixed** — this version quotes only output copied from the actual saved `results_*.txt` files |
| Item 4's "exact, no numpy SVD anywhere" is false for item 3 (Step 1 used numpy/floats) | **CONFIRMED** (Step 1 does `import numpy`, uses `1e-10` float threshold) | **Fixed** — Step 2g makes item 3 exact too; `claim.md` item 4 now scoped correctly |

**No concern was dismissed.** Every one either identified a real defect
(fixed) or a real limitation now stated explicitly (accepted, documented).

## What survives, stated at its correct strength

- 3 exact facts (one per plane): `c((J_eps)|_plane k · v_k) = i^{eps_k} c(v_k)`
  for `eps_k=+1`, with `eps_k=−1` following by linearity — not 24, not 6.
- The 2-of-8 global `C`-linearity is the combinatorial corollary "all three
  agree", requiring no further explanation.
- Non-integrability (Nijenhuis ≠ 0), computed directly with no relabelling,
  is exactly the "all-agree" set — genuinely confirmed, not tautological.
- All of the above is exact (`sympy` rational arithmetic throughout,
  including now the Nijenhuis computation).

## Four self-caught or skeptic-caught defects, one pattern

| # | defect | caught by |
|---|---|---|
| 1 | rationalised numeric SVD output, residual `2.1e-4` | the honesty-check assert written before trusting it |
| 2 | tested only `+i`, missed `−i` | re-reading the pre-registration's own `±i` wording |
| 3 | tested family column `k` against a.c.s. position `k`, wrong pairing | building an independent falsification test and reading its output |
| 4 | Step 1's relabelling test is tautological; "24 tests" inflated | context-blind FL Step 8a skeptic, from code alone, no execution |

Defects 1–3 were structural bugs in the arithmetic, caught by gates built
while doing the work. Defect 4 was different in kind: the arithmetic was
correct throughout — the error was in how much evidentiary weight the
prose around it claimed. No amount of re-running the same code would have
caught it; it took an outside reader asking "does this actually test what
it says it tests?"

## What this does NOT establish (see claim.md; superseded by the novelty check above)

~~The plausible classical explanation (Weyl group `S₃` orbit of Borel
choices = the 6 integrable structures; the 2 all-agree tuples are the
exceptional non-Weyl ones) remains **unverified** — candidate C154.~~
**No longer open — see the correction at the top of this file.** Borel–Hirzebruch
(1958) and Burstall–Salamon (1987) already establish exactly this; confirmed
by novelty check before any C154 was built. What remains open instead: the
actual *values* `c(v_k)`, not their sign/eigenvalue structure — see the
correction's final paragraph.

## Reproduce

```
python c153_step1_nijenhuis_correlation.py       # withdrawn as evidence; correction appended in-file
python c153_step2_exact_rational_verification.py # exact reconstruction, 2-of-8, AND Step 2g (real Nijenhuis test)
python c153_step3_per_plane_factorization.py     # per-plane law, 3 facts (not 24); correction appended in-file
```
