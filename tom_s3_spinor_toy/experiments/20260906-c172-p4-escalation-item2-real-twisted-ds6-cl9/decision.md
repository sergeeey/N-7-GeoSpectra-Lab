# C172 — Decision

**Date:** 2026-09-06
**Verdict:** `BLOCKED-KERNEL-MULTIPLICITY-MISMATCH` + `PARTIAL-STRUCTURE-HOLDS-NO-EXPLICIT-ZERO` (co-firing, per claim.md's own convention). `[VERIFIED-tool]` for the computed facts; the headline claim this round set out to establish is **FALSIFIED as originally framed**, per an independent context-blind skeptic pass.

---

## 0. Summary — what actually happened this round, in order

1. Built round59's own real twisted `D_S6` (`build_dirac`, 64x64 on `Σ⊗Σ`,
   reused verbatim via `importlib`, not re-transcribed) into E3's Cl(9)
   product-Dirac framework, replacing E3's flat Clifford-algebra stand-ins.
2. Four pre-registered checks ran. Checks 1 (chirality anticommutation),
   2 (decoupling), and 4 (explicit combined zero vector) all passed
   cleanly. Check 3 (kernel multiplicity matches round59's own claimed
   `dim ker=1`) **failed**: direct full-matrix nullspace gave `dim ker(D)=36`,
   not 1.
3. **The first draft of this round's own verdict logic replaced the frozen
   kill-criterion with a different, weaker "reconciliation" check
   immediately after seeing this failure**, and declared
   `REAL-TWISTED-KERNEL-VERIFIED-IN-CL9-FRAMEWORK`. This was a genuine
   post-hoc criterion-shift (this project's own AOG-1 anti-overfitting
   rule exists exactly for this failure mode).
4. An independent, context-blind skeptic pass (claim.md + code only, no
   session history — Context Asymmetry Rule) caught this, plus two further
   defects, and returned `WEAKENED` overall with one component at
   `FALSIFIED`. Full report: §4 below.
5. This decision.md reports the result the skeptic actually validated:
   the frozen criterion is honored (check 3 failed as originally
   specified → `BLOCKED-KERNEL-MULTIPLICITY-MISMATCH` fires), checks 1/2/4
   are downgraded from "evidence for the claim" to "confirmed but
   non-discriminating structural facts" (they hold for ANY Hermitian
   operator with a kernel, not specifically for the real twisted
   operator), and one genuinely new, honestly-scoped fact survives (§3).

---

## 1. What was computed, `c172_real_twisted_ds6_cl9.py`, `results_c172.json`

| Check | Result | Status after skeptic review |
|---|---|---|
| 1 — `chi6_twisted={chi6⊗I_8}` anticommutes with real `D` | exact, `[VERIFIED-tool]` | **Confirmed but non-discriminating** — a dimension-general Clifford-algebra fact (chirality anticommutes with odd-degree generators, commutes with even-degree bivectors) that E3's own decision.md (L16-20, L91-93) already stated in prose as holding for ANY operator built the same way. This round's contribution is checking it *for this specific D*, not discovering a new fact. |
| 2 — decoupling `D_full²=D²⊗I₂+I₆₄⊗D_S3(t)²` | exact at t=0,1,0.5, `[VERIFIED-tool]` | **Confirmed but forced.** Given check 1 and `chi6²=I`, this identity has no remaining algebraic degree of freedom in which to fail — it is not an independent test. |
| 3 — `dim ker(D)` matches round59's claimed `dim ker=1` | **FAILED**: `dim ker(D)=36` | This is the FROZEN, pre-registered criterion (claim.md, kill-criterion table). It failed. `BLOCKED-KERNEL-MULTIPLICITY-MISMATCH` fires, honestly, not explained away. |
| 4 — explicit `v⊗w`, `D_full·(v⊗w)=0` (both an arbitrary kernel vector AND round59's own physically-selected one) | exact at t=0,1, `[VERIFIED-tool]` | **Confirmed but forced.** One line of tensor algebra (`Dv=0`, `D_S3(t)w=0` ⟹ `D_full(v⊗w)=(Dv)⊗w+(χ·v)⊗(D_S3w)=0`) — needs neither check 1, check 2, nor Hermiticity. Would pass identically for E3's own flat stand-ins, or for the zero matrix. The `arbitrary_kernel_vector` branch is, in retrospect, a **negative control that should have discriminated physical from non-physical kernel directions and did not** — its passing is evidence the test lacks power, not evidence for the claim. |
| 5 (added post-skeptic) — direct nullspace of the FULL 128x128 `D_full` | `dim ker(D_full)=36` at t=0/1, `=0` at t=0.5; matches `dim ker(D)×dim ker(D_S3(t))` exactly | `[VERIFIED-tool]`, genuinely new: this is what E3's own decision.md actually asked for ("confirm `min|eig(D_full)|=0` exactly... by diagonalizing"), done directly rather than inferred. Confirms the skeptic's own analytic derivation (`D_full` Hermitian + decoupling ⟹ `ker(D_full)=ker(D)⊗ker(D_S3(t))`) computationally, not just on paper. |
| Reconciliation (round59's own restricted-sector vector vs. full `ker(D)`) | round59's vector IS in the full kernel, exact | **Zero discriminating power** (skeptic F4): given round59's own already-published `residual_zero=True` and `s=4>0`, this cannot fail — it restates round59's own rank-1 computation in different notation, not an independent cross-check. Kept as a correct, honest explicit-vector construction; not cited as evidence. |
| Hermiticity of `D`, `D_full` | both exactly Hermitian | `[VERIFIED-tool]`, genuine and useful (explains check 5's mechanism), but was itself checked only at `t=0.5` in the first draft — a minor scope gap, not load-bearing since check 5 now verifies the kernel dimension directly at every `t` tested. |

---

## 2. Kill Analysis (Perelman/OSA discipline)

**What this round kills:** the specific headline claim it set out to establish
— that plugging the real twisted `D_S6` into E3's Cl(9) framework produces a
"genuine, explicit combined zero mode... not a deduction from separately-
verified facts" that verifies C169 escalation item 2. This is **exactly
backwards**: check 4's success IS precisely that deduction (`Dv=0` and
`D_S3(t)w=0` imply `D_full(v⊗w)=0`), executed as matrix multiplication
instead of stated in prose — E3's own decision.md (L68-70) had already named
this as "a valid deduction from three independently-verified facts," and
this round did not close that gap, it re-performed the same deduction with
extra steps.

**What this round does NOT kill:**
1. Round59's own already-certified result (`dim ker(D⁺_{S⁻})=1` within the
   physically-relevant, su(3)-invariant, G2-isotypic-sector-excluded
   scope) — untouched, and in fact independently reinforced: round59's own
   restricted-sector kernel vector IS confirmed to be a genuine, nonzero
   element of the full unrestricted `ker(D)` (no contradiction found).
2. The chirality/decoupling structural facts (checks 1-2) — true, general,
   and worth having on record, just not specific to this construction.
3. C169's own overall verdict (`CHANNEL-STRUCTURE-MAKES-QUESTION-ILL-POSED`
   + `BLOCKED-NEEDS-NEW-MACHINERY`) — untouched. Item 3 (`SU(3)`-to-
   triality basis bridge) remains entirely unattempted. Item 2 (this
   round's own target) is **not resolved** — see Relaxation Map below.

**Relaxation Map — what a future attempt on item 2 would actually need:**
the single genuinely open, still-undecided question this round surfaced is
whether the "extra" 35 dimensions of `ker(D)` (beyond round59's own
1-dimensional physically-selected vector) are consistent with Rounds
52-56's own claimed positivity bound on the non-trivial G2-isotypic
sectors. Two live possibilities, NEITHER checked here:
  (a) Rounds 52-56's positivity bound was established for a DIFFERENTLY
      SCOPED operator/sector than the raw, unprojected 64x64 `D` this
      round diagonalized (most likely, given round59's own extensive,
      multiply-verified track record — but not confirmed);
  (b) there is a genuine, unexamined tension between "`D` has a
      36-dimensional kernel" and "non-trivial G2-isotypic sectors have
      strictly positive `D²`" that neither round59 nor this round
      resolves.
A future round should compute the SU(3) (or G2) representation content of
the full 36-dimensional `ker(D)` directly and check it against Rounds
52-56's own stated scope — this is the cheapest test that could actually
discriminate (a) from (b), and was not run here.

---

## 3. What survives — the honest, non-forced residue

1. **An explicit vector, `v = b·u₀ - a·u₁ = -√3·u₀ + u₁`** (using round59's
   own certificate amplitudes `a=-1, b=-√3`), is the first explicit
   realization in this project of round59's abstract "rank(D⁺|₁)=1" claim
   as an actual vector in the full 64-dim space, confirmed (not merely
   inferred) to satisfy `D·v=0` exactly. Small, but genuine and new.
2. **`ker(D_full) = ker(D) ⊗ ker(D_S3(t))` exactly**, verified by direct
   nullspace computation (check 5) of the FULL 128x128 operator at
   t=0, t=1 (dim 36) and t=0.5 (dim 0) — not merely deduced. This is the
   literal thing E3's own decision.md asked a future round to do
   ("diagonalize... confirm min|eig(D_full)|=0"). It is now done, with the
   honest caveat that only 1 of `ker(D_full)`'s 36 dimensions at t=0/1 is
   currently known to be physically meaningful (round59's own scope); the
   other 35 are of unexamined physical status (see Relaxation Map above).

---

## 4. Independent skeptic pass (mandatory — this is a novel construction
   with a strong positive headline claim, not a confirmatory check; FL
   Step 8a applies in full, context-blind: claim.md + code only)

**Verdict: `WEAKENED` overall, with the headline verdict LABEL specifically
`FALSIFIED`** (the frozen kill-criterion was met — check 3 failed — and the
round's own first-draft response was a post-hoc criterion substitution,
not a legitimate resolution).

Seven falsification attempts (F1-F7), findings:
- **F1** (hidden generator mismatch between `chi6` and `D`): attempted,
  **failed to falsify** — `chi6` and `D` are built from the same `E`
  object, confirmed by direct code reading. Dismissed as a real risk.
- **F2** (check 2 not independent): **confirmed** — algebraically forced
  given check 1 + `chi6²=I`; E3's own decision.md already states the
  general fact. Accepted, downgraded to "structural fact, not evidence."
- **F3** (check 4 forced by tensor algebra, not specific to the real
  operator): **confirmed**, the most consequential finding — one line of
  algebra, needs none of checks 1/2/Hermiticity. Accepted; headline
  language corrected (§0 item 5 above); `check_hermiticity`'s docstring
  explanation of "why check 4 works" was itself wrong (invoked
  `ker(D_full²)=ker(D_full)`, an argument that explains check 5, not
  check 4's direct multiplication) — corrected in code comments.
- **F4** (reconciliation check has zero discriminating power given
  round59's own already-published numbers): **confirmed**. Accepted;
  downgraded to "correct construction, not independent evidence" (§1
  table). A real code bug was also found here (early-return path returned
  a bare dict where the caller unpacks a tuple — unreachable in this run
  since `len(dom_on)==2` held, but a genuine latent defect) — **fixed**.
- **F5** (frozen kill-criterion was met and then replaced post-hoc):
  **confirmed, the FALSIFIED-class finding**. Accepted in full; this
  decision.md honors the original frozen criterion (§0 item 3, §2).
- **F6** (the "arbitrary kernel vector" branch is actually a negative
  control that should have discriminated and did not, because check 4
  lacks power per F3): **confirmed**. Accepted; reclassified in §1 table.
  `v_round59`'s own branch is NOT subject to this critique (it IS
  su(3)-invariant by construction) and remains legitimate.
- **F7** (overclaimed scale — "full 9-dimensional Dirac operator" is
  actually a 64-dim algebraic reduction-to-invariants (round59's own
  scope, "Twisted Dirac operator on invariants") tensored with a single
  2x2 S³ mode, with MISMATCHED connections — untwisted/Nomizu on the S⁶
  side, torsion-deformed on the S³ side, not one consistent connection on
  a genuine product manifold): **confirmed**. Accepted; the scale claim
  is corrected here and should not be repeated in any future citation of
  this round.

No skeptic finding is dismissed. All seven are Fixed or Accepted-with-
documentation, per this project's Step 8a Response Matrix — none required
the "true kill" escalation (core predicate false with no viable response),
because the underlying computations (F1's non-issue, the surviving §3
facts) are sound; only the INTERPRETATION and VERDICT LABELING were wrong,
and both are corrected in this document.

---

## 5. Floor–Ceiling Interval (FL Step 4a)

Not directly applicable in the usual continuous-metric sense (this is an
exact/discrete existence check, like C170/C171). The closest analogue,
per the skeptic's own F2/F3 findings: the "floor" here is exactly what E3
already established with flat stand-ins (checks 1/2/4-type facts hold for
ANY Hermitian operator with a kernel) — this round's own result sits AT
that floor, not above it, for checks 1/2/4. The one place this round rose
above the floor is check 5 (direct diagonalization of the real `D_full`,
which a flat stand-in's decision.md never did) and the explicit-vector
constructions in §3.

---

## 6. What this does NOT mean

1. Does NOT complete C169's escalation item 2 as originally framed — the
   headline "verified" language is retracted; see §0, §4.
2. Does NOT complete item 3 (`SU(3)`-to-triality basis bridge) — untouched.
3. Does NOT establish or contradict Rounds 52-56's G2-isotypic positivity
   bound — the tension named in §2's Relaxation Map is genuinely open, not
   resolved either way by this round.
4. Does NOT decide `t=0` vs `t=1` selection (OB1's central question) —
   both give an identical `dim ker(D_full)=36` structure; no new
   information on selection.
5. Does NOT invalidate round59's own certified result — independently
   reinforced (round59's own vector confirmed nonzero in the full
   kernel), not contradicted.

---

## 7. Pearl Registry entry (7th recurrence of "forced, not discovered")

To be added to `pearl_registry/INDEX.md`: checks built to confirm a
specific, physically-motivated construction (chirality anticommutation +
tensor-product zero-mode combination) turned out to be forced by general
algebraic structure (Clifford-algebra grading; elementary tensor algebra)
independent of which specific operator was plugged in — the 7th instance
of this project's own recurring pattern (C144/C153/C154/C156/C158/C168
precede it). New variant: this time the "forcing" was caught only by an
INDEPENDENT SKEPTIC PASS after a first-draft self-assessment missed it
(unlike C168, where the round's own honesty check caught it directly) —
worth flagging as a case where self-check discipline alone was
insufficient and the mandatory-skeptic-for-novel-constructions rule (FL
Step 8a) earned its cost directly.

---

## 8. Retroscan note

C169 §4 (and this project's broader OB1/OB14 discussion) cites "round59's
kernel is exactly 1-dimensional" as an established fact. This round found
the UNRESTRICTED matrix has a 36-dimensional kernel — **this does NOT
contradict or require revising C169 §4**, which refers to the
physically-scoped, su(3)-invariant-sector-restricted quantity round59
itself computed, confirmed unaffected by this round (§2, §4-F4). Recorded
here so a future reader encountering "36" in this round's own JSON output
does not mistake it for a correction of round59's own headline number.

---

## 9. Status

`experiments/20260906-c172-p4-escalation-item2-real-twisted-ds6-cl9/` —
DONE, skeptic-reviewed, verdict corrected post-review.
`BLOCKED-KERNEL-MULTIPLICITY-MISMATCH` (frozen criterion) +
`PARTIAL-STRUCTURE-HOLDS-NO-EXPLICIT-ZERO` (structural facts confirmed,
not discriminating). C169 escalation item 2 remains **open**, now with a
sharper diagnosis: the natural chirality/decoupling/product-kernel
construction is algebraically forced and cannot by itself distinguish the
real twisted operator from a flat stand-in; the actual open question is
the physical status of `ker(D)`'s 35 "extra" dimensions against Rounds
52-56's own positivity claim (§2 Relaxation Map) — the cheapest next test
on this line, not yet attempted. Registry files (`OPEN_BLOCKERS.md`,
`CLAIM_LEDGER.yaml`, `pearl_registry/INDEX.md`, `null_results/INDEX.md`)
deliberately NOT touched by this round pending user confirmation of scope
(this round produced a corrected-but-still-open result, not a clean
REJECT or PROMOTE, so the right registry action is not obvious without
discussion). No git operations run.
