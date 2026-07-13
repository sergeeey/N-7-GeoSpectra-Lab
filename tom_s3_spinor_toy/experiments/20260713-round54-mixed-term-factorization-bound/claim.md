# Round54-MixedTermBound Claim — exact factorization audit + O(√C₂) bound

**Date:** 2026-07-13
**FL tier:** [x] Standard (structural audit of already-existing code, no new representation computed, per explicit user scope)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim (user's frozen claim, verbatim scope): does the mixed
   A-B cross-term, for general irreducible ρ, factor as
   `M_ρ = Σ_p A_p ⊗ ρ(X_p)` with FIXED `A_p`, `X_p` and all ρ-dependence
   isolated in `ρ(X_p)` — and if so, does the standard compact-Lie-group
   Cauchy-Schwarz bound `‖ρ(X)‖≤‖X‖√C₂(ρ)` give `‖M_ρ‖≤K√C₂(ρ)`?
2. `decision.md` grep: done — this is the direct, same-day continuation
   of Round 53's sharpened revival condition (`parked/INDEX.md`,
   `L4B-HIGHER-REPS` row).
3. `round*_claim.md` + scripts grep: done — Round 22's own script
   (`g2su3_nomizu_crossterms.py`) is the ONLY place this construction
   exists; read in full, line by line, for this round (see Estimand).
4. `null_results/` + `parked/` grep: done, confirmed NOT the R45-Leibniz
   duplicate (same distinction established in Round 53's own claim.md —
   R45 concerns interpreting an already-computed ρ=7 residual matrix;
   this round concerns the general ρ-scaling structure of the operator
   itself, a different mathematical question).
5. `git log -S`/`-G` pickaxe: done via Round 52/53's own gates.
6. Primary source re-read: done — `g2su3_nomizu_crossterms.py`,
   `g2su3_equivariance_check.py` (`build_D_matrix64`),
   `g2su3_v7_multiplicity_dirac.py` (`clifford_left_64`, `rho7_ep`),
   `g2su3_H_element.py` (`build_T_table`, `torsion_T`) all read directly,
   line by line — not paraphrased, not assumed from function/variable
   names (per the user's own explicit warning: "нельзя предполагать по
   имени").
7. **Status:** [x] OPEN → this round.

**Correction to Round 53, found during this round's own gate/audit
(reported here, not suppressed):** Round 53 claimed Agricola 2002's
Theorem 3.2 shows the torsion-cross-term is representation-INDEPENDENT
(a fixed operator, `O(1)` in ρ). Direct code reading in this round
shows this is **not correct for this project's actual construction**:
`torsion_cross_term` (`g2su3_nomizu_crossterms.py:177-190`) has the form
`Σ_{p<q,r} T(p,q,r)·Ms[p]·Ms[q]·w(ρ_7(e_r)·v)` — it explicitly contains
one factor of `ρ_7(e_r)`, exactly the same structural shape as
`mixed_AB_term`. Agricola's bare Theorem 3.2 (for the UNTWISTED operator
on the bare spinor bundle alone) does not have an analog of this
`ρ(e_r)`-dependence, because her degree-3 term is pure Clifford
multiplication with no representation action anywhere — but THIS
project's TWISTED "matrix-coefficient section" construction (Round 17's
own formula, general for any V_ρ) genuinely re-introduces one factor of
`ρ_ρ(e_r)` when the bracket `[e_p,e_q]` is expanded, because
`ρ_V([e_p,e_q])=Σ_r T(p,q,r)ρ_V(e_r)+...` is applied to `v`, not used as
an abstract fixed Clifford element the way Agricola's untwisted case
allows. **Agricola's theorem does not directly transfer to this
project's twisted operator, contrary to Round 53's conclusion.**

---

## Estimand

**Population:** the two off-type-carrying pieces of `D_7²`'s five-piece
decomposition (Round 22): `torsion_cross_term` and `mixed_AB_term`, each
generalized from ρ=7 to an arbitrary G₂-irrep ρ by replacing every
`rho7_ep`/`rho7_nuk` call with the analogous `ρ_ρ(e_p)`/`ρ_ρ(ν_k)`.
**Intervention:** verify, by direct inspection of the ρ=7-specific code
(not by name or by assumption), whether each piece factors as
`Σ (fixed 64×64 matrix) · w(ρ_ρ(generator)·v)` with ALL ρ-dependence
isolated in a SINGLE, LINEAR application of `ρ_ρ` to a fixed Lie algebra
element.
**Comparator:** the four invariants the user specified as required for
the bound to be valid.
**Endpoint:** PASS/FAIL per invariant, and (if PASS) the general bound
`‖torsion+mixed_AB‖(ρ) ≤ K√C₂(ρ)` for some ρ-independent constant K.
**Summary measure:** structural (factorization form confirmed or not),
not a specific numeric K (K's actual value is out of this round's scope
— user's own Round 55).
**MCID:** N/A — descriptive structural audit.

---

## Claim

Both `torsion_cross_term` and `mixed_AB_term`, as actually implemented
in `g2su3_nomizu_crossterms.py` (not merely by their names), factor as
`Σ_r B_r · w(ρ_ρ(e_r)·v)` for FIXED 64×64 matrices `B_r` built entirely
from the manifold's own torsion table `T(p,q,r)` and the fixed Clifford
structure `Ms[p]`, `D64` on the 64-dimensional fibre `Σ⊗Σ` — with the
SAME structure holding when ρ_7 is replaced by a general ρ (verified
via Round 17's own general-ρ formula, `g2su3_v7_multiplicity_dirac.py`
docstring lines 10-14, which is written for generic `V_ρ`, not
ρ=7-specifically). All four of the user's invariants hold for BOTH
pieces (not just mixed_AB), giving a UNIFIED bound
`‖torsion(ρ)+mixed_AB(ρ)‖ ≤ K√C₂(ρ)` via the standard compact-Lie-group
Cauchy-Schwarz argument, superseding (and correcting) Round 53's
weaker/incorrect O(1) torsion claim with a stronger, code-verified,
unified O(√C₂(ρ)) bound covering the ENTIRE correction.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition (per the 4 user-specified invariants) | Threshold |
|---|---|
| Invariant 1: D64 depends on V_7/ρ (not fixed on the bare 64-dim fibre) | `build_D_matrix64()` (`g2su3_equivariance_check.py:53-66`) found to reference V_7 or `rho7_*` anywhere |
| Invariant 2: A_p={e_p,D64} or T(p,q,r)·Ms[p]Ms[q] contain hidden ρ-dependent branching coefficients | `clifford_left_64` (`g2su3_v7_multiplicity_dirac.py:84-100`) or `build_T_table`/`torsion_T` (`g2su3_H_element.py:69-85`) found to reference V_7, ρ_7, or any representation-specific data |
| Invariant 3: quadratic terms `ρ(e_p)ρ(e_q)` appear (not purely linear) | any function found to call `rho7_ep`/`rho7_nuk` twice within one summand |
| Invariant 4: a non-orthogonal (norm >1) projection distorts the bound | the operator-norm bound is derived on a strict subspace via a non-isometric embedding |

If FAIL (any triggers) → kills the factorization claim for that piece;
report which piece and why, do not claim the unified bound.
If PASS (none trigger) → the unified `K√C₂(ρ)` bound is established
structurally (K's numeric value deferred to Round 55).

**Verification performed, per invariant:**
- **Invariant 1 — PASS.** `build_D_matrix64()` (`g2su3_equivariance_check.py:53-66`) builds D64 entirely from `D_on_simple_tensor(eta,xi)` applied to the 64 basis vectors of `Sigma⊗Sigma` (`SUBSETS`, `DIM=8`) — zero reference to V_7, `rho7_*`, or any G₂-representation-specific object anywhere in the function. Independently confirmed by Round 17's own docstring (`g2su3_v7_multiplicity_dirac.py:10-14`): "`D(psi_{v,w})|_e = -sum_p e_p.w(rho_V(e_p) v) + D_on_simple_tensor(w(v))`" is stated for a GENERIC representation `V_ρ` (`rho_V`), with `D_on_simple_tensor` explicitly identified as "EXACTLY... already validated, calibrated against AHL2023 throughout this whole experiment" — i.e. representation-independent by the original derivation's own design, not merely by accident of the ρ=7 specialization.
- **Invariant 2 — PASS.** `clifford_left_64` (`g2su3_v7_multiplicity_dirac.py:84-100`): docstring "Clifford mult on the LEFT tensor factor only" — acts purely on the 64-dim `Sigma⊗Sigma` via `e_action(p,eta)`, zero V_7/ρ reference. `build_T_table`/`torsion_T` (`g2su3_H_element.py:69-85`): `T(i,j,k)=⟨[Z_i,Z_j]_m,Z_k⟩=2⟨Λ_m^{1/2}(e_i)e_j,e_k⟩` — built entirely from `LEVI_CIVITA_NOMIZU` and `bivector_on_vector6`, geometric data of the fixed 6-dimensional `𝔪` alone, zero V_7/ρ reference anywhere.
- **Invariant 3 — PASS.** `torsion_cross_term` (`:177-190`): single `Mr7 = rho7_ep(r)` call per `(p,q,r)` triple, no products of two `rho7_*` calls. `mixed_AB_term` (`:193-202`): single `Mp7 = rho7_ep(p)` call per `p`, likewise no quadratic terms. Confirmed directly from loop structure in both functions.
- **Invariant 4 — PASS, by a different route than originally anticipated.** The bound is derived on the operator acting on the raw `Hom(V_ρ,F)` matrix-coefficient space directly (via the single `ρ_ρ(e_r)v` application), not via any SU(3)-isotypic-block extraction. Restricting a bounded operator to any subspace (e.g. the physically-relevant SU(3)-equivariant sections) cannot increase its operator norm — this is automatic linear algebra, not an assumption requiring separate verification. Round 22's own `extract_coeffs`/16-dim-basis machinery (`:278-283`) is a DIAGNOSTIC tool used to verify type-preservation on specific test vectors, not part of the operator's mathematical definition — it does not enter the bound's derivation at all.

---

## Checks planned

- T1: read `build_D_matrix64` directly, confirm zero V_7/ρ dependence.
- T2: read `clifford_left_64`, confirm zero V_7/ρ dependence.
- T3: read `build_T_table`/`torsion_T`, confirm zero V_7/ρ dependence.
- T4: confirm linearity (single `rho7_ep`/`rho7_nuk` call per summand) in
  both `torsion_cross_term` and `mixed_AB_term`.
- T5 (adversarial, the one that actually found something): explicitly
  check whether Round 53's Agricola-based claim survives contact with
  Round 22's actual code — it does NOT for the O(1) torsion claim
  specifically, but the underlying mechanism (Cauchy-Schwarz on a
  linear-in-ρ(X) factorization) turns out to cover BOTH pieces anyway,
  via a route Round 53 did not consider.

---

## What this does NOT mean

1. Does NOT compute the actual numeric constant K — that is explicitly
   deferred to a future round (user's own "Round 55"), consistent with
   the "one round, one deliverable" discipline already established this
   session.
2. Does NOT enumerate the finite exceptional set of small ρ where
   positivity is not yet automatic — deferred to a future round
   ("Round 56").
3. Does NOT compute or verify anything for ρ=27, 64, or 77 specifically
   — no new representation's spectrum was computed, per explicit user
   constraint.
4. Does NOT change `preprint.tex` — per explicit user instruction this
   round, and consistent with "no premature strengthening" until the
   numeric constants are actually in hand.
5. Does NOT mean Round 53 was worthless — its Prior-Result-Gate work,
   its correct identification that Agricola's theorem is the relevant
   general reference, and its correct localization of the open question
   to "does a general bound exist" all directly enabled this round's
   finding. Its SPECIFIC conclusion (torsion is O(1) via direct
   application of Agricola's bare theorem) is superseded here.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
