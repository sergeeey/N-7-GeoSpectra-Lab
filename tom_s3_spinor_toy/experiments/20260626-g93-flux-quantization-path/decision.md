# G93 Decision — Flux quantization as path constraint

**Verdict: PATH_CONSTRAINT_REQUIRES_UV_INPUT**

## Key finding: V_main has NO 2D minimum

This was hidden in G91 because we restricted to the 1D slice rho3=rho6^2.
In the full 2D space:

  dV_main / d(ln rho3) = -3 * V_main / rho3

At the AdS region (V_main < 0) this derivative is POSITIVE everywhere.
V_main monotonically decreases as rho3→0. No 2D minimum exists.

**The G91 "minimum" is a constrained minimum on the 1D path — not a 2D critical point.**

## EFT validity verdict

| Minimum | rho3 | rho6 | Status |
|---|---|---|---|
| G91 (on path, no Casimir) | 1.3902 | 1.1791 | MARGINAL (rho6<1.5) |
| G92 (Casimir, off path) | 0.3207 | 1.7051 | **INVALID** (rho3 < 1) |
| G93 (all N3,N6 scanned) | ≤0.30 | 1.26–2.30 | **INVALID** (rho3 hits bound) |

G92 and G93 minima are both in the sub-stringy regime. Supergravity EFT
breaks down for rho < 1. These results are NOT physically reliable.

## What flux quantization does and doesn't do

- **Does:** shifts rho6_min (larger N6 → larger rho6_min, as expected)
- **Doesn't:** pull rho3 into the EFT-valid regime (rho3 > 1)
- Root cause: V_s6flux ~ n6^2/rho3^3/rho6^12 doesn't change the rho3 gradient

No integer (N3, N6) pair in {1,2,3}×{0,1,2,3,4} produces a minimum
with rho3 > 1 and rho3/rho6^2 ≈ 1.

## Physical conclusion

**The path rho3=rho6^2 cannot be dynamically enforced by:**
- The main potential V_main alone (no 2D min at all)
- Casimir energy of form C/rho3^4 (min at sub-stringy rho3)
- Additional S6 flux quanta N6 (same problem in rho3 direction)

**The path constraint must come from the UV theory — from Tom's ansatz:**
- Likely: a symmetry relation between S3 and S6 radii in the full string/M-theory
- Possibly: constraint from Dirac quantization of higher-form fluxes not captured here
- Or: the path was a parametric choice and the true physical minimum is elsewhere

## What this means for the prediction

| Scenario | ratio m_mod/m_KK |
|---|---|
| G91 (on path rho3=rho6^2, 1D) | 0.198% — our best EFT result |
| G92 (off path, Casimir, 2D) | 0.39% — BUT EFT invalid |
| G93 (flux scan, all invalid) | N/A — all sub-stringy |

**Best current prediction: 0.198% from G91 (only EFT-valid result).**
The uncertainty is ±factor 2 from GA1 (lambda) and an unknown factor
from the path constraint origin.

## Open items transferred

1. **What enforces rho3=rho6^2?** Needs Tom's Part 4/5 input on the full
   compactification geometry. Cannot be answered within current 2D EFT.

2. **S3 stabilization in EFT regime?** Need a stabilizing term that:
   - Creates a minimum at rho3 > 1 (not at rho3=0.32)
   - Doesn't require rho3=rho6^2 to be imposed externally
   Candidate: non-perturbative contribution from S3 wrapped D-branes
   (exp(-vol_S3) ~ exp(-rho3^3) → creates minimum at large rho3).

3. **G94 candidate:** D-brane instanton on S3: A_NP2 * exp(-B * rho3^3)
   (analogous to the S6 non-perturbative term in G91, but acting on S3).
   This would be the S3 analogue of the KKLT superpotential.
