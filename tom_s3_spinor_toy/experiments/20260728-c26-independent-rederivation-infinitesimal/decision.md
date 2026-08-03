# C26 (SU(2)_L x SU(2)_R representation pattern) -- independent second derivation

## Claim under review

round77/E11 (C26) found: the t=0 spinor `psi^(0)` (constant left-invariant)
is an exact SU(2)_L singlet / genuine SU(2)_R doublet; `psi^(1)` (t=1,
right-invariant profile `gbar(x)*psi_0`, c0=-2) is the mirror -- SU(2)_L
doublet / SU(2)_R singlet. Verified there via a FINITE-transformation test
(pick a generic second quaternion `h`, check `ACTION_L(h,psi)==psi` vs
`!=psi`, etc.).

## Why a genuine second method, not a forced port of Tom's technique

Goal-expansion hypothesis (b) originally asked to "redo C26 via Tom's own
explicit-diagonalization method." A literal port doesn't fit -- Tom's setup
matches an l-multiplet against abstract SO(3) generators via a similarity
transform; round77's question (how does ONE spinor transform under two
group actions) has a different shape. Instead of forcing an ill-fitting
analogy, used the actually-analogous move: **differentiate round77's own
finite actions at the identity** to get INFINITESIMAL (Lie-algebra)
generators as genuine differential operators, then check directly whether
they annihilate the spinor (singlet) or act as the true fundamental
representation (doublet, non-degenerate) -- structurally the same TYPE of
check Tom did (compare a differential operator's action to an abstract
generator), honestly adapted rather than copy-pasted.

## Method ([VERIFIED-tool], `rederive_c26_infinitesimal.py`)

Using round76's own already-verified `X_i^L`, `X_i^R` vector fields
(reused by import, not re-derived) and their established flow
correspondence (round76 Part 1: flow of `X^L` = right translation, flow of
`X^R` = left translation):

- Infinitesimal SU(2)_L generator on `psi`: `-X_Y^R(psi)` (differentiating
  `ACTION_L(exp(eps*Y),psi)(G)=psi(exp(-eps*Y)G)`).
- Infinitesimal SU(2)_R generator on `psi`: `Y*psi + X_Y^L(psi)`
  (differentiating `ACTION_R(exp(eps*Y),psi)(G)=exp(eps*Y).psi(G.exp(eps*Y))`).

## Result

**t=0 (`psi^(0)=(a,b)`, a genuine constant):**
- SU(2)_L generators on `psi^(0)`: exactly zero for all three `Z_i` ->
  **exact singlet**, confirmed.
- SU(2)_R generators on `psi^(0)`: exactly equal `Z_i*(a,b)` (the literal
  fundamental-representation matrix acting on the constant vector) for all
  three `Z_i` -> **genuine doublet**, confirmed, non-degenerate by
  construction (the full su(2) algebra acts as its own defining rep).

**t=1 (`psi^(1)=gbar(x)*psi_0`, c0=-2):**
- SU(2)_R generators on `psi^(1)`: exactly zero for all three `Z_i` ->
  **exact singlet**, confirmed.
- SU(2)_L generators on `psi^(1)`: nonzero for all three `Z_i`, and
  explicitly checked NOT proportional to `psi^(1)` itself (the "degeneracy
  check" `g[0]*psi1[1] - g[1]*psi1[0]` is a nonzero polynomial in
  `x0..x3`, not identically zero) -> **genuine, non-degenerate doublet**,
  confirmed.

All four checks agree exactly with round77's own finite-transformation
result -- the complementary singlet/doublet pattern is confirmed via a
completely independent computational route (infinitesimal Lie-algebra
generators vs finite group-element pullback testing), sharing only the
already-verified `X_i^L`/`X_i^R` vector-field infrastructure, not the
comparison method itself.

## Evidence tier upgrade

Per this project's own Independent Verification Strength Ladder
(`~/.claude/rules/falsification-ladder.md`): this is "same model, isolated
computation, different construction technique" -- a genuine step up from
round77's own single-method result. **C26's representation-labeling claim
is upgraded from INTERNALLY_CERTIFIED to INDEPENDENTLY_REPRODUCED** (two
structurally different methods, same session/model -- not yet a
cross-model or externally-reconstructed tier, which would require a
genuinely different tool/person).

## What this does NOT mean

- Does not touch the SPECULATIVE physical correspondence (C26's own
  3-stacked-assumption caveat: SU(2)_L=left-translation convention unstated
  in preprint.tex; psi^(1) only exists under c0=-2; no physical principle
  requires the S3 zero mode to match S6's chirality label) -- unaffected,
  exactly as open as before.
- Does not resolve C27 (multiplicity-2) or C25 (H1c) -- unrelated.
- Does not constitute a cross-model or externally-reconstructed
  verification (per the Independent Verification Strength Ladder, that
  would require a genuinely different tool or reviewer, not just a
  different technique within the same session).

## Check (reproduces this derivation)

```
cd experiments/20260728-c26-independent-rederivation-infinitesimal
python rederive_c26_infinitesimal.py
```
Expect all four booleans (`su2L_all_zero`, doublet match for t=0,
`su2R_all_zero` for t=1, nonzero+non-degenerate for t=1's SU(2)_L action)
to print True.
