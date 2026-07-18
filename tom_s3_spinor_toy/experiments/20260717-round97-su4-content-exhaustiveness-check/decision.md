# Round97 — Decision

**Date:** 2026-07-17
**Verdict:** `NO-GO_CONFIRMED__ROUND90_EXHAUSTIVENESS_HOLDS`
**Go/no-go:** round90's `(4,2,1)`/`(4̄,1,2)` cubic-`SU(4)³`-anomaly finding
rests on a complete field list; no counterexample found.

## Method

Direct `Grep` of `preprint.tex` (tool-verified, not from memory) for every
mention of `SU(4)`, `bidoublet`, explicit representation tuples
(`(4,2,1)`, `(4,1,2)`), and — more broadly — every fermion/singlet mention
in the document, to check for any additional chiral field carrying an
`SU(4)_{PS}` charge beyond the two already used by round90.

## Finding

`preprint.tex:289` ("Standard Model fermion content for one generation")
through `:362` enumerates the FULL fermion content this project ever
assigns: quarks, leptons, right-handed neutrino singlet (`:336-338`,
`Y=0`, `SU(3)_c` singlet, `SU(2)_L` singlet — itself consistent with, not
an addition to, the `(4̄,1,2)` multiplet's own singlet-under-`SU(2)_L`
component), and the Higgs bidoublet `(2,2)_0` (`:360-362`, `:1181`) — a
SCALAR, not a chiral fermion, hence structurally irrelevant to the
fermion-triangle cubic gauge anomaly regardless of any `SU(4)` charge it
might carry (gauge anomalies are sourced by chiral fermion loops only). No
additional chiral, `SU(4)`-charged fermion field is mentioned anywhere in
the document. Two literature citations (`:1210` Dolan-Nash, `:1220`
Spin(8)-triality lines) are external comparison points, not this project's
own field content.

## Applying the pre-registered criterion

**NO-GO CONFIRMED** — grep finds no additional chiral `SU(4)`-charged
fermion field beyond `(4,2,1)`/`(4̄,1,2)`. Round90's cubic-anomaly analysis
is based on a complete list, per this project's own text.

## Kill Analysis

- **What this confirms:** round90/95's assumption of exhaustive
  `SU(4)`-charged content — now independently grep-verified, not merely
  inherited.
- **What this does NOT resolve:** gate G97 (whether `SU(4)_{PS}` is
  geometrically realizable by ANY construction) — untouched, still the
  single decisive remaining gap in the Pati-Salam/anomaly route (see
  round96-goal-expansion-100 A1/E2 for continued search directions).
- **Net effect combined with round96 (E25):** the Pati-Salam/anomaly
  route's ENTIRE positive case now rests on gate G97 alone — every
  perturbative anomaly channel accessible within the already-geometrically-
  realized `G_eff=SU(3)_c×SU(2)_L×SU(2)_R` is checked and shows no forcing
  (round92, round96); the one channel that DOES force coexistence
  (`SU(4)³`, round90) requires `SU(4)` gauged, which is exactly what G97
  blocks, and this round confirms round90's own anomaly bookkeeping (not
  just G97's blocking status) is not undermined by some overlooked field.

## What this does NOT mean

Does not affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`,
`safe_for_runtime=False`. Does not modify `preprint.tex`. No file outside
this new folder was touched.

## Check (reproduces this decision)

```
grep -n 'SU(4)\|bidoublet\|fermion\|singlet' preprint.tex
```
