# E13 (round79) — Claim: reconciling the S3-side multiplicity-2 finding (E12)
# against this project's own pre-existing "32 states = one generation" convention

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

## Background (what this experiment does NOT re-derive)

- E12 (`experiments/20260717-round78-e12-multiplicity-gate/decision.md`) tool-verified
  `dim ker(D_{S3,t=0}) = dim ker(D_{S3,t=1}) = 2` (under `c0=-2`), each an irreducible
  SU(2) doublet, giving `2 x 1 (G74A) x 3 (channels) = 6` internal zero modes where the
  torsion-escape-route program needs `3`. E12 explicitly left open (Relaxation Map,
  option 1) whether "1 generation = 1 S3-side SU(2) doublet" is a valid re-reading of
  `preprint.tex:292-298`.
- E11 (`experiments/20260717-round77-su2lr-correspondence-test/decision.md`) tool-verified
  the representation content: `t=0` kernel is an exact SU(2)_L singlet / genuine SU(2)_R
  doublet; `t=1` kernel (under `c0=-2` only) is the exact mirror, SU(2)_L doublet / SU(2)_R
  singlet. This experiment reuses this finding by citation; it does not re-derive it.

## The three readings under test (pre-registered before running the check below)

**(a) "Both torsion sectors, simultaneously":** the t=0 zero mode supplies exactly the
RIGHT-HANDED half of one generation's S3-side content and the t=1 zero mode supplies
exactly the LEFT-HANDED half; a full physical generation requires BOTH torsion values
to be simultaneously, physically realized (not "select one of t=0/t=1").
  - **Verdict criteria:**
    - *Structural* PASS requires: an independent, pre-existing (not newly invented for
      this experiment) project artifact that already splits the S3-side "4-component
      SO(4) spinor representation" into two 2-dimensional SU(2)_L-doublet /
      SU(2)_R-doublet blocks, with the SAME dimension (2+2) and SAME representation
      labels (singlet-of-X/doublet-of-Y) that E9-E12 found for t=0 and t=1.
    - *Physical* PASS additionally requires: a stated (not manufactured here) mechanism
      or motivation in this project for why the S3 connection would take DIFFERENT
      torsion values in the two chirality sectors simultaneously.
    - FAIL condition: no such artifact exists, or the dimensions/labels do not match, or
      matching requires forcing/relabeling not licensed by the existing text.

**(b) "Particle + CPT conjugate":** the 2-dimensional kernel at a SINGLE torsion value
already supplies both a state and its own CPT conjugate as its two dimensions; the
SU(2)-doublet structure E11 found is not gauge-doublet content at all but
particle/antiparticle content.
  - **Verdict criteria:**
    - PASS requires: under this project's own existing 32-state bookkeeping, the
      particle/antiparticle (CPT-conjugate) doubling is actually carried by the SAME
      S3-side label that E11 found to define the SU(2) doublet — i.e. a particle and
      its CPT conjugate carry DIFFERENT S3-side chirality labels in the existing
      convention, consistent with "the 2 dimensions of the kernel = particle & antiparticle."
    - FAIL condition: the existing convention carries CPT/antiparticle doubling on a
      DIFFERENT factor (S6) than the one E11's SU(2)-doublet finding lives on (S3), with
      the S3-side label IDENTICAL between a particle and its own antiparticle — this
      would make (b) a category error (conflating a continuous gauge rotation with a
      discrete antiunitary conjugation) under the project's own existing bookkeeping,
      not merely "unconfirmed."

**(c) "Genuinely open":** neither (a) nor (b) is licensed by a careful reading of
existing conventions; new physical input is required.
  - Applies by default if both (a) and (b) fail their PASS criteria above, or if (a)
    passes only structurally but not physically (a specific, nameable partial state
    distinct from a blanket "open").

## Check

`python e13_reconciliation_check.py` — cross-checks E11/E12's tool-verified findings
against `experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`
(an experiment predating the torsion-escape program, hence not built to match it),
using that file's own S3-state table, SM_TABLE, and its own explicit
particle/antiparticle naming convention (verbatim-copied into the script here, cited,
not modified). Expected outputs, pre-registered:
- `dimension_match_t0`, `dimension_match_t1` — do the G6 chirality blocks have
  dimension 2, matching E12?
- `label_match_t0`, `label_match_t1` — do the G6 blocks carry the SAME
  SU(2)_L/SU(2)_R singlet/doublet labels E11 found?
- `cpt_doubling_independent_of_chir_s3` — is the particle/antiparticle doubling in G6's
  own 32-state table carried by a label OTHER than the S3-side chirality block (refutes
  (b) if true; supports (b) if false)?

## Caveat / What this does NOT mean (pre-registered)

1. A structural (dimension + label) match for (a) does NOT establish that the S3
   connection actually CAN or DOES take two different torsion values simultaneously in
   different sectors — that is a separate, physical-mechanism question this check
   cannot answer computationally.
2. This does NOT resolve how the S3-side count (whatever it turns out to be) combines
   with the S6-side "8" bookkeeping / the actual `dim ker(D_{S6,twisted})=1` per channel
   (G74A) and the triality-channel count (3, G73) into a single, consistent total — that
   is a separate reconciliation this experiment does not attempt.
3. Does NOT touch H1c (which of t=0/t=1, if either alone, is physically selected) or
   KT-8 (whether any zero mode of the untwisted `D_full` exists at all).
4. A refutation of (b) does not by itself promote (a) to a full resolution — see
   criteria above; (a) requires BOTH a structural AND a physical PASS.
