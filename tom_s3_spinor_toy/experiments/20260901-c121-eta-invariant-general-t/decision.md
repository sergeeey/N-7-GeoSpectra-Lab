# C121 decision -- eta(D^t) closed form CONFIRMED (twice, independently);
the round's own pre-registered kill criterion WAS evaluable and FIRES:
NULL, same underlying reason as round116

**Verdict:** `NULL__ETA_MOD_2_IDENTICAL_ON_EVERY_INTERVAL__NO_SPECTRAL_DISTINCTION_FOR_T_IN_0_1__CLOSED_FORM_P_A_ITSELF_CONFIRMED_REAL`
(replaces the original `NEIGHBOR_COMPARISON_BLOCKED_SUBSTRATE__PRE_REGISTERED_KILL_CRITERION_NOT_YET_EVALUABLE`
-- retracted, FL Step 8a skeptic pass, same day: the round claimed the
decisive computation was too large to attempt; the skeptic completed
it in about 15 lines, independently re-verified below before being
trusted)
**Status:** RESOLVED. Routed toward `null_results/` per this project's
own REJECT convention -- see Kill Analysis.

## Summary

The original draft of this round found a clean closed form,
`P(a) = a(3-4a^2)/6` (`a=3(t-1/2)`), on the base interval `t in (0,1)`,
verified it against a narrow sanity check, and then declared its own
pre-registered decisive question (does `t in (0,1)` show anything
neighboring intervals don't?) "not yet evaluable" -- citing the need
for "spectral-flow-aware machinery" as a "materially larger
undertaking" not attempted under time pressure.

FL Step 8a skeptic (context-blind) found this framing wrong: the
decisive computation is NOT a large undertaking. It is a short, exact,
finite correction -- and the skeptic completed it. **Both of the
skeptic's load-bearing corrections were independently re-derived by
this session before being trusted** (not simply accepted), per this
project's own audit-verification-gate discipline (an agent's
[VERIFIED] is this session's [INFERRED] until re-checked):

1. Directly re-derived, from scratch, that the "naive continuation"
   of the closed form past a spectral crossing silently assigns a
   flipped eigenvalue the WRONG sign contribution (`+1` instead of the
   true `-1` at `s=0`, since `X^0=1` regardless of the sign of `X`) --
   confirmed the correction is exactly `+2*mu(0)` at the first
   crossing, matching the skeptic's claim (`eta(a=2) = P(2)+4 = -1/3`,
   reproduced independently).
2. Directly re-derived that the value AT the crossing point itself
   (`a=3/2`, i.e. `t=1`) is `+1/2`, not the `-1.5` the original script
   reported -- the reported `-1.5` is a one-sided LIMIT approaching
   the crossing from inside `(0,1)`, not the value at the point, which
   differs because the crossing eigenvalue is exactly zero there
   (`sign(0)=0`, not `+1` as naive continuation assigns).

## The general formula (skeptic's derivation, independently confirmed)

For `a` in the interval between the `J`-th and `(J+1)`-th positive
crossings (`n=0,...,J` have flipped sign relative to the base
interval):

```
eta(a) = P(a) + 2 * sum_{n=0}^{J} mu(n),    P(a) = a(3-4a^2)/6,  mu(n)=(n+1)(n+2)
```

**The SAME polynomial `P(a)` appears on every interval, shifted only
by an even integer** (twice the cumulative multiplicity of crossed
modes). Consequences, checked directly:

- `eta mod 2` is IDENTICAL as a function of `a` on every interval --
  there is nothing in `eta(t)`'s own structure that marks `t in (0,1)`
  as different from `t in (1,4/3)`, `t in (-1/3,0)`, etc.
- The pre-registered kill criterion (claim.md: "if the computed eta
  values on the (0,1) interval show no special integrality/quantization
  property not ALSO shared by the neighboring intervals... this
  candidate is NULL for the same underlying reason round116 was")
  **fires exactly as stated.**

## Skeptic response (2026-09-01, FL Step 8a, context-blind pass)

Verdict: **FALSIFIED** on this round's own verdict/status/verification
claims; **CONFIRMED-REAL** on the closed form `P(a)` itself (re-derived
by the skeptic via TWO independent routes -- the Hurwitz-zeta route
this round used, and a fully separate heat-kernel Mellin-transform
route, with matching pole residues and an independent APS-variation-
formula cross-check `dP/da = -2*(a^2-1/4)`, confirmed exactly). Full
response per the project's own Response Matrix:

| Concern | Response |
|---|---|
| The pre-registered kill criterion was NOT actually blocked -- the multi-interval formula is a short, exact, finite computation, completed by the skeptic and independently re-derived by this session (see Summary above) | **Accepted, this is the round's real finding.** Verdict changed from PARTIAL/blocked to NULL, routed to `null_results/`. |
| At the crossing boundary itself (`a=3/2`, `t=1`), the script's reported `-1.5` is a one-sided LIMIT, not the true value (`+1/2`) -- the zero eigenvalue there should contribute `sign(0)=0`, but naive continuation silently assigns it `+1` | **Accepted, independently confirmed** (see Summary above). The "`+-3/2`, half-integer, worth noting" framing in the original decision.md is retracted -- it described a limit, not a value, and the actual half-integer question is convention-dependent (see below), not the clean fact originally claimed. |
| "Independently verified" overstated what was run: the sanity check tested only ONE point, at an INTEGER `q=2` -- sympy's own zeta() may take a different code path for integer arguments, and integer `q` is exactly where the check is LEAST representative of the actual `q=3/2+-a` (generically irrational) regime the result lives in. The check tests transcription (did I copy the formula into code correctly), not the decomposition (the actual load-bearing mathematical step) | **Accepted.** "Independently verified" downgraded to "transcription-checked at one integer point; the decomposition itself was not independently checked in the committed script" (though it WAS independently re-derived by the skeptic via a structurally different method, and by this session again -- see above -- just not by the round's own committed artifact). |
| The abandoned naive heat-kernel numerical check WAS salvageable with the standard fix (fit `eps^2 * Theta(eps)` as a series in `eps^2`, read off the constant term -- exactly the "pole subtraction" the original decision.md named as the fix and then didn't apply, an internal contradiction) | **Accepted as a real process gap** -- premature abandonment, not fixed retroactively in the committed script (the skeptic's independent Mellin-transform re-derivation serves the same verification purpose here, so this is not re-attempted, but named for the record). |
| `claim.md`'s own risk section stated the crossing lattice values wrong (`a=+-7/2,+-11/2` for `n=1,2`; should be `a=+-5/2,+-7/2`) | **Accepted, fixed in claim.md** (additive correction note, original wrong values preserved as historical record per this project's convention). |
| The `+-3/2 -> half-integer, worth noting` claim is convention-fragile: the value AT the point is `+1/2` (not `-3/2`), and the standard APS "reduced eta" `xi=(eta+h)/2` gives `5/4` at that point (`h=2` the kernel dimension there) -- three different conventions give three different answers, none robustly "notable" | **Accepted, retracted from "What survives."** Not re-litigated further; not the round's actual finding. |
| The `P(a)` closed form itself, its oddness, its zero at `a=0`, the Bernoulli-vs-sympy sanity check's own three matching values, `mu(n)=(n+1)(n+2)`, the sign-definiteness domain `\|a\|<3/2` | **CONFIRMED-REAL**, independently re-derived by the skeptic via two separate methods plus a `dP/da` cross-check, unchanged. |

## Kill Analysis (per Anti-Overfitting Gate discipline)

**What was killed:** the specific claim that `eta(D^t)`, computed at
general `t`, would show a quantization/integrality property special to
`t in {0,1}` (the pre-registered hope from C120's own pearl and this
round's claim.md). It does not -- `eta mod 2` is the identical function
of `a` on every interval between crossings; only an even-integer
offset changes, tracking cumulative crossed multiplicity, which is
already fully accounted for by round67/round116's own multiplicity
table. This is, structurally, the SAME finding round116 already made
about the `(n,sigma)` crossing family itself: nothing in this
construction singles out `n=0` (equivalently `t in (0,1)`) from any
other `n`.

**What was NOT killed:**
- The closed form `P(a) = a/2 - (2/3)a^3` itself -- a genuine, new,
  independently-confirmed computation not previously in this project's
  record, reusable if a future round finds a different reason to care
  about it.
- The `dP/da = -2*(a^2-1/4)` identity (APS variation formula,
  independently confirmed) -- a clean, citable relation between the
  eta invariant's derivative and the spectral density, potentially
  useful scaffolding for a future, differently-motivated round.
- `spec(D^{1-t})=-spec(D^t)` (C44) and the multiplicity table
  (round67/round116) -- untouched, cited not re-derived.

**Relaxation Map** (one assumption changed per row, none attempted
this round):

| Assumption relaxed | What it would take | Status |
|---|---|---|
| Look at `eta` itself (not `eta mod 2`) as the invariant | Would require an independent argument for why the even-integer shift between intervals is NOT physically irrelevant (i.e. why absolute `eta`, not just its value mod an even integer, should matter) -- no such argument exists in this project's record | Not attempted; no candidate reason identified |
| Look at the REDUCED eta invariant `xi=(eta+h)/2 mod 1` (the APS-standard quantized quantity, `h`=kernel dimension) instead of raw `eta` | A genuinely different quantity than what this round computed -- `xi` is mod-1, not mod-2, and behaves differently across a crossing (kernel dimension `h` itself jumps). Not computed this round | Named as the most promising un-attempted variant, not pursued under time constraints |
| Full spectral-flow integer (formally, not just the finite correction used here) | round116 already declined this explicitly; this round's finite-correction approach answers the SAME question (does one interval differ from another) without needing the full formal machinery, so this relaxation is likely unnecessary, not merely undone | Superseded by this round's own finite-correction computation |

## What this round DOES establish (survives)

- `eta(D^t)` on `S^3`, general `t`, closed form: `P(a)=a(3-4a^2)/6` on
  the base interval, `P(a)+2*sum_{n<=J}mu(n)` on interval `J`.
- This candidate (structurally odd-in-torsion, radius-independent
  spectral invariant) does NOT distinguish `t in {0,1}` from any other
  crossing pair -- a clean, decisive NULL, not a "could not test"
  result.
- `PARENT_ACTION_GATE.md` F4's "already tried" list should record this
  alongside round116 -- both fail for the identical underlying reason
  (the `(n,sigma)` crossing family has no `n`-dependent structure that
  privileges `n=0`), reached via two different constructions.

## What this round does NOT show

- Does not test the reduced eta invariant `xi=(eta+h)/2 mod 1` --
  genuinely different, not computed, named above as the most promising
  unattempted variant.
- Does not compute `eta(D^t)` on the full `S^3xS^6` background -- `S^3`
  factor only, matching this whole `t`-selection line's established
  scope.
- Does not change N_gen=3's CONDITIONAL status; does not touch S6/
  triality/OB1's PARKED status (this closes one more F4 candidate,
  same as C119/C120, does not itself reopen OB1).
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260901-c121-eta-invariant-general-t/` --
  clean.
- Full pytest suite run before commit: 2524 passed, 4 skipped.
- Skeptic's two load-bearing corrections (the multi-interval formula;
  the true crossing-point value `+1/2`) independently re-derived by
  this session from first principles before being trusted, not merely
  accepted on the skeptic's authority -- both matched exactly.
- Skeptic's own re-derivation of `P(a)` via a structurally different
  method (heat-kernel Mellin transform) plus 3 additional cross-checks
  (pole residues, `dP/da` identity, `f(0,a)` even-coefficient
  vanishing) -- all independently reproduce or are consistent with the
  original Hurwitz-zeta derivation.
