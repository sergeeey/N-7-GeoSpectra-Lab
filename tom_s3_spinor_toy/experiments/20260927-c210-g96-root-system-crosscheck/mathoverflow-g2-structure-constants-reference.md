# MathOverflow reference record — "Reference Request: Structure constants for G2"

**Source:** https://mathoverflow.net/questions/322858/reference-request-structure-constants-for-g2
**Fetched:** 2026-09-27, via the Stack Exchange API v2.3 (`/2.3/questions/322858`,
`/2.3/questions/322858/answers`, both with `filter=withbody`) -- not by
scraping the HTML page (see MathOverflow's `robots.txt`: `Disallow: /`,
`Content-signal: search=no, ai-train=no`, checked directly before use).
**License:** CC BY-SA 4.0 (per the API response's own `content_license`
field).

## Question (verbatim, D_S, 2019-02-10, score 9)

Defines, for a split semisimple real Lie group `G` with Borel `B=TU`, an
ordering on the positive roots `Phi+`, and root-subgroup isomorphisms
`u_alpha: R -> U_alpha`. Asks for the unique real numbers
`C_{alpha,beta,i,j}` such that

```
u_alpha(x) u_beta(y) u_alpha(x)^-1 = u_beta(y) * prod_{i,j>0, i*alpha+j*beta in Phi+} u_{i*alpha+j*beta}(C_{alpha,beta,i,j} x^i y^j)
```

specifically for the root system G2, with a reference giving an explicit
root ordering and the constants written down.

## Answers (verbatim content, all fetched with body)

1. **Andrei Smolensky (accepted, score 9):** R. W. Carter, *Simple groups
   of Lie type*, table after Section 12.4 -- but only `C_{alpha,beta,1,1}`
   values are listed there. Full commutator formulas inside `U+` are in
   Table IV of N. Vavilov and E. Plotkin, *Chevalley groups over
   commutative rings: I. Elementary calculations* (image linked,
   `https://i.sstatic.net/CVNnA.png` -- NOT independently transcribed or
   OCR'd here; treat as a pointer, not a verified table).
2. **Peter McNamara (score 5):** SGA III, Exposé XXIII, Section 3.4.
3. **Jim Humphreys (score 5):** earliest reference is the 1956-58
   Chevalley seminar (republished 2005, ed. P. Cartier, Ch. 21, no
   characteristic assumption needed); Humphreys' own GTM 21 *Linear
   Algebraic Groups* (Springer, 1975) Sec 33.5 follows the same method;
   SGA3 similarly. Lie-ALGEBRA-level calculations (characteristic 0,
   closest in spirit to a Lie-bracket structure-constant table rather
   than the group-commutator formula above) are in Humphreys' GTM 9
   *Introduction to Lie Algebras and Representation Theory*, Sec 19.3.

## Why this is NOT directly comparable to G96 (see claim.md/decision.md for the full reasoning)

Every reference above gives constants in a **Chevalley basis**, indexed
by an explicit **ordering of the root system** (root subgroups / root
vectors `E_alpha`, one per root). G96 built its 14 generators as an
**arbitrary SVD null-space basis** of octonion derivations, with no root
labeling, no chosen ordering, and no Cartan subalgebra ever extracted --
and never published an explicit structure-constant table at all, only a
closure/Jacobi verification via reconstruction residuals. C210 closes
this gap the honest way: not by transcribing Carter's or Vavilov-
Plotkin's table (neither book was opened), but by extracting G96's own
Cartan and root system directly and checking it against the ABSTRACT,
basis-independent G2 root system data (6+6 split, sqrt(3) ratio, 30-degree
spacing) that both the MO answers' cited sources and any Chevalley-basis
table must also, necessarily, reproduce.
