# Assumptions (shared across Claims A, B, C)

| # | Assumption | Status | Where used |
|---|-----------|--------|-----------|
| 1 | H^6(S^6;ℤ) ≅ ℤ (top cohomology of S^6 is rank 1) | Established (standard, S^6 compact orientable 6-manifold) | Claim A step 1 |
| 2 | H²(S^6)=H⁴(S^6)=0 ⟹ c₁=c₂=0 for any SU(3)-homogeneous bundle | Established [G50] | Claim A, prior candidate cert |
| 3 | c₃(T^{1,0}S^6) = χ(S^6) = 2 (Chern-Gauss-Bonnet) | Established [G33] | Prior candidate cert; not re-derived here |
| 4 | Â(S^6) = 1 exact | Established [G73] | Prior candidate cert; not re-derived here |
| 5 | The physically relevant twisted Dirac operator on a reducible SU(3)-homogeneous bundle ⊕E_i is the STANDARD one built from a block-diagonal connection ∇_E=⊕∇_{E_i}, D_E=c∘∇_E | Assumed for Claim C's frozen scope — NOT proved to be the only possible SU(3)-equivariant Dirac-type operator | Claim C |
| 6 | Schur's lemma forbids a nonzero ZERO-ORDER equivariant intertwiner between inequivalent irreps V_i→V_j | Established (standard rep theory) | Claim C — but insufficient alone; does not forbid FIRST-ORDER symbols T*S^6⊗V_i→V_j |

**Note on assumption 5/6 interaction (the correction that motivated this round):**
Assumption 6 only rules out a zero-order off-diagonal term. A genuine
SU(3)-equivariant first-order differential operator can have an off-diagonal
symbol built from the tangent representation (T*S^6⊗V_i→V_j can be nonzero
even when V_i≇V_j, if the tensor product T*S^6⊗V_i contains a copy of V_j).
Whether such an intertwiner exists for the specific pairs in play (e.g.
T*S^6⊗3̄ ⊇ 6?) is an open representation-theoretic question, not resolved by
Schur's lemma, and not attempted in this round — see `claim-C-exact-chirality.md`
§ Open Extension.
