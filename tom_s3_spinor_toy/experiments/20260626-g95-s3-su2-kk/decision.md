# G95 Decision — SO(4) = SU(2)_L x SU(2)_R from S³

**Verdict: VERIFIED**

## Claim

KK reduction on S³ produces gauge group SO(4) = Iso(S³), which decomposes exactly as
SU(2)_L x SU(2)_R. One factor — SU(2)_L — is the SM weak interaction candidate.

## Algebraic result

Decomposition via 't Hooft symbols (s=1/2 normalization):

```
J+_i = (1/2)(L_{0i} + eps_{ijk} L_{jk}/2)   [SU(2)_L generators]
J-_i = (1/2)(L_{0i} - eps_{ijk} L_{jk}/2)   [SU(2)_R generators]
```

Verified to machine precision:

| Check | Result |
|---|---|
| dim(SO(4)) | 6 [VERIFIED] |
| [J+_a, J+_b] = -eps_abc J+_c | err=0.00e+00 [VERIFIED] |
| [J-_a, J-_b] = +eps_abc J-_c | err=0.00e+00 [VERIFIED] |
| [J+_a, J-_b] = 0 (decoupled) | max err=0.00e+00 [VERIFIED] |
| SO(4) closure | max err=2.22e-16 [VERIFIED] |

Note: SU(2)_L and SU(2)_R have OPPOSITE sign conventions ([Ja,Jb] = ±eps Jc)
because they are self-dual and anti-self-dual rotations respectively — physically
this reflects their opposite chirality under parity.

## SM relevance

- SU(2)_weak = SU(2)_L (the J+ sector of SO(4) = Iso(S³))
- This identifies the weak isospin gauge group ALGEBRAICALLY from the S³ geometry
- KK scale from G94: m_KK = 1.5/rho3 = 0.778 M_s = 1.38e17 GeV >> M_GUT
- All KK modes (6 gauge bosons: W1,W2,W3 for L and R) are at m_KK scale
- SU(2)_R must be spontaneously broken at compactification scale (Tom's mechanism needed)

## What this does NOT mean

1. Does NOT prove SU(2)_L = SM weak interaction uniquely; only that such an identification
   is algebraically consistent. Physical selection of L vs R requires parity breaking mechanism.
2. Does NOT explain why SU(2)_R is broken (needs Tom's Part 4/5 spinor structure)
3. Does NOT give coupling constant g_W (free parameter at this stage)
4. Does NOT address generations (3 generations not explained by SO(4) algebra)

## Status in SM derivation roadmap

| Group | Source | Status |
|---|---|---|
| SU(3)_color | SU(3) subset G2 subset SO(7) | G96 VERIFIED |
| SU(2)_L | SU(2)_L subset SO(4) = Iso(S³) | G95 VERIFIED |
| SU(2)_R | SU(2)_R subset SO(4) = Iso(S³) | G95 VERIFIED (must break) |
| U(1)_Y | Y = T3_R + (B-L)/2 | G97 PARTIAL (B-L open) |
