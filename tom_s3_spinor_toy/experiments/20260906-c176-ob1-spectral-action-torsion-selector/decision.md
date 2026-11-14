# C176 — Decision

**Date:** 2026-09-06
**Verdict:** `SPECTRAL-SELECTOR-DIES-AT-HALF`. `[VERIFIED-tool]`. Matches
this round's own pre-registered expectation (written in claim.md BEFORE
running the script) — the leading-order spectral-action term prefers
`t=1/2` (Levi-Civita), not `t=0,1`. A genuine, unanticipated side-finding
in the subleading term is reported honestly, not smoothed over.

---

## 0. Summary

Computed the Seeley-DeWitt coefficients `a_2(t)` (in full) and a
dimension-general PARTIAL `a_4(t)` for `S³`'s Cartan-Schouten torsion
family `D_S3(t)`, using Hanisch-Pfäffle-Stephan 2009's own cited,
torsion-corrected formula (arXiv:0911.5074, eq. 3/6/7 — read directly
from the paper this session). Reused round67's generators and round99's
own verified curvature formula `R^t(Zi,Zj)Zk=t(t-1)[[Zi,Zj],Zk]`,
extended from one illustrative component (round99) to the FULL Riemann
tensor (all 27 components), giving:

| Quantity | Formula (computed, not assumed) | Shape |
|---|---|---|
| `T_0^2(t)` (torsion-squared) | `4(2t-1)²` | upward parabola: **0 at t=1/2, max at t=0,1** |
| `‖Riem(t)‖²` | `192·t²(t-1)²` | downward-then-up: **0 at t=0,1, max at t=1/2** (matches round99's single-component check exactly) |
| `‖Ric(t)‖²` | `192·t²(t-1)²` | identical to `‖Riem‖²` (Einstein space, `Ric∝g`, confirmed) |

**`a_2(t) = (9(2t-1)² - 1)/(8π²)`** (using `R_LC=6`, this project's own
independently-anchored value — see §2): minimum EXACTLY at `t=1/2`
(value `-1/(8π²)≈-0.0127`), larger at `t=0,1` (`1/π²≈0.101`). Since
`a_2`'s entire `t`-dependence comes from the `+9/2·T_0²(t)` term (the
paper's own fixed `R` does not vary with `t` in this construction — see
§1), and `T_0²(t)` is a positive-coefficient upward parabola zero at
`t=1/2`, **`a_2` is structurally forced to prefer `t=1/2`, not `t=0,1`,
given the sign of the coefficient in the cited formula.**

**`a_4_partial(t)`** (dimension-general terms only — `R²,‖Ric‖²,‖Riem‖²,
R·T_0²,(T_0²)²`, explicitly excluding the `n=4`-specific `Ω_ij` piece):
`(81(2t-1)⁴-18(2t-1)²+1)/(32π²)` — has a LOCAL MAXIMUM at `t=1/2` and
MINIMA at `t=1/3` and `t=2/3` — **not at `t=0,1`, an unanticipated third
location.**

**Net conclusion:** since `a_2` is the `Λ²`-weighted, dominant term as
`Λ→∞` (the regime that defines the spectral-action expansion at all),
and `a_2` alone already picks `t=1/2` over `t=0,1` cleanly and by a
sizeable margin (`1/π²` vs `-1/(8π²)`, i.e. `t=0,1` is worse by roughly
`9/(8π²)`, not a close call), **the spectral action, as constructed from
this specific, cited, torsion-corrected formula, does NOT select `t=0,1`
— it selects the Levi-Civita connection, the answer that gives ZERO
zero-modes and was already known to be uninteresting.**

---

## 1. A real convention discrepancy found, diagnosed, and resolved (not glossed over)

Before trusting the above, this round's own by-hand derivation of a
"scalar curvature of `∇^t`" (contracting the fresh Riemann tensor as
`Ric(j,l)=Σ_i Riem(i,j,i,l)`) gave `24t²-24t`, while round111's own
already-committed `Scal(t)=24t(1-t)` (i.e. `-24t²+24t`) is EXACTLY THE
NEGATIVE. Diagnosed directly, not assumed: round111's own script
(`e34_scalar_curvature_action.py`, re-read this session) contracts
`Ricci(a,b)=Σ_c⟨R(Zc,Za)Zb,Zc⟩` — **1st-and-4th-index contraction** — vs
this round's own **1st-and-3rd-index contraction**. Using the Riemann
tensor's own antisymmetry in its last two indices (verified: `Riem(i,j,k,
l)=4t(t-1)(δik δjl-δjk δil)`, antisymmetric in `(k,l)` and in `(i,j)`
both), the two contractions are provably exact negatives of each other —
**not a bug in either script, a genuine, well-known sign-convention choice
for defining Ricci from a general (non-Levi-Civita, torsion-carrying)
curvature tensor.**

**Resolution:** round111's own convention is the one anchored to an
INDEPENDENT, textbook-standard formula (`Ric_LC(X,X)=-(1/4)B(X,X)`, the
Killing form for a compact Lie group), cross-checked in round111's own
script against the general `R^t`-derived formula at `t=1/2` and found to
AGREE (`cross_check_ok=True`, re-verified directly this session by
re-running that script). Round111's `Scal_LC=6` (a concrete, POSITIVE
number) also matches Hanisch-Pfäffle-Stephan's own explicitly stated sign
convention ("spheres have positive curvature ... `R=12` for the
4-dimensional sphere"). **This round's own `a_2`/`a_4` computation
therefore uses `R_LC=6` (round111's own, independently-anchored value),
not this round's own ad hoc contraction** — the discrepancy is fully
reconciled, not left as an open contradiction. This round's OWN
Riemann/Ricci-NORM computations (`‖Riem‖²`, `‖Ric‖²`) are unaffected by
this sign ambiguity (a squared norm cannot see an overall sign flip),
only the SIGNED `scal_from_riemann(t)` diagnostic quantity was affected,
and that quantity is not used anywhere in the actual `a_2`/`a_4` formulas.

---

## 2. Pre-registration check (per this project's own discipline)

Claim.md's own "pre-registered expectation," written BEFORE running the
script: *"given `T_0²(t)∝(2t-1)²`... the naive expectation is that `a_2(t)`
is MINIMIZED at `t=1/2`, not `t=0,1`... `SPECTRAL-SELECTOR-DIES-AT-HALF`
is the a priori MORE LIKELY outcome."* **Confirmed exactly, by direct
computation, not merely by the hand-derivation that motivated writing it
down.** This round's own prediction survived contact with the actual
symbolic calculation — a clean instance of "prediction before data" done
correctly (per this project's own discipline and the external reviewer's
own explicit request).

---

## 3. Kill Analysis

**What this round kills:** the specific hope that Hanisch-Pfäffle-
Stephan's own torsion-corrected spectral action formula, applied
literally to `S³`'s Cartan-Schouten family, supplies a genuine `t=0,1`
selector via its leading (`a_2`) term. It does not — the coefficient sign
on `T_0²` in the cited formula structurally forces the opposite
preference.

**What this round does NOT kill:**
1. The GENERAL IDEA that SOME spectral/gravitational action could select
   `t=0,1` — only this SPECIFIC formula (4D-derived, applied with `a_2`
   as the leading term) has been checked. A different action (a genuinely
   9D/13D construction for this project's own actual product-manifold
   spectral triple, not the 4D formula borrowed here) remains untested.
2. C137's own, separately-established conclusion (no dynamically-derived
   fermion condensate is available) — untouched, a different mechanism.
3. `N_gen=3`'s CONDITIONAL status, OB1's PARKED status, or any other
   `ASSUMPTIONS_MATRIX.md` row — all unaffected; this is one more
   specific, concrete negative finding added to the existing list.

**Relaxation Map:** the honest next step, if this line is pursued further,
is NOT to look for a different sign convention that "fixes" this result
(that would be exactly the parameter-tuning the third pre-registered
outcome warns against) — it is to ask whether the ACTUAL 9D/13D spectral
action this project's own construction would use (not a borrowed 4D
formula) has a structurally different coefficient on the analogous
torsion-squared term, which requires redoing the Seeley-DeWitt
computation's `n`-dependent pieces (the `Ω_ij`/Clifford-trace part this
round explicitly excluded) for the actual dimension — a substantially
bigger undertaking than this round, not attempted here.

---

## 4. Side finding (Pearl Gate) — `a_4_partial`'s own minima at t=1/3, 2/3

`a_4_partial`'s minima at `t=1/3,2/3` (not `0,1,1/2`) are a genuinely new,
unanticipated location this round did not predict and does not currently
have an interpretation for. Since `a_4` is subleading (`Λ⁰`-weighted) and
does not override `a_2`'s own `t=1/2` preference at leading order, this
does NOT change the round's own verdict — but `t=1/3,2/3` appearing at
all, from a formula that had no `t=1/3` built into it anywhere, is a
concrete, falsifiable, currently-uninterpreted fact worth flagging for
`pearl_registry/INDEX.md` (not done here, pending user confirmation of
scope) in case a future round's own different context (e.g. a `ℤ_3`-
related construction, given this project's own extensive `ℤ_3`/triality
work this same session, C167-C174) makes `t=1/3,2/3` meaningful.

---

## 5. What this does NOT mean

1. Does NOT prove no spectral/gravitational action anywhere can select
   `t=0,1` — only that this ONE, specific, cited, literally-4D-derived
   formula's leading term does not.
2. Does NOT change `N_gen=3`'s CONDITIONAL status.
3. Does NOT resolve row B (kernel multiplicity=2) or the D/E tension.
4. The `a_4`-partial computation is NOT a full `a_4` (the `Ω_ij`/Cl(3)
   trace piece is excluded, per claim.md's own pre-registered scope
   limit) — its own minima at `t=1/3,2/3` should not be over-interpreted
   as a complete answer for the subleading term.

---

## 6. Floor–Ceiling / verification substrate note

This is an exact symbolic computation (sympy), not a statistical estimate
— the "floor" analogue is round99's own already-verified single-component
check (which this round's full-tensor computation exactly reproduces,
`matches_round99_R121=True`), and the "ceiling" analogue is the
independent cross-check against round111's own textbook-anchored
`Scal_LC=6` (which resolved, not merely noted, the sign discrepancy in
§1). Both ends check out. READY, no blocked-infrastructure issue.

---

## 7. Independent skeptic pass (Step 8a) — RUN, verdict `CONFIRMED-REAL`

Run context-blind per this project's Context Asymmetry Rule: the skeptic
was given ONLY `claim.md`, the script, and `results_c176.json` — explicitly
denied access to this `decision.md` (i.e. denied §§1-6 above, this
author's own reasoning/framing/verdict), and told it could independently
read/run any file the script itself imports or cites (round67/round99/
round111's scripts) to check facts. It attempted 5 falsification attacks.

**Overall verdict: `CONFIRMED-REAL`.** None of the 5 attacks broke the
central claim (`SPECTRAL-SELECTOR-DIES-AT-HALF`). Per this project's
Response Matrix, each concern gets an explicit response below rather than
being silently accepted or waved away:

| # | Skeptic's attack | Outcome | Response |
|---|---|---|---|
| 1 | Is `a_2`'s formula actually a correct transcription of HPS eq. 3/6/7? | Could not fetch arXiv from its sandbox (`NEEDS-REAL-DATA` for the literal check) — but **independently re-derived the same formula from the general heat-kernel coefficient `a_2=(4π)^{-n/2}(1/6)∫(R·tr I − 6·tr E)dvol` plus HPS's own stated `E=3/4·dT+R/4−9/8·T_0²`, from scratch, without reading my transcription** — and got the exact same `(1/16π²)(9/2·T_0²−R/3)`. | **Accepted as a stronger check than my own single-source read of the paper** — an independent from-scratch derivation is a better corroboration than "I read the PDF correctly." No action needed. |
| 2 | Is the symbolic computation (`T_0²`, Riemann, Ricci norms) actually right, not just "ran without a Python exception"? | Independently re-derived `[Z_i,Z_j]=-2ε_{ijk}Z_k` from round67's own generators, got `T_0²=4(2t-1)²` by hand: matches. Cross-checked `‖Ric‖²=R²/n` (Einstein-space identity for n=3) against the script's `‖Riem‖²`: matches. | **Dismissed as not breaking anything** — this is a second, independent hand-derivation landing on the same numbers. Strengthens confidence. |
| 3 | Is the "cross-check against round111" genuinely independent, or decorative? | **Real finding.** `R_LC` is `t`-independent, so it **drops out of `∂a_2/∂t` entirely** — the `t=1/2` minimum of `a_2` holds for ANY value of `R_LC` (sign included). The round111 cross-check therefore verifies the VALUE of `a_2` at its extrema (e.g. distinguishing `-1/(8π²)` from `1/π²` concretely) and matters for the `a_4_partial` numeric analysis (its `t=1/3,2/3` minima ARE `R_LC`-sign-sensitive) — but it does **not** back the `a_2` verdict itself, which §0's headline framing ("net conclusion... `a_2`... picks `t=1/2`... by a sizeable margin") could be read as implying. | **Accepted as a documented limitation, claim NOT changed** — the verdict is unaffected, but the framing overstated how much work the round111 cross-check was doing for it specifically. Recorded here so a future reader doesn't credit §1's reconciliation with confirming the verdict — it doesn't need to; the verdict is R_LC-independent by construction. |
| 4 | Does substituting `R_LC=6` (vs. leaving it symbolic, vs. flipping its sign) change which verdict fires? | No — `a_2''(1/2)=9/π²>0` regardless of `R_LC`. Confirmed directly from `a2_analysis_symbolic` in `results_c176.json` (same critical point, same "min" classification, independent of `R_LC`). | Same as #3 — accepted, no action; this is the mechanism behind #3's finding. |
| 5 | Is claim.md's own "a_2 is dimension-independent in its derivation" framing accurate? | **Weakened, technically imprecise as stated.** The actual numeric prefactor of `a_2` scales with `dim(spinor rep)=2^⌊n/2⌋` and `(4π)^{-n/2}`, both of which genuinely differ between n=3 (this project's actual case) and n=4 (HPS's own derivation) — so literally porting HPS's numeric coefficients `9/2` and `1/3` unchanged to n=3, as this script does, is not strictly "dimension-independent." What IS dimension-independent, and is the only thing the verdict actually needs, is the **relative sign** between the `T_0²` and `R` terms in `E` (both enter with the same sign in every dimension via the same Lichnerowicz/Weitzenböck structure) — and sign alone is what selects `t=1/2` over `t=0,1`. | **Accepted as a narrowing caveat on claim.md's own wording, not a retraction.** claim.md is left as originally written (frozen pre-registration, per this project's own discipline of not editing claim.md after the fact) — this table is where the correction lives. The verdict `SPECTRAL-SELECTOR-DIES-AT-HALF` survives because it only depends on the sign structure (dimension-robust), not the exact prefactor (which is NOT dimension-independent as claimed). A rigorous n=3 Seeley-DeWitt re-derivation (not borrowed n=4 coefficients) remains the honest next step if this line is pursued further — this was already flagged in §3's Relaxation Map as "a substantially bigger undertaking," now with an added concrete reason (not just the excluded `Ω_ij` term, but the prefactor itself).

**Net effect on the round's own verdict:** unchanged — `SPECTRAL-SELECTOR-DIES-AT-HALF` survives independent, context-blind attack on 5 separate axes, 3 of which strengthen it (independent formula re-derivation, independent symbolic re-derivation, R_LC-sign-independence of the mechanism) and 2 of which narrow its framing without breaking it (round111 cross-check overstated as load-bearing; "dimension-independent" overstated as literal prefactor-equality rather than sign-equality). No FALSIFIED concerns; no true-kill condition (core predicate false with no viable response) was reached — per this project's Response Matrix, all 5 concerns land in Dismissed/Accepted-limitation, none in the rare "actually kills the claim" bucket.

---

## 8. Status

`experiments/20260906-c176-ob1-spectral-action-torsion-selector/` — DONE,
INCLUDING independent skeptic pass. Verdict `SPECTRAL-SELECTOR-DIES-AT-HALF`
for the specific formula tested, now `[VERIFIED-tool]` at BOTH the original
computation AND an independent context-blind skeptic re-derivation (§7) —
this is a materially stronger evidence status than a single-pass result.
A genuine sign-convention discrepancy with round111 found and resolved in
place (not hidden, §1); the skeptic separately found the round111
cross-check to be decorative for the actual verdict mechanism (§7, item 3)
— narrows the story, does not change the verdict. One honestly-reported,
uninterpreted side-finding (`a_4_partial` minima at `t=1/3,2/3`, §4) —
skeptic did not specifically attack this side-finding beyond confirming
its `R_LC`-sign-sensitivity (§7, item 4); still flagged, not yet added to
`pearl_registry/INDEX.md`. OB1's row A remains open — this closes one more
specific candidate mechanism (the borrowed 4D spectral action formula,
now with an added honest caveat that it was borrowed, not re-derived for
n=3), joining the static-symmetry route (C173) and the condensate route
(C137) as checked-and-negative. Registry (`OPEN_BLOCKERS.md`,
`pearl_registry/INDEX.md`) not yet updated pending user confirmation of
scope. No git operations run for this update.

**UPDATE (2026-09-06, registry pass):** `pearl_registry/INDEX.md` updated
with the `a_4_partial` `t=1/3,2/3` side-finding. `OPEN_BLOCKERS.md` OB13
updated with a cross-reference this round did not originally make: `a_2(t)`
is manifestly EVEN in `(t-1/2)` (a function of `(2t-1)²`) — exactly OB13's
own registry category. Per OB13's corrected understanding (C123), an even
functional cannot break the residual `t=0`-vs-`t=1` degeneracy but COULD
select `{0,1}` as a set (as round99's own even curvature toy did); `a_2`
does not even achieve that weaker outcome, landing on the single-well
`t=1/2` case instead — see OB13 for the full comparison across this
project's even functionals. `ASSUMPTIONS_MATRIX.md` row A updated to list
this round among tried-and-negative candidate mechanisms.
