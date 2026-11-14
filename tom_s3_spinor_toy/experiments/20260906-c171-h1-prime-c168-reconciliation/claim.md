# C171 Claim — H1'=zeta_p^{-1} vs C168's H_1=zeta_p reconciliation

**Date:** 2026-09-06
**FL tier:** [x] Micro-scoped, run under Standard artifact discipline (narrow
  reconciliation named explicitly by C170's own Relaxation Map — not a new
  multi-day investigation)
**Question type:** [x] descriptive (does substituting one matrix for another
  in an already-built computation reproduce the same classification?) —
  explicitly NOT causal/predictive; no new physics is being claimed either way.

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: does `H_t (x) tau` with `H_1' = zeta_p^{-1}` (C170's own
   derived holonomy for its `t=1` candidate `psi_1(g)=g^{-1}.psi_0`) give the
   SAME invariant-subspace dimension and channel-participation classification
   as C168's `H_1 = zeta_p` computation?
2. `decision.md` grep (`zeta_p_inverse`, `H1'`, `H_1'`, "reconciliation"):
   [x] done, 0 hits for a prior *reconciliation attempt* — hits found only in
   C168/C170's own files (the source material this round reconciles), not a
   duplicate of this specific check. Reviewed at: `experiments/20260906-c168*/`,
   `experiments/20260906-c170*/`.
3. `round*_claim.md` + scripts grep: [x] done, 0 hits — no prior round ever
   substituted `zeta_p^{-1}` into C168's own `invariant_subspace_report`
   machinery.
4. `null_results/` + `parked/` grep: [x] done, 0 hits for this specific
   substitution.
5. `git log -S`/`-G` pickaxe: not run — both source files (C168, C170) are
   same-day, uncommitted-adjacent siblings in this session; the substitution
   itself has not been attempted per the file-grep checks above, which is the
   operative fact for this gate.
6. Primary source re-read: C168's `decision.md` §T4–T8 and
   `c168_triality_correlation_check.py` re-read in full above (this session);
   C170's `decision.md` §4–5 and `c170_explicit_ker_ds3.py` Step 5 re-read in
   full above (this session) — both fresh, not from memory.
7. **Status:** [x] NEW

---

## AI-Hypothesis Pre-Gate — Novelty Check (Step -3, abbreviated per
   delegation instructions — this is a narrow, well-motivated confirmatory
   check named explicitly by C170's own Relaxation Map, not a novel
   construction requiring literature search)

This is not a new hypothesis about the world — it is a consistency check
between two computations already inside this project (C168, C170), whose
outcome is already predicted by C168's own T8 character-theory theorem
(`V (x) W ≅ dim(V)` copies of `W` for `W` = regular rep of a finite group,
for ANY `V`). No external literature claim is being made; Source Trace
(Step -4) is inherited from C168's own already-cited Baez/triality source
(pearl_registry row 33) and C167/C170's own Agricola citations — not
re-verified again here since no new external fact is introduced.

---

## Estimand

**Population:** the single linear-algebra object `D_1' := H_1' (x) tau`
acting on `C^2 (x) C^3`, where `H_1' := zeta_p^{-1}` (`p=3`), `tau` = C168's
own certified 3x3 cyclic permutation matrix on `{v,s,c}`.
**Intervention:** substitute `H_1'=zeta_p^{-1}` in place of C168's
`H_1=zeta_p` inside C168's own `invariant_subspace_report(H, tau_m, label)`
function (reused verbatim via `importlib`, not reimplemented).
**Comparator:** C168's own `t=1` result (`H_1=zeta_p`, dim=2,
`NON-EXCLUSIVE-ALL-THREE-PARTICIPATE`).
**Endpoint:** `dim_invariant_eigenvalue_1_subspace` and `classification`
string returned by the (reused, unmodified) function.
**Summary measure:** exact equality of (dimension, classification) between
the two sectors, computed symbolically (sympy), not floating-point.
**MCID:** not applicable — this is an exact/discrete equality check
(dimension is an integer, classification is a categorical label), not a
continuous statistic with a practical-significance threshold.

---

## Claim

Substituting `H_1' = zeta_p^{-1}` for C168's `H_1 = zeta_p` in C168's own
`H_t (x) tau` invariant-subspace computation reproduces the IDENTICAL
classification C168 found for `H_1 = zeta_p`: dimension-2 invariant subspace,
all three channels `{v,s,c}` participating (`NON-EXCLUSIVE-ALL-THREE-
PARTICIPATE`).

Supporting sub-claim:
1. `zeta_p^{-1}` is itself an order-exactly-3 element of `SU(2)` (re-verified,
   not assumed) — so C168's own T8 theorem (forced-by-tau-alone, for ANY rep
   `V` of `ℤ₃`) already predicts this MUST hold; this check confirms the
   prediction is correctly realized for this SPECIFIC substitution, not
   merely asserted from the abstract theorem.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Dimension mismatch | `dim_invariant(H_1' (x) tau) != dim_invariant(H_1 (x) tau)` (i.e. != 2) |
| Classification mismatch | `classification(H_1' sector) != "NON-EXCLUSIVE-ALL-THREE-PARTICIPATE"` |
| `H_1'` not order-3 | `(H_1')^3 != I` or `H_1' == I` (would mean the substitution itself is malformed, not a physics finding) |

If FAIL (either dimension or classification mismatch, with `H_1'` confirmed
order-3) → kills the unconditional form of C168's own T8 theorem as applied
to this specific pair of matrices — a SERIOUS, unexpected finding requiring
careful re-examination of either C168's or C170's own conventions (elementary
group/representation theory says this should not be possible for any
order-3 element, so a failure here would point to a coding bug in one of the
two reused functions, not a new physics discovery). Verdict:
`RECONCILIATION-FAILED`.

If PASS (dimension and classification match, `H_1'` confirmed order-3) →
confirms C170's own `BLOCKED-BASIS-MISMATCH` flag is resolved SPECIFICALLY
for this substitution (C168's classification-level machinery is convention-
insensitive here, as its own T8 theorem predicts) — does NOT change C169's
overall verdict. Verdict: `RECONCILIATION-CONFIRMED`.

If the check cannot be run cleanly (e.g. C168's function cannot be imported
without modification, or `H_1'` construction diverges from C170's own Step 5
computation) → `AMBIGUOUS-OR-INCONCLUSIVE`, report honestly, do not force a
verdict either way.

If FAIL → kills: the naive expectation that ANY order-3 `SU(2)` element can
be dropped into C168's construction without re-checking — would NOT kill
C168's own T8 theorem itself (that remains a correct abstract fact) but
would indicate a mismatch between this round's own concrete substitution and
what T8 actually covers, requiring re-examination before either C168 or C170
can be trusted at the level of concrete matrices.

If PASS → survives: C170's own Relaxation Map's expectation ("plausible,
since `zeta_p^{-1}` is also order-3 with the same eigenvalue set") — closes
ONE specific loose end (the basis/holonomy convention mismatch C170 flagged),
not a reopening of C168/C169's broader conclusions.

---

## Checks planned

- T1: re-derive `H_1' = zeta_p^{-1}` exactly as C170's own Step 5 did (reuse
  C170's `step5_holonomy_vs_c168` construction or recompute identically),
  confirm order-exactly-3 (not identity, cube is identity).
- T2: import C168's own `invariant_subspace_report` function via
  `importlib.util.spec_from_file_location` (reuse, not reimplement) and call
  it with `H_1'` in place of `H_1`, using C168's own `tau`.
- T3 (adversarial/edge case): also run the SAME substitution with `H_1'`
  literally recomputed as `zeta3.inv()` (sympy matrix inverse of C168's own
  `zeta3` object) as an independent cross-check against the closed-form
  `zeta_p^{-1}` construction — the two must agree exactly, or the "same
  matrix" claim is itself ambiguous.

---

## What this does NOT mean

1. Does NOT re-open or re-litigate C168's own K6 "forced not discovered"
   conclusion, nor its T1–T8 results — those are cited and reused verbatim,
   not re-derived from scratch or contested.
2. Does NOT re-open or re-litigate C170's own `t=0`/`t=1` construction or its
   `BLOCKED-BASIS-MISMATCH` framing beyond the single specific loose end named
   by its own Relaxation Map.
3. Does NOT change C169's overall verdict (`CHANNEL-STRUCTURE-MAKES-
   QUESTION-ILL-POSED` + `BLOCKED-NEEDS-NEW-MACHINERY`) — items 2 (`Cl(9)`
   twisted `D_S6`) and 3 (`SU(3)`-to-triality bridge) of C169's escalation
   remain entirely untouched regardless of this round's outcome.
4. Even on `RECONCILIATION-CONFIRMED`, does NOT license combining C170's
   `S³`-side `t=1` candidate vector with round59's actual kernel vector into
   a genuine `ker(D_full)` on `S³×S⁶` — that composition still needs C169 §5
   items 2–3, not attempted here.
5. Does NOT establish that `psi_1(g)=g^{-1}.psi_0` is the unique or
   physically-preferred `t=1` construction — unchanged from C170's own
   caveat.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

`RECONCILIATION-CONFIRMED` — `H_1'=zeta_p^{-1}` substituted into C168's own
reused `invariant_subspace_report()` function gives dimension 2 and
`NON-EXCLUSIVE-ALL-THREE-PARTICIPATE`, identical to C168's own `H_1=zeta_p`
sector. `H_1'` independently confirmed order-exactly-3 and confirmed
identical whether built via closed-form exponential or via C168's own
`zeta3.inv()`. See `decision.md` for full detail.

**Evidence:** [VERIFIED-sympy 3/3] (T1, T2, T3 all pass; results in
`results_c171.json`)

**Status:** CLOSED RECONCILIATION-CONFIRMED
