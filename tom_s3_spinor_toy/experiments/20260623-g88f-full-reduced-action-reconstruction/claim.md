# G88F Claim: Full reduced-action reconstruction audit

## Hypothesis

The repository already contains enough local ingredients to reconstruct a full
4D reduced action with consistent Einstein-frame normalization, canonical
radion field, and KK-scale comparison.

## Success condition

`REDUCED_ACTION_RECONSTRUCTED` is allowed only if the local repository contains
all of the following in a single reproducible chain:

1. an explicit reduced 4D action or a deterministic symbolic reconstruction of it;
2. Einstein-frame normalization;
3. canonical radion field;
4. a KK-scale definition in the same frame;
5. a same-frame mass ratio derived from that action.

## Falsifiers

- only partial ingredients are available;
- the reduced action is missing and must be imported from outside the repo;
- canonicalization exists but not the normalized 4D action;
- the KK scale exists only as a coordinate proxy;
- the ratio depends on `M4=Ms=1` or another temporary convention.

## Allowed verdicts

- `REDUCED_ACTION_RECONSTRUCTED`
- `INSUFFICIENT_ACTION`
- `CANONICAL_PROXY_ONLY`
- `COORDINATE_ARTIFACT`
- `INVALID_ACTION`
- `MIXED`

## Reproduction command

```powershell
python tom_s3_spinor_toy/experiments/20260623-g88f-full-reduced-action-reconstruction/g88f_full_reduced_action_reconstruction.py
```

