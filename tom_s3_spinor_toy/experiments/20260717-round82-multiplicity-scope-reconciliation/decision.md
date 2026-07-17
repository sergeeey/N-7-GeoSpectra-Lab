# decision.md — Round 82: Multiplicity-Scope Reconciliation

> **⚠️ Provenance correction (2026-07-17, added after this file was written):**
> this file's citations of "G74A: dim ker=1 EXACTLY" point to a superseded
> argument (G74A's own two lemmas are now known to be insufficient, per
> `preprint.tex`'s own current text) — the $\dim\ker=1$ NUMBER is correct
> and this file's verdict is unaffected, but the correct citation is the
> later `dolan-casimir-g2su3`+`round59` computation, not G74A. See
> `reports/PROJECT_360_ROUND3_SYNTHESIS.md`, "Provenance correction"
> section, and the superseding note now added to
> `experiments/20260621-g74a-lichnerowicz-gap/decision.md`.

**Date:** 2026-07-17
**Verdict:** **ORTHOGONAL_EXPLORATORY_LINE** — the E12/E13 (KT-13) 6-vs-3
multiplicity excess does **not** threaten the published G73/G74A/G74B
N_gen=3 headline. It is a defect internal to the S³-torsion escape-route
program (E1-E15 / KT-8-KT-13), which was itself already explicitly labeled,
in `preprint.tex` and in `README.md`/`RESEARCH_STATUS_REPORT.md`, as a
"candidate mechanism," "physically unmotivated," and "not a step toward
N_gen=3" — **before** E12 ran. No overclaim in the current public-facing
text was found; if anything the text is already more conservative than the
question presupposes (see § 5 below, which is the one place this
reconciliation surfaced something worth flagging).

---

## 1. What operator does G74A's `dim ker = 1` actually refer to?

**Exact quote, `experiments/20260621-g73-three-channel-dirac/decision.md:8`:**
> "**Claim:** ind(D_{S⁶} ⊗ S⁻) = Â(S⁶) · c₃(S⁻)/2 = 1 per Z₃-triality channel."

**Exact quote, `experiments/20260621-g74a-lichnerowicz-gap/decision.md:8-9`:**
> "**Claim:** Two independent lemmas together prove dim ker(D_{S⁶}⊗S⁻) = 1
> EXACTLY per channel. This upgrades G73 (N_gen ≥ 3) to N_gen = 3 (no extra
> zero modes possible)."

The two lemmas that produce this exact count are both stated, explicitly, as
being about the S⁶ factor only:

- **Lemma A** (`experiments/20260621-g74a-lichnerowicz-gap/decision.md:11-24`):
  a Weitzenböck/Lichnerowicz spectral-gap argument "On round S⁶ with radius
  ρ₆" (line 15), comparing S⁶'s scalar curvature `R=30/ρ₆²` against the
  bundle curvature of `S⁻` — no S³ quantity appears anywhere in this
  argument.
- **Lemma B** (`experiments/20260621-g74a-lichnerowicz-gap/decision.md:33-42`):
  "S⁶ = G₂/SU(3): the twisted Dirac operator D_{S⁶}⊗S⁻ is G₂-equivariant" —
  again an S⁶-only coset-space/Peter-Weyl/Schur argument.

**Combined conclusion, same file, line 49:**
> "**Together: dim ker = 1 EXACTLY per channel**"

and line 51: "Three channels × 1 zero mode = **N_gen = 3 EXACTLY**."

**Direct answer to the assigned question:** G74A's `dim ker=1` refers
exclusively to the **S⁶-side twisted operator `D_{S⁶}⊗S⁻`**. The S³ factor
does not appear anywhere in G73's or G74A's derivation — not as an operator
factor, not as a multiplicity correction, not as an index contribution. The
"three channels" that get multiplied by 1 to give N_gen=3 are the three
Z₃-triality channels of the S⁶-side bundle `S⁻` (G67/G73), not three copies
of anything on S³. This is independently confirmed by G74B, which builds the
chirality argument purely from `ind(D^+_{S⁶}⊗S⁻)` and the same `dim ker=1`
input (`experiments/20260621-g74b-chirality-from-index/decision.md:8-9,
19-29`) — again zero mention of S³.

## 2. How does the torsion-escape-route program (E1-E15) itself describe its
relationship to G73/G74A/G74B?

**E7 (`experiments/20260717-round72-e7-t-selection-principle/decision.md`)**
never claims to be extending or fixing G73/G74A/G74B. Its own scope
statement (line 142-143):
> "Does not promote KT-8, does not touch E3's scope caveat, does not explain
> the n=1,2 crossings."

E7 is entirely about the **S³-side** connection family `∇^t` (Agricola's
Cartan-Schouten one-parameter family) and whether `t=0,1` are geometrically
distinguished — a question that only exists because of a **separate**,
later-discovered gap, KT-8, not because of anything wrong with G73/G74A/G74B.

**E12 (`experiments/20260717-round78-e12-multiplicity-gate/decision.md`)**
is the most explicit of all on this point. Its own go/no-go line (lines 5-8):
> "**Go/no-go:** This is a **real, unresolved problem for the
> torsion-escape-route program** (E2/E3/E7/E9/E9-followup). It is NOT
> resolved here, and no attempt is made to manufacture a resolution."

And its own "What this result does NOT kill" section (lines 148-151):
> "**What this result does NOT kill:** the t=0/t=1 flatness result itself
> (E7), the explicit parallel-spinor constructions (E9/E10) as MATHEMATICAL
> facts about `ker(D^t)`, or **G74A's own S⁶-side result. All of these
> survive completely intact** — only the IMPLICIT 'dim=1' assumption used
> when combining them into a generation count is affected."

And explicitly, line 190-192 ("What this does NOT mean," item 4):
> "Does **not** touch G74A's own S⁶-side result, which stands exactly as
> established (dim ker(D_{S6,twisted})=1 per channel, both directions
> closed)."

E12 names the program it threatens by its own label — "the
torsion-escape-route program" — and repeatedly, explicitly excludes
G73/G74A/G74B from the scope of its own finding.

**KT-8 itself** (`reports/PROJECT_360_ROUND3_SYNTHESIS.md:492-495`) states
the origin of the whole torsion-escape-route program and, symmetrically,
also excludes G73/G74A/G74B from its own blocking finding:
> "It does **not** contradict G73/G74A/G74B, G8, or any existing gate —
> those compute the index/kernel of D_{S⁶}⊗S⁻ *alone* on the S⁶ factor, and
> that computation is untouched by this finding."

and (line 496-499):
> "It **does** mean the 'zero modes' counted by the headline N_gen=3
> mechanism are zero modes of the S⁶-factor operator alone, not of the true
> 9D internal Dirac operator that would set 4D fermion masses in a standard
> Kaluza-Klein spectroscopy sense."

`reports/PROJECT_360_ROUND3_SYNTHESIS.md:894-937` (KT-12 section) frames E7
the same way — an attempt to find "an independent physical/geometric
selection principle for E2/E3's torsion parameter t," i.e. a candidate fix
for KT-8, explicitly noted (line 937) to "**not promote E2/E3** or change
KT-8's status in any way."

## 3. Is the torsion program part of the SAME published result, or a
SEPARATE attempt to fix a DIFFERENT gap (KT-8)?

Separate, and the sequencing is directly readable from
`reports/PROJECT_360_ROUND3_SYNTHESIS.md`'s own dated history:

- **2026-06-21:** G73/G74A/G74B PROMOTE — established purely on the S⁶
  factor (`D_{S⁶}⊗S⁻`), no S³ operator involved at all.
- **2026-07-16/17:** KT-8 discovered — the FULL 9D product operator
  `D_{S³×S⁶}` (untwisted, round, Levi-Civita S³ — the ansatz actually used
  in the paper) has **zero kernel**, `min|eig(D_full)| = 1.5` regardless of
  the S⁶ factor's spectrum (`reports/PROJECT_360_ROUND3_SYNTHESIS.md:487`).
  This is a **new, independent** finding about a **different operator** (the
  full product, not the S⁶ factor alone) than the one G73/G74A/G74B ever
  computed.
- **2026-07-17, same day:** E1-E15 (round65-round81) are a chain of attempts
  to find a modification of the S³ factor (torsion deformation, `t≠1/2`)
  that would give the FULL product operator a nonzero kernel — i.e., to
  patch KT-8, not to re-derive or extend G73/G74A/G74B's S⁶-only index
  count.
- **E12/E13 (KT-13)** then finds that the specific candidate patch
  (`t=0,1` torsion deformation) has its own internal defect: the S³-side
  kernel it supplies is 2-dimensional, not 1-dimensional, so even if this
  patch were physically motivated (which E7/KT-12 already found it is not —
  H1c/H2/H3 all OPEN or BLOCKED), it would give `3×2=6` internal states, not
  the needed 3.

The dependency graph is one-directional: KT-8 depends on nothing from
G73/G74A/G74B being wrong (both are explicitly independently-confirmed
correct, three times over, per KT-8's own text); the torsion program depends
entirely on KT-8 existing as a motivation; E12's multiplicity gap is a
defect purely internal to the torsion program's own candidate object,
`ker(D_{S³,t})`. There is no edge in this graph that runs from E12 back into
G73/G74A/G74B.

## 4. The reconciliation verdict

**ORTHOGONAL_EXPLORATORY_LINE**, per the pre-registered criteria in
`claim.md`.

- G73/G74A/G74B's `dim ker(D_{S⁶}⊗S⁻)=1 EXACTLY` result is about the S⁶
  factor alone. It has never depended on, and does not depend on, any
  property of the S³ factor's kernel — round, untwisted, or torsion-deformed.
  E12's finding (`dim ker(D_{S³,t})=2`) therefore cannot mathematically
  touch it: the two claims are about different operators on different
  factors, confirmed identical in every source read for this reconciliation
  (§1-§3 above, all citing the source documents' own words, not this
  reconciliation's inference).
- The torsion-escape-route program (E1-E15) exists to patch a **separate**
  gap, KT-8 — the full-operator zero-mode problem — which itself was
  discovered a month after G73/G74A/G74B were promoted, and which every
  source in this program (E7, E12, KT-8, KT-12, KT-13, all quoted above)
  consistently describes as independent of, and not a threat to,
  G73/G74A/G74B.
- Therefore the "search for a mechanism to resolve 6→3" is not solving a
  problem that threatens the headline N_gen=3 mathematical result — it is
  attempting to salvage a **candidate, already-flagged-as-physically-
  unmotivated escape route** for a different, admittedly still-unresolved
  problem (KT-8, the full-operator zero mode gap). Resolving 6→3 would not,
  by itself, establish physical N_gen=3 either (H1c/H2/H3 — why nature would
  select this torsion value at all — remain OPEN/BLOCKED regardless of the
  multiplicity count, per E7's own table,
  `experiments/20260717-round72-e7-t-selection-principle/decision.md:78-87`).
  Both problems (multiplicity, and physical selection of t) must be solved
  for the escape route to become a real resolution of KT-8; neither is
  solved yet; and even if both were solved, G73/G74A/G74B's own PROMOTE
  status would be unaffected, since that status was never conditioned on
  the escape route in the first place.

## 5. Overclaim / consistency check against the current public claim surface

Per the task's explicit instruction, the public-facing text
(`preprint.tex`, `README.md`, `RESEARCH_STATUS_REPORT.md`) was checked for
any statement that the torsion-escape-route is necessary for, or already
folded into, N_gen=3.

**No such statement was found.** If anything, the current text is *more*
conservative than a naive reading of "G73/G74A/G74B PROMOTE" would suggest,
because of KT-8 (a separate, prior correction, not something this
reconciliation needed to add):

- `preprint.tex:1467-1497` (the torsion item in the Open Problems section)
  is titled, verbatim:
  > "**$S^3$ torsion deformation: a candidate escape route for the
  > full-operator zero-mode gap [candidate mechanism --- physically
  > unmotivated, not a resolution].**"
  and ends (line 1496-1497):
  > "Recorded here as a candidate mechanism for future work, **not as a step
  > toward $N_{\mathrm{gen}}=3$**."
- `README.md:11-42` (a "Status correction" block dated 2026-07-17, i.e.
  written the same day as this program, already present before this
  reconciliation) states explicitly (lines 17-19, 26-33):
  > "**Unchanged and correct:** G73+G74A+G74B establish ind(D_{S⁶}⊗S⁻)=1 per
  > channel with an internally-certified 1-dimensional local kernel on the
  > S⁶ factor — a real, tool-verified mathematical result."
  > "**N_gen=3 is therefore not yet an established physical result** — only
  > a mathematical index on one factor, not a demonstrated massless 4D
  > fermion."
  > "**Candidate (mathematical, not physical) escape route found the same
  > day:** a torsion-deformed S³ connection removes this obstruction at
  > computable parameter values, but no physical principle is known for
  > selecting them over the standard connection used elsewhere. **Not a
  > resolution.**"
- `RESEARCH_STATUS_REPORT.md:9-21` carries the identical correction
  verbatim in substance: "**N_gen=3 is not yet an established physical
  result**... A torsion-deformed S³ connection gives a mathematical (not
  physical) candidate escape route, no selection principle known."

**Conclusion of the overclaim check:** the public claim surface already
treats the torsion program as non-load-bearing for N_gen=3, and already
treats physical N_gen=3 (as opposed to the S⁶-only mathematical index) as
*not yet established* — for reasons (KT-8) that have nothing to do with the
6-vs-3 multiplicity gap this reconciliation was asked about. E12's own
multiplicity finding has not yet been individually added to `preprint.tex`
(confirmed by grep — no hits for "multiplicity," "E12," "KT-13," or
"dim.*ker.*2" anywhere in `preprint.tex`; the only related passages are
about the `rho=7/rho=14` and G74A/G102 kernel-dimension audits, which are
unrelated open items). This is a **completeness gap, not a correctness/
overclaim risk**: because the torsion item is already scoped as "candidate,
not a step toward N_gen=3," omitting the further detail that its own
candidate kernel is 2-dimensional (not 1-dimensional) does not change what
a reader could conclude about N_gen=3's status — the item was already
telling the reader not to rely on it. Recommended as a low-priority future
edit (add one sentence to `preprint.tex:1467-1497` citing KT-13/E12's 6-vs-3
finding, for completeness), **not** an urgent fix, since no false claim is
currently being made.

## 6. Kill Analysis (per Anti-Overfitting Gate — recorded even though this is
a descriptive reconciliation, not a REJECT)

- **What this reconciliation rules out:** the reading in which "the E12/E13
  multiplicity gap threatens the published N_gen=3 headline" — that reading
  is false, per every primary source checked (§1-§4). It also rules out the
  weaker worry that the public docs might be silently relying on the
  torsion route without saying so — checked directly (§5), not found.
- **What remains unresolved:** the torsion program's own two internal
  problems (H1c/H2/H3 physical selection of t, and the 6-vs-3 multiplicity
  excess) are both still open; whether KT-8 (the full-operator zero-mode
  gap) will ever be resolved by any mechanism is unknown; whether some
  future mechanism could reconnect the S³-side kernel structure to
  G73/G74A/G74B in a way that *would* make it load-bearing is not excluded
  in principle, only shown to not currently be the case.
- **Relaxation map (if the situation changes):** if a future experiment
  proposes citing the torsion-escape-route's resolution (were it ever found)
  as *required* for physical N_gen=3 in the abstract or main text (rather
  than as a candidate fix for the separate KT-8 gap), that would be the
  trigger to re-open this reconciliation and re-check for overclaim.

## Check (reproduces this decision)

All claims above are grounded in direct `Read`/`Grep` of the cited files at
the cited line numbers, performed in this session:
- `experiments/20260621-g73-three-channel-dirac/decision.md`
- `experiments/20260621-g74a-lichnerowicz-gap/decision.md`
- `experiments/20260621-g74b-chirality-from-index/decision.md`
- `experiments/20260717-round72-e7-t-selection-principle/decision.md`
- `experiments/20260717-round78-e12-multiplicity-gate/decision.md`
- `reports/PROJECT_360_ROUND3_SYNTHESIS.md` (KT-8, KT-9, KT-12, KT-13
  sections, located via `Grep` before targeted `Read`)
- `preprint.tex` (grepped for "torsion", "multiplicity", "E12", "KT-13",
  "one generation"/"32 states"; targeted `Read` of lines 1440-1504)
- `README.md` (lines 1-45)
- `RESEARCH_STATUS_REPORT.md` (lines 1-45)

No new physics/math computation was performed. No existing file was
modified.
