# G89A Decision — Majorana gauge-invariance and selection-rule audit

## Verdict

`DIRAC_ONLY_ALLOWED`

## Result

The local repository treats the neutrino sector as Dirac-only and keeps exact
`B-L` in the active selection rules.

Evidence used:

- `nu_R` appears with `B-L = -1`;
- the finite Dirac operator preserves `B-L`;
- the Higgs bidoublet is `B-L = 0`;
- no `B-L = 2` scalar/operator is present in the checked local sources;
- the repo explicitly says the Majorana mass for the right-handed neutrino is
  not yet explored.

## Interpretation

Under the current symmetry structure, a bare `nu_R^T C nu_R` term is not
available as a gauge-invariant mass term. A Majorana mass would need explicit
`B-L` breaking or a new field/operator not present in the current repository.

## Next gate

`G89B` — geometric spinor-bilinear singlet audit

