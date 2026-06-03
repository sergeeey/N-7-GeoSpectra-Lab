# GeoSpectra Lab — Project Sketch

> One page. Read this first. Then decide whether to dive into the README, the reports, or just leave.

## 1. What this is

GeoSpectra Lab is a **falsification-first numerical harness** for testing spectral signals on finite-lattice compact product toy geometries.

It is **not** a physics proof.

## 2. Core question

> Can a spectral signal survive strong falsification controls well enough to justify a geometry-specific interpretation?

## 3. Current answer

**No.**

The current result supports:

```
DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC
```

## 4. What survived

The true-IPR contrast **survived** the corrected S³ Dirac operator rerun:

| Stage | Aggregate IPR contrast (W=20 vs W=0) |
|---|---:|
| Before S³ Dirac fix (v0.1.21) | ~7.15× |
| After S³ Dirac fix (v0.1.24)  | ~7.07× |
| **Change** | **<1.1%** |

The operator bug was real, but **not** load-bearing for the signal.

## 5. What failed

The signal is **not specific enough** to support an S³×S¹ physical claim.

The harness distinguishes lattice product structure from random/scrambled baselines, but does **not** distinguish Wilson-term internal details.

## 6. Evidence ladder

| Level | Test | Result | Meaning |
|---|---|---|---|
| **L1** | Random Hermitian | ✅ rejected | Not pure noise |
| **L2** | Scrambled geometry | ✅ rejected | Topology matters |
| **L3** | FFT vs lattice | ✅ distinguished | Discretization matters |
| **L4** | Ring / Wilson ring | ✅ accepted | Lattice family stable |
| **L5** | Scrambled Wilson | ❌ not distinguished | Operator details not specific |

**Sensitivity ceiling: L3.** Anything finer than discretization method is invisible to the current harness.

## 7. Safe claim

GeoSpectra is currently a **methodology and falsification platform** for finite-lattice spectral experiments, **not** evidence for physical S³×S¹ compactification.

## 8. Next scientific move

Build an **Artifact Zoo** and **Control Zoo**:

- spectral clones (multiple discretizations of the same geometry)
- fake geometries (parameter-matched but structurally wrong)
- parameter-matched nulls
- alternative discretizations
- S³×S² port (per Tom Lawrence redirect, CAMP 2026-05-26 — minimum 2 extra dimensions for covariant compactification framework)
- per-family divergence audit (ring stable vs spectral_circle weakening)

## 9. Why it matters

The value of the project is **not** that it proved the original hypothesis.

The value is that it **detected where the original interpretation fails** — and did so transparently, with an audit trail, before any external claim was published.

---

## Where to go next

| If you want... | Read |
|---|---|
| Full project description with citations | [`../README.md`](../README.md) |
| What can/cannot be said externally | [`CLAIMS_AND_CAVEATS.md`](CLAIMS_AND_CAVEATS.md) |
| Research motivation + framing | [`RESEARCH_CONTEXT.md`](RESEARCH_CONTEXT.md) |
| 15 main artefacts as outcome cards | [`OUTCOMES.md`](OUTCOMES.md) |
| Repository hygiene audit | [`GITHUB_SHOWCASE_AUDIT.md`](GITHUB_SHOWCASE_AUDIT.md) |
| The current FINAL verdict reasoning | [`../reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md`](../reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md) |
| Cross-script reproduction audit | [`../reports/UNIFIED_RESULT_RECONCILIATION_AUDIT_v0.1.24.md`](../reports/UNIFIED_RESULT_RECONCILIATION_AUDIT_v0.1.24.md) |

---

**Last updated:** 2026-06-03 (post v0.1.24 release)
**Author:** Sergey Boyko — Ronin Institute for Independent Scholarship 2.0 (Research Scholar)
**ORCID:** [0009-0009-2178-5701](https://orcid.org/0009-0009-2178-5701)
