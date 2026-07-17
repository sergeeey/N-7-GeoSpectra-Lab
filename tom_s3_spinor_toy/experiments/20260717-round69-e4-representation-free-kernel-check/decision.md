# Round69-E4 Decision — BLOCKED_BASELINE_CALIBRATION_FAILED (status corrected 2026-07-17)

**Date:** 2026-07-17
**Status-correction note (same day):** originally labeled this a "NULL /
INCONCLUSIVE" result. Corrected per this project's own Verification
Substrate Gate concept (`falsification-ladder.md` Step 2a: "test could not
run ≠ claim failed"): the target claim `dim ker(D_S6⊗S⁻)=1` was never
actually tested — the pipeline failed at baseline calibration, before
reaching the twisted operator at all. This is a **substrate/tooling
failure**, not a NULL result about the target claim, and must not be
recorded as evidence against it (or for it). Canonical status:
`BLOCKED_BASELINE_CALIBRATION_FAILED` — target claim status is unchanged
from before this experiment (`UNTESTED` by this specific method, not
`REJECTED` or `FALSIFIED`).

**Verdict: the representation-theory-free direct-diagonalization attempt did
NOT reach a calibrated, trustworthy computation of even the UNTWISTED
reference spectrum, and therefore was NOT extended to the twisted operator
(the actual claim). This is reported as a genuine BLOCKED (substrate-gate)
result per the Kill Criteria fixed in claim.md before running — not a
downgraded PASS, and not a NULL about the target claim.**

---

## What was actually built and verified

`round69_e4_direct_construction.py`, run start to finish, output captured:

**Part 1 — explicit Clifford algebra (fully verified, [VERIFIED-tool]
throughout, `pytest`-style assertions in the script itself, all passed):**
- Cl(6): 6 explicit 8×8 gamma matrices (Kronecker products of Pauli
  matrices), Clifford relations {γᵢ,γⱼ}=2δᵢⱼI verified by direct symbolic
  computation for all 36 (i,j) pairs.
- Chirality operator γ₇ = i·γ₁γ₂γ₃γ₄γ₅γ₆: verified Hermitian and γ₇²=I.
- Chirality projectors Π± = (I±γ₇)/2: verified rank 4 each (these are S⁺,
  S⁻ — matches DIM_S6_SPINOR=8 split 4+4 used in g73/g74a).
- Ambient Cl(7) radial element Γ(x)=Σxₐγₐ (a=1..7, with γ₇ playing the role
  of the 7th generator — the standard "extra Clifford generator = chirality
  element" trick): verified Γ(x)²=|x|²I exactly, symbolically.

This part is genuinely representation-theory-free: nothing above references
SU(3), G₂, weights, characters, or Casimir values. It is pure Clifford
algebra (fixed matrices) plus elementary vector algebra.

**Part 2 — exact sphere-moment calculus + Galerkin construction (verified
self-consistent):**
- Closed-form moment formula for ∫_{S⁶} x^α dσ (classical Gaussian-type
  integral, Gamma-function ratio) — self-check `7·⟨x₁⁴⟩ + 2·C(7,2)·⟨x₁²x₂²⟩
  = 1` verified exactly.
- Built the full 64×64 (8 monomials {1,x₁,…,x₇} × 8-dim Clifford fibre)
  Galerkin matrix for the UNTWISTED operator, symbolic in one free
  normalization constant K standing in for the hypersurface
  (Gauss–Weingarten) connection's mean-curvature-correction coefficient.

**Part 3 — calibration scan (the actual test): FAILED to reproduce the
known spectrum.**

Known target (already used and cited by G74A's own script, Bär 1996 /
Camporesi-Higuchi 1996): untwisted D_S6 eigenvalues = ±(k+3), k=0,1,2,… —
so the lowest mode must give exactly ±3.

Scanning K over all half-integers in [-8,8]: the matrix's nonzero
eigenvalues satisfy **eigenvalue² = K·(K+6) exactly**, confirmed
numerically at every K tried (including a clean rational hit: K=2 gives
eigenvalue=4 exactly, since K²+6K-16=(K-2)(K+8)=0). But **no rational K in
this family gives eigenvalue=3**: K²+6K-9=0 has irrational roots
-3±3√2. At the textbook-motivated coefficient K=n/2=3 (from the standard
Weingarten-correction coefficient c=1/2, K=c·n), the predicted eigenvalue is
√27=3√3≈5.196, not 3.

## Kill Analysis (per Anti-Overfitting Gate, mandatory for any NULL)

**What this NULL kills:** the specific from-scratch hypersurface-connection
formula `∇ψ = ∂ψ + K·Γ(x)ψ` used here, AS PARAMETRIZED (single free scalar
K multiplying Γ(x) with the sign/order convention coded), does not
reproduce the known spectrum for any natural K. This is a **tooling
failure**, not a claim about the manifold or the physics.

**What this NULL does NOT kill:**
- The underlying target claim dim ker(D_S6⊗S⁻)=1 is untouched — nothing
  here bears on it either way.
- The general STRATEGY (ambient Clifford trivialization + hypersurface
  connection + Galerkin projection) is not shown wrong — the clean,
  reproducible algebraic relation eigenvalue²=K(K+6) found at every scanned
  K shows the PIPELINE is internally consistent and doing something
  coherent; it is very unlikely to be random noise or a gross coding bug
  (a genuinely broken matrix would not produce a clean quadratic relation
  across 30+ independent substitutions). The likely fault is a normalization/
  sign convention mismatch in the connection formula itself (most probable
  candidate: this construction uses the "positive" Clifford signature
  (Γₐ²=+I); most Riemannian-geometry Dirac-operator references use the
  negative signature (Γₐ²=-I), and the Gauss–Weingarten correction-term
  coefficient does not simply flip sign under that change — it would need
  re-derivation, not just a sign flip, which was not done here).
- The degree≤1 truncation itself, independent of the K-calibration issue,
  showed severe collapse (nullity 48 of 64 at K=2) — meaning even a
  correctly-calibrated K might need a higher-degree truncation (degree≤2 or
  3) to give a trustworthy, non-artifact-dominated eigenvalue count. This
  was not attempted (see Relaxation Map).

**Relaxation Map (single-assumption changes, per Minimal Relaxation Rule):**

| Assumption | Relax to | Cost |
|---|---|---|
| Clifford signature Γₐ²=+I | Rebuild with Γₐ²=-I (standard Riemannian convention) and re-derive the connection formula's coefficient from scratch under that signature | Moderate — most promising single fix |
| Degree≤1 truncation | Extend to degree≤2 (36 raw monomials, rank-deficient Gram matrix from the sphere relation Σxᵢ²=1, needs pseudo-inverse or explicit SVD-based basis reduction) | High — real implementation effort, ~2-3x the code already written |
| Single free scalar K | Allow a more general ansatz (e.g. two independent coefficients for the two terms currently tied together) | Moderate |
| Connection formula derived by hand | Re-derive via a symbolic computer-algebra cross-check against a KNOWN worked example (e.g. S² or S³, where the closed-form spectrum is elementary and widely tabulated) before attempting S⁶ | Low-moderate — good next first step, smaller sanity check |

## Rescue Review

Formulation killed: the SPECIFIC coefficient-calibration of this hyper-
surface-connection ansatz, at degree≤1 truncation. Not `hard_killed` — the
general strategy is `parked`, pending the Relaxation Map fixes above.
`weak_alive` status (promotable to `alive` with AOG) would require actually
implementing one of the relaxations and getting a clean calibration; not
done here given the effort already invested in this pass.

## Second, smaller, not-attempted alternative (documented for continuation)

The task's own fallback option 2 (a different formula/route entirely, e.g.
octonion-structure-constant recomputation) was scoped but not implemented:
S⁶'s G₂/SU(3) structure can be built bottom-up from the standard octonion
multiplication table (Fano-plane structure constants, e.g. Baez 2001 "The
Octonions" §2.2), from which the isotropy Lie algebra su(3)=Stab(x₀)⊂g₂ and
its action on T_{x₀}S⁶ can be computed by direct commutator/nullspace linear
algebra — recomputing G74A's Casimir input (4/3) from raw structure
constants rather than looking up "C₂(fundamental of SU(3))=4/3" from a
formula table. This is smaller in scope than a full operator diagonalization
(no PDE-style truncation/Galerkin machinery needed) and would give a
genuinely different (though still adjacent-to-representation-theory, since
"find invariants/eigenvalues of a Lie-algebra action" is the same style of
move round59 already used) partial cross-check of one load-bearing number.
Flagged as the most promising next step; not started here due to time.

## Skeptic-style self-audit (asymmetric, applied to this experiment itself)

- **Is "representation-theory-free" actually true of what was achieved?**
  Yes for Part 1 (Clifford algebra) and the calculus in Part 2 (sphere
  moments are a classical Gaussian-integral fact, not branching/character
  theory). The construction never invoked SU(3) weights, G₂ Dynkin labels,
  characters, or Casimir eigenvalues. Honest residual: choosing "degree≤1
  polynomials on S⁶" as the truncation space is *equivalent to* (though
  never computed via) the SO(7) spherical-harmonic classification of
  L²(S⁶) — a deep structural fact about the function space that IS
  representation-theoretic at heart, even though the computational method
  used here (raw monomials, exact calculus, linear algebra) never
  references it explicitly. This residual is flagged honestly per the
  task's explicit instruction, not hidden.
- **Could the NULL itself be a bug that would show a false PASS if fixed
  trivially?** Possible but the clean, reproducible eigenvalue²=K(K+6)
  relation across 30+ independent K substitutions is strong evidence the
  pipeline is coherent, not randomly broken — a real coding bug (e.g. wrong
  matrix indices) would much more likely produce numerically messy,
  non-algebraic eigenvalue patterns, not a clean quadratic relation.

## Consequence

- Headline claim dim ker(D_S6⊗S⁻)=1: **UNCHANGED**. This experiment neither
  supports nor undermines it — it documents that an independent,
  representation-theory-free re-derivation is harder to achieve tractably
  than the task's framing suggested, which is itself the honest finding
  requested.
- The project's existing representation-theoretic verification stack
  (G73 index theorem + G74A Lichnerowicz/Schur + round59 three routes)
  remains the only currently-validated evidence for dim ker=1. Per the
  brainstorm's own critique, this stack's routes share the SU(3)/G₂
  branching-rule assumption as common ground — that residual dependency
  is NOT resolved by this experiment.

## Recommendation

1. Do NOT update preprint.tex, README, or any existing experiment folder on
   the basis of this result (per task constraints; also nothing here
   changes any existing verified claim).
2. If this line of attack is revived: start with the Clifford-signature fix
   (Γₐ²=-I) and validate on S² first (2-sphere, elementary tabulated
   spectrum, much cheaper sanity check) before returning to S⁶.
3. Alternatively, the octonion-structure-constant route (documented above)
   is smaller in scope and may be more tractable as a next independent
   check of G74A's Casimir input specifically.
4. Pearl candidate (impact 3/10, `[CANDIDATE]`, `next_check` = whenever this
   line is revived): the ambient-Cl(7)-trivialization + Gauss-Weingarten
   connection technique used here (Parts 1-2 of the script) is a reusable,
   verified, representation-theory-free building block for ANY future
   attempt to diagonalize an operator on S⁶ directly — independent of
   whether the specific K-calibration in this pass is ever fixed.

## Files

- `claim.md` — frozen before running, kill criteria intact, none forced.
- `round69_e4_direct_construction.py` — runnable, self-contained (sympy +
  numpy only), prints the full Part 1/2/3 trace including the honest
  verdict at the end. Re-run: `python round69_e4_direct_construction.py`.
