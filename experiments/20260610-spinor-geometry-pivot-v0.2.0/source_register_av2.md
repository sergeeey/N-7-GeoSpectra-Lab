# AV-2 G0 — Source Register (Step -4 Source Trace)

**Gate:** AV2-G0 (blocking gate from claim_av2_angular.md)
**Date:** 2026-06-10
**Primary source:** Camporesi & Higuchi, *"On the eigenfunctions of the Dirac
operator on spheres and real hyperbolic spaces"*, gr-qc/9505009,
J.Geom.Phys. 20 (1996) 1-18.
**Local copy:** `references/camporesi_higuchi_grqc9505009.pdf` (fetched from
arXiv 2026-06-10, 45 pp., PDF 1.4)
**Verdict:** **G0 PASS** — every formula required for AV-2 located in the PDF
and cross-checked numerically against existing code.

---

## Equation register (all read directly from PDF pages 8-10)

Conventions: geodesic polar θ ∈ [0,π]; Hopf α = θ/2; N = 3 for S³; ρ = (N−1)/2.

| Eq. | Content | Status | Numerical cross-check |
|---|---|---|---|
| 3.17 | S^{N−1} spinor harmonics: ∇̸̃ χ^{(±)}_{lm} = ±i(l+ρ)χ^{(±)}_{lm} | VERIFIED_FROM_PDF | n/a (angular, used in AV-2 E2) |
| 3.18-3.19 | Separation: φ_{+nlm} = φ_nl(θ)χ^{(−)}_{lm} and ψ_nl(θ)χ^{(+)}_{lm} | VERIFIED_FROM_PDF | n/a |
| 3.25 | φ_nl(θ) = (cos θ/2)^{l+1}(sin θ/2)^l P^{(N/2+l−1, N/2+l)}_{n−l}(cos θ) | VERIFIED_FROM_PDF (re-confirmed) | matches `phi_nl_hopf` (legacy E0, 6.7e-7) |
| 3.26 | λ²_{n,N} = (n+N/2)² | VERIFIED_FROM_PDF (re-confirmed) | E0 gate |
| **3.27** | **ψ_nl(θ) = (cos θ/2)^l (sin θ/2)^{l+1} P^{(N/2+l, N/2+l−1)}_{n−l}(cos θ)** | **VERIFIED_FROM_PDF (NEW)** | **matches `g_nl_hopf` exactly** — docstring upgraded from "mirror construction" |
| 3.28 | ψ_nl(θ) = (−1)^{n−l} φ_nl(π−θ) | VERIFIED_FROM_PDF (NEW) | rel err ≤ 2.3e-15, 6 modes |
| **3.29** | [d/dθ + ρ cot θ − (l+ρ)/sin θ] φ_nl = −(n+N/2) ψ_nl | VERIFIED_FROM_PDF (NEW) | rel err ≤ 5e-7 (FD), 5 modes |
| **3.30** | [d/dθ + ρ cot θ + (l+ρ)/sin θ] ψ_nl = +(n+N/2) φ_nl | VERIFIED_FROM_PDF (NEW) | rel err ≤ 5e-7 (FD), 5 modes |
| 3.32 | ψ^{(−)}_{±nlm} = c_N(nl)/√2 · (φ_nl χ^{(−)}_{lm}, ±i ψ_nl χ^{(−)}_{lm})ᵀ | VERIFIED_FROM_PDF (NEW) | structure for AV-2 G1 |
| 3.33 | ψ^{(+)}_{±nlm} = c_N(nl)/√2 · (i ψ_nl χ^{(+)}_{lm}, ±φ_nl χ^{(+)}_{lm})ᵀ | VERIFIED_FROM_PDF (NEW) | structure for AV-2 G1 |
| 3.35-3.37 | Normalization: \|c_N(nl)\|⁻² = ½∫₀^π dθ sin^{N−1}θ (φ_nl² + ψ_nl²); both terms equal by 3.28 | VERIFIED_FROM_PDF (NEW) | see 3.38 |
| **3.38** | \|c_N(nl)\|⁻² = ∫ sin^{N−1}θ φ_nl² dθ = 2^{N−2}\|Γ(N/2+n)\|² / [(n−l)!(N+n+l−1)!] | VERIFIED_FROM_PDF (NEW) | rel err ≤ 6e-16, 5 modes |
| 3.41 | Addition theorem: Σ_{s,l,m} ψ^{(s)†}_{+nlm} ψ^{(s)}_{+nlm} = const on S^N | VERIFIED_FROM_PDF (NEW) | candidate AV-2 G2 sanity check |
| 3.5 | Spin connection: ω_{ijk}=(1/sinθ)ω̃_{ijk}, ω_{iNk}=−(cosθ/sinθ)δ_{ik} | VERIFIED_FROM_PDF (2026-06-05, re-located) | needed only if full 2D lattice built |
| 3.9 | ∇_a ψ = e_a ψ − ½ ω_{abc}Σ^{bc}ψ | VERIFIED_FROM_PDF (2026-06-05) | — |

## Key consequences for AV-2 (grounded, no longer [INFERRED])

1. **H-AV2 boundary mechanism is now PDF-grounded:** ψ_nl ∝ (cos θ/2)^l →
   at α = π/2 the partner component behaves as cos^l α; for l = 0 it is
   NONZERO at the south pole ("for l = 0 they are nonzero at the south
   pole", p. 9). Full-mode densities |φ_nl|² + |ψ_nl|² therefore have
   boundary exponent cos^{2l} — including cos⁰ — exactly the ingredient the
   radial-proxy bilinears lacked.
2. **The first-order system 3.29-3.30 IS the 2-component radial system**
   required for G1 — no spin connection needed at this level (it is already
   absorbed in the ρ cot θ term). The full 2D lattice (risk item 1 of the
   pre-registration) is NOT required for G1/G2/E1.
3. **Measure warning (conventions):** full-spinor orthonormality uses weight
   sin^{N−1}θ dθ = 4 sin²α cos²α (2dα) for N=3 — NOT the radial-proxy weight
   sinα cosα dα. AV-2 inner products must use the sin²θ weight.
4. **Eq 3.41 gives a free integration test for G2:** the degeneracy-weighted
   density sum must be constant on S³.

## What was NOT found / out of scope

- Hopf-coordinate form of the spin connection: NOT in the paper (C-H work in
  geodesic polar). Not needed for the G1/G2/E1 path (consequence 2). If a
  full 2D Hopf lattice is ever required, this becomes a separate derivation
  task with its own source trace.
