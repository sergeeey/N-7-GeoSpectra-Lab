# G72 Decision — Chirality Bundle Audit

**Date:** 2026-06-21

**Verdict:** OPEN; triality multiplicity is not yet a generation theorem

**Evidence status:** [CODE] for the internal consistency audit;
[HYPOTHESIS] for the physical triality bundles

## Result

The current project does not define twisting bundles \(E_v,E_s,E_c\) for the
three triality labels. Their ranks as complex bundles, third Chern numbers,
orientation signs, and simultaneous appearance in the physical action remain
unknown.

Consequently:

\[
\#\{8_v,8_s,8_c\}=3
\]

does not determine

\[
\sum_i\operatorname{index}D_{E_i}.
\]

Three channels can consistently produce either:

\[
(+1)+(+1)+(+1)=3,
\]

or a vector-like result such as

\[
0+(+1)+(-1)=0.
\]

## Necessary and sufficient topological target

For a complex twisting bundle over \(S^6\), \(H^2(S^6)=H^4(S^6)=0\), so
\(c_1=c_2=0\). The relevant index formula reduces to

\[
\operatorname{index}D_E
=\int_{S^6}\operatorname{ch}_3(E)
=\frac12\int_{S^6}c_3(E).
\]

Therefore three net chiral modes require:

\[
\sum_{i=v,s,c}\int_{S^6}c_3(E_i)=6.
\]

This equation is a target condition, not a derivation from triality.

## Internal contradiction discovered

G13 states:

\[
\int_{S^6}c_3(T^{1,0}S^6)=2,
\qquad
\operatorname{index}D_{T^{1,0}S^6}=1.
\]

The canonical nearly-Kähler almost-complex tangent bundle is homogeneous under
the \(G_2\) action on

\[
S^6=G_2/SU(3).
\]

This is a counterexample to the unqualified G30/G32 statement that every
\(G_2\)-equivariant bundle over \(S^6\) has \(c_3=0\) and index 0.

Thus the universal G30 no-go does **not** survive in its present formulation.
A narrower theorem may still hold for a specified class of representations,
connections, or Dirac-induction conventions, but that scope must be defined
and proved. G30/G32 should not be used as final evidence for G72 until repaired.

## Current bundle ledger

| Channel | Bundle | \(c_3\) | Index | In one action? |
|---|---|---:|---:|---|
| \(8_v\) | unknown | unknown | unknown | not proved |
| \(8_s\) | unknown | unknown | unknown | not proved |
| \(8_c\) | unknown | unknown | unknown | not proved |

Current status: `UNRESOLVED`.

## Exact question for Tom

> Can the triality-related Spin(8) modules \(8_v,8_s,8_c\) be realized as
> three distinct complex twisting bundles \(E_v,E_s,E_c\) over
> \(S^6=G_2/SU(3)\)? If so, what are their third Chern numbers and orientation
> signs, do all three occur in one \(S^3\times S^6\) Dirac action, and does
> coupling to the \(S^3\) spin connection preserve their zero modes?

## Source anchors

- Butruille, *Homogeneous nearly Kähler manifolds*:
  https://arxiv.org/abs/math/0612655
- Foscolo–Haskins, *New \(G_2\) holonomy cones and exotic nearly Kähler
  structures on the 6-sphere...*:
  https://arxiv.org/abs/1501.07838

These support the homogeneous nearly-Kähler status of \(S^6\). The
top-Chern/Euler identity and Atiyah–Singer formula are applied in the existing
G13 implementation.
