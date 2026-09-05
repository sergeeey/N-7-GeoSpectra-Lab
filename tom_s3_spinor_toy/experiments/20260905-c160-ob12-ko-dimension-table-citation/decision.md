# C160 Decision — OB12: sign-triple <-> KO-dimension table citation

**Date:** 2026-09-05
**Executing agent:** fresh continuation (general-purpose), no turn-limit constraint.
**Prior attempts:** two prior "verifier" subagent runs made verbal claims of having
found the table but hit an 8-turn limit before writing anything. Both treated as
**UNVERIFIED** per this round's brief. This document is the first written record.

---

## What was searched (in the order claim.md specified)

### Route A — Connes, "Gravity coupled with matter and the foundation of
non-commutative geometry", arXiv:hep-th/9603053 (1996)

Fetched via `mcp__arxiv__download_paper` (HTML endpoint, 66784 raw chars) and read
in full via `mcp__arxiv__read_paper` (dumped to a local file because the full text
exceeded the tool-call token cap; searched programmatically with a small Python
script reading that file — not recalled from memory).

**Found the general axiom and its table**, in the paper's own words (source text,
verbatim, offset ~23490 in the fetched HTML-to-text conversion):

> "7) Reality. There exists an antilinear isometry J : H -> H such that
> J a J^{-1} = a* for all a in A and J^2 = epsilon, J D = epsilon' D J and
> J gamma = epsilon'' gamma J where epsilon, epsilon', epsilon'' in {-1,+1}
> are given by the following table from the value of n modulo 8,
>
> n =        0    1    2    3    4    5    6    7
> epsilon    1    1   -1   -1   -1   -1    1    1
> epsilon'   1   -1    1    1    1   -1    1    1
> epsilon''  1   -1    1   -1  [row visually cuts off in the HTML extraction
>                                after 4 entries — see Data Quality Note below]"

This IS the "table over n mod 8 with rows for J^2, JD vs DJ, J-gamma vs gamma-J"
described in the task brief, from Connes' own axiom paper, in his own notation
(epsilon, epsilon', epsilon'' — same names OB12's text anticipated). Convention:
`epsilon = J^2`, `epsilon' ties J D = epsilon' D J` (i.e. `J D J^-1` vs `D`),
`epsilon'' ties J gamma = epsilon'' gamma J` (i.e. `J gamma J^-1` vs `gamma`).
This ordering is **identical** to this project's own tuple ordering
`(J^2, JDJ^-1/D, JgJ^-1/g)` — no reordering needed to compare.

**Data Quality Note (honest, not glossed over):** the `epsilon''` row, as
extracted from arXiv's HTML rendering of this 1996 paper, visually terminates
after 4 values (`1, -1, 1, -1` for n=0..3) before the surrounding prose resumes
("We can now state our first result, Theorem..."). This is very likely an
artifact of the HTML5 conversion of old TeX table markup (`\hbox`/`\cr`-style
plain-TeX tables render unreliably through arXiv's auto-converter), not a
genuine 4-column table in the original — Connes' table is universally cited
elsewhere as an 8-column table. **This was not silently trusted or extrapolated**
(extrapolating a period-2 pattern would in fact give the WRONG answer for n=6,
see below) — Route B below supplies the missing n=6 value directly and
explicitly, from prose, not from this incomplete table.

### Route B — Chamseddine, Connes, Marcolli, "Gravity and the standard model
with neutrino mixing", arXiv:hep-th/0610241 (2006/2007) — the CCM paper this
project's informal "KO-dim 6" label is already attributed to

Same fetch method (215014 raw chars, HTML endpoint; searched via local script,
not memory). Two directly relevant, verbatim passages:

**(1) Definition 2.7** (general axiom, restates Connes' table in identical
notation and identical variable ordering):

> "Definition 2.7. A real structure of KO-dimension n in Z/8 on a spectral
> triple (A, H, D) is an antilinear isometry J : H -> H, with the property
> that (2.8) J^2 = epsilon, JD = epsilon' D J, and J gamma = epsilon''
> gamma J (even case). The numbers epsilon, epsilon', epsilon'' in {-1,1}
> are a function of n mod 8 given by
>
> n          0    1    2    3    4    5    6    7
> epsilon    1    1   -1   -1   -1   -1    1    1
> epsilon'   1   -1    1    1    1   -1    1    1
> epsilon''  1   -1    1   -1  [same 4-entry cutoff as Route A — same source
>                                table, same HTML-rendering artifact]"

This independently reproduces Route A's table (same values for the two complete
rows, `epsilon` and `epsilon'`), confirming the extraction is faithful for those
rows and that the cutoff in the third row is a rendering artifact common to both
fetches of the same underlying table, not a one-off download error.

**(2) Section 2.4, "The subalgebra and the order one condition", equations
(2.17)-(2.19)** — this is the direct, concrete instantiation for CCM's own
finite geometry `H_F` (their `N=3`-generation object, the literal ancestor this
project's `H_F` is modeled on):

> "We let H_F be the sum of N=3 copies of the A_LR-bimodule M_F of
> Proposition 2.4 ... We define the Z/2-grading gamma_F by (2.18)
> gamma_F = c - J_F c J_F, c=(0,1,-1,0) in A_LR. One then checks that
> (2.19) J_F^2 = 1, J_F gamma_F = - gamma_F J_F. The relation (2.19),
> together with the commutation of J_F with the Dirac operators, is
> characteristic of KO-dimension equal to 6 modulo 8 (cf. Definition 2.7)."

This is not a table lookup at all — it is CCM stating, in prose, for their own
`(A_F, H_F, D_F, J_F, gamma_F)`, the exact three facts:
- `J_F^2 = +1`
- `J_F` commutes with the Dirac operator (i.e. `J_F D_F J_F^-1 = +D_F`)
- `J_F gamma_F = - gamma_F J_F` (i.e. `J_F gamma_F J_F^-1 = -gamma_F`)

— and then explicitly names this exact combination "characteristic of
KO-dimension equal to 6 modulo 8." This is stronger evidence than the table
alone: it is CCM doing the convention-matching work themselves, for the literal
object this project's Entry 1 is an analogue of, removing any need for this
round to infer/extrapolate the table's damaged third row.

**Cross-check against Route A's table (sanity, not required for the verdict):**
at `n=6`, Route A's table gives `epsilon=1`, `epsilon'=1` — consistent with (2.19)'s
`J_F^2=1` and "commutes with D". The table's incomplete `epsilon''` row cannot be
checked at n=6 directly (only n=0..3 are legible) — which is exactly why this
round relies on the explicit (2.19) prose statement for the third sign, not on
extrapolating the truncated row. (A naive period-2 extrapolation of `1,-1,1,-1`
would give `epsilon''(n=6)=+1`, which would be WRONG — CCM's own text says `-1`
at n=6. This mismatch is recorded here precisely so nobody is tempted to
"complete the pattern" from the damaged table later.)

---

## Convention-matching against this project's own computed tuple

This project's Entry 1 (`docs/ko_dimension_registry.md`), `[VERIFIED-sympy, C36]`
/ `[VERIFIED, G18 T6/T7]`:

| slot | this project's value | CCM's (2.19) value for their `H_F` | match? |
|---|---|---|---|
| `J^2` | `+1` | `J_F^2 = +1` | yes |
| `J D J^-1` vs `D` | `+1` (commute) | "commutation of `J_F` with the Dirac operators" (commute) | yes |
| `J gamma J^-1` vs `gamma` | `-1` (anticommute) | `J_F gamma_F = - gamma_F J_F` (anticommute) | yes |

All three slots match exactly, in the same order, using CCM's own stated
convention for their own analogous object. No reordering or convention
translation was needed — CCM's `(epsilon, epsilon', epsilon'')` ordering is
identical to this project's `(J^2, JDJ^-1/D, JgJ^-1/g)` ordering.

CCM's own conclusion for this exact tuple: **"characteristic of KO-dimension
equal to 6 modulo 8."**

---

## Verdict

**RESOLVED.**

- A real, fetched (not recalled) primary source — in fact two, Connes'
  axiom paper (hep-th/9603053, Definition/table) and CCM itself
  (hep-th/0610241, Definition 2.7 + the direct (2.19) instantiation for their
  own `H_F`) — states the sign-triple, in the same variable order this
  project already uses, and CCM explicitly identifies `(+1, +1, -1)` (their own
  computed values for their own `H_F`, matching this project's independently
  computed tuple exactly) with KO-dimension 6 mod 8.
- The convention was checked, not assumed: CCM's `epsilon = J^2`,
  `epsilon'` <-> `J D J^-1` vs `D`, `epsilon''` <-> `J gamma J^-1` vs `gamma`
  is identical in ordering to this project's own docstring ordering — the
  ordering-mismatch risk OB12's text specifically flagged did not materialize.
- The only genuine defect found (the `epsilon''` table row rendering
  incomplete past n=3 in both fetches) was not papered over: it is recorded
  above, was not extrapolated, and was resolved instead by a second,
  independent, more specific quote (CCM's own (2.19) applied to their `H_F`)
  that does not depend on the damaged row at all.

## Registry update

`docs/ko_dimension_registry.md` Entry 1 updated: `mapping_status` from
`BLOCKED_BY_EXTERNAL_INPUT` to `RESOLVED`, with:
- **KO number:** 6 (mod 8)
- **Primary source:** A. Chamseddine, A. Connes, M. Marcolli, "Gravity and the
  standard model with neutrino mixing," arXiv:hep-th/0610241, Section 2.4,
  eq. (2.19) (instantiating the general axiom of A. Connes, "Gravity coupled
  with matter and the foundation of non-commutative geometry,"
  arXiv:hep-th/9603053, Definition/table for axiom 7, "Reality" — same table
  restated as CCM's own Definition 2.7)
- **Convention:** `epsilon=J^2`, `epsilon'` <-> `JDJ^-1` vs `D`, `epsilon''`
  <-> `JgammaJ^-1` vs `gamma` — identical ordering to this project's own tuple,
  no translation needed.

## What this does NOT mean (carried over from claim.md, restated as executed)

- Does not touch the geometric-side reality types (C32/C33) or their
  combination with this finite KO-number — untouched, per the registry's own
  scope note.
- Does not change OB2's status.
- Does not constitute or require the internal n-mod-8 derivation route (OB12's
  other, harder closure option) — this round closed OB12 via the cheap
  citation route only, as scoped.

## Files touched this round

- `experiments/20260905-c160-ob12-ko-dimension-table-citation/decision.md` (this file, new)
- `docs/ko_dimension_registry.md` (Entry 1 `mapping_status` row updated — see diff)

Not touched (per brief): `preprint.tex`, `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`, git.
