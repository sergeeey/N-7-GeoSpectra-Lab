# E1–E6 Verification Round (2026-07-17)

Five experiments, run sequentially per the 100-directions-brainstorm critique
(`reports/100_DIRECTIONS_BRAINSTORM_2026-07-17.md`). Each is a real
`experiments/20260717-roundNN-.../` folder with `claim.md` + `decision.md`
following this project's own convention. Summary below; full derivations are
in each folder.

**Status calibration correction (2026-07-17, same day, accepted):** two of
the five verdicts below were mislabeled in the first write-up of this round
and have been corrected, both in the individual `decision.md` files and in
this summary:
- **E4** was labeled "NULL / honest inconclusive." Corrected to
  `BLOCKED_BASELINE_CALIBRATION_FAILED` per this project's own Verification
  Substrate Gate concept (`falsification-ladder.md` Step 2a): the target
  claim was never actually tested (the pipeline failed at baseline
  calibration, before reaching the twisted operator) — "test could not run"
  must not be recorded as a NULL result about the target claim.
- **E5 (CP³)** was labeled a bare "PASS." Corrected to `ROUTE_C_PASS` — Route
  C is a necessary-condition/isotropy-Schur-bound check (`dim ker ≤ 1`), not
  equivalent to establishing the exact kernel `(dim ker D⁺, dim ker D⁻)=(1,0)`
  for the physically-relevant operator, which remains a separate, unclosed
  L4A/L4B-style calculation for CP³.

## Canonical statuses

| ID | Canonical status | What is actually established |
|---|---|---|
| E1 | `VERIFIED_TEXTUAL_INTERPRETATION / DIMENSIONAL_INCONSISTENCY_CONFIRMED` | In the current construction, S³ is used as a genuine physical KK factor; the literal dimension is 4+3+6=13 |
| E2 | `SUPPORTED_CANDIDATE_MECHANISM` | In the frozen convention, the family `D_S3(t)` has computable zero-crossings. No physical principle for selecting `t` exists |
| E3 | `PROVED_AT_PRODUCT-ALGEBRA_LEVEL / GLOBAL_SCOPE_CAVEAT` | For the standard graded product construction, the operator's square decouples into a sum of squares, independent of the specific connection on S³ — but only within the frozen product ansatz (no mixed/parent-interaction terms) |
| E4 | `BLOCKED_BASELINE_CALIBRATION_FAILED` | The independent method failed its own untwisted baseline; the twisted claim was never tested |
| E5A (CP³) | `ROUTE_C_PASS` | The same cheap Route-C criterion (already used for S⁶/SU(3)-T²) passes on CP³ — a necessary-condition check, not an exact-kernel claim |
| E5B (S³×S³) | `OPEN_STRUCTURALLY_DISTINCT` | The needed cheap argument does not apply, because an isotropy-trivial slot is present (unlike the other three spaces) — requires a separate calculation |
| E6 | `ILL-POSED` | CH2016's own page-18 basis data for S³×S³ is not internally Hermitian-consistent (B(X,X)=5/3≠B(Y,Y)=2, hand-verified); the Levi-Civita Nomizu map needed to compute `Term2` could not be built without a non-forced choice. `Term2` remains fully open (not zero, not nonzero — untested) |
| Universality (overall) | `SUPPORTED_ON_ROUTE_C: 3/4` | Not yet a theorem about exact kernels on all four homogeneous NK6 manifolds |

## One-line results (original framing, kept for narrative continuity)

| ID | Folder | One-line result |
|---|---|---|
| E1 | `round66-e1-dimension-role-decision` | S³ is a genuine physical KK factor (confirmed via Freund-Rubin flux + Lawrence mechanism + KT-8, all three require it); total spacetime dimension is **13, not 10** — the "10D" language throughout `preprint.tex` is a mislabeling (representation-dimension/spacetime-dimension conflation), not evidence of an alternative reading. **Established: the written ansatz is 13D. NOT established: a consistent 13D parent theory exists.** |
| E2 | `round67-e2-s3-torsion-deformation` | Torsion-deforming S³'s connection (Agricola's naturally-reductive family) gives an exact, closed-form family `D_S3(t)` with genuine zero modes at computable t (e.g. t=0, t=1 for n=0) — independently spot-verified this session (ω=I exactly, crossings match). Does **not** close KT-8: no physical reason given for picking any specific t over Levi-Civita. Crossing values are convention-dependent (torsion normalization, orientation, Levi-Civita reference point) and must be reported together with the full frozen convention, not as bare numbers |
| E3 | `round68-e3-full-operator-torsion-deformed` | The product-decoupling identity `D_full² = D_S3(t)²⊗1 + 1⊗D_S6²` holds to machine precision for the torsion-deformed S³ factor too — independently re-verified this session for an **arbitrary** D_S3 (not just the torsion family), confirming the decoupling never depended on S³'s connection at all. At E2's t=0 crossing, the S³ floor is genuinely removed. Still does **not** close KT-8 (same physical-motivation gap as E2). Scope: proved for the frozen product Dirac ansatz (no mixed connection/flux terms coupling the two factors) — not proved for every possible modified full operator a future parent action might introduce |
| E4 | `round69-e4-representation-free-kernel-check` | Attempted a representation-theory-free direct diagonalization of the twisted S⁶ operator to independently re-verify dim ker=1 without reusing G73/G74A's shared representation-theoretic method. Could not calibrate even the known untwisted baseline spectrum (clean algebraic relation found, but no natural constant reproduces the target eigenvalue) — correctly stopped rather than extend unvalidated machinery. Headline claim status is **unchanged, untested by this method** (not "NULL result against it") |
| E5 | `round70-e5-universality-cp3-s3xs3` | CP³'s prior "ill-posed" verdict (Round 64) is narrowed: that specific mechanism (Charbonneau-Harland instanton deformation) is confirmed unusable for a *second*, independent reason (operator-type mismatch, not just representation-type) — but a different mechanism (Route C, already used for S⁶/SU(3)-T²) DOES pass on CP³ using only already-published data (**Route-C pass, not exact-kernel establishment**). S³×S³ genuinely differs structurally: the isotropy-trivial slot Route C needs to be *absent* is present there, so the cheap argument doesn't decide it (not a NULL, not a PASS — structurally open) |

## What actually changed vs. before this round

- **New, higher-priority open item:** the dimension mislabeling (E1) is now
  confirmed with a firmer basis (Freund-Rubin consistency check) than the
  earlier external-review KT-1 finding, which was acknowledged but never
  acted on. This should be corrected in `preprint.tex` alongside/adjacent to
  KT-1's own already-added open-problems item.
- **KT-8 still stands, but a candidate (unproven) escape route now exists**
  (E2+E3 combined): torsion-deforming S³ mathematically removes the obstruction,
  but with zero physical motivation for the specific deformation — this is
  the same FITTED-vs-DERIVED trap this project's own methodology already
  flags (G56/λ lesson). Not promotable to the preprint as a resolution.
- **Universality programme gains one space (CP³), loses clean closure on
  another (S³×S³ now explicitly open, not silently assumed):** 3 of 4
  homogeneous nearly-Kähler 6-manifolds now pass the same frozen Route-C
  check (S⁶, SU(3)/T², CP³); S³×S³ is a genuine, structurally-distinct open
  question, not a gap in effort.
- **One process finding (E4):** this project's exact-kernel result for S⁶
  currently has no representation-theory-independent verification — all
  existing "independent" passes share the same underlying branching-rule
  machinery. This is a real, currently-unclosed methodological gap, not
  a defect in the result itself.

## Verification notes (this session, not just the delegated agents)

Per this project's own audit-verification-gate ("agent's VERIFIED = my
INFERRED until I re-check"), the following were independently spot-checked
directly (not just accepted from agent reports):
- E2: Clifford relations for Cl(3), ω=Z1Z2Z3=I exactly, and the n=0 zero
  crossings at t=0,1 — reproduced via direct sympy computation, matched
  exactly.
- E3: the decoupling identity `D_full²=D_S3²⊗1+1⊗D_S6²` — reproduced for an
  arbitrary (non-torsion-family) Hermitian D_S3, residual 8.9e-16, confirming
  the result is more general than even E3 itself tested (true for any D_S3,
  not just the torsion family).
- E1, E4, E5: not independently re-derived (E1 is a documentation/consistency
  check with direct file citations, easy to verify by inspection; E4 is a
  BLOCKED/substrate-gate result, lower stakes for overclaiming since it
  makes no positive claim; E5's core claims are standard Clebsch-Gordan/
  Casimir facts, cross-checked by the agent itself against the cited primary
  source's own stated values).

## Kill-table entries (canonical, machine-readable form)

```text
E1_DIMENSION:
  CLAIM: literal current ansatz is 10D
  STATUS: REFUTED
  CORRECTED CLAIM: literal product ansatz is 13D
  PARENT 13D THEORY: OPEN

E2_S3_TORSION:
  ZERO-CROSSINGS: VERIFIED IN FROZEN CONVENTION
  PHYSICAL_SELECTION_OF_t: OPEN
  KT8_RESOLVED: NO

E3_PRODUCT_DECOUPLING:
  ALGEBRAIC_IDENTITY: PROVED FOR FROZEN PRODUCT ANSATZ
  MIXED_PARENT-INTERACTION ROBUSTNESS: OPEN

E4_KERNEL_INDEPENDENCE:
  NEW METHOD CALIBRATION: FAILED
  TARGET KERNEL CLAIM: UNTESTED
  INDEPENDENT VERIFICATION: OPEN

E5_NK6_ROUTE_C:
  S6: PASS
  SU3/T2: PASS
  CP3: PASS
  S3xS3: OPEN
  FULL UNIVERSALITY (exact kernel, all 4): OPEN

E6_S3XS3_NOMIZU_TERM2:
  LEVI_CIVITA_NOMIZU_MAP_FROM_CH2016_P18: ILL-POSED (source data not Hermitian-consistent)
  TERM2_COEFFICIENT: UNTESTED
  NEXT_STEP: check CH2016 pp.7-12 for cyclic/Z3-eigenspace construction
```

## Safe preprint wording for E1 (proposed, not yet applied)

If/when E1's dimension correction is integrated into `preprint.tex`, the
precise scope must be preserved — established only that the *written
geometric ansatz* is 13-dimensional, not that a consistent 13D parent theory
exists:

> The construction uses a four-dimensional external spacetime together with
> the compact factors S³×S⁶, and therefore corresponds, under a literal
> Kaluza–Klein interpretation, to a thirteen-dimensional product ansatz.
> Earlier references to a ten-dimensional spacetime conflated
> representation-theoretic and spacetime dimensions. No complete
> thirteen-dimensional parent theory is claimed.

Every occurrence of "10D"/"ten-dimensional"/"9D"/"nine-dimensional" needs to
be checked across `preprint.tex` (abstract, introduction, captions,
conclusions), `README.md`, and other `reports/` files before this is applied
— not just the three load-bearing usages E1 itself checked.

## E6 — explicit S³×S³ Nomizu/torsion operator audit (completed)

`experiments/20260717-round71-e6-s3xs3-nomizu-torsion-audit/`

**Verdict: `ILL-POSED`** (one of the four pre-registered kill criteria,
triggered honestly — not a PASS, FAIL, or BLOCKED). Building the explicit
Levi-Civita Nomizu-map connection for S³×S³ from Charbonneau-Harland 2016's
own stated page-18 data (`X_i,Y_i` basis + Killing-form `B` + literal
almost-complex-structure action `J(X_i)=Y_i`) requires an extra, non-forced
convention choice with no canonical resolution in the primary-source pages
consulted.

**Core finding, independently spot-checked in this session:**
`B(X₁,X₁)=5/3` but `B(Y₁,Y₁)=2` under CH2016's own literally-stated basis
and metric normalization — these must be equal for `(B,J)` to form a
genuine Hermitian pair, so CH2016's own page-18 data is not
self-consistent as literally transcribed. Verified by hand:
`B(X₁,X₁)=(1/6)[(1+√2)²+(1−√2)²+4]=(1/6)(10)=5/3`;
`B(Y₁,Y₁)=6·[(1/6)+(1/6)]=2`. Confirmed.

Two independent, structurally different repairs were attempted (Hermitize
the metric to fit the stated `J`; or keep the metric and solve for the
metric-compatible `J_B` instead) — they disagree with each other, and a
built-in control check confirmed the natural-reductivity checker code
itself is correct (raw, unmodified `B` passes the control by a fully
general theorem, unrelated to S³×S³). The finding was then independently
reproduced within the same session via a *different* basis (CH2016's
Appendix C, `K_i,L_i`) and a *different* method (general 3-parameter
metric sweep) — same numbers, same conclusion.

**What survives:** E5's isotropy-Schur bound (`dim ker≤1`) and the Route-C
crux finding (isotropy-trivial slot present, unlike the other 3 spaces) —
neither depends on the Nomizu-map construction that hit the obstruction.
**What remains open:** `Term2`'s actual coefficient on that slot — the
substrate needed to compute it was never certified trustworthy, so no
claim (zero, nonzero, or otherwise) is made about it.

**Concrete next step (Relaxation Map, not attempted):** CH2016 pages 7–12
(not consulted this round) may contain a direct cyclic/ℤ₃-eigenspace
construction of S³×S³'s complex structure that sidesteps this specific
basis ambiguity by construction, rather than requiring a choice between
two ad hoc repairs.

## Not yet done

- None of E1-E5's findings have been written into `preprint.tex` or
  `reports/PROJECT_360_ROUND3_SYNTHESIS.md`'s main kill-table — this file is
  a standalone summary. Integration is a separate decision (particularly E1's
  dimension correction, which is the highest-priority candidate for that).
- Nothing in this round has been committed to git.
- E2/E3's candidate KT-8 escape route needs a physical selection principle
  before it could be considered for promotion — not attempted here.
- E5's S³×S³ open question needs the explicit torsion/Nomizu-connection
  computation (scoped in E5's own decision.md as comparable in cost to the
  original L4A/L4B derivation) — not attempted here.
