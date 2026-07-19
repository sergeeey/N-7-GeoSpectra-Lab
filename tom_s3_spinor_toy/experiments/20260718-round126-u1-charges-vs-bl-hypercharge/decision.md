# Round126 — Decision

**Date:** 2026-07-18
**Verdict:** `NO_INDEPENDENT_EVIDENCE` — the apparent "match" to `B-L`'s 3:1
charge ratio is a **tautological consequence of the scan's own
normalization convention**, not evidence about `su(3)`'s centralizer
structure. Self-corrected after mandatory skeptic review and independent
verification; this is a near-null result, reported honestly rather than
as the "exciting discovery" the first draft initially framed it as.

**Go/no-go:** the physical-identification question round124 flagged
("check the `u(1)×u(1)` charges against `Q`/`Y`/`B-L`") remains
**genuinely open** — this round does NOT close it, and the specific
scan methodology used here cannot close it even in principle. A cleaner
next attempt would need a different approach (see Relaxation Map).

## What the first draft found, and why it was wrong

First draft: scanned all unit-norm combinations `a·gen1+b·gen2` of
round124's 2-dim `su(3)`-centralizer, computed the charge (eigenvalue
magnitude) on `8_v`'s 2-dim singlet subspace and 6-dim triplet subspace,
and found a `θ` where the ratio hits exactly `3` (matching `B-L`'s
`|singlet|:|triplet| = |−1|:|1/3| = 3`), with charges landing on the
*exact* algebraic values `√3/2` (singlet) and `√3/6` (triplet), verified
to machine precision via `scipy.optimize.brentq`. This was initially
presented as a striking, non-trivial coincidence.

**Skeptic review, `WEAKENED`, decisive correction:** the "clean numbers"
are a **forced mathematical identity**, not new information. Because
`centralizer_dim` returns an SVD-orthonormal basis (each generator has
Frobenius norm exactly `√2`, and the two are exactly orthogonal —
`⟨gen1,gen2⟩_F≈8e-17`), any unit-norm combination `a²+b²=1` has
`‖combo‖²_F=2` exactly. Since the triplet block carries the charge with
multiplicity 3 (3 conjugate pairs) and the singlet with multiplicity 1,
Frobenius-norm conservation gives `2q_s²+6q_t²=2`, i.e. `q_s²+3q_t²=1`.
**Imposing any target ratio `r=q_s/q_t` (via `q_s=r·q_t`) forces
`q_t=1/√(r²+3)`, `q_s=r/√(r²+3)` — a closed-form value for *every* `r`,
not a special property of `r=3`.** For `r=3` this happens to simplify to
`√3/2, √3/6`; for `r=1,2,5,10` it gives `1/2,1/2`; `√(4/7),√(1/7)`; etc. —
all equally "clean" in the same algebraic sense. **Verified independently
by me directly** (not just trusting the skeptic's analytical claim,
since that agent lacked Bash access): re-ran the Frobenius-norm
computation myself and confirmed `‖gen1‖_F=‖gen2‖_F=√2` exactly,
orthogonality to `~1e-17`, and the forced-value formula for `r∈{1,2,3,5,10}`
— matches the skeptic's derivation exactly.

**Second, equally important correction:** finding *some* `θ` where
`ratio=3` is not surprising in the first place. `ratio(θ)` is continuous
and spans roughly `[0.077, 38.8]` over the scan (checked: `gen1` alone
gives ratio `≈0.077`, `gen2` alone gives ratio `≈38.8`) — by the
Intermediate Value Theorem, **any** target ratio in this wide range,
including `3`, is guaranteed to be hit somewhere. This is not a discovery
about `B-L` specifically; the same scan would "find a match" for
essentially any other established charge ratio in this project (`B`
alone: ratio `0`; various `Y_R` combinations: ratios in `{0,1,1.5,3,∞}`) —
none of these "hits" carry independent evidential weight without first
establishing that hitting the target ratio is itself non-generic, which
it is not here.

## What survives, honestly

- The **narrow, correct** technical fact: round124's centralizer does
  contain *some* direction with charge ratio exactly 3 between the
  singlet and triplet pieces of `8_v`. This is true, but — per the two
  corrections above — carries essentially no independent evidential
  content: it is guaranteed by IVT (existence) and fully determined by
  Frobenius-norm bookkeeping (the specific values), not a property
  discovered about `su(3)`'s representation content.
- The pre-registered "sign structure" kill criterion (`claim.md`) is, per
  skeptic's finding, **structurally unreachable by this round's own
  code** — `antisym_eigvals_on_subspace` computes eigenvalues via `-M@M`
  (even in `M`), which destroys the sign information needed to check
  relative sign structure between the singlet and triplet blocks. This is
  why the script's own verdict logic correctly never emits
  `PATTERN_MATCH_FOUND` (only the more conservative `RATIO_3_FOUND`) —
  the code was honestly scoped even before this decision's own further
  correction, but the underlying methodology cannot answer the physical-
  identification question regardless.
- The `Y=(B-L)/2` (at `T3R=0`) vs `B-L` ambiguity flagged in the first
  draft is arithmetically correct (verified against G15's own T9 gate:
  singlets `Y=±1/2`, triplets `Y=±1/6`, ratio `3`, identical to `B-L`) —
  but this is now a minor point next to the larger genericity problem.
- The basis-identification gap flagged in `claim.md` (is `8_v` the same
  object as G15's "`S⁶` spinor"?) remains completely unresolved — this
  round's methodology could not have closed it even if the ratio-scan
  approach itself had been sound.

## Kill Analysis

- **What this kills:** the "exact algebraic ratio match" framing as
  evidence for a `B-L`-like physical identification — it was never
  independent evidence to begin with.
- **What this does NOT kill:** round124's own `su(3)⊕u(1)⊕u(1)` finding
  (`Hom=0` for all off-diagonal pairs) — untouched, that result did not
  depend on any ratio-matching argument.
- **What survives as a genuinely scoped next step:** the physical-
  identification question is still open and needs a fundamentally
  different method — see Relaxation Map.

## Relaxation Map

| Option | What it would require |
|---|---|
| Resolve the `8_v` vs G15-"`S⁶` spinor" basis-identification gap directly | Construct an explicit isomorphism (or prove none exists) between round124's octonion-table basis and G14/G15's qubit/Pauli-tensor basis — the prerequisite for ANY literal charge comparison, not attempted in either round |
| Test against a NULL/random-direction baseline instead of a single target ratio | Scan many RANDOMLY chosen established-charge ratios (not just `B-L`'s `3`) against the SAME centralizer and report what fraction "match" by the same criterion — would make the IVT/genericity problem visible as a control, rather than being caught only by skeptic review after the fact |
| Check sign structure properly | Would require an eigenvector-based (not `-M@M`-based) charge extraction preserving the `+iλ`/`−iλ` labeling, plus an EXTERNAL physical labeling of which eigenvector is "quark" vs "antiquark" (not derivable from round124's construction alone) |

## What this does NOT mean

1. Does NOT establish or refute a physical identification of round124's
   centralizer charges with `B-L`, `Y`, or any other established charge —
   genuinely undetermined by this round's methodology.
2. Does NOT affect round124's own `Hom=0` finding or its `CANDIDATE_FOUND`
   status for Gate 1 — untouched.
3. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.

## Standing lesson (this round specifically — a new, distinct failure mode)

**A "found a match" result needs a genericity/baseline check BEFORE
interpretation, not after — and "the numbers came out clean" is not
itself evidence, if the normalization convention forces clean numbers for
every possible target.** This is a sharper, more specific instance of
this project's own `skeptic-triggers.md` Trigger 2 (unexpected success)
and the `pearl_registry` lesson from the prior round125
("generic-intersection-dimension check... apply it before interpreting
any... result as 'just a number'") — extended here from subspace-overlap
dimensions to eigenvalue-ratio scans specifically. **Rule going forward
for this class of check:** before scanning a 1-parameter family for a
target ratio, first compute the achievable RANGE of the ratio and ask
whether the target sits inside a wide, generic range (weak evidence if
found) or requires fine-tuning to a narrow sub-range (stronger evidence).

## Check (reproduces the verification)

```
cd experiments/20260718-round126-u1-charges-vs-bl-hypercharge
python e43_u1_charges_vs_bl_hypercharge.py
```
Expect: a ratio-3 crossing reported with charges near `√3/2, √3/6` — this
reproduces the narrow technical fact, not the (corrected, withdrawn)
"discovery" framing.
```
python -c "import numpy as np; ..." # Frobenius-norm check, see decision.md body
```
Expect: `‖gen1‖_F=‖gen2‖_F=√2` exactly, `⟨gen1,gen2⟩_F≈0`, confirming the
tautology derivation.
