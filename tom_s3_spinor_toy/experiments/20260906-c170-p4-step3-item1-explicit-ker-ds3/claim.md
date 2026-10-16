# C170 — Claim

**Experiment ID:** `20260906-c170-p4-step3-item1-explicit-ker-ds3`
**Parent:** `experiments/20260906-c169-p4-step3-kernel-eigenvalue-scoping/decision.md`
§5 item 1 ("`ker(D_S3(t))` built as an explicit vector, not merely 'an
eigenvalue of 0 exists'"), attempted in isolation per C169's own Relaxation
Map (§6) and an independent skeptic's lead (C169 §10a item 1) that this
specific item may be cheaper than escalation items 2/3.

## Step -5: Zero-Signal Gate

- **Entity:** `D_S3(t)`, the torsion-deformed Dirac operator on `S³=SU(2)`
  alone, built in `experiments/20260717-round67-e2-s3-torsion-deformation/`
  (E2) and `experiments/20260717-round72-e7-t-selection-principle/` (E7/H1b).
- **Falsifiable predicate:** an explicit vector `psi` in the same 2-dim
  complex spinor space C167/C168's `H_t` acts on (Pauli-basis `SU(2)`
  spinor rep), satisfying `D_S3(t)*psi = 0` at `t=0` and/or `t=1`, can be
  written down and verified — as opposed to only "an eigenvalue of `D_S3(t)`
  crosses zero at `t=0,1`" (E2) or "a parallel spinor exists by an abstract
  holonomy argument" (E7/H1b), neither of which exhibits `psi`.
- **Measurable outcome:** a symbolic (sympy) computation either produces
  `psi` and verifies `D_S3(t)*psi=0` (or the equivalent `Nabla^t`-parallel
  condition) exactly, or fails to, at each of `t=0`, `t=1`, independently.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive** (does this specific algebraic object exist
and what is it — not a causal or predictive claim; no population/estimand
canvas beyond the falsifiable predicate above is needed for a symbolic
existence/construction check, consistent with how E2/E7/C167/C168 were all
scoped as Micro/Standard-tier symbolic checks in this project's convention).

## Kill-criterion table (frozen before running `c170_explicit_ker_ds3.py`
— NOTE: exploratory hand-derivation to determine feasibility, per this
project's own established scoping-round practice — see e.g. C169 itself —
preceded freezing this table; the table below reflects the actual test run,
and `decision.md` states plainly which parts of the derivation were done
before vs. after this file was written)

| Verdict | Condition |
|---|---|
| `EXPLICIT-VECTOR-EXTRACTED-AND-EIGENVALUE-COMPUTED` | Both `t=0` and `t=1` yield certified explicit kernel vectors, AND applying `H_t` (C167/C168, reused via import) to them and checking eigenvalue-1 survival succeeds at both points without caveat |
| `BLOCKED-BASIS-MISMATCH` | Vector(s) extracted but do not live in / cannot be checked against `H_t`'s representation space without an unresolved convention bridge |
| `BLOCKED-NO-EXISTENCE-PROOF-FOUND` | round72/E7 or round67/E2 do not actually establish what C169 claimed (existence at `t=0,1`) |
| `CHEAPER-THAN-EXPECTED` / `NOT-CHEAPER-THAN-EXPECTED` | Honest report against C169 §10a's skeptic lead |
| Co-firing allowed | Multiple verdicts may fire together if the true result is a mixed one (e.g. `t=0` cheap, `t=1` not) — this project's convention (C169 itself co-fired two verdicts) |

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** all facts used (Agricola arXiv:math/0202094 eq.5/Thm 4.2,
  E2/E7's own already-committed results, C167/C168's own already-committed
  code) are either already `[VERIFIED-external-source]`/`[VERIFIED-tool]` in
  this project's own prior rounds (re-cited, not re-verified against the PDF
  again this round) or freshly `[VERIFIED-tool]` this round via sympy.
- **Novelty Check:** `grep`-checked (this session) that no prior round in
  this project ever built the spin-connection matrices `M_i(t)` explicitly
  or an explicit parallel-spinor vector for `D_S3(t)` — confirmed absent
  (E2/E7 only ever used eigenvalue-level formulas). This is new construction
  within this project, not a restatement of an existing result.

## What this does NOT mean (pre-registered)

1. Does NOT complete C169's full escalation (§5 items 2 and 3 — the twisted
   `Cl(9)` `D_S6` reassembly and the `SU(3)`-to-triality basis bridge — remain
   entirely untouched and `BLOCKED-NEEDS-NEW-MACHINERY` regardless of this
   round's outcome).
2. Does NOT, even if fully successful, license combining the resulting
   `S³`-side vector with round59's actual kernel vector into a genuine
   `ker(D_full)` on `S³×S⁶` — that composition is exactly what items 2/3
   are needed for (C169 §5), and is out of scope here.
3. Does NOT re-litigate C168's own T5-T8 results (the `H_t⊗tau` classification
   is forced by tau alone, per C168's own generality check) — if this round's
   vector construction changes anything, it can only be about the S³-side
   input to that tensor product, not about whether the classification itself
   is forced.
