# C71 -- triality bridge extension; monodromy approach to round118's condition (iii) found tautological

**Experiment id:** `20260811-c71-triality-bridge-extension-and-mixing-test`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C70 (round59<->channel_v su(3) bridge found, machine precision);
`experiments/20260717-round118-matter-generation-factorization-test/` (2026-07-17,
pre-existing, precisely scoped `H_physical=H_matter(x)H_generation`, WEAK reading:
necessary condition VERIFIED, sufficiency conditions (i)-(iii) explicitly UNVERIFIED)
**User direction (mid-round):** given a scope investigation found round59's D_59 is not
usable as literally described in `predictions_before_data.md` (dimension mismatch, no
J/gamma exists for it, no P_i projectors exist), the user chose to pick up round118's own
already-scoped, still-open sufficiency conditions using C70's fresh intertwiner results as
new input, rather than force the original literal plan or merge documents first.

---

## What this round actually tested

**Step 1 (valid, verified):** does C70's round59<->channel_v bridge extend to channel_s
and channel_c? Reused C70's exact pipeline (direct solve + positive/negative Gate-3
controls + explicit intertwiner verification) unmodified, swapping the target generator
set for `su3_g102_on_channel_s()`/`su3_g102_on_channel_c()` (new helper functions, same
`restrict_to_subalgebra` construction C68 already used for channel_v).

**Step 2 (attempted, found tautological -- see Kill Analysis):** a proposed
"triality monodromy" test -- compose the three found intertwiners `U_v, U_s, U_c` around
the v->s->c->v cycle (`V_vs=U_s U_v^-1`, `V_sc=U_c U_s^-1`, `V_cv=U_v U_c^-1`) and check
whether the product is a clean scalar (interpreted as "no admixture," a candidate
well-posed version of round118's condition (iii)). **This does not work as a test of
anything -- see below.**

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | `U_s`, `U_c` exist with the same machine-precision signature as C70's `U_v`, verified via the same Gate-3-controlled pipeline | pending |
| **P2** | a single `Phi` (solved once against channel_v) also bridges directly to channel_s and channel_c without independent re-solving | pending |
| **P3** | the triality-cycle monodromy `V_cv V_sc V_vs` is a clean scalar (informative, IF the construction is not itself forced to be scalar by algebra alone) | pending -- flagged in advance as the step most likely to need a triviality check before being trusted |

## kill_criterion

P1 fails if no nondegenerate `U_s`/`U_c` is found, or if either fails Gate-3 controls.
P3's interpretation is void (not merely "fails") if the monodromy construction is shown to
be a pure algebraic identity independent of any su(3)/geometric input -- this must be
checked directly (matrix-algebra inspection, not just numerics) before any interpretation
is drawn, per this project's Perelman-audit "no premature promotion" discipline.

## What this cannot show

- Does **not** resolve round118's sufficiency conditions (i)-(iii) at the actual 32-dim
  `H_matter` (G18's NCG finite Hilbert space) level -- those require an S⁶-zero-mode to
  Standard-Model-content embedding this project has not built anywhere, and this round
  does not attempt to invent one without physical motivation.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- If P3's monodromy result is void (see decision.md), this round supplies **zero** evidence
  either for or against round118's condition (iii) -- not a weak positive, not a negative,
  genuinely no information, and must be reported as such rather than smoothed over.
