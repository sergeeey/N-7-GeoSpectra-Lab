# C237 decision: PROMOTE as exact computation (scope: four sampled points, polynomials of degree ≤ 4)

Script: vacuum_point_stabilizer.py, log run_output_c237.txt (exit 0, 39 PASS, 4 self-controls CAUGHT).

Result [VERIFIED-tool, exact sympy]:
- At (1,0,0,0), (½,½,½,½), (1/3,2/3,2/3,0), (0,0,0,1): all six motion fields are tangent, rank 3 (transitive), stabilizer algebra dimension 3; every stabilizer vector satisfies β = g⁻¹αg; at (1,0,0,0) it is the diagonal α = β.
- SU(2)_L alone and SU(2)_R alone act freely (rank 3) at every sampled point.
- Invariant polynomials of SU(2)_L × SU(2)_R on (a,b,c,d), degrees 1..4: dimensions 0, 1, 0, 1 (r², r⁴ only).
- Hessian of λ(r² − v²)² at (v,0,0,0) is diag(8λv²,0,0,0); its kernel equals the span of the three broken (axial) directions; the massive direction at P0 = (1,0,0,0) is the coordinate a (the singlet of C236 only because the pole was placed on the a-axis).
- Stabilizer on R⁴ at (1,0,0,0): Casimir 0 on the normal direction, 2·1 on the tangent block (b,c,d) (triplet).

Representation-level: the choice of the point is a gauge choice for SU(2)_L × SU(2)_R (transitive action, conjugate stabilizers); what matters physically is only the stabilizer class (diagonal SU(2)) and the split 3 + 1.

Interpretation-level, NOT established: that this is Tom's "redefinition of fields about a vacuum point", that the triplet corresponds to Goldstone-like modes of his model, or that "nonlinear realisation" in his sense means the constraint r = const (which removes the singlet mode). All depend on his definitions.

Link to Q4/C236: the same split 1 ⊕ 3 under SU(2)_diag appears (a vs b,c,d); interpretation-level and WEAKENED by the skeptic: the split a vs (b,c,d) appears because the vacuum point was put at P0; at another vacuum point the massive direction is u, not a. Identifying a target-space field direction with a function on S³ goes through a representation isomorphism and is gauge-dependent. Whether Tom means this is [UNKNOWN].

Skeptic concerns: none run yet.

## Skeptic review (2026-11-04, context-blind, independent rerun reproduces the log byte for byte)
- Core math (transitivity, 3-dim stabilizer, invariant counts 0,1,0,1, Hessian, 3+1 split): CONFIRMED-REAL. Accepted limitations: (i) transitivity follows from the left action alone, the four sampled points add nothing; (ii) the check "beta = g^-1 alpha g" is a tautology once rank = 3 (the kernel of the motion map is that equation); (iii) the Hessian result cannot discriminate: any SO(4)-invariant f(r^2) has Hessian 4 f'' v^2 e_a e_a^T at a minimum, so "kernel = broken directions" is Goldstone's theorem for the chosen potential; no non-invariant potential was tested.
- Link to C236 "massive direction = fourth harmonic": Accepted, downgraded to interpretation-level (text above corrected).
- Self-controls are negations of positive checks: no independent evidence. Accepted.

Ledger: C237_VACUUM_POINT_STABILIZER_IS_DIAGONAL_SU2_ACTION_TRANSITIVE_INVARIANTS_ONLY_R2_THREE_PLUS_ONE_SPLIT
