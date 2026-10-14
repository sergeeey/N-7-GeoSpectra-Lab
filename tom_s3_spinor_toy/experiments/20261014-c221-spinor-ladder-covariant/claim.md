# C221 Claim — ladder operators and the spin-1/2 multiplet of SO(3) on S²: the literal orbital route, and the spin-weighted (covariant) route

**Date:** 2026-10-14
**FL tier:** [x] Standard (derivation round for external correspondence; no project physics claim)
**Question type:** [x] descriptive (exact calculation; no population, no intervention)

## Why this round exists

The correspondent's message of 2026-10-14 sets the next stage after C220: use the ladder operators to find the
complex harmonics of the spinor multiplet of `SO(3)`. Five steps, paraphrased: (1) eigenfunctions of `L_z` in polar
coordinates with eigenvalues `−1/2, +1/2` (an `e^{imφ}` factor times an unknown function `χ(θ)`); (2) `L₊ Y_{1/2,1/2} = 0`
gives `χ_{1/2,1/2}`; (3) the lowering operator on the `m = −1/2` eigenfunction gives `χ_{1/2,−1/2}` (the message says
`m = −1`; read here as `−1/2`, since steps 1 and 4 use `±1/2` — the literal `m = −1` reading is also computed and
labelled); (4) `L₋ Y_{1/2,1/2}` should be `Y_{1/2,−1/2}` and `L₊ Y_{1/2,−1/2}` should be `Y_{1/2,1/2}`, which may fix the
normalisation; (5) compare that normalisation with integration over the sphere.

## Prior Result Gate

1. `C179`: a multiplet of ordinary (single-valued) functions on `Sⁿ` cannot carry a spinor representation
   (`NOGO-CONFIRMED`). Expected consequence for this round: any `m = ±1/2` solution is double-valued (`e^{±iφ/2}`).
2. `C184b`/`C185`/`C195`–`C197`: the `S²` doublet derived by descent from `S³`:
   `χ_{+1/2} = e^{−iφ/2} cos(θ/2)`, `χ_{−1/2} = e^{iφ/2} sin(θ/2)`, plus a tower (spin weights 1/2, 3/2). Its labels are
   opposite to the `L_z` eigenvalue (checked in a scratch preview on 2026-10-14: `χ_{+1/2}` has `L_z = −1/2`).
3. `C220`: the integer (`l=1`) version of exactly this procedure, with `L± Y_{1,m} = √2 Y_{1,m±1}`.
4. **Status:** [x] NEW (no round applies the five steps to the spinor case; no `null_results`/`parked` hit).

## Estimand

One sentence, written before the formal run: *we compute, exactly, the solutions of the five steps for the spin-1/2
multiplet on the unit sphere, first with the orbital operators `L±` of McMurry p. 144 (spin weight `s = 0`), then with the
spin-weighted operators `L±^{(s)} = e^{±iφ}(±∂_θ + i cotθ ∂_φ − s/sinθ)`, reporting where each step holds, where it
fails, and what condition on `s` makes the chain close.*

**Population:** functions `ψ(θ,φ) = χ(θ) e^{±iφ/2}` on the unit sphere (`dΩ = sinθ dθ dφ`). **Method:** exact symbolic
computation (sympy) with analytic norms; an independently written re-implementation (given only the definitions and a
task list, no expected answers) compares results.
**Conventions fixed before the run:** `L_z = −i∂_φ`; `m` is the `L_z` eigenvalue; `L² = L₋L₊ + L_z² + L_z`.

## Pre-registered predictions

**Honesty note:** a scratch preview (not part of this round, not archived) already computed items P1–P3, P5 and the
`s = 1/2` closure by hand-assisted sympy before this file was written. These are therefore **predictions, not blind
ones**; the independence of the check comes from the separately written re-implementation, whose author did not see them.

| # | Prediction | If false |
|---|---|---|
| P1 | `s=0`: `L₊(χe^{iφ/2})=0 ⇒ χ = C sin^{1/2}θ`; `L₋(χe^{−iφ/2})=0 ⇒ χ = C' sin^{1/2}θ`; `L² = 3/4` on both | report |
| P2 | `s=0`, step 4: `L₋ψ_↑ = −cotθ ψ_↓`, `L₊ψ_↓ = +cotθ ψ_↑` — a **θ-dependent** ratio, so step 4 does not hold with a constant coefficient; the lowering chain does not terminate (`L₋²ψ_↑ ∝ sin^{−3/2}θ e^{−3iφ/2}`, not square-integrable) | report |
| P3 | `s=0`: `⟨ψ_↑,ψ_↑⟩ = π²` (`N = 1/π`); `⟨L₋ψ_↑, L₋ψ_↑⟩ = π²` (the algebra identity `j(j+1) − m(m−1) = 1`) | report |
| P4 | For generic `F` and generic `s`: `[L₊,L₋] = 2L_z`, `[L_z,L±] = ±L±` (the extra term does not spoil `su(2)`) | report |
| P5 | `s = 1/2`: `L₊(χe^{iφ/2})=0 ⇒ χ = C sin(θ/2)`; `L₋(χe^{−iφ/2})=0 ⇒ χ = C' cos(θ/2)`; closure: `L₋ψ_↑ = ψ_↓`, `L₊ψ_↓ = ψ_↑` with constants of modulus 1 (Condon–Shortley sign for `ψ_↓`); `L² = 3/4`; `N = 1/√(2π)` for both | report |
| P6 | The `s = 1/2` pair equals the `C184b` doublet up to normalisation and sign, with the labels reversed (`C184b`'s `χ_{+1/2}` is the `m = −1/2` member) | report |
| P7 | Closure scan over `s ∈ {0, ±1/2, ±1, ±3/2}`: the pair closes for `s = ±1/2` (mirror images under `θ → π−θ`) and not for `s = 0`; the other values are **exploratory**, no prediction | report |
| P8 | Both members at `s = ±1/2` are anti-periodic: `ψ(φ+2π) = −ψ(φ)` (consistent with C179) | report |

## Controls

- **D1 (integer positive control):** `s = 0`, integer `m`: `L₊[χe^{iφ}] = 0 ⇒ χ = C sinθ`, and `L₋ Y_{1,1} = √2 Y_{1,0}` with the C220 harmonics (the same code path reproduces C220).
- **D2 (negative control, wrong operator):** `s = 1/2` operators applied to the integer harmonics `Y_{1,m}` do **not** close on the `l=1` set.
- **D3 (negative control, algebra) — WITHDRAWN, see Amendment 1:** as pre-registered, "unequal constants in `L₊` and `L₋` (`+1/2`, `−1/2`) break `[L₊,L₋] = 2L_z`". This prediction was **false**. Replaced by D3a/D3b/D3c below.
- **D4 (negative control, scan):** the closure test returns **no** for `s = 0`, i.e. it can say no.
- **D5 (literal reading):** step 3 read literally (`m = −1`, `s = 0`) gives `χ = C sinθ`, the **vector** `m = −1` function, not a spinor.

## Kill criterion

If no `s` makes the `m = ±1/2` pair close (P5/P7), the covariant route fails and the result is reported as: steps 1–3 and 5
hold, step 4 fails with orbital operators, and no spin-weight rescues it; stop and escalate. If the independent
re-implementation disagrees with the main script on any of T1–T9, resolve before anything is written to the correspondent.

## What this result does NOT mean

1. It does not show that a multiplet of ordinary single-valued functions carries the spin-1/2 representation (`C179` stands;
   these functions are double-valued).
2. It does not say which functions the correspondent is looking for; only that the orbital route gives `sin^{1/2}θ e^{±iφ/2}`
   and the `s = 1/2` route gives the `C184b` doublet.
3. It does not derive the geometric origin of the `−s/sinθ` term (identification with the Lie derivative of a spinor along a
   rotation, or with a frame term, is a **hypothesis**, untested here). The standard construction of spin-weighted
   harmonics is recalled from memory `[MEMORY]` and not checked against a source here.
4. It does not bear on `N_gen = 3` or `OB1`.

## Amendments (made after the first runs; the original text above is kept)

1. **D3 was wrong and is replaced (found by the independent pass, then reproduced by the main script).** The commutator
   `[L₊^{(a)}, L₋^{(b)}] F − 2L_z F` is `0` for symbolic `a`, `b` and a generic `F(θ,φ)` (checked with sympy; the script now
   does this in D3a). So the commutator test **cannot** detect `a ≠ b`. No explanation of why is claimed here. Replacement controls, written after seeing this:
   - **D3a** (main, not a control): the commutator test is blind to unequal constants (the original D3 prediction, reversed).
   - **D3b** (negative control): with `L₊` at `s = 1/2` and `L₋` at `s = −1/2` the closure ratio `L₋ψ_↑/ψ_↓` is θ-dependent.
   - **D3c** (negative control): formal adjointness `⟨G, L₊^{(a)}F⟩ = ⟨L₋^{(b)}G, F⟩` (real test functions that vanish at the
     poles) holds for `a = b` and fails for `a ≠ b`.
   These three are post-hoc replacements, not pre-registered.
2. **Check B3d** first compared the norm of `L₋ψ_↑` computed from the raw, unsimplified operator output, which sympy could
   not integrate (`nan`). It now uses the exact equality `L₋ψ_↑ = ψ_↓` already proved in B3b. The content of the check is
   unchanged; the first version of the code was the problem, not the claim.
3. **Exploratory finding, not pre-registered and not counted as evidence:** the independent pass reports that the pair
   closes iff `j − |s| ∈ ℤ≥0` (the spin-weighted-harmonics rule), checked on 21 `(j, s)` pairs. This script scans only
   `s ∈ {0, ±1/2, ±1, 3/2}` at `j = 1/2` (P7) in its first version; `−3/2` was added after the skeptic round (Amendment 5).
5. **After skeptic round 1 (see `decision.md` section 8):** `s = −3/2` added to the scan (it was in the pre-registered set but missing from the code); D3b now divides by the lowest-weight state of the `L₋` actually applied; D5 is counted as an ordinary check, not a control (counts now 29 main, 5 controls). The wording of P6 and P8 is narrowed in `decision.md` (P6: one convention, quantisation along −z; P8: anti-periodicity is a statement in the `e^{±iφ/2}` gauge); the claim text above is kept as pre-registered.
4. **Preview.** The scratch preview mentioned in the honesty note covered P1–P3, P5 and the `s = 1/2` closure. P4, P6, P7, P8
   and the controls D1–D5 were written before any code for them existed, but after the preview had shown the shape of the
   answer, so they are not blind either.
