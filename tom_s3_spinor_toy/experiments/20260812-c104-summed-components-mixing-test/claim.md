# C104 -- does summing over all four D^1_{a,b} components produce genuine mixing?

**Experiment id:** `20260812-c104-summed-components-mixing-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C100 (found `M_k` for the single fixed `D^1_{1/2,1/2}`
component is an INJECTIVE EMBEDDING -- each level-k input state maps to
exactly one level-(k+1) output state, not a many-to-many mixing
operator). C101-C103 (built the full 2- and 3-level `D_PW` using this
same single-component `M_k`, found real spectrum + genuine spectral
shift + apparent truncation convergence).

---

## Counterfactual Frame

C100's own decision.md named this explicitly: "genuine multi-state
mixing... would require summing over MULTIPLE `(a,b)` components, not
attempted this round." research-audit's own Q4 (boyko-project-radar
scan) named this as an independently-runnable next test. This round
tests the LITERAL, simplest reading: does

```
M_k^sum := M_k^{(1/2,1/2)} + M_k^{(1/2,-1/2)} + M_k^{(-1/2,1/2)} + M_k^{(-1/2,-1/2)}
```

(summing the four single-component matrices C100's own method can
build for any `(a,b)`) produce a matrix where SOME input state maps to
MULTIPLE output states -- i.e. genuine mixing?

**This is an exploratory test of ONE specific alternative construction,
not a claim that `M_k^sum` is the physically correct multiplication
operator.** `Σ_{a,b} D^1_{ab}(g)` (sum of all four matrix elements of
the defining representation) is a well-defined scalar function of `g`,
but choosing it over the single `a=b=1/2` component is itself an
unverified modeling choice, exactly as flagged for the r-untouched
ansatz in C101-C103 -- this round does not resolve which (if either)
is physically motivated, only whether summing changes the qualitative
STRUCTURE (injective vs mixing) found in C100.

**Minimal Relaxation Rule applied:** this round changes exactly ONE
assumption from C100-C103 (which `D^1` component(s) to use) and holds
everything else fixed -- same `r`-untouched ansatz (`M_k^sum ⊗ I_r`),
same certified `L_i`/`R_i` generators, same magnetic-number labeling.

## Method

For `k=1,2,3`: build all four `M_k^{(a,b)}` matrices using C100's own
CG-assembly method (only `(a,b)` varies, everything else identical),
sum them elementwise into `M_k^sum`, then check its structural
properties directly (nonzero-entry count vs. `dim_k^2`, the exact test
C100 used to characterize injectivity).

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (reuse sanity)** | each individual `M_k^{(a,b)}` still passes the same P0-P1 checks C100 ran (correct dims, Wigner-3j cross-check) for at least the already-certified `(1/2,1/2)` component | pending |
| **P1 (the actual question)** | `M_k^sum` has MORE than `dim_k^2` nonzero entries for at least one `k`, i.e. genuine mixing (multiple output states reachable from a single input, or vice versa) -- NOT merely `dim_k^2` again (which would mean the four components' images never overlap, summing accomplishes nothing structurally new) | pending |
| **P2 (if P1 holds)** | is the mixing "generic" (most/all input states spread to multiple outputs) or "sparse" (only a few inputs show mixing, most remain injective)? | pending |

## kill_criterion

If P0 fails, this round's own reuse of C100's method has a bug -- stop,
debug before drawing any conclusion. If P1 is FALSE (still exactly
`dim_k^2` nonzero entries), that is itself a real, informative finding:
it would mean the four `(a,b)` components' images are disjoint at
every `k` tested -- a clean, checkable, likely SELECTION-RULE-driven
fact (each `(a,b)` shifts `(m_q,m_p)` differently, and if those four
shifted targets never collide for any input state, no amount of
summing produces overlap) -- worth stating precisely rather than
assuming summing "must" produce mixing.

## What this cannot show

- Does not establish that `M_k^sum` (if it does show mixing) is the
  physically correct multiplication operator -- one candidate among
  several, exactly as unverified as the single-component choice it
  replaces.
- Does not build a new `D_PW` using `M_k^sum` even if mixing is found
  -- that would be a natural follow-up, not attempted here.
- Does not resolve `r`'s role -- same untouched ansatz.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.
