"""G23: Chiral decomposition of H_F — SM chirality from the Z₂ grading γ_F.

QUESTION: Does the finite grading γ_F (from G18) produce the correct SM chirality
assignment, and is the Witten index (dim H^+ − dim H^−) zero?

SETUP:
  H_F = ℂ^{32} = S³_4 ⊗ S⁶_8 (one SM generation, from G11–G21)
  γ_F = Z₂ grading on H_F (from G18, KO-dim 6 spectral triple)
  H_F^+ = {ψ : γ_F ψ = +ψ}  (R-chirality sector, S³ components 2,3)
  H_F^- = {ψ : γ_F ψ = −ψ}  (L-chirality sector, S³ components 0,1)

ANALYTIC PREDICTIONS:
  (1) γ_F = diag(−I_{16}, +I_{16}): L-sector (0-15) carries γ_F = −1,
      R-sector (16-31) carries γ_F = +1.

  (2) Witten index = dim(H_F^+) − dim(H_F^−) = 16 − 16 = 0.
      PHYSICAL MEANING: On a compact manifold with positive curvature (S³×S⁶),
      the Atiyah-Singer index theorem forces ind(D) = 0 (Witten vanishing theorem 1985).
      Our finite spectral triple respects this: equal numbers of L and R spinors.

  (3) {D_F, γ_F} = 0: The Yukawa operator maps L↔R.
      This is the signature of a chirality-breaking Dirac operator — exactly right.
      D_F: H_F^- → H_F^+ and H_F^+ → H_F^-.

  (4) {J_F, γ_F} = 0: CPT flips chirality (KO-dimension 6 axiom from G18).

  (5) [γ_F, G] = 0 for all G in SU(2)_L × SU(2)_R × SU(3) × U(1)_{B-L}:
      Chirality is a gauge-invariant quantum number.

  (6) SM chirality assignment:
      H_F^- (γ_F = −1, L-sector): SU(2)_L doublets {ν_L, e_L, d̄_L, u_L}
      H_F^+ (γ_F = +1, R-sector): SU(2)_R doublets {ν_R, e_R, d̄_R, u_R}
      → SU(2)_L acts EXCLUSIVELY within H_F^-
      → SU(2)_R acts EXCLUSIVELY within H_F^+
      → SU(3) × U(1)_{B-L} act within EACH sector independently.

  The SM chirality is NOT from an asymmetry in spinor count (Witten says that's 0),
  but from the DIFFERENT GAUGE QUANTUM NUMBERS of H_F^+ and H_F^-.
  This is the geometric origin of the SM chiral gauge theory from S³×S⁶.

GATES:
  C1: γ_F² = I (Z₂ grading)
  C2: {D_F, γ_F} = 0 (Yukawa flips chirality: key off-diagonal structure)
  C3: {J_F, γ_F} = 0 (KO-dim 6 relation: CPT flips chirality)
  C4: [γ_F, G] = 0 for all 15 Pati-Salam generators (chirality is gauge-invariant)
  C5: Witten index = 0 (dim H_F^+ = dim H_F^- = 16)
  C6: SU(2)_L ⊂ End(H_F^-) only (SU(2)_L acts on left-chiral sector)
  C7: SU(2)_R ⊂ End(H_F^+) only (SU(2)_R acts on right-chiral sector)

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

from g18_ncg import gamma_F as gamma_F_sym, J_F as J_F_sym, YUKAWA_PAIRS  # noqa: E402
from g21_extended_schur import J_32, K_32, SU3_32, BL_32, _to_np  # noqa: E402

N = 32


# ── Build operators numerically ────────────────────────────────────────────────

gamma_F: np.ndarray = _to_np(gamma_F_sym)
J_F: np.ndarray = _to_np(J_F_sym)

D_F: np.ndarray = np.zeros((N, N), dtype=complex)
for i, j, c in YUKAWA_PAIRS:
    D_F[i, j] = D_F[j, i] = 1.0  # all couplings = 1

GENS_PATI_SALAM: list[np.ndarray] = J_32 + K_32 + SU3_32 + [BL_32]

# ── Chiral projectors ─────────────────────────────────────────────────────────

gamma_diag: np.ndarray = np.diag(gamma_F).real
L_STATES: np.ndarray = np.where(gamma_diag < 0)[0]  # γ_F = −1: L-chirality
R_STATES: np.ndarray = np.where(gamma_diag > 0)[0]  # γ_F = +1: R-chirality

DIM_L: int = len(L_STATES)
DIM_R: int = len(R_STATES)
WITTEN_INDEX: int = DIM_R - DIM_L  # convention: ind = dim(H^+) − dim(H^-)


# ── Gate verification ─────────────────────────────────────────────────────────


def _anticomm_max(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.max(np.abs(A @ B + B @ A)))


def _comm_max(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.max(np.abs(A @ B - B @ A)))


def verify_gates() -> str:
    gates_pass = 0

    # C1: γ_F² = I
    err = float(np.max(np.abs(gamma_F @ gamma_F - np.eye(N))))
    assert err < 1e-12, f"C1 FAIL: γ_F² ≠ I (err={err:.2e})"
    gates_pass += 1

    # C2: {D_F, γ_F} = 0 — Yukawa flips chirality
    ac = _anticomm_max(D_F, gamma_F)
    assert ac < 1e-10, f"C2 FAIL: {{D_F, γ_F}} ≠ 0 (max={ac:.2e})"
    gates_pass += 1

    # C3: {J_F, γ_F} = 0 — KO-dim 6 relation
    ac = _anticomm_max(J_F, gamma_F)
    assert ac < 1e-12, f"C3 FAIL: {{J_F, γ_F}} ≠ 0 (max={ac:.2e})"
    gates_pass += 1

    # C4: [γ_F, G] = 0 for all 15 Pati-Salam generators
    worst = max(_comm_max(gamma_F, G) for G in GENS_PATI_SALAM)
    assert worst < 1e-10, f"C4 FAIL: [γ_F, G] ≠ 0 for some G (max={worst:.2e})"
    gates_pass += 1

    # C5: Witten index = 0 (dim H_F^+ = dim H_F^- = 16)
    assert DIM_L == 16, f"C5 FAIL: dim(H_F^-) = {DIM_L} (expected 16)"
    assert DIM_R == 16, f"C5 FAIL: dim(H_F^+) = {DIM_R} (expected 16)"
    assert WITTEN_INDEX == 0, f"C5 FAIL: Witten index = {WITTEN_INDEX} (expected 0)"
    gates_pass += 1

    # C6: SU(2)_L acts within H_F^- only (off-diagonal L→R and R→L blocks are zero)
    for k, J in enumerate(J_32):
        J_on_R = J[np.ix_(R_STATES, R_STATES)]
        J_cross = J[np.ix_(R_STATES, L_STATES)]
        assert np.max(np.abs(J_on_R)) < 1e-10, (
            f"C6 FAIL: SU(2)_L generator J_{k + 1} acts on H_F^+ (R-sector)"
        )
        assert np.max(np.abs(J_cross)) < 1e-10, (
            f"C6 FAIL: SU(2)_L generator J_{k + 1} crosses chirality sectors"
        )
    gates_pass += 1

    # C7: SU(2)_R acts within H_F^+ only
    for k, K in enumerate(K_32):
        K_on_L = K[np.ix_(L_STATES, L_STATES)]
        K_cross = K[np.ix_(L_STATES, R_STATES)]
        assert np.max(np.abs(K_on_L)) < 1e-10, (
            f"C7 FAIL: SU(2)_R generator K_{k + 1} acts on H_F^- (L-sector)"
        )
        assert np.max(np.abs(K_cross)) < 1e-10, (
            f"C7 FAIL: SU(2)_R generator K_{k + 1} crosses chirality sectors"
        )
    gates_pass += 1

    return f"PASS_G23_CHIRALITY ({gates_pass}/7)"


# ── Main ──────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    print("G23: Chiral Decomposition of H_F")
    print("=" * 50)
    print(f"N = {N}")
    print()

    print("γ_F diagonal (first 32 entries):")
    print(f"  {np.diag(gamma_F).real.astype(int).tolist()}")
    print()

    print("Chiral sectors:")
    print(f"  H_F^- (γ_F=−1, L-chirality): states {L_STATES.tolist()}")
    print(f"  H_F^+ (γ_F=+1, R-chirality): states {R_STATES.tolist()}")
    print(f"  dim(H_F^-) = {DIM_L}, dim(H_F^+) = {DIM_R}")
    print(f"  Witten index = dim(H^+) − dim(H^-) = {WITTEN_INDEX}")
    print()

    print("Key algebraic relations:")
    print(f"  γ_F² = I:          {np.allclose(gamma_F @ gamma_F, np.eye(N))}")
    print(f"  {{D_F, γ_F}} = 0:  {np.allclose(D_F @ gamma_F + gamma_F @ D_F, 0)}")
    print(f"  {{J_F, γ_F}} = 0:  {np.allclose(J_F @ gamma_F + gamma_F @ J_F, 0)}")
    worst_comm = max(_comm_max(gamma_F, G) for G in GENS_PATI_SALAM)
    print(f"  [γ_F, all gens]:   max = {worst_comm:.3e}  (= 0: chirality is gauge-invariant)")
    print()

    print("D_F chirality structure:")
    D_LL = D_F[np.ix_(L_STATES, L_STATES)]
    D_RR = D_F[np.ix_(R_STATES, R_STATES)]
    D_LR = D_F[np.ix_(L_STATES, R_STATES)]
    D_RL = D_F[np.ix_(R_STATES, L_STATES)]
    print(f"  D_F[L,L] (diagonal L): max = {np.max(np.abs(D_LL)):.3e}  (= 0: no mass in L sector)")
    print(f"  D_F[R,R] (diagonal R): max = {np.max(np.abs(D_RR)):.3e}  (= 0: no mass in R sector)")
    print(f"  D_F[L,R] (off-diag):   max = {np.max(np.abs(D_LR)):.3e}  (= 1: Yukawa L←R)")
    print(f"  D_F[R,L] (off-diag):   max = {np.max(np.abs(D_RL)):.3e}  (= 1: Yukawa R←L)")
    print()

    print("SM chirality assignment (from gauge sector action):")
    print("  SU(2)_L ⊂ End(H_F^-): left-chiral doublets {ν_L, e_L, d̄_L, u_L}")
    print("  SU(2)_R ⊂ End(H_F^+): right-chiral singlets {ν_R, e_R, d̄_R, u_R}")
    print()
    print("  Physical mechanism: SM chirality ≠ spinor count asymmetry")
    print("  (Witten index = 0: equal L and R spinors on S³×S⁶)")
    print("  SM chirality = different gauge quantum numbers for H_F^+ vs H_F^-")
    print()

    print(verify_gates())
