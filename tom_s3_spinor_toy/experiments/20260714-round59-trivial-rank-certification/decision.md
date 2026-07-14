# Round59-TrivialRankCertification Decision — PASS, L4B rank hypothesis discharged (internally)

**Date:** 2026-07-14
**Verdict: PASS — all 6 pre-registered PASS criteria met, 0 of 3 adversarial
skeptics refute.** `rank(D⁺|₁)=1` is now certified at the
"independently-written code" rung of the Verification Strength Ladder
(Strong), PLUS a closed-form analytic derivation that a human referee can
check by hand. Upgrades the trivial-component status from
[HYPOTHESIS-STRONG] ("pending independent sign-off") to
**[VERIFIED-INDEPENDENT-INTERNAL]** — external human review remains the one
outstanding rung above this.

## Results (workflow `wzvdwo1ui`, 6 agents, 0 errors; model: Fable 5)

| Route | Verdict | Key result |
|---|---|---|
| **A — from-scratch reimplementation** | PASS | Calibration 12/12 (both Killing branches ψ±, all 6 directions, exact); full-fibre invariant dims **(2, 1)** computed not assumed; `a = −1`, `b = −√3`, **s = 4 > 0** exact; zero leakage outside target across all 64 fibre coordinates; convention sweep: every calibration-consistent variant gives s = 4; the ONE variant that would kill the argument (global Nomizu sign flip) is exactly the one that fails calibration — legitimately excluded |
| **B — completeness/consistency audit of the original** | PASS | Full-64-dim-fibre nullspace confirms dims (2,1) with NO extra invariants — **closes a genuine gap: `v_b = y123⊗1` lay OUTSIDE the 9-dim block the original `g2su3_find_invariant.py` searched** (it was hand-supplied in the original; now independently derived). ⟨v_a,v_b⟩ = 0 exact; Hermiticity `D⁻=(D⁺)†` exact (⟨ŵ,Du_i⟩ = conj⟨u_i,Dŵ⟩, both −1 and −√3); residual (1−P_tar)Du_i = 0 over all 64 coords; s = 4 invariant under real O(2) and complex U(2) basis rotations |
| **C — analytic anchor (primary literature only)** | CONSISTENT | From the Killing equation alone: **D ψ± = ∓√3 ψ±** (Clifford e_i²=−1 verified from the paper's own convention). Friedrich bound saturated: scal = 4n(n−1)μ² = 10, (n/(4(n−1)))·scal = 3 = λ². **Closed form: `b = ⟨w, D⁺v_b⟩ = −√3` exactly** — Term1 = (D y123)⊗1 = −√3·w (the Killing eigenvalue), Term2 ≡ 0 by pairwise cancellation AND by rep theory (Λ²⊗Λ² = 3⊗3 has no SU(3) singlet). Since the target is 1-dimensional, **b ≠ 0 alone already forces rank = 1**, independent of the a-channel and of any global sign/phase convention. Bonus: also derives D⁺v_a = −√3·w, reproducing the original's raw-representative values |

**Normalization note (resolves an apparent discrepancy):** the original
reported `D(v_a)=D(v_b)=−√3·w` in the RAW basis (‖v_a‖²=3, ‖v_b‖=1). In
orthonormal bases the matrix is (a,b)=(−1,−√3), certificate s=1+3=**4**.
Same map, two normalizations — routes A and B agree exactly on both forms.

**Why the coefficient is −√3 (new understanding, not just confirmation):**
the trivial-block amplitude IS the Killing-spinor Dirac eigenvalue
−√3 = −n·μ (n=6, μ=1/(2√3)); the AHL normalization corresponds to the round
S⁶ of radius √3 (scal 10 vs unit-sphere 30). The rank-1 result is therefore
not a numerical accident of this coset — it is forced by the existence of
Killing spinors with nonzero Killing constant.

## Skeptic response matrix (Step 8a; none is a veto, each answered)

| Skeptic | Verdict | Finding | Response |
|---|---|---|---|
| 0 — common-mode hunter | NOT refuted | (a) Real common-mode surface identified: the calibration gate pins the connection only on span{ψ₊,ψ₋}; the calibration-invisible ambiguity class was solved for EXACTLY — it is the 8-dim su(3) isotropy lift. (b) A/C share the same PDF transcription — mutually dependent | (a) **Mitigated by direct adversarial probe**: skeptic perturbed the connection by 3 distinct su(3)-valued shifts — calibration still passes 12/12, yet a, b, s all UNCHANGED; structural reason: b depends only on quantities the gate pins (∇ on invariant spinors, Σe_i²=−6, grading — Term2 has disjoint support from w). The entire invisible class cannot flip s to 0. (b) **Accepted limitation, documented**: A/C independence holds vs the ORIGINAL 20260708 code (which is what the claim required), not vs each other — all routes are one AHL2023-p.42 transcription checked three ways. See "residual shared legs" below |
| 1 — independence auditor | NOT refuted, no hidden dependence | Route A architecturally disjoint from originals (matrix-based vs functional style; zero shared code idiosyncrasies; sole import sympy; no file I/O; no reference to −√3 as target anywhere). PDF transcription independently re-verified page-by-page against the paper — all tables match sign-for-sign | No action needed — this was the claim's core independence requirement, and it held under hard audit |
| 2 — mathematical referee | NOT refuted | Re-derived the full analytic chain with own independent code: eigenvalue, Friedrich normalization, dims (2,1) by hand AND by nullspace; Term2=0 shown convention-robust (eq.(5) structurally forces the pairwise cancellation). Noted the honest residual: all three routes share ONE source (AHL2023 Thm 5.1/Remark 5.2) and ONE CAS (sympy) | **Accepted limitation, documented**: the single-source/single-CAS leg is irreducible inside this session. Next rungs available if ever needed: a different CAS (Sage/Mathematica), a different primary source for the S⁶ spin geometry, or external human review — the last is the actual remaining gap for the preprint |

## Residual shared legs (honest scope of "independent")

1. All routes transcribe the same primary source (AHL2023). A transcription
   error IN THE PAPER ITSELF would fool all three. Partially mitigated:
   Skeptic 2's Friedrich-bound cross-check anchors the key eigenvalue to
   textbook Dirac-spectrum theory independent of AHL's tables.
2. All routes use sympy. A CAS bug affecting exact rational/radical
   arithmetic on 64-dim matrices would be common-mode. Considered
   negligible for this operation class, flagged for completeness.
3. Same author-AI system wrote all routes (different code paths, same
   session). This is why the status is [VERIFIED-INDEPENDENT-INTERNAL],
   not [CONFIRMED-REAL] — external review is the remaining rung.

## Consequence (combined with Rounds 52-56)

- Non-trivial G₂-isotypic sectors: certified positive (general bound,
  K_cert=2√6/3) — Rounds 52-56.
- Trivial component: rank(D⁺|₁)=1 — THIS round, three routes + analytic
  closed form.
- Therefore per channel: **dim ker(D⁺_{S⁻}) = 1, dim ker(D⁻_{S⁻}) = 0** —
  the L4B rank hypothesis is discharged at internal-certification level.
- Downstream unlocks (все были явно conditional on L4B): Exact-kernel
  corollary, Lemma L5's "all three modes purely left-handed" part,
  Yukawa-degeneracy theorem's hypothesis. The remaining headline blocker is
  now ONLY L3b (channel independence — external, Spin(8), Tom).

## Pearl (registered in pearl_registry/INDEX.md)

The trivial-block amplitude equals the Killing-spinor Dirac eigenvalue
(−n·μ), and the twisting correction (Term2) vanishes by rep theory. This
gives a MECHANISM, not a coincidence — and a falsifiable prediction for the
Universality open problem: on any nearly-Kähler coset with Killing spinors
(CP³, SU(3)/T², S³×S³), the analogous trivial-block rank should also be 1,
by the same two-line argument, WITHOUT rebuilding the full L4A/L4B
machinery. Impact 6/10.

## Recommendation

1. **preprint.tex update (needs separate confirmation, not applied here):**
   upgrade the L4B trivial-component language from "assumed, not proved /
   working hypothesis, pending independent sign-off" to "verified by two
   independent implementations (one written blind to the original code,
   re-transcribing all structure constants from the primary source) and by
   a closed-form analytic derivation from the Killing-spinor equation
   (internal verification, experiment
   `20260714-round59-trivial-rank-certification`, this work); external
   review outstanding". Affected spots: §sec:kernel rank paragraph +
   Exact-kernel corollary, Lemma L5's conditional clause, Yukawa-degeneracy
   theorem hypothesis wording, Open Problems L4B entry, abstract's
   "conditional on the L4B kernel-rank assumption" clause. Root README.md's
   just-added conditional wording (commit `dbeeaff`) likewise.
2. Root README/CLAIMS sync after preprint edit (same pass).
3. L3b memo for Tom — unchanged next external item, per the standing plan.

## Files

- `claim.md` — frozen BEFORE the run (kill criteria intact, none fired)
- `round59_route_a_independent.py` — from-scratch, primary-source transcription
- `round59_route_b_consistency.py` — completeness + Hermiticity + rotations
- `round59_route_c_analytic.py` — analytic chain verification
- Workflow transcript: `wzvdwo1ui` / `wf_1cec8ba2-a81` (journal.jsonl has all
  6 agents' full structured returns, incl. the 3 skeptics' full rationales)
