# C124 claim -- PRE-REGISTRATION ONLY. Execution deliberately deferred to
a separate session. No `decision.md` in this folder yet, by design.

## Why pre-registration, not execution, in this session

C123 (same day) narrowed the open OB1 question to: does a genuine 13D-
covariant local invariant reduce, without a hand-inserted `4+3+6` split,
to (a gauge-invariant transgression equivalent of) `CS₃(ω_{S³})
∧ch₃(E_{S⁶})∧vol₄`? This session already knows the exact closed form of
`CS₃(ω^t)` -- derived, re-derived, and cross-checked by 4+ independent
routes today alone. Starting a search for "which 13D invariant reduces
to this" in the SAME session that already has the target expression
memorized is a textbook HARKing setup: admissibility criteria would be
at constant risk of unconsciously flexing to admit whatever expression
the search turns up. Per this project's own Adaptive Iteration Branch
Rule and the Minimal Relaxation Rule (`falsification-ladder.md`), the
discipline is to freeze the claim and the pass/fail criteria BEFORE the
search, then execute blind -- ideally in a session (or by an agent)
that does not carry today's specific derivations as working memory.

**This file is that freeze. It contains no attempt at the search
itself.**

## Question type (EstimandOps L0)
**Descriptive/existence.** Does a specific mathematical object (an
admissible 13D-covariant local invariant with the stated reduction
property) exist in the space of invariants this project's own field
content allows? No causal or predictive claim; this is a classification
question about parent-action content, not a t-selection search.

## The claim, precisely

$$
\exists\ I_{13} \text{ (a local 13D-covariant invariant, built from
this project's already-admitted fields, before any compactification
ansatz)}
$$
such that, after reduction on $M_{13}=M_4\times S^3\times S^6$, it
contains a nonzero term
$$
\lambda\;CS_3(\omega_{S^3})\wedge ch_3(E_{S^6})\wedge\mathrm{vol}_4,
\qquad \lambda\neq0,
$$
or a gauge-invariant transgression equivalent (a difference of two
Chern-Simons forms, or the boundary term of a genuine 14-form
characteristic class -- NOT a bare, non-gauge-invariant `CS₃(ω)` used
directly, per the gauge-invariance concern already on record from the
external review that produced this claim), **without manually inserting
a "these four vielbeins belong to `M₄`, these six to `S⁶`" splitting
by hand.**

## Admissibility criteria -- ALL SIX required for a PASS verdict

1. `I₁₃` is admissible under the FULL 13D symmetry (Lorentz + gauge)
   BEFORE any compactification ansatz is applied.
2. The `M₄`/`S³`/`S⁶` splitting is not hand-inserted -- it must arise
   from the background ansatz already frozen by this project
   (`PARENT_ACTION_GATE.md` F1), not from choosing which indices go
   where in order to land on the target expression.
3. The coefficient of the reduced term is nonzero on this project's
   ACTUAL background (reuse C123's own already-certified `∫ch₃=1`;
   do not re-derive it, and do not silently swap in a different bundle
   to make this easier).
4. The `t`-dependence comes from the action/invariant itself (through
   `ω_{S³}=ω^t`), not introduced via spectral data (Dirac zero modes,
   eigenvalue crossings) at any point in the derivation.
5. Gauge/Lorentz variation of `I₁₃` is zero, or differs from zero only
   by an admissible boundary/topological term (standard for
   Chern-Simons-type actions -- large gauge transformations shifting
   the action by a quantized integer multiple are fine; anything else
   is not).
6. The resulting term is not simply an already-existing parent-action
   candidate from this project's own prior work, relabeled (check
   against `PARENT_ACTION_GATE.md` F4's full "already tried" list
   before declaring PASS).

## Hard rule -- criteria 1 or 2 violated kills the branch STRUCTURALLY

If criterion 1 fails (no 13D-Lorentz/gauge-admissible invariant exists
with the right field content and degree) or criterion 2 fails (the only
way to reach the target expression requires hand-inserting the
`4+3+6` split), **the branch is dead, full stop -- not "try a
different normalization" or "adjust the ansatz."** This distinction
matters because both failure modes are cheap to mistake for a fixable
technical snag; per the Anti-Overfitting Gate (`falsification-ladder.md`
AOG-1/AOG-2), relaxing criterion 1 or 2 after the fact to rescue the
branch is exactly the kind of post-hoc, non-pre-registered relaxation
this freeze exists to prevent.

## Mandatory search order (Strong Inference, Platt 1964) -- prevents
starting from the target expression and working backward

$$
\boxed{
\text{all admissible 13D invariant tensors}
\;\rightarrow\;
\text{all admissible 13-forms}
\;\rightarrow\;
4{+}3{+}6\text{ reduction}
\;\rightarrow\;
\text{search the reduced output for a }CS_3\text{-shaped term}
}
$$

**Executing this in the reverse order (start from `CS₃∧ch₃∧vol₄`,
search backward for something that reduces to it) is explicitly
FORBIDDEN and would invalidate a PASS verdict regardless of the
algebra's correctness.** The blind-execution session should build the
list of admissible 13D invariant tensors (curvature 2-forms, torsion
3-forms, gauge field strengths already in this project's field content,
and their wedge products up to the required degree) FIRST, independent
of what CS-shaped term is being hunted for, and only then reduce and
inspect the output.

## Two mandatory negative controls (both required before any PASS is
accepted -- neither substitutes for the other)

### Control 1 -- permutation / arbitrary-3-subspace control

If the SAME parent invariant `I₁₃`, applied to an ARBITRARY choice of
3-dimensional subspace of the 9D internal space (not specifically
`S³`), also automatically generates an analogous CS-shaped term for
that arbitrary subspace -- i.e. `S³` is not structurally distinguished
by the invariant itself, only by which subspace the ansatz later
happens to pick out -- then the mechanism is an **artifact of the
decomposition**, not a genuine `S³`-specific selection principle. PASS
requires that `S³` (not an arbitrary 3-subspace) is what the invariant,
independent of the compactification choice, actually singles out.

### Control 2 -- untwisted-`S⁶` control (`ch₃(E)=0`)

Formally replace the twist bundle with a topologically trivial one, so
`ch₃(E)=0`. The candidate parent term `I₁₃` must REMAIN admissible
(criteria 1, 2, 5, 6 unaffected -- those are properties of the
invariant, not of this specific bundle choice), but the EFFECTIVE
SELECTOR through this channel must vanish (`λ·0=0`). If the selector
effect survives this substitution -- i.e. if `I₁₃` still somehow
produces a nonzero `t`-selecting term with a trivial twist bundle --
the mechanism is not genuinely mediated by `S⁶`'s topology at all; it
is a masked bare `CS₃(ω^t)` (already on record, already known, not new
content per C123's own finding that a bare `CS₃` and the `S⁶`-coupled
version have the identical `t`-shape up to a positive constant). This
control is what distinguishes "the `S⁶` factor is doing real work" from
"the `S⁶` factor is along for the ride."

## What this round does NOT show, and explicitly defers

1. Does not attempt the search itself -- no candidate 13D invariant is
   proposed, checked, or ruled out here. That is the blind-execution
   session's job.
2. Does not touch C123's own verdict (`PARTIAL`) or OB1's `PARKED`
   status.
3. Does not re-litigate C123's `P₄=vol₄` finding or the `CS₃` vs `η(D^t)`
   non-collapse result -- both taken as given, cited, not re-derived.
4. Does not attempt F6 (full fluctuation-operator stability) for the
   Yang-Mills mechanism -- deliberately kept OUT of this file; see
   below.

## Separately, NOT mixed into C124 (recorded here for completeness,
already logged in `experiments/20260901-c123-.../decision.md`)

Yang-Mills 1-parameter stability, epistemically marked precisely:

- **Established:** within the homogeneous one-parameter family `∇^t`,
  `E(t)=Ct²(1-t)²` has `E''(0)=E''(1)=2C>0` (stable) and `E''(1/2)=-C<0`
  (unstable) -- `t=0,1` are local minima, `t=1/2` a local maximum,
  along this slice only.
- **Unknown:** stability against the FULL space of perturbations
  `δω(x)`, in particular any `δω(x) \not\propto \partial_t\omega^t`
  (i.e. fluctuations not confined to the 1-parameter family itself).
  `global value/minimum ≠ local fluctuation spectrum` -- these are
  genuinely different claims, and only the first is established.
- **Explicit scoping decision:** the full Hessian/spectral calculation
  needed to resolve the "Unknown" line is NOT to be attempted before
  C124's own blind execution -- it is expensive, and does not itself
  close the parent-action gap even if it succeeds, so it does not
  belong ahead of C124 in priority order (per C123's own
  priority-ordered Relaxation Map).

## Next step (separate session, blind execution)

A future session (or agent instance, ideally one without this
session's specific `CS₃(ω^t)` derivations in working context) reads
this file, builds the admissible-13D-invariant list FIRST per the
mandatory search order above, reduces, and only then checks the output
against the six admissibility criteria and two negative controls. The
resulting `decision.md` in this same folder records PASS / BLOCKED /
structural no-go per the outcomes named in
`experiments/20260901-c123-.../decision.md`'s Relaxation Map, priority
1.
