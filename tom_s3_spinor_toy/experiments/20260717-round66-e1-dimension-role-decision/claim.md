# E1 — What is the physical role of S³? (dimension/role decision matrix)

## Stakes
Internal-only (audit note feeding a preprint correction), external-facing
once acted on (blocking item for the paper's own dimension count).

## Question type
Descriptive — classifying which of 4 candidate roles for S³ is actually the
one operative in the paper's own existing derivations. Not causal, not
predictive.

## Claim (falsifiable)
Exactly one of the four candidate roles for S³ —
(1) genuine physical internal KK-compactification factor,
(2) gauge-fibre of a principal bundle (no independent spinor KK tower),
(3) parameter/moduli space (non-dynamical),
(4) part of the finite (NCG) spectral geometry (not a continuous manifold factor)
— is consistent with ALL of the paper's own already-stated substantive
derivations. If more than one is consistent, or if none is, the claim is
falsified and the dimension question requires a different framing than a
single-role pick.

## Method
Grep every place `preprint.tex` uses S³ in a load-bearing way and check which
role(s) that usage requires. Four independent load-bearing usages identified:

| preprint.tex location | What it requires of S³ |
|---|---|
| L189 (Lawrence spin-connection-as-gauge mechanism, SU(2)_L×SU(2)_R from SO(4) isometry via KK reduction) | Role 1 (genuine KK reduction of a physical factor) — Lawrence's mechanism is specifically about a compact factor's OWN spin connection becoming a 4D gauge field upon dimensional reduction, which presupposes S³ is a bona fide reduced dimension, not merely a fibre label |
| L973-982 (Freund-Rubin 3-form flux "on S³", $V_\text{flux}\propto C^3/\rho_6^{12}$, explicit "10D SUGRA limit" language) | Role 1 exclusively — Freund-Rubin compactification is the textbook mechanism for a genuine compact manifold threaded by flux; it is not meaningful for a gauge-fibre, moduli space, or finite spectral factor |
| KT-8 (this audit, 2026-07-16/17; `D_full² = D_{S3}²⊗1 + 1⊗D_{S6,E}²`) | Role 1 exclusively — the product Dirac operator argument requires S³ to contribute its own continuous spinor KK tower with a genuine spectrum, which only role 1 supplies |
| L289 ("10-dimensional Dirac spinor... decomposes under SO(4)×G₂") | Ambiguous framing — conflates the *dimension of the SO(4) spinor representation* (4 complex components) with a *spacetime dimension count*, independent of which role is chosen |

## Kill criterion
If any two of the three load-bearing usages (Lawrence mechanism,
Freund-Rubin flux, KT-8) require *different, mutually incompatible* roles →
claim is falsified, and the paper's internal role assignment is genuinely
inconsistent (not just mislabeled), requiring a structural fix, not a wording
fix.

## What this does NOT mean
Does not itself resolve KT-1 (parent action for the twist) or KT-8 (full
operator zero mode) — it only decides which physical picture those items
should be stated relative to. Does not prove the dimension label "10D" is
wrong in every possible future version of the theory — only that it is
inconsistent with the specific mechanisms this paper currently uses.
