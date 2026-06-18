# HYP_01-EXT — Claim: S³×S¹ volume conservation generates flux-modulus coupling

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** On S³×S¹ with constant 4-volume (R_S3³·R_S1 = V_0), the KK flux
energy is

  V_eff(φ) = 3·N_S3² · exp(−φ/2)  +  N_S1² · exp(+3φ/2)

and has a discrete interior minimum at

  φ* = ln(N_S3 / N_S1)

where φ is the compactification modulus (measures R_S3/R_S1 with V_0 fixed),
N_S3 is the flux quantum on the S³ cycle, N_S1 on the S¹ cycle.

The coupling between the two terms — the feature that creates the minimum —
arises entirely from the volume constraint, with no free parameter.
HYP_01 (origin/main) required an ad-hoc κ; here κ is fixed by topology.

**Check:** `python hyp01ext_s3s1.py` → `PASS_HYP01EXT_S3S1_FLUX_MODULUS` (5/5)

**Verified (numpy + scipy):**
- C1: φ* = ln(N_S3/N_S1) matches scipy.minimize_scalar to ≤1e-5 (5 cases) [VERIFIED-scipy]
- C2: ∂V/∂φ = 0 and V'' > 0 at φ* → genuine interior minimum [VERIFIED-numpy]
- C3: Falsifier — decouple S¹ → dV/dφ < 0 everywhere → no minimum [VERIFIED-numpy]
- C4: φ*(N_S3=N_S1) = 0 (equal fluxes → equal radii, symmetric point) [VERIFIED-numpy]
- C5: V_S3/V_S1 = 3 at φ* for all (N_S3, N_S1) — universal equipartition [VERIFIED-numpy]

**Mechanism (why topology fixes the coupling):**
Volume conservation R_S3³ · R_S1 = const forces R_S3 = exp(φ/4) and
R_S1 = exp(−3φ/4). This 1:−3 ratio in the exponents is the coupling.
The S³ term pulls φ toward −∞ (expand S¹), the S¹ term pulls toward +∞ (expand S³).
They balance at φ* = ln(N_S3/N_S1), a flux-ratio condition.

**Equipartition at φ*: V_S3/V_S1 = 3 universally**
At the minimum, the S³ modes carry exactly 3× the kinetic energy of the S¹ modes.
The factor 3 = l(l+2)|_{l=1} is the lowest S³ eigenvalue, not a dimension count.

**What this adds over HYP_01:**
| | HYP_01 | HYP_01-EXT |
|---|---|---|
| φ*/λ* | numeric ≈ −0.303 | closed-form ln(N_S3/N_S1) |
| Coupling parameter | ad-hoc κ | none — from R_S3³R_S1=const |
| Falsifier | κ=0 decouples | R_S1=const decouples |
| φ dependence | generic f(λ) | derived from S³×S¹ topology |

**Caveat / What this does NOT mean:**
1. φ is NOT Tom's free coupling λ. They are different objects in different sectors.
   This experiment says nothing about λ — λ remains a free parameter (security constraint).
2. Does NOT claim φ is fixed in the full quantum gravity/compactification sense.
   This is a toy kinetic model — no dilaton, curvature, or backreaction included.
3. Does NOT make claims about S³ global structure conclusions (WAIT for Tom on rows 17+19).
4. Does NOT imply the Standard Model gauge couplings are fixed by this mechanism.

**Inputs:** BG-H1 (S³×S¹ KK bridge); HYP_01 (origin/main, flux stabilization)

**Status:** PASS_HYP01EXT_S3S1_FLUX_MODULUS [VERIFIED-numpy+scipy, 2026-06-18, 5/5]
