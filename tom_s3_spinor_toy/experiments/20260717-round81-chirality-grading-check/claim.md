# E15 (round81) Claim — Does the natural S3 Clifford volume element split the E12 doublet?

**Date:** 2026-07-17
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY — filled BEFORE writing anything below)

1. **Exact claim:** the Cl(3) volume element `omega := Z1.Z2.Z3` (this
   project's own `Z_i = i*sigma_i` convention) acts as a natural
   chirality/grading operator on the S3 factor's spinor space and splits the
   2-dimensional torsion-crossing kernel found in E12 (round78) into two
   1-dimensional eigenspaces, supplying a natural projection to a single
   physical mode.
2. **`decision.md` grep** (formula + synonyms: "omega", "chirality operator",
   "grading", "volume element", "Z1.*Z2.*Z3"): **done** — hits in
   `round67-e2` (decision.md), `round73-e9`, `round76-e9followup`,
   `round78-e12`, `round79`, `round80` decision.md files. **All reviewed**:
   E2 computes `omega=Z1.Z2.Z3` and finds it is scalar/central, but uses this
   ONLY to calibrate Kostant's cubic element `H=(3c/2)*omega` inside
   Agricola's `D^t` formula (a purely algebraic ingredient of the connection
   family, not framed as a chirality/grading operator, and not applied to
   the E12 kernel-splitting question, which did not exist yet when E2 was
   written). No existing decision.md asks or answers "does omega split the
   E12 doublet" — this is a genuinely new question, reusing an old
   computation for a new purpose.
3. **`round*_claim.md` + scripts grep:** **done**, same files as above,
   0 hits framing this exact question.
4. **`null_results/` + `parked/` grep** ("omega", "S3 chirality", "grading
   operator", "Z1.*Z2.*Z3"): **done, 0 hits.** No prior REJECT/ARCHIVE entry
   addresses this candidate mechanism.
5. **`git log -S`/`-G` pickaxe:** not run (this is a new, small, self-
   contained script; the relevant prior computation, E2's `compute_omega_
   and_check_scalar`, was read directly above, not searched via pickaxe).
6. **Primary source re-read:** not applicable — this experiment does not
   depend on an external primary source beyond this project's own
   already-established, re-verified-in-this-script Clifford convention
   (E2/E9/E10/E12, all read directly this session, see decision.md).
7. **Status:** [x] NEW

---

## Estimand

**Population:** the 2-dimensional complex vector space of constant
(t=0) / `gbar`-twisted-constant (t=1) spinors on S3, i.e. the exact kernel
`ker(D_{S3,t=0 or 1})` tool-verified by E12 (round78) to be 2-dimensional.

**Intervention:** apply the Cl(3) volume element `omega := Z1.Z2.Z3` (E2's
own convention) to this space, as the natural candidate for a
chirality/grading operator built from the tensor-product Dirac operator's
own Clifford structure.

**Comparator:** the null hypothesis that `omega` acts as a scalar (a
multiple of the identity) on this 2-dimensional space, i.e. provides no
splitting at all.

**Endpoint:** number of distinct eigenvalues of `omega` on `ker(D_{S3,t})`
(1 = no splitting / NULL for this mechanism; 2 = splits into two 1-dim
eigenspaces / candidate mechanism found).

**Summary measure:** exact symbolic eigenvalue count (not a statistical
quantity — this is an algebraic, exactly-computable fact, no sampling
involved).

**MCID:** not applicable (binary/discrete outcome, no threshold needed:
either `omega` has 1 or 2 distinct eigenvalues on this space, exactly).

---

## Claim

`omega = Z1.Z2.Z3` splits the E12 kernel into two 1-dimensional eigenspaces,
one of which can be identified as "the physical mode," resolving the
multiplicity-2 excess.

Supporting sub-claims:
1. `omega` is well-defined as an operator on the S3 spinor factor
   (a fixed 2x2 matrix, independent of `t` and of position on S3).
2. `omega`, restricted to the E12 kernel (all of `C^2` at `t=0`; the
   `gbar`-twisted image of `C^2` at `t=1`), has two distinct eigenvalues.
3. If (2) holds, at least one of the two resulting eigenspaces can be
   linked to an already-established chirality/orientation convention in
   this project (e.g. G74B's S6-side chirality sign), giving a *motivated*
   way to select one eigenspace as physical.

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| `omega` is proportional to the identity on `C^2` (1 distinct eigenvalue) | `n_distinct_eigenvalues(omega) == 1` |
| The E12 kernel (both at t=0 and the gbar-twisted t=1 image) is a single eigenspace of `omega`, not split | a single scalar `lambda` solves `omega*psi = lambda*psi` identically for the FULLY GENERIC kernel vector, both at t=0 and t=1 |

If FAIL (kill condition triggers) → kills: this specific candidate mechanism
("natural Clifford volume-element grading splits the E12/E14 doublet") for
resolving E12's multiplicity-2 excess. Does NOT kill the underlying
multiplicity-2 finding itself (E12 stands regardless), nor any other
not-yet-tried mechanism (E12's own Relaxation Map lists others).

If PASS → survives: a genuine, tool-verified candidate splitting exists,
motivating a follow-up experiment (round82+) to check whether either
eigenspace can be linked to an established chirality convention (G74B) —
this experiment would NOT itself complete that link, only establish the
splitting exists.

If no hypothesis is killed by FAIL → gate is not scientifically motivated.
**This gate IS scientifically motivated**: FAIL directly closes off one
specific, concretely-nameable mechanism from E12's own Relaxation Map
("new projection specific to the S3 factor" — no candidate existed there;
this experiment supplies and tests the most natural one), narrowing the
remaining option space for future rounds.

---

## Checks planned

- T1: independently re-derive `omega=Z1.Z2.Z3` and its Clifford relations
  from scratch (not citing E2's result), verify scalar/central.
- T2: exact `sympy .eigenvects()` eigenstructure of `omega` — count distinct
  eigenvalues directly, not just a scalar/non-scalar binary flag.
- T3: apply `omega` to the FULLY GENERIC (symbolic `a,b`, not spot-checked at
  `(1,0)`/`(0,1)` alone) kernel vector at t=0, and to the fully generic
  `gbar(x)*(a_,b_)` kernel family at t=1 (E10/E12's own right-invariant-frame
  convention) — adversarial/edge-case check: confirm the same verdict holds
  in BOTH frames, since `omega` is position- and frame-independent by
  construction, this is checked directly rather than merely asserted.
- T4 (side-note, not part of the kill criterion): check whether a generic
  degree-1 ("vector-type") Clifford element `alpha*Z1+beta*Z2+gamma*Z3` splits
  `C^2` — expected yes (ordinary Pauli-type matrices), explicitly flagged as
  NOT a valid chirality/grading candidate (basis-dependent, transforms
  non-trivially under the very SU(2) that E14/round80 already showed acts
  irreducibly on this space).

---

## What this does NOT mean

1. Does NOT prove no chirality/grading mechanism can ever split the E12
   doublet — only that THIS specific, most-natural candidate (the Cl(3)
   volume element) does not, for a specific, checkable structural reason
   (centrality in odd Clifford dimension + Schur's lemma on an irreducible
   2-dim representation).
2. Does NOT resolve E12/E13's multiplicity-2 excess if this experiment's
   kill condition triggers (expected outcome per the Pauli identity
   `sigma_x sigma_y sigma_z = i*I`, already anticipated in the task
   framing) — E12's Relaxation Map remains open regardless of this
   experiment's outcome.
3. Does NOT apply to the S6 factor's own chirality mechanism (G74B) — that
   operator lives on a genuinely even-dimensional (6-real-dimensional)
   factor with a different Clifford structure (`Cl(6)`'s volume element
   behaves differently from `Cl(3)`'s), and this experiment does not
   re-examine G74B.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE** — see
`decision.md` for the full writeup.

**Evidence:** [VERIFIED-sympy] — `python e15_chirality_grading_check.py` →
`verdict.label == "NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE"`.

**Status:** CLOSED FAIL (kill condition triggered; clean, decisive negative
result for this specific candidate mechanism — reported honestly per the
task's explicit instruction not to force a resolution).
