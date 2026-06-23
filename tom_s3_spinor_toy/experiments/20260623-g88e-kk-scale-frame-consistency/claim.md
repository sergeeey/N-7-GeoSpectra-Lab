# G88E Claim: KK-scale and frame consistency audit

## Hypothesis

The radion mass and the KK scale can only be compared physically if they are defined in the same frame and the same normalization stack.

## Success condition

`FRAME_MAP_CLOSED` is allowed only if the repository explicitly provides:

1. the frame of the radion mass;
2. the frame of the KK scale;
3. the map connecting them;
4. the Planck/string normalization used for both.

## Falsifiers

- the KK scale is only defined as a coordinate proxy;
- the radion mass is only canonicalized in a metric-only sense;
- the comparison depends on `M4=Ms=1`;
- the required map from `M4/Ms` to the used mass scale is absent;
- frame conventions conflict across the sources.

## Allowed verdicts

- `FRAME_MAP_CLOSED`
- `FRAME_MAP_MISSING`
- `SCALE_CONVENTION_DEPENDENT`
- `INVALID_KK_SCALE`
- `MIXED`

## Reproduction command

```powershell
python tom_s3_spinor_toy/experiments/20260623-g88e-kk-scale-frame-consistency/g88e_kk_scale_frame_consistency.py
```

