# C157 — PRE-REGISTRATION (written before any census was computed)

**Date:** 2026-09-05. **Tier:** FL Full. **L0 (EstimandOps): DESCRIPTIVE.**
**Mandate constraint accepted:** autonomy covers search, computation, literature,
hypothesis-switching and negative results. It does NOT cover declaring a
discovery. A candidate must pass all five: theorem, out-of-sample test, null
model, literature novelty audit, independent skeptic pass.

## The question (inherited from C156's failure)

C156 established that the chirality split of the invariant spinor space is
FORCED to be even when `N = |Phi^+|` is ODD, via the fixed-point-free involution
`eps -> -eps`, which flips the parity of the sign vector iff `N` is odd. On the
two `N`-EVEN spaces tested (`G_2`, `A_2 x A_2`) the observed `2+2` split was
therefore **unexplained**. Question: is there a canonical, Weyl-theoretic reason?

## Reformulation (derived before computing anything)

Let `Phi^+ = {beta_1..beta_N}`, `rho = (1/2) sum_{beta>0} beta`. An invariant
spinor corresponds to `eps in {+-1}^N` with `sum_k eps_k beta_k = 0`. Put
`S = {k : eps_k = -1}`. Since `sum_{Phi^+} beta = 2 rho`,

        sum_{k not in S} beta_k - sum_{k in S} beta_k = 0
    <=> sum_{beta in S} beta = rho .

**Invariant spinors <-> subsets of positive roots summing to the Weyl vector**,
with chirality `= (-1)^{|S|}`.

## The theorem, stated and proved BEFORE the census

> **THEOREM (chirality balance).** For every root system, the number of subsets
> `S` of `Phi^+` with `sum_{beta in S} beta = rho` and `|S|` even equals the
> number with `|S|` odd. Equivalently `dim Sigma^T_+ = dim Sigma^T_-` for every
> full flag manifold `G/T`, with no parity hypothesis on `N`.

*Proof.* The signed count is the coefficient of `e^0` in
`prod_{beta>0} (1 - e^{beta})` up to the overall factor `e^{-rho}`; equivalently
it is the zero-weight multiplicity of the virtual module `Sigma^+ - Sigma^-`.
Its character is the Weyl denominator,
`ch(Sigma^+) - ch(Sigma^-) = prod_{beta>0}(e^{beta/2} - e^{-beta/2})
 = sum_{w in W} sgn(w) e^{w rho}`.
The coefficient of `e^0` picks out the `w` with `w rho = 0`. Since `rho` is
regular and nonzero and `W` acts by invertible isometries, there are none.
Hence the signed count is `0`, i.e. the two parities are equinumerous. **QED**

**Status of this proof: it is three lines from a classical identity. It is
therefore expected to be KNOWN.** The novelty audit is Step 4 and its likely
outcome is "classical corollary". That expectation is written down here so a
later "we discovered it" cannot be retrofitted.

## Pre-registered predictions

| # | prediction | falsified by |
|---|---|---|
| **P1** | the split is even for **every** root system in the census, `N` odd or even, including systems where `Z(Phi)` is empty (trivially `0 = 0`) | any system with `|Z_+| != |Z_-|` |
| **P2** | the `eps -> -eps` involution explains ONLY the `N`-odd cases; for `N` even it maps each parity class to itself, so balance there needs the theorem | finding that `eps -> -eps` flips parity for some even `N` |
| **P3** | **NULL MODEL (the test the skeptic will demand, registered now):** replace `Phi^+` by a random set of `N` integer vectors with even total, target `= half the total`. The signed count is then generically NONZERO. Predict: balance occurs in a **small minority** of random draws, decisively below the 100% that root systems give | balance occurring at ~100% for random sets too, which would make the theorem's content vacuous exactly as HYPOTHESIS S was in C156 |
| **P4** | the correspondence `eps <-> S`, and `chirality = parity(|S|)`, reproduces the chirality splits already computed with actual Clifford algebra in C156 (`A_2` 1+1, `G_2` 2+2, `A_2 x A_2` 2+2) | any mismatch ⟹ the reformulation is wrong and everything above collapses |

## Census scope

`A_r, B_r, C_r, D_r` up to the largest tractable rank, plus `G_2`, `F_4`, and
`E_6` if reachable. Counting is by **dynamic programming over partial sums**
(dict keyed by the running vector, carrying even/odd size counts), NOT by `2^N`
enumeration, so `N = 36` is reachable where brute force would not be.

## What this will NOT establish, whatever happens

1. Novelty. The proof is a corollary of the Weyl denominator formula; the prior
   expectation is that it is classical and known to specialists.
2. Anything about `N_gen = 3`, triality, `2/3`, or `lambda`. Explicitly excluded
   by the mandate.
3. Anything about the C155 rank-2 map — that is a separate, later channel.
4. A canonical parity-reversing involution. The theorem proves the COUNTS are
   equal without exhibiting a bijection; whether a canonical involution exists
   is a strictly stronger, separate question, and is NOT answered here.
