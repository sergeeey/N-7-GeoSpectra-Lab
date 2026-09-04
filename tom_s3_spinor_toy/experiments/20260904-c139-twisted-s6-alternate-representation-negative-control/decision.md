# C139 decision -- twisted S6 Dirac operator with an alternate (tangent/
# vector-representation) twist bundle gives an invariant-sector kernel of
# 0, NOT 1 -- a real, first-ever kernel != 1 result, verified two
# independent ways -- PROMOTE, but QUALIFIED: an independent skeptic pass
# showed the "Term1=0" mechanism is FORCED by Schur's lemma for ANY
# zero-singlet twist bundle (not independent evidence of a special
# result), confirmed by follow-up computation in this same round; the
# genuinely non-forced fact is narrower (Term2, the twist connection's
# OWN contribution, is nonzero) and is reported as such, not oversold

**Date:** 2026-09-04
**Experiment:** `20260904-c139-twisted-s6-alternate-representation-negative-control`
**Question type (EstimandOps L0):** Descriptive.
**Script:** `c139_twisted_s6_alternate_representation.py` -- **Results:**
`results_c139.json`

## Verdict

```text
PROMOTE_QUALIFIED__KERNEL_0_NOT_1_FOR_ALTERNATE_TWIST_M__LITERAL_PREDICATE_CLEARS
  __VERIFIED_TWO_INDEPENDENT_ROUTES__NUMERIC_SVD_AND_EXACT_SYMPY__c=-2sqrt3/3__s=4/3
  __UNDISCLOSED_SYMMETRY_CHECK_CLEAR__NO_EQUIVARIANT_MAP_SIGMA_TO_M_EXISTS
  __SKEPTIC_PASS_1_FOUND_TERM1=0_IS_FORCED_BY_SCHUR_FOR_ANY_ZERO_SINGLET_TWIST
  __NOT_INDEPENDENT_EVIDENCE__CONFIRMED_BY_FOLLOWUP_COMPUTATION__CONCEDED_IN_FULL
  __GENUINELY_NON_FORCED_FACT_IS_NARROWER__TERM2_NONZERO__NOMIZU_SPECIFIC_GEOMETRY
  __ONE_MAJOR_SELF_CAUGHT_SIGN_BUG_FIXED_AND_VERIFIED_BEFORE_SKEPTIC_EVER_SAW_IT
  __DIMENSION_SHAPE_CAVEAT_PARTIALLY_VALID__KERNEL_INTEGER_PARTLY_REP_THEORY_BOOKKEEPING
  __DOES_NOT_FALSIFY_NGEN3__NARROWS_ROUND59S_TWIST_CHOICE_TO_NEEDING_JUSTIFICATION
```

**One line:** twisting the S6 Dirac operator's second factor by `m_C`
(the complexified isotropy/tangent representation of `S6=G2/SU(3)`,
module type `3+3bar`, dimension 6 -- genuinely different from `Sigma`'s
`1+1+3+3bar`, dimension 8) instead of by another copy of `Sigma`, using
the SAME `NOMIZU`/`ADNU` data and the same Leibniz-rule twisted-Dirac
construction round59 used, gives an invariant-sector kernel of **0**, not
**1** -- the first time in five attempts (four in C73/C73b, this one)
that a wrong-twist test has produced a different kernel dimension. **An
independent skeptic pass (Section 11) then showed that the mechanism
this decision.md originally offered as evidence the result was
"meaningful, not a shape artifact" (Term1 vanishing exactly) is itself
FORCED by su(3) representation theory for ANY twist bundle lacking a
trivial summand -- confirmed by a direct follow-up computation in this
same round (Section 8b), not merely accepted on the skeptic's say-so.
This is conceded in full, not minimized: it means the honest content of
the result is narrower than the first draft claimed. What survives,
independently of that concession, is that Term2 (the twist bundle's own
Levi-Civita connection, realized in the vector representation) is
NONZERO -- a fact NOT forced by Schur's lemma, genuinely dependent on
NOMIZU's specific geometry, and the actual locus of whatever
discriminating power this round has. **A SECOND, differently-worded
skeptic pass (Section 12) then correctly pointed out that a single
computed point does not establish this non-vanishing holds across the
whole admissible connection family (a linear functional can have a
zero locus). Rather than defer this, the round ran the direct test
in response (Section 8c, reusing C73b's own 2-dimensional admissible-
family machinery): kernel=0 holds at all 13 swept angles, `|c(theta)|`
constant to machine precision -- robust across the entire family, the
SAME "topologically protected" signature C73b found for round59's own
certificate, not a single-point accident.**

---

## 0. Background, read in full before computation (per claim.md)

- `experiments/20260714-round59-trivial-rank-certification/decision.md`
  -- read in full. `Sigma = Lambda^bullet(C^3)`, module type `1+1+3+3bar`,
  `(a,b,s)=(-1,-sqrt(3),4)`, `dim ker(D+|_1)=1`.
- `experiments/20260811-c73-round59-real-twisted-dirac-battery/decision.md`
  and
  `experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/decision.md`
  -- read in full. Four prior wrong-twist attempts, all non-discriminating:
  (a) Nomizu sign flip -- `|b|` unchanged. (b) alternate bigrading pairing
  -- IDENTICAL `(a,b)` via a hidden even/odd duality in `Sigma`. (c)
  mismatched-parity pairing -- identically zero but ALGEBRAICALLY FORCED
  (D preserves second-factor Clifford parity exactly). (d) `S+` twist --
  same magnitude structure, consistent with a known conjugation symmetry.
- `pearl_registry/INDEX.md` row 89, quoted exactly (§0a below).
- `experiments/20260811-c73b-.../decision.md`'s own "What survives, as a
  genuinely scoped next step" section, quoted exactly (§0a below) -- the
  precise specification this round implements.
- `experiments/20260705-g102-spin8-fiber-obstruction/decision.md` -- for
  `su(3)`-module context (`Hom_su3`, `Hom_g2` tables; also the source of
  the "anti-homomorphism sign bug" precedent directly relevant to §3d
  below).
- `null_results/INDEX.md` -- grepped for "wrong-twist"/"different
  representation"/"1+1+3+3bar", **zero matches** `[VERIFIED-tool, this
  session]` -- confirms no other round has attempted a non-`(1+1+3+3bar)`
  twist under a different name.
- `parked/INDEX.md` -- grepped, no matches for this specific question
  either (rows present are about the unrelated OB1/H1c `t`-selection
  family).
- `CLAIM_LEDGER.yaml` `C2_ROUND59_KERNEL_DIM1` and `C4_NGEN3_HEADLINE`
  entries read in full -- `C2` has `depends_on: [C1_S6_INDEX_1]`; `C4`
  `depends_on: [C1_S6_INDEX_1, C2_ROUND59_KERNEL_DIM1, C3_KT8_NO_ZERO_MODE,
  C_G67C3_THIRD_CHANNEL]`. Six total direct `CLAIM_LEDGER.yaml` dependents
  of `C2` were independently hand-counted `[VERIFIED-tool via grep, this
  session]` (matches the 2026-09-04 A1/A2/A3 audit's own count).

### 0a. Quoted verbatim

**Pearl row 89** (`pearl_registry/INDEX.md`, 2026-08-11, C73):
*"Building `D_S6` twisted by a DIFFERENT representation than `Sigma` (a
non-`(1+1+3+3bar)`-type bundle, or a deliberately non-`G2`-equivariant
twist) and checking that the resulting invariant-sector kernel is NOT 1
would supply a genuine discriminating negative control for the first
time."* ... *"before citing round59's kernel=1 result as having passed a
negative control (it has not, honestly) -- and before investing in a
second Dirac-battery round, since this construction is comparable in
scope to round59's own original 3-route build."* Row's own 2026-08-11
update (C73b): *"The 'different representation than Sigma' construction
named here remains the only unexplored route."*

**C73b's "What survives" section:** *"A discriminating negative control,
if one is still wanted, needs a twist bundle that is NOT related to `S-`
by any symmetry of `Sigma`'s own construction (not `S+`, not a sign flip,
not a bigrading relabeling) -- e.g. a twist by a representation with a
DIFFERENT `su(3)`-module type entirely (not `1+1+3+3bar`), or an
explicitly non-`G2`-equivariant perturbation. This is a substantial new
construction, comparable in scope to round59's own original build effort,
not attempted here."*

## 1. Zero-Signal Gate (FL Step -5)

| field | content |
|---|---|
| Entity | a twisted S6 Dirac operator `D_{S6,twist'}`, twisted by `W'=m_C` (complexified tangent/isotropy rep of S6) instead of `Sigma`, built with the same Killing-spinor/homogeneous-space machinery |
| Falsifiable predicate | the invariant-sector kernel of `D_{S6,twist'}` is `=1` (matching round59, non-discriminating) or `!=1` (discriminating) |
| Measurable outcome | the explicit kernel dimension, computed via the same calibration-adjacent procedure round59 used, cross-checked numerically and exactly |

All three fillable => gate **PASSES**.

## 2. PRE-REGISTERED CHOICE of alternate representation -- written before
   any kernel was computed, per claim.md's Anti-Overfitting Gate instruction

**Chosen:** `W' = m_C`, the **complexified isotropy (tangent) representation**
of `S6 = G2/SU(3)` -- the SAME 6-dimensional space `NOMIZU` is already a
connection on, represented via the **standard/vector representation** of
`so(6)` (`bivec_to_6x6`, reused from C73b's own file, unmodified in
formula), rather than the 8-dimensional **spin representation** `Sigma`
uses.

**Why this option, over the other two named in claim.md:**

| Candidate (claim.md's own menu) | Assessment |
|---|---|
| **su(3) adjoint, dim 8, module type "8"** | Rejected as first choice: `NOMIZU[i]` are general `so(6)` bivectors, not confined to the `su(3)` subalgebra, so representing them via `ad(-)` on the adjoint requires FIRST projecting `NOMIZU[i]` onto its `su(3)`-component (the reductive-decomposition `h`-part) -- an extra construction step not already present anywhere in this project's code, adding a genuinely new assumption (which projection, which normalization) this round would have to invent from scratch. |
| **Explicitly non-`G2`-equivariant perturbation of `Sigma`** | Rejected as first choice: harder to make falsifiable in a clean, reproducible way (what counts as "the" perturbation is itself a choice with many degrees of freedom), and further from a natural, already-motivated geometric object. |
| **`W' = m_C`, the tangent/vector rep -- CHOSEN** | `NOMIZU[i]` is, BY CONSTRUCTION, a connection value on the tangent bundle `T_pS6 = m` -- representing it via the vector/defining representation of `so(6)` is not an invented auxiliary structure, it is the SAME geometric object (the Levi-Civita connection) in its OWN native representation, requiring no new assumption beyond the representation-theoretic fact `so(6)` has both a spin rep (dim 8, what `Sigma` uses) and a vector rep (dim 6). `bivec_to_6x6` already exists in this project's own code (C73b), independently validated there (`NOMIZU` reconstructs to residual `5.6e-16` in the `Hom_su3(m,Lambda^2 m)` basis C73b built using this exact function) -- reused, not invented. |

**What a DIFFERENT choice would have looked like** (per claim.md's
explicit instruction to state this): had the su(3) adjoint been chosen,
the twist bundle would carry dimension 8 (same as `Sigma`) but module
type `8` (irreducible, no singlets) instead of `1+1+3+3bar` -- isolating
"module type matters" cleanly from "dimension matters," a genuinely
different and complementary test not attempted here, named explicitly as
future scope in §14.

**Module type, stated before computing anything:** `m_C = 3 (+) 3bar`
(the standard fact that a complex representation `V`, viewed as real and
then complexified, gives `V (+) Vbar` -- here `V` = the fundamental `3`
of the isotropy `su(3)`, since `T_pS6` for the nearly-Kahler `S6=G2/SU(3)`
carries a natural complex structure identifying it with `C^3`). Dimension
6, NOT 8; **zero** trivial (singlet) summands, unlike `Sigma`'s **two**
(`Lambda^0` and `Lambda^3`). This module-type difference is stated here,
BEFORE §3-4 verify it computationally.

## 3. Undisclosed-symmetry check -- done BEFORE the kernel computation,
   per claim.md's explicit instruction and this project's own C73 trap

Four checks, all `[VERIFIED-tool]`, all run and passing before §5-6's
kernel computation:

**3a.** `spin_lift` of ANY `so(6)` bivector (not just `su(3)`'s own
`ADNU`) preserves `Sigma`'s even/odd `Z2` parity exactly (`NAB_i`'s
even-odd off-diagonal block is exactly `0`, all `i`) -- a structural fact
about quadratic Clifford elements, verified directly on `NOMIZU`'s own
`NAB_i`, not assumed.

**3b.** `Sigma`'s `EVEN_IDX` (dim 4, `S+`) and `ODD_IDX` (dim 4, `S-`)
blocks are each **irreducible** under `{NAB_i}` (commutant dimension `1`
each, Schur's lemma). Consequence: the ONLY `{NAB_i}`-invariant subspace
dimensions achievable inside `Sigma` are `{0,4,4,8}` -- **6 is not among
them.** No `{NAB_i}`-invariant 6-dimensional subspace of `Sigma` can
exist AT ALL, independent of whether it would "look like" `m`.

**3c.** Direct intertwiner search: solving for all `T` (6x8) satisfying
`T@NAB_i = (rho_m(NOMIZU_i))@T` for every `i=1..6` simultaneously (the
vec-Kronecker nullspace method, same pattern as C73b's own
`equivariant_torsion_basis`) gives **nullspace dimension 0** -- no
nonzero equivariant map `Sigma -> m` exists under the SAME six connection
generators. This is the most direct, construction-independent test of
"is `nabla^m` secretly `nabla^Sigma` restricted to a subspace, under a
change of basis" -- **the exact shape of the trap that invalidated C73's
attempt (b)** (a hidden even/odd duality reproducing IDENTICAL numbers
under relabeling), checked here computationally before any kernel value
was known.

**3d. A genuine, self-caught defect, found by this check, not hidden.**
The FIRST run of this script's structure-constant regression check
(added specifically because an early full run gave an unexpected `0` for
BOTH `domain_inv` and `target_inv` -- see below) found: `bivec_to_6x6`
(C73b's own function, reused UNMODIFIED in formula) and `spin_lift`
(round59's own function) represent the SAME abstract `so(6)` bivector
generator with **opposite sign**, under this project's own `e_k^2=-1`
Clifford convention. Verified two ways:

1. **Empirically**, by extracting `su(3)` structure constants
   independently from two TRUSTED, already-validated representations
   (`Sigma`'s own `EVEN_IDX` 3-dimensional piece via `spin_lift`, and `m`
   via `bivec_to_6x6`) and comparing: `f_sigma = -f_m` **exactly**
   (`max|f_sigma + f_m| = 6.66e-16`, machine precision) over every
   nonzero structure-constant entry.
2. **Analytically** (worked by hand, not just observed): for `e_k^2=-1`,
   `ad_{(1/2)e_a e_b}(e_a) = e_b`, `ad_{(1/2)e_a e_b}(e_b) = -e_a` -- i.e.
   the spin-lift adjoint action gives generator-matrix entries
   `L[b,a]=+coeff, L[a,b]=-coeff`, exactly OPPOSITE to `bivec_to_6x6`'s
   own convention (`mat[i,j]+=coeff, mat[j,i]-=coeff`, i.e.
   `mat[a-1,b-1]=+coeff`). This is a DERIVABLE consequence of this
   project's specific `e_k^2=-1` convention (not the more common
   `e_k^2=+1`), not an arbitrary coincidence.

**Why this is NOT a defect in C73b's own already-published result:**
`bivec_to_6x6` was used SELF-CONSISTENTLY throughout C73b (both
`m_generators()` for `su(3)` and the `NOMIZU`-based reconstruction use the
SAME function, SAME sign) -- an overall sign flip of ALL generators
leaves C73b's own equivariance condition (`sum Ma[l,k]T[l,i,j]=...`,
linear and homogeneous in `Ma`) and its nullspace UNCHANGED. This is a
consistency problem that only arises the FIRST time (this round) the two
representations are combined in a SINGLE joint Leibniz generator
(`kron(su3_ops[a],I) + kron(I,rho_m[a])`), which literally requires both
sides to represent "the same `X_a`" simultaneously.

**How found, in the round's own workflow (transparency on process, per
this project's Hindsight Distortion Gap Heuristic -- recorded same-session,
not reconstructed):** the first full run of the script gave
`domain_inv=0, target_inv=0` where §2's pre-registered Clebsch-Gordan
prediction said `1,1`. Rather than accept this as a surprising physics
result, the SAME run's Verification-Substrate-Gate self-check (§5) --
which reproduces round59's OWN known `(a,b,s)` using the identical
generalized code path with `W'=Sigma` -- was ALSO wrong (`domain=3,
target=3` instead of the certified `2,1`), immediately flagging that the
generic scaffolding, not the physics, was broken. That specific
self-check bug was a block-index mistake (using the full 8-dim second
factor instead of round59's own `EVEN_IDX`-restricted second factor) and
was fixed first; after the fix, §5 reproduced round59 EXACTLY (`a=-1,
b=-sqrt(3)`, domain/target `2,1`, byte-identical `D` matrix), but §4's
`m`-side computation STILL gave `domain=target=0`. Only then was the
sign-convention hypothesis formed and checked directly (§3d above),
confirmed, and fixed via a `rho_vector()` wrapper (negating
`bivec_to_6x6`'s output; C73b's own file untouched). **The choice of
representation (`m`, the tangent/vector rep) was never changed at any
point in this process -- only genuine, independently-diagnosed
computational bugs in shared scaffolding were fixed, each caught by a
validation mechanism (the round59-reproduction self-check; the
structure-constant cross-check) that does not know or care what the
answer for `m` "should" be.** This is explicitly NOT the Anti-Overfitting
Gate's forbidden pattern (relaxing/changing a hypothesis after an
uninteresting result) -- both bugs were caught as bugs (via a
non-negotiable, representation-agnostic validation gate failing) before
any interpretable physics result existed at all.

## 4. su(3)-invariant sector dimensions -- Clebsch-Gordan prediction,
   verified against SVD-nullspace, THEN against exact sympy nullspace

**Prediction (§2, before any computation, using standard `su(3)` tensor
product rules `3(x)3=3bar(+)6`, `3(x)3bar=1(+)8`, and `Lambda^2(V)=V*`
for `dim V=3`):**

```
target = EVEN_IDX (x) m = (1 (+) 3bar) (x) (3 (+) 3bar)
       = 1 (+) 3 (+) 3 (+) 3bar (+) 6bar (+) 8         trivial mult = 1
domain = ODD_IDX (x) m  = (3 (+) 1) (x) (3 (+) 3bar)
       = 1 (+) 3 (+) 3bar (+) 3bar (+) 6 (+) 8         trivial mult = 1
```
(dimension check: `1+3+3+3+6+8=24=4x6` both cases, `[VERIFIED-tool]`)

**Cross-validation of the METHOD itself, before trusting its prediction
for `m`:** applying the identical CG method to round59's OWN known
construction (`EVEN(x)EVEN`, `ODD(x)EVEN`) correctly reproduces the
CERTIFIED `target=1, domain=2` **exactly** -- confirming the
representation-theoretic method is sound, independent of the later bug in
§3d (which was a numeric-code bug, not a CG-method error).

**Computed (post-fix, `[VERIFIED-tool]`, two independent routes):**

| | CG prediction | numeric (SVD nullspace) | exact (sympy nullspace) |
|---|---|---|---|
| `domain_inv` (`ODD_IDX (x) m`) | 1 | **1** | **1** |
| `target_inv` (`EVEN_IDX (x) m`) | 1 | **1** | **1** |

Both `domain_inv` and `target_inv` are exactly **1-dimensional** -- unlike
round59's `(2,1)`. This structural difference (a `1x1`, not `2x1`,
certificate) is itself an honest, load-bearing fact, addressed explicitly
in §9's caveat, not glossed over.

## 5. Verification-Substrate-Gate self-consistency: generalized machinery
   reproduces round59 exactly, `[VERIFIED-tool]`

Before trusting ANY result from the newly-generalized code
(`invariant_basis_gen`, `block_global_gen`, `build_twisted_dirac_np`), it
is run with `W'=Sigma` (i.e. the SAME twist round59 used) through the
IDENTICAL code path used for `W'=m`:

- `build_twisted_dirac_np(E,NAB,8,NAB)` matches C73's own trusted
  `build_numeric_dirac` **byte-for-byte** (`max|diff|=0.0`).
- The generalized `invariant_basis_gen`/`block_global_gen`, applied to
  round59's OWN `ODD_IDX(x)EVEN_IDX -> EVEN_IDX(x)EVEN_IDX` blocks,
  reproduce `a=-1, b=-sqrt(3)` (round59's certified values) exactly, and
  `domain=2, target=1` exactly.

This confirms the generic scaffolding is correct BEFORE it is trusted on
the new representation -- exactly the discipline claim.md's verification
plan requires ("Reuse round59's own calibration procedure as closely as
possible").

## 6. Main computation: the certificate for `W'=m`

`D'(eta (x) w) = sum_i (e_i . nabla^Sigma_i eta)(x)w + (e_i.eta)(x)(nabla^m_i w)`
-- the identical Leibniz-rule twisted-Dirac structure round59's
`build_dirac` uses, with the second factor's connection
`nabla^m_i = rho_vector(NOMIZU[i])` (sign-corrected per §3d).

`[VERIFIED-tool]` `D'` is exactly Hermitian (`max|D'-D'^dagger|=0.0`).

**Certificate** (domain `ODD_IDX(x)m`, dim 1 -> target `EVEN_IDX(x)m`,
dim 1):

```
c = <w_hat, D' u_hat>  =  -2*sqrt(3)/3   (exact, sympy)
                       =  -1.1547005... + 0.0j   (up to a free basis phase, see below)
s = |c|^2 = 4/3   (exact)
rank = 1  (full rank, since c != 0)
kernel_dim (forward, domain-side) = 1 - 1 = 0
kernel_dim (backward, target-side) = 1 - 1 = 0   (Hermitian adjoint, `max|fwd-bwd^dagger|=2.2e-16`)
```

**`kernel_dim = 0`, NOT `1`.** This is the falsifiable predicate's
`!= 1` branch -- discriminating, for the first time in five attempts.

**On the numeric-vs-exact phase mismatch** (`c_numeric =
-1.1336-0.2196j` vs `c_exact = -1.1547+0.0j`): `|c_numeric| =
|c_exact| = 1.1547005...` exactly, but the RAW phase differs. This is an
EXPECTED gauge freedom, not a discrepancy: since `domain_inv`/`target_inv`
are each 1-dimensional, the orthonormal basis vector is defined only up
to an independent overall phase in each of the two nullspace routes
(SVD-numeric vs sympy-exact) -- `c`'s phase is basis-dependent, `|c|`
(equivalently `s`) is not. `[VERIFIED-tool]`
`exact_abs_c_matches_numeric_abs_c` confirms `||c_exact|-|c_numeric||
< 1e-6`.

## 7. Deformation/linearity check, `[VERIFIED-tool]`

`D'(t)` (NOMIZU scaled by `t`, both factors) is exactly linear in `t`
(same algebraic argument as C73's own `test_deformation`, since
`build_twisted_dirac_np` is linear in both `nab_np` and `conn_w_np`,
each linear in `NOMIZU`): `c(0.5)=0.5*c(1)`, `c(2.0)=2.0*c(1)`, both
exact to `<1e-6`. `kernel_dim=0` is therefore not a fine-tuned property
of `t=1` specifically -- it holds for every `t != 0` in this family (the
map only degenerates to `kernel=1` at the singular point `t=0`, exactly
as in C73's own analogous finding for `Sigma`).

## 8. Mechanistic decomposition -- does a clean single-term mechanism
   recur (as in round59), and is `c != 0` structurally forced or
   incidental? **[REVISED after skeptic pass 1 -- see §8b; the ORIGINAL
   framing below is left visible, struck through in spirit not in text,
   because this project's culture requires the WRONG reasoning to stay
   on record, not be silently replaced. §8b is the corrected account.]**

`D' = Term1 + Term2`, `Term1 = sum_i kron(E_i@NAB_i, I_W)` (Clifford +
Sigma-connection on the first factor, IDENTITY on the twist factor),
`Term2 = sum_i kron(E_i, connW_i)` (Clifford on the first factor,
twist-bundle connection on the second). `[VERIFIED-tool]`
`term1+term2=c` exactly.

```
Term1 (Killing-eigenvalue-analog piece)  =  0            EXACTLY
Term2 (twist-bundle-connection piece)    =  c  (= -2sqrt3/3)   the SOLE contributor
```

**Original (first-draft) reading, offered as evidence the result was
"meaningful, not a shape artifact":** *"Round59 found `Term2=0`, leaving
`Term1` (the Killing-spinor eigenvalue) as the sole surviving piece.
Here, `Term1=0` for an analogous representation-theoretic reason... a
clean, structurally-explicable split is not the signature of an
unremarkable, dimension-counting-driven nonzero number."* **This framing
was WRONG, in the specific sense §8b makes precise: the split IS forced,
by a general fact that has nothing to do with `m` specifically.**

## 8b. Skeptic-triggered correction, verified independently in this same
    round -- Term1's vanishing is FORCED, not evidence

Skeptic pass 1 (§11) identified that `Term1`'s single-factor piece,
`A := sum_i E_i @ NAB_i` (the ordinary, untwisted operator on `Sigma`
alone -- literally `Term1` with the twist-identity factored out), is
**exactly `su(3)`-equivariant**, and that `su(3)`-equivariance alone
forces `A` to annihilate `ODD_IDX`'s `3`-constituent (since `EVEN_IDX =
1 (+) 3bar` contains no copy of `3`, an equivariant map out of a `3` into
`EVEN_IDX` must be zero by Schur's lemma) -- **for ANY twist bundle `W'`
lacking a trivial (`su(3)`-singlet) summand**, since the domain singlet
`u_hat` is then forced to draw its ENTIRE first-factor component from
`ODD_IDX`'s `3`-piece (§4: the sole singlet source in `ODD_IDX(x)W'` is
`3(x)Wbar-piece->1` when `W'` has no `1`), and `Term1` kills that piece
identically regardless of what `W'` is.

**Independently re-derived and computed in this round** (not merely
accepted from the skeptic's assertion), `[VERIFIED-tool]`:

```
max_a |[A, su3_ops[a]]|            =  0.0   exactly, all a=1..8
A restricted to ODD_IDX's 3-piece  =  the ZERO 4x3 matrix, exactly
A restricted to ODD_IDX's singlet  =  maps to EVEN_IDX's singlet with
                                       coefficient -sqrt(3)  (matches
                                       round59's own Killing eigenvalue
                                       EXACTLY -- an unplanned, welcome
                                       independent confirmation of
                                       round59's own certified mechanism,
                                       found only because this check was
                                       run)
```

**Consequence, conceded in full:** `Term1=0` here is **not independent
evidence** that `c!=0` reflects a special, non-generic property of `D'`
or of `m` specifically. It is a **general fact about `su(3)`-equivariant
operators acting on `Sigma` alone**, true for the twist by `m` and would
be equally true for ANY OTHER twist bundle with zero singlets -- the
`su(3)`-adjoint (`8`, §2's runner-up) included. §8's original "clean
structural mechanism, therefore meaningful" argument is **withdrawn as
stated**; the reasoning was circular, restating "`m` has no singlet" in
different words rather than independently corroborating it.

**What DOES survive as a genuinely non-forced fact:** `Term2 != 0`.
Unlike `Term1`, `Term2`'s vanishing or non-vanishing is NOT determined by
`su(3)` representation theory alone -- Schur's lemma, applied to an
equivariant operator restricted between two matching (both-trivial)
isotypes, only forces the result to be SOME scalar, not a SPECIFIC one
(zero or otherwise); `Term2`'s actual value depends on `NOMIZU`'s
specific numeric realization on `m` via the vector representation. This
is analogous IN KIND (a nonvanishing scalar computed from real geometric
connection data, not forced to any particular value by representation
theory) to round59's own certified mechanism (where `Term1`'s value was
the genuinely geometric, non-forced fact, equal to the Killing
eigenvalue) -- but it is a NARROWER claim than §8's original framing:
what this round actually establishes is **"the twist bundle's own
Levi-Civita connection, realized on `m`, couples nontrivially to
`Sigma`'s Clifford structure in the singlet sector"** -- not "the wrong
twist is generically penalized by `D_S6`."

## 8c. Skeptic-2-triggered angular sweep -- is `Term2 != 0` a family-wide
    fact, or a single-point accident? `[VERIFIED-tool]`, decisive

FL Step 8a skeptic pass 2 (§12) raised a sharp, correct, and directly
actionable objection: `Term2` is a functional of the connection choice
within C73b's own already-certified 2-(real-)dimensional admissible
`su(3)`-equivariant torsion family `Hom_su(3)(m_tangent, Lambda^2
m_tangent)` -- `NOMIZU` is ONE point in that family. A functional that
is merely R-linear in the 2 real parameters generically has a 1-dimensional
zero locus, so a SINGLE point giving `Term2 != 0` does not by itself
establish `Term2 != 0` HOLDS across the family -- exactly the concern
C73b itself raised and answered for round59's own `b`-coefficient, via a
13-angle sweep (C73b's own Part 3).

**Response: the identical sweep was run for `Term2`/`c`, reusing C73b's
own `m_generators`/`equivariant_torsion_basis`/`vec_to_nomizu_dict`/
`matdict_to_nomizu` UNMODIFIED** (Section 7b of the script), at the same
13 angles (`0` to `270` degrees, `22.5`-degree steps) C73b used:

```
|c(theta)|  =  1.154701...   IDENTICAL at all 13 angles, spread = 6.7e-16
Term1(theta) = 0              EXACTLY, at all 13 angles
kernel(theta) = 0             at EVERY tested angle -- never 1
```

**This is decisive, and resolves the objection in the STRONGER
direction, not the weaker one.** `Term2` is not merely nonzero at
`NOMIZU`'s point -- its MAGNITUDE is exactly constant across the whole
2-dimensional admissible family, the same signature C73b found for
round59's own kernel-protection (`|b|=sqrt(3)` constant across the
identical 13-angle sweep, "kernel-rank protection is a statement about
[the parameter's] MAGNITUDE, which is protected, not its phase, which is
free" -- C73b's own decision.md). This means `Term2` is C-LINEAR in a
SINGLE complex parameter (not merely R-linear in 2 independent reals,
which is what would have produced a real 1-dimensional zero locus and
justified the skeptic's concern) -- its zero locus is the single point
"zero connection" (not an admissible unit-magnitude direction), not a
line cutting through the family. **`kernel=0` is therefore
"topologically protected across the whole admissible connection
family," in EXACTLY the sense C73b certified for round59's own
`kernel=1`** -- not a single-direction accident, and not a
coincidence of `NOMIZU`'s specific numeric values.

**Also confirmed by the same sweep:** `Term1=0` holds at EVERY angle,
not just `NOMIZU`'s -- consistent with §8b's forcing argument (which
never used `NOMIZU`'s specific values, only `su(3)`-equivariance and the
zero-singlet module type), independently corroborated here numerically
across the whole family, not merely asserted to generalize.

**What this does, and does not, resolve relative to skeptic pass 1's
Attack 3 (§11):** it establishes that the SPECIFIC discrimination found
here (`Term2 != 0`, `kernel=0`) is a robust, family-wide geometric fact,
not noise -- directly answering "is this a single-point artifact." It
does **not** answer the SEPARATE, still-open point that a
matched-singlet-count twist bundle (e.g. `m (+) 2*1`, an 8-dimensional
twist with the same singlet count as `Sigma`) would be a MORE
directly comparable test to round59's own `(2,1)`-shaped certificate --
that remains genuinely unbuilt, named explicitly in §14/§16 as concrete
future work, not conflated with what THIS check establishes.

## 9. The dimension-shape caveat -- reassessed after §8b/§8c, PARTIALLY
   VALID, not merely raised-and-dismissed

**Original concern (unchanged from the first draft):** `domain_inv`/
`target_inv` here are each **1-dimensional**, unlike round59's `(2,1)`.
For a `1x1` scalar, `kernel in {0,1}` only, and "nonzero" is close to the
default/expected outcome for a non-forced map of that shape.

**Re-assessed verdict on this concern, after §8b: the concern is
PARTIALLY VALID, not fully answered.** The shape `(1,1)` (vs round59's
`(2,1)`) is itself a DIRECT, forced consequence of `m` having zero
singlets (§4's Clebsch-Gordan count: a twist bundle with `k` singlets
contributes `k` extra domain-invariant dimensions via the `1(x)1->1`
channel, on top of the ONE dimension every zero-or-more-singlet twist
bundle gets via its `3(x)3bar->1`-type channel -- `Sigma`'s `k=2` gives
domain `2`; `m`'s `k=0` gives domain `1`). And §8b shows `Term1=0` is
ALSO forced by the same zero-singlet fact. So BOTH the shape `(1,1)` AND
`Term1`'s vanishing trace back to the single fact "`m` has no `su(3)`
singlet" -- they are not two independent lines of evidence, they are one
fact viewed twice. **The genuinely informative, non-forced content of
this round is narrower than "kernel != 1 for a wrong twist" -- it is
specifically "`Term2 != 0` for this particular geometric connection
realized on this particular twist bundle."** Whether "`Term2 != 0`"
counts as answering pearl row 89's question ("does the resulting
invariant-sector kernel differ from 1") is, by the LITERAL kill
criterion, YES (kernel is computed to be 0, verified, not asserted) --
but the READING of that as "the wrong twist is dynamically penalized,
the way round59's own certificate showed the right one is dynamically
selected" is not fully supported, and is not claimed here beyond what
§8b actually establishes.

**What this section does NOT walk back:** the COMPUTATION itself
(`kernel=0`, verified two independent ways, Hermitian, linear, clear of
the undisclosed-symmetry trap) stands, unchanged by this reassessment.
What changes is the INTERPRETIVE WEIGHT placed on it -- from "a clean
discriminating result comparable in kind to round59's own certificate"
(first draft) to "a real, computed, first-ever `kernel!=1` result, whose
informative content is specifically located in `Term2`'s non-vanishing,
not in the `Term1=0`/shape mechanism this draft originally (wrongly)
credited" (this revision).

## 10. Kill criterion evaluation (claim.md's own three branches)

- **(a)** kernel `=1` for the chosen alternate twist -> would be NULL.
  **Does not fire**: kernel `=0`.
- **(b)** no consistent alternate twist constructible -> would be
  BLOCKED. **Does not fire**: `W'=m` is fully constructed, Hermitian,
  linear, and reproduces round59 exactly under the `W'=Sigma`
  specialization (§5).
- **(c)** the "different" representation turns out related to `Sigma` by
  an undisclosed symmetry -> would invalidate the result (the exact C73
  attempt-(b) trap). **Checked explicitly, does not fire** (§3):
  dimension mismatch (`m`=6 vs `Sigma`'s achievable `{0,4,4,8}`) and a
  direct zero-nullspace intertwiner search both confirm no such symmetry
  exists.

**Verdict: kill criterion does NOT fire on any of its three literal
branches -- PROMOTE by claim.md's literal definition** ("a legitimately
different, non-repeat twist... kernel genuinely `!=1`"). **Qualified per
§8b/§9**: the LITERAL predicate clears, but skeptic pass 1 (§11) found,
and this round's own follow-up computation confirmed, that the strongest
version of the ORIGINAL justification for treating this as "meaningful,
not a shape artifact" (§8's Term1=0 mechanism) does not hold up as
independent evidence. The verdict below is PROMOTE on the literal
predicate, explicitly NOT on the stronger claim the first draft made.

## 11. FL Step 8a -- skeptic pass 1 (context-blind, independent agent)

Per claim.md's mandatory instruction for this high-stakes round, this
pass was run via an INDEPENDENT `Agent(skeptic)` invocation given ONLY
`claim.md`, this `decision.md` (the FIRST-DRAFT version, before §8b's
correction -- i.e. genuinely context-blind, not shown this round's own
later self-correction), and the script/results files -- no session
history, no reasoning chain from the rounds above. **This section
reports the pass's actual findings and this round's response; §8/§8/§9
above have ALREADY been rewritten to incorporate the response -- the
skeptic did not see the corrected version, this decision.md as a whole
now reflects it.**

### 11a. Skeptic pass 1 -- verdict and findings

**Skeptic's overall verdict: `WEAKENED`.** Full transcript available via
the orchestrating session (agent id `a3efdc7cfd101ec1c`); summarized and
responded to per the FL Step 8a Response Matrix below.

| # | Skeptic finding | Severity | Response |
|---|---|---|---|
| 1 | Section 3d's sign-convention fix (`rho_vector = -bivec_to_6x6`) -- independently re-derived by hand from the `e_k^2=-1` Clifford algebra (`ad_{(1/2)e_1e_2}(e_1)=e_2`, `ad_{(1/2)e_1e_2}(e_2)=-e_1`) and cross-checked via an independent structure-constant commutator computation. Both confirm the fix is analytically correct, not a rationalization toward a preferred answer. Also noted: kernel dimension is INVARIANT to which overall sign convention is chosen (negating `rho_m` flips `Term2`'s sign but not `Term1=0` nor `\|c\|`) | Informational (confirms, does not weaken) | **`[CONFIRMED-REAL]`, accepted with thanks** -- an independent by-hand derivation is a genuinely stronger confirmation than this round's own structure-constant regression check alone (Verification Strength Ladder: "same model, isolated context" doing independent symbolic algebra by hand is closer to the "differently-motivated" rung than a second run of the same numeric check would have been). No action needed beyond citing it here. |
| 2 | **Section 8's `Term1=0` "mechanism" is forced by the module-type choice (`m` has zero `su(3)` singlets), not independent structural evidence** -- by-hand Schur's-lemma argument: `A` (Term1's single-factor operator) is `su(3)`-equivariant; the `3`-piece of `ODD_IDX` cannot map equivariantly into `EVEN_IDX=1+3bar` (no `3`-constituent there); hence `Term1` annihilates the domain singlet for ANY zero-singlet twist bundle, not just `m` | **HIGH -- directly undermines §8/§9's central defense of the result's interpretive strength** | **`[FALSIFIED]` as originally argued -- accepted in full, not dismissed.** Independently re-derived and computed in THIS round (§8b): confirmed `A` is exactly `su(3)`-equivariant (`max|[A,su3_ops[a]]|=0.0`, all `a`) and its restriction to `ODD_IDX`'s `3`-piece is the exact zero matrix. §8/§9 rewritten to concede this fully and relocate the round's genuinely non-forced content to `Term2`'s non-vanishing. This is the single most important finding of this round's entire skeptic process. |
| 3 | The "kernel=1 vs kernel=0" discrimination reduces largely to representation-theoretic bookkeeping (singlet-count difference between `Sigma` and `m` mechanically determines both the `(2,1)` vs `(1,1)` shape AND `Term1`'s vanishing) rather than testing `D_S6`'s dynamics; a genuinely stronger test would use a twist bundle with the SAME singlet count as `Sigma` (e.g. `m (+) 2*1`) | MEDIUM -- an important scoping point, not a defect in the computation | **Accepted as a valid scoping limitation, added to §14 and §16 (registry proposals) as explicit future work**, not attempted in this round (a `1+3+3bar+1` twist bundle is a materially new, more complex construction -- comparable in scope to this round's own build, per this project's own "one assumption at a time" discipline). Named honestly as the "genuinely matched-shape test" this round does NOT supply. |
| 4 | Section 5's `W'=Sigma` self-consistency check does not exercise the `rho_vector` sign-fix path at all (it uses `NAB_np` on both factors, never `bivec_to_6x6`/`rho_vector`) -- the "25/25 checks pass" headline is less impressive than it looks, since the ONE check that validates the sign fix (`rho_vector_sign_fix_matches_spin_lift_structure_constants`) is close to tautological given how the fix was constructed | LOW-MEDIUM -- accurate observation, mitigated | **Accepted, and mitigated by finding #1** (the skeptic's OWN independent by-hand derivation, not merely this round's internal check, confirms the fix) -- disclosed explicitly rather than left as an implicit strength of the "25/25" figure. |
| 5 | The deformation/linearity check (§7) is algebraically forced by construction (linear operator), not an independent test | LOW | **Accepted** -- §7 was never claimed as independent confirmation beyond "not a fine-tuned property of `t=1`"; retained for that narrower purpose only, not for anything stronger. |
| 6 | The undisclosed-symmetry check (§3) is robust to the sign-convention choice (checked both ways) | Informational (confirms) | **`[CONFIRMED-REAL]`, no action needed.** |

### 11b. Response to the overall `WEAKENED` verdict

**Accepted, not contested.** The skeptic's central finding (#2) is
correct, independently reproduced in this same round (§8b), and has
already changed this decision.md's own framing, verdict qualification,
and registry proposals (§15) BEFORE this document reached its current
form -- not smoothed over, not left as a footnote. Per this project's FL
Step 8a Response Matrix, `WEAKENED` (not `FALSIFIED` of the core
predicate) is the correct classification: the CORE falsifiable predicate
(`kernel != 1`, computed and verified) survives; the INTERPRETIVE weight
originally placed on it does not, and has been rewritten accordingly.

Agent id `a3efdc7cfd101ec1c`.

## 12. FL Step 8a -- skeptic pass 2, differently-worded (Paraphrase-
    Sensitivity Probe)

Per claim.md's explicit instruction ("run a SECOND, differently-worded
pass... regardless of the first pass's verdict, unless the first pass
returns a clean, unqualified confirmation with zero findings") -- given
this round's stakes (6 ledger dependents including `C4_NGEN3_HEADLINE`)
and genuine novelty risk, a second independent `Agent(skeptic)` pass was
run with a differently-phrased, informal-register falsification prompt
(no formal "falsification agent" framing, colloquial task description),
same claim.md + decision.md (this time the version ALREADY revised per
pass 1's finding, i.e. the pass-2 agent saw §8/§8b/§9/§11 as they now
read) + code, no session history. Agent id `a6c59ca71046b9708`.

### 12a. Skeptic pass 2 -- verdict and findings

**Skeptic's overall verdict: `WEAKENED`.**

| # | Skeptic finding | Severity | Response |
|---|---|---|---|
| 1 | **`Term2` is a linear functional on C73b's own 2-dim admissible torsion family; a single point (`NOMIZU`) giving `Term2!=0` does not establish it holds across the family (generic 1-dim zero locus) -- the round should have run the SAME angular sweep C73b ran for round59's own `b`-coefficient, and had not** | **HIGH -- directly actionable, previously missing** | **Run in this same round (§8c), not deferred.** 13-angle sweep, reusing C73b's own `equivariant_torsion_basis`/`m_generators` unmodified: `\|c(theta)\|` constant to `6.7e-16` across ALL 13 angles, `Term1=0` at every angle, `kernel=0` at every angle -- NEVER hits `kernel=1` anywhere in the admissible family. This resolves the objection in the STRONGER direction: `Term2` is C-linear in a single complex parameter (matching C73b's own finding for round59's `b`), so its zero locus is the single non-admissible point "zero connection," not a line through the family. `kernel=0` is "topologically protected across the whole admissible family," exactly as C73b certified for round59's own `kernel=1`. |
| 2 | Even after the pass-1-triggered revision, §9's language may still be "spin" -- softer than the first draft but still overselling; the registry text (§15) still calls the result "discriminating" | MEDIUM | **Partially accepted.** §9/§15 revised further (this pass) to state precisely what §8c newly establishes (family-wide robustness of `Term2!=0`) alongside what remains conceded from pass 1 (`Term1=0`/shape-forcing, matched-singlet-count test not attempted) -- "discriminating" is retained in registry wording ONLY because it is literally true of the computed kernel value, with the mechanism now stated alongside it, not standing alone. |
| 3 | §3c's "no equivariant map Sigma->m" check is Schur-trivial given `so(6)=su(4)`'s three pairwise-inequivalent irreps (`4`,`4bar`,`6`) -- confirms the check is correct but closes a WEAKER class of trap than C73's actual attempt-(b) (a hidden duality between different pieces of the SAME `Sigma`, not a map into an external `m`) | LOW-MEDIUM -- accurate, scopes the check correctly | **Accepted.** §3c's role restated (see this section's own text, not re-litigated in §3 itself to avoid further churn) as "rules out the specific failure shape it was designed to catch, via a genuinely necessary but representation-theoretically forced computation" -- not claimed as a stronger, more surprising result than it is. |
| 4 | Sign-convention fix independently re-derived by the skeptic from `e_k^2=-1` Clifford algebra, matching both this round's own derivation (§3d) and skeptic pass 1's independent derivation -- now confirmed by THREE separate derivations | Informational (confirms, strongly) | **`[CONFIRMED-REAL]`, strengthened.** Two independent adversarial agents plus this round's own derivation all agree -- Verification Strength Ladder rung effectively raised for this specific sub-claim. |
| 5 | The bug-hunt-until-expected-value workflow (§3d) is "a near miss" -- would have been unresolvable without an independently-checkable analytic derivation | LOW-MEDIUM, process observation | **Accepted as stated**, already disclosed in §3d's own "How found" paragraph; no further action, the analytic derivation (now confirmed 3x independently) is exactly the mitigation the skeptic identifies as necessary. |
| 6 | The "5th attempt" framing (grouping this round with C73/C73b's four) is imprecise -- those four tested twists WITHIN `Sigma`'s own symmetry class (preserving singlet count); this round tests a twist OUTSIDE that class (different module type) -- a different KIND of question, not simply the fifth try at the same one | MEDIUM -- a fair, clarifying reframing | **Accepted, incorporated** (§14, registry wording) -- this round is reframed as "the first attempt at a structurally different question (module-type change) after four attempts that stayed within `Sigma`'s own symmetry class," not merely "attempt five." |
| 7 | The matched-singlet-count test (echoing skeptic pass 1's finding #3) remains the decisive test not yet run; citing this round's result as clearing pearl row 89 "in current form... propagates a stronger evidentiary weight than the round earns" | MEDIUM-HIGH | **Accepted as the correctly-scoped residual limitation.** Named explicitly, not smoothed over, in §14/§16/registry proposals as required future work; pearl row 89's closure wording (§15) is written to state exactly what was and was not established, per this exact instruction. |

### 12b. Response to the overall `WEAKENED` verdict, and net effect of
    both passes together

**Accepted in the same spirit as pass 1: real findings taken seriously,
none dismissed, one (finding #1) directly resolved by new computation in
this round rather than deferred.** The NET effect of running two
differently-worded, context-blind, independent skeptic passes on this
high-stakes claim: pass 1 found a genuine flaw in the round's own
REASONING (the Term1=0 "mechanism" was circular) and pass 2 found a
genuine GAP in the round's own TESTING (the family-wide robustness of
Term2 was asserted, in the first draft's language, without having been
checked) -- both were real, both are now fixed IN THIS ROUND (not
deferred to a future one), and the SECOND fix (§8c) is a positive,
strengthening result, not merely a repair. What remains open after both
passes (the matched-singlet-count test) is explicit, scoped, and
proposed as concrete future work (§16), not silently absorbed into an
inflated verdict.

## 13. Kill Analysis (Anti-Overfitting Gate discipline)

**What this round kills:** the specific hypothesis (implicit in the
pattern of four prior C73/C73b nulls, and explicitly named as the
"substantially more likely" reading in C73b's own decision.md) that
round59's construction "simply does not have an internally-accessible
wrong-twist control at all" -- FALSE as stated: an internally-accessible
control DOES exist, for a twist bundle outside `Sigma`'s own symmetry
class (module type `3+3bar`, not `1+1+3+3bar`).

**What is NOT killed:**
- round59's own certified `(a,b,s)=(-1,-sqrt(3),4)`, `dim ker(D+|_1)=1`
  -- untouched, independently re-reproduced here as a byproduct (§5).
- `N_gen=3`'s CONDITIONAL status -- unaffected (§14).
- The FOUR prior C73/C73b attempts' own conclusions (sign flip
  non-discriminating, bigrading hidden duality, parity-forced zero, `S+`
  conjugation symmetry) -- all remain correct diagnoses of THOSE four
  specific constructions; this round used a genuinely different one.

**Relaxation Map** (one assumption changed relative to the four prior
attempts, per the Minimal Relaxation Rule):

| Assumption relaxed | What changed | Result |
|---|---|---|
| Twist bundle stays within `Sigma`'s own symmetry class (`1+1+3+3bar` module type) | Replaced with `m_C` (`3+3bar` module type, dimension 6) | `kernel: 1 -> 0`, discriminating |

Only ONE assumption changed (module type / choice of twist bundle) --
everything else (`NOMIZU`, `ADNU`, calibration discipline, Leibniz-rule
construction, `ODD_IDX`/`EVEN_IDX` first-factor grading) is held fixed
and reused unmodified, satisfying the Minimal Relaxation Rule explicitly.

**Reframing per skeptic pass 2 finding #6 (§12), accepted:** this round
is more accurately described as **the first attempt at a structurally
DIFFERENT question** than as "the fifth attempt at the same one." C73's
four attempts all tested twists that stayed WITHIN `Sigma`'s own
symmetry class (preserving its `1+1+3+3bar` module type and singlet
count exactly: a sign flip, a bigrading relabel, a parity mismatch, a
chirality conjugate). This round is the first to test a twist OUTSIDE
that class (a genuinely different module type, `3+3bar`, zero singlets).
The pattern-of-five framing in this document's title/verdict block is
retained because it IS still true chronologically and IS still the
correct answer to pearl row 89's literal question -- but the KIND of
test is different, not merely the fifth repetition of the same kind that
happened to work this time.

## 14. What this round does NOT show

- Does **NOT** falsify `N_gen=3` or `C2_ROUND59_KERNEL_DIM1` -- round59's
  OWN certified `kernel=1` for the `Sigma`-twisted operator is
  UNTOUCHED and independently re-confirmed here (§5). This round shows a
  DIFFERENT operator (twisted by `m`, not `Sigma`) has a different
  kernel -- exactly what a discriminating negative control is supposed
  to show, and exactly what claim.md's own "What this round does NOT
  show" section anticipated: *"it would show round59's SPECIFIC twist
  choice needs independent physical justification beyond 'it gives
  kernel=1', a narrower and more actionable finding, not a refutation."*
  Stated here as that narrower finding, explicitly, not overclaimed as
  more.
- Does **NOT** identify what that independent physical justification
  IS -- this round establishes that a justification is now genuinely
  NEEDED (previously, the absence of ANY discriminating control meant
  the question "why `Sigma` and not something else" could not even be
  posed as a real alternative; now it can), not what the justification
  says. `Sigma` remains Tom Lawrence's own construction, directly
  motivated by AHL2023's spinor-bundle framework -- this round does not
  argue `Sigma` is wrong, only that it is no longer the UNIQUE twist
  giving the calibration-compatible construction a nontrivial invariant
  kernel structure.
- Does **NOT** fully dissolve §9's dimension-shape caveat -- §8c's
  angular sweep shows `Term2 != 0` is robust across the WHOLE admissible
  connection family (not a single-point accident, the specific concern
  skeptic pass 2 raised), but §8b's separate finding stands: `Term1=0`
  and the `(1,1)`-shaped invariant sector are BOTH forced the moment a
  zero-singlet twist bundle is chosen, so the discrimination is real and
  robust but narrower in mechanism than round59's own `(2,1)`-shaped
  certificate. Both are true at once; neither is allowed to silently
  cancel the other in this document's own framing.
- Does **NOT** test the su(3)-adjoint alternative (`dim 8, module type
  8`, unbuilt, §2's runner-up) or, more decisively per BOTH skeptic
  passes, a **matched-singlet-count twist bundle** (e.g. `m (+) 2*1`,
  8-dimensional with the SAME 2-singlet structure as `Sigma`) -- the
  latter would be the most directly comparable test to round59's own
  `(2,1)`-shaped certificate, testing whether `D_S6` discriminates
  `Sigma` from a same-shape alternative rather than merely from a
  different-shape one. Explicitly named as the single most valuable next
  step, not attempted here (§16).
- Does **NOT** reopen C123-C138's verdicts (OB1/H1c `t`-selection is a
  separate question from this round).
- Does **NOT** change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does **NOT** solicit Tom Lawrence's Part 5.

## 15. Registry actions -- NOT performed by this round, proposed only

This round does not edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
`null_results/INDEX.md`, `pearl_registry/INDEX.md`, `CLAIM_LEDGER.yaml`,
or `.claude/memory/activeContext.md`. Proposed exact wording:

**`CLAIM_LEDGER.yaml`** -- new entry (does NOT modify `C2_ROUND59_KERNEL_DIM1`
or `C4_NGEN3_HEADLINE`):

```yaml
  - id: C139_ALTERNATE_TWIST_M_KERNEL_ZERO
    statement: "Twisting D_S6 by W'=m_C (complexified tangent/isotropy rep, module type 3+3bar, dim 6, ZERO su(3) singlets) instead of Sigma (module type 1+1+3+3bar, dim 8, TWO singlets) -- same NOMIZU/ADNU data, same Leibniz-rule construction -- gives an invariant-sector kernel of 0, not 1: the first kernel!=1 result after four prior non-discriminating attempts (C73/C73b), and ROBUST across C73b's own already-certified 2-dim admissible su(3)-equivariant torsion family (13-angle sweep: |c(theta)| constant to 6.7e-16, kernel=0 at every angle, never 1 -- 'topologically protected' in exactly the sense C73b certified for round59's own kernel=1, NOT a single-point accident). c=<w_hat,D'u_hat>=-2*sqrt(3)/3 exact (sympy), s=|c|^2=4/3, verified two independent routes (numeric SVD and exact sympy nullspace), Hermitian, exactly linear in the NOMIZU scale t. Undisclosed-symmetry check (pre-registered, before the kernel computation): no equivariant map Sigma->m exists (Sigma's only achievable {NAB_i}-invariant dims are {0,4,8}; direct intertwiner-nullspace search confirms 0). QUALIFIED per two independent skeptic passes (both WEAKENED verdicts, both findings incorporated, not dismissed): (1) Term1 (identity-on-twist piece) is EXACTLY 0, but this is FORCED by su(3) Schur's lemma for ANY zero-singlet twist bundle (independently verified: the untwisted operator A is exactly su(3)-equivariant and annihilates ODD_IDX's 3-piece identically), NOT independent evidence of a special result -- conceded in full. (2) The genuinely non-forced, load-bearing fact is narrower: Term2 (the twist bundle's OWN Levi-Civita connection contribution) is nonzero, robustly across the whole admissible family (confirmed by the angular sweep, addressing the OTHER skeptic pass's single-point-accident concern). (3) domain/target invariant sectors are each 1-dimensional (not round59's 2,1) because m has zero singlets -- this shape difference is itself a direct, forced consequence of the module-type choice, not fully independent of the kernel-value difference. One self-caught sign-convention bug (bivec_to_6x6 vs spin_lift represent the same so(6) generator with opposite sign under this project's e_k^2=-1 convention) found, fixed, and independently re-derived by BOTH skeptic passes from first principles (three independent confirmations total)."
    truth_status: SUPPORTED
    test_outcome: PASS
    execution_status: READY
    evidence_status: INTERNALLY_CERTIFIED
    lifecycle_status: ACTIVE
    evidence_file: "tom_s3_spinor_toy/experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md"
    depends_on: [C2_ROUND59_KERNEL_DIM1]
    supersedes: "no prior claim -- resolves pearl_registry row 89's own literal question for the first time, with an explicit qualification on evidentiary strength (see notes/statement)"
    does_not_imply:
      - "that C2_ROUND59_KERNEL_DIM1 or N_gen=3 is falsified -- round59's OWN Sigma-twisted kernel=1 is independently re-confirmed here (Section 5), untouched"
      - "what the specific physical justification for choosing Sigma over m is -- only that one is now genuinely needed, not previously testable at all"
      - "that D_S6 discriminates Sigma from a twist bundle of MATCHED singlet count (the more directly comparable test to round59's own (2,1)-shaped certificate) -- not attempted; the current result compares Sigma to a twist of DIFFERENT shape (1,1), which two independent skeptic passes confirmed is a real but narrower discrimination than round59's own certificate structure"
      - "that the su(3)-adjoint alternative (dim 8, module type 8, named but not attempted) would give the same or a different result"
      - "any change to N_gen=3's CONDITIONAL status"
```

**`pearl_registry/INDEX.md`** -- close row 89 (append, matching the style
C121/C138 used to close prior rows):

```
**RESOLVED, C139 (2026-09-04), PROMOTE (qualified -- see decision.md for the full, two-skeptic-pass-revised account, not just this summary).** The construction this row named as "the only unexplored route" is now built: twisting D_S6 by m_C (tangent/isotropy rep, module type 3+3bar, dim 6, zero su(3) singlets, genuinely different from Sigma's 1+1+3+3bar/two-singlets) gives invariant-sector kernel=0, not 1 -- robust across C73b's own already-certified 2-dim admissible torsion family (13-angle sweep, kernel=0 at every angle, never 1), not a single-point accident. Two independent context-blind skeptic passes both returned WEAKENED and both findings were incorporated, not dismissed: the round's original "Term1=0 is a clean structural mechanism" argument was shown to be circular (forced by Schur's lemma for ANY zero-singlet twist, verified independently in-round) -- the genuinely non-forced content is narrower, specifically Term2's (the twist connection's own contribution) robust non-vanishing. domain/target being 1-dim (not round59's 2,1) is a direct, forced consequence of the zero-singlet module-type choice, not fully independent of the kernel-value difference. One self-caught sign-convention bug (bivec_to_6x6 vs spin_lift, opposite sign under this project's e_k^2=-1 convention) found and independently re-derived by both skeptic passes (three confirmations total). Does NOT falsify N_gen=3 or C2_ROUND59_KERNEL_DIM1 (round59's own kernel=1 independently re-confirmed, Section 5) -- narrows round59's twist choice to needing independent physical justification. The MOST DIRECTLY comparable test to round59's own (2,1)-shaped certificate -- a matched-singlet-count twist bundle, e.g. m(+)2*1 -- remains unbuilt and is the single most valuable next step (both skeptic passes independently converged on this). See CLAIM_LEDGER.yaml C139_ALTERNATE_TWIST_M_KERNEL_ZERO and this decision.md (Sections 8b/8c/11/12 especially) for the full derivation and both skeptic passes in full.
```

**`PARENT_ACTION_GATE.md`** -- one-line addition to the relevant OB1/
headline-evidence tracking section (exact placement per the orchestrating
session's judgment; suggested wording): *"round59's kernel=1 result now
has its first genuine wrong-twist kernel!=1 result (C139, alternate twist
by the tangent rep m_C, kernel=0, robust across the whole admissible
connection family, not a single-point accident) -- round59's specific
twist choice (Sigma) is not the unique construction giving a nontrivial
invariant kernel; independent physical justification for Sigma is now a
well-posed, testable open question, not previously even askable. Two
independent skeptic passes qualified the strength of this finding
(kernel-value difference partly reflects forced representation-theory
shape, not purely dynamics); the decisive follow-up (a matched-singlet-
count twist bundle) remains unbuilt."*

**`OPEN_BLOCKERS.md`** -- proposed new item (or amendment to an existing
A3-shaped item, per the orchestrating session's judgment): *"why Sigma
(not m, or another twist bundle) is the physically correct twist for
round59's D_S6 construction -- C139 established that this question is
now well-posed (an alternative WITH a different kernel exists), but did
not answer it. BLOCKED-EXTERNAL-OR-THEORETICAL: likely requires either a
physical argument from Tom Lawrence's own framework for why the twist
bundle must be another copy of the spinor bundle specifically, or an
internal argument this project has not yet attempted."*

**`null_results/INDEX.md`** -- NOT applicable (this round's verdict is
PROMOTE, not REJECT).

**Concrete next-step recommendation (both skeptic passes independently
converged on this -- flagged here as the single most valuable follow-up,
not merely filed as a passive caveat):** build a **matched-singlet-count**
twist bundle -- e.g. `m_C (+) 2*1` (dimension 8, module type `3+3bar+1+1`,
matching `Sigma`'s OWN singlet count exactly while still differing in
which specific irreducible pieces carry the non-trivial content) -- and
recompute the certificate. This would be the most directly
shape-comparable test to round59's own `(2,1)`-shaped certificate, and
would isolate whether `D_S6` discriminates `Sigma` from a genuinely
alternative construction of the SAME invariant-sector shape, closing the
residual gap both skeptic passes identified. Comparable in scope to this
round's own build (a new twist bundle plus its connection), not a large
undertaking.

## 16. Verification

- `python -m ruff check experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/`
  -- (run separately, not re-verified here per house instruction against
  running the full suite; script itself formatted clean by the project's
  own pre-commit hook during drafting).
- `c139_twisted_s6_alternate_representation.py` -- **30 distinct boolean
  check names from 29 call sites, 30/30 PASS, 0 FAIL.** AST self-audit
  confirms no `check()` call is passed a literal constant.
- Two genuine defects self-caught and fixed BEFORE this document reached
  its first-draft form (not found afterward by an external reviewer): (i)
  a block-index mistake in the round59-reproduction self-check (§3d) that
  IMMEDIATELY exposed a second, independent bug; (ii) the sign-convention
  mismatch between `bivec_to_6x6` and `spin_lift` itself (§3d), the
  round's central self-caught finding, independently re-derived by BOTH
  subsequent skeptic passes.
- Two genuine defects in the INTERPRETATION (not the computation) caught
  by the two independent skeptic passes AFTER the first draft, and both
  fully resolved within this same round rather than deferred: (i) the
  `Term1=0` "mechanism" was circular (skeptic pass 1, §11, confirmed by
  in-round follow-up computation, §8b); (ii) the family-wide robustness
  of `Term2!=0` was asserted without having been checked (skeptic pass 2,
  §12, resolved by the angular sweep, §8c, which strengthened rather than
  weakened the result).
- Every load-bearing number verified from at least two independent
  angles: `domain_inv`/`target_inv` dimensions (Clebsch-Gordan prediction
  vs. numeric SVD vs. exact sympy nullspace -- three-way agreement); `c`
  (numeric SVD-basis route vs. exact sympy route, matching in magnitude,
  PLUS constant across a 13-angle family sweep); the sign-convention fix
  (empirical structure-constant match vs. an independent by-hand
  derivation from the Clifford algebra, re-derived independently by BOTH
  skeptic passes -- four confirmations total); the CG counting method
  (validated against round59's OWN already-certified `(2,1)` before being
  trusted for `m`'s `(1,1)` prediction); `Term1=0`'s forced status
  (skeptic-asserted, independently re-derived and computed in this round,
  §8b).
- Repo-wide test suite not run (no shared code touched; only new files
  inside this experiment's own directory; C73/C73b/round59's own files
  read but not modified).

---

## Evidence tier of the central conclusion

**Central conclusion (revised to match what the two skeptic passes
actually leave standing, not the first draft's stronger claim):**
*twisting round59's S6 Dirac operator by `W'=m_C` (the complexified
tangent/isotropy representation, module type `3+3bar`, dimension 6, zero
`su(3)` singlets) instead of `Sigma` (module type `1+1+3+3bar`, dimension
8, two singlets) -- using the identical Leibniz-rule construction and the
same `NOMIZU`/`ADNU` connection data -- gives an invariant-sector kernel
dimension of `0`, not `1`, ROBUSTLY across the whole admissible
connection family (not a single-point accident). This is a real,
first-ever `kernel!=1` result for this question. Its mechanism is
narrower than originally claimed: the `(1,1)`-shaped invariant sector and
`Term1`'s exact vanishing are BOTH forced by `su(3)` representation
theory the moment a zero-singlet twist bundle is chosen (true for ANY
such twist, not special to `m`); the genuinely non-forced, load-bearing
fact is that `Term2` (the twist bundle's own Levi-Civita connection
contribution) is nonzero and stays nonzero across the entire admissible
family.*

**Tier: `[VERIFIED-tool]`, confidence HIGH** for the computation itself --
30/30 machine checks pass, the headline number cross-verified via two
independent routes (numeric float and exact sympy Rational/`sqrt(3)`
arithmetic, agreeing in magnitude to `<1e-6`) PLUS constant across a
13-angle sweep of the full admissible connection family, the generalized
machinery independently validated by exactly reproducing round59's own
certified, skeptic-reviewed `(a,b,s)=(-1,-sqrt(3),4)` before being
trusted on the new representation, one genuine self-caught sign-
convention defect found and fixed via a representation-agnostic
regression check and independently re-derived by two further adversarial
agents, and the undisclosed-symmetry trap (the exact failure mode of
C73's attempt (b)) explicitly checked and cleared BEFORE the kernel value
was computed.

**Tier of the "meaningfully discriminating" interpretation: split into
its two now-separated components, per both skeptic passes:**

- **`Term1=0` is FORCED, `[VERIFIED-tool]`, confidence HIGH, NOT
  independent evidence of anything special about `m`** -- this was the
  first draft's central error (§8's original framing), caught by skeptic
  pass 1, independently re-derived and computed in this same round
  (§8b: `A` is exactly `su(3)`-equivariant, annihilates `ODD_IDX`'s
  `3`-piece identically, `max|[A,su3_ops[a]]|=0.0` all `a`). Conceded in
  full, not minimized.
- **`Term2 != 0`, robust across the whole admissible connection family,
  `[VERIFIED-tool]`, confidence HIGH** -- this is the round's actual
  load-bearing, non-forced finding, established by the angular sweep
  (§8c, triggered by skeptic pass 2's correct objection that a
  single-point sample does not establish family-wide robustness):
  `|c(theta)|` constant to `6.7e-16` across 13 angles spanning C73b's own
  certified 2-dim admissible family, matching the SAME "topologically
  protected, magnitude-constant" signature C73b found for round59's own
  `b`-coefficient.
- **Whether "`Term2 != 0`, robustly" carries the SAME evidentiary weight
  as round59's own full `(a,b,s)` certificate (built from a `(2,1)`-shaped
  sector, not `(1,1)`) -- `[INFERRED]`, confidence MEDIUM** -- genuinely
  not fully closed by computation alone; both skeptic passes independently
  converged on the same concrete resolution (a matched-singlet-count
  twist bundle), named as the decisive next step (§16), not attempted
  here.

**Marker on the whole round:** PROMOTE on the literal, pre-registered
predicate (`kernel != 1`, verified, robust, not a hidden-symmetry
artifact) -- explicitly NOT on the stronger "clean discriminating
mechanism comparable to round59's own certificate" claim the first draft
made, which was withdrawn in full (§8b) after skeptic pass 1, with the
round's genuinely non-forced content relocated to `Term2`'s robust
non-vanishing (§8c) after skeptic pass 2. Two independent, context-blind,
differently-worded skeptic passes both returned `WEAKENED`; both sets of
findings were incorporated into this decision.md itself (not merely
logged and left unaddressed), one via a full concession and reframing,
the other via new computation that strengthened the result. Carried
forward explicitly, not smoothed over, into the proposed
`CLAIM_LEDGER.yaml` entry and pearl-registry closure text (§15).
