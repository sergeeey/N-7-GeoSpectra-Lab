# E22 (round92) — Claim: Endpoint Anomaly Audit

## 0. Zero-Signal Gate

- **Entity:** the two Cartan-Schouten torsion-connection endpoint zero-mode
  sectors of this project's S³-side torsion-escape-route construction,
  `ker D_{S3,t=0}` and `ker D_{S3,t=1}` (each tensored with the S⁶-side
  twisted-Dirac kernel, per triality channel), as already established by
  E9/E12/E16/E17 (reused, not re-derived here).
- **Falsifiable predicate:** whether the perturbative gauge-anomaly
  coefficients and Witten `SU(2)` global-anomaly parities of each endpoint
  sector, computed under a FROZEN gauge group, are individually nonzero/odd
  but sum to zero/even in the union.
- **Measurable outcome:** an explicit numeric anomaly-coefficient
  computation (script, this folder) for each endpoint alone and for the
  union, classified against three pre-registered, mutually exclusive
  verdict categories (Section 4 below).

All three fields fillable → gate PASSES, proceed.

## 1. L0 — Question classification (EstimandOps)

**Descriptive.** This experiment computes and classifies already-established
representation content and anomaly coefficients of this project's own
zero-mode kernels under a specified gauge group. It does not estimate a
causal effect, does not predict an unobserved future value, and does not
require a DAG or identifiability check. It is a structured
classification/audit exercise, exactly like E16/E17/E21/E21-followup before
it — no causal layer applies.

## 2. FROZEN GAUGE GROUP — stated first, irrevocably, before any computation

$$G_{\mathrm{eff}} = \mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$$

**This is Option (i), not Option (ii) (`SU(4)_{PS}×SU(2)_L×SU(2)_R`), and this
choice is FINAL for this experiment — it will not be switched after seeing
results.**

**Reasoning for this choice, stated before any computation:**

`experiments/20260717-round90-pati-salam-gauge-completeness/decision.md`
(E21) Section 1 tool-verifies, by direct quotation of `preprint.tex` at six
independent locations (`:78-80`, `:187-198`, `:258-279`, `:355-374`,
`:1174`), that this project's own text geometrically realizes exactly
`SU(3)_c×SU(2)_L×SU(2)_R` from the `SO(4)×G_2` isometry of `S³×S⁶` — a real,
computed gauge-kinetic term, not a bookkeeping label. The SAME experiment's
Section 5a, reconfirmed directly this round by reading `preprint.tex:280-285`
and `preprint.tex:420-424` again, states as the paper's own explicit,
repeated admission: "an internal check (gate G97, this work) finds no
`SU(4)` subgroup in `Iso(S³×S⁶)`" — i.e. `SU(4)_{PS}` is **not** geometrically
realized anywhere in this project's own construction. Testing anomaly
cancellation for a gauge group (`SU(4)_{PS}×SU(2)_L×SU(2)_R`) that this
project's own text admits it does not geometrically realize would not be a
meaningful test of THIS project's own physics — it would be testing a
different, larger theory this project does not claim to have built. Per the
task's own explicit instruction, Option (i) is therefore adopted as the
frozen `G_eff`, precisely BECAUSE round90/round91 already established Option
(ii) is unavailable in this project's own geometric construction (gate G97).
**This choice will not be revisited after computing anomaly coefficients,
regardless of outcome.**

## 3. Precise test steps (in order, per endpoint, then for the union)

For each of `t=0`, `t=1`, and the union `t=0 ⊕ t=1`:

1. **Kernel content.** Cite (do not re-derive) E9/E12/E16/E17/G67/G73/G74A's
   already-established `dim ker(D_{S3,t})=2`, `dim ker(D_{S6,twisted})=1` per
   triality channel, ×3 triality channels, and the `(1,2)`/`(2,1)`
   representation assignment under `SU(2)_L×SU(2)_R` (Convention A: `t=0`↔
   `(1,2)`, `t=1`↔`(2,1)`, per `CONVENTION_TABLE.md` row 6, convention-
   independent up to an overall `L`↔`R` relabeling per E17 Section 1).
2. **`G_eff` representation assignment.** Determine, using ONLY this
   project's own already-established facts, the `SU(3)_c` representation of
   the S6-side zero mode per channel, combined with the S3-side
   `SU(2)_L`/`SU(2)_R` doublet assignment from step 1. Explicitly flag which
   parts are DERIVED from established facts versus UNESTABLISHED/imported.
3. **Anomaly coefficients for `G_eff`'s actual generators**: `[SU(3)_c]^3`,
   `[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`, `[grav]^2 U(1)_Y` — reusing
   `preprint.tex`'s own already-existing, already-symbolically-verified
   anomaly computation and hypercharge formula(s) as starting point/cross-
   check where applicable (cited exactly, including any internal
   inconsistency found between the paper's own stated `Y`-formulas — see
   Section 5 of `decision.md`), not re-deriving SM anomaly theory from
   scratch.
4. **Witten `SU(2)` parity** (mod-2 doublet count) for `SU(2)_L` and
   `SU(2)_R` SEPARATELY, for each endpoint alone. Per round90's own
   correction (its decision.md's ⚠️ note), this checks something genuinely
   DIFFERENT from the perturbative anomalies of step 3 — report both,
   without conflating them.
5. Repeat 1-4 for the union `t=0 ⊕ t=1`.

## 4. Pre-registered verdicts (exactly these three, no new categories)

- **PASS:** `anomaly(t=0 alone) ≠ 0`, `anomaly(t=1 alone) ≠ 0`,
  `anomaly(t=0⊕t=1) = 0`, for the ACTUALLY-DERIVED (frozen) `G_eff`, with an
  explicit endpoint-to-sector map, across the anomaly conditions that can be
  computed.
- **BLOCKED:** the endpoint kernels' representations under `G_eff` cannot be
  determined from what this project has already established (e.g. the
  `SU(3)_c` assignment of the S3-side content, or the System-A/System-B
  reconciliation round91 already flagged, is missing), or the relevant gauge
  group itself is not fully established.
- **FAIL:** each endpoint is separately anomaly-free already (no forcing),
  or both endpoints give the identical representation (no genuine two-sector
  structure).

**Pre-registered expectation, stated honestly before computing (per
round91's own finding, reused as a starting hypothesis, not a foregone
conclusion):** round91 Section 1 already establishes, via a direct
group-theory inference (`SU(3) ⊂ G_2`, `S^6=G_2/SU(3)`, applied to the
S6-twisted kernel's `G_2`-singlet character), that System A's per-channel
content carries **no internal color multiplicity** — it is manifestly an
`SU(3)_c` SINGLET. If this holds up on direct re-verification this round
(Section 3.2 below), it is entirely possible — and would be a legitimate,
expected, non-forced outcome — that the `[SU(3)_c]`-dependent anomaly
conditions turn out to be trivially satisfied (already zero) for BOTH
endpoints separately, which would NOT license PASS (no forcing), and that
the `U(1)_Y`-dependent conditions cannot be computed at all because this
project's text has never assigned a numeric `B-L`/hypercharge value to the
twisted S6-kernel specifically (an existing, explicitly-flagged gap, per
`experiments/20260717-round83-joint-representation-decomposition/
decision.md`, "Assumptions carried, unresolved," item 3). **Do not force a
different outcome if this is what the computation shows — BLOCKED, precisely
naming which specific representation assignment is missing, is exactly as
valuable an outcome here as PASS or FAIL.**

## 5. Kill criterion

This experiment is KILLED (verdict = BLOCKED, not silently abandoned) if,
after Section 3 steps 1-2 are attempted honestly, ANY of the `G_eff`-charge
assignments needed for a REQUIRED anomaly condition (steps 3-4) cannot be
derived from this project's own already-established text/experiments without
importing an unverified assumption. This is not a failure of the experiment —
it is the pre-registered, legitimate BLOCKED outcome.

## What this does NOT mean (pre-registered, before results)

1. Does not re-open or re-litigate round90 (E21)'s or round91 (E21-followup)'s
   own verdicts — this experiment reuses their findings by citation only.
2. Does not attempt to test Option (ii) (`SU(4)_{PS}` unification) — that
   option is explicitly and irrevocably excluded from this experiment's scope
   per Section 2.
3. Does not affect this project's `N_gen=3` headline claim (G73/G74A/G74B
   S⁶-only chain) — this experiment concerns only the separate, already-
   non-load-bearing S³-side torsion-escape-route program.
4. A BLOCKED verdict here does not mean the underlying physics question is
   permanently unanswerable — only that this project's CURRENT text does not
   yet supply the specific missing assignment(s) named in the decision.
