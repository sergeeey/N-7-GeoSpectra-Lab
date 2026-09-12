# Open Blockers Registry

**Purpose:** genuinely open items, each with what would resolve it. Phase 0
(Freeze) deliverable per MASTER_TZ_RDR22 Section 21. Companion to
`CLAIM_LEDGER.yaml` (status per claim) and `SUPERSEDED_RESULTS.md` (what
changed). Ordered roughly by how directly each blocks the `N_gen=3` headline.

**Compressed 2026-09-12** (was 2923 lines). Every round's full derivation —
every C-number, every skeptic pass, every self-caught bug — is preserved
verbatim in `.claude/memory/history/OPEN_BLOCKERS-archive-2026-09-12.md`.
The full chain for any item is also its own permanent record in
`experiments/<id>/decision.md` (the FL-mandated artifact) — this file only
synthesizes the CURRENT status, it does not re-derive it.

---

## OB1 — KT-8: no zero mode for the full S³×S⁶ Dirac operator [PARKED 2026-07-17]

The untwisted S³ connection gives zero zero-modes on the full internal
operator; a torsion-deformed connection (`t≠0`) is available but nothing
selects which `t` (or whether `t=0,1` together) is physically required.
**PARKED — reopen only on new external input.** Every internally-buildable
route this project can construct from its own content has been tried and
converges on the same wall: the missing ingredient is triality-channel
information nothing internal supplies. Major lines exhausted: the
bordism/Pin-structure chain (C127-C131, four independent convergences on
"needs round95"); the P4 diagonal-orbifold/holonomy chain (C167-C173,
closed by a general Lie-theory fact — triality is an OUTER automorphism of
Spin(8), no construction internal to the connected group can realize it);
the P5 SO(4)×SO(4) postulate (C191, user-authorized, REJECTED as literally
stated — S³'s own isometry alone can't distinguish the triality channels).
Also checked and NULL: 6 external geometric-selection schemes surveyed
(Randall-Sundrum, GKP/KKLT + SU(3)-structure generalization, G2-holonomy
M-theory, Horava-Witten, CSDR — none transfers); flux quantization
(circular); NCG-necessity of the two-sector combination (14-round chain,
answer: not coherent as a geometry, see OB2). **Reopen condition:** a
concrete external candidate (literature, or Tom), or a new derivation map
from other work in this project. Full chain: `experiments/202608*` through
`experiments/20260909-c191-*`.

## OB2 — does "two coexisting D's" (t=0 and t=1 together) even make sense as a spectral triple? [ANSWERED 2026-08-10: NO]

**Settled, no further work expected.** Two independent proofs, neither
relying on the other: (1) the KO-2/KO-4 ambiguity in the real structure
`J` is proven irreducible — an internal choice, not resolvable by any
data in the construction (C57/C60). (2) Independently, the doubled
construction fails BOTH orientability and Poincaré duality (C49/C52) — it
is not a valid NCG geometry at all, regardless of the KO question. C60's
own verdict: "bookkeeping on bookkeeping on a non-geometry." A ~20-round
chain (C41-C60) closed every escape route (sector-mixing algebras,
non-factorizing J, fine-tuned cancellations) exhaustively before reaching
this. Full chain: `experiments/20260810-c11-*`.

## OB3 — B-L operator on the twisted kernel [CORRECTED + FORMALIZED 2026-07-17]

This registry's own original entry was wrong (claimed no construction
existed; round94 already had one). Now consolidated into one canonical
statement (`BL_TWISTED_KERNEL_CANONICAL_STATEMENT.md`) with 5 explicit
scope constraints. **Residual open:** whether the physical zero mode is
one particle in a tensor-product bundle or a different identification of
the two `Σ` factors, and B-L's non-uniqueness among a `dim≥3` admissible
family — no additional principle singles it out yet.

## OB4 — the third triality channel (8_v) is a model postulate, not derived [split status]

**Gate 1 (algebraic distinguishability of 8_v/8_s/8_c) — DONE.** Two
independent routes (SO(4)×SO(4) block-chirality; su(3)⊕u(1)⊕u(1)) plus an
explicit verified isomorphism ℂ⊗8_v≅Σ (machine precision). **Gates 2-6
(physical realization) — PARKED**, not falsified: blocked on Tom
Lawrence's unpublished Part 5 (per this project's own DO NOT INITIATE
CONTACT constraint) or an independent G2-breaking-compatible spectral-gap
argument (none exists — G74A's own Lemma B requires exact G2 symmetry).
A cheap operational filter now exists for future proposals aimed at this
blocker: the G44 Information-Retention Gate (`C150` —
`experiments/20260904-c150-g44-information-retention-gate/GATE.md`): does
the proposed mechanism factor through g2-restricted representation data?
If yes, it's closed without computation. Full chain:
`TRIALITY_DISTINGUISHABILITY_GATE.md`, `experiments/20260717-round119-*`,
`experiments/20260718-round124-*`.

## OB5 — public-wording consistency check [RESOLVED 2026-07-17]

Re-verified directly against the original CLAIM_BOUNDARY_AUDIT findings —
both HIGH items fixed (no co-authorship claim; N_gen=3 caveated
everywhere it appears). One residual minor wording nit: two lines in
`preprint.tex` (434, 1294) say "collaboration with T. Lawrence" for what
is actually "input from," slightly more definite than warranted. Not
urgent, not a fence violation.

## OB6 — Codex items 5 and 8 [BOTH MOOT 2026-09-06]

Item 5 (physical action for the OB2 doubled construction): moot, since
OB2 showed that construction isn't a valid geometry at all. Item 8
(precise gauge group if SU(4) were realized): moot, since BOTH routes by
which SU(4) could ever become an actual gauge symmetry are closed — the
product-manifold route (G97: only su(3)⊕u(1) realized) and the
non-product/doubled route (OB2, above).

## OB7 — round111 uncommitted [RESOLVED 2026-07-17] · OB9 — E7-E13 chain needed consolidation [RESOLVED 2026-07-19]

OB7: committed, merged, pushed same day. OB9: 6 new `CLAIM_LEDGER.yaml`
entries added (C22-C27) plus one `DERIVATION_GRAPH.yaml` chain.
**Headline finding from the consolidation itself:** the torsion-escape
program has TWO independent unresolved blockers, not one — which `t` is
selected (→ OB1/OB13) AND a separate multiplicity-2 gap (a selected zero
mode is 2-dimensional, giving 6 internal modes across 3 triality
channels, not the needed 3). Resolving one does not complete the other.

## OB8 — round96's mixed-Y anomaly sweep was incomplete [RESOLVED 2026-07-17]

The 2 missing conditions were computed (round112) — both vanish. **Real
discriminating power is weaker than it looks**, per mandatory skeptic
review: each zero traces to `U(1)_Y` being identically zero or degenerate
with an internal Cartan generator at that endpoint given the current
frozen inputs, not to a genuine cancellation between competing charged
states. Cubic non-abelian channels ([SU(2)_L]³, [SU(2)_R]³) remain a
genuinely untested class.

## OB10 — geometric spinor bundle's own reality/Majorana condition [RESOLVED, corrected twice, net effect zero]

Final answer: under a UNIFORM Clifford convention (Cl(0,9)), the bundle
is REAL, matching Spin(9)'s Δ9=ℝ16. Two earlier wrong answers
(pseudo-real, then a second miscalculated correction) both traced to
mixing two sub-projects' opposite sign conventions — a repo-wide audit
(C34, 370 files) confirmed this exact bug exists nowhere else. A separate
sign error (`J_F²` stated as −1, actually +1) was found and fixed across
11 documents including `preprint.tex`. **Net effect on the multiplicity-2
gap (OB9/C27): zero** — closed either way, by a different mechanism than
first thought (the S⁶ factor collapses to a scalar on the 1-dim kernel,
not "pseudo-reality lives entirely in the S³ factor").

## OB11 — matter-generation tensor factorization (H_physical=H_matter⊗H_generation) [PARTIAL]

**Condition (i)** (identical internal block structure across the 3
triality channels) — **VERIFIED** (Casimir spectra match exactly).
**Condition (ii)** (no channel-mixing in the Dirac operator) — the hard
half's algebra-level intertwiner is **FOUND** (C70, machine precision,
15/15 restarts) after a long localization chain (C61→C69) ruled out a
shared-pipeline bug and pinned the real obstruction; C193 (2026-09-09)
further narrowed the remaining gap (J's su(3)-equivariance becomes
automatic once J is explicitly constructed — an existence argument, not
yet a built matrix). **Condition (iii)** (triality acting purely as
`1⊗t`, no admixture) — the so(8)-algebra half is **CLOSED EXHAUSTIVELY**
(C78: the entire so(8) commutant of the physical D is exactly su(3),
dimension 8 — no candidate subalgebra can ever work); the one remaining
door (a genuinely non-product D entangling the S³-frame and S⁶-triality
indices) had one honest attempt (C79) and came back NULL. A separate
STRONG reading (gauged SU(4) Pati-Salam matter) is independently BLOCKED
by gate G97. **Net: necessary condition verified, sufficiency still
open**, and assembling the actual channel-decomposed physical Dirac
operator (the real remaining task) is entangled with OB1. Full chain:
`experiments/20260803-ob11-*` through `experiments/20260909-c193-*`.

## OB12 — KO-dimension mapping [RESOLVED 2026-09-05]

Confirmed KO-dim 6 directly against real primary sources (Connes
hep-th/9603053; Chamseddine-Connes-Marcolli hep-th/0610241 eq. 2.19,
fetched and read directly) — previously only inherited by citation from
CCM without independent verification. That gap is now closed.

## OB13 — the two searches for a `t`-selector were in a provably blind parity sector [mostly settled, no selector found yet]

Core fact: any function EVEN in `(t-1/2)` cannot break the t=0-vs-t=1
degeneracy (though it CAN legitimately select `{0,1}` as a set against
other values — a correction made in C123 to an earlier overstatement of
this rule). Both original curvature-based searches were even, so their
nulls carried no selection information — not a failure of the searches,
a structural blind spot. Separately, and more importantly: `C125` PROVED
(not just observed) that NO genuine gauge transformation relates the full
13D configuration at t=0 to t=1 — so H1c does **not** dissolve into gauge
redundancy; `t=0` vs `t=1` is a genuine physical choice, needing a real
selector. One residual sub-case (a purely-orientation-compensated
"Family C") stays undecided, pending round95. Further even-functional
candidates tried since (C176/C177, spectral-action expansions) all give
a single well, not the double-well shape that would select `{0,1}` — no
selector has been found by any route tried so far. Full chain:
`experiments/20260810-*iota*`, `experiments/20260901-c123-*`,
`experiments/20260906-c176-*`, `experiments/20260906-c177-*`.

## OB14 — why `Σ` (not `m` or another twist bundle) is the physically correct twist for round59's `D_S6` [BLOCKED-INTERNAL/EXTERNAL]

A long, thorough search (C139 through C175) found: `Σ` is NOT the unique
twist bundle giving a nontrivial kernel (a genuine alternative, `m`, gives
kernel=0 — a real negative control, unlike 4 earlier attempts that never
discriminated). But a more fundamental problem surfaced along the way
(C141): the kernel of every twisted-`D_S6` construction tried exactly
equals a graded rank-nullity floor computable from pure su(3) branching
data alone — meaning this whole test family may not be able to
discriminate `Σ`'s specific geometric content from an alternative at all.
**Five independent candidate classes for a genuine discriminating test
were tried and rejected** (C70/C71 triality intertwiners — gauge freedom,
not independent data; G102's channels — forced identical by su(3); C134
torsion; the S⁶⊂ℝ⁷ shape operator; the canonical connection's own
curvature `R^c` — all forced to zero by Schur's lemma given `H=SU(3)`
holonomy). Two independent literature checks (AHL2023 direct read;
Charbonneau-Harland 2016's full deformation-theory computation) both
independently confirm the same zero, via completely different methods.
**No internally-buildable test remains identified.** Needs either a
not-yet-conceived construction or external input from Tom (subject to
DO NOT INITIATE CONTACT). Full chain: `experiments/20260904-c139-*`
through `experiments/20260906-c175-*`.
