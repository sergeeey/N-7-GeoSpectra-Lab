# C177 — Decision

**Date:** 2026-09-06
**Verdict:** `EXACT-SELECTOR-DIES-AT-HALF`. `[VERIFIED-tool]`. Robust across
ALL 3 pre-registered cutoff functions × ALL 5 pre-registered `Λ` values
(15/15 combinations): `argmin_t S_f(t,Λ) = 1/2` and `S_f''(0)>0` in every
single case, `0/15` showed `REGULATOR-DEPENDENT` behavior. Matches this
round's own pre-registered expectation exactly.

---

## 0. Summary

Computed the spectral action `S_f(t,Λ) = Σ_{n,σ} m(n)·f(D^t(n,σ)²/Λ²)`
directly from `D^t`'s own EXACT, already-established closed-form spectrum
on `S3` (`D^t(n,σ)=σ(n+3/2)+3(t-1/2)`, `m(n)=(n+1)(n+2)` — both
`[VERIFIED-tool]` in round67/E2 and G7, reused not re-derived) — no
borrowed heat-kernel coefficients, no n=4-vs-n=3 dimensional mismatch
(the honest caveat that limited C176). Three qualitatively different
cutoffs (`f1=e^{-u}`, `f2=e^{-u²}`, `f3`=smooth COMPACTLY-supported bump)
across five `Λ` values (3, 5, 10, 20, 50):

| Cutoff | Λ range tested | `argmin_t` | `S_f''(0)` sign |
|---|---|---|---|
| `f1=e^{-u}` | 3–50 | `1/2`, all 5 | `+`, all 5 |
| `f2=e^{-u²}` | 3–50 | `1/2`, all 5 | `+`, all 5 |
| `f3` compact bump | 3–50 | `1/2`, all 5 | `+`, all 5 |

**Net conclusion:** the exact-spectrum spectral action, for every cutoff
and scale tested, prefers `t=1/2` (Levi-Civita, torsion-free) over
`t=0,1` — the same qualitative answer C176 found with a borrowed 4D
formula, now obtained from the genuinely correct n=3 object, with zero
dimensional-mismatch caveat.

---

## 1. A genuine bug found mid-round, fixed, and reported (not hidden)

**First run of the script returned `INTERNAL-INCONSISTENCY`** (this
round's own pre-registered kill-criterion for exactly this situation —
see claim.md's kill-criterion table). Diagnosed directly: the
finite-difference cross-check of `S_f''(0)` steps `t` directly, while the
hand-derived closed-form formula (module docstring) was derived and
documented in `x=3(t-1/2)`. Since `dx/dt=3` (constant, affine), `d²/dt² =
9·d²/dx²` — the two methods differed by EXACTLY a factor of 9 (verified:
`95.7125/10.6347=9.0000...`, `159.5208/17.7245=9.0000...`, same ratio at
every `Λ` tested) — a units mismatch in this round's own verification
code, not a physics error. **Fixed** by converting the closed-form value
to `d²/dt²` (`× 9`) before comparison; re-ran, `agree=True` at every
`(cutoff,Λ)` combination.

A SECOND, independent issue surfaced in the same first run: the sympy
mechanical cross-check (Step 5, entirely separate code path from Step 4's
hand-derivation) gave a NEGATIVE second derivative at `Λ=10` while every
other method gave positive — traced to severe under-truncation
(`n_max_symbolic=6` fixed regardless of `Λ`; at `Λ=10` the n=6 term still
carries `exp(-0.5625)≈0.57` of its weight, nowhere near converged).
**Fixed** by scaling `n_max_symbolic` with `Λ` (`min(60, ⌈6Λ⌉)`); re-ran,
now matches the closed-form value to 12 significant figures at both
`Λ=5` (`17.724538509055154` vs `17.7245385090551...`) and `Λ=10`
(`35.449077018110124` vs `35.449077018110316`) — an INDEPENDENT,
mechanical (sympy `diff`, no shared code with the hand-derivation)
confirmation of the closed-form `S_f''(0)` formula stated in the module
docstring.

Both fixes are cheap, understood, and verified — neither touches the
actual physics conclusion (both were bugs in the VERIFICATION harness,
not the spectral-action computation itself, which used the correct
spectrum/multiplicity throughout both runs).

---

## 2. Pre-registration check (per this project's own discipline)

Claim.md's own pre-registered expectation: *"the a priori expectation is
`EXACT-SELECTOR-DIES-AT-HALF`, again the boring, already-anticipated
outcome — NOT `CONFIRMED`."* **Confirmed exactly.** The MORE informative
alternative outcomes named in advance (`REGULATOR-DEPENDENT`, or a
disagreement with C176) did NOT occur — `0/15` combinations showed
regulator-dependence, and the exact-spectrum result AGREES with C176's
borrowed-formula result.

**Direct bearing on C176's own skeptic pass (item 5):** C176's skeptic
found claim.md's "dimension-independent derivation" framing technically
imprecise (n=4-vs-n=3 numeric prefactors genuinely differ) but argued the
verdict survives because it depends only on the dimension-robust SIGN
structure. This round is the empirical test of that argument, run on the
ACTUAL n=3 object rather than a borrowed n=4 formula — **and it
corroborates the skeptic's dismissal**: the sign is the same, the
verdict is the same. This does not retroactively make C176's borrowed
formula "correct" (it remains a legitimate honest caveat that it was
borrowed), but it does mean the caveat did not, in fact, change the
answer for this specific question.

---

## 3. Kill Analysis

**What this round kills:** the hope that a SIMPLE, standard, physically
reasonable spectral-action regulator (exponential, Gaussian, or a smooth
compactly-supported cutoff), applied to the EXACT, dimensionally-correct
n=3 spectrum of `D^t` on `S3`, delivers a `t=0,1` selector. It does not,
for any of 3 qualitatively different regulators across a 15x range of
cutoff scales `Λ`.

**What this round does NOT kill:**
1. A genuinely DIFFERENT action functional — not a cutoff/regularization
   of the SAME trace, but a structurally different physical principle
   (e.g. one where the torsion-squared term enters with the OPPOSITE
   sign, which is not what the exact `D^t` spectrum's own structure
   produces here) — untested, and there is no candidate for one inside
   this project's current content.
2. A genuine uniform theorem over an ENTIRE function class of cutoffs —
   this round tested 3 representative functions, not an exhaustive
   family (see claim.md's own scope limitation 1). A pathological or
   highly oscillatory `f` outside this pre-registered family is not
   covered.
3. `N_gen=3`'s CONDITIONAL status, OB1's PARKED-vs-OPEN status, row B, or
   the D/E tension — all unaffected; this closes one more specific
   candidate mechanism inside the "static/dynamical selection" branch of
   `ASSUMPTIONS_MATRIX.md` row A, joining C137 (condensate) and C176
   (borrowed spectral action) as checked-and-negative, and now doing so
   WITHOUT C176's dimensional-mismatch caveat.

**Relaxation Map:** the honest next step, if this specific line (spectral
action as a `t`-selector) is pursued further, is NOT to search for a
4th regulator hoping for a different answer (that would be exactly the
"keep trying cutoffs until one works" pattern P3/`REGULATOR-DEPENDENT`
was designed to catch, and this round already found 3/3 agree) — it is
to ask whether ANY physically-motivated action (not merely a
regularization choice) could carry the OPPOSITE sign on the
torsion-squared-like term. No such candidate exists in this project's
current content; this is a larger, separate undertaking, not attempted
here.

---

## 4. What this does NOT mean

1. Does NOT prove no physically-motivated selection principle for `t`
   can exist — only that 3 specific, standard spectral-action regulators
   applied to the exact `S3` spectrum do not supply one.
2. Does NOT change `N_gen=3`'s CONDITIONAL status.
3. Does NOT resolve row B or the D/E tension.
4. Does NOT retroactively validate C176's borrowed 4D formula as a
   general method — it validates that, FOR THIS SPECIFIC QUESTION, the
   borrowed formula happened to give the same answer as the correct
   object. A different question (e.g. the exact numeric VALUE of `a_4`,
   not just the sign of its second derivative) might still differ
   between the two methods — not tested here.

---

## 5. Floor–Ceiling / verification substrate note

This is an exact symbolic/numeric computation, not a statistical
estimate with a fitted pass/fail threshold — so the usual "could a
no-mechanism null model beat the criterion" concern does not apply the
same way it would to a statistical claim. Stated with explicit numbers
per this project's own Floor-Ceiling discipline anyway, for the specific
quantity this round's verdict actually rests on, `S_f''(0)` at
`(f1, Λ=5)`:

- **FLOOR (mechanism removed):** if the torsion-shift `x=3(t-1/2)` is
  artificially zeroed out (no `t`-dependence at all — a construction
  with NO mechanism), `S_f''(0) ≡ 0` identically, by construction (there
  is nothing left to differentiate with respect to `t`). This is the
  trivial value ANY no-mechanism construction gives — the observed value
  must clear this floor by a wide, non-marginal margin for the sign to
  mean anything.
- **OBSERVED:** `S_f''(0) [d²/dt²] = 159.5208` (finite-difference on the
  actual truncated spectral sum, `n_max=40`).
- **CEILING (privileged/exact access):** the fully independent sympy
  mechanical symbolic differentiation (Step 5, no code shared with the
  finite-difference or the hand-derived closed form), `n_max_symbolic=30`
  (converged, see §1's fix): `9 × 17.724538509055154 = 159.520846581...`.
- **Efficiency `= (observed − floor)/(ceiling − floor) = 159.5208/159.5208
  ≈ 1.000`** — the observed value sits essentially exactly AT the
  privileged/exact value, clearing the floor (0) by the full margin. This
  is the expected outcome for an exact computation cross-validated 3
  independent ways (§1) — not a statistical estimate with room for the
  observed value to fall short of ceiling, so `efficiency≈1` here signals
  "the numeric computation is correct," not "the world is at its limit"
  (the usual interpretation of `efficiency≈1` for a fitted/statistical
  claim, per this project's own Floor-Ceiling documentation — the
  distinction matters and is stated explicitly so this isn't misread as
  the same kind of result).

The general evenness proof `S_f(x)=S_f(-x)` (from multiplicity symmetry
alone) was additionally verified numerically to `<1e-9` relative
difference at every one of 4 spot-check offsets, for all 15
`(cutoff,Λ)` combinations (`all_even_to_1e-9=True` everywhere). Truncation
residuals reported per this project's Explicit Truncation Marker
convention: max residual ratio across all runs was `6.3e-28` (f1, Λ=50)
— several orders below any threshold of concern; `0.0` exactly for most
combinations (many terms underflow to exact zero in float64 well before
`n_max`). READY, no blocked-infrastructure issue.

---

## 6. A minor, non-alarming texture worth noting (not a finding)

`f3` (compact cutoff)'s `S_f''(0)` magnitude does NOT vary monotonically
with `Λ` the way `f1`/`f2` do (`51.8, 504.4, 198.9, 571.7, 1414.9` at
`Λ=3,5,10,20,50` respectively) — expected, since a hard-edged transition
band interacts with the DISCRETE mode spacing differently as `Λ` changes
(how many modes fall inside vs. outside the transition region is not a
smooth function of `Λ`). The SIGN is consistently positive throughout,
which is the only thing this round's verdict depends on — flagged here
for completeness, not treated as informative on its own.

---

## 7. Independent skeptic pass (Step 8a) — RUN, verdict `CONFIRMED-REAL`

Run context-blind per this project's Context Asymmetry Rule: given ONLY
`claim.md`, the script, and `results_c177.json` — explicitly denied both
this `decision.md` AND C176's own `decision.md` — plus told it could
independently read/run round67/E2, G7, and C176's `claim.md`/results to
check sourced facts. It ran 5 falsification attempts, wrote its own
from-scratch hand re-derivation of both the evenness proof and the
`S_f''(0)` closed form (not just reading the code), and independently
spot-checked one numeric value by hand.

**Overall verdict: `CONFIRMED-REAL`, scope-limited exactly as claim.md
itself already limits it** (3 specific cutoffs, 5 specific `Λ`, no claim
of uniformity over an admissible-function class). Per this project's
Response Matrix:

| # | Skeptic's attack | Outcome | Response |
|---|---|---|---|
| 1 | Is the spectrum/multiplicity formula correctly sourced from round67/G7? | **Not broken.** Independently read round67's `claim.md` line 33 + `e2_s3_torsion_deformation.py` step 4, confirmed `D^t(n,σ)=σ(n+3/2)+(t-1/2)·h_H`, `h_H=3`. Noted the multiplicity `(n+1)(n+2)` is a standard textbook S³ Dirac result (cites Bär 1996) and is directly stated in round67's own `claim.md` line 73, not actually computed inside G7 (G7 is cited for the eigenvalue ladder itself) — a minor sourcing-precision correction to this round's own claim.md wording, not a factual error. | **Accepted as a small wording correction** — claim.md's phrase "cross-checked against G7" should be read as "corroborated by the same `(n+3/2)` convention appearing in G7's independent KK computation," not "G7 derives the multiplicity." No effect on the verdict. |
| 2 | Does the evenness proof `S_f(x)=S_f(-x)` actually hold, including edge cases (`n=0`, `Λ→0`)? | **Not broken.** Independently re-derived from scratch: the σ↔-σ swap exchanges the two arguments of `g(x)=f((a+x)²/L²)+f((a-x)²/L²)` while leaving the sum invariant, given equal per-sign multiplicity — holds for every `n` including `n=0`, and for any `Λ>0` (no `Λ→0` limit is taken anywhere in this round). | **Dismissed as not breaking anything** — independent proof matches. |
| 3 | Is the closed-form `S_f''(0)` formula actually the correct second derivative? | **Not broken.** Independently differentiated `g(x)` twice from scratch and got `g''(0)=(4/L²)f'(u₀)+(8a²/L⁴)f''(u₀)` — the exact formula in the module docstring, including recognizing the same `dx/dt=3` conversion factor this round's own §1 already caught as a bug in the verification harness (not the math). | **Dismissed** — independent, from-scratch derivation confirms the docstring formula. |
| 4 | Is the numeric computation trustworthy (truncation, hidden shared-bug risk across the 3 cross-checks, pre-registration order)? | **Mostly not broken; one genuine gap named.** Truncation residuals confirmed adequate at every `Λ`. The sympy cross-check confirmed genuinely independent (raw, unsimplified `sp.diff`, no shared code path) — agreement across 3 methods is real corroboration, not a shared bug. **Could NOT independently verify, from what it was given, that the 3 cutoffs were chosen BEFORE running the script** (no git history in its read set) — flagged as a weak downgrade rather than assumed innocent. | **Resolved, not just accepted:** checked filesystem timestamps directly (not available to the skeptic) — `claim.md` (`20:00:09`) predates the script's `c177_...py` (`20:03:20`, reflecting the LAST edit including the two bug fixes in §1) and `results_c177.json` (`20:03:32`). The two mid-round edits fixed a units-conversion bug and a truncation bug in the VERIFICATION code — neither added, removed, nor altered which 3 cutoff functions were tested (`f1`,`f2`,`f3` were present in the original script draft, unchanged since). No cherry-picking occurred. |
| 5 | Is "argmin of a regularized trace over an unbounded discrete spectrum" even conceptually well-defined? | **Not broken.** Confirmed this is standard Connes spectral-action calculus (a cutoff function applied to a self-adjoint operator's spectrum, summed with multiplicity) — no `Λ→∞` limit is taken in this round (each `Λ` is evaluated separately, all sums converge absolutely), so no divergence/ill-definedness concern applies. | **Dismissed** — no conceptual confusion found. |

**Net effect on the round's own verdict:** unchanged and now stronger —
`EXACT-SELECTOR-DIES-AT-HALF` survives 5 independent, context-blind
attacks (3 of which involved the skeptic performing its OWN from-scratch
re-derivations rather than trusting this round's code), with the single
named gap (pre-registration timing) resolved by an independent
filesystem-timestamp check rather than left open. No FALSIFIED concerns;
no true-kill condition reached.

---

## 8. Status

`experiments/20260906-c177-ob1-exact-spectrum-spectral-action-test/` —
DONE, INCLUDING independent skeptic pass. Verdict
`EXACT-SELECTOR-DIES-AT-HALF`, now `[VERIFIED-tool]` at the original
computation, an internal 3-way cross-check (§1), AND an independent
context-blind skeptic re-derivation (§7) — four independent confirmations
of the same sign, the strongest evidence status any single round in this
project's `t`-selection line has reached. Corroborates C176's own result
via a dimensionally correct, non-borrowed method and directly confirms
C176's skeptic's own item-5 dismissal (sign-structure argument). Two
genuine bugs found and fixed mid-round, both in verification code (not
the physics), both reported honestly (§1); the skeptic independently
re-derived the same formulas from scratch and got the same answer,
which is a stronger check than re-reading the fix. Registry
(`OPEN_BLOCKERS.md` OB1 row, `pearl_registry/INDEX.md`) not yet updated
pending user confirmation of scope. No git operations run for this
update.

**UPDATE (2026-09-06, registry pass):** `OPEN_BLOCKERS.md` OB13 updated
with a cross-reference this round's own claim.md did not originally make:
the proven evenness `S_f(x)=S_f(-x)` (§-5b in claim.md) places this round
squarely in OB13's own even-functional registry category. Per OB13's
corrected understanding (C123), an even functional cannot break the
residual `t=0`-vs-`t=1` degeneracy but COULD select `{0,1}` as a set (as
round99's own even curvature toy did); this round's exact-spectrum
`S_f(t,Λ)` does not even achieve that weaker outcome, confirming the same
single-well shape C176's `a_2(t)` found — see OB13 for the full
comparison. `ASSUMPTIONS_MATRIX.md` row A updated to list this round
among tried-and-negative candidate mechanisms.
