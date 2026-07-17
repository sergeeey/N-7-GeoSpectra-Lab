# E11 — Claim: is the preprint's Freund-Rubin S³ flux the physical source of T^t?

**Date:** 2026-07-17
**FL tier:** [x] Full (bridges two previously-separate parts of the paper —
moduli stabilization §"Modulus Stabilization" and today's torsion-deformation
line E2/E7/E9/E10; project CLAUDE.md requires Full tier for research claims)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: is the already-existing Freund-Rubin 3-form flux on S³ (used for
modulus stabilization in `preprint.tex` §"Modulus Stabilization") structurally
and/or physically the source of the torsion `T^t = (2t-1)[X,Y]` studied in
E2 (`experiments/20260717-round67-e2-s3-torsion-deformation/`), and does the
existing flux quantization/EOM machinery in this project select `t=0` or
`t=1` (the two Cartan-Schouten flat values E2/E7 found)?

## Stakes

Internal-only. This is an open exploratory bridge between two previously
unconnected parts of the paper (moduli stabilization and the E2/E3/E7/E9/E10
torsion-deformation line), not promoted to `preprint.tex` here.

## Background (established, not re-derived here)

- `preprint.tex` line 985-989 (§"Modulus Stabilization"): "The flux-induced
  potential from a Freund-Rubin 3-form flux on S³ is: `V_flux(ρ3,ρ6) ∝
  C³/ρ6^12`, where `C = g2²/g3² = 15ρ3³/(16πρ6^6)`." This is a **scalar
  effective-potential term**, not an explicit component-level 3-form.
- `experiments/20260621-g54a-freund-rubin/decision.md` (F1/F2, PASS/VERIFIED):
  `V_flux = 15q²ρ3³/(16πρ6^6)` "matches geometric formula `q²×Vol(S³)/(2Vol(S⁶))`"
  and `V_flux(q=1) ≡ g2²/g3²` — an *exact structural equality* between the flux
  energy density and the spectral-action gauge-coupling ratio, both derived
  from `Vol(S³)/Vol(S⁶)`. Also established there (F3/F4): the flux quantum `q`
  is a free multiplicative input never solved for by any EOM in this project;
  the existing minimum condition (`dV/dρ6=0`, `eq:min-cond` in `preprint.tex`)
  fixes `ρ6` (or the ratio `κ=ρ6,min/ρ6*`), not `q` and not any torsion-like
  quantity.
- `preprint.tex` line 1107-1112: by Künneth, `H³(S³×S⁶;ℝ)=ℝ⊕0=ℝ` since
  `b_3(S⁶)=0`; "the harmonic 3-form flux threading S³ is topologically
  quantized and scales as `Vol(S³)/Vol(S⁶)`." This confirms the flux lives in
  `H³(S³)` — a 1-dimensional cohomology group — consistent with (but not
  identical to) the pointwise statement that `Λ³((ℝ³)*)` is 1-dimensional.
- E2/E7 (`experiments/20260717-round67-.../`, `experiments/20260717-round72-.../`):
  the torsion `T^t=(2t-1)[X,Y]` on S³=SU(2)/{e} has zero-mode crossings at
  `t∈{-2/3,-1/3,0,1,4/3,5/3}` (n=0,1,2); the n=0 pair `{0,1}` is independently
  singled out by full-curvature flatness (`R^t=0 ⟺ t(t-1)=0`, the two
  Cartan-Schouten connections) — but **no physical selection principle between
  t=0 and t=1, or for the torsion magnitude in general, has been established**
  (E7's H2/E8 gate: a generic curvature²+torsion² action has `t=1/2` as an
  unconditional stationary point, and `t=0,1` only if the torsion-energy term
  is dropped by hand — `b=0`, an ad hoc choice).
- `preprint.tex` line 1467-1497 (existing "S³ torsion deformation" open-problem
  item) already states: "no physical principle is known for selecting `t=0`
  ... over the Levi-Civita value `t=1/2`" and "the crossing values are also
  convention-dependent (torsion normalization, orientation, ...)."

## Claim (three falsifiable sub-questions, each independently gated)

**Q1 (structural type match):** Is `T^t`, as a trilinear antisymmetric object
on S³=SU(2), the SAME KIND of geometric object as the Freund-Rubin flux used
in `preprint.tex`'s moduli section — i.e. is each a multiple of the SAME
1-dimensional generator of invariant 3-forms on S³ (the volume form), rather
than two structurally unrelated objects (e.g. the flux being purely a
volume-form/scalar quantity unrelated to the specific bracket-built
antisymmetric structure `g([X,Y],·)` that defines torsion)?

**Q2 (physical flux→torsion mechanism):** Does a known physical mechanism (in
the standard Freund-Rubin/flux-compactification literature, or in this
project's own normalization) relate a 3-form flux's magnitude/quantization to
the torsion it would source on the same manifold — and if so, is that
mechanism currently wired into `preprint.tex`, or would it require a NEW
normalization/coupling not currently in the paper?

**Q3 (selection of t=0/t=1 specifically):** Would the EXISTING Freund-Rubin
flux quantization/EOM condition already used in `preprint.tex` (which fixes
`ρ6` via `dV/dρ6=0`), if applied to a torsion-sourcing role, single out `t=0`
or `t=1` specifically — or some other value, or no value at all without
further, currently-absent input?

## Kill criterion (MANDATORY — filled BEFORE running)

| Sub-question | PASS | FAIL | OPEN | ILL-POSED |
|---|---|---|---|---|
| Q1 | `T^t` proven (symbolically, all 27 basis triples) to be an exact scalar multiple of the standard volume-form/Levi-Civita symbol on the orthonormal frame, matching the flux's own volume-form origin (`Vol(S³)`) | `T^t` is NOT expressible as a multiple of the volume form (would require off-diagonal / non-eps structure) | — | — |
| Q2 | A specific, already-existing (not newly invented) normalization in `preprint.tex` directly equates a flux quantity to `(2t-1)` or an equivalent torsion-magnitude parameter | grep of `preprint.tex` for torsion/contorsion/H-flux/connection-deformation finds ZERO wiring between the flux and any connection/torsion object outside the already-known, already-caveated E2/E3 item | A generic mechanism (H-flux-sources-contorsion, standard in flux compactifications) exists in the wider literature, is structurally plausible given Q1, but is NOT currently implemented in this paper's normalization and would require new machinery to instantiate | The identification requires a convention choice with no canonical resolution from data already in the paper |
| Q3 | The existing `dV/dρ6=0` condition (or a natural one-line extension of it) can be shown to evaluate to `t=0` or `t=1` without new fitted inputs | The existing EOM structure demonstrably fixes a DIFFERENT quantity (`ρ6`, or `q` unconstrained) and, by direct extension of E7's own E8-gate finding, a generic torsion-energy term does NOT robustly select `t=0,1` without ad hoc coefficient cancellation | A plausible but unverified path exists requiring substantial new machinery (e.g. a 2-flux system, G54-A's own flagged G54-D follow-up) | — |

**Explicit escape route:** this is a one-session, definitional/consistency
analysis plus two cheap, concrete symbolic checks (Q1's volume-form
proportionality, Q2's `Vol(S³)/2Vol(S⁶) = 15/(16π)·ρ3³/ρ6^6` identity). It does
NOT attempt to derive a new torsion-sourcing Lagrangian or solve a new EOM —
that would be a separate, larger follow-up (flagged in decision.md if the
verdict here motivates one). A "the connection requires new machinery not in
the paper" verdict is an accepted, valid, non-forced outcome per the task's
own explicit framing — this experiment does NOT attempt to manufacture a
positive connection where the definitions do not cleanly support one.

## Method

1. Read `preprint.tex`'s Freund-Rubin flux definition/normalization in full
   (`§"Modulus Stabilization"`, plus the Künneth/`b_3(S⁶)=0` remark and the
   coupling-ratio derivation `§"Gauge coupling ratio prediction"`) — DONE, see
   decision.md for exact line citations.
2. [VERIFIED-tool] Build S³'s structure constants (E2/E7's own convention,
   `c=2`, orthonormal frame) and compute `T^t(e_i,e_j,e_k)=(2t-1)⟨[e_i,e_j],e_k⟩`
   for all 27 ordered triples; verify total antisymmetry and that `T^t` is
   EXACTLY `(2t-1)c` times the standard Levi-Civita/volume-form symbol (i.e.
   the only independent component is `T^t(e1,e2,e3)`) — `round75_freund_rubin_torsion_link.py`.
3. [VERIFIED-tool] Independently re-derive, from the standard n-sphere volume
   formula (`Vol(S^n)=2π^{(n+1)/2}/Γ((n+1)/2)·ρ^n`), that
   `Vol(S³)/(2·Vol(S⁶)) = 15ρ3³/(16πρ6^6)` exactly — confirming G54-A's own
   claim that the paper's flux coefficient `C` traces back to `Vol(S³)`, the
   integral of the SAME volume form `T^t` is a multiple of.
4. [VERIFIED-tool] `grep -ni "torsion|contorsion|H-flux|NS-NS|connection deformation"`
   across the FULL `preprint.tex` to check whether any existing text wires the
   flux into a connection/torsion object anywhere outside the already-known
   E2/E3 item (which itself explicitly disclaims a selection principle).
5. Cite (not re-derive) E7's own E8-gate finding (`experiments/20260717-round72-.../decision.md`)
   on whether a generic curvature+torsion action selects `t=0,1` — directly
   relevant to Q3 since a flux-sourced torsion term would structurally be
   exactly this kind of "torsion-energy" addition to an action.
6. Synthesize Q1/Q2/Q3 verdicts in decision.md, citing exact `preprint.tex`
   line numbers and this project's own prior experiment decisions.

## What this does NOT mean

1. Does **not** derive a new EOM, Lagrangian, or torsion-sourcing mechanism.
   If Q2/Q3 come back OPEN (requiring new machinery), this experiment does
   NOT attempt to build that machinery — it only identifies precisely what
   would be needed and why it is currently absent.
2. Does **not** claim the Freund-Rubin flux and `T^t` are "the same object"
   in any dynamical sense merely because both are proportional to the S³
   volume form — Q1's PASS (if it PASSes) is flagged explicitly as a
   near-tautological consequence of `dim(S³)=3` (`dim Λ³((ℝ³)*)=C(3,3)=1`):
   ANY invariant 3-form on S³, of whatever physical origin, must be a
   multiple of the same 1-dimensional generator. This is necessary but very
   far from sufficient for a genuine flux-sources-torsion claim.
3. Does **not** touch, weaken, or promote E2/E3/E7/E9/E10's own scope caveats
   (product-decoupling generalization, H1c open, H2/E8 BLOCKED/UNDERDETERMINED).
4. Does **not** resolve the project's own open "ρ3 modulus stabilization" or
   "non-perturbative origin of λ" items (`preprint.tex` lines 1499-1524) —
   this experiment is scoped narrowly to the flux↔torsion structural question.
5. If Q1 PASSes and Q2/Q3 come back OPEN/FAIL (the expected, honest outcome
   per the task's own framing), this does NOT mean the flux↔torsion idea is
   permanently dead — it means a genuinely NEW normalization/coupling
   (e.g. explicitly writing the flux as a component 3-form entering the
   fermionic covariant derivative, à la NS-NS `H`-flux torsion in
   Strominger-Hull-type systems) would need to be introduced, which is a
   substantial new modeling step, not a re-reading of what is already in
   `preprint.tex`.

## Check

`python round75_freund_rubin_torsion_link.py` →
`verdict.q1_T_is_multiple_of_volume_form == true`,
`verdict.q2_flux_C_equals_volume_ratio_exactly == true`.
Full Q2/Q3 textual verdict recorded in `decision.md` (grep-based, not scripted).
