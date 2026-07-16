# Project 360° Scientific Red Team — Round 1: Claim Ledger

**Date:** 2026-07-15
**Scope:** Track B (`tom_s3_spinor_toy/`) primary; Track A (`cc_toy_lab/`) and the
third track (`paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`) light cross-check only.
**Method:** synthesis of existing project artifacts (not re-derivation) + targeted
file/line verification of current claim wording. No new experiments run, no code
changed. See `.claude/plans/dazzling-painting-quail.md` for the full 6-round design;
this is Round 1 only.

**Evidence markers used below:** `[VERIFIED]` = confirmed by Read/Grep this session;
`[INFERRED]` = logical conclusion from verified facts, chain stated.

---

## A. Atomized N_gen=3 dependency chain

Starting decomposition follows the project's own published structure
(`README.md`, `tom_s3_spinor_toy/preprint.tex §sec:open`), not a fresh derivation.
Each row's status was checked against the cited file, not taken from memory.

| ID | Statement | Status | Evidence | Depends on |
|---|---|---|---|---|
| L2-INDEX | ind(D_S⁶⊗S⁻) = 1 per triality channel (α = v,s,c) | **PROVED** | `preprint.tex:1227-1234` (L3a); experiment `E-L3-PARTIAL` | — |
| L3B-EQUIV | E_v ≅ E_s ≅ E_c as G₂-equivariant bundles; no G₂-invariant op distinguishes channels | **PROVED** | `preprint.tex:1236-1245`, Theorem `thm:elb3`; `experiments/20260625-l3b-bundle-obstruction/` | — |
| L3B-EXHAUST | No continuous symmetry inside 𝔰𝔬(8) at all commutes with the geometric G₂ action (dim 𝔠_{so(8)}(g₂)=0) — full internal search space exhausted, not just the G₂-equivariant subcase | **PROVED** | `preprint.tex:1241-1245`; gate G102 (2026-07-05); `null_results/INDEX.md` row `G102` | L3B-EQUIV |
| L3B-INDEXARITH | No irreducible SU(3) twist gives index exactly 3 (jumps 1→7); no G₂-invariant-connection reducible bundle gives exact (3,0) kernel without extra mirror modes | **PROVED** | `preprint.tex:1246-1254`; experiments `20260715-index-formula-s-tensor-t-candidate`, `20260715-round-su3-index-map-audit` (both dated today) | — |
| L3B-SPIN8-GAP | Distinguishing the 3 channels requires an external Spin(8) fibre-symmetry **postulate** not derivable from the present geometric construction | **OPEN — this is the load-bearing gap** | `preprint.tex:1254-1260`; `L3B_SPIN8_INTERFACE_SPEC.md` (full spec document, drafted 2026-07-14) | L3B-EXHAUST + L3B-INDEXARITH |
| L3B-F4-ROUTE | Candidate: F₄ = Aut(J₃(𝕆)) ⊃ Spin(9) ⊃ Spin(8); triality realized as an *inner* automorphism (S₃ permuting octonion slots) once the ambient algebra is enlarged from 𝔰𝔬(8) to 𝔣₄ | **OPEN, actively worked today** — "condition 1" (algebraic existence of the S₃ automorphism) closed; conditions 2-5 (does this correspond to an operator on the *physical* Dirac construction, does it commute with the *physical* D) explicitly **not done** | `L3B_SPIN8_INTERFACE_SPEC.md:54-169`; own text: *"this is a candidate ROUTE, not a solution"* (line 123-124); a same-day naive attempt at building the map already hit a proven no-go (E-L3B) and the doc explains why (lines 139-163) | L3B-SPIN8-GAP |
| L4A/L4B-KERNEL-TRIVIAL | dim ker(D⁺\|₁) = 1 on the trivial component | **Internally certified** by 3 independent routes (from-scratch reimplementation blind to original code; full-fibre completeness+Hermiticity audit; closed-form analytic derivation) — **external review outstanding** | `preprint.tex:1277-1308`; `experiments/20260714-round59-trivial-rank-certification/` | L2-INDEX |
| L4B-NONTRIVIAL | Non-trivial G₂-isotypic components: ρ=7 established, ρ=14 strongly supported (one flagged, honestly-scoped sign caveat), all higher ρ certified by a proven general bound (Round 55/56) | **CERTIFIED**, same external-review caveat as above | `preprint.tex:1277-1300`; `parked/INDEX.md` row `L4B-HIGHER-REPS` (STATUS: CLOSED, Round 56) | L4A/L4B-KERNEL-TRIVIAL |
| CHIRALITY | sign(ind) = sign(c₃) = +1 → left-handed zero-mode excess, geometric SM chirality | **PROVED**, unconditional (survives regardless of L3B-SPIN8-GAP outcome) | G74B, PROMOTE 31/31 (memory + `README.md:258`) | L2-INDEX |

### Recomposition Gate check (falsification-ladder.md § Step 8a)

**Question:** does {L2-INDEX + L4A/L4B-KERNEL + CHIRALITY}, all individually proved
or internally-certified, license the headline "N_gen = 3" as commonly stated —
or does the recomposition silently smuggle in the still-open L3B-SPIN8-GAP?

**Verdict: the recomposition does smuggle it in, but the project's *own current*
primary sources already say so explicitly and correctly** — this is not a new
defect, it is a check that the honest framing is intact:
- `preprint.tex` table (line 1142): `N_gen=3` listed as **"Conjectured (Atiyah-
  Singer L2; L3 open)"**, not proved.
- `preprint.tex` title itself: *"Toward Three Generations..."* — conditional framing
  at the top level.
- `preprint.tex:1163-1171` §Comparison states outright: "N_gen=3 is *conjectured*,
  not derived... conditional on the open channel-independence problem (L3b)."
- Root `README.md:23`: "N_gen = 3 (arithmetic exact; depends on open gate G67-C3...)".

**This is the correct verdict for `preprint.tex` and root `README.md`.** It is
*not* the correct verdict for two other files still in the public claim surface —
see Section C.

---

## B. What Round 1 did *not* re-derive (by design)

- The 37 entries in `null_results/INDEX.md` and 5 in `parked/INDEX.md` — these
  already carry Kill Analysis / revival conditions and were spot-checked for
  internal coherence only (G102, G43-B5→G48, L4B-HIGHER-REPS chains all read
  consistently across files).
- The `pearl_registry/INDEX.md` (41 entries, 26 still `pending`) — not
  individually re-scored this round; flagged as a Round 2 task (check for
  high-`impact_score` pearls past their `next_check` date).
- Track A's own 26-claim registry (`CLAIMS_REGISTRY.md`) — already `ALL_SUBSETS_
  VERIFIED`, dated 2026-06-30, internally consistent on spot-check; not re-audited.

---

## C. Public claim-surface consistency (follow-up to `reports/CLAIM_BOUNDARY_AUDIT_2026-06-25.md`)

The June 25 audit found 3 HIGH + 2 MEDIUM findings. Re-checked against current
file state (2026-07-15, ~3 weeks and ~40 experiments later):

| June 25 finding | Current status | Evidence |
|---|---|---|
| **HIGH-1** — "In collaboration with Tom Lawrence" (authorship-adjacent) | **FIXED** | `preprint.tex` author block (lines 50-60) lists Sergey Boyko solely. The two remaining "collaboration" mentions (`preprint.tex:404`, `:1259`) are forward-looking and correctly conditional: *"the remaining open question, to be addressed in collaboration with T. Lawrence"* — describes what confirming the open input would require, not a present claim of collaboration or endorsement. |
| **HIGH-2** — N_gen=3 stated stronger than L3 state in `README.md` (root), `tom_s3_spinor_toy/README.md`, `RESEARCH_STATUS_REPORT.md` | **PARTIALLY FIXED — new instance found** | Root `README.md` and `tom_s3_spinor_toy/README.md` now correctly hedge (see §A). But `RESEARCH_STATUS_REPORT.md:321` still reads *"Three generations — **RESOLVED** (G73+G74A+G74B). N_gen=3 **exactly**..."* and `:348` *"N_gen=3 **EXACTLY** (G73-G74B)"* — both dated "Updated 2026-06-22," i.e. **predate gate G102 (2026-07-05)**, which is the result that proved the Spin(8) postulate is NOT internally derivable. This file was updated elsewhere (line 202 has the correct, current 2026-07-05-dated hedge: *"N_gen = 3 from geometry + one explicit postulate"*) but lines 321/348 were never revisited — a live instance of the **Type-4 "lag" failure** named in `research-methodology.md` § Классификатор (new NULL/finding not applied retroactively to older claims in the same document). |
| **HIGH-3** — `preprint_abstract.md` stale, contradicts `preprint.tex` | **STILL OPEN, now worse** | `preprint_abstract.md` header says "Draft: 2026-06-21 (revised)" — predates G102, round59 kernel certification, and the F4 route entirely. Body text unconditionally states *"We prove N_gen = 3 exactly..."* and *"This is a zero-parameter prediction: no SM input is used to locate ρ_min"* — no conditional framing, no mention of L3b/G67-C3 at all. This file is still linked from root `README.md:239` ("Preprint abstract (T1/T2 theorems)") as a documentation-map entry, so a reader following that link gets the strongest, least-hedged version of the claim in the entire repository. Also uses "zero-parameter" language the user's own memory record flags as the wrong term (`boyko-knowledge-audit-preprint.md`: should be "zero-fit"). |
| **MEDIUM-1** — stabilization wording overstates parameter status | Not re-checked this round (lower priority; scoped for Round 2 if time permits) | — |
| **MEDIUM-2** — markdown claim-audit test misses current risk phrases | Not re-checked this round | — |

### New finding (not in June 25 audit): third-track paper's abstract states a negative result that is easy to misread against Track B

`paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md` abstract states: *"a physics rescue
track showing that S³×S⁶ with R > 0 cannot produce chiral fermions or three
generations via known mechanisms (gauge bundles, flux, orbifolds, non-commutative
geometry)."* [VERIFIED, abstract text]

This sentence is technically scoped correctly (the parenthetical excludes the
twisted-Atiyah-Singer-index mechanism Track B actually uses — matching
`CLAIMS_REGISTRY.md`'s own footnote¹ on the same underlying result). **But** a
full-text search of this paper for any mention of `tom_s3_spinor_toy`, "Track B",
"N_gen", "Atiyah", or "twisted index" returns **zero matches** [VERIFIED, grep].
This paper never cross-references Track B at all. An external reader who finds
this standalone preprint (it is a public-facing artifact in its own right, not an
internal note) has no way to learn that a separate, later, different-mechanism
result in the same repository reaches the opposite conclusion for the same base
geometry S³×S⁶ — the four-word parenthetical "via known mechanisms" is the *only*
thing preventing a direct-seeming contradiction, and it isn't reinforced anywhere
else in the document. This is a **publication-architecture gap** (the user's Lens
10), not a scientific error in either paper.

---

## D. Track A / third-track light cross-check

- **No leakage found** [VERIFIED, grep across `tom_s3_spinor_toy/README.md`,
  `RESEARCH_STATUS_REPORT.md`, `preprint.tex`, `preprint_abstract.md` for
  `DISCRETIZATION_SENSITIVE`/`cc_toy_lab`/`Gate 4B`]: Track B does not cite Track
  A's numerical results as support for anything. Clean separation maintained.
- Track A's own claim boundary (`README.md` "Current Claim Boundary" table) is
  explicit and already honest — no further action needed this round.
- Third track: see the new finding in §C above; otherwise frozen and internally
  consistent on a quick read.
- One stale/superseded intermediate file noticed in passing:
  `PHASE4_GEOMETRY_RECOVERABILITY_SYNTHESIS.md` (dated 2026-06-29, "NOT frozen,
  PARTIALLY_REPRODUCED") appears superseded the very next day by
  `CLAIMS_REGISTRY.md` (2026-06-30, "ALL_SUBSETS_VERIFIED"). Not urgent — flagging
  for Round 2/6 housekeeping (candidate for an explicit "superseded by" note or
  removal), not a scientific finding.

---

## E. Live branches ranked for Round 2 (expert-lens attacks)

1. **L3B-SPIN8-GAP / L3B-F4-ROUTE** — the one mathematically load-bearing open
   gap in the whole N_gen=3 chain, and it is being actively worked *today*.
   Highest value target for the rep-theory + index-theory + adversarial-reviewer
   lenses: is the F4/J₃(𝕆) route a real physical mechanism or (per the document's
   own honest self-assessment) "bookkeeping, not physics"?
2. **L4A/L4B-KERNEL** external-review-outstanding status — good target for the
   spectral-analysis + software-verification lenses (can a from-scratch outside
   agent reproduce the 3 internal certification routes independently, per the
   Context Asymmetry rule?).
3. **Public claim-surface fixes from §C** — cheapest, highest-certainty-of-impact
   items: update `RESEARCH_STATUS_REPORT.md:321,348` and `preprint_abstract.md`
   to match the current honest position, and add a one-line cross-reference from
   the third-track paper's abstract or a footnote pointing to the Track A/B
   distinction already made in `CLAIMS_REGISTRY.md`.
4. **Gauge sector / B-L** — `preprint.tex:395-406` already flags that SU(4) is
   not among the isometries and B-L requires field-content input beyond the
   present construction; worth a dedicated phenomenology-lens pass in Round 3.

---

## F. Limitations of this Round 1 pass

- This is a synthesis of existing, already-adjudicated project artifacts plus
  targeted current-state verification — it is not an independent re-derivation
  of any piece of mathematics, and does not itself constitute the "expert lens
  attacks" (geometry/index/rep-theory/spectral/physics/phenomenology) the full
  360° design calls for. Those are Round 2+.
- The pearl registry (41 entries) and the 37 null-results were checked for
  cross-file coherence, not individually re-verified.
- Track A and the third track received only a leakage/consistency check, not a
  numerical audit (matches the scope decision in the plan; their verdicts are
  already closed and honest).
