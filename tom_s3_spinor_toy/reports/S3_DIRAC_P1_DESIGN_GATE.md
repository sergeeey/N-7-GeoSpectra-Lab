# S3 Dirac P1 Design Gate

Date: 2026-06-07

## Decision

[INFERRED] P1 should start with a `Spectral/Wigner-D` design path, not a point-cloud `kNN` graph Dirac operator and not a Hopf finite-difference grid.

Current status:

```text
P1 status = DESIGN_ONLY
selected path = spectral_wigner_basis
implementation status = not started
```

This decision does not start `SU(2)` instanton, index, chirality, spectral-flow, eta-invariant, or zero-mode work.

## Basis For The Decision

[CODE] The project already has:

- `ben_achour_scalar_modes.py` for the displayed Ben Achour scalar phase convention;
- `wigner_d_micro_audit.py` for the Wigner-D convention bridge;
- `s3_dirac_exact_baseline.py` for the exact clean Dirac spectrum baseline;
- `reports/S3_DIRAC_EXACT_BASELINE_P0_AUDIT.md` for P0 scope and caveats.

[VERIFIED-SYNTHETIC] The exact P0 baseline verifies the clean round `S3` spectrum:

```text
lambda_{k,+/-} = +/- (k + 3/2) / R
degeneracy per sign = (k + 1)(k + 2)
```

[INFERRED] A spectral/Wigner-D route keeps the next layer closest to the representation theory already audited, and avoids introducing graph discretization artifacts before the spinor conventions are stable.

## Options Compared

| Option | Status | Main Advantage | Main Risk | P1 Verdict |
|---|---|---|---|---|
| Spectral/Wigner-D basis | Preferred | Best convention control; aligns with current Ben Achour/Wigner-D work | Requires explicit spinor-harmonic convention and matrix-element formulas | `GO_DESIGN` |
| Point-cloud kNN graph Dirac | Backlog | Could later test point-cloud numerics | Requires frames, spin connection, parallel transport, Hermiticity, and convergence checks | `NO_GO_NOW` |
| Hopf finite difference grid | Backlog | Direct coordinate operator possible | Coordinate singularities and boundary handling near Hopf poles | `NO_GO_NOW` |
| Existing discrete Dirac library/method | Research backlog | May reuse known discretization theory | Needs literature/tool verification before adoption | `RESEARCH_ONLY` |

## Spectral/Wigner-D P1 Scope

[INFERRED] The safe P1 implementation target is:

```text
P1a: representation-level spectral Dirac scaffold
```

Allowed:

- define spinor-harmonic label conventions;
- map labels to the P0 exact eigenvalue formula;
- compare generated spectral labels against `s3_dirac_exact_baseline.py`;
- keep the `ben_achour_displayed_phase` convention explicit;
- parameterise the alternative `xi'` convention without using it silently.

Not allowed in P1a:

- point-cloud kNN graph Dirac;
- graph spin connection;
- finite-difference Hopf Dirac;
- `SU(2)` instanton;
- index theorem claims;
- chirality claims on odd-dimensional `S3`;
- zero-mode claims;
- heavy diagonalisation.

## Required P1a Acceptance Checks

[INFERRED] Before P1a can be called complete, it needs tests for:

- label generation through a small cutoff;
- eigenvalue agreement with `analytic_dirac_spectrum_s3`;
- degeneracy agreement per sign;
- no zero modes for the clean round `S3` case;
- explicit convention metadata in the returned records;
- no use of `branch` as `chirality`.

## kNN Graph Dirac Blocker

[INFERRED] A kNN Dirac operator is blocked until a separate design proves how it handles:

- local tangent frames at each point;
- spin structure;
- spin connection;
- parallel transport between neighboring points;
- gamma/Pauli matrices across local frames;
- measure/weighting;
- Hermiticity or self-adjointness;
- convergence to the exact clean `S3` spectrum.

[HYPOTHESIS] Without these structures, false low modes are likely.

## Claim Discipline

[CODE] P1 must keep these claims separate:

```text
analytic exact spectrum = verified by P0 unit tests
spectral label scaffold = future P1a code, not yet implemented
numerical Dirac convergence = NEEDS-REAL-DATA
instanton/index/zero-mode result = backlog, no claim
```

## Next Step

[INFERRED] The next safe coding task is not a full Dirac operator. It is:

```text
P1a_SPECTRAL_LABEL_SCAFFOLD
```

Minimum deliverable:

- module that emits spectral spinor-branch records under explicit convention metadata;
- tests comparing those records to the P0 exact analytic baseline;
- no gauge fields and no numerical discretization.
