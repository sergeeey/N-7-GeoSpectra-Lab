# Gauge/Hilbert Frame-to-Gauge Audit (Round120, 2026-07-17)

**Gauge/Hilbert/Triality closure program, item 5** of the user's own 8-step
sequence (after `SPIN13_TO_SPIN4_DECOMPOSITION.md`, the round118
matter-generation factorization test, and `TRIALITY_DISTINGUISHABILITY_
GATE.md`).

**What this file is:** a consolidation + internal-consistency audit, not new
physics. For each gauge factor this project claims, it names the exact
geometric mechanism (full metric isometry, holonomy/structure-group of a
narrower compatible structure, or neither), cites the primary source, and
checks whether the project's own internal registries agree with
`preprint.tex`'s current, more careful text.

## 1. The frame-vs-gauge distinction being audited

Two logically distinct notions get called "gauge structure from geometry"
in Kaluza-Klein constructions, and conflating them is a known failure mode
this project has already self-caught once (round102, §below):

- **Isometry-derived:** the gauge group is (a subgroup of) the full
  isometry group of the compact factor's metric — genuine Killing vectors,
  the standard KK mechanism.
- **Holonomy/structure-group-derived:** the gauge group is the stabilizer of
  some additional compatible structure (an almost-complex structure, a
  spinor, a 3-form) — a subgroup of the isometry group, geometrically real
  but a logically weaker, narrower claim than "this is the full isometry
  group."

## 2. Consolidated table: mechanism per gauge factor

| Gauge factor | Mechanism | Status | Source |
|---|---|---|---|
| `SU(2)_L×SU(2)_R` | **Isometry-derived.** Full isometry group `SO(4)≅SU(2)_L×SU(2)_R` of `S³`'s bi-invariant round metric. | `PROVED`, externally confirmed by Tom Lawrence (2026-06-19, "you're a physicist" — `RESEARCH_STATUS_REPORT.md:306`) | `preprint.tex:193-195,273-275`; `experiments/20260615-g6-s3xs6-spinor-content/decision.md` |
| `SU(3)_c` | **Holonomy-derived.** Stabilizer `G_2⊂SO(7)` of the compatible almost-complex structure `J` on `S⁶`'s round metric (same metric as used for the isometry computation below — see §3) — `G_2/SU(3)` coset structure, not the full `SO(7)` isometry. | `PROVED` (G10, cross-checked independently by G69's CSDR route) | `preprint.tex:275-277`; `experiments/20260617-g10-s6-so6-gauge/decision.md`; `experiments/20260621-g69-csdr-coset/decision.md` |
| `U(1)_{B-L}` | **Neither** — not an isometry generator of `Iso(S³×S⁶)=SO(4)×SO(7)` (gate G97). Identified instead from fermion zero-mode charge content, not from the isometry group directly. | `OPEN`, explicitly flagged in `preprint.tex` itself | `preprint.tex:280-287,425-436` |
| Full Pati-Salam `SU(4)_{PS}` (`SU(3)×SU(2)×SU(2)×U(1)_{B-L}` unified) | **Blocked at the group level** — no `SU(4)` subgroup exists in `Iso(S³×S⁶)`, for same-factor or diagonal embeddings, within the standard product-manifold framework. | `PROVED` (G97, closed 3 independent ways: round102, round108, round109) | `CLAIM_LEDGER.yaml` `C7_GATE_G97_CLOSED` |
| `SO(4)×SO(4)` triality-distinguishing candidate | **Neither** (by construction) — genuinely breaks `G_2`, not derivable from either the `S³` or `S⁶` frame alone without new (Part 5) physical input. | `PARTIAL` per round119's corrected gate application (`GATE 1 OF 7 DONE / GATES 2-6 OPEN`) | `TRIALITY_DISTINGUISHABILITY_GATE.md` |

## 3. Round102's flagged "which metric" subtlety — checked, found already resolved by the project's own text

`experiments/20260717-round102-a1-su4-isometry-precision-check/decision.md`
(its "Assumptions carried, unresolved" section) flags: *"Whether 'Killing
vectors of the round `S⁶` metric' is even the correct notion of 'isometry'
to use given this project's ACTUAL construction uses the nearly-Kähler (not
necessarily round) `G_2`-compatible metric — flagged by the skeptic's point
5 as a further open subtlety, not resolved here."*

**Checked this round:** `preprint.tex:464` states explicitly, "On `S⁶` with
the round metric, the spinor bundle splits..." — confirming the SAME round
metric is used throughout this project, both for the `G97` isometry
computation (`SO(7)`) and for the compatible almost-complex structure `J`
that defines the twisted Dirac operator (`G_2⊂SO(7)`, the stabilizer of
`J`). There is no separate, unaddressed "nearly-Kähler-only metric" —
`S⁶`'s standard nearly-Kähler structure is compatible with its round metric
(a special feature of `S⁶` specifically, not a generic NK6 space), so the
isometry group used for `G97` (`SO(7)`, the full round-metric isometry
group) is a strict superset of `G_2` (the subgroup that also preserves
`J`), not a different or incompatible geometric setup.

**Consequence — narrower than first stated [skeptic correction]:** this
resolves only the *metric-identity* sub-question ("not necessarily round"
→ it is the round metric, confirmed). It does **not** resolve a distinct,
finer question round102's flag can also be read as raising: given the
physics (the twisted Dirac operator) depends on the metric *together with*
`J`, is the physically relevant ambient symmetry group `SO(7)` (bare
metric) or `G_2` (metric+`J`)? Skeptic review found this is a genuine,
separate framing question that `preprint.tex:464` does not settle — it only
confirms which metric, not which ambient group is the "correct" one to
check isometry against. **Consequential impact is low regardless:** `G97`'s
result (no `SU(4)` in `SO(7)`, dim 21) implies, a fortiori by a dimension
count alone (`dim(G_2)=14<21`), no `SU(4)` in the smaller `G_2` either — so
neither reading changes any physics conclusion. What is corrected here is
only the precision of the claim: the metric-identity sub-question is
resolved; the ambient-group framing question is a matter of which group one
chooses to check against, not an open computational gap, and is left as
such rather than marked fully "resolved."

## 4. Registry staleness found: `docs/gates_tracker.md` G10 entry

**Finding:** `docs/gates_tracker.md` (its own header: "Source of truth —
edit here, then run `python scripts/export_results.py` to regenerate
Excel/PDF") carries this row, dated 2026-06-17, unchanged since:

> `G10 | Gauge Structure | S⁶ spin connection → SO(6) gauge field | PASS |
> so(6)≅su(4); 15 generators; cross-spectator effect | 6/6 | 2026-06-17`

Read without cross-referencing `preprint.tex`'s later text, this row could
be misread as claiming a genuine 15-generator `SO(6)`/`SU(4)` gauge sector
exists in this construction. It does not, per `preprint.tex`'s own later,
more careful framing (§2 above) and gate `G97` (dated within this session's
round90-102 work, after G10): only `SU(3)_c×SU(2)_L×SU(2)_R` (a
9-generator, not 15-generator, structure) is actually realized as a gauge
group from the isometry, and `SU(4)`/full `SO(6)` as a gauge symmetry is
explicitly `BLOCKED` (`C7_GATE_G97_CLOSED`). The underlying computation in
G10 (`so(6)≅su(4)`, 15 generators of the spin-connection's structure
algebra) is correct and unchanged — the risk is the row's own PASS label
and unqualified phrasing, read in isolation, not the computation itself.

**Note also, corrected [skeptic correction]:** first draft claimed the
tracker's coverage "stops at the early gates (`G1`-`G30`ish)" — this is
factually wrong and was caught by skeptic review. `docs/gates_tracker.md`
was in fact kept current through `G106` (dated 2026-07-06, header states
"Last updated: 2026-07-07") — it includes `G50`, `G73`, `G74A/B`, `G90`,
`G91`, `G100`, `G102`-`G106`, well past the early gates. The accurate,
narrower finding: `G97` and its round102/108/109 corroborations — all dated
2026-07-17, this session, *after* the tracker's last update — are simply
not yet folded back into the tracker, the same ordinary lag any actively-
developed registry has relative to same-day work, not a stopped-early
tracker.

**Fix applied this round:** added an inline caveat to G10's row (Key
Result cell) in `docs/gates_tracker.md`, cross-referencing `G97` and
`CLAIM_LEDGER.yaml`'s `C7_GATE_G97_CLOSED`. **Not attempted this round:**
regenerating `docs/exports/gates_tracker.xlsx`/`.pdf` (a mechanical script
run, `python scripts/export_results.py --all`) or folding the full
round90-119 work into the tracker's own gate rows — both flagged as
follow-up, not done here, to keep this round scoped to the one concrete
staleness finding.

## 5. What this does NOT mean

1. Does NOT change any physics conclusion — the mechanism table in §2 is a
   restatement of already-established facts (G6, G9, G10, G69, G97,
   round102, round119), not a new derivation.
2. Does NOT claim `preprint.tex` itself is inconsistent — it is not; the
   staleness found is between the older internal tracker and the newer,
   already-correct preprint text.
3. Does NOT affect `N_gen=3`'s conditional status, `lambda=FREE_COUPLING_
   PARAMETER`, or `safe_for_runtime=False`.
4. Does NOT resolve `U(1)_{B-L}`'s open geometric origin, or the
   `SO(4)×SO(4)` candidate's physical-realization gap (round119 OB4) —
   both remain exactly as open as before.

## Sources

- `tom_s3_spinor_toy/preprint.tex` lines 258-298 (gauge structure), 425-436
  (G97 caveat), 464 (round metric confirmation)
- `tom_s3_spinor_toy/docs/gates_tracker.md` (G10, G10b rows and header)
- `tom_s3_spinor_toy/experiments/20260617-g10-s6-so6-gauge/decision.md`
- `tom_s3_spinor_toy/experiments/20260621-g69-csdr-coset/decision.md`
- `tom_s3_spinor_toy/experiments/20260717-round102-a1-su4-isometry-precision-check/decision.md`
- `tom_s3_spinor_toy/CLAIM_LEDGER.yaml` `C7_GATE_G97_CLOSED`
- `tom_s3_spinor_toy/TRIALITY_DISTINGUISHABILITY_GATE.md`
