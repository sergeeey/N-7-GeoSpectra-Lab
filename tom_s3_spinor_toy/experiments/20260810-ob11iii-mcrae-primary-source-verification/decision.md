# decision — OB11(iii) hard half: McRae 2025 independently re-confirmed, newly connected to this project's own T

## Verdict

`PRIOR_CITATION_CONFIRMED__QUESTION_GENUINELY_OPEN_NOT_NO_GO__NOW_CROSS_REFERENCED_TO_OB11` →
**C67 SUPPORTED.**
**Date:** 2026-08-10 · L0: descriptive · primary source read in full (18 pages), saved to repo
as `McRae_2025_Exploring_Triality_Explicitly.pdf`.

---

## What this round actually establishes (corrected from an initial mischaracterization)

This round set out assuming the in-repo citation (pearl_registry, 2026-07-15) was a secondhand
paraphrase needing verification. **That assumption was wrong and was caught before being written
up**: the 2026-07-15 entry already states it read "the full 18-page paper directly (not just
abstract)" and quotes it accurately. This round's independent re-read is a genuine no-collapse
re-check (same conclusion, reached again from scratch) rather than a correction of an error — the
real, novel content here is different: (a) an independent confirmation the original reading holds
up, and (b) for the first time, an explicit connection between McRae's finding and **this
project's own `T`** (C62, built weeks after the original pearl entry, hence not something that
entry could have referenced), plus a formal cross-reference into OB11's own registry entry, where
this citation had not previously been linked despite bearing directly on condition (iii).

## The status question this round actually answers

Is McRae's "no intertwining action upon the representation space" statement a **proven theorem**
of the paper, or an **author's own open remark**? This distinction matters for how OB11(iii)
should be characterized, and was not made explicit in the original pearl entry. Direct reading
answers it precisely: it is the author's own stated open question, in a paper that explicitly
disclaims novel research.

## The load-bearing passage, quoted exactly (p.17, §5)

> "One obstruction to making this work in the 'obvious' way is finding outer automorphisms which
> act at the level of the representation, and not merely on the algebra. For example in the
> Euclidean case K and H both act on the algebra, and so the automorphism has no 'intertwining'
> action upon the representation space (the fields). However in the Lorentzian case with T and *,
> complex conjugation can be made to act not only upon the Lie algebra generators, but upon the
> fields as well. Thus the question becomes if there is some way, some combination of
> automorphisms, in some base field for our representation or some hyper-complex number system,
> where we can have a non-linear intertwiner which cubes to the identity, yet its square remains
> a non-linear intertwiner as well? For example a standard conjugate-linear operator cannot work,
> because when squared it becomes linear, and so this could not garner us three distinct
> representations. Perhaps if one can realize[s] the triality as three dualities it could be
> feasible."

And, the paper's own closing self-assessment: *"No novel research has been done in this work, it
is foremost a pedagogical piece."*

## Interpretation

McRae's own constructions (`H` for the compact/Euclidean case, `T` for the Lorentzian case — an
unrelated name collision with this project's own `T`) are **algebra-level** automorphisms: linear
maps on the 28-dimensional space of `so(8)` generators, satisfying the right cube-to-identity
property, but not acting on the 8-dimensional representation spaces where actual spinor fields
live. This is *exactly* the level this project's own `T` (`triality_so4xso4_invariance.py`, C62)
already reaches — independently arrived at, consistent with, and now cross-validated against, the
primary literature's own state of the art, not behind it. The paper does **not** prove a
state-level intertwiner is impossible; it reports that the author's own natural, linear attempts
fail, and explicitly speculates (without resolving) that a genuinely non-linear construction or a
reformulation via "three dualities" might work.

## Kill Analysis

**Not killed:** OB11(iii)'s algebra-level half (C62) — untouched, still confirmed.

**Correctly re-scoped, not killed either:** OB11(iii)'s state-level half was never actually
"closed by a no-go theorem" — that was an imprecision in how the earlier citation was carried
forward, now fixed. It remains **genuinely open**, in the strongest sense: open in the primary
literature itself, not merely unattempted inside this project.

**Deliberately not attempted:** constructing a state-level intertwiner here would mean attempting
original mathematical research the cited paper's own author states is beyond their own
"pedagogical" scope — a materially different, much higher-risk undertaking than the rest of this
session's work, which stayed within reusing and extending already-verified constructions. Not
pursued, per the same discipline that kept every other round this session honestly scoped.

## What this does NOT show

1. Does **not** construct a state-level triality operator — deliberately not attempted, see above.
2. Does **not** change condition (iii)'s live status: algebra-level confirmed (C62), state-level
   open (now correctly characterized, not newly resolved).
3. Does **not** affect `N_gen=3`'s CONDITIONAL status.
4. Does **not** imply the paper is wrong or low-quality — it is explicitly, honestly scoped by its
   own author as pedagogical, and is accurate as far as it goes; the correction here is entirely
   about how this project cited it, not about the paper's own content.

## Provenance

Primary source: McRae, C., "Exploring Triality Explicitly: Convenient bases for SO(8), Spin(1,7),
and G2," arXiv:2502.14016v1 [math.RT], 19 Feb 2025. Fetched and read in full this session (not
from memory, not from the prior secondhand citation), saved locally at
`McRae_2025_Exploring_Triality_Explicitly.pdf` (repo root) for reproducibility.
