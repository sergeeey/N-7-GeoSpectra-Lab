# Open Blockers Registry

**Purpose:** genuinely open items, each with what would resolve it. Phase 0
(Freeze) deliverable per MASTER_TZ_RDR22 Section 21. Companion to
`CLAIM_LEDGER.yaml` (status per claim) and `SUPERSEDED_RESULTS.md` (what
changed). Ordered roughly by how directly each blocks the `N_gen=3` headline.

---

## OB1 — KT-8: no zero mode for the full S3xS6 Dirac operator (blocking)

**What's open:** the untwisted (Levi-Civita) S³ connection gives the full
internal Dirac operator on `S³×S⁶` zero zero-modes. A torsion-deformed S³
connection (`t≠0`) is a mathematically available escape route, but **no
selection principle** is known for *which* `t` (or whether both `t=0,1`
together) is physically required.

**What would resolve it:** a "parent action" — some action/symmetry/anomaly/
topology principle that forces a specific `t` (or forces `t=0` and `t=1`
together) rather than leaving it as an arbitrary choice. This is the target of
the entire round62-111 search (see `CURRENT_STATE_ROUND111.md`).

**Current best lead:** round111's `Scal(t)=Scal_LC-6(2t-1)²` decomposition
sharpens the question to: what is the actual sign/magnitude of the
torsion-squared coefficient in a real gravitational or spectral action (not
yet derived from first principles)?

**Owner / next step:** open; `/boyko-goal-expansion-100`'s remaining ~90
untried candidates (non-geometric flux, generalized/doubled/exceptional field
theory, discrete torsion, cobordism invariants — see the skill's own
2026-07-17 report) are the next place to look if the Pati-Salam route (OB2)
doesn't reopen.

---

## OB2 — D4: does "two coexisting D's" even make sense as a spectral triple?

**What's open:** round103 found this genuinely unresolved, not closed. `t`
indexes the spin connection, a spectral-triple geometric datum; a
block-diagonal `D=diag(D^0,D^1)` construction (round110's toy) is a
legitimate NCG move per round105's cross-model audit, but nothing yet shows
it corresponds to an actual physical S³×S⁶ construction with a first-order
condition, correct off-diagonal terms, or spectral-action coefficients.

**What would resolve it:** either (a) a properly specified non-product
spectral triple that satisfies the standard NCG axiom checklist (only
partially checked so far, round110), or (b) an argument that the product
ansatz genuinely cannot be left this way, closing the route negatively.

**Owner / next step:** Codex's own item 5 (promote `t` to a finite
matrix-valued order parameter with internal Z2 exchange symmetry) — proposed,
never attempted.

---

## OB3 — B-L operator on the twisted kernel (not constructed)

**What's open:** B-L is only defined as a post-hoc label on the *untwisted*
S⁶ weight space (`bl_charge()` in `g6_spinor_decomposition.py`; the `BmL`
matrix in `g15_hypercharge.py` commutes with `su(3)⊕u(1)`, 9 of the full
15-dim `so(6)` algebra, not the whole algebra — gate G98). No construction of
B-L directly on the twisted kernel (the physical, dim-1-per-channel,
G2-singlet Hilbert space) exists.

**What would resolve it:** a multi-lens pass on this exact question was run
this session (`/multi-lens` on "can B-L be built as an operator directly on
the twisted kernel"); its findings were not yet folded into a formal
experiment round as of this Phase 0 pass — check the multi-lens output (in
this session's transcript, not yet written to a file) before re-deriving from
scratch.

**Owner / next step:** write up the multi-lens findings as a proper
`experiments/<id>/claim.md`+`decision.md` round; currently only exists as
conversational output.

---

## OB4 — C_G67C3: the third triality channel (8_v) is a model postulate, not derived

**What's open:** G102 found no fiber symmetry large enough for a Spin(8)-Schur
argument to coexist with the S⁶ geometry — the third channel required for
`N_gen=3`'s "×3" step is a **model postulate** for Tom Lawrence's specific
framework, not internally derivable from this project's own geometry alone.

**What would resolve it:** either an independent physical argument for why
the postulate should hold (not attempted), or accepting `N_gen=3` as
conditional on this specific, named, falsifiable assumption indefinitely.

**Owner / next step:** genuinely blocked without new input; flagged as one of
the two irreducible open premises in `DERIVATION_GRAPH.yaml`'s D2 chain.

---

## OB5 — Public-wording consistency check (not re-verified this pass)

**What's open:** `reports/CLAIM_BOUNDARY_AUDIT_2026-06-25.md` found `N_gen=3`
stated as unconditional/derived in several files (`README.md`,
`tom_s3_spinor_toy/README.md`, `RESEARCH_STATUS_REPORT.md`) as of 2026-06-25.
`RESEARCH_STATUS_REPORT.md` itself was since patched (its own 2026-07-17
correction section, verified present this session). Whether `README.md` (root
and `tom_s3_spinor_toy/`) and `preprint.tex`'s headline sections were
similarly patched was verified for the **abstract/headline sync specifically**
(memory record `p0-headline-sync-2026-07-17`, done 2026-07-17, not committed
at that time) but a fresh, complete re-grep against the June 25 audit's exact
HIGH-1/HIGH-2/MEDIUM-1/MEDIUM-2 findings was **not** re-run in this Phase 0
pass.

**What would resolve it:** a focused grep pass — `grep -rn "N_gen.*=.*3\|three generations" README.md tom_s3_spinor_toy/README.md tom_s3_spinor_toy/preprint.tex` — checking each hit against the current conditional status, plus re-checking HIGH-1 (the "in collaboration with Tom Lawrence" phrasing).

**Owner / next step:** natural Round-2-style follow-up task, cheap (grep +
read, no new computation) — flagged rather than done here to keep Phase 0
strictly a consolidation pass, not a new audit.

---

## OB6 — Codex items 5 and 8 (never attempted)

**What's open:**
- **Item 5:** promote `t` to a finite matrix-valued order parameter with
  internal Z2 exchange symmetry (see OB2 above — same underlying question).
- **Item 8:** separate global-vs-local anomaly conditions after the spin-lift
  construction (round107) — not attempted at all.

**Owner / next step:** both are explicit, named, ready-to-run next steps from
round105's cross-model audit; neither requires new infrastructure.

---

## OB7 — round111 uncommitted

**What's open:** `tom_s3_spinor_toy/experiments/20260717-round111-codex-item6-scalar-curvature-action/`
(claim.md, decision.md, script) plus the corresponding
`reports/PROJECT_360_ROUND3_SYNTHESIS.md` round111 section are written to disk
but not yet committed to git — no explicit "закоммить это" was given for
round111 before the MASTER_TZ document arrived and redirected this session
into the Phase 0 track.

**Owner / next step:** commit alongside (or before) this Phase 0 deliverable
set, on the next explicit user commit instruction. Not a research blocker —
purely a git-hygiene item, listed here so Phase 0's own freeze snapshot isn't
mistaken for reflecting a fully-committed repo state.
