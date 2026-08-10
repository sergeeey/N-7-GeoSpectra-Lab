# C11 step 1 — is there a NATURAL algebra `A`, and does it make the doubling necessary?

**Experiment id:** `20260810-c11-step1-algebra-search`
**Date:** 2026-08-10
**Track:** B (`tom_s3_spinor_toy`)
**Predecessors:** C42 (one-operator reading closed) → C43 (block supplies a grading)
→ **C44 (that grading is GENERIC — the doubling is NOT yet earned)**

---

## Why this now carries the full weight

C44 removed the grading as evidence for the `t=0/t=1` doubling: `spec(D^{1-t}) = -spec(D^t)`
is an identity in `t`, so the grading exists for every mirror pair and says nothing about
`t=0,1`. What survived is only that the grading is **not obstructed** for a block, where
C35 showed it **is** obstructed for one operator — a removed obstacle, not a positive reason.

So the question "is the doubling earned?" now rests entirely on the remaining
`PARENT_ACTION_GATE` fields, and the algebra is the cheapest of them because first-order,
orientability and Poincaré duality are all defined **relative to** `A`.

## L0 (EstimandOps): **Descriptive**

We are describing which algebras are admissible on the given `(H, D_block, gamma)`, not
predicting an observable and not making a causal claim.

---

## The claim under test

> **C45 (proposed).** On `H = L2(S3,S) (+) L2(S3,S)` with `D_block = D^0 (+) D^1`, there is a
> natural unital `*`-algebra `A` satisfying the spectral-triple axioms available at this
> stage, and its existence makes the doubling **structurally necessary** rather than
> optional.

**Falsifier, fixed in advance:** if every admissible `A` either (a) acts block-diagonally
with independent sector actions, or (b) reduces to one algebra duplicated on both sectors,
or (c) is not unique among typed candidates — then the algebra does **not** earn the doubling,
and C45 is **FALSIFIED as stated**.

---

## Red-flag criteria — stated BEFORE the search (portfolio requirement)

| Flag | Fires when | What it means |
|---|---|---|
| **RF1 gratuitous** | admissible `A` contains all of `{(even,I),(odd,I),(even,s3),(odd,s3)}` | `H` splits as a direct sum of two INDEPENDENT spectral triples — the doubling is a relabelling |
| **RF2 duplicate** | admissible `A` is exactly `A0 (x) I` (same function on both sectors) | second copy is a pure multiplicity — adds nothing |
| **RF3 mixing** | admissible `A` contains a sector-off-diagonal term (`s1` or `s2`) | genuine mixing — necessary but NOT sufficient for "earned" |
| **RF4 non-unique** | ≥2 inequivalent typed candidates are admissible | the construction has no selection power — the same disease C44 found for the grading |
| **RF5 gamma non-unique** | the set of valid gradings has positive-dimensional moduli | "the algebra selected by the grading" is not even well-defined without extra input |

**RF4 and RF5 are the ones C44 taught us to check.** A property satisfied by a whole family
of alternatives is not evidence for the particular member we care about.

---

## Predictions, recorded before running

| # | Prediction | Why |
|---|---|---|
| **P1** | the sector-distinguishing part of `D_block` is a **bounded** operator (`(3/2)·s3`), so the bounded-commutator axiom imposes **zero** constraint on the sector index | C42's own fact: the torsion shift `(t-1/2)h_H` is the SAME for every level |
| **P2** | the set of valid gradings has **large** moduli (∏ U(d_lambda)) — RF5 fires | eigenvalue multiplicities `(n+1)(n+2)` are large and grow |
| **P3** | `gamma_geo = U_iota (x) s1` anticommutes with `D_block`, and **both factors are needed** — `I (x) s1` and `U_iota (x) I` each FAIL | `U_iota` flips `D^{1/2}`, `s1` flips `s3`; neither alone flips both |
| **P4** | the `gamma_geo`-even algebra is **not** `A0 (x) I`: an iota-ODD function may not act as the same function on both sectors | `(odd, I)` is `gamma`-odd |
| **P5** | ≥2 inequivalent typed candidates survive ⇒ **RF4 fires** ⇒ C45 falsified as stated | admissibility is closed under passing to unital subalgebras |

P5 is the prediction that would kill the claim. It is recorded here so that a null result
cannot be re-read afterwards as a success.

---

## What this CANNOT show

- It cannot show the doubling is **wrong** — only whether the algebra argues for it.
- It does not supply `J`, first-order, orientability or Poincaré duality (steps 3–6).
- It does not touch `N_gen=3` (step 7, explicitly deferred).
- **ASSUMPTION A1, not re-derived here:** `U_iota D^{1/2} U_iota^dag = -D^{1/2}`, i.e. the
  spinor lift of the orientation-reversing isometry `iota` flips the Dirac operator. Provenance:
  C39 (`iota` is orientation-REVERSING, verified) + the standard fact that an orientation-reversing
  isometry conjugates `D` to `-D`. If A1 fails, `gamma_geo` fails and P3–P5 are void.
- **OPEN, flagged not assumed:** whether the Pin-lift satisfies `U_iota^2 = +1` (needed for
  `gamma^dag = gamma`). Both signs are carried through the search.

## kill_criterion

If the search finds that **exactly one** typed candidate is admissible AND it contains a
sector-mixing term AND no smaller unital subalgebra is admissible, C45 stands. Anything
else falsifies it as worded.
