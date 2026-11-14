# C239 decision: PROMOTE as bookkeeping check (scope: the explicit generators and spinor statements on the poster)

Script: poster_fermion_bookkeeping.py, log run_output_c239.txt (exit 0, 23 PASS). Independent evidence from controls: 3 (boost without the factor i; non-projector P_L; P_L = (1 - sigma_3)/2 incompatible with the boosts, the last added after the skeptic review). The other CAUGHT lines (B2 'T acts on the right-handed block', B4 'equal weight sets') are negations of checks that already passed and carry no independent information. First run crashed on a dictionary key (my script), fixed; two meaningless controls of the first draft replaced before the final run.

Results [VERIFIED-tool, numerical, tolerance 1e-12]:
- B1 The printed generators are internally consistent: J, K close into the Lorentz algebra ([K,K] = −iεJ; this closure holds for any matrix in slot 2 and does not show that slot 2 is chirality); T_i = ½(1⊗P_L⊗σ_i⊗1) close into su(2) for a projector P_L, and P_L is pinned down by [T,K] = 0 to (1 ∓ σ₁)/2 (the sign is a convention; (1 − σ₃)/2 fails [T,K] = 0, tool-checked); C_i' = ½(1⊗1⊗1⊗λ_i') close into su(3); T, C commute with J, K and with each other.
- B2 Under Lorentz × SU(2)_L × SU(3)_C the 32 states split as 16 left-handed (SU(2)_L doublets, Casimir ¾) + 16 right-handed (singlets), and 24 coloured (Casimir 4/3) + 8 colourless. This is the standard-model content of one generation with a right-handed neutrino (particle states, no antiparticles). It holds for any rank-1 P_L and any 3 + 1 embedding of λ, so this check cannot fail and should not be counted as evidence. It is true BY CONSTRUCTION: the matrices were built from the known charges ("Can then use known charges to construct explicit matrix forms", poster). So it is bookkeeping, not evidence that harmonics produce it.
- B3 The count 2·2·3·2 = 24, 2·2 = 4, 2·2 = 4, 32 = 2·2·2·4 is correct. Spin(4) Dirac spinor = (½,0) ⊕ (0,½) under su(2)_L ⊕ su(2)_R (poster S1 correct).
- B4 Spin(7) 8-component spinor restricted to Spin(6) = 4 ⊕ 4̄, with inequivalent blocks (weight sets (+++,+−−,−+−,−−+) and (−−−,−++,+−+,++−)); 4̄ weights are the negatives of 4 weights. Poster S2 is correct as a statement of the content 4 ⊕ 4̄.

Findings [HYPOTHESIS; all rest on how the poster's abstract representations map onto the tensor slots of the 32-dimensional matrices, a mapping the poster does NOT print]:
1. The poster's colour generator is the identity on slots 1-3 (spin, chirality, isospin). Under the SO(10) reading the 16 restricts to (2,1,4) + (1,2,4bar), so any conjugation between 4 and 4bar belongs BETWEEN the chirality blocks (the Spin(7) spinor 8 = 4 + 4bar of the poster), not between isospin copies; treating right-handed fields as particles in the 4 is standard Pati-Salam bookkeeping. The earlier wording "most delicate step" was an overstatement and is withdrawn. What stays: the poster does not say which slot carries 4 + 4bar.
2. WITHDRAWN as stated ("the isospin factor is not the SU(2)_L of the S³ isometry"): it assumed that the SO(4) four-component spinor is spin × chirality. The poster's diagram (right-handed spinor of SO(4) <-> SU(2)_R, left-handed <-> SU(2)_L) fits equally well, or better, chirality × isospin; under that reading (skeptic probe P4) P_L ⊗ σ/2 and P_R ⊗ σ/2 close into su(2) ⊕ su(2) and the four states are (1/2,0) ⊕ (0,1/2), and T_i is exactly the SU(2)_L of the SO(4) spinor. The slot assignment is [UNKNOWN].
3. Hypercharge is not constructed on the poster (see C241 for the added standard form).
4. Poster statement "harmonics on S³ are distinguished by third generators of SU(2)_L and SU(2)_R" agrees with C236/C238 (A7): joint spectrum (m_L, m_R). [Not recomputed in C239.]

Provenance note: the poster's sha256 matches; the local file is Lawrence_Field_configs_spinors_no-go_poster.pdf (poster title: "Field configs, spinors, no-go - Tom Lawrence.pdf").

Bridge to our C235 (representation-level, from the C235 table, not recomputed here): the SO(4) spinor representations (½,0) and (0,½) of the poster appear as the sectors (j_L,k) = (½,0) [2 states, D0 = 3] and (0,½) [2 states, D0 = 0] of C²-valued fields on S³; larger sectors are bigger SO(4) representations. Whether "spinor representation of SO(4)" on the poster means these sectors or a fibre representation attached to scalar harmonics is [UNKNOWN].

Relation to project memory [MEMORY, not re-opened]: the project's Pati–Salam / SU(4) work (Rounds 90-95, 107-109) concerns SU(4) × SU(2)² on S³ × S⁶ with G₂ acting on S⁶ (stabiliser SU(3)), while the poster uses the round S⁶ with SO(7) isometry and SO(6) ≅ SU(4) stabiliser. These are different constructions; no conclusion transfers without comparison.

## Skeptic review (2026-11-04, context-blind; independent rerun reproduces the original log byte for byte; poster page 1 read)
- The coded generators match the poster's printed ones (tensor order and factors). B1, B3, B4: CONFIRMED-REAL as algebra/representation theory. B2: CONFIRMED but cannot fail (Accepted, wording above).
- Finding 1: WEAKENED (Accepted, rewritten). Finding 2: FALSIFIED as stated / overreach (Accepted, withdrawn; alternative slot reading recorded). Finding 3 confirmed. Finding 4: not recomputed here.
- Self-controls: only 2 of the original 4 were independent; one real control added. Accepted.
- Most dangerous unverified premise: the mapping of the poster's abstract representations (SO(4) 4-component spinor, SO(7) 8 = 4 + 4bar) onto the tensor slots of the 32-dimensional matrices. Not printed on the poster; any statement depending on it stays [UNKNOWN].

Ledger: C239_POSTER_32_STATE_GENERATORS_CONSISTENT_BOOKKEEPING_BY_CONSTRUCTION_SLOT_MAPPING_NOT_PRINTED
