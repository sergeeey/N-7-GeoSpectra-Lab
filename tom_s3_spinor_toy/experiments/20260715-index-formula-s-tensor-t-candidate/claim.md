---
experiment_id: 20260715-index-formula-s-tensor-t-candidate
round: 1
date: 2026-07-15
tier: Standard-Ladder
status: closed
parent: external analysis (unverified agent output, relayed by user) proposing
  E = S^- (x) T^{1,0}S^6 as a candidate twist bundle relevant to the still-open
  L3b / third-triality-channel (8_v) search (see G102, L3B_SPIN8_INTERFACE_SPEC.md)
---

# claim.md — Does E = S^-⊗T^{1,0}S^6 give a clean index-3 twisted Dirac operator?

## Background

L3B_SPIN8_INTERFACE_SPEC.md (drafted 2026-07-14) documents that G102 exhausted
the *G2-equivariant* internal search space for a Spin(8)-type mechanism
distinguishing the three triality channels. An external analysis (source:
unverified, relayed by user, NOT independently authored by this project)
proposed a DIFFERENT candidate bundle, E := S^- (x) T^{1,0}S^6 where
S^- := 1 (+) T^{1,0}S^6 (our own established twist bundle, G73), claiming its
twisted-Dirac index is 7, not the hoped-for 3 -- and separately proposed a
general SU(3) representation index formula I(p,q) with an "exact-chirality
obstruction" theorem for reducible candidates.

Per this project's audit-verification-gate ("agent's VERIFIED != our
VERIFIED"), neither claim was accepted at face value -- both were
independently re-derived from scratch.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal -- index-theorem computation for a specific bundle
plus a general representation-theoretic index formula. NOT empirical, NOT causal.

## Claim under test

H1: ind(D_{S^6} (x) (S^- (x) T^{1,0}S^6)) = 7 (not 3), using only this
project's own already-established facts (c_3(T^{1,0}S^6) = chi(S^6) = 2, from
G33; A-hat(S^6) = 1 exact, from G73) as inputs.

H2: The claimed formula I(p,q) = [(p-q)(p+1)(q+1)(p+q+2)(p+2q+3)(2p+q+3)]/120
gives I(fundamental 3) = 1, I(3bar) = -1, I(6) = 7.

H3: For any SU(3)-equivariant reducible bundle with block-preserving twisted
Dirac operator, dim ker(D+) >= sum of positive per-block indices and
dim ker(D-) >= sum of |negative per-block indices| -- so a bundle combining
positive- and negative-index irreducible summands to a net index of 3 (e.g.
6 (+) 3bar^{+4}, net index 7+4x(-1)=3) necessarily carries EXTRA mirror zero
modes, not an exact (3,0) kernel.

## Falsification test

Direct, from-scratch sympy computation:
1. Represent T^{1,0}S^6's Chern roots as x, y, z=-x-y (c_1=0 forced by
   H^2(S^6)=0, an established project fact), compute ch_3(T) and c_3(T)=xyz
   exactly, check ch_3(T)/c_3(T).
2. Build T(x)T's 9 Chern roots (all pairwise sums x_i+x_j), compute ch_3(T(x)T).
3. Build E = S^-(x)T = T (+) (T(x)T), compute ch_3(E) and the ratio ch_3(E)/ch_3(T).
4. Separately, symbolically evaluate the claimed I(p,q) formula at
   (p,q)=(1,0),(0,1),(2,0) and compare to claimed values 1,-1,7.

## What this does NOT mean if CONFIRMED

1. Does NOT contradict G73 (ind(D(x)S^-)=1 per channel) -- that result is
   about S^- alone, a DIFFERENT (smaller, rank-4) bundle than E=S^-(x)T
   (rank-12) tested here. Both can be simultaneously true.
2. Does NOT close L3b or resolve the 8_v channel -- it rules out ONE proposed
   candidate construction, it does not prove no candidate exists.
3. Does NOT validate the rest of the external analysis this candidate was
   embedded in (e.g. its "Spin(8) Interface Test" proposal, separately found
   to duplicate L3B_SPIN8_INTERFACE_SPEC.md with less precision) -- this
   experiment concerns only the index-formula claims (H1-H3), not the
   surrounding commentary.
