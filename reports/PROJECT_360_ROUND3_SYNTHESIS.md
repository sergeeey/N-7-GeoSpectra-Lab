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

**KT-8 status: CLOSED, no remaining gap.** Both open items from the initial
write-up are now resolved: (1) the construction is confirmed standard against
an independent published source, not merely self-consistent, and (2) the
vanishing cross-term is now an algebraic theorem, not a numerical observation.
ker(D_{S³×S⁶})=0 for the project's actual construction stands as a fully
verified, tool-and-literature-confirmed result.

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

## KT-10 (2026-07-17) — Does the S⁶ index/kernel construction generalize to the other 3 homogeneous nearly-Kähler 6-manifolds?

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
CH2016's own page-18 basis data is **not internally Hermitian-consistent**:
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

---

**KT-9/10/11 status update:** none of these three have been integrated into
`preprint.tex` — E1 (dimension correction) and E2/E3 (S³ torsion deformation
candidate mechanism) were integrated as dedicated open-problems items
(commits `c2a65c4`, `ec32211`); KT-9/E4 (methodological gap), KT-10/E5
(universality, mixed), and KT-11/E6 (ill-posed) remain standalone findings
in their own experiment folders and in this report only. Full derivations:
`reports/E1_E5_VERIFICATION_ROUND_2026-07-17.md` and the individual
`experiments/20260717-round69/70/71-.../decision.md` files.
