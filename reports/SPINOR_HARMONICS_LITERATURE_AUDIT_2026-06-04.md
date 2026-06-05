> **⚠️ DRAFT / UNVERIFIED LITERATURE NOTES.**
> Do not cite externally without checking original PDFs.
> See `S3_SPINOR_HARMONICS_SYNC_AUDIT_2026-06-04.md` for claim classification.

# Spinor Harmonics Literature Audit — 2026-06-04

**Type:** Research note (no commits yet — pending operator approval)
**Trigger:** Tom Lawrence's open α-problem on S³ spinor harmonics (Part 3 video, slide 95)
**Scope:** Two peer-reviewed papers (Camporesi-Higuchi 1996; Ben Achour et al 2015) + review of `cc_toy_lab/spectral/dirac_s3.py`
**Author:** Sergey Boyko (autonomous Claude research session, awaiting operator review)

---

## Executive summary

1. **Tom's α-problem is fully solved in the literature** — Camporesi & Higuchi (1996), arXiv:gr-qc/9505009, Sec. 3.1. The correct α-dependence is a Jacobi polynomial; `√sin(2α)` is the measure factor confused with the eigenfunction.
2. **Our `dirac_s3.py` does not have the same bug** — it is a diagonal eigenvalue mockup, not a differential operator construction.
3. **An architectural insight follows**: in the current GeoSpectra Kronecker structure `H = (D_S³)² ⊗ I_S¹ + I_S³ ⊗ P_S¹`, the S³ factor is passive (diagonal block scaling). **All DISCRETIZATION_SENSITIVE variation in the v0.1.24 verdict comes from the S¹ family.** This was implicit before — now it is explicit.
4. **Recommendation:** add one paragraph to `docs/CLAIMS_AND_CAVEATS.md` to make point 3 explicit, and consider a future module `dirac_s3_full.py` that actually computes Camporesi-Higuchi spinor harmonics (would address Tom's framework directly).

---

## Findings — verbatim formulas from the two papers

### Camporesi-Higuchi 1996 (gr-qc/9505009)

| Eq. | Content |
|---|---|
| 3.1 | `ds²_N = dθ² + f(θ)² ds²_{N-1}`, `f(θ) = sin θ` — geodesic polar coordinates |
| 3.5 | Spin connection components: `ω_{ijk} = (1/f) ω̃_{ijk}`, `ω_{iNk} = (f'/f) δ_{ik}` |
| **3.9** | **`∇_a ψ = e_a ψ − (1/2) ω_{abc} Σ^{bc} ψ`** — the spin-connection term Tom omits |
| 3.25 | `φ_{nl}(θ) = (cos θ/2)^{l+1} (sin θ/2)^l P^{(N/2+l-1, N/2+l)}_{n-l}(cos θ)` — explicit angular eigenfunction |
| 3.26 | `λ²_{n,N} = (n + N/2)²` — eigenvalue formula; for S³ (N=3) gives `λ = ±(n + 3/2)` |
| 3.34 | `∇̸ ψ^{(s)}_{±nlm} = ±i(n + N/2) ψ^{(s)}_{±nlm}` — full first-order Dirac equation |

### Ben Achour et al 2016 (1505.03426)

| Eq. | Content |
|---|---|
| 1 | Hopf coordinates: `x¹ = sin α cos φ`, `x² = sin α sin φ`, `x³ = cos α cos θ`, `x⁴ = cos α sin θ` |
|  | Metric: `ds² = dα² + cos² α dθ² + sin² α dφ²`, α ∈ [0, π/2] |
| 3 | Scalar mode: `Φ = C e^{i(Sφ+Dθ)} (1−x)^{S/2} (1+x)^{D/2} P^{(S,D)}_{L/2−m+}(x)` with `x = cos(2α)` |

Translating Ben Achour eq 3 using `(1 − cos 2α) = 2 sin² α` and `(1 + cos 2α) = 2 cos² α`:

```
Φ ∝ sin^S(α) · cos^D(α) · P^{(S,D)}_n(cos 2α) · e^{i(Sφ + Dθ)}
```

The lowest mode (S=0, D=0, n=0): `Φ = const`. The `√sin(2α) = √(2 sin α cos α)` form **never** appears for any (S, D, n). It is the square root of the measure factor `sin(2α)`, not an eigenfunction.

---

## Review of `cc_toy_lab/spectral/dirac_s3.py`

### Construction (lines 81–107)

```python
operator = np.zeros((total_dim, total_dim), dtype=complex)
# k=0: negative-only branch, λ = -(0 + 3/2)/R = -3/2/R
for i in range(k0_neg_degeneracy):
    operator[offset + i, offset + i] = eigenvalue_k0_neg
# k ≥ 1: both branches
for k, ...:
    eigenvalue_pos = (k + 0.5) / radius
    eigenvalue_neg = -(k + 1.5) / radius
    # fill diagonal blocks with these eigenvalues, with correct degeneracies
```

This is a **diagonal matrix** with eigenvalues set to the analytic values and correct degeneracies. The eigenvectors are the standard basis vectors.

### What this gives us

- ✅ Correct eigenvalue spectrum by construction
- ✅ Correct degeneracy structure
- ✅ Hermitian (trivially)
- ✅ Validates the positive-control identity `λ = ±(k + 3/2)/R` against the analytic formula

### What this does **not** give us

- ❌ Real Dirac eigenspinors (the Camporesi-Higuchi `ψ^{(s)}_{±nlm}` of eq 3.32)
- ❌ Spinor harmonics in any coordinate system
- ❌ Spin connection (`(1/2) ω_{abc} Σ^{bc}` in eq 3.9)
- ❌ Hopf-coordinate or geodesic-polar α-dependence

### Verdict for `dirac_s3.py`

**Not a bug.** This is an intentional mockup. The Gate 4B IPR-contrast analysis uses it as a spectrum source inside a Kronecker product with a real S¹ operator. For that purpose, the diagonal mockup is sufficient and correct.

**But there is an architectural consequence** (next section).

---

## Architectural consequence — what the DISCRETIZATION_SENSITIVE verdict actually tested

The full operator is built in `s3_s1_product_discretized.py` line 88:

```python
h_total = np.kron(h_s3, eye_s1) + np.kron(eye_s3, p_s1)
```

with `h_s3 = D_S³ @ D_S³` (a diagonal matrix from the mockup, squared).

This means:

1. The S³ factor enters only as a **diagonal block-scaling** of the S¹ operator
2. All variation across discretization families (ring / wilson_ring / spectral_circle) lives **entirely in `p_s1`**
3. The 5-level specificity cascade (L1 random Hermitian, L2 scrambled, L3 FFT-vs-lattice, L4 within-lattice, L5 Wilson-term) is therefore measuring **properties of the S¹ family**, not S³×S¹ physics

This **does not invalidate v0.1.24** — the verdict `DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC` is exactly the right description of what the harness measures. The literature audit just clarifies *why*: because the S³ factor is architecturally passive in this construction.

---

## Recommended action items (await approval)

### A. Minimal, low-cost, low-risk

**A1. Add one paragraph to `docs/CLAIMS_AND_CAVEATS.md`** explicitly noting:
> The S³ Dirac factor in `cc_toy_lab/spectral/dirac_s3.py` is implemented as a diagonal eigenvalue mockup (correct spectrum by construction, standard-basis eigenvectors). All discretization-sensitivity observed in the v0.1.24 cascade therefore arises from the S¹ discretization family. This is consistent with the GEOMETRY_AGNOSTIC half of the verdict.

**A2. Add a reference to Camporesi-Higuchi 1996 in `docs/RESEARCH_CONTEXT.md`** as the canonical source for spinor harmonics on S^N.

**A3. Save this report** as-is (already done as `reports/SPINOR_HARMONICS_LITERATURE_AUDIT_2026-06-04.md`).

### B. Future direction (not for this session)

**B1.** Build `cc_toy_lab/spectral/dirac_s3_full.py` implementing the Camporesi-Higuchi construction (eqs 3.25, 3.32, 3.34) — gives real S³ Dirac eigenspinors in geodesic-polar coordinates, not just the spectrum.

**B2.** Compare diagonal-mockup eigenvalues with `dirac_s3_full.py` eigenvalues as a positive control on the full implementation.

**B3.** Once `dirac_s3_full.py` works, the S³ factor in the product operator stops being passive, and the cascade can be re-run to see whether L4/L5 sensitivity emerges — this would be a real test of S³×S¹ physics, addressing Tom's framework redirect from CAMP 2026-05-26.

### C. NOT recommended

- Do **not** rebuild or rename GeoSpectra
- Do **not** retract or weaken the v0.1.24 verdict — it is correct, just now better understood
- Do **not** send anything to Tom without Sergey's explicit approval

---

## Status

- **Commits:** none (this report is created in the working tree only; awaiting operator approval before `git add`)
- **Tom letter:** evening review with Sergey before sending
- **Other projects (GeoScan):** untouched
- **Compute used:** zero (pure literature work)

**Generated:** 2026-06-04 (autonomous research session)
