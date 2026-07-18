# Current State — through Round 111 (2026-07-17)

**Purpose:** single authoritative status snapshot, per MASTER_TZ_RDR22 Phase 0
("Freeze"). Consolidates `RESEARCH_STATUS_REPORT.md`'s 2026-07-17 correction,
`reports/PROJECT_360_ROUND3_SYNTHESIS.md`'s round86-111 arc, and this session's
external-fact-check corrections. Does not re-derive anything — every line below
traces to an existing file. See `CLAIM_LEDGER.yaml` for the itemized, tagged
version of the claims summarized here, and `OPEN_BLOCKERS.md` /
`SUPERSEDED_RESULTS.md` for the two companion registries.

## Headline status (unchanged from RESEARCH_STATUS_REPORT.md's own correction)

- **N_gen=3 is NOT YET an established physical result.** G73+G74A+G74B's
  `ind(D_S6⊗S⁻)=1` per channel × 3 channels result on the **S⁶ factor alone**
  is unchanged and correct. **KT-8 (2026-07-16/17)** found the full internal
  Dirac operator on `S³×S⁶` — for the untwisted, Levi-Civita S³ actually used —
  has **no zero mode**. This blocks N_gen=3 from being a massless-4D-fermion
  statement until a selection principle for a torsion-deformed S³ connection is
  found (or some other escape). Total ansatz dimension is 13 (4+3+6), not 10.
- `lambda = FREE_COUPLING_PARAMETER` — confirmed exhausted (G83-G86B, G102-G104),
  never derived. Unaffected by anything below.
- `safe_for_runtime = False` — research only. Unaffected.
- Track A (`cc_toy_lab/`) verdict: `DISCRETIZATION_SENSITIVE` (FINAL, closed,
  independent of Track B). Track C (`paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`)
  frozen 2026-06-30, H0 wins. Neither is touched by the round86-111 work below.

## The KT-8 escape-route search (rounds 62-111), current state

The entire round62-111 arc is a search for **why** the S³-torsion family (Cartan-
Schouten connections `∇^t` on `S³=SU(2)`, parameterized by `t∈[0,1]`, `t=0`↔
left-invariant frame, `t=1`↔right-invariant frame only under `c0=-2`) should
select/require **both** `t=0` and `t=1` sectors together, rather than one
arbitrarily chosen sector — a genuine "parent action" for the S³ torsion
compactification. Two families of candidate mechanism were tried:

1. **External string-theory analogies (rounds 86-89)** — bi-Hermitian sigma
   models, Strominger-Hull/WZW, Killing-spinor cone constructions. **ALL FAIL**:
   each mechanism is tied to a 2D worldsheet structure (chirality, even
   dimension) this compactification does not have. General lesson: "formula
   matched, mechanism didn't transfer" (see `docs/mechanism-transfer-gate` in
   memory).
2. **Pati-Salam gauge/anomaly route (rounds 90-111)** — the substantive,
   spacetime-native line, still active:
   - SU(2)_R is genuinely gauged in `preprint.tex` (round90).
   - The correct anomaly is the cubic `SU(4)³` one, not the Witten SU(2)
     anomaly (round91 self-correction).
   - `K3≡T3R` proven (round93, documentation bug fixed); `B-L=0` on the
     twisted kernel via Leibniz-lift (round94).
   - **Gate G97 — "no SU(4) gauge realization in `Iso(S³×S⁶)`" — now CLOSED**
     within the standard product-manifold framework, three independent ways:
     - Round102: `so(6)≅su(4)` as algebras confirmed, but SU(4)≠SO(6) as
       groups and G2-holonomy≠SO(7)-isometry substitution was a category
       error (skeptic-corrected, `WEAKENED`).
     - Round108: true stabilizer of the associative 3-form `φ` is exactly
       `g2` (dim 14); isotropy at a point is `su(3)` (dim 8) — both `<15`,
       ruling out same-factor SU(4) realization (`CONFIRMED-REAL`, two
       independent computations agree: nullspace + orbit-stabilizer theorem).
     - Round109: general Lie-theory argument — any homomorphism from the
       simple algebra `su(4)` is 0-or-injective; `dim(so(4))=6<15` forces
       the `so(4)` component to zero for **any** `su(4)→so(4)⊕X`
       embedding, closing the diagonal-embedding reading too (`WEAKENED`,
       2 honesty corrections: `su(4)` simplicity is cited not derived here;
       proof covers Lie-algebra homomorphisms of the standard product
       Killing algebra only, not field-dependent/twisted constructions).
   - **Remaining route:** leaving the strict product-manifold ansatz
     (round103's still-open fork — a block-diagonal/dynamical-torsion
     spectral triple is a legitimate NCG move round103 could not rule out).
     Round110 built a toy block spectral triple (no exchange symmetry found,
     but honestly flagged as not independent of round106's inputs). Round111
     computed the actual scalar curvature of `∇^t` — `Scal(t)=24t(1-t)`,
     decomposing exactly as `Scal_LC - 6(2t-1)²` (Einstein-Cartan-style split)
     — single-humped, opposite to round99's hoped-for double well, but this
     narrows (does not close) the open question to one precise target: the
     real sign/coefficient of the torsion-squared term in an actual action.
   - Round96: computed all three anomaly conditions
     (`[SU(3)_c]²U(1)_Y`, `[U(1)_Y]³`, `[grav]²U(1)_Y`) for both endpoints
     separately using the now-fixed `Y=T3R+(B-L)/2` — **none show forcing**
     (`FAIL`). A prose over-claim ("robust to any B-L") was later found FALSE
     by direct computation and corrected (round96/105).
   - Round97: SU(4)-charged content in `preprint.tex` confirmed exhaustive
     (Higgs bidoublet is scalar, irrelevant) — `NO-GO_CONFIRMED`.
   - B-L itself: only defined as a post-hoc label on the **untwisted** S⁶
     weight space (`bl_charge()`), commuting with `su(3)⊕u(1)` (9 of 15
     `so(6)` generators) but not the full 15-dim algebra. No construction of
     B-L directly on the **twisted kernel** exists (multi-lens analysis this
     session; open, see `OPEN_BLOCKERS.md`).
   - A6/A2 (spin-connection equivariance / anomaly inflow at fixed points,
     rounds 101/104): both `BLOCKED`/`NOT_APPLICABLE` — same underlying gap
     (how `ι`'s isometry action lifts to the spinor **fiber**) seen from two
     angles, not independent findings.
   - D4 (product-ansatz coexistence, round103): genuinely unresolved — `t`
     indexes the spin connection (a spectral-triple geometric datum), not a
     gauge-representation choice; "two D's" needs a properly specified
     (possibly non-product) spectral triple.

3. **Independent cross-model audit (round105, Codex/GPT-5.6):** judged the
   Claude-side skeptic had **overcorrected** on both round102(G97) and
   round103(D4) — gauge bosons come from the Lie **algebra**, not group
   topology (so `so(6)=su(4)` IS physically relevant regardless of the
   SU(4)≠SO(6)-as-groups point); block-diagonal Dirac operators ARE standard
   NCG practice. Independently re-verified round96's arithmetic error.
   Proposed 8 follow-ups; items 1-2-3-4-6-7 attempted (rounds 106-111,
   106/107/108/110/111 above); items **5** (t as a finite matrix-valued order
   parameter with Z2 exchange) and **8** (separate global-vs-local anomaly
   conditions post-spin-lift) remain untouched.

## Standing methodological pattern (worth carrying forward)

Mandatory skeptic review (context-asymmetric: claim+code only, no reasoning
chain) caught real errors or overreach in **9 of the last 12 rounds**
(99, 102, 103, 106, 107, 108×2, 109, 110, 111) — almost always narrowing an
overreached physics conclusion while leaving a correct, narrower mathematical
core intact. Two rounds (107, 108) saw the claim **survive strengthened** after
correction rather than narrowed. One round (110) was corrected purely on
evidentiary novelty (restating prior inputs in new language ≠ new evidence).

## What this file deliberately does NOT do

Per MASTER_TZ Phase 0 scope: does not attempt Module reports A-G, an Interface
Audit, Global Recomposition Audit, independent-reconstruction packages, the
13D→4D spinor audit, frame-to-gauge audit, torsion-stability audit, triality-
distinguishability gate, or the RDR 2.2 methodology/pilot track. Those are
explicitly out of scope for this pass — see the Phase 0 plan
(`C:\Users\serge\.claude\plans\dazzling-painting-quail.md`) for the full
rationale and the recommended Phase 1 next step.
