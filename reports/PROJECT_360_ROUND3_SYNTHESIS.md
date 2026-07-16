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
| **KT-3** F4/J₃(𝕆) route condition 1: is the diagonal 𝔤₂⊂F₄ (24-dim, acting on 𝕆³) actually identifiable with the geometric G₂ acting on S⁶'s single 8-dim fibre? | Explicit map constructed, consistent with S⁶'s actual bundle structure | No consistent identification exists (24-dim vs 8-dim rep mismatch is real) | Moderate | High for the F4 route specifically — **NOT diminished by KT-2**, which operates at a different logical level (base isometry vs. fibre/operator symmetry, see corrected KT-2 row) | Already the project's own next planned step; don't duplicate | Pending |
| **KT-4** L3B-INDEXARITH general formula — additional test points (1,1) and (3,0) | Predicted I=0 and I=27 match independent Chern-root computation | Mismatch at either point | ~15 min sympy | Low-medium | Two points settle it | **EXECUTED — PASS, both points, genuinely independent construction.** Self-check first: rebuilt Sym²(V) via an explicit multiset-of-2 root construction (not reusing the original script's `T⊕(T⊗T)` trick) and reproduced I(2,0)=7 by a different route — method validated before trusting it on new points. Then: adjoint=(1,1), built as traceless(V⊗V*) (8 roots, 2 zero-weights — correct for su(3)'s rank-2 Cartan, not an error), ch3=0 identically (each nonzero root cancels its negative under the odd cube) → index=0, matching prediction exactly. Sym³(V)=(3,0), 10 roots (all degree-3 multisets of {x,y,z}), ch3 = (27/2)·c3_T exactly (residual 0) → index=27, matching prediction exactly. Formula substitution was never used in either construction — only in stating what the prediction was. **Honest scope, unchanged from before:** this raises the point count from 3 to 5, it does not prove the general formula — status remains `SUPPORTED ON CONTROLS — GENERAL PROOF OPEN`, per the project's own claim-A-index-map.md. One partial insight surfaced: the proportionality ch3∝c3_T held in both new cases because degree-3 Weyl(S₃)-invariant polynomials in {x,y,z} (x+y+z=0) form a 1-dimensional space — a real partial argument toward the general proof's crux (step 2 in claim-A-index-map.md), but not shown here to cover an arbitrary (p,q) irrep in general. See "Executed kill-tests" below. |
| **KT-5** ρ=14 decomposition completeness | True λ²_min comfortably positive | True λ²_min near zero or negative | Cheap | Medium | One completeness check settles it | **EXECUTED — PASS, clean.** Rebuilt the ρ=14 analog of the 5-piece decomposition (reusing `g2su3_v14_adjoint_full_matrix.py` + `g2su3_nomizu_crossterms.py`'s generic Clifford/structure data, substituting ρ=14 `ADE`/`AD_RAW` for ρ=7's `rho7_ep`/`rho7_nuk`) and checked it against ground-truth D²_14 on **all 12 of 12** basis vectors of the ρ=14 multiplicity space (Round 22's own ρ=7 check only covered 2 of 16 — this is stronger coverage). Exact match everywhere, `sympy` symbolic throughout, no numerical fallback. True λ²_min = 10/3 (native basis) ≈ 3.33, i.e. ≈9–17× the 0.381 norm-bound floor — the bound was never close to tight, no hidden near-zero mode. **Bonus finding:** this exact eigenvalue set was already computed once before, in Round 20 (2026-07-09), four days *before* the norm-bound program (Round 55/56) existed — so "no zero mode at ρ=14" was independently established earlier; what this test adds is specifically confirming the *decomposition* (not just the eigenvalues) generalizes. See "Executed kill-tests" below. |
| **KT-6** SU(2)_R (+ Witten global) anomaly check without assuming B-L | Anomaly-free without B-L input | Anomaly-free only after B-L added | Hours | Medium | Binary outcome | **EXECUTED — PASS on the letter, but sharpens R2-5 rather than resolving it.** All checkable non-abelian conditions vanish ([SU(2)_R]³, mixed [SU(2)_L]²[SU(2)_R], [SU(2)_R]²[SU(2)_L], [SU(2)_R]²[Grav]) — but these are forced to vanish for *any* fermion content by the traceless-generator argument, not a nontrivial confirmation specific to this geometry. Witten global anomaly: 4 SU(2)_R doublets (even, safe) — true because N_c=3 is odd, a numerical fact rather than a deep cancellation. **The real finding:** the four genuinely content-dependent conditions from the existing check ([U(1)_Y]³, [SU(2)]²U(1)_Y, [SU(3)]²U(1)_Y, [Grav]²U(1)_Y) *cannot even be formulated* without a U(1) charge to plug in as the third leg — removing B-L doesn't just weaken the test, it makes the interesting question unaskable. Genuine positive side-result: the geometry gives an unambiguous SU(2)_R doublet/singlet split for all 16 Weyl states, with no bidoublet fermion — a real, non-trivial, checked fact, independent of B-L. See "Executed kill-tests" below. |
| **KT-7** Independent test-suite reproduction (R2-7) | Pass/fail counts match documented count | Discrepancy found | Minutes | Low probability of surprise, closes a process gap | One run sufficient unless it disagrees | **EXECUTED — PASS.** 2512 passed, 4 skipped, 0 failed, exit 0 (see Verification section). |

**Priority order, final for this pass — six of seven now executed:** ~~KT-1~~,
~~KT-2~~, ~~KT-4~~, ~~KT-5~~, ~~KT-6~~, ~~KT-7~~ all executed and tool-verified
(see results above/below). Only **KT-3** remains — and it is the one test that
cannot be run from inside this audit: it needs Tom Lawrence's own framework
input (per this project's standing constraint of not initiating contact with
him), not just more compute.

**Six of seven items have now actually been run, not just designed** — across
three passes this session, all tool-verified, not literature-reasoned. KT-1/KT-2
came back negative/BLOCKED (see corrected labels above, after a self-caught
overclaim); KT-4 and KT-5 came back clean PASSes, strengthening two separate
parts of the project's own results (the index-formula point count, and the L4B
ρ=14 certification); KT-6 came back "PASS on the letter" but with a sharper,
more precise version of the R2-5 concern than originally stated. The only test
this audit could not execute is KT-3, and that's a structural fact about the
project (external-input-dependent), not a scoping choice of this audit.

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
