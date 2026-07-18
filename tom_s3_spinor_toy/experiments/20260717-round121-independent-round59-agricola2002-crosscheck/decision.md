# Round121 — Decision

**Date:** 2026-07-17
**Verdict:** `NULL — CANDIDATE ROUTE DISQUALIFIED, TWO PRECISE REASONS
IDENTIFIED, NOT ONE VAGUE ONE` (a near-miss caught before being written up
as a false positive, not a physics finding)

**Go/no-go:** the Agricola 2002 PDF cannot serve as round59's own named
"different primary source" independent-verification rung. This is a
genuine, scoped, honest NULL for the verification-route question — it does
not touch round59's own claim or status.

## What was checked, and what was found

**Step 1 — read the PDF in full.** `Agricola_2002_Dirac_naturally_reductive.pdf`
is Ilka Agricola's 2002 paper (arXiv:math/0202094), "Connections on
naturally reductive spaces, their Dirac operator and homogeneous models in
string theory" — a general theory paper establishing the one-parameter
connection family `∇^t` (t=0 canonical, t=1/2 Levi-Civita, t=1 "anticanonical",
t=1/3 Kostant's cubic Dirac operator) and a Kostant-Parthasarathy-type
formula for `(D^t)²` on ANY naturally reductive homogeneous space, worked
out in detail on a specific example (the 5-dimensional Stiefel manifold
`V_{4,2}`) — not on `S⁶=G₂/SU(3)` specifically.

**Step 2 — checked whether this source is already used in this project.**
`grep -n "Agricola" preprint.tex` returns line 1720-1725 (bibliography
entry, confirming this is the exact same paper, arXiv:math/0202094) and
multiple body citations (lines 697, 721, 737, 750-751, 1302, 1353, 1475).
**This source is NOT independent — it is already `preprint.tex`'s own
primary citation** for the Kostant-Parthasarathy formula used throughout
§sec:schur (L4B). Treating it as an independent check of round59's claim
would have been a genuine evidence-laundering error (this project's own
Perelman-audit anti-pattern list names this explicitly: "same source
confirms multiple independent claims").

**Step 3 — read exactly what it is used for, since disqualification-by-
citation alone would be an incomplete answer.** `preprint.tex:719-745`
(§sec:schur) uses Agricola2002's formula, `λ²(ρ,σ) = C₂(G₂;ρ) - C₂(SU(3);σ)`,
applied with `C₂(G₂;(1,0))=4` (minimum non-trivial `G₂` Casimir) and
`C₂(SU(3);(1,1))=3` (maximum non-trivial `SU(3)` Casimir in the relevant
fibre), giving the gap `λ²≥4-3=1>0` **for every non-trivial `G₂`-isotypic
component** — this is Rounds 52-56's already-certified result (the
non-trivial-sector positivity, cited in `L3B_SPIN8_INTERFACE_SPEC.md`'s own
status table). **Round59's own claim is about the TRIVIAL `G₂`-isotypic
sector specifically** (`rank(D⁺|₁)=1`, where `ρ=1` the trivial
representation) — and on that sector, `C₂(G₂;1)=0` by definition, so the
formula gives `λ²(1,σ) = -C₂(SU(3);σ) ≤ 0`, a **structurally uninformative,
non-positive bound** that cannot distinguish rank 0 from rank 1. This is
precisely why round59 needed a dedicated, separate computation in the
first place — the general Casimir-gap formula is vacuous exactly on the
sector round59's claim lives on.

**Consequence, corrected [skeptic correction]:** first draft framed this as
"TWO separable reasons" for disqualification, implying each independently
sufficient. Skeptic found this overstates (b)'s scope: reason (a) alone
(already cited in `preprint.tex`) is sufficient by itself to disqualify
Agricola2002 as an "independent" source under round59's own criterion —
this is the primary, safe finding. Reason (b) is a narrower, additional
observation about specifically the ONE simplified Casimir-difference
formula (`λ²(ρ,σ)=C₂(G₂;ρ)-C₂(SU(3);σ)`, `preprint.tex:724`) that
`preprint.tex` reuses — it does NOT constitute a full audit of every
mechanism in Agricola2002's general theory, and should not be read as
closing the door on the whole paper. **In particular, this round did NOT
check** whether Agricola2002's separate Theorem 4.2 (constant spinors
satisfy `H·ψ≠0`, i.e. the torsion-cubic term never annihilates a
`G`-invariant/constant spinor) bears on round59's trivial-sector question —
the "trivial `G₂`-isotypic sector" (`ρ=1` in the Peter-Weyl decomposition)
plausibly corresponds to Agricola's "constant spinor" case, and whether her
Theorem 3.3's exact formula for that case (`Ω_g=0`, giving
`(D^{1/3})²ψ=[Q(ρ_g,ρ_g)-Q(ρ_h,ρ_h)]ψ`, a fixed positive-definite constant,
NOT the naive Casimir-difference shorthand) could give a genuine,
independently-derivable bound is a real, open question this round leaves
unresolved rather than closed — checking it would require careful
root-system computation for `(g₂,su(3))` that risks a fresh derivation
error if rushed, and is deliberately not attempted here. This is flagged as
a concrete, scoped next step, not folded into this round's "vacuous"
conclusion, which is now understood to rest on reason (a) primarily.

**Step 4 — alternative CAS availability, checked directly [corrected —
first-draft check was inconclusive, re-ran cleanly]:**
```
which sage maple math Mathematica wolframscript  → none found
which python && python --version → Python 3.13.5 (the incumbent, same as round59's own routes)
```
No alternative CAS (Sage, Maple, Mathematica) is available in this
environment — only Python/sympy, the same interpreter round59's own three
routes already used. This rung is closed by environment constraint, not
by choice; it does not, by itself, add anything beyond round59's own
already-documented "single-CAS" residual leg.

## Kill Analysis

- **What this kills:** the specific candidate this round tested (Agricola
  2002 as an independent verification source for round59) — for two
  precise, separable reasons (already-cited; structurally vacuous on the
  relevant sector).
- **What this does NOT kill:** round59's own `rank(D⁺|₁)=1` finding, its
  `[VERIFIED-INDEPENDENT-INTERNAL]` status, or any downstream conclusion
  (Exact-kernel corollary, Lemma L5, Yukawa-degeneracy theorem hypothesis)
  — all untouched.
- **What survives as a scoped, honest statement of the actual remaining
  gap:** none of round59's own three named rungs (different CAS, different
  primary source, external human review) is currently available or
  applicable within this session. The gap to full external certification
  is not closable from inside this project right now — this is the honest
  conclusion, not a discouraging one to hide.

## Relaxation Map

| Option | What it would require |
|---|---|
| Check whether Agricola2002's OWN Theorem 4.2 (constant-spinor non-vanishing, `H·ψ≠0`) applies to round59's trivial-sector claim via the exact `Ω_g=0` specialization of Theorem 3.3 — NOT the naive Casimir-difference shortcut `preprint.tex` already reuses | Careful root-system computation of `Q(ρ_g₂,ρ_g₂)-Q(ρ_su(3),ρ_su(3))` for `(g₂,su(3))` specifically — deliberately not attempted this round to avoid a rushed Lie-theory derivation error; a genuinely open, scoped next step, distinct from "find a different paper" |
| A genuinely different primary source for the S⁶ Killing-spinor eigenvalue specifically (not the general Kostant-Parthasarathy machinery, which is already shared) | A paper computing the round-S⁶/G₂-nearly-Kähler Killing eigenvalue independently of both AHL2023 and Agricola2002 — e.g. Grunewald's original 1990 nearly-Kähler classification paper, or Bär's 1993 Killing spinor classification — not checked this round, a concrete next candidate |
| A different CAS | Requires Sage/Mathematica/Maple installed in this environment — confirmed absent (`which` checked directly), an infrastructure question outside this round's scope |
| External human review | Requires an actual outside referee (journal review, or Tom Lawrence's own input per the standing collaboration) — cannot be supplied by this session |

## What this does NOT mean

1. Does NOT change round59's own status or verdict.
2. Does NOT claim the trivial-sector rank result is in any doubt — the
   doubt is only about which VERIFICATION ROUTES are available, not about
   the result itself.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Does NOT modify `CLAIM_LEDGER.yaml`'s `C2_ROUND59_KERNEL_DIM1` entry —
   its `evidence_status: INTERNALLY_CERTIFIED` is unchanged, since nothing
   here strengthens or weakens it either way.

## Standing lesson (this round specifically)

**A candidate "independent" source must be checked against the project's
own citation trail BEFORE being used, not after a plausible-sounding
write-up is drafted.** This round caught the disqualifying fact (already
cited in `preprint.tex`) at the investigation stage, before drafting any
claim of independent confirmation — avoiding a near-miss version of the
"evidence laundering" anti-pattern this project's own `perelman-audit.md`
names explicitly.

**Second, separate lesson, from the mandatory skeptic pass on this round
itself:** the first draft of this decision presented reasons (a) and (b)
as "two separable reasons," each independently sufficient — skeptic found
this overstated (b)'s scope (it disqualifies only the one formula
`preprint.tex` reuses, not the whole source) and surfaced a genuinely
unexamined avenue (Theorem 4.2) this round's "vacuous" framing had
implicitly foreclosed without checking. Fourth consecutive round (118,
119, 120, 121) where a first-draft consolidation/investigation claim
needed a skeptic-caught correction — the pattern holds even for negative/
cautionary findings, not just positive ones.

## Check (reproduces the citation-trail verification)

```
grep -n "Agricola" preprint.tex | grep -v "AgrHofLawn"
```
Expect: bibliography entry (line ~1720-1725, arXiv:math/0202094) plus
multiple body citations (lines 697, 721, 737, 750-751, 1302, 1353, 1475),
confirming this source is already part of this project's own derivation,
not independent of it.
