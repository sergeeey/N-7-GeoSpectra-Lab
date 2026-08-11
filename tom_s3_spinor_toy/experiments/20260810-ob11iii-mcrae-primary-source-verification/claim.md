# OB11(iii), hard half — primary-source verification of the McRae 2025 citation

**Experiment id:** `20260810-ob11iii-mcrae-primary-source-verification`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** pearl_registry entry 2026-07-15 (McRae citation, secondhand at the time),
`experiments/20260810-ob11iii-triality-su3-invariance/` (C62, this project's own `T`)

---

## Why this round exists, and a correction made while scoping it

The user asked to continue through all remaining items, including OB11(iii)'s hard half: an
explicit *state-level* triality operator (not just the algebra-level `1⊗t` this project's own
`T` already provides, per C62). Prior grounding this session cited McRae 2025 (arXiv:2502.14016)
via a pearl-registry entry (2026-07-15) — this round initially assumed that entry was a
secondhand paraphrase and set out to verify it against the primary source. **Checking the pearl
entry's own text before writing anything further showed this assumption was wrong: the
2026-07-15 entry already states "Read the full 18-page paper directly (not just abstract)" and
quotes the paper accurately.** The primary source was still fetched and read independently in
full this round (18 pages, arXiv v1, now saved in this repo as
`McRae_2025_Exploring_Triality_Explicitly.pdf`) — not because the earlier reading was suspected
sloppy, but as a genuine no-collapse re-check (per this project's own audit discipline) and
because it enables something the 2026-07-15 entry could not: **connecting the finding to this
project's own `T` construction (C62, built weeks later)**, and formally cross-referencing it into
OB11's own registry entry, where it had not previously been linked.

## The claim under test

> **C67 (working).** The 2026-07-15 pearl citation is accurate — independently re-confirmed, not
> corrected. McRae 2025 does **not** prove a no-go theorem that Euclidean-signature triality
> admits no representation-space intertwiner. It reports that the paper's own two constructed
> automorphisms
> (`H`, `K` — real, linear, acting on the 28-dimensional Lie algebra of generators) fail to act at
> the representation level, states this as an **open question** in its closing "Final Comments and
> Remarks" section, and explicitly disclaims novel research ("No novel research has been done in
> this work, it is foremost a pedagogical piece"). The question of whether *some* state-level
> operator exists (e.g. a genuinely non-linear intertwiner, or "triality realized as three
> dualities," the author's own speculation) is left open by the paper, not closed against.

## What was checked

Direct read of all 18 pages of the primary source. Key structural facts confirmed:

- §2.3.1 (p.6-7): `H`, the paper's Euclidean triality automorphism, acts on the **28-dim vector
  space of `so(8)` generators** (quartets of the `V_ij`/`L_ij`/`R_ij` basis), with `H³=I₄` in its
  compact 4×4 form — an algebra-level automorphism, matching in kind (not detail) this project's
  own `T` (`triality_so4xso4_invariance.py`, C62, `T³=I` verified on the `so(4)⊕so(4)` subalgebra).
- §4.3-4.4 (p.15-16): the Lorentzian analogue `T` (unrelated name collision with this project's
  own `T`) *does* act on both generators and, via complex conjugation, on the fields — but the
  paper itself flags in §5 that a conjugate-linear operator "cannot work" for triality's genuine
  period-3 structure, since it squares to a linear map.
- §5 (p.17), the exact source sentence: *"in the Euclidean case K and H both act on the algebra,
  and so the automorphism has no 'intertwining' action upon the representation space (the
  fields)."* Immediately followed by: *"the question becomes if there is some way... where we can
  have a non-linear intertwiner which cubes to the identity, yet its square remains a non-linear
  intertwiner as well? ... Perhaps if one can realize[s] the triality as three dualities it could
  be feasible."* — explicitly posed as **open**, not resolved, not proven impossible.
- Final paragraph (p.17): *"No novel research has been done in this work, it is foremost a
  pedagogical piece."*

## What this does NOT mean

- Does **not** mean a state-level triality operator is easy, or close to being found — the primary
  source's own author, having built the explicit bases needed to even ask the question precisely,
  does not know how to construct one either.
- Does **not** mean this project should attempt an original construction here — that would be
  attempting genuinely unresolved research (matching what the paper's own author flags as beyond
  reach in "pedagogical" scope), a materially different and much higher-risk undertaking than
  anything else this session attempted. Not attempted.
- Does **not** change condition (iii)'s status: the algebra-level half (`U` exists, `U³=1`) remains
  confirmed (C62); the state-level half remains open, now with a precisely-characterized,
  correctly-cited reason why, rather than an imprecise secondhand summary.
- Nothing about `N_gen=3`'s CONDITIONAL status changes.
