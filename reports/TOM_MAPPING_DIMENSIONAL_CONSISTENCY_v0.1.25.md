# Tom Mapping — Dimensional Consistency + Language Bridge — v0.1.25

**Date:** 2026-06-04
**Purpose:** Tool-verify the group↔geometry dimension mapping Tom Lawrence gave,
stitch the languages honestly, and record a deferred geometry roadmap.
**Scientific status:** This is a *dimensional consistency note* and *communication
bridge*, NOT a physics result. Confirms nothing about compactification.

---

## 0. Context

Tom's clarification of the intuition picture ("Geometry hides. Symmetry emerges."):
the naive S¹→U(1), S²→SU(2), S⁶→SU(3) is replaced by a **dimension-counting**
routing through the orthogonal groups:

| Gauge group | Routed via | Acts on | Extra dims | Compact space |
|-------------|-----------|---------|-----------|---------------|
| U(1) | ≅ SO(2) | ℝ² | 2 | S² |
| SU(2) | ~ SO(3) | ℝ³ | 3 | S³ |
| SU(3) | ⊂ SU(4) ~ SO(6) | ℝ⁶ | 6 | S⁶ |

---

## 1. Stitch 1 — Dimension Counting: **CONSISTENT** [VERIFIED-tool]

Computed with `cc_toy_lab/geometry/analytic_spectra.py`:

| Group | S^d | dim(S^d) | λ₁ (Laplacian) | deg(ℓ=1) | scalar curvature |
|-------|-----|----------|----------------|----------|------------------|
| U(1)  | S² | 2 | **2.0** | 3 | 2.0 |
| SU(2) | S³ | 3 | **3.0** | 4 | 6.0 |
| SU(3) | S⁶ | 6 | **6.0** | 7 | 30.0 |

**Key identity (verified):** the first non-zero scalar-Laplacian eigenvalue of S^d
equals its dimension:
> λ₁(S^d) = 1·(1 + d − 1) = **d** = (extra dimensions in Tom's count).

So the dimension language stitches *exactly*: each gauge sector's extra-dimension
count d reappears as a clean spectral invariant λ₁ = d on the matched sphere S^d.
This is a real, checkable correspondence — useful as a shared coordinate with Tom.

---

## 2. Stitch 2 — Isometry Nuance: **MISMATCH FLAGGED** [VERIFIED-tool]

The isometry group of S^d is **SO(d+1)**, one larger than the SO(d) Tom uses to
route the dimension count:

| S^d | Isometry group | Tom's routing group | Same? |
|-----|----------------|---------------------|-------|
| S² | SO(3) (≅ SU(2) locally) | SO(2) for U(1) | ✗ |
| S³ | SO(4) | SO(3) for SU(2) | ✗ |
| S⁶ | SO(7) | SO(6) for SU(3) | ✗ |

**Why this matters (honest caveat):** in a Kaluza–Klein picture, gauge symmetry
emerges from the **isometry** of the internal space. The isometry of S² is SO(3) ≅
SU(2), *not* U(1). So Tom's mapping is a **dimension-counting** correspondence
("n extra dims → S^n"), NOT an isometry-group correspondence. Both readings are
legitimate but they answer different questions:

- *Dimension counting* (Tom's routing): how many extra dims realise the group → S^n.
- *Isometry emergence* (KK-style): what symmetry the sphere's geometry produces → SO(d+1).

This is a precise, constructive point to raise with Tom — it sharpens, not rejects,
his framework.

---

## 3. What GeoSpectra CAN / CANNOT Say Here

| CAN [VERIFIED] | CANNOT |
|----------------|--------|
| λ₁(S^d)=d, deg(ℓ=1)=d+1, curvature=d(d−1) — exact analytic spectra | Derive U(1)/SU(2)/SU(3) from any spectrum |
| Dimension counting is internally consistent | Confirm gauge-group emergence |
| Isometry(S^d)=SO(d+1) ≠ routing SO(d) | Claim the harness *tests* Tom's model |
| Select future geometries motivated by the mapping | Call a localization signal a "symmetry" |

**Hard caveat from our own data:** the v0.1.22 negative-controls verdict is
**GEOMETRY_AGNOSTIC** — the harness does not even distinguish Wilson-term details
within the lattice family. So running it on S²/S³/S⁶ may **not** discriminate them.
The Tom-aligned ladder is a *geometry-selection* roadmap, NOT a discriminator —
until/unless the harness is made geometry-sensitive.

---

## 4. Deferred Geometry Roadmap (Tom-aligned)

Recorded for future direction. **NOT scheduled** — current harness is geometry-agnostic.

```
S³×S¹   — current falsification polygon (DONE: DISCRETIZATION_SENSITIVE)
  │
  ├─ S²  — U(1) sector   (extra dims 2, λ₁=2)   [analytic spectrum exists: exp_01]
  ├─ S³  — SU(2) sector  (extra dims 3, λ₁=3)   [analytic spectrum exists: exp_02]
  ├─ S⁶  — SU(3) sector  (extra dims 6, λ₁=6)   [analytic spectrum exists: exp_03]
  └─ S³×S⁶ — combined toy geometry              [product spectrum exists: exp_04]
```

**Precondition before this ladder is worth running:** demonstrate the harness can
distinguish *geometry* (currently it cannot — Level 5 unresolved). Otherwise the
ladder produces geometry-agnostic outputs and adds no discriminating evidence.

---

## 5. Draft Reply to Tom (refined)

> Tom, thank you — that clarification is very helpful, and I checked it against our
> analytic spectra. The dimension counting stitches cleanly: the first Laplacian
> eigenvalue of Sⁿ is exactly n, so your routing U(1)→2→S², SU(2)→3→S³,
> SU(3)→6→S⁶ lines up with λ₁ = 2, 3, 6 on each sphere.
>
> One nuance I wanted to flag precisely: the *isometry* group of Sⁿ is SO(n+1),
> one larger than the SO(n) in the dimension routing (e.g. S² has isometry SO(3) ≅
> SU(2), not U(1)). So I read your mapping as a dimension-counting correspondence
> rather than a Kaluza–Klein isometry-emergence one — both are valid, they just
> answer different questions. Happy to be corrected if your framework routes it
> differently.
>
> My current work stays narrow: a finite-lattice spectral stress-test harness, not
> a compactification proof — and candidly, our latest negative-controls result is
> "geometry-agnostic", so the harness can't yet discriminate these spheres. But your
> mapping is exactly the principled roadmap I want for future toy geometries: S²,
> S³, S⁶, and products. And yes — "Geometry hides. Symmetry emerges." feels like the
> right guiding phrase.

---

## 6. Verdict

```
DIMENSION_COUNTING: CONSISTENT [VERIFIED-tool]
ISOMETRY_ROUTING:   NUANCE FLAGGED (SO(d+1) vs SO(d))
SCIENTIFIC_CLAIM:   NONE — communication + roadmap only
HARNESS_READINESS:  geometry-agnostic → ladder deferred
```

**Usefulness (per user's own scoring):** Tom communication 9/10, roadmap 8/10,
scientific confirmation 0/10. This note serves the first two, claims nothing on the third.

---

**Status:** FINAL
**Files referenced:** `cc_toy_lab/geometry/analytic_spectra.py`, `experiments/exp_01..04`
**Date:** 2026-06-04
