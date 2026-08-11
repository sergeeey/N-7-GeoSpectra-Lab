# decision -- transcription error in Meier eq 6.3 identified and repaired; certified representation substrate for k=0..10; independently confirmed by a second, unrelated derivation

## Verdict

`MEIER_EQ63_TRANSCRIPTION_ERROR_CONFIRMED_AND_REPAIRED__SUBSTRATE_CERTIFIED_K0_TO_K10__INDEPENDENTLY_CONFIRMED_BY_CAMPORESI_HIGUCHI`
-> **P1-P6 all CONFIRMED exactly as predicted.**
**Date:** 2026-08-12 · L0: descriptive · script: `c85_certification.py`,
results: `results_c85.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** quaternion algebra | i^2=j^2=k^2=-1, ij=k, ji=-k exact | **CONFIRMED**, all 5 checks exact via raw Hamilton product (sympy). | [VERIFIED-sympy] |
| **P2** literal transcription | passes k=0,1, fails k>=2 | **CONFIRMED EXACTLY** -- brackets/Casimir/eq64 all pass k=0,1, all three fail simultaneously for every k=2..10 tested. | [VERIFIED-sympy] |
| **P3** repaired hypothesis (p-1->p-k) | passes ALL k=0..10 | **CONFIRMED** -- brackets, Casimir (Lemma 6.1), and eq 6.4 all hold exactly, k=0..10, no exceptions. | [VERIFIED-sympy] |
| **P4** negative control | perturbing repair (delta=1/2) breaks brackets/Casimir | **CONFIRMED** -- k=1..5 tested, all correctly rejected. | [VERIFIED-sympy] |
| **P5** round67 crosscheck | total multiplicity (per-copy x (k+1) q-copies) = (n+1)(n+2) exactly | **CONFIRMED**, n=0..7, exact match for both sigma=-1 (D=-(n+3/2)) and sigma=+1 (D=+(n+3/2)) branches. | [VERIFIED-sympy+numpy] |
| **P6** independent third source | Camporesi-Higuchi's unrelated method gives the same formula | **CONFIRMED**, exactly -- eq (3.57): eigenvalues +-i(n+N/2), N=3 gives +-(n+3/2); eq (3.58): degeneracy D_3(n)=2*(n+2)!/(n!*2!), symbolically simplified to (n+1)(n+2) exactly (sympy, verified n=0..5 numerically too). | [VERIFIED-external-source, VERIFIED-sympy] |

## The transcription-error finding, and why it is trustworthy

Meier's paper (arXiv:1103.4097) prints eq 6.3 as
`l_{e3}|p> = (p-1)i|p+1> - p*i|p-1>`. Transcribed character-for-character
from the PDF (re-verified against the source directly, not from memory),
this construction is a genuine `sp(1)`-representation (satisfies
`[l_{e_i},l_{e_j}]=2*l_{e_k}` exactly, a hard, basis-independent algebraic
requirement) ONLY at k=0 and k=1 -- both trivial or nearly-trivial cases
where `p-1` and `p-k` happen to coincide numerically for all valid p
(exactly when k=1). At every k>=2 tested, the literal formula breaks the
bracket relations, the Casimir identity, AND the quadratic eigenvalue
relation (eq 6.4) simultaneously and by a growing margin.

An external reviewer's falsifiable prediction -- replace `(p-1)` with
`(p-k)`, matching eq 6.2's own pattern -- was tested directly: the
repaired construction passes every one of the same three hard invariants
exactly, for every k=0 through k=10 tested, with zero exceptions. A
negative control (perturbing the repaired coefficient by a nonzero
constant) immediately and correctly breaks the same invariants, ruling
out the possibility that the checks are simply too weak to discriminate.

This is treated as a **strong, well-supported working hypothesis about
the source**, not a confirmed published erratum -- no such erratum was
searched for or found this round. The repair's CORRECTNESS as the
representation this codebase now uses is separately and independently
established by Phase 3 below, regardless of whether the printed formula
is in fact a typo.

## Independent confirmation (Phase 3) -- why this matters more than the self-repair alone

Per the reviewer's own explicit caution ("нельзя доверять только
собственной починке" -- don't trust only your own repair), Camporesi &
Higuchi (gr-qc/9505009, 1995) was read directly. Their derivation method
is completely unrelated to Meier's: separation of variables in geodesic
polar coordinates, an induction on the sphere dimension N starting from
S^2, and Jacobi-polynomial eigenfunctions -- no quaternions, no Sp(1)
representation theory, no Peter-Weyl decomposition anywhere in their
construction. Their closed-form results (eq 3.57, 3.58) for N=3 (odd)
give EXACTLY `+-(n+3/2)` with degeneracy `(n+1)(n+2)` -- the identical
formula round67 has used, uncited-correctly, since 2026-06-20 (g34,
`experiments/20260620-g34-flux-quantization/`), and the identical formula
the repaired Meier construction now reproduces exactly.

**Two structurally independent derivations converging on the identical
closed-form result is substantially stronger evidence than either
derivation's own internal consistency checks, however thorough those
checks are.** This resolves, decisively, the open question carried since
round67: the formula is correct, and now has a genuine primary-source
citation (Camporesi & Higuchi 1995/96, and Meier 2011 for the explicit
basis) instead of the unsupported "Sire & Xu" attribution.

## What survives, and what is now available for future rounds

The certified `l_{e_i}` matrices (repaired variant), for any k, are now
available as a trustworthy building block. Combined with the
programmatically-verified quaternion right-multiplication matrices, an
explicit D-bar (and hence D = D-bar - 3/2) operator can be built at any
Peter-Weyl level k -- the substrate C84A called for. The physical
`(n, sigma)` re-indexing (`sigma=-1` at level `k=n` directly, `sigma=+1`
at level `k=n+1`'s "+1/2" eigenspace) is now a certified, not merely
conjectural, structural fact.

**Named, explicit next step (C84B, not attempted this round):** compute
selection-rule matrix elements `<n',m'|T|n,m>` for the actual coupling
operator T used throughout C79-C83, using this now-certified substrate,
to determine whether the coupling is diagonal in the Peter-Weyl level
(`Delta n=0`, validating independent per-level testing) or genuinely
mixes adjacent/other levels (`Delta n!=0`, requiring the coupled block
construction named in the reviewer's own C84C proposal).

## Kill Analysis

**Killed:** the LITERAL transcription of Meier's eq 6.3 as a usable
construction for k>=2 -- it is algebraically inconsistent there, confirmed
three independent ways (brackets, Casimir, eq 6.4).

**Not killed, now strengthened:** round67's own closed-form eigenvalue/
multiplicity formula (was uncited-correctly since 2026-06-20; now has two
independent, verified primary sources); C84's own sigma=-1 branch result
(unaffected, uses only the n=0 scalar convention, not this construction);
the entire C79-C83 arc's own n=0 results (unaffected).

**New capability, not a kill:** an explicit, certified representation
substrate for k>=1, previously absent from this entire codebase across
all prior rounds (C74-C84 all cited the closed-form formula abstractly,
never building explicit matrices beyond the trivial n=0 scalar case).

## What this does NOT show

1. Does **not** prove the repair holds for all k (tested k=0..10; the
   clean, exception-free pattern is a strong structural argument but not
   an exhaustive proof for arbitrarily large k).
2. Does **not** compute any selection-rule matrix elements or run any
   coupling/spectral-flow test -- this round certifies the substrate
   only, per the reviewer's own explicitly staged C84A/B/C plan.
3. Does **not** search for or find a published erratum for Meier (2011)
   -- the transcription-error finding is a strong internal+cross-source
   diagnosis, not a confirmed correction to the published record.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c85-peter-weyl-representation-certification/c85_certification.py
```
Self-contained -- builds quaternion algebra and l-matrices from scratch,
no reuse of prior rounds' scripts (this round's subject matter, the
orbital/Peter-Weyl substrate, was never previously constructed anywhere
in this codebase).
