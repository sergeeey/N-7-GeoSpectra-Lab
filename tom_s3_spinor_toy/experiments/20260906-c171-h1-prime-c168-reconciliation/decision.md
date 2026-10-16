# C171 — Decision

**Date:** 2026-09-06
**Verdict:** `RECONCILIATION-CONFIRMED`. `[VERIFIED-tool]`

---

## 0. Summary

C170's own Relaxation Map (`experiments/20260906-c170-p4-step3-item1-explicit-ker-ds3/decision.md`
§8) named exactly one narrow next step: check whether `H_1' = zeta_p^{-1}`
(C170's own derived holonomy for its `t=1` candidate `psi_1(g)=g^{-1}.psi_0`)
reproduces C168's own classification when substituted for `H_1 = zeta_p` in
C168's `H_t (x) tau` invariant-subspace computation. This round ran exactly
that substitution, reusing C168's own `invariant_subspace_report()` function
verbatim via `importlib` (not reimplemented), and confirms: **YES, it
reproduces the identical result** — dimension-2 invariant subspace, all
three channels `{v,s,c}` participating, `NON-EXCLUSIVE-ALL-THREE-PARTICIPATE`
in both sectors, exactly matching C168's own `H_1=zeta_p` sector.

This was the EXPECTED outcome per C168's own T8 character-theory theorem
(`V (x) W ≅ dim(V)` copies of the regular rep `W`, for ANY representation `V`
of `ℤ₃`) — `zeta_p^{-1}` is order exactly 3 whenever `zeta_p` is, so T8
already predicted this could not come out any other way. This round checked
the prediction concretely rather than merely citing the abstract theorem,
per this project's own discipline that a concrete substitution can catch a
convention error the abstract argument would not reveal.

---

## 1. What was computed (T1–T3), `c171_h1_prime_reconciliation.py`,
   `results_c171.json`

**T1 — `H_1'` construction, closed form.** `H_1' := zeta_p^{-1}`, built the
same way as C170's own Step 5 (`theta=2*pi/3`, `zeta=diag(e^{i theta},
e^{-i theta})`, then `.inv()`). Confirmed order-exactly-3 directly
(`H1_prime_cubed == I`, `H1_prime != I`).

**T3 (adversarial cross-check, run before the main check) — two independent
constructions of `H_1'` agree exactly.** Recomputed `H_1'` a second,
independent way: `C168`'s own `zeta3` object (imported live, not
re-transcribed) inverted via sympy's `.inv()`. The closed-form construction
(T1) and this direct-inverse construction agree EXACTLY
(`matches_closed_form_construction: true`), and both match C170's own
already-reported `zeta_p_inverse` string
(`Matrix([[exp(-2*I*pi/3), 0], [0, exp(2*I*pi/3)]])`) read directly from
`results_c170.json` for cross-reference. There is no ambiguity about which
matrix "`zeta_p^{-1}`" refers to across the three rounds (C168, C170, C171).

**T2 — the main check: substitute `H_1'` into C168's own reused function.**
`c168_module.invariant_subspace_report(H1_prime_closed_form, c168_module.tau,
...)`, called via `importlib.util.spec_from_file_location` against C168's
actual script file (not a copy, not a reimplementation — the identical
Python function object C168 itself used). Result:

| | C168 original (`H_1=zeta_p`) | C171 (`H_1'=zeta_p^{-1}`) |
|---|---|---|
| `dim_invariant_eigenvalue_1_subspace` | 2 | 2 |
| `classification` | `NON-EXCLUSIVE-ALL-THREE-PARTICIPATE` | `NON-EXCLUSIVE-ALL-THREE-PARTICIPATE` |
| `channel_participates_v_s_c` | `[true, true, true]` | `[true, true, true]` |

Dimension matches, classification matches, both are the expected
non-exclusive-all-three-participate outcome. All three kill-criterion
sub-checks from claim.md pass: `H_1'` is confirmed order-3 (not malformed),
dimension matches, classification matches.

**Note on the individual eigenvector components (not load-bearing for the
verdict):** the two sectors' `channel_weight_per_invariant_vector` lists are
identical AS A SET but appear in swapped order between the two invariant
eigenvectors (C168's original has channel-weight pattern
`[complex, 1, 1]` then `[1, complex, 1]`; C171's has `[1, complex, 1]` then
`[complex, 1, 1]`) — an artifact of `H_1'` and `H_1` having swapped diagonal
entries (`zeta_p^{-1}` is literally `zeta_p` with its two diagonal entries
exchanged), which permutes sympy's `eigenvects()` return order. This does
NOT affect the claim's own endpoint (dimension + classification, both of
which are basis/ordering-independent), and is recorded here only for
completeness, per this project's Hindsight Distortion Gap discipline
(recorded same-session, not reconstructed later).

---

## 2. Kill Analysis (Perelman/OSA discipline)

**What this round kills:** the specific open question C170's own Relaxation
Map left unchecked — whether `H_1'=zeta_p^{-1}` reproduces C168's
classification "by the SAME T7-style generality argument." Confirmed: yes.
The `BLOCKED-BASIS-MISMATCH` flag C170 raised is resolved SPECIFICALLY for
this substitution — C168's classification-level machinery is convention-
insensitive to the `zeta_p` vs `zeta_p^{-1}` choice, exactly as its own T8
theorem predicts.

**What this round does NOT kill:**
1. C169's own overall verdict (`CHANNEL-STRUCTURE-MAKES-QUESTION-ILL-POSED`
   + `BLOCKED-NEEDS-NEW-MACHINERY`) — untouched. Items 2 (`Cl(9)` twisted
   `D_S6`) and 3 (`SU(3)`-to-triality basis bridge) of C169's escalation
   remain entirely unattempted.
2. C168's own K6 finding (forced-by-tau-alone, low independent
   discriminating weight beyond C133) — this round's result is fully
   CONSISTENT with K6 (it is, in fact, a direct further confirmation of
   T8's generality, one more data point in the same family C168's own T7
   already tested with a generic order-3 element and the identity control).
   It does not strengthen or weaken K6's own verdict.
3. C170's own broader `t=0`/`t=1` construction — untouched, cited and
   reused only at the single point named by its Relaxation Map.
4. C170's own honest flag that `psi_1(g)=g^{-1}.psi_0` is ONE candidate,
   not proven unique — untouched.

**Relaxation Map:** none needed — this was a single, narrow, terminal
check named by a prior round's own Relaxation Map, not itself opening a
new branch. If a future round pursues C169's items 2–3, this result means
it may treat C170's `t=1` candidate vector's holonomy convention as
reconciled with C168's classification-level machinery, without needing to
redo this specific check.

---

## 3. Floor–Ceiling Interval (FL Step 4a) — reasoned through, briefly

This is a categorical equality check (dimension + classification match or
not), not a continuous metric. The "floor" here is the degenerate case
C168's own T7 already ran (`H_1=Identity`, mechanism fully removed) which
gave the SAME classification — already flagged by C168 itself as
`CRITERION_INVALID`-equivalent at the classification level (the test cannot
distinguish "mechanism present" from "mechanism absent"). This round's
result is a further, expected instance of that same known floor-flatness,
not a new floor-defect finding — it does not change C168's own §5
Floor–Ceiling conclusion, which this round explicitly does not re-litigate.
No new ceiling construction is relevant here; the check is exact/discrete,
not a continuous statistic needing an attainability bound.

---

## 4. What this does NOT mean

1. Does NOT re-open or re-litigate C168's own K6 conclusion or T1–T8
   results — cited and reused verbatim, not re-derived or contested.
2. Does NOT re-open or re-litigate C170's own `t=0`/`t=1` construction
   beyond the single named loose end.
3. Does NOT change C169's overall verdict — items 2–3 of its escalation
   remain entirely untouched and `BLOCKED-NEEDS-NEW-MACHINERY`.
4. Does NOT license combining C170's `S³`-side `t=1` candidate vector with
   round59's actual kernel vector into a genuine `ker(D_full)` on `S³×S⁶` —
   that composition still needs C169 §5 items 2–3, not attempted here.
5. Does NOT establish `psi_1(g)=g^{-1}.psi_0` as the unique or
   physically-preferred `t=1` construction — unchanged from C170.
6. Does NOT constitute new evidence beyond what C168's own T7/T8 already
   established in general — this is a specific instance confirming the
   general theorem was applied correctly to C170's own concrete matrix, not
   an independent discovery.

---

## 5. Verification substrate (FL Step 2a, abbreviated)

Same toolchain as C168/C170 (sympy, already a project dependency, no new
dependencies). The one methodological choice worth naming: `H_1'` was
constructed and cross-checked TWO independent ways (closed-form exponential,
and `C168`'s own `zeta3.inv()`) before being fed into C168's reused
function, specifically so that any latent convention mismatch between how
C170 built `zeta_p^{-1}` and how C168's `zeta3` object is actually
structured would be caught before, not after, the main comparison. Both
constructions agreed exactly (symbolic, not floating-point). `C168`'s own
script was imported via `importlib.util.spec_from_file_location` under the
module name `"c168_module"` (not `"__main__"`), so its own
`if __name__ == "__main__":` guard did not fire and `results_c168.json` was
not touched or overwritten by this round. READY, no blocked-infrastructure
or untrusted-environment issue encountered. Script and full JSON output
(`results_c171.json`) committed alongside this decision (pending user's own
git step, per scope boundary below).

---

## 6. Recommendation on independent skeptic pass

**No independent skeptic pass run this round, and a lighter-weight
self-check is judged sufficient**, per the task's own explicit allowance
(FL Step 8a "pre-answered concerns," applicable here because: (a) this is a
narrow, well-motivated CONFIRMATORY check of a specific substitution, not a
novel construction; (b) the result matched the expectation cleanly
(`RECONCILIATION-CONFIRMED`, no unexpected finding); (c) the load-bearing
theorem (C168's own T8, character theory) was ALREADY independently
skeptic-confirmed in C168's own Section 6a pass, and this round's
computation is a direct, mechanical instance of that already-verified
theorem, not a new derivation; (d) this round reused C168's own function
verbatim via `importlib` rather than reimplementing the invariant-subspace
logic, which removes the main class of error an independent code review
would look for (a subtly different reimplementation silently producing a
matching answer by coincidence); (e) the adversarial cross-check (T3,
independent construction of `H_1'` two ways) was built into this round's own
script rather than deferred to a reviewer, addressing the most likely
failure mode (an ambiguous or wrong `H_1'`) directly.

Per the task's own explicit instruction: had the result been
`RECONCILIATION-FAILED` or `AMBIGUOUS-OR-INCONCLUSIVE`, a skeptic pass would
have become mandatory regardless of cost discipline. Since neither occurred,
none is run. This self-check discipline is recorded explicitly here (not
merely asserted) so a future reader can verify the reasoning, not just the
conclusion.

---

## 7. Status

`experiments/20260906-c171-h1-prime-c168-reconciliation/` — the single
narrow reconciliation task named by C170's own Relaxation Map is DONE.
`RECONCILIATION-CONFIRMED`: `H_1'=zeta_p^{-1}` reproduces C168's own
dim-2, all-channels-participate classification exactly, as C168's own T8
theorem predicted. This closes ONE specific loose end (the
`BLOCKED-BASIS-MISMATCH` convention gap C170 flagged) — it does NOT
complete C169's overall escalation; items 2 (`Cl(9)` twisted `D_S6`) and 3
(`SU(3)`-to-triality basis bridge) remain entirely untouched and
`BLOCKED-NEEDS-NEW-MACHINERY`. Registry files (`OPEN_BLOCKERS.md`,
`pearl_registry/INDEX.md`, `null_results/INDEX.md`, `CLAIM_LEDGER.yaml`)
deliberately NOT touched by this round, per the task's own scope boundary.
No git operations run.
