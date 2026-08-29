# C109 decision -- the k=1 anomaly requires the FULL 4-component
interference, is extremely fragile, and is precisely (not just
correlationally) diagnosed

**Verdict:** `K1_ANOMALY_REQUIRES_FULL_4COMPONENT_INTERFERENCE__FRAGILE_TO_ANY_SINGLE_PERTURBATION`
**Status:** RESOLVED -- precise mechanistic diagnosis of C108's own open pearl

---

## Summary

Diagnosed C108's own open pearl: why does D_PW built from C104's
`M_k^sum` break reality only at k=1 (`max|Im|=0.106`), never at k>=2?

**All 5 predictions confirmed, after one self-caught bug fixed
mid-round (see Verification section):**

| # | Prediction | Outcome |
|---|---|---|
| P0 | `j1=k/2` equals fixed `j2=1/2` only at k=1 | **CONFIRMED**. |
| P1 | `M_1^sum` has exactly 1 fully-populated row; `M_2,3^sum` have 0 | **CONFIRMED**. |
| P2 | Zeroing any single one of `M_1^sum`'s 16 nonzero entries restores exact reality | **CONFIRMED**, all 16 cases. |
| P3 | All 14 proper subsets of the 4 `(a,b)` components (sizes 1,2,3) give exactly real spectra | **CONFIRMED**. |
| P4 | Only the full size-4 subset gives a non-real spectrum, matching C108's own value | **CONFIRMED** -- `max\|Im\|=0.10592470995283362`, identical to C108's own number. |

## What this genuinely establishes

1. **A structural fact unique to k=1, confirmed exactly**: the auxiliary
   CG coupling representation is fixed at `j2=1/2` throughout the whole
   C99-C108 multiplication-operator series. The source level's own
   representation is `j1=k/2`. Only at k=1 does `j1=j2=1/2` -- this
   single coincidence is what makes k=1 structurally distinguished
   (confirmed: `M_1^sum` has a fully-populated row that `M_2^sum`,
   `M_3^sum` genuinely lack).
2. **But that structural feature is NOT the causal mechanism by
   itself** -- P2 shows the effect is destroyed by zeroing ANY single
   one of the 16 nonzero entries of `M_1^sum`, not just the ones in the
   fully-populated row. The reality-breaking is not localized to one
   row or one entry.
3. **The precise, sharp trigger (P3+P4)**: of all 15 nonempty subsets
   of the 4 `(a,b)` CG components, exactly ONE -- the complete set of
   all 4 together -- produces the non-real spectrum. Every proper
   subset (1, 2, or 3 out of 4) is exactly real. This means the effect
   is a genuine INTERFERENCE phenomenon requiring the simultaneous,
   exact combination of all 4 channels, occurring only where the k=1
   structural coincidence (P0/P1) provides the necessary condition for
   it to be possible at all.
4. **Extremely fragile / knife-edge**: this is the opposite fragility
   pattern from C106's own pearl (there, single-entry perturbation of a
   REAL-spectrum coupling stayed real, surprisingly robust). Here,
   single-entry perturbation of a NON-real coupling snaps it back to
   exactly real, in every one of 16 tested cases. Both observations
   together suggest non-real spectra are the rare, fine-tuned exception
   in this whole family, and exact reality is the generic/default
   state -- consistent with the broader pattern across C101-C108 (every
   other tested coupling gave exactly real spectra; this is the sole
   counterexample, and it is itself fragile).

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the hypothesis that the k=1 anomaly is caused by a single,
identifiable structural feature (a specific row or entry) -- P2 directly
falsifies this: any single change removes it.

**NOT killed, sharpened:** the actual mechanism -- full 4-component
interference, contingent on the k=1-specific `j1=j2` coincidence (P0/P1
supply the necessary structural precondition, P3/P4 supply the precise
sufficient trigger).

**New open question (not resolved, still a pearl):** WHY does the full
4-component sum specifically interfere destructively only when `j1=j2`?
A closed-form group-theoretic explanation (e.g. relating `M_1^sum` to a
specific, non-standard linear combination of the fundamental
representation's own matrix entries -- `sum_{a,b} D^1_{ab}(g)`, not a
covariant quantity like a trace or a Cartesian component) is plausible
but not derived or verified this round.

## What this cannot show

- Does not derive a first-principles proof of why `j1=j2` enables
  interference.
- Does not test whether an analogous resonance at a DIFFERENT matching
  `j1=j2` (e.g. `j2=1` tested at k=2) reproduces the same phenomenon.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260830-c109-k1-anomaly-full-four-component-interference/`
  -- clean, 0 errors.
- **Self-caught bug, recorded transparently**: the first version of this
  round's script classified subsets by counting `"+"` characters in a
  joined label string (`"+".join(subset)`), but the component labels
  themselves (`"++"`, `"+-"`, `"-+"`, `"--"`) already contain `+`
  characters -- an invalid proxy for subset size. This produced a wrong
  P4 classification (`assert p4_ok` failed, caught immediately by the
  round's own kill_criterion assertion, not silently accepted). Fixed by
  tracking subset size explicitly (`r` from `itertools.combinations`)
  instead of inferring it from the label string; re-ran cleanly with all
  5 predictions confirmed, `max|Im|` for the full subset matching C108's
  own `0.10592470995283362` exactly bit-for-bit -- confirms the fix was
  purely a classification-logic correction, not a change to the
  underlying (always-correct) numeric computation.
- This round's formal script independently re-derives every number found
  during the disclosed scratch exploration (claim.md's Counterfactual
  Frame).
