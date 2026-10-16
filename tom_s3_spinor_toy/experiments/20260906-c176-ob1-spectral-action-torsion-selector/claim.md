# C176 — Claim

**Experiment ID:** `20260906-c176-ob1-spectral-action-torsion-selector`
**Parent:** OB1 row A (t-selection) — the "decisive experiment" proposed by an
external reviewer (relayed by the user) in response to this session's own
over-broad conclusion that C137's condensate-mechanism rejection closed the
ENTIRE dynamical-selection door. Corrected: C137 only closed the confinement/
SUSY-condensate route; the spectral/gravitational-action route (does the
Seeley-DeWitt-expanded action `S_spec(t)` have genuine minima at `t=0,1`,
not just `t=1/2`?) was never checked. Built per user's explicit direction
("строй сейчас").

## Step -5: Zero-Signal Gate

- **Entity:** the Seeley-DeWitt/heat-kernel coefficients `a_0, a_2, a_4` of
  `D_S3(t)^2` (round67/E2's Cartan-Schouten torsion family on `S3=SU(2)`,
  `T^t=(2t-1)[X,Y]`), assembled into the truncated spectral action
  `S_spec(t) = Λ^n F_n a_0 + Λ^{n-2} F_{n-2} a_2 + ... + F_0 a_4`, using the
  EXACT, cited torsion-corrected formula from Hanisch, Pfäffle & Stephan
  2009 (arXiv:0911.5074, "The Spectral Action for Dirac Operators with
  skew-symmetric Torsion", eq. 3, 6, 7 — verified this session by direct
  read of the paper's own arXiv HTML source, not a secondary summary).
- **Falsifiable predicate:** does `a_2(t)` (and, to the extent the n=3-vs-
  n=4 dimensional mismatch allows, the dimension-independent PART of
  `a_4(t)`) have genuine local minima at `t=0` AND `t=1` (not just
  `t=1/2`), for coefficients taken directly from the cited paper's own
  formula (not tuned to produce this answer)?
- **Measurable outcome:** exact symbolic computation (sympy) of `T_0^2(t)`
  (torsion-squared invariant), the full Riemann/Ricci tensors of `∇^t`
  (extending round99's own single-component check to all independent
  components), and `a_2(t)`'s exact functional form; report critical
  points and their nature (min/max/saddle).

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Does a specific, cited formula, applied to
already-established project objects, have a specific mathematical
property (minima at specific points) — not causal, no estimand canvas
beyond the falsifiable predicate above.

## Honest scope limitation, stated BEFORE computing (not after)

Hanisch-Pfäffle-Stephan's own `a_4` formula (their eq. 7, and its further
decomposition via `Ω_ij`) is derived **for n=4** specifically — the
`(1/12)Σtr(Ω_ij Ω_ij) = -1/24||Riem||² - ...` decomposition uses a
Clifford-trace identity (`tr(e_k e_l e_s e_t)=4(δδ-δδ)`) whose numerical
prefactor is specific to the `Cl(4)` spinor module dimension, NOT
directly transferable to our `n=3` (`S3`) case without re-deriving the
analogous `Cl(3)` trace identity. This round therefore computes:
1. **`a_2(t)`** — the paper's own explicit closed form `(1/16π²)(9/2·T_0² -
   1/3·R)` is DIMENSION-INDEPENDENT in its derivation (Bochner formula eq.3
   only uses Clifford relations + `tr(dT)=0`, no `n=4`-specific trace
   identity) — computed IN FULL, exactly, for `S3`.
2. **`a_4(t)`, PARTIAL** — only the terms NOT requiring the `Ω_ij`
   decomposition (`R², ||Ric||², ||Riem||², R·T_0², (T_0²)²` — all
   dimension-general once the tensors themselves are computed for `n=3`),
   explicitly EXCLUDING the `Ω_ij`-trace-dependent piece, which is flagged
   as future work, not silently dropped.
This is NOT the full a_4 — reported as a leading/partial proxy, honestly
labeled, per this project's own "no silent caps" discipline.

## Kill-criterion table (frozen before running `c176_spectral_action_t_selector.py`)

| Verdict | Condition |
|---|---|
| `SPECTRAL-SELECTOR-CONFIRMED` | `a_2(t)` (at minimum; `a_4`-partial checked for consistency) has genuine local MINIMA at `t=0,1` with `a_2''(0), a_2''(1) > 0`, using the cited paper's own coefficients unmodified |
| `SPECTRAL-SELECTOR-DIES-AT-HALF` | The extremum is at `t=1/2` (Levi-Civita) instead — the "boring", already-anticipated outcome (round99's own curvature-only proxy pointed the OPPOSITE way; torsion-squared `T_0²(t)` is expected, by direct construction, to be an UPWARD parabola zero at `t=1/2` and maximal at `t=0,1` — meaning a POSITIVE-coefficient `T_0²` term in `a_2` would itself prefer `t=1/2`, not `t=0,1` — this is a real, pre-identified risk, not invented after seeing the result) |
| `PARAMETER-DEPENDENT-NOT-DERIVED` | The qualitative conclusion (double-well vs single-well) flips depending on which of the cut-off moments `F_0,F_2,F_4` or which physically-motivated sign convention for "extremize" (minimize vs maximize the action) is chosen — a genuine, honestly-reported non-derivation |

**Pre-registered expectation (written BEFORE running the script, matching
this project's own "prediction before data" discipline):** given
`T_0²(t) ∝ (2t-1)²` (upward parabola, zero at `t=1/2`, positive at `t=0,1`
— a direct, un-computed-yet but structurally forced consequence of
`T^t=(2t-1)[X,Y]` with `[X,Y]` a fixed nonzero tensor) and the paper's own
coefficient `+9/2` on `T_0²` in `a_2`, the NAIVE expectation is that
`a_2(t)` is MINIMIZED at `t=1/2`, not `t=0,1` — i.e. `SPECTRAL-SELECTOR-
DIES-AT-HALF` is the a priori MORE LIKELY outcome, not `CONFIRMED`. This
is written down now specifically so a later "it worked" cannot be
suspected of being reverse-engineered from the answer.

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** Hanisch-Pfäffle-Stephan arXiv:0911.5074 fetched and
  read directly this session (HTML source, not a summary); round67/round99/
  round111's own already-committed, tool-verified pieces reused via
  `importlib`, not re-derived from scratch.
- **Novelty Check:** `grep`-confirmed no prior round in this project has
  computed `a_2(t)`/`a_4(t)` for the `S3` torsion family — G38 (2026-06-20)
  computed a DIFFERENT spectral-action minimization, over the bundle Chern
  class `c₃` on `S⁶`, not over `t` on `S³` — not a duplicate.

## What this does NOT mean (pre-registered)

1. Does NOT, even if `SPECTRAL-SELECTOR-CONFIRMED`, prove this is THE
   physically correct action for this project's actual 13D construction —
   only that the specific, cited 4D torsion-spectral-action formula,
   applied to `S3`'s own torsion family, has this property.
2. Does NOT resolve row B (kernel multiplicity=2 at `t=0,1`) or the D/E
   tension (`ASSUMPTIONS_MATRIX.md`) even if row A closes.
3. Does NOT change `N_gen=3`'s CONDITIONAL status regardless of outcome.
4. The `a_4`-partial computation, even if consistent with a double-well,
   does NOT constitute a full a_4 derivation — the `Ω_ij` piece is
   explicitly not computed here.
