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
