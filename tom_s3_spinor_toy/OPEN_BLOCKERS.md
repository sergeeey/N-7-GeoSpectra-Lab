# Open Blockers Registry

**Purpose:** genuinely open items, each with what would resolve it. Phase 0
(Freeze) deliverable per MASTER_TZ_RDR22 Section 21. Companion to
`CLAIM_LEDGER.yaml` (status per claim) and `SUPERSEDED_RESULTS.md` (what
changed). Ordered roughly by how directly each blocks the `N_gen=3` headline.

---

## OB1 — KT-8: no zero mode for the full S3xS6 Dirac operator [PARKED 2026-07-17]

```
STATUS: PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT
```

**Why parked, not closed:** after rounds 114-117 (4 independent mechanism
attempts, all honestly null/falsified — see below) plus the earlier
round62-113 arc, the search has reached the point of diminishing returns.
Continuing to sweep more internally-generated candidates
(non-geometric flux, doubled/exceptional field theory, cobordism
invariants, `F₄`, `Spin(10)`, etc.) without a new external constraint is
not a good use of further effort right now. Not falsified — the parent
action may well exist — just not found by anything triable from inside
this project's current toolkit.

**Reopen condition (any one of):**
1. A concrete candidate action is found (external literature or new
   internal insight).
2. A directly relevant parent mechanism is published somewhere new.
3. A new derivation map linking geometry → Dirac operator → torsion
   emerges from OTHER work in this project (e.g. the gauge/Hilbert/
   triality closure program below).
4. Any candidate MUST pass `PARENT_ACTION_GATE.md`'s checklist before
   being attempted, not just be "interesting."

**What's open (original framing, preserved):** the untwisted (Levi-Civita) S³ connection gives the full
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
doesn't reopen. **Any future attempt: check against
`PARENT_ACTION_GATE.md` first** — its F3 field (the `t`-convention
question) is now RESOLVED (round113): `preprint.tex`'s `D_{S³}(t)`
Dirac-shift and round99/111's Cartan-Schouten `∇^t` are the same
connection, cite directly rather than re-deriving.

**Attempted, FALSIFIED (round114):** a claimed "independent cross-check"
of round67's `h_H=3` calibration via
`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` (arXiv:2203.02961, a
real, previously-unused, already-downloaded source in this repo) turned
out to reduce algebraically to citing that paper's own already-stated
Killing constant (`Cor 3.14`, itself the classical Friedrich 1980 round-S³
value) — no independent evidence. See `null_results/INDEX.md`
`Round114-AHL2023` and `pearl_registry/INDEX.md`'s new entry (the
"one-line-reducibility test" for future literature cross-checks). Genuine
literature searches in this direction remain worthwhile — this specific
round's SPECIFIC computation, not the whole approach, was the failure.

**Attempted, NULL-with-a-pearl (round115):** tested whether this project's
own already-established quantized `H³(S³)` flux (Hodge corollary,
`lambda-dim-gate/decision.md`) could select `t=0,1` via standard flux
quantization, if the torsion is identified with a genuine NS-NS-type flux.
**Confirmed circular for unconditional selection** (any target `t` admits
some `ρ₃`) — but found, along the way, that `ρ₃` is not actually "fully
free" as first assumed: a candidate stabilization mechanism exists (G94,
`ρ₃≈1.93`, itself conditional on an admittedly free coupling). Plugging
G94's value into the flux-quantization formula gives `K≈1.14` — 14% from
an integer, suggestive but explicitly **not** treated as evidence (rests
on 3 stacked unverified inputs). Logged as a genuine Pearl (recompute if a
future, non-coupling-conditional `ρ₃`-stabilization result appears),
`pearl_registry/INDEX.md`. See
`experiments/20260717-round115-flux-quantization-torsion-selection/decision.md`.

**Attempted, equivalent-restatement (round116):** applied brainstorm item
28 ("spectral flow") in modest form to round67's own crossing family —
proved (general closed form, not spot-check) that `t=0,1` are the unique
innermost, symmetric pair closest to the Levi-Civita point, for all `n`.
Skeptic: this is an **equivalent restatement** of `D^t` being affine with
scalar slope, not new information — and silently drops the `(n+1)(n+2)`
eigenspace multiplicity, a real gap if "spectral flow" is ever invoked
more formally. Logged as a methodological Pearl (multiplicity must be
tracked in any future formal spectral-flow attempt). See
`experiments/20260717-round116-minimal-crossing-pair-structure/decision.md`.

---

## OB2 — D4: does "two coexisting D's" even make sense as a spectral triple? [PARTIAL PROGRESS 2026-08-03]

**Codex's item 5 now attempted — genuine partial progress, not full
resolution.** Round110's own attempt tested the WRONG question (literal
self-invariance of `D_block` under a fixed swap — correctly found
`False`, but that's not the Z2 statement Codex's proposal actually
describes). Promoted `t` to a general rank-1 Hermitian projector `T`
(Bloch-sphere parametrized, not restricted to the diagonal `T=diag(0,1)`
case) and confirmed the CORRECT Z2 statement holds: `D(T)=T⊗H` and
`D(1-T)` are unitarily equivalent via an internal `SU(2)` conjugation
`S_n=m̂·σ` (`m̂⊥n̂`), verified exactly for the diagonal case and via a
numeric spot-check (8 random Bloch-sphere points, residual ~1e-16) for
the general case — realizing Codex's own "off-diagonal fluctuations
possible" language. See
`experiments/20260803-ob2-t-matrix-order-parameter-z2/decision.md`.
**Still open per `PARENT_ACTION_GATE.md`'s 6-field OB2 checklist:** a
naive grading candidate (`γ=(I-2T)⊗I₂`) explicitly FAILS `{γ,D}=0`
(reported honestly, not smoothed over); real structure `J` not
attempted; the physical action (F6) remains entirely unaddressed, as
Codex's own text already flagged.

**Original description (superseded framing, kept for history):**
round103 found this genuinely unresolved, not closed. `t`
indexes the spin connection, a spectral-triple geometric datum; a
block-diagonal `D=diag(D^0,D^1)` construction (round110's toy) is a
legitimate NCG move per round105's cross-model audit, but nothing yet shows
it corresponds to an actual physical S³×S⁶ construction with a first-order
condition, correct off-diagonal terms, or spectral-action coefficients.

**What would resolve it:** either (a) a properly specified non-product
spectral triple that satisfies the standard NCG axiom checklist (only
partially checked so far, round110), or (b) an argument that the product
ansatz genuinely cannot be left this way, closing the route negatively.

**Owner / next step:** grading and real structure remain genuinely open
(see 2026-08-03 update above); the physical action (F6) is the harder,
still fully open task. **Any future attempt: check against
`PARENT_ACTION_GATE.md` first** (6 additional fields for a non-product
spectral triple — algebra, Hilbert space, Dirac operator, grading, real
structure, physical interpretation — now 3 of 6 supplied, 1 attempted-
and-failed, 1 not attempted, 1 stated as interpretation).

---

## OB3 — B-L operator on the twisted kernel [CORRECTED + FORMALIZED 2026-07-17]

**This entry's own original text was WRONG, not just incomplete — flagged
honestly, not smoothed over.** It claimed "no construction of B-L directly
on the twisted kernel exists." This is false: **round94 (E24), already
committed BEFORE this Phase 0 registry was written, constructs exactly
that** — `BL_64 = leibniz64(BmL)` on the 64-dim twisted `Σ⊗Σ` fibre, with
the physical kernel vector `k` confirmed an exact `BL_64` eigenvector,
`B-L=0`. The multi-lens exercise this entry originally referenced was run
BEFORE round94's own result was cross-checked against it, and the
resulting stale framing was carried into this registry without re-verifying
against round94's own decision.md at write time — an audit-verification-
gate lapse in this registry's own construction, corrected here.

**Now formalized:** `BL_TWISTED_KERNEL_CANONICAL_STATEMENT.md`
(`tom_s3_spinor_toy/`) consolidates round94+round107+G98+round61 into one
canonical statement with 5 explicit scope constraints (the specific lifted
operator, the specific zero mode, confirmed-but-irrelevant non-
commutativity with `D_full`, B-L as a constructed not physically-derived
label, and the mode being a genuine `SU(4)` singlet not Pati-Salam matter).
**Nothing new computed** — pure consolidation of already-adjudicated
results, correcting this registry's own error in the process.

**Residual genuinely open items** (per the canonical statement's own "what
this does NOT mean"): whether the physical zero mode should be interpreted
as one particle in a tensor-product bundle vs. a different physical
identification of the two `Σ` factors (round94's own Relaxation Map, still
open); and `B-L`'s own non-uniqueness among a `dim≥3` admissible family
(round61) — no additional physical principle singles it out.

---

## OB4 — C_G67C3: the third triality channel (8_v) is a model postulate, not derived [UPDATED 2026-07-19, round128 + boyko-agent disposition review]

**Disposition, made explicit (2026-07-19):** this OB conflates two
sub-branches with different correct status — splitting them out, per
`boyko-agent`'s go/no-go review of the whole line:

- **Gate 1 (algebraic distinguishability of `8_v/8_s/8_c`) — DONE.** Two
  structurally independent routes reach it (`SO(4)×SO(4)` block-chirality,
  round119; `su(3)⊕u(1)⊕u(1)`, round124, `Hom=0` for all three off-diagonal
  pairs). Round127→128 went further and constructed + verified (machine
  precision, `iso_residual~1e-15`, exhaustive over all 12 members of
  `Aut(su(3))`) an explicit isomorphism `ℂ⊗8_v ≅ Σ`. This is a completed
  **positive** result, not open work — do not re-list it under "open."
- **Gates 2-6 (physical realization) — formally `PARKED`, not open-in-
  progress and NOT `REJECT`/falsified.** Per this project's own Substrate
  Gate (`falsification-ladder.md`: "test could not run ≠ claim failed"),
  a block on unpublished external input (Tom Lawrence's Part 5, which the
  project's own hard constraint forbids soliciting) must never be recorded
  as evidence against the claim. Revival condition: Part 5's actual
  content, or an independent `G₂`-breaking-compatible spectral-gap argument
  (none currently exists). Directly precedented by OB1/KT-8's own park
  decision ("not falsified, just not found — reopen only on new external
  input").
- **B-L physical-identification sub-thread — near-closed.** round126
  (`NO_INDEPENDENT_EVIDENCE`, tautology) + round128 (`NO_LITERAL_MATCH` for
  the first of 12 `Aut(su(3))` candidates) leave one live kill criterion
  (`S_NOT_UNIQUE_UP_TO_SCALE`, only 1/12 checked) — see round128's own
  decision.md Relaxation Map for the cheap follow-up.

Original 2026-07-18 entry preserved below for the detailed derivation
history.


**What's open, current status (`GATE 1 OF 7 DONE / GATES 2-6 OPEN`, per
`TRIALITY_DISTINGUISHABILITY_GATE.md`):** G102 found no fiber symmetry inside
`so(8)` alone large enough for a Spin(8)-Schur argument to coexist with the
S⁶ geometry. But `L3B_SPIN8_INTERFACE_SPEC.md`'s own later work (same day,
2026-07-15) found a genuine advance beyond that: the `SO(4)×SO(4)`
block-chirality construction **algebraically distinguishes all three
channels** (`8_v,8_s,8_c`, not just `v` from `{s,c}`) and is itself
triality-invariant — a rank-4 structure that categorically escapes the
rank-3 `SO(7)` ceiling every earlier candidate hit. This is genuinely more
than "no candidate found" — it is "an algebraic candidate exists; its
physical realization does not." What remains a **model postulate** for Tom
Lawrence's specific framework is narrower than before: whether `SO(4)×SO(4)`
(or an equivalent structure) acts *globally* on the actual compactification
(not just the fiber), and whether the physical Dirac operator is consistent
with it once `G₂` is broken (mandatory for this route) — both explicitly
named "the blocker, needs Part 5" in the source document itself.

**What would resolve it:** Part 5's actual content (unpublished, not
solicited per this project's standing constraint), or an independent
`G₂`-breaking-compatible spectral-gap argument (no such tool currently
exists — this project's own G74A Lemma B explicitly requires exact `G₂`
symmetry and does not degrade gradually).

**Second, independent candidate found (round124, 2026-07-18):**
`su(3)⊕u(1)⊕u(1)` — `su(3)` combined with its own 2-dim abelian
centralizer in `so(8)` (already computed by G102) — gives `Hom=0` for
*all three* off-diagonal channel pairs (direct Schur-lemma non-
isomorphism, arguably cleaner than `SO(4)×SO(4)`'s explicit chirality-
matching argument) and fixes zero vectors in `8_v` (also escapes `SO(7)`
confinement). Verified tool-side, including basis-rotation invariance.
**Same remaining obstruction, not a further advance:** this candidate is
also outside `g₂` (which has zero center, hence no room for an abelian
ideal commuting with its own `su(3)`), so it requires the identical
`G₂`-breaking and hits the identical G74A Lemma B obstruction. Two
independent, structurally different candidates now both reach Gate 1 —
strengthens confidence Gate 1 is robust, does not touch Gates 2-6.

**Are the two candidates secretly the same structure? Checked, answer no
(round125, 2026-07-18):** `SO(4)×SO(4)` (12-dim) and `su(3)⊕u(1)⊕u(1)`
(10-dim), both as subspaces of `so(8)`'s 8-dim vector representation,
share an exact 3-dimensional intersection (two independent SVD methods
agree, tolerance-swept 1e-4 to 1e-12, skeptic-reviewed CONFIRMED). The
shared 3-dim subalgebra is abelian (`u(1)³`, all pairwise commutators
zero to ~1e-15) — genuinely non-generic (generic expectation for a 12-dim
and 10-dim subspace of a 28-dim ambient is exactly 0, not "small"), but
**not** the same structure: `PARTIAL_OVERLAP`, neither identical nor one
containing the other. Does not touch Gates 2-6; does not identify the
shared `u(1)³` with any known physical charge. See
`experiments/20260718-round125-so4xso4-vs-su3-centralizer-comparison/decision.md`.

**Owner / next step:** genuinely blocked without new input; flagged as one of
the two irreducible open premises in `DERIVATION_GRAPH.yaml`'s D2 chain. See
`TRIALITY_DISTINGUISHABILITY_GATE.md` for the full gate application,
`experiments/20260717-round119-triality-distinguishability-gate/decision.md`
for the skeptic-reviewed correction history, and
`experiments/20260718-round124-su3-centralizer-triality-candidate/decision.md`
for the second candidate.

---

## OB5 — Public-wording consistency check [RESOLVED 2026-07-17]

**Re-verified directly** (grep + read, `README.md`, `tom_s3_spinor_toy/README.md`,
`tom_s3_spinor_toy/preprint.tex`, `tom_s3_spinor_toy/preprint_abstract.md`)
against the exact June 25 `CLAIM_BOUNDARY_AUDIT` findings:

- **HIGH-1 (author-line "in collaboration with Tom Lawrence")** —
  **FIXED.** `preprint.tex`'s current author block (line ~55-58) reads only
  "Sergey Boyko, Independent researcher, Ronin Institute for Independent
  Scholarship" — no co-authorship/collaboration claim at the author level.
  `tom_s3_spinor_toy/README.md`'s own Attribution section (line 341-344) is
  unambiguous: "Developed independently by Sergey Boyko... All errors and
  interpretations are entirely my own," plus an explicit "**This is NOT:**...
  Endorsed by Tom Lawrence or affiliated with his research group" fence
  (line 337).
- **HIGH-2 (N_gen=3 stated as unconditional/derived)** — **FIXED** in every
  file checked. Root `README.md`'s own Verdict line (line 23) and
  `tom_s3_spinor_toy/README.md`'s top-of-file correction (lines 11-42)
  both carry the full KT-8 caveat. Every later "N_gen=3" restatement in
  `tom_s3_spinor_toy/README.md` (lines 85, 144, 236 — inside the
  Three-Generation Investigation section) sits under an explicit blanket
  override (line 39-42: "This status correction is authoritative... over any
  'N_gen=3' statement elsewhere in this file that does not carry this same
  caveat") — a deliberate, honest design choice rather than an oversight.
  `preprint.tex`'s own abstract (lines 70-77) states the full-operator
  zero-mode gap caveat inline, in the abstract itself, not just in a later
  section.
- **Residual, minor (not a HIGH-1 violation, but adjacent language worth
  naming):** `preprint.tex:434` and `:1294` still use the phrase
  "collaboration with T. Lawrence" / "to be addressed in collaboration with
  T. Lawrence" to describe an open question awaiting his input. This is
  materially weaker than the original HIGH-1 finding (no co-authorship
  implied, correctly scoped to "his expertise would resolve this"), but given
  the project's own hard "DO NOT INITIATE CONTACT" fence and that no
  confirmed collaboration exists, the word "collaboration" itself is
  slightly more definite than warranted — a candidate one-word wording fix
  ("input from" or "clarification from" rather than "collaboration with"),
  not urgent, not a fence violation.

**Verdict: substantially resolved.** No overclaim found beyond the one
minor wording item above.

---

## OB6 — Codex items 5 and 8 (item 8 re-scoped 2026-07-17; not yet well-posed)

**What's open:**
- **Item 5 [PARTIAL PROGRESS 2026-08-03, see OB2 above]:** promote `t` to
  a finite matrix-valued order parameter with internal Z2 exchange
  symmetry — attempted; the Z2 exchange itself is verified (via the
  correct statement, unitary equivalence of `D(T)` and `D(1-T)`, not
  round110's mis-posed self-invariance test), but grading, real
  structure, and the physical action remain open. Not fully resolved.
- **Item 8 — re-scoped, NOT ready-to-run as originally logged:** Codex's
  exact wording (`codex_review_2026-07-17.md:172-174`) is "If the actual
  gauge group is `SO(6)`, `Spin(6)`, or a quotient of
  `SU(4)×SU(2)_L×SU(2)_R`, global anomalies and permitted representations
  depend on that quotient... The precise global group should be derived
  after the spin lift rather than assumed." **This presupposes `SU(4)` is
  realized as an actual local gauge symmetry of the construction** — but
  gate G97's closure (rounds 102/108/109, `CLAIM_LEDGER.yaml` `C7`) already
  established it is **not**, within the standard `S³×S⁶` product-manifold
  framework (only `su(3)⊕u(1)`, 9/15 generators, is geometrically realized;
  the full `su(4)` doesn't preserve `B-L`, gate G98). Item 8's question is
  therefore contingent on round103's still-open non-product-ansatz fork
  (`C11_D4_PRODUCT_ANSATZ_FORK`) actually succeeding first — attempting it
  now, against the current closed-G97 state, risks the same
  answering-the-wrong-question trap round102's and round103's first drafts
  fell into (see `SUPERSEDED_RESULTS.md` SR4). Surfaced this scoping issue
  during a 2026-07-17 re-read of Codex's exact wording, before starting a
  round — not attempted, deliberately, rather than forced through a shaky
  premise.

**Owner / next step:** item 5 remains ready whenever OB2 is picked up. Item
8 should be re-attempted only after (or explicitly conditional on) OB2/C11
progress — re-read Codex's wording again at that point to confirm the
premise then holds, rather than assuming this note's conclusion is still
current.

---

## OB7 — round111 uncommitted [RESOLVED 2026-07-17]

~~What's open: round111 + the Phase 0 deliverable set written but not
committed.~~ **Resolved:** committed (`6e7c5ac`), merged (`bd4363f`), and
pushed to `origin/main` on 2026-07-17, same day. Kept here (struck through,
not deleted) so anyone reading this file's history sees the item was real
and closed, not silently dropped — matches this registry's own purpose of
tracking status changes honestly (see `SUPERSEDED_RESULTS.md` for the
general pattern this follows).

---

## OB8 — round96's mixed-Y anomaly sweep is incomplete: two channels never computed [RESOLVED 2026-07-17]

~~What's open: round96 only computed three of five mixed-anomaly
conditions...~~ **Resolved by round112 (E26):** computed
`[SU(2)_L]²U(1)_Y` and `[SU(2)_R]²U(1)_Y` for both `t=0,1` endpoints —
both vanish identically at both endpoints and in union
(`FAIL__BOTH_REMAINING_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING__EXTENDS_ROUND96`).
SM sanity check confirms the formula itself is correctly stated.

**Important scope correction, per mandatory skeptic review (kept, not
smoothed over):** the skeptic found this closure carries **far less
discriminating power** than it first appears — each of the four zeros
(this round's two + it retroactively applies to round96's three at `t=1`)
traces to `U(1)_Y` being either identically zero or degenerate with an
internal `SU(2)` Cartan generator at the relevant endpoint, **given the
current frozen inputs** (round94's `B-L=0` specifically) — not to a
nontrivial cancellation between competing, independently-charged states.
Sharpened conclusion: at `t=1`, `Y≡0` identically, so **every** mixed-`U(1)_Y`
anomaly condition (all 5, not just these 2) is forced to zero there for one
shared structural reason, not five separate confirmations. Round100's
"anomaly route exhausted" framing must still **not** be broadened beyond the
mixed-`U(1)_Y` class — cubic non-abelian channels (`[SU(2)_L]³`, `[SU(2)_R]³`)
remain a genuinely untested class.

**Full detail:** `tom_s3_spinor_toy/experiments/20260717-round112-remaining-mixed-y-anomaly-channels/decision.md`.

**New, smaller follow-up surfaced by this closure (not logged as its own
OB — low priority):** a cleaner test of the code's own discriminating power
would use an adversarial input (`B-L≠0` at one endpoint) to confirm the
formula would actually flag forcing if present, since the current FAIL
can't distinguish "no forcing exists" from "the inputs make forcing
undetectable by construction" — a Validation-Theater-Guard-style concern,
not required to accept this closure but worth naming.

**Original description (superseded, kept for history):** round96 only
computed three mixed-anomaly conditions — `[SU(3)_c]²U(1)_Y`, `[U(1)_Y]³`,
`[grav]²U(1)_Y` — for both `t=0,1` endpoints; `[SU(2)_L]²U(1)_Y` and
`[SU(2)_R]²U(1)_Y` were never computed, in round96 or round92.

**Source:** `tom_s3_spinor_toy/experiments/20260717-round96-mixedY-anomaly-with-bl0/decision.md`;
`tom_s3_spinor_toy/experiments/20260717-round112-remaining-mixed-y-anomaly-channels/decision.md`
(correction note, top of file); `CLAIM_LEDGER.yaml` entry `C10_MIXED_Y_ANOMALY_FAIL`
(already scoped correctly to "three conditions," not "all").

---

## OB9 — E7-E13 chain deserves its own Phase-0-style consolidation pass [RESOLVED 2026-07-19]

~~What's open: while fixing round80/E14's registry omission
(`SUPERSEDED_RESULTS.md` SR7), confirmed that the whole preceding chain —
round72 (E7, t-selection principle), round73 (E9, explicit parallel
spinor), round74 (E10, chirality sign link), round75 (E11, Freund-Rubin
torsion link), round78 (E12, multiplicity gate) — is committed to git
(`92e5fb2`) but not individually represented in `CLAIM_LEDGER.yaml` or
`DERIVATION_GRAPH.yaml`.~~

**Resolved:** read rounds 72-78 in full (`decision.md` for each), added 6
new `CLAIM_LEDGER.yaml` entries (`C22`-`C27`, covering H1a/REFUTED,
H1b/PROVED-with-sign-caveat, the sign-convention gap itself, H1c/OPEN, the
SU(2)_L/R representation pattern, and the multiplicity-2 FAIL) and one new
`DERIVATION_GRAPH.yaml` chain (`D4_TORSION_ESCAPE_ROUTE_MULTIPLICITY_
BLOCKED`), cross-checked against round80/E14's own Z2-symmetry finding for
consistency — the iota isometry strengthens E7's algebraic `t<->1-t`
symmetry to a genuine geometric diffeomorphism but does not resolve H1c.

**Headline synthesis (new, from this consolidation, not previously stated
anywhere as a single claim):** the torsion-escape-route program has TWO
independent, currently unresolved blockers, not one — (1) H1c (which of
`t=0`/`t=1` is physically selected, C25, OPEN) and (2) the multiplicity-2
gap (C27, REFUTED as stated — even a selected `t=0` or `t=1` zero mode is
2-dimensional, giving 6 total internal modes across 3 triality channels,
not the needed 3). Resolving (1) alone would NOT complete the program;
(2) is a logically separate problem requiring new physical input (a
reality/Majorana condition, an orbifold projection, or a reconciliation
with `preprint.tex`'s own 32-state SO(4)-spinor convention — none of
which exist in this project yet).

**Prompted by:** external correspondence with Tom Lawrence (2026-07,
message batch referencing his own independent harmonics-on-S³/chirality/
Dirac-to-Weyl-massless-reduction analysis) — this consolidation exists so
a future technical exchange can cite the project's own established
results precisely rather than re-deriving them under time pressure.

---

## OB10 — geometric spinor bundle's own reality/Majorana condition [RESOLVED 2026-08-03]

**Resolved:** built the 16-dim product Clifford module from this repo's own
already-established S³ (`Cl(0,3)`, round67) and S⁶ (`Cl(6,0)`, s6-harm-g0/G13)
generators, per preprint.tex:1467-1480's own stated tensor-product formula.
Found the product signature is actually **mixed, `Cl(6,3)`** (not the uniform
`Cl(9,0)`/`Cl(0,9)` the "3+6=9≡1 mod 8" text below implicitly assumed — the
two established sub-constructions use opposite Clifford sign conventions).
Despite that correction, a direct, adversarially-widened search (256
candidates, `{I,σ1,σ2,σ3}⁴` factorized ansatz) found a unique, Hermitian,
unitary charge-conjugation operator `B`, `B·conj(B)=-I` → **PSEUDOREAL
(quaternionic) type** — matching, not contradicting, the finite algebra's own
`J_F²=-1` (also pseudo-real). No-collapse-checked (reproduced under an
independent, equally-valid Clifford-factor ordering). See
`experiments/20260803-ob10-ko-dimension-majorana-check/decision.md`.

**What this does NOT mean:** does not check `[D_full,B]`/`{D_full,B}` against
the actual differential Dirac operator (only the algebraic Clifford-module
type was checked); does not construct a combined `J=B⊗J_F`; does not touch
OB1/OB2/OB4/OB11 or the `N_gen=3` headline (confirmed free-standing per
`GLOBAL_RECOMPOSITION_AUDIT.md`'s own C19 audit).

**Downstream consequence found 2026-08-06 (C31) — this result was NOT
free-standing after all, in one specific direction.** `B` factorizes exactly
as `B_{S³}⊗B_{S⁶}` with the S³ slot pseudo-real (`−I₂`) and the S⁶ slot real
(`+I₈`) — i.e. the pseudo-reality sits entirely in the S³ factor, which is
also exactly where C27's multiplicity-2 excess lives. That closes the
"new reality/Majorana condition" row of C27's Relaxation Map as a positive
no-go (exhaustive: no compatible REAL antilinear structure exists on that
factor at all). C27 itself remains unresolved. See
`experiments/20260806-ob10-c27-majorana-halving/decision.md`. Note this
does not contradict the C19 audit above, which correctly found OB10 does not
feed `D2`'s zero-mode COUNTING argument — the link found here is to C27's
option space, a different object.

**Original description (superseded framing, kept for history):** the
finite/NCG algebra's real structure `J_F` is
established (`J_F²=-1`, `{J_F,γ_F}=0`, `[D_F,J_F]=0`, `preprint.tex:349`).
But whether the GEOMETRIC `S³×S⁶` spinor bundle itself — independent of
the separately-reconstructed finite algebra `A_F` — satisfies a
compatible reality/Majorana condition is **not addressed anywhere** in
`preprint.tex` or `experiments/`. Confirmed after a 12-term search
(`Killing spinor`, `KO-dimension`, `quaternionic`, `pseudo-real`,
`nearly-Kähler`, `parallel spinor`, `symplectic Majorana`,
`spectrum-symmetric`, and others) across both the paper and every
experiment file — the only hits found are about a DIFFERENT question
(`SU(2)` gauge-representation pseudo-reality, used for anomaly
cancellation; Killing-spinor existence/multiplicity arguments), not the
geometric spinor bundle's own reality-type classification.

**What would resolve it:** determine the KO-dimension of the GEOMETRIC
factor (`S³` has KO-dim 3, `S⁶` has KO-dim 6; product KO-dim would be
`3+6=9 ≡ 1 mod 8` — the quaternionic/symplectic-Majorana regime in the
standard 8-fold KO-periodicity table) and check whether this project's
own spinor bundle construction is consistent with that regime, or derive
the reality structure directly from the explicit Clifford/Pauli
realizations already used throughout rounds 67-117.

**Owner / next step:** surfaced during `SPIN13_TO_SPIN4_DECOMPOSITION.md`
(gauge/Hilbert/triality closure program, item 2 of that audit). Genuinely
new — not previously logged anywhere in this project's registries.

---

## OB11 — matter-generation tensor factorization: necessary condition verified, sufficiency open [PARTIAL, 2026-08-03]

**Condition (i) now VERIFIED, (ii)/(iii) still open.** Scope-clarifying
finding first: `SU(2)_L×SU(2)_R` lives entirely on the S³ factor of
`H_matter` (round90, `preprint.tex:292-310`) and never acts on the
S⁶-side `8_v/8_s/8_c` fiber at all (round119 corrected an earlier false
`SU(3)×SU(2)×SU(2)`-in-`SO(6)` embedding claim) — so condition (i)'s
`SU(2)_L×SU(2)_R` part is vacuous (the S³-side factor is identical
across channels by construction); the only substantive part is
`SU(3)_c`. Directly verified by diagonalizing the quadratic Casimir of
G102's own already-established `su(3)` action on each channel: all three
(`8_v,8_s,8_c`) give an IDENTICAL spectrum (2 zero + 6 equal-nonzero
eigenvalues, matching the predicted `1⊕1⊕3⊕3̄` pattern), not just an
equal-dimension `Hom`-count as before. See
`experiments/20260803-ob11-internal-block-structure-check/decision.md`.
Conditions (ii) (no channel-mixing in the Dirac operator) and (iii)
(triality acting purely as `1⊗t`) remain open — (ii) specifically
requires assembling a genuinely new channel-decomposed differential
Dirac operator, entangled with the still-open OB1 (per the 2026-07-19
substrate-check below), not attempted this round.

**Original description (superseded framing for condition (i) alone, kept
for history — (ii)/(iii) below are unaffected and still fully open):** the user's own proposed hypothesis
(`H_physical=H_matter⊗H_generation`, WEAK reading: `H_matter`=32-dim
already-realized `SU(3)_c×SU(2)_L×SU(2)_R` content, `H_generation`=3-dim
triality-channel label) has one necessary condition **verified**
(`grep`-confirmed, `preprint.tex`): the charge formula `Q=T₃L+Y` has no
per-channel index, so the gauge group acts uniformly across all 3
triality channels. **But this is necessary, not sufficient** — a genuine
tensor factorization also requires (i) identical internal block
structure of the 3 32-dim blocks, not just identical charges, (ii) no
channel-mixing terms in the full Dirac operator, (iii) triality acting
purely as `1⊗t` with no admixture on the matter factor. **None of these
three are checked anywhere in this project.**

**Note — the STRONG reading (genuine gauged `SU(4)` Pati-Salam matter,
`(4,4̄)`) is separately BLOCKED** by gate G97 (see
`null_results/INDEX.md` `Round118-STRONG-reading`) — this OB is only
about the WEAK reading, which remains a live, partially-checked
candidate, not a dead end.

**What would resolve it:** check the Dirac operator's block structure
across the 3 triality channels (`8_v`,`8_s`,`8_c`) for cross-channel
mixing terms.

**Substrate check (2026-07-19, `boyko-agent` disposition review) — the
"likely extractable from round107/round110" claim below does NOT hold,
verified by direct read:** round110's Dirac object is a 4×4 constant-
spinor toy (`D_block=diag(0,0,3c/2,3c/2)`) for the `t=0/t=1` torsion
block — it contains no `8_v/8_s/8_c` channel structure at all. round107
computes the 15 `so(6)=su(4)` generators Leibniz-lifted onto the 64-dim
`Σ⊗Σ` fibre (the SU(4)-orbit of the twisted kernel) — a different
construction from the Cl(0,8)-built `v/s/c` reps where the triality
channels actually live (G102/round124/127/128). **Neither file contains a
channel-decomposed physical Dirac operator with off-diagonal
`8_v↔8_s↔8_c` blocks.** This OB's own "cheap, well-scoped follow-up"
label below is therefore substrate-unverified and should not be treated
as ready — resolving it requires *assembling* a channel-decomposed
physical Dirac operator (a new, not-yet-costed construction), which is
also entangled with the still-open OB1/KT-8 full-operator question.

**Owner / next step:** NOT cheap as originally labeled (see substrate
check above) — requires scoping as its own SMALL–LARGE round if pursued,
not a quick extraction. Full detail (superseded "cheap" framing):
`experiments/20260717-round118-matter-generation-factorization-test/decision.md`.
