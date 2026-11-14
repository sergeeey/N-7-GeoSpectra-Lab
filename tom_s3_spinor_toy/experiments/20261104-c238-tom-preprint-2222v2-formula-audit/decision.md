# C238 decision: PROMOTE as an exact check of the preprint's algebra (scope: statements listed in claim.md)

Script: preprint_formula_audit.py, log run_output_c238.txt (exit 0, 26 PASS, 5 self-controls CAUGHT). Two vacuous checks in the first draft (one compared with True, one true for any variation) were found before recording and replaced.

Results [VERIFIED-tool, exact sympy]:
- A1 SIGN MISMATCH INSIDE THE PAPER: eq (3) (rotation "as a diffeomorphism", x' = x cos ω + y sin ω, y' = −x sin ω + y cos ω) maps θ → θ − ω, but eq (5) says θ → θ + ω. In the paper a diffeomorphism and its covariance share one formula by construction (eqs 1 = 2, 3 = 4), so (3) = (4) is not evidence about which of (3), (5) is the slip. The paper splits into {(3), Figure 4, (4), (6), Figure 5} (clockwise, θ → θ − ω) and {(5), (13)} (θ → θ + ω; eq 13 drags V'(θ) = V(θ − δθ)). Which side is the misprint is not decided here. Same in v1. Status: [UNRESOLVED], an unresolved misprint/convention slip. Not to be corrected on his behalf.
- A2 the worked examples (21)-(30) are numerically correct: V(A) = (−4, 12); V_r = 13, V_θ = 13/2; A moves to θ' = π/2 with V_θ unchanged.
- A3 eq (14) ∂_θ = x∂_y − y∂_x is correct. Eq (57) as printed ("iL_z = x∂_y − y∂_z = ∂_φ") has a misprint: y∂_z should be y∂_x. Eq (54) λ = in correct.
- A4 eq (60) is the metric induced by the embedding (59). Eqs (62)-(63) are the infinitesimal rotation by −θ (the sign convention of the paper's passive/inverse style), keep the point on the sphere, are Killing for (60), and tend to (65)-(68) as r → ∞.
- A5 the "straightforward generalisation to S^N" works for S³: P_a = z∂_a and M_ab close as so(4): [P_a,P_b] = −M_ab, [M_ab,P_c] = δ_bc P_a − δ_ac P_b; all six are Killing for g_ab = δ_ab + q_a q_b/(r² − q²); [P_a/r, P_b/r] = −M_ab/r² → 0 (the translations of the decompactification limit).
- A6 the counting claim of §5.5 is correct for N₂ = 1..8: the commutant of the Cartan subalgebra of so(N₂) inside so(N₂+1) has exactly one more generator iff N₂ is odd.
- A7 For N₂ = 3: A_L3 − A_R3 and A_L3 + A_R3 are single-plane rotations of R⁴ ((c,d)-plane: stabiliser of (1,0,0,0); (a,b)-plane: the extra broken commuting generator). On the degree-n harmonics the joint spectrum of (iX₃, iY₃) is all pairs (m_L, m_R), each once, n = 1,2,3. In the rank reading (extra generator commuting with the Cartan subalgebra of so(N₂), which is what A6 and the script test) the extra generator for S³ is the broken one, m_L − m_R at function level. WEAKENED by the skeptic and re-checked by tool: X₃ − Y₃ commutes with D₃ but NOT with the diagonal Casimir ([X₃−Y₃, Cas_diag] ≠ 0 at degree 1), so it is not simultaneously diagonal with (l, m) of the diagonal SO(3). Tom's text says the extra number is determined simultaneously with the quantum numbers of SO(N₂), which label its harmonics (l and m, eqs 55-56). Under that stronger reading no element of so(4) other than D₃ itself qualifies, and the identification m_L − m_R is NOT established. Do not write "his extra quantum number is m_L − m_R" anywhere.

Consequences for our tracks (representation-level):
- C237 (stabiliser = diagonal SU(2) = Tom's so(N₂), broken triplet = his N₂ "translations" that become rotations) is the S³ case of §5.4-5.5; the link "fourth harmonic a of C236 = dependent coordinate z" holds only when the north pole is placed on the a-axis (gauge P0 = (1,0,0,0)); at another vacuum point the massive direction is u, not a. [HYPOTHESIS]
- His footnote 2: "currently investigating harmonics with half-integer values of l for two- and three-spheres" (new in v2; absent in v1). On S³ the scalar sectors (s,s) with half-integer s exist (degree odd); whether his "l" is s or the diagonal spin (always an integer in s ⊗ s) is [UNKNOWN].

Interpretation-level, NOT established: that the chapter's results coincide with the preprint's; that his "vacuum point" of the call is the north pole of §5.4; that the extra discrete quantum number is physical.

Skeptic concerns: none run yet.

## Skeptic review (2026-11-04, context-blind, independent rerun: all three scripts reproduce byte for byte)
- A1: CONFIRMED-REAL in the printed paper (pages 5-6 read as images, v1 and v2 identical). Concern "the script label says (3) is the covariance, not the active map": Accepted and fixed (script label made neutral, decision text above corrected).
- A2-A5: CONFIRMED-REAL. Accepted limitations: the (54) check verifies one instance; the (62)-(63) -> (65)-(68) check tests z/r -> 1 only (the paper's limit also needs l = theta r fixed); the A3 control reads y d_z as zero on f(x,y), a chosen reading.
- A6: CONFIRMED in the rank reading; N2 = 1 is hard-coded (cdim, rk = 1, 0), N2 = 2..8 computed. Accepted.
- A7: WEAKENED (see above). Accepted and re-verified by my own check (scratch a7_check.py: [X3-Y3, D3] = 0, [X3-Y3, Cas_diag] != 0).
- Cross-cutting: every listed self-control is the negation of a positive check on the same run, so the CAUGHT count adds no evidence beyond the positive checks. Accepted.
- Most dangerous premise: that Tom's objects are the ones computed here (X+Y diagonal, north pole (1,0,0,0), m_L - m_R). Marked as interpretation-level [UNRESOLVED].

Ledger: C238_PREPRINT_ALGEBRA_CHECKED_EQ3_EQ5_SIGN_MISMATCH_EXTRA_GENERATOR_ONLY_IN_RANK_READING
