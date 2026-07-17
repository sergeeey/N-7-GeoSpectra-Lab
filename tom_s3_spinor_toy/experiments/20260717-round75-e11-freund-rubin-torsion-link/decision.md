# E11 — Decision

**Date:** 2026-07-17
**Verdict:** **Q1 PASS (structural type match, tautological but real) / Q2 OPEN
(generic mechanism exists in the literature, NOT currently wired into this
paper) / Q3 FAIL-AS-POSED (no existing mechanism selects t=0 or t=1; a direct
extension of E7's own E8-gate finding predicts it would NOT, even if the link
were built).**
**Go/no-go:** Does not promote the E2/E3/E7/E9/E10 torsion-deformation line,
does not touch KT-8, does not modify `preprint.tex`'s Freund-Rubin/moduli
section. A genuinely new modeling step (not a re-reading of existing text)
would be required to pursue this further.

---

## Preliminary: exact Freund-Rubin flux definition/normalization in `preprint.tex`

Read in full (`§"Modulus Stabilization"`, lines 974-1069; `§"Gauge coupling
ratio prediction"`, lines 359-420; Künneth remark, lines 1107-1112).

- **`preprint.tex:985-989`:** "The flux-induced potential from a Freund–Rubin
  3-form flux on $S^3$ is: $V_{\mathrm{flux}}(\rho_3,\rho_6) \propto
  C^3/\rho_6^{12}$, where $C = g_2^2/g_3^2 = 15\rho_3^3/(16\pi\rho_6^6)$."
  This is a **scalar energy-density term** in an effective potential. There is
  **no explicit component-level 3-form tensor** written anywhere in the paper
  (no `F_{ijk}` or similar with free indices) — the flux enters only through
  the scalar `C`, itself defined via the gauge-coupling ratio.
- **`preprint.tex:363-371`:** `C = g2²/g3² = 15ρ3³/(16πρ6^6)` is stated as
  derived from the spectral action's gauge-kinetic normalization
  (`g2²∝1/Vol(S³)`, `g3²∝1/Vol(S⁶)`). Note for the record (flagged, NOT
  resolved, genuinely out of scope here): the naive per-factor proportionality
  as literally written would give `g2²/g3² ∝ Vol(S⁶)/Vol(S³) = ρ6^6/ρ3³`,
  whereas the stated closed form has `ρ3³` in the numerator — the reciprocal
  power pattern. This is very plausibly an artifact of the standard
  Kaluza-Klein fact that a wrapped gauge boson's effective coupling depends on
  the *other* factor's volume too (`1/g²∝Vol(\text{complement})/Vol(\text{wrapped
  cycle})`), which the schematic per-factor statement elides — but this
  experiment did not verify that reconciliation and does not need to: it is
  orthogonal to the flux↔torsion question and is taken as given, exactly as
  `preprint.tex` and `experiments/20260621-g54a-freund-rubin/decision.md`
  (F1/F2, independently `[VERIFIED]` there) both already state it.
- **`experiments/20260621-g54a-freund-rubin/decision.md` (F1/F2, PASS,
  [VERIFIED] tag in that experiment's own report):** independently confirms
  `V_flux = 15q²ρ3³/(16πρ6^6)` "matches geometric formula
  `q²×Vol(S³)/(2Vol(S⁶))`" and that `V_flux(q=1) ≡ g2²/g3²` is an "EXACT
  structural equality" — both traced to `Vol(S³)/Vol(S⁶)`. This is the most
  precise existing statement in this project of what the flux "is": a scalar
  built from the ratio of the two factors' volumes, carrying one integer flux
  quantum `q`.
- **`preprint.tex:1107-1112`:** By Künneth, `H³(S³×S⁶;ℝ)=ℝ` (since
  `b_3(S⁶)=0`), and "the harmonic 3-form flux threading S³ is topologically
  quantized and scales as `Vol(S³)/Vol(S⁶)`." This confirms the flux is
  understood, at the level of de Rham cohomology, to be valued in the
  1-dimensional `H³(S³;ℝ)` — consistent with, though not identical to, the
  pointwise fact used below that `Λ³((ℝ³)*)` is 1-dimensional.
- **`experiments/20260621-g54a-freund-rubin/decision.md` (F3/F4):** the flux
  quantum `q` is a free multiplicative input, never solved for by any EOM in
  this project ("Flux fixes the RATIO ρ3/ρ6²=C via energetics, but does NOT
  fix the scale ρ6... It is a 'ratio stabilizer,' not a 'scale stabilizer'").
  The existing minimum condition `dV/dρ6=0` (`preprint.tex` eq. `min-cond`,
  line 1019-1023) fixes `ρ6` (equivalently `κ=ρ6,min/ρ6*`, eq. G66/G62), not
  `q`, and not any torsion-like quantity.

**Conclusion of the preliminary:** the Freund-Rubin flux, as currently used
in `preprint.tex`, is a **scalar** (energy density built from a volume ratio
and an integer flux quantum), never written as an explicit component 3-form,
and never coupled to any connection/torsion object anywhere in the paper.

---

## Q1 — Structural type match: is T^t the same KIND of object as the flux?

**Verdict: PASS**, via `round75_freund_rubin_torsion_link.py`
(`results_e11.json`).

Two independent symbolic checks, both `[VERIFIED-tool]`:

1. **Torsion is a volume-form multiple.** Building `T^t(e_i,e_j,e_k) =
   (2t-1)⟨[e_i,e_j],e_k⟩` from the same structure constants E2/E7 already
   established (`c=2`, orthonormal frame, `[e_i,e_j]=c·ε_{ijk}e_k`), all 27
   ordered triples were checked exactly: `T^t` is totally antisymmetric and
   equals `(2t-1)·c·ε_{ijk}` exactly — i.e. its ONLY independent nonzero
   component (up to the antisymmetry-forced sign pattern) is
   `T^t(e1,e2,e3)=4t-2`. `results_e11.json`:
   `q1_torsion_is_volume_form_multiple.all_components_match_multiple_of_eps
   == true`, `.totally_antisymmetric == true`, `.dim_Lambda3_R3_star == 1`.
2. **The flux's own magnitude traces back to `Vol(S³)`, the integral of the
   SAME volume form.** Independently re-derived (not reusing G54-A's script)
   from the standard n-sphere volume formula: `Vol(S³)=2π²ρ3³`,
   `Vol(S⁶)=16π³ρ6^6/15`, giving `Vol(S³)/(2·Vol(S⁶)) = 15ρ3³/(16πρ6^6)` —
   **exactly** matching `preprint.tex`'s stated `C` formula, confirming
   G54-A's own claim. `results_e11.json`:
   `q2_flux_volume_ratio_check.ratio_equals_paper_C_exactly == true`.

**Honest interpretation (flagged explicitly, per the task's instruction not
to overreach):** this PASS is a **near-tautological consequence of
`dim(S³)=3`**. Since `Λ³((ℝ³)*)` (the space of totally antisymmetric
trilinear forms on a 3-dimensional space) has dimension `C(3,3)=1`, *any*
invariant 3-form on S³ — whatever its physical origin — must be a scalar
multiple of the same generator (the volume form / structure-constant-built
Cartan 3-form, which coincide for a 3-dimensional compact Lie group). The
Freund-Rubin flux (built from `Vol(S³)`, i.e. the integral of this same
generator) and the torsion `T^t` (a pointwise multiple of the same generator)
are therefore automatically "the same kind of object" in this narrow sense —
but this is forced by dimension-counting alone, not evidence of any specific
dynamical relationship between the two. **A FAIL here would have been the
informative outcome** (it would have ruled out the connection outright); a
PASS is expected and establishes only a necessary, not remotely sufficient,
condition for Q2/Q3.

---

## Q2 — Physical mechanism relating flux magnitude to torsion parameter

**Verdict: OPEN.** A generic mechanism exists in the broader
flux-compactification/string literature, but it is **not currently wired
into `preprint.tex`**, and connecting it would require new machinery.

- **Generic mechanism (well known, [DOCS]-level, not project-specific):** in
  flux compactifications with an NS-NS-type 3-form background (`H`-flux), the
  standard construction (Strominger-Hull systems, heterotic/type-II flux
  backgrounds) replaces the Levi-Civita connection with a **torsionful**
  connection `∇^± = ∇^{LC} ± (1/2)H` in the fermionic (gravitino/Killing
  spinor) sector, where the contorsion tensor is literally `∓H` — i.e. a
  3-form flux background directly sources a torsion tensor of exactly the
  antisymmetric-3-form type discussed in Q1. This is a standard, textbook-
  level fact about how flux backgrounds generate torsion; it is not
  reproduced or verified numerically here (out of scope — it is cited as
  the general mechanism that WOULD need to be invoked, not as something this
  project has established).
- **Grep of the FULL `preprint.tex` (`[VERIFIED-tool]`)** for
  `torsion|contorsion|H-flux|NS-NS|connection deformation|\nabla^t` finds:
  - All "torsion" hits outside the S³ item (lines 747, 754, 789, 823, 1320,
    1342, 1355-1356) refer to a **completely different, unrelated torsion
    correction** — the G₂/SU(3) Dolan-Casimir torsion term on **S⁶**
    (`experiments/20260708-dolan-casimir-g2su3/`), not S³, and not connected
    to any flux.
  - The only S³-torsion text (lines 1467-1497, the pre-existing "S³ torsion
    deformation" open-problem item, itself citing E2/E3) explicitly states:
    "no physical principle is known for selecting `t=0` ... over the
    Levi-Civita value `t=1/2`" and flags the crossing values as
    "convention-dependent (torsion normalization, orientation, ...)."
  - Zero hits for "contorsion," "H-flux," "NS-NS," or "connection
    deformation" anywhere in `preprint.tex`.
- **Conclusion:** `preprint.tex` currently treats the Freund-Rubin flux
  purely as a **bosonic scalar** entering the moduli potential `V_flux`. It is
  never coupled to the fermionic sector's connection, nor to any explicit
  torsion tensor, anywhere in the paper. The generic H-flux→contorsion
  mechanism cited above is structurally the RIGHT KIND of mechanism (per Q1's
  finding that both objects live in the same 1-dimensional space), but
  **instantiating it here would require a new, currently-absent
  normalization convention**: specifically, a definite proportionality
  constant relating the flux quantum `q` (an integer, fixing the coefficient
  of `H` in `H³(S³;ℤ)≅ℤ`) to `(2t-1)` (the torsion-parameter coefficient of
  the SAME generator, dimensionless in the chosen unit convention). No such
  constant is derivable from anything currently written in `preprint.tex` —
  `V_flux` is quadratic-in-flux (an energy density, `∝q²` per G54-A F1-F3),
  not linear in the flux 3-form itself, so even the SIGN of any hypothetical
  `q↔(2t-1)` proportionality is not fixed by the existing potential (a
  `V_flux∝q²` term is blind to the sign of `q`, whereas `t=0` vs `t=1`
  correspond to a genuine sign flip of the torsion, `T^0=-[X,Y]` vs
  `T^1=+[X,Y]` per E7's own decision.md).

**This is exactly the outcome flagged as expected/valid in the task
instructions:** the flux, as currently normalized, is wired only into the
bosonic potential, not the fermionic torsion sector; connecting the two would
require introducing a new coupling this paper does not currently have.

---

## Q3 — Would the existing flux EOM select t=0 or t=1 specifically?

**Verdict: FAIL-AS-POSED / NO.** Two independent, converging reasons:

1. **Directly, from what the existing EOM actually does.** The only EOM
   currently in this project's moduli-stabilization machinery
   (`dV_total/dρ6=0`, `preprint.tex` eq. `min-cond`, giving G66's
   `κ²=(n+1)/n=7/6`) solves for **`ρ6`** (a continuous compactification
   radius), not for the flux quantum `q`, and not for any torsion-like
   discrete parameter. Per G54-A F3/F4 (already established, cited above),
   `q` itself is a free input in this project, never fixed by any
   minimization — so even granting Q2's hypothetical link `q↔(2t-1)`, there
   is currently no mechanism in this paper that would evaluate `q` to any
   specific number, let alone one landing on the exact algebraic roots
   `t∈{0,1}` of `t(t-1)=0` (the Cartan-Schouten flatness condition E7
   established independently). `ρ6`-fixing and `q`-fixing are two different,
   currently-unlinked problems in this project's own machinery.
2. **By direct extension of E7's own E8-gate finding** (already run in
   `experiments/20260717-round72-e7-t-selection-principle/decision.md`,
   cited here, not re-derived): for the natural candidate action
   `F(t)=a|R^t|²+b|T^t|²` (curvature-squared plus torsion-squared, the
   generic quadratic functional a flux-sourced-torsion contribution would
   structurally resemble, since a flux-energy term is itself quadratic in
   the flux/torsion 3-form), `F'(t)=2(2t-1)[aA·t(t-1)+2bB]`. `t=1/2` is
   **always** a stationary point; `t=0,1` are stationary **only if `b=0`**
   (the torsion-energy term dropped by hand) or under special coefficient
   cancellation. A flux-sourced torsion-energy contribution is precisely a
   nonzero `b`-term of this kind — so, by this project's own already-computed
   result, adding a Freund-Rubin-flux-derived torsion-energy term to a
   generic action would **generically shift the stationary point away from
   `t=0,1`, back toward (or through) `t=1/2`**, not select `t=0` or `t=1`.
   Selecting `t=0,1` from an EOM of this generic shape requires the SAME ad
   hoc `b=0` cancellation E7 already flagged as unmotivated fine-tuning — it
   would not emerge "for free" from wiring in the Freund-Rubin flux.

**Conclusion:** No existing mechanism in this project selects `t=0` or `t=1`
via the Freund-Rubin flux. Moreover, the most natural way to build the
missing link (a quadratic torsion-energy EOM term, structurally what a
flux-sourced-torsion contribution would look like) is one this project has
ALREADY tested in a structurally equivalent form (E7's E8 gate) and found to
push the stationary point AWAY from `t=0,1`, not toward it, unless an
unmotivated coefficient is set to zero.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result rules out:** (a) that the Freund-Rubin flux and `T^t`
  are structurally unrelated types of object (Q1 — ruled out; they are both
  forced into the same 1-dimensional `Λ³` generator by `dim(S³)=3`); (b) that
  the EXISTING flux quantization/EOM machinery in this project already
  selects `t=0` or `t=1` (Q3 — ruled out directly, and by structural
  extension of E7's own E8-gate result, which shows the natural way of
  building such a link would push AWAY from `t=0,1`).
- **What remains unresolved / open:** whether a NEW, explicitly-introduced
  H-flux-sources-contorsion coupling (writing the flux as an actual
  component 3-form entering the fermionic covariant derivative, with a
  specific `q↔(2t-1)` proportionality constant fixed by an independent
  physical requirement — e.g. supersymmetry of the resulting background, a
  Strominger-Hull-type torsional-connection consistency condition) could, if
  built, select a value of `t`. This was explicitly NOT attempted here (Q2's
  "would require new machinery" finding, per the task's own scoping
  instruction) — it is a substantially larger follow-up, comparable in scope
  to H2/E8 (already flagged BLOCKED/UNDERDETERMINED in E7) or to a full
  Strominger-Hull-system construction for this specific compactification.
- **Relaxation Map (if pursued further):** the cheapest next test, in order
  of cost, would be: (a) explicitly write the flux as a component 3-form
  `F_3 = q·vol_{S3}` with a stated normalization for `q` in the SAME units
  `T^t`'s `(2t-1)` is measured in (pure bookkeeping, no new physics); (b)
  state the standard `∇^± = ∇^{LC}±(1/2)F_3` ansatz explicitly and derive
  what value of `t` it would correspond to as a function of `q` (this
  directly reuses the `(2t-1)=±(\text{const})·q` bookkeeping from (a)); (c)
  only then ask whether ANY existing or new EOM in this project would fix
  `q` to a value giving `t=0` or `t=1` — which, per this experiment's Q3
  finding, would require overcoming the generic `t=1/2`-preferring pull
  identified by E7's E8 gate, i.e. a genuinely new physical requirement
  (e.g. supersymmetry) not currently present anywhere in this project.

## Scientific significance

This experiment establishes a real, if narrow, structural fact: the
Freund-Rubin flux used in this paper's moduli-stabilization section and the
torsion `T^t` studied today in E2/E7 are FORCED, by `dim(S³)=3` alone, to be
proportional to the same geometric generator (`Λ³((ℝ³)*)`, 1-dimensional).
This is worth recording as a genuine, verified structural fact about S³
specifically — it does NOT hold for S⁶ (`Λ³` there is high-dimensional,
`dim=20`), so this is a special feature of the S³ factor, consistent with why
this project's other S³-specific mechanisms (E2/E7's torsion family, the
Kostant cubic element collapsing to a scalar for `n=3`) keep recurring in
this "n=3 is special" pattern. However, the SAME dimension-counting fact that
makes Q1 PASS also makes it a WEAK/near-vacuous PASS — it does not, by
itself, license treating the flux and the torsion as physically identified,
and this project's own already-computed E8-gate result (E7) independently
suggests that even a natural, non-ad-hoc way of wiring the two together would
push the stationary point away from `t=0,1`, not toward it.

## Recommended next action

Not started here (per the escape route in claim.md, this experiment is
scoped to the definitional/consistency analysis and two cheap symbolic
checks only). If pursued: build the explicit component-3-form flux ansatz
`F_3=q·vol_{S3}` and the standard `∇^±=∇^{LC}±(1/2)F_3` coupling as a NEW,
clearly-flagged modeling addition (not a re-reading of existing text),
following the Relaxation Map above — order (a)→(b)→(c). Until that is done,
do NOT cite "the Freund-Rubin flux sources T^t" or "the flux selects t=0/1"
in `preprint.tex` or any report; the honest current state is "structurally
the same TYPE of object (Q1, PASS, but dimension-forced and weak), no
existing coupling or selection mechanism in this project (Q2/Q3, OPEN/FAIL),
and this project's own prior E8-gate result predicts that building the most
natural such coupling would push away from t=0,1, not toward it."

## Summary table

| Sub-question | Verdict | Basis |
|---|---|---|
| Q1 — structural type match | **PASS** (dimension-forced, near-tautological) | `[VERIFIED-tool]`: T^t is an exact multiple of the S³ volume-form generator; flux's own `C` traces to `Vol(S³)/(2Vol(S⁶))` exactly, same generator (`results_e11.json`) |
| Q2 — physical flux→torsion mechanism | **OPEN** | Generic H-flux→contorsion mechanism is standard in the literature and structurally plausible given Q1, but zero wiring exists in `preprint.tex` (`[VERIFIED-tool]` grep); would need a new `q↔(2t-1)` normalization not derivable from anything currently written |
| Q3 — existing EOM selects t=0/1 | **FAIL-AS-POSED / NO** | Existing EOM fixes `ρ6`, not `q` or torsion (G54-A F3/F4); direct extension of E7's own E8-gate result shows a generic torsion-energy term pushes the stationary point away from `t=0,1` toward `t=1/2`, not toward the Cartan-Schouten values, absent an ad hoc `b=0` cancellation |
