# Claim — Round99 (B4 from goal-expansion-100): Toy V(t) From Curvature,
Double-Well Plausibility Check

**Question type:** Descriptive (classical differential-geometry
computation + a toy-model plausibility check — NOT a full spectral-action
derivation, which remains B1, unattempted).

## Section 1 — Background

Goal-expansion-100's B1 proposes treating `t` as a dynamical modulus with
potential `V(t)`, hoping for a double-well shape (minima at `t=0,1`) that
would give a domain-wall/coexistence picture. B4 is the cheap
plausibility check BEFORE attempting B1's full spectral-action derivation:
does ANY natural, non-arbitrary curvature-based quantity already produce
this shape, using only the family's own classical geometry?

**Reused fact (established elsewhere in this project, not re-derived
here):** the Cartan-Schouten family `∇^t_XY = t[X,Y]` (for left-invariant
`X,Y`) is flat at `t=0` and `t=1`, and equals the (curved) Levi-Civita
connection at `t=1/2`.

## Section 2 — What this experiment computes (new this round)

The curvature `R^t(X,Y)Z` of `∇^t` as an explicit function of `t`, for
`X,Y,Z` = the `su(2)` generators used elsewhere in this project
(`Z_i=iσ_i`, `experiments/20260717-round67-e2-s3-torsion-deformation/
e2_s3_torsion_deformation.py:100-107`), via DIRECT matrix computation of
`∇^t_X∇^t_Y Z - ∇^t_Y∇^t_X Z - ∇^t_{[X,Y]}Z`, not merely the classical
Jacobi-identity argument (`R^t=t(t-1)[[X,Y],Z]`) stated symbolically.

## Section 3 — Pre-registered criteria

- **CONFIRMED (double-well plausible):** `R^t` is verified to vanish at
  `t=0,1` and be nonzero at `t=1/2` (consistent with the already-
  established flat/curved facts), AND a natural curvature-penalty
  quantity `V(t) ∝ ‖R^t‖²` is shown to have `V(0)=V(1)=0 < V(t)` for all
  `t∈(0,1)`, i.e. a genuine double-well with minima exactly at the two
  torsion-escape-route endpoints.
- **REFUTED:** `R^t` does not vanish at `t=0,1` (would contradict this
  project's own established "flat" fact — a red flag requiring
  re-verification of a prior result, not acceptance of this one), or the
  resulting `V(t)` does not have minima at `t=0,1` specifically.

## Section 4 — What this does NOT claim

- Does NOT derive `V(t)` from the actual spectral action (Chamseddine-
  Connes-Marcolli formalism) — that is B1's full task, unattempted here.
  `‖R^t‖²` is a PLAUSIBLE, standard ingredient of a gravitational action
  (Einstein-Hilbert-squared / Gauss-Bonnet-type term), not a proven
  component of THIS project's specific spectral action.
- Does NOT claim `t` is physically dynamical — this is a toy-model
  plausibility check, `[HYPOTHESIS]`-level throughout.
- Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
  `safe_for_runtime=False`.
