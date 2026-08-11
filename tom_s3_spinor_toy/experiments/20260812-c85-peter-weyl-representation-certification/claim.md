# C85 -- certified Peter-Weyl representation substrate for S3's Dirac operator, general level k

**Experiment id:** `20260812-c85-peter-weyl-representation-certification`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C84 (sigma=-1 branch + honest n=1 NULL, provenance gap
found: "Sire & Xu" citation does not support the multiplicity formula).
Directed jointly by the user's own C84A/B/C restructuring proposal and a
follow-up adjudication of a bug this round's own certification gate caught.

---

## What this round actually did (three phases, each gating the next)

**Phase 1 -- provenance correction.** Read Sire & Xu (arXiv:2005.01448)
directly, page by page. [VERIFIED] It legitimately supports the GENERAL
product-manifold Clifford decoupling identity round67/round68 cite it
for (their eq 2.2-2.3, confirmed to match exactly) -- but contains NO
S3-specific spectrum content at all. The "(n+1)(n+2)" multiplicity
formula's citation to this paper, silently propagated through round67
into every round of the C74-C84 arc, is unsupported. The formula ITSELF
was independently cross-checked as correct (via the general classical
round-sphere formula) before continuing.

**Phase 2 -- explicit construction, found a real bug, adjudicated it.**
Built Meier (2011, arXiv:1103.4097, "Eigenspaces of the Spin Dirac
operator over S^3") eqs 6.1-6.4 explicitly: l_{e_i} matrices ((k+1)-dim,
the orbital/domain action) tensored with quaternionic right-multiplication
(the Clifford/value action, built from the raw Hamilton product, not
hand-derived). [VERIFIED-sympy] The LITERAL transcription of eq 6.3
passes every structural check (Lie-bracket consistency `[l_i,l_j]=2l_k`,
the Casimir identity `Lemma 6.1: -sum l_i^2 = k(k+2)*Id`, and eq 6.4's
quadratic relation) at k=0,1 -- but FAILS all three, unambiguously, at
every k>=2 tested (k=2..10).

An external reviewer supplied a precise, falsifiable hypothesis:
`(p-1)` in eq 6.3's `|p+1>` coefficient is a transcription typo for
`(p-k)` (matching eq 6.2's own `(p-k)` pattern) -- and `p-1` and `p-k`
are numerically IDENTICAL exactly when `k=1`, which is EXACTLY why k=1
passed "by accident" while k=2+ exposed the discrepancy. [VERIFIED-sympy]
Tested literal vs repaired side by side, k=0..10: repaired passes ALL
three structural invariants at every k; literal passes only k=0,1 and
fails all of k=2..10, exactly matching the predicted signature. A
NEGATIVE CONTROL (perturbing the repaired coefficient by a nonzero
delta=1/2) immediately breaks brackets and Casimir for k=1..5, confirming
the gate can reject a wrong construction, not just accept by
construction. The repaired construction's eigenvalues/multiplicities
were cross-checked against round67's own target formula (using the
CORRECT total = per-copy-multiplicity x (k+1) q-copies count, after
catching and fixing a real bug in the FIRST version of this crosscheck
that compared per-copy against total directly) -- exact match for
n=0..7.

**Phase 3 -- independent third-source confirmation, different method.**
Per the reviewer's own suggestion to not trust only the self-repair,
fetched and read Camporesi & Higuchi (1995/1996, gr-qc/9505009, "On the
eigenfunctions of the Dirac operator on spheres and real hyperbolic
spaces") directly. This derives the S^N Dirac spectrum via an ENTIRELY
DIFFERENT method (separation of variables in geodesic polar coordinates
+ Jacobi polynomials, an induction on dimension N -- no quaternions, no
Peter-Weyl, no representation theory of Sp(1) at all). [VERIFIED-external-
source] Their eq (3.57): eigenvalues `+-i(n+N/2)` (N=3: `+-(n+3/2)`,
exact match). Their eq (3.58) (N odd case): degeneracy
`D_N(n) = 2^{(N-1)/2}(N+n-1)!/(n!(N-1)!)`, which for N=3 simplifies
EXACTLY to `(n+1)(n+2)` -- confirmed by direct algebraic simplification
(2*(n+2)!/(n!*2!) = (n+1)(n+2)). This is a genuine independent
confirmation: two structurally unrelated derivation methods (Meier's
representation-theoretic quaternionic construction, now repaired and
certified, vs Camporesi-Higuchi's analytic separation-of-variables
approach) converge exactly on the same closed-form eigenvalue AND
degeneracy formula that round67 has used, uncited-correctly, since
2026-06-20.

## The claim under test

> **C85.** round67's own closed-form S3 Dirac spectrum (`+-(n+3/2)`,
> multiplicity `(n+1)(n+2)` each sign) is CORRECT (now independently
> confirmed by a fully unrelated derivation method), and an EXPLICIT,
> algebraically-certified matrix representation realizing it at every
> level k=0..10 now exists in this codebase for the first time -- built
> from Meier's construction with one identified and adjudicated
> transcription-error repair, verified against three hard, basis-
> independent structural invariants (Lie brackets, Casimir, eq 6.4) plus
> a working negative control.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (quaternion algebra)** | raw Hamilton product satisfies i^2=j^2=k^2=-1, ij=k | pending |
| **P2 (literal transcription)** | passes k=0,1, fails k>=2 on brackets/Casimir/eq64 | pending |
| **P3 (repaired hypothesis)** | passes ALL of k=0..10 on brackets/Casimir/eq64 | pending |
| **P4 (negative control)** | perturbing the repair by nonzero delta breaks brackets/Casimir immediately | pending |
| **P5 (round67 crosscheck)** | repaired construction's total multiplicities (per-copy x (k+1)) match (n+1)(n+2) exactly, n=0..7 | pending |
| **P6 (independent third source)** | Camporesi-Higuchi's unrelated method gives the identical eigenvalue+degeneracy formula for N=3 | pending |

## kill_criterion

P1 fails -> stop, a foundational arithmetic error, nothing downstream can
be trusted. P2 not matching the predicted k=0,1-only pattern would refute
the "transcription error" hypothesis outright (the literal formula would
need a different diagnosis). P3/P4 together are the actual adjudication:
P3 passing AND P4 correctly breaking is the standard for accepting the
repair; P3 passing without a working P4 would not be trustworthy (an
error-tolerant check proves nothing). P5 is the bridge back to physics --
without it, a "certified" representation could still be certifying the
wrong physical object. P6 is the highest-value single check in this
round: agreement between two unrelated derivation methods is far stronger
evidence than either method's own internal consistency checks, however
thorough.

## What this cannot show

- Does **not** prove the repair holds for all k (tested k=0..10 only,
  though the exact, clean pattern -- literal breaks precisely where
  p-1 != p-k, repaired never breaks -- is a strong structural argument,
  not merely an empirical coincidence over a finite range).
- Does **not** yet compute any coupling/selection-rule matrix elements
  `<n',m'|T|n,m>` (C84B's own next step) -- this round only certifies the
  SUBSTRATE those computations would need.
- Does **not** report the found transcription-error hypothesis to Meier
  or search for a published erratum (an available future action, not
  attempted here).
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
