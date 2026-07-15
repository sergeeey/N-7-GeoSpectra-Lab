# Round63-WrappedS3InstantonChannel Claim — does the a=3 channel survive when actually computed?

**Date:** 2026-07-15
**FL tier:** [x] Full (touches the moduli-stabilization headline result
ρ₆_min≈1.179; a real physics computation, not scoping)
**Question type:** [x] descriptive (does a specific substitution into an
already-established formula produce an EFT-valid extremum)

---

## Prior Result Gate (mandatory — this topic has a documented fragility history)

**Hard lesson already on record** (`null_results/INDEX.md`, entry META-C1):
the ORIGINAL "λ-dimensional obstruction" theorem (2026-06-22,
`experiments/20260622-lambda-dim-gate/`) used the WRONG trajectory
(slope-1, $\rho_3=\alpha\rho_6$) and concluded $\exp(-\lambda/\rho_6^2)$ is
constant for ALL $a$ — this was **SUPERSEDED 2026-06-23**: the physical
trajectory is slope-2 ($\rho_3\propto\rho_6^2$, verified G28/G29), on which
$\exp(-\lambda/\rho_6^2)$ **is** $\rho_6$-dependent for $a\neq 0$. The
corrected result lives in `preprint.tex` §sec:lambda (eq:buckingham-pi,
eq:slope2-exp) — re-read directly this round, not from memory, given the
demonstrated risk of exactly this kind of subtle substitution error.

**Confirmed by direct re-derivation before writing this claim** (not trusted
from the text alone): with $\lambda_{\mathrm{geom}}=c\cdot\rho_3^a\rho_6^{2-a}$
and $\rho_3=C'\rho_6^2$ (slope 2), $\lambda_{\mathrm{geom}}=c(C')^a\rho_6^{a+2}$,
so $\exp(-\lambda_{\mathrm{geom}}/\rho_6^2)=\exp(-c(C')^a\rho_6^a)$ — matches
`preprint.tex` eq:slope2-exp exactly. For $a=3$ (wrapped-$S^3$ instantons,
$\lambda\sim\Vol(S^3)\sim\rho_3^3$): $\exp(-c(C')^3\rho_6^3)$.

**Existing machinery this round reuses (cited, not re-derived):**
- `experiments/20260626-g94-s3-np-instanton/`: an ACTUAL D2-brane instanton
  term $A_{S3}\exp(-c_{S3}\rho_3^3)$ was already built and calibrated
  (window $0.248<c_{S3}<0.372$, best fit $c_{S3}\approx 0.235$) — but for a
  **different purpose** (stabilizing $\rho_3$ itself against $V_{\mathrm{main}}$
  in a 2D potential), not for the $\lambda_{\mathrm{np}}/\rho_6^2$ ansatz used
  in the 1D $V_{\mathrm{total}}(\rho_6)$ formula (eq:Vtotal) that the
  established $\rho_6$-min result (G62, $\rho_{6,\min}\approx1.179$) is built on.
- `preprint.tex` eq:Vtotal: $V_{\mathrm{total}}(\rho_6)=V_0 C^3
  f(\rho_6)/\rho_6^{12}$, $f(\rho_6)=1-\exp(\lambda(1/\rho_6^{*2}-1/\rho_6^2))$
  — $\lambda$ here is a **free constant**, not yet a function of $\rho_6$.

**This round's actual gap, precisely identified:** these two threads have
never been connected. G94's D-brane term and the abstract's own $a=3$ formula
share the same physical origin ($S_{\mathrm{inst}}\propto\Vol(S^3)\propto\rho_3^3$)
but live in different parametrizations (bare $\exp(-S_{\mathrm{inst}})$ vs.
$\exp(-\lambda_{\mathrm{geom}}/\rho_6^2)$) and different formula slots (2D
$V_{\mathrm{main}}$ stabilizing $\rho_3$, vs. 1D $f(\rho_6)$ stabilizing
$\rho_6$). Nobody has substituted a genuinely $\rho_6$-dependent
$\lambda(\rho_6)=c(C')^3\rho_6^3$ into $f(\rho_6)$ and checked what happens
to the established $\rho_{6,\min}\approx 1.179$ result.

---

## Frozen claim

Define $f_{a=3}(\rho_6) := 1-\exp\!\bigl(c(C')^3\rho_6^3\cdot(1/\rho_6^{*2}-1/\rho_6^2)\bigr)$
— i.e. eq:Vtotal's own $f(\rho_6)$ with the constant $\lambda$ replaced by the
$a=3$ channel's own derived $\rho_6$-dependence $\lambda(\rho_6)=c(C')^3\rho_6^3$
(same functional form the rest of $V_{\mathrm{total}}$ already uses $\lambda$
in, substitution only, no other change).

**Question, not a predetermined answer:** does
$V_{\mathrm{total},a=3}(\rho_6)=V_0 C^3 f_{a=3}(\rho_6)/\rho_6^{12}$ have an
EFT-valid extremum ($\rho_6>1$, genuine local minimum not saddle,
$d^2V/d\rho_6^2>0$ there) for some range of the coefficient $c(C')^3$
(playing the same free-parameter role $\lambda$ already plays in the
established, constant-$\lambda$ zero-fit result)? If yes: does the resulting
$\rho_{6,\min}$ range overlap with, or diverge from, the established
$\rho_{6,\min}\approx1.179$?

---

## Kill criteria / pre-registered outcomes (all informative)

| Outcome | Condition | Verdict |
|---|---|---|
| **PROMOTE** | A genuine EFT-valid minimum exists for a non-degenerate range of $c(C')^3$, AND the resulting $\rho_{6,\min}$ range is consistent with (overlaps or closely brackets) the established $\approx1.179$ | The $a=3$ channel is a live, working candidate for $\lambda_{\mathrm{np}}$'s origin — closes the last open channel from the abstract's own G83-G86B table |
| **STRUCTURAL NULL** | No EFT-valid minimum exists for any $c(C')^3>0$ (e.g. monotonic $f_{a=3}$, or minimum only at sub-stringy $\rho_6<1$) | Joins G83-G86B as a confirmed-null channel — the table caption "not computed" becomes "computed, NULL", closing the Open Problems item honestly rather than leaving it open |
| **INCOMPATIBLE NORMALIZATION** | A minimum exists but only for $c(C')^3$ values wildly inconsistent with G94's own already-established, physically-motivated window ($0.248<c_{S3}<0.372$) when the two are related via the shared $\rho_3^3$ origin | Reported as a genuine tension between the two existing pieces of machinery, not silently reconciled — flag for a future round, do not force an answer |
| **ILL-POSED** | The substitution itself is not well-defined (e.g. $C'$ and $c_{S3}$ turn out to be dimensionally or physically incompatible, or eq:Vtotal's $C$ dependence interacts with $a=3$'s own $C'$-dependence in an inconsistent way) | Report precisely what breaks — this is itself the honest answer, not a failure |

## Method

1. Build $V_{\mathrm{total},a=3}(\rho_6)$ symbolically (sympy, exact), reusing
   the EXACT existing eq:Vtotal structure with only $f\to f_{a=3}$ changed.
2. Scan $c(C')^3$ over a broad range (both signs, several orders of
   magnitude) — do not assume the sign or scale in advance.
3. For each value: solve $dV/d\rho_6=0$ symbolically or via robust numerics,
   classify every critical point (min/max/saddle/none), check EFT validity
   ($\rho_6>1$, real, positive).
4. Cross-check: does any $c(C')^3$ value in the surviving range correspond,
   via the shared $\rho_3^3\propto\Vol(S^3)$ origin, to G94's own established
   $c_{S3}\in(0.248,0.372)$ window under the slope-2 trajectory substitution
   $\rho_3=C'\rho_6^2$? State the precise relation attempted and whether it
   closes or not — do not force a match if the two do not actually relate
   simply (e.g. if $C'$ differs in normalization between the two threads).
5. Independent second route: re-derive the same result via a genuinely
   different method (e.g. asymptotic/perturbative expansion for small and
   large $\rho_6$ instead of the same symbolic critical-point solve) to
   catch algebra errors, matching this project's own established practice
   (Round 59/61) rather than trusting one code path.

## What this does NOT mean

1. Does NOT change the established constant-$\lambda$ zero-fit result
   ($\rho_{6,\min}\approx1.179$, G62) regardless of outcome — that result
   stands on its own as a DIFFERENT (simpler, $\lambda$=const) ansatz; this
   round tests a SPECIFIC alternative, does not retroactively invalidate it.
2. Does NOT claim to derive $\lambda_{\mathrm{np}}$'s microscopic value from
   string theory even if PROMOTE — $c(C')^3$ remains a free normalization
   unless independently fixed (matching G94's own caveat: "does NOT prove
   $c_{S3}=0.235$ is the physical value").
3. Does NOT reopen or modify G94's own $\rho_3$-stabilization result — that
   round's own $c_{S3}$ window is cited, not re-verified or re-run here.

## Fence

- λ = FREE_COUPLING_PARAMETER (this round tests one specific functional
  form for it; does not fix its numerical value even if PROMOTE)
- safe_for_runtime = False
