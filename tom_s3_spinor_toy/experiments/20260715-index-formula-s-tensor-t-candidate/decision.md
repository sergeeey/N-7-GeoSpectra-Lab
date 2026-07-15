# Index-formula candidate decision — CONFIRMED (both H1 and H2), REJECT for the candidate bundle

**Date:** 2026-07-15
**Verdict:** H1 CONFIRMED (index=7, not 3), H2 CONFIRMED (I(p,q) formula matches
at 3, 3bar, 6), H3 confirmed as elementary consequence. Candidate bundle
E=S^-(x)T^{1,0}S^6 is REJECTED as a clean index-3 twist -- independently
re-derived from scratch, not accepted from the external source at face value.

## Evidence

Ran `verify_index_formula.py` (sympy, from-scratch, no dependence on the
external source's own code):

1. Represented T^{1,0}S^6's Chern roots (x, y, z=-x-y, forcing c_1=0 per
   H^2(S^6)=0). Computed ch_3(T)/c_3(T)=1/2 exactly.
2. Built T(x)T's full 9 Chern roots (all pairwise sums), computed
   ch_3(T(x)T)/c_3(T)=3 exactly.
3. Built E=S^-(x)T=T (+) (T(x)T), computed ch_3(E)/ch_3(T)=7 exactly.
4. Using this project's own established facts (c_3(T)=chi(S^6)=2 from G33,
   A-hat(S^6)=1 exact from G73) as the ONLY external inputs: ind(D(x)E) =
   int(ch_3(E)) = 7 x int(ch_3(T)) = 7 x 1 = 7.
5. Symbolically evaluated the claimed I(p,q) formula at (p,q)=(1,0),(0,1),(2,0):
   got exactly I(3)=1, I(3bar)=-1, I(6)=7 -- matching the external source's
   claimed values precisely, via a completely independent route (general
   closed-form formula vs. direct Chern-root expansion). Two unrelated methods
   converging on the same number is strong evidence this is real math, not
   coincidence or hallucination.
6. H3 (exact-chirality obstruction) confirmed as elementary consequence of
   index = dim ker D+ - dim ker D-: for E=6(+)3bar^4 (net index 3), the two
   summands individually force dim ker D+ >= 7 and dim ker D- >= 4, i.e. at
   least 11 total zero modes, not an exact (3,0) kernel. The premise (operator
   block-preserves SU(3) isotypic decomposition, no intertwiner 3bar->6 exists
   by Schur's lemma since they are inequivalent irreps) is standard
   representation theory, correctly stated by the external source.

## Kill Analysis (mandatory per Anti-Overfitting Gate)

**What this kills:** the specific candidate E=S^-(x)T^{1,0}S^6 as a way to
realize a clean index-3 (or index-1-per-channel-times-3) twisted Dirac
operator relevant to the still-open 8_v/third-triality-channel search (G102,
L3B_SPIN8_INTERFACE_SPEC.md). This candidate gives index 7, an unambiguously
wrong number, not close to 3.

**What this does NOT kill:** G73's own established result
(ind(D(x)S^-)=1 per channel) -- that is a DIFFERENT, smaller bundle (S^- alone,
rank 4) than E=S^-(x)T (rank 12) tested here. Also does not kill the broader
L3b question or claim no Spin(8)-type mechanism exists -- it rules out one
specific proposed construction, one of presumably many that could be tried.

**Relaxation map (not started):** the I(p,q) formula + exact-chirality
obstruction theorem, now independently verified, is a reusable, CHEAP
screening tool -- any future candidate bundle proposal for the 8_v channel can
be checked against I(p,q) in seconds before investing in a full construction,
rather than discovering an index mismatch only after building the whole thing.

## Provenance note

The candidate and both formulas originated from an external analysis of
unknown/unverified authorship, relayed by the user (not this project's own
prior work). Per audit-verification-gate discipline, nothing from that source
was recorded as fact until re-derived independently here. The source's
surrounding commentary (a proposed "Spin(8) Interface Test", found separately
to duplicate `L3B_SPIN8_INTERFACE_SPEC.md` with less precision) was NOT
re-verified and is NOT endorsed by this experiment -- only H1-H3 specifically.

## Cost

~15 minutes: two independent sympy computations (Chern-root expansion,
formula substitution), no new physical construction, reusing only already-
established project facts (G33's c_3=2, G73's A-hat=1) as inputs.

## Files

- `claim.md` — frozen before running
- `verify_index_formula.py` — the independent from-scratch sympy verification,
  exit 0, all assertions pass
