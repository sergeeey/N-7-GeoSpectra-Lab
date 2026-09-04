# C141 decision -- twist bundle W'' = m_C (+) 2*1 (dim 8, module type
# 3+3bar+1+1, TWO su(3) singlets -- matching Sigma's own two-singlet count),
# using the precheck-cleared "decoupled extra singlets" connection --
# NULL, QUALIFIED (deflationary): claim.md's own naive "matched singlet
# COUNT implies matched invariant-sector SHAPE to round59's own restricted
# (2,1)" is FALSE (verified: domain=target=3). Two SUCCESSIVE context-blind
# skeptic passes progressively corrected this decision.md's own verdict.
# Pass 1 found the first draft's BLOCKED conclusion was itself wrong (a
# genuine shape-matched reference point, "T1" = Sigma self-twisted
# unrestricted, DOES exist and was computed: shape (3,3), kernel=1,
# matching m(+)2*1's own shape exactly) -- this looked, at first, like a
# genuine PROMOTE (kernel 1 vs 0 at matched shape). Pass 2 then found THAT
# conclusion was ALSO wrong: the kernel difference (1 vs 0) is FULLY
# explained by a graded (per-connection-summand, not merely aggregate)
# rank-nullity floor, computable from PURE su(3) branching data alone --
# independently reverified here, exactly matching the observed kernel in
# all 4 twist-bundle constructions ever computed in this project's history
# (round59, C139, C141, T1). The round's own Dirac-operator computation
# contributes NO new geometric/dynamical fact beyond what round59 and C139
# already separately established (each individual channel's connection
# data is nonzero) -- the AGGREGATE kernel outcome, given that, is pure
# representation-theory arithmetic. This is the round's real, honest,
# and considerably more significant finding than either of the two
# provisional verdicts that preceded it.

**Date:** 2026-09-04
**Experiment:** `20260904-c141-matched-singlet-count-twist-m-plus-2singlets`
**Question type (EstimandOps L0):** Descriptive.
**Script:** `c141_matched_singlet_twist.py` -- **Results:** `results_c141.json`

## Verdict

```text
NULL_QUALIFIED__KERNEL_DIFFERENCE_IS_A_GRADED_BRANCHING_ARTIFACT_NOT_DYNAMICS
  __CLAIM_MD_NAIVE_2_1_PREDICTION_FALSE__VERIFIED_DOMAIN_TARGET_3_3_TWO_ROUTES
  __DRAFT_1_BLOCKED_VERDICT_FALSIFIED_BY_SKEPTIC_PASS_1__T1_COMPARISON_FOUND
  __T1_SIGMA_SELF_TWIST_UNRESTRICTED__SHAPE_3_3__KERNEL_1__ROBUST_13_ANGLES
  __DRAFT_2_PROMOTE_VERDICT_ITSELF_FALSIFIED_BY_SKEPTIC_PASS_2__GRADED_FLOOR
  __GRADED_PER_SUMMAND_RANK_NULLITY_FLOOR_EXACTLY_PREDICTS_KERNEL_IN_4_OF_4_CASES
  __ROUND59__C139__C141__T1__ALL_MATCH_FLOOR__NO_PURELY_GEOMETRIC_RESIDUE_FOUND
  __KERNEL_DIFFERENCE_COMPUTABLE_FROM_SU3_BRANCHING_ALONE__NO_DIRAC_OPERATOR_NEEDED
  __LITERAL_KERNEL_VALUES_STAND_VERIFIED__INTERPRETATION_AS_DYNAMICS_WITHDRAWN
  __SPECULATIVE_INTERNALLY_GRADED_CONSTRUCTION_PROPOSAL_WITHDRAWN__PROVEN_IMPOSSIBLE
  __TWO_SKEPTIC_PASSES_RUN__EACH_FALSIFIED_THE_PRIOR_DRAFTS_OWN_VERDICT__SEE_SECTIONS
```

**One line:** the naive expectation ("matching Sigma's total singlet count
gives a matching invariant-sector shape `(2,1)`") is false -- verified two
independent ways, `m(+)2*1` gives `(3,3)`. This decision.md went through
**three** verdicts before landing on this one, each overturned by an
independent, context-blind check -- reported here in full, not smoothed
over. **Draft 1** concluded `BLOCKED` (no valid shape-matched comparison
possible). **A context-blind FL Step 8a skeptic pass 1** found this wrong:
the correct comparison is not against round59's own `EVEN_IDX`-restricted
`(2,1)` certificate, but against **Sigma self-twisted with the SAME
unrestricted-second-factor convention** this round already applies to
`m(+)2*1` (computed for the first time here, "T1": shape `(3,3)`, matching
`m(+)2*1`'s own shape exactly, kernel `= 1`, robust across the whole
13-angle admissible family, containing round59's own certified sector as
an exact subspace -- Section 9). **Draft 2**, on this basis, concluded
`PROMOTE`: kernel `1` (Sigma self-twist) vs kernel `0` (`m(+)2*1`),
identical shape, a genuine discrimination. **A second, differently-worded,
context-blind skeptic pass 2 then found THIS conclusion wrong too**: both
`T1` and `m(+)2*1` are direct sums over `{connection}`-invariant summands
of their twist bundle (already conceded for `m(+)2*1` in draft 2's own
Section 8; true for `T1` too, since round59's own connection `NAB`
provably preserves the `EVEN_IDX`/`ODD_IDX` split exactly). Applying
rank-nullity **per summand**, not to the aggregate `(3,3)` shape, gives a
**graded floor** computable from pure `su(3)` branching data alone (Section
10) -- and this floor **exactly equals the observed kernel in all four**
twist-bundle constructions ever computed in this project's history (round59
`=1`, C139 `=0`, this round `=0`, `T1` `=1`), independently re-verified
here by direct computation, not merely accepted from the skeptic. **The
kernel difference this round set out to find is therefore fully explained
by pure representation theory, given only the ALREADY-ESTABLISHED (by
round59/C139, not new to this round) fact that each individual channel's
connection data is nonzero -- it requires no new geometric computation
about `D_S6` at all.** This is reported honestly as the round's real
finding: a **deflationary, methodologically important** result (this whole
family of "kernel of the twisted Dirac operator" tests may not probe
`Sigma`-specific dynamics the way the "why `Sigma`, not `m`" research
question assumed), not the shape-controlled discrimination either earlier
draft claimed.

---

## 0. Background, read in full before computation (per claim.md)

- `experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`
  IN FULL, especially Sections 2, 3d, 5, 8b, 9, 11, 12, and 17 (the
  equivalence precheck).
- `experiments/20260904-c139-.../c139_precheck_m_plus_2singlets.py` -- the
  pre-cleared "decoupled extra singlets" construction this round reuses
  directly.
- `experiments/20260714-round59-trivial-rank-certification/round59_route_a_independent.py`
  and its `decision.md` -- **read in full for THIS round's own revision**,
  not merely cited secondhand via C139: round59's own `certificate()`
  function (script lines 268-303) and `main()` (lines 351-360) show
  explicitly that the certified `(a,b,s)=(-1,-sqrt(3),4)`, `(2,1)` result
  restricts the SECOND factor of the domain/target blocks to `EVEN_IDX`
  specifically (`domain_second=EVEN_IDX`, `target_second=EVEN_IDX`), not
  the full 8-dim Sigma -- this is the fact the first draft of this
  decision.md missed and the skeptic pass caught (Section 9).
- `experiments/20260811-c73-.../decision.md` and
  `experiments/20260811-c73b-.../decision.md` -- four prior
  non-discriminating wrong-twist attempts, for context.
- `pearl_registry/INDEX.md` row 89 and `OPEN_BLOCKERS.md` OB14 ("why
  Sigma, not m").
- `CLAIM_LEDGER.yaml` `C139_ALTERNATE_TWIST_M_KERNEL_ZERO` and
  `C2_ROUND59_KERNEL_DIM1` -- `does_not_imply` fields read in full.

### 0a. Quoted verbatim -- the exact precheck conclusion this round reuses

C139 decision.md Section 17 (ADDENDUM): *"the twisted Dirac construction
does **not** depend on `su(3)`-branching alone... Verified directly, not
just argued `[VERIFIED-tool]`: an explicit intertwiner-nullspace search...
returns nullspace dimension **0**... A full C141 round on `m(+)2*1`, using
this natural (decoupled-singlet) construction, would be a real,
non-redundant, decisive test."*

C139 decision.md Section 3d (the passage this round's Section 9 directly
builds on): *"the SAME run's Verification-Substrate-Gate self-check (§5)
... was ALSO wrong (`domain=3, target=3` instead of the certified `2,1`)
... That specific self-check bug was a block-index mistake (using the full
8-dim second factor instead of round59's own `EVEN_IDX`-restricted second
factor) and was fixed first."* -- **this round's Section 9 recognizes that
the "buggy" `(3,3)` configuration C139 discarded here is, under a
consistent unrestricted-second-factor convention, the mathematically
correct comparandum for `m(+)2*1`'s own `(3,3)` shape, and computes its
KERNEL for the first time.**

## 1. Zero-Signal Gate (FL Step -5)

| field | content |
|---|---|
| Entity | a twisted S6 Dirac operator `D''_{S6,twist=m+2*1}`, twisted by `m(+)2*1` (dim 8, TWO singlets, module type `3+3bar+1+1`) with the precheck-cleared decoupled-singlet connection |
| Falsifiable predicate | the invariant-sector kernel of `D''` differs from the kernel of the METHODOLOGICALLY CONSISTENT self-twisted-Sigma reference operator, at MATCHED invariant-sector shape |
| Measurable outcome | the explicit kernel dimensions of both `D''` and the corrected reference operator, and the domain/target invariant-sector shapes of both, computed via numeric SVD + exact sympy |

All three fillable => gate **PASSES**.

## 2. PRE-REGISTRATION -- Clebsch-Gordan derivation, done by hand BEFORE
   any invariant-sector computation, per claim.md's explicit instruction

**Claim.md's own naive expectation:** *"predict `(2,1)` via Clebsch-Gordan
BEFORE computing, matching `Sigma`'s own shape, since the singlet count now
matches."*

**This round's own by-hand derivation** (script Section 1, `trivial_mult()`,
a genuinely computed, failable function): using `EVEN_IDX = 1(+)3bar`,
`ODD_IDX = 3(+)1`, `W'' = 3(+)3bar(+)1(+)1`, Frobenius reciprocity gives
`domain = mult_W(3bar)+mult_W(1) = 1+2 = 3`, `target = mult_W(1)+mult_W(3)
= 2+1 = 3` -- **predicted `(3,3)`, NOT claim.md's naive `(2,1)`.**

**Cross-validation of the method:** the SAME `trivial_mult()` formula
reproduces round59's own certified `(2,1)` exactly when applied to
`EVEN_IDX` as the twist module (`[VERIFIED-tool]`
`cg_method_reproduces_round59_own_certified_domain_2_via_trivial_mult_function`
and the matching `target` check).

**Section 1b -- general formula, added in response to skeptic pass 1
(Section 9's own finding, F5 in the response matrix below), SUPERSEDING
the first draft's less general "asymmetric split" framing (left visible
below per the Hindsight Distortion Gap Heuristic, not deleted):**

For ANY twist module `W`, `domain - target = mult_W(3bar) - mult_W(3)`
EXACTLY (`[VERIFIED-tool]`
`f5_general_domain_minus_target_formula_holds_for_all_test_modules`,
checked against `EVEN_IDX`, `m`, `m+2*1`, and full `Sigma` -- all match).
This is the PRECISE, general reason claim.md's naive expectation fails:
round59's own twist bundle, in the sense relevant to its certified `(2,1)`
shape, is **`EVEN_IDX` alone** (dim 4, module type `1+3bar`, ONE singlet,
`mult(3bar)-mult(3) = 1`) -- NOT the full 8-dim `Sigma` (which, self-
twisted without restriction, has `mult(3bar)-mult(3) = 0`, giving shape
`(3,3)`, matching `m+2*1` exactly -- Section 9 below). The first draft's
"Sigma's two singlets split asymmetrically between `EVEN_IDX`/`ODD_IDX`"
account was directionally motivated but imprecise about WHAT is actually
being compared; this general formula is the corrected, verified account.

**Original (first-draft) framing, left in place, NOT deleted:** *"in
`Sigma`, the two singlets are split, one into `EVEN_IDX`... and one into
`ODD_IDX`... A twist bundle's singlet contributes to the domain/target
count only through its pairing with `ODD_IDX`'s or `EVEN_IDX`'s own
singlet respectively."* This is not WRONG as a description of why `m+2*1`
gives `(3,3)`, but it obscured the fact that round59's OWN reference shape
`(2,1)` comes from a DIFFERENT, smaller object (`EVEN_IDX` alone, dim 4)
than "Sigma's own shape" (which, computed consistently, is `(3,3)`, same
as `m+2*1`) -- this is the correction Section 9 makes precise and
decisive.

**Section 1b also adds (skeptic pass 1 findings F6, F7):**

- **F6 -- counting-bound context:** rank-nullity forces `kernel >=
  domain-target` whenever `domain>target`, for ANY operator, independent
  of the specific Dirac construction. round59's own `kernel>=1` is
  THEREFORE partly a free consequence of its `(2,1)` shape (`[VERIFIED-tool]`
  `f6_round59_kernel_ge_1_is_partly_a_free_shape_consequence`) -- its real,
  non-forced content is that rank is EXACTLY 1 (the map is nonzero), not
  more. For `m+2*1` and for T1 (Section 9), `domain=target=3`, so this
  bound is TRIVIAL (`kernel>=0`, no information) on BOTH sides
  (`[VERIFIED-tool]`
  `f6_c141_own_comparison_domain_equals_target_bound_is_trivial`) --
  meaning the kernel difference found in Section 9 (`1` vs `0`) is **fully
  "real" content on both sides, not a shape-forced artifact either way**.
  This STRENGTHENS, not weakens, the validity of the Section 9 comparison.
- **F7 -- exhaustive check that no "2-singlet, internally-graded"
  construction can achieve `(2,1)`:** a brute-force search over
  `(mult_1,mult_3,mult_3bar) in {0,1,2,3}^3` finds `(domain,target)=(2,1)`
  holds ONLY for `(1,0,1)` (`= EVEN_IDX` itself) and `(0,1,2)` (a different,
  not-yet-tried module type) -- `[VERIFIED-tool]`
  `f7_2_1_shape_requires_exactly_these_two_module_types`. **Neither has 2
  singlets**, so ANY twist bundle carrying two singlets (`mult_1=2`,
  including the internally-even/odd-graded construction the first draft of
  this decision.md proposed in a now-WITHDRAWN Section 11.4 and pearl-
  registry row) is **provably incapable** of reproducing round59's own
  `(2,1)` shape. This is not a limitation of this round's imagination --
  it is a closed, exhaustively-checked fact. That speculative proposal is
  withdrawn in full (Section 15's registry proposals reflect this).

## 3. Twist bundle construction -- reused, not re-derived, per claim.md's
   explicit instruction

`W'' = m_C (+) 2*1` (dim 8, module type `3+3bar+1+1`). Connection:
`conn_i = rho_vector(NOMIZU[i]) (+) 0_2` for `i=1..6` -- **the precheck's
own construction object, imported directly** (`PRECHECK.conn_m_plus_2singlets`),
not a re-typed formula.

`[VERIFIED-tool]` (fresh, in this round's own script):

- `conn_w2_extra_singlets_fully_decoupled_full_2x2_block_zero`.
- `conn_w2_top_left_6x6_matches_c139_rho_vector_m_exactly`.

The `su(3)`-generator (`ADNU`) action on `W''` -- built fresh here (not
present in the precheck): `rho_vector(ADNU[a])` on the `m`-block, exact
ZERO on the two extra (trivial-by-construction) singlets, `a=1..8`.

**Module-type check, `[VERIFIED-tool]`:**

- `w2_commutant_dim_6_matches_3_plus_3bar_plus_1mult2` -- commutant
  dimension `6` (`= 1^2+1^2+2^2`, confirming module type `3+3bar+1(mult 2)`).
- `w2_has_exactly_2_su3_singlets` -- confirms singlet COUNT genuinely
  matches `Sigma`'s own (Section 9 resolves what "matches" should actually
  mean at the SHAPE level).

## 4. Re-verification of the precheck's equivalence result (in-round,
   not mere citation) -- skeptic-pass-1-scoped honestly (F8, F9)

A fresh `intertwiner_nullspace(...)` search, run in THIS round's own
script:

```
[VERIFIED-tool] no_equivariant_map_sigma_to_w2_reverified_fresh_in_c141
  dim(intertwiner space) = 0
[VERIFIED-tool] c141_reverification_matches_precheck_own_null_dim
  c141 fresh = 0, precheck = 0
```

**Honest scoping, per skeptic pass 1 finding F8 (accepted):** this
re-execution uses the SAME numerical method (vec-Kronecker intertwiner
search) and the SAME connection object (`PRECHECK.conn_m_plus_2singlets`)
as the precheck's own check -- it is a genuine REPRODUCIBILITY check
(confirms the computation gives the same answer when re-run fresh, in a
different script, catching stale-cache/environment-dependent bugs), not an
INDEPENDENT-METHOD verification in the strong sense (a different algorithm
or implementation would be needed for that). This is a downgrade in
claimed strength from the first draft's language ("re-verified... not
merely citing"), made explicit here rather than left overclaimed.

**Per skeptic pass 1 finding F9 (accepted, scope noted):** the precheck's
OWN "second independent method" (Section 2 dimension-counting via
`achievable_dims = {0,4,8}`) hardcodes a fact already established in C139
Section 3b rather than independently re-deriving it -- this is a
limitation of the PRECHECK file itself (owned by C139, not modified by
this round per the task's read-only-reuse instruction), not of this
round's OWN re-verification, which relies only on the freshly-run,
non-hardcoded intertwiner-nullspace search above.

Kill criterion (c) (Section 11) does not fire, on this basis.

## 5. su(3)-invariant sector dimensions -- verify Section 2's prediction

`[VERIFIED-tool]`, numeric SVD nullspace:

```
domain_inv (ODD_IDX (x) W'') = 3     (predicted 3, MATCHES)
target_inv (EVEN_IDX (x) W'') = 3    (predicted 3, MATCHES)
```

**`[FAIL]` (intentional, informative, per claim.md's kill criterion (b)):**
`shape_matches_claim_md_naive_2_1_expectation` -- computed `(3,3)` vs
claim.md's own naive `(2,1)`. This finding stands, unchanged from the
first draft -- what changes (Section 9) is the CONCLUSION drawn from it.

## 6. Main computation: D'' restricted to the `(3,3)` invariant sector

`[VERIFIED-tool]` `d_dprime2_is_hermitian`: exact.

**Certificate:**

```
block shape = (3, 3)
singular values = [1.7320508, 1.7320508, 1.1547005]   (all clearly nonzero)
rank = 3   (FULL rank)
kernel_dim = 0
```

`[VERIFIED-tool]` exact sympy cross-check confirms `kernel_dim_exact = 0`,
matching numeric exactly (Section 7 of the script).

## 7. Exact (sympy) cross-check and mechanistic decomposition

Exact block matrix:

```
  [        0      -sqrt(3)         0     ]
  [        0          0        -sqrt(3)  ]
  [ -2*sqrt(3)/3       0            0    ]
```

`Term1`/`Term2` decomposition (`D'' = Term1+Term2`, `Term1` = Sigma-only,
identity on twist factor; `Term2` = twist bundle's own connection):

**Basis-dependent (exact entries, `[VERIFIED-tool]`):** `Term1` has 2
nonzero entries, both `-sqrt(3)`; `Term2` has 1 nonzero entry,
`-2*sqrt(3)/3`, an EXACT symbolic match to `C139.c_exact` (imported live
from the freshly-reloaded C139 module).

**Basis-INDEPENDENT restatement, added in response to skeptic pass 1
findings F10/F11 (the entrywise "permutation pattern" depends on the
specific orthonormal basis `gram_schmidt` returns; rank and singular
values do not):**

```
[VERIFIED-tool] term1_rank_is_exactly_2_basis_independent
[VERIFIED-tool] term1_nonzero_singular_values_both_equal_sqrt3
[VERIFIED-tool] term2_rank_is_exactly_1_basis_independent
[VERIFIED-tool] term2_sole_nonzero_singular_value_equals_c139_abs_c_exact
```

`Term1` has rank exactly `2` (both nonzero singular values `= sqrt(3)`
exactly); `Term2` has rank exactly `1` (its sole nonzero singular value
`= |C139.c_exact| = 2*sqrt(3)/3` exactly) -- these facts are invariant
under any change of orthonormal basis on `domain_inv`/`target_inv`
separately, unlike the specific matrix entries above.

**Interpretation:** two of the three `(3,3)` channels carry only `Term1`
(round59's own Killing eigenvalue, `-sqrt(3)`, duplicated once per extra
decoupled singlet); one channel carries only `Term2` (C139's own isolated
`m`-twist result, embedded unchanged). `kernel=0` here arises because all
three channels are independently nonzero. **Section 8 addresses whether
this makes the result "forced" or trivial.**

## 8. Skeptic-pass-1-triggered: is this decomposition a discovery, or
   forced by construction? (response to finding F3, accepted in full)

**Skeptic pass 1's finding F3, accepted without qualification:** the
decoupled-singlet connection mandated by claim.md (`conn_i =
rho_vector(NOMIZU[i]) (+) 0_2`) makes `D''` a DIRECT SUM, by construction,
BEFORE any computation: for `w` in the `m`-block, `D''` acts exactly as
C139's own `D'_{Sigma(x)m}`; for `w` an extra singlet (zero connection),
`D''(eta(x)w) = (A eta)(x)w` where `A = sum_i E_i NAB_i` is round59's own
untwisted operator. **`D'' = D'_{Sigma(x)m} (+) A (+) A`, derivable in two
lines, known before Section 7's computation.** The first draft's framing
of Section 7/8's decomposition as "the load-bearing finding of this round"
overstated its novelty; the SKEPTIC's two-line argument is the real
derivation, and this round's exact/basis-independent verification
(Sections 7 above) CONFIRMS it computationally rather than discovering it.
Accepted in full, not minimized.

### 8a. Draft-2 argument for why the positive result survives this
    concession -- WITHDRAWN by skeptic pass 2 (Section 10), left visible
    per the Hindsight Distortion Gap Heuristic, NOT deleted

**[The text below is this decision.md's SECOND draft reasoning. It is
WRONG, in the specific way Section 10 makes precise. Left in place,
unedited, so the incorrect reasoning stays on record rather than being
silently replaced -- do not read this subsection as this document's
current position; read Section 10.]**

*"The concession applies EQUALLY to T1 (Section 9) -- and the comparison
between the two is not thereby made empty. T1 (Sigma self-twisted,
unrestricted) is ALSO shown (Section 9's subspace-embedding check) to
decompose: round59's own certified (2,1)/kernel-1 sub-block, embedded
exactly, plus a "new" 2x1 sub-block that is automatically full rank (any
nonzero 2x1 matrix is injective). Both T1's kernel=1 and m+2*1's kernel=0
are, in this sense, "explained" by recognizable, previously-established
building blocks -- neither is a surprising new mechanism.*

*What is NOT explained by shape or by the individual building blocks alone
is the DIFFERENCE in overall rank. At the level of the full (3,3) sector,
the rank-nullity bound is trivial for BOTH constructions (Section 2's F6
finding: domain=target=3 on both sides, kernel>=0 gives no information)...
This structural difference -- not a "new mechanism" in either individual
piece, but a genuine difference in how the SAME shape's pieces combine --
is the round's verified, non-overstated positive result."*

**Why this is wrong (found by skeptic pass 2, Section 10, independently
re-verified by direct computation, not merely accepted):** the error is
applying rank-nullity to the AGGREGATE `(3,3)` shape and stopping there.
Both `T1` and `m+2*1` are direct sums over MULTIPLE `{connection}`-invariant
summands (Section 8's own concession establishes this), and rank-nullity
must be applied **per summand**, not just in aggregate, because each
summand is an independently-acting block of the SAME operator with NO
cross-terms between summands (by construction, for `m+2*1`; by `NAB`'s
own `EVEN_IDX`/`ODD_IDX`-preservation, for `T1`). `T1`'s own two summands
have PER-SUMMAND shapes `(2,1)` (round59's own `EVEN_IDX`) and `(1,2)` (the
"new" piece) -- giving a GRADED floor of `max(0,2-1) + max(0,1-2) = 1 + 0 =
1`, exactly the observed kernel. `m+2*1`'s three summands (`m`, singlet,
singlet) each have shape `(1,1)` -- graded floor `0+0+0 = 0`, exactly the
observed kernel. **The "difference in overall rank" this subsection claimed
was non-forced IS forced, by the SAME rank-nullity argument correctly
applied at the right granularity.** See Section 10 for the full,
independently-verified analysis across all four twist bundles tested in
this project's history.

## 9. THE DECISIVE COMPARISON: T0/T1, the genuine apples-to-apples test
   (skeptic-pass-1-triggered, resolves the first draft's own BLOCKED
   verdict)

**Why this section exists.** The first draft of this decision.md, on
finding `shape != (2,1)` (Section 5), concluded the round was `BLOCKED`:
no valid shape-matched comparison to round59's own certificate was
possible. A context-blind FL Step 8a skeptic pass (Section 12) found this
conclusion itself was wrong, by identifying that round59's OWN certified
`(2,1)` is computed with the SECOND factor of its self-twist RESTRICTED to
`EVEN_IDX` (round59's own script, `round59_route_a_independent.py` lines
351-360: `domain_second=EVEN_IDX, target_second=EVEN_IDX`, not the full
8-dim second factor) -- a DIFFERENT convention than this round's own
`m(+)2*1` computation (Section 5), which uses the FULL, unrestricted
second factor throughout (`list(range(8))`, since `m(+)2*1` has no natural
`EVEN_IDX`-like sub-piece to restrict to). Comparing shapes computed under
two DIFFERENT conventions is not apples-to-apples.

**The methodologically consistent fix:** apply the SAME "unrestricted
second factor" convention this round already uses for `m(+)2*1` to
`Sigma`'s OWN self-twist. C139's own decision.md Section 3d recorded, as a
byproduct of an unrelated bug-hunt, that this configuration gives shape
`(3,3)` -- but the bug was simply fixed (restricted back to `EVEN_IDX`)
and the `(3,3)` configuration's KERNEL was never computed anywhere in this
project. **Computed here for the first time.**

### 9a. T0 -- positive control

Reproduces round59's own `EVEN_IDX`-restricted certificate EXACTLY, using
THIS section's own machinery, before T1 is trusted:

```
[VERIFIED-tool] t0_positive_control_reproduces_round59_shape_2_1
  domain=2, target=1
[VERIFIED-tool] t0_positive_control_reproduces_round59_kernel_1
  kernel=1
```

### 9b. T1 -- the apples-to-apples comparison

Sigma self-twisted (`conn_w = NAB`, i.e. `Sigma`'s own connection, the SAME
one round59 uses), with the SAME unrestricted-second-factor convention:

```
[VERIFIED-tool] t1_shape_matches_c141_own_w2_shape_3_3
  domain=3, target=3   -- EXACTLY matches m+2*1's own shape
```

```
T1 singular values = [2.0, 2.0, 0.0]
T1 rank = 2, T1 kernel_dim = 1
```

`[VERIFIED-tool]` `t1_exact_kernel_matches_numeric` (exact sympy, block
matrix reproduced in `results_c141.json`, `t0_t1_apples_to_apples_comparison.t1_block_exact`)
confirms `kernel=1` exactly, matching the numeric result.

`[VERIFIED-tool]` `t1_kernel_constant_across_whole_admissible_family` -- a
13-angle sweep of C73b's own admissible torsion family (identical
methodology to Section 8's own sweep for `m+2*1`) shows `T1`'s `kernel=1`
holds at EVERY tested angle -- robust, not a single-point accident.

### 9c. Subspace-embedding consistency: T1 is a faithful enlargement of T0
    (claim corrected per skeptic pass 2 finding D)

`[VERIFIED-tool]` `t0_domain_and_target_embed_exactly_in_t1` -- projecting
`T0`'s own domain/target basis vectors onto `T1`'s span gives residuals of
`1.1e-16` and `0.0` respectively: `T0`'s sector sits inside `T1`'s sector
as an exact subspace. **Corrected claim (skeptic pass 2, finding D,
accepted):** this specific fact is a NECESSARY consequence of elementary
linear algebra -- if `V` is a sub-representation of `W` (which `Sigma_even
= EVEN_IDX` is, of `Sigma`, since `NAB` preserves the grading, Section 3a),
then invariants of `V` are automatically invariants of `W`; the check
confirms this holds NUMERICALLY (a legitimate regression/sanity check on
the computation, catching a bug if one existed) but does not, by itself,
confirm anything SPECIFIC to this operator's dynamics. **The genuinely
informative version of this question -- do `T0` and `T1` share the SAME
kernel VECTOR, not merely a nested invariant-subspace structure -- is
answered in Section 9e (yes: `T1`'s kernel is literally round59's own
kernel vector, re-derived), which is where the real content of this
embedding lives.**

### 9d. The comparison itself

```
                        domain  target  kernel
T0  (round59, restricted)    2       1       1
T1  (Sigma self-twist,       3       3       1
     unrestricted -- the
     genuine reference point)
C141 (m+2*1, this round)     3       3       0
```

**`SHAPE-MATCHED DISCRIMINATION (T1 kernel != C141 kernel): True`**
(`[VERIFIED-tool]` printed directly by the script). Identical shape
`(3,3)`, identical (unrestricted-second-factor) methodology, kernel
differs: `1` for `Sigma` twisted by itself, `0` for `Sigma` twisted by
`m(+)2*1`. Both verified two independent routes (numeric SVD + exact
sympy), both robust across the whole 13-angle admissible connection
family. **This paragraph, and Section 8a above, is this decision.md's
SECOND-draft conclusion -- claiming the DIFFERENCE was "not forced by
shape" and therefore a "genuine, verified, shape-controlled
discrimination." Section 9e below (skeptic-pass-2-triggered) shows this
is WRONG: the difference IS forced, once shape is correctly understood at
the per-summand, not merely aggregate, level.**

## 9e. THE ACTUAL EXPLANATION: the graded rank-nullity floor
    (skeptic-pass-2-triggered, withdraws Section 8a/9d's "genuine
    discrimination" conclusion)

**Why this section exists.** A second, differently-worded, context-blind
FL Step 8a skeptic pass, given this decision.md's own SECOND draft
(Sections 0-9d as they then read, i.e. including the `T1`-vs-`m+2*1`
"genuine discrimination" conclusion) plus the script and results, found a
decisive flaw: Section 8 already concedes `m+2*1`'s `D''` is a direct sum
over its twist bundle's `{connection}`-invariant summands (`m`, singlet,
singlet); and round59's own connection `NAB` is independently established
(C139 Section 3a, reused fact) to preserve the `EVEN_IDX`/`ODD_IDX` split
of `Sigma` EXACTLY -- meaning `T1` (`Sigma` self-twisted) is ALSO a direct
sum, over exactly two `{connection}`-invariant summands: `Sigma_even` (=
`EVEN_IDX`, `T0`'s own twist bundle) and `Sigma_odd` (= `ODD_IDX`, a "new"
summand). **Rank-nullity, correctly applied PER SUMMAND rather than to the
aggregate `(3,3)` shape, gives a strictly stronger lower bound than
Section 2's F6 aggregate-only bound -- and this GRADED floor, computable
from `su(3)` branching data ALONE (no Dirac operator, no `NOMIZU`, no
connection geometry of any kind beyond knowing which summands exist),
EXACTLY equals the observed kernel.**

**Independently re-verified here (not merely accepted from the skeptic),
both by hand and in the registered script (`c141_matched_singlet_twist.py`
Section 10, `graded_floor()` function, check
`graded_rank_nullity_floor_exactly_predicts_observed_kernel_in_all_4_cases`):**

```
construction            {connection}-invariant summands      graded floor   observed kernel
T0 / round59             EVEN_IDX = {1,3bar}                       1              1
C139 (m)                 m = {3,3bar}  (single block,               0              0
                          not decoupled)
C141 (this round,        m={3,3bar}, singlet={1}, singlet={1}       0              0
 m+2*1)                  (THREE summands, decoupled by
                          construction)
T1 (Sigma self-twist)    Sigma_even={1,3bar}, Sigma_odd={3,1}       1              1
                          (TWO summands, decoupled by NAB's
                          own EVEN/ODD-preservation)
```

**4 of 4 match, exactly**, `[VERIFIED-tool]`. The graded floor for a
summand `W_k` is `max(0, mult_{W_k}(3bar) - mult_{W_k}(3))` (Section 2's
own `trivial_mult()`-derived formula, applied per summand instead of to
the aggregate); the total floor is the sum over summands. For `T1`:
`Sigma_even` contributes `max(0,1-0)=1` (round59's own forced floor,
Section 2's F6 finding, correctly applied to THIS summand); `Sigma_odd`
contributes `max(0,0-1)=0` (a "wide," automatically-injective direction,
domain 1 < target 2). Total `=1`, exactly the observed kernel. For `m+2*1`:
all three summands are square (`domain=target=1` each), contributing `0`
each; total `=0`, exactly the observed kernel.

**What this means, stated plainly, withdrawing Section 8a/9d's
conclusion:** the kernel DIFFERENCE between `T1` (`=1`) and `m+2*1` (`=0`)
that Section 9d called "a genuine, verified, shape-controlled
discrimination... not forced by shape" **IS fully forced by shape** --
specifically, by the GRADED shape (how many `{connection}`-invariant
summands each twist bundle has, and each summand's own domain-target
imbalance), a quantity computable ENTIRELY from `su(3)` representation
theory, with **no reference to `D_S6`'s specific geometry, `NOMIZU`, the
Killing-spinor equation, or any Dirac-operator computation whatsoever**,
beyond the SEPARATELY-established (by round59 for its own `(a,b)`, by
C139 for its own `Term2`) fact that each individual channel's connection
data happens to be nonzero -- a fact this round's own computation
INHERITS, not newly establishes (every numeric value appearing in `m+2*1`'s
own certificate -- `-sqrt(3)` and `-2*sqrt(3)/3` -- is imported unchanged
from round59 and C139 respectively; see Section 7's basis-independent
singular-value checks, which are EXACT matches, not merely "the same order
of magnitude").

**Is this pattern (kernel always exactly equals the graded floor) itself
guaranteed by a theorem, making even the individual "nonzero" facts
trivial too?** `[INFERRED]`, confidence MEDIUM, genuinely open: this round
does NOT establish that. C139's own Section 9 discussion explicitly noted
that, for a `1x1` scalar channel, `Term2 != 0` was NOT theoretically
guaranteed in advance -- it required actual computation of `NOMIZU`'s
specific geometric data, and COULD have been exactly zero (which would
have exceeded C139's own floor of `0`, giving kernel `1` instead of `0`).
So each INDIVIDUAL channel's non-vanishing is genuine, verified geometric
content (established by round59/C139, not automatic) -- what this round's
own graded-floor analysis shows is that, GIVEN those already-established
facts, the AGGREGATE kernel of any FURTHER construction built by
recombining them via a direct sum (as BOTH `T1` and `m+2*1` are) is fully
predictable from branching data alone, contributing NOTHING new about
`D_S6`'s geometry beyond what was already known.

## 10. Kill criterion evaluation (claim.md's own three branches),
    re-evaluated in light of Sections 9 and 9e

- **(a)** kernel `=1` for `m+2*1` -> would be NULL. **Does not fire on the
  LITERAL kernel value**: computed kernel `=0` (Section 6). **But per
  Section 9e, this literal non-fire is exactly what pure `su(3)` branching
  (the graded floor `=0` for `m+2*1`'s three square summands) predicts,
  independent of `D_S6`'s specific geometry** -- so while the branch does
  not literally fire, its own underlying INTENT (does the round establish
  that `D_S6` fails to discriminate, in a way attributable to shape/
  branching alone?) is realized, just not via the literal `kernel=1`
  wording claim.md anticipated.
- **(b)** the domain/target invariant-sector shape is not `(2,1)` as
  claim.md naively predicted -> report the actual shape and why the CG
  prediction failed, before interpreting any kernel value. **Fires, as
  reported (Section 5).** Section 9's `T1` comparison initially appeared to
  supply a valid alternative shape-matched test despite this -- but Section
  9e shows the resulting kernel VALUE is, like the shape mismatch itself,
  a branching/representation-theory artifact, not evidence of `D_S6`'s
  geometry. **Kill criterion (b)'s own underlying concern -- "do not treat
  a shape effect as if it were a clean discriminating result" -- fires
  more broadly and more decisively than its literal wording anticipated.**
- **(c)** undisclosed equivalence to `Sigma` despite the precheck ->
  **checked (Section 4), does not fire** (this remains correct and
  unaffected by Sections 9e/10's findings -- non-equivalence to `Sigma` and
  "the kernel is a branching artifact" are separate, non-contradictory
  facts: `m+2*1` genuinely is NOT equivalent to `Sigma` as an operator, it
  just doesn't need to be for its kernel to be predictable from branching
  data alone).

**Net effect, after both skeptic passes:** claim.md's own kill criterion
(b) fires, and its DEEPER concern -- that an apparent discrimination might
reduce to "a bare singlet-count/shape effect" -- is vindicated in a
STRONGER, more general form than claim.md's own literal wording anticipated
(a GRADED, per-summand branching effect, not merely an aggregate
singlet-count one). This round reports **NULL, QUALIFIED**: not because
the literal kernel value is `1` (it is `0`), but because the round's own
central finding (Section 9e) is that this construction's kernel VALUE
-- like its shape -- carries no information about `D_S6`'s geometry beyond
what pure `su(3)` representation theory, combined with ALREADY-ESTABLISHED
(not new) facts from round59 and C139, already determines. This is
`NULL` in claim.md's own intended SENSE ("`D_S6` does NOT discriminate
`Sigma`'s specific geometric content from this alternative, in any way
this test can detect") even though the literal numeral differs from the
`kernel=1` wording claim.md's kill criterion (a) anticipated. It is
**not** `PROMOTE` (Section 9e withdraws the only argument that supported
that, Section 8a/9d), and **not** `BLOCKED` (the construction, and a valid
comparison, were both completed and computed without obstruction --
the obstruction is interpretive, not constructive).

## 11. Kill Analysis (Anti-Overfitting Gate discipline)

**What this round kills:**
1. The specific, implicit hypothesis that "matching `Sigma`'s total
   `su(3)`-singlet count" is sufficient to reproduce round59's OWN
   `EVEN_IDX`-restricted `(2,1)` shape. **FALSE**, verified two ways
   (Section 5), and F7 (Section 2) shows this is not just false for
   `m+2*1` specifically but for ANY 2-singlet twist bundle whatsoever.
2. The SECOND DRAFT's own `PROMOTE` verdict (and, en route, the FIRST
   DRAFT's `BLOCKED_BY_INVALID_PREMISE` verdict). **Both FALSE**, per
   Sections 9/9e -- a valid, decisive, shape-matched COMPARISON does exist
   once the reference point is corrected from round59's restricted `(2,1)`
   to the methodologically consistent `T1` (`(3,3)`) (killing draft 1's
   verdict) -- but that comparison's OUTCOME (kernel `1` vs `0`) is itself
   fully explained by a graded rank-nullity floor computable from pure
   `su(3)` branching data, not by any dynamical fact about `D_S6` (killing
   draft 2's verdict).
3. **The implicit assumption, shared by claim.md, both of C139's skeptic
   passes, and this round's own first two drafts, that "kernel of the
   twisted Dirac operator, at matched shape" is a test capable of
   discriminating `Sigma`'s specific geometric content from an alternative
   at all.** Section 9e shows that, for every construction tested in this
   project's history (4/4), the kernel is fully determined by `su(3)`
   branching plus the prior, separately-established fact that individual
   channels don't vanish -- meaning this FAMILY of tests, not merely this
   one instance of it, may not be capable of showing what the "why Sigma,
   not m" research question needs. This is the round's most consequential
   finding and is flagged as a priority pearl-registry item (Section 15),
   not merely a footnote.

**What is NOT killed:**
- C139's own `kernel=0` result for `W'=m` -- untouched, independently
  re-confirmed as a Substrate-Gate regression check (Section 0 of the
  script).
- round59's own certified `(a,b,s)=(-1,-sqrt(3),4)`, `dim ker=1` --
  untouched, and independently re-confirmed here TWICE: once as `T0`
  (Section 9a), and shown to embed exactly inside `T1` (Section 9c).
- `N_gen=3`'s CONDITIONAL status -- unaffected (Section 13).
- The precheck's own equivalence-clearing conclusion -- re-confirmed
  (Section 4), with an honest downgrade of the re-verification's claimed
  independence (F8/F9).

**Relaxation Map** (one assumption changed relative to C139's own `W'=m`,
per the Minimal Relaxation Rule):

| Assumption relaxed | What changed | Result |
|---|---|---|
| Twist bundle has zero `su(3)` singlets (`W'=m`, C139) | Replaced with `W''=m(+)2*1`, matching `Sigma`'s own TWO singlets | Invariant-sector shape changes from `(1,1)` to `(3,3)` -- matching the CORRECT reference `T1` (Sigma self-twist, unrestricted), not round59's own restricted `(2,1)`; kernel changes from C139's `0` (shape `(1,1)`) to this round's `0` (shape `(3,3)`) -- but now genuinely comparable to `T1`'s `1` at the SAME shape |

## 12. FL Step 8a -- skeptic pass 1 (context-blind, independent agent),
    formal framing

Per claim.md's mandatory instruction for this high-stakes round, this pass
was run via an independent `Agent(skeptic, model=opus)` invocation given
ONLY `claim.md`, this `decision.md` (the FIRST-DRAFT version -- genuinely
context-blind, no session history), `c141_matched_singlet_twist.py`,
`results_c141.json`, and (as explicitly permitted, to check reuse
correctness) C139's own `decision.md` and `c139_precheck_m_plus_2singlets.py`.
No Bash tool was available to the agent in this run; its findings are
therefore `[DERIVED]`/`[CITED]` from the files, not independently executed
by the agent itself -- all findings below were independently verified by
THIS round via actual computation (Sections 2, 4, 7, 8, 9) before being
accepted.

### 12a. Skeptic pass 1 -- verdict and findings

**Skeptic's overall verdict: `FALSIFIED`** (of the first draft's
`BLOCKED_BY_INVALID_PREMISE` verdict and several supporting claims; NOT of
the underlying computed numbers, which the skeptic states are believed
correct).

| # | Skeptic finding | Severity | Response |
|---|---|---|---|
| F1 | round59's twist bundle, in the sense relevant to its certified `(2,1)`, is `EVEN_IDX` alone (dim 4, one singlet), not full `Sigma` (dim 8, two singlets) -- the "matched singlet count" design matched the wrong reference object | **CRITICAL** | **`[CONFIRMED-REAL]`, accepted in full.** Independently verified by reading round59's own script (Section 0 of this decision.md, quoted verbatim) and by Section 9's `T0` computation. Section 2 (1b) and Section 9 rewritten accordingly. |
| F2 | `NO_SHAPE_CONTROLLED_COMPARISON...` is false -- `m+2*1` has module type identical to full `Sigma`, so `(3,3)` is the full-Sigma-self-twist shape (already recorded in C139 Sec 3d); the like-for-like comparison was one API call away and was not run | **CRITICAL** | **`[CONFIRMED-REAL]`, accepted in full and RUN (Section 9, `T1`).** This is the central correction of this revision: `T1` kernel `=1` vs `m+2*1` kernel `=0`, verified two independent ways, robust across the family. |
| F3 | `D'' = D'_{Sigma(x)m} (+) A (+) A` by construction (block-diagonal connection => direct-sum Dirac) -- Section 7/8's decomposition is a construction triviality, not a discovery; the actual derivation is 2 lines, available before any computation | **CRITICAL** | **`[CONFIRMED-REAL]`, accepted in full, not minimized (Section 8).** The 2-line argument is credited explicitly. **Correction (2026-09-04, same session, after skeptic pass 2): Section 8a's original response to F3 -- arguing the RANK DIFFERENCE survived this concession -- was itself wrong. Section 9e (skeptic-pass-2-triggered) shows F3's own direct-sum observation, applied at the correct (per-summand) granularity, is EXACTLY what explains the kernel difference too. F3 was even more right than its own first response gave it credit for.** |
| F4 | The precheck's clearance criterion ("no intertwiner exists" => "non-redundant, decisive test") is the wrong gate for informativeness -- non-equivalence to `Sigma` does not imply the result is not a forced/trivial direct sum | **CRITICAL** | **`[CONFIRMED-REAL]`, accepted, and validated further by skeptic pass 2 (Section 9e): non-equivalence to `Sigma` is real (Section 4) but genuinely does NOT imply informativeness -- Section 9e shows the "informative" `T1`-vs-`m+2*1` comparison this round thought it had found (Section 9) is ITSELF a forced branching artifact, exactly the failure mode F4 warned about.** |
| F5 | Section 2's "singlets split asymmetrically" mechanism is imprecise; the general, correct formula is `domain-target = mult_W(3bar)-mult_W(3)` for ANY `W`, verified against `EVEN_IDX`, `m`, `m+2*1`, full `Sigma` | HIGH | **`[CONFIRMED-REAL]`, accepted, Section 2 (1b) rewritten** with the general formula, verified computationally (`f5_general_domain_minus_target_formula_holds_for_all_test_modules`). **This is the same formula Section 9e later applies PER SUMMAND to derive the graded floor -- F5's correction was load-bearing for the round's eventual real finding, not merely a cosmetic fix.** |
| F6 | Missing retroscan: `kernel >= mult_W(3bar)-mult_W(3)` unconditionally (rank-nullity) -- round59's own `kernel>=1` is partly free; `m+2*1`/`T1`'s `domain=target=3` makes the bound trivial on both sides, so their kernel DIFFERENCE is fully "real" | HIGH | **Partially accepted, then SUPERSEDED.** The AGGREGATE version of this bound (applied to the whole `(3,3)` shape) is correctly trivial, as stated. But this round's own SECOND draft used that aggregate triviality to conclude the kernel difference was "fully real" -- **skeptic pass 2 found the aggregate bound is the wrong granularity; the GRADED (per-summand) version of the identical rank-nullity argument is NOT trivial and exactly predicts the kernel difference (Section 9e).** F6's own literal claim (aggregate bound is trivial) stands; the CONCLUSION this round drew from it (Section 8a) does not. The two module-level check()s originally added for F6 were removed for a separate reason (self-audit gap, see F13's response and skeptic pass 2 finding "G") -- their content is superseded by Section 9e/10's graded analysis regardless. |
| F7 | The first draft's Section 11.4/pearl proposal (an internally even/odd-graded 2-singlet construction) provably CANNOT achieve `(2,1)` -- brute-force shows only `(1,0,1)` and `(0,1,2)` work, neither has `mult_1=2` | HIGH | **`[CONFIRMED-REAL]`, accepted, verified by brute-force search in-script (`f7_2_1_shape_requires_exactly_these_two_module_types`). The speculative Section 11.4 and its pearl-registry proposal are WITHDRAWN in full** (Section 15) -- superseded by the much stronger, actually-computed `T1` finding, which makes the speculative proposal moot as well as wrong. |
| F8 | Section 4's re-verification uses the SAME method and SAME connection object as the precheck's own check -- a reproducibility check, not independent-method verification; presented with stronger language than warranted | MEDIUM | **Accepted, language downgraded in Section 4** to state precisely what is and is not established by this check. |
| F9 | The precheck's own "dimension-counting" method hardcodes `achievable_dims={0,4,8}` from C139 Sec 3b rather than re-deriving it -- a tautology-adjacent check | MEDIUM | **Accepted as a valid observation about the PRECHECK file** (owned by C139, not modified per the read-only-reuse instruction); noted in Section 4 that this round's own conclusions rely only on the freshly-run intertwiner search, not this precheck sub-check. |
| F10 | `term2_single_nonzero_entry_matches_c139_own_c_exact` compares a basis-gauge-dependent matrix entry (C139's own decision.md documents this exact gauge freedom for 1-dim sectors); could be a phase artifact | MEDIUM | **Accepted, addressed with a basis-independent restatement (Section 7/6c of the script): rank + singular value** of `Term2` (`=1`, sole singular value `=|C139.c_exact|` exactly), invariant under orthonormal basis choice, verified alongside the original entrywise check (kept as a stronger, but explicitly basis-dependent, supporting observation). |
| F11 | The "exactly permutation-diagonal" pattern is partly a basis artifact of which orthonormal basis `gram_schmidt` happens to return; kernel/rank conclusions are unaffected | LOW-MED | **Accepted, addressed the same way as F10** (Section 7/6c): `Term1` rank `=2`, singular values both `=sqrt(3)` exactly, basis-independent. |
| F12 | `preregistered_prediction_computed_before_any_invariant_sector_numerics`'s check NAME claims "before" (temporal ordering), but the boolean condition only tests arithmetic agreement -- a check cannot establish provenance | LOW-MED | **Accepted.** The temporal-ordering claim is supported by the script's own linear execution structure (Section 1 runs before Section 4/5's nullspace computation), not by this check's boolean condition; the check's actual content (arithmetic agreement between the hand derivation and the code's own formula) is accurately described in its `detail` string. |
| F13 | AST self-audit gap: a `True if <cond> else bool(...)` conditional expression is an `ast.IfExp`, not an `ast.Constant`, so a literal `True` branch is not caught by the self-audit even though the audit claims "no `check()` call is passed a literal constant" | LOW | **Fixed, not merely disclosed.** The dead-code guard removed entirely (script Section 6); replaced with an explicit, always-live `block2_exact_is_nonempty_before_eigenvalue_check` precondition check plus the original eigenvalue check with no conditional literal branch. |
| F14 | Section 8/9's (first-draft) 13-angle robustness sweep for `m+2*1` is largely inherited from C73b's/C139's own already-certified sweeps, not new | LOW | **Accepted as a fair characterization of the FIRST DRAFT's own Section 9 (angular sweep for `m+2*1`).** Noted that Section 9 of THIS revision's own `T1` sweep (13 angles, `kernel_dim` constant `=1`) IS a genuinely new computation, run here for the first time. |

### 12b. Response to the overall `FALSIFIED` verdict

**Accepted in full, not contested, not minimized.** The skeptic's central
findings (F1-F4) identified a genuine, decisive gap in the first draft's
own reasoning: concluding `BLOCKED` from a shape mismatch against the
WRONG reference point, without checking whether a methodologically
CORRECT reference point existed. Rather than merely documenting the
critique, this round RAN the missing computation (`T1`, Section 9) in
response, which **reversed the round's own verdict from `BLOCKED` to a
provisional `PROMOTE`** -- at the time, the strongest possible outcome for
a Step 8a response: not a defensive rebuttal, but a decisive, verified,
positive result found BECAUSE of the skeptic's critique.

**Update (same session, after skeptic pass 2, Section 13): that provisional
`PROMOTE` was itself found to be wrong**, by a second, independent,
differently-worded skeptic pass applying the SAME kind of rigor (per-
summand rank-nullity, Section 9e) that pass 1's own F6 finding had already
supplied half the ingredients for, but which pass 1 itself did not apply at
the decisive (graded, not aggregate) granularity. This is not a failure of
pass 1's own findings (F1-F14 all stand, independently verified, Section
12a) -- it reflects that ONE context-blind pass, however thorough, is not
guaranteed to catch every issue, which is exactly why claim.md mandated a
SECOND, differently-worded pass for a round at this stake level, and why
that second pass was run rather than skipped once pass 1 returned a
seemingly complete, positive resolution.

Agent id (this session's record): see orchestrating session's own agent
log for the exact id; findings independently re-verified by this round via
direct computation before acceptance, per house rule #6 and the
Audit-Verification-Gate protocol (agent `[VERIFIED]` = this round's own
`[INFERRED]` until independently re-checked -- done, Sections 2/4/7/8/9,
and again for pass 2's findings, Section 13/9e).

## 13. FL Step 8a -- skeptic pass 2, differently-worded (informal register)

Per claim.md's explicit instruction ("run TWO differently-worded passes
regardless of the first pass's verdict... unless the first pass returns a
clean, unqualified confirmation with zero findings" -- pass 1 returned
`FALSIFIED` with 14 findings, so a second pass was mandatory regardless),
a second independent `Agent(skeptic, model=opus)` invocation was run with
a differently-phrased, informal-register prompt (colloquial framing, no
"falsification agent" language), given ONLY `claim.md`, this decision.md
(the SECOND-DRAFT version -- i.e. including Sections 0-9d/12 as they then
read, the provisional `PROMOTE` verdict, and pass 1's own full response
matrix), `c141_matched_singlet_twist.py`, `results_c141.json`, and (as
explicitly permitted) C139's own `decision.md` and round59's own
`round59_route_a_independent.py`. No Bash tool was available to the agent;
findings are `[DERIVED]`/`[CITED]` from the files, independently
re-verified by THIS round via direct computation (Section 9e, and the
standalone verification script confirming the graded-floor prediction
against all four cases exactly) before acceptance.

### 13a. Skeptic pass 2 -- verdict and findings

**Skeptic's overall verdict: `FALSIFIED`** (of the second draft's
`PROMOTE` verdict and its Section 8a argument specifically; the underlying
computed NUMBERS are again stated as correct, and several of pass 1's own
fixes are spot-checked and confirmed genuine).

| # | Skeptic finding | Severity | Response |
|---|---|---|---|
| A | Section 8a applies rank-nullity to the AGGREGATE `(3,3)` shape, but both `T1` and `m+2*1` are direct sums over MULTIPLE `{connection}`-invariant summands (conceded elsewhere in the same document) -- rank-nullity must be applied PER SUMMAND, giving a GRADED floor that is NOT trivial and exactly predicts the observed kernel (`T1`: `(2,1)`-summand floor `1` + `(1,2)`-summand floor `0` `=1`; `m+2*1`: three `(1,1)`-summand floors, `0` each, total `0`) | **CRITICAL** | **`[CONFIRMED-REAL]`, independently re-verified by direct computation (not merely accepted), Section 9e / script Section 10, `graded_rank_nullity_floor_exactly_predicts_observed_kernel_in_all_4_cases`. This is the central correction of this revision.** Section 8a is left in place, marked withdrawn, per the Hindsight Distortion Gap Heuristic. |
| B | `T1`'s kernel vector is literally round59's own certified kernel vector (`{a,b}=(-1,-sqrt(3))`, embedded via the subspace-embedding Section 9c already established) -- `T1 kernel=1` **is** round59's `kernel=1`, re-derived, not new | **CRITICAL** | **`[CONFIRMED-REAL]`, accepted.** Consistent with, and a sharper restatement of, Finding A -- incorporated into Section 9e's account of why `T1`'s floor is exactly `1` (from its `Sigma_even` summand, i.e. `T0`/round59's own sub-block). |
| C | The `-sqrt(3)` Killing-eigenvalue value is analytically derivable in 3 lines from round59's own calibration equation (already certified PASS) -- claim.md's kill criterion (a) (`kernel=1`) had no reachable branch given the prior certificates, an FL Step-4a floor defect | **HIGH** | **Accepted with a precision.** The SPECIFIC NUMERIC VALUES (`-sqrt(3)`, `-2sqrt(3)/3`) are genuine geometric facts (Killing-spinor eigenvalue of `S6`, `NOMIZU`'s specific realization on `m`) established by round59/C139's own prior, real computation -- not automatic from `su(3)` representation theory alone (Section 9e's own `[INFERRED]` caveat already notes this: C139's own `Term2` could, in principle, have been exactly zero). What Finding C adds, correctly, is that GIVEN those prior facts as already-established, this round's OWN test had no reachable path to a genuinely informative outcome -- an FL Floor-Ceiling-style defect this round did not check for at design time (Section 15 flags a `ceiling.md`-style gate as future methodology). |
| D | The `T0 subset T1` embedding (Section 9c) is trivially guaranteed by linear algebra (`V subseteq W` sub-representation `implies` `V^G subseteq W^G`) -- the check run confirms nothing about the operator, and the informative check (do `T0` and `T1` share the SAME kernel vector) was not run | **HIGH** | **`[CONFIRMED-REAL]`, accepted.** Section 9c's language is corrected below to state this precisely; the informative version (same kernel vector) is confirmed as part of Finding B's resolution. |
| E | The precheck's non-redundancy argument (`Sigma` splits `{4,4}` under `{NAB_i}`, `m+2*1` splits `{6,1,1}`) is the SAME fact that produces the different graded floors -- invoked to argue the test is meaningful, then not applied when interpreting the result | **HIGH** | **Accepted.** A precise, correct observation connecting Section 4's equivalence-check machinery to Section 9e's graded-floor argument -- both trace to the same underlying fact (different `{connection}`-invariant summand structure). |
| F | `[VERIFIED-tool]` tag attached to "the rank difference is not forced" (Section 8a) -- no tool tests "not forced"; that is an argument, and (per Finding A) a wrong one | MEDIUM | **Accepted.** The evidence-tier section (below) is rewritten to remove this mismarking; Section 8a's claim is now explicitly marked withdrawn, not `[VERIFIED-tool]`. |
| G | AST self-audit still has a live gap: `check(name, (CLAIM_MD_NAIVE_DOMAIN - CLAIM_MD_NAIVE_TARGET) == 1, ...)` compares module-level hardcoded literals, unfailable by construction, evading the `ast.Constant`-only detection via name binding | MEDIUM | **Fixed, not merely disclosed.** The two F6-motivated `check()` calls using this pattern were removed from the script (replaced with plain informational `print()`s, superseded by Section 10's real, non-hardcoded `graded_floor()` computation) rather than defended or re-justified. |
| H | F5's "4 test modules" contains a duplicate (`"m+2*1"` and `"full Sigma self-twist"` are the identical dict) -- 3 distinct modules, not 4 | MEDIUM | **Fixed.** Script's `F5_TEST_MODULES` dict corrected to list 3 distinct abstract module types, with an explanatory comment on why `m+2*1` and full `Sigma` share one (that IS the whole point of the precheck's non-redundancy analysis: same `su(3)`-module type, different `{NAB_i}`-level action). |
| I | Kill criterion (b) fired, the reference point was changed post-hoc after seeing the mismatch, and the verdict flipped to `PROMOTE` -- the Anti-Overfitting Gate (labeled "Kill Analysis" in Section 11) was never actually run (AOG-1 pre-registration fails by construction, since `T1` was found only after the `BLOCKED` verdict) | MEDIUM | **Accepted as an accurate process observation.** Given the verdict has now moved to `NULL_QUALIFIED` (this section), the specific AOG concern about a premature `PROMOTE` is moot for the FINAL verdict -- but the underlying methodological point (a post-hoc reference-point change should be flagged, not silently smoothed into a clean-looking positive result) is a valid, general lesson, folded into the pearl-registry proposal (Section 15). |
| J | `T1`'s "new" `(1,2)` sub-block may ALSO recycle a prior C73 computation (attempt (b), "alternate bigrading pairing"), not merely be assembled from scratch -- worth checking, not yet checked | LOW-MED `[INFERRED]` | **Not resolved in this round** (would require reading C73's own decision.md in detail, out of scope given the verdict has already moved to `NULL_QUALIFIED` on other, decisive grounds). Flagged honestly as an open question, not investigated further, since it would not change the round's verdict either way. |
| K | The verdict block (as it read in the second draft) asserts the difference is "NOT forced by shape alone," while Section 14's caveats never concede the graded-shape point -- caveats guard a different flank than the verdict's actual weak point | LOW | **Moot after this revision** -- the verdict block and Section 14 (below) are both rewritten to reflect the `NULL_QUALIFIED` conclusion; there is no longer a mismatch to guard against, since the graded-floor finding is now the verdict's own central content, not a caveat. |

### 13b. Response to the overall `FALSIFIED` verdict

**Accepted in full.** Independently re-verified (script Section 10,
standalone Python check reproducing the same 4/4 match) before acceptance,
per house rule #6 -- not merely taken on the skeptic's authority. Per this
project's FL Step 8a Response Matrix, this is the RARE case where the
skeptic's finding, followed to its logical conclusion, changes the
round's own verdict a SECOND time in the same session -- from `BLOCKED`
(draft 1) to `PROMOTE` (draft 2) to `NULL, QUALIFIED` (this, final,
draft). Each transition was driven by an independent, context-blind check
finding a genuine flaw in the PRIOR draft's own reasoning, not by
this round second-guessing itself without new information. The skeptic's
own proposed "fallback" framing (a falsifiable, generalizable statement:
*"the invariant-sector kernel equals the graded rank-nullity floor for
every twist bundle tested so far; the first twist bundle whose kernel
differs from its own floor would be the first genuinely dynamical result
in this line of work"*) is adopted, with attribution, as this round's own
final positive contribution (Section 9e, Section 15's pearl proposal).

## 14. What this round does NOT show

- Does **NOT**, regardless of outcome, change `N_gen=3`'s CONDITIONAL
  status, `lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed =
  False`, or `safe_for_runtime = False`.
- Does **NOT** reopen C123-C140's verdicts.
- Does **NOT** show `D_S6`'s kernel structure discriminates `Sigma`'s
  specific geometric content from `m+2*1` (or from `T1`'s own self-twist)
  in any dynamically meaningful sense -- Section 9e shows the observed
  kernel difference is fully predictable from `su(3)` branching data
  alone, given only the already-established (round59/C139) fact that
  individual channels are nonzero. **This is the opposite of what the
  round's own second draft claimed**, and is the correction this final
  version makes.
- Does **NOT** establish, and actively argues against, `T1`-vs-`m+2*1`
  being read as "the decisive test both of C139's skeptic passes wanted" --
  it IS a validly computed, shape-matched comparison (Section 9 stands),
  but its OUTCOME carries no more dynamical information than the `su(3)`
  branching data that predicts it exactly.
- Does **NOT** establish that the pattern "kernel always equals its graded
  floor" is a THEOREM (true by necessity for any twist bundle) as opposed
  to an EMPIRICAL regularity confirmed in the 4 cases tested so far --
  genuinely open (Section 9e's own `[INFERRED]` marker), and named
  explicitly as the concrete, falsifiable next test (Section 15).
- Does **NOT** identify the specific physical justification for `Sigma`
  over `m+2*1`, or advance the "why Sigma, not m" question (`OB14`) in the
  POSITIVE direction either draft 1 or draft 2 believed it had -- if
  anything, this round's real finding suggests the "kernel of the twisted
  Dirac operator" family of tests, AS A WHOLE, may not be capable of
  answering that question, which is a more consequential (if more
  deflationary) contribution to `OB14` than either provisional verdict was.
- Does **NOT** retroactively invalidate round59's or C139's own computed
  kernel VALUES (both remain correct, independently re-confirmed here) --
  it questions the INTERPRETIVE weight that was placed on those values as
  evidence of `D_S6`'s dynamics, a question this round raises but does not
  resolve for those PRIOR rounds' own registry entries (flagged, not acted
  on, per Section 15).
- Does **NOT** fully close `OPEN_BLOCKERS.md` OB14.
- Does **NOT** solicit Tom Lawrence's Part 5.

## 15. Registry actions -- NOT performed by this round, proposed only

This round does not edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
`null_results/INDEX.md`, `pearl_registry/INDEX.md`, `CLAIM_LEDGER.yaml`,
or `.claude/memory/activeContext.md`. Proposed exact wording:

**`CLAIM_LEDGER.yaml`** -- new entry (does NOT modify
`C139_ALTERNATE_TWIST_M_KERNEL_ZERO`, `C2_ROUND59_KERNEL_DIM1`, or
`C4_NGEN3_HEADLINE`):

```yaml
  - id: C141_KERNEL_IS_GRADED_BRANCHING_FLOOR_NOT_DYNAMICS
    statement: "Testing whether D_S6 discriminates Sigma from a twist bundle W''=m(+)2*1 (dim 8, module type 3+3bar+1+1, matching Sigma's own two-singlet COUNT, C139-precheck-cleared decoupled-extra-singlets connection) -- NULL, QUALIFIED (deflationary). claim.md's own naive prediction that matched singlet COUNT gives Sigma's own restricted shape (2,1) is FALSE (verified two ways: domain=target=3). Two SUCCESSIVE context-blind FL Step 8a skeptic passes progressively corrected this round's own verdict. Pass 1 found the apples-to-apples reference point is NOT round59's own EVEN_IDX-restricted (2,1) certificate but Sigma SELF-TWISTED with the SAME unrestricted-second-factor convention this round already uses for m(+)2*1 ('T1', computed for the first time here): shape (3,3), matching m(+)2*1 exactly, kernel=1, robust across the whole 13-angle admissible family, containing round59's own certified sector as an exact subspace. This initially looked like a genuine shape-controlled discrimination (kernel 1 vs 0). Pass 2 found this conclusion was ALSO wrong: both T1 and m+2*1 are direct sums over their twist bundle's {connection}-invariant summands; applying rank-nullity PER SUMMAND (not to the aggregate (3,3) shape) gives a GRADED floor computable from PURE su(3) branching data alone (no Dirac operator, no NOMIZU, no connection geometry beyond knowing which summands exist) -- and this floor EXACTLY equals the observed kernel in ALL FOUR twist-bundle constructions ever computed in this project's history: round59/T0 (floor=1, observed=1), C139/m (floor=0, observed=0), C141/m+2*1 (floor=0, observed=0), T1/Sigma-self-twist (floor=1, observed=1). Independently re-verified by direct computation (script Section 10, graded_floor() function), not merely accepted from the skeptic. This means the kernel difference is fully explained by pure representation theory, GIVEN ONLY the already-established (by round59/C139, not new to this round) fact that individual connection channels are nonzero -- this round's own Dirac-operator computation contributes no new geometric/dynamical fact about D_S6 beyond recombining already-known values (round59's own Killing eigenvalue -sqrt(3), C139's own Term2 value -2*sqrt(3)/3, both re-verified as EXACT matches via basis-independent singular-value checks, not approximate). Equivalence to Sigma re-verified fresh (intertwiner nullspace=0). A speculative alternative construction proposed and later withdrawn (an internally even/odd-graded 2-singlet twist bundle) was shown, by exhaustive brute-force search, to be PROVABLY INCAPABLE of achieving round59's own (2,1) shape regardless. GENUINELY OPEN, flagged not resolved: whether 'kernel always equals its graded floor' is a theorem or an empirical regularity holding only in the 4 cases tested so far -- the first twist bundle whose kernel EXCEEDS its own graded floor would be the first genuinely dynamical result in this entire line of work."
    truth_status: SUPPORTED
    test_outcome: NULL
    execution_status: READY
    evidence_status: INTERNALLY_CERTIFIED
    lifecycle_status: ACTIVE
    evidence_file: "tom_s3_spinor_toy/experiments/20260904-c141-matched-singlet-count-twist-m-plus-2singlets/decision.md"
    depends_on: [C139_ALTERNATE_TWIST_M_KERNEL_ZERO, C2_ROUND59_KERNEL_DIM1]
    supersedes: "no prior claim -- first attempt at the matched-singlet-count follow-up both of C139's skeptic passes recommended; two successive context-blind skeptic passes each found and corrected a flaw in this round's own prior verdict (BLOCKED -> PROMOTE -> NULL_QUALIFIED), the second correction being the round's actual, final finding"
    does_not_imply:
      - "that N_gen=3, C2_ROUND59_KERNEL_DIM1, or C139_ALTERNATE_TWIST_M_KERNEL_ZERO is falsified -- all three are untouched as COMPUTED FACTS; round59's own kernel=1 is independently re-confirmed twice here (T0, and as an exact subspace of T1). This entry DOES flag, without acting on it, that the INTERPRETIVE weight placed on those prior results as evidence of D_S6's dynamics (as opposed to branching arithmetic) may need re-examination -- see the proposed pearl-registry row for the specific, falsifiable open question"
      - "that D_S6's kernel structure can NEVER discriminate genuine geometric content from any twist bundle -- only that, in the 4 cases tested so far, it has not needed to (each result matches its own graded floor); a future twist bundle whose kernel EXCEEDS its graded floor would be a genuine counterexample and the first real positive result in this line"
      - "that the graded-floor equality is a proven theorem -- it is an empirical regularity, confirmed 4/4, not derived from a general argument that it must always hold"
      - "what the specific physical justification for choosing Sigma over m+2*1 is"
      - "any change to N_gen=3's CONDITIONAL status"
```

**`pearl_registry/INDEX.md`** -- new row (a genuinely new, falsifiable,
actionable insight, distinct from row 89's own closure by C139, and
distinct in kind from an ordinary result-pearl -- this one questions a
whole FAMILY of prior tests' interpretive weight, not just this round's
own construction):

```
| 2026-09-04 | C141 (this round, post-skeptic-pass-2 revision) | For EVERY twist-bundle-kernel computation in this project's history (round59/T0, C139, C141, T1 -- 4/4), the observed invariant-sector kernel EXACTLY equals a graded rank-nullity floor computable from PURE su(3) branching data alone (sum over the twist bundle's {connection}-invariant summands of max(0, mult_summand(3bar)-mult_summand(3))), given only the separately-established fact that individual channels don't vanish. No case tested so far shows a kernel EXCEEDING this floor. This means the "kernel of the twisted Dirac operator" family of tests, as practiced in this project through round59/C73/C73b/C139/C141, may not be capable of discriminating Sigma's specific geometric content from an alternative in the way the "why Sigma, not m" research program (OB14) has assumed -- the aggregate outcome may be a branching-theory tautology dressed as a dynamical test, in every instance examined | The first twist bundle (of any shape, any summand structure) whose OBSERVED kernel EXCEEDS its OWN graded rank-nullity floor (computed via the same trivial_mult()-based method C141's Section 10 uses, entirely before running any Dirac-operator computation) would be the first genuinely dynamical, non-branching-forced result in this entire research line -- falsifiable and cheap to check for any future candidate BEFORE building it (compute the floor first; if the floor already equals the hoped-for kernel, the test cannot be informative, an FL Floor-Ceiling-style pre-check this project's own methodology did not previously have for this specific test family) | 9 | Any future round proposing a twist-bundle kernel computation as evidence for or against Sigma's geometric preference; OR a retrospective audit of round59/C139/C141's own registry entries asking whether their INTERPRETIVE claims (not their computed values) should be qualified in light of this finding | 2026-10-15 | pending |
```

**`PARENT_ACTION_GATE.md`** -- one-line addition (suggested wording):
*"the both-skeptic-recommended matched-singlet-count follow-up to C139
(m(+)2*1) is now built (C141, post-skeptic-pass-2 revision): the round
went through two provisional verdicts (BLOCKED, then PROMOTE) before a
second context-blind skeptic pass found the decisive fact -- the kernel
difference between Sigma self-twisted (unrestricted, shape (3,3),
kernel=1) and m(+)2*1 (same shape, kernel=0) is FULLY explained by pure
su(3) branching data (a graded rank-nullity floor), not by D_S6's
geometry. Verified 4/4 across every twist-bundle kernel this project has
ever computed. The 'why Sigma, not m' question (OB14) remains open, and
this result raises a more consequential, if less comfortable, possibility:
this whole FAMILY of kernel-based tests may not be capable of answering it
at all. Flagged as priority pearl-registry item, not acted on further by
this round."*

**`OPEN_BLOCKERS.md`** -- proposed amendment to OB14 (append, do not
replace): *"C141 (2026-09-04, post-skeptic-pass-2 revision) found that the
invariant-sector kernel of every twisted-Dirac-operator construction
tested in this project's history (round59, C139, C141, and a newly
computed 'Sigma self-twisted unrestricted' comparison) exactly equals a
graded rank-nullity floor computable from PURE su(3) branching data, given
only the already-established fact that individual connection channels are
nonzero. This means the 'kernel of D_S6' test family, as practiced so far,
may not be able to discriminate Sigma's specific geometric content from an
alternative -- a more fundamental obstacle to 'why Sigma, not m' than any
single twist-bundle result. The falsifiable escape route (a twist bundle
whose kernel EXCEEDS its own graded floor) is named in pearl_registry
(this date) as the concrete next test."*

**`null_results/INDEX.md`** -- arguably applicable given the round's real
finding is deflationary (the intended test does not discriminate dynamics)
even though the literal verdict tag used elsewhere in this document is
`NULL_QUALIFIED` rather than a REJECT of a specific pre-registered claim;
left to the orchestrating session's judgment whether this warrants a
`null_results/INDEX.md` entry in addition to the `CLAIM_LEDGER.yaml` entry
above -- if added, proposed one-line summary: *"C141 (2026-09-04): kernel
of twisted D_S6, at any tested shape/twist-bundle combination so far, is
fully predicted by su(3) branching (graded rank-nullity floor) -- the
'kernel discriminates Sigma's geometry' hypothesis implicit in this
research line is NOT supported by any of the 4 cases examined; see
CLAIM_LEDGER.yaml C141_KERNEL_IS_GRADED_BRANCHING_FLOOR_NOT_DYNAMICS."*

## 16. Verification

- `c141_matched_singlet_twist.py` -- **50 distinct boolean check names from
  49 call sites, 49/50 PASS, 1 intentional/informative FAIL**
  (`shape_matches_claim_md_naive_2_1_expectation`). AST self-audit
  confirms no `check()` call is passed a literal constant. Two rounds of
  self-audit-adjacent fixes were required (not merely disclosed): the
  original `True if <shape==0> else bool(...)` dead-code branch (skeptic
  pass 1 finding F13) was removed; and two later `check()`s comparing only
  module-level hardcoded literals (skeptic pass 2 finding "G", evading the
  `ast.Constant`-only detection via name binding) were removed in favor of
  plain informational output, superseded by Section 10's real,
  non-hardcoded `graded_floor()` computation.
- Substrate-Gate regression (Section 0 of the script): C139's own module,
  freshly reloaded, shows 30/30 of ITS OWN checks passing and its own
  headline `kernel=0` unchanged.
- Every load-bearing number verified from at least two independent angles:
  domain/target invariant-sector dims (by-hand CG, cross-validated against
  round59's certified values, numeric SVD, exact sympy); the `(3,3)` block's
  kernel/rank (numeric SVD vs exact sympy); `T1`'s kernel (numeric SVD vs
  exact sympy, plus a 13-angle robustness sweep); `T0`'s reproduction of
  round59 (both shape and kernel, exact match); the subspace-embedding of
  `T0` inside `T1` (least-squares projection residual, two separate checks
  for domain and target); the mechanistic decomposition's `Term2` value
  (both an exact symbolic match to `C139.c_exact` AND a basis-independent
  singular-value match to `|C139.c_exact|`); the general `domain-target`
  formula (checked against 3 distinct test modules, corrected from an
  earlier miscounted "4" per skeptic pass 2 finding H); **the graded
  rank-nullity floor's exact match to all 4 observed kernels (Section 10,
  independently re-verified by a standalone script in addition to the
  registered one, matching exactly).**
- Repo-wide test suite not run (no shared code touched; only new files
  inside this experiment's own directory; C139/precheck/R59/C73/C73B files
  read via `load_module` but not modified).

---

## Evidence tier of the central conclusion

**Central conclusion (final, after two rounds of skeptic-triggered
correction):** the invariant-sector kernel of EVERY twisted-`D_S6`
construction computed in this project's history -- round59's own
`EVEN_IDX`-restricted certificate, C139's `m`, this round's `m(+)2*1`, and
`Sigma` self-twisted without restriction (`T1`, computed here for the
first time) -- exactly equals a **graded rank-nullity floor** computable
from PURE `su(3)` branching data alone (Section 9e/10), given only the
separately-established (by round59/C139, not new to this round) fact that
each individual connection channel is nonzero. **This means the kernel
"discrimination" this round's own second draft reported (`T1=1` vs
`m+2*1=0`, same shape `(3,3)`) carries no dynamical/geometric information
about `D_S6` beyond what representation theory already predicts** -- it
is NOT evidence that `D_S6` prefers `Sigma`'s specific geometric content
over `m(+)2*1`'s.

**Tier: `[VERIFIED-tool]`, confidence HIGH** for all computations
themselves -- 49/50 machine checks pass (the one "failure" being the
intentional, correctly-detected shape-mismatch-to-claim.md's-naive-
prediction finding), every headline number cross-verified via at least two
independent routes, `T0` confirming the machinery against round59's
certified values before `T1` is trusted, `T1`'s robustness independently
swept across the whole admissible family, and the graded-floor prediction
independently re-verified (both in the registered script and via a
separate standalone check) against all 4 historical cases.

**Tier of "the kernel difference is genuine dynamical content, not merely
recycled facts" -- the SECOND draft's own central claim:
`[FALSIFIED]`, confidence HIGH, by skeptic pass 2, independently
re-verified by direct computation (Section 9e/10) before acceptance.**
Both `T1` and `m+2*1` are direct sums over `{connection}`-invariant
summands; rank-nullity applied per summand (not merely in aggregate, which
was the second draft's own error) gives a floor that exactly matches the
observed kernel in all 4 tested cases -- meaning the difference IS forced,
by shape, at the correct (graded) level of granularity.

**Tier of "the graded-floor equality is a general theorem, not an
accident of the 4 cases checked so far": `[INFERRED]`, confidence LOW-
MEDIUM** -- genuinely open, named explicitly (Section 9e, Section 15) as
the concrete, falsifiable, cheap-to-check-in-advance next test: does ANY
twist bundle's kernel ever exceed its own graded floor?

**Tier of "this whole family of tests cannot discriminate `Sigma`'s
geometry from any alternative, in principle": `[INFERRED]`, confidence
LOW** -- this round shows it hasn't, in 4/4 cases; it does NOT show it
cannot, in principle, for some other construction. Stated as a hypothesis
worth testing (Section 15's pearl proposal), not as an established fact.

**Marker on the whole round: `NULL_QUALIFIED` (deflationary).** This
decision.md carries THREE successive verdicts, each overturned by an
independent, context-blind, computationally-re-verified check, in the
same session: `BLOCKED` (draft 1) -> `PROMOTE` (draft 2, after skeptic
pass 1) -> `NULL_QUALIFIED` (this, final, draft, after skeptic pass 2).
Each transition is recorded in full, not smoothed over (Sections 8a, 9d,
12, 13). The round's real, final contribution is not the shape-matched
comparison it set out to build, but the discovery that this comparison --
and, by the same argument, every twisted-`D_S6` kernel computation in this
project's history -- may be a representation-theory tautology rather than
a dynamical test, a finding with implications beyond this single round,
flagged as a priority pearl-registry item for the orchestrating session's
attention.
