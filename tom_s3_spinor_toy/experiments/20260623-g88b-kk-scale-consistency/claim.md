# G88B Claim: KK / Planck / String Scale Consistency Audit

**Question type:** deterministic audit
**Date:** 2026-06-23
**Status target:** open

## Hypothesis

The mass ratio only becomes physical if the KK scale, the Planck scale, and the
string-scale normalization are all specified in the same convention.

## Pass condition

The audit passes if the repository provides a consistent scale map that fixes
the KK comparison unambiguously.

## Fail condition

The audit fails if `m_mod/m_KK` depends on the normalization convention or if
the required `M4/Ms` map is absent.

## Allowed verdicts

- `SCALE_MAP_CLOSED`
- `SCALE_MAP_OPEN`
- `SCALE_CONVENTION_DEPENDENT`
- `INVALID_KK_COMPARISON`
- `MIXED`

## Falsifiers

- the KK ratio changes under admissible normalization changes;
- the required Planck/string scale map is missing;
- the repository only supplies string-unit or coordinate-unit ratios.

## Reproduction command

```bash
python tom_s3_spinor_toy/experiments/20260623-g88b-kk-scale-consistency/g88b_kk_scale_consistency.py
python -m pytest tom_s3_spinor_toy/tests/test_g88b_kk_scale_consistency.py -q
```
