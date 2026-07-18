# Round104 (A2) — Decision

**Date:** 2026-07-17
**Verdict:** `NOT_APPLICABLE__CODIMENSION_MISMATCH`
**Go/no-go:** the standard Callan-Harvey anomaly-inflow mechanism does
not apply to `ι`'s fixed-point locus as envisioned by A2 — a cheap,
dimensional/structural check settles this without needing the full
inflow computation.

## Reasoning

Callan-Harvey-type anomaly inflow requires a **codimension-1** interface
(a domain wall) separating two bulk phases/regions, across which an
anomalous current flows — this is the structural content of the
descent-equation argument underlying the mechanism (the bulk
Chern-Simons-type term's variation under a gauge transformation is
exactly canceled by an anomalous current localized ON the codimension-1
wall). Round80 (E14, Section A, reused unchanged) established `ι`'s
fixed-point set on `S³` is **`{g=+1, g=-1}`, two ISOLATED POINTS** — a
**codimension-3** locus in the 3-dimensional `S³` (0-dimensional points
in a 3-manifold), not a codimension-1 wall. This is a structural mismatch
with the standard inflow mechanism's own applicability requirement, not
merely a computational obstacle.

**What WOULD be the natural framework for isolated fixed points of an
involution**, instead of Callan-Harvey inflow: equivariant/orbifold index
theory (Atiyah-Bott-Segal fixed-point formula), where curvature "shows up"
concentrated AT isolated fixed points as a correction to a naive index
count — this is exactly round101's (A6) own framework, already attempted
and found `BLOCKED` (naive spin-connection pullback is `x`-dependent,
needs the inhomogeneous term). A2 and A6, on inspection, are the SAME
underlying mathematical question approached from two different physics
vocabularies ("anomaly inflow" vs. "equivariant index defect") — not two
independent candidates.

## Applying the pre-registered criteria (claim.md Section 2)

**NOT APPLICABLE, structural mismatch** — codimension-1 required,
codimension-3 found.

## Kill Analysis

- **What this kills:** A2 as an INDEPENDENT candidate from A6 — it is not
  a genuinely different mechanism, it is the same equivariant-index
  question in different language, already attempted (round101, BLOCKED).
- **What this does NOT kill:** the equivariant-index-defect framing
  itself, which remains open exactly as round101 left it (needs the
  inhomogeneous/Maurer-Cartan term for a full spin-level treatment).
- **Net effect:** narrows the goal-expansion-100 candidate list by one —
  A2 does not need separate future pursuit; any future work on this
  angle should be filed under A6's own Relaxation Map, not as a fresh
  direction.

## What this does NOT mean

Does not affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`. No file outside this new folder was touched.
