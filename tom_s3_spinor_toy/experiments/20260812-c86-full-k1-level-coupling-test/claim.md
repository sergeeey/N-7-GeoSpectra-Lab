# C86 (C84B/C) -- does C79-C83's coupling postulate connect physical n=0 and n=1 within level k=1's own Hilbert space?

**Experiment id:** `20260812-c86-full-k1-level-coupling-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C85 (certified Peter-Weyl substrate, k=0..10). Directed
by the external reviewer's C84B proposal: compute selection-rule matrix
elements to determine whether C79-C83's coupling operator T is diagonal
in Peter-Weyl level (independent per-n testing valid) or genuinely mixes
levels (requiring the coupled-block construction the reviewer named
C84C).

---

## The setup this round makes possible for the first time

C85's re-indexing established: physical n's sigma=-1 branch is level
k=n directly; physical n's sigma=+1 branch is level k=n+1's own "+1/2"
eigenspace. A direct, previously-unnoticed consequence: **level k=1's
own full 8-dimensional Hilbert space (q x p x r) contains BOTH physical
n=1's sigma=-1 branch (D-bar=-1, total multiplicity 6) AND physical
n=0's sigma=+1 branch (D-bar=+3, total multiplicity 2) simultaneously.**
This is the first time in this entire arc (C79-C85) that two different
physical n's coexist in ONE properly-normalized, certified Hilbert
space -- C79-C83's own n=0 construction used an ad hoc scalar
approximation (`d_s3_scalar * I2`) that could never test this question,
because it never had access to any orbital structure at all.

## The claim under test

> **C86.** C79-C83's coupling operator `T = sum_i Z_i (x) Leibniz(g_i)`
> -- built from round67's LEVEL-INDEPENDENT 2x2 Clifford generator Z_i,
> acting only on the Delta_m/r index -- is tested on level k=1's full
> 8-dimensional S3 factor (512-dim joint space with S6) for the FIRST
> time, to determine whether it has nonzero matrix elements connecting
> physical n=0 and n=1. This is NOT decidable by inspection: T is built
> to act as identity on the (p,q) orbital indices, but D-bar's own
> eigenspaces (Meier's basis: `{e0 (x) |p>, e2 (x) |p-1>}` pairs) are
> GENUINE (r,p)-MIXED combinations, not simply "fixed p, varying r" --
> so T preserving p as a tensor index does not automatically mean T
> preserves D-bar's own eigenspaces. Checked numerically, per this
> project's own OB10/C85-established discipline of never trusting this
> kind of structural claim by hand-argument alone.

## Predictions, recorded before running the permanent script

| # | Prediction | Outcome |
|---|---|---|
| **P1 (D_S3 construction)** | full level-k=1 D_S3 reproduces BOTH n=0's sigma=+1 (D=1.5, mult 2) and n=1's sigma=-1 (D=-2.5, mult 6) exactly, from C85's certified substrate | pending |
| **P2 (self-dual triple)** | no crossing (compressed, raw-kernel-excluded test) | pending |
| **P3 (anti-self-dual triple)** | no crossing | pending |

## kill_criterion

P1 failing would mean this round's own construction has a bug
(reusing C85's already-certified substrate incorrectly) -- must stop and
fix before trusting anything downstream. **P2/P3 are the actual test.**
A "no crossing" result is a genuine, informative extension of the clean-
null pattern from n=0-only testing to this round's genuinely richer
n=0<->n=1 joint test -- not a foregone conclusion, since T's action on
D-bar's own (r,p)-mixed eigenbasis was not obviously trivial before
computing it. A crossing would be the reviewer's own hypothesized "M3"
mechanism (inter-level mixing) made concrete for the first time in this
project, and would require the same extra scrutiny (fine-scan avoided-
crossing verification) every unexpectedly positive result in this arc
has received before being trusted.

## What this cannot show

- Does **not** test any level k>=2, or any n=1<->n=2 (or higher) mixing
  -- k=1 only, testing n=0<->n=1 specifically.
- Does **not** test any coupling candidate other than round119's
  `so(4)_1` self-dual/anti-self-dual pair (the same candidates used
  throughout C79-C85 for direct before/after comparison).
- Does **not** rule out that a genuinely DIFFERENT coupling ansatz
  (e.g. one built from the orbital generators l_{e_i} themselves, rather
  than round67's level-independent Z_i) could produce inter-level
  mixing -- only this SPECIFIC, already-extensively-tested postulate is
  addressed here.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
