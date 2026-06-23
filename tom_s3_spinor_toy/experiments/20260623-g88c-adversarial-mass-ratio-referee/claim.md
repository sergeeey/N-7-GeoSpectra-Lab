# G88C Claim: Adversarial Physical Mass Ratio Referee

**Question type:** deterministic audit
**Date:** 2026-06-23
**Status target:** referee verdict

## Hypothesis

The old `2.02%` value should only be called physical if the reduced 4D action
and the KK scale are defined in the same canonical convention.

## Pass condition

The referee passes if it can classify the old ratio and the canonical proxy
without ambiguity.

## Fail condition

The referee fails if the audit cannot distinguish a coordinate artifact from a
canonical proxy, or if it claims a physical prediction without the missing
action/scale map.

## Allowed verdicts

- `PHYSICAL_CONFIRMED`
- `CANONICAL_PROXY_ONLY`
- `COORDINATE_ARTIFACT`
- `INSUFFICIENT_ACTION`
- `INVALID_COMPARISON`
- `MIXED`

## Falsifiers

- the old `2.02%` value survives canonical normalization unchanged;
- the canonical proxy equals the old ratio;
- the available action is sufficient to fix the physical scale.

## Reproduction command

```bash
python tom_s3_spinor_toy/experiments/20260623-g88c-adversarial-mass-ratio-referee/g88c_adversarial_mass_ratio_referee.py
python -m pytest tom_s3_spinor_toy/tests/test_g88c_adversarial_mass_ratio_referee.py -q
```
