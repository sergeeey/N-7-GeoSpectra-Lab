# C241 decision: filed as a consistency / bookkeeping note, not PROMOTE (scope: the poster's 32 states plus the standard Y)

Script hypercharge_on_poster_32.py, log run_output_c241.txt (exit 0, 11 PASS; no self-control is independent evidence, see the skeptic review).

Results [VERIFIED-tool, numerical, tolerance 1e-12]:
- Y = T³_R + (B−L)/2 commutes with J, K, T_i and C_i'; T³_R commutes with all of them; Q = T³_L + Y commutes with T³_L, T³_R, Y, B−L and colour.
- Electric charges on the 32 states: +2/3 ×12, −1/3 ×12, 0 ×4, −1 ×4 (u, d, ν, e with both chiralities, 3 colours, 2 spins).
- Y on the left-handed block: +1/6 ×12, −1/2 ×4; on the right-handed block: +2/3 ×6, −1/3 ×6, 0 ×2, −1 ×2.
- The states with SU(3)_C Casimir 0, SU(2)_L Casimir 0 and Y = 0 are exactly 2, right-handed, Q = 0: the right-handed neutrino. So the poster's statement "right-handed neutrino is invariant under SU(3)_C ⊗ SU(2)_L ⊗ U(1)_Y" holds under the standard definition.
- Without the (B−L)/2 term (Y = T³_R) the charges are ±1/2 only: the term is needed.

Caveat (honest reading): H1-H4 hold because the extension was chosen in the standard form; the check shows the poster's tensor structure is consistent with the standard assignment, which is bookkeeping, not a derivation of Y from harmonics. The identification of T³_R with the S³ right isometry J3R (C232) is [HYPOTHESIS]; the poster does not give it.
Skeptic concerns: none run.

After the C239 skeptic review: the slot reading (spin x chirality x isospin x colour) used here for T3R and B-L is the one suggested by the poster text "2 (spin) x 2 (chirality) x 3 (colour) x 2 (isospin)", but the poster does not print how the S3 SO(4) spinor and the SO(7) spinor sit in the slots; the check says the standard Y is consistent with THIS reading, nothing about the alternative one.

## Skeptic review (2026-11-04, context-blind; rerun reproduces the log byte for byte)
- H3 (Y, T3R, Q commute with J, K, T, C): CONFIRMED arithmetic, no evidential weight: it holds by slot structure (P_L P_R = 0, B-L matrix commutes with the embedded lambda); a nonsense Y with lepton value -5 passes it too (now shown by a check in the script).
- H1, H2 (charge and Y spectra): bookkeeping; the six Y eigenvalues are inputs. The isospin axis of T3R is free: P_R x sigma_1/2 gives the identical Q spectrum.
- H4 (nu_R is 2 right-handed states with Q = 0): holds by construction: the SU(2)_L Casimir is (3/4)(1 - g5)/2 identically, so 'Casimir 0' is the same as g5 = +1, and Y(nu_R) = 0 is the B-L input. The names (u, d, nu, e) are assigned through the input.
- H5: CONFIRMED, trivial. The decision's caveat 'by construction, bookkeeping not derivation' is stated correctly.
- Slot reading: the printed generators already fix the slots (J on slot 1, K and P_L on slot 2, sigma on slot 3, lambda on slot 4); putting T3R elsewhere does not commute with J, K, T. The real freedom is the added extension itself, not the slot reading: the caveat above is withdrawn in that form.
- Self-controls: none can fail independently; the control 'Y(nu_R) != 0' could never fire (built on a list filtered by |Y| < 1e-6) and was replaced by the H3 weakness check.
- Proposed test that could fail (not done): require Y to lie in the algebra spanned by the printed generators plus one explicitly stated geometric SU(2)_R (for example J3R of C232 under a written-down embedding), then ask whether the Y values come out.
- Most dangerous premise: that the poster's chirality-slot labels are the S^3 SO(4)-spinor sectors and that T3R is an S^3 isometry. Not tested here.

Ledger: C241_STANDARD_HYPERCHARGE_ADDED_TO_POSTER_32_STATES_GIVES_STANDARD_CHARGES_BY_CONSTRUCTION_NOT_A_DERIVATION
