# C194 Decision — REJECT the one candidate tried; the OVERCLAIM in an earlier draft of this decision was itself caught and corrected by a context-blind skeptic pass (2026-09-10, see §2a).

**Date:** 2026-09-10 (revised same day after skeptic pass)
**Verdict:** **REJECT** (the specific claim: `U(θ,φ,ψ)·v` gives Tom's four
k=0 objects a non-constant Hopf-coordinate form). `6 of 6` checks pass —
the two checks that establish this negative directly are B1/B2. Checks
C1/C2/D1 establish a narrower, correctly-scoped fact than the first draft of
this file claimed (see §2a) — they show constants lie in `D₀`'s kernel, NOT
that nothing else does. Exact symbolic arithmetic + 30-digit numeric
cross-check where symbolic `simplify` under-collapsed mixed
exponential/half-angle forms.

All numbers trace to `c194_hopf_zero_mode_check.py` and `run_output.txt`.

**Revision note:** a context-blind physics skeptic pass (prompted by
drafting the reply to Tom) found that §2's original argument — "a derivative
applied to a constant is zero, therefore the kernel is exactly the
constants" — is a non-sequitur: `X_0^R = 2∂/∂ψ` alone is also a pure
first-derivative operator, and its own kernel (all functions independent of
`ψ`) is far larger than the constants. C1/C2 only establish
`constants ⊆ ker(D₀)`; the reverse inclusion needs a different argument,
given below. §2, §3, §4, §5, §6 are corrected accordingly. This is
recorded, not hidden — see `~/.claude/rules/falsification-ladder.md` §
Hindsight Distortion Gap Heuristic.

---

## 0. Honest process note

The core computation (checks A1, B1, B2) was first run as an exploratory
scratch script mid-conversation, *before* this experiment folder existed —
in direct response to the previous turn's plan proposing `U(θ,φ,ψ)·v` as
"very likely correct." That proposal was **wrong**, caught by direct
computation within the same turn, not asserted and later found false. This
folder formalizes and cleanly re-runs the same checks from a fresh script
(not a copy of scratch output) so the result is reproducible and not merely
recalled — see `~/.claude/rules/falsification-ladder.md` § Hindsight
Distortion Gap Heuristic: same-session correction is the trustworthy case,
recorded here at zero gap rather than reconstructed later.

---

## 1. What was tested, and what broke

The candidate: multiply the already-verified Euler/Hopf `SU(2)` matrix
`U(θ,φ,ψ)` (unitary, `det=1`, both checked in `C184`) by a constant 2-vector
`v`, hoping this gives Tom's k=0 objects a genuine, non-constant functional
form in `(θ,φ,ψ)`.

**Check A1** re-confirms `U(θ,φ,ψ)` is exactly the "quaternionic basis" map
`x₀·I + x₁·(iσ₁) + x₂·(iσ₂) + x₃·(iσ₃)` with the Hopf substitution plugged
in — i.e. `U`'s own matrix *entries* are linear (degree-1) functions of the
ambient coordinates `(x₀,x₁,x₂,x₃)`.

**Check D1** makes this explicit and general: `U`'s entries are degree-1
homogeneous polynomials in `(x₀..x₃)`, uniformly, not just "by coincidence"
at one entry.

**Consequence, checks B1/B2:** `U·v`, for ANY constant `v`, is therefore
automatically a degree-1 object — never degree-0. Concretely, `U·(1,0)ᵀ`
computed in Hopf coordinates (B1, 30-digit numeric match) turns out to be
**exactly** (up to an overall sign, checked symbolically, B2) `C184c`'s own
already-published `D₀=+3` eigenspinor at the **k=1** level
(`run_output_c.txt`, "F" section) — not a new object, and specifically not
the k=0 zero mode. This is the same "dimension trap" `C179` §2 already named
for a different pair (vector vs spinor, both dimension 4) — here it recurs
between k=1 and k=0.

---

## 2. What C1/C2 actually establish, and what they do not

Checks C1/C2 test the actual operator directly, independent of any specific
candidate. `C188`'s own closed-form Euler-angle generators

```
X_0^R = 2 ∂/∂ψ
X_1^R = 2cos(ψ) ∂/∂θ + 2sin(ψ)/sin(θ) ∂/∂φ − 2sin(ψ)/tan(θ) ∂/∂ψ
X_2^R = −2sin(ψ) ∂/∂θ + 2cos(ψ)/sin(θ) ∂/∂φ − 2cos(ψ)/tan(θ) ∂/∂ψ
```

are **pure first-derivative operators** — no zeroth-order (additive) term
anywhere (C1, checked by applying each to the constant `1` and finding `0`).
Consequently `D₀ = −i Σₐ σₐ Xₐᴿ` annihilates **every** constant pair `(a,b)`
identically, symbolically, with `a,b` left as free symbols, not merely
checked at one numeric point (C2).

**This establishes ONE inclusion only: `constants ⊆ ker(D₀)`.** It does
**not**, by itself, establish the reverse inclusion (`ker(D₀) ⊆ constants`),
and the first draft of this file wrongly treated it as if it did. The
counterexample is inside this file's own notation: `X_0^R = 2∂/∂ψ` alone is
also a pure first-derivative operator, and its kernel is every function
independent of `ψ` — nowhere near "just the constants." A pure-derivative
operator's kernel size is not determined by the fact that it is a
derivative; it depends on the specific operator.

## 2a. The actual reason `ker(D₀) = constants` (at the checked levels)

The real argument is representation-theoretic, already established by prior
rounds, not new to this one. `D₀`'s known spectrum, from `C184`'s angular-
momentum coupling (orbital level `k` tensored with the spin-1/2 index) and
independently confirmed level-by-level by `C188`, has two branches:
`λ = −k` and `λ = k+2`, checked exactly for `k=0,1,2,3`
(`C184` §3a: `j_R=0` at `k=1` gives `D₀=+3`, matching `k+2=3`; `j_R=1` gives
`D₀=−1`, matching `−k=−1`; `C188` §3: `λ=0,−1,−2,−3` for `k=0..3` on the
`−k` branch). At `k=0` there is only ONE branch (orbital `j=0` tensored with
spin-1/2 gives total `j=1/2` only — there is no second branch to couple
against, unlike `k≥1`), and it has `λ=0` for the whole 2-dimensional level.
For `k≥1`, `−k≤−1` and `k+2≥3`; neither branch reaches `0`. So `D₀=0` occurs,
among the levels actually checked (`k=0..3`), **only** at `k=0`, where the
level itself is the 2-dimensional space of constants by definition of
"level 0" (the trivial scalar harmonic).

**Scope, stated honestly:** this establishes `ker(D₀) = constants` for the
checked levels `k≤3`, resting on the SAME already-published spectrum values
this project has used elsewhere (`C184`, `C188`) — not on anything newly
computed in checks C1/C2, which establish only the one-directional
inclusion above. Whether the `−k`/`k+2` pattern continues to rule out `D₀=0`
at every `k>3` is inference from the pattern, matching `C188`'s own stated
scope ("does not extend beyond k=3... continuation is inference"), not a
completed proof for all `k`.

---

## 3. What this actually gives the reply — corrected, narrower claim

The honest statement, matching what §2/§2a actually establish (no more):

> Within the specific operator this project has built (`D₀`, the flat,
> left/right-invariant-generator construction used throughout `C184`/`C188`
> — not a Levi-Civita/curved-connection construction, which this project has
> not built for this purpose), the four objects are constant, and the ONE
> candidate tried for making them coordinate-dependent (`U(θ,φ,ψ)·v`) turns
> out to reproduce an already-known `k=1` object instead of supplying new
> `k=0` content. This does **not** establish that no possible local-frame
> convention could give a non-constant expression — only that this operator's
> own zero-eigenspace, checked at `k≤3`, is exactly the constants, and that
> the one natural candidate tried does not escape that.

This **narrows**, rather than confirms as flatly wrong, a specific line in
the already-sent `rev6` letter (*"write the same objects directly in the
Hopf coordinates without using [group] identification, and they pick up the
coordinate frame's own rotation, and stop looking constant"*). The honest
correction is not "that was wrong" but **"that was under-specified — it
depends on which local frame is meant, and I hadn't named one; the
construction this project has built does not supply that frame on its
own."** Calling it flatly wrong, as the first draft of this file did, is
itself an overclaim in the other direction — this round killed one
candidate and established one narrow inclusion, not a general
impossibility. The reply owes Tom this more careful framing, not a
flat retraction.

---

## 4. Kill Analysis

**Killed:** the specific candidate `ψ = U(θ,φ,ψ)·v` as a source of a
non-constant k=0 Hopf expression. Also killed (in the revision): the
overclaim that C1/C2 alone prove `ker(D₀)=constants` — they prove only
`constants ⊆ ker(D₀)`.
**Not killed:** the underlying `D₀` operator, `C184`'s constants themselves,
`C188`'s Euler-angle generators, the representation-theoretic argument in
§2a (which DOES establish `ker(D₀)=constants` at `k≤3`, on different
grounds than first claimed), or the general possibility that SOME
externally-specified local frame convention — possibly a genuinely
different, curved-connection operator rather than `D₀` itself — could give
a non-constant expression. That route is open, not closed, and was never
actually tested here; only ONE flat-frame candidate was.
**Relaxation Map:** the one surviving option is to ask Tom directly which
local-frame convention he means (matching his own letter's own SO(3)-
ambiguity remark), rather than guessing a second candidate construction —
and to be explicit with him that only one candidate, not an exhaustive
search, has been ruled out.

## 5. Floor–Ceiling (Step 4a)

Metric: **how many of the 2 basis solutions of the operator's own `D₀=0`
eigenspace (established as exactly the constants at `k≤3` via §2a's
representation-theoretic argument, not via C1/C2 alone) are genuinely
non-constant functions of `(θ,φ,ψ)`.**

FLOOR (mechanism absent) = `0.0`. Given §2a's result that `ker(D₀)` at
`k≤3` is exactly the 2-dimensional constants, the count of non-constant
solutions within that space is `0` by definition — not by the C1/C2
argument alone, which only shows constants are among them.

CEILING (best case, the counterfactual this round rules out for the ONE
candidate tried) = `2.0`. Both basis vectors of the eigenspace non-constant —
this is what a genuine, frame-dependent zero mode (the kind `C187`'s
vielbein attempt was chasing) would have looked like.

OBSERVED = `0` (check B1/B2: the one candidate actually tried collapses
onto an already-known k=1 object, contributing zero non-constant k=0
solutions).

EFFICIENCY = `(0 − 0) / (2 − 0)` = **`0.0`** for the ONE candidate tested —
this is narrower than the first draft's claim that C1/C2 close off "every
other candidate of this general shape": C1/C2 do not do that; only §2a's
cited spectrum result bounds the space itself, and only B1/B2 actually
tested a candidate.

## 6. What this does NOT establish

- Does NOT mean Tom's request is unanswerable — it means the *specific*
  candidate tried is a dead end, and the real next question is which
  external frame convention to use.
- Does NOT establish that no local-frame convention whatsoever could give a
  non-constant expression — only one candidate (not built from an explicit
  frame/vielbein at all) was tested.
- Does NOT affect `C184`, `C184b`, `C185`, `C188`'s own verdicts.
- Does NOT constitute a submission — must pass a fresh skeptic pass (context-
  blind, claim.md + script only) before anything from this round is quoted
  to Tom, per `integrity.md`'s Submission Gate. (This revision was itself
  produced BY such a pass, 2026-09-10 — see the revision note at the top.)

## 7. Reproduction

```
cd experiments/20260910-c194-s3-hopf-zero-mode-frame-check
python c194_hopf_zero_mode_check.py
```

`6/6`. `ruff check` and `ruff format`: clean.
