# C211 Decision — CSDR gravity-moduli potential for S6=G2/SU(3)

**Date:** 2026-10-02
**Verdict:** PASS_NEW_INPUT — new, externally-anchored number computed for F6; does NOT close F6.

## Results [VERIFIED-numpy]

```
dim(g2) = 14, dim(su3) = 8, dim(complement) = 6     [matches G96/C210 exactly]
[complement,complement] spanned by su3+complement:   residual = 8.74e-16  (PASS, < 1e-9)
max|f^a_bc| (coset-coset-coset structure constant):  0.458320             (nonzero -> non-symmetric, as expected)

Term1 = sum_ace (f^a_ce)^2        = 8.000000
Term2 = 2 sum_acd f^c_da f^d_ca   = -16.000000
Term1 + Term2                      = -8.000000
Term2 / Term1 (normalization-invariant) = -2.000000 exactly
```

`experiments/20261002-c211-csdr-moduli-potential-g2su3/results_c211.json`.

## What this is

Eq. (4.27) of Chatzistavrakidis-Manousselis-Prezas-Zoupanos (arXiv:0712.2717,
full text fetched via `mcp__arxiv__download_paper`, not abstract-only) gives
the metric-moduli scalar potential for a Coset Space Dimensional Reduction
over `S/R`, with the gravity-only (non-gauge-sector) piece built entirely
from the coset's own `[complement,complement]` structure constants:

```
V_gravity-only propto  gamma_ab gamma^cd gamma^ef f^a_ce f^b_df  +  2 gamma^ab f^c_da f^d_cb
                        = Term1                                      Term2
```

The paper states explicitly these two terms are nonzero ONLY for
non-symmetric coset spaces. `S6=G2/SU(3)` is the field's own standard
example of a non-symmetric (nearly-Kahler) coset — so these terms are a
genuine, computable gravity-sector quantity, not vacuous, for THIS project's
S6 factor. Both terms were evaluated directly on G96/C210's own already-
certified generators (14 g2 generators from the octonion-derivation
condition, 8-dim su(3) stabilizer of e6, 6-dim complement already shown by
G96 Step 5b to be an SU(3) representation 3+3bar) — no new generator
construction, reusing the exact same basis-splitting code (verbatim copy
of G96's `main()` Steps 4/4b, not an independent re-derivation that could
silently diverge).

## Clean-number check (research-methodology.md Principle 6 — degeneracy)

Term1=8, Term2=-16 are suspiciously clean integers. Checked: this is NOT a
coincidence needing a degeneracy warning in the sense Principle 6 guards
against (two DIFFERENT formulas giving the same number) — it is one formula
evaluated once. What IS true, and is stated honestly in `claim.md` §4: the
ABSOLUTE values 8/-16/-8 are an artifact of the specific normalization
choice (Frobenius-orthonormal complement basis, i.e. gamma_ab=delta_ab at
"unit radius") — rescaling the complement generators by a factor `s` scales
Term1 by `s^2` and Term2 by `s^2` identically (both are degree-2 in `f`,
which is itself linear-homogeneous in the generators), so the RATIO
Term2/Term1 = -2 exactly is the one normalization-INVARIANT number here,
and is what should be quoted/compared against any future independent
computation of this same quantity.

## Relationship to existing project results (explicitly NOT claimed)

- Does NOT relate to round111's S3 Ricci scalar `Scal(t)=24t(1-t)` — that
  is a DIFFERENT coset factor (S3, not S6) and a different object (full
  Einstein-Hilbert curvature of a 1-parameter metric family, not a CSDR
  moduli-potential structure-constant contraction).
- Does NOT relate to C134/C207's ECSK torsion+metric EOM — different
  formalism entirely (algebraic torsion sourced by fermion zero modes vs.
  CSDR's own gravity-modified Kaluza-Klein ansatz with a separate gauge
  sector). No claim that C211's V and C134/C207's torsion EOM must agree,
  disagree, or are even talking about the same action.
- DOES relate, as the closer and more honest comparison: C132's P11 used
  the SAME family of formula (Forgacs-Manton CSDR potential) but on S3's
  PURE-GAUGE "part (i)" term, never the gravity-modified non-symmetric-
  coset term C211 computes, and never on S6. No overlap in content.

## Kill Analysis (per Falsification Ladder — both kill conditions in claim.md)

**What was killed:** nothing — both kill conditions (basis-completeness
residual, Term1 nonzero) passed, so the claim survives as stated.
**What this does NOT establish:** see claim.md §"What this does NOT mean"
(4 items) — most importantly, this is ONE term of a larger effective
Lagrangian (eq. 4.26), not a complete action for F6, and the absolute
numbers are normalization-dependent (only the ratio -2 is invariant).

## Next step this motivates (not started here)

The THIRD term of eq. (4.27) (the gauge-sector contribution,
`4 e^{2*beta*phi} gamma^ab f_iac f^ic_b`) requires fixing an explicit
embedding of this project's SU(3) into a higher-dimensional gauge group —
this project has never fixed that gauge group for the S6 factor (the
closest candidate is the spectral-action framework referenced in G29/G54's
own pearls, not yet connected to CSDR). That is a SEPARATE, larger task,
not attempted here — flagging it rather than silently leaving the
potential "half computed" without saying so.

## Status

`PARENT_ACTION_GATE.md` F6 section updated with this result (superseding
the earlier, less-targeted CSDR citation added 2026-09-28, which cited the
pure-gauge Forgacs-Manton/Kapetanakis-Zoupanos papers — this result uses
the gravity-aware extension instead, the directly relevant one for F6).
