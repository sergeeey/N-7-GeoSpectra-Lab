# G89B Decision — B-L breaking operator audit

## Verdict

`DIRAC_ONLY_CONFIRMED`

## Result

The repository does not contain a `B-L = +2` scalar/operator/sector that could
compensate the `nu_R^T C nu_R` bilinear.

Observed candidates:

- Higgs bidoublet: `dBL = 0`, useful for Dirac Yukawas, not Majorana breaking;
- forbidden lepton-number-violating channels: `|dBL| = 2`, explicitly marked
  forbidden rather than available;
- no geometric or NCG candidate with `B-L = +2` was found in the checked local
  sources.

## Interpretation

The current model branch remains Dirac-only for neutrinos.
If a Majorana term is desired later, a new `B-L` breaking field/operator must be
added explicitly.

## Next gate

`G89C` — geometric spinor-bilinear singlet audit

