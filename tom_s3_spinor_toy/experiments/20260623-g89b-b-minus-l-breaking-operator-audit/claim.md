# G89B Claim: B-L breaking operator audit for Majorana neutrino mass

## Hypothesis

The repository may contain a `B-L = +2` scalar/operator/sector that can
compensate the `nu_R^T C nu_R` bilinear and permit a gauge-invariant Majorana
mass term.

## Success condition

`B_MINUS_L_BREAKING_OPERATOR_FOUND` is allowed only if the repository explicitly
contains a candidate with:

1. `B-L = +2` quantum numbers, or an equivalent two-unit breaking operator;
2. a documented coupling to `nu_R nu_R`;
3. a plausible source from geometry, NCG, or an identified scalar sector;
4. a mechanism for acquiring a VEV or mass scale.

## Falsifiers

- exact `B-L` remains preserved by the active fermion sector;
- the Higgs/bidoublet sector has `dBL = 0` only;
- the only lepton-number-violating channels are explicitly marked forbidden;
- the repo still says Majorana mass is not yet explored / not constructed.

## Allowed verdicts

- `B_MINUS_L_BREAKING_OPERATOR_FOUND`
- `MAJORANA_REQUIRES_NEW_B_MINUS_L_FIELD`
- `DIRAC_ONLY_CONFIRMED`
- `OPEN_MISSING_QUANTUM_NUMBERS`
- `OPEN_MISSING_SCALAR_SECTOR`
- `MIXED`

## Reproduction command

```powershell
python tom_s3_spinor_toy/experiments/20260623-g89b-b-minus-l-breaking-operator-audit/g89b_b_minus_l_breaking_operator_audit.py
```

