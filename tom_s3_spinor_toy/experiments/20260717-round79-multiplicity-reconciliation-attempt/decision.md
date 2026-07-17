# E13 (round79) — Decision

**Date:** 2026-07-17
**Verdict:** `STRUCTURAL_A_CONFIRMED__B_REFUTED__PHYSICAL_MECHANISM_STILL_OPEN`
**Go/no-go:** This narrows, but does **not** close, E12's Relaxation Map option 1
("reconcile the 32-state and zero-mode-kernel frameworks"). It rules out reading (b)
outright (not merely "unconfirmed" — a genuine category error under this project's own
existing convention), and finds that reading (a)'s *structural* half is an exact,
non-forced match to an independent, pre-existing project artifact. Reading (a)'s
*physical* half (why the S3 connection would take two different torsion values
simultaneously, in different chirality sectors) remains completely open, exactly as
unmotivated as the single-crossing selection problem the paper's own text (see below)
already disclaims having solved. **This is not full resolution.** Read the "What this
does NOT mean" section before citing this as closing E12's gap.

## Bottom line, stated plainly first

This project already has, at `experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`
(written 2026-06-15, roughly a month before the torsion-escape-route program existed,
so it was not built to match E9-E12), a table that splits the S3-side "4-component
SO(4) spinor representation" into exactly two 2-dimensional blocks:
```
chir_s3="+": T3L=+-1/2, T3R=0   -- SU(2)_L doublet, SU(2)_R singlet
chir_s3="-": T3L=0, T3R=+-1/2   -- SU(2)_L singlet, SU(2)_R doublet
```
This is an EXACT dimension-and-label match, checked computationally
(`e13_reconciliation_check.py`, reusing G6's own tables verbatim), to E11/round77's
tool-verified findings: `chir_s3="-"` == the `t=0` kernel (SU(2)_L singlet / SU(2)_R
doublet, dim 2); `chir_s3="+"` == the `t=1` kernel under `c0=-2` (SU(2)_L doublet /
SU(2)_R singlet, dim 2). This is reading **(a)'s structural claim, confirmed** — and it
is a genuinely surprising, non-manufactured finding, because G6 was never designed with
the torsion family in mind.

At the same time, the SAME script shows reading **(b) is refuted, not merely
unsupported**: in G6's own construction, the particle/antiparticle (CPT-conjugate)
doubling that takes "16" to "32" is carried ENTIRELY by the S6 factor (the sign of
B-L / the S+ vs S- chirality of the octonionic spinor), and the S3-side `chir_s3` label
is IDENTICAL for every one of the 8 checked particle/antiparticle pairs (`uL`/`uLbar`,
`dL`/`dLbar`, `uR`/`uRbar`, `dR`/`dRbar`, `nuL`/`nuLbar`, `eL`/`eLbar`, `nuR`/`nuRbar`,
`eR`/`eRbar` — all 8 pairs share `chir_s3`). This means the S3-side 2-dimensional kernel
cannot be relabeled as "particle + its own CPT conjugate" without directly contradicting
G6's own, already-established bookkeeping — the doubling that gives "plus their CPT
conjugates" (`preprint.tex:298`) lives on a different factor entirely.

## Result, section by section

### Section A — what `preprint.tex` and G6/G7 actually say about the "4" and "32" [VERIFIED-tool/DOCS]

1. `preprint.tex:292-298` ("Standard Model fermion content for one generation"):
   "The Dirac spinor on $S^3\times S^6$ decomposes ... into $(rep_{S^3})\otimes(rep_{S^6})$
   pairs, with $rep_{S^3}$ the 4-component SO(4) spinor representation ... **(representation
   dimensions, not a spacetime dimension count** --- see \S\ref{sec:open}, "Total
   dimension is 13, not 10")." This parenthetical is the paper's OWN explicit warning
   that "4" is a representation-theory bookkeeping label, not a count of actual
   solutions of any specific operator.
2. `preprint.tex:70-77` (abstract): "For the stated
   direct-product $S^3\times S^6$ Dirac operator with twisting only on $S^6$, the
   positive $S^3$ spectral gap prevents these modes from becoming zero modes of the
   full internal operator ... The gauge-structure and fermion-quantum-number results
   below should be read at the level of this $S^6$-factor mechanism, **not as an
   established 4D physical spectrum**." This is the paper's own, explicit,
   [VERIFIED-tool] (grep) statement that the 32-state/quantum-number bookkeeping is
   NOT tied to an actual zero mode of `D_full` in the untwisted construction.
3. `preprint.tex:1421,1452` (the "Full-operator zero-mode gap" item, KT-8): "$\ker
   D_{\mathrm{full}}=0$ ... This is a blocking gap, not merely an open question: the
   representation-theoretic quantum numbers derived elsewhere in this paper
   ... are not currently shown to correspond to an actual zero mode of the physical
   internal Dirac operator." Direct textual confirmation of Section A.1-2: the
   32-state bookkeeping and the "does a zero mode exist" question are explicitly
   flagged, by the paper itself, as two different things that have not been shown to
   connect.
4. `preprint.tex:1468,1487` (the "$S^3$ torsion deformation" item, the source of
   `t=0,1`): "**This does not resolve the gap above**: no physical principle is known
   for selecting $t=0$ (or any other crossing) over the Levi-Civita value $t=1/2$
   ... introducing torsion on $S^3$ specifically to zero out this obstruction, without
   an independent derivation of why nature ... would select that value, is exactly the
   kind of *fitted, not derived* reasoning this project avoids elsewhere." This is
   [VERIFIED-tool] (grep + read) confirmation that the paper explicitly disclaims a
   physical selection principle for even ONE crossing value — a precondition that
   matters directly for reading (a), below.
5. `experiments/20260615-g6-s3xs6-spinor-content/decision.md`: "Does NOT prove these
   are zero modes of the physical Dirac operator." `experiments/20260615-g7-kk-spectrum/claim.md`:
   "'Lightest level carries SM content' means representation-theoretically (from G6),
   NOT that these are the physical massless fermions ... NO zero modes exist on pure
   round $S^3\times S^6$ (Lichnerowicz theorem)." Both [VERIFIED-tool] (Read), both
   independently confirm Section A.1-3 from the *experiment* side, not just the paper
   text.
6. **Minor correction to E12's own citation:** E12 (round78, Section E.2) paraphrases
   this as "G7's own script: 'all 32 SM states appear at every (m,n) level'." Reading
   G7's actual `claim.md` directly, the precise statement is narrower: "The **lightest**
   KK level (m=0, n=0) carries all 32 SM states from G6" — G7 does not claim this for
   every `(m,n)` level, only the lightest one. This does not change E12's conclusion
   (the bookkeeping is still representation-content-only, disconnected from actual
   zero-mode existence, confirmed independently in points 1-5 above), but the "every
   level" phrasing should not be re-cited as if G7 said it literally.

**Conclusion of Section A:** the "32 = 4x8, one generation" framework in this project
is, by the paper's OWN explicit statements (not this experiment's interpretation), a
REPRESENTATION-CONTENT / gauge-quantum-number bookkeeping exercise, entirely prior to
and independent of the question "does an actual zero mode of `D_full` exist, and at
what dimension." This licenses treating the "4" as something that COULD, in principle,
be given a concrete physical realization by ANY mechanism that supplies the right
dimension and representation content on the S3 factor — which is exactly the kind of
match Section B checks for, without presupposing the answer.

### Section B — computational cross-check (`e13_reconciliation_check.py`) [VERIFIED-tool]

Script re-derives G6's full 32-state table from G6's OWN verbatim tables (S3-state
list, `bl_charge`, `SM_TABLE` including its own explicit "Conjugates" section) — this
is not new representation theory, it is a direct re-execution of an existing,
independent artifact for cross-checking purposes.

```
dim(chir_s3='+')  = 2   dim(chir_s3='-')  = 2
plus block is SU(2)_L doublet / SU(2)_R singlet: True
minus block is SU(2)_L singlet / SU(2)_R doublet: True
internally_consistent (no name maps to 2 different chir_s3): True

particle antiparticle  chir(p) chir(anti)  same?
      uL        uLbar        +          +   True
      dL        dLbar        +          +   True
      uR        uRbar        -          -   True
      dR        dRbar        -          -   True
     nuL       nuLbar        +          +   True
      eL        eLbar        +          +   True
     nuR       nuRbar        -          -   True
      eR        eRbar        -          -   True

verdict = {
  'g6_cross_check_32_of_32_matched': True,
  'dimension_match_t0': True, 'dimension_match_t1': True,
  'label_match_t0': True, 'label_match_t1': True,
  'internally_consistent': True,
  'cpt_doubling_independent_of_chir_s3': True,
  'structural_option_a_confirmed': True,
  'option_b_refuted': True,
}
```

Reading the table: `uL` and its antiparticle `uLbar` BOTH carry `chir_s3="+"` (they
differ only in their S6-side B-L sign, i.e. only in which SU(3) representation, `3` vs
`3bar`, and which hypercharge they carry) — the S3-side chirality label plays no role
in distinguishing particle from antiparticle anywhere in this table. Every one of the
8 checked pairs confirms this identically; `internally_consistent=True` additionally
confirms no SM name is inconsistently assigned two different `chir_s3` values anywhere
in the regenerated 32-state table (i.e. this is not an artifact of only checking 8 of
32 records — every record naming e.g. "uL" agrees on `chir_s3`).

### Section C — what this establishes for readings (a)/(b)/(c)

**Reading (a) — structural half: CONFIRMED, non-forced.** The G6 table already
requires, independently of any torsion-family consideration, that the S3-side "4"
splits into exactly a 2-dim SU(2)_L-doublet/SU(2)_R-singlet block and a 2-dim
SU(2)_L-singlet/SU(2)_R-doublet block — and this is EXACTLY what the tool-verified
E9-E12 zero-mode computations produce at `t=1` and `t=0` respectively, both in
dimension (2 each) and in representation label (singlet/doublet assignment, matching
E11's own finding under the SAME `SU(2)_L`=left-translation convention E11 already used
and flagged as an unstated-in-`preprint.tex` assumption). This is not a coincidence
manufactured for this experiment: G6 predates the torsion program by roughly a month
and was never built with `t=0,1` in mind, which is exactly why finding an exact match
here (rather than an approximate or reinterpretable one) is meaningful, tool-verified
evidence — not a comfortable post-hoc relabeling.

**Reading (a) — physical half: still OPEN, unchanged.** Confirming the structural match
does **not** supply, derive, or motivate a mechanism for the S3 connection actually
taking two DIFFERENT torsion values (`t=0` in the sector that becomes SU(2)_R-doublet
content, `t=1` in the sector that becomes SU(2)_L-doublet content) SIMULTANEOUSLY within
one physical construction. Section A.4 already tool-verified that this project's own
text disclaims having a physical selection principle for even ONE crossing value; a
simultaneous, sector-dependent pair is a STRICTLY LARGER, currently unmotivated
postulate — "why would the same geometric S3 factor carry two different torsion
connections depending on which SU(2) factor a fermion is charged under" is not asked or
answered anywhere in this project. This experiment does not attempt to answer it either
— per the Anti-Overfitting Gate, inventing such a mechanism here, just because the
representation-content dimensions happen to line up, would be exactly the "fitted, not
derived" pattern `preprint.tex` itself already warns against for the single-crossing
case.

**Reading (b): REFUTED**, not merely "unconfirmed" or "speculative." Under this
project's OWN existing 32-state bookkeeping (G6), the particle/antiparticle doubling is
demonstrably carried by a DIFFERENT factor (S6, via B-L sign) than the one E11's
SU(2)-doublet finding concerns (S3). Relabeling the tool-verified SU(2)_R-doublet
structure at `t=0` as "particle + antiparticle" would require asserting that G6's own
`chir_s3` label secretly ALSO encodes CPT conjugation — but the computation shows
`chir_s3` is identical across all 8 checked particle/antiparticle pairs, i.e. it carries
NO information distinguishing a particle from its antiparticle anywhere in this
project's existing bookkeeping. Additionally, on general grounds (not requiring the G6
cross-check): E11's finding is that the 2-dimensional kernel is closed under a
CONTINUOUS Lie-group action (`h.psi != psi` for generic `h in SU(2)_R`, a nontrivial
rotation) — CPT conjugation is a discrete, antiunitary operation, not a continuous
gauge rotation; treating a genuine irreducible continuous-group doublet as "particle +
antiparticle" would be a category error unless a further, independent postulate
supplied a reason the two are the same object under both operations simultaneously. No
such postulate exists in this project. Both the general argument and the concrete G6
cross-check point the same way.

**Reading (c):** does NOT apply in the simple "genuinely open, no traction anywhere"
form the task allows for as a legitimate outcome — this experiment found real,
tool-verified, non-manufactured structural traction for (a) that E12 did not have
(E12 checked only the summary text at `preprint.tex:292-298`, not the underlying G6
script's `chir_s3` split, so it correctly reported this avenue as merely "real but
unresolved" without having actually run this specific check). However, "(a) structural
half confirmed, physical half open" and "(c) open, no traction" converge on the SAME
practical conclusion for the torsion-escape-route program right now: **the multiplicity
gap is not resolved, and no comfortable resolution should be adopted**, because reading
(a) in full (the only complete reading that would resolve E12's gap) needs a physical
mechanism this project does not have.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** reading (b) ("the doublet IS the particle+antiparticle
  pair") as a viable resolution of E12's multiplicity-2 finding, under this project's
  own existing bookkeeping conventions. This is a genuine kill, grounded in a direct
  computation on an independent, pre-existing artifact (G6), not merely "not yet
  confirmed."
- **What this result does NOT kill:** reading (a)'s structural half, which survives and
  is strengthened (an exact, non-manufactured dimension-and-label match to a
  month-older, independently-motivated artifact). It also does not touch E9's/E10's/E11's
  own findings (parallel-spinor constructions, representation labels), which this
  experiment reuses by citation without re-deriving.
- **What survives, confirmed stronger than before:** the SU(2)_L-doublet /
  SU(2)_R-doublet split this project's torsion-escape zero modes exhibit is not an
  arbitrary artifact of the specific torsion construction — it matches, dimension for
  dimension and label for label, a REPRESENTATION-CONTENT requirement this project
  already had, independently, before the torsion program existed. This gives any future
  attempt at reading (a)'s physical half a concrete, specific target to explain (why
  would `t=0` be selected in exactly the sector that needs an SU(2)_R doublet, and
  `t=1` in exactly the sector that needs an SU(2)_L doublet) rather than an unstructured
  "the numbers happen to match."

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Physical mechanism for sector-dependent torsion | Independent derivation (not fitting) of why the effective S3 connection differs between the SU(2)_L-doublet and SU(2)_R-doublet sectors of the SAME KK tower — e.g. from a parent action, a chirality-dependent coupling to the torsion 3-form, or a reason the "which translation direction (left/right) a fermion is charged under" determines which torsion crossing it sees |
| Reconcile with the S6-side and channel-count logic | Even with (a)'s physical half solved, the resulting S3-side content (4, from 2+2) combined with `dim ker(D_{S6,twisted})=1` per channel (G74A) and 3 channels gives `4x1x3=12` internal zero modes — not obviously `32` (G6's one-generation count, which uses the FULL "8" S6 representation, not the twisted operator's 1-dim kernel) or `3` (E12's "needed" target). This experiment does not attempt this second reconciliation; it is a distinct, still-open question this decision explicitly does not resolve. |
| Independent verification of the `SU(2)_L`=left-translation convention | Unchanged from E11: still an imported, not paper-derived, assumption (`preprint.tex` never states which translation direction is `SU(2)_L`) |
| Verify `psi^(1)` exists under this project's own calibrated `c=+2`, not only `c0=-2` | Unchanged from E10/E11: round76 Part 4 found the one candidate tested fails under `c=+2` |

## Assumptions carried, unresolved

- E11's `SU(2)_L`=left-translation identification (imported convention, not stated in
  `preprint.tex`) is reused here without re-derivation; if reversed, the `chir_s3="+"`/
  `chir_s3="-"` labels in G6 would need re-checking against the FLIPPED E11 labels too
  (this would not change the DIMENSION match, only which block is called `SU(2)_L` vs
  `SU(2)_R`-doublet — the structural finding that dimensions 2+2 match is convention-independent).
- `psi^(1)`'s existence only under `c0=-2` (round76 Part 4), not this project's own
  calibrated `c=+2`, is reused unchanged.
- KT-8 (no zero mode of the untwisted `D_full` exists at all) is reused unchanged; this
  experiment's finding concerns representation-content matching, which per Section A is
  explicitly independent of KT-8's zero-mode-existence question.

## What this does NOT mean

1. Does **not** establish a physical mechanism for simultaneous, sector-dependent
   torsion — the single largest remaining gap, stated plainly.
2. Does **not** reconcile the resulting S3-side count with the S6-side "8"/`G74A`'s "1
   per channel"/`G73`'s "3 channels" framework into one consistent total — a separate,
   still-open reconciliation.
3. Does **not** resolve H1c (which of `t=0`/`t=1` alone, if either, is physically
   selected) or KT-8 (whether ANY zero mode of the untwisted `D_full` exists).
4. Does **not** imply E12's "excess factor of 2" framing was simply wrong — E12's dim
   ker computation and "needed=3" framing both stand; this experiment instead shows that
   the natural "needed" TARGET for the S3 factor, per this project's own pre-existing
   G6 bookkeeping, may itself be revisited (dimension 4 = 2+2, not "1 per channel") IF
   reading (a)'s physical half is ever established — but that "if" is precisely the
   unresolved part.
5. Does **not** claim novelty in observing that CPT conjugation and continuous gauge
   rotation are different kinds of operations — this is standard; what is new here is
   the concrete, tool-verified demonstration that THIS project's own existing 32-state
   table already keeps them on different factors (S3 vs S6), closing off reading (b)
   specifically for this project's own bookkeeping, not as a general physics claim.

## Check (reproduces this decision)
`python e13_reconciliation_check.py` →
`verdict.structural_option_a_confirmed==True`,
`verdict.option_b_refuted==True`,
`verdict.label=="STRUCTURAL_A_CONFIRMED__B_REFUTED__PHYSICAL_MECHANISM_STILL_OPEN"`.
