# C157 — chirality balance of invariant spinors on flag manifolds

**Question type (EstimandOps L0): DESCRIPTIVE.** Tier: FL Full.
**Mandate gate (user-imposed): a candidate discovery needs theorem +
out-of-sample test + null model + novelty audit + independent skeptic pass,
ALL FIVE. Novelty audit FAILS (see `novelty_check.md`) — reported honestly as
such, not talked up.**

## The question this round answers

C156 established that the chirality split of the invariant-spinor space
`Sigma^T` is FORCED even only when `N = |Phi^+|` is ODD (the involution
`eps -> -eps` flips parity iff `N` odd). On the `N`-EVEN spaces tested (`G_2`,
`A_2 x A_2`) the observed `2+2` split was left unexplained.

## Reformulation (derived, not observed)

`eps in {+-1}^N` with `sum eps_k beta_k = 0`, `S = {k : eps_k = -1}`. Since
`sum_{Phi^+} beta = 2 rho`, `sum_k eps_k beta_k = 0 <=> sum_{beta in S} beta =
rho`. **Invariant spinors correspond to subsets of positive roots summing to
the Weyl vector**, chirality `= (-1)^{|S|}`.

## THEOREM (proved before any census was run)

> For every root system, `dim Sigma^T_+ = dim Sigma^T_-`, with no parity
> hypothesis on `N`.

*Proof.* The signed count of such `S` is the coefficient of `e^0` in
`ch(Sigma^+) - ch(Sigma^-) = prod_{beta>0}(e^{beta/2}-e^{-beta/2}) =
sum_{w in W} sgn(w) e^{w rho}` (Weyl denominator). The `e^0` coefficient needs
`w rho = 0`. `W` acts by isometries and `rho != 0` (a sum of positive roots), so
`|w rho| = |rho| != 0` for every `w` — no regularity assumption needed, isometry
alone suffices. Hence the signed count is 0. **QED.**

**[Correction, skeptic-caught]:** an earlier version of this proof cited `rho`'s
*regularity* (trivial stabilizer in `W`) as the reason `w rho != 0`. That is a
true fact about `rho` but the wrong lemma here — regularity says which `w` FIX
`rho`, not that `rho` is nonzero. The simpler, sufficient reason (`W` preserves
length, `rho != 0`) was pointed out by a context-blind skeptic pass and verified
directly above.

## Evidence (all exact, sympy/integer arithmetic)

**P4 regression** — the reformulation reproduces C156's actual Clifford-algebra
numbers: `A_2` → 1+1, `G_2` → 2+2, `A_2 x A_2` → 2+2. Passed.

**P1 exhaustive census** — 18 root systems (`A_2..A_6`, `B_2..B_5`, `C_2..C_5`,
`D_4,D_5`, `G_2`, `F_4`, `E_6`), via DP over partial sums (not `2^N`
enumeration). **Every system balances exactly**, including `E_6` with
`|Z(Phi)| = 13,697,920` split `6,848,960 / 6,848,960`. 10 systems admit
invariant spinors at all (`A_2,A_4,A_6,C_3,C_4,D_4,D_5,G_2,F_4,E_6`); 7 of those
have `N` even, the class this round set out to explain.

**P3 null model** — random integer vector sets of the same `(N, dim)` shape,
random reachable target, same DP census (state-space-guarded, see
`c157_step2_census.py`'s `StateBlowup`). Result, **materially different from
C156's**:

| shape | balanced rate (random) |
|---|---|
| `A_2` (N=3) | 5% |
| `G_2` (N=6, dim 2) | 35% |
| `A_2 x A_2` (N=6, dim 4) | 1% |
| `D_4` (N=10, dim 3) | 35% |
| `F_4` (N=16, dim 2) | 85% |

Unlike C156 (100% generic surjectivity, hypothesis killed outright), balance is
**far from generic** at small/moderate `N` — the actual root systems' exact
balance is not what a random configuration of the same shape typically does.
**Caveat, stated plainly:** the random rate rises toward the true value as `N`
grows (85% at `N=16`), a real limitation of this null model's discriminating
power at large `N`, not glossed over.

## Novelty audit — FAILS, and this determines the verdict

`novelty_check.md`: the theorem is the `lambda=0`, `r=T` special case of the
Gross–Kostant–Ramond–Sternberg formula (1998), reviewed in
Pengpan (arXiv:hep-th/9910119) Eq.(2), built from Kostant's own cubic Dirac
operator — the SAME operator this project's C144 already identified as the
origin of `D_Sigma`. **Classical, not new.** Matches the pre-registration's own
stated expectation, written before the proof was attempted.

## What this does NOT establish

1. **Not a discovery**, by the user's own five-gate mandate: novelty fails.
2. Nothing about `N_gen = 3`, `lambda`, triality, or any physical claim —
   explicitly excluded by the mandate.
3. No canonical parity-reversing involution was exhibited — the theorem proves
   the COUNTS are equal via a character identity, not via an explicit bijection.
   Whether one exists is a separate, harder, unanswered question.
4. The null model's discriminating power weakens at large `N` (85% at F_4
   shape) — the "well below generic" finding is solid for small/moderate `N`
   only.
5. `E_6`'s root construction (8-dim ambient, D5+half-spinor pattern) was
   validated only by its exact root count (36) and internal consistency, not
   against an external table.
