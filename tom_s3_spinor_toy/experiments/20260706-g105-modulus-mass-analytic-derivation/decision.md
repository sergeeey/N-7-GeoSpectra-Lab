# G105 Decision — Analytic derivation of the modulus-mass power law

**Verdict: PROMOTE (5/5 checks after skeptic-driven fixes)** — G103's numerically-fitted
m_mod ~ lambda^0.4928 is upgraded from FITTED to DERIVED: it is the leading-order (exactly
0.5) plus computable next-order correction of a small-lambda expansion of the SAME potential
G60/G61/G103/G104 already use. The same expansion's zeroth-order term independently
reproduces G66's kappa^2=(N+1)/N, for every N=2..10 tested — G66 and G103 turn out to be one
expansion, not two independent facts.

## G105 results [VERIFIED-python — results_g105.json, `python g105_modulus_mass_analytic.py`]

| Check | Result | Threshold | Status |
|---|---|---|---|
| D1: x0^2=(N+1)/N leading-order, N=2..10 | exact match, all 9 | float precision | ✅ |
| D2: this gate's GLOBAL fit (exact, same 9 points as G103) vs G103's own fit | 0.4913 vs 0.4928 | < 0.01 | ✅ |
| D3: independent rho_min vs every G103 sweep point | max diff 1.3e-6 | < 1e-5 | ✅ |
| D4: exponent → 0.5 as lambda → 0 | 0.4987 → 0.4995 → 0.4999 | monotonic | ✅ |
| D5: perturbative vs exact exponent at lambda=0.60 (mu~0.5, not small) | 0.4840 vs 0.4835 | < 0.02 | ✅ |

## Skeptic review (FL Step 8a) — [SKEPTIC-VERDICT: WEAKENED → response applied]

Context-asymmetric review (claim.md + code only, no session history, no reasoning chain).
Overall verdict on the FIRST pass: **WEAKENED** — "core algebra is correct, but the claim is
over-scoped and one of the four falsification checks (D2) compares mismatched quantities."
Per the Response Matrix (Fix / Accept-with-doc / Dismiss), this was NOT a kill (the skeptic
explicitly stated "core mathematical error found: none") — each concern is addressed below.

| # | Concern | Response | Status |
|---|---|---|---|
| 1 | "mu=0 stationary point" is imprecise wording — f(x,0)=0 identically for ALL x, so every x is trivially "stationary"; what's meant is lim_{mu->0} x_min(mu) from the O(mu) coefficient | **Fixed** | Reworded in claim.md and the script's module docstring to say "lim_{mu->0} x_min(mu), taken from the O(mu) coefficient of f, not from f at mu=0 itself" |
| 2 | **D2 compared a LOCAL closed-form exponent at lambda=1/3 to G103's RANGE-AVERAGED fit exponent over [0.15,0.60] — different observables that can agree or disagree independent of whether the underlying claim is true.** Strongest single objection. | **Fixed** | Added `global_fit_exponent()`: reproduces G103's own methodology exactly (log-log linear fit, EXACT non-perturbative f'', same 9 lambda points). D2 now compares fit-to-fit: 0.4913 (this gate) vs 0.4928 (G103) — the coincidence that the OLD local-at-1/3 value (also 0.4913) matched just as well is now understood: lambda=1/3 sits near the log-mean of the fit range, so the local derivative there approximates the range average — a real but incidental relationship, not the basis of the claim anymore |
| 3 | "GENERIC consequence for any N" conflates two different genericity claims: (a) algebraic — trivially true for the functional FORM, for any n; (b) physical — that an actual S^a x S^N compactification reduces to this exact potential SHAPE for N outside {6}, which is NOT independently proven here | **Fixed (scoped down)** | claim.md and the script docstring now explicitly split these: D1 is stated as algebraic genericity only. Physical genericity is attributed to G104's own (a,N)-generalized construction (already implemented in this project, empirically checked at exactly 2 points: (2,6) and (3,6)) — NOT re-derived or extended by G105. Added as explicit "does NOT mean" point 4 |
| 4 | Perturbative truncation's accuracy at the TOP of G103's fit range (lambda=0.60, mu~0.505 — not a small parameter) was previously bounded only indirectly, via D3's rho_min (potential-level) check — the mass-level (f'') accuracy specifically was unverified there | **Fixed** | Added D5: direct comparison of the perturbative (A,B) local exponent against an EXACT numerical local derivative at lambda_max — 0.4840 vs 0.4835, well within tolerance even at mu~0.5. The O(mu^2) truncation is accurate across the full range actually used, not just asymptotically |
| — | No hidden N-dependent singularity found (probe checked N=1, non-integer N, N→infinity) | Accepted as a clean negative finding | No fix needed |

Skeptic's own summary after the concerns above: *"the algebra I hand-verified matches; ...
Not FALSIFIED — no core mathematical error found."* All four fixable concerns are now fixed
in claim.md, the script, and the tests; re-running the check suite (7/7 tests, 5/5 gate
checks) confirms the fixes did not break anything the skeptic had confirmed as correct.

## Post-hoc investigation: is this a "missing puzzle piece" for another project?

Prompted by the user asking whether this result might resolve an existing cross-project pearl.
The only existing candidate bridge (cross_domain_insights.md, 2026-06-21: Buckholtz Eq.32's
(4/3) factor vs kappa^2=(n+1)/n at n=3) was investigated. Finding: **that bridge was ALREADY
tested and killed inside the Buckholtz project itself**, 2026-06-23 (`FALSIFIED-AS-MECHANISM`,
~456 other parametric families also give 4/3 — a look-elsewhere-effect kill), but the GLOBAL
memory entry (cross_domain_insights.md, shared across projects) was never updated to reflect
that — a cross-project NULL-propagation gap this project's own `null_retroscan.py` guard
cannot catch (it only scans within one project's own null_results/INDEX.md). Fixed today:
cross_domain_insights.md entry corrected from "🥈 Silver, pending" to "🪨 Stone,
FALSIFIED-AS-MECHANISM", with citations to the Buckholtz project's own pearl_registry and
DISCOVERY_GATE.md.

G105 does not revive that bridge — if anything it reinforces the original kill: D1 shows
kappa^2=(N+1)/N is algebraically generic across N=2..10, not special to N=3, which makes
hitting the specific value 4/3 (=kappa^2 at N=3) by coincidence in an unrelated formula LESS
surprising, not more. No other specific cross-project application was identified; this
result's realistic value is internal (methodological upgrade + unification for this project's
own preprint), not a cross-project bridge.

## Independent reviewer pass (post-skeptic-fix) — LGTM, 1 documentation-only finding

A second, independent reviewer (not the skeptic) checked the FIXED version and found the
skeptic's fixes genuine (not renamed/hidden), plus one new P2 finding worth recording here
rather than in a code change: the dimensionless toy potential `f(x,mu)` used by this gate and
G103's actual physical potential (with its volume/PATH_K prefactors) are only APPROXIMATELY
proportional, not exactly — `m2_mod / |f''|` drifts ~0.4% across G103's lambda range (2.0220e-6
at lambda=0.15 to 2.0303e-6 at lambda=0.60). This does not change D2's verdict (recomputing
G103's fit on full-precision m_mod gives 0.49276 vs this gate's 0.49129 — diff 0.0015, still
well under the 0.01 threshold) but means "the SAME expansion of ONE potential" (claim.md
background) is precise about the SHAPE/exponent structure, not a claim that the two
potentials' overall normalization is exactly constant. Recorded here per that reviewer's
explicit recommendation rather than treated as a blocker (0.4% is over 6x smaller than the
tolerance it would need to threaten).

## Caveats

- Does not derive lambda's value — `lambda = FREE_COUPLING_PARAMETER` unchanged.
- Does not explain the physical origin of the exp(-lambda/rho^2) functional form — G103's
  UV-mechanism NULL stands unchanged; this gate assumes the form as given.
- The exponent-0.5 result is now KNOWN to be non-diagnostic of any specific UV mechanism
  (per skeptic Probe 3 discussion): any future model with a potential of this same schematic
  shape would show the same mass law, regardless of that model's own physical origin.
- Physical genericity across N is inherited from G104's construction, checked at 2 points
  (2,6) and (3,6) — not independently extended to other N by this gate.

## Relation to prior results

- G66 (2026-06-21, PROMOTE): source of kappa^2=(N+1)/N, now understood as this expansion's
  zeroth-order term rather than a separate derivation.
- G103 (2026-07-05, PROMOTE): source of the FITTED 0.4928 exponent and the lambda-blindness
  framing this gate explains structurally.
- G104 (2026-07-05, NULL): source of the (a,N)-generalized potential construction this gate's
  "physical genericity" caveat is scoped against.

## Pearl Gate

→ pearl_registry/INDEX.md G104 row marked superseded; new G105 row added recording the
PROMOTE verdict and the corrected next-check (a pre-registered third (a,N) point testing the
PRECISION of the A,B correction formula, not the existence of the pattern — already proven).
→ cross_domain_insights.md Buckholtz entry corrected (see section above).
