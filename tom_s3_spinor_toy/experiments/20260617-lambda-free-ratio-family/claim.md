# Claim: λ-free ratio FAMILY — closed form generalising V-RATIO-G0's √2

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The single λ-free ratio R=√2 found in V-RATIO-G0 is one entry of a closed-form
family. For the S³ vector-operator (rank-1) raising sector j → j+1 at target weight m, the
ratio of the two matrix elements reaching m is

    R²(j, m) = 2 (j − m + 1) / (j + m)

This is λ-free for every (j,m) (Wigner-Eckart: the reduced element and coupling λ cancel in
any within-sector ratio). √2 = R(j=1/2, m=1/2).

**Check:** `python lambda_free_ratio_family.py` → `PASS_LAMBDA_FREE_RATIO_FAMILY_CONFIRMED` (5/5)

**Verification (two independent ways, [VERIFIED-sympy]):**
1. Symbolic proof for general (j,m): the CG-formula ratio reduces exactly to 2(j−m+1)/(j+m).
2. Numeric match against `sympy.physics.wigner.clebsch_gordan` at all 21 tower points (j=1/2..3): 0 mismatches.
3. √2 special case recovered (consistency with V-RATIO-G0).
4. d(ratio)/dλ = 0 confirmed.

**New λ-free predictions (beyond the known √2):**
| j | m | R² | R |
|---|---|----|---|
| 1/2 | 1/2 | 2 | √2  *(V-RATIO-G0, known)* |
| 1 | 0 | 4 | **2** |
| 3/2 | 3/2 | 2/3 | **√6/3** |
| 2 | 0 | 3 | **√3** |
| 2 | −1 | 8 | **2√2** |

**Caveat / What this does NOT mean:**
1. These are RATIOS of the S³ vector-operator matrix elements — internal structural relations.
   They are NOT predictions of a coupling constant, a mass, or any directly-observable SM quantity.
2. λ-freedom follows from the Wigner-Eckart theorem applied to this operator — it is standard
   representation theory, not a new physical mechanism. The contribution is the explicit closed
   form + the fact that it holds for THIS construction independent of the (still-free) λ.
3. Falsifiable ONLY in the sense that, if the V-operator matrix elements are computed/compared
   within a sector, these ratios must hold. Not yet connected to experiment.
4. Generalises V-RATIO-G0; does NOT fix λ, does NOT touch G6–G9 (chirality / SM content).

**Why this is delta (not restatement of √2):** V-RATIO-G0 gave one number and the principle.
This gives the GENERATING FORMULA for the whole tower (infinitely many ratios) with a symbolic
proof — a law, not an instance.

**Status:** PASS_LAMBDA_FREE_RATIO_FAMILY_CONFIRMED [VERIFIED-sympy, 2026-06-17, 6/6 pytest]
