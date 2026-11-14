# C216 Decision — Kobayashi-Nomizu route gives Ric^c=4.0, NOT C215's
# predicted 1.5 — plus a significant unresolved Castellani-formula anomaly
# discovered while diagnosing the mismatch

**Date:** 2026-10-02
**Verdict:** MISMATCH (per claim.md's own pre-registered kill criterion) —
C212's torsion re-confirmed via a SECOND, independent construction; C213's
Castellani-formula code shown to disagree with an independent symmetric-
space control by exactly a factor of 2, root cause NOT identified, NOT a
simple global coefficient bug (two specific hypotheses tested and refuted).

> **RESOLVED 2026-10-03 by C217** (`experiments/20261003-c217-castellani-
> convention-factor/`). The "unresolved Castellani anomaly" below is a
> CONVENTION factor, not a bug: Castellani's eq. (3.34) defines the
> curvature components by `R^a_b = R^a_{b de} V^d ^ V^e` WITHOUT the
> standard 1/2, so his `R^a_{bde}` (and the code's output) is exactly 1/2
> of the standard Riemann tensor. 2 x C213's tensor equals the unit round
> S6 tensor entry by entry (1296 entries, error 2e-15) on BOTH the control
> and the non-symmetric G2/SU(3), and KN + Friedrich-Ivanov (no Castellani
> code) independently gives Ric^g = 5 = 4 + 1. Consequences: the MISMATCH
> with 1.5 stands and is now explained (C215's 1.5 should be 4.0); C214's
> REJECT is retracted; the "two refuted hypotheses" and the "suggestive,
> NOT confirmed" language in Sections 2-4 below are SUPERSEDED (the
> skeptic review of this round correctly noted that no diagnostic here
> scaled all four terms together, and that G2/SU(3) = the round sphere
> makes Ric^g = 5 a consequence, not a lead). Text below is kept as the
> record of what was believed when it was committed; corrections to
> statements that were simply wrong are marked CORRECTED.

## Results [VERIFIED-numpy]

```
--- CONTROL round S6=SO(7)/SO(6), expect Ric=5, T=0 ---
KN:  Ric^c = 5.000000*delta  (spread 8.9e-16, off-diag 2.4e-16), leak 2.2e-16
KN:  |T|^2 = 0.000000, total-antisymmetry err 0.0e+00
Castellani Ric^g = 2.500000*delta  (spread 4.4e-16, off-diag 1.2e-16)
  -- HALF the textbook value, on an independently-built control

--- G2/SU(3), ambient-unit frame (C214/C215 basis, scale=sqrt(3)) ---
KN:  Ric^c = 4.000000*delta  (spread 1.8e-15, off-diag 1.7e-15), leak 3.7e-15
KN:  |T|^2 = 24.000000  (EXACTLY matches C212/C214's octonion-route torsion)
Castellani Ric^g = 2.500000*delta  (CORRECTED: this is C214's rescaled value; C213 itself reported 0.8333 at r=1, the same code at r=sqrt3 gives 2.5)
triangle_max_err = 2.5 on BOTH spaces (CORRECTED: this was in results_c216.json but not shown here; it is exactly (Ric^c + corr) - Castellani = 5 - 2.5, i.e. the factor 1/2 of C217)

PREDICTION from C215 (Friedrich-Ivanov route): Ric^grad = 1.5
KN route gives Ric^c = 4.000000
[MISMATCH]
```

`experiments/20261002-c216-kobayashi-nomizu-ricci-check/results_c216.json`.

## 1. What passed cleanly

**KN's own implementation is well-calibrated.** The positive control
(S6=SO(7)/SO(6), a symmetric space with a known textbook answer) gives
`Ric^c=5.000000` exactly — matching the standard unit-n-sphere Ricci
eigenvalue `n-1=5` for `n=6` — with torsion exactly zero (expected: a
symmetric space's canonical connection is torsion-free) and negligible
reductive-decomposition leak (`2.2e-16`). This was checked BEFORE trusting
the method on the unknown (G2/SU(3)), per this project's own "instrument
calibration before discovery" lesson (C201).

**The torsion cross-check is a genuinely strong, independent confirmation.**
KN's bracket-only torsion construction (`T^c(X,Y)=-[X,Y]_m`, no octonion
cross product in the KN code) gives `|T|^2=24.000000` for G2/SU(3) —
matching C212/C214's octonion-cross-product construction to the digit.
CORRECTED wording (skeptic review): these are two different OPERATIONS
(a Lie-bracket projection vs. an octonion triple product), but both start
from G96's `phi`-derived data, so the match checks the shared
normalization and the two formulas' agreement, not a fully independent
derivation from scratch. Still a strong consistency check.

## 2. What failed, and the diagnostic chain this triggered

KN's G2/SU(3) result, `Ric^c=4.0`, does NOT match C215's predicted `1.5` —
a large, clean mismatch (not noise), failing claim.md's own pre-registered
kill criterion. Because KN's own control passed exactly and the torsion
cross-check independently confirmed KN's basis/scale handling, the natural
next question was whether C213's Castellani-formula code (which produced
the `Ric^g=2.5` feeding into C215's Friedrich-Ivanov computation) is
itself reliable outside the N^010 points it was originally calibrated on.

**Diagnostic 1 — reuse C213's own code on the SO(7)/SO(6) control
(`debug_reuse_c213_on_control.py`):** imports C213's actual
`build_structure_constants`/`riemann_ricci` functions directly (not a
C216 retyping) and runs them on the SAME control. Result: `2.500000`,
not the textbook `5.0`. This is a real property of C213's ORIGINAL code,
not a C216 transcription artifact.

**Diagnostic 2 — term-by-term breakdown
(`debug_castellani_term_breakdown.py`):** on the control (a symmetric
space, `C_KKK=0` identically, confirmed `max|C_KKK|=0.0`), only term2
(the pure-H-curvature term) survives; terms 1/3/4 are exactly zero (they
all depend on `cbold`, which is identically zero when `C_KKK=0`).
Doubling term2's coefficient (`0.5 -> 1.0`) gives exactly `5.0` on the
control — a clean, exact fix FOR THIS CASE.

**Diagnostic 3 — does the same fix hold on N^010's own double calibration
(`debug_n010_t2_sensitivity.py`)?** NO. Doubling term2's coefficient on
N^010 (which has `C_KKK != 0`, all four terms active) breaks the
calibration badly — `12,12,...,12` (correct, matches the published R=12
at BOTH eq 5.72 and eq 5.73 points) becomes `16/30` or `23.1/22` (wrong).
**This REFUTES "term2's coefficient is universally wrong" as the
explanation** — the original coefficient (`0.5`) is demonstrably correct
wherever N^010's own published values can check it.

**Diagnostic 4 — is the control's discrepancy a degenerate-uniform-r
code-path artifact (`debug_uniform_r_perturbation.py`)?** NO. Perturbing
one generator's `r` away from exact uniformity (`eps` from `0` to `0.3`)
changes the Ricci SMOOTHLY, with no discontinuity near `eps=0` jumping
toward `5.0`. **This REFUTES a degenerate-uniform-r code path** as the
mechanism.

**Diagnostic 5 — cross-check against C165's independently-built `R^c`
(`debug_cross_check_c165.py`):** `experiments/20260906-c165-canonical-
connection-curvature-check/` (found via this round's own Prior Result
Gate) already built the identical KN `R^c(X,Y)=-[X,Y]_h` object for
S6=G2/SU(3), via the same cited source (Nomizu 1954), but in G96's raw,
UN-rescaled complement basis (`scale=1`, not C212-215's ambient-unit
`scale=sqrt(3)`) and for a different purpose (a Schur's-Lemma vanishing
question, not a Ricci computation). Re-running THIS round's own
`kn_curvature_torsion` at `scale=1` gives `Ric^c=4/3` exactly (a clean
rational number). CORRECTED (the original sentence stated the scaling
law inverted and contradicted its own arithmetic): the code and numbers
give `Ric^c(scale) = Ric^c(1) * scale^2` (`4/3 -> 4.0`, factor
`scale^2 = 3`); `scale` multiplies the generators to form the orthonormal
frame `e_a = scale*K_a`, so a larger `scale` means SHORTER reference
generators in the metric, not a bigger sphere. This is a
SELF-CONSISTENCY check of C216's own scale-handling (algebraically
guaranteed, not new information) — C165 itself never computed a Ricci
tensor, only the raw curvature 2-form, so it does not independently
pin down the absolute value `4.0` beyond what C216 already established.

## 3. Net status: unresolved, not patched (SUPERSEDED by C217 — see the RESOLVED banner at the top; hypotheses (a)/(b) below are both wrong, the cause is Castellani's eq. 3.34 convention)

**The control's 2.5-vs-5.0 discrepancy is real, reproducible, and NOT
explained by either hypothesis tested.** Two live explanations remain,
NOT distinguished by this round:

(a) A genuine bug in Castellani's formula specific to the symmetric-space
    (`C_KKK=0`) limit, which N^010 (non-symmetric, `C_KKK != 0`) never
    exercises in isolation — i.e. term2's coefficient could be correct
    ONLY when terms 1/3/4 are also active, with some compensating
    structure this round did not identify.
(b) A generator-normalization mismatch specific to how this round's ad
    hoc SO(7)/SO(6) `K`/`H` matrices were built (`a_ij` via
    `1/sqrt(2)`-normalized antisymmetric matrices) vs. whatever
    convention Castellani's `r`-parametrization structurally assumes —
    independent of whether C213/C214's G2/SU(3) or N^010 numbers are
    themselves correct.

**A suggestive (NOT confirmed) consistency check, stated explicitly as
unconfirmed:** IF the mechanism behind the control's discrepancy also
means C213's G2/SU(3) `Ric^g` should really be `5.0` (not `2.5`), THEN
Friedrich-Ivanov's formula (`Ric^g = Ric^grad + corr`, with `corr`'s trace
`=|T|^2/4=6.0` — an EXACT algebraic identity for any totally antisymmetric
3-tensor, not a numeric coincidence, re-derived here: `trace(corr) =
-(1/4)*sum T[i,b,k]*T[b,i,k] = -(1/4)*sum(-T[i,b,k]^2) = (1/4)|T|^2`)
would give `Ric^grad = 5.0 - 1.0 = 4.0` — EXACTLY matching KN's
independently-verified value. **This is NOT established here** — it is
named explicitly as the most promising lead for a dedicated follow-up
round, not acted on by silently revising C213/C214/C215's own numbers.

## 4. Kill Analysis (Anti-Overfitting Gate discipline)

**What this round kills:** the specific claim that C215's `Ric^grad=1.5`
is independently confirmed by the Kobayashi-Nomizu route — it is NOT; KN
gives `4.0`.

**What this round does NOT kill:**
- C212's torsion construction (`|T|^2=24`) — RE-CONFIRMED via a second,
  completely independent construction (Lie bracket vs. octonion cross
  product), the strongest cross-check in this entire chain.
- C213's STRUCTURAL findings (isotropy, Einstein-ness of the Castellani-
  computed tensor, and the exact match to N^010's own two published
  points) — these survive regardless of whether the absolute value `2.5`
  is itself correct, since isotropy/Einstein-ness and the N^010 match are
  invariant under whatever mechanism (if any) causes the newly-found
  control discrepancy.
- The KN implementation itself — independently validated via its own
  positive control AND the torsion cross-check; trusted going forward.
- Friedrich-Ivanov's formula and theorem — cited, general, not
  re-derived or challenged here; only its INPUT (`Ric^g=2.5`, from
  Castellani) is now in question, not the formula itself.

**What is newly, genuinely unresolved (not present before this round):**
whether C213/C214's specific numeric value `Ric^g=2.5` for G2/SU(3) is
correct, or carries an unidentified factor-of-2 issue related to the same
mechanism that makes Castellani's code give half the textbook answer on
an independent symmetric-space control. **This is explicitly flagged, not
resolved, and not silently patched.**

**Relaxation Map (candidate next steps, none attempted here):**

| variant | changed assumption | status |
|---|---|---|
| R1 | Build a SECOND independent symmetric-space control with a DIFFERENT generator-normalization convention (e.g. matching N^010's own Gell-Mann/Pauli-style construction instead of ad hoc `a_ij` matrices) to distinguish hypothesis (a) from (b) in Section 3 | Not attempted — the cheapest next differentiating test for this specific question |
| R2 | Re-derive Castellani's eq 3.35-3.36 term2 coefficient directly from the paper's own stated conventions (not from the N^010 numeric match alone) to check whether it is explicitly stated as symmetric-space-conditional | Not attempted — requires a careful primary-source re-read, not hand algebra |
| R3 | If (a) or (b) above is confirmed and C213's true `Ric^g=5.0`, re-open C214's REJECT verdict (the Russo/Agricola bridge predicted `Ric=5.0` and was rejected ONLY because Castellani's code gave `2.5`) — NOT done here, named explicitly so it is not silently forgotten | Not attempted — would require re-verifying C214's own bridge derivation independently, a separate, careful round |

## 5. Addenda added to related decisions (flagged, not rewritten)

Per `research-methodology.md` principle 5 (immediate retroscan when a new
result bears on existing claims), short UPDATE notes pointing to this
round's finding were added to `experiments/20261002-c213-...-calibrated/
decision.md`, `experiments/20261002-c214-torsion-ricci-relation-check/
decision.md`, and `experiments/20261002-c215-friedrich-ivanov-ricci-
torsion/decision.md` — each clearly marked as an addendum, none of their
own verdicts changed by this round.

## 6. Status

Not added to `PARENT_ACTION_GATE.md` — an internal-consistency/diagnostic
result about S6's own intrinsic geometry and about this project's own
Castellani-formula code, not a new F6 equation-of-motion input. Logged to
`null_results/INDEX.md` per the MISMATCH/REJECT protocol, with a pearl_
registry entry for the unresolved Castellani anomaly as the concrete next
step.
