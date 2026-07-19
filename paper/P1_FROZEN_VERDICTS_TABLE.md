# P1 — Frozen Verdicts Table (triality-distinguishability / physical-realization line)

**Frozen 2026-07-19.** This table is the fixed evidentiary base for the P1
no-go manuscript (`P1_NOGO_MANUSCRIPT_OUTLINE.md`). Every cell below was
re-verified by direct read of the cited `decision.md` during this freeze —
not reconstructed from memory or from a prior summary. **Do not add rows
without re-opening this file explicitly** — this is a frozen snapshot, not
a living document; new results belong in a new round, referenced from a
future manuscript revision, not silently appended here.

**Scope fence (read before anything else):** this table concerns ONLY the
triality-distinguishability / `su(3)+centralizer` physical-realization
line (rounds 102, 119, 124, 127, 128, and the OB1/KT-8 product-Dirac
result). It does **not** concern, strengthen, weaken, or otherwise touch
this project's separate `N_gen=3` headline claim, which is derived
independently via the `S⁶`-only Dirac-index chain (G73/G74A/G74B) and is
verified by an entirely different experiment lineage (see
`ROUND59_EXTERNAL_VERIFICATION_PACKET/` for that lineage's own,
independent external-verification track). Any manuscript drafted from this
table must state this fence explicitly in its first section, not as a
footnote.

| # | Round / source | Theorem or claim | Scope | Key assumptions | Evidence | Escape routes / what would overturn it |
|---|---|---|---|---|---|---|
| 1 | G102 (`20260705-g102-spin8-fiber-obstruction`, 2026-07-05) | No continuous symmetry inside `so(8)` commutes with the geometric `G₂` action on the octonion fiber (`dim c_{so(8)}(g₂)=0`). Triality is an **outer** automorphism; the only inner symmetries present (`su(3)`: `Hom=6`; the 2-dim abelian centralizer) see all three channels as one module. | Intrinsic/geometric symmetries only — induced by the `S³×S⁶` construction itself. Does **not** rule out symmetries external to this geometry. | `S⁶=G₂/SU(3)` coset (G0/G10-B/G11); octonion algebra `𝕆=ℝ⁸`; `Cl(0,8)` chirality-split `v/s/c` triple (reused from G101). | [VERIFIED] 8/8 pre-registered numerical predictions (`P1`-`P8`) exact, plus 1 control (bracket-homomorphism check), 9/9 total tests; residuals at machine epsilon; no borderline singular values. | Postulating an independent fiber `Spin(8)` not induced by the `S⁶` geometry (an external axiom — widens scope, does not refute the theorem); a non-Schur/discrete distinguishing mechanism (none found, not excluded). |
| 2 | Round119 (`20260717-round119-triality-distinguishability-gate`, 2026-07-17) | `SO(4)×SO(4)` (from the octonion `H⊕Hℓ` split) algebraically distinguishes all 3 triality channels — escapes the `SO(7)` rank ceiling that confined every earlier internal candidate. Gate 1 of 7 (per `L3B_SPIN8_INTERFACE_SPEC.md` §7) is done. | External to `g₂` — a candidate structure, not yet shown to act globally on the actual compactification. | The abstract `SO(4)×SO(4)` algebra with the claimed block-chirality property (verified as an algebraic fact). | [VERIFIED] Source's own §7 gate table read directly; corrected via mandatory skeptic review (3 issues fixed, incl. an overclaimed "PARTIAL" label). | Gate 2 (`L3B` §7 — does `K` act globally, not just on the fiber) is named "the blocker, needs Part 5" (Tom Lawrence's unpublished work — not solicited per this project's standing constraint). `G74A` Lemma B's exact-`G₂`-only proof does not survive `G₂`-breaking, which this route requires — no known internal spectral-gap alternative. |
| 3 | Round124 (`20260718-round124-su3-centralizer-triality-candidate`, 2026-07-18) | `su(3)⊕u(1)⊕u(1)` (`su(3)` plus its own 2-dim abelian centralizer in `so(8)`) gives `Hom=0` for all 3 off-diagonal channel pairs (direct Schur non-isomorphism) — a second, structurally distinct route to the same Gate-1 milestone. | Same as row 2 — external to `g₂`, same physical-realization gap. | Reuses `G102`'s own `derivation_basis`/`stabilizer_basis`/`centralizer_dim` machinery unmodified. | [VERIFIED-tool] `Hom` diagonal `4,4,4` / off-diagonal `0,0,0`; independently re-run with 2 basis-rotation checks (not just the skeptic's analytical trace), residuals `~1e-15`. | Same Gate-2 blocker as row 2. Physical identification of the `u(1)×u(1)` charges attempted (round126): `NO_INDEPENDENT_EVIDENCE` — the apparent match was a tautology of the scan's own Frobenius-norm normalization. |
| 4 | Round127→128 (`20260718-round127-...`, `20260718-round128-...`, 2026-07-18/19) | `ℂ⊗8_v` (round124's octonion vector rep) and `Σ` (G14/G15's `S⁶` Dirac spinor) are isomorphic as complex `su(3)`-representations — established abstractly (round127, End-dimension identity) then via an **explicit, machine-precision-verified intertwiner `S`** (round128), exhaustively checked across all 12 members of `Aut(su(3))`. | A pure representation-theory statement about two objects constructed elsewhere in this project. Does **not** by itself say anything about physical realization. | Reuses G10-B/G11/G14/G15/G102's constructions unmodified. | [VERIFIED] `iso_residual~1e-15` across all 12 candidates. Two computational bugs found and fixed en route (a `Minv`/`M` sign inversion, caught by mandatory skeptic review; a Fortran/C-order `vec()` reshape mismatch, self-caught) — both independently re-verified before the result was accepted. | None currently known against round128's own explicit-`S` claim (machine-precision, exhaustive over the full automorphism group). **Provenance note (SR8, `SUPERSEDED_RESULTS.md`, 2026-07-19):** round127 never found or claimed an explicit `S` (`results_round127.json`: `isomorphism_found=false`, `iso_residual=null`) — its `hom_dim=4` naive-pairing result is a pure rank computation and is unaffected by round128's later reshape-order fix. Round127 must therefore never be cited as independent corroboration of round128's explicit intertwiner — round127's sole surviving contribution to this row is the abstract End-dimension argument; the explicit `S` is round128's alone. The separate question of physical identification is row 5. |
| 5 | Round128 (same experiment, B-L comparison, 2026-07-19) | Transporting round124's `su(3)`-centralizer through the verified `S` and comparing to `G15`'s established `BmL` operator gives **no literal match for any of the 12 valid choices of `S`** (relative residuals `0.53`–`1.00`, zero clean matches against a `1e-4` threshold). | The specific physical-identification question first raised in round126 — does THIS ONE algebraic candidate correspond to the known `B-L` charge? Does not address whether any other structure might. | `BmL` as constructed in G15 (`SO(6)⊃SU(3)×U(1)` embedding); round124's specific centralizer construction. | [VERIFIED] all 12 `Aut(su(3))` candidates checked, not just one — closes the `S_NOT_UNIQUE_UP_TO_SCALE` kill criterion definitively. | A genuinely different algebraic candidate (not round124's specific one) might still match `B-L` — not ruled out here. Round61-BL separately showed `B-L` itself is not unique among a `dim≥3` admissible family — an independent caveat on the whole question. |
| 6 | OB1/KT-8 (`OPEN_BLOCKERS.md` OB1, PARKED 2026-07-17) | The untwisted (Levi-Civita) `S³` connection gives the full internal `S³×S⁶` Dirac operator **zero zero-modes**. A torsion-deformed connection (`t≠0`) is mathematically available, but no selection principle is known for which `t` (or whether `t=0` and `t=1` together) is physically required. | The FULL product operator on `S³×S⁶` — not the `S⁶`-only operator used by the separate `N_gen=3`/round59 chain (see scope fence above). | Standard Cartan-Schouten torsion family `D_{S³}(t)`; no external parent-action input. | [VERIFIED] confirmed 3× + cross-checked against literature; rounds 114-117 — 4 independent mechanism-search attempts, all honestly null or falsified. | `PARKED`, not `REJECTED` — per this project's own Substrate Gate, reopens only on: (1) a concrete parent-action candidate from literature or new insight, (2) a directly relevant published mechanism, (3) a new derivation map from other project work, (4) any candidate must pass `PARENT_ACTION_GATE.md`'s checklist first. |

## Composite disposition (as of this freeze)

- **Established, positive:** row 1 (intrinsic obstruction), rows 2+3 (two
  independent external algebraic candidates reach "Gate 1"), row 4
  (explicit isomorphism, exhaustively verified).
- **Established, negative (the no-go core):** row 5 (`B-L` no-literal-match,
  0/12), row 6 (no zero-mode for the untwisted product operator, PARKED).
- **Not established either way, out of scope for P1:** whether `SO(4)×SO(4)`
  or `su(3)+centralizer` act *globally* on the actual compactification
  (Gate 2, "the blocker" — needs Tom Lawrence's Part 5, not solicited).

## Reproduction

Every `[VERIFIED]` cell above traces to a specific `decision.md` cited in
its row's source column. Re-reading each `decision.md` in full is the
correct reproduction step — this table is a compressed index, not a
replacement for the source.
