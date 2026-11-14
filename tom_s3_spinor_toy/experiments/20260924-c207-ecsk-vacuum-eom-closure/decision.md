# C207 Decision — F6 (metric EOM) closes REJECT for ECSK/C134; F7 moot

**Date:** 2026-09-24
**Verdict:** REJECT (F6, ECSK/C134/frozen-background candidate)

## What was computed (`[VERIFIED-sympy]`, `c207_ecsk_vacuum_eom_closure.py`)

| Check | Result |
|---|---|
| `trace(Ric_S3) == Scal(t)` for the 3-dim Einstein-space relation `Ric=lambda*I`, `Scal=3*lambda`, using round111's own `8t(1-t)` eigenvalue and `24t(1-t)` scalar formulas | Residual `0` — internally consistent |
| `Ric_S3` eigenvalue at `t=1/2` | `2` (nonzero, positive) |
| Full `Ric_S3` matrix at `t=1/2` | `2*I_3`, all three eigenvalues `= 2 != 0` |
| Matches round111's independently published `Scal_LC=6`? | Yes, exactly |
| Any finite `rho_3` sets `Ric_S3` to zero? | No — `2/rho_3^2` has no real root |

All 6 boolean checks pass (`all_pass: True`, `results_c207.json`).

## The argument, stated plainly

1. C134 (2026-09-02): ECSK's torsion equation of motion, in vacuum, for
   4D-chiral fermion content, forces `T=0` — the ONLY self-consistent
   point is `t=1/2`.
2. KT-8 (project-certified 3x + literature): at `t=1/2`, the full
   twisted Dirac operator has NO zero modes. `psi=0` there, trivially —
   so the fermion stress tensor `T_{MN}` vanishes identically, and the
   metric field equation reduces to the pure vacuum Einstein equation
   `Ric(g)=0`, with no matter source available to balance any curvature.
3. round111 (2026-07-17): the `S3` factor's Ricci tensor (Killing-form
   metric) is `Ricci^t(Z_a,Z_b) = 8t(1-t)*delta_ab` — an Einstein metric.
   At `t=1/2` this is `2*delta_ab`, confirmed nonzero here as a full
   matrix (not inferred from the trace alone).
4. Standard fact (not project-specific, cited not derived): the Ricci
   tensor of a Riemannian product `M4 x S3 x S6` is block-diagonal —
   `Ric = Ric(M4) (+) Ric(S3) (+) Ric(S6)`, no cross terms. A single
   nonzero block is sufficient to make the total nonzero.

**Conclusion:** since `Ric_S3 != 0` at `t=1/2` (step 3), and Ricci is
block-diagonal on a product (step 4), `Ric(g) != 0` on the full frozen
`M4xS3xS6` background at `t=1/2` — **regardless of what the `S6` block's
own curvature turns out to be**. The vacuum Einstein equation is
violated at the ONE point ECSK's own torsion sector permits.

## Why this is cheap, not a new discovery

This round does not derive anything new about the `S6` nearly-Kähler
geometry, and does not need to — the whole point of using the
block-diagonal product fact is that ONE nonzero block already settles
the question, so the harder, genuinely unresolved question of the exact
`S6` curvature (this project has no certified value for the actual
nearly-Kähler metric's Ricci tensor, only a round-sphere PROXY value
used elsewhere for an unrelated Lichnerowicz-gap estimate, `experiments/
20260621-g74a-lichnerowicz-gap/`, which was NOT reused here precisely
because it is not certified to be the same metric) is sidestepped
entirely. Everything actually computed here reuses two already-published
numbers (round111's `8t(1-t)` and `24t(1-t)`) and applies one textbook
fact. The only genuinely new step is the explicit chaining — which
nobody had written down as a formal, closed conclusion before this
round.

## Kill Analysis (mandatory for REJECT, per `falsification-ladder.md`)

**What was killed:** the specific claim that the ECSK-with-fermion-
condensate-torsion mechanism (C134), evaluated on THIS project's frozen
`M4xS3xS6` product-of-homogeneous-spaces background, supplies a genuine
F6-passing background/torsion equation-of-motion pair. It does not — the
torsion sector is satisfied only at a point where the metric sector is
provably violated.

**What was NOT killed:**
- C134's own torsion-equation derivation itself (`T=0` at `t=1/2`) —
  unaffected, still `[VERIFIED-tool]`.
- The general ECSK framework as a candidate action principle — only this
  SPECIFIC background (bare product of round/homogeneous compact spaces,
  no flux) is shown incompatible with it.
- This project's separate Freund-Rubin/flux program (G54-G66) — untouched,
  and in fact this round's radius-independence corollary (no finite
  `rho_3` rescues the `S3` block) is a clean, independent confirmation of
  *why* that program needed flux support in the first place: a bare
  compact positively-curved factor can never be rescaled to Ricci-flat.
- OB1/N_gen=3's own `S6`-only chain (G73/G74A/G74B) — different substrate,
  untouched.

**Relaxation Map** (per the Anti-Overfitting Gate, one assumption at a
time, not bundled):
- *Remove* the "bare product, no flux" assumption → routes to the
  existing G54-G66 Freund-Rubin program, a SEPARATE, already-explored
  direction, not a new one this round opens.
- *Remove* the "frozen radii" assumption (relax `rho_3` alone) → this
  round's own radius-independence check already closes this escape for
  the `S3` factor specifically (no finite `rho_3` helps).
- *Replace* the fermion-condensate-torsion source with a different
  torsion source → already explored and REJECTed by C137 (fermion
  condensate has no dynamical derivation in this project's frozen
  content) — a genuinely different candidate would need its own new
  physical mechanism, not examined here.

## What this means for `PARENT_ACTION_GATE.md` / `OPEN_BLOCKERS.md`

F6's status for the ECSK/C134 candidate specifically should be updated
from `PARTIAL, not PASS` to `REJECT` (metric sector formally shown
violated, not merely unaddressed). F7 should be logged as `MOOT` for this
same candidate (no fixed point exists to test stability of) — this is
itself a form of answering F7, not a gap, and should not be counted
alongside genuinely open F7 items for other, still-live candidates.

## Reproduce

```
cd experiments/20260924-c207-ecsk-vacuum-eom-closure
python c207_ecsk_vacuum_eom_closure.py
```

`ruff check` — clean (verified before this write-up).
