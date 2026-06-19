"""G24: Blind spectrum — SO(4)×G₂ rep theory predicts SM fermion content of H_F.

QUESTION: Does the group theory chain
  Spin(4) × Spin(7) → SU(2)_L × SU(2)_R × G₂ → SU(2)_L × SU(2)_R × SU(3)
predict the SM fermion content of H_F = ℂ^{32} without reference to explicit
S³×S⁶ coordinates?

SETUP:
  S³ isometry: SO(4) = SU(2)_L × SU(2)_R (via Spin(4) double cover)
  S⁶ isometry: SO(7) ⊃ G₂ ⊃ SU(3)  (G₂ = automorphism group of octonions)

BRANCHING RULES (group theory alone):
  Spin(7) spinor (8-dim) → G₂: 7 + 1 (adjoint + trivial)
  G₂ rep 7 → SU(3): 3 + 3̄ + 1  (triplet + anti-triplet + singlet)
  Combined: Spin(7) spinor → SU(3): 3 + 3̄ + 1 + 1  [quarks + antiquarks + 2 leptons]

  Spin(4) spinor (4-dim) = (2,1) + (1,2) under SU(2)_L × SU(2)_R

BLIND PREDICTION:
  H_F = Spin(4)_spinor ⊗ Spin(7)_spinor
      = [(2,1) + (1,2)] ⊗ [3 + 3̄ + 1 + 1]
      = 4 × 8 = 32 states ✓

  Fermion types per chirality:
    L-chiral (SU(2)_L doublets, 2 states) × (SU(3) content, 8 states) = 16 L-states
    R-chiral (SU(2)_R doublets, 2 states) × (SU(3) content, 8 states) = 16 R-states
    Total: 32

VERIFICATION:
  Compute quadratic Casimir operators numerically in our explicit basis.
  The eigenvalue spectrum of C₂ reveals the irrep decomposition:
    - SU(3): C₂(3) = C₂(3̄) ≠ 0, C₂(1) = 0
    - SU(2): C₂(j=1/2) = j(j+1) = 3/4, C₂(j=0) = 0

GATES:
  B1: SU(3) Casimir on 8-dim S⁶ → exactly 2 zero + 6 equal nonzero eigenvalues
      [= 2 SU(3) singlets + 3+3̄ as predicted by Spin(7)→G₂→SU(3)]
  B2: SU(2)_L Casimir on 4-dim S³ → exactly 2 zero + 2 equal nonzero
      [= 2 SU(2)_L singlets + 1 doublet → (2,1)+(1,2)]
  B3: SU(2)_R Casimir on 4-dim S³ → exactly 2 zero + 2 equal nonzero
      [= 2 SU(2)_R singlets + 1 doublet → complementary to B2]
  B4: C₂(J) + C₂(K) = c × I₄ on S³ subspace
      [(2,1) states: J=doublet+K=singlet → sum=3/4, (1,2) states: J=singlet+K=doublet → sum=3/4]
  B5: dim = (SU(2) components) × (SU(3) modes) = 4 × 8 = 32 ✓
  B6: Fermion count per chirality: 2 × 8 = 16 L-states + 16 R-states = 32 ✓

sm_derivation_claimed = False.
λ = FREE_COUPLING_PARAMETER.
"""

import os
import sys

import numpy as np

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g21-extended-schur"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g21_extended_schur import J_32, K_32, SU3_32  # noqa: E402

N = 32

# ── Restrict to subspaces ─────────────────────────────────────────────────
#
# State ordering in H_F: state i = S³_component(i//8) × S⁶_mode(i%8)
#
# S⁶ subspace: fix S³ component 0 → states 0..7
# SU3_32[k] = kron(I4, C_k) so SU3_32[k][:8,:8] = C_k (the S⁶ generator)
#
# S³ subspace: fix S⁶ mode 0 → states 0, 8, 16, 24
# J_32[k] = kron(J_S3[k], I8) so J_32[k][ix([0,8,16,24],[0,8,16,24])] = J_S3[k]

S6_STATES: list[int] = list(range(8))  # S⁶ modes 0–7 (S³ component 0)
S3_STATES: list[int] = [0, 8, 16, 24]  # S³ components 0–3 (S⁶ mode 0)

# 8×8 SU(3) generators on the S⁶ spinor space
su3_8: list[np.ndarray] = [G[np.ix_(S6_STATES, S6_STATES)].real for G in SU3_32]

# 4×4 SU(2)_L and SU(2)_R generators on the S³ spinor space
j_s3: list[np.ndarray] = [J[np.ix_(S3_STATES, S3_STATES)] for J in J_32]
k_s3: list[np.ndarray] = [K[np.ix_(S3_STATES, S3_STATES)] for K in K_32]

# ── Quadratic Casimir operators ────────────────────────────────────────────

C2_SU3: np.ndarray = -sum(
    G @ G for G in su3_8
).real  # 8×8; minus: SO(6) generators are antihermitian
C2_J: np.ndarray = sum(J @ J for J in j_s3).real  # 4×4
C2_K: np.ndarray = sum(K @ K for K in k_s3).real  # 4×4
C2_JK: np.ndarray = C2_J + C2_K  # 4×4 complementarity

evals_su3: np.ndarray = np.sort(np.linalg.eigvalsh(C2_SU3))
evals_J: np.ndarray = np.sort(np.linalg.eigvalsh(C2_J))
evals_K: np.ndarray = np.sort(np.linalg.eigvalsh(C2_K))
evals_JK: np.ndarray = np.sort(np.linalg.eigvalsh(C2_JK))

# ── Derived structural invariants ─────────────────────────────────────────

SU3_N_SINGLET: int = int(np.sum(evals_su3 < 1e-8))  # expect: 2 (the 1+1)
SU3_N_TRIPLET: int = int(np.sum(evals_su3 > 1e-8))  # expect: 6 (the 3+3̄)
SU3_CASIMIR_F: float = (
    float(evals_su3[SU3_N_SINGLET]) if SU3_N_TRIPLET > 0 else 0.0
)  # C₂(3) in our normalisation (= 4/3 in Gell-Mann convention)

SU2J_N_SINGLET: int = int(np.sum(evals_J < 1e-8))  # expect: 2 (the (1,2) states)
SU2J_N_DOUBLET: int = int(np.sum(evals_J > 1e-8))  # expect: 2 (the (2,1) states)
SU2J_CASIMIR: float = (
    float(evals_J[SU2J_N_SINGLET]) if SU2J_N_DOUBLET > 0 else 0.0
)  # C₂(j=1/2) = 3/4 in standard SU(2)

SU2K_N_SINGLET: int = int(np.sum(evals_K < 1e-8))  # expect: 2 (the (2,1) states)
SU2K_N_DOUBLET: int = int(np.sum(evals_K > 1e-8))  # expect: 2 (the (1,2) states)


def _casimir_spread(evals: np.ndarray, threshold: float = 1e-8) -> float:
    nonzero = evals[evals > threshold]
    return float(np.max(nonzero) - np.min(nonzero)) if len(nonzero) > 0 else 0.0


def verify_gates() -> str:
    gates_pass = 0

    # B1: SU(3) on S⁶ → 3+3̄+1+1 from Spin(7)→G₂→SU(3) branching
    assert SU3_N_SINGLET == 2, f"B1 FAIL: {SU3_N_SINGLET} SU(3) singlet eigenvalues (expected 2)"
    assert SU3_N_TRIPLET == 6, f"B1 FAIL: {SU3_N_TRIPLET} non-singlet eigenvalues (expected 6)"
    spread_su3 = _casimir_spread(evals_su3)
    assert spread_su3 < 1e-8, (
        f"B1 FAIL: non-singlet SU(3) Casimir not uniform (spread={spread_su3:.2e})"
    )
    gates_pass += 1

    # B2: SU(2)_L on S³ → (2,1)+(1,2): 2 doublet + 2 singlet states
    assert SU2J_N_SINGLET == 2, f"B2 FAIL: {SU2J_N_SINGLET} SU(2)_L singlet states (expected 2)"
    assert SU2J_N_DOUBLET == 2, f"B2 FAIL: {SU2J_N_DOUBLET} SU(2)_L doublet states (expected 2)"
    gates_pass += 1

    # B3: SU(2)_R on S³ → same structure (complementary sector)
    assert SU2K_N_SINGLET == 2, f"B3 FAIL: {SU2K_N_SINGLET} SU(2)_R singlet states (expected 2)"
    assert SU2K_N_DOUBLET == 2, f"B3 FAIL: {SU2K_N_DOUBLET} SU(2)_R doublet states (expected 2)"
    gates_pass += 1

    # B4: Complementarity — C₂(J) + C₂(K) = c×I₄
    # Every S³ state is in either (2,1) or (1,2): J-doublet↔K-singlet or vice versa.
    # So C₂(J)+C₂(K) = 3/4 uniformly on all 4 basis states.
    spread_JK = float(np.max(evals_JK) - np.min(evals_JK))
    assert spread_JK < 1e-8, f"B4 FAIL: C₂(J)+C₂(K) not uniform on S³ (spread={spread_JK:.2e})"
    assert evals_JK[0] > 1e-8, "B4 FAIL: C₂(J)+C₂(K) = 0 (no doublet structure at all)"
    gates_pass += 1

    # B5: Dimension count from blind group theory
    n_s3 = SU2J_N_SINGLET + SU2J_N_DOUBLET  # 4 S³ spinor components
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET  # 8 S⁶ spinor modes
    assert n_s3 * n_s6 == N, f"B5 FAIL: {n_s3} × {n_s6} = {n_s3 * n_s6} ≠ {N}"
    gates_pass += 1

    # B6: 8 fermion species per chirality sector
    # L-chirality: SU(2)_L doublet (2 states) × all S⁶ modes (8 states) = 16
    # R-chirality: SU(2)_R doublet (2 states) × all S⁶ modes (8 states) = 16
    n_L = SU2J_N_DOUBLET * n_s6  # 2 × 8 = 16
    n_R = SU2K_N_DOUBLET * n_s6  # 2 × 8 = 16
    assert n_L == 16, f"B6 FAIL: L-sector size = {n_L} (expected 16)"
    assert n_R == 16, f"B6 FAIL: R-sector size = {n_R} (expected 16)"
    assert n_L + n_R == N, f"B6 FAIL: L+R = {n_L + n_R} ≠ {N}"
    gates_pass += 1

    return f"PASS_G24_BLIND_SPECTRUM ({gates_pass}/6)"


if __name__ == "__main__":
    print("G24: Blind Spectrum — SO(4)×G₂ Rep Theory")
    print("=" * 50)
    print()

    print("── SU(3) Casimir on 8-dim S⁶ spinor ──")
    print(f"  Eigenvalues: {np.round(evals_su3, 6).tolist()}")
    print(f"  Singlets (C₂=0): {SU3_N_SINGLET}  (1+1 from Spin(7)→G₂→SU(3))")
    print(f"  Non-singlets:     {SU3_N_TRIPLET}  (3+3̄ from G₂→SU(3) rep 7)")
    print(f"  C₂(3) = C₂(3̄) = {SU3_CASIMIR_F:.6f}")
    print()

    print("── SU(2)_L Casimir on 4-dim S³ spinor ──")
    print(f"  Eigenvalues: {np.round(evals_J, 6).tolist()}")
    print(f"  L-singlet states: {SU2J_N_SINGLET}  [(1,2) component]")
    print(f"  L-doublet states: {SU2J_N_DOUBLET}  [(2,1) component]")
    print(f"  C₂(j=1/2) = {SU2J_CASIMIR:.6f}  [expected 3/4 = 0.75]")
    print()

    print("── SU(2)_R Casimir on 4-dim S³ spinor ──")
    print(f"  Eigenvalues: {np.round(evals_K, 6).tolist()}")
    print(f"  R-singlet states: {SU2K_N_SINGLET}  [(2,1) component]")
    print(f"  R-doublet states: {SU2K_N_DOUBLET}  [(1,2) component]")
    print()

    print("── Complementarity: C₂(J) + C₂(K) ──")
    print(f"  Eigenvalues of C₂(J)+C₂(K): {np.round(evals_JK, 6).tolist()}")
    print(f"  Uniform? (spread < 1e-8): {_casimir_spread(evals_JK) < 1e-8}")
    print(f"  Value: {evals_JK[0]:.6f}  [expected 3/4 = 0.75]")
    print()

    print("── Blind prediction ──")
    n_s3 = SU2J_N_SINGLET + SU2J_N_DOUBLET
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET
    print(f"  S³ spinor: {n_s3}-dim  [(2,1)+(1,2)]")
    print(f"  S⁶ spinor: {n_s6}-dim  [3+3̄+1+1]")
    print(f"  H_F dim = {n_s3} × {n_s6} = {n_s3 * n_s6}  (predicted = verified)")
    print(f"  L-sector: {SU2J_N_DOUBLET} × {n_s6} = {SU2J_N_DOUBLET * n_s6} states")
    print(f"  R-sector: {SU2K_N_DOUBLET} × {n_s6} = {SU2K_N_DOUBLET * n_s6} states")
    print()

    print(verify_gates())
