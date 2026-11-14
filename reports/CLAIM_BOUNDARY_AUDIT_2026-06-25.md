# Claim Boundary Audit - 2026-06-25

Scope: Track B public claims, L3/L3b proof chain, and arXiv readiness.
Audit basis: repository HEAD `7c851f0`, local files as of 2026-06-25.

## Verdict

**REWORK before public release / arXiv.**

The current `preprint.tex` is substantially more honest than older overview files,
but the public claim surface is inconsistent. The strongest problem is not Python
correctness; it is claim strength drifting ahead of the newest L3B result.

## Blocking Findings

### HIGH-1: Collaboration claim conflicts with project fences

[CODE] `tom_s3_spinor_toy/preprint.tex:57` says:
`In collaboration with Tom Lawrence`.

[CODE] This conflicts with the repository's own public fence:
`README.md:226` says GeoSpectra is developed independently and is not endorsed
by Tom Lawrence; `tom_s3_spinor_toy/preprint_abstract.md:78` says no Tom
Lawrence endorsement claim; `activeContext.md:715` says hard fences include
no Tom endorsement.

Risk: external readers can interpret "in collaboration with" as co-authorship,
endorsement, or formal affiliation.

Required fix: replace with a narrower acknowledgement, e.g. "Inspired by and
building on Lawrence [2022]; discussions acknowledged separately" unless explicit
written permission exists for the collaboration claim.

### HIGH-2: N_gen=3 public claims are stronger than the current L3 state

[CODE] Older public files claim "N_gen=3 EXACTLY" or "derived":
`README.md:23`, `README.md:31`, `README.md:94`,
`tom_s3_spinor_toy/README.md:3`, `tom_s3_spinor_toy/README.md:50`,
`tom_s3_spinor_toy/README.md:201`, `tom_s3_spinor_toy/README.md:247`,
`tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md:15`,
`tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md:197`,
`tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md:316`.

[CODE] The newest L3 evidence says:
- E-L3-PARTIAL proves `ind=1 per channel`, but full L3 independence remains open
  (`20260625-l3-partial/decision.md:31-34`, `:52-58`).
- E-L3B proves the pure G2 path is impossible; the three G2-equivariant bundles
  are isomorphic (`20260625-l3b-bundle-obstruction/decision.md:19-31`).
- Full distinction requires Spin(8) input and is conditional on preserving Spin(8)
  as an internal fiber symmetry (`decision.md:54-67`).
- `preprint.tex` correctly says `N_gen=3` is conjectural/open at lines 86-91,
  168-170, 596, and 622-623.

Risk: public README/status files can be cited against the current preprint and
against the L3B impossibility theorem.

Required fix: downgrade public wording to:
`ind(D_S6 x S-) = 1 per triality channel is proved; N_gen=3 is conditional/conjectural pending L3b, i.e. Spin(8) fiber-symmetry input or another independence proof.`

### HIGH-3: `preprint_abstract.md` is stale and contradicts `preprint.tex`

[CODE] `tom_s3_spinor_toy/preprint_abstract.md:20` says "We prove N_gen = 3
exactly"; `preprint_abstract.md:48` repeats "zero-parameter prediction".

[CODE] `preprint.tex` now says N_gen=3 is conjectural and L3b is open
(`preprint.tex:86-91`, `:622-623`, `:842-860`).

Risk: reviewers may read the markdown abstract first and see a stronger claim
than the actual arXiv source.

Required fix: mark `preprint_abstract.md` stale or update it from `preprint.tex`.

## Major Findings

### MEDIUM-1: Stabilization wording still overstates the parameter status

[CODE] `preprint.tex:111-119` abstract says the radius is fixed by a zero-fit
condition and gives a moduli-to-KK ratio around 2%, while also saying lambda is
free. The body is better: `preprint.tex:682-699` narrows this to "zero-parameter
in the sense independent of C" once `(lambda, rho6*)` are fixed, and labels
2.02% as a coordinate-space proxy with a canonical proxy around 0.25%.

[CODE] `activeContext.md:75-76` records prior audit findings that the
"zero-parameter" rho claim was an overclaim and the 2.02% physical-mass claim
was falsified.

Required fix: in the abstract, replace "zero-parameter prediction" with
"conditional analytic consequence under the stated potential inputs"; replace
"m_mod/m_KK approx 2%" with "coordinate-space proxy; physical ratio open".

### MEDIUM-2: Markdown claim audit misses the current risk class

[VERIFIED-SYNTHETIC] `python -m pytest -q ... test_markdown_claim_audit.py`
passes, but the test only scans older forbidden phrases: lambda fixed, S3xS1
solved, topology validation, Tom ansatz solved, etc.

[CODE] It does not currently guard:
- `N_gen=3 EXACTLY`
- `We prove N_gen = 3 exactly`
- `zero-parameter prediction`
- `m_mod/m_KK = 2.02%` as a physical ratio
- `In collaboration with Tom Lawrence`

Required fix: extend the claim-audit regex list after the wording is corrected,
so these phrases cannot regress.

## L3/L3b Proof-Chain Status

| Node | Status | Evidence |
|---|---|---|
| L2 index `ind=1` for S- | PROVED internally | E-KP1 + preprint |
| L4B `dim ker=1` | PROVED internally | `20260625-kp-zero-mode/decision.md:12-40` |
| Coker zero | PROVED internally | `20260625-e-coker/decision.md:12-41` |
| L3a `ind=1 per channel` | PROVED internally | `20260625-l3-partial/decision.md:11-29` |
| L3b G2-geometric independence | REJECTED | `20260625-l3b-bundle-obstruction/decision.md:15-31` |
| L3b Spin(8) independence | CONDITIONAL / OPEN | `decision.md:56-67` |
| `N_gen=3 exactly` | CONDITIONAL, not final public claim | follows only if L3b closes |

Cheapest decisive next test: confirm whether the proposed S3xS6 setup preserves
Spin(8) as an internal fiber symmetry in the sector where `8_v`, `8_s`, and
`8_c` live. If not, the present chain supports one proved zero mode per labelled
channel, but not three independent generations.

## arXiv Gate

Technical package: **PASS with minor warnings**.

[VERIFIED] `preprint.log` shows PDF output written and no LaTeX fatal/undefined
errors were found by log scan; only warnings about float placement and PDF string
tokens. The package `tom_s3_spinor_toy/arxiv_preprint_2026-06-25.tar.gz`
contains `preprint.tex`.

Content gate: **REWORK/BLOCK** until HIGH-1, HIGH-2, and HIGH-3 are fixed and
the tarball is regenerated.

## Safe Public Wording

Allowed:
`We prove ind(D_S6 x S-) = 1 for the twisted S- bundle and show the same index
calculation applies to each SO(8) triality channel. The full N_gen=3 conclusion
requires an additional L3b independence input, most likely Spin(8) fiber symmetry.`

Forbidden until L3b is closed:
`N_gen=3 EXACTLY`, `we prove three generations`, `three independent derivations`,
`derived Standard Model generations`, `in collaboration with Tom Lawrence`,
and any physical `m_mod/m_KK=2.02%` prediction without the coordinate-proxy caveat.

