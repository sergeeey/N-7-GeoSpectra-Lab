# Parent Action Gate — pre-registered checklist for OB1/OB2

**Purpose:** before any future attempt at OB1 (parent action search) or OB2
(spectral-triple architecture), this gate freezes what a candidate
construction must supply and states the pass/fail criterion for each field
— per this project's own FL discipline (define the gate before running the
test), and per the user's own recommended next step ("заморозить минимальный
`PARENT_ACTION_GATE`"). **This file supplies no answer** — it is a template
a candidate construction is checked against, matching `claim.md`'s own
kill-criterion discipline applied one level up (to the whole OB1/OB2
research direction, not a single experiment).

A candidate construction PROMOTES past this gate only if every field below
is answered, cited, and internally consistent. A construction that answers
some fields and leaves others as "not yet supplied" is not a failure — it
is accurately `PARTIAL`, and should be logged as such, not rounded up.

## The 7 required fields

### F1 — Background

**Must state:** the exact manifold and metric ansatz. Already frozen by
this project: `S³×S⁶` (dim 3+6=9 internal, +4 spacetime = 13 total,
`RESEARCH_STATUS_REPORT.md`'s own 2026-07-17 correction). A candidate
construction may reuse this unchanged, or explicitly propose a
modification — but if it modifies the background, it must state whether
`N_gen=3`'s own S⁶-only chain (G73/G74A/G74B, independent of this program)
is preserved or affected.

**Pass criterion:** background stated explicitly, with an explicit
yes/no on whether it's the frozen `S³×S⁶` product or a named modification.

### F2 — Twist

**Must state:** which bundle is twisted, and by what. Already frozen:
twisting only on `S⁶` (`D_{S⁶,twisted}`, dim-1 kernel per channel, round59/
dolan-casimir), `S³` left untwisted in the paper's own baseline
(`D_{S³}^{\mathrm{LC}}`).

**Pass criterion:** states explicitly which factor(s) carry a nontrivial
twist in the candidate construction, and whether this matches or departs
from the frozen baseline.

### F3 — Torsion family [RESOLVED, round113, 2026-07-17]

~~Two DIFFERENT parameterizations already exist in this project and must
not be silently conflated~~ — **resolved: they are the same connection.**
`preprint.tex`/round67-68's `D_{S³}(t)=D_{S³}^{\mathrm{LC}}+(t-\tfrac12)h_H`
(Kostant Dirac-operator shift) and round99/round111's curvature
`R^t(X,Y)Z=t(t-1)[[X,Y],Z]` are both built from the **literal same
connection**, `∇^t_X Y = t[X,Y]` — round113 verified this directly by
reading round99's own script (`e26_toy_Vt_curvature_double_well.py` lines
63-89), which explicitly defines `nabla_t(X,Y,tt)=tt*[X,Y]` and derives its
`R^t` from it — not a coincidental match of two independently-asserted
formulas. Mandatory skeptic review initially found this only one-
directionally verified (round113's own script showed `∇^t⟹R^t`, not that
round99 itself used that `∇^t`); closed by the direct source-read above.
`t=0,1` in both conventions refer to the SAME physical (flat,
left/right-invariant) configuration; `t=1/2` in both is the SAME
Levi-Civita point. See
`experiments/20260717-round113-t-convention-reconciliation/decision.md`
for the full verification chain and the residual bi-invariant-metric-
compatibility caveat (stated explicitly in both original sources, not
independently re-verified here).

**Pass criterion (now satisfied by citation):** any future construction
may cite round113 directly rather than re-deriving this reconciliation.

### F4 — t-selection mechanism (the central question)

**Must state:** the specific action/symmetry/anomaly/topology principle
that selects a specific `t` value (or forces `t=0` and `t=1` together)
rather than leaving it as an arbitrary choice.

**Already tried and found insufficient** (see `OPEN_BLOCKERS.md` OB1,
`CURRENT_STATE_ROUND111.md`): external string-worldsheet analogies (rounds
86-89, formula-matched but mechanism didn't transfer); Pati-Salam gauge/
anomaly forcing (rounds 90-112, fully computed within `G_eff`, no forcing
found in any mixed-`U(1)_Y` channel; cubic non-abelian channels
`[SU(2)_{L,R}]³` still untested); gate G97 closes the standard product-
manifold SU(4) realization entirely (rounds 102/108/109).

**Pass criterion:** names a mechanism NOT already in the above list, or
explicitly names which item above it is extending and states the new
structural argument that distinguishes it from the already-failed version
(per `feedback-mechanism-transfer-gate-2026-07-17`'s 6-field gate).

### F5 — Fermionic Dirac operator

**Must state:** the exact operator, `D_full` or its replacement, and its
relationship to the background/twist/torsion choices above. Already
frozen (baseline): `D_full² = D_{S³,t}²⊗1 + 1⊗D_{S⁶,S⁻}²` (E2/E12), with
KT-8's own finding that this has NO zero mode at the Levi-Civita point
(`t=1/2` in the `h_H` convention).

**Pass criterion:** operator stated explicitly (not just "a modified
operator"), and its zero-mode structure computed, not assumed.

### F6 — Background equations

**Must state:** what equations of motion (if any) the candidate
background/torsion configuration is required to satisfy. **Currently: none
have been derived for this program** — round111 computed a bare curvature
scalar `Scal(∇^t)`, explicitly NOT the same as a derived action's
Euler-Lagrange equation (its own honest scope note). This is the single
largest gap in the whole OB1 program.

**Pass criterion:** an actual action principle is named (Einstein-Cartan,
Chamseddine-Connes-Marcolli spectral action, or another explicitly cited
framework) and its equations of motion are derived or cited, not merely
gestured at.

### F7 — Stability

**Must state:** whether the selected configuration(s) are stable under
small perturbations of the torsion parameter, the background metric, or
the gauge content. **Currently: not checked at all** for any candidate in
this program.

**Pass criterion:** an explicit perturbative check (e.g. second-variation
sign, spectral gap under a symbolic small parameter) is performed, not
assumed from the existence of a critical point alone.

## For OB2 specifically (spectral-triple architecture) — 6 additional fields

If the candidate construction is a non-product/twisted spectral triple
(Connes-style `(A,H,D)`, round103's still-open fork), it must ALSO supply:

| Field | Status in round110's toy attempt |
|---|---|
| Algebra `A` | Not stated beyond the finite matrix model |
| Hilbert space `H` | `H_block=ℂ²⊕ℂ²`, a toy, not the intended continuum space |
| Dirac operator `D` | `D_block=diag(0,0,3c/2,3c/2)`, self-adjoint, trivially bounded (finite matrix) |
| Grading `γ` | Not checked |
| Real structure `J` | Not checked |
| Physical interpretation | Not stated — what does each block physically represent? |

**Pass criterion for OB2:** all 6 fields stated and the standard NCG axiom
checklist (first-order condition, orientability, Poincaré duality,
KO-dimension) checked — round110 only partially addressed 2 of these
(construction + swap-symmetry), explicitly flagged as such.

## How to use this gate

1. Before starting a new OB1 or OB2 round, fill this checklist's fields for
   the SPECIFIC construction being proposed — as a section in that round's
   own `claim.md`, referencing this file, not copying it.
2. Any field left `NOT SUPPLIED` must be stated as such explicitly in the
   round's own verdict — do not round a `PARTIAL` construction up to
   `PROMOTE`.
3. F3's convention-reconciliation check is flagged as the single highest-
   priority item to resolve FIRST, independent of which of OB1/OB2 is
   pursued — both directions currently risk silently mixing two different
   `t`-parameterizations without knowing it.

## What this gate does NOT do

1. Does NOT propose a parent action itself — purely a checklist.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT supersede `claim.md`'s own per-experiment template — this is a
   program-level gate, one level above a single experiment's kill
   criterion.
