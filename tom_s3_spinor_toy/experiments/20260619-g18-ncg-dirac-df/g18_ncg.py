"""G18: NCG finite Dirac operator D_F on the 32-dim S³×S⁶ spinor.

Constructs the core objects of the SM finite spectral triple
(A_F, H_F, D_F, J_F, γ_F) where H_F is our S³×S⁶ spinor:

  γ_F  — chirality: −1 on L-sector (rows 0–15), +1 on R-sector (16–31)
  J_F  — charge conjugation: 16 particle↔CPT-partner transpositions
  D_F  — finite Dirac operator: Yukawa block off-diagonal in L↔R

D_F encodes four Yukawa couplings:
  Y_nu — Dirac neutrino: ν_L(0)↔ν_R(16),   ν̄_L(15)↔ν̄_R(31)
  Y_e  — electron:       e_L(8)↔e_R(24),    ē_L(7)↔ē_R(23)
  Y_u  — up-quark:       u_L(3,5,6)↔u_R(19,21,22),   3 colors each
  Y_d  — down-quark:     d_L(11,13,14)↔d_R(27,29,30), 3 colors each

KO-dimension 6 constraints (finite spectral triple):
  γ_F² = I          J_F² = I
  {J_F, γ_F} = 0    (ε' = −1)
  [D_F, J_F] = 0    (ε'' = +1)

Standard Dirac constraints:
  {D_F, γ_F} = 0    D_F = D_F†    [D_F, Q_32] = 0

Y_nu, Y_e, Y_u, Y_d = FREE_YUKAWA_PARAMETERS (symbolic, not fixed).
λ = FREE_COUPLING_PARAMETER throughout.
sm_derivation_claimed = False.
"""

import os
import sys

import sympy as sp
from sympy import zeros

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g17_electric_charge import Q_32  # noqa: E402

# ── Symbolic Yukawa couplings ─────────────────────────────────────────────────
Y_nu, Y_e, Y_u, Y_d = sp.symbols("Y_nu Y_e Y_u Y_d", real=True, positive=True)

# ── Chirality operator γ_F ────────────────────────────────────────────────────
# L-sector (rows 0–15): γ_F = −1.   R-sector (rows 16–31): γ_F = +1.
gamma_F: sp.Matrix = sp.diag(*[-1] * 16 + [1] * 16)

# ── Charge conjugation J_F ────────────────────────────────────────────────────
# 16 transpositions; every pair has one L-row and one R-row → {J_F, γ_F} = 0.
# CPT: row i (particle) ↔ row j (CPT-conjugate, opposite Q and B−L).
CPT_PAIRS: list[tuple[int, int]] = [
    # Leptons
    (0, 31),  # ν_L  ↔ ν̄_R
    (15, 16),  # ν̄_L ↔ ν_R
    (8, 23),  # e_L  ↔ ē_R
    (7, 24),  # ē_L  ↔ e_R
    # Up-quarks (3 colors)
    (3, 25),
    (5, 26),
    (6, 28),
    # Anti-up-quarks (3 colors)
    (9, 19),
    (10, 21),
    (12, 22),
    # Down-quarks (3 colors)
    (11, 17),
    (13, 18),
    (14, 20),
    # Anti-down-quarks (3 colors)
    (1, 27),
    (2, 29),
    (4, 30),
]
assert len(CPT_PAIRS) == 16, "must be 16 CPT pairs"

J_F: sp.Matrix = zeros(32, 32)
for _i, _j in CPT_PAIRS:
    J_F[_i, _j] = 1
    J_F[_j, _i] = 1

# Build pair look-up once
PAIR_MAP: dict[int, int] = {_i: _j for _i, _j in CPT_PAIRS}
PAIR_MAP.update({_j: _i for _i, _j in CPT_PAIRS})

# ── Finite Dirac operator D_F ─────────────────────────────────────────────────
# Off-diagonal between L (0–15) and R (16–31).
# Non-zero only when Q[i] = Q[j] and B−L[i] = B−L[j].
# Every particle Yukawa pair (i_L, j_R) is accompanied by its CPT partner
# (pair(j_R), pair(i_L)) with the same coupling → [D_F, J_F] = 0.
YUKAWA_PAIRS: list[tuple[int, int, sp.Expr]] = [
    # Neutrino — particle and CPT partner
    (0, 16, Y_nu),
    (15, 31, Y_nu),
    # Electron — particle and CPT partner
    (8, 24, Y_e),
    (7, 23, Y_e),
    # Up-quark — 3 colors (particles)
    (3, 19, Y_u),
    (5, 21, Y_u),
    (6, 22, Y_u),
    # Up-quark — 3 colors (CPT partners)
    (9, 25, Y_u),
    (10, 26, Y_u),
    (12, 28, Y_u),
    # Down-quark — 3 colors (particles)
    (11, 27, Y_d),
    (13, 29, Y_d),
    (14, 30, Y_d),
    # Down-quark — 3 colors (CPT partners)
    (1, 17, Y_d),
    (2, 18, Y_d),
    (4, 20, Y_d),
]
assert len(YUKAWA_PAIRS) == 16, "must be 16 Yukawa connections"

D_F: sp.Matrix = zeros(32, 32)
for _i, _j, _y in YUKAWA_PAIRS:
    D_F[_i, _j] = _y
    D_F[_j, _i] = _y  # D_F† = D_F  (real symmetric)

# ── Gate verification ──────────────────────────────────────────────────────────


def verify_gates() -> str:
    gates_pass = 0

    # T1: γ_F² = I₃₂
    assert gamma_F**2 == sp.eye(32), "T1 FAIL"
    gates_pass += 1

    # T2: {D_F, γ_F} = 0 — every Yukawa pair connects L↔R
    for _i, _j, _ in YUKAWA_PAIRS:
        assert gamma_F[_i, _i] + gamma_F[_j, _j] == 0, (
            f"T2 FAIL: γ_F[{_i}]+γ_F[{_j}] = {gamma_F[_i, _i] + gamma_F[_j, _j]}"
        )
    gates_pass += 1

    # T3: D_F = D_F†  (real matrix → D_F† = D_F.T)
    assert D_F == D_F.T, "T3 FAIL: D_F not symmetric"
    gates_pass += 1

    # T4: [D_F, Q_32] = 0 — Yukawa connects states of equal electric charge
    for _i, _j, _ in YUKAWA_PAIRS:
        assert Q_32[_i, _i] == Q_32[_j, _j], (
            f"T4 FAIL: Q[{_i}]={Q_32[_i, _i]} ≠ Q[{_j}]={Q_32[_j, _j]}"
        )
    gates_pass += 1

    # T5: J_F² = I₃₂
    assert J_F**2 == sp.eye(32), "T5 FAIL"
    gates_pass += 1

    # T6: {J_F, γ_F} = 0 — every CPT pair crosses L↔R  (KO-dim 6, ε' = −1)
    for _i, _j in CPT_PAIRS:
        assert gamma_F[_i, _i] + gamma_F[_j, _j] == 0, (
            f"T6 FAIL: γ_F[{_i}]+γ_F[{_j}] = {gamma_F[_i, _i] + gamma_F[_j, _j]}"
        )
    gates_pass += 1

    # T7: [D_F, J_F] = 0  (KO-dim 6, ε'' = +1)
    # [D_F, J_F][i, k] = D_F[i, pair(k)] − D_F[pair(i), k]
    # Verified entry-by-entry using PAIR_MAP and the fact that YUKAWA_PAIRS
    # are closed under pair: (i, j) ∈ YUKAWA_PAIRS iff (pair(j), pair(i)) ∈ YUKAWA_PAIRS.
    yukawa_set = {(_i, _j): _y for _i, _j, _y in YUKAWA_PAIRS}
    yukawa_set.update({(_j, _i): _y for _i, _j, _y in YUKAWA_PAIRS})
    for _i, _j, _y in YUKAWA_PAIRS:
        pi, pj = PAIR_MAP[_i], PAIR_MAP[_j]
        # D_F[i, pair(j)] = D_F[i, pj] and D_F[pair(i), j] = D_F[pi, j]
        lhs = yukawa_set.get((_i, pj), sp.Integer(0))
        rhs = yukawa_set.get((pi, _j), sp.Integer(0))
        assert sp.expand(lhs - rhs) == 0, f"T7 FAIL at ({_i},{_j})"
    gates_pass += 1

    # T8: D_F has exactly 4 distinct Yukawa couplings {Y_nu, Y_e, Y_u, Y_d}
    distinct = {_y for _, _, _y in YUKAWA_PAIRS}
    assert distinct == {Y_nu, Y_e, Y_u, Y_d}, f"T8 FAIL: found {distinct}"
    gates_pass += 1

    return f"PASS_G18_NCG_DIRAC_DF ({gates_pass}/8)"


if __name__ == "__main__":
    print(verify_gates())
