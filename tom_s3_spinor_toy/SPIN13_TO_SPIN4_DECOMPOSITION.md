# Spinor Decomposition Audit — KK Product Ansatz to 4D Physics

**Reframing note (explicit, per user decision 2026-07-17):** the original
task named this "`Spin(1,12)→Spin(1,3)×Spin(3)×Spin(6)`". This framing is
**not used** — `preprint.tex`'s own "Total dimension is 13, not 10"
open-problems entry (line 1375) already caught and corrected exactly this
conflation: *"Earlier references in this paper to a 'ten-dimensional'
spacetime or spinor conflated two unrelated quantities: the dimension of
the SO(4) spinor representation on S³ (4 complex components) with an
actual spacetime dimension count."* There is no established `Spin(1,12)`
structure group in this project — standard supergravity caps at 11D
(Nahm's theorem), and no consistent 13D parent theory is claimed. This
audit instead covers what the project **actually has**: a Kaluza-Klein
**product ansatz** — 4D external spacetime × S³ (internal) × S⁶
(internal) — treated as independent factors from the start, not a
unified higher-D spacetime broken down via holonomy reduction.

## What this audit is (and is not)

**Is:** a consolidation of already-established facts (cited, not
re-derived) into the specific form requested — a single, unambiguous
answer to "where do the 32 states come from and how do they map to 4D
physics" — plus an honest identification of what remains genuinely open.

**Is not:** a new computation. Every claim below traces to an existing
`preprint.tex` section or experiment folder.

## The actual structure (established)

The internal (non-4D) Dirac spinor on the compact `S³×S⁶` factor
decomposes under `SO(4)×G₂` as:

```
(rep_{S³}) ⊗ (rep_{S⁶})  =  (4-component SO(4) spinor) ⊗ (8-component G₂ spinor)
                          =  32 complex components
```

(`preprint.tex:287-289`, `§sec:sm-content`). This is tensored with the
external 4D spacetime's own Weyl/Majorana structure separately — the 4D
part is NOT itself part of this 32-count; the 32 is entirely the
INTERNAL (S³×S⁶) representation content for one physical 4D fermion
generation.

## Checklist (5 exit-criteria items, per the requested audit)

**Mandatory context-blind skeptic review was run on the first draft of
this audit and found real problems — corrected below, not smoothed over.
Verdict labels changed from the first draft are marked explicitly.**

### 1. Dimension of the internal spinor: 32, per generation — ESTABLISHED, reconciling logic added (was asserted without it, skeptic-corrected)

`preprint.tex:287-298`. `4-component SO(4) Dirac spinor ⊗ 8-component G₂
Dirac spinor = 32 complex components`. **First-draft gap, fixed:** the
original text asserted this "matches CCM" without showing the
reconciling arithmetic — skeptic correctly demanded it. Traced explicitly:
`preprint.tex:298`'s own words are "32 complex spinor components decompose
into exactly the particle content of one SM generation... **plus** their
CPT conjugates" — i.e. the 32 splits as `16 (particle content, one
generation's worth of Weyl fields) + 16 (their CPT/antiparticle
conjugates)`. This `16+16=32` convention — treating antiparticle states as
SEPARATE basis elements of the internal Hilbert space, not a redundant
doubling — is the STANDARD Connes-Chamseddine-Marcolli finite-triple
convention (`H_F` is defined this way in the original CCM construction).
**Caveat, honestly flagged:** this specific claim (that 32=16+16 matches
CCM's OWN stated convention) rests on general/recalled knowledge of the
CCM literature, not an in-session tool-verified read of Connes' own
papers — marked `[WEAK]`, not `[VERIFIED]`, pending an actual primary-
source check if this becomes load-bearing for a future claim.

### 2. Reality conditions — gap CONFIRMED after a broader search (skeptic demanded, done)

- **Finite/NCG algebra `J_F`:** established (`preprint.tex:349`):
  `J_F²=-1`, `{J_F,γ_F}=0`, `[D_F,J_F]=0` — verified.
- **Geometric `S³×S⁶` spinor bundle itself:** first draft grepped only 4
  terms and declared the gap on that basis — skeptic correctly called
  this insufficient (negative evidence from an under-searched space).
  **Broadened to 12 terms** (`Killing spinor`, `KO-dimension`,
  `quaternionic`, `pseudo-real`, `nearly-Kähler`, `parallel spinor`,
  `symplectic Majorana`, `spectrum-symmetric`, checked in BOTH
  `preprint.tex` and every `experiments/` file). Found: 3 `Killing
  spinor` hits (existence/multiplicity arguments, e.g. G2-invariant
  Killing spinors on S⁶ — a different question, not spinor-bundle
  reality-type classification) and 4 `pseudo-real` hits — **all four are
  about `SU(2)` gauge-REPRESENTATION pseudo-reality for anomaly
  cancellation** (`[SU(2)]³=0` automatically, a group-theory fact about
  the gauge group), categorically different from asking whether the
  GEOMETRIC spinor bundle on `S³×S⁶` carries its own Majorana/real
  structure. **The gap survives the broader search** — genuinely
  confirmed, not just asserted from an under-searched grep.

### 3. 4D chirality — DOWNGRADED to CONDITIONAL (was ESTABLISHED, skeptic-corrected — accepted, real error caught)

**First-draft error, accepted:** claimed Lemma L5's `sign(ind)=+1` result
stands as an independent, standalone `ESTABLISHED` PASS. Skeptic correctly
pointed out this is not self-contained: `sign(ind)` is only a meaningful,
non-vacuous physical statement if `ind≠0` for the relevant operator. Item
5 (below) already documents that the FULL internal Dirac operator
(untwisted S³ × twisted S⁶) has **no zero mode at all** (KT-8) — so L5's
own S⁶-only chirality statement, while mathematically correct and
genuinely geometrically forced (not hand-assigned — that much survives),
does **not** by itself establish a physical, nonzero-index chirality
statement about the FULL operator. **Corrected verdict: CONDITIONAL,
inheriting item 5's own status** — the mathematical mechanism (chirality
from S⁶ orientation) is real and not manually assigned, but whether it
governs an actual nonzero physical index is exactly OB1/KT-8's still-open
question.

### 4. Particle/antiparticle counting vs. generation counting — ESTABLISHED, now with cited mechanism evidence (first draft asserted this, skeptic correctly demanded proof)

**First-draft gap, fixed:** claimed the 3 triality channels are
"structurally distinct" from the 32-state content without citing evidence
that they act on independent structure rather than permuting labels
*within* one fixed 32-dimensional block (the skeptic's specific concern:
this is exactly the "index-to-count jump" trap this project's own memory
already flags elsewhere). **Checked directly**
(`experiments/20260621-g73-three-channel-dirac/decision.md`): the three
`Z₃`-triality channels (`8_v`, `8_s`, `8_c`) are three **separate physical
twist choices** for the S⁶-side Dirac operator — `ind(D_{S⁶}⊗E)` computed
independently for `E=8_v`, `E=8_s`, `E=8_c`, each giving index 1
separately (`G73`). This is NOT a symmetry permuting labels inside one
32-state block — it is three genuinely distinct bundle constructions,
each supplying its own copy of the 32-state content. Confirms (with
evidence, not just assertion) that CPT-doubling (within one channel's
32) and triality-channel-multiplication (across three separate channels)
are structurally independent operations. **PASS stands, now cited.**

### 5. Exact map: internal zero modes → 4D Weyl fields — ESTABLISHED for the content, CONDITIONAL for the physical realization

The electric charge formula `Q=T₃L+Y`, `Y=K₃+(B-L)/2` (`preprint.tex:300-301`,
K₃≡T₃R proven round93) assigns each of the 32 states a definite SM quantum
number set — quarks, leptons, right-handed neutrino (exactly one per
generation, `preprint.tex:335-337`) — **all four anomaly conditions
verified per-generation** (`preprint.tex:305-317`). This is a real,
tool-verified table, not hand-assigned.

**BUT** — per `CURRENT_STATE_ROUND111.md`/`CLAIM_LEDGER.yaml` C3 (KT-8):
this whole 32-state content is established on the S⁶ factor's own index,
which does **not yet** correspond to a demonstrated zero mode of the FULL
internal Dirac operator (untwisted S³ × twisted S⁶ has NO zero mode). So
the map "which representation label attaches to which state" is
established; whether that state is a genuine, physical, massless 4D
fermion is exactly OB1's own still-open question (now parked).

## Overall verdict (revised after mandatory skeptic review)

**PASS on 2 of 5 items** (dimension — with reconciling logic now shown;
particle/antiparticle-vs-generation separation — with cited mechanism
evidence). **CONDITIONAL on 2** (chirality — downgraded from the
first-draft's standalone PASS, correctly inherits the zero-mode
question's own status; the zero-mode/physical-realization question
itself, tied to the parked OB1). **OPEN on 1** (geometric spinor bundle's
own reality condition — gap confirmed, not just asserted, after
broadening the search from 4 to 12 terms across both `preprint.tex` and
`experiments/`).

This audit does **not** find the failure modes the task's own kill
criteria named (no manual doubling to reach 32 — the 16+16 split is the
standard, cited CCM convention, not an ad hoc fix; no hand-assigned
chirality — L5's mechanism is genuinely geometric even though its
physical force is conditional; no particle/antiparticle-as-generation
conflation — now shown with cited mechanism evidence, not asserted). What
remains open is narrower and more precise than "does the whole map work":
specifically (a) the geometric reality-condition gap, (b) whether L5's
chirality mechanism governs an actual nonzero physical index, and (c) the
already-tracked, parked OB1 question of whether this content attaches to
an actual massless 4D zero mode — (b) and (c) are the same underlying
KT-8 issue, not two separate gaps.

## What this does NOT mean

1. Does NOT resolve OB1 (parked) — the zero-mode/physical-realization
   gap is the SAME KT-8 issue, untouched by this audit.
2. Does NOT claim the 13D ansatz has a consistent parent theory —
   `preprint.tex`'s own correction on this point stands, unaffected.
3. Does NOT affect `N_gen=3`'s own conditional status (`CLAIM_LEDGER.yaml`
   C4) — this audit describes the CONTENT of one generation's 32 states,
   not whether 3 independent generations are physically realized (that's
   `C_G67C3`, also still open).
4. Does NOT independently re-verify the underlying gates (G17, G23, G93,
   the anomaly conditions) — all reused by citation from `preprint.tex`.

## Sources

`preprint.tex` §Framework (lines 264-300), §SM Fermion Content (287-337),
§NCG Spectral Triple (341-360), §Chirality/Lemma L5 (884-920), §Open
Problems "Total dimension is 13, not 10" (1375-1396);
`experiments/20260621-g73-three-channel-dirac/decision.md` (triality-
channel mechanism, item 4); `CLAIM_LEDGER.yaml` C3, C4, C_G67C3;
`CURRENT_STATE_ROUND111.md`. Mandatory skeptic review (context-blind,
document + no reasoning chain) run before finalizing — see corrections
inline in each checklist item above.
