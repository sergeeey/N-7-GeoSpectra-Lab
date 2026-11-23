# Decision: four ledger gaps closed with qualified entries (C244 to C247)

**Date:** 2026-11-23

## Result

All ten scripts were copied into `scripts/` with style-only fixes (ruff safe fixes plus four hand edits: an f-string, a `bool(...)`, a default argument binding the loop variable, a `noqa`) and re-run from there with `python -I` (exit 0 for all). The 13 logs in `logs/` are byte-identical to the logs of the run before the fixes.

| ledger row | script | log | what the log shows |
|---|---|---|---|
| C244 | `verify_euler_operators.py` | `run_verify_euler_operators.txt` | 12 PASS, ALL PASS: generators J+-, weight k, charts N and S, frame sign |
| C244 | `verify_euler_closure_rule.py` | `run_verify_euler_closure_rule.txt` | ALL AGREE: predicted and measured closure agree in every scanned row (14 predicted closures, 22 predicted failures); rule equals the exploratory rule of C221 on 21 pairs |
| C244 | `verify_euler_final.py` | `run_verify_euler_final.txt` | 30 PASS, ALL PASS: single-valuedness, body-fixed generator |
| C244 | `verify_euler_dictionary_signs.py` | `run_verify_euler_dictionary_signs.txt` | 14 PASS, ALL PASS: the sign of the lowering coefficient is a phase convention; frame column and state have opposite weights |
| C244 | `verify_euler_vs_sympy_wignerd.py` | `run_verify_euler_vs_sympy_wignerd.txt` | 69 checks pass; negative control (wrong sign of the d_psi term) fails in 18 of 18 cases with k != 0 |
| C245 | `q4_m_minus_one_stage2.py` | `run_q4_m_minus_one_stage2.txt` | 9 PASS, FAILS none |
| C245 | `m_minus_half_ladder_check.py` | `run_m_minus_half_ladder_check.txt` | 4 PASS, FAILS none |
| C246 | `verify_dirac_closed_form.py` | `run_verify_dirac_closed_form.txt` (+ `results_dirac_closed_form.txt`) | max error 9.16e-16 at 20 points; control with +Gamma: 2.04 |
| C246 | `verify_tom_bridge_sigmaL_formula.py` | `run_verify_tom_bridge_sigmaL_formula.txt` | identity holds on all test fields (residual ~1e-15); negative control 2(1 - sigma.L) fails on all discriminating fields |
| C246 | `verify_tom_frame_identity_full.py` | `run_verify_tom_frame_identity_full.txt` | factor c = 2i with residual ~1e-15 for the rotated frame; identity frame residual of order 3 to 4 |
| C247 | none | none | open question; the half that is already certified is the degree-1 block of TOM-CERT-01 |

## Status of each part

| part | status |
|---|---|
| extra term = derivative along the third Euler angle (C244) | exact sympy plus random-point checks; reproduced here |
| closure rule agrees with C221's exploratory rule (C244) | scanned (j, k) rows only |
| match with the standard edth operator (C244) | secondary source only; primary source not opened |
| literal m = -1 reading is the l = 1 lowest-weight state (C245) | exact |
| scalar ladder at m = +-1/2 does not close (C245) | exact; restates C221 (1) |
| bridge identity on S^1-invariant spinors (C246) | numerical on test fields (degrees 0 to 3), negative controls fail; analytic proof exists in a private theorem note, not re-derived here |
| sign/convention relation to the published reduction (C246) | hand algebra from equations read; pages 4 to 7 and 11 to 19 of the source not read; not a script result |
| reading of the recorded statement (C247) | OPEN; hypothesis that the statements concern different spaces is INFERRED, untested |

## What this decision does NOT establish

- That C221's own entry is corrected: it is unchanged; the memory note saying the origin of the term was "closed" overstated what the ledger recorded until C244.
- Novelty: none claimed for any of the four.
- Which space or operator the correspondent uses (R17 needs his answer).
- That the reduction of C246 is the correspondent's equation.

## Follow-ups

- Read the unread pages of the published reduction, or fetch the primary source (needs an explicit yes for the download).
- Open the primary source of the edth operator.
- Ask the correspondent which space his statement about the harmonic basis refers to (R17).

Ledger: C244_EULER_ANGLE_ORIGIN_OF_EXTRA_TERM_AND_CLOSURE_RULE_REPRODUCED_PRIMARY_SOURCE_NOT_OPENED, C245_LITERAL_M_MINUS_ONE_IS_L1_LOWEST_WEIGHT_SCALAR_LADDER_AT_M_PM_HALF_DOES_NOT_CLOSE, C246_S3_S2_REDUCTION_IDENTITY_NUMERICALLY_VERIFIED_RELATION_TO_PUBLISHED_REDUCTION_PARTLY_UNREAD, C247_OPEN_READING_OF_FERMION_WAVEFORMS_SUBSET_OF_HARMONIC_BASIS_AGAINST_C222_C224
