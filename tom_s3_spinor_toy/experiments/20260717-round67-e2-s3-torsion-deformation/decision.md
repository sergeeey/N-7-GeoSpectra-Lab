# E2 — Decision

**Date:** 2026-07-17
**Verdict:** PASS_CANDIDATE_MECHANISM_FOUND (not NULL) — but does **not** close KT-8
**Go/no-go:** OPEN — worth a follow-up gate, not yet promotable to the preprint

## Result

Contrary to the "expect NULL" framing this experiment was scoped under (see the parent audit's
KT-8 finding that S³'s Levi-Civita spectrum never reaches zero), the torsion-deformed family
D^t **does** have zero modes — in fact infinitely many, at a discrete, exactly-computable,
evenly-spaced (in n) set of t values. For n=0,1,2:

```
t*  ∈  { -2/3, -1/3, 0, 1, 4/3, 5/3 }   (n=0 gives t=0 and t=1; n=1 gives -1/3 and 4/3; n=2 gives -2/3 and 5/3)
```

This is a direct, algebraically exact consequence of one crisp structural fact, verified
[VERIFIED-tool] this session: for S³ specifically (dim m = 3), Kostant's cubic torsion element H
(Agricola, arXiv:math/0202094, eq. 5) collapses to a scalar multiple of the identity operator on
the spinor factor, because H has only one Clifford triple (Z1·Z2·Z3 = Cl(3)'s central volume
element ω, with ω²=1) — there is nothing for it to mix. This means the entire one-parameter
family D^t is just the known Levi-Civita spectrum ±(n+3/2) shifted by a single additive constant
(t−1/2)·h_H, h_H=3 (calibrated from Agricola's own Theorem 4.2 + this project's established n=0
eigenvalue 3/2). An additive shift of a discrete, symmetric, unbounded ladder crosses zero
infinitely often as t is varied — this was close to inevitable once ω was confirmed scalar, not
a delicate coincidence.

Full evidence chain (script + symbolic solve + independent numeric cross-check, all in
`results_e2.json`):
- Clifford relations for Cl(3): exact, `step1_clifford_relations_all_ok = true`.
- ω = Z1·Z2·Z3 = **exactly** the 2×2 identity matrix in this representation (not just
  proportional — literally I₂), central, ω²=I: `step2_omega_ok = true`.
- Closed-form crossings (sympy `solve`) agree with an independent dense-grid numeric root-find
  to 5.6e-17 (floating-point noise around an exact rational answer):
  `verdict.numeric_exact_cross_check_passed = true`.

## Why this is NOT a resolution of KT-8 (the reason for OPEN, not GO)

1. **Scope gap (the big one).** This experiment computes ker(D_S3(t)) for the S³ factor *alone*.
   Closing KT-8 requires the *full* 9D product operator on S³×S⁶ to have a zero mode. Whether the
   Clifford product-decoupling identity KT-8 used (`D_full² = D_S3²⊗1 + 1⊗D_S6,twisted²`) still
   holds once S³'s factor connection is torsion-deformed (not Levi-Civita) was **not**
   independently verified against literature here — Sire & Xu (the source KT-8 cites) only covers
   the Levi-Civita-on-both-factors case. The generalization is structurally plausible (the
   cross-term cancellation in that identity depends only on S⁶'s own chirality/Dirac
   anticommutation, not on what connection is used on the S³ factor) but this is [INFERRED], not
   [VERIFIED-external-source]. This is the single largest open item before this candidate
   mechanism could be called anything stronger than "candidate."
2. **FITTED, not DERIVED — same trap this project's own methodology flags elsewhere.** Finding
   that *some* t gives a zero mode is a much weaker claim than finding a *principled reason* to
   pick that t over t=1/2 (Levi-Civita, the physically default/round choice). This experiment does
   not supply that reason. Introducing torsion on the S³ factor is a real physical modification
   to the compactification (a legitimate ingredient in string-theory literature — see Agricola
   §4, Strominger's equations — but not something this project has used anywhere else), and
   picking t=0 (say) specifically to kill KT-8 would be exactly the kind of "positioning a
   minimum/zero rather than deriving a value" pattern this project's own CLAUDE.md calls out
   (the λ=0.30 vs 0.337 lesson). Any future promotion of this mechanism needs an independent
   argument for why t=0 (or whichever crossing) is the physically selected value.
3. **Symmetric-space presentation gives zero freedom.** If S³ is instead presented as the
   symmetric space (SU(2)×SU(2))/SU(2)_diag, Agricola's paper states plainly that the entire
   one-parameter family collapses to a single connection (Levi-Civita, torsion≡0 identically).
   The deformation freedom used here depends on choosing the *other* natural presentation
   (S³ = SU(2)/{e}, the bi-invariant-metric-on-a-Lie-group case) — a real, legitimate, and
   commonly-used presentation, but a choice nonetheless, and one that should be stated explicitly
   whenever this result is cited.
4. **Consistency with the rest of the project's construction is unexamined.** Whether a
   torsion-ful connection on S³ is compatible with the NCG spectral-triple construction (G18+),
   the S⁶ Freund-Rubin flux setup, or any other established gate in this project was not checked.

## Scientific significance

Regardless of whether it ends up closing KT-8, this is a genuinely new, clean structural fact
about this project's own geometry: Kostant's cubic Dirac operator is *exactly* a scalar shift on
S³ specifically (because dim m = 3 leaves only the central volume element in H), giving an exact,
closed-form, easily falsifiable family of torsion connections with S³-zero-modes. This is worth
keeping as a **pearl-registry candidate** (the "H is scalar for the smallest naturally-reductive
case" fact could recur in other odd-3-dimensional factors elsewhere in this line of research)
independent of the KT-8 question.

## Kill Analysis (per this project's own Anti-Overfitting Gate — recorded even though this is
not a REJECT, since the experiment's original framing anticipated a NULL and got a PASS instead)

- **What this result rules out:** the naive expectation that S³'s Dirac spectrum is "rigid" and
  cannot be pushed to zero by any natural deformation — it can, and the deformation needed
  (Kostant's canonical torsion family) is about as standard/non-exotic as such families get.
- **What remains unresolved:** whether this mechanism actually closes KT-8 (requires the product
  decoupling check, item 1 above) and whether any specific crossing t is physically motivated
  (item 2 above) rather than merely mathematically available.

## Recommended next action

If this line is pursued further: (a) verify the generalized product-decoupling formula for a
torsion-deformed factor directly (build the explicit 16-dim Cl(9) construction as KT-8's own
second pass did, but with S³'s factor set to D_S3(t) at, say, t=0, and check the cross-term still
vanishes to machine precision); (b) look for an independent physical selection principle for t
(e.g. does any of {-2/3,-1/3,0,1,4/3,5/3} correspond to a distinguished value elsewhere in this
project's own conventions, such as t=0/t=1 being the canonical/anticanonical — i.e. the two
*flat* connections in Agricola's classification — which is at least a more principled anchor
than an arbitrary crossing). Until both are done, do not cite this as closing KT-8 in
`preprint.tex` or any report.
