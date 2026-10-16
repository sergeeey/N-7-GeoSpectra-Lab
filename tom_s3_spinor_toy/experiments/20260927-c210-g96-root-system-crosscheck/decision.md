# C210 Decision — G96's G2 realization matches the standard root system exactly

**Date:** 2026-09-27
**Verdict:** PROMOTE

## What was computed (`[VERIFIED-numpy]`, `c210_g96_root_system_crosscheck.py`)

| Check | Result |
|---|---|
| `dim(g2)` (rebuilt verbatim from G96) | 14 |
| `ad(H1)` zero-eigenvalue multiplicity | 2 (rank-2 Cartan) |
| `ad(H1)` nonzero eigenvalues | 12, real parts `~7e-16` (purely imaginary) |
| `H1, H2` commute | max `\|[H1,H2]\|` = `1.4e-15` |
| Root pairs extracted | 6 (as expected, 6 positive roots) |
| Root-vector residual (`[H2,E_k]` vs `i*phi_k*E_k`) | max `7e-16` |
| 12 norms-squared (trace form) | six at `1/3`, six at `1.0` exactly |
| long/short norm-squared ratio | `3.0` exactly |
| all 12 consecutive angular gaps | `30.0` degrees exactly |

All 6 structural checks pass (`all_pass: True`, `results_c210.json`).

## Why the naive comparison the user asked for doesn't directly work, and what was done instead

The MathOverflow question found via the Stack Exchange API
(`mathoverflow-g2-structure-constants-reference.md`, this directory) is
about **Chevalley-basis** structure constants `C_{alpha,beta,i,j}` for
commutators of root subgroups, in an explicitly ORDERED root system --
sourced to Carter's book, Vavilov-Plotkin, the Chevalley seminar, and
Humphreys' two books. G96 (`experiments/20260626-g96-s6-g2-su3/`) built
14 generators as an arbitrary SVD null-space basis of octonion
derivations and verified only closure/Jacobi/SU(3)-stabilizer -- it never
extracted a Cartan subalgebra, never chose a root ordering, and never
published a structure-constant table of its own. These are two different
mathematical objects in two unrelated, incompatible bases; a direct
number-for-number comparison would be meaningless (and neither Carter's
nor Vavilov-Plotkin's book was opened to transcribe their tables).

**What IS a valid, meaningful comparison:** the abstract ROOT SYSTEM
itself (basis-independent -- both a Chevalley-basis construction and
G96's octonion-derivation construction must, if both are genuinely `g2`,
reproduce the SAME root system up to isometry). This round extracts that
root system directly from G96's own basis via the ambient trace form
(canonical, doesn't depend on which arbitrary generator was picked as the
starting Cartan element) and checks it against the standard, textbook G2
root system (6 short + 6 long roots, length ratio `sqrt(3)`, 30-degree
spacing) -- confirmed via WebSearch before use
(`https://en.wikipedia.org/wiki/Root_system` and related sources), not
asserted from memory.

## A self-caught methodological bug, fixed before the final check

First version measured angles using the raw `(theta_k, phi_k)` eigenvalue
coordinates directly. This gave WRONG, irregular gaps (6.3, 22.6, 122.0,
18.6, 5.9, 4.5 degrees) -- not because the root system itself is wrong
(the LENGTH/ratio check, which correctly used the trace form throughout,
already gave the exact right answer, `3.0`), but because `{H1,H2}` is not
generally an orthonormal pair under the trace form, so raw-coordinate
angles are not the true geometric angles. Fixed by Gram-Schmidt
orthonormalizing `{H1,H2}` into `{e1,e2}` under the trace form (verified
orthonormal: `trace_form(e1,e1)=1.0`, `trace_form(e2,e2)=1.0`,
`trace_form(e1,e2)~0`) before projecting the root elements and measuring
angles -- exactly the same discipline this project applied to the
length/ratio computation from the start.

## What this means going forward

G96's own status stays `VERIFIED` (unaffected, and now independently
strengthened at the root-system level, not just closure). No physics
claim (OB1/N_gen=3, S6=G2/SU(3)) is touched -- this is purely an internal
consistency/verification round on the algebra itself, prompted by a user-
initiated cross-check against external literature found via MathOverflow.

## Reproduce

```
cd experiments/20260927-c210-g96-root-system-crosscheck
python c210_g96_root_system_crosscheck.py
```

`ruff check` -- clean (verified before this write-up).
