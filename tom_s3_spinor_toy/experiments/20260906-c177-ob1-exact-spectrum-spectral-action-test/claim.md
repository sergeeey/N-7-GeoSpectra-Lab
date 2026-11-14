# C177 — Claim

**Experiment ID:** `20260906-c177-ob1-exact-spectrum-spectral-action-test`
**Parent:** OB1 row A (t-selection). Direct follow-up to C176: an external
reviewer (relayed by the user), reacting to C176's own honest caveat that
its `a_2`/`a_4` formula was BORROWED from a 4D-derived paper (Hanisch-
Pfäffle-Stephan) and applied to `S3`'s n=3 case without a genuine n=3
re-derivation, proposed a cheaper and more direct alternative: skip the
general Seeley-DeWitt/Gilkey heat-kernel machinery entirely and compute
the spectral action `S_f(t,Λ)` directly from `D^t`'s own EXACT, ALREADY-
ESTABLISHED, CLOSED-FORM spectrum on `S3` — no borrowed coefficients, no
dimensional mismatch, just a sum over known eigenvalues. Built per user's
explicit direction ("го дальше по OB1, что ещё можно проверить" + the
external reviewer's detailed proposal).

## Step -5: Zero-Signal Gate

- **Entity:** the exact spectrum of `D^t` on `S3` — `D^t(n,σ) = σ(n+3/2) +
  3(t-1/2)` for `n=0,1,2,...`, `σ=±1`, each `(n,σ)` with multiplicity
  `m_n=(n+1)(n+2)` — **already established in this project**, not derived
  fresh here: the additive-shift form is `[VERIFIED-tool]` in round67/E2
  (`decision.md` lines 22-27: Kostant's cubic torsion element `H` collapses
  to a scalar on `S3` because `dim m=3` leaves only the central volume
  element, calibrated `h_H=3` from the established `n=0` eigenvalue `3/2`);
  the multiplicity `m_n=(n+1)(n+2)` (per sign) is `[VERIFIED-tool]` in the
  SAME round (`claim.md` line 73, cross-checked against G7's independent
  KK-spectrum computation, `g7_kk_spectrum.py`).
- **Falsifiable predicate:** for the truncated spectral action `S_f(t,Λ) =
  Σ_{n,σ} m_n · f(D^t(n,σ)²/Λ²)`, computed EXACTLY (no heat-kernel
  approximation, no borrowed coefficients), does `argmin_t S_f(t,Λ)` sit
  at `t=1/2` ROBUSTLY across a pre-registered family of admissible cutoff
  functions `f` and a range of `Λ`, or at `t=0,1`, or does it depend on
  the choice of `f`/`Λ` (making the "selector" regulator-dependent, not
  geometric)?
- **Measurable outcome:** (a) numeric sweep of `S_f(t,Λ)` over `t∈[-1,2]`
  for 3 pre-registered `f`'s and several `Λ` values, report `argmin`; (b)
  an analytic proof that `S_f(x)=S_f(-x)` where `x=3(t-1/2)` (so `t=1/2`
  is ALWAYS a critical point, for any `f`, by a multiplicity-symmetry
  argument — not assumed, derived below); (c) the sign of `S_f''(0)` —
  the quantity that actually decides min-vs-max at `t=1/2` — computed
  both symbolically (for the two smooth `f`'s) and numerically (all
  three), across the same `Λ` range as (a), checked for INTERNAL
  CONSISTENCY against (a)'s own `argmin` (a contradiction between the two
  would signal a bug, not a finding).

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Does a specific, exactly-defined function
`S_f(t,Λ)` (built from an already-established closed-form spectrum) have
a specific mathematical property (minimum location) for specific,
pre-registered choices of `f` and `Λ` — not causal, no estimand canvas
beyond the falsifiable predicate above.

## Honest scope limitation, stated BEFORE computing (not after)

1. This tests **3 specific, pre-registered cutoff functions**, not "all
   admissible `f`." A genuine universal theorem ("no cutoff function in
   class X can select `t=0,1`") would require bounding `S_f''(0)`'s sign
   uniformly over an entire function space — this round does NOT attempt
   that; it reports representative evidence from 3 functions chosen for
   qualitatively different tail behavior (exponential, Gaussian, compactly
   supported), not an exhaustive proof.
2. The analytic evenness proof `S_f(x)=S_f(-x)` (Step -5(b)) is genuinely
   general (holds for ANY `f`, proven from the multiplicity structure
   alone) — but the SIGN of `S_f''(0)` is not general; it must be checked
   per-`f`, per-`Λ`, which is exactly what this round does.
3. Numeric sums are truncated at a finite mode number `N`; each run
   reports the truncation residual (last-term magnitude relative to the
   partial sum) explicitly, per this project's own Explicit Truncation
   Marker convention — a silently-truncated sum is not evidence.
4. **This round is also an indirect check on C176's own skeptic-pass item
   5** (which argued the `t=1/2`-preferred verdict is "dimension-robust"
   because it depends only on the SIGN structure between `T_0²` and `R`
   terms, not the exact n=4-vs-n=3 prefactor). If THIS round's
   exact-n=3-spectrum calculation agrees with C176's borrowed-n=4-formula
   calculation, that corroborates the skeptic's dismissal. If they
   disagree, that would falsify the skeptic's item-5 dismissal and mean
   the dimension mismatch mattered after all — worth stating explicitly
   before running, so neither outcome can later be described as expected.

## Kill-criterion table (frozen before running the script)

| Verdict | Condition |
|---|---|
| `EXACT-SELECTOR-CONFIRMED` | `argmin_t S_f(t,Λ) ∈ {0,1}` (not `1/2`) for ALL 3 pre-registered `f`'s, across the full pre-registered `Λ` range, with `S_f''(0)<0` (confirming `t=1/2` is a local MAX, consistent with the numeric argmin) |
| `EXACT-SELECTOR-DIES-AT-HALF` | `argmin_t S_f(t,Λ) = 1/2` for ALL 3 `f`'s across the full `Λ` range, with `S_f''(0)>0` (local MIN at `t=1/2`, consistent with C176's borrowed-formula result) |
| `REGULATOR-DEPENDENT` | The verdict (min at `1/2` vs `0,1`) FLIPS depending on which `f` or which `Λ` is used — the "selector" is not geometric/universal, it is an artifact of the chosen cutoff. This is the single most informative possible outcome: it would kill the entire "spectral action selects t" program, not just one formula. |
| `INTERNAL-INCONSISTENCY` | The numeric `argmin` (Step -5a) and the analytic `S_f''(0)` sign (Step -5c) disagree with each other for the SAME `f,Λ` — signals a bug in the computation, not a physics finding; must be fixed before any verdict is reported. |

**Pre-registered expectation (written BEFORE running the script):** given
that C176's borrowed-n=4-formula calculation already found `t=1/2`
preferred, and that the SAME qualitative mechanism (a positive coefficient
on the torsion-squared-like term, here appearing via the `+8a_n²/Λ⁴ f''`
term dominating at large `Λ`) is structurally present in the exact-n=3
spectrum too, the a priori expectation is `EXACT-SELECTOR-DIES-AT-HALF`,
again the "boring", already-anticipated outcome — NOT `CONFIRMED`. This
also means the MORE informative possible finding would be
`REGULATOR-DEPENDENT` (a genuine surprise) or a disagreement with C176
(which would matter for evaluating the skeptic's own item-5 dismissal),
not `CONFIRMED`.

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** the spectrum formula and multiplicity are this
  project's own already-`[VERIFIED-tool]` results (round67/E2, G7) —
  reused via `importlib`, not re-derived from scratch and not sourced
  from an external paper this time (no new literature dependency for
  this round, unlike C176).
- **Novelty Check:** `grep`-confirmed via the project's own pre-check
  hook that no existing `null_results/INDEX.md` entry duplicates this —
  `G38-S2` minimizes over the bundle Chern class `c₃` on `S6` (a
  different variable entirely, not `t` on `S3`); `META-C1` is the
  unrelated `λ`-dimensional-obstruction chain; `C137-P3Condensate` is the
  fermion-condensate mechanism, not spectral action. C176 itself (this
  round's own direct predecessor) used a BORROWED heat-kernel formula, not
  the exact spectrum — this round's method is genuinely different, not a
  restatement.

## What this does NOT mean (pre-registered)

1. Does NOT, under any outcome, prove this is THE physically correct
   selection principle for this project's actual 13D construction — only
   that the exact `S3`-restricted spectral action, for 3 specific cutoffs,
   has this property.
2. Does NOT resolve row B (kernel multiplicity=2) or the D/E tension
   (`ASSUMPTIONS_MATRIX.md`) under any outcome.
3. Does NOT change `N_gen=3`'s CONDITIONAL status regardless of outcome.
4. Even `REGULATOR-DEPENDENT` does NOT prove no universal selector could
   ever exist — only that these 3 particular cutoffs disagree; a genuine
   uniform theorem over a full function class remains a separate, larger
   undertaking (see scope limitation 1 above).
