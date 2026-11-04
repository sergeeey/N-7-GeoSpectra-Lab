# C240 decision: PROMOTE only for R1 (Schur) and R2 (sector table); R3 and R4 downgraded after the skeptic review (scope: degrees 0..1)

Script chirality_bidoublet.py, log run_output_c240.txt (exit 0, 8 PASS, 3 self-controls CAUGHT).

Results [VERIFIED-tool, exact sympy]:
- R1: the only 2×2 matrices commuting with σ₁, σ₂, σ₃ are the scalars. So there is no chirality (γ₅-like) operator on spin-½ fields of S³ itself; "left-handed / right-handed" on Tom's poster is an SO(4)-spinor label ((½,0) / (0,½)), not a property of D0 or of C².
- R2: degrees 0..1 give sectors (0,½) [2 states, D0 = 0], (½,0) [2 states, D0 = 3], (½,1) [6 states, D0 = −1]; same table as C235.
- R3 (downgraded): D0 commutes with X_k and K_k, so it is block diagonal in (j_L,k) and does not connect (0,½) with (½,0). Skeptic: the check is a tautology of the degree grading (every operator built preserves the polynomial degree, and the two sectors sit at degrees 0 and 1 and are D0's own eigenspaces); a random degree-preserving non-invariant operator passes it too. It is a statement about the grading, not a finding about D0.
- R4 (downgraded): multiplication of the (0,½) sector by the four degree-1 harmonics gives the whole degree-1 ⊗ C² space, with components of rank 2 in (½,0) and rank 6 in (½,1). Skeptic: the rank-8 statement is by construction, and the (2 + 6) split is NOT non-trivial content: the component ranks equal the dimensions of the sector projectors (the R2 table), and a random non-equivariant invertible map gives the same 2 and 6. The Clebsch-Gordan rule (0,½) ⊗ (½,½) = (½,0) ⊕ (½,1) is true textbook representation theory, not tested by this run (a degree-2 version is also vacuous: j_L is fixed by the function degree).

Representation-level (textbook, not tested here): a tensor operator in (½,½) can connect (0,½) with (½,0); the degree-1 harmonics are such an object. Necessity (Wigner-Eckart) was not tested. Interpretation-level, NOT established: that this is the correspondent's mass mechanism (his poster only plans a geometric explanation of the Higgs mechanism); the two SU(2)s here are the isometries X and K = Y + S, the (½,½) object is the fixed coordinate functions, not a dynamical field with a vacuum value. The left-right bidoublet analogy is [MEMORY].

## Skeptic review (2026-11-04, context-blind; rerun reproduces the log byte for byte)
- R1: CONFIRMED as maths (Schur), WEAKENED as worded: it tests constant 2x2 matrices only; on the function space many operators commute with spin. The real reason S^3 has no chirality is that the Clifford volume element sigma1 sigma2 sigma3 = i is a scalar in odd dimension (not shown). The poster carries chirality on its own C^2 slot, so R1 does not bear on it. Accepted.
- R2: CONFIRMED (exact), duplicates the C235 table. R3, R4: WEAKENED / FALSIFIED as stated; accepted and rewritten above.
- Self-controls: all three are negations of the positive checks (no independent evidence). Accepted.
- Most dangerous premise: that the poster's left/right labels are the S^3 SO(4)-spinor sectors (0,½)/(½,0) and that the right SU(2) is an S^3 isometry. Not tested; [UNKNOWN]. Partial support, not checked [HYPOTHESIS]: D0 - 3/2 puts (0,½) and (½,0) at the lowest Dirac levels -3/2 and +3/2.
- Filing: R1 and R2 only; not to be presented to the correspondent as results (letter rule 10, trivial).

Ledger: C240_NO_CHIRALITY_OPERATOR_ON_C2_AND_SECTOR_TABLE_DEGREES_0_1_D0_BLOCK_DIAGONAL_IS_A_GRADING_TAUTOLOGY
