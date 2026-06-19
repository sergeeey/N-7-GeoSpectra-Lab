"""G19: Higgs quantum numbers from D_F Yukawa structure on S³×S⁶.

For each Yukawa pair (i_L, j_R) in D_F (G18), the coupling ψ̄(i_L) φ ψ(j_R)
requires a scalar φ with quantum numbers dX = X[j_R] − X[i_L].

RESULTS (all 16 pairs, 8/8 gates):
  dQ   = 0          → only neutral Higgs mediates (no charged Higgs vertex)
  dBL  = 0          → Higgs is B−L singlet (color-neutral, lepton-neutral)
  |dT3L| = 1/2      → SU(2)_L doublet (half-integer, not singlet or adjoint)
  |dT3R| = 1/2      → SU(2)_R doublet
  dT3L + dT3R = 0   → anti-diagonal bidoublet pairing
  dY   = dT3R       → Y entirely from T3R component (B−L contributes nothing)

Two neutral components (dQ = 0) that appear:
  (dT3L, dT3R) = (−1/2, +1/2)  — 8 uptype pairs   [ν_L,u_L and CPT conjugates ē_L,d̄_L]
  (dT3L, dT3R) = (+1/2, −1/2)  — 8 downtype pairs  [e_L,d_L and CPT conjugates ν̄_L,ū_L]

This identifies the required Higgs as the (2, 2)₀ bidoublet of SU(2)_L × SU(2)_R.
After SU(2)_R → U(1)_T3R breaking, the neutral (Q=0) component of the bidoublet
becomes the SM Higgs doublet H with Y = +1/2: representation (1, 2)_{1/2}.

Geometric origin of dBL = 0:
  BmL_32 = kron(I₄, BmL) — the B−L operator lives entirely in the S⁶ fiber.
  Both partners (i_L, j_R) in a Yukawa pair share the SAME S⁶ fiber index
  (the L/R distinction is in S³, not S⁶), so BmL_32[j_R, j_R] = BmL_32[i_L, i_L].
  Therefore the mediating scalar has no S⁶ quantum numbers — it is a pure S³ object.

Pati-Salam breaking chain encoded in structure:
  SU(2)_L × SU(2)_R × U(1)_{B−L}   (full left-right symmetry of S³×S⁶)
    → SU(2)_L × U(1)_Y               (after SU(2)_R breaking, H gains VEV)
    → U(1)_Q                          (after EW breaking)

Sources: J₃ = G11, K₃ = G16, B−L = G15, Y = G16, Q = G17, D_F = G18.

λ = FREE_COUPLING_PARAMETER. Y_nu/Y_e/Y_u/Y_d = FREE_YUKAWA_PARAMETERS.
sm_derivation_claimed = False.
"""

import os
import sys

import sympy as sp

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g18_ncg import YUKAWA_PAIRS  # noqa: E402
from g17_electric_charge import Q_32  # noqa: E402
from g16_t3r_k3 import BmL_32, J3_32, K3_32, Y_32  # noqa: E402

half = sp.Rational(1, 2)

# ── Higgs quantum numbers for each Yukawa pair ────────────────────────────────
# dX ≡ X[j_R] − X[i_L].
# The scalar φ mediating ψ̄(i_L) φ ψ(j_R) must carry these quantum numbers.

HIGGS_QN: list[dict] = []
for _i, _j, _ in YUKAWA_PAIRS:
    HIGGS_QN.append(
        {
            "pair": (_i, _j),
            "dT3L": J3_32[_j, _j] - J3_32[_i, _i],
            "dT3R": K3_32[_j, _j] - K3_32[_i, _i],
            "dBL": BmL_32[_j, _j] - BmL_32[_i, _i],
            "dY": Y_32[_j, _j] - Y_32[_i, _i],
            "dQ": Q_32[_j, _j] - Q_32[_i, _i],
        }
    )

# The two neutral components of the (2,2)₀ bidoublet
HIGGS_COMPONENT_P = (-half, +half)  # (dT3L, dT3R) for uptype fermions
HIGGS_COMPONENT_M = (+half, -half)  # (dT3L, dT3R) for downtype fermions
BIDOUBLET_COMPONENTS = frozenset({HIGGS_COMPONENT_P, HIGGS_COMPONENT_M})


# ── Gate verification ─────────────────────────────────────────────────────────


def verify_gates() -> str:
    gates_pass = 0

    # T1: dQ = 0 — only neutral Higgs component mediates Yukawa vertices
    for qn in HIGGS_QN:
        assert qn["dQ"] == 0, f"T1 FAIL at {qn['pair']}: dQ = {qn['dQ']}"
    gates_pass += 1

    # T2: |dT3L| = 1/2 — SU(2)_L doublet (rules out singlet and adjoint)
    for qn in HIGGS_QN:
        assert abs(qn["dT3L"]) == half, f"T2 FAIL at {qn['pair']}: |dT3L| = {abs(qn['dT3L'])} ≠ 1/2"
    gates_pass += 1

    # T3: |dT3R| = 1/2 — SU(2)_R doublet
    for qn in HIGGS_QN:
        assert abs(qn["dT3R"]) == half, f"T3 FAIL at {qn['pair']}: |dT3R| = {abs(qn['dT3R'])} ≠ 1/2"
    gates_pass += 1

    # T4: dT3L + dT3R = 0 — anti-diagonal pairing (bidoublet neutral components)
    for qn in HIGGS_QN:
        assert qn["dT3L"] + qn["dT3R"] == 0, (
            f"T4 FAIL at {qn['pair']}: dT3L+dT3R = {qn['dT3L'] + qn['dT3R']}"
        )
    gates_pass += 1

    # T5: dBL = 0 — Higgs is B−L singlet, lives in S³ factor not S⁶
    for qn in HIGGS_QN:
        assert qn["dBL"] == 0, f"T5 FAIL at {qn['pair']}: dBL = {qn['dBL']}"
    gates_pass += 1

    # T6: dY = dT3R — Y of Higgs comes entirely from T3R (dBL=0 → dY = dT3R + 0/2)
    for qn in HIGGS_QN:
        assert qn["dY"] == qn["dT3R"], (
            f"T6 FAIL at {qn['pair']}: dY = {qn['dY']}, dT3R = {qn['dT3R']}"
        )
    gates_pass += 1

    # T7: exactly 2 distinct (dT3L, dT3R) values — (2,2) bidoublet structure
    observed = frozenset((qn["dT3L"], qn["dT3R"]) for qn in HIGGS_QN)
    assert observed == BIDOUBLET_COMPONENTS, (
        f"T7 FAIL: got {observed}, expected {BIDOUBLET_COMPONENTS}"
    )
    gates_pass += 1

    # T8: equal split — 8 pairs per bidoublet component (symmetry of spectrum)
    n_p = sum(1 for qn in HIGGS_QN if (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_P)
    n_m = sum(1 for qn in HIGGS_QN if (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_M)
    assert n_p == 8 and n_m == 8, f"T8 FAIL: n_plus={n_p}, n_minus={n_m} (expected 8 each)"
    gates_pass += 1

    return f"PASS_G19_HIGGS_BIDOUBLET ({gates_pass}/8)"


if __name__ == "__main__":
    print(verify_gates())
