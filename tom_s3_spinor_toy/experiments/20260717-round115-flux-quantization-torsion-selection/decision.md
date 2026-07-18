# Round115 — Decision

**Date:** 2026-07-17
**Verdict:** `NULL_FOR_UNCONDITIONAL_SELECTION__GENUINE_CONDITIONAL_(T,RHO3)_CORRELATION__SUGGESTIVE_NOT_CONFIRMED_NEAR_INTEGER`
(skeptic: `CONFIRMED` overall NULL, with two documented weakenings + one gap,
both addressed below before finalizing)

**Go/no-go:** identifying the S³ torsion with a genuine, quantized H-flux
does **not**, on its own, select `t=0,1` over any other value — this
restates (does not close) `PARENT_ACTION_GATE.md` F6. But the mechanism
supplies a real, non-vacuous, falsifiable conditional relationship between
`t` and `ρ₃` (not previously stated in this project), and a numerical
check against this project's own candidate `ρ₃` value (G94) lands
suggestively — though not confirmably — close to selecting `t=0,1`.

## What was computed [VERIFIED-tool: sympy, this round]

1. `Vol(S³_ρ)=2π²ρ³` confirmed by direct integration (standard formula).
2. Schematic quantization condition `(2t-1)·c·Vol(S³)=2πnQ` solved for
   `t(n,ρ₃)`.
3. **Circularity test:** for target `t∈{0,1,1/3,7}`, a real positive `ρ₃`
   solving the condition exists for **every** target — the mechanism does
   not distinguish `t=0,1` from arbitrary other values without an
   independent fix on `ρ₃`.
4. **c, directly recomputed** (not assumed): `c:=⟨[Z₁,Z₂],Z₃⟩=-2` in the
   `Z_i=iσ_i`, `⟨X,Y⟩=-½Tr(XY)` frame — the same frame round99/111/113 use.

## Skeptic review [context-asymmetric: claim.md + code only] — three findings, all addressed

**Finding 1 (gap — addressed):** the round only proved "∃ρ₃ for any target
t" (trivial) and skipped the sharper, physically relevant check: does a
*naturally motivated* `ρ₃` give an integer `n` at `t=0,1` specifically?
**Addressed:** re-ran with `ρ₃=1.9281`, this project's own candidate value
(`experiments/20260626-g94-s3-np-instanton/decision.md`, grep-confirmed),
and `Q=(2π)²` (α'=1 natural units, standard NS-NS convention). Result:
`K=|c|·π·ρ₃³/Q ≈ 1.1408` — 14% from the nearest integer. **Not an exact
match**, but not wildly off either.

**Finding 2 (label undersold real content — addressed):** the mechanism
gives a genuine `(t,ρ₃)` correlation curve, not a vacuous restatement.
Stated explicitly in the corrected verdict: **conditional** on future
`ρ₃`-stabilization, this formula would predict specific allowed `t` values
— real, falsifiable content, just not yet actionable since `ρ₃` isn't
independently fixed.

**Finding 3 (uncited "unstabilized" claim — addressed, and the claim was
actually WRONG as originally stated):** grep confirmed this project does
**not** treat `ρ₃` as fully free — G94 (`decision.md`, gates G94-G102)
found a **candidate** D2-brane-instanton stabilization mechanism, giving
`ρ₃≈1.928-1.93`. This is itself explicitly caveated by that file's own
line 76: *"Does NOT prove c_S3=0.235 is the physical value — this is a
free coupling."* **Net effect:** `ρ₃` is not "fully free" (my original
framing was too strong, corrected here), but the one candidate value that
exists is itself conditional on an admittedly free coupling — so the
underlying circularity concern is not resolved, only **pushed back one
level**, and compounded: the `K≈1.14` near-miss rests on THREE stacked,
independently-unverified inputs (the torsion=flux identification itself;
the specific `Q=(2π)²α'` normalization, recalled not tool-verified for
this exact construction; and G94's own coupling-conditional `ρ₃`).
Tuning any ONE of these three could move `K` to exactly 1, or away from
it, with equal ease — this is a numerological-coincidence risk, explicitly
**not** presented as confirmation.

## Applying the corrected verdict

Kill criterion's `NULL, restates F6` branch is met for **unconditional**
selection (the original circularity concern stands). But per the
skeptic's Finding 2, "restates F6, does not close it" **undersells** the
actual content — corrected to explicitly name the genuine conditional
`(t,ρ₃)` relationship and the suggestive-but-unconfirmed `K≈1.14` finding,
rather than dismissing the round as fully vacuous.

## Kill Analysis

- **What this kills:** the naive hope that flux quantization alone,
  without further input, picks out `t=0,1`. It does not — any target `t`
  admits some `ρ₃`.
- **What this does NOT kill:** the torsion-as-flux identification itself
  (untested, not refuted); the possibility that a FUTURE, independent
  `ρ₃`-stabilization result (not G94's own coupling-conditional one) could
  make this formula predictive.
- **What survives, sharper than before:** a precise, falsifiable formula
  (`t=½+Qn/(2πcρ₃³)`) relating `t` and `ρ₃`, plus a documented, honest
  numerical near-miss (`K≈1.14` at G94's own candidate value) — worth
  revisiting if `ρ₃` is ever independently pinned down by a mechanism NOT
  itself resting on a free coupling.

## Relaxation Map (future work, not attempted here)

| Option | What it would require |
|---|---|
| Independently derive `ρ₃` (not conditional on a free coupling like G94's `c_S3`) | A genuinely new stabilization mechanism — the actual open problem `preprint.tex` already names |
| Tool-verify the exact `Q=(2π)²α'` NS-NS quantization normalization for THIS specific construction | Read a primary SUGRA/string-flux-quantization source directly (WebFetch/pymupdf), not recalled from memory |
| Independently justify the torsion=flux identification itself | Requires an actual action principle connecting the Cartan-Schouten torsion to a physical NS-NS 3-form — the same F6 gap, one level down |

## What this does NOT mean

1. Does NOT establish or refute the torsion-as-flux identification.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. `lambda`'s own flux-based origin (G83-G86B,
   same Hodge-corollary flux, different role — sourcing the exponential
   suppression, not the S³ Dirac-operator torsion) remains closed and
   untouched by this round.
3. Does NOT claim `K≈1.14` as evidence for anything — explicitly flagged
   as a numerological-coincidence risk, not a finding to build on without
   independent verification of all three stacked inputs.

## Check (reproduces this decision)

```
cd experiments/20260717-round115-flux-quantization-torsion-selection
python e37_flux_quantization_check.py
```
Expect: `vol_S3_formula_confirmed=True`, real-positive-root exists for all
4 target `t` values in Part 3, `c=-2` (Part 4), `K≈1.1408` (14.1% from
nearest integer).
