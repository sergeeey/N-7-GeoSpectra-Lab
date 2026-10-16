# C221 Decision — the five ladder-operator steps for the spin-1/2 multiplet: steps 1–3 and 5 work with the orbital operators, step 4 does not; with a spin-weight term (s = ±1/2) all five close

**Date:** 2026-10-15
**Verdict:** **PROMOTE as a derivation** (status line at the end: skeptic round 1 is recorded in section 8).
In `c221_spinor_ladder.py` (`run_output.txt`, `results_c221.json`): `29/29` main checks pass, `5/5` negative
controls behave as required, and `1` further check that restates another is held back and **not counted** as
evidence. A separately written re-implementation (a subagent given the definitions only, no expected answers)
agrees on every substantive result (section 5). Same model family wrote both, so this is independent *code*, not an
independent *mind*.

Every number below is copied from `run_output.txt` or from the independent pass's printed output.
`[VERIFIED-sympy]` = exact symbolic; `[VERIFIED-numeric]` = high-precision numeric at sample angles.

## 0. Conventions (fixed in `claim.md` before the run)

| Item | Definition |
|---|---|
| Sphere | unit `S²`, `dΩ = sinθ dθ dφ` |
| `L_z` | `−i ∂_φ`; `m` is its eigenvalue |
| Orbital ladder operators (McMurry p.144, as in C201/C206/C220) | `L₊ = e^{iφ}(∂_θ + i cotθ ∂_φ)`, `L₋ = e^{−iφ}(−∂_θ + i cotθ ∂_φ)` |
| Spin-weighted family | `L±^{(s)} = e^{±iφ}(±∂_θ + i cotθ ∂_φ − s/sinθ)`; `s = 0` is the orbital case |
| Casimir | `L² = L₋L₊ + L_z² + L_z` |
| Action on `χ(θ)e^{imφ}` | `L₊ → e^{i(m+1)φ}(χ' − m cotθ χ − sχ/sinθ)`, `L₋ → e^{i(m−1)φ}(−χ' − m cotθ χ − sχ/sinθ)` |

How the five steps of the 2026-10-14 message were read: step 3 says "`m = −1`"; steps 1 and 4 use `±1/2`, so it is
read as `m = −1/2`. The literal reading (`m = −1`, `s = 0`) is also computed (control D5): it gives `χ = C sinθ`, the
vector function `∝ sinθ e^{−iφ}`, not a spinor.

## 1. Orbital operators (`s = 0`): steps 1, 2, 3 and 5 work; step 4 fails

| Step | Result | Check |
|---|---|---|
| 1. `L_z` eigenfunctions | `ψ = χ(θ) e^{±iφ/2}` has `L_z = ±1/2` | A1 |
| 2. `L₊[χ e^{iφ/2}] = 0` | `χ' − ½ cotθ χ = 0`, so `χ = C sin^{1/2}θ` (first-order linear ODE: unique up to `C`, A2b) | A2, A2c |
| 3. `L₋[χ e^{−iφ/2}] = 0` | `−χ' − ½ cotθ χ = 0`, so `χ = C′ sin^{1/2}θ` | A3 |
| 4. `L₋ψ_↑ ∝ ψ_↓`, `L₊ψ_↓ ∝ ψ_↑` | **fails**: `L₋ψ_↑ = −cotθ · ψ_↓`, `L₊ψ_↓ = +cotθ · ψ_↑`. The ratio depends on `θ` (unbounded at both poles) | A4a, A4b |
| 5. normalisation | `⟨ψ_↑,ψ_↑⟩ = ⟨ψ_↓,ψ_↓⟩ = π²` (so `N = 1/π`); `⟨L₋ψ_↑,L₋ψ_↑⟩ = π²` as well; `⟨ψ_↑,ψ_↓⟩ = 0` | A7a–c |

with `ψ_↑ = sin^{1/2}θ e^{iφ/2}`, `ψ_↓ = sin^{1/2}θ e^{−iφ/2}` (unnormalised). `L² = 3/4` on both (A6), as `L₊ψ_↑ = 0`
alone forces `m² + m = 3/4`.

Further, [VERIFIED-sympy, A5a/A5b]: `L₋²ψ_↑ = −sin^{−3/2}θ e^{−3iφ/2}`, and `∫|L₋²ψ_↑|² dΩ = 2π ∫ sin^{−2}θ dθ`
diverges (cut at `ε`: `2π · 2 cot ε → ∞`). The lowering chain does not terminate and leaves the square-integrable
functions after two steps.

**What the equal norms do and do not say.** `⟨L₋ψ_↑, L₋ψ_↑⟩ = π² = ⟨ψ_↓,ψ_↓⟩` is the algebra identity
`j(j+1) − m(m−1) = 3/4 + 1/4 = 1` times the norm of `ψ_↑`; it holds for any pair obeying `L² = 3/4`,
so it is **not** evidence that `L₋ψ_↑` is `ψ_↓`. The independent pass printed the decisive fact: the overlap
`⟨ψ_↓, L₋ψ_↑⟩ = 0` (`2π ∫ sin^{1/2}θ · (−cosθ sin^{−1/2}θ) · sinθ dθ = 0`), and `L²(L₋ψ_↑) = 3/4 · L₋ψ_↑`. So at
`s = 0`, `L₋ψ_↑ = −cosθ sin^{−1/2}θ e^{−iφ/2}` is a *second, orthogonal* solution with the same `L_z`, the same `L²` and the same norm,
and it is not `ψ_↓` [VERIFIED-sympy, independent pass only; not in the main script].

**Double-valuedness** (A8, `P8`): `ψ(φ+2π) = −ψ(φ)` for both. This is the expected consequence of `C179` (no multiplet of
single-valued functions on `Sⁿ` carries a spinor representation); it is not a new result.

## 2. Spin-weighted operators (`s = ±1/2`): all five steps close

**Algebra** [VERIFIED-sympy, B1a/B1b]: for a generic function `F(θ,φ)` and generic `s`,
`[L₊,L₋]F = 2L_z F`, `[L_z,L₊]F = L₊F`, `[L_z,L₋]F = −L₋F`. The extra `−s/sinθ` term does not spoil `su(2)`.
(It also does not need to be the same in `L₊` and `L₋` for the commutators to hold — section 4, D3a.)

**Highest and lowest weight** [VERIFIED-sympy, B2a–c]: `f'/f = m cotθ + s/sinθ` integrates to
`f = sin^mθ · tan^s(θ/2)` (using `d/dθ ln tan(θ/2) = 1/sinθ`); `L₊[sin^m tan^s(θ/2) e^{imφ}] = 0` and
`L₋[sin^{−m} tan^{−s}(θ/2) e^{imφ}] = 0` for symbolic `m`, `s`. An independent `dsolve` of the `s = 1/2` ODE agrees (ratio
constant at 4 angles).

**s = 1/2** [VERIFIED-sympy, B3a–e], normalised, Condon–Shortley sign on the lower member:

```
ψ_↑ = + sin(θ/2) e^{ +iφ/2} / √(2π)     L_z = +1/2,   L₊ψ_↑ = 0
ψ_↓ = − cos(θ/2) e^{ −iφ/2} / √(2π)     L_z = −1/2,   L₋ψ_↓ = 0
L₋ψ_↑ = + ψ_↓        L₊ψ_↓ = + ψ_↑        L² = 3/4 on both        ⟨ψ_↑,ψ_↑⟩ = ⟨ψ_↓,ψ_↓⟩ = 1
```

So step 4 holds with coefficient exactly `1 = √(j(j+1) − m(m∓1))` at `j = 1/2`, and step 5 agrees: the norm forced by
step 4 (`|L₋ψ_↑| = |ψ_↓| = |ψ_↑| = 1`) equals the norm from integration over the sphere, with `N = 1/√(2π)`.
Without the minus sign on `ψ_↓` the coefficients are `−1` and `−1`; that sign is a convention.
The mirror choice `s = −1/2` is the image of this under `θ → π − θ`: `cos(θ/2) e^{iφ/2} → sin(θ/2) e^{−iφ/2}` with
constant `+1` in both directions (B6).

**Relation to C184b** (B4): the pair equals the `S²` doublet of `C184b` up to normalisation and sign, **with the labels
reversed**: `C184b`'s `χ_{+1/2} = e^{−iφ/2} cos(θ/2)` has `L_z = −1/2`, and `χ_{−1/2} = e^{iφ/2} sin(θ/2)` has `L_z = +1/2`.
The label in `C184b` is therefore not the `L_z` eigenvalue.

**Antiperiodic** (B3e): `ψ(φ+2π) = −ψ(φ)` for both members.

## 3. Closure scan over `s` (`P7`)

Highest-weight and lowest-weight functions for each `s`, `m = ±1/2`; closure means both ratios
`L₋ψ_↑/ψ_↓` and `L₊ψ_↓/ψ_↑` are constant in `θ` (30-digit evaluation at four angles):

| `s` | closes | `L₋ψ_↑/ψ_↓` | `L₊ψ_↓/ψ_↑` |
|---|---|---|---|
| `0` | no | θ-dependent (`−cotθ`) | θ-dependent (`+cotθ`) |
| `+1/2` | **yes** | `−1` (unnormalised) | `−1` |
| `−1/2` | **yes** | `+1` | `+1` |
| `±1` | no | θ-dependent | θ-dependent |
| `+3/2` | no | θ-dependent | θ-dependent |
| `−3/2` | no | θ-dependent (`2004 … 0.16`) | θ-dependent |

The independent pass derived the general-`s` ratios in closed form (not in the main script):
`r₋ = L₋ψ_↑/ψ_↓ = −(cosθ + 2s) tan^{2s}(θ/2) / sinθ`, `r₊ = (cosθ − 2s) tan^{−2s}(θ/2) / sinθ`, with product
`(4s² − cos²θ)/sin²θ`, which equals `1` for `s = ±1/2`. The pair closes at `s = ±1/2` among the tested values,
and the main script's closure test returns "no" at `s = 0` (control B5b), so it can say no.
`s = −3/2` was missing from the first version of the scan (the pre-registered set had it); it was added after the skeptic pointed this out, and it does not close. The skeptic also derived by hand, and its script confirmed, that for all real `s` at `j = 1/2` the ratio is θ-independent iff `4s² − 1 = 0`, so the closure condition is exactly `s = ±1/2`; the main script itself only samples seven values.

## 4. Controls

| Control | Result |
|---|---|
| D1 integer positive control (`s = 0`, `m = 1`): `L₊[sinθ e^{iφ}] = 0`, `L₋Y(1,1) = √2 Y(1,0)` | passes (reproduces C220) |
| D2 wrong operator: `s = 1/2` operators on `Y(1,m)` | do not close |
| D3 (as pre-registered): unequal constants break `[L₊,L₋] = 2L_z` | **prediction was wrong**, see below |
| D3a: `[L₊^{(a)}, L₋^{(b)}]F = 2L_z F` for symbolic `a`, `b`, generic `F` | holds: the commutator test is blind to `a ≠ b` |
| D3b: `L₊` at `s = 1/2`, `L₋` at `s = −1/2`: closure ratio | θ-dependent (`−cotθ` against the lowest-weight state of the `L₋` actually used; the first version divided by the wrong function, same conclusion): closure fails |
| D3c: adjointness `⟨G, L₊^{(a)}F⟩ = ⟨L₋^{(b)}G, F⟩` (real test functions vanishing at the poles) | holds for `a = b` (gap `< 1e−15`), fails for `a ≠ b` (gap `> 0.1`; independent pass: `3.58`, `1.79`, `3.58` for `(½,−½)`, `(0,½)`, `(1,0)`) |
| D5 literal step 3 (`m = −1`, `s = 0`) | `χ = C sinθ`: the vector function, not a spinor. Counted as an ordinary check, not a control (skeptic) |

D3 as pre-registered predicted that unequal constants break the commutator relation. The independent pass found, and the main
script then reproduced symbolically, that it does not. D3a–c are post-hoc replacements (`claim.md`, Amendment 1).

## 5. Independent re-implementation (2026-10-14/15)

A subagent was given the operator definitions and a list of tasks T1–T10, no expected answers, and wrote its own code
(`ops.py` and four scripts; the scripts are not archived, the printed outputs are in `independent_pass_outputs.txt`). Its printed
results agree with the main script on:

| Task | Independent pass result | Main script |
|---|---|---|
| T1 commutators, generic `F`, symbolic `s` | all three vanish; Casimir equals `−f″ − cot f′ + (m + s cosθ)²/sin²θ f + s² f` | B1a/B1b |
| T2 highest/lowest weight | `s = 0`: `√sinθ`; `s = ±1/2`: `sin^{1/2}tan^{±1/2}(θ/2)` (= `√2 sin(θ/2)`, `√2 cos(θ/2)`); general `sin^{1/2}tan^{±s}(θ/2)` | A2, A3, B2 |
| T3 ratios | `s = 0`: `−1/tanθ`, `+1/tanθ`; `s = 1/2`: `−1`, `−1`; `s = −1/2`: `+1`, `+1` | A4a, B3b, B6 |
| T4 chain at `s = 0` | `L₋²ψ_↑ = −sin^{−3/2}θ e^{−3iφ/2}`; integral diverges (`× ε → 4π`) | A5a, A5b |
| T5 norms | `s = 0`: `π²` each (also `L₋ψ_↑`); `s = ±1/2`: `4π` each, `N = 1/(2√π)` for the unnormalised `sin^{1/2}tan^s` | A7a, A7b, B3d |
| T6 closure scan | closes only for `s = ±1/2` | B5 scan |
| T7 normalised pair | matches section 2 including the sign; exact residuals vanish after the half-angle reduction | B3 |
| T8 periodicity | `ψ(φ+2π) = −ψ` for both | A8, B3e |
| T9 integer control | `L±Y(1,m) = √2 Y(1,m±1)`, `L²=2` | D1 |
| T10 different constants | commutator vanishes for `a ≠ b`; adjointness and closure discriminate | D3a–c |

Not independently checked: the Condon–Shortley sign convention (given), the C184b identification (B4 uses the repository's saved
doublet), anything beyond double precision. The independent pass also surfaced facts the main script does not cover
(general-`s` closed-form ratios; `⟨ψ_↓, L₋ψ_↑⟩ = 0` at `s = 0`; the next paragraph).

**Exploratory, not pre-registered, not counted as evidence:** for the highest-weight state with `m = j`, whether
`L₋^{2j}ψ_↑ ∝ ψ_↓` with a constant was tested on 21 pairs (`j ∈ {1/2, 1, 3/2}`, `s ∈ {0, ±1/2, ±1, ±3/2}`) against the rule
"`j − |s|` is a non-negative integer". In its first test (relative spread of the ratio below `1e−7`) 19 of 21 agreed.
The two others (`j = 3/2`, `s = ±3/2`) exceeded that tolerance; in a second run on a narrower angle range
(`θ` from 0.3 to `π − 0.3`) they gave `−6` and `+6`, constant to about `1e−10` (for `s = −3/2` sympy did not reduce the
exact ratio to a constant, so that one is numeric only). The likely cause is loss of precision near the poles at high order, which is
my reading and was not tested. With that second run the rule is consistent with all 21 pairs. It is a statement of the form known for spin-weighted
harmonics `[MEMORY]` and has not been checked against a source here.

## 6. Pre-registered predictions

| # | Prediction | Result |
|---|---|---|
| P1 | `s = 0`: solutions `√sinθ`, `L² = 3/4` | holds (A2, A3, A6) |
| P2 | `s = 0`, step 4: ratio `∓cotθ`, chain does not terminate, `L₋²ψ_↑ ∝ sin^{−3/2}θ` non-normalisable | holds (A4a, A5a, A5b) |
| P3 | `s = 0`: `⟨ψ,ψ⟩ = π²`, `⟨L₋ψ_↑,L₋ψ_↑⟩ = π²` | holds (A7a, A7b) |
| P4 | `su(2)` relations for generic `F` and `s` | holds (B1a, B1b) |
| P5 | `s = 1/2`: `sin(θ/2)`, `cos(θ/2)`, closure with modulus-1 constants, `L² = 3/4`, `N = 1/√(2π)` | holds (B3a–d) |
| P6 | equals the C184b doublet, labels reversed | functions agree (B4). Reworded after the skeptic: "labels reversed" and "up to sign" are one convention, not two discrepancies; C184b with its own labels and signs is the Condon–Shortley `s = 1/2` doublet quantised along `−z` (equivalently, the opposite orientation of `φ`). Nothing suggests an error in C184b |
| P7 | closes for `s = ±1/2`, not for `s = 0`; other `s` exploratory | holds; `±1` and `3/2` also do not close (section 3) |
| P8 | antiperiodic at `s = ±1/2` | holds as arithmetic (A8, B3e), but it is built in by the `e^{±iφ/2}` form: it is true in this gauge. The gauge-independent statement is that a rotation by `2π` acts as `−1`; for `s = ±1/2` the half-integer phase can be removed by regular patch gauges (skeptic's check S9), which weakens "double-valued" for the spin-weighted pair |

The first runs had two failures that were not physics: a symbolic-integration problem in B3d (fixed in the code, same claim),
and a wrong pre-registered control, D3 (section 4). The honesty note in `claim.md` stands: P1–P3, P5 and the `s = 1/2`
closure were first seen in a scratch preview, so they are predictions, not blind ones.

## 7. What this does not show

1. It does not show that a multiplet of ordinary, single-valued functions carries the spin-1/2 representation (`C179` stands).
   Both routes give double-valued functions.
2. It does not show that the correspondent's intended fields are the `s = 1/2` pair. It shows what the orbital operators give
   (steps 1–3 and 5 work, step 4 does not) and that one extra term makes all five close.
3. It does not derive where the `−s/sinθ` term comes from. Reading it as the Lie derivative of a spinor along a rotation,
   or as a frame term, is a hypothesis, untested here. The identification with the standard spin-weighted spherical harmonics is recalled
   from memory `[MEMORY]` and is not checked against a source here.
4. It does not bear on `N_gen = 3`, `OB1`, or on `λ` (`FREE_COUPLING_PARAMETER`).
5. The exploratory `j − |s|` rule (section 5) is not part of the result.

## 8. Skeptic concerns (FL step 8a, claim.md + code + output + the McMurry p.144 page, no session history)

Round 1, a context-blind `skeptic` agent (stated for the record: it substitutes for the `reviewer`, per the Independent Review Fallback Policy). It had no shell, so it derived everything by hand and wrote a script `c221_falsify.py`; I ran that script myself: `23/23 PASS` (`python -I`). It did not see the independent re-implementation of section 5. It read McMurry p.144 as an image and reports that the operators match the script's `s = 0` operators term by term and that `[L₊,L₋] = 2L_z` on that page forces `L_z = −i∂_φ`.

| Concern | Response |
|---|---|
| Maths of P1–P5, P7 wrong? | None found. Re-derived by hand; spot checks agree with `run_output.txt` (my run of its script: 23/23) |
| `s = −3/2` pre-registered but not scanned | **Fixed**: added; does not close. Amendment 4 |
| D3b divided by the wrong function | **Fixed** (denominator is now the lowest-weight state of the `L₋` applied); conclusion unchanged (ratio `−cotθ`) |
| D5 counted as a control | **Accepted**: now an ordinary check. Counts are `29/29` and `5/5` |
| About 10 of the 28 main checks cannot fail or are forced (A1, A7c, A8, B3e by definition; A6, B3c, A7b and the agreement half of B3d by algebra; B1a/b blind to `s`; B4, B5c, B6 restatements; D2 cannot pass) | **Accepted.** The checks that discriminate: A2/A3, A4a/b, A5a, B2b/c, B3a, θ-independence in B3b, the unit integrals in B3d, B5a/b, D1, D3c (skeptic counts roughly 15–17). The `29/29` figure is therefore not 29 independent pieces of evidence |
| `zero()` can silently fall back to numeric (one value of `m`, `s`, four angles); the json does not record which path ran | **Accepted limitation.** The symbolic-`m`,`s` statements in B2a/B2b are true by hand derivation (skeptic's and mine in section 2) but the code does not show it |
| A5b integrates a typed-in `sin⁻²θ` | **Accepted**; the integrand was also derived by hand (workings §3) |
| Mirror `θ → π−θ` claim in B5a untested in the script | Accepted; confirmed by the skeptic's script (S3: `L±^{(−s)}[F∘P] = −(L±^{(s)}F)∘P`) |
| "exact symbolic" overstated: the scan, B2c and D3c are numeric | **Fixed in wording** (section 3 says numeric at four angles; the letter says "computed", not "exactly", for these) |
| Estimand promised "what condition on `s`" but the script only samples | **Mitigated**: condition is `s = ±1/2` (skeptic's derivation, run and confirmed); the script alone does not derive it |
| P6 wording (two discrepancies, one convention) | **Fixed** (section 6) |
| P8 "double-valued" is gauge-dependent for `s = ±1/2` | **Accepted, reworded** (section 6, `claim.md` "does not mean" 1 stands for `s = 0`) |
| Kill criterion text says "steps 1–3 and 5 hold" while step 5's norm comparison has nothing to compare at `s = 0` | **Accepted**: at `s = 0` step 5 gives the norms `π²`; the equality `‖L₋ψ_↑‖ = ‖ψ_↓‖` is forced by adjointness and does not support step 4 (section 1 already says so) |
| Status "NEW" holds only inside the project; the `s = 0` failure resembles Pauli's 1939 single-valuedness argument and the `s = 1/2` pair is the standard spin-weight-1/2 / monopole harmonics | **Accepted, unverified**: both are from memory, not checked against a source. The letter calls it a reproduction, not a discovery |
| The independent pass (section 5) was not examined by the skeptic | Accepted: it is same-model-family code, and the skeptic's own hand derivation is now a second line for P1–P5 and P7 |

Results of the skeptic's own tests, all run by me via its script: closure for all real `s` at `j = 1/2` only at `s = ±1/2`; the Casimir is `3/4` for every `s` (so A6/B3c carry no evidence about which `s` is right); `D3c` in closed form `(32π/15)|b − a|`; patch-gauge check S9 (regular for `s = 1/2`, singular for `s = 0`).
No concern touched the core predicate (the orbital route fails at step 4, one `s = ±1/2` term closes it). Verdict stays PROMOTE as a derivation, with the narrower wording above.

## 9. Status

Script, controls, independent pass and skeptic round 1 agree on the mathematics. Wording of P6, P8 and the estimand was narrowed as recorded in sections 6 and 8. Not committed at the time of writing this section. The full test suite had one failure, `tests/test_g21_extended_schur.py::test_more_generators_smaller_commutant`, in code this round did not touch (the working tree has only the untracked C221 folder); it is not investigated here. Correspondence package (letter, workings PDF, Russian translation) is drafted, not sent.
