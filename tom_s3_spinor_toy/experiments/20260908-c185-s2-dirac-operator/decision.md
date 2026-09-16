# C185 Decision — PROMOTE. The S² Dirac operator is built and its spectrum derived; ONE pre-registered caveat (the χ frame-match) was NOT actually closed — see §4 addendum, 2026-09-10.

**Date:** 2026-09-09 (§4 addendum added 2026-09-10)
**Verdict:** **PROMOTE** — all seven pre-registered predictions hold, the
injected-error control breaks the pattern, `13 of 13` checks pass. Exact
symbolic arithmetic throughout; no floating point in any verdict. The
spectrum/multiplicity result is solid; the separate, pre-registered
"χ is written in a different frame than this operator's eigenspinors"
subtlety was flagged in `claim.md` as needing explicit resolution and was
never actually resolved — this was silently dropped rather than reported,
until a context-blind skeptic pass on correspondence drafted from this
round caught it. See §4.

All numbers trace to `c185_s2_dirac.py` and `run_output.txt`.

---

## 1. What was open, and what is now closed

`C182`'s own `decision.md` line 116, in its own words:

> **The `S²` Dirac eigenvalues `±(l+1)` are NOT derived.** Only multiplicities.
> The `S²` Dirac operator was not built.

That sentence had already travelled into an outgoing letter, where it read as an
asymmetry against `S³` — there an operator was built and its whole spectrum
computed (`C180`, `C184`), here only multiplicities by descent. Both halves are
now closed:

| | before | now |
|---|---|---|
| the operator | not built | built from the metric: frame → Cartan → connection → `D`, each step verified |
| self-adjointness | — | `P3`, by the Euler-operator test |
| Lichnerowicz | — | `P4`, exact: `D² − (∇*∇ + R/4) = 0` componentwise, `R = 2` |
| eigenvalues | cited | **derived**: `±1, ±2, ±3` |
| multiplicities | `2, 4, 6` by Hopf descent | `2, 4, 6` again, from the operator's own spectrum |
| `0` not an eigenvalue | — | `P6d`, checked |

**The spectrum, computed:**

```
lambda = -3 :  m = -5/2 -3/2 -1/2 +1/2 +3/2 +5/2      multiplicity 6
lambda = -2 :  m = -3/2 -1/2 +1/2 +3/2                multiplicity 4
lambda = -1 :  m = -1/2 +1/2                          multiplicity 2
lambda = +1 :  m = -1/2 +1/2                          multiplicity 2
lambda = +2 :  m = -3/2 -1/2 +1/2 +3/2                multiplicity 4
lambda = +3 :  m = -5/2 -3/2 -1/2 +1/2 +3/2 +5/2      multiplicity 6
```

`|λ| = n+1` with multiplicity `2(n+1)` **per sign**, `n = 0, 1, 2`.

**`P7`, the one that makes this more than a textbook re-derivation:** those
multiplicities `2, 4, 6` are the same three numbers `C182` obtained by counting
Hopf weight-sector dimensions at `k = 1, 3, 5` — a route sharing no machinery
with this one. Two independent computations, three numbers each, all agreeing.

---

## 2. How the spectrum is computed, and why not the obvious way

The first attempt routed the eigenfunctions down from `S³` by the Hopf descent,
to reuse `C182`/`C184b`'s machinery. **It ran 25 minutes of CPU and produced
nothing** — every matrix entry needed `simplify` on an expression mixing
exponentials with half-angle trigonometry, inside a double loop. Killed, not
debugged: the approach was wrong, not the code.

What replaced it is exact and finite. With `ψ = (f(θ), g(θ)) e^{imφ}`, `m`
half-integer, the eigenvalue equation is two first-order ODEs; in
`s = sin(θ/2)`, `c = cos(θ/2)` — where `ds/dθ = c/2`, `dc/dθ = −s/2` — and
multiplied by `4sc`, they become **polynomial identities**. Taking `f`, `g`
homogeneous of degree `N` makes both sides homogeneous of degree `N+2`, so the
whole problem is a linear system over `ℚ(i)` and the spectrum is a list of
nullspace dimensions. No transcendental simplification anywhere.

A degree-`N` solution reappears inside every higher `N` (multiply by
`s² + c² = 1`), which is why one scan at `N = 5` captures all three levels.

**Floor, as pre-registered:** "some operator has some spectrum" is nearly free —
a *wrong* connection also yields a discrete spectrum with multiplicities. The
criterion was never "eigenvalues were obtained" but "`n+1` with multiplicity
`2(n+1)`". Tested directly: doubling the connection coefficient gives
`[0, 0, 0]` — the pattern is not merely different, it disappears.

---

## 3. Three checks failed. All three were the check, not the operator.

This is the round's most useful finding and it is about method, not about `S²`.

**`P4` — compared `D²` against the scalar Laplacian.** Lichnerowicz is about the
**spinor connection** Laplacian, which carries the connection inside the `φ`
derivative. The residue the failing check reported,
`(sin²θ − 2cos θ + 1)/(4 sin²θ)`, is *exactly the connection term it had left
out*. Rebuilt from the same connection `D` itself uses → residue `[0, 0]`.

**`P3`, first attempt — guessed an antiderivative** and compared the residue
against it. A guess that misses cannot distinguish "not self-adjoint" from
"guessed wrong". Replaced by the Euler-operator test, which decides whether an
expression is a total derivative without needing to know what of.

**`P3`, second attempt — the test pair itself was malformed.** It gave the two
spinor components *opposite* `φ` phases. `D` swaps components, so `Dψ = λψ` is
consistent only when both carry one and the same `e^{imφ}`. The Euler operator
duly returned residues proportional to `e^{±iφ}` — the signature of a badly
shaped test pair, not of a non-symmetric operator. Corrected → `[0, 0, 0, 0]`.

Three failures, three checks, zero defects in the object under test. Worth
stating plainly because the opposite reading — "the operator is broken" — was
available at each step and would have been wrong each time.

---

## 4. What this does NOT establish

- **No novelty is claimed.** `±(n+1)` with multiplicity `2(n+1)` on the round
  `S²` is textbook. What changed is that this project can now produce it from
  its own construction instead of citing it.
- **Does NOT make the `S²` spinors functions.** The obstruction is untouched;
  this is an operator acting on the same double-valued objects.
- **Levels beyond `n = 2` are not checked.** The pattern is verified at
  `n = 0, 1, 2`; that it continues is inference, not computation here.
- **The unit radius is assumed**, as is the round metric. Nothing here addresses
  a deformed sphere.
- **Does NOT settle the frame question for `S³`**, which is separate and still
  as stated in `C184`.
- **Does NOT resolve the frame subtlety `claim.md` itself pre-registered as
  needing explicit resolution, and this section originally omitted that gap
  instead of reporting it (found 2026-09-10, by a context-blind skeptic
  reviewing correspondence drafted from this round, not by this round's own
  self-review).** `claim.md`'s own "Substrate note" states: *"the doublet
  `chi` derived in `C184b` is written in the frame the Hopf descent
  produces, which is NOT the coordinate frame a coordinate-built Dirac
  operator uses. A hand-check... found `D chi` is not proportional to `chi`
  in the naive pairing... this round must resolve it explicitly rather than
  quietly re-pair things until something matches."` It was not resolved:
  `c185_s2_dirac.py`'s eigenspinor ansatz (lines 218-224) is
  `ψ=(f,g)e^{imφ}` with the SAME `m` on both components (lines 141-143
  explain why: `D` swaps the two components, so consistency requires a
  shared phase) — while `χ` from `C184b` carries OPPOSITE φ-phases on its
  two components (`e^{-iφ/2}`, `e^{+iφ/2}`). These are different frames;
  `χ` was never transported into the one this operator's eigenspinors
  live in, and `kernel_dim()` (line 233) only ever checks dimensions, never
  extracts or tests an actual eigenfunction against `χ`. The `m`-values do
  line up (`±1/2` at `|λ|=1`, matching `χ`'s own labels) — the explicit
  frame-transport and match is still owed, not done. This is a genuine,
  still-open item, not a closed one; any future claim that "χ is confirmed
  to be C185's `|λ|=1` eigenspinor" is not yet supported by this round.

---

## 5. Consequence for the outgoing letter

`DRAFT_REPLY_TO_TOM_2026-09-08_PART2.md` §7 carried, until now:

> **That the S² objects cannot be functions I have shown, but not from an
> operator on S² itself** — the argument runs through the descent from S³. An
> `S²` Dirac operator built directly would be an independent check, and I have
> not built one.

That is now false in its second half, and the bullet is replaced by the
result — the spectrum, derived, `13/13`. It should NOT be replaced by
silence on frames: see §4's added addendum — the honest replacement bullet
states the spectrum is derived AND that `χ`'s match to this operator's own
`|λ|=1` eigenspinor is not yet explicitly verified (a frame-transport still
owed), not "the caveat is fully closed."
The `χ` in §1 can be called eigenfunctions of an operator this project built —
still not a novelty claim, but no longer a borrowed identification.

---

## 6. Reproduction

```
cd experiments/20260908-c185-s2-dirac-operator
python c185_s2_dirac.py
```

13/13, about 40 seconds. `ruff check` and `ruff format`: clean.
