# Round49-RGE Controls

## Positive control (T1+T2) — reproduce preprint.tex's own published numbers

The script's `run_ratio()` function, given the SAME PDG-2022 M_Z boundary
values and the SAME beta coefficients (b3=-7, b2=-19/6, MS-bar) already
cited in `preprint.tex`'s "RGE matching constraint" paragraph
(`sec:coupling`), must reproduce three numbers already published in the
paper before the new M_s-scale result is trusted.

[VERIFIED-tool 2026-07-13] `python round49_rge_matching.py`:

| Check | preprint.tex value | Script output | Match |
|---|---|---|---|
| Ratio at M_Z (cross-check of PDG inputs) | 0.287 / 0.2865 | 0.2867 | within 0.01 |
| Ratio at 1 TeV | 0.362 | 0.3621 | within 0.01 |
| Ratio at 10 TeV | 0.430 | 0.4292 | within 0.01 |
| Backward-solved M_KK (ratio = 15/16π) | ~130 GeV | 130.72 GeV | within 5 GeV |

All four PASS. Method validated against independently-published (not
self-authored-and-tested-same-session) reference values — these numbers
were already in `preprint.tex` before this round started, so they are not
circular: the script did not "invent" its own target to hit.

## Negative control (T3) — discriminating power

[VERIFIED-tool 2026-07-13] Deliberately corrupted `alpha_s(M_Z)` from
0.1179 (correct, PDG 2022) to 0.13 (~10% wrong) and re-ran the M_Z-ratio
cross-check:

```
Deliberately wrong alpha_s=0.13 -> ratio(M_Z)=0.2600 (correct target 0.2865)
Discriminated as wrong: True
```

The check correctly flags a ~10% input error as outside the 0.01
tolerance — confirms the positive-control gate in Step 0 of the script
has real discriminating power, not a tautological always-pass.

## No-Collapse spot check

[VERIFIED-tool 2026-07-13] Re-ran `run_ratio(M_S_GEV, ...)` with
`alpha_s(M_Z)` at the PDG 1-sigma edges (0.1179 ± 0.0009, current
world-average uncertainty):

```
alpha_s(M_Z)=0.1170: ratio(M_s)=1.0093, factor=3.382x
alpha_s(M_Z)=0.1179: ratio(M_s)=1.0079, factor=3.378x  (central value)
alpha_s(M_Z)=0.1188: ratio(M_s)=1.0066, factor=3.373x
```

The factor mismatch stays in [3.373x, 3.382x] across the full PDG
1-sigma range — a 0.2% relative spread. The ~3.4x mismatch finding is
not sensitive to PDG input uncertainty at this level (dominated by the
~35 e-folds of running from M_Z to M_s, not by M_Z boundary precision).
