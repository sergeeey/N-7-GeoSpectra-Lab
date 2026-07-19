# Round128 — Claim

**User-requested continuation of round127:** find the Cartan-Weyl
alignment between `su3_v` (round124/G102's octonion vector-rep `su(3)`)
and `su3_sigma` (G14/G15's `S⁶`-spinor `su(3)`), completing the last
open step from round127's own Kill Analysis / Relaxation Map.

## Prior Result Gate

Round127 established, with high confidence (End-dimension identity,
`Hom(V,V)=6` on both sides forcing the `1⊕1⊕3⊕3̄` decomposition uniquely),
that `ℂ⊗8_v` and `Σ` are the SAME abstract `su(3)`-module — but a naive
generator-by-index pairing gave `Hom=4`, traced to the two constructions'
generator bases never having been aligned to the same abstract Lie
algebra elements. Round127's own skeptic review flagged this alignment
step as a LIVE check that could still falsify the abstract-isomorphism
claim if it turns out to be impossible — not a mere formality.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Does there exist an explicit linear
change of basis `Φ` (on the abstract 8-dim `su(3)` Lie algebra) and an
invertible intertwiner `S` (on the 8-dim representation spaces) such that
`S·A_i·S⁻¹ = Σⱼ Φᵢⱼ·B_j` for all `i`, where `{A_i}=su3_v` and `{B_j}
=su3_sigma`?

## Method (pre-registered)

1. **Find the Cartan subalgebra (CSA) of `su3_v` independently:** pick a
   generic element `H=Σcᵢ Aᵢ` (random real coefficients), compute its
   centralizer within `span(su3_v)` — for a generic/regular `H`, this
   centralizer IS the 2-dim CSA containing it (same technique G10-B
   itself already used and verified for the vector-rep `su(3)`).
2. **For `su3_sigma`, reuse G10-B's own already-identified Cartan
   generators** (`H₁=(2/3)M₀₁−(1/3)M₂₃−(1/3)M₄₅`,
   `H₂=−(1/3)M₀₁+(2/3)M₂₃−(1/3)M₄₅`, explicit 6×6 so(6) matrices, already
   verified to span a rank-2 CSA of `su3_vec`), then Clifford-lift them
   via `lift_to_spinor` to get the CSA of `su3_sigma` directly — reusing
   already-verified work rather than re-deriving from scratch.
3. **Find root vectors on each side:** diagonalize the joint action of
   the 2-dim CSA on the 6-dim complement (within each `su(3)` copy),
   extracting the 6 root vectors and their `(α,β)` eigenvalue pairs — the
   standard `A₂` root system (regular hexagon in the Cartan dual plane).
4. **Match the two root systems** up to the residual symmetry of `A₂`
   (Weyl group, order 6, plus the outer `ℤ₂` from complex conjugation,
   order 12 total) — find the specific rotation/reflection/scaling that
   aligns corresponding root vectors' eigenvalue patterns.
5. **Construct `Φ`** from the matched CSA + root correspondence, then
   re-run the Hom-space computation with `Φ`-aligned generators, searching
   for an invertible `S`.
6. **If found:** transport round124's `su(3)`-centralizer through `S`
   into `Σ`'s basis and compare literally against G15's `BmL` matrix —
   completing round126's original goal for the first time with a
   methodologically sound approach.

## Pre-registered kill criteria

| Outcome | Verdict |
|---|---|
| Either side's "generic" `H` fails to give a 2-dim centralizer (i.e. accidentally non-regular) | Retry with a different random seed — not a structural failure, a generic-element sampling issue |
| Root systems, once matched by the best available alignment, do NOT correspond (residual mismatch beyond numerical tolerance) | **ALIGNMENT_FAILED** — would retroactively weaken round127's abstract-isomorphism claim; report honestly, do not force a match |
| Root systems align, `Φ` constructed, but the resulting Hom-space search still finds no invertible `S` | **ALIGNMENT_INSUFFICIENT** — the CSA/root alignment alone doesn't fix the full isomorphism (e.g. a residual discrete ambiguity remains unresolved); report the residual Hom dimension found |
| Root systems align, `Φ` constructed, invertible `S` found, verified (`S·A_i·S⁻¹=ΦB` to high precision) | **ALIGNMENT_SUCCESSFUL** — proceed to the literal `B-L` comparison |

## What this does NOT mean (pre-registered)

1. Even `ALIGNMENT_SUCCESSFUL` does not itself establish a physical
   identification with `B-L` — that is a separate, subsequent comparison
   (step 6), with its own honest reporting regardless of outcome.
2. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT re-derive G10-B/G11/G14/G15's or G102's own computations —
   reuses all of them by direct import.
