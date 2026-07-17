# E22 (round95) — Decision

**Date:** 2026-07-17
**Verdict:** `TENSION_DISSOLVES__CONTINGENT_ON_H1C_KT8_STAYING_OPEN`
**Go/no-go:** L5's `S^6`-side chirality asymmetry and round90's `S^3`-side
Pati-Salam anomaly requirement are, as this project's text currently stands,
claims about two different, currently-unlinked invariants: L5 is an exact
statement about `D_{S^6}\otimes S^-` alone (an S6-only topological index fixing
the TOTAL generation count via triality); round90's anomaly requirement is a
statement about the S3 factor's own `SU(2)_L`/`SU(2)_R` representation content
(governed by the connection parameter `t`, via H1c — still open). No
established derivation in this project links "which S6 triality-channel +
chirality-sector" to "which S3 `t`-sector," so L5's result does not currently
entail, constrain, or contradict any specific count of S3-side `SU(2)_L`- vs.
`SU(2)_R`-doublet matter. **This dissolution is honestly contingent, not
permanent** — see Section 5 for the concrete, falsifiable way it could turn
into a real contradiction if H1c/KT-8 is ever resolved in one particular
direction.

---

## 1. What does `sign(ind)=+1` (Lemma L5) actually count? [VERIFIED-tool/DOCS]

**Answer: reading (a) — a net topological index (Atiyah-Singer), computed
entirely on the `S^6` factor, per triality channel. NOT reading (b) — it does
not, by itself, specify or constrain each generation's `SU(2)_L`/`SU(2)_R`
representation content on the `S^3` factor.**

### 1a. The derivation itself is S6-only

`preprint.tex:886-897` (Lemma L5, read directly this round, exact current
text): "The net chirality is left-handed: `sign(ind)=+1` forces a left-handed
excess among the three Dirac zero modes `psi^(alpha)` (`alpha in {v,s,c}`),
unconditionally. With the L4B rank result (`dim ker(D^+|_1)=1`,
Section~\ref{sec:kernel}...), all three zero modes are purely left-handed."

`preprint.tex:898-903`: "`sign(ind) = sign(c_3(S^-)) = sign(+2) = +1`. A
positive index means `dim ker(D^+) > dim ker(D^-)`, regardless of the L4B
trivial-sector rank... With the verified `dim ker(D^-)=0`... all three zero
modes are in `D^+`."

`G74B` (`experiments/20260621-g74b-chirality-from-index/decision.md:11-31`,
reused, not re-derived): "`D^+: S^+ \otimes E \to S^- \otimes E`... Atiyah-
Singer: `ind(D^+\otimes E) = dim ker(D^+) - dim ker(D^-)`. From G74A: `dim
ker(total) = dim ker(D^+)+dim ker(D^-) = 1` (per channel). From G73: `ind =
dim ker(D^+) - dim ker(D^-) = +1` (per channel)... unique solution: `dim
ker(D^+)=1, dim ker(D^-)=0`... Three channels: `3x(L=1,R=0)` → 3 left-handed
zero modes, 0 right-handed." And the sign itself: "`ind = Â(S^6)*c_3(S^-)/2 =
1*(+2)/2 = +1`... `c_3(S^-)=+2 >0` (positive, from G33: `chi(S^6)=+2` with
standard orientation)."

Every input to this computation — `D^+`, `D^-`, `c_3(S^-)`, `chi(S^6)`, the
`G_2`-branching triality channels — is a property of the `S^6` factor's own
twisted spinor bundle and Dirac operator. Nothing in the derivation refers to
the `S^3` factor, the connection parameter `t`, or any `SU(2)` gauge quantum
number. This is the same fact E17 (round85) already used, by direct citation
of the paper's own Proposition-T2 discussion (`preprint.tex:135-140`, quoted
in full in Section 1b below): the S6-index computation is "an exact statement
about `D_{S^6}\otimes S^-` alone."

### 1b. The project's own text disclaims that this index says anything about
the S3 factor, by itself

`preprint.tex:135-140` (read directly this round, exact current text,
discussing why the untwisted-`S^3` Proposition T2 does not immediately kill
the twisted-index mechanism): "the full operator decouples exactly as
`D_full^2 = D_{S^3}^2\otimes 1 + 1\otimes D_{S^6,S^-}^2`... so the untwisted
`S^3` factor's strictly positive spectral floor `(3/2 rho_3)^2` survives
unconditionally: `ker D_full=0` regardless of the `S^6`-factor's twisted
index. **The three-channel index computation is therefore an exact statement
about `D_{S^6}\otimes S^-` alone, not — without a further physical ingredient
acting on the `S^3` factor — about a massless 4D fermion mode of the full
construction.**"

This is the load-bearing sentence for Question 1: this project's OWN text,
independent of this experiment, already states that the S6-index result does
NOT by itself describe a full, physical 4D fermion — constructing one requires
"a further physical ingredient acting on the `S^3` factor" that is not
supplied by L5/G73/G74A/G74B. E17 quotes and relies on this exact sentence
(`experiments/20260717-round85-e17-sector-coexistence-gate/decision.md:9-16`).

### 1c. The "left-handed = SU(2)_L doublet" language is an informal, aspirational
label, not a derived cross-factor link

`preprint.tex:908-912` (read directly this round): "Matching the `S^6`
orientation convention to the SM convention for `SU(2)_L`, the left-handed
Dirac zero mode corresponds to the left-handed SM fermion doublet." This
sentence performs a NAMING MATCH — it borrows the Standard Model's own
convention (in the SM, "left-handed" 4D-Weyl fermions are, by the SM's own
chiral gauge-theory construction, `SU(2)_L` doublets) to say what physical
role this S6-chirality sector WOULD play, once/if a full 4D fermion is
constructed. It is not, and — per Section 1b — cannot yet be, a claim that
THIS project's own `S^3`-factor construction assigns that role to one
specific `t`-sector, because:

- which `t`-sector (`t=0` or `t=1`) pairs with which S6-triality-channel to
  form an actual 4D fermion is exactly this project's own open question H1c
  (`experiments/20260717-round83-joint-representation-decomposition/
  decision.md`; carried forward unresolved through E9, E12, E16, E17, E18/
  round86 — see also E17's own framing below, Section 2), and
- E17 Section 1 (`experiments/20260717-round85-e17-sector-coexistence-gate/
  decision.md:18-30`) establishes that `SU(2)_L`-vs-`SU(2)_R` representation
  content on the `S^3` factor is determined ENTIRELY by which `t`-sector
  (`t=0` ↔ one representation, `t=1` ↔ its mirror, `{(1,2),(2,1)}` under either
  labeling convention) is physically present — a completely separate piece of
  machinery from the S6-index computation.

**Conclusion for Question 1: `sign(ind)=+1` counts (a) — a net topological
index / generation-count on the `S^6` factor, entirely independent of, and
prior to, any specific claim about the `S^3` factor's `SU(2)_L`/`SU(2)_R`
representation content. Its "left-handed"/"SM doublet" language is a
physical-interpretation label for what this S6-sector WOULD become, not an
already-established statement of WHICH `S^3` `t`-sector it pairs with.**

---

## 2. What does round90's Pati-Salam argument actually require? [DOCS, reused]

Per round90/E21 Section 4 (`experiments/20260717-round90-pati-salam-gauge-
completeness/decision.md:230-274`, reused verbatim, not re-derived): the
argument requires that "a genuinely gauged `SU(2)_R` with charged matter
cannot leave that matter as `SU(2)_R` singlets — it must organize into
complete `SU(2)_R` doublets" and, combined with E9/E12's fact that only `t=0`
and `t=1` have nonzero `S^3`-side kernel, concludes "there is nowhere else
within this specific connection family to obtain the required `SU(2)_R`
doublet's worth of matter except `t=0`'s kernel."

This is reading (b) as posed in the task, but with a sharper qualification
worked out fresh here in Section 3: it is a requirement about REPRESENTATION
CONTENT — that matter transforming as `(4,2,1)` (`SU(2)_L` doublet) and matter
transforming as `(4̄,1,2)` (`SU(2)_R` doublet) must BOTH exist in this
project's matter content — and per round90's own corrected Section 3a/3, the
formal anomaly condition is stated as a SUM condition: `A(F_L) + A(F_R^c) = 0`
(cubic `SU(4)^3` anomaly), not an a priori "`N_L = N_R`" axiom.

**Critically, this requirement is defined entirely on the `S^3` factor** — it
concerns which `SU(2)_L`/`SU(2)_R` representations this project's matter
content contains, which (per Section 1c / E17 Section 1) is governed
exclusively by the `S^3` connection parameter `t`, not by anything on the
`S^6` factor.

---

## 3. Does the cubic anomaly condition actually require `N_L = N_R`, or is it
weaker? [Worked out directly, not asserted]

Round90's own text (`decision.md:12-18`, the correction note) frames the
requirement as "only their SUM vanishes" and contrasts this with "`N_L = N_R`"
as though the sum-condition were strictly weaker. **Worked out directly here:
for THIS project's specific, already-established matter content, the two
conditions are mathematically equivalent — not weaker.**

The general cubic-anomaly condition is `sum_i (mult_i * A_i) = 0`, summed over
ALL chiral-fermion representations charged under the gauged group (`SU(4)` in
this case; scalars such as the Higgs bidoublet do not contribute to a gauge
anomaly, which is a purely chiral-fermion-loop effect). Per round90 Section
3a (reused): `A(4,2,1) = +2`, `A(4̄,1,2) = -2` — these coefficients are FIXED,
generation-independent numbers (each copy of `(4,2,1)` contributes exactly
`+2`; each copy of `(4̄,1,2)` contributes exactly `-2`).

Per E17 Section 1 (`decision.md:73-80`, reused): under either labeling
convention, `{ker D^{t=0}, ker D^{t=1}} = {(1,2),(2,1)}` EXACTLY — i.e., this
project's `S^3`-connection-family construction supplies ONLY these two
representation types, and no others (no exotic `SU(4)`-charged representation
appears anywhere in this project's established S3-side content).

**If** `n_L` denotes the total number of generations whose `S^3`-side content
is realized in the `(4,2,1)`-type ("`SU(2)_L` doublet") sector, and `n_R` the
number realized in the `(4̄,1,2)`-type ("`SU(2)_R` doublet") sector, and no
other `SU(4)`-charged matter exists (per E17), then:

```
sum = n_L*(+2) + n_R*(-2) = 0   =>   n_L = n_R
```

**This is elementary arithmetic on round90's own cited coefficients, given
E17's own cited restriction to exactly two representation types — not an
assumption imported from outside this project.** So: **within this project's
own specific, already-established matter content, "representation-content
coexistence" and "count symmetry (`N_L = N_R`)" are the SAME requirement, not
two different strengths of requirement.** Round90's own framing of the sum-
condition as categorically weaker than `N_L=N_R` is correct IN GENERAL gauge
theory (extra compensating representations could unbalance the sum without
requiring `n_L=n_R`) but does not describe a genuine escape route available
to THIS project, because no such compensating representation exists in its
own established content. This refines, but does not overturn, round90's
Section 4 conclusion — round90's own "forced, not free" framing (`decision.md:
258-263`) is, if anything, strengthened by this arithmetic.

---

## 4. Direct resolution: same invariant or different invariants? [Combining 1-3]

**Different invariants, currently unlinked in this project's own text.**

- L5/G74B's `sign(ind)=+1` fixes a property of the **`S^6` factor**: the total
  number of independent triality channels with a surviving, chirality-definite
  zero mode (giving `N_gen=3`), and — per channel — which of the two `S^6`-
  spinor-bundle sectors (`D^+` vs `D^-`) that zero mode occupies. This is a
  count/index defined without reference to `t`, `SU(2)_L`, or `SU(2)_R`.
- Round90's Pati-Salam requirement (as sharpened in Section 3) fixes a
  property of the **`S^3` factor**: how many of the (up to 3) generations'
  `S^3`-side content is realized in the `t=0` sector (`SU(2)_R`-doublet-type)
  vs. the `t=1` sector (`SU(2)_L`-doublet-type) — requiring `n_L = n_R`.
- **No established derivation in this project's text specifies a pairing rule
  between "which `S^6` triality-channel + chirality-sector" and "which `S^3`
  `t`-sector."** This pairing is exactly what constructing an actual, full 4D
  massless fermion mode would require (Section 1b's "further physical
  ingredient acting on the `S^3` factor") — and per E17's own headline verdict
  (`BLOCKED__REPRESENTATION_CONTENT_CONSISTENT__PHYSICAL_COEXISTENCE_
  UNDECIDABLE_WITHOUT_PARENT_ACTION`) and E18/round86's `BLOCKED` verdict on
  the same underlying question (KT-1), this pairing rule (H1c) is explicitly,
  repeatedly flagged as OPEN — not derivable from anything this project
  currently has.

Since the two claims are about different mathematical objects (an S6-only
index vs. an S3-only representation-content count) and no bridge between them
is established, **L5's asymmetric S6-result does not currently entail, imply,
or contradict any specific value of `n_L` or `n_R` on the S3 side.** The
apparent tension flagged by E14 Reading 3 and round90 Section 5c rests on
reading L5's informal "left-handed = SM `SU(2)_L` doublet" LABEL (Section 1c)
as if it were already a cross-factor derivation — which, per Sections 1b-1c,
it is not.

**Verdict: `TENSION_DISSOLVES`, as this project's text currently stands.**

---

## 5. Honest contingency — why this dissolution is not permanent

A `TENSION_DISSOLVES` verdict must not be read as "this can never become a
real problem." It is contingent on H1c/KT-8 remaining open, in a specific,
falsifiable sense worth naming explicitly (per this project's own Anti-
Overfitting Gate discipline — a NULL/BLOCKED-adjacent finding must still say
what it does NOT kill):

**If** this project ever establishes a definite pairing rule linking S6-
triality-channels to S3 `t`-sectors (closing H1c/KT-8), **and** that pairing
rule assigns ALL 3 generations to the SAME `S^3` `t`-sector — which is exactly
what a LITERAL, non-aspirational reading of L5's "all three zero modes are
purely left-handed" (`preprint.tex:891-892`) would suggest, if that sentence
is ever upgraded from an interpretive label to an actual derived cross-factor
statement — **then** the tension becomes concrete and sharp: `n_L=3`,
`n_R=0`, which:

1. Violates round90's Section 3-4 anomaly requirement `n_L=n_R` (Section 3
   above) directly (`3 != 0`).
2. **Additionally and independently** would violate Witten's `SU(2)` global
   anomaly for `SU(2)_L` itself (round90 Section 3a, `Phys. Lett.` B117 (1982)
   324-328, reused by citation): an `SU(2)` gauge theory with an ODD number of
   doublets is inconsistent, and `n_L=3` is odd. This second consequence is a
   NEW observation (not previously flagged in E14 or round90) worth recording
   as a pearl candidate (below) — it does not change today's verdict, since it
   only fires under the same not-yet-established literal-pairing scenario.

This is the concrete, falsifiable form the Relaxation Map takes: the
dissolution found here holds only in the ABSENCE of a specific future result
(a literal, derived S6-to-S3 pairing forcing all 3 generations into one
`t`-sector). It is not evidence that no such pairing exists — only that none
is currently established.

---

## 6. Was flagging this tension at E14/round90 reasonable, or could it have
been resolved earlier? [Honest either-way assessment, per the task's own
instruction]

**Mixed — reasonable caution at E14's time; a resolvable oversight by
round90's time, using material round90 itself already had.**

- **E14 (round80):** at the time Reading 3 was written, this experiment's own
  Section 1b/1c distinction (S6-index vs S3-representation-content) was not
  yet articulated anywhere in the project, and E17 (round85, which supplies
  the clean `{(1,2),(2,1)}` table) had not yet been run. Flagging "this
  sits in tension with L5's established asymmetric result" as an open,
  unreconciled item was a fair, honest thing to do with what was known then —
  it correctly refused to assert the tension was resolved, and correctly
  refused to assert it was fatal. This was reasonable caution, not an error.
- **Round90 (E21), Section 5c:** by this point, E17 Section 1's
  representation table AND the exact `preprint.tex:135-140` "S6-index alone,
  not about a massless 4D fermion mode of the full construction" sentence
  were both already available — round90 itself cites E17 elsewhere (Section
  4) and could have applied the same count-vs-content distinction this
  experiment makes. Instead, Section 5c restates the tension as "sharpened,"
  without checking whether L5's asymmetry is even a claim ABOUT the same S3-
  side quantity round90's own argument concerns. **This was a resolvable gap
  at round90's own time, using round90's own already-cited sources** — not a
  new fact this experiment had to independently discover from scratch. Stated
  honestly, without excusing it: this is a case where the "count vs. content"
  distinction could have narrowed Section 5c's finding from "unresolved
  tension, sharpened" to "apparent tension dissolves under inspection, subject
  to a stated contingency" one round earlier than it did.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the specific reading of L5's "left-handed/SM
  `SU(2)_L` doublet" sentence (`preprint.tex:908-912`) as an ALREADY-derived
  statement about the `S^3` factor's representation content — it is not; per
  Sections 1b-1c it is an informal label pending the still-open H1c/KT-8
  pairing. It also kills round90's own implicit framing of "sum condition
  weaker than `N_L=N_R`" as an escape route available to THIS project
  specifically (Section 3) — for this project's own restricted matter content,
  the two conditions are equivalent.
- **What this result does NOT kill:** H1c (which `t`-sector, if either, is
  physically selected) — untouched, exactly as open as E9-E18 left it. KT-8
  (whether a stated 13D parent action exists) — untouched. The `N_gen=3`
  headline claim (G73/G74A/G74B) — untouched, and this experiment reconfirms
  it is logically independent of the S3-side program this tension concerns.
  Round90's own `BLOCKED` verdict on full Pati-Salam gauge completeness —
  untouched; this experiment addresses only the narrower Section 5c tension,
  not round90's Section 5a (`SU(4)` incompleteness) or 5b (anomaly-check-
  language gap), both of which stand as round90 left them.
- **What survives, confirmed here:** the S6-index (L5) and the S3-
  representation-content question (round90) are different invariants, with no
  established bridge between them in this project's current text — this is a
  citation-level finding (Sections 1b, 1c, 4), not a new numerical result.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Close H1c/KT-8 with a definite S6-channel↔S3-`t`-sector pairing rule | A stated 13D parent action (E18/KT-1's core gap) specifying independent fields for `t=0` and `t=1` and how each couples to the 3 triality channels — not attempted here |
| Check whether such a pairing, if found, assigns all 3 generations to one `t`-sector or splits them | Depends entirely on the still-missing parent action; cannot be checked in advance of it |
| If the "all-3-to-one-sector" scenario of Section 5 is ever realized | Would need to reconcile with BOTH round90's `n_L=n_R` requirement AND the newly-flagged Witten-odd-doublet problem (Section 5, point 2) — a strictly harder combined constraint than round90 alone identified |
| Upgrade L5's "left-handed = SM doublet" sentence from label to derivation | Would require an explicit argument for why the S6-chirality sector (`D^+`/`D^-`) determines, rather than merely suggests a name for, the S3 `t`-sector — not supplied anywhere in this project currently |

## Pearl-registry candidate

**Observation:** if this project's H1c/KT-8 gap is ever closed by a pairing
rule that assigns all 3 generations to the same `S^3` `t`-sector (matching a
literal reading of L5's "all three purely left-handed"), the resulting
`n_L=3` would ALSO independently violate Witten's `SU(2)` global anomaly for
`SU(2)_L` (odd doublet count) — a stronger and more immediate inconsistency
than the cubic-anomaly `n_L=n_R` violation round90 already flagged, since
Witten's anomaly is a nonperturbative, all-or-nothing consistency condition on
`SU(2)_L` alone, not requiring any matching to `SU(2)_R` content at all.
**Falsifiable prediction:** if/when H1c is ever closed, the FIRST check on any
proposed pairing rule should be "is the resulting per-`SU(2)_L`-sector doublet
count even," before even reaching round90's `SU(4)`-anomaly question.
**Impact score ~4** (affects how any future H1c/KT-8-closing attempt in this
project must be checked; narrow, project-internal — not registered to the
global registry). `next_check`: before any future experiment claims to close
H1c/KT-8, verify the resulting `S^3`-side doublet counts against BOTH this
project's own round90 cubic-anomaly requirement AND this Witten-parity check,
not round90's condition alone.

## Assumptions carried, unresolved

- `D_full^2 = D_{S3,t}^2 \otimes I + I \otimes D_{S6,twisted}^2` (E2/E12's
  decoupling ansatz) — presupposed throughout, exactly as E9-E21 presuppose it;
  not re-litigated here.
- E17 Section 1's `{(1,2),(2,1)}` representation-content table — reused
  exactly as established; the `t=1` entry holds only under `c0=-2`
  (`CONVENTION_TABLE.md` row 5), carried forward unresolved.
- Round90 Section 3a's cubic-anomaly coefficients (`A(4,2,1)=+2`,
  `A(4̄,1,2)=-2`) — reused from round90's own `[VERIFIED-tool]`-sourced
  Wikipedia quote and `[WEAK]`-sourced modern-paper cluster; not
  independently re-verified against a primary source this round.
- Whether any OTHER `SU(4)`-charged representation could ever enter this
  project's construction (which would reopen the "sum condition weaker than
  `N_L=N_R`" escape route dismissed in Section 3) — not checked here; assumed
  absent based on E17's own stated exhaustive `{(1,2),(2,1)}` finding, which
  itself concerns only the S3-connection-family's OWN kernel content, not a
  proof that no other geometric mechanism could ever supply additional
  `SU(4)`-charged matter.

## What this does NOT mean

1. Does NOT resolve H1c or KT-8 — both remain exactly as open as E9-E18 left
   them.
2. Does NOT affect the `N_gen=3` headline claim (G73/G74A/G74B) — confirmed
   here, via citation, to be logically independent of this tension.
3. Does NOT overturn round90/E21's own `BLOCKED` verdict on Pati-Salam gauge
   completeness (Sections 5a, 5b, 5d of that experiment stand unchanged) — this
   experiment addresses only round90's own Section 5c narrowly.
4. Does NOT claim the tension can never recur — Section 5 states precisely,
   and without hedging, the specific future scenario that would revive it.
5. Does NOT claim round90's general "sum condition weaker than `N_L=N_R`"
   framing is wrong in general gauge theory — only that it does not describe
   an available escape route for THIS project's own specific, already-
   established S3-side matter content (Section 3).
6. Does NOT introduce any new numerical computation or script — this is a
   citation-level classification round, following round86-90's own precedent
   for literature/text-classification experiments.

## Check (reproduces this decision)

This is a citation-and-classification round; there is no new numerical script
(per round86-90's own precedent). The "check" is: every `preprint.tex` line
cited above (135-140, 886-897, 898-903, 908-912) was read directly this round
via `Read`/`Bash sed`, not from memory or a prior round's paraphrase; every
internal experiment citation (G74B, E12/round78, E17/round85, round90/E21,
G23) was reused by direct `Read` of the cited file this round; Section 3's
arithmetic (`n_L=n_R` from the sum condition given exactly two fixed-
coefficient representation types) is elementary algebra on round90's own
cited coefficients and E17's own cited representation-exhaustiveness claim,
shown explicitly rather than asserted; the final verdict follows deductively
from Sections 1-4 applied to the pre-registered criteria in `claim.md`, with
the contingency (Section 5) and reasonableness assessment (Section 6) stated
honestly per the task's own instruction not to force either outcome.
