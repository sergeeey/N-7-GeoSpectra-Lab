# Zenodo upload metadata — "Toward Three Generations from the Geometry of S3 x S6"

Go to https://zenodo.org/deposit/new, upload preprint.pdf (+ optionally preprint.tex
and a snapshot of the test suite as a zip), then fill the form with the fields below.

## Upload type
**Publication** -> **Preprint**

## Title
Toward Three Generations from the Geometry of S3 x S6

## Authors
- Name: Boyko, Sergey
- Affiliation: Ronin Institute for Independent Scholarship
- ORCID: 0009-0009-2178-5701

(reuse the same ORCID as the existing .zenodo.json for the parent repo, for consistency)

## Description (paste into the Zenodo "Description" field)

We derive the Standard Model gauge structure and fermion quantum numbers for one
generation from the geometry of S3 x S6. By identifying the spin connection with
gauge fields (following Lawrence, arXiv:2203.09473), we obtain the gauge group
SU(3) x SU(2)_L x SU(2)_R geometrically, with the full electric charge formula
Q = T3L + (B-L)/2 and all 32 spinor states matching one SM generation. The
U(1)_{B-L} factor needed to complete the Pati-Salam algebra is not itself an
isometry of S3 x S6 (no SU(4) subgroup exists in Iso(S3xS6)); it is identified
from fermion charge content, and a dedicated internal search confirms it is one
member of a family of anomaly-free U(1) generators consistent with the derived
gauge action, chirality, and real structure -- not uniquely selected by these
constraints alone. The gauge coupling ratio g2^2/g3^2 = 15/(16 pi) at equal radii
agrees with the SM value at M_Z within 4.0%, though running the same ratio to the
theory's own predicted string scale gives a ~3.4x mismatch, indicating the M_Z
agreement is a near-electroweak-scale coincidence rather than a scale-consistent
prediction.

We prove that the Atiyah-Singer index of the twisted Dirac operator on
S6 = G2/SU(3) equals exactly one per triality channel (all three SO(8)
representations 8_v, 8_s, 8_c on identical footing), and that the exact
trivial-component kernel dimension (needed to fix dim ker = 1 rather than 2) is
verified by three independent internal routes -- a from-scratch reimplementation,
a full-fibre completeness/Hermiticity audit, and a closed-form analytic
derivation identifying the amplitude as a Killing-spinor Dirac eigenvalue.
We conjecture N_gen = 3 from the G2 = Fix(Z3 subset Aut(O)) triality structure
permuting these three channels. A theorem (Bundle Obstruction, E-L3B) proves
that the G2-equivariant path to channel independence is ruled out, and a further
internal check shows no continuous symmetry inside so(8) at all can distinguish
the three channels internally; this is the paper's one remaining open problem --
distinguishing the three channels requires an additional Spin(8) fibre-symmetry
input external to the present geometric construction.

This is a candidate mathematical mechanism, not an experimentally confirmed theory
of nature -- every conditional or open point above is stated explicitly in the
paper's own Open Problems section, not glossed over. The companion verification
suite (2488 tests: 2484 passing, 4 skipped, exact-arithmetic sympy derivations
for every claim) is available at the linked GitHub repository.

Status: preprint, prepared for arXiv submission (hep-th).

## Keywords
- three generations
- Atiyah-Singer index theorem
- G2 holonomy
- Kaluza-Klein compactification
- coset space dimensional reduction
- octonion triality
- Standard Model fermions
- Dirac operator
- spectral triple
- noncommutative geometry

## License
CC-BY-4.0 (Creative Commons Attribution 4.0) -- same as chosen on the arXiv submission form

## Related/alternate identifiers
- Relation: "isSupplementedBy" -> https://github.com/sergeeey/N-7-GeoSpectra-Lab
  (resource type: software)
- Relation: "isPartOf" or "isVersionOf" -> concept DOI 10.5281/zenodo.20252650
  (only if you consider this a sibling deposit of the same parent project;
  otherwise leave the two Zenodo records independent -- Track A and Track B are
  scientifically distinct results in this repo, so independent records are
  probably cleaner)

## Contributors
- Name: Claude (Anthropic)
- Type: Other
- Affiliation: Anthropic
(matches the existing .zenodo.json convention -- keep AI-disclosure consistent
across arXiv preprint, GitHub repo, and Zenodo record)

## Version
v2 (2026-07-15) -- corresponds to git commit 7505a98 on branch main. Supersedes
v1 (2026-07-08, commit 279fa68): title hedged ("Toward..."), L4B trivial-rank
now internally certified (was open), B-L honestly scoped via a dedicated
uniqueness search (was unexamined), RGE-scale mismatch disclosed in abstract,
7 preprint-wide overclaim/sync fixes applied (Round 58 self-audit), test suite
2488 tests / 2484 passing (one pre-existing failure fixed, unrelated to this
paper's claims).

## Publication date
2026-07-15

## Language
eng

## Notes
This deposit establishes a timestamped, citable public record of this exact
manuscript version (matching git commit 7505a98) prior to peer endorsement
requests being sent to external researchers. UPDATE THIS FILE AGAIN if the
preprint changes further before the actual Zenodo upload -- diff `preprint.tex`
against the commit hash above first.
