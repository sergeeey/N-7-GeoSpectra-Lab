# Note for Tom — SENT VERSION (2026-06-07, 23:51)

**Status:** SENT via Discord — 2026-06-07, 23:51  
**Do NOT modify this file — it is the authoritative record of what was transmitted**

---

## Exact text sent

Hi Tom,

I've now gone through the relevant Part 3 slides much more carefully, especially the sections around equations (45)–(72) and (98)–(104): the block-form generators, the SU(2)_R × SU(2)_L action on S³, the angular coordinates, the dragging action, and the Hilbert-space / orthonormality discussion.

This helped me understand that my first GeoSpectra direction was too narrow for what you are doing. My earlier S³ implementation was useful as a simplified numerical proxy and as training infrastructure, but it was not yet a faithful implementation of the full S³ harmonic/spinor structure you are using.

So I have separated the work into two layers:

the existing GeoSpectra toy/spectral validation harness;
a small separate S³ spinor-harmonic sanity layer, just to understand your calculation more carefully.

I am not treating this as a result yet. I am using it only to check conventions and to avoid mixing scalar, vector, and spinor harmonics.

There is one possible angle I may have found, related to your expansion of √g in harmonics and the Hilbert-space inner product over S³.

In your orthonormality condition over S³, is the Riemannian volume measure implicit in the integral? In the angular coordinates from your slides, where r = ρ sinα and r̃ = ρ cosα, this would introduce a Jacobian factor proportional to sinα cosα, equivalently sin(2α).

I ask because in a small sanity check, √sin(2α) behaves like the square root of that volume-density factor. This may be completely consistent with your √g expansion, so I do not want to overstate it. I just want to understand whether the harmonic coefficients are being extracted using the weighted S³ inner product, or an unweighted coordinate measure.

A second related clarification: in your notation, should I understand α as the two-plane / Hopf-type angle from your angular coordinates, or is it related to the geodesic-polar angle used in the Camporesi-Higuchi Dirac eigenspinor construction?

I've also checked the literature more carefully now: Ben Achour et al. is useful for Hopf-coordinate scalar/vector harmonics on S³, while Camporesi-Higuchi is the relevant source for Dirac spinor eigenfunctions. I'm trying not to mix those objects.

If this line of thought is useful, I can send a short, carefully checked note with the toy calculation and the precise caveats.

Best,
Sergey

---

## Two pre-registered questions (what we await answers to)

**Q1 — Inner product / measure:**
Is the Riemannian volume measure implicit in the S³ orthonormality integral?
i.e., is the norm weighted by sinα cosα dα (= sin(2α)/2 dα)?

**Q2 — Coordinate convention:**
Is α the Hopf-type angle (α ∈ [0, π/2]) from the angular coordinates r = ρ sinα, r̃ = ρ cosα,
or the geodesic-polar angle θ (θ ∈ [0, π]) from Camporesi-Higuchi?

## What Tom's answer determines

| Tom answers | Phase 3 action |
|-------------|----------------|
| Q1: weighted measure YES | √sin(2α) = √volume_density interpretation confirmed → write short note with Phase 2 numerics |
| Q1: unweighted / different norm | Sturm-Liouville hypothesis weakened → revise interpretation |
| Q2: Hopf α | Coordinate mapping α_Hopf = θ_geod/2 confirmed → direct comparison valid |
| Q2: geodesic-polar θ | Need coordinate transform before any comparison |
| No response / unclear | Wait, do not speculate |

## Phase status after send

| Phase | Status |
|-------|--------|
| Phase 0 — design spec | ✅ DONE (42ecde4) |
| Phase 1 — PDF verification | ✅ DONE (7139ae1, 3da1477) |
| Phase 2 — numerical sanity check | ✅ DONE (d33ee00, 11/11 tests) |
| Phase 3 — note to Tom | ✅ SENT — awaiting Tom's response |

**Next action:** Wait for Tom. Do not speculate. Do not modify scientific claims.

---

**Created:** 2026-06-07
