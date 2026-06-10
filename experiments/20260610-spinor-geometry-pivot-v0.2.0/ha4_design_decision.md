# HA-4 Design Decision — S^d Discrimination and S³×S¹ Bridge

**Date:** 2026-06-10  
**Gate:** E6 / HA-4 (from decision_record_v0.2.0.md, experiment order)  
**Inputs:** E0 PASS + KT-3 PASS + decision_record_v0.2.0.md contradictions table  
**Status:** research_only — no physical promotion

---

## Decision

```
HA-4_VERDICT:  ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE

S^d spectral fingerprint results justify continuing toward an S³×S¹ Dirac
harness, but they do not by themselves resolve the original GEOMETRY_AGNOSTIC
verdict.  A separate S¹/Wilson coupling bridge gate is required before any
Phase 3 paper claim about S³×S¹.
```

---

## Options Evaluated

| Option | Label | Verdict |
|---|---|---|
| A | ONE_TRACK: S^d as justified stepping stone to S³×S¹ | **CHOSEN** (with bridge gate) |
| B | TWO_TRACKS: clean S^d spectroscopy is independent from S³×S¹ | REJECTED (premature) |
| C | PIVOT: S³×S¹ requires a fundamentally different Dirac harness | DEFERRED (not enough evidence either way) |

---

## Evidence Evaluated

### For Option A (stepping stone)

**E0 [VERIFIED-tool 2026-06-10]:**
The discrete Dirac² operator on Hopf α-grid recovers λ_n = n + d/2 with error
7e-7. This establishes that a discrete Dirac operator CAN be built for S³ and
can discriminate d=3 from d=6 via |λ_min| = d/2 — at the radial-proxy level.

**KT-3 [VERIFIED-tool 2026-06-10]:**
Diagonal disorder W·diag(ξ) up to W=0.5 shifts |λ_min| by at most 3.7e-3.
Safety margin at W=0.1 is 335×. Shift scales as W/√N (extended-state averaging).
This means the S³ contribution to the eigenvalue is *structurally stable* under
the kind of disorder present in the original S³×S¹ harness.

**Product structure (analytic argument, [INFERRED]):**
For the Dirac operator on S³×S¹, the eigenvalues satisfy:
```
λ²(S³×S¹) = λ²(S³) + (m/R_S1)²      m ∈ ℤ  (periodic BC)
                                        m ∈ ℤ + 1/2  (antiperiodic BC)
```
This means:
1. The S³ radial contribution λ_n(S³) = n + 3/2 appears additively in λ².
2. The KT-3-verified robustness of λ_min(S³) = 3/2 carries over: the S³
   contribution to λ²(S³×S¹) is robust to diagonal S³-sector disorder.
3. Dirac on S³×S¹ has ADDITIONAL discriminating power via the KK tower
   (m/R_S1)² that has no analog in the scalar Laplacian harness.

These three facts together make the S³ spectral fingerprint a structural
building block of the S³×S¹ Dirac fingerprint — not a coincidental similarity.

### Against premature Option B (two tracks)

If we declared the S^d result a separate, independent project:
- We would lose the physical connection between the clean radial result
  and the original disorder problem.
- The KK tower structure of Dirac on S³×S¹ directly inherits the S³ piece.
- There is no physical reason to believe the S^d result is irrelevant to
  S³×S¹ — the connection is analytic (product formula above).

Option B is the conservative path but is **premature closure**: we cannot
rule out the bridge without attempting it.

### Against Option C (fundamental pivot)

There is no verified evidence that S³×S¹ requires a different Dirac design.
The existing operator structure (Hopf coordinates + chirality blocks) extends
naturally to the product geometry. Option C should be revisited only if the
bridge gate fails.

---

## Why ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE and Not Plain ONE_TRACK

Plain ONE_TRACK would imply the bridge is already established.
It is not. Three unresolved gaps remain:

| Gap | Description | Required to close |
|---|---|---|
| BG-1 | S¹ coupling: no Dirac operator on S¹ direction built yet | Build S³×S¹ Dirac lattice |
| BG-2 | Wilson term / boundary conditions on S¹ | Decide periodic vs antiperiodic BC, verify KK gap |
| BG-3 | Off-diagonal disorder (hopping disorder on S¹) untested | Extend disorder sweep to S¹ hopping sector |

Until BG-1 is closed, the connection is an analytic argument, not a demonstrated result.

---

## Bridge Gate Definition

```
BG-GATE (required before Phase 3 S³×S¹ claims):

Demonstrate that the full S³×S¹ Dirac spectrum discriminates at least one
pair of geometries that were indistinguishable to the v0.1.22 scalar harness,
under the same disorder regime used in that harness.

Minimum required:
  1. Implement discrete S³×S¹ Dirac operator (product lattice: Hopf × circle)
  2. Verify KK tower structure: |λ_min| includes (m/R_S1)² contribution
  3. Run disorder test on S¹ sector at W comparable to v0.1.22 disorder level
  4. Show at least ONE geometry pair that Dirac discriminates but scalar cannot

Kill condition:
  If (4) fails after genuine attempt → HA-4 = Option B or C; record in null_results/

This is Phase 3. Current work (v0.2.0) is the radial-proxy justification phase.
```

---

## Scope Limitations — What This Decision Does NOT Claim

1. **BG-GATE is NOT trivially solvable.** Implementing the S³×S¹ Dirac
   lattice is a non-trivial engineering task (2D operator, spin connection
   on product manifold, Wilson term for doublers).

2. **KT-3 tests diagonal S³-sector disorder only.** S¹-hopping disorder
   (off-diagonal, representing varying circle radius) is untested and may
   behave differently.

3. **"GEOMETRY_AGNOSTIC for scalar" ≠ "GEOMETRY_SENSITIVE for Dirac".**
   KT-3 and E0 establish that Dirac CAN discriminate pure spheres. Whether
   it can discriminate the specific configurations that confused v0.1.22 is
   an open question — answered only by BG-GATE execution.

4. **No promotion.** This decision is about research trajectory, not
   physical results. λ = FREE_COUPLING_PARAMETER unchanged.

5. **HA-4 is NOT resolved.** This decision specifies how to resolve it.

---

## NC-2 Dependency

Before building the S³×S¹ harness (Phase 3), the remaining Tier-3 negative
control **NC-2 (permuted grid)** should be closed. NC-2 tests that the
fingerprint depends on geometric grid structure, not a matrix artifact.
If NC-2 fails → the fingerprint is artifactual → BG-GATE attempt would be
premature.

**Recommended order:**
```
NC-2 (permuted grid negative control) → BG-GATE design (Phase 3)
```

---

## Updated HA-4 Status

| Field | Old (pre-decision) | New (post-decision) |
|---|---|---|
| HA-4 status | SCOPE GAP (undesigned) | DECIDED: ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE |
| Next action | undefined | NC-2 → BG-GATE design |
| Phase 3 entry condition | HA-4 unresolved | NC-2 PASS + BG-GATE designed |

---

**Hard constraints compliance:**
- No S³×S¹ claim made: ✓ (bridge gate explicitly not closed)
- No physical promotion: ✓ (research_only throughout)
- IPR not primary endpoint: ✓ (mentioned only in context of localization endpoint note)
- tom_ansatz radial-only: ✓ (finding status unchanged)
