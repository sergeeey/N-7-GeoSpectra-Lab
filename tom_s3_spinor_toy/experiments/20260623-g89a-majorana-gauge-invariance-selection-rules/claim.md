# G89A Claim: Majorana gauge-invariance and selection-rule audit

## Hypothesis

The repository can determine whether a right-handed neutrino Majorana term
`nu_R^T C nu_R` is allowed by the current gauge and selection-rule structure.

## Success condition

`MAJORANA_ALLOWED` is allowed only if the repository explicitly shows:

1. the quantum numbers of `nu_R`;
2. the Majorana bilinear is a gauge singlet;
3. `B-L` is not exact or is already broken in the relevant sector;
4. no selection rule forbids the bilinear.

## Falsifiers

- `nu_R` carries `B-L = -1` and `B-L` is exact;
- the finite Dirac operator preserves `B-L`;
- the repository has no `B-L = 2` scalar/operator;
- the neutrino sector is explicitly Dirac-only.

## Allowed verdicts

- `MAJORANA_ALLOWED`
- `MAJORANA_FORBIDDEN_BY_B_MINUS_L`
- `MAJORANA_REQUIRES_B_MINUS_L_BREAKING`
- `DIRAC_ONLY_ALLOWED`
- `INSUFFICIENT_QUANTUM_NUMBERS`
- `MIXED`

## Reproduction command

```powershell
python tom_s3_spinor_toy/experiments/20260623-g89a-majorana-gauge-invariance-selection-rules/g89a_majorana_gauge_invariance_selection_rules.py
```

