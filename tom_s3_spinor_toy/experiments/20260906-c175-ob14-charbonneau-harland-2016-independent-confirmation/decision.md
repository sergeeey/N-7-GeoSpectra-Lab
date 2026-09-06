# C175 — Decision

**Date:** 2026-09-06
**Verdict:** `INDEPENDENT-CONFIRMATION-OF-RIGIDITY`. `[VERIFIED-tool]`
(primary source read directly, exact theorem/table cited, not a summary).

---

## 0. Summary

Read Charbonneau & Harland 2016 (already in the repo, previously used
only for the Universality open problem, never cross-checked against
OB14) directly, pages 1-4 and 14-20. Their Theorem 3 gives the exact
deformation-space dimension of the canonical connection on each of the
four homogeneous nearly-Kähler 6-manifolds, computed via a METHOD THIS
PROJECT HAS NEVER USED (elliptic deformation theory / Dirac-operator
kernel of instanton perturbations, not this project's own twisted-Dirac-
on-invariants construction), under TWO different structure groups: the
space's own natural isotropy group `H`, and the broader `SU(3)` structure
group coming from the nearly-Kähler `SU(3)`-structure common to all four.

**Theorem 3's own tables (page 17), verbatim structure:**

| Deformations within `H`-bundle | `G₂/SU(3)` | `SU(2)³/SU(2)` | `Sp(2)/Sp(1)×U(1)` | `SU(3)/U(1)²` |
|---|---|---|---|---|
| | `0` | `0` | `W^R_{(1,0)}` | `0` |

| Deformations within `SU(3)`-bundle | `G₂/SU(3)` | `SU(2)³/SU(2)` | `Sp(2)/Sp(1)×U(1)` | `SU(3)/U(1)²` |
|---|---|---|---|---|
| | `0` | `g` (adjoint) | `W^R_{(1,0)} ⊕ 2g` | `6g` |

**The load-bearing fact for OB14: `G₂/SU(3)`'s own column reads `0, 0` —
ZERO deformations, in BOTH the natural-isotropy framing AND the broader
`SU(3)`-structure-group framing.** The paper's own text states the
mechanism directly (p.17): "Case: `G₂/SU(3)` with structure group SU(3).
**This case is identical to the case of structure group `H`, since
`H=SU(3)`**." `G₂/SU(3)` is the ONE space among the four whose isotropy
`H` already equals the full `SU(3)` — so there is no "broader frame" to
gain deformation freedom from. The other three spaces (`H` a proper
subgroup of `SU(3)`) all gain nonzero deformation freedom precisely
because there IS room between their smaller `H` and the full `SU(3)`.

---

## 1. Connection to OB14

OB14's own search (C134, C139-C166) asks, in different language: is there
ANY real (non-decoupled), independently-motivated geometric coupling data
available on `S⁶=G₂/SU(3)` beyond what its own irreducible isotropy
representation `m` already supplies? Every internal construction tried
(C70/C71 intertwiners, G102, C134's ECSK torsion, the shape operator,
`R^c`) and the one relevant external source found so far (AHL2023) all
answered NO. **This paper answers the SAME underlying question a fourth,
structurally independent way — not by checking a specific candidate
coupling term, but by computing the FULL deformation space of the
canonical connection under the widest structure group available (`SU(3)`,
already the biggest group compatible with the nearly-Kähler structure) —
and gets zero.** Since the deformation space is, by construction, the
space of ALL infinitesimal perturbations compatible with the instanton
equation under that structure group, a zero deformation space under the
BROADEST available structure group is a strictly stronger statement than
"this one candidate coupling vanishes" — it says no coupling of ANY kind,
built from data compatible with the `SU(3)`-structure, can perturb this
connection at all.

**This is not a new escape route (contrary to the hypothesis that
motivated reading the paper) — it is the strongest confirmation yet found
of OB14's own existing negative result, via a method with no shared
machinery with any of this project's own prior attempts.**

---

## 2. Kill Analysis

**What this round kills:** the specific hope (stated honestly in claim.md
before reading pages 14-20) that the paper's "large deformation spaces...
regarded as instantons on the tangent bundle with structure group SU(3)"
result would apply to `G₂/SU(3)` and supply new coupling data. It does
not — `G₂/SU(3)` is explicitly the one space of the four where this
enlargement is vacuous, because its own `H` already exhausts `SU(3)`.

**What this round does NOT kill:** OB14's own status (`BLOCKED-INTERNAL`,
no internally-buildable test remains) — unchanged, now with one
additional, independent confirmation rather than a new option.
`C142`/`C164`'s own two remaining theoretical escapes ((i') a `W_cand`
avoiding `m` entirely, (ii') external input from Tom) — untouched,
neither strengthened nor weakened by this round, since this paper's
result concerns deformations of `m` itself, not alternative twist bundles
disjoint from `m`.

**Relaxation Map:** none opened — this was a confirmatory literature
check, not a new construction attempt.

---

## 3. Side finding (Pearl Gate) — relevant to a DIFFERENT open problem,
   not OB14

The asymmetry Theorem 3 exposes — `G₂/SU(3)` uniquely has `H=SU(3)`
among the four homogeneous nearly-Kähler 6-manifolds, while the other
three have `H` a PROPER subgroup of `SU(3)` and correspondingly gain real
deformation freedom under the broader frame — is directly relevant to
this project's separate, still-open **Universality** question (does the
round59-type mechanism generalize to `CP³`, `SU(3)/T²`, `S³×S³`?). Any
future Universality argument that treats the four spaces as
interchangeable instances of "a nearly-Kähler coset with Killing spinors"
should account for this real structural difference (rigidity is not
uniform across the four spaces even at the level of the canonical
connection's own deformation theory) — flagging for `pearl_registry/
INDEX.md`, not resolved here, out of this round's own scope (OB14 only).

---

## 4. What this does NOT mean

1. Does NOT prove no construction anywhere could supply `W_cand`'s
   missing data — only that this specific, now-checked method does not,
   for `G₂/SU(3)`.
2. Does NOT change `N_gen=3`'s CONDITIONAL status.
3. Does NOT resolve the Universality open problem — the side finding in
   §3 is named, not investigated.
4. Does NOT contradict this paper's own use elsewhere in the project
   (C140/C151/round65/70/71's Weitzenböck-formula/Killing-spinor
   machinery) — a different part of the same paper, unaffected.

---

## 5. Verification substrate (FL Step 2a, abbreviated)

Primary source read directly from the PDF already committed in the repo
root (`Charbonneau_Harland_2016_NK_instantons.pdf`); DOI and arXiv ID
cross-checked on the paper's own first page. No computation performed —
this round transcribes and interprets an already-published, peer-reviewed
theorem (Comm. Math. Phys. 2016), not a fresh derivation. READY, no
blocked-infrastructure issue.

---

## 6. Recommendation on independent skeptic pass

**Not run, judged unnecessary**: this round transcribes an explicit,
already-peer-reviewed theorem's own stated table, directly relevant to a
question the paper's own authors did not have in mind (OB14) but whose
connection is a straightforward reading, not a novel derivation with
overclaim risk. Low stakes for a skeptic pass, matching this project's
own precedent for pure literature-verification rounds (C166 also skipped
one). If a future round tries to BUILD on this connection (e.g. arguing
it settles the Universality question), that round should get one.

---

## 7. Status

`experiments/20260906-c175-ob14-charbonneau-harland-2016-independent-confirmation/`
— DONE. OB14 remains `BLOCKED-INTERNAL`, now independently reconfirmed by
a fourth, structurally distinct method. No new escape route found; the
extended literature search asked for (this session's own plan) has been
attempted and, for THIS specific paper, returned confirmation rather than
a new option. Registry (`OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`)
not yet updated — pending user confirmation of scope. No git operations
run.
