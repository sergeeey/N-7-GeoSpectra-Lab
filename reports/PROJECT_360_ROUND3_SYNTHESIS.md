# Project 360° Scientific Red Team — Round 3: Kill-Table, Recomposition, Publication Map

**Date:** 2026-07-15
**Inputs:** Round 1 (`PROJECT_CLAIM_LEDGER_360_ROUND1.md`), Round 2 (`PROJECT_360_ROUND2_EXPERT_ATTACKS.md`).
This closes the remaining deliverables of the 6-round design (cross-expert conflict
was largely resolved by the convergence already found in Round 2; this round adds
the formal kill-table, a recomposition verdict, and a publication map).

**Update (same day, after initial synthesis):** KT-1 and KT-2 — the two
highest-priority tests below — were actually executed (tool-verified, not just
designed), and KT-7 completed. Results are inline in the table and in
"Executed kill-tests — results" below. This also prompted three cheap wording
fixes applied directly: `RESEARCH_STATUS_REPORT.md:321,348` (stale
"RESOLVED/EXACTLY" predating G102), `preprint_abstract.md` (stale banner +
"exactly"→conditional, "zero-parameter"→"zero-fit"), `README.md:25` (stale test
count).

---

## Kill-Table

| Claim / test | PASS (predefined) | FAIL (predefined) | Cost | Impact if it flips | Stop rule | Result |
|---|---|---|---|---|---|---|
| **KT-1** Parent-action origin of D⊗S⁻ (R2-1) | D⊗S⁻ falls out of a stated reduction | No parent action stated | Days | **Highest** | If ambiguous after 1 honest attempt, mark `BLOCKED-INFRASTRUCTURE`, not FAIL | **EXECUTED — BLOCKED-EXTERNAL, corrected from an earlier "FAIL/(B)" mislabel** (this session's own predefined stop rule says exactly this case — "reduction ambiguous" — should be marked BLOCKED, not FAIL, and the first write-up of this result didn't follow its own rule). What was actually shown: no parent higher-dimensional action producing D⊗S⁻ is stated anywhere in `preprint.tex` or its references; the twist is a mathematically-motivated choice (computable nonzero index), and the reduction is *under-specified* (no background field/flux/gauge-bundle is named that would source the S⁻ twist) — the agent could not complete a derivation because the input needed to attempt one doesn't exist in the project's own sources, which is a BLOCKED verdict, not a demonstrated FAIL of the physical idea. Closest real analog (heterotic "standard embedding," Candelas-Horowitz-Strominger-Witten 1985) requires a pre-existing independent 10D gauge sector this project's framework structurally lacks (`preprint.tex:1400-1401`). **Not currently on the paper's own open-problems list**, unlike every other comparably load-bearing assumption — this is the actionable finding, independent of the PASS/FAIL/BLOCKED label question. See "Executed kill-tests" below. |
| **KT-2** Does triality ℤ₃ descend to a nontrivial isometric action on S⁶=G₂/SU(3)? (convergent finding, geometry+index lenses) | Yes → Atiyah-Bott-Lefschetz closes L3b | No (expected) → equivariant-index escape closed | Cheap | High | One clean answer either way ends this sub-question | **EXECUTED — FAIL confirmed, tool-verified, but narrower in scope than first written up.** Built the full octonion algebra + 𝔤₂=Der(𝕆) (14-dim, SVD-confirmed; independently spot-checked by a second, from-scratch construction — see Verification section, dim=14 reproduced at machine precision, 7.1e-15) and the complete 28×28 triality operator T on 𝔰𝔬(8). Fix(T) = 𝔤₂ exactly (residuals ~1e-15). Since S⁶=G₂/SU(3) is built from G₂'s transitive action, triality is the literal identity **on the base manifold S⁶ as a diffeomorphism**. **Scope correction (this was under-stated in the first write-up):** this closes ONLY the "triality as a nontrivial *geometric/isometric* action on the base S⁶" escape route — it does NOT close, and does NOT render moot, "triality as an external symmetry acting on the *fibre* / multiplicity space / zero-mode Hilbert space," which is exactly what the F4/J₃(𝕆) route (KT-3) is trying to construct. Those are logically distinct claims — a base-isometry no-go says nothing about an operator-level symmetry that never claims to move points of S⁶. The earlier "priority order" note below that this "may make KT-3 moot" is retracted as overstated. |
| **KT-3** F4/J₃(𝕆) route condition 1: is the diagonal 𝔤₂⊂F₄ (acting on 𝕆³) actually identifiable with the geometric G₂ acting on S⁶'s physical fibre/operator content? | Explicit map constructed, consistent with S⁶'s actual bundle structure | No consistent identification exists | Moderate | High for the F4 route specifically — **NOT diminished by KT-2**, which operates at a different logical level (base isometry vs. fibre/operator symmetry, see corrected KT-2 row) | If the check requires Tom's own framework input, mark `BLOCKED-EXTERNAL`, not FAIL | **EXECUTED — BLOCKED-EXTERNAL, run at the user's explicit request even with no new input from Tom (correspondence log checked first: nothing new since 2026-06-22; a 2026-07-13 public post about Part 4 is not a reply to us).** New tool-verified check (not just re-reading the project's own prose): built the diagonal g₂ embedded in 𝕆³ and the S₃ slot-permutation U explicitly — U centralizes the diagonal g₂ exactly (residual 0), restricted to one slot the diagonal action literally *is* the ordinary G₂ action already used in the paper — but this is a tautology of block-repeating one matrix three times, carrying no information about whether the physical construction actually has this combined fibre. Cross-checked against `preprint.tex`'s actual construction: the real physical content is **three separately-existing 8-dim bundles/operators, one per channel** — no combined 24-dim fibre or combined operator exists anywhere in the current construction. **Precision correction the agent caught in its own task framing** (worth recording): 𝕆³ decomposes as one copy each of 8_v⊕8_s⊕8_c (per the project's own quoted primary source, Baez), not three copies of 8_v as an earlier framing assumed — doesn't change the verdict but sharpens why the route looks promising and where exactly it stops. **Precise boundary:** last checkable-without-Tom fact = the diagonal-g₂/F₄ algebra is internally consistent; first fact requiring Tom = whether the actual physical field content should be reorganized into this combined fibre, which nothing internal to the project supplies independent grounds for. See "Executed kill-tests" below. |
| **KT-4** L3B-INDEXARITH general formula — additional test points (1,1) and (3,0) | Predicted I=0 and I=27 match independent Chern-root computation | Mismatch at either point | ~15 min sympy | Low-medium | Two points settle it | **EXECUTED — PASS, both points, genuinely independent construction.** Self-check first: rebuilt Sym²(V) via an explicit multiset-of-2 root construction (not reusing the original script's `T⊕(T⊗T)` trick) and reproduced I(2,0)=7 by a different route — method validated before trusting it on new points. Then: adjoint=(1,1), built as traceless(V⊗V*) (8 roots, 2 zero-weights — correct for su(3)'s rank-2 Cartan, not an error), ch3=0 identically (each nonzero root cancels its negative under the odd cube) → index=0, matching prediction exactly. Sym³(V)=(3,0), 10 roots (all degree-3 multisets of {x,y,z}), ch3 = (27/2)·c3_T exactly (residual 0) → index=27, matching prediction exactly. Formula substitution was never used in either construction — only in stating what the prediction was. **Honest scope, unchanged from before:** this raises the point count from 3 to 5, it does not prove the general formula — status remains `SUPPORTED ON CONTROLS — GENERAL PROOF OPEN`, per the project's own claim-A-index-map.md. One partial insight surfaced: the proportionality ch3∝c3_T held in both new cases because degree-3 Weyl(S₃)-invariant polynomials in {x,y,z} (x+y+z=0) form a 1-dimensional space — a real partial argument toward the general proof's crux (step 2 in claim-A-index-map.md), but not shown here to cover an arbitrary (p,q) irrep in general. See "Executed kill-tests" below. |
| **KT-5** ρ=14 decomposition completeness | True λ²_min comfortably positive | True λ²_min near zero or negative | Cheap | Medium | One completeness check settles it | **EXECUTED — PASS, clean.** Rebuilt the ρ=14 analog of the 5-piece decomposition (reusing `g2su3_v14_adjoint_full_matrix.py` + `g2su3_nomizu_crossterms.py`'s generic Clifford/structure data, substituting ρ=14 `ADE`/`AD_RAW` for ρ=7's `rho7_ep`/`rho7_nuk`) and checked it against ground-truth D²_14 on **all 12 of 12** basis vectors of the ρ=14 multiplicity space (Round 22's own ρ=7 check only covered 2 of 16 — this is stronger coverage). Exact match everywhere, `sympy` symbolic throughout, no numerical fallback. True λ²_min = 10/3 (native basis) ≈ 3.33, i.e. ≈9–17× the 0.381 norm-bound floor — the bound was never close to tight, no hidden near-zero mode. **Bonus finding:** this exact eigenvalue set was already computed once before, in Round 20 (2026-07-09), four days *before* the norm-bound program (Round 55/56) existed — so "no zero mode at ρ=14" was independently established earlier; what this test adds is specifically confirming the *decomposition* (not just the eigenvalues) generalizes. See "Executed kill-tests" below. |
| **KT-6** SU(2)_R (+ Witten global) anomaly check without assuming B-L | Anomaly-free without B-L input | Anomaly-free only after B-L added | Hours | Medium | Binary outcome | **EXECUTED — PASS on the letter, but sharpens R2-5 rather than resolving it.** All checkable non-abelian conditions vanish ([SU(2)_R]³, mixed [SU(2)_L]²[SU(2)_R], [SU(2)_R]²[SU(2)_L], [SU(2)_R]²[Grav]) — but these are forced to vanish for *any* fermion content by the traceless-generator argument, not a nontrivial confirmation specific to this geometry. Witten global anomaly: 4 SU(2)_R doublets (even, safe) — true because N_c=3 is odd, a numerical fact rather than a deep cancellation. **The real finding:** the four genuinely content-dependent conditions from the existing check ([U(1)_Y]³, [SU(2)]²U(1)_Y, [SU(3)]²U(1)_Y, [Grav]²U(1)_Y) *cannot even be formulated* without a U(1) charge to plug in as the third leg — removing B-L doesn't just weaken the test, it makes the interesting question unaskable. Genuine positive side-result: the geometry gives an unambiguous SU(2)_R doublet/singlet split for all 16 Weyl states, with no bidoublet fermion — a real, non-trivial, checked fact, independent of B-L. See "Executed kill-tests" below. |
| **KT-7** Independent test-suite reproduction (R2-7) | Pass/fail counts match documented count | Discrepancy found | Minutes | Low probability of surprise, closes a process gap | One run sufficient unless it disagrees | **EXECUTED — PASS.** 2512 passed, 4 skipped, 0 failed, exit 0 (see Verification section). |

**All seven kill-tests are now executed and tool-verified.** ~~KT-1~~, ~~KT-2~~,
~~KT-3~~, ~~KT-4~~, ~~KT-5~~, ~~KT-6~~, ~~KT-7~~ (see results above/below).
KT-3 was run at the user's explicit request even with no new input from Tom
Lawrence (checked the correspondence log first — nothing new since
2026-06-22), specifically to document precisely what is and isn't checkable
without him, rather than leave it untried. It correctly came back
BLOCKED-EXTERNAL, not FAIL — the project's own standing constraint (don't
initiate contact) means the remaining piece genuinely cannot be resolved by
more compute from inside this audit.

**All seven items have now actually been run, across four passes this
session, all tool-verified, not literature-reasoned.** KT-1/KT-2/KT-3 came
back negative/BLOCKED (KT-1 and KT-2 after a self-caught overclaim in the
first write-up — see corrected labels above); KT-4 and KT-5 came back clean
PASSes, strengthening two separate parts of the project's own results (the
index-formula point count, and the L4B ρ=14 certification); KT-6 came back
"PASS on the letter" but with a sharper, more precise version of the R2-5
concern than originally stated.

---

## Recomposition verdict

**Question restated (Falsification-Ladder Recomposition Gate):** do the
individually-verified pieces (ind=1 per channel [PROVED] + dim ker=1 internally
certified [pending external review] + sign(ind)=+1 [PROVED]) combine, as worded, to
license "N_gen=3, three Standard Model generations"?

**Verdict: No — and the project's own primary documents already say so correctly.**
`preprint.tex`'s table explicitly lists N_gen=3 as "Conjectured (Atiyah-Singer L2;
L3 open)," and the title itself is "*Toward* Three Generations." Executing KT-1 and
KT-2 does not change this verdict; it sharpens it with two new, tool-verified facts.

**What changed as a result of this audit (now with KT-1/KT-2 executed, not just designed):**
1. **New open item, logically upstream of L3b, confirmed real (KT-1, executed):**
   there is no stated parent physical action anywhere in `preprint.tex` or its
   references for the twist choice D⊗S⁻ — it is a mathematically-motivated choice
   (nonzero computable index), not a physical derivation. This is not a hedge or a
   suspicion; an agent read the full paper and its bibliography and confirmed the
   gap is real and, notably, not currently listed among the paper's own otherwise-
   thorough open-problems caveats. **Recommend the project add this as an explicit
   open-problems item** (this audit did not edit `preprint.tex` itself — that is a
   scientific-content decision for the project author, not a wording/staleness fix).
2. **The most natural escape route for L3b is now confirmed closed, not just
   suspected (KT-2, executed):** the triality ℤ₃'s fixed subspace was computed
   directly over the full 28-dimensional 𝔰𝔬(8) (not the partial 12-dim check the
   project's own same-day script had done) and found to equal 𝔤₂ exactly, to
   machine precision. Triality is the literal identity map on S⁶. The
   ℤ₃-equivariant-index idea that two independent expert lenses reached for is
   foreclosed. This does not touch the project's own separately-pursued
   SO(4)×SO(4) fiber-breaking route (already known, by the project's own concurrent
   work, to hit a different wall) — but it does mean the F4/Spin(9) work should
   treat the symmetric/equivariant escape as closed, not pending.
3. **Applied, not just flagged:** `RESEARCH_STATUS_REPORT.md:321,348` (stale
   "RESOLVED/EXACTLY," predated G102), `preprint_abstract.md` (stale banner added,
   "exactly"→conditional, "zero-parameter"→"zero-fit"), and `README.md:25`/Track-B
   test count (stale "2210"→"2500+", cross-checked against this round's own
   independent pytest run) were all corrected directly during this audit.

**None of this is a rejection of the project's math.** Every lens that tried to
independently re-derive a load-bearing calculation (index arithmetic, centralizer
computation, Killing-spinor kernel argument) found it correct, and the two
executed kill-tests (KT-1, KT-2) were themselves independent tool-verifications,
not re-statements of the project's own claims. The recomposition finding remains
specifically about the step from "individually true pieces" to "the headline as
worded" — the project's own most-current, most-careful documents already get this
right, and this round both confirms that framing with fresh evidence and applies
the small set of documents that had drifted from it.

---

## Publication map

Given the accumulated results, four separable, independently defensible
publications emerge — separating them reduces the risk that the whole program
gets judged by its hardest-to-defend claim (N_gen=3 exactly) instead of its most
solid ones.

| # | Paper | Core content | Status | Risk if published now |
|---|---|---|---|---|
| **P1** | **Channel-degeneracy no-go on nearly-Kähler S⁶** (pure math) | E-L3B (E_v≅E_s≅E_c), G102 (centralizer=0), the now-executed ℤ₃-triality-fixed-point argument (KT-2, tool-verified this round) — an honest, self-contained negative result about why triality-based generation counting cannot be closed internally on G₂/SU(3) | **Strong candidate, not yet submission-ready** — still needs, before that status: a single canonical statement of G102's scope (continuous-symmetry-only, per Round 2 R2-2's own correction), an external (non-agent) mathematician's read of the exact-kernel argument, and one pass to unify notation/conventions across `preprint.tex`, `L3B_SPIN8_INTERFACE_SPEC.md`, and the underlying experiment decision.md files, which currently differ slightly | Low relative to P3 — this is a no-go theorem, defensible independent of whether N_gen=3 is ever resolved — but "ready now" (this report's original wording) overstated it; the checklist above is real work, not a formality |
| **P2** | **Spectral-gap certification methodology on naturally reductive cosets** (computational math) | L4A/L4B kernel certification technique, the Kostant-Parthasarathy-for-cubic-vs-Levi-Civita pitfall, the general Casimir bound, and the honest lesson about "three routes sharing one source/CAS ≠ strong independence" per the project's own verification ladder | **Strong candidate, not yet submission-ready** — same caveat as P1: needs an external read of the exact-kernel argument (currently internally certified only, per Round 2 R2-4) before a referee-facing methods paper can credibly claim the technique works in general | Low — methodological, useful to the field independent of the physics claims, but "ready now" was likewise too strong |
| **P3** | **"One generation from S³×S⁶ geometry; three generations conditional on external input"** (the physics paper — retitled per skeptic's suggestion) | Current `preprint.tex` content, retitled and reframed so the abstract matches what the body proves; KT-1's result (no stated parent action for the D⊗S⁻ twist — currently BLOCKED-EXTERNAL, not on the paper's own open-problems list) should be added as an explicit open item before submission | **Furthest from ready of the four** — needs the Round 1 §C wording fixes (done), the KT-1 finding written into §sec:open, and ideally an attempt at the specific parent-action derivation (the 7-input "Parent Operator and Physical Provenance" program below) before the title change is even the main issue | Medium-high if submitted as-is: both the title/abstract framing AND the newly-surfaced missing-parent-action gap are things a hostile reviewer would hit; neither is a one-paragraph fix once KT-1 is taken seriously |
| **P4** | **Gauge sector and anomaly structure of the S³×S⁶ construction** | B-L non-uniqueness (Round61-BL), the G97 isometry-group finding, KT-6 (SU(2)_R anomaly check, not yet run) — a self-contained phenomenology note on what the geometry does and doesn't fix in the gauge sector | **Needs KT-6 run first** — unchanged from initial assessment | Low once KT-6 is done; this is honest, bounded scope work |

**Recommended sequencing, corrected:** none of the four are actually "ready now" —
that phrasing in the first version of this report overstated it. P1/P2 are
*closer* to ready (lower remaining risk, no open scientific gap, just external
review and notation unification). P3 is furthest from ready: it now carries both
the known title/framing issue and the newly-confirmed KT-1 gap (no stated parent
action), and should not be submitted until at least the latter is written into
the paper's own open-problems list, per the recommendation below.

---

## Verification status (this round)

**KT-7 closed.** An independent pytest reproduction of the Track B test suite was
run directly via Bash (not delegated to an agent, to close the R2-7 gap after the
first agent reported `BLOCKED-INFRASTRUCTURE` for lack of tool access). First
attempt was lost when the session was interrupted mid-run (background task
`bx2v7vtop` returned no completion record — process death, not a test failure; per
the Substrate Gate this is correctly not counted as evidence either way). Re-run to
completion:

```
cd tom_s3_spinor_toy && python -m pytest tests/ -q --tb=short
2512 passed, 4 skipped, 75 warnings in 294.79s (0:04:54)
exit code 0
```

**[VERIFIED-REAL]** Zero failures, clean exit code, run to completion by an
independent invocation (this session, not the original authoring session). This
confirms the project's test-suite claims are not validation theater — a real
external run reproduces a healthy suite.

**One minor doc-lag finding, same pattern as Round 1 §C:** root `README.md`'s
Track B summary table (line 25) states "**2210 tests**" without a date qualifier.
The actual current count in the identical scope (`tom_s3_spinor_toy/tests/` only)
is 2516 collected (2512 passed + 4 skipped) — the badge undercounts by ~300 tests,
consistent with continuous growth since whenever that number was last set (compare:
2221 passed on 2026-06-22 per `PROJECT_CURRENT_STATE.md`; 2748/2488 *collected*
including `experiments/` on 2026-07-05/07-13 per `tom_s3_spinor_toy/README.md`).
Not a scientific problem — a small instance of the project's own recurring
"badge/count drifts from CI-authoritative source" pattern (`CLAUDE.md` Claim Scope
Discipline section already names this exact failure mode for README test badges).
**Applied** (see "Applied fixes" below).

**Explicit status labels (adopted from an external second-pass review of this
audit, which correctly pushed back on conflating these):**
```
SOFTWARE REPRODUCTION      — PASS   (2512/4/0, exit 0, independently re-run)
SCIENTIFIC INDEPENDENT VERIFICATION — NOT ESTABLISHED
```
Passing tests confirms the current implementation is internally consistent and
reproduces its own recorded expectations from a clean invocation — it does *not*
confirm the underlying physics/math formulas are correct, that no fixture encodes
its own expected answer, or that a shared convention error couldn't sit in both
the code and its tests simultaneously. This distinction matters because it is
easy to read "0 failures" as stronger evidence than it is; the project's own
`integrity.md` Validation Theater Guard makes the same point about self-authored
tests, and it applies here even though this test suite is not synthetic-data
validation theater in the sense that rule targets — the two claims (test suite
is healthy vs. results are physically correct) are simply independent of each
other and should not be merged into one number.

**Applied fixes (uncommitted working-tree edits — git diff shown, no commit made
without being asked):**
```
$ git diff --stat
 README.md                                   |  2 +-
 tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md |  4 ++--
 tom_s3_spinor_toy/preprint_abstract.md      | 19 ++++++++++++++++---
 3 files changed, 19 insertions(+), 6 deletions(-)
```
Full diff available via `git diff` in the repo; not reproduced here for length.
This addresses a fair complaint raised in an external second-pass review of this
audit ("no confirmed diff/commit for the claimed edits") — the edits are real,
inspectable, and currently uncommitted by design (commits are not made without
explicit user request per this session's operating rules).

**Independent spot-check of KT-2's foundational building block (this session,
separate from the KT-2 agent's own construction):** re-derived octonion
multiplication from scratch via Fano-plane structure constants (not reusing the
project's or the KT-2 agent's code) and verified, via a fresh SVD-based
derivation-space computation: alternativity holds to 7.1e-15 over 50 random
trials, and dim(Der(𝕆)) = 14 exactly (rank 50 of 64). This corroborates the
foundational fact KT-2's fuller claim (Fix(T)=𝔤₂ over the complete 28-dim 𝔰𝔬(8))
is built on. **Caveat, stated plainly per the Audit Verification Gate ("agent's
[VERIFIED] = your [INFERRED] until independently re-checked"):** this spot-check
reproduces the dim=14 building block, not the full 28×28 triality-operator-and-
fixed-subspace computation — that fuller result remains at the level the KT-2
agent reported (tool-verified by that agent, cross-checked against the project's
own partial same-day script, but not fully re-derived a second time by me from
first principles). Given the spot-check passed cleanly, this is reasonable
grounds for confidence, not full independent reproduction of every step.

**Recommended next research step (not part of this audit's own scope, but worth
naming as a possible Round 4 for the project itself, adapting a suggestion from
an external second-pass review):** a "Parent Operator and Physical Provenance"
investigation, frozen as a claim ("D_{S⁶}⊗S⁻ follows from a specific
higher-dimensional action and reduction mechanism, not chosen post-hoc for its
index") with explicit PASS/FAIL/BLOCKED criteria and 7 required inputs (parent
theory dimension/signature, fermion representation under the parent gauge/
Lorentz group, the full kinetic action, the spin-bundle decomposition on
S³×S⁶, the origin of the SU(3) connection, the rule assigning the internal
fermion representation S⁻, and all normalization/chirality conventions). KT-1
(this round) is a first, partial pass at exactly this question and already
returned BLOCKED-EXTERNAL — the fuller investigation would need those 7 inputs
specified before a PASS/FAIL verdict (rather than BLOCKED) becomes possible.

---

## Executed kill-tests, round 2: KT-5 and KT-6

Both executed with Bash-equipped agents reusing existing project code (not
rebuilt from scratch), same day.

### KT-5 — ρ=14 decomposition completeness: PASS, clean, no caveats

Reused `g2su3_v14_adjoint_full_matrix.py` (the ρ=14 representation, already
built in the repo) and the generic Clifford/structure-constant data from
`g2su3_nomizu_crossterms.py` (the module that did Round 22's original ρ=7
check), substituting ρ=14 inputs (`ADE`, `AD_RAW`) for ρ=7's (`rho7_ep`,
`rho7_nuk`). Reconstructed the 5-piece sum and checked it against ground-truth
`D²_14` on all 12 of 12 basis vectors of the ρ=14 multiplicity space — exact
match everywhere, symbolic `sympy` throughout, no numerical shortcuts. True
λ²_min = 10/3 (native basis, ≈3.33), 9–17× the previously-certified 0.381
norm-bound floor. This closes the completeness gap Round 3's first pass flagged
as the real (under-stated) ρ=14 risk — it is no longer inferred by analogy with
ρ=7, it is directly checked. Side finding worth the project's own attention:
this exact eigenvalue set had already been computed once, in Round 20
(2026-07-09), four days before the Round 55/56 norm-bound program existed —
worth cross-referencing so the two results are cited together rather than
independently.

### KT-6 — SU(2)_R anomaly / Witten global anomaly: PASS on the letter, sharper finding underneath

All checkable non-abelian conditions ([SU(2)_R]³, mixed [SU(2)_L]²[SU(2)_R] and
[SU(2)_R]²[SU(2)_L], [SU(2)_R]²[Grav]) vanish — but by the traceless-generator
argument, which holds for *any* fermion content, not a nontrivial confirmation
of this specific geometry. The Witten global (mod-2) anomaly is safe: 4 SU(2)_R
doublets (even) — true because N_c=3 is odd, a numerical fact rather than a
structural guarantee (had this project's own N_c come out even, this specific
check would have flagged a fatal inconsistency; worth noting since N_c=3 is
itself a separately-established result elsewhere in this project, not derived
here).

**The result does not resolve R2-5's presupposition concern — it sharpens it.**
The four genuinely content-dependent anomaly conditions from the project's
existing check ([U(1)_Y]³, [SU(2)]²U(1)_Y, [SU(3)]²U(1)_Y, [Grav]²U(1)_Y) require
a U(1) charge as their third leg; without B-L, they cannot be *formulated*, not
merely left unconfirmed. So "anomaly-free without B-L" is technically true but
for a different, weaker reason than the original test anticipated (it's not
that the interesting checks pass independently of B-L — it's that removing B-L
removes the ability to ask the interesting question at all).

**Genuine positive side-result, independent of the B-L question:** the geometry
gives an unambiguous SU(2)_R doublet/singlet split for all 16 Weyl states in one
generation, with no bidoublet Weyl fermion anywhere in the content (checked over
all 32 states including CPT conjugates) — the (2,2)₀ bidoublet the project
discusses elsewhere is a boson (Higgs/Yukawa sector), not a fermion, and doesn't
complicate this check. This is a real, checked, non-trivial fact about the
construction, not previously stated this explicitly.

### Impact on the recomposition verdict

KT-5 strengthens confidence in L4B (the internally-certified kernel result) —
one more piece of it is now exactly verified rather than analogically inferred.
KT-6 adds a fifth item to the "what changed" list in the Recomposition verdict
above: the anomaly-cancellation claim in `preprint.tex:284-294` and its
underlying script should be captioned as checking anomaly-freedom *given* the
B-L/Y assignment, not as an independent confirmation of it — the distinction
matters for exactly the same reason KT-1 mattered (a claim resting on an input
that's separately still open should say so at the point it's used, not just in
a different section's open-problems list).

### KT-3 — F4/J₃(𝕆) route condition 1: BLOCKED-EXTERNAL, run anyway on request

Executed at the user's explicit instruction ("run KT-3 anyway, without new
input from Tom") after confirming via the correspondence log that nothing new
relevant to L3b/Spin(8) has arrived since 2026-06-22 (the most recent update,
2026-07-13, is a public Part-4 video post, not a reply to this project).

**What was newly tool-verified, not just re-read from the spec document:**
built the diagonal g₂ (14-dim) embedded in 𝕆³ and the S₃ cyclic slot-
permutation U explicitly, from scratch. U centralizes the diagonal g₂ exactly
(residual 0 to machine precision); restricted to a single slot, the diagonal
action literally *is* the ordinary G₂ action already used elsewhere in the
paper's S⁻ construction. **But this is a tautology** — block-repeating one
8×8 matrix three times and permuting the blocks commute by elementary linear
algebra; it carries zero information about whether the actual physical
construction has this combined 24-dim fibre. Cross-checked directly against
`preprint.tex`'s real content (not the spec document's description of it):
the construction has **three separately-existing 8-dimensional bundles, one
per channel, each with its own independent twisted Dirac operator** — no
combined fibre or combined operator exists anywhere in the current paper.

**A genuine, useful correction surfaced during this check:** the task as
originally framed described 𝕆³ as "three copies of the vector rep 8_v" — the
project's own quoted primary source (Baez) actually gives one copy each of
8_v, 8_s, 8_c. This doesn't change the BLOCKED verdict, but it explains more
precisely why the F4 route looks structurally promising (it's one copy of
each real channel, not three redundant copies) and sharpens exactly where the
gap is.

**The precise boundary (this is the actionable output of KT-3):** the last
thing checkable without Tom Lawrence's input is that the diagonal-g₂/F₄
algebra is internally self-consistent. The first thing that genuinely
requires his framework is whether the actual S³×S⁶ physical field content
should be reorganized into this single combined fibre with a combined,
block-diagonal Dirac operator — nothing internal to the project (the S³
spin-connection gates, the SU(4) branching, the warp-factor checks, or the
same-day SO(4)×SO(4) route, which independently hit its own structural wall)
supplies grounds for that reorganization. This is exactly the question
`L3B_SPIN8_INTERFACE_SPEC.md` was written to hand to Tom, precisely worded,
whenever he responds.

With KT-3 now run, **all 7 kill-tests in this audit are executed.** KT-3's
BLOCKED-EXTERNAL status does not change — it was already the expected
outcome per the project's own standing constraint — but it is now backed by
a fresh, independently tool-verified check rather than resting only on the
project's own same-day self-assessment.

### KT-4 — index formula at (1,1) and (3,0): PASS, both, genuinely independent

Reused the exact method from `experiments/20260715-index-formula-s-tensor-t-candidate/verify_index_formula.py`
(Chern roots x,y,z with x+y+z=0, calibration ∫ch3(T)=1 from G33) but built two
NEW bundles from scratch rather than substituting into the closed-form I(p,q):

- **Self-check first** (method validation before trusting it on new points):
  rebuilt Sym²(V) via an explicit multiset-of-2 root construction — a different
  route than the original script's `T⊕(T⊗T)` trick — and independently
  reproduced I(2,0)=7.
- **(1,1) = adjoint**, built as traceless(V⊗V*): 8 roots (2 zero-weights,
  correctly reflecting su(3)'s rank-2 Cartan subalgebra). ch3 = 0 identically
  (every nonzero root cancels its negative under cubing) → index = 0, exactly
  matching the prediction.
- **(3,0) = Sym³(V)**: 10 roots (all degree-3 multisets of {x,y,z}). ch3 =
  (27/2)·c3_T exactly (residual 0) → index = 27, exactly matching the prediction.

Formula substitution was never used to compute either index — only to state
what the predictions were, so this is a genuine, independent check by the
project's own definition of what would count as one (claim-A-index-map.md's
own falsification-test description). Point count for the direct-Chern-root
method rises from 3 to 5.

**Honest scope, per the project's own status line — unchanged despite the
clean result:** this does not prove the general formula I(p,q) for all (p,q).
Status remains `SUPPORTED ON CONTROLS — GENERAL PROOF OPEN`. One partial insight
did surface, worth logging for the project: the proportionality ch3∝c3_T held
in both new cases because degree-3 Weyl(S₃)-invariant polynomials in {x,y,z}
(with x+y+z=0) form a 1-dimensional space — this is a real partial argument
toward closing claim-A-index-map.md's step 2 (the crux of the still-open general
proof), but it was only shown here for bundles built as Sym^k(V) or
traceless(V⊗V*), not for an arbitrary (p,q) irrep constructed by a general
plethysm — the representation-ring route (R(SU(3))→K⁰(S⁶)→ℤ) that
claim-A-index-map.md names as the genuinely independent Path B remains untried.

---

## Independent second-pass verification of KT-4, KT-5, KT-6 (2026-07-16)

At the user's request, KT-4, KT-5, and KT-6 were re-verified by fresh agents
with no access to this report (or Round 1/2) and, for KT-6, no access to the
first pass's own committed script — genuinely independent re-derivations, not
re-runs of the same code. Per this project's own Independent Verification
Strength Ladder, this moves the evidence for these three results from "same
model, isolated context" toward "independently-written code" — a real step up,
though still the same underlying model family, not a cross-model check.

**KT-4 — CONFIRMED, with a new insight.** Independent construction (own Sym^p(V)
and adjoint=V⊗V̄-minus-trivial code, Weyl-dimension-formula cross-check, 4-point
numeric spot-check in addition to symbolic) reproduced I(1,1)=0 and I(3,0)=27
exactly. New, genuinely additional finding: the adjoint's weight multiset is
exactly invariant under negation, which forces ch3=0 by parity for *any*
self-conjugate irrep (p,p) — a structural reason (not just this computation)
that generalizes beyond the two checked points, independently derived, not in
the first pass's writeup.

**KT-6 — CONFIRMED.** Independent construction (own SU(2) generator matrices,
own fermion-multiplet table built by tracing through the block-generator code
rather than reading the first pass's script) reached the identical structural
conclusion — Q_R=(u_R,d_R) and L_R=(ν_R,e_R) are genuine SU(2)_R doublets, no
bidoublet fermion exists, 4 doublets (even) for the Witten check — and
independently arrived at essentially the same meta-observation as the first
pass (3 of 5 conditions are group-theoretic tautologies true for any content;
only the bidoublet-absence fact and the doublet-parity count are actually
informative about this specific geometric derivation).

**KT-5 — CONFIRMED, after correctly catching a real process gap.** The second-pass
agent first found *no trace* in the repository of the ρ=14 5-piece-decomposition
check the first pass claimed to have run (no file, no decision.md entry) and
flagged this honestly as a discrepancy rather than assuming the claim was true.
Instructed to actually perform the reconstruction fresh, it did so and got an
**exact symbolic match** on all 12 of 12 basis vectors of the ρ=14 multiplicity
space (λ²_min=10/3, matching the first pass exactly) — plus a sign-convention
control the first pass didn't report as explicitly: the opposite sign
convention fails cleanly on all 12/12 vectors (6-23 nonzero residual entries
each), confirming the match is a real, sensitive test, not a vacuous one.
**Verdict: the first pass's claim was accurate — the work was real, it just was
never persisted to the repository as a file.** This is a legitimate process
lesson (see below), not a validation-theater finding.

**New artifact created this pass:** `tom_s3_spinor_toy/experiments/20260708-dolan-casimir-g2su3/g2su3_v14_5piece_decomposition_check.py` —
the ρ=14 decomposition-vs-ground-truth check, now actually saved to the repo
(closing the gap the second-pass agent found). Not yet wired into a formal
Round entry/decision.md — that would be a follow-up for the project itself if
it wants to formally promote this into its own gate-tracker, separate from
this audit.

**Process lesson worth recording:** an agent that computes something real but
doesn't save the artifact leaves the *project* unable to verify the claim was
ever actually checked, even when the claim itself was true. "I ran it and got
X" is weaker than "here is the file that ran and got X" — this matches the
project's own Verification Substrate Gate concept (artifacts must be persisted
to a file/log, not asserted only in conversation) and should be treated as a
standing instruction for any future audit work: save the script, not just the
reported number.

---

## KT-8 (2026-07-16/17) — Does the full 9D product Dirac operator on S³×S⁶ have a zero mode at all?

**Origin:** an external adversarial review (pasted in full by the user, "RDR 2.1"
framework, claim ledger C1-C28) raised a concern its own author labeled KT-2
(unrelated to this report's KT-2 above — different numbering scheme, same slug
collision the project's own methodology names as a Type-1 error class, see
`~/.claude/rules/research-methodology.md` § Классификатор): the paper's own
earliest gate (`experiments/20260615-g8-chirality-obstruction/`, 2026-06-15)
already established that the bare S³ Dirac operator has spectrum ±(m+3/2)/ρ —
strictly bounded away from zero — and explicitly named this "the Witten
problem." The reviewer's claim: since the physical, 4D-mass-determining object
is the *full* 9-dimensional internal Dirac operator on the product S³×S⁶, not
the S⁶ factor alone, and S³'s own factor never has a zero mode, does the full
product operator have a zero mode at all — regardless of what the S⁶-only
twisted operator D_{S⁶}⊗S⁻ does?

Per this project's own external-agent-findings rule (external review "VERIFIED"
= this audit's "INFERRED" until independently tool-verified — see
`feedback-external-agent-findings-gate.md`), the reviewer's claim was *not*
accepted at face value. Two independent steps were taken:

**Step 1 — delegated construction (general-purpose agent, first pass).** Built
the explicit Clifford-algebra product structure required for an odd (dim 3) ⊗
even (dim 6) factorization: Γ_M(e_j) = Γ³_j ⊗ χ₆ for the three S³ directions,
Γ_M(f_i) = I₂ ⊗ Γ⁶_i for the six S⁶ directions (the only construction that
satisfies the Clifford relations across the product — verified to machine
precision). Reused the project's own established S³ eigenvalue (1.5 = 3/2·ρ₃,
from G8) and 20,000 random S⁶-side test operators, including near-zero-
eigenvalue ones mimicking the actual twisted zero mode. Result: D_full² =
D₁²⊗I + I⊗D₂² exactly, zero cross-term (~1e-15), min|eig(D_full)| = 1.5
regardless of D₂'s spectrum.

**Step 2 — independent from-scratch re-verification (this session, direct
Bash tool call, no agent, no reuse of the first pass's script).** Built Cl(3)
from Pauli matrices, Cl(6) via an independent Jordan-Wigner construction (3
fermionic modes → 6 gammas on an 8-dim rep), verified both satisfy the
Clifford anticommutation relations exactly, built the chirality operator χ₆
(χ₆²=I, Hermitian, anticommutes with all 6 gammas — all confirmed), assembled
the full 9-generator, 16-dim Cl(9) representation and verified all 81
anticommutation relations exactly. Set D₁ = 1.5·σ_z (matching G8's floor) and
D₂ = a random Hermitian combination of the 6 gammas scaled to produce a
near-zero eigenvalue (got ±0.185, i.e., deliberately small to stress-test the
claim). Computed D_full directly and squared it.

**[VERIFIED-tool], independently reproduced twice with different code:**
```
max|Dfull^2 - (D1^2 (x) I + I (x) D2^2)| residual: 4.44e-16   (machine epsilon)
min |eigenvalue| of Dfull: 1.5114                              (D2's near-zero mode: 0.185)
expected floor from D1 alone: 1.5
```
The product operator's spectral gap is bounded below by S³'s own gap (3/2·ρ₃)
**regardless of what the S⁶ factor's spectrum does** — confirmed with an
S⁶-side operator specifically chosen to have a near-zero eigenvalue, and the
full-operator floor still came out at 1.5, not near zero. **ker(D_{S³×S⁶}) = 0**
for the actual construction this project uses (twist applied only on S⁶, S³
left round/untwisted) — the external reviewer's KT-2 concern is CONFIRMED, not
merely plausible.

**What this does and does not mean:**
- It does **not** contradict G73/G74A/G74B, G8, or any existing gate — those
  compute the index/kernel of D_{S⁶}⊗S⁻ *alone* on the S⁶ factor, and that
  computation is untouched by this finding.
- It **does** mean the "zero modes" counted by the headline N_gen=3 mechanism
  are zero modes of the S⁶-factor operator alone, not of the true 9D internal
  Dirac operator that would set 4D fermion masses in a standard Kaluza-Klein
  spectroscopy sense (massless 4D fermion ⟺ zero mode of the *full* internal
  operator, not one factor of a product). No file in the repository (`g8`
  through the current preprint, checked by grep for "massless", "4D mass",
  "KK tower") states or defends an alternative physical mechanism that would
  let a per-factor zero mode still yield a genuinely massless 4D state despite
  the full operator being gapped.
- This is a **structural gap upstream of, and independent of, KT-1** (parent
  action for the twist) — KT-1 asks "why this twist," KT-8 asks "even granting
  the twist, does the resulting *full* operator do what a KK zero mode needs to
  do." Both are now confirmed real, both are currently absent from
  `preprint.tex`'s own open-problems list (KT-1 was added 2026-07-16, see
  below; KT-8 is not yet added — this is the immediate open action item).

**Confidence grading (per this audit's own evidence policy):**
- The matrix computation itself (Clifford relations, D_full² decoupling,
  spectral floor) — **[VERIFIED-tool]**, high confidence, independently
  reproduced twice with different code by two different actors (delegated
  agent + this session directly) on the same underlying math.
- That Γ_M(e_j)=Γ³_j⊗χ₆, Γ_M(f_i)=I₂⊗Γ⁶_i is *the* standard/unique way to build
  a Dirac operator on a product of an odd- and an even-dimensional factor —
  **[INFERRED]** from first principles (it is the only assignment that
  satisfies the Clifford relations across the product, checked directly), not
  yet cross-checked against an external canonical reference (e.g.
  Lawson–Michelsohn, *Spin Geometry*, Ch. II) for whether some other
  convention or a nontrivial connection term could reintroduce a cross-term.
  This is the one remaining gap before treating KT-8 as fully closed rather
  than "closed under the standard construction."
- The claim that no alternative physical mechanism is stated anywhere in the
  paper — **[VERIFIED-tool]** via grep (exhaustive keyword search, zero hits),
  not exhaustive prose-reading of every paragraph for an unnamed argument.

**Not yet done (explicit, not a silent gap):** integrating this finding into
`preprint.tex`'s open-problems section (mirroring how KT-1 was added
2026-07-16); updating the recomposition verdict above to reflect that the
"ind=1 per channel" input to N_gen=3 is now known to be an S⁶-factor-only
statement, not a full-operator zero-mode statement; the remaining ~24 claims
in the external reviewer's C1-C28 ledger beyond KT-1/KT-2(theirs)/KT-4 have not
been individually re-verified.

### Literature cross-check (2026-07-17) — closes the remaining [INFERRED] gap

At the user's explicit request, the one open item above (uniqueness of the
Clifford product construction) was checked against the published literature
rather than left as a first-principles inference.

**[VERIFIED-tool, external source]** Sire & Xu, "A variational analysis of the
spinorial Yamabe equation on product manifolds," arXiv:2005.01448, Eq.
(2.2)-(2.3): for a Riemannian product M₁×M₂ with M₁ even-dimensional, Clifford
multiplication on S(M₁)⊗S(M₂) is

```
(ξ⊕ζ)·(ψ⊗φ) = (ξ·ψ)⊗φ + (ω_C^{M1}·ψ)⊗(ζ·φ)
```

i.e. M₁'s own generators act plainly (⊗Id), while M₂'s generators are twisted
by ω_C^{M1}, M₁'s chirality/volume element — giving the product Dirac operator

```
D = D_{M1}⊗Id_{S(M2)} + ω_C^{M1}⊗D_{M2}
```

with, per the paper's own text, **no separate curvature-correction term** — the
formula "arises naturally from the Clifford algebra structure of V⊕W" alone
(their §2.1, the standard `Cl(V⊕W)` graded-tensor-product construction, the
same one underlying Lawson–Michelsohn Ch. I). Substituting M₁=S⁶ (even,
χ_C^{S6}=χ6), M₂=S³ reproduces **exactly** the construction used in both of
this audit's independent computations (Γ_M(e_j)=Γ³_j⊗χ6 for the S³
generators, Γ_M(f_i)=I⊗Γ⁶_i for the S⁶ generators) — this was not an arbitrary
or convenient choice, it is *the* standard construction for a product with an
even-dimensional factor, confirmed against an independent published source.

**This also upgrades the decoupling from a numerical spot-check to an
algebraic identity.** Expanding D² directly from the formula above:
```
D² = D_{M1}²⊗I + (D_{M1}ω_{M1} + ω_{M1}D_{M1})⊗D_{M2} + ω_{M1}²⊗D_{M2}²
```
The cross-term vanishes identically because a chirality operator always
anticommutes with its own manifold's Dirac operator (`{ω_{M1}, D_{M1}}=0` is
general, not S⁶-specific — it is the defining property of a chirality
operator) and `ω_{M1}²=Id` (also general) — giving `D² = D_{M1}²⊗I +
I⊗D_{M2}²` as an algebraic fact, not a coincidence that happened to hold to
1e-16 in this particular numerical test. The earlier numerical residual
(4.4e-16) is now understood as floating-point noise around an exact zero,
not an approximately-small quantity.

**KT-8 status: CLOSED, no remaining gap — for the round, untwisted
Levi-Civita $S^3$ ansatz specifically.** Both open items from the initial
write-up are now resolved: (1) the construction is confirmed standard against
an independent published source, not merely self-consistent, and (2) the
vanishing cross-term is now an algebraic theorem, not a numerical observation.
$\ker(D_{S^3\times S^6})=0$ for that specific construction stands as a fully
verified, tool-and-literature-confirmed result. **Scope calibration
(2026-07-17, accepted):** after KT-9/E2/E3 (below), this must not be quoted
as "the full operator on $S^3\times S^6$ has no zero mode" without
qualification — that statement is refuted only for the round/Levi-Civita
$S^3$ factor. KT-9's own product-decoupling identity shows
$\ker D_{S^3}(t)\neq0 \wedge \ker D_{S^6,S^-}\neq0 \Rightarrow
\ker D_{\mathrm{full}}(t)\neq0$ for a torsion-deformed $S^3$ factor at
computable $t$ — a mathematical escape route from this exact no-go, not a
physical resolution of it (no parent-action selection principle for $t$ is
known). The no-go stands for the specific ansatz actually used in this
paper's results; it does not extend to the full class of possible
$S^3$-factor modifications.

### Third independent confirmation (2026-07-17, external reviewer, different model)

A second external adversarial review (different AI system, RDR-2.1-style
framework) independently re-derived the same result via a simplified symbolic
2×2 spectral-block argument (generic eigenvalue pair λ on S³, ±μ on S⁶,
block `[[λ,μ],[μ,-λ]]`, exact SymPy diagonalization) rather than the full
16-dimensional Clifford construction used in this audit's own two passes.
**Cross-checked quantitatively, not just narratively:** `sqrt(1.5²+0.185²) =
1.51137` against this audit's own from-scratch computation's `1.5113689` —
agreement to 5 significant figures (the reviewer's D2-eigenvalue input was
reported rounded to 0.185, accounting for the 6th-digit difference). Per this
project's own Independent Verification Strength Ladder, a genuinely different
AI model reaching the same quantitative result is a real step up from
"same model, isolated context," though this audit's own external-agent-findings
rule was still applied: the reviewer's own sweeping claim-ledger relabeling
(REFUTED across C1-C28) was *not* accepted at face value — only the specific,
independently-checkable KT-8 mathematics was treated as confirmed.

**Calibration correction to the above (2026-07-17, same day, user-provided):**
two refinements to how this third pass should actually be graded, both accepted.

1. **The numeric match certifies the spectral-block arithmetic, not the
   underlying operator-algebra step.** `sqrt(1.5²+0.185²)=1.51137` matching
   this audit's `1.5113689` is a strong catch for sign errors, wrong linear
   combinations, bad diagonalization, or normalization mistakes in the block
   realization — but it cannot, by itself, verify the actual claim that
   `D_full² = D1²⊗I + I⊗D2²` (the two inputs 1.5 and 0.185 and the target
   formula were shared across all three passes, not independently arrived
   at). Real independence for *that* step comes from the combination of three
   genuinely different derivations already on record: the full 16-dim
   Clifford construction, the 2×2-block symbolic derivation, and the
   invariant analytic proof from chirality-operator anticommutation
   (`{ω,D_own}=0`, `ω²=Id` — both dimension-general facts, not S⁶-specific).
   The numeric match is a consistency certificate *on top of* those three,
   not a fourth independent derivation of the central step.
2. **"Different AI model" is not the same rung as a blind external review.**
   Downgrade the confidence label from "a real step up toward 'different
   model'" to the more precise **"implementation-independent and
   derivation-diverse verification"** — models can share the same standard
   construction, the same question framing, and (critically, as happened
   here) the same expected answer and input numbers, none of which a truly
   independent check would have. The next rung up, per this project's own
   Independent Verification Strength Ladder, would require handing an
   external reviewer *only*: the frozen claim, the product-ansatz
   assumptions, the two factor-operator definitions, and the PASS/FAIL
   criterion — withholding both the expected result (`ker D_full=0`) and the
   specific number (`1.51137`).

### Abstract wording tightened further (2026-07-17, same day)

The initial abstract fix (above) still used the phrase "candidate mechanism,"
which risked being read as an already-existing (if caveated) 4D-generation
mechanism. Retightened per the same feedback to a more precise formulation:
the $S^6$-level index mechanism is stated first and scoped explicitly to
"one net chiral mode per postulated triality channel"; the positive $S^3$
spectral gap is stated as the reason these modes cannot become zero modes of
the full internal operator; and an explicit sentence now reads "The
gauge-structure and fermion-quantum-number results below should be read at
the level of this $S^6$-factor mechanism, not as an established 4D physical
spectrum." Recompiled (`pdflatex -halt-on-error`, exit 0, no undefined
references).

### Integration into preprint.tex (2026-07-17)

At the user's explicit direction (choosing the "full status rebuild" option
over a narrower open-problems-only addition), KT-8 has now been written
directly into `preprint.tex`, not just recorded in this audit report:

1. **Abstract** — the opening claim ("We derive the Standard Model gauge
   structure...") softened to "We construct a candidate mechanism...", with an
   explicit forward-reference to the full-operator gap; the chirality/zero-mode
   sentence and the Proposition~T2 sentence both corrected to state that the
   twist evades T2 only on the S⁶ factor, not on the full 9D operator.
2. **Existing open-problems item 4 (KT-1, added 2026-07-16)** — corrected: it
   previously asserted Prop. T2 "does all of the work" / is fully evaded by the
   twist; this was itself an overclaim that KT-8 refutes. Now correctly scoped
   to "evaded on the S⁶ factor" with a forward-reference.
3. **New open-problems item, "Full-operator zero-mode gap"** — added
   immediately after item 4, marked **REFUTED within the stated product
   ansatz — blocking** (not merely "open"), with the full derivation, the
   Sire–Xu literature citation, and an explicit statement that resolving it
   requires new physical input on the S³ factor specifically.
4. **"Fermion mass hierarchy" item** — cross-referenced: its "S³ factor is a
   fixed, generation-independent block" claim is now flagged as conditional on
   a physical zero mode existing at all, which the new item shows is not
   currently the case.
5. **Bibliography** — added `SireXu2020` entry (arXiv:2005.01448).

**Verified:** `pdflatex -interaction=nonstopmode -halt-on-error` run twice
(to resolve cross-references) — exit 0 both times, 27 pages (was 26), zero
"Undefined reference" or LaTeX-error lines in either log.

**Status update (2026-07-17):** KT-8 and its literature cross-check, the
abstract retightening, and the E1/E2/E3 preprint integrations below have
all since been committed, merged (`--no-ff`), and pushed to `origin/main`
(commits `744b53b`, `3b818a4`, `c2a65c4`, `ec32211`). The remaining ~24
claims in the external reviewers' ledgers beyond KT-1/KT-2(theirs)/KT-4/KT-8
have not been individually re-verified.

---

## KT-9 (2026-07-17) — Is there a representation-theory-independent verification of dim ker(D_{S⁶}⊗S⁻)=1?

**Origin:** the 100-directions-brainstorm critique (item 82's correction,
`reports/100_DIRECTIONS_BRAINSTORM_2026-07-17.md`) flagged that this
project's existing "independent" passes on the exact-kernel result (G73
index theorem, G74A Lichnerowicz/Schur, Round59's three routes) all share
the same underlying SU(3)/G₂ representation-theoretic branching-rule
machinery at some point — implementation-independent, not
mathematically-independent.

**Attempt (`experiments/20260717-round69-e4-representation-free-kernel-check/`):**
built an explicit ambient Cl(7)-trivialization + Gauss–Weingarten hypersurface
connection + exact sphere-moment Galerkin projection — genuinely
representation-theory-free (no SU(3)/G₂ weights, characters, or Casimir
values invoked anywhere in the construction). Before attempting the actual
twisted claim, the method was calibrated against the already-published
UNTWISTED baseline spectrum $\pm(k+3)$ as a mandatory positive control.

**Result — `BLOCKED_BASELINE_CALIBRATION_FAILED`.** The calibration scan
found a clean, reproducible algebraic relation (eigenvalue$^2=K(K+6)$,
confirmed at 30+ independently-scanned values of the free normalization
constant $K$) — but no natural $K$ reproduces the required baseline
eigenvalue 3 (the textbook-motivated $K=3$ predicts $3\sqrt3\approx5.196$
instead). Because the untwisted baseline could not be certified, the
twisted operator (the actual claim) was correctly never attempted — extending
uncalibrated machinery would produce unverified code, not a trustworthy
check.

**Status calibration note:** this was originally reported as a "NULL /
inconclusive" result and has been corrected. Per this project's own
Verification Substrate Gate (`falsification-ladder.md` Step 2a — "test
could not run ≠ claim failed"), the target claim was never actually tested;
only the tooling failed at baseline calibration. The headline
`dim ker=1` claim's status is **unchanged, untested by this method** — not
weakened, not strengthened.

**What this does mean:** a real, currently-unclosed methodological gap —
this project's exact-kernel result for S⁶ has no
representation-theory-independent verification yet. Not a defect in the
result itself, but a real limitation on how independently it has actually
been checked. Relaxation Map (in the experiment's own `decision.md`): the
most likely fix is a Clifford-signature convention mismatch ($\Gamma_a^2=+I$
vs the standard Riemannian $-I$), not attempted here.

---

## KT-10 (2026-07-17) — Do the other 3 homogeneous nearly-Kähler 6-manifolds pass the same Route-C structural prefilter as S⁶?

**Scope calibration (2026-07-17, accepted):** this section's title is
deliberately narrower than "does the S⁶ construction generalize" or
"is universality confirmed on 3/4 spaces" — Route C is a necessary-condition
prefilter (an isotropy-Schur bound plus a no-singlet check), not a
sufficient demonstration of a twist's existence, a nonzero index, an exact
one-dimensional kernel, three generations, or a lift to the full operator.
Passing Route C means only: no obstruction of this specific,
representation-theoretic kind was found. `ROUTE_C_PASS` is the correct and
complete status; "universality confirmed for 3 of 4" would be an overclaim.

**Origin:** this project's own "Universality" open item (\S\ref{sec:open})
asks whether the Lichnerowicz–$G_2$-Schur mechanism (L4) applies to
$\mathbb{CP}^3$, $\mathrm{SU}(3)/T^2$, and $S^3\times S^3$, the other three
Butruille-classified homogeneous nearly-Kähler 6-manifolds. Prior state:
$\mathrm{SU}(3)/T^2$ rank-one established (Round 65); $\mathbb{CP}^3$
found "ill-posed, no computation possible" (Round 64, via
Charbonneau–Harland 2016's instanton-deformation machinery); $S^3\times S^3$
untested.

**Result (`experiments/20260717-round70-e5-universality-cp3-s3xs3/`) — mixed, both parts diagnosed carefully:**

**Part A ($\mathbb{CP}^3$) — `ROUTE_C_PASS`, corrects Round 64 without reversing it.**
Round 64's finding is confirmed and *reinforced* with a second, independent
reason (CH2016's own instanton operator only reaches
$\Lambda^1\oplus\Lambda^2$ of the spinor bundle, never the full $S\otimes S^-$
this project's mechanism needs — an operator-type mismatch on top of Round
64's representation-type mismatch). But Round 64 overgeneralized this into
"no computation is possible on $\mathbb{CP}^3$ at all": a *different*
mechanism (Route C — the same isotropy-Schur/no-singlet check already
validated for S⁶/SU(3)-$T^2$) is directly computable from CH2016's own
already-published isotropy data (verified: $\mathfrak{m}^{1,0}=V(1,1)\oplus
V(0,-2)$, $\Lambda^2(\mathfrak{m}^{1,0})\otimes\Lambda^2(\mathfrak{m}^{1,0})$
excludes the trivial rep, same crux structure as S⁶/SU(3)-$T^2$) and DOES
pass. **Important scope caveat:** Route C is a necessary-condition/
isotropy-Schur-bound check ($\dim\ker\leq1$) — it does **not** establish the
exact kernel $(\dim\ker D^+,\dim\ker D^-)=(1,0)$ for the physically-relevant
operator, which remains a separate, unclosed L4A/L4B-style calculation for
$\mathbb{CP}^3$ (this project's own L4A/L4B tension for S⁶ itself — Kostant–
Parthasarathy proved only at $t=1/3$, not the physical $t=1/2$ — was not
attempted to be resolved here or transported to $\mathbb{CP}^3$; doing so was
explicitly scoped out as comparable in cost to the original 21-round
`dolan-casimir-g2su3` derivation).

**Part B ($S^3\times S^3$) — `OPEN_STRUCTURALLY_DISTINCT`, not a gap in effort.**
$\mathfrak{m}^{1,0}=V2$ (single copy of the 3-dim adjoint of
$\mathrm{SU}(2)_{\mathrm{diag}}$), and
$\Lambda^2(\mathfrak{m}^{1,0})\otimes\Lambda^2(\mathfrak{m}^{1,0})=V0\oplus
V2\oplus V4$ — this **does** contain the isotropy-trivial $V0$, the opposite
finding from S⁶, SU(3)-$T^2$, and $\mathbb{CP}^3$. Route C's cheap
no-singlet argument therefore does not decide $S^3\times S^3$ either way
(not NULL, not PASS — the coefficient on that slot is genuinely unknown, a
real structural difference, not unfinished work). The isotropy-Schur bound
($\dim\ker\leq1$) still holds independently regardless.

**Pearl candidate noted (not promoted):** the three Route-C-PASS spaces all
have $\chi(M)\neq0$ (2, 6, 4); the one open space has $\chi(S^3\times
S^3)=0$ — a testable but unconfirmed correlation, `impact_score` 4/10, `n=4`
too small to distinguish from coincidence.

---

## KT-11 (2026-07-17) — Explicit S³×S³ Nomizu/torsion construction to resolve KT-10's open $\mathrm{Term2}$ coefficient

**Origin:** direct follow-up to KT-10 Part B — attempting to compute the
actual coefficient on the isotropy-trivial slot, using
Charbonneau–Harland 2016's own explicit basis for $S^3\times S^3=
\mathrm{SU}(2)^3/\mathrm{SU}(2)_{\mathrm{diag}}$ (page 18 of the PDF, in
this repo).

**Result (`experiments/20260717-round71-e6-s3xs3-nomizu-torsion-audit/`) — `ILL-POSED`,
one of four pre-registered kill criteria, not a PASS/FAIL/BLOCKED.**
**Scope calibration (2026-07-17, accepted):** attribution below is to "the
set of formulas extracted from CH2016 page 18 and combined under the
conventions used in this experiment," not to a claim that CH2016 itself
contains an error — without a dedicated source-level audit, several
explanations remain open and undistinguished: an actual typo/error in the
source; a missing scale factor; different normalizations used on nearby
pages of the same source; a mismatched/miscombined basis; a transcription
error on this project's side (checked once, see below, but not exhaustively
ruled out); or the two formulas (the Killing form $B$ and the almost-complex-
structure action $J$) describing different metrics or reductive splittings
that should not have been combined directly. The finding below is that
\emph{this specific combination}, as used, is inconsistent — not a verdict
on CH2016 as a source.
The formulas extracted from CH2016's page 18 and combined under this
experiment's conventions are **not internally Hermitian-consistent**:
their stated Killing form gives $B(X_1,X_1)=5/3$ but $B(Y_1,Y_1)=2$, though
$J(X_i)=Y_i$ (their own literal statement) requires these to be equal.
**Independently hand-verified this session** (30 seconds, sympy-free):
$B(X_1,X_1)=\tfrac16[(1+\sqrt2)^2+(1-\sqrt2)^2+4]=\tfrac16(10)=\tfrac53$;
$B(Y_1,Y_1)=6\cdot[\tfrac16+\tfrac16]=2$. Confirmed exactly. Two
structurally different repairs were attempted (Hermitize the metric to fit
the stated $J$; or keep the metric and solve for the metric-compatible
$J_B$ instead) — they disagree with each other, and a built-in control
check confirmed the natural-reductivity checker code itself is correct (raw,
unmodified $B$ passes by a fully general theorem). The whole finding was
then independently reproduced within the same session via a *different*
CH2016 basis (Appendix C) and a *different* method (general 3-parameter
metric sweep) — identical numbers.

**What survives:** KT-10's isotropy-Schur bound ($\dim\ker\leq1$) and Route-C
crux finding — neither depends on the Nomizu-map construction that hit the
obstruction. **What remains open:** $\mathrm{Term2}$'s actual coefficient —
the substrate needed to compute it was never certified trustworthy, so
no claim (zero, nonzero, or otherwise) is made about it either way.

**Concrete next step (not attempted):** CH2016 pages 7–12 (not consulted
this round) may contain a direct cyclic/$\mathbb{Z}_3$-eigenspace
construction of $S^3\times S^3$'s complex structure that sidesteps this
specific basis ambiguity by construction, rather than requiring a choice
between two ad hoc repairs.

**Diagnostic table for the next pass (distinguishes the competing
explanations above, not yet filled in):**

| Formula | Page | Convention | Checkable invariant | Result |
|---|---|---|---|---|
| Reductive splitting | — | — | $[\mathfrak{h},\mathfrak{m}]\subset\mathfrak{m}$ | |
| Metric coefficients | — | — | positive definiteness | |
| $B(X,X)$ | — | — | consistent basis normalization | |
| Nomizu map | — | — | metric compatibility | |
| Torsion | — | — | skew symmetry | |
| $\mathbb{Z}_3$-action | — | — | automorphism and invariance | |

Filling this table (cheap, reuses CH2016 pages already partially read) would
distinguish source error / missing scale factor / normalization mismatch /
basis mismatch / transcription error / different-metric-context before any
further Nomizu-construction attempt.

---

**KT-9/10/11 status update:** none of these three have been integrated into
`preprint.tex` — E1 (dimension correction) and E2/E3 (S³ torsion deformation
candidate mechanism) were integrated as dedicated open-problems items
(commits `c2a65c4`, `ec32211`); KT-9/E4 (methodological gap), KT-10/E5
(universality, mixed), and KT-11/E6 (ill-posed) remain standalone findings
in their own experiment folders and in this report only. Full derivations:
`reports/E1_E5_VERIFICATION_ROUND_2026-07-17.md` and the individual
`experiments/20260717-round69/70/71-.../decision.md` files.

---

## KT-12 (2026-07-17) — Is there an independent physical/geometric selection principle for E2/E3's torsion parameter $t$?

**Origin:** E2/E3's own explicit caveat — the torsion-deformed $S^3$
connection removes KT-8's obstruction at computable crossing values (e.g.
$t=0,1$ at the lowest level), but no physical principle was known for
selecting any of them over the Levi-Civita value $t=1/2$. Per this
project's own Adaptive Iteration Branch Rule, four rival hypotheses were
frozen **before** running any test:

| Hypothesis | Content |
|---|---|
| H1 | $t$ fixed by requiring existence of a Killing spinor on $S^3$ under $\nabla^t$ |
| H2 | $t$ fixed by background/gravitational equations of motion for the torsion-sourcing field |
| H3 | $t$ fixed by anomaly cancellation in the resulting 4D effective theory |
| H4 | $t$ is a free parameter; the zero-mode value is fine-tuning |

**Result (`experiments/20260717-round72-e7-t-selection-principle/`) — `PASS_H1_SUBQUESTION_INDEPENDENT_CRITERION_FOUND`, H1's cheapest sub-question only.**
Reading Agricola (arXiv:math/0202094) §2 — established via curvature/Ricci
computations, entirely **before** her §3 introduces the Dirac operator at
all — $t=0$ is her "canonical connection" (Ambrose–Singer: the unique
connection with $\nabla T=\nabla R=0$) and $t=1$ is her "anticanonical
connection" (same Ricci tensor). **Independently re-derived this session**
(direct symbolic computation, Jacobi identity, confirmed on a non-vacuous
basis triple — not just citing the paper): for $S^3=\mathrm{SU}(2)/\{e\}$,
the full curvature tensor factors exactly as
$R^t(X,Y)Z=t(t-1)\cdot S(X,Y,Z)$ and vanishes identically **iff** $t\in\{0,1\}$
— the classical Cartan–Schouten flat connections on any Lie group with a
bi-invariant metric, a fact with **zero reference to spinors or zero
modes**. Cross-referencing E2's own `results_e2.json` (read-only): the
$n=0$ zero-mode crossing set is **exactly** $\{0,1\}$ — matching this
independent, purely-geometric criterion precisely — while the $n=1,2$
crossings ($\{-1/3,4/3\}$, $\{-2/3,5/3\}$) are confirmed **not** in that set.

**What this does and does not mean:**
- Supports H1's necessary sub-question: $t=0,1$ are not arbitrary — a real,
  independent geometric distinction exists.
- Does **not** prove H1's actual claim (Killing spinor existence at
  $t=0,1$) — that requires a further, unattempted spinorial computation.
- Explains only 2 of 6 crossings; H4 remains the honest default for the
  $n=1,2$ crossings.
- H2 and H3 remain completely untested (each would require a
  background-field EOM setup or a 4D anomaly computation this project does
  not have — comparable in scope to a new multi-round investigation).
- **Does not promote E2/E3** or change KT-8's status in any way.

**Verdict table:**

| Hypothesis | Status after KT-12 |
|---|---|
| H1 | Sub-question PASS (independent geometric distinction found); full claim untested |
| H2 | OPEN — not attempted |
| H3 | OPEN — not attempted |
| H4 | Downgraded for $t=0,1$ specifically; still the honest default for $n=1,2$ crossings |

**Recommended next action (cheapest first):** build the explicit
Killing-spinor equation for $\nabla^t$ on $S^3$ (reusing Agricola's Theorem
4.2 apparatus, already partially used by E2) and check it directly at
$t=0,1$ — H1's actual claim, not yet tested. Until then, do not cite
"$t=0,1$ are physically selected" anywhere — only "independently
geometrically distinguished (Cartan–Schouten flat connections), a
necessary but not sufficient condition for H1."

### Recomposition (2026-07-17, same day, accepted) — H1 splits into three distinct claims, one of them PROVED

A follow-up review correctly identified that "H1 (Killing spinor)" as
originally frozen conflated three logically distinct claims. Verified
independently before accepting (re-derived $F'(t)$ below directly in sympy;
the holonomy argument itself is a standard theorem, checked for gaps —
none found, since $S^3$ simply-connected kills any $\mathbb{Z}_2$ spin-lift
ambiguity outright). Full derivation in
`experiments/20260717-round72-e7-t-selection-principle/decision.md`.

- **H1a (ordinary Riemannian Killing spinor selects $t$): REFUTED as a
  selector.** Round $S^3$'s Killing spinors exist w.r.t. Levi-Civita
  ($t=1/2$) regardless of the $\nabla^t$ family — this criterion cannot
  distinguish $t=0,1$ from anything else. Wrong formalization of H1 from
  the start.
- **H1b ($\nabla^t$-parallel spinor $\Rightarrow$ zero mode of $D^t$):
  PROVED, not merely supported.** Chain: $R^t=0$ at $t=0,1$ (already
  established) $\Rightarrow$ $\nabla^t$ metric-compatible for every $t$
  (general fact for the canonical family) $\Rightarrow$ flat +
  metric-compatible + $S^3$ simply-connected ($\pi_1=0$) $\Rightarrow$
  trivial holonomy in both $\mathrm{SO}(3)$ and its $\mathrm{Spin}(3)$ lift
  (standard holonomy theorem — no monodromy obstruction since there is no
  nontrivial loop at all) $\Rightarrow$ global $\nabla^t$-parallel spinor
  exists at $t=0,1$ $\Rightarrow$ $D^t\psi=\sum_ie_i\cdot\nabla^t_{e_i}\psi=0$
  **identically** for that spinor, by definition of $D^t$ as the Dirac
  operator of $\nabla^t$. The $n=0$ crossings are therefore a **structural
  consequence**, not a spectral coincidence.
- **H1c (physics selects one of $\{0,1\}$): OPEN, unchanged.** Flatness
  picks the *pair* $\{0,1\}$ (opposite-sign torsion, Cartan–Schouten
  $(\mp)$-connections) symmetrically; distinguishing one requires an
  additional, $t\leftrightarrow1-t$-asymmetric physical input (orientation/flux
  sign, SUSY equation, parent-theory chirality convention, boundary
  condition) not present in the purely geometric argument.

**E8 gate registered (preliminary analytic test done, not a full
experiment):** does an independently-motivated action select $t=0$ or $t=1$
(H2)? For the simplest candidate $F(t)=a|R^t|^2+b|T^t|^2$
($|R^t|^2\propto t^2(t-1)^2$, $|T^t|^2\propto(2t-1)^2$):
$F'(t)=2(2t-1)[aA\,t(t-1)+2bB]$ — **re-derived and confirmed in sympy this
session**, giving $F'(0)=-4bB$, $F'(1)=4bB$, $F'(1/2)=0$ exactly. $t=1/2$ is
*always* stationary; $t=0,1$ are stationary only if $b=0$ (the torsion-energy
term is dropped by hand) or under special cancellation. **Preliminary
status: `BLOCKED/UNDERDETERMINED`** — no parent action is frozen, and a
generic curvature+torsion functional does not robustly select $t=0,1$.
PASS/FAIL criteria for a future full E8 recorded in the experiment's own
`decision.md`.

**Updated summary:**
```text
Flatness selector: PROVED for t=0,1.
Torsion-parallel spinor existence: PROVED for t=0,1 (simply-connected holonomy).
Zero mode of matching Dirac operator: PROVED.
Ordinary Killing-spinor criterion (H1a): REFUTED as selector.
Physical selection of one t (H1c): OPEN.
Equations of motion (H2, E8 preliminary): BLOCKED/UNDERDETERMINED.
Anomaly cancellation (H3): OPEN, not attempted.
Higher-mode crossings (n=1,2): UNEXPLAINED, H4 active there.
```
This is a real strengthening: the $n=0$ torsion escape route is no longer
just a supported candidate mechanism — it is a **mathematically explained
Cartan–Schouten zero-mode mechanism**. Still not a physical resolution:
which sign is realized, and why nature would select this deformation over
Levi-Civita at all, remain open (H1c, H2, H3). Does not promote KT-8; does
not touch E3's own scope caveat; does not explain the $n=1,2$ crossings.

---

## E9 (2026-07-17) — direct construction of the parallel spinor (mechanical verification of H1b)

**Origin:** H1b's recomposition (above) argued via an abstract holonomy
theorem that a global $\nabla^t$-parallel spinor exists at $t=0,1$. This
experiment (`experiments/20260717-round73-e9-explicit-parallel-spinor/`)
builds it explicitly rather than resting on the abstract argument alone.

**Result — `PASS_T0_ONLY__T1_NAIVE_ANSATZ_FAILS_PARTIAL`.** Derived the
explicit spin connection $\Omega_i(t)=(1/4)\sum\Gamma^k_{ij}(t)Z_j Z_k$ from
$\nabla^t_XY=t[X,Y]$ directly (not assumed) and found, exactly,
$\Omega_i(t)=-(tc/2)Z_i$ — independently re-verified this session in sympy.
Cross-check: $\sum_i Z_i\Omega_i(t)=t\cdot H$ matches E2's own Kostant element
$H$ exactly, a non-circular confirmation.

**$t=0$: clean PASS, no caveats.** $\Omega_i(0)=0$ for all $i$
(re-verified), so any constant left-invariant spinor is exactly
$\nabla^0$-parallel, and substituting into Agricola's $D^t$ formula gives
$D^0\psi=0$ exactly — a direct, mechanical confirmation of H1b at $t=0$, not
merely an application of the abstract theorem.

**$t=1$: honest PARTIAL, not forced.** The same left-invariant ansatz gives
**only** the trivial solution $\psi=0$ at $t=1$ — independently re-verified
this session (`sympy.solve` reproduced exactly: solving
$\Omega_i(1)\psi=0$ for all $i$ gives $\psi=0$ only). This does **not**
contradict H1b's abstract argument for $t=1$: the left-invariant frame
itself is $\nabla^t$-parallel only at $t=0$ ($\Gamma^k_{ij}(t)=0$ iff
$t=0$, shown to be the unique root), while at $t=1$ the connection is still
flat as an operator but the natural parallel trivialization is plausibly the
**right**-invariant frame instead (the classical left/right duality of the
two Cartan–Schouten connections) — **not constructed here**, flagged
`[INFERRED, NOT verified]`, a well-scoped, cheap-ish follow-up.

**What this does and does not mean:** strengthens $t=0$'s zero mode from
"proved via general theorem" to "proved via general theorem **and**
explicitly exhibited." Does not claim $t=1$'s parallel spinor fails to
exist — only that this project's established left-invariant convention does
not realize it; H1b's abstract argument for $t=1$ is untouched. Does not
touch H1c/H2/H3, does not promote E2/E3, does not resolve the $n=1,2$
crossings.

**Follow-up (not attempted):** construct the explicit right-invariant frame
for $S^3=\mathrm{SU}(2)$ and repeat this same check at $t=1$ to complete
the symmetric picture — would require introducing group-coordinate
machinery (Euler angles or the exponential map) not previously used in this
line of work.

---

## E10 (2026-07-17) — does an existing convention link S³'s torsion sign (H1c) to S⁶'s already-fixed chirality?

**Origin:** H1c (which of $t=0,1$ is physically realized) remains open;
this project already fixes SM chirality via a single discrete input (S⁶'s
orientation, `preprint.tex:889-891`: "the chirality of the weak interaction
is fixed by the orientation of $S^6$ ... no additional discrete inputs are
required"). Explored whether an analogous, already-implicit consistency
requirement links S³'s torsion sign to this.

**Result (`experiments/20260717-round74-e10-chirality-sign-link/`) —
`OPEN` on all three sub-questions, honest negative, verified.** (1) Product
orientability: both S³ and S⁶ are simply connected, so the product spin
structure is unique regardless of either factor's orientation — no link
possible via this route (consistent with `preprint.tex:889-891`'s own "no
additional discrete inputs" statement, independently spot-checked, exact
match). (2) Chirality-matching: **structurally blocked** by this project's
own KT-8/E3 result — the product-decoupling identity's cross-term
cancellation depends *only* on the S⁶ factor's chirality operator
(`preprint.tex:1479-1482`, spot-checked, exact match), so $t$ cannot touch
the chirality grading at all. (3) No existing S³ orientation convention is
fixed anywhere in the paper. One **[SPECULATIVE]** synthesis was flagged
(not an existing convention, not a PASS): a possible correspondence between
$t=0/1$'s left/right-invariant parallelization (E9) and the
$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ gauge identification already used
for S³'s isometry group — requires two unverified steps, named as a cheap
future test, not pursued further here.

---

## E11 (2026-07-17) — is the existing Freund-Rubin flux on S³ the physical source of the torsion parameter $t$?

**Origin:** `preprint.tex`'s own Modulus Stabilization section already uses
a Freund-Rubin 3-form flux on S³ (`V_{\mathrm{flux}}\propto C^3/\rho_6^{12}$,
line 987). Since $S^3$'s torsion $T^t$ is itself structurally a 3-form
(the only invariant one, as $\dim\Lambda^3(\mathbb{R}^3)^*=1$), explored
whether the two are — or could naturally be — the same object.

**Result (`experiments/20260717-round75-e11-freund-rubin-torsion-link/`) —
mixed, no overreach.** **Q1 (dimension-forced structural match): PASS,
but near-tautological** — verified $T^t(e_i,e_j,e_k)=(2t-1)c$ times the
same Levi-Civita/volume symbol the flux's own magnitude traces to; since
$\dim(S^3)=3$ forces any invariant 3-form to be a multiple of the same
generator, this is close to automatic, not by itself informative. **Q2
(flux as physical torsion source): OPEN** — `preprint.tex` uses the flux
purely as a **scalar** in the potential (spot-checked line 985-989, exact
match: "$V_{\mathrm{flux}}\propto C^3/\rho_6^{12}$" with no 3-form indices
or connection coupling anywhere) — zero wiring currently exists between the
flux and any connection/torsion object; instantiating the standard
NS-NS-flux-sources-contorsion mechanism would require a new normalization
convention not derivable from anything in the paper.

**Q3, status calibration (2026-07-17, accepted) — "FAIL-AS-POSED" was too
strong; split into bosonic vs fermionic sensitivity.** The original finding
(a quadratic bosonic flux-energy functional $V_{\mathrm{flux}}\propto q^2$
is blind to the sign of $q$) is correct and stands as
**`Bosonic flux potential selects sign($q$): FAIL`** — the existing EOM
($dV/d\rho_6=0$) fixes $\rho_6$, not the flux quantum, and a quadratic
functional cannot distinguish $\pm q$ by construction, directly consistent
with E7/KT-12's own E8-gate finding (a torsion-energy term of this type
needs $b=0$ for $t=0,1$ to be stationary at all). **However,** the
*fermionic* sector is not generally bound by this: in the standard
connections-with-skew-torsion literature this project already draws on
(Agricola's own paper, already cited throughout E2/E7/E9, is titled
"...their Dirac operator and homogeneous models in **string theory**"),
the torsionful connection coupling to a Killing spinor is typically
**linear** in the flux, e.g. $\nabla^{\pm}=\nabla^{\mathrm{LC}}\pm\frac18 H$
in one standard normalization — so flipping $\mathrm{sign}(q)$ swaps
$\nabla^+\leftrightarrow\nabla^-$, meaning the fermionic/parallel-spinor
sector **can** distinguish the two torsion signs even where the bosonic
potential cannot. Corrected split:
```text
Bosonic flux potential selects sign(q): FAIL.
Fermionic torsionful connection distinguishes sign(q): PASS structurally.
Full parent theory selects one sign: OPEN.
```
This does **not** establish that heterotic supergravity literally applies
to this project's 13D ansatz — it only shows the general no-go argument
("$q^2$ is blind to sign, therefore no flux mechanism can ever select
$t=0$ or $1$") is false as a *general* claim; the specific bosonic
functional tested by E7's E8-gate remains a real, valid finding for that
functional alone.

**Net effect of E9/E10/E11:** none resolve H1c, H2, or H3. E9 strengthens
$t=0$'s zero mode from abstract to explicitly-constructed; E10 and E11 both
independently and honestly rule out two natural candidate routes to
resolving H1c/H2 using only what already exists in this paper — a
consistency-based selection principle would need genuinely new physical
input, not a repackaging of existing structure.

---

## E9-followup (2026-07-17) — right-invariant frame at $t=1$, completing E9's own flagged next step

**Status calibration (2026-07-17, accepted):** the verdict label below is
retitled from "PARTIAL" to **"PASS geometrically; CONVENTION RECONCILIATION
OPEN."** The literal Pauli-matrix commutator $[Z_1,Z_2]=-2Z_3$ is
`[VERIFIED-tool]` — but this does **not** by itself establish that this
project uses "the wrong sign" for anything physical. The tangent-bundle
structure constant $c_{\mathrm{tan}}$ (in $[e_i,e_j]=c_{\mathrm{tan}}
\epsilon_{ijk}e_k$) and the Clifford-representation matrix commutator sit on
opposite sides of several unreconciled conventions: the Clifford-algebra sign
convention itself, frame orientation, the specific spin-lift map used, the
left-frame$\leftrightarrow$right-frame transition, and a possible
$e_i\mapsto-e_i$ relabeling. Two flat Cartan–Schouten connections with
opposite-sign torsion existing on any Lie group with a bi-invariant metric,
one trivialized by the left-invariant frame and the other by the
right-invariant frame, is the standard, expected structure (Cartan &
Schouten 1926; see also arXiv:0911.1602 on flat metric connections with
antisymmetric torsion) — not a new numerical anomaly. Correct registration:
"literal Pauli commutator: VERIFIED; mapping to tangent structure constants:
UNRECONCILED; physical sign error: NOT ESTABLISHED." See E13 below for the
proposed convention-reconciliation gate.

**Origin:** E9 (above) explicitly left open whether $t=1$'s parallel spinor
lives in the right-invariant frame instead of the left-invariant one used
throughout E2/E7/E9.

**Result (`experiments/20260717-round76-e9followup-right-invariant-frame/`)
— `PASS_MIRROR_NULL__PLUS_EXPLICIT_T1_SPINOR_UNDER_SIGN_CAVEAT`, mixed,
genuinely subtle, no overreach.**

1. **Literal task, mechanically reapplying E9's recipe to the
   right-invariant bracket: clean mirror NULL.** Built explicit left/right
   -invariant vector fields on SU(2) via the concrete unit-quaternion model
   and verified, by direct differentiation, that right-invariant fields
   carry the exact opposite-sign structure constant of the left-invariant
   ones. Mechanically re-deriving $\Omega_i^{\mathrm{right}}(t)$ the same
   way E9 built $\Omega_i^{\mathrm{left}}(t)$ gives the mirror image — and
   at $t=1$ this **still** gives only the trivial solution $\psi=0$. Taken
   alone, this would say E9's hypothesis is not rescued by "the same recipe,
   flipped frame."

2. **Deeper check — does E9's own, already-defined $t=1$ connection (not a
   freshly-built one) make the right-invariant fields fully parallel?
   Yes, exactly.** Expressing the right-invariant field via its honest,
   group-element-dependent adjoint-action coefficients in the left-invariant
   basis and applying E9's *original* Leibniz-extended connection gives
   $\nabla^1 f_i=0$ identically for every $i$ — a genuinely different, and
   stronger, question than (1), and it comes back positive. **Independently
   re-verified this session:** the literal matrix commutator
   $[Z_1,Z_2]=-2Z_3$ for this project's own Clifford generators
   ($Z_i=i\sigma_i$) — confirming the crux discrepancy below directly, not
   just accepting the agent's report.

3. **The crux, previously-invisible discovery: two different notions of
   the structure constant "$c$" disagree in sign.** This project's own
   abstract bookkeeping calibrates $c=+2$ (via the unrelated physics fact
   $h_H=3$), but the literal matrix commutator of the same Clifford
   generators used throughout E2/E7/E9 gives $c_0=-2$ — **confirmed by
   direct computation** ($[Z_1,Z_2]=-2Z_3$, verified independently this
   session). An explicit parallel spinor at $t=1$ ($\psi(x)=\bar g(x)\psi_0$
   on the quaternion model) was found and verified exactly — **but only
   under $c_0=-2$; the identical candidate demonstrably fails under this
   project's own calibrated $c=+2$.**

**What this does and does not mean:** does **not** affect E2/E7's own
headline results (the $t=0,1$ crossing values and $R^t=0$ flatness hold for
generic/symbolic $c$, regardless of sign — E7's own claim.md already states
this explicitly). Does **not** resolve H1c/H2/H3. **Does** mean: an
explicit $t=1$ parallel spinor should not be cited without stating which
sign convention it uses — "an explicit parallel spinor exists for $t=1$ in
the sign convention matching the concrete Clifford realization directly; it
has not been shown to exist, and by this same computation demonstrably
fails as tested, in this project's own calibrated sign." A different
candidate spinor under $c=+2$ was not tried and remains a cheap open
follow-up.

**Two pearl-registry candidates flagged (not yet promoted):** (1) a
"frame-recipe-reapplication trap" — mechanically reapplying a
connection-defining recipe to a new frame does not, in general, reproduce
an already-defined connection's restriction to that frame; these can be
different connections sharing the same formula pattern. (2) the abstract-c-
vs-concrete-$c_0$ sign gap itself, as a standing caveat for any future
computation in this line of work that mixes symbolic structure-constant
bookkeeping with an actual concrete matrix/manifold realization.

---

## E10-followup (2026-07-17) — testing the speculative $\mathrm{SU}(2)_{L,R}$ correspondence flagged by E10

**Status calibration (2026-07-17, accepted):** split into two separate
claims with different confidence. The **mathematical transformation
pattern** (constant spinor in the left-invariant trivialization is invariant
under left translations and transforms as a genuine spinor under right
translations, with the roles exchanged in the right-invariant
trivialization) is `SUPPORTED / likely provable` as a clean theorem once
conventions are fixed — expected: $\ker D^{t=0}\sim(\mathbf1,\mathbf2)$,
$\ker D^{t=1}\sim(\mathbf2,\mathbf1)$ under $\mathrm{SU}(2)_L\times
\mathrm{SU}(2)_R$ — not a coincidence with the paper's own notation. The
**physical claim** that $(\mathbf2,\mathbf1)$ corresponds to an actual 4D
left-handed weak fermion remains `OPEN`: it requires the full
thirteen-dimensional spinor, its decomposition under both the external and
internal spin groups, an explicit identification of the geometric
$\mathrm{SU}(2)_L$ with the physical weak $\mathrm{SU}(2)_L$, reality/
projection conditions, and the full zero-mode space — none of which is
established. Additionally: E10's own claim that S⁶'s orientation
"structurally cannot" influence $t$ is correct **only within the frozen,
decoupled product-operator ansatz** — in an as-yet-unknown parent theory,
fluxes, orientations, and torsion signs could in principle be linked by
shared equations of motion (this qualifies, not reverses, E10's finding).

**Result (`experiments/20260717-round77-su2lr-correspondence-test/`) —
`CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT`.**
The representation-theory computation itself is clean and exact:

| | $\mathrm{SU}(2)_L$ (left translation) | $\mathrm{SU}(2)_R$ (right translation) |
|---|---|---|
| $\psi^{(0)}=$ const ($t=0$) | singlet | doublet |
| $\psi^{(1)}(x)=\bar g(x)\psi_0$ ($t=1$, only under $c_0=-2$) | doublet | singlet |

Cross-referenced against this project's own conventions
(spot-checked, exact): `preprint.tex:332` states
"$\mathrm{SU}(2)_L$ singlet ... the right-handed neutrino $\nu_R$" (i.e.
$\mathrm{SU}(2)_L$ doublet $\leftrightarrow$ left-handed, singlet
$\leftrightarrow$ right-handed, standard SM convention) — $\psi^{(1)}$'s
$\mathrm{SU}(2)_L$-doublet content matches exactly what this project
independently calls "left-handed."

**Reported as `SPECULATIVE-ONLY`, explicitly not a PASS — three
independent, unresolved assumptions are stacked:**
1. `preprint.tex` never states $\mathrm{SU}(2)_L=$ left-translation
   specifically (confirmed by direct search) — reversing this convention
   flips every label in the table above.
2. $\psi^{(1)}$ only exists under $c_0=-2$; the E9-followup above already
   showed it fails under this project's own calibrated $c=+2$.
3. No physical principle requires an S³-factor mode to match S⁶'s
   chirality label at all — and per KT-8, no zero mode of the full 9D
   operator currently exists in the round, untwisted ansatz actually used;
   the entire $t=0,1$ torsion family remains "physically unmotivated, not
   a resolution" (the item above).

**Net effect:** a clean, internally-consistent, but convention-dependent
representation-theoretic pattern, recorded for future reference — does not
promote H1c, KT-8, or any preprint.tex claim.

---

## KT-13 / E12 (2026-07-17) — full-kernel multiplicity gate

**Origin:** a follow-up review correctly flagged, as priority #1 ahead of
any further work on H1c/H2/H3, that E2's own `claim.md` already recorded
(as an `[INFERRED]` identification device, not a flagged physical concern)
that the $n=0$ level of the round S³ Dirac spectrum has complex
multiplicity 2, not 1 — `dim=(0+1)(0+2)=2`. If real and unresolved, this
means the torsion-escape-route program's zero mode is not one physical
state but a 2-dimensional space, giving 6 internal zero modes across the
3 postulated triality channels, not the needed 3.

**Result (`experiments/20260717-round78-e12-multiplicity-gate/`) —
`FAIL_MULTIPLICITY_2_CONFIRMED__NO_NATURAL_PROJECTION_FOUND`. Real,
unresolved. Independently re-verified this session** (given the
significance, not merely accepted): since $\Omega_i(0)=0$ identically for
*every* $i$ (already established, this session, independent of $\psi$),
$D^0\psi=\sum_iZ_i\cdot Z_i(\psi)+0=0$ holds trivially for the **entire**
2-dimensional space of constant spinors $(a,b)$, not a single vector — this
follows immediately from what was already verified, not a new subtle
computation, and confirms the crux number directly.

**Two independent routes (both tool-verified in the experiment):**
Peter–Weyl representation theory (spin-$j$ angular-momentum matrices,
$j=0$ level: eigenvalue $+3/2$, multiplicity 2 exactly) and direct
symbolic reconstruction (the full generic constant-spinor family at $t=0$,
and the full generic $\psi(x)=\bar g(x)\psi_0$ family at $t=1$ under
$c_0=-2$) agree exactly. The tensor-product kernel identity
$\ker(D_{\mathrm{full}})=\ker(D_{S^3,t})\otimes\ker(D_{S^6,S^-})$ for a
decoupled sum-of-squares operator was grounded in an explicit toy
computation, not just asserted algebra.

$$\dim\ker(D_{S^3,t=0\text{ or }1})=2,\quad \dim\ker(D_{S^6,\mathrm{twisted}})=1
\text{ (G74A)}\implies\dim\ker(D_{\mathrm{full}})=2\text{ per channel},
\quad 3\times2=6\text{ total},\quad\text{not }3.$$

**Three possible reductions investigated, none found to resolve it (not
forced):** (1) no Majorana/reality/Weyl condition exists anywhere in
`preprint.tex`'s spinor content that could halve this. (2) The kernel is
confirmed (reusing E10-followup) to be one irreducible $\mathrm{SU}(2)$
doublet, not unstructured — but `preprint.tex:292-298`'s own existing "one
generation = 32 states" convention requires the **full** 4-component
$(\mathbf2,\mathbf1)\oplus(\mathbf1,\mathbf2)$ SO(4) representation
simultaneously, at *every* KK level, regardless of any $\ker(D_{S3,t})$ —
whether "one doublet = one generation slot" is even a valid re-reading of
that convention is **not settled anywhere in this project**; concluding it
resolves the excess would be exactly the kind of manufactured resolution
this experiment was told not to produce. (3) No existing orbifold/
projection result in this project (G27, G31) targets this specific object.

**What this does and does not mean:** does **not** invalidate E7's
flatness result or E9/E10's explicit parallel-spinor constructions as
mathematical facts about $\ker(D^t)$ — those stand exactly as established.
**Does** kill the implicit treatment, throughout E2/E3/E7/E9/E9-followup,
of "the $t=0$ (or $t=1)$ constant spinor" as a single physical zero mode —
it is a genuine 2-dimensional space. Does not touch G74A's own S⁶-side
result. **Recommended prerequisite, before any further H1c/H2/H3 work:**
determine whether `preprint.tex`'s "32-states = one generation" convention
and the torsion-crossing kernel-dimension count are talking about the same
object at all — this project has not yet asked, let alone answered, that
question.

---

## KT-13 follow-up (2026-07-17) — attempting to reconcile the multiplicity excess

**Origin:** at the user's request, attempted the first item of KT-13/E12's
own Relaxation Map: reconcile the existing "32 states = one generation +
CPT conjugates" convention with the newly-found 2-dimensional torsion
kernel, before proceeding to any further gates.

**Result (`experiments/20260717-round79-multiplicity-reconciliation-attempt/`)
— `STRUCTURAL_A_CONFIRMED__B_REFUTED__PHYSICAL_MECHANISM_STILL_OPEN`.**

**A genuine, non-manufactured structural match found and independently
verified this session:** `experiments/20260615-g6-s3xs6-spinor-content/
g6_spinor_decomposition.py` — an experiment dated **2026-06-15, one month
before today's torsion-deformation program existed** — already splits the
S³-side 4-component representation into two 2-dimensional chirality blocks:
`chir_s3="+"` ($T_{3L}=\pm\tfrac12,T_{3R}=0$ — $\mathrm{SU}(2)_L$
doublet/$\mathrm{SU}(2)_R$ singlet) and `chir_s3="-"`
($T_{3L}=0,T_{3R}=\pm\tfrac12$ — $\mathrm{SU}(2)_R$ doublet/
$\mathrm{SU}(2)_L$ singlet) — **verified directly this session, exact
match, source code lines cited.** This is exactly E10-followup's $t=1$ and
$t=0$ kernels respectively. Because G6 predates the torsion program
entirely, this correspondence was not built to order.

**Reading (a), structural half: CONFIRMED.** The kernel structure found
today is not new or arbitrary — it reproduces a chirality split this
project already used, independently, a month ago.

**Reading (a), physical half: still OPEN.** Nothing establishes *why* the
S³ connection would need two different torsion values ($t=0$ **and** $t=1$)
simultaneously in different chirality sectors — this project's own text
(`preprint.tex`) already states there is no physical principle for
selecting even *one* crossing value over $t=1/2$; a simultaneous,
sector-dependent pair is a strictly larger, currently unmotivated
postulate.

**Reading (b): REFUTED, not merely unsupported.** All 8 checked particle/
antiparticle pairs in G6's own table share the *same* `chir_s3` label —
CPT/antiparticle doubling in this project's own existing bookkeeping is
carried entirely by the S⁶ factor ($B-L$ sign), not the S³ factor.
Relabeling the $\mathrm{SU}(2)$ doublet found today as "particle +
antiparticle" content directly contradicts the project's own existing
table.

**What this does not do:** does not supply the missing physical mechanism
for why both torsion values would be simultaneously realized; does not
reconcile the S³-side count with the S⁶-side/triality-channel counting in
full ($4\times1\times3=12$ vs. the needed 3 vs. G6's own 32); does not
touch H1c or KT-8. **Minor correction surfaced and applied:** KT-13/E12's
own text paraphrased an earlier gate (G7) as claiming the 32-state content
"appears at every $(m,n)$ level" — the actual source states this only for
the lightest level; corrected here.

**Net effect:** the multiplicity excess is now understood to correspond to
a real, previously-known structural pattern (not noise), but remains
physically unresolved — a genuine partial result, not a full reconciliation.

---

### E14 (round80) — $\mathbb{Z}_2$ left-right symmetry search

Per the user's instruction to continue searching for a physical mechanism
after the reconciliation attempt above. Tested whether group inversion
$\iota: g \mapsto g^{-1}$ on $S^3=\mathrm{SU}(2)$ realizes the $t
\leftrightarrow 1-t$ symmetry as a genuine geometric isometry, and whether
this could force both $t=0,1$ to be simultaneously physically present.

**Verdict:** `PASS_GEOMETRIC_Z2_CONFIRMED__PHYSICAL_MECHANISM_STILL_OPEN`
— independently re-run and re-verified by me (`python
e14_z2_left_right_symmetry.py`, matched the agent's own output exactly).

**Geometric result (tool-verified, real strengthening of E7):** $\iota(g)
:=g^{-1}$, concretely $\Phi(x_0,x_1,x_2,x_3)=(x_0,-x_1,-x_2,-x_3)$ on this
project's own quaternion model, is an isometry of the round metric,
exactly realizes group inversion, exchanges left- and right-invariant
frames exactly ($d\iota(Z_i^L)=-Z_i^R$ and vice versa), and — via one new
computed identity (the "cross product of $\mathrm{SO}(3)$-rotated
vectors" identity, verified for all 27 $(i,j,m)$ combinations) — pulls
back the *whole* Cartan-Schouten connection family exactly,
$\iota^*(\nabla^t)=\nabla^{1-t}$ for **all** $t$, not just $t=0,1$ as E7
showed at the curvature-eigenvalue level alone. $\iota$ is
orientation-reversing ($\det J=-1$), has exactly 2 fixed points ($g=\pm1$),
and lies outside the connected $\mathrm{SO}(4)$ this project's gauge group
is built from.

**Physical mechanism: NOT established.** Three readings tried, none closes
the gap in the needed direction:
1. "Same physics, different labels" → argues for *under*-counting (2
   states total, not 4), the wrong direction.
2. "Gauge $\iota$ as an orbifold $S^3/\langle\iota\rangle$" → requires
   $t=1-t$, i.e. $t=1/2$ uniquely — the torsion-free Levi-Civita value
   KT-8 already shows has **no** zero modes. This *collapses* the escape
   route rather than doubling it — a clean, decisive negative sub-result.
3. "Left-Right-symmetric model building requires both doublets" → the
   only reading pointing the right direction, but it is a phenomenological
   *choice*, not a geometric consequence, and sits in unreconciled tension
   with this project's own Lemma L5 (`preprint.tex:884–912`), which derives
   an explicitly *asymmetric* (non-parity-symmetric) chirality result for
   the S⁶ factor.

Grep of `preprint.tex` confirms no existing use of $\iota$ or any S³-side
involution anywhere; the only existing discrete choice is a *different*
$\mathbb{Z}_2$ (S⁶ orientation, Lemma L5), not shown or expected to be
linked to this one.

**Does not resolve:** H1c, KT-8, or E12/E13's 6-vs-3 gap. **Does
establish:** a new, genuine geometric fact (stronger than E7), and rules
out the orbifold-descent reading specifically as a route to the needed
doubling.

---

### E15 (round81) — Chirality-grading check on the S³ doublet

Direct follow-up: does the S³ Clifford volume element $\omega=Z_1Z_2Z_3$
(this project's own $Z_i=i\sigma_i$ convention) split the 2-dimensional
E12 kernel into two 1-dimensional eigenspaces, supplying a natural
"pick one" mechanism?

**Verdict:** `NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE`
— independently re-run and re-verified by me, matched exactly.

$\omega=Z_1Z_2Z_3$ computes to **exactly the $2\times2$ identity matrix**
(the standard Pauli identity $\sigma_x\sigma_y\sigma_z=iI$, confirmed
directly, not merely cited). It is central (commutes with all $Z_i$), has
a single eigenvalue ($+1$, multiplicity 2), and acts as this same scalar
on the full kernel at both $t=0$ and $t=1$ — no splitting at either value.

**This is not a computational accident — it generalizes.** For any
odd-dimensional Clifford algebra ($n=3$ here) the volume element
$e_1\cdots e_n$ is always central, and Schur's lemma forces a central
operator to act as a scalar on any *irreducible* representation. E14
already established the doublet is irreducible under the surviving
$\mathrm{SU}(2)$. **This rules out the entire class of $\mathrm{SU}(2)$-
covariant, S³-internal operators as a source of the needed 2→1
reduction** — not just $\omega$ specifically. A side-check confirmed a
generic degree-1 element does split $\mathbb{C}^2$, but this is
basis-dependent (transforms as a vector under the same $\mathrm{SU}(2)$)
and carries no invariant meaning — reproduces E14's obstruction from an
independent angle, not a counterexample to it.

**Does not touch:** E12's multiplicity finding, E14's result, or
G74A/G74B (S⁶ is even-dimensional — a structurally different case,
untouched here).

---

### Round82 — Multiplicity-gap scope reconciliation

Given E14 and E15 both closed off natural mechanisms without resolving
the gap, the next cheapest test (per E12's own flagged, previously-
unattempted prerequisite) was to check whether the "6 vs 3" excess
actually threatens the *published* $N_{gen}=3$ headline (G73/G74A/G74B) at
all, or is internal only to the separate, exploratory torsion-escape-route
line (E1–E15) patching a *different*, later-discovered gap (KT-8).

**Verdict:** `ORTHOGONAL_EXPLORATORY_LINE` — the multiplicity excess does
**not** threaten the published headline.

**Verified by direct citation, independently spot-checked:**
- G74A's `dim ker = 1 EXACTLY` (`experiments/20260621-g74a-lichnerowicz-gap/decision.md:8-24`)
  is proved for the operator $D_{S^6}\otimes S^-$ — **S⁶-side only**. The
  S³ factor does not appear in G73/G74A/G74B at all (confirmed by reading
  the operator definition directly, not by citing a summary).
- The torsion program exists only because KT-8 (discovered 2026-07-16/17,
  a month **after** G73/G74A/G74B, 2026-06-21) found the *untwisted, full*
  $S^3\times S^6$ product operator has zero kernel — an unrelated question
  from a different discovery date.
- E7, E12, and KT-8's own text each independently already state this
  scoping in their own words (e.g. E12: *"a real, unresolved problem for
  the torsion-escape-route program... G74A's own S⁶-side result... survive
  completely intact"*).
- Checked the public claim surface for leakage: `preprint.tex:1468`
  ("candidate mechanism --- physically unmotivated, not a resolution"),
  confirmed directly by grep — no overclaim found; the torsion route was
  never presented as necessary for $N_{gen}=3$.

**One low-priority completeness gap, not an overclaim:** `preprint.tex`'s
torsion open-problems item does not yet mention the specific 6-vs-3
finding — flagged for a future one-sentence addition, not urgent, since
the existing wording already tells readers not to rely on this route.

**Practical consequence:** continuing to search for a 6→1 (or 6→3)
reduction mechanism remains legitimate research into whether KT-8 can ever
be resolved via this route, but the stakes are lower than E12's own
framing implied — nothing already published or certified is at risk
either way.

---

### E16 (round83) — Joint representation decomposition: is the doublet malignant or benign?

The decisive question round82 left open: does the 2-dimensional
$\ker(D_{S^3,t})\otimes\ker(D_{S^6,\text{twisted}})$ per channel represent
two independent copies of a full generation's gauge content (genuine
doubling, $N_{\rm family}=6$) or the two $T_3$-components of a single
weak-isospin doublet (benign — multiplicity 2 is not a defect)?

**Verdict:** `PASS__ONE_WEAK_ISOSPIN_DOUBLET__NARROW_SCOPE` —
independently re-verified: re-ran the script (identical output), and
directly re-checked the three load-bearing citations myself (G6's
`s3_states` dicts, lines 29–36, carry only `T3L,T3R,chir_s3` — no
SU(3)/B-L field, confirmed by reading the file directly; `bl_charge()`/
`su3_label()` take only the S⁶ weight as argument; `preprint.tex:1533–1536`
states verbatim, in the construction that defines $N_{\rm gen}=3$, "the
$S^3$ spinor factor is a fixed, generation-independent block, and the
generation index lives entirely within the $S^6$/octonion triality
structure").

**The argument, in one line:** since $\ker(D_{S^6,\text{twisted}})$ is
exactly 1-dimensional (G74A), both joint-kernel basis vectors are (their
own $S^3$ vector) $\otimes$ (the SAME single fixed $S^6$ vector) — so any
quantum number that is a property of the $S^6$ factor alone
(triality-channel/SU(3), $B{-}L$, the $\mathrm{sign}(\mathrm{ind})=+1$
chirality of G74B) is necessarily IDENTICAL for both states, while the two
states differ only in $T_3$ (`+1/2` vs. `-1/2`, reconfirmed independently
here on this project's own concrete matrix family) under the one surviving
$\mathrm{SU}(2)$ factor. This is exactly the standard structure of a weak
doublet (e.g. $u_L/d_L$), not two copies of one particle — FAIL (identical
full quantum numbers including $T_3$) is cleanly ruled out, not merely
unconfirmed.

**Scope, stated precisely (per the experiment's own "what this does NOT
mean"):** this resolves only the specific malignant-vs-benign reading of
the multiplicity-2 finding. It does **not** resolve H1c (physical
selection of $t$), does **not** touch KT-8 (whether the untwisted
full-operator zero mode exists at all), and does **not** address whether
the torsion-escape route needs BOTH the $t=0$ and $t=1$ doublets
simultaneously to supply a complete generation's full
$(2,1)\oplus(1,2)$ content (E12 Section E.2 / E14 Reading 3 — still open).
The dimension-2 finding itself (E12/E13) is unchanged; what changes is its
representation-theoretic reading.

---

### Provenance correction (2026-07-17) — G74A's own argument is superseded; the number it not the citation survives

A user critique, independently verified by direct re-reading of
`preprint.tex` (not merely re-checked against the cited experiment file),
found that **E12/round82/round83's repeated citation of "G74A: dim
ker$(D_{S^6}\otimes S^-)=1$ EXACTLY" points to a stale, superseded
argument** — the underlying $\dim\ker=1$ *fact* is correct and still
holds, but `experiments/20260621-g74a-lichnerowicz-gap/decision.md`'s own
two lemmas, taken as literally stated, are **both** now known to be
insufficient/invalid, and the CURRENT `preprint.tex` (§\ref{sec:kernel},
§\ref{sec:lichnerowicz}, §\ref{sec:schur}, lines 649–873) already says so
explicitly, in its own words:

- **G74A's Lemma A** (the "8/45 Lichnerowicz-dominance / safety factor
  5.625" argument) is exactly the naive bound `preprint.tex:685–688`
  itself flags as broken: *"A uniform lower bound $R/4+F_{S^-}>0$... would
  force $\ker(D\otimes S^-)=0$ — contradicting $\mathrm{ind}=1\neq0$."*
  This is labeled **L4A, an open problem**, not a result — the opposite of
  G74A's own "PROMOTE" framing.
- **G74A's Lemma B** (G₂-equivariance + Schur's lemma "pins" $\dim\ker\leq
  1$) is also directly contradicted by the current text
  (`preprint.tex:815–819`): the trivial $G_2$-representation appears with
  multiplicity **2**, not 1, in the relevant fibre, and *"Schur's lemma
  only forces $D^+|_{\mathbf1}$ to be some linear map on this 2-dimensional
  space — it does not fix which one."* Settling rank 0 vs. 1 requires
  explicit computation, not Schur's lemma alone.

**What actually establishes $\dim\ker=1$ EXACTLY, per the current,
authoritative `preprint.tex`:** an explicit, later computation —
`experiments/20260708-dolan-casimir-g2su3` (2026-07-08) and
`experiments/20260714-round59-trivial-rank-certification` (2026-07-14),
**both post-dating G74A** (2026-06-21) — constructs the Levi-Civita
twisted Dirac operator directly and diagonalizes it, giving
$\mathrm{rank}(D^+|_{\mathbf1})=1$ by three mutually-reinforcing routes
(independent reimplementation, full-fibre completeness audit, closed-form
analytic derivation from the Killing-spinor eigenvalue), status
`[VERIFIED-INDEPENDENT-INTERNAL]`, external review outstanding.

**Net effect:** every load-bearing use of "$\dim\ker(D_{S^6}\otimes
S^-)=1$" in E12/round82/round83 above is **unaffected in substance** —
the number is correct, and round82's core verdict (the S³ multiplicity gap
does not threaten the published headline) and round83's core verdict (the
doublet is benign, not two family copies) both survive unchanged, since
neither depended on *which specific argument* proves $\dim\ker=1$, only on
the fact that it equals 1. What changes is citation accuracy only: future
citations of this fact should point to
`dolan-casimir-g2su3`+`round59` (or simply "L4B, internally certified,
external review outstanding" as `preprint.tex` itself now says), not to
G74A's decision.md, whose own two lemmas are superseded. A superseding note
has been added to `experiments/20260621-g74a-lichnerowicz-gap/decision.md`
itself (history preserved, not rewritten) to prevent this stale citation
from recurring in future sessions.

---

### Round84 (convention table, labeled "E13" per the user's original plan — do not confuse with round79's internal script name) — Convention reconciliation

Six recurring sign/orientation/labeling ambiguities, flagged across E9/E10/
E11/E12/E14/E15/E16, reconciled into one table
(`experiments/20260717-round84-e13-convention-reconciliation-table/CONVENTION_TABLE.md`),
independently spot-checked (grep counts on `preprint.tex` for
"$\mathrm{SU}(2)_L$"/"$\mathrm{SU}(2)_R$"/"left-invariant"/"right-invariant"
matched exactly: 12/9/0/0).

**Verdict:** `PASS_5_OF_6_RECONCILED__1_CONFIRMED_AMBIGUOUS`.

| # | Topic | Status |
|---|---|---|
| 1 | $S^3$ orientation | FIXED (implicit, by universal reuse of $\{Z_i=i\sigma_i\}$) |
| 2 | Structure-constant sign ($c=+2$ abstract vs. $c_0=-2$ concrete) | CONVENTION CHOICE, both valid — rule: use $c_0=-2$ for any concrete directional-derivative computation, $c=+2$ only for scalar Kostant-calibration bookkeeping |
| 3 | Clifford convention $Z_i=i\sigma_i$ | FIXED — byte-identical across all 8 scripts (E2/E9/E10/E11/E12/E14/E15/E16) |
| 4 | Spin lift $\Omega_i(t)=-(tc/2)Z_i$ | FIXED formula; numeric substitution governed by item 2 |
| 5 | $t=0/t=1$ ↔ left/right-invariant | FIXED for $t=0$ unconditionally; $t=1$ correspondence established **only** under $c_0=-2$ |
| 6 | $\mathrm{SU}(2)_L/\mathrm{SU}(2)_R$ geometric identification | **AMBIGUOUS — confirmed genuinely unresolvable** from existing project text (0 hits for "left-invariant"/"right-invariant"/"translation" anywhere in `preprint.tex`) |

**Recommendation applied to E17 (below):** test both labeling conventions
explicitly rather than assuming one, since item 6 cannot be closed from
existing text.

---

### Round85 (E17) — $t=0/t=1$ sector-coexistence gate

The decisive remaining question in the E12→E16 chain: does the physical
construction need BOTH the $t=0$ and $t=1$ torsion sectors simultaneously
to supply one full generation's $(2,1)\oplus(1,2)$ content, or is this
undetermined without deeper input?

**Verdict:** `BLOCKED__REPRESENTATION_CONTENT_CONSISTENT__PHYSICAL_COEXISTENCE_UNDECIDABLE_WITHOUT_PARENT_ACTION`
— independently spot-checked (`preprint.tex:291–298`, `g6_spinor_decomposition.py:29-36`
both confirmed exactly as cited).

**Positive, necessary-condition finding:** under BOTH tried
$\mathrm{SU}(2)_L/R$ labelings (per round84's mandate — the ambiguity from
item 6 does not affect this part), $\ker D^{t=0}$ and $\ker D^{t=1}$ are
convention-independently the mirror pair $\{(1,2),(2,1)\}$ — never two
copies of the same piece. Their union would reproduce exactly the 4-state
$S^3$-side content `preprint.tex:291–292` already requires ("4-component
$\mathrm{SO}(4)$ spinor representation"), matching G6's own pre-existing
4-state table (2×$(2,1)$+2×$(1,2)$), with **no double-counting** against
the "32 states + CPT conjugates" convention (`preprint.tex:296–298`) —
CPT doubling is carried entirely by the S⁶ factor (E13/round79), an
orthogonal axis untouched by this question.

**What remains genuinely undecidable:** whether both sectors actually
coexist physically (sufficient condition), as opposed to being two
mutually exclusive values of one connection parameter on one $S^3$ factor.
E14's three tried mechanisms all still fail to force coexistence (Reading
1: under-counting; Reading 2: collapses to $t=1/2$, killed by KT-8;
Reading 3: unadopted phenomenological choice, in tension with Lemma L5's
asymmetric chirality). E11/round75's Freund-Rubin exploration found no
flux-torsion coupling that could settle this either way. **The missing
ingredient is identified precisely: a stated 13D parent action specifying
how many independent Dirac fields/connections the compactification
actually contains** — nothing short of that closes this gate.

**Net status of the full torsion-escape-route investigation (E1→E17, this
session) — calibrated (2026-07-17, per user review):** "the mechanism is
proved" is too broad a claim; the honest three-part status is:

```
Mathematical torsion-escape mechanism (Cartan-Schouten flatness,
ker D_{S3}^{t=0,1} != 0):          PROVED, within the frozen product ansatz.
Representation content
(one SU(2) doublet per sector,
(1,2)+(2,1) mirror pair, no
double-counting vs. the 32-state
convention):                        CONSISTENT, internally verified.
Physical realization (does the
theory actually contain/select
t=0, t=1, or both):                 BLOCKED — needs a parent action.
```

This entire line remains, as established in round82, **orthogonal to and
non-threatening of** the already-published $G73$/$G74A$/$G74B$
$N_{\mathrm{gen}}=3$ headline. The corrected provenance for that headline's
own exact-kernel step (per the G74A correction above) is stated precisely
as: **the scientific conclusion ($\dim\ker=1$) SURVIVES, certified through
`round59`; G74A's own original proof route (Lemma A + Lemma B) is
SUPERSEDED/invalid as stated** — the result and its proof are not the same
thing, and only the latter needed replacing.

**Updated claim ledger (E1→E17, this session):**

| Claim | Status |
|---|---|
| $S^6$ index $=1$ | `PROVED` (G73) |
| Local $S^6$ kernel $=(1,0)$ | `INTERNALLY CERTIFIED` — Round59 (survives; G74A's own proof route superseded) |
| Baseline (untwisted, Levi-Civita) full $S^3\times S^6$ kernel | `REFUTED` — KT-8 |
| Torsion ($t=0,1$) produces $S^3$ zero modes | `PROVED` — E2/E7/E9 |
| Multiplicity 2 = two generations | `REFUTED` — E16 |
| Multiplicity 2 = one $\mathrm{SU}(2)$ doublet | `PASS` — narrow, factorized scope (E16) |
| $t=0,1$ give the mirror $(1,2)/(2,1)$ pair | `PASS` — up to $L/R$ labeling (E17) |
| Both sectors physically coexist | `BLOCKED` — needs parent action (E17) |
| Gauge $\mathrm{SU}(2)_L/R$ derived from geometry | `OPEN` — round84 |
| Physical $N_{\mathrm{gen}}=3$ | `BLOCKED` |

**Bottom line:** the representation-content problem this sub-investigation
set out to resolve is closed; the coexistence problem has been reduced,
precisely, to the absence of a stated parent action — the chain E1→E17 is
**executed, not "fully closed"**; its final state is an exact `BLOCKED` at
the parent-action level, not an open-ended unknown.

---

### Round86 (E18) — Parent-action discriminator

Frozen claim: does a single action/field construction exist in which
$t=0$ and $t=1$ arise as two NECESSARY left/right sectors (not two
mutually exclusive values of one free parameter)? PASS required producing
one of three concrete constructions (a physically-derived two-sector
Hilbert space; two parity-related connections $\nabla_L,\nabla_R$ with an
action and equations of motion; a single sign-selecting dynamical/
topological field) with an action, fields, symmetry, EOMs, and an
explanation for *why* both sectors are present, with no manual doubling.

**Verdict:** `BLOCKED__NO_PARENT_ACTION_FOUND_IN_PROJECT_OR_CITED_LITERATURE__MISSING_INGREDIENT_NAMED`
— independently spot-checked (`preprint.tex:408–409`, and AHL2023
Corollary 3.14/p.48 via direct PDF text extraction) both confirmed exactly
as cited.

**Literature check (this project's own three cited geometry references,
searched systematically, not merely re-cited):** Agricola 2002 (the
literal source of this project's $\nabla^t$ family) studies $t$ pointwise
throughout — $t=1$ even has its own name ("anticanonical connection,"
p.5, sharing $t=0$'s Ricci tensor) but is never combined with $t=0$ into
one joint object anywhere in the paper. Agricola-Hofmann-Lawn 2023
contains the single closest analogue found — a genuine, structurally
motivated PAIR of Killing spinors on round $S^3=\mathrm{SU}(2)$
(eigenvalues $\pm1/2$, Corollary 3.14) — but this is a different
mathematical object (one Levi-Civita connection, split by Killing
*eigenvalue* sign) from this project's $t=0/t=1$ question (two different
*connections*, both torsionful); conflating them would repeat exactly the
kind of symbol-overload error this project's own methodology is designed
to catch. Charbonneau-Harland 2016 (nearly-Kähler instanton rigidity on
$S^6$) contains no relevant construction at all.

**This project's own prior work re-examined for the same purpose:**
E11/round75's Freund-Rubin flux potential remains quadratic in the flux
quantum (blind to sign, candidate 3 fails); `preprint.tex`'s one
"left-right symmetry of $S^3$" mention (line 409) is a phenomenological
gauge-coupling-equality assumption for the Weinberg-angle formula, with
zero cross-reference to the torsion question anywhere in the paper
(candidate 2 fails) — independently reconfirming E14/E17's own prior
identification of this exact reading.

**Why BLOCKED, not FAIL** (a distinction the experiment itself argues for
carefully): this is an absence-of-evidence result — a systematic search of
the sources actually available to this project — not a proof that no such
construction CAN exist. The missing ingredient is precisely nameable:
`preprint.tex:1370–1419` (item KT-1) already flags the SAME class of gap
("no parent action identified") for the structurally analogous S⁶-twist
question, and separately notes that Nahm's theorem caps standard
supergravity at 11 dimensions, so a literal 13D parent action "is not
available off the shelf" — this is a substantial, named missing
ingredient, not an unlooked-up citation.

**Pearl candidate flagged (project-internal, not registered globally):**
AHL2023's $\pm1/2$ Killing-spinor pair on $S^3$ is a genuine coexisting
structure on the exact manifold this project studies, on the wrong
parameter axis. IF the standard cone-construction correspondence between
Killing spinors on $S^n$ and parallel spinors on the flat cone $C(S^n)$
could be shown to relate this $\lambda=\pm1/2$ split to the project's
$t=0/1$ split, it might supply exactly candidate 1 — flagged
`[CANDIDATE]`, impact ~4, not adopted, `next_check`: if the
torsion-escape-route program is revisited.

**This closes the E1→E18 chain for this session** with the parent-action
question left open exactly as precisely as it can be stated: not "we
don't know," but "here is exactly what's missing, and here is confirmation
it isn't sitting unread in this project's own already-cited sources."

---

### Round87 — Gates-Hull-Roček bi-Hermitian sigma-model candidate

Per continued instruction to search for a physical parent-action mechanism,
tested the single most concrete external candidate round86's own
Relaxation Map flagged: does the Gates-Hull-Roček (1984) construction —
`(2,2)`-supersymmetric torsionful sigma models requiring two connections
$\nabla^\pm=\nabla^{LC}\pm\tfrac12H$, tied to independent left-/right-moving
worldsheet chiralities — supply the missing action?

**Verdict: `FAIL`** (for this specific candidate only — does not re-open
round86's overall `BLOCKED`). Independently re-verified: downloaded and
grepped `arXiv:1111.0551` (Sevrin-Staessens-Terryn, cites Gates-Hull-Roček
1984 directly) myself; confirmed word-for-word the quote "an
$N=(2,2)$ supersymmetry provided $G$ is an **even-dimensional** reductive
Lie group," and confirmed the paper's only two worked group-manifold
examples are $\mathrm{SU}(2)\times\mathrm{U}(1)$ (4D) and
$\mathrm{SU}(2)\times\mathrm{SU}(2)$ (6D) — standalone $\mathrm{SU}(2)$
(3D, this project's $S^3$) never appears, for an elementary reason: odd-
dimensional manifolds admit no almost-complex structure at all, and the
construction is fundamentally built on one. A second, independent
obstruction: the construction's own reason for needing both signs (closing
$(2,2)$ SUSY on independent left/right *2D worldsheet* sectors) has no
counterpart in this project's spacetime Kaluza-Klein compactification,
which has no worldsheet.

**Net effect:** forecloses an entire class of future candidates (any
generalized-complex-geometry / Hitchin-pair mechanism) for this project's
odd-dimensional factors ($S^3$, and the full 9D $S^3\times S^6$ internal
space) — a genuine, useful negative result, not merely "this one paper
doesn't apply." The remaining most concrete untried path (per the
Relaxation Map) is candidate 3's non-complex-structure route: a direct
Strominger-Hull-system flux/Killing-spinor sign-selection search, not yet
attempted beyond this project's own citations.

---

### Round88 — Strominger-Hull flux sign-selection (two sub-questions)

Pursued round86/87's flagged remaining path directly. Split into two
distinct questions: **A** (does flux/level quantization SELECT one sign of
`t`, resolving H1c?) and **B** (does anything require BOTH signs to
COEXIST, the original parent-action question?).

**Structural check first (per round87's precedent):** the classical
Strominger-Hull system requires a 6-real-dimensional, $\mathrm{SU}(3)$-
structure manifold — confirmed via Fiset's PhD thesis (arXiv:1909.07936,
`[Hul86b, Str86]` cited directly) plus independent WebSearch corroboration
across 3 modern papers. $S^3$ (3D, odd) cannot carry an almost-complex
structure at all (elementary fact: $J^2=-1$ requires even dimension) — the
classical system does not apply, for the identical class of reason
round87 found for Gates-Hull-Roček. This forces an explicit pivot to
$\mathrm{SU}(2)_k$ WZW-model / general $(1,1)$-sigma-model-with-torsion
literature, confirmed as the structurally correct target via Hull's own
statement (arXiv:hep-th/9610103): "WZW-models on even dimensional groups
are particular examples of $(2,2)$ σ-models" — independently re-verified
by me directly from the downloaded PDF, word for word, line 303.

**Verdict A:** `FAIL__UNITARITY_BOUND_IS_ORIENTATION_RELATIVE_NOT_AN_ABSOLUTE_SELECTION`.
The WZW level bound $k\in\mathbb{Z}_{>0}$ (unitarity, a real, tool-verified
Kac-Moody representation-theory derivation) looked promising, but three
converging facts show it selects nothing absolute: the level's sign is
tied to a free choice of orientation of the 3-manifold extension of the
Wess-Zumino term; reversing orientation is compensated by $g\mapsto g^{-1}$
(exactly this project's own $\iota$); and $k<0$ is explicitly "definable,
just non-unitary" in that convention, not physically excluded. This is
structurally the SAME unresolved convention this project's own
`CONVENTION_TABLE.md` (row 1, $S^3$ orientation) already flags — using it
to claim a physical selection of $t=0$ over $t=1$ would repeat exactly the
"condition without stated condition" error this project's own methodology
is designed to catch.

**Verdict B:** `FAIL__WORLDSHEET_CHIRALITY_MECHANISM_DOES_NOT_TRANSFER_TO_SPACETIME_KK_COMPACTIFICATION__BROADER_AND_CLEANER_THAN_ROUND87`.
A genuinely new finding: the base $(1,1)$-SUSY sigma-model-with-torsion
(NOT the $(2,2)$/Gates-Hull-Roček system round87 already ruled out) —
independently verified via direct extraction of Hull's arXiv:hep-th/9610103
(eq. 3.1-3.3) — has NO complex-structure or even-dimension requirement, and
genuinely contains BOTH $\nabla^+$ and $\nabla^-=\nabla^{LC}\pm\tfrac12H$
simultaneously in one action, free of round87's dimensional obstruction.
**But** the reason both signs coexist there is that a 2D string worldsheet
has two independent light-cone chiralities ($D_+,D_-$), each assigned one
fermion superpartner of the SAME target-space map — a fact about the
worldsheet $\Sigma$, not about the target manifold in isolation. This
project's $S^3$ is used throughout as a spacetime Kaluza-Klein internal
factor with no 2D string worldsheet anywhere — transferring the argument
would require asserting this compactification secretly has two
independent worldsheet-chirality sectors, which nothing in this project's
framework supports. This closes off a strictly BROADER literature class
than round87 (which needed both an even-dimension AND a chirality
argument; this shows the chirality mismatch alone already suffices, even
without the dimension obstruction).

**Pearl candidate, independently verified on both sides:** E14/round80's
own $\iota:g\mapsto g^{-1}$ (orientation-reversing, exactly 2 fixed points
at $g=\pm1$) has a genuine, independently-tool-verified counterpart in the
WZW-orientifold literature (arXiv:hep-th/0110267, independently re-checked
by me, word for word, lines 418-420): "the standard orientifold symmetry
$g\mapsto g^{-1}$ is a reflection through the axis of rotation with fixed
points at the poles" — the identical map, on the identical manifold, with
the identical fixed-point count and location, there used to compensate
worldsheet parity. Flagged `[CANDIDATE]`, impact ~5, not adopted:
falsifiable next check (not run) — is $\iota$ composed with $t\leftrightarrow1-t$
a genuine symmetry of the full $D_{S^3,t}$ operator or action, reusing
E14's own script infrastructure.

**Net effect:** round86/E18's Relaxation Map item "broaden the literature
search... Strominger-Hull flux-compactification literature" is now
CLOSED — both the classical system and its natural non-complex-structure
generalization fail, for two distinct, precisely-named reasons. Remaining
open paths: a genuinely new parent-action derivation, or pursuing the
$\iota$-composed-with-$t\leftrightarrow1-t$ pearl check.

---

### Round89 — Cone-construction / Killing-spinor pearl (round86's flagged item)

Pursued the pearl round86 flagged but never attempted: does AHL2023's
`S³=SU(2)` Killing-spinor pair ($\lambda=\pm1/2$, Corollary 3.14) connect
to this project's own $t=0/t=1$ parallel-spinor pair via a genuine bridge,
rather than being "the wrong parameter axis" as round86 assumed without
checking?

**Verdict: `PARTIAL_OPPOSITE_SIGN_STRUCTURAL`** — independently re-verified:
re-ran the script (byte-identical output), inspected every field of
`results_e19.json` directly, and re-checked the AHL2023 PDF text myself
(confirmed word-for-word: "the round metric admits a pair of invariant
Killing spinors for **the** constant $1/2$" — singular, same-sign, for the
`n=1` case).

**The bridge is real** (round86's "wrong axis" dismissal was itself an
unchecked assumption): using only this project's own already-established
formulas (E9's spin-lift $\Omega_i(t)=-(tc/2)Z_i$, E7's
$t{=}1/2{=}$Levi-Civita identification), substituting a $\nabla^t$-parallel
spinor into the connection-difference formula gives an EXACT Riemannian
Killing-spinor equation $\nabla^{LC}_X\psi=\lambda(t)\cdot X\cdot\psi$ with
$\lambda(t)=(c/2)(t-1/2)$ — freshly derived and tool-verified, not
previously written down anywhere in this project. At this project's own
$c_0=-2$: $\lambda(0)=+1/2$, $\lambda(1)=-1/2$ — an **exact magnitude
match** to AHL2023's stated Killing constant, no rescaling needed.

**But the sign structure is a hard mismatch, not a convention artifact:**
$\lambda(t)=(c/2)(t-1/2)$ forces $\lambda(1)=-\lambda(0)$ identically, for
**every** value of $c$ — this project's $t=0/t=1$ pair is structurally
incapable of being anything but an opposite-sign Killing pair. AHL2023's
own most-specific statement for exactly this case ($S^3=\mathrm{SU}(2)$,
$n=1$, p.48) gives a **same-sign** pair ("the constant $1/2$," singular) —
the opposite structure. It only matches the general Corollary 3.14 wording
("constants $1/2,-1/2$ — or $1/2,1/2$, depending on $n$"), which AHL2023
itself assigns to a different $n$, not $n=1$.

**Net effect:** sharpens, rather than rescues, round86's original
dismissal — not "these look like different objects" (round86's untested
guess) but "the actual bridge, built explicitly, produces an exact
magnitude match and a precise, unavoidable sign mismatch." A genuine new
mathematical fact about this project's own $\nabla^t$ family (promotable
as a pearl) that does **not** narrow E18's parent-action/coexistence gap
— even a full sign-match would only ever have supplied a mathematical
coexistence fact, not the missing physical action. Flagged as a pearl
(impact ~3, project-internal): if the cone-construction bridge itself is
ever built explicitly (still not attempted), check whether it reproduces
the same $\lambda=\pm1/2$ result or resolves the sign mismatch
differently, before assuming the coexistence question is fully closed
either way. Self-caught and reported: a sign bug in a redundant
verification helper (not the substantive derivation), fixed and re-run
before this verdict was reached.

**Calibrated summary of rounds 86–89, stated precisely (per user review,
2026-07-17):** the Cartan-Schouten family on $S^3$ and the torsionful
connections $\nabla^\pm=\nabla^{LC}\pm\tfrac12H$ of two-dimensional
supersymmetric sigma models coincide algebraically after normalization.
This coincidence establishes that the two flat Cartan-Schouten endpoints
admit a standard torsionful-connection interpretation. It does **not**,
however, transfer the sigma-model's reason for retaining both signs: in
the latter, the pair is forced by the two chiral directions of an
external worldsheet. The present Kaluza-Klein construction contains no
such worldsheet or corresponding pair of chiral sectors. Thus the
simultaneous physical inclusion of $t=0$ and $t=1$ remains unmotivated
within the current parent structure. Algebraic match: verified. Geometric
analogy: verified. Mechanism transfer: refuted. Simultaneous $t=0,1$ in
the current KK model: open. A parent string/worldsheet extension remains
a possible NEW theory to build, not a result this project currently has.

---

### Round90 — Pati-Salam gauge-completeness (spacetime-native candidate)

Given rounds 87-89 all failed for the SAME root reason (the "why both
signs" justification lived in an external, string-worldsheet structure
with no counterpart in this project's spacetime KK compactification), this
round tested a genuinely different, **spacetime-native** candidate: does
this project's own commitment to a Pati-Salam-type gauge structure
(`SU(3)_c\times SU(2)_L\times SU(2)_R`) require both `t=0` and `t=1`
content via ordinary gauge-theory consistency (Witten's `SU(2)` global
anomaly — an even number of gauged `SU(2)` doublets required for
consistency), rather than any borrowed string-theoretic mechanism?

**Verdict:** `BLOCKED__SU2R_GAUGING_IS_GENUINE_AND_STRONGER_THAN_PRIOR_ROUNDS_CREDITED__BUT_FULL_SU4xSU2LxSU2R_COMBINATION_IS_SELF-ADMITTED_INCOMPLETE`
— independently spot-checked (`preprint.tex:355–374`, `:305–320`,
`:1586–1601`, all three confirmed exactly as cited).

**The genuine new finding:** `preprint.tex` commits `\mathrm{SU}(2)_R` as
an actual GAUGED 4D symmetry — not merely a `T_{3R}` bookkeeping label —
via the same Kaluza-Klein spin-connection mechanism (Lawrence 2022)
already used for `\mathrm{SU}(2)_L` and `\mathrm{SU}(3)_c`, reinforced by
an actual computed gauge-kinetic term from the spectral action
($g_2^2\propto 1/\mathrm{Vol}(S^3)$, giving the coupling-ratio prediction
already in the paper) and a Higgs-bidoublet assignment under
$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$. **This is a materially
stronger and earlier claim than the narrow $g_{2R}=g_{2L}$ coupling-VALUE
assumption** that rounds 86/E17 already correctly found insufficient —
the gauging commitment itself is independent of, and prior to, that later
numerical assumption. Grounded externally via Wikipedia's Pati-Salam
summary and, more rigorously, Witten's independent 1982 `SU(2)` global
anomaly (an odd number of gauged `SU(2)` doublets is mathematically
inconsistent) — a gauged $\mathrm{SU}(2)_R$ with charged matter genuinely
requires complete doublets, in an even number, supplying a real,
spacetime-native reason (not a string-worldsheet borrowing) to need both
an $\mathrm{SU}(2)_L$-doublet's and an $\mathrm{SU}(2)_R$-doublet's worth
of matter — mapping cleanly onto E17's already-established
$t{=}1\leftrightarrow(2,1)$, $t{=}0\leftrightarrow(1,2)$ identification.

**Why it stops at BLOCKED, not PASS — three independent, self-admitted
gaps:** (a) the full $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times
\mathrm{SU}(2)_R$ unification this argument is normally checked against is
NOT geometrically realized here — `preprint.tex` itself states (gate G97)
that no $\mathrm{SU}(4)$ subgroup exists in
$\mathrm{Iso}(S^3\times S^6)=\mathrm{SO}(4)\times\mathrm{SO}(7)$ at all,
with $\mathrm{U}(1)_{B-L}$ patched in from fermion charges, not gauged;
(b) this project's own explicit, already-verified anomaly-cancellation
computation checks only the Standard Model's own broken-phase conditions
(`U(1)_Y`-based), never a manifestly-`\mathrm{SU}(2)_R`-gauged or
Witten-global-anomaly condition — a previously-unexamined verification
gap this round surfaces, not previously flagged by any prior round; (c)
Lemma L5's asymmetric $S^6$-chirality tension (already flagged in E17
Section 5) remains unresolved — a more solidly-grounded "both sectors
needed" argument sharpens, rather than dissolves, the puzzle of why the
identical logic wouldn't also force a symmetric (rather than the paper's
own asymmetric) result on the $S^6$ factor. No stated parent action
(E18/KT-1's core gap) is supplied either way.

**Pearl flagged:** the general distinction this round turned on — a gauge
symmetry's mere EXISTENCE (a structural commitment) is categorically
different from, and can be much stronger than, a SPECIFIC coupling-value
or numerical-equality assumption used downstream for one phenomenological
estimate — is worth re-checking wherever a prior round rejected a
"left-right symmetric" reading on the basis of a narrow downstream
assumption, before assuming the broader underlying claim was covered too.

**Net effect on the parent-action search (rounds 86-90):** narrows the
open question from "is there ANY real, non-borrowed argument for
Pati-Salam-style coexistence" to a specific, nameable remaining gap:
resolve gate G97's $\mathrm{SU}(4)$-incompleteness (or show the narrower
$\mathrm{SU}(2)_R$-only Witten-anomaly argument suffices without full
$\mathrm{SU}(4)$), verify the manifestly-$\mathrm{SU}(2)_R$-gauged anomaly
condition using this project's own already-existing 32-state bookkeeping,
and reconcile with Lemma L5's asymmetric chirality. This is the closest
any of rounds 86-90 have come to a genuine, spacetime-native resolution —
still short of PASS, but for the first time with concrete, addressable
next steps rather than a closed-off literature class.

---

### Round91 — SU(2)_R doublet-parity count (round90's own flagged next step)

Round90's Relaxation Map flagged the cheapest concrete next step: does
this project's own already-established fermion content actually have an
EVEN or ODD count of gauged $\mathrm{SU}(2)_R$ doublets, checked using only
this project's own bookkeeping (not imported Standard Model conventions)?
If $t=0$'s content is the ONLY source of $\mathrm{SU}(2)_R$-doublet matter
and completing an otherwise-odd count, that would sharpen round90's
`BLOCKED` toward a genuine `PASS`.

**Verdict:** `BLOCKED__ONLY_T-INDEXED_METHODOLOGY_GIVES_ODD_COUNT_BUT_FAILS_ITS_OWN_SU2L_CROSSCHECK__RIVAL_BOOKKEEPING_GIVES_EVEN_BUT_IS_NOT_ESTABLISHED_AS_APPLICABLE`
— independently re-run and re-verified (script output matched exactly;
directly confirmed `g6_spinor_decomposition.py` contains zero occurrences
of `t`/torsion — a genuinely separate bookkeeping system; directly
confirmed G74A's own "$G_2$-singlet" characterization, lines 65/72/92).

**A genuinely valuable finding, via a clean self-administered kill-test:**
this project contains exactly ONE bookkeeping system actually indexed by
the connection parameter $t$ (the E9–E17 zero-mode chain: $\dim\ker
D_{S^3,t}=2$, $\dim\ker D_{S^6,\mathrm{twisted}}=1$ per channel, $\times 3$
triality channels, with G74A's own $G_2$-singlet characterization implying
NO further color multiplicity). Applying this ("System A") to $t=0$ alone
gives **1 doublet/channel $\times$ 3 channels = 3, ODD**. But applying the
*identical* methodology, as a required cross-check, to the
$\mathrm{SU}(2)_L$/$t=1$ sector ALSO gives 3, ODD — directly contradicting
the independently well-established fact (real Standard Model physics,
and this project's own SEPARATE `G6` color-carrying bookkeeping) that the
true $\mathrm{SU}(2)_L$ doublet count is EVEN (12: 3 generations $\times$
4 color/lepton doublets). **A counting methodology that gives a wrong
answer on the one case where the true answer is already known cannot be
trusted on the case where it is not.**

The rival bookkeeping (`g6_spinor_decomposition.py`, color-carrying,
predates the $t$-parameter program entirely) WOULD give self-consistent
even totals (24 including CPT-conjugates, 12 excluding) — but its
applicability to the actual $t=0/t=1$ zero-mode split is exactly the
reconciliation gap E12 Section E.2 / E17 Section 2 already flagged as
open and unattempted. This round shows that gap has concrete, blocking
consequences for the specific question round90 raised, not just an
abstract loose end.

**Net effect:** round90's Relaxation Map item is not closed — this
project's own established fermion content is not yet precise enough, on
its own terms, to determine the $\mathrm{SU}(2)_R$ doublet parity. The
missing ingredient is now named precisely: reconcile the topological
zero-mode count (System A) against the physical color/family multiplicity
(System B), or supply the parent action that would fix which one governs
the actual physical spectrum. This is a well-argued, honest `BLOCKED`, not
a dead end — it identifies a concrete prerequisite question (System A vs.
System B reconciliation) that sits upstream of the SU(2)_R parity question
itself.

---

### Round90 correction (2026-07-17, user review) — Witten anomaly REFUTED as the mechanism; correct mechanism identified

Independently re-verified: round90's central claim that **Witten's `SU(2)`
global anomaly** forces both Pati-Salam sectors is **REFUTED**. Each
multiplet ($F_L\sim(4,2,1)$ or $F_R^c\sim(4̄,1,2)$) already contains 4
$\mathrm{SU}(2)$-doublets on its own (the `4` of $\mathrm{SU}(4)$ supplies
the multiplicity) — an EVEN count, so either piece alone is already
Witten-anomaly-free; the criterion never singled out the pair.

**The correct mechanism, verified independently:** the perturbative
(cubic) $\mathrm{SU}(4)^3$ gauge anomaly. $A(F_L)=A(4)\times\dim(2)\times
\dim(1)=+2$; $A(F_R^c)=A(4̄)\times\dim(1)\times\dim(2)=-2$ — only their
**sum** vanishes. A genuinely gauged, chiral $\mathrm{SU}(4)_{\mathrm{PS}}$
(not $\mathrm{SU}(2)_R$ alone) requires both pieces for consistency.

**Registered status (R90-A through R90-E, per user's framing):**

| ID | Claim | Status |
|---|---|---|
| R90-A | `preprint.tex` treats $\mathrm{SU}(2)_R$ as a genuine gauge factor | VERIFIED TEXTUALLY; physical derivation from geometry alone OPEN |
| R90-B | Witten `SU(2)` anomaly forces both Pati-Salam multiplets | **REFUTED** — each multiplet has an even (4) doublet count alone |
| R90-C | Genuinely gauged chiral $\mathrm{SU}(4)_{\mathrm{PS}}$ requires both $(4,2,1)$ and $(4̄,1,2)$ for cubic anomaly cancellation | SUPPORTED / algebraically verified ($+2-2=0$) |
| R90-D | This project has the required gauged $\mathrm{SU}(4)_{\mathrm{PS}}$ (or $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$) completion | OPEN — blocked by gate G97 and $B{-}L$ geometric origin |
| R90-E | $t=0$ and $t=1$ map to the two Pati-Salam matter sectors | OPEN — no explicit map constructed |

**Overall:** promising internal gauge-consistency lead (a genuine advance
over rounds 87-89's external-analogy dead ends), the original Witten-anomaly
sub-claim refuted, physical $t$-selection still blocked. Round91's own
SU(2)_R doublet-parity investigation is superseded in its specific framing
(it checked the wrong anomaly type) but its System-A-vs-System-B
bookkeeping finding stands independently. Corrections applied additively to
`experiments/20260717-round90-.../decision.md` and
`experiments/20260717-round91-.../decision.md` — history preserved, not
rewritten, matching this project's own G74A-correction precedent.

---

### Round92 — Endpoint-to-representation anomaly audit (user's frozen-$G_{\mathrm{eff}}$ design)

Ran the user's own precisely-specified experiment: freeze
$G_{\mathrm{eff}}=\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$
(Option i — the geometrically-realized group, per round90; explicitly
NOT switching to the unrealized $\mathrm{SU}(4)_{\mathrm{PS})$ option
after seeing results), determine each endpoint's representation, and
compute the anomaly coefficients for real, checking whether only the
union cancels.

**Verdict:** `BLOCKED` — independently re-verified a key new finding:
`preprint.tex` contains **two distinct, unreconciled hypercharge
formulas**: $Y=K_3+(B{-}L)/2$ (line 302/309, the one actually used in the
paper's own verified anomaly-cancellation computation) versus
$Y=T_{3R}+(B{-}L)/2$ (line 408, used only in the self-flagged-illustrative
Weinberg-angle section) — confirmed by direct grep, both exactly as
cited.

**What succeeded:** both endpoints ($t{=}0\leftrightarrow(1,2)$,
$t{=}1\leftrightarrow(2,1)$) are independently re-derived (from
$\mathrm{SU}(3)\subset G_2$ combined with the kernel living in the
$G_2$-trivial isotypic component) to be $\mathrm{SU}(3)_c$ SINGLETS at
BOTH endpoints — new confirmation, traced to the *current* authoritative
source rather than the superseded G74A lemma, of round91's own inference.
$[\mathrm{SU}(3)_c]^3$ is trivially computable (zero for both endpoints
and their union, since both are singlets) — shows no forcing, not the
PASS pattern. Witten $\mathrm{SU}(2)_L/\mathrm{SU}(2)_R$ parity is also
computable (reusing round91): each endpoint is a total singlet under the
*other* $\mathrm{SU}(2)$ factor, so the union changes neither parity —
no cross-endpoint cancellation there either.

**What blocked:** the $U(1)_Y$-mixed anomaly conditions
($[U(1)_Y]^3$, $[\mathrm{SU}(3)_c]^2 U(1)_Y$, $[\mathrm{grav}]^2 U(1)_Y$)
require a numeric $B{-}L$/hypercharge value for the twisted $S^6$-kernel
that has never been assigned anywhere in this project (a gap already
flagged in round83) — and even if it were, it is unclear WHICH of the
two hypercharge formulas above would apply, since `g6_spinor_decomposition.py`
uses the second (Weinberg-only) formula, not the one actually verified for
anomaly cancellation in the paper's own text.

**Net effect:** neither PASS nor a clean FAIL is supported — 3 of 4
required anomaly conditions cannot be computed from this project's own
current content, and the one that can be computed ($[\mathrm{SU}(3)_c]^3$)
shows no forcing on its own. `BLOCKED` precisely names the missing piece:
a numeric $B{-}L$/hypercharge assignment for the twisted $S^6$ kernel,
plus resolution of which of the two hypercharge formulas actually applies
— a genuine, previously-unnoticed internal inconsistency this round
surfaces as a byproduct, independent of the main anomaly-audit question.

---

### Round93 — Charge-operator and representation-lift gate (user's recalibration of round92)

Per the user's own precise recalibration: round92's blocker is broader
than "missing numeric $B{-}L$" — it is the absence of an explicit map
from torsion-endpoint zero modes to independent 4D Weyl fields with
well-defined charge operators. Ran the user's exact 4-part design (A:
operator provenance table; B: resolve the two $Y$ formulas; C:
all-left-handed census excluding CPT duplicates; D: $\mathrm{SU}(4)$ lift).

**Verdict:** `BLOCKED` — narrower and sharper than round92's, because
Part B reached a genuine, tool-verified **positive** resolution.

**Part B, the headline finding, independently re-verified:** $K_3=T_{3R}$
is **proven**, not merely argued — direct matrix computation
(re-run myself, `K3_equals_T3R_as_32x32_operator=True`,
`no_s6_side_k3_construction_found_in_code=True`) shows they are the
identical operator in every piece of this project's own code that
computes with it (10 files: G11, G12, G16, G17, G19, G21–G24, KT-6). The
"two distinct, unreconciled $Y$-formulas" round92 flagged traces to a
**documentation propagation error**, not a physical ambiguity:
$K_3$-as-defined-in-code is built entirely from the S³-side
$\mathrm{SU}(2)_R$ generator (`g11_block_generators.py`, "trivial on
$S^6$"), and `g16_t3r_k3.py`'s own docstring frames the whole experiment
as testing whether "$K_3$ eigenvalues give $T3R=\pm1/2$" — i.e. $K_3$ and
$T_{3R}$ were never meant to be different quantities. But **G16's own
`decision.md:9`** (written the same day as its own script) states "$K_3$
is the Cartan generator of $\mathrm{SO}(6)\supset\mathrm{SU}(3)$ on
$S^6$" — directly contradicting its own code, confirmed word-for-word by
direct read. This wrong description propagated verbatim into
`preprint_draft.md:125–126` and then into `preprint.tex:304–305`,
**surviving three independent citation-only rounds** (90, 91, 92) that
each read the paper's prose without tracing back to the underlying code.
The paper's own already-verified anomaly computation
(`g12_anomaly_check.py`, underlying `preprint.tex:309–320`) already used
$T_{3R}$ consistently the whole time — there is no internal
inconsistency in the published anomaly result itself, only a mislabeled
one-line prose description of $K_3$'s geometric origin.

**Part A/C, what remains blocked:** $B{-}L$ has never been constructed as
an operator on the twisted torsion-endpoint kernel's Hilbert space at
all — it exists only as a post-hoc LABEL on G6's untwisted, per-KK-level
8-state weight space. This is a genuinely different, deeper gap than
Part B's (a missing *operator on the relevant space*, not a formula
ambiguity), untouched by the $K_3=T_{3R}$ resolution — the sole remaining
blocker, stated in its sharpest form yet.

**Part D:** an explicit $\mathrm{SU}(4){\cong}\mathrm{SO}(6)$ action does
close the untwisted $S^6$ spinor into complete $4\oplus\bar4$
representations (re-verified: `chirality_split_is_4_plus_4bar=True`) —
but is confirmed neither an isometry (gate G97) nor $B{-}L$-preserving
for the full 15-generator algebra (gate G98, re-verified with a
basis-dependence clarification: commutes with the 9-dim
$\mathfrak{su}(3)\oplus\mathfrak{u}(1)$ subalgebra, not the full 15) —
gauging the full $\mathrm{SU}(4)$ would erase the very $B{-}L$
distinction the hypercharge program depends on. `SU4_ANOMALY_ROUTE:
NOT_APPLICABLE`, correctly not computed further.

**Pearl flagged (impact ~6, worth a general sweep):** a `decision.md`
summary written the same day as its own script, contradicting that
script's own code, survived undetected through three later rounds that
each cited `preprint.tex`'s downstream prose without grepping the
underlying source. Before promoting any future "unreconciled formula" or
"apparent inconsistency" finding based on prose alone, grep the
underlying script's own construction first — a ~15-minute check that
here overturned what three prior rounds had treated as an open physical
question.

**Net effect on the parent-action search (rounds 86–93):** the hypercharge
formula ambiguity is resolved (closed, positively); the sole remaining
blocker on the $B{-}L$/anomaly line is now named as precisely as
possible — not "no numeric value assigned" but "no operator exists
anywhere relating the twisted kernel's Hilbert space to any weight-labeled
basis where a $B{-}L$ charge would even be well-defined." Round85/E17's
$t=0/t=1$ coexistence question and round91's System-A/System-B
reconciliation remain untouched, exactly as before.

---

### Round94 — B-L eigenvalue on the twisted kernel (cheapest differentiating test, via multi-lens)

A `/multi-lens` pass on the round93-flagged B-L blocker identified the
cheapest differentiating test: since $B{-}L\propto$ the central $U(1)$
generator of $\mathfrak{su}(3)\oplus\mathfrak{u}(1)\subset\mathfrak{so}(6)$
(G15's own T8 result) and the twisted kernel is exactly 1-dimensional, if
this generator preserves the kernel, $B{-}L$ is automatically a scalar
there (elementary linear algebra) — a calculation, not new physics.

**Verdict:** `PASS_WITH_DOCUMENTED_CAVEAT` — $B{-}L=0$ for the physical
twisted zero mode. Independently re-verified: re-ran the script (identical
output); directly confirmed $v_a,v_b,w$ match
`round59_route_b_consistency.py:219–221` exactly, and $B{-}L=(2H{-}3)/3$
matches `g15_hypercharge.py:105–106` exactly.

**Structural compatibility (Part 1):** dolan-casimir/round59's 8-dim fibre
$\Sigma=\Lambda^\bullet(\mathbb{C}^3)$ IS the same $\mathrm{SU}(3)$-module
as G15's weight space (both $1\oplus3\oplus\bar3\oplus1$), verified
entrywise via an explicit degree-preserving bijection — no basis-conversion
gap, contrary to what might have been feared.

**Eigenvalue (Part 2):** Leibniz-lifting $B{-}L$ to the 64-dim twisted
fibre (reusing round59's own `leibniz64` function unchanged, just fed
$B{-}L$'s degree matrix instead of an $\mathrm{su}(3)$ generator) shows
round59's own invariant basis vectors $v_a,v_b$ are each individually
$B{-}L$-eigenvectors with eigenvalue $0$ — a structural consequence of
$\mathrm{SU}(3)$-representation theory (invariants in the domain block
force total exterior degree $=3$, and both degree-$(1,2)$ and
degree-$(3,0)$ combinations give $B{-}L=0$), independent of the specific
torsion/coset construction. The physical kernel vector
$k=-\sqrt3\,u_1+u_2$ (recomputed fresh, reproducing round59's own cited
coefficients independently) is therefore automatically an eigenvector too.

**The honest caveat (Part 4), reported in full, not minimized:** a genuine
incompatibility exists — the Leibniz-lifted $B{-}L$ operator does NOT
commute with the full twisted Dirac operator $D_{\mathrm{full}}$ (confirmed
freshly, two independent ways), reconfirming G98's original concern at a
sharper, more relevant level than G98's own untwisted-space check. **This
is shown, not merely argued, not to threaten the eigenvalue claim**: the
kernel's eigenvalue depends only on the entire 2-dimensional domain already
being one $B{-}L$-eigenspace (an $\mathrm{SU}(3)$-representation-theory
fact), not on which specific direction within that space the
torsion-dependent Dirac operator happens to null.

**Honest labeling tension, flagged explicitly by the experiment itself:**
the pre-registered PASS criterion literally required the risk-check to
find "no incompatibility" — one WAS found. The experiment argues PASS is
still the correct call because the specific doubt BLOCKED requires
("doubtful without further work") does not survive: no further work
resolves it, the eigenvalue is shown definitively insensitive to the
incompatibility found. A stricter reader could relabel this
`BLOCKED-BUT-RESOLVED` without changing the underlying computation or
its conclusion — flagged here for full transparency, not smoothed over.

**Net effect:** closes round93's sole remaining blocker for the S⁶-side
hypercharge program — $B{-}L$ is now a genuine, tool-verified operator on
the twisted kernel's own Hilbert space (value $0$), not merely a
post-hoc label on a different (untwisted) space. Does not touch
round85/E17's $t{=}0/t{=}1$ coexistence question or round91's
System-A/System-B reconciliation (both remain S³-side, untouched). Pearl
flagged: the Leibniz-lift technique used here is a general, reusable
pattern for extending any central/abelian charge from a single fibre to a
twisted/tensor-product fibre — worth reusing before inventing new
machinery next time a similar extension is needed.

---

### Round95 — Lemma L5 vs. Pati-Salam tension: same invariant or different?

The last remaining conceptual obstacle repeatedly flagged (E14 Reading 3,
round90 Section 5c) but never directly tested: does Lemma L5's $S^6$-side
asymmetric chirality result genuinely conflict with round90's
$S^3$-side Pati-Salam "both sectors needed" requirement?

**Verdict:** `TENSION_DISSOLVES__CONTINGENT_ON_H1C_KT8_STAYING_OPEN` —
independently re-verified: read `preprint.tex:886–912` (Lemma L5's exact
current text) and `preprint.tex:135–140` (the decoupled-operator
disclaimer) directly, both confirmed word-for-word.

**Why the tension dissolves:** L5's $\mathrm{sign}(\mathrm{ind})=+1$ is an
exact statement about $D_{S^6}\otimes S^-$ **alone** — this project's own
text says so explicitly: "the three-channel index computation is
therefore an exact statement about $D_{S^6}\otimes S^-$ alone, not —
without a further physical ingredient acting on the $S^3$ factor — about
a massless 4D fermion mode of the full construction" (`preprint.tex:135–140`).
Round90's Pati-Salam requirement, by contrast, concerns the $S^3$ factor's
own $\mathrm{SU}(2)_L$/$\mathrm{SU}(2)_R$ representation content
(governed by $t$, per E17). L5's own "left-handed = SM $\mathrm{SU}(2)_L$
doublet" sentence (`preprint.tex:908-912`) is an interpretive LABEL for
what the S6-sector would become, not an already-derived cross-factor
statement — the actual pairing rule (which S6 triality-channel links to
which S3 $t$-sector) is exactly H1c, still open. Different invariants, no
established bridge — the apparent conflict was reading a label as if it
were a derivation.

**A genuine refinement worked out fresh, not just cited:** round90's own
framing of the cubic anomaly's "sum condition" as weaker than requiring
$n_L=n_R$ is correct in general gauge theory, but — given round90's own
cited coefficients ($A(4,2,1)=+2$, $A(4̄,1,2)=-2$) and E17's own
established fact that this project's S3-content contains ONLY these two
representation types — the sum condition $n_L\cdot(+2)+n_R\cdot(-2)=0$ is
mathematically EQUIVALENT to $n_L=n_R$ for this project specifically, not
a weaker escape hatch.

**Honest contingency, not a permanent resolution:** if H1c/KT-8 is ever
closed by a pairing rule assigning ALL 3 generations to one $t$-sector
(matching a literal, non-aspirational reading of L5's "all three purely
left-handed"), the tension becomes sharp and concrete: $n_L=3$, $n_R=0$,
violating round90's $n_L=n_R$ directly. **New pearl, independently
flagged:** this scenario would ALSO independently violate Witten's
$\mathrm{SU}(2)$ global anomaly for $\mathrm{SU}(2)_L$ alone (3 is odd) —
a stronger, more immediate inconsistency than the cubic-anomaly
violation, worth checking FIRST in any future H1c-closing attempt.

**Honest self-assessment (per the task's own instruction to judge, not
excuse):** E14's original caution was reasonable given what was known at
the time. Round90 Section 5c, however, already had E17's representation
table and the exact `preprint.tex:135-140` disclaimer in hand and could
have made this same count-vs-content distinction one round earlier — a
resolvable oversight, not a new fact this experiment had to discover from
scratch.

**Net effect:** closes the Lemma-L5 tension flagged repeatedly since E14
— not permanently, but with the exact condition under which it would
revive stated precisely. Does not resolve H1c or KT-8, does not affect
$N_{\mathrm{gen}}=3$, does not overturn round90's own `BLOCKED` verdict
on the separate SU(4)-incompleteness and anomaly-check gaps (Sections
5a/5b of that round stand unchanged).

---

### Rounds 96-100 — `/boyko-goal-expansion-100` follow-through: Pati-Salam
route exhausted within `G_eff`; curvature double-well found (weakened);
Friedrich-Ivanov no-go inconclusive

Following a `/boyko-goal-expansion-100` (deep mode) solution-space search
for the parent-action mechanism (34 non-duplicate candidates, saved
separately — see memory), the top-ranked, cheapest candidates were
executed in sequence.

**Round96 (E25) — `FAIL__ALL_THREE_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING`.**
Round93's `K_3≡T_{3R}` finding collapses round92's "two unreconciled
$Y$-formulas" into one (`Y=T_{3R}+(B{-}L)/2`), and round94's `B{-}L=0`
makes it fully computable. Tool-verified (`sympy`): all three previously-
BLOCKED mixed-$U(1)_Y$ anomaly conditions (`[SU(3)_c]^2U(1)_Y`,
`[U(1)_Y]^3`, `[\mathrm{grav}]^2U(1)_Y`) evaluate to **zero for `t=0`
alone, `t=1` alone, AND the union** — not just the union. `t=0` alone is
zero due to an internal $\pm1/2$ cancellation within its own doublet
(robust to whatever `B-L` turns out to be); `t=1` alone is zero
specifically because `B-L=0`. Either way, no forcing pattern is available
from this channel.

**Round97 — `NO-GO_CONFIRMED__ROUND90_EXHAUSTIVENESS_HOLDS`.** Direct
grep of `preprint.tex` for every fermion/singlet/`SU(4)` mention confirms
round90's `(4,2,1)`/`(4̄,1,2)` cubic-anomaly analysis rests on a complete
field list — the only other `SU(4)`-adjacent object (the Higgs bidoublet
$(2,2)_0$) is a scalar, structurally irrelevant to a fermion-triangle
gauge anomaly regardless of its own charge.

**Round98 (C5) — `INCONCLUSIVE__SOURCE_ACCESS_INSUFFICIENT_HONEST_UNKNOWN`.**
Friedrich & Ivanov (2002, arXiv:math/0102142, confirmed real via
`WebFetch`) prove "at most one connection with totally skew-symmetric
torsion" for almost-contact-metric/almost-Hermitian/$G_2$-structures,
with string-theory applications in dimension $n=5,6,7$. Whether this
uniqueness theorem's actual hypotheses (not just its stated applications)
extend to $n=3$/$S^3$=SU(2) could **not** be determined — the PDF did not
render as readable text via `WebFetch`, and a related survey
(Agricola, arXiv:math/0606705) gave only an abstract. Reported honestly
as `<unknown>`, not guessed either way, per this project's own Evidence
Policy (`[UNKNOWN] > false [INFERRED]`).

**Round99 (B4) — `WEAKENED__CLASSICAL_MATH_CONFIRMED_PHYSICAL_FRAMING_OVERREACHED`.**
Reproduced (not novel — Cartan & Schouten, 1926) the classical curvature
formula $R^t(X,Y)Z=t(t-1)[[X,Y],Z]$ for this project's own generator
convention, tool-verified for all 27 index triples: flat at $t=0,1$,
curved at $t=1/2$, and a genuinely nonzero curvature-norm component
(`R^t(Z_1,Z_2)Z_1`) gives a double-well $V(t)\propto[t(t-1)]^2$ with
minima exactly at $t=0,1$. **Self-caught bug before presenting:** the
first script version used a degenerate, identically-zero index triple
(`R^t(Z_1,Z_2)Z_3\equiv0$ for all $t$, since `[Z_1,Z_2]\propto Z_3$
already) — corrected before this was reported. **Skeptic review
(context-asymmetric, claim+code only) verdict: WEAKENED** — the pure math
is correct, but `V(t)` is a bare kinematic tensor-component norm, not a
derived term of the actual spectral action; no volume integral, kinetic
term for $t$, or equations of motion were constructed. This shows the
double-well shape is available "for free" from classical geometry alone
**if** such a term appears in the real action — a plausibility ingredient
for B1's full (unattempted) spectral-action derivation, not a mechanism
or a derivation in itself.

**Round100 (E1) — `CONSISTENT__NO_CONTRADICTION__ONE_SHARPENED_SUMMARY_SIGNAL`.**
A constraint-satisfaction sweep collecting all of rounds 86-99's
established facts into one table found no contradiction, and one useful
sharpening: **every perturbative and global anomaly channel computable
within the geometrically-realized `G_eff=SU(3)_c\times SU(2)_L\times
SU(2)_R` has now been checked (round92, round96, round91/92) and shows no
forcing** — the Pati-Salam/anomaly route (rounds 90-97) is exhausted for
its own internal method. The ONE channel that would force coexistence
(round90's cubic $SU(4)_{PS}^3$) remains blocked by the single, precisely
-named gate G97 (`SU(4)` not geometrically realized) — not a diffuse
"needs more checking," but a sharp, single remaining structural question.

**Net effect of rounds 96-100:** the Pati-Salam/anomaly parent-action
route is now fully exhausted within the frozen `G_eff` — nothing left to
check there except gate G97 itself (alternative `SU(4)` realizations,
goal-expansion-100 candidates A1/E2, unattempted). A new, independent,
not-yet-conclusive candidate (curvature-double-well/`t`-as-modulus, B1)
was opened but not resolved (round99, `WEAKENED`) — its full
spectral-action derivation remains open. The Friedrich-Ivanov structural
no-go (C5) remains a genuinely open literature question, not resolved
either way. Does not affect $N_{\mathrm{gen}}=3$
(G73/G74A/G74B, S⁶-only), `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`. Not yet committed to git.

---

### Rounds 101-102 — A6 (spin-connection equivariance) and A1 (gate G97
precision check, self-corrected after skeptic review)

**Round101 (A6) —
`NAIVE_APPROACH_BLOCKED__X_DEPENDENT__INHOMOGENEOUS_TERM_NEEDED`.** The
one item explicitly flagged as unattempted in round80/E14's own
Relaxation Map ("full spin-connection-level check... `[INFERRED]`, not
independently verified") was attempted: the naive component-substitution
analogue of round80's own torsion-tensor pullback trick
(`Ω_i^R(t)(x):=Σ_j b_i^j(x)Ω_j(t)`, reusing E9/round73's spin connection
and round80's own `b_i^j(x)` coefficients unchanged) was tool-verified to
be genuinely `x`-dependent, not constant — the mathematically correct
reason being that a connection 1-form is not a tensor and acquires an
inhomogeneous (Maurer-Cartan-type) term under a non-constant frame change,
which torsion (a genuine tensor) does not. This is an honest, informative
negative result, not a failure: it correctly identifies exactly what a
full spin-level check would need to add (the `g⁻¹dg`-type term), narrower
than before, not resolved.

**Round102 (A1) —
`WEAKENED__NARROW_ALGEBRA_LEVEL_OPEN_QUESTION__NOT_A_REOPENING`,
self-corrected after mandatory skeptic review.** Given gate G97's status
as the single most heavily-cited blocker in the entire rounds 90-101
chain, this round attempted a precision check of its literal wording
("no `SU(4)` subgroup in `Iso(S³×S⁶)=SO(4)×SO(7)`") — noting
`so(6)⊂so(7)` is a genuine, tool-verified Lie-algebra fact (isotropy
subalgebra of a point on `S⁶`), and `so(6)≅su(4)` (D₃=A₃). **First-draft
proposal (WITHDRAWN after skeptic review, recorded honestly, not
smoothed over):** argued this made G97's wording imprecise, but that
substituting the `G₂`-holonomy group (14-dim, `dim<15=dim(su(4))`, the
mechanism `preprint.tex` actually cites for deriving `SU(3)_c`) as "the
relevant ambient" repaired the conclusion. **Skeptic (Step 8a,
context-asymmetric) verdict: WEAKENED**, catching two real errors: (1)
`SO(6)≠SU(4)` as GROUPS (`SU(4)` is the double cover `Spin(6)`) — G97's
literal GROUP-level wording is actually defensible as written, i.e. I had
the direction of the imprecision backwards; (2) substituting `G₂`-
holonomy for `SO(7)`-isometry is a **category error** (isometries and
holonomy are logically distinct notions) — the dimension argument only
rules out `su(4)⊂g₂` alone, and does NOT address the literally-cited
`SO(4)×SO(7)`, where `so(6)⊂so(7)` still sits unaddressed at the pure
ALGEBRA level. **What genuinely survives, narrowly:** a previously-
unasked, well-defined, unresolved question — does the algebra-level
`so(6)⊂so(7)` embedding correspond to Killing vectors of `S⁶` that are
actually consistent with this project's already-fixed `SU(3)_c`/fermion
content, or not? Flagged, not answered. **Does NOT reopen gate G97**,
does NOT supply a working `SU(4)` alternative, does NOT license
revisiting any downstream round's conclusions.

**Net effect of rounds 101-102:** both items from goal-expansion-100's
"queued next steps" (A6, A1) are now attempted; A6 gives a clean,
correctly-explained negative result; A1's headline finding is its own
self-correction process working exactly as designed (skeptic catching a
category error before it reached the user as an overclaim) — the
substantive open question it narrows down to (algebra-level `so(6)`
realizability) is new, but unresolved. Neither round changes any
established verdict in rounds 86-100. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`. Not yet committed to git.

---

### Round103 — D4 (moonshot): is the product-decoupling ansatz
structurally incompatible with `t=0`/`t=1` coexistence?

**Verdict:** `FALSIFIED__MY_REFRAMING_ATTEMPT_FAILED__QUESTION_GENUINELY_OPEN`
(skeptic verdict, context-asymmetric review). The explicit "moonshot"
tier item from goal-expansion-100: attempt to prove/disprove whether
`D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12, presupposed throughout
E1-E102) structurally forbids ANY mechanism forcing `t=0`/`t=1`
coexistence.

**Proposed dissolution (WITHDRAWN after skeptic review):** argued
coexistence is trivially ALLOWED — just postulate two separate fermion
multiplets, one coupling to `D_{S3,0}`, one to `D_{S3,1}`, "analogous to
chiral gauge coupling." **Skeptic verdict: FALSIFIED** — this analogy is
a category error: `t` parametrizes the SPIN connection (part of the
geometric datum defining the internal space in the Connes-style spectral
triple `(A,H,D)` framework this project uses elsewhere), not a gauge
representation choice layered on a fixed geometry. "Two different `D`'s
for different fields on the same internal manifold" is either (a) an
admission the spectral triple is under-specified, or (b) an implicit
redefinition of the internal geometry itself into a genuinely different
object (doubled `S³`, or dynamical torsion à la Einstein-Cartan-Sciama-
Kibble) — not a free-lunch bypass.

**Net effect:** the moonshot does not resolve either way — no formal
incompatibility proof, no formal compatibility demonstration survives.
What DOES survive as this round's actual product: a sharper statement of
what "coexistence" concretely requires — either (i) a spectral triple on
`S³` admitting multiple consistent Dirac operators (a specific, checkable
NCG-axiom question, unattempted), or (ii) explicitly leaving the
`S³×S⁶` product ansatz for a doubled/dynamical-torsion geometry (linking
to round99's B1 "t-as-modulus" direction). This is an honest report of a
failed attempt at a genuinely hard question, per this round's own
pre-registered acknowledgment that moonshot items carry real non-
resolution risk — not a forced conclusion. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`. Not yet committed to git.

**Session status after rounds 96-103:** all three items the user
requested this turn ("продолжай к A6, D4, A1") are now attempted — A6
(round101, clean negative result), D4 (round103, genuinely open, honest
non-resolution), A1 (round102, self-corrected, narrow open question
flagged). Combined with rounds 96-100, the Pati-Salam/anomaly route is
exhausted within the frozen `G_eff`; the sole remaining structural
question for an alternative `SU(4)` realization is now precisely the
algebra-level `so(6)` question round102 identified; the `t`-as-dynamical-
-modulus direction (B1/round99) and this round's spectral-triple fork are
the two most promising NOT-yet-closed avenues for a genuine future
follow-up.

---

### Round104 — A2 (anomaly inflow at ι's fixed points):
`NOT_APPLICABLE__CODIMENSION_MISMATCH`

Cheap, purely dimensional check: Callan-Harvey-style anomaly inflow
requires a codimension-1 interface; round80/E14's `ι` fixed-point locus
on `S³` (`{g=±1}`, 2 isolated points) is codimension-3 — a structural
mismatch with the mechanism's own applicability requirement, settled
without needing the full inflow computation. On inspection, A2 and A6
(round101) turn out to be the SAME underlying equivariant-index question
in two different physics vocabularies, not independent candidates — A2
does not need separate future pursuit.

### Remaining goal-expansion-100 candidates — honest status, not pursued
further this session

Of the 34 non-duplicate candidates in the original report, 9 have now
been attempted with real verification (A1, A2, A3/A4, A6, A7, B4, C5, D4,
E1). The remaining ~25 (C1/C2/C3/C6 non-geometric-flux/DFT/ExFT/twistor
variants; D1/D2 bordism/TQFT-categorical framings; B1's full
spectral-action derivation, B2/B3/B5 modulus-dynamics variants; A5
Green-Schwarz-without-strings; E2 full GAP/LiE computational search; E3
Lean/Coq formalization) were **not** pursued further this session — an
honest accounting, not silent abandonment:

- **B1's full task (deriving `V(t)` from the actual spectral action)**
  remains the single most promising NOT-yet-attempted item — round99
  showed the double-well shape is at least plausible from classical
  curvature alone, and round103's spectral-triple fork independently
  points at the same direction (does the spectral triple admit dynamical
  torsion). This is a substantially larger undertaking than any single
  round attempted so far, correctly flagged as such in both places.
- **E2 (full GAP/LiE search)** was partially subsumed by round102's own
  explicit `so(6)⊂so(7)` construction and its correction — a full
  systematic Lie-subalgebra classification search remains open but the
  highest-value single sub-question it would need to answer (does
  `so(6)` embed via Killing vectors consistent with the fixed `SU(3)_c`)
  is now precisely named, not vague.
- **C1/C2/C3/C6/D1/D2/A5/E3** remain at their original low
  `confidence` scores (0.05–0.2) from the goal-expansion-100 report —
  no new information surfaced this session to change that assessment;
  pursuing them further without a stronger prior would not be a good use
  of effort relative to sharpening B1 or the round102 algebra-level
  question.

**Session status after round104:** per user's explicit request, this
project's own rounds 90-104 chain (Pati-Salam/anomaly route + literature
no-go + curvature-modulus + spin-equivariance + ansatz-incompatibility +
anomaly-inflow) is queued for an independent cross-model review (Codex/
GPT via `codex-companion.mjs task`) — specifically checking whether the
Claude-based skeptic overcorrected anywhere (round102's G97 finding,
round103's D4 finding), and whether a viable path is being missed. See
next section for the result.

---

### Round105 — Independent cross-model audit (Codex/GPT): skeptic
OVERCORRECTED on both flagged cases; new gaps found; one arithmetic
overclaim self-confirmed and corrected

Per user's explicit request, ran Codex (`codex-cli`, updated
0.142.4→0.144.5 to fix a model-compatibility error) as a genuinely
independent reviewer of rounds 90-104 — "different model" review, rated
Medium independence on this project's own Independent Verification
Strength Ladder, stronger than same-model-different-prompt. Full
transcript: `experiments/20260717-round105-codex-cross-model-audit/
codex_review_2026-07-17.md`.

**Headline: Codex judged the internal Claude-based skeptic to have
OVERCORRECTED on BOTH of the two high-stakes cases it was asked to
scrutinize hardest** (round102's gate-G97 finding, round103's D4
moonshot) — `[INFERRED]`-level claims from Codex, not yet independently
spot-checked at the deep-NCG/group-theory level, per this project's own
evidence discipline (Codex's `[VERIFIED]` = this project's `[INFERRED]`
until tool-checked).

**Case 1 (G97):** Codex agrees the skeptic's "G₂-holonomy is a category
error" point was correct, but argues its second point (`SU(4)≠SO(6)` as
GROUPS) does not, by itself, rescue G97's physical conclusion — because
KK gauge bosons come from Lie-ALGEBRA elements (Killing-vector
commutators), and `so(6)≅su(4)` being present as an algebra is the
physically relevant fact for gauge-boson counting, group topology
notwithstanding. Codex's verdict: *"G97, as a physical
no-`SU(4)`-gauge-algebra gate, is not established... round102 should
have reopened G97 conditionally."* Also flags `preprint.tex`'s own
"`G₂` holonomy of `S⁶=G₂/SU(3)`" phrasing as conflating coset-isotropy
with holonomy-of-the-cone (citing Foscolo-Haskins, arXiv:1501.07838 —
**not independently verified this round**).

**Case 2 (D4):** Codex agrees "two multiplets" doesn't FORCE coexistence
and agrees `t` genuinely indexes a spin connection (geometric datum,
not a free gauge choice) — but argues a block-diagonal Dirac operator
`D=diag(D_{t=0},D_{t=1})` is standard NCG practice for a multiplicity
bundle, not an under-specified/redefined geometry. Verdict: *"round103's
original 'coexistence is allowed' was basically correct... the skeptic
confused 'not dynamically motivated' with 'not a standard legitimate
construction.'"* Cites Dąbrowski-Sitarz, arXiv:1012.3055 — **not
independently verified this round.**

**One concrete claim WAS independently spot-checked and confirmed**
[VERIFIED-tool, direct `sympy`, done before accepting Codex's claim]:
round96's decision.md prose ("t=0's cancellation is robust to any `B-L`
value") is **false** — `Y_++Y_-=b`, `Y_+³+Y_-³=b(b²+3)/4`, neither zero
for general `b`, only at `b=0` specifically. **Corrected via an additive
note in round96/decision.md** (this project's standard pattern). The
round96 script's own numerical output (evaluated only at the correct
`B-L=0`) is unaffected — only the interpretive prose overclaimed.

**New gaps Codex found, not previously flagged by any Claude-run round**
(all `[INFERRED]`, not independently checked this round): round92/96
never computed `[SU(2)_L]²U(1)_Y`/`[SU(2)_R]²U(1)_Y` (narrower
"exhausted" claim than round100 stated); the computed `G₂`-trivial
(`SU(3)_c`-SINGLET) twisted kernel may be structurally in tension with
identifying it as Pati-Salam `4`/`4̄` matter (a Pati-Salam `4` restricts
to `3⊕1`, not a pure singlet) — flagged as needing an explicit
intertwiner, not just imported representation labels; round97's grep
check proves manuscript-text completeness, not KK-spectrum
representation-theoretic exhaustiveness.

**Codex's 8 concrete proposed next steps** (not yet attempted): (1)
compute the stabilizer of the FULL background (metric+torsion+`J`+twist,
not just the round metric — the decisive calculation neither round97 nor
round102 performed), (2) construct the explicit `Spin(6)⊂Spin(7)` spin
lift and branch the twisted kernel under it, (3) audit the `G₂`-trivial-
kernel-vs-Pati-Salam-`4` tension, (4) build/test the block spectral
triple against actual NCG axioms, (5) promote `t` to a finite
matrix-valued order parameter with internal `ℤ₂`, (6) full Seeley-DeWitt
spectral-action computation for `D_t²` (round99 only computed one
curvature norm), (7) complete round101 by explicitly computing the
missing `U⁻¹dU` inhomogeneous term — Codex calls this "a finite symbolic
calculation," the cheapest of the eight, (8) separate global-vs-local
anomaly conditions once the spin lift determines the correct global
group.

**Codex's own overall confidence rating on the whole rounds 90-104
chain: 4/10** — *"The existing chain has not found a parent action. It
also has not established a no-go."*

**Net effect and honest calibration:** this round's job was to report
Codex's findings, not to unilaterally accept them — per this project's
own audit-verification-gate discipline, one concrete, cheaply-checkable
claim was independently spot-checked and confirmed correct (calibration
point: the review is substantive, not hallucinated), while the deeper
NCG/group-theory arguments and both external citations remain `[INFERRED]`,
flagged for future verification, not treated as settling gate G97 or D4.
Neither gate is re-closed nor finally reopened by this round alone — both
are flagged for a future round using Codex's own concrete next steps.
Does not affect $N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`,
or `safe_for_runtime=False`. Not yet committed to git.

---

### Round106 — Codex item 7 attempted: `PARTIAL`, harder than "finite
symbolic calculation," third self-correction this session

Attempted Codex/round105's cheapest proposed next step (complete
round101's spin-connection check). Two genuine, uncontested sharpenings
survive [VERIFIED-tool]: (1) `b(x)` is exactly the `Ad(g(x)⁻¹)` matrix in
the `{Z_i}` basis; (2) round101's "naive" `Σb·Ω` computation IS the
correct value of `ω^t(Z_i^R)`, by linearity of 1-forms — not a shortcut
missing a term at THAT step; the real gap is a different, unaddressed
one (how `ι` acts on the spinor FIBER, i.e. which spinors are "constant"
in which frame). A third claim — that `H=(3c/2)I₂` being scalar means
"no spin-lift conjugation of any kind" can relate the `t`/`1-t`
eigenvalues — was **`WEAKENED`** by skeptic review: "constant spinor" is
itself frame-dependent (`ι` induces a point-dependent frame twist,
`S(x)⁻¹ψ` generically isn't constant in the new frame even if `ψ` was in
the old one), so the argument answers a narrower question than intended,
and "no conjugation" ≠ "no mechanism of any kind" (pullback isn't
restricted to pure conjugation). Narrow form survives: a globally
constant conjugation cannot relate the two scalar values except at
`t=1/2`.

**Session-level note:** this is the THIRD time this session (rounds 102,
103, 106) that a confident claim in this exact territory (spin lifts,
connection pullbacks) required a skeptic-driven correction — the mandated
escalation discipline caught a real issue each time, and the gap's
location is now independently triangulated three ways (round101, Codex/
round105, round106) — a real, if modest, sharpening, not a resolution.
Does not affect $N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`,
or `safe_for_runtime=False`. Not yet committed to git.

---

### Round107 — Codex items 2+3: the physical twisted-kernel vector IS a
genuine `SU(4)` singlet, not merely an `SU(3)_c` singlet

Directly attempted Codex/round105's items 2 ("construct the explicit
spin lift, branch the twisted kernel under `Spin(6)≅SU(4)`") and 3
("audit whether the `G₂`-trivial kernel can represent Pati-Salam `4`/`4̄`
at all"). Reused round93's own already-constructed `so6_spin_gens` (15
generators, `SU(4)=SO(6)` acting on the 8-dim `S⁶` spinor space `Σ`) and
round94's own `k_vec` (the explicit physical zero mode in the 64-dim
`Σ⊗Σ` fibre). New computation: Leibniz-lifted all 15 generators to the
64-dim fibre and applied them to `k_vec` directly.

**Result [VERIFIED-tool, two rounds of skeptic review]:** all 15
generators annihilate `k_vec` exactly — `span{k_vec, G_1·k_vec,...,
G_15·k_vec}` has rank **1**. A real basis-convention subtlety had to be
handled explicitly (round93's `so6_spin_gens` use a different 8-dim basis
convention — a "3-qubit kron-index" convention shared with `G6`/`G15` —
than the `Σ⊗Σ` machinery's own `SUBSETS`/exterior-algebra convention): an
explicit permutation matrix `P` was constructed and validated. **Skeptic
pass 1 (`WEAKENED`)** correctly flagged that validating `P` against `B-L`
alone (a DIAGONAL matrix with degenerate eigenvalue multiplicities
`1,3,3,1`) is too weak — a wrong permutation within a degenerate
eigenspace would still pass. **Fixed:** added a stronger cross-check
using the 8 NON-diagonal `SU(3)_c` generators, permuted via `P` and
compared against an INDEPENDENTLY-built reference (`su3_matrix_on_sigma`,
a different module, no kron/qubit convention at all) — individual
generators don't match one-to-one (different labeling convention,
expected) but a span-rank check confirms both sets span the IDENTICAL
8-dimensional subspace. **Skeptic pass 2** confirmed this span check is
logically sufficient for the 9-dim `su(3)+u(1)` piece, but honestly
flagged that the remaining 6 "extra" `so(6)` generators rest on
`lift_to_spinor`'s internal consistency, not an independent third
construction — reported as an explicit residual caveat, not smoothed
over.

**Honest framing correction (both skeptic passes):** this does NOT
establish Pati-Salam-incompatibility from scratch — round92 already
showed `k_vec` is `SU(3)_c`-singlet, which alone rules out identifying it
with a Pati-Salam `4`/`4̄`. What this round adds specifically: under the
standard `4⊗4̄=1⊕15` branching, the adjoint `15` ALSO contains an
`SU(3)`-singlet piece (`15=8⊕3⊕3̄⊕1`), so the known 2-dim `SU(3)`-trivial
block `k_vec` lives in could a priori have been the genuine `SU(4)`-
singlet OR the singlet-inside-the-adjoint. This round determines WHICH:
`k_vec` sits exactly along the pure `SU(4)`-singlet direction —
**strengthening**, not solely establishing, round92's conclusion, and
closing off the entire `1⊕15` branching (not just the singlet piece) as
a possible rescue for the Pati-Salam-matter-content assumption.

**Net effect:** directly and constructively answers Codex/round105's
item 3 concern with a concrete, twice-adversarially-reviewed computation
— the twisted kernel cannot represent Pati-Salam matter under any
reading of the `SU(4)=SO(6)` action already available in this project's
own machinery. Does NOT reopen or resolve gate G97 (a logically separate,
geometric-realization question). Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`. Not yet
committed to git.

---

### Round108 — Codex item 1: the physically-relevant ambient group for
gate G97 is `G₂` (14-dim) or `SU(3)` (8-dim), NOT the full `SO(7)`
(21-dim) — directly computed, both readings confirmed `<15=dim(su(4))`

Directly computed, rather than merely cited, Codex/round105's own
top-ranked "decisive calculation" — the stabilizer of the FULL background
(not just the round metric) within `so(7)`.

**Method:** built the standard associative 3-form `φ₀` (Bryant 2005
convention, confirmed standard by skeptic review) and all 21 `so(7)`
generators; validated the tensor-action formula against the metric first
(all 21 generators must preserve `g=δ` — confirmed, independently
re-derived by hand by skeptic review too); computed the TRUE stabilizer
dimension of `φ` as the nullspace of the full `35×21` linear map
`X↦X·φ` — **exactly 14**, a UNIQUE dimensional fingerprint for `g₂`
among `so(7)`'s subalgebras (Dynkin classification: `so(6)=15`,
`g₂=14`, `so(5)⊕so(2)=11`, `so(4)⊕so(3)=9`).

**Skeptic pass 1 correctly flagged an overreach:** "stabilizer of `φ`"
(`G₂`) ≠ "stabilizer of the FULL background including the almost-complex
structure `J`" specifically, since `J` is POINT-DEPENDENT
(`J_x(v)=x×v`) — fixing `φ` everywhere doesn't fix a point. **Fixed:**
computed the further subalgebra of the 14-dim `G₂` that ALSO fixes a
base point `x₀` — dimension **8**, matching `SU(3)` (`G₂`'s isotropy at a
point, directly matching `S⁶=G₂/SU(3)`). Skeptic pass 2 independently
re-derived this via the orbit-stabilizer theorem
(`dim(G₂)-dim(orbit)=14-6=8`, since `G₂` acts transitively on `S⁶`) and
confirmed dimension 8 is similarly a unique fingerprint (`G₂` has rank 2,
so any subalgebra has rank ≤2; `su(3)` is the only compact rank-≤2
algebra of dimension 8) — **`CONFIRMED-REAL`**, with an explicit,
retained overreach guard (below).

**Overreach guard, per skeptic pass 2, load-bearing — retained
verbatim:** *"this rules out `SU(4)⊂`Stab(background restricted to the
`S⁶` factor) by naive dimension, but does NOT rule out diagonal
embeddings `SU(4)→G_iso(S³)×G_iso(S⁶)` that split generators across the
product... closes the naive same-factor embedding; diagonal/product
embeddings remain the actual G97 question."** This is exactly round102's
own earlier-flagged "diagonal embedding" possibility, still unaddressed.

**Net effect:** BOTH plausible readings of "the physically relevant
ambient group" (`G₂`=14-dim, or `SU(3)`=8-dim if `J` is required too)
are now directly computed, not merely cited — and both are smaller than
`dim(su(4))=15`, so the same-factor `SU(4)` embedding question is closed
under either reading. The ONE genuinely open route left for gate G97 is
now precisely named: a cross-factor/diagonal embedding combining S³-side
and S⁶-side generators together — not attempted here or in round102.
Does NOT close gate G97. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round109 — the diagonal-embedding question, closed by a general
argument, with two honesty corrections

Attempted the ONE remaining route flagged by rounds 102 and 108: does a
"diagonal" `SU(4)` embedding, combining `S³`-side (`so(4)`, 6-dim) and
`S⁶`-side (`so(7)`/`g₂`/`su(3)`) generators TOGETHER, exist?

**Method — a general argument, not an exhaustive search:** any
Lie-algebra homomorphism `φ:g→h` FROM a SIMPLE algebra `g` is either
zero or injective (`ker(φ)` is an ideal; simple algebras have only
`{0}` and themselves as ideals — confirmed correct by skeptic review
without reservation). `su(4)` is simple (`A₃`); `dim(so(4))=6<15=
dim(su(4))` makes an injective map `su(4)→so(4)` impossible by dimension
count alone. Combining: for ANY homomorphism
`φ=(φ₁,φ₂):su(4)→so(4)⊕X`, `φ₁` is FORCED to be the zero map — for
every possible embedding, no case-by-case search needed. Every `su(4)`
embedding into `so(4)⊕X` therefore collapses entirely to a same-factor
embedding into `X` alone, already closed by rounds 102/108.

**Skeptic review: `WEAKENED`, two honesty corrections accepted, core
argument unchanged:**
1. The script's own Killing-form check (non-degenerate) establishes
   `su(4)` is SEMISIMPLE, not SIMPLE — a genuine gap, caught via a clean
   counter-example (5 copies of `su(2)`, dim 15 total, also semisimple
   but not simple). `su(4)`'s actual simplicity is a standard,
   well-established classification fact (`A₃`), cited here, not
   independently derived by this round's own computation.
2. The proof rigorously closes ONLY the Lie-algebra-homomorphism reading
   of "diagonal embedding" (exactly what the Killing-vector algebra of a
   genuine PRODUCT manifold with product metric gives) — it does NOT
   address field-dependent/point-dependent identifications, bundle-
   twisted constructions, or any construction leaving the strict `S³×S⁶`
   product ansatz. **This connects directly to round103's own finding**
   (a block-diagonal/dynamical-torsion construction leaving the product
   ansatz is a standard, legitimate NCG move, not ruled out there) — this
   round's clean no-go, by its own honest scope, does not automatically
   extend to such a construction.

**Net effect — the actual product of rounds 102+108+109 together:**
within the standard `S³×S⁶` product-manifold framework, gate G97's
original conclusion ("no `SU(4)` gauge-algebra realization exists") is
now fully, rigorously, and GENERALLY established — closed for both
same-factor (102/108) and diagonal (109) readings — with the honest
remaining caveat that this framework-internal closure does not extend to
genuinely non-product/twisted constructions, which remains round103's
own still-open fork. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round110 — Codex item 4: build and test the block spectral triple;
one wrong question corrected, one overclaim honestly downgraded

Attempted Codex/round105's item 4: build `D_block=diag(D^0,D^1)` on
`H_block=ℂ²⊕ℂ²` and test the NCG-axiom checklist (bounded, compact
resolvent, grading, real structure, first-order condition, off-diagonal
terms, spectral-action coefficients, block-exchange symmetry).

**Constructed** [VERIFIED-tool]: `D_block=diag(0,0,3c/2,3c/2)`, reusing
E9's own `H=(3c/2)ω` (scalar) — self-adjoint; boundedness/compact
resolvent trivially hold (any finite matrix), honestly scoped as a
finite-dimensional-model artifact, not a claim about the intended
continuum triple.

**Skeptic correction 1:** first draft tested whether a unitary conjugates
`D^0` directly into `D^1` — flagged as the WRONG, needlessly elaborate
question (`D^0=0`, so `T·0·T⁻¹=0` for ANY invertible `T`, trivially).
**Corrected** to the physically meaningful question — does a block-swap
unitary `S=[[0,I],[I,0]]` satisfy `S·D_block·S⁻¹=D_block`? Computed:
`S·D_block·S⁻¹=diag(3c/2·I,0)≠D_block` — confirms no block-exchange
symmetry, via the correct formulation this time.

**Skeptic correction 2 [honest downgrade, not smoothed over]:** this
round's conclusion rests on the SAME two inputs round106 already
established (`H` scalar; `D^0=0`, `D^1=3c/2`) — restated in NCG/block-
spectral-triple language, correctly answering Codex's own checklist item,
but NOT independent confirming evidence beyond round106, despite the
first draft's "genuine cross-check" framing.

**Net effect:** Codex's item-4 checklist is now directly, correctly
answered for the parts this project's own finite/discrete modeling
choice can address (construction, basic properties, swap-symmetry); the
algebra/real-structure/off-diagonal-coupling/first-order-condition/
spectral-action-coefficient parts remain genuinely open, honestly not
filled in with invented, unjustified choices. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

### Round111 — Codex item 6: the actual scalar curvature `Scal(t)`, not
a toy norm — a clean Einstein-Cartan decomposition falls out, physics
conclusion honestly narrowed

Attempted Codex/round105's item 6 (full spectral-action computation) at
its most tractable, always-present leading order: the actual Ricci
tensor and scalar curvature of `∇^t`, replacing round99's own
acknowledged-as-a-toy curvature-NORM-SQUARED quantity.

**Computed** [VERIFIED-tool, cross-validated two independent ways]:
using round99's own `R^t(X,Y)Z=t(t-1)[[X,Y],Z]` and the metric making
`{Z_i}` orthonormal, `Ricci^t` is proportional to the metric (Einstein,
as symmetry predicts) and `Scal(t)=24t(1-t)` — zero at `t=0,1` (matching
the already-established "flat" fact) and MAXIMIZED, not minimized, at
`t=1/2` (value 6). **Mandatory cross-check** against a completely
independent, textbook route (`Ric_LC=-¼·`Killing-form, standard
bi-invariant-metric formula, confirmed correct by skeptic) gives the
SAME value (`Scal_LC=6`) at `t=1/2` — strong evidence the computation
itself is right.

**Genuine structural finding, found by skeptic review, kept as this
round's actual headline:** the numbers decompose EXACTLY as
`Scal(t)=Scal_LC-6·(2t-1)²` — the constant Levi-Civita scalar curvature
of the fixed metric, MINUS a term proportional to `(2t-1)²`, and
`(2t-1)` is exactly this project's own established torsion coefficient
(`T^t=(2t-1)c·vol`). A clean, physically-recognizable Einstein-Cartan-
type split (curvature-of-metric minus torsion-squared), not a
coincidence.

**Skeptic correction — physics conclusion narrowed, not the math:**
first draft claimed this refutes round99's double-well hope for "any"
gravitational/spectral action — skeptic correctly rejected this as
overreach: the genuine Einstein-Hilbert term of the metric ALONE is the
CONSTANT `Scal_LC=6` (the metric itself doesn't change with `t,` only
the connection does); a real Einstein-Cartan action treats the metric-
curvature and torsion-squared pieces as SEPARATE terms with
INDEPENDENTLY-determined coefficients this project has never derived
from an actual action. The bare `Scal(∇^t)` computed here corresponds to
one specific (not obviously privileged) choice of that coefficient — a
genuinely different sign choice could still produce a double well.
**Corrected scope:** this round shows `Scal(∇^t)` itself is single-
humped; it does NOT close off every possible gravitational-action
reading of round99's hope, but it DOES replace a vague "compute the full
spectral action" task with a precise, well-defined open question (derive
the actual torsion-squared coefficient from a real action principle).

**Net effect:** a clean, doubly-cross-validated mathematical result with
an honestly narrowed physics conclusion — sharper than round99, not a
final closure. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round112 — closing OB8: the 2 mixed-`U(1)_Y` channels round96 never
computed; skeptic finds the closure is near-tautological, not new evidence

MASTER_TZ_RDR22 Phase 0 (Freeze) produced a `CLAIM_LEDGER.yaml`/
`OPEN_BLOCKERS.md`/`DERIVATION_GRAPH.yaml`/`SUPERSEDED_RESULTS.md`/
`CURRENT_STATE_ROUND111.md` registry (5 files, `tom_s3_spinor_toy/`), and a
currency re-check of an externally-pasted summary table's row 17 surfaced
that round96's own correction note (added after Codex's round105 review)
already recorded `[SU(2)_L]²U(1)_Y` and `[SU(2)_R]²U(1)_Y` were never
computed — logged as `OPEN_BLOCKERS.md`'s OB8.

**Computed** [VERIFIED-tool, sympy]: both conditions, for `t=0` alone,
`t=1` alone, and union, reusing round92's per-endpoint representation
content and round93+round94's `Y=T3R+(B-L)/2`, `B-L=0` unchanged. **All
four values are exactly 0.** A sanity check (same formula applied to the
known SM field content) reproduces the SM's own known
`[SU(2)_L]²U(1)_Y` cancellation exactly, confirming the formula itself.

**Skeptic review: arithmetic `CONFIRMED-REAL`, framing `WEAKENED`.** The
skeptic independently re-derived all four values by hand and found the
formula correctly applied — but identified that each zero traces to a
**different, individually trivial** mechanism (an `SU(2)` factor being a
singlet, or `U(1)_Y` degenerating into an internal `SU(2)_R` Cartan
generator once `B-L=0`), not a nontrivial cancellation between competing
rep content. Sharpened finding: at `t=1`, `Y≡0` identically given round94's
own `B-L=0` — so **every** mixed-`U(1)_Y` anomaly condition (round96's
three plus this round's two) is forced to zero there by one shared
structural fact, not five independent confirmations (see
`SUPERSEDED_RESULTS.md` SR5 — round96's own three `t=1` zeros are
retroactively reread this way, nothing computational retracted).

**Net effect:** OB8 closes as `FAIL`, extending round96's verdict to the
full 5-condition mixed-`U(1)_Y` set — but the skeptic's correction means
this closure carries less new discriminating power than the pre-registered
kill criterion implied; it mostly confirms what round94's `B-L=0` already
entailed. Round100's "anomaly route exhausted" framing remains correctly
scoped to the mixed-`U(1)_Y` class only — cubic non-abelian channels
(`[SU(2)_L]³`, `[SU(2)_R]³`) remain untested. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

### Round113 — reconciling the two `t`-parameter conventions
(`PARENT_ACTION_GATE.md` field F3): resolved, not a symbol-overload error

A newly-drafted `PARENT_ACTION_GATE.md` (a pre-registered checklist for any
future OB1/OB2 attempt, per the user's own requested next step) flagged a
specific, concrete risk in its own F3 field: `preprint.tex`/round67-68's
Kostant Dirac-operator shift `D_{S³}(t)=D_{S³}^{\mathrm{LC}}+(t-\tfrac12)h_H`
and round99/round111's Cartan-Schouten curvature
`R^t(X,Y)Z=t(t-1)[[X,Y],Z]` had never been shown to use the same `t`.

**Computed** [VERIFIED-tool, sympy]: built round67's own stated connection
`∇^t_X Y := t[X,Y]` directly, derived the standard curvature tensor from
it, and checked it against round99/111's own formula on all 27 independent
basis triples — **exact match**, plus the torsion definition matches
round67's own stated `T^t=(2t-1)[X,Y]`, plus an independent Jacobi-identity
hand-derivation confirms the same result.

**Skeptic review: `WEAKENED`, load-bearing gap identified and closed by a
direct follow-up, not smoothed over.** The initial check only verified one
direction — that round67's connection PRODUCES round99/111's curvature
formula — not that round99/111's own construction actually USED that
connection (the map connection→curvature is not injective in general, so
agreement alone doesn't prove identity). **Closed directly**: reading
round99's own original script (not round111's later reuse) shows it
explicitly defines `nabla_t(X,Y,tt)=tt*[X,Y]` and derives its `R^t` from it
— the literal same construction, confirmed by source-read, not assumed.

**Net effect:** F3 is resolved, not a live risk — round67/68's Dirac-
operator zero modes and round99/111's curvature computation describe the
SAME connection family, usable together without a translation step. This
does not itself supply a parent action (OB1's central question is
untouched) — it removes a real, if ultimately benign, prerequisite risk
before either OB1 or OB2 proceeds. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round114 — OB1 mechanism search: a claimed literature cross-check,
`FALSIFIED` — the elaborate computation was a citation in disguise

User selected OB1 (mechanism search among untried candidates) over OB2 at
an explicit checkpoint. `100_DIRECTIONS_BRAINSTORM_2026-07-17.md`'s own
adversarial critique flagged items 21/25 (compare the whole torsion-
connection family, check whether coefficients originate from an action) as
highest-priority. Found `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`
(arXiv:2203.02961) — already downloaded in this repo, never read in
rounds 67-113 — classifying invariant/Killing spinors on
`S^{2n+1}=SU(n+1)/SU(n)`, including `n=1` (`S³=SU(2)/{e}`, round67's own
presentation), with an explicit 1-parameter torsion-connection family
(`Proposition 3.17`).

**Computed** [VERIFIED-tool, sympy]: the Clifford representation from this
paper's own §2.1 formulas, confirmed `{eᵢ,eⱼ}=-2δᵢⱼ`, built
`D^s(ψ_+)=s/2-3/2` from the paper's own `Theorem 3.13`/`Proposition 3.17`
— magnitude `3/2` at `s=0`, matching round67's own cited Levi-Civita
eigenvalue; zero crossing at `s=3`. First-draft label: "genuine independent
cross-check."

**Skeptic review: `FALSIFIED`, the strongest correction of any round this
session — not merely narrowed.** The construction `D=Σeᵢ·A(eᵢ)·ψ`
algebraically collapses to `-tr(A)` regardless of any Clifford-
representation convention choice (since `A` is diagonal in this basis and
`eᵢ²=-1` always) — meaning the entire matrix-building apparatus was
**decorative**: the computed `3/2` is derivable in one line directly from
the paper's own `Corollary 3.14` (`λ₁=λ₂=1/2`, itself a restatement of the
classical Friedrich 1980 round-`S³` Killing constant, the same fact
round67 already cites via this project's own G4/G8 gates). **Two sources
correctly stating the same textbook number is not two independent
computations agreeing** — no new evidence was actually produced.

**Net effect:** relabeled `REPRODUCTION_OF_FRIEDRICH_1980_VIA_AHL2023_
KILLING_CONSTANT`, logged in `null_results/INDEX.md` (`Round114-AHL2023`).
One disconnected minor fact survives (zero-crossing `s=3` in AHL2023's own
parameter, not linked to round67's `t`). New standing methodological
lesson recorded in `pearl_registry/INDEX.md`: before accepting any future
"literature cross-check" round, verify the result is NOT derivable in one
line directly from the cited source's own stated theorem — if it is, the
elaborate surrounding computation adds no evidence regardless of its own
internal correctness. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round115 — OB1 continued: does the S³ flux quantization (already
established, Hodge corollary) select `t=0,1`? Circular for unconditional
selection, but a genuine, honest near-miss pearl surfaces along the way

Tested whether identifying the S³ torsion `T^t` with this project's own
already-established, topologically-quantized `H³(S³)` flux
(`lambda-dim-gate/decision.md`'s Hodge corollary, also `preprint.tex`
line 1117) supplies a parent-action-level selection principle, applying
round114's own lesson (check for circularity BEFORE building elaborate
machinery) up front, pre-registered in `claim.md`.

**Computed** [VERIFIED-tool]: `Vol(S³_ρ)=2π²ρ³` (direct integration);
schematic flux-quantization condition `(2t-1)cVol(S³)=2πnQ`; **circularity
test** — a real positive `ρ₃` solving this condition exists for `t=0`,
`t=1`, **and** for `t=1/3` and `t=7` alike, confirming the mechanism
cannot distinguish `t=0,1` from arbitrary other targets without an
independent fix on `ρ₃`.

**Skeptic review: `CONFIRMED` the NULL, with two documented weakenings and
one factual gap — all addressed, not smoothed over.** (1) The round had
skipped the sharper, physically relevant numerical check at a *naturally
motivated* `ρ₃` — added: using `c=-2` (directly recomputed, same frame as
round99/111/113) and this project's own candidate stabilization value
(**G94, `ρ₃≈1.93`**, gates G94-G102) with a standard NS-NS quantization
normalization, `K=|c|πρ₃³/Q ≈ 1.1408` — 14% from the nearest integer.
(2) The round's original "restates F6, does not close it" framing
undersold real, non-vacuous content: a falsifiable `(t,ρ₃)` correlation
formula. (3) **The round's original claim that `ρ₃` is a "fully free,
unstabilized modulus" was itself too strong and grep-corrected**: a
candidate mechanism (G94) does exist, though it is itself conditional on
an admittedly free coupling (`c_S3`, its own decision.md line 76) — the
circularity concern is not resolved, only pushed back and compounded (the
`K≈1.14` near-miss now rests on three stacked, independently-unverified
inputs).

**Net effect:** genuine NULL for unconditional `t`-selection — but a
precise, falsifiable `(t,ρ₃)` relationship and an honestly-caveated
`K≈1.14` near-miss are logged as a Pearl (`pearl_registry/INDEX.md`),
worth recomputing if a future, non-coupling-conditional `ρ₃`-stabilization
result ever appears. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`; does not
reopen the already-closed `λ`-origin question (same flux, different role).

---

### Round116 — OB1 continued: the minimal-crossing-pair structure — an
equivalent restatement, not new information, with one real gap surfaced

Applied brainstorm item 28 ("spectral flow, `N_gen=SF{D(u)}`") in a
modest, honest form directly to round67's own already-computed `D^t`
crossing values (`t*∈{-2/3,-1/3,0,1,4/3,5/3}`) — not a new technique, a
structural reading of numbers already on record.

**Computed** [VERIFIED-tool]: generalized round67's tabulation to a
symbolic closed form for all `n≥0`: `t*(n,+1)=-n/3`, `t*(n,-1)=n/3+1`.
Proved (not spot-checked) that the six crossings are evenly spaced at
exactly `1/3`, symmetric about `t=1/2`, and that `t=0,1` (the `n=0` pair)
are the UNIQUE innermost crossings, with no crossing strictly between
them, for all `n`.

**Skeptic review: `WEAKENED`, three findings.** (1) The round's own
`n=0..19` spot-check for "no interior crossing" was redundant — the
general closed form already proves it for all `n` in one line of algebra;
methodologically weaker presentation than the argument already available,
though not wrong. (2) **Real content gap, accepted:** the `(n,σ)`
parametrization silently drops the `(n+1)(n+2)` eigenspace multiplicity at
each crossing — matters the moment "spectral flow" (inherently
multiplicity-weighted) is invoked even informally, as this round's own
title does. (3) **Framing overclaim, corrected:** everything in the
structural claims follows in one line from `D^t` being affine in `t` with
SCALAR slope `h_H=3` — this is an **equivalent restatement**, not a
"sharper characterization" as first framed; symmetry, even spacing, and
"n=0 innermost" are generic consequences of any monotonic affine family,
not new derived content.

**Net effect:** the numerical facts stand (correctly, for all `n`, not
just spot-checked values), but the round adds essentially no new
information beyond repackaging round67's own tabulation — logged
honestly, not oversold. The multiplicity gap is recorded as a
methodological Pearl for any future formal spectral-flow attempt. Does
not affect $N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

### Round(s) — Phase-0 registry gap fix: round80/E14's `Z2` left-right
isometry result, missing entirely, now added

While searching OB1 for a new candidate (does a discrete `Z2` symmetry
force `t=0,1` coexistence), found that round80 (E14) — a substantial,
already-completed exploration of EXACTLY this idea, done earlier in this
same long session before the Phase 0 registry was written — was **entirely
absent** from `CLAIM_LEDGER.yaml`/`PARENT_ACTION_GATE.md`. This is the
second such omission this session (see round94/OB3, `SUPERSEDED_RESULTS.md`
SR6). Round80's own genuine result: a tool-verified isometry
`iota(g)=g^{-1}` pulls back the WHOLE Cartan-Schouten family exactly
(`iota*(∇^t)=∇^{1-t}` for all `t`), but gauging it as an orbifold
identification forces `t=1/2` uniquely — killing that specific route.
Three physical readings tried, none succeed; Reading 3 (Left-Right-
symmetric model-building analogy) is the only one pointing the right
direction but sits in unreconciled tension with Lemma L5. Fixed: added
`CLAIM_LEDGER.yaml` `C18`, a `PARENT_ACTION_GATE.md` F4 entry, and
`SUPERSEDED_RESULTS.md` SR7 (sharpening SR6's lesson: substantial rounds
completed BEFORE the registry-writing pass are the ones most likely to be
missed — grep `experiments/` first). Also flagged, not fixed
(`OPEN_BLOCKERS.md` OB9): the preceding E7-E12 chain (rounds 72-78) is
committed but not individually registered either.

---

### Round117 — attempting to reconcile round80's own flagged tension
(Reading 3 vs Lemma L5): the attempt tested the wrong question

Tried to resolve round80/E14's one genuinely open thread — does S³'s
`iota`-parity (Reading 3) really conflict with Lemma L5's unconditional S⁶
chirality fixing? — via a candidate distinction: `SU(2)_L×SU(2)_R` is
gauged (round90), `S⁶`'s orientation is not, so "demand parity" applies
to one but not the other.

**Computed** [VERIFIED-tool]: `S⁶`'s orientation-flip, mirrored directly
against round80's own `iota` construction, lies in the SAME disconnected
`O(7)\SO(7)` component that `iota` occupies in `O(4)\SO(4)` — both
"ungauged" in the narrow sense of not being in the connected isometry
group this project's gauge construction uses.

**Skeptic review: `FALSIFIED`, the "resolution attempt fails" label was
not an earned conclusion.** "In the disconnected component of the
isometry group" is **not** the same question as "is a symmetry of the
physical action" (the actual criterion Reading 3's Left-Right-symmetric-
model logic needs — real parity in physics is exactly the counterexample:
never gauged, still a genuine action-symmetry with real consequences).
Separately, the two `Z2`'s act on structurally different data — `iota`
exchanges frame/gauge-multiplet labels; `S⁶`'s orientation sets a
chirality-OPERATOR sign — which may not even be comparable objects.
Round80's own Section D also found `iota` is never invoked by any
established mechanism, while `S⁶`'s orientation IS (Lemma L5 cites it
directly) — a possibly more relevant asymmetry this round's test never
checked.

**Net effect:** this round kills only a narrow strawman ("`iota` is
literally inside the gauged continuous `SO(4)`") that nobody was actually
defending — round80's real tension (Reading 3 vs Lemma L5) remains
**exactly as open as before**, genuinely untouched, not advanced. Logged
honestly (`null_results/INDEX.md` `Round117-L5Reconciliation`), with a new
methodological Pearl: isometry-group component membership is an
insufficient proxy for physical symmetry/mechanism relevance. Does not
affect $N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

### OB1 parked; new phase begins — 13D→4D spinor decomposition audit

Per the user's own strategic assessment of the master-TZ status, OB1 was
formally marked `PARKED` (not closed — reopen conditions specified in
`OPEN_BLOCKERS.md` OB1 and `parked/INDEX.md`), and the project moved to a
new phase: the gauge/Hilbert/triality closure program, starting with a
13D→4D spinor decomposition audit.

**Reframing caught before writing anything:** the task's own proposed
framing ("`Spin(1,12)→Spin(1,3)×Spin(3)×Spin(6)`") was checked against
`preprint.tex`'s own "Total dimension is 13, not 10" open-problems entry
— which had ALREADY caught and corrected exactly this conflation (no
`Spin(1,12)` structure exists; standard supergravity caps at 11D; no
consistent 13D parent theory is claimed). Flagged to the user before
writing; user confirmed reframing to what the project actually has: a KK
product ansatz (4D spacetime × S³ internal × S⁶ internal), not a unified
higher-D spacetime.

**`SPIN13_TO_SPIN4_DECOMPOSITION.md` written**, consolidating already-
established facts (no new computation) against the requested 5-item
checklist. **Mandatory skeptic review corrected 3 of 5 items on first
draft, all accepted:**
1. Item 1 (32-state dimension): first draft asserted "matches CCM" without
   showing the reconciling arithmetic — added: `32=16 (particle content)
   +16 (CPT conjugates)`, the standard CCM finite-triple convention
   (flagged `[WEAK]`, not independently tool-verified against primary CCM
   sources).
2. Item 2 (reality conditions): first draft's "gap found" rested on a
   4-term grep — skeptic correctly called this insufficient negative
   evidence. Broadened to 12 terms across `preprint.tex` AND every
   `experiments/` file; the gap **survived** the broader search (found
   hits are about a different question — `SU(2)` gauge-representation
   pseudo-reality for anomaly cancellation, not the geometric spinor
   bundle's own reality-type classification). Logged as new
   `OPEN_BLOCKERS.md` OB10.
3. Item 3 (chirality): first draft claimed Lemma L5 stands as a
   standalone `ESTABLISHED` PASS — skeptic correctly noted `sign(ind)=+1`
   is only physically meaningful if `ind≠0`, and the FULL operator (not
   just S⁶'s) has no zero mode at all (KT-8) — **downgraded to
   CONDITIONAL**, inheriting KT-8's own status.
4. Item 4 (particle/antiparticle vs. generation counting): first draft
   asserted the 3 triality channels are "structurally distinct" from the
   32-state content without evidence — skeptic flagged this as exactly
   the project's own known "index-to-count jump" trap. Checked directly
   (`experiments/20260621-g73-three-channel-dirac/decision.md`): the 3
   channels ARE genuinely separate bundle constructions (`ind(D_{S⁶}⊗E)`
   computed independently for `E=8_v,8_s,8_c`), not internal relabelings
   — PASS confirmed, now with cited evidence.

**Net effect:** revised overall verdict is PASS on 2 of 5 (down from the
first draft's overclaimed 3), CONDITIONAL on 2, OPEN on 1 (new). Logged
as `CLAIM_LEDGER.yaml` C19. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

### Round118 — matter-generation factorization test: two skeptic passes,
one genuine audit-gate violation self-caught and fixed

Item 3 of the gauge/Hilbert/triality closure program. Tested the user's
own proposed hypothesis (`H_physical=H_matter⊗H_generation`, `S⁶`-kernel
in the generation factor, `(4,4̄)` in a separate matter factor, triality
on generation, gauge on matter) against the user's own pre-registered
kill-test.

**First draft:** concluded `BLOCKED_AT_CONSTRUCTION_STAGE` — citing gate
G97 and a dimension-counting argument (the 1-dim twisted kernel can't
factor nontrivially).

**Skeptic pass 1: `FALSIFIED` the severity.** G97 is specifically about
GAUGED `SU(4)` Pati-Salam unification — the round applied it too broadly
to a hypothesis that could equally be read via the ALREADY-realized
`SU(3)_c×SU(2)_L×SU(2)_R` gauge group (untouched by G97). Also attacked a
strawman reading of "kernel lives in the generation factor" (as if
`H_generation` IS the 1-dim kernel, rather than a 3-dim space with one
slot per triality channel). Recommended splitting into STRONG (genuine
`SU(4)`) and WEAK (already-realized gauge group) readings.

**Revision:** added a direct test of the WEAK reading — but asserted, in
a code comment, that the charge formula has no per-channel index
"without independently re-grepping it in this script," then used that
unverified assertion as load-bearing evidence for "the WEAK reading is
already true."

**Skeptic pass 2: `FALSIFIED` this new claim on the project's own
audit-verification-gate rule.** An honestly-labeled "not verified"
assertion is still an assertion — it should have been a stop sign to
actually check, not a license to proceed with the caveat attached.
Separately found a deeper, independent gap: even granting charge-
uniformity, this is **necessary, not sufficient** for genuine tensor
factorization — also needing identical internal block structure, no
Dirac-operator channel-mixing, and triality acting with no admixture on
the matter factor. None of these three are checked anywhere in this
project.

**Fixed directly:** `grep -n "8_v\|8_s\|8_c" preprint.tex | grep "Q\s*=\|
Y\s*=\|T_{3"` → zero hits, confirming the charge formula has no
per-channel index — the necessary condition IS now genuinely verified,
not asserted.

**Final honest verdict, three-way, per skeptic's own recommended
fallback:** STRONG reading (genuine gauged `SU(4)` `(4,4̄)`) —
`BLOCKED` by G97 (`null_results/INDEX.md` `Round118-STRONG-reading`).
WEAK reading's necessary condition (charge uniformity) — `VERIFIED`.
WEAK reading's full sufficiency (tensor factorization) — `UNVERIFIED`,
genuinely open, not a dead end (`OPEN_BLOCKERS.md` OB11). **Standing
lesson:** asserting a claim in a code comment with an honest "not
verified" caveat, then treating it as load-bearing anyway, is its own
distinct failure mode from simply forgetting to check — the caveat
itself should trigger the check, not excuse skipping it. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

## Round119 — Triality distinguishability gate: applying an already-built rubric surfaces a registry overclaim, caught by skeptic

**Gauge/Hilbert/Triality closure program, item 4.** Rather than build a new
gate from scratch, recognized that `tom_s3_spinor_toy/L3B_SPIN8_INTERFACE_
SPEC.md` (drafted 2026-07-15, extended same day through an `SO(4)×SO(4)`
block-chirality candidate) already **is** a fully-built triality
distinguishability gate — precise question, five-condition existence spec,
anti-circularity screen, PASS/PARTIAL/NO/DISQUALIFIED rubric all present.
The genuine gap was that this rubric had never been formally applied to its
own most-advanced result, and the project's registries (`OPEN_BLOCKERS.md`
OB4, `CLAIM_LEDGER.yaml` `C_G67C3_THIRD_CHANNEL`) still described the state
as flatly "not internally derivable," understating the `SO(4)×SO(4)` finding.

**First draft applied the rubric and landed on `PARTIAL`.** Mandatory
context-asymmetric skeptic review (claim.md + gate document only, no
reasoning chain) returned `WEAKENED`, with three concrete findings:

1. Condition 2 (`[D,U]=0` for the *physical* Dirac operator) was downgraded
   to "not independently re-verified" — understating that the source's own
   G74A discussion shows the relevant proof technique (Lemma B) "does not
   degrade gradually with perturbation size; it simply no longer applies, at
   any nonzero perturbation" once `G₂` breaks, which the `SO(4)×SO(4)` route
   requires. Not merely unchecked — the source's own tooling cannot check it.
2. Condition 3 was claimed "Holds, verified" in full, conflating the
   algebraic-distinguishability half (genuinely done, per the source's own
   §7 gate 1) with the global/physical half (§7 gate 2, explicitly "the
   blocker, needs Part 5"). Only the algebraic half is established.
3. The cross-connection to round118 contained a hard arithmetic/category
   error: `SU(3)×SU(2)×SU(2)` was claimed to have rank 3 and to "embed inside
   `SO(6)`" — actually rank 4, and `SU(2)_L×SU(2)_R` lives on the `S³`
   factor, not as an `S⁶`-side `SO(6)` subgroup at all. Corrected to a much
   more modest, explicitly unresolved connection.

**Fixed all three inline** in `TRIALITY_DISTINGUISHABILITY_GATE.md` (marked
`[skeptic correction]`, original claims kept visible, not silently
rewritten). **Corrected verdict:** not a flat `PARTIAL` — `GATE 1 OF 7 DONE
/ GATES 2-6 OPEN`, using the source's own sharper §7 gate numbering rather
than forcing the finding into one of the coarser §4 bins. Updated
`OPEN_BLOCKERS.md` OB4 and `CLAIM_LEDGER.yaml` `C_G67C3_THIRD_CHANNEL` to
this corrected, narrower status — avoiding propagating the overclaim into
project state. **Standing lesson:** a generous rubric label sitting next to
already-hedged narrative ("Spin(8)-adjacent", "bare-geometry level") does
not by itself prevent the *label* from overclaiming — check a document's
finer internal framing (here, §7) against its coarser one (§3/§4) directly
before picking a label; "no discrepancy found" is itself a claim requiring
verification, not a safe default. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, `safe_for_runtime=False`, or L3b's overall
open status (unchanged either way).

---

## Round120 — Frame-to-gauge audit: consolidates the gauge/isometry/holonomy mechanism table, catches a genuine tracker staleness and two of its own overclaims

**Gauge/Hilbert/Triality closure program, item 5.** Built
`GAUGE_HILBERT_RECOMPOSITION.md`: a consolidated table naming the exact
geometric mechanism behind each gauge factor this project claims
(`SU(2)_L×SU(2)_R` — isometry-derived, Tom-confirmed; `SU(3)_c` — holonomy-
derived, `G₂/SU(3)` coset; `U(1)_{B-L}` — open, not an isometry generator;
full `SU(4)_{PS}` — blocked, gate G97). Found and fixed a genuine registry
staleness: `docs/gates_tracker.md` (its own header: "Source of truth") had
carried its G10 row ("S⁶ spin connection → SO(6) gauge field... 15
generators") unchanged since 2026-06-17, with no cross-reference to gate
G97's later finding that full `SU(4)`/`SO(6)` as a gauge symmetry is
blocked — read in isolation, the row risks implying a working 15-generator
gauge sector that does not exist. Fixed with an inline caveat citing G97.

**Two of the audit's own first-draft claims were themselves overclaims,
caught by the mandatory skeptic pass:** (1) a claim that round102's
flagged "which metric" subtlety was fully "resolved" by `preprint.tex:464`
— skeptic found this resolves only the metric-identity question (round vs.
not-round), not a separate, genuine framing question (is `SO(7)` or `G₂`
the physically correct ambient isometry group, given the physics depends on
the compatible structure `J`) — corrected to state the narrower, accurate
scope (consequential impact low regardless, since `G97`'s `SO(7)` result
implies the `G₂` case a fortiori by dimension count). (2) a claim that
`docs/gates_tracker.md`'s coverage "stops at the early gates" — directly
checked (`grep -n "^| G9[0-9]\|^| G10[0-9]\|Last updated"
docs/gates_tracker.md`) and found factually wrong: the tracker was kept
current through G106 (2026-07-06); only G97 and its round102/108/109
corroborations (dated 2026-07-17, this session, after the tracker's last
update) are missing — an ordinary same-day lag, not a stopped tracker.

**Standing lesson:** third consecutive round (118, 119, 120) where a
first-draft consolidation claim was more confident than its cited source
supports — consolidation/audit work carries its own overclaim risk,
distinct from new-physics work, and needs the same skeptic discipline.
Does not affect $N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

## Round121 — Independent Round59 reconstruction: candidate source disqualified, near-miss caught, one open avenue surfaced

**Gauge/Hilbert/Triality closure program, item 6.** Investigated whether
`Agricola_2002_Dirac_naturally_reductive.pdf` (arXiv:math/0202094, already
sitting untracked in the repo) could serve as round59's own named
"different primary source" independent-verification rung for its
`rank(D⁺|₁)=1` trivial-sector claim. Found it cannot: a direct grep of
`preprint.tex`'s own bibliography shows this source is already cited
throughout §sec:schur (L4B) for the Kostant-Parthasarathy formula — not
independent of round59's existing derivation chain. Caught this at the
investigation stage, before drafting any claim of independent confirmation
— a near-miss of exactly the "evidence laundering" anti-pattern
`perelman-audit.md` names explicitly.

**A narrower additional observation** (not, as first drafted, an
independently-sufficient second reason — corrected by skeptic review): the
one simplified Casimir-difference formula `preprint.tex` reuses from this
source (`λ²(ρ,σ)=C₂(G₂;ρ)-C₂(SU(3);σ)`) is structurally vacuous on the
trivial sector round59's claim concerns (`C₂(G₂;trivial)=0` gives no useful
bound) — precisely why round59 needed its own dedicated computation. But
skeptic correctly flagged that Agricola2002's *separate* Theorem 4.2
(constant-spinor non-vanishing, `H·ψ≠0`) was never checked against this
specific question — a genuinely open, distinct avenue, not folded into the
"vacuous" conclusion. Deliberately not pursued this round (would require
careful `(g₂,su(3))` root-system computation, risking a rushed derivation
error).

Confirmed no alternative CAS (Sage/Maple/Mathematica) is available in this
environment — only Python/sympy, the same interpreter round59's own three
routes already used.

**Honest conclusion:** none of round59's own three named verification
rungs (different CAS, different primary source, external human review) is
currently available or applicable within this session. Round59's
`[VERIFIED-INDEPENDENT-INTERNAL]` status is unchanged — neither
strengthened nor weakened. Fourth consecutive round (118-121) where a
first-draft claim needed a skeptic-caught correction, this time on a
negative/cautionary finding rather than a positive one — the discipline
holds either way. Does not affect $N_{\mathrm{gen}}=3$,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.

---

## Round122 — Global recomposition audit: headline claim confirmed unchanged, audit catches its own overclaim and a real hidden premise

**Gauge/Hilbert/Triality closure program, item 7** (last audit before item
8, preprint rewrite). Applied the project's own Recomposition Gate to
`CLAIM_LEDGER.yaml` and `DERIVATION_GRAPH.yaml`'s `D2_NGEN3_FULL_CHAIN`,
checking whether the two newest claims (`C19` spinor decomposition, `C20`
matter-generation factorization) needed to be added as premises, and
whether `preprint.tex`'s public text still accurately reflects the
project's internal state.

**Core finding: `N_gen=3` remains `CONDITIONAL`, unchanged.** `C19` and
`C20` are correctly parallel/explanatory investigations, not premises the
counting argument (`ind=1`, `dim ker=1`, channel count) depends on — `OB11`
(C20's open sufficiency question) is absorbed by `C_G67C3`'s own already-
open status, not a separate new gap. Found `preprint.tex`'s L3b Open
Problems text is stale (understates, doesn't overclaim) — it never
mentions the `SO(4)×SO(4)` partial advance from round119, queued as a
precise punch-list item for item 8, not applied here.

**Skeptic review of the audit itself caught two real problems:** (1) the
first draft claimed "no smuggling found anywhere in the ledger" when only
4 of 22 claims (`C19`, `C20`, `C_G67C3`, plus the newly-added `C21`) were
actually traced against `D2` — corrected to the narrower, accurate scope.
(2) A genuine hidden premise: `DERIVATION_GRAPH.yaml`'s own `D2` inference
text cited `sign(ind)=+1 (proved, G74B)` as part of the counting argument,
but this had no `CLAIM_LEDGER.yaml` entry and was missing from `D2`'s own
premises list — exactly the "hidden ingredient" failure mode the
Recomposition Gate exists to catch, missed by the audit's own first pass.
Fixed directly (added `C21_G74B_CHIRALITY_SIGN`), not deferred, since it's
a ledger-accuracy fix rather than a public-facing edit.

**A second self-correction, caught only by direct tool verification:**
the fix's own first attempt said "21 entries" (an off-by-one miscount,
missing that `C_G67C3_THIRD_CHANNEL` has no numeric prefix) — caught by
running `grep -c "^  - id:"` before finalizing rather than trusting the
recount, giving the correct 22.

**Standing lesson:** a recomposition audit is itself subject to the
overclaim risk it exists to catch. Fifth consecutive round (118-122)
where skeptic review corrected a first-draft consolidation claim — this
time a meta-level audit auditing itself. Does not affect
$N_{\mathrm{gen}}=3$, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`.

---

## Round123 — Preprint rewrite (item 8, final): L3b updated, skeptic catches structural-obstruction euphemism

**Gauge/Hilbert/Triality closure program, item 8 — final item.** Executed
round122's one concrete punch-list item: added a paragraph to
`preprint.tex`'s L3b Open Problems entry describing the `SO(4)×SO(4)`
block-chirality candidate (round119) that algebraically distinguishes all
three triality channels for the first time in this investigation.

**Skeptic review of the new manuscript text** (held to the same bar as
internal files, arguably higher since this is public-facing) found every
mathematical claim accurate against source, but caught real information
loss in the compression: the first draft's "physical Dirac operator
remains consistent... once G₂ is broken" read as an ordinary future-work
caveat, when the actual situation is sharper — the existing proof of the
*exact* kernel dimension (G74A's Lemma B) uses Schur's lemma on *exact*
`G₂` symmetry, a technique that doesn't merely need re-checking once `G₂`
breaks but **structurally no longer applies at any nonzero breaking**, with
no `Spin(4)×Spin(4)`-equivariant analogue available. Skeptic's own framing:
"promoting a structural obstruction... to a procedural caveat... these read
the same to a skimming reader but mean different things to a careful one,
and preprints get read carefully." Also caught a compressed physical-
identification gap (which `SO(4)` factor, if either, is `S³`'s actual gauge
group is entirely unaddressed by the construction) and undefined notation
(`H`, `ℓ`) that the internal spec's thicker context could get away with but
a standalone public paragraph could not.

Fixed directly, not deferred — rewrote the closing section of the new
paragraph to name both obstructions precisely. Compiled clean:
`pdflatex` ×2, exit 0 both passes, 30 pages, no undefined references.

**This completes the entire 8-step gauge/Hilbert/triality closure
program** (park OB1 → `SPIN13_TO_SPIN4_DECOMPOSITION.md` → matter-
generation factorization → `TRIALITY_DISTINGUISHABILITY_GATE.md` →
`GAUGE_HILBERT_RECOMPOSITION.md` → independent round59 reconstruction
attempt → `GLOBAL_RECOMPOSITION_AUDIT.md` → this preprint update).
`N_gen=3` remains exactly as `CONDITIONAL` as it was at the start of this
arc — six rounds (118-123) of substantial work, zero change to the
headline claim's logical status, one genuine editorial gap closed, one
ledger-accuracy gap found and fixed, and six consecutive rounds where
mandatory skeptic review caught something a first draft missed. Does not
affect `lambda=FREE_COUPLING_PARAMETER` or `safe_for_runtime=False`.

---

## Round124 — SU(3)-coordinate triality distinguishability candidate: a second, cleaner route to Gate 1

**User-requested follow-up** to the gauge/Hilbert/triality closure
program: a new distinguishing-structure candidate built from `SU(3)`
representation-theoretic coordinates (per the user's explicit choice
among several candidate interpretations), not the octonion `H⊕Hℓ` split
used by round119's `SO(4)×SO(4)` construction.

**Found:** `su(3)⊕u(1)⊕u(1)` — `SU(3)` (the isotropy group of
`S⁶=G₂/SU(3)`) combined with its own 2-dimensional abelian centralizer in
`so(8)` (already computed by gate G102, dimension only, never combined
with `su(3)` before) — gives `Hom=0` for **all three** off-diagonal pairs
among the triality representations `8_v,8_s,8_c` (a direct Schur-lemma
proof of pairwise non-isomorphism, cleaner than the `SO(4)×SO(4)` route's
explicit chirality-matching argument) and fixes **zero** vectors in `8_v`
(also escapes confinement to `SO(7)`, the rank ceiling that killed every
`su(3)`/`g₂`/`so(6)`/`so(7)`-subgroup candidate up to now).

**Verification, tool-side and independent of the skeptic pass:** re-ran
the computation myself (the skeptic agent used for review lacked Bash
access and could only trace the code analytically — per this project's
own `audit-verification-gate.md`, that alone wasn't accepted as
sufficient). Directly confirmed: `su(3)` alone fixes exactly 2 vectors in
`8_v` (the expected control), and — the one thing the skeptic pass
flagged as needing empirical rather than analytical confirmation — the
`Hom=0` result is invariant under rotating the 2-dimensional centralizer
basis (checked with two independently-chosen rotation angles), confirming
it depends only on the centralizer's linear span, not on an arbitrary
choice of orthonormal basis.

**Same remaining obstruction as `SO(4)×SO(4)`, not a further advance
toward closing L3b:** `g₂` is simple (zero center), so this centralizer
sits outside `g₂` — realizing it physically would also require breaking
`G₂`, triggering the identical G74A Lemma B obstruction documented in
round119's own gate application. Two independent, structurally different
candidates now both reach the same milestone (`GATE 1 OF 7 DONE`) —
strengthens confidence that this gate is robust, but Gates 2-6 (physical
identification, dynamical consistency) remain exactly as open as before.

Updated `TRIALITY_DISTINGUISHABILITY_GATE.md`, `OPEN_BLOCKERS.md` OB4, and
`CLAIM_LEDGER.yaml`'s `C_G67C3_THIRD_CHANNEL` to cite the second candidate.
Does not affect $N_{\mathrm{gen}}=3$'s `CONDITIONAL` status,
`lambda=FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
