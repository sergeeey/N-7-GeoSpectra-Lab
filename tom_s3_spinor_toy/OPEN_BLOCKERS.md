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
never attempted. **Any future attempt: check against
`PARENT_ACTION_GATE.md` first** (6 additional fields for a non-product
spectral triple — algebra, Hilbert space, Dirac operator, grading, real
structure, physical interpretation — round110's own toy only partially
addressed 2 of the 6).

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
- **Item 5:** promote `t` to a finite matrix-valued order parameter with
  internal Z2 exchange symmetry (see OB2 above — same underlying question).
  Still genuinely ready to attempt whenever OB2 is picked up — no premise
  issue found.
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

## OB9 — E7-E13 chain deserves its own Phase-0-style consolidation pass [flagged, not done]

**What's open:** while fixing round80/E14's registry omission
(`SUPERSEDED_RESULTS.md` SR7), confirmed that the whole preceding chain —
round72 (E7, t-selection principle), round73 (E9, explicit parallel
spinor), round74 (E10, chirality sign link), round75 (E11, Freund-Rubin
torsion link), round78 (E12, multiplicity gate) — is committed to git
(`92e5fb2`) but **not individually represented** in `CLAIM_LEDGER.yaml` or
`DERIVATION_GRAPH.yaml`. Per a global-memory note from earlier in this
session, this chain found: H1 split (H1a REFUTED / H1b PROVED via
holonomy / H1c OPEN), explicit parallel spinors at `t=0,1`, and E12's own
multiplicity gate (`FAIL`, giving 6 not 3 internal modes, no natural
projection) — directly relevant to OB1/`PARENT_ACTION_GATE.md` F4/F7.

**Why not fixed now:** this is a larger consolidation task (5+ rounds,
each needing its own accurate re-citation) than the single-round fixes in
SR6/SR7 — doing it properly means reading each `decision.md` in full, not
a quick registry patch. Flagging rather than rushing a shallow fix.

**Owner / next step:** a dedicated future pass (not part of the current
OB1 mechanism search) should read rounds 72-78 in full and add proper
`CLAIM_LEDGER.yaml` entries + a `DERIVATION_GRAPH.yaml` chain for
"H1a/H1b/H1c t-selection," cross-checked against round80/E14's own summary
of them (already read, this session) for consistency.

---

## OB10 — geometric spinor bundle's own reality/Majorana condition [new, confirmed]

**What's open:** the finite/NCG algebra's real structure `J_F` is
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
