# E3 — Decision

**Date:** 2026-07-17
**Verdict:** PASS_DECOUPLING_SURVIVES_TORSION_DEFORMATION — but does **not** close KT-8
**Go/no-go:** OPEN — genuinely useful result, one of two remaining gaps before this candidate
mechanism (E2 + E3 combined) could even be considered for `preprint.tex`; the other gap
(physical selection of t) is untouched and is the harder one.

## Result

The KT-8 product-decoupling identity `D_full^2 = D_S6^2(x)Id_S3 + Id_S6(x)D_S3^2` survives
**exactly** (decoupling residual ~1e-15 to 1e-16, machine epsilon) once S3's factor is replaced
by the torsion-deformed `D_S3(t)` from E2, for every t tested (0, 0.25, 0.5, 1) and for two
structurally different D_S6 test operators. It also survives for an **arbitrary random
Hermitian D_S3 completely unrelated to the torsion family** — confirming the reasoning in the
task prompt: the cross-term in the Sire-Xu expansion is `{chi6,D_S6}(x)D_S3`, which vanishes
iff `{chi6,D_S6}=0` alone (a fact about chi6 and D_S6, the S6 factor's own chirality operator
and Dirac operator, that has nothing to do with D_S3). D_S3 never enters that condition. This
means the decoupling was never fragile — it holds for *any* self-adjoint operator standing in
for the S3 factor, torsion-deformed or not, physically motivated or not.

**Regression check (internal consistency, not a new result):** at t=0.5 (Levi-Civita) with the
single-generator D_S6 test operator (scaled to eigenvalue 0.185, matching KT-8's own reported
test value), this from-scratch construction reproduces KT-8's published
`min|eig(D_full)| = 1.5113689` to 3.6e-6 — confirms this independent rebuild (no script from
KT-8's own second pass survives in the repo; grep confirmed zero hits before starting) is the
same construction, not a different or miscalibrated one.

**The key numeric consequence (answers the prompt's question (b)):** at t=0 (E2's crossing,
where `D_S3(0)` has exact eigenvalues {0, -3}), `min|eig(D_full)|` drops from the Levi-Civita
floor of 1.5114 down to **exactly the D_S6 test operator's own smallest eigenvalue** (0.185 for
the single-generator variant, 0.2088 for the projector variant) — the S3 floor is **removed**.
At t=0.25 (a generic, non-crossing value, sanity check), `min|eig(D_full)| = 0.7725 =
sqrt(0.75^2 + 0.185^2)` exactly matches the decoupling formula's prediction — confirming the
formula correctly interpolates between the floor-present (t=0.5) and floor-absent (t=0,1) cases,
not just at the two special crossing points.

Full evidence (script + `results_e3.json`):
- Cl(3), Cl(6) Clifford relations: exact, residual = 0.0 (entries are all in {0,+-1,+-i}, no
  floating-point rounding at all for these particular matrices).
- chi6 properties (Hermitian, chi6^2=Id, anticommutes with all 6 generators): all confirmed,
  residual = 0.0.
- Cl(9) 9-generator assembly (45 unordered pairwise relations): all confirmed, residual = 0.0.
- Decoupling residual across all (t, D_S6-variant) combinations and the arbitrary-D_S3 check:
  max 1.78e-15 (machine epsilon for these particular ~O(1)-scale 16x16 complex matrices).
- `predicted_min_from_decoupling_formula` (computed purely from D_S3's and D_S6's own
  eigenvalues via `sqrt(a^2+b^2)`) matches the actual numerically-diagonalized
  `min_abs_eig_d_full` to <1e-9 in every single case tested.

## Why this is NOT a resolution of KT-8 (the reason for OPEN, not GO)

1. **The physical-selection gap is untouched and is the harder problem.** This experiment
   answers a purely structural/mathematical question (does the decoupling formula survive) with
   a clean, unconditional YES. It supplies **zero** additional physical motivation for why t=0
   (or t=1, or any crossing) should be the value nature/this project's ansatz actually picks over
   t=1/2 (Levi-Civita, the round/default choice). E2 already flagged this as the harder,
   unresolved half of the problem (the FITTED-vs-DERIVED trap, same pattern as the
   G56/lambda=0.30 lesson this project's own methodology calls out); this experiment does not
   move that needle at all. Until a principled selection argument exists, "ker(D_full)=0 or
   != 0" is not actually a fixed fact about this project's geometry — it is a fact about a
   free parameter t whose physical value is unknown.
2. **The D_S6 test operators are flat Clifford-algebra stand-ins, not the real physical
   operator.** Neither of the two D_S6 variants used here (single-generator, projector) is a
   reconstruction of the actual curvature-twisted differential Dirac operator on S6 whose exact
   zero mode was established in G73/G74A (ind=1 per channel). That operator involves genuine
   covariant-derivative/curvature data far beyond a flat point's Clifford algebra, and
   reconstructing it is out of scope here (it is G73/G74A's own already-completed job). The
   logical chain "decoupling holds (this experiment) + D_S3(0) has exact zero (E2) + D_S6,twisted
   has exact zero (G73/G74A) => D_full has exact zero at t=0" is a valid deduction from three
   independently-verified facts, but it is a **deduction**, not a fresh direct computation of
   `ker(D_full)` with the real operator plugged in. That direct computation (assembling the
   actual G73/G74A twisted operator into this same 16-dim Cl(9) framework and diagonalizing) has
   not been done and would be the natural next, stronger check.
3. **Symmetric-space presentation caveat carries over unchanged from E2.** The torsion freedom
   used here depends on S3 = SU(2)/{e} (Lie group presentation), not the symmetric-space
   presentation (SU(2)xSU(2))/SU(2)_diag, which has zero deformation freedom. Nothing in this
   experiment changes that; it is inherited from E2 as-is.
4. **Consistency with the rest of the project's construction remains unexamined** (NCG spectral
   triple G18+, Freund-Rubin flux setup) — same open item E2 already recorded.

## Scientific significance

This closes exactly the one specific gap E2's own decision.md flagged as its "single largest
open item" (item 1: does the product-decoupling formula survive a torsion-deformed S3 factor?)
— and the answer is a clean, structurally unconditional YES, stronger than what was asked:
the decoupling formula turns out to depend on **nothing at all about D_S3** (not on it being
Levi-Civita, not on it being from the torsion family, not even on it being self-adjoint in any
particular basis — any Hermitian 2x2 matrix works). This is a genuinely new, useful structural
fact: the KT-8 cross-term-vanishing argument was never actually about "S3's operator has no
zero mode" — it was entirely about "chi6 anticommutes with its own factor's operator," a fact
that was already known to be general (KT-8's own third-pass literature confirmation already
noted `{omega_M1,D_M1}=0` is dimension-general, not S6-specific) but had not been explicitly
exercised against a genuinely different D_S3 before this experiment.

## Kill Analysis (per this project's own Anti-Overfitting Gate — recorded even though this is
not a REJECT, matching E2's own practice of recording this section for a PASS-not-NULL result)

- **What this result rules out:** the possibility that KT-8's decoupling argument secretly
  depended on some property of the Levi-Civita S3 operator specifically (e.g. its exact
  eigenvalue spectrum, or torsion-freeness) rather than purely on the S6-side chirality fact.
  It does not.
- **What remains unresolved:** (a) whether the real curvature-twisted D_S6,twisted operator,
  actually plugged into this same Cl(9) framework rather than stood in for, still gives an
  exact zero at t=0 (very likely, given the decoupling now holds unconditionally, but not
  literally re-verified with the real operator here); (b) whether any t value is physically
  selected rather than merely mathematically available — completely open, unaddressed by
  either E2 or this experiment.

## Recommended next action

If this line is pursued further: (a) plug the actual G73/G74A twisted D_S6 operator (not a flat
Clifford-algebra stand-in) into this same 16-dim Cl(9) framework and confirm
`min|eig(D_full)|=0` exactly at t=0/t=1, closing the one remaining "stand-in vs real operator"
gap noted in item 2 above; (b) look for an independent physical selection principle for t
(same open item E2 already recommended — has anyone in this project's own conventions ever
picked t=0 or t=1 for an unrelated reason? no evidence of this currently). Until (b) especially
is done, do not cite this experiment (combined with E2) as closing KT-8 in `preprint.tex` or
any report — the mathematical obstruction is removable, but removability is not the same as
"removed for a stated physical reason," and this project's own CLAUDE.md explicitly forbids
exactly that kind of FITTED-for-DERIVED substitution.
