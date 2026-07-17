# E17 (round85) — Decision

**Date:** 2026-07-17
**Verdict:** `BLOCKED__REPRESENTATION_CONTENT_CONSISTENT__PHYSICAL_COEXISTENCE_UNDECIDABLE_WITHOUT_PARENT_ACTION`
**Go/no-go:** This is the honest outcome the task explicitly anticipated as
legitimate. A genuine, positive sub-finding survives (Section 1 below): the
representation-content of `t=0` and `t=1` combined is fully consistent with
this project's own pre-existing "one generation" bookkeeping (G6), with no
double-counting risk. But the deeper, decisive question — whether `t=0` and
`t=1` are ever SIMULTANEOUSLY physically realized, as opposed to being two
mutually exclusive candidate values of one connection parameter — is not
decidable from anything this project has established, and requires a stated
13D parent action this project explicitly does not have (KT-8). **Neither
PASS nor FAIL is honestly supportable; BLOCKED is the correct verdict.**

## Bottom line, stated plainly first

Under BOTH `SU(2)_L`/`SU(2)_R` labeling conventions, `ker D^{t=0}_{S³}` and
`ker D^{t=1}_{S³}` (the latter established only under `c0=-2`,
`CONVENTION_TABLE.md` row 5) are confirmed to transform as the mirror-image
pair `(1,2)` and `(2,1)` (or vice versa) — i.e. exactly the two chiral halves
of a full `Spin(4)` Dirac spinor, `(2,1)⊕(1,2)`, which is precisely the
4-component `SO(4)` representation `preprint.tex:293-294` states one
generation's S³-side content should be. **If** both sectors were
simultaneously present, their union would exactly reproduce G6's own
pre-existing 4-state S3-side bookkeeping (`g6_spinor_decomposition.py:29-36`),
with no extra states and no double-counting against the "32 states = one
generation + CPT conjugates" convention (`preprint.tex:296-298`), because
G6's CPT doubling is a wholly separate, S6-side-only mechanism (E13/round79).
**This is a genuine necessary-condition PASS.**

But the **sufficient** condition for PASS — that `t=0` and `t=1` actually DO
coexist as one consistent physical construction, rather than being two
logically distinct, mutually exclusive values of a single connection
parameter `t` on the one S³ factor — is not established or derivable from
anything in this project's text. `t` is a single real parameter of one
connection family `∇^t` on one S³ factor (`preprint.tex:1467-1497`); a
physical compactification has one specific metric/connection, hence
(pending a selection principle, H1c, still open) at most one specific value
of `t` realized, not two values simultaneously, unless a genuinely new
structural ingredient (e.g. two separate fermion fields on the same S³, one
coupled to each connection) is introduced — and no such ingredient is stated
anywhere in this project. E14/round80's own three explicit attempts to find a
mechanism forcing simultaneous presence (Section E below) all fail to supply
one, and two of the three actively point away from it. **This is exactly the
pre-registered BLOCKED condition: undecidable without a parent 13D action.**

---

## 1. Representation content under BOTH labeling conventions [VERIFIED-tool, reused]

Per `CONVENTION_TABLE.md` row 6 (`experiments/20260717-round84-e13-convention-
reconciliation-table/CONVENTION_TABLE.md:71-77`), the geometric identification
of which S³ isometry action (left-translation vs right-translation) is the
physical `SU(2)_L` is confirmed genuinely unresolved from existing project
text. Both conventions are stated here explicitly, reusing (not
re-deriving) round77/E11's tool-verified `T₃` eigenvalues
(`experiments/20260717-round77-su2lr-correspondence-test/decision.md:81-86`)
and round83/E16's independent re-confirmation
(`experiments/20260717-round83-joint-representation-decomposition/decision.md:76-99`,
`T3(v1)=1/2, T3(v2)=-1/2`).

| Sector | Convention A (`SU(2)_L`=left-translation) | Convention B (mirror: `SU(2)_L`=right-translation) |
|---|---|---|
| `ker D^{t=0}` (2-dim, `Ω_i(0)=0` for any `c`, unconditional per `CONVENTION_TABLE.md` row 5) | `SU(2)_L` **singlet**, `SU(2)_R` **doublet** → `(1,2)` | `SU(2)_L` **doublet**, `SU(2)_R` **singlet** → `(2,1)` |
| `ker D^{t=1}` (2-dim, right-invariant frame, established **only under `c0=-2`**) | `SU(2)_L` **doublet**, `SU(2)_R` **singlet** → `(2,1)` | `SU(2)_L` **singlet**, `SU(2)_R` **doublet** → `(1,2)` |

Source table:
`experiments/20260717-round77-su2lr-correspondence-test/decision.md:81-86`
(the "Clean summary table," Convention A as stated there); Convention B is
its exact mirror, per that same file's own flagged reversal
(`decision.md:122-129`, "if the convention is reversed... every label in the
table above flips"). Under **either** convention, the pair `{ker D^{t=0}, ker
D^{t=1}}` is exactly `{(1,2), (2,1)}` — the two chiral halves of one full
`Spin(4)` Dirac spinor — never two copies of the same piece. This is
convention-INDEPENDENT: the labeling ambiguity flips which name (`L` or `R`)
attaches to which sector, but never produces "two `(2,1)`'s" or "two
`(1,2)`'s" under either reading. **This directly answers the task's
instruction to test both conventions: the qualitative structural finding
(one `(1,2)`, one `(2,1)`, never a duplicate) is convention-independent.**

**`c0=-2` check (does this discussion silently violate `CONVENTION_TABLE.md`
row 5's caveat?):** No. Every statement about `ker D^{t=1}` above is stated,
as it must be, as holding only under `c0=-2`
(`experiments/20260717-round76-e9followup-right-invariant-frame/decision.md:129-168`);
this experiment does not at any point substitute the abstract `c=+2` into a
`t=1` claim. Per round77's own already-flagged caveat (reused, not
re-derived, `decision.md:130-136`), no candidate `t=1` spinor has ever been
constructed or tested under `c=+2` anywhere in this project — so every
`ker D^{t=1}` entry in the table above describes an object that, under this
project's own abstractly-calibrated `c=+2`, is **not currently known to
exist at all**. This caveat is carried forward, not resolved, here.

---

## 2. Does ONE sector alone suffice, or are both needed to match the existing "one generation" bookkeeping? [CODE + DOCS]

**Direct answer: one sector alone does NOT supply the full content this
project's own G6 bookkeeping assigns to one generation's S3-side content; a
second, independent mechanism or the other sector is needed to complete it,
and no independent alternative mechanism exists in this project's text.**

`experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py:29-36`
(re-quoted from `experiments/20260717-round83-joint-representation-
decomposition/decision.md:107-114`, re-verified there by direct `Read` this
project cycle, not re-read fresh in this round but cited to an already
tool-confirmed source):

```python
s3_states = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]
```

This is **4 states total**: two with `(T3L=±1/2, T3R=0)` — the `(2,1)` piece
— and two with `(T3L=0, T3R=±1/2)` — the `(1,2)` piece. This is exactly
`preprint.tex:293-294`'s "4-component `SO(4)` spinor representation" (32 =
4×8, with 8 the `G2` spinor dimension on S⁶, `preprint.tex:294`) — i.e. G6's
own, independently-existing bookkeeping already assumes/requires BOTH the
`(2,1)` and `(1,2)` pieces (4 states, not 2) as the S3-side content of ONE
generation. Since `dim ker D^{t=0} = 2` and `dim ker D^{t=1} = 2`
independently (E12, `experiments/20260717-round78-e12-multiplicity-gate/
decision.md:12-18`, "Section D — total count"), **ONE sector alone supplies
only 2 of the 4 states G6's bookkeeping assigns per generation** — exactly
ONE of `(2,1)` or `(1,2)`, never both. Matching G6's own 4-state convention
from the torsion-escape-route zero-mode construction, if that convention is
even the right target (see caveat below), requires content from BOTH
sectors; no alternative mechanism supplying the missing 2 states from a
single sector, or from anywhere else, is stated anywhere in this project
(`experiments/20260717-round78-e12-multiplicity-gate/decision.md:97-137`,
Section E, checked Majorana/reality conditions — none found — and
orbifold/projection routes — none targets `ker(D_{S3,t})` itself).

**Caveat, carried forward, not resolved here (already flagged by E12 and
E16):** whether G6's 4-state, per-KK-level bookkeeping (built independently
of any zero-mode-existence question — `experiments/20260717-round78-e12-
multiplicity-gate/decision.md:114-116`, "all 32 SM states appear at every
`(m,n)` level" per G7's own script, regardless of whether any
`ker(D_{S3,t})` is realized) is even the correct target for the
torsion-escape-route's zero-mode construction to match, or whether these are
two logically separate bookkeeping exercises this project has never
reconciled, is **itself unresolved** (`experiments/20260717-round78-e12-
multiplicity-gate/decision.md:110-128`, Section E.2, and reused verbatim in
`experiments/20260717-round83-joint-representation-decomposition/
decision.md:261`, first row of the Relaxation Map — still listed "still
open, unchanged by this experiment" as of round83). This experiment does not
resolve that caveat; it only establishes that IF the two frameworks are to be
matched, both sectors (not one) are needed, and that doing so introduces no
inconsistency of content (Section 3 below).

---

## 3. Double-counting check against the "32 states" convention [DOCS + CODE]

**No double-counting risk found**, conditional on both sectors actually
coexisting (Section 4 addresses whether that itself holds).

`preprint.tex:292-298` states the 32-complex-component decomposition (one
generation + CPT conjugates) as `(rep_{S^3})⊗(rep_{S^6})` — one **fixed**
4-component S3-side representation tensored with the 8-component S6-side
representation. `preprint.tex:1533-1536` (cited and reused, not re-derived,
via `experiments/20260717-round83-joint-representation-decomposition/
decision.md:138-144`) states explicitly that "the S³ spinor factor is a
fixed, generation-independent block" and the generation index lives entirely
in the S⁶/octonion triality structure. Combined with G6's own 4-state S3-side
list (Section 2 above) — which already includes BOTH the `(2,1)` and `(1,2)`
pieces as ONE package, not as two independently-counted layers — realizing
`ker D^{t=0} ∪ ker D^{t=1}` (4 states total, under either labeling
convention, per Section 1) reproduces this SAME 4-state package exactly,
component for component (T3L/T3R/chir_s3 values match one-to-one under
either convention). There is no room for an EXTRA duplicate copy: G6's
bookkeeping has never independently counted a 5th, 6th, 7th, or 8th S3-side
state, so there is nothing beyond these same 4 for the `t=0`/`t=1` union to
collide with.

The CPT-conjugate doubling (`preprint.tex:298`, "plus their CPT conjugates")
is, per E13/round79 (reused via `experiments/20260717-round83-joint-
representation-decomposition/decision.md:177-191`, Section D), carried
**entirely by the S6 factor's `B-L` sign**, confirmed there for all 8
checked particle/antiparticle pairs sharing the same `chir_s3` value — i.e.
this doubling operates on an axis (the S6 factor) orthogonal to, and
independent of, which of the 4 S3-side states (`t=0`'s 2, or `t=1`'s 2) is in
play. **Using both `t=0` and `t=1` content does not touch, inflate, or
duplicate the CPT-conjugate count** — that count is fixed separately by the
S6 factor regardless of which (or how many) S3-side states are combined with
it.

**Direct answer to the task's specific question:** using both `t=0` and
`t=1` sectors' content is **additional, not duplicative**, relative to the
existing 32-state convention — it supplies exactly the content that
convention's own S3-side bookkeeping already independently assumes, with the
CPT-doubling axis (S6-side) left completely untouched.

---

## 4. Is there ANY existing mechanism fixing whether both sectors are simultaneously present? [VERIFIED-tool, DOCS — negative result]

**No.** Three independent lines of this project's own prior work were
checked directly (not re-derived), per the task's instruction to search
rather than assume:

**(a) E14/round80's own Z2-isometry exploration — the closest existing
attempt at exactly this question.** `experiments/20260717-round80-z2-left-
right-symmetry-search/decision.md:200-257` (Section E, "does this force BOTH
t=0 and t=1 to be present?") tried three readings and found none succeeds:

- **Reading 1** ("same physics, different labels," `decision.md:205-214`):
  if `t=0` and `t=1` are isometry-related descriptions of the SAME physical
  configuration, this argues for **UNDER**-counting (the two 2-dim kernels
  would be the SAME 2 physical states seen twice, not 4 independent ones) —
  the opposite of what PASS needs, and, if adopted, this reading would make
  Section 2/3's "clean 4-state match" above an artifact of double-counting a
  single 2-dimensional space as though it were two distinct ones. **This
  project's text does not decide between this reading and the alternative
  (that `t=0` and `t=1` are physically distinct configurations related by a
  symmetry, not identical) — see the sharper structural point below.**
- **Reading 2** (gauging `iota` as an orbifold identification,
  `decision.md:216-232`): requires `t=1-t`, i.e. `t=1/2` uniquely — the
  Levi-Civita, torsion-free value KT-8 already shows has **no zero modes at
  all** (`preprint.tex:1421-1465`). This is a clean, decisive negative: the
  most natural way to literally IDENTIFY the two sectors as one gauged
  structure collapses the entire escape-route mechanism, rather than
  producing coexistence.
- **Reading 3** ("Left-Right-symmetric/Pati-Salam parity requires both
  doublets," `decision.md:234-251`): this is the reading closest to
  supplying what PASS needs (Section 5 below expands on why), but it is
  explicitly flagged there as a **model-building CHOICE**, not a consequence
  the geometry forces, and it sits in direct, unreconciled tension with this
  project's own established, explicitly ASYMMETRIC chirality mechanism
  (Lemma L5, `preprint.tex:884-908`, `sign(ind)=+1` forces a left-handed
  EXCESS on the S6 factor, not a parity-symmetric result).

None of the three readings closes the gap in PASS's direction; Readings 1
and 2 point away from it, Reading 3 is an unadopted, tension-carrying choice.

**(b) E11/round75's Freund-Rubin flux exploration.**
`experiments/20260717-round75-e11-freund-rubin-torsion-link/decision.md:113-167`
(Q2) finds the flux, as currently normalized in `preprint.tex`, is wired only
into the bosonic moduli potential (`V_flux`, `preprint.tex:985-989`), never
coupled to the S3 connection/torsion sector at all (`decision.md:131-144`,
zero grep hits for "contorsion," "H-flux," "NS-NS," or "connection
deformation" anywhere in `preprint.tex`). `decision.md:171-212` (Q3) finds
the existing flux EOM fixes `ρ6` (a continuous modulus), not the flux
quantum `q` and not any torsion-like discrete parameter — so nothing in this
project's flux sector currently constrains `t`, let alone whether both `t=0`
and `t=1` occur simultaneously. **Checked freshly for this experiment (not
assumed): nothing in E11/round75 changes when both `t` sectors are
considered TOGETHER rather than one at a time** — the flux coupling gap
(Q2, OPEN) and the EOM-selects-nothing-about-`t` finding (Q3, FAIL-AS-POSED)
are structural absences in the paper's normalization, independent of how
many `t`-sectors are being asked about; a mechanism that doesn't exist for
one sector does not newly appear for two.

**(c) KT-8 / the missing parent action.** `preprint.tex:1421-1465` ("Full-
operator zero-mode gap") establishes, independent of `t`, that `ker D_full =
0` identically for the round, untwisted Levi-Civita ansatz used throughout
the paper — i.e. **neither `t=0` nor `t=1` is currently known to correspond
to an actual zero mode of the physical 9D operator this paper's physics
depends on**; the torsion family is explicitly flagged, in the paper's own
words, as a "candidate mechanism... physically unmotivated, not a
resolution" (`preprint.tex:1467-1497`, esp. `1487-1497`: "no physical
principle is known for selecting `t=0` (or any other crossing) over the
Levi-Civita value `t=1/2`... Recorded here as a candidate mechanism for
future work, not as a step toward `N_gen=3`"). No stated 13D parent action
exists anywhere in this project from which either `D^{t=0}` or `D^{t=1}` —
let alone both simultaneously — would follow by dimensional reduction; this
absence is the same gap independently flagged as KT-1 in this project's own
Open Problems section (per this project's `activeContext.md`, "no stated
parent action for the D⊗S⁻ twist," added to `preprint.tex` by an
independent audit, logically prior to L3b).

**Structural point this experiment adds (not previously stated this way in
E14, but a direct, honest logical consequence of combining E14 Section E
with the basic form of `∇^t`, marked `[INFERRED]`, not independently
tool-computed beyond what E14 already verified):** `t` is a single real
parameter of ONE connection family `∇^t` on the ONE S³ factor
(`preprint.tex:1467-1497`; E2/E7's own construction, reused throughout
E9–E16). A physical compactification has one specific metric/connection on
its internal manifold — hence, absent an explicit new structural ingredient,
at most ONE value of `t` is the actual physical connection at a time, not
two simultaneously. Genuinely realizing both `t=0` and `t=1` at once would
require something this project does not state anywhere: either two distinct
fermion fields on the same S³ (one coupled to each connection), or a
mechanism making `t` itself a dynamical field with two coexisting
vacua/sectors, or an explicit orbifold-type construction along the lines
E14 Reading 2 already tried and found collapses to `t=1/2` instead. This is
the concrete reason the pre-registered BLOCKED condition ("not decidable
without a parent 13D action") is met here, rather than a vaguer appeal to
"insufficient information": the specific missing ingredient is a parent
action or field-content statement that would say how many independent
Dirac fields on S³, coupled to how many values of `t`, this compactification
actually contains.

---

## 5. Are the two sectors Pati-Salam left/right partners? [DOCS, structural]

**Structurally plausible, and consistent with this project's own gauge-group
statement, but not established or adopted anywhere in this project's text.**

`preprint.tex:278-281` and `preprint.tex:417-424` (`§`Weinberg-angle
caveat) both state, in the paper's own words, that this project's gauge
algebra `SU(3)_c×SU(2)_L×SU(2)_R` (from the `SO(4)` isometry of S³) IS "Pati-
Salam without the `U(1)_{B-L}` factor" (`preprint.tex:424`). In standard
Pati-Salam / left-right-symmetric model building, a single generation
contains BOTH an `SU(2)_L` doublet and an `SU(2)_R` doublet (e.g.
`Q_L~(2,1)`, `Q_R~(1,2)`) — precisely the pattern Section 1's table shows
for `{ker D^{t=0}, ker D^{t=1}}` under either labeling convention. E14's own
Reading 3 (`decision.md:234-251`, reused, not re-derived here) already
identifies this exact analogy as the one reading among its three that points
toward the needed coexistence — but flags it explicitly as importing a
LEFT-RIGHT-SYMMETRIC model-building assumption this project's own
established chirality mechanism does not have: Lemma L5
(`preprint.tex:884-908`) derives an explicitly ASYMMETRIC left-handed excess
on the S6 factor (`sign(ind)=+1`), not a parity-symmetric L/R pairing. Any
argument that "Pati-Salam symmetry forces both S3-side sectors" would need
to explain why the identical logic does not equally force a symmetric
(rather than the paper's own already-established asymmetric) result on the
S6 factor — a reconciliation neither this experiment nor E14 attempts or
resolves. **Answer: consistent in representation-theoretic form, but a
model-building CHOICE in unreconciled tension with an already-established
part of this project's own construction, not a consequence its existing
text derives.**

---

## 6. Charge-conjugation (CPT) relationship between `t=0` and `t=1`? [DOCS, negative/silent result]

**E13/round79's CPT finding is silent on this specific question — it tested
a different axis.** `experiments/20260717-round83-joint-representation-
decomposition/decision.md:177-191` (Section D, reusing E13/round79)
establishes that the CPT/particle-antiparticle doubling in this project's
bookkeeping is carried entirely by the S6 factor's `B-L` sign, and
specifically that the **two `T₃`-components within one single fixed-`t`
doublet** are NOT related by CPT conjugation. This finding addresses whether
the 2 states WITHIN one sector (at one fixed `t`) are charge-conjugates of
each other — it does not test, and is not logically about, whether the
`t=0` sector AS A WHOLE and the `t=1` sector AS A WHOLE are charge-conjugates
of one another (a genuinely different axis: across `t`, not within a fixed
`t`). **This project's text neither derives nor rules out a
charge-conjugation relationship between `t=0` and `t=1` — the question is
untested, not settled either way, by anything cited here.**

Separately: the one concrete geometric map this project has constructed
relating `t=0` and `t=1` — `iota: g ↦ g⁻¹`
(`experiments/20260717-round80-z2-left-right-symmetry-search/
decision.md:18-31`) — is confirmed (`decision.md:52-58`) to be an
**orientation-reversing spatial isometry** of S³ (`det(J)=-1`), i.e. a
parity-type map. CPT combines charge conjugation, parity, AND time reversal;
`iota` alone realizes at most a parity-like piece on the S³ factor, with no
charge-conjugation or time-reversal content established for it anywhere in
this project. **`iota` is not shown to be, or to imply, a CPT operation.**

---

## Applying the pre-registered criteria

| Criterion | Finding | Basis |
|---|---|---|
| Representation content of `{ker D^{t=0}, ker D^{t=1}}` matches required `(2,1)⊕(1,2)`, under either labeling | **YES, convention-independent** | Section 1 |
| One sector alone suffices (via some other stated mechanism) | **NO — no alternative mechanism found; both are needed to match G6's own 4-state bookkeeping, IF that bookkeeping is the right target (itself an open reconciliation, per E12 Section E.2)** | Section 2 |
| Double-counting against "32 states + CPT" convention | **NO risk found — additive, not duplicative** | Section 3 |
| Existing mechanism (flux/parent-action/32-state convention) fixing simultaneous presence | **NONE found — E14's 3 readings fail to supply one (2 of 3 point away); E11/round75's flux exploration finds zero coupling; KT-8 confirms no parent action exists at all** | Section 4 |
| Pati-Salam L/R partnership | **Structurally consistent, but an unadopted model-building choice in tension with Lemma L5's asymmetry** | Section 5 |
| Charge-conjugation (CPT) relationship between sectors | **Untested by anything in this project; E13/round79's finding is on a different axis** | Section 6 |

**PASS is not supported**: the necessary condition (representation content,
Sections 1–3) is satisfied, but PASS's actual wording requires "one
consistent Hilbert space where `t=0` and `t=1` TOGETHER give exactly the
required... multiplets" — this requires establishing that both are
simultaneously, consistently present, which Section 4 shows is not
established, and which the "single parameter of one connection" structural
point (Section 4c) shows is not even a well-posed question absent a parent
action specifying how many fermion fields/connections this compactification
actually contains.

**FAIL is not supported either**: FAIL requires the two sectors to give
"independent copies of the SAME physical multiplets" — but `ker D^{t=0}`
and `ker D^{t=1}` carry DIFFERENT representation content (`(1,2)` vs `(2,1)`,
Section 1), not identical copies of one multiplet. The one FAIL-adjacent
concern (E14 Reading 1's "under-counting" scenario, Section 4a) would, if
true, make combining both sectors an artifact of double-counting a single
2-dimensional space — but this project's text does not establish Reading 1
over its alternative (that `t=0` and `t=1` are physically distinct
configurations related by an ungauged symmetry) either; it is exactly as
undecided as the coexistence question itself.

**BLOCKED is the honest verdict**: per the pre-registered criterion, "this
cannot be settled without a parent 13D action — determining whether the two
operators are parts of one consistent theory or two logically separate
constructions is not decidable from what this project has established."
Section 4c states precisely, in this project's own terms, what such a
parent action would need to supply: an explicit statement of how many
independent Dirac fields on the S³ factor this compactification contains,
and how each couples to the connection family `∇^t` — a genuinely new
physical input, not a re-reading of anything currently written.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the possibility that the `t=0`/`t=1`
  coexistence question could be answered by representation-theory
  bookkeeping alone — Sections 1–3 show the bookkeeping is fully consistent
  either way (coexistence would not create a double-counting problem), so a
  clean PASS or FAIL cannot be manufactured from that angle; the deciding
  factor lies entirely in physical structure (how many fields/connections
  exist), not in quantum-number arithmetic. It also kills, specifically, the
  temptation to read E14 Reading 3 (Pati-Salam parity) as an established
  mechanism — Section 5 confirms it remains an unadopted choice in tension
  with Lemma L5.
- **What this result does NOT kill:** H1c (physical selection of `t`), KT-8
  (whether ANY zero mode of the full untwisted operator exists), E12/E13's
  own multiplicity findings, or E16's doublet-reading of a single sector —
  all untouched, cited by reference only. It also does not kill the
  possibility that both sectors DO coexist (Reading 3 / Pati-Salam-style
  left-right symmetry remains a live, if unadopted, hypothesis) — only that
  this project's existing text cannot currently confirm or exclude it.
- **What survives, confirmed stronger than before:** the specific,
  previously-vague "does using both sectors risk double-counting" worry
  (present implicitly since E12 Section E.2 first flagged the 32-state
  reconciliation as open) is now answered concretely and negatively — no
  double-counting risk exists in the representation-content bookkeeping
  itself (Section 3). This narrows the remaining open question from "is
  there a double-counting problem AND a coexistence problem" to just "is
  there a coexistence problem" (Section 4), which is itself now stated in
  the most precise form available in this project to date (Section 4c): a
  missing statement of field content/parent action, not a vaguer "more
  research needed."

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Resolve Reading 3 (Pati-Salam parity) vs Lemma L5 (asymmetric chirality) tension | Either an independent argument for why S3 needs L/R-symmetric doubling while S6 does not, or abandonment of Reading 3 as the coexistence mechanism |
| State an explicit 13D parent action / field content | The single missing ingredient identified in Section 4c: how many independent Dirac fields on S³, coupled to how many values of `t`; without this, "coexistence" is not even a well-posed question, per KT-8's own already-flagged parent-action gap |
| Test whether E14 Reading 1 (same physics, different labels) or its alternative (physically distinct, symmetry-related configurations) is correct | Would require an independent physical criterion for when a diffeomorphism-related pair of field configurations counts as "the same state" vs "two states" — not attempted anywhere in this project |
| Reconcile G6's 4-state per-KK-level bookkeeping with the zero-mode-kernel framework | Still E12 Section E.2's own top recommended next step, unchanged by this experiment — this experiment assumes, for Sections 2–3 only, that matching G6's convention is the right target, without independently establishing that it is |

## Assumptions carried, unresolved

- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's own
  `[INFERRED, NOT independently literature-verified]` decoupling assumption)
  — this experiment's classification presupposes it holds, exactly as
  E12/E16's own findings do.
- `SU(2)_L`=left-translation vs its mirror (`CONVENTION_TABLE.md` row 6) —
  both tested explicitly here (Section 1); the verdict is confirmed
  convention-independent, so this ambiguity does not affect the BLOCKED
  outcome.
- Whether G6's 4-state, per-KK-level bookkeeping is the correct target for
  the torsion-escape-route zero-mode construction to match (E12 Section
  E.2) — assumed, for the purpose of Sections 2–3's double-counting check
  only, NOT independently re-derived or newly established here.
- `t=1`'s existence only under `c0=-2`, not the abstractly-calibrated
  `c=+2` (`CONVENTION_TABLE.md` row 5) — carried forward exactly, not
  resolved; every `ker D^{t=1}` statement in this decision is conditional on
  this sign choice.

## What this does NOT mean

1. Does **not** establish H1c (physical selection between `t=0`, `t=1`,
   both, or neither) — untouched; if anything, this experiment shows the
   question is more structurally subtle than "which one does nature pick,"
   since "both, simultaneously" is not even well-posed without a parent
   action stating the field content.
2. Does **not** resolve KT-8 (whether ANY zero mode of the full untwisted
   `D_full` exists) — untouched; the entire torsion-escape-route program
   this experiment examines is, per `preprint.tex:1467-1497`'s own words, a
   "candidate mechanism... physically unmotivated, not a resolution,"
   independent of this experiment's BLOCKED verdict.
3. Does **not** claim the representation-content match (Section 1–3) is
   novel physics — it follows from standard `Spin(4)=SU(2)×SU(2)` Dirac
   spinor decomposition (2,1)⊕(1,2), combined with facts this project
   already tool-verified (E9–E16); what is new here is the concrete
   cross-check that THIS project's own specific G6 bookkeeping and THIS
   project's own specific zero-mode kernels align, not a new representation-
   theory fact.
4. Does **not** claim a Pati-Salam left-right-symmetric reading of this
   construction is wrong — only that it is an unadopted model-building
   choice, not a consequence this project's existing text derives, and that
   it carries an unreconciled tension with Lemma L5's already-established
   asymmetric chirality mechanism.
5. Does **not** claim a charge-conjugation relationship between `t=0` and
   `t=1` is ruled out — only that it is untested by anything in this
   project; E13/round79's own CPT finding addresses a different axis (within
   one fixed-`t` doublet, not across `t`).
6. Does **not** re-derive or challenge any of E9/E10/E11/E12/E13/E14/E15/E16's
   own tool-verified results — all reused here purely by citation.
7. Does **not** imply this project's `N_gen=3` headline claim (which rests
   on the independently-established G73/G74A/G74B S6-only triality/index/
   chirality chain, per `activeContext.md` and `reports/
   PROJECT_360_ROUND3_SYNTHESIS.md`) is affected — this experiment concerns
   only the separate, S3-side torsion-escape-route program, which this
   project's own text (`preprint.tex:1467-1497`) already characterizes as a
   candidate mechanism, not a load-bearing part of the `N_gen=3` result.
8. A BLOCKED verdict here does **not** mean further progress is impossible
   — Section 4c identifies exactly what is missing (a parent-action/field-
   content statement), which is a well-defined, if substantial, follow-up,
   not an appeal to general uncertainty.

## Pearl-registry candidate

One transferable observation, concrete enough to flag: **the "do both
candidate sectors coexist" question, for a one-parameter family of
connections/twists on a SINGLE compact factor, reduces structurally to a
question about how many independent field copies the parent theory
contains — it is not answerable by representation-theory bookkeeping alone,
no matter how cleanly that bookkeeping lines up (Sections 1–3 here).** This
is a general pattern worth watching for elsewhere in this project wherever a
single continuous parameter (like this project's own torsion parameter `t`,
or a KK level `n`, or a modulus) is asked to supply two "simultaneously
present" physical sectors: the representation-content check and the
field-content/parent-action check are logically independent, and a clean
pass on the first does not license skipping the second. Impact score ~4
(narrow to this project's own torsion-escape-route line of work and any
future similar one-parameter-family constructions; not registered to the
global `pearl_registry/INDEX.md` — project-internal, not cross-domain).

## Check (reproduces this decision)

This is a reconciliation/classification round against already-established
project artifacts — there is no new script. The "check" is: (1) every
citation above traces to a file:line that exists and says what is claimed
(spot-checked via direct `Read`/`Grep` during this session — `preprint.tex`
lines 271-298, 417-424, 884-912, 1421-1497 were read in full this round;
`g6_spinor_decomposition.py:29-36` was cross-checked against round83's own
already tool-verified quotation of it); (2) the final verdict follows
deductively from the pre-registered PASS/FAIL/BLOCKED criteria in `claim.md`
applied to the six findings in Sections 1–6 above, with no step skipped or
forced.
