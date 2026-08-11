# decision -- bridge extends to all 3 channels (real); monodromy test is a tautology (self-caught, not reported as evidence)

## Verdict

`STEP1_BRIDGE_EXTENDED_VERIFIED__STEP2_MONODROMY_TAUTOLOGICAL_SELF_CORRECTED__ROUND118_CONDITIONS_STILL_OPEN`
-> **P1 CONFIRMED. P2 CONFIRMED (but see caveat -- itself a consequence of construction, not
surprising). P3 VOID -- caught as a tautology before being reported as a finding.**
**Date:** 2026-08-11 · L0: descriptive · scripts: `c71_step1_triality_bridge.py`,
`c71_step2_triality_monodromy.py`; results: `results_c71_step1.json`,
`results_c71_step2.json`.

---

## Step 1 results, all [VERIFIED-numpy]

| Channel | max_residual (Phi solve) | \|det(Phi)\| | hom_dim | explicit intertwining residual |
|---|---|---|---|---|
| channel_s | 4.44e-16 | 1.0000 | 6 | 5.31e-16 |
| channel_c | 1.78e-14 | 1.0000 | 6 | 5.03e-16 |

Same machine-precision signature as C70's channel_v result. **The round59<->G102 su(3)
bridge extends to all three triality channels**, each independently verified via C70's
full pipeline (direct solve + positive/negative Gate-3 controls, reused unmodified).

## Step 1b -- single Phi bridges to all three channels

Reusing the SAME `Phi` (solved once, only against channel_v) to build `M_k`, and searching
for intertwiners to channel_s and channel_c directly (no independent re-solve): **succeeds
for both**, `hom_dim=6` in each case. **Caveat, checked directly and confirmed:** this is
NOT a surprising or new physics fact. `compute_structure_tensor(gens_v)`,
`compute_structure_tensor(gens_s)`, `compute_structure_tensor(gens_c)` are **literally
identical tensors** (`max diff = 2.2e-16`, verified directly) -- because G102's
`restrict_to_subalgebra` builds `v_out/s_out/c_out` as three different REPRESENTATIONS of
the *same* 8 abstract `su(3)` generators (`stabilizer_basis(der)`), not three
independently-normalized copies. Any `Phi` solving the abstract structure-constant match
against one channel trivially satisfies it against all three, by construction. Reported
honestly as expected, not claimed as a discovery.

## Step 2 -- the monodromy test is void (Kill Analysis)

**What was attempted:** interpret `V_cv @ V_sc @ V_vs` (the composite of the three found
representation-space intertwiners, chained around the full triality cycle) as a test of
round118's condition (iii), "triality acting purely as `1⊗t` with no admixture." A first
numerical run found the monodromy scalar `c = 1.0000000 - 4.2e-17j` (i.e. the monodromy IS,
to machine precision, the exact identity), robust across four independent random-seed
choices for the underlying intertwiner search (`(0,0,0)`, `(1,2,3)`, `(7,13,99)`,
`(42,43,44)` all gave `c=1.000000` with residual `~1e-15`).

**Why this is void, not a finding:** by construction,
```
V_cv @ V_sc @ V_vs = (U_v U_c^-1)(U_c U_s^-1)(U_s U_v^-1)
                    = U_v (U_c^-1 U_c)(U_s^-1 U_s) U_v^-1
                    = U_v U_v^-1 = Identity
```
**This is a pure matrix-algebra telescoping identity.** It holds for ANY three invertible
matrices `U_v, U_s, U_c`, regardless of what they represent -- su(3) intertwiners,
arbitrary noise, anything invertible. The seed-robustness check (which DID rule out one
specific failure mode -- that "identity" was an artifact of `search_nonzero_intertwiner`'s
particular random-search bias converging to the same representative every time) was the
right instinct but the wrong question: the correct check, done only after the numerics
looked suspiciously clean (skeptic-triggers.md Trigger 1: exact "1.000000" is exactly the
shape that demands verification before trusting it), was direct algebraic inspection of how
`V_vs`, `V_sc`, `V_cv` were DEFINED -- which immediately shows the cancellation. **This
construction cannot distinguish a genuine triality symmetry from three arbitrary invertible
matrices; it has zero discriminating power and supplies zero evidence for or against
condition (iii).**

**Lesson recorded (matching this project's own precedent, e.g. C70's unconstrained-solve
trap):** when a composite quantity is built by CHAINING intertwiners end-to-end
(`A B^-1 · B C^-1 · C A^-1`), check for telescoping cancellation algebraically BEFORE
running any numerics, not after. A clean numerical result across multiple random seeds is
consistent with either "real structure" or "the test is definitionally incapable of
producing anything else" -- seed-robustness alone cannot distinguish these; only inspecting
the construction can.

## Kill Analysis

**What this kills:** the specific "chain the three intertwiners around the cycle" approach
to testing round118's condition (iii) -- shown to have no discriminating power, not
salvageable by re-running with different controls (the telescoping is unconditional).

**What this does NOT kill:** round118's condition (iii) itself remains genuinely open --
this round supplies no evidence toward it either way. Step 1's bridge-extension result
(channel_s, channel_c intertwiners found and verified) stands, unaffected by step 2's
failure -- it did not depend on the monodromy construction.

**What survives, as a genuinely scoped next step:** a test of "no admixture" that isn't a
tautology would need to compare the composite intertwiners against an INDEPENDENTLY
specified reference (e.g. an explicit triality automorphism of `so(8)`/`Spin(8)` acting on
the ambient space that `v_out/s_out/c_out` were restricted FROM, checked against whether
`V_vs` etc. actually equal that reference map) -- not simply checking self-consistency of a
closed loop, which is vacuous by construction. Not attempted here; would need the explicit
`so(8)` triality outer-automorphism, not yet located in this codebase.

## What this does NOT show

1. Does **not** resolve round118's sufficiency conditions (i)-(iii) at the 32-dim
   `H_matter` level -- genuinely still open, no progress made on them by this round despite
   the "full rigorous" ambition; the gap (no S⁶-zero-mode-to-SM-content embedding exists in
   this project) is a real gap, not closed by a clever reuse of C70's 8-dim data.
2. Does **not** change `N_gen=3`'s CONDITIONAL status.
3. Does **not** invalidate C70 -- C70's own bridge (round59<->channel_v) and this round's
   extension (channel_s, channel_c) are genuine, Gate-3-verified, non-tautological results
   at the su(3)-module level. What fails is a SPECIFIC attempted USE of that data (the
   monodromy), not the underlying bridge data itself.

## Reproduction

```
python experiments/20260811-c71-triality-bridge-extension-and-mixing-test/c71_step1_triality_bridge.py
python experiments/20260811-c71-triality-bridge-extension-and-mixing-test/c71_step2_triality_monodromy.py
```
Step 2's script prints the monodromy scalar and unitarity defect, with inline comments
now correctly labeling which parts of the output are Schur-forced (block-diagonal, scalar
on the 3/3bar) vs which were believed informative before the tautology was caught (the
overall-identity result). Kept in the repo for the documented negative lesson, not deleted.
