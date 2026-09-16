---
# C193 — is `spin_lift` a Lie-algebra homomorphism? (title corrected after skeptic review — see Correction 2: it is an ANTI-homomorphism, and it narrows, not closes, OB11(ii)'s "J remains unchecked" gap)

**Date:** 2026-09-09
**FL tier:** [x] Full (research claim touching OB11(ii), per project CLAUDE.md)
**Question type:** [x] descriptive (does a specific algebraic identity hold —
not a causal or predictive claim)

---

## Priority context — why this round, right now

Session-level priority survey (this round, before computing anything):
`OB1`/H1c is `PARKED`, exhaustively closed for every internally-testable
`P5` reading (C191, today) and independently cross-checked (C192, today).
`OB14` is `BLOCKED-INTERNAL`, independently reconfirmed FOUR separate ways
(C142, C164/C165, C166, C175) — no internally-buildable candidate remains,
only external (Tom Lawrence, `DO NOT INITIATE CONTACT`) or new-construction
(high AOG-5 risk) routes are open. `OB13`'s residual ("Family C") needs
"round95's missing S⁶↔S³ link" — not concretely scoped as a next
computation. `OB4` has a screening gate (C150) but no live proposal to
screen. **`OB11(ii)` is the one open blocker with a concretely scoped,
unblocked next step**, per `C149` (2026-09-04): *"`J` remains unchecked...
it is a one-line check once `J` is in hand, and it is a prerequisite [for
resuming OB11(ii)'s planned transport test]."*

## Why this round does NOT build `J` geometrically

Building `J` (the `S⁶=G₂/SU(3)` nearly-Kähler almost-complex structure) as
an explicit `so(6)` bivector in round59's own 6-index convention requires
cross-referencing `G96`'s octonion structure tensor's index/basis ordering
against round59's `NOMIZU`/`ADNU` convention — real, nontrivial work with
genuine risk of a NEW convention bug (exactly this project's most common
failure mode, per `patterns.md`/this session's own memory). **Cheapest
Differentiating Test Protocol** (`falsification-ladder.md`): before paying
that cost, check whether the answer is already DECIDED by a cheaper,
more general fact — `spin_lift`'s own algebraic structure — that needs no
geometric construction at all.

## Correction, added after running (never-delete-only-annotate — the
original pre-registered claim below is left UNEDITED)

The identity as pre-registered below (coefficient `+1`) **failed** on every
generic random pair tested (`Q2`) and on `34/48` `NOMIZU`/`ADNU` pairs
(`Q3`). Diagnosed (`diag_scale.py`), not assumed: the entrywise ratio
`lhs/rhs` on every nonzero-`rhs` entry sampled was **exactly `−1`**
(`sympy`-exact), the same shape as this session's own `C192` finding
(`comm(L1,L2)=−2·L3`) — a single, consistent, hand-derivable normalization
constant, not a structural break. Hand-derivation confirms it: the standard
`(1/4)Σ_{a,b}X_ab[e_a,e_b]` bivector formula reduces to
`Σ_{a<b}X_ab·e_ae_b` (no extra `1/2`), while `spin_lift` as CODED uses
`coeff·(1/2)·E[a]E[b]` per term — i.e. `spin_lift(X) = (1/2)ρ(X)` for the
standard homomorphism-normalized `ρ`. Since `[½ρ(X),½ρ(Y)]=¼ρ([X,Y]) =
½·(½ρ([X,Y])) = ½·spin_lift([X,Y])`... **[a genuine sign, not the `1/2`
scale, is what the computation actually found — the by-hand derivation
above predicts a further factor of `1/2`, which does NOT match the
computed exact `−1`; the by-hand scale derivation is flagged here as
UNRESOLVED and not to be trusted over the computed result — see
`decision.md` § Skeptic Concerns for how this discrepancy is scoped.]**
The corrected, verified identity is `[spin_lift(X,E), spin_lift(Y,E)] =
−spin_lift([X,Y]_so6, E)`, confirmed on `5/5` generic random pairs and
`48/48` `NOMIZU`/`ADNU` pairs (`run_output.txt`). **The corollary about `J`
is unaffected by this correction**: the argument only needs
`[J,ad(ν_a)]_so6=0 ⟹ spin_lift(0)=0` (times any constant, sign included),
which holds regardless of the exact proportionality constant.

## Falsifiable claim (pre-registered, ORIGINAL WORDING — see Correction above)

`round59_route_a_independent.py`'s `spin_lift` function — `spin_lift(X,E) =
Σ_{(a,b)∈X} X_ab · (1/2)·E[a]·E[b]`, for `X` a sparse `so(6)` bivector term
list, `E` the Clifford generators — is a genuine **Lie-algebra
homomorphism** `so(6)→spin(6)` (standard Clifford-algebra representation
theory, but not previously verified computationally IN this project's own
specific 8-dim `Λ•L'` realization of `Σ`, which is an unusual presentation
— abstract exterior algebra on a Lagrangian subspace, not the more common
tensor/Kronecker-product gamma-matrix construction this project uses
elsewhere, e.g. `so4xso4_branching.py`):

```
[spin_lift(X,E), spin_lift(Y,E)]  =  spin_lift([X,Y]_so6, E)
```

for `X`, `Y` ANY real antisymmetric `6×6` matrices (not just `NOMIZU`/
`ADNU`), where `[X,Y]_so6 = XY−YX` is the ordinary matrix commutator (also
antisymmetric, hence itself a valid `so(6)` element / term list).

**Corollary this round draws IF the claim holds (stated before computing,
not fitted after):** since `SU(3)` is, by definition, the isotropy
subgroup stabilizing the near-Kähler almost-complex structure `J` on
`S⁶=G₂/SU(3)` — i.e. `[J, ad(ν_a)|_m]=0` for `a=1..8` **at the vector
(`so(6)`) level**, a standard structural fact `[DOCS]`, not new geometric
content — the homomorphism property forces `[spin_lift(J,E),
RHO[a]]=spin_lift([J,ad(ν_a)],E)=spin_lift(0,E)=0` for all `a`, **without
ever constructing `J`'s explicit 6-index form**. This would close C149's
flagged prerequisite by a structural argument, the same shape as `γ`'s
own "forced by `spin_lift` parity" finding in C149 — checked here as a
DIFFERENT, more general mechanism (bracket-preservation, not
parity-preservation), not assumed to be the same fact.

## Kill criterion

**REJECTED** if `[spin_lift(X,E), spin_lift(Y,E)] ≠ spin_lift([X,Y]_so6,E)`
for ANY tested pair of antisymmetric `X`, `Y` with `[X,Y]≠0` (a degenerate
commuting pair, where both sides are trivially zero, is uninformative and
does not count as a pass). A failure would mean `spin_lift`, AS CODED in
this specific `Λ•L'` presentation, is not a clean Lie homomorphism — this
would be a significant, previously-unknown finding, since `spin_lift` is
used throughout `C139`/`C141`/`C142`/`C146`/`C149`/`C162`/`C164`/`C165` to
build every twisted-Dirac and su(3)-generator operator in this whole
sub-line of the project, and NONE of those rounds tested this general
property directly (each only tested SPECIFIC inputs — `NOMIZU`, `ADNU` —
never the abstract bracket-preservation identity on generic input).

## Positive/negative control

**Positive control (reproduces known structure):** `X=NOMIZU[i]`,
`Y=ADNU[a]` for a specific `(i,a)` pair — the identity should hold here
too (a special case), and can be cross-checked against the fact that
`ADNU` is DEFINED as `ad(ν_a)` restricted to `m`, i.e. `NOMIZU` should
transform as a vector under `ADNU`'s bracket, giving an independently
meaningful (not just algebraically forced) check.

**Negative control (must discriminate):** if `spin_lift` were coded with a
bug (e.g. a missing sign, wrong index in the `(1/2)` convention, or
applied per-listed-term without correctly encoding the implicit
antisymmetric completion — see § Method derivation below), the identity
would fail for GENERIC `X`, `Y` even though it might accidentally hold for
special low-rank cases like `NOMIZU`/`ADNU`. Testing multiple GENERIC
(non-`NOMIZU`/`ADNU`) random pairs is the actual discriminating test, not
the positive control alone.

## Correction 2, added after context-blind skeptic review (Step 8a) — verdict WEAKENED, all 5 substantive concerns accepted

1. **[HIGH] The `J`-corollary is an EXISTENCE statement, not a closure.**
   The corollary shows SOME `J`-in-round59's-basis would have
   `spin_lift(J)` automatically commuting with `RHO[a]` — it does not
   construct that `J`, does not produce `spin_lift(J)` as a matrix, and
   nothing from this round enters the actual planned transport-test code.
   `C149`'s "`J` remains unchecked" is **narrowed** ("`J`'s equivariance
   is guaranteed once built") — **NOT closed** operationally. Same
   non-substantive character as `γ`'s own "forced by parity" finding in
   `C149` — flagged as a real risk in this file BEFORE the skeptic pass
   (§ Falsifiable claim's corollary, above), and the skeptic pass confirmed
   the risk was realized, not merely hypothetical.
2. **[HIGH] "Homomorphism up to a sign" is imprecise — it is a genuine
   ANTI-homomorphism**, i.e. `spin_lift: so(6)→spin(6)` with
   `[spin_lift(X),spin_lift(Y)]=−spin_lift([X,Y])`. Concretely confirmed
   (`Q4b`, added after this concern): `RHO[a]=spin_lift(ADNU[a])` satisfies
   the **flipped** `su(3)` structure constants
   (`[RHO[a],RHO[b]]=−spin_lift([ADNU[a],ADNU[b]])`), not the standard
   ones — `28/28` non-degenerate generator pairs, exact. **Practical
   consequence, not yet acted on:** any future round reusing `spin_lift`'s
   output as if it carried STANDARD `su(3)` structure constants (e.g. for
   a Casimir-sign, weight-label, or orientation argument) should be
   audited against this anti-homomorphism fact — flagged here, not
   silently absorbed. Candidate `pearl_registry` entry, see `decision.md`.
3. **[HIGH] The `−1` vs. `+1/2` sign/scale discrepancy (§ Correction,
   above) remains genuinely UNRESOLVED**, and per the skeptic: this is
   itself informative — nobody currently has a first-principles derivation
   of `spin_lift`'s exact normalization, meaning the computation is
   trusted but the INTERPRETATION of what `spin_lift` computes is not
   fully understood. Does not affect THIS round's corollary (any
   consistent constant times zero is zero) but should not be reused
   elsewhere without resolving it first.
4. **[MEDIUM] The `SU(3)`-stabilizes-`J` premise is coordinate-free — it
   does not identify which antisymmetric `6×6` matrix, IN ROUND59'S OWN
   `ADNU`/`NOMIZU` BASIS, represents `J`.** Nearly-Kähler `S⁶` admits both
   `J` and `−J`; which orientation the planned transport test would
   actually need is not determined here. The strongest honest reading of
   the corollary is "*there exists* a `J`-in-this-basis with the claimed
   property," not "`J`'s equivariance is verified."
5. **[MEDIUM] `Q4`'s sign match is NOT fully independent of `Q2`'s `−1`**
   — both plausibly trace to the same underlying convention in round59's
   `ADNU`/`NOMIZU` indexing. `Q4`'s own check label is corrected in the
   script to no longer claim independence.

**What survives at full strength, unweakened:** the identity
`[spin_lift(X),spin_lift(Y)]=−spin_lift([X,Y]_so6)` itself — exact,
`5/5` generic pairs + `48/48` `NOMIZU`/`ADNU` pairs + `28/28`
`ADNU`-generator pairs (`Q4b`), a real, previously-untested, non-trivial
algebraic fact about `spin_lift` as coded. **What this round should be
reported as:** verifying `spin_lift`'s anti-homomorphism property (real,
useful, reusable finding with a flagged downstream-audit consequence) —
NOT as closing OB11(ii)'s `J`-prerequisite.

## What this round does NOT establish

- Does not construct `J` explicitly, geometrically, or verify it against
  `G96`'s octonion tensor — only cites `SU(3)`-stabilizes-`J` as a standard
  structural fact `[DOCS]`.
- Does not run OB11(ii)'s actual planned transport step (transporting `D`,
  `J`, `γ`, `B-L` through `U`) — only closes the flagged PREREQUISITE
  (`J`'s equivariance) via a structural argument, not the transport itself.
- Does not change `N_gen=3`'s `CONDITIONAL` status.
- If the homomorphism claim is REJECTED (kill criterion fires), this does
  NOT retroactively invalidate `C146`'s `D_Σ`-equivariance finding (which
  was checked directly on `D_Σ`, not via this general property) — it would
  mean the general property doesn't hold as coded, a narrower but still
  significant finding about `spin_lift` itself.

## Reproduction

```
cd experiments/20260909-c193-ob11ii-spin-lift-homomorphism-closes-j-gap
python c193_spin_lift_homomorphism.py
```
