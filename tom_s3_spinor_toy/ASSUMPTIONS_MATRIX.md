# Assumptions Matrix — what `N_gen=3` actually rests on

**Purpose:** one place that lists every load-bearing assumption behind the
`N_gen=3` CONDITIONAL headline, what it depends on, and what breaks if it
changes. Built 2026-09-06 in response to an external review that asked for
exactly this ("составить единую таблицу предпосылок... для каждого пункта
указать, какие другие пункты он меняет") — see
`correspondence`-style audit note in this session's own memory. Companion to
`OPEN_BLOCKERS.md` (per-item deep detail) and `PARENT_ACTION_GATE.md`
(what a valid OB1 fix must satisfy) — this file does not replace either,
it cross-references them.

**Read this before proposing a new construction that touches more than one
row.** The review's own central worry was exactly this: individually-true
results being silently assembled into a claim none of them actually license.

---

## The five load-bearing pieces

| # | Assumption / choice | Currently | Depends on | Breaks if changed |
|---|---|---|---|---|
| A | **Which connection on S³** (torsion parameter `t`) | No selection principle known. Untwisted Levi-Civita (`t=1/2`) gives **zero** zero-modes on the full operator (OB1, PARKED). `t=0,1` are mathematically available but not gauge-equivalent to each other or to `t=1/2` (C125, proven) — a genuine physical choice, not a labeling artifact | Nothing internal picks `t` — every internally-generated candidate mechanism (curvature, Yang-Mills, Chern-Simons, bordism/anomaly, Pin-structure, fermion condensate [C137, REJECT — no dynamically-derived condensate available], borrowed-4D and exact-n=3-spectrum spectral action [C176/C177, both `[VERIFIED-tool]`, both skeptic-confirmed `CONFIRMED-REAL`, both even in `(t-1/2)` per OB13's registry and both landing on the single-well `t=1/2` case, not even the weaker `{0,1}`-as-a-set outcome round99's own even toy achieved]) has been tried and found either structurally blind or requiring the still-missing round95 S⁶↔S³ link | Whichever `t` is eventually justified must ALSO satisfy row B below at that same `t` — a selection principle that fixes `t` but breaks the kernel multiplicity is not a fix |
| B | **Kernel multiplicity stays 1, not 2, at whichever `t` is selected** | At `t=0` or `t=1`, `dim ker(D_{S³})=2` (an SU(2) doublet), not 1 — verified two ways. This DOUBLES the naive generation count unless something projects it back down | Row A (only matters once a `t≠1/2` is actually adopted) | If OB1 is ever "solved" by picking `t=0` or `t=1` without also solving this, the fix produces 6 generations, not 3, not a smaller problem |
| C | **Which twist bundle** (`Sigma` vs `m`, `m⊕2·1`, `T1`-style self-twist) | `Sigma` gives kernel=1 (round59); `m` gives kernel=0 (C139); `m⊕2·1` gives kernel=0 (C141). C141's own finding: **all four constructions ever tried match a "graded branching floor" computable from pure `su(3)` representation theory alone** — the kernel differences carry no independent dynamical information, they are arithmetic consequences of which bundle was picked | Nothing internal selects `Sigma` specifically — this is OB14, still open | If a future physical argument selects a DIFFERENT bundle than `Sigma`, the graded-floor formula (not a new computation) already predicts what kernel it will give — check the floor before building anything |
| D | **Full G₂ symmetry, needed for the kernel-uniqueness proof (Lemma B / G74A)** | `dim ker ≤ 1` is proven ONLY under the full `G₂` isotropy action | Directly in tension with row E | Any mechanism that breaks `G₂` (needed for row E) must be re-checked against Lemma B — it is not automatically safe |
| E | **Something must break `G₂` to distinguish the 3 triality channels** (`8_v,8_s,8_c` need to be physically inequivalent, not just abstractly isomorphic) | 2 of 3 channels distinguished (L≠R via pseudoscalar, G68). The 3rd (vector, `8_v`) is a **model postulate**, not derived (OB4) | Breaking `G₂` enough to realize this (row E) COSTS row D's uniqueness guarantee: under one tested reduction, `G₂`-singlet count 1→2, which turns `dim ker≤1` into `dim ker≤2` (quantified, C40) | This is the sharpest, most concrete open tension in the whole headline result — rows D and E cannot both be satisfied for free, and no mechanism tried so far threads this needle |

---

## The two-object type question (C133→C136→C161, external review's own priority #1)

**RESOLVED 2026-09-06: TYPE-MISMATCH, confirmed.** C133's `lambda_0/lambda_1`
(`decision.md:586,604`: coordinates on an abstract 2-dim Hom-space, "a
dimension, not a finite set" — nothing acts on it, nothing computes it) and
C136's `alpha` (`c136_joint_killing_spinor_check.py:618-637`,
`alpha_from_residual`: an actual least-squares SOLVE for a torsion-endomorphism
coefficient, a deterministic function of `(t,frame,chi4,chi6)`) are different
mathematical objects. Cross-vocabulary grep between the two experiments'
decision.md files: zero hits either direction (C133 never mentions Killing
spinors/torsion/`nabla`; C136 never mentions Hom-space/Schur/Spin(8)/triality
beyond the bare word "channel"). The only shared structure is that both use
a two-valued "t-sector" label — C133's is a discrete bookkeeping choice of
which support pattern is switched on; C136's is the literal affine torsion
parameter `t` of Agricola's connection family, evaluated at its two
parallel-spinor endpoints. Same name, unrelated referents — do not spawn a
future round looking for a "missing selection rule" between these two
specific objects; that was never the right question. See
`experiments/20260905-c161-all-to-both-construction-scoping/decision.md` §9
for where this was first flagged, and the 2026-09-06 audit note in this
project's own session memory for the full verification (both key citations
independently re-checked, not just read off the audit's own report).

---

## How to use this file

Before proposing any new mechanism aimed at OB1 or OB4: check which row(s)
it touches. A construction that fixes row A without checking row B is not a
fix. A construction that fixes row E without re-checking row D is not
finished until that re-check is done (per `PARENT_ACTION_GATE.md`'s own
checklist, which this table summarizes but does not replace).

**What this table is NOT:** a claim that `N_gen=3` is wrong, or a new
result. Every row above cites an already-existing, already-registered
project finding (`OPEN_BLOCKERS.md` OB1/OB4/OB11/OB14, `CLAIM_LEDGER.yaml`
C40/C125/C139/C141/C161). This file's only contribution is laying five
separately-true, separately-registered findings next to each other so the
interaction between them is visible without re-reading 2000+ lines of
`OPEN_BLOCKERS.md`.

**Created:** 2026-09-06. **Not yet cross-linked from `OPEN_BLOCKERS.md` or
`PARENT_ACTION_GATE.md`** — do that next if this file proves useful; not
done here to avoid touching either file while it appears to be under
concurrent edit (line-count shifted mid-session, 2026-09-06).
