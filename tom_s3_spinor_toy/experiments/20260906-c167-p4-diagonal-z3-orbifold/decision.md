# C167 — Decision

**Date:** 2026-09-06
**Verdict:** `HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P` (per claim.md's pre-registered
table) — Step 1 of P4 (C132's diagonal ℤ_p orbifold candidate) PASSES as a
**general** mechanism, not a p=3-specific one.
**Go/no-go:** P4 stays ALIVE for a future round attempting Step 2
(triality-correlation / pairing rule). This round does NOT complete P4 and
does NOT resolve OB1.
**Independent skeptic pass (2026-09-06, strict Context Asymmetry): `CONFIRMED-REAL`** -- see "Update" section below.

---

## What was computed (T1–T5, all exact — sympy, roots of unity, matrix
identities, no floating point in the load-bearing checks)

`c167_holonomy_descent_check.py`, full output in `results_c167.json` /
`run_output.txt`.

**T5 — freeness.** For every tested p (1,2,3,4,5), ζ_p^k ≠ I for
0<k<p and ζ_p^p = I exactly (sympy `simplify`, exact roots of unity). The
left-ℤ_p action is free for all p≥1, confirming the standard fact used
without further proof in claim.md sub-claim 1.

**T1 (general-p, done FIRST per AOG-5) — symbolic closed form.** For
symbolic positive-integer `p`, `Ad(ζ_p)` computed directly by conjugation on
the Pauli basis (`ζ_p σ_k ζ_p⁻¹`, `k=1,2,3`) gives, **exactly**:

```
Ad(ζ_p) = [[cos(4π/p),  sin(4π/p), 0],
           [-sin(4π/p), cos(4π/p), 0],
           [0,          0,         1]]
```

— a rotation by angle **−4π/p** about the axis fixed by ζ_p (the sign is an
orientation/handedness artifact of this conjugation convention, checked
explicitly and irrelevant to whether the matrix equals the identity). This
symbolic form was verified to match a hand-derived expectation exactly
(`matches_expected_form_up_to_orientation_sign: true`).

**Ad(ζ_p) = Id ⟺ 4π/p ≡ 0 (mod 2π) ⟺ p | 2 ⟺ p ∈ {1,2}.** This is a closed
algebraic condition, derived once, for ALL p — not fitted to p=3.

**T1 (concrete sweep p=1,2,3,4,5):**

| p | ζ_p central (±I)? | Ad(ζ_p) = Id? | rotation angle (numeric, rad) | π₁(L(p,1)) |
|---|---|---|---|---|
| 1 | — (ζ_1=I, no quotient) | **True** | — | 0 |
| 2 | **True** (ζ_2=−I) | **True** | — | ℤ₂ |
| 3 | False | **False** | −2.0944 (= −4π/3, i.e. 2π/3 mod 2π) | ℤ₃ |
| 4 | False | **False** | −3.1416 (= −π exactly) | ℤ₄ |
| 5 | False | **False** | −2.5133 (= −4π/5) | ℤ₅ |

**The asymmetry holds for p=3, 4, AND 5 — not only p=3.** This is the
AOG-5-mandated result: the mechanism is tied to non-centrality of ζ_p in
SU(2), a structural fact about SU(2)'s center ({±I}, order 2), not to any
property special to p=3 or to N_gen=3. p=2 is correctly the ONE degenerate
case (ζ_2=−I is central), exactly as the closed-form condition predicts —
this is `HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P`, not
`HOLONOMY-ASYMMETRY-ONLY-AT-P3`. Kill condition K2 (claim.md) did NOT fire.

**T2 — exact matrix-identity verification of the transformation laws**, at a
non-diagonal sample point `g₀` (rotation by 60° about the x-axis, NOT the
identity, NOT on the ζ_p torus), for each generator `A ∈ {σ1,σ2,σ3}` and
each p∈{2,3,4,5}:

**CORRECTED 2026-09-06, independent skeptic pass:** the word "adversarial"
above overclaims what T2 actually establishes. The skeptic's own from-
scratch derivation showed both transformation-law identities
(`(L_ζ)_*X_A(g₀)=X_A(ζg₀)` and `(L_ζ)_*Y_A(g₀)=Y_{Ad(ζ)A}(ζg₀)`) reduce to
associativity of matrix multiplication and hold for ANY `g₀`, not only a
specially-chosen non-diagonal one -- so T2 is a correctness sanity check on
the code's own bookkeeping (confirming the left/right-invariant field
definitions are implemented consistently), not an independent falsification
test capable of catching a wrong `Ad(ζ)` value. **The actual load-bearing,
non-tautological computation is T1** (the `Ad(ζ_p)` matrix itself, verified
in Point 1 below) -- T2 corroborates that T1's `Ad(ζ)` is being APPLIED
correctly inside the transformation law, but does not independently confirm
`Ad(ζ)`'s VALUE. This narrows, but does not remove, T2's evidentiary role;
the round's central claim rests on T1, which the skeptic independently
re-derived by hand and confirmed exactly (see "Update" section below).

- `(L_ζ)_* X_A(g₀) = X_A(ζg₀)` **exactly**, for every A, every tested p
  (left-invariant frame: no twist). 12/12 checks pass.
- `(L_ζ)_* Y_A(g₀) = Y_{Ad(ζ)A}(ζg₀)` **exactly**, for every A, every tested
  p (right-invariant frame: Ad-twisted, matching the SAME Ad(ζ) computed
  independently in T1). 12/12 checks pass.

This is the load-bearing verification: it confirms, as an exact matrix
identity (not an appeal to the general Lie-theory argument alone), that the
left-invariant frame descends untwisted while the right-invariant frame
descends with precisely the Ad(ζ)-twist claimed — on a concrete, adversarial
point, not just at the identity where many such identities degenerate
trivially.

**T3 — edge cases p=1, p=2.** p=1 (no real quotient) gives Ad=Id trivially,
sanity-confirmed. **p=2 is the case most at risk of being mishandled:** ζ_2
= −I is central, so BOTH connections give trivial holonomy at p=2 — the
diagonal-ℤ_p mechanism gives **no asymmetry at p=2**, and this is not a
computational accident but the direct consequence of −I being the (unique
nontrivial) central element of SU(2). Any future round must not silently
extend the "asymmetry confirmed" language to p=2.

**T4 — π₁.** π₁(L(p,1)) = ℤ_p for p≥2 (standard, cited, not re-derived),
vs. π₁(S³)=0. This is exactly the precondition round72/E7's H1b proof used
("S³ is simply connected... no monodromy obstruction") — removed for p≥2 in
general, but the removal is CONSEQUENCE-FREE at p=2 (Ad(ζ_2)=Id means the
holonomy group happens to act trivially on su(2) even though π₁≠0) and
CONSEQUENCE-BEARING at p≥3.

**Structure-constant cross-check (Step 5, not load-bearing):** the abstract
`ad(Z₃)` generator from round72/E7's own `[Zᵢ,Zⱼ]=c·εᵢⱼₖZₖ` convention
(c=2) has the same qualitative shape (antisymmetric, fixes the quotient
axis) as the concrete `Ad(ζ)` computed here — consistent, not independently
informative (the abstract convention alone cannot fix group-level
periodicity, as noted in claim.md and the script).

---

## Well-posedness subtlety (C132's "ι maps left-cosets to right-cosets") — addressed, not assumed

C132 flagged that it was unclear, prior to computation, whether the failure
of the right-invariant frame to descend was a genuine failure, or whether it
secretly re-describes a well-defined frame on an orientation-reversed lens
space `L(p,p−1)≅L(p,1)`.

**Resolution:** the T2 computation above answers the question directly and
unambiguously, without invoking the inversion map `ι` at all. It computes,
as an exact matrix identity, how the right-invariant frame transforms under
the SAME left-translation map `L_ζ` that defines the quotient the round
specified — not under some other (right-translation, or ι-conjugated)
action that would correspond to a different quotient. Because `(L_ζ)_*
Y_A(g₀) = Y_{Ad(ζ)A}(ζg₀)` is a closed, single-valued formula (not two
candidate answers), there is no remaining ambiguity about which lens space
or which orientation is in play for THIS question: on the specific manifold
`L(p,1)=S³/(ℤ_p acting by left translation)`, the right-invariant frame's
holonomy is `Ad(ζ_p)`, period. The `ι`/orientation-reversal question C132
raised is a genuine, separate question (whether a DIFFERENT, ι-related
construction gives an equivalent description) but it does not bear on, and
does not leave open, the specific holonomy-descent question this round was
scoped to answer. Kill condition K5 did NOT fire.

**Not resolved by this round (explicitly, so it isn't silently claimed):**
whether relating t=0↔t=1 (which round72 shows corresponds to a sign flip of
the torsion, `T⁰=−[X,Y]` vs `T¹=+[X,Y]`) via inversion `ι(g)=g⁻¹` is itself
compatible with staying on the SAME quotient `L(p,1)`, or whether it moves
to `L(p,p−1)`. This is a real, separate structural question for a future
round if Step 2 (pairing) is attempted, since Step 2 needs to relate the
t=0 and t=1 sectors on a single consistent quotient manifold.

---

## Spin structure caveat (new finding this round, not in C132's original P4 sketch)

`H¹(L(p,1);ℤ₂) = Hom(ℤ_p,ℤ₂)`, which is **ℤ₂ for p even, 0 for p odd**
(standard fact about lens spaces, cited — not re-derived here). This means:

- **p odd (3, 5):** unique spin structure. The trivial-vs-Ad(ζ)-twisted
  holonomy computed above is unambiguous with respect to spin structure
  choice.
- **p even (2, 4):** TWO inequivalent spin structures exist. The
  computation above is about the FRAME BUNDLE (SO(3)) holonomy, which is
  spin-structure-independent; but which SPIN lift (element of Spin(3)=SU(2)
  covering the computed SO(3) holonomy) corresponds to "the" spin structure
  induced by the trivially-descending left-invariant frame is NOT
  determined by this round's computation and is flagged as an open point
  for p even specifically. This does not affect the p=3,5 (odd) rows of the
  table, which are the ones directly relevant if a future round wants to
  avoid this ambiguity entirely.

This caveat was NOT anticipated in C132's original P4 sketch (which
mentioned `H¹(L(3,1);ℤ₂)=0` only for the odd case it was considering) —
worth flagging explicitly because the sweep this round's AOG-5 discipline
requires (p even included) surfaces it, where a p=3-only round would not
have.

---

## Kill Analysis (Perelman/OSA discipline)

**What this result kills:** the hypothesis that the diagonal-ℤ_p
holonomy-descent mechanism is available ONLY at p=3 (which would have been
the red flag pattern AOG-5 exists to catch — "choosing 3 because N_gen=3").
That specific failure mode is now excluded: the mechanism is general for
all noncentral ℤ_p (p≥3), tied to a structural fact about SU(2)'s center,
not to 3 specifically.

**What this result does NOT kill / leaves fully open:**
1. Whether this holonomy fact translates into an actual change in
   `dim ker D^t` on the quotient (C132's own stated Step-1 measurable
   outcome) — NOT computed this round (see "What this does NOT mean" #2 in
   claim.md).
2. Step 2 — the triality-correlation/pairing construction — entirely
   unattempted, per the task's own scoping instruction.
3. The p-even spin-structure ambiguity (new finding above).
4. Whether the ι/orientation-reversal question matters for Step 2's
   pairing construction (flagged, not resolved).

**Relaxation Map (if a future round needs to narrow further):**
- Remove: nothing needs removing — the general-p result is the strongest
  form of the claim and it held.
- Weaken: restrict to p odd (3,5,7,...) to sidestep the spin-structure
  ambiguity entirely, if Step 2 turns out to need a unique spin structure.
- Replace: none needed at this stage.

---

## What this does NOT mean (repeating claim.md, now confirmed post-hoc, not weakened by results)

1. Does NOT establish that this asymmetry is the same object as, or feeds
   into, any triality-correlation / generation-pairing mechanism (P4 Step
   2) — untouched this round, by design.
2. Does NOT establish that a Dirac zero mode actually disappears at t=1 on
   L(p,1) — this round tested the CONNECTION/FRAME holonomy, not
   `dim ker D^t` on the quotient.
3. Does NOT resolve which spin structure the trivially-descending
   left-invariant frame picks out for p even (new caveat, see above).
4. Does NOT constitute evidence for p=3 specifically — the result is
   general across p≥3, which is evidence for a topological MECHANISM, not
   for N_gen=3. Any future round citing this result for N_gen=3 must
   additionally explain why p=3 (not p=4 or p=5) is the physically relevant
   choice — that is a SEPARATE, unaddressed question (this round's honest
   scope boundary, restated from claim.md).
5. Does NOT complete OB1 — this is Step 1 of a multi-round investment C132
   itself flagged for ANY new OB1 construction. OB1 remains
   `PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT` at the project level unless
   and until a future round's Step 2 (and the Dirac-kernel computation)
   produces something that meets that bar; this round's result alone does
   not reopen OB1.

---

## Verification substrate (FL Step 2a, abbreviated)

- Environment: sympy (already a project dependency, used identically to
  round72/E7's own script), no new dependencies.
- All load-bearing checks (`Ad_is_identity`, T2's matrix identities, T5
  freeness) are EXACT (sympy `simplify` to zero/identity), not
  floating-point tolerance checks. The only floating-point values in the
  record (`rotation_angle_about_z_numeric_radians_if_nontrivial`) are
  explicitly marked non-load-bearing, for human-readable reporting only.
- Script and full JSON output committed to this experiment folder for
  reproducibility (`c167_holonomy_descent_check.py`, `results_c167.json`,
  `run_output.txt`).
- READY verdict: no blocked-infrastructure or untrusted-environment issue
  encountered.

---

## Floor–Ceiling Interval (FL Step 4a) — not applicable, reasoned explicitly rather than skipped silently

This gate asks whether a METRIC being compared to a threshold has room to
move (floor = mechanism-removed null, ceiling = privileged-access optimum).
This round's central result (`Ad(ζ_p) = Id` or not) is not a metric with a
threshold — it is an exact, closed-form algebraic fact (an element of SO(3)
either equals the identity matrix or it does not), verified two independent
ways that serve the SAME role floor/ceiling serve for a statistical result:

- **Floor-equivalent (mechanism removed):** p=1 (no quotient at all) and
  p=2 (ζ central, quotient exists but the specific mechanism — non-
  centrality — is absent) both give `Ad=Id` exactly, as the theory predicts.
  If the code had a bug that made EVERYTHING report `Ad=Id` regardless of
  input, this would be indistinguishable from the true floor — but it isn't:
  p=3,4,5 give `Ad≠Id`, so the check has room to fail and didn't uniformly
  pass.
- **Ceiling-equivalent (independent derivation):** the general symbolic
  closed form (`Ad(ζ_p)` for symbolic p, matching the hand-derived
  expectation exactly) is a SEPARATE derivation from the concrete p=3,4,5
  matrix evaluations — they agree, which plays the ceiling role of "does an
  independently-obtained answer confirm the same result," not a privileged-
  access numerical optimum.

A continuous efficiency ratio is not meaningful for a binary exact identity
check; the discriminating-test criteria (does the test respond, and does it
have room to fail) are satisfied by the p=1,2 vs p=3,4,5 contrast above,
which is why this is reported as reasoned-through rather than silently
skipped.

---

## Recommendation on independent skeptic pass

**Yes, recommend a skeptic pass before this finding is registered
(pearl_registry / OPEN_BLOCKERS), for reasons specific to this round, not
just "the project's convention says so":**

1. This is a from-scratch, multi-round-scoped construction touching OB1's
   central blocker (per the task brief's own framing) — the project's own
   Full-Ladder discipline (Step 8a) makes this mandatory for a PROMOTE-
   direction result, and this result is being reported as PASS.
2. The result rests on a specific convention choice (which conjugation
   direction realizes `Ad`, matrix vs. abstract-structure-constant
   realizations) that this round cross-checked internally (Step 5) but has
   not been checked by a second, differently-primed reader — exactly the
   kind of self-consistency-only verification the Context Asymmetry Rule
   exists to catch.
3. The general-p closed form (`Ad(ζ_p)=Id ⟺ p|2`) is the load-bearing
   claim for the AOG-5 anti-circularity argument; if this closed form
   contains a sign or off-by-factor-of-2 error a skeptic could catch (e.g.
   the double-cover angle-doubling factor), the "general mechanism, not
   p=3-specific" conclusion could silently flip.
4. The spin-structure-for-p-even caveat is a new finding this round did not
   originally anticipate needing — a sign that the surrounding claim space
   is not yet fully mapped, which is exactly when an independent
   falsification pass earns its cost.

I have NOT run that skeptic pass myself this round (out of scope per the
task's own instruction to report back rather than continue the FL pipeline
autonomously) — flagging it as the explicit next action for whoever picks
this up, per FL Step 8a's Context Asymmetry Rule (skeptic should receive
`claim.md` + this script + `results_c167.json` only, NOT this decision.md's
own reasoning chain).

---

## Update -- independent context-blind skeptic pass (orchestrating
   session, 2026-09-06), strict Context Asymmetry (claim.md + script +
   results_c167.json ONLY, decision.md withheld per the round's own
   recommendation), verdict CONFIRMED-REAL with minor WEAKENED markers

**Verdict: `CONFIRMED-REAL`.** The load-bearing claim -- `Ad(ζ_p)=Id` iff
`p∈{1,2}`, rotation by `4π/p` for `p≥3` -- is mathematically sound. The
skeptic independently re-derived the `SU(2)→SO(3)` angle-doubling factor
by hand from scratch (`ζσ_1ζ^{-1}=cos(2θ)σ_1-sin(2θ)σ_2`, etc., for
`ζ=diag(e^{iθ},e^{-iθ})`) and confirmed the code's `4π/p` (i.e. `2×2π/p`)
matches exactly -- the specific "off-by-factor-of-2" failure mode flagged
as a risk in Section "Recommendation" above does NOT occur.

**Two concerns raised, both addressed:**

1. **A real, non-load-bearing code bug found and fixed.** The skeptic
   found `results_c167.json`'s `zeta_p_is_central_(+-I)` field reported
   `false` for BOTH p=1 and p=2 (should be `true` for both, since
   `ζ_1=I` and `ζ_2=-I` are both central in `SU(2)`). Root cause: the
   `is_identity()` helper was applied to an already-subtracted matrix
   (`is_identity(z - eye(2))` tests `z==2I`, never true), instead of a
   direct zero-matrix comparison. **Fixed**
   (`c167_holonomy_descent_check.py`, `z_is_central` now uses
   `simplify(z-eye(2))==zeros` / `simplify(z+eye(2))==zeros` directly),
   re-ran, confirmed `zeta_p_is_central` now correctly reads
   `[true,true,false,false,false]` for p=[1,2,3,4,5], matching the
   skeptic's own hand computation exactly. **This bug never affected the
   verdict**: `Ad_is_identity` (the field the verdict logic actually
   uses) is computed independently, directly on the 3x3 `Ad` matrix, and
   was already correct throughout.
2. **The "adversarial sample point" characterization in T2 (above)
   overclaimed** -- corrected in place (see the inline correction to the
   T2 section above): the transformation-law identities T2 checks reduce
   to matrix-multiplication associativity and hold for ANY sample point,
   not a specially-adversarial one. T2 remains valid as an implementation-
   consistency check, but T1 (the `Ad(ζ_p)` computation itself,
   independently re-derived by the skeptic) is what actually carries the
   claim's evidentiary weight.

**Also independently confirmed by the skeptic, no issues found:** freeness
(`ζ_p^k≠I` for `0<k<p`) verified by direct hand computation; the p=5
symbolic `Ad_zeta_matrix` entries (involving `(-1)^{1/5}`-type expressions)
confirmed to be genuine sympy symbolic-root artifacts of a real, orthogonal
rotation matrix, not a computation error (numerically evaluated and
matched against the expected `4π/5` angle); p=2's trivial holonomy
confirmed as a real, non-vacuous consequence of `-I`'s centrality, not a
degenerate "anything passes" case.

**Net effect: no change to the verdict** (`HOLONOMY-ASYMMETRY-CONFIRMED-
ALL-P` stands). One real cosmetic bug fixed (non-load-bearing); one
overclaimed characterization (T2's "adversarial" framing) corrected in
place; the actual load-bearing computation (T1) independently re-derived
and confirmed exact.

---

## Status

`experiments/20260906-c167-p4-diagonal-z3-orbifold/` — Step 1 of P4
COMPLETE, verdict `HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P`, PASS, general
mechanism (not p=3-specific), independent skeptic pass CONFIRMED-REAL
(minor corrections applied above). Registry files (`OPEN_BLOCKERS.md`,
`pearl_registry/INDEX.md`, `null_results/INDEX.md`, `CLAIM_LEDGER.yaml`)
deliberately NOT yet touched by this experiment round itself; committed
and registered by the orchestrating session per its own standing
convention.
