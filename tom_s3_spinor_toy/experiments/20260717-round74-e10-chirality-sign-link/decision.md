# E10 — Decision

**Date:** 2026-07-17
**Verdict:** **OPEN on all three sub-questions — no existing project convention
currently links t=0-vs-t=1 to S⁶'s chirality.** One genuine, already-flagged gap
confirmed (Q3/preprint.tex:1493-1495 already names "orientation" as an open
convention-dependency, corroborating this experiment's motivating premise). One
new, clearly-[SPECULATIVE] candidate synthesis identified (SU(2)_L/R vs.
left-/right-invariant frames) — **not** an existing convention, **not**
verified, **not** a resolution of H1c.
**Go/no-go:** Does not promote H1c, KT-8, or E2/E3/E7/E9. At most contributes one
new candidate follow-up question (labeled "E11-candidate" below) to a future
round, if pursued.

## Q1 — Product-orientability link (S³ orientation ↔ S⁶ orientation)

**Answer: no such statement exists in this project's text.**

`preprint.tex` discusses orientation exactly twice as a physically load-bearing
discrete choice, and both instances are about $S^6$ alone:
- Line 120-124: "The sign $\mathrm{sign}(\mathrm{ind})=\mathrm{sign}(c_3)=+1$
  gives a left-handed zero-mode excess... fixing a discrete chirality label with
  a single input: the $S^6$ orientation."
- Line 884-912 (Lemma L5): "the chirality of the weak interaction is fixed by
  the orientation of $S^6$ up to a single $\ZZ_2$ choice; no additional discrete
  inputs are required." (line 890-891, repeated 910-912).

Both instances explicitly claim **"no additional discrete inputs are
required."** This is itself informative: the paper's own headline claim is that
$S^6$'s orientation is *sufficient* — it does not, anywhere, invoke or require a
companion orientation choice on $S^3$, and does not state an orientability
constraint linking the two factors' orientations (e.g. no statement of the form
"the product $S^3\times S^6$ admits a spin structure only for a compatible pair
of orientations," nor any $w_1$/$w_2$ Stiefel–Whitney-class discussion for the
product). $S^3$ and $S^6$ are each individually simply-connected and
orientable, so the product $S^3\times S^6$ is automatically orientable
regardless of any choice on either factor (orientability of a product of
orientable manifolds is unconditional — no constraint to violate). A genuine
spin-structure subtlety could in principle arise only from *which* spin
structure is chosen if $H^1(\cdot;\ZZ_2)\neq 0$ obstructed uniqueness, but
$S^3\times S^6$ is simply connected ($\pi_1=0$ for both factors), so the spin
structure is unique — there is no room for a nontrivial orientation-pairing
constraint of the kind the question asks about.

**Verdict Q1: OPEN — no link exists, and, more strongly, no link is
*topologically possible* via the mechanism the question envisions (a
compatibility constraint between two spin structures), because
simple-connectedness makes the product spin structure unique once each factor's
orientation is picked separately.** This is a clean negative result, not a gap
in search coverage.

## Q2 — Chirality-matching link (does t affect the full zero mode's chirality?)

**Answer, via the project's own established mechanism: no.**

preprint.tex:1421-1445 ("Full-operator zero-mode gap") derives, for the product
ansatz used throughout the paper:
```
D_full^2 = D_{S^3}^2 ⊗ 1 + 1 ⊗ D_{S^6,S^-}^2
```
via the forced Clifford-product construction $\Gamma_{\mathrm{full}}(e_j) =
\Gamma^{S^3}_j\otimes\chi_{S^6}$ (tangent to $S^3$) and
$\Gamma_{\mathrm{full}}(f_i) = \mathbf 1\otimes\Gamma^{S^6}_i$ (tangent to
$S^6$) — "matching the standard construction for a Riemannian product with an
even-dimensional factor... derived from the graded Clifford-algebra structure of
$\mathrm{Cl}(V\oplus W)$" (line 1428-1434). Crucially, line 1479-1482 states
this decoupling identity survives *any* deformation of the $S^3$ factor,
including the torsion family: "The product-decoupling identity from the item
above was independently verified to survive this deformation — in fact for
*any* operator on the $S^3$ factor, not only the torsion family, since the
cross-term cancellation depends only on the $S^6$ factor's own chirality
operator [$\chi_{S^6}$]."

This is the direct answer to Q2: the **chirality grading** of $D_{\mathrm{full}}$
(the operator that distinguishes $\ker D^+$ from $\ker D^-$, which is what
`sign(ind)` and Lemma L5 are about) is built entirely out of $\chi_{S^6}$ — the
$S^3$ factor's own connection (Levi-Civita, or any $\nabla^t$ deformation,
$t=0,1$ or otherwise) enters $\Gamma_{\mathrm{full}}$ only through
$\Gamma^{S^3}_j$, tensored with $\chi_{S^6}$, and never appears in the chirality
operator itself. $S^3$ is odd-dimensional (3D); it has no independent
$\Gamma_5$-type chirality grading of its own in this construction — the whole
project's chirality bookkeeping is a property of the even-dimensional $S^6$
factor alone.

**Verdict Q2 (direct mechanism): OPEN/FAIL as a source of a matching-chirality
gate.** Within the project's own established Clifford-product framework, $t$
cannot, by construction, affect the chirality label of a hypothetical
$D_{\mathrm{full}}$ zero mode — that label is already fully and exclusively
fixed by $S^6$, independent of whatever is eventually found on $S^3$. There is
no room for a "does t match S⁶'s chirality" consistency condition through this
channel, because $t$ structurally cannot touch chirality here.

**A separate, NOT-yet-existing candidate link (clearly [SPECULATIVE], reported
per Q2 in the interest of completeness, not as a PASS):** `\S`\,sec:gauge-S3
(preprint.tex:273-279) identifies $\mathrm{Iso}(S^3)=\mathrm{SO}(4))\cong
\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ with the electroweak-plus-right gauge
factors directly, where $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ acts on
$S^3=\mathrm{SU}(2)$ by left and right group translation respectively (this is
the only geometrically natural realization of $\mathrm{SO}(4)$ acting on a Lie
group by isometries of its bi-invariant metric — not separately stated in
`preprint.tex`, but the standard, unique such action). Separately,
`experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md`
([INFERRED], not independently verified there) attributes the $t=1$ failure of
the left-invariant ansatz to the classical fact that the Cartan–Schouten
$(-)$-connection ($t=0$) is parallelized by **left**-invariant vector fields
while the $(+)$-connection ($t=1$) is parallelized by **right**-invariant vector
fields. By standard Lie theory, left-invariant vector fields are exactly the
ones invariant (trivial) under left translation and transform under right
translation via the adjoint representation — i.e. they are **singlets under the
left-translation action** and **charged under the right-translation action**.

Combining these two established-but-previously-unconnected facts gives a
*representation-theoretic* candidate correspondence: **if** the isometry
labeled $\mathrm{SU}(2)_L$ in `\S`\,sec:gauge-S3 is (as its name suggests, but
is nowhere explicitly stated in `preprint.tex`) the *left*-translation factor,
**then** the $t=0$ zero mode (built in the left-invariant frame, E9) would be an
$\mathrm{SU}(2)_L$-singlet — structurally resembling an SM right-handed field
(which is also an $\mathrm{SU}(2)_L$ singlet) — while a hypothetical $t=1$ zero
mode built in the right-invariant frame (not yet constructed; flagged as
E9's own "candidate E10/follow-up," now literally this experiment's number)
would be $\mathrm{SU}(2)_L$-**charged** (a doublet) — structurally resembling an
SM left-handed field, and thus matching, by gauge-representation content, the
same "left-handed" label that $S^6$'s $\mathrm{sign}(c_3)=+1$ already fixes via
a completely independent mechanism.

**This candidate link is explicitly NOT promoted to PASS**, for three
independent reasons, each sufficient on its own:
1. `preprint.tex` never states which translation direction is
   "$\mathrm{SU}(2)_L$" — this is presented here as the only geometrically
   natural convention, not as something the paper commits to.
2. Whether the *spinor* (as opposed to the vector frame used in E9's
   construction) genuinely inherits the same triviality/non-triviality pattern
   under $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ was **not checked** in this
   experiment or in E7/E9 — this requires a representation-theory computation
   (decompose the spin-lift construction under the $\mathfrak{su}(2)\oplus
   \mathfrak{su}(2)$ action) that was explicitly out of scope here.
3. Even if (1) and (2) both held, this would only argue that *if* a $t=1$ zero
   mode is eventually constructed (E9's own flagged open follow-up, the
   right-invariant trivialization was never built), *and if* the physical
   requirement is that such a mode be an $\mathrm{SU}(2)_L$ doublet, *then*
   $t=1$ would be the physically preferred choice — a chain of two unverified
   conditionals, not a proof, and moreover this "physical requirement" is
   itself external input the paper never states (it would have to be argued for
   independently, e.g. from wanting the eventual $S^3$-factor's zero mode to
   carry the same electroweak quantum numbers as the $S^6$-factor's zero mode —
   itself a new physical assumption not currently anywhere in the paper, since
   presently the $S^3$ factor's zero mode does not even exist per KT-8's own
   "blocking gap" verdict).

**Verdict Q2 (candidate synthesis): reported as [SPECULATIVE — new candidate
gate for a possible future round], explicitly NOT a PASS.**

## Q3 — Existing S³ orientation/chirality convention elsewhere in the paper

**Answer: no explicit fixing found, but the paper's own text already flags this
exact gap.**

Searched `preprint.tex` for every occurrence of "orientation," "S^3," and the
full \S\,sec:gauge-S3 section (line 255-298). Findings:
- \S\,sec:gauge-S3 (line 273-279) fixes $\mathrm{Iso}(S^3)=\mathrm{SO}(4))\cong
  \mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ as a *representation-theoretic*
  (gauge-group) identification, with no accompanying orientation/handedness
  statement about $S^3$ itself (unlike the $S^6$ treatment, which explicitly
  invokes "standard orientation," `\ZZ_2` choice, and matching to the SM
  convention — see Q1 above).
- Line 1493-1495 (in the "$S^3$ torsion deformation" open-problems item) already
  states, **unprompted, in the paper's own words**, prior to this experiment:
  *"The crossing values are also convention-dependent (torsion normalization,
  **orientation**, choice of Levi-Civita reference point) and must always be
  quoted together with the full frozen convention, not as bare numbers."* This
  is external corroboration — from the project's own already-existing text, not
  from anything invented in this experiment — that "orientation" is a real,
  previously-recognized loose end for exactly this torsion family. But the
  sentence only *names* orientation as a dependency; it does not specify what
  the $S^3$ orientation convention actually is, nor connect it to $S^6$'s.

**Verdict Q3: OPEN, with one useful confirmation** — the project's own text
independently corroborates that this experiment's motivating question
("orientation" as a missing piece for the $S^3$ torsion family) is not a
manufactured concern but one the paper's authors (this project, in an earlier
session) already flagged as unresolved. No existing convention was found that
resolves it.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result rules out:** (a) that there is currently any
  orientability/topological obstruction linking $S^3$'s and $S^6$'s orientations
  (Q1 — ruled out on structural grounds: simple connectedness makes the product
  spin structure unique regardless); (b) that the sign of $t$ can affect the
  chirality grading of $D_{\mathrm{full}}$'s kernel through the project's
  established Clifford-product mechanism (Q2, direct channel — ruled out by the
  project's own decoupling identity, preprint.tex:1479-1482).
- **What remains unresolved / open:** H1c (which of $t=0,1$ is physically
  realized) — untouched; whether the $\mathrm{SU}(2)_L$/left-translation
  identification (needed for the Q2 candidate synthesis) is even the right
  convention — unstated in the paper, would need to be decided or derived; and
  whether spinors (not just vectors) inherit the left/right-invariant-frame
  triviality pattern — unverified.
- **Relaxation Map for the one surviving candidate (Q2 synthesis):** if pursued,
  the cheapest next test is representation-theoretic, not physical: decompose
  the $t=0$ constant spinor $\psi$ explicitly constructed in E9
  (`e9_explicit_parallel_spinor.py`) under the $\mathfrak{su}(2)_L\oplus
  \mathfrak{su}(2)_R$ action (i.e. verify directly whether $\psi$ is a genuine
  $\mathrm{SU}(2)_L$-singlet, not merely assumed to inherit the vector-frame
  pattern) — this is a well-defined, cheap follow-up using tools already built
  in E9, but was not run here (out of scope for a literature/scoping
  experiment) and is NOT a promise that running it would produce a PASS.

## Summary table

| Sub-question | Verdict | Basis |
|---|---|---|
| Q1 — product orientability link | **OPEN — no link exists; topologically ruled out as impossible via the envisioned mechanism** | Both factors simply connected ⟹ unique product spin structure regardless of orientation choices; preprint.tex never states such a link (only $S^6$'s own orientation is invoked, "no additional discrete inputs required," preprint.tex:890-891) |
| Q2 — chirality-matching link (direct, established mechanism) | **OPEN/FAIL — structurally impossible**: $t$ cannot enter the chirality grading | preprint.tex:1479-1482 — decoupling identity depends only on $\chi_{S^6}$ |
| Q2 — chirality-matching link (candidate synthesis, SU(2)_L/R vs. left/right-invariant frames) | **[SPECULATIVE] — new, not previously existing; NOT verified; NOT a PASS** | Combines \S\,sec:gauge-S3 (preprint.tex:273-279) with E9's [INFERRED] left/right-invariant duality; requires an unstated convention + an unverified spinor-representation computation |
| Q3 — existing S³ orientation convention elsewhere | **OPEN — not fixed anywhere**, but the gap is independently corroborated by the paper's own pre-existing text (preprint.tex:1493-1495) | \S\,sec:gauge-S3 gives no handedness statement for $S^3$; line 1493-1495 already names "orientation" as unresolved |

## Why this is an honest OPEN, not a forced PASS

Per this project's own methodology (`~/.claude/rules/falsification-ladder.md`,
`research-methodology.md`), a genuine "no such link exists, would need new
physical/mathematical input" is a legitimate and useful outcome, not a failure
of this experiment. All three sub-questions come back OPEN with respect to any
*already-implicit* project convention. The one candidate synthesis surfaced
(Q2's SU(2)_L/R link) is reported transparently as new and speculative — not
smuggled in as a resolution — precisely to avoid the "structuring noise as
signal" failure mode this project's Zero-Signal Gate and Anti-Overfitting Gate
exist to catch. Nothing here promotes E2/E3/E7/E9, touches H1c, KT-8, or any
`preprint.tex` claim.

## Recommended next action (if pursued further — not started here)

In order of cheapness: (a) explicitly decide/derive which translation direction
on $S^3=\mathrm{SU}(2)$ this project intends by "$\mathrm{SU}(2)_L$" (a
convention choice, analogous in kind to fixing $S^6$'s orientation) — cheapest,
pure bookkeeping; (b) decompose E9's explicit $t=0$ spinor under
$\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R$ to check the singlet/doublet
claim directly (reuses E9's own `e9_explicit_parallel_spinor.py` machinery); (c)
only after (a) and (b), and only if a genuine physical reason for
"the eventual S³ zero mode must match S⁶'s left-handed label" is separately
motivated (not yet done anywhere in this project), would t=0-vs-t=1 selection
via chirality-matching become a testable H1c candidate. None of (a)-(c) was
attempted in this experiment.
