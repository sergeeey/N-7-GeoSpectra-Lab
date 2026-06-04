# W-Sweep Pre-Registration — v0.1.25

**Date:** 2026-06-03
**Status:** PRE-REGISTERED (written before any W-sweep execution)
**Prerequisite:** Gate 4B v0.1.24 SIGNAL_PRESERVED at W=20
**Question type:** Descriptive

---

## Purpose

W=20 was chosen from Gate 3C exploratory finding — NOT from a systematic sweep.
The W-sweep asks: at what disorder strength does the localization signal emerge,
peak, and (if it does) weaken?

**This matters because:**
- Locating the onset W gives a testable prediction (W_c ≈ disorder threshold)
- Mapping the full curve (IPR vs W) strengthens the Anderson interpretation
- Finding W_optimal ≠ 20 would refine future experiments

---

## Estimand

**Population:** ring family only (primary; wilson_ring as secondary replication)

**Intervention:** Anderson disorder W ∈ {0, 5, 10, 15, 20, 25, 30}

**Comparator:** W=0 baseline (IPR(W=0) per size)

**Endpoint:** true_IPR(W) by disorder strength at fixed s1_size=64

**Summary measure:** IPR(W) curve — onset, peak, saturation/rolloff

**MCID:**
- ONSET: W where IPR(W) first exceeds 1.5× IPR(W=0)
- PEAK: W where IPR(W) is maximum
- MONOTONE: IPR(W) strictly increasing through W=30

---

## Grid

| Parameter | Values |
|-----------|--------|
| Family | ring (primary), wilson_ring (secondary) |
| s1_size | 64 (fixed — sufficient for trend, fast) |
| W | 0, 5, 10, 15, 20, 25, 30 |
| j_max | 3 |
| seeds | 123, 456, 789 |
| alpha | 0.0 |
| **Total** | **2 × 7 × 1 × 3 = 42 cases** |

Runtime estimate: ~10s/case on server → ~7 min total.

---

## Decision Rules (Pre-Registered)

Gate 4B reference: ring IPR(W=20, s1=64) ≈ 0.320

| Outcome | Criterion | Interpretation |
|---------|-----------|----------------|
| MONOTONE | IPR strictly ↑ from W=0 to W=30 | No rolloff in range; W=20 sub-optimal |
| PEAK_AT_20 | IPR peaks at W=20 ±5 | Gate 4B choice validated |
| PEAK_BELOW_20 | IPR peaks at W<15 | W=20 over-disordered |
| PEAK_ABOVE_20 | IPR peaks at W>20 | W=20 under-disordered |
| ONSET_HIGH | IPR < 1.5× at W=10 | Onset above W=10 |

**Follow-up rule:** If PEAK found → rerun Gate 4B at W_peak with same 216-case grid.

---

## What This Result Does NOT Mean

1. W_peak is NOT "the optimal disorder for compactification."
2. Onset does NOT prove Anderson localization phase transition.
3. Results at s1=64 only — may differ at s1=128.
4. Does NOT generalize to spectral_circle (excluded from primary).

---

**Status:** PRE-REGISTERED — awaiting server execution
**Next step:** `scripts/run_w_sweep_v0.1.25.py --dry-run`
