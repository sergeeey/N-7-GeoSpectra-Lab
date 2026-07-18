# Round99 (B4) — Decision

**Date:** 2026-07-17
**Verdict:** `WEAKENED__CLASSICAL_MATH_CONFIRMED_PHYSICAL_FRAMING_OVERREACHED`
(skeptic verdict, Step 8a, context-asymmetric review — claim + code only,
no session history given to the reviewer)
**Go/no-go:** the pure differential-geometry computation is correct and
tool-verified; the "this motivates a domain-wall/modulus interpretation"
framing is **not licensed** by what was actually computed and is corrected
below, per the skeptic response matrix.

## What happened (including a self-caught bug, before the skeptic ran)

The first version of `e26_toy_Vt_curvature_double_well.py` computed
`R^t(Z1,Z2)Z3` as its illustrative curvature component — this triple is
**identically zero for every `t`** (since `[Z1,Z2]=-2Z3` is already
proportional to `Z3`, so `[[Z1,Z2],Z3]=[-2Z3,Z3]=0`, a self-commutator).
The "double-well" `V(t)` in that version was a bare symbolic
`(t(t-1))^2`, never actually tied to a verified nonzero curvature
component — an internal inconsistency caught by re-inspecting the script's
own output (`curved_at_t_half=False` contradicted the intended claim)
BEFORE presenting it. **Fixed** by switching to the non-degenerate
`(i,j,k)=(1,2,1)` triple (`R^t(Z1,Z2)Z1`), which IS genuinely nonzero at
`t=1/2` (`[[0,-1],[1,0]]`, confirmed by direct matrix output) and zero at
`t=0,1`. Re-run confirms `curved_at_t_half=True`, `V0=V1=0`, `Vhalf=1/16`,
critical points `{0, 1/2, 1}`, `V''(0)=V''(1)=64>0` (genuine local minima,
not merely zeros).

## Skeptic falsification (Step 8a, context-asymmetric: claim + code only)

Verdict: **WEAKENED**. Per the response matrix (falsification-ladder.md):

| Concern | Response |
|---|---|
| Math itself (`R^t=t(t-1)[[X,Y],Z]`, double-well shape) | **Confirmed correct** — re-derived independently by the skeptic, matches |
| **Framing overreach:** this is Cartan-Schouten's own 1926 classical result, not a new finding | **Accepted, corrected below** — must be stated as a REPRODUCTION of a 100-year-old classical fact about bi-invariant-metric connections, not a novel computation |
| **Physics unearned:** `V(t)` is a bare kinematic tensor-component norm, not an action term — no volume integral, no kinetic term for `t`, no equations of motion, no actual domain-wall/sigma-model construction was built | **Accepted, corrected below** — "would motivate a domain-wall interpretation IF a gravitational action contained this term" overstates what was shown; nothing here establishes that the actual spectral action (Chamseddine-Connes-Marcolli) DOES contain a term proportional to this curvature norm |
| **Mechanism gap unchanged:** algebraic minima existing at both `t=0,1` does not, by itself, force simultaneous physical realization of both — that is exactly the open parent-action question this whole program (rounds 86-99) is trying to answer, not something this round resolves | **Accepted** — this round supplies ONE ingredient (a plausible reason the two endpoints could be geometrically privileged) toward B1's full spectral-action derivation, not a substitute for it |

## Corrected statement of what this round actually establishes

1. **[FACT, reproduction of classical Cartan-Schouten (1926) result, tool-
   verified here for this project's own generator convention]:** the
   curvature of `∇^t_XY=t[X,Y]` on `su(2)` is `R^t(X,Y)Z=t(t-1)[[X,Y],Z]`
   — vanishing exactly at `t=0,1` (flat), maximal in magnitude at `t=1/2`
   (Levi-Civita). This is consistent with, and gives an explicit
   quantitative form to, this project's own already-established "t=0,1
   flat" fact.
2. **[FACT]:** the squared-norm of a genuinely nonzero curvature component
   (`R^t(Z1,Z2)Z1`) is exactly proportional to `[t(t-1)]^2`, which has
   double-well shape with minima at `t=0,1`.
3. **[HYPOTHESIS, NOT established by this round]:** that the actual
   spectral action used elsewhere in this project contains a term
   proportional to this (or any) curvature-norm-squared quantity for the
   S³ factor's connection — this was NOT checked, and doing so is exactly
   B1's full, unattempted task.
4. **[HONEST CONCLUSION]:** this round shows the double-well shape is
   available "for free" from classical geometry alone (not an ad hoc
   fitted potential) IF such a term appears in the action — a plausibility
   ingredient, not a derivation, and not a mechanism. It does NOT move the
   parent-action question past B1's own pre-registered unattempted status.

## Applying the pre-registered criteria (claim.md Section 3)

**CONFIRMED (double-well plausible)** — for the narrow mathematical claim
only, as corrected above. The BROADER framing implied by claim.md's own
Section 1 motivation ("giving a domain-wall/coexistence picture") is
**WEAKENED**, not confirmed, per the skeptic review.

## Kill Analysis

- **What this kills:** nothing about the core parent-action question — B1
  remains fully open and unattempted (deriving whether the real spectral
  action contains this term).
- **What this does NOT kill:** the classical curvature computation itself
  (robust, reproduced correctly, tool-verified, matches known 1926 result).
- **What survives:** a concrete, falsifiable NEXT step for B1: check
  whether the Chamseddine-Connes-Marcolli spectral action, applied to
  `D_{S3,t}`, produces a term proportional to `‖R^t‖²` (or any other
  `t`-dependent term with a double-well shape) — NOT attempted here.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Derive `V(t)` from the actual spectral action (B1's full task) | Apply the heat-kernel expansion of `D_{S3,t}²` and extract the `t`-dependent terms — a substantially larger undertaking than this round |
| Check if OTHER curvature-based quantities (Ricci scalar, not just the Riemann-tensor-norm used here) also give a double-well | Cheap follow-up, not attempted |

## Assumptions carried, unresolved

- `∇^t_XY=t[X,Y]` (this project's established family definition) —
  reused, not re-derived.
- The specific curvature-norm-squared functional form (`‖R^t(Z1,Z2)Z1‖²`)
  as "the" natural curvature-penalty term — one CHOICE among several
  possible norms (e.g. Ricci-scalar-squared, Weyl-tensor-based), not shown
  to be uniquely privileged.

## What this does NOT mean

1. Does NOT establish that `t` is physically dynamical, or that a
   domain-wall solution actually exists in this construction.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT modify `preprint.tex` or any prior experiment. No file
   downloaded/saved outside this new folder; nothing submitted externally.
4. Does NOT claim priority for the curvature formula itself — Cartan and
   Schouten (1926) is the origin; this round only verifies it holds for
   this project's specific generator/sign convention.

## Check (reproduces this decision)

```
cd experiments/20260717-round99-toy-Vt-curvature-double-well
python e26_toy_Vt_curvature_double_well.py
```
Expect: `curvature_formula_R_t_equals_t_t-1_confirmed_all_27_triples=True`,
`flat_at_t0=True`, `flat_at_t1=True`, `curved_at_t_half=True`,
`V0=0, V1=0, Vhalf=1/16`, `critical_points=['0','1','1/2']`,
`minima_confirmed_by_second_derivative=True`.
