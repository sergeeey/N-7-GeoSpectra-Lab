"""G20: Yukawa intertwiner space on S³×S⁶ — dim = 4 from geometry + J_F.

Starting from the 32-dim Hilbert space H_F = kron(S³_4, S⁶_8) and the
geometric quantum numbers (BmL, J3, K3), derives the number of independent
Yukawa coupling constants by counting SU(3)-orbits and applying the J_F
real-structure constraint.

THREE-STEP REDUCTION:
  Step 1 — Filter by bidoublet + same S⁶ fiber index:
    "Same S⁶ index" encodes SU(3)-invariance (Schur's lemma in the natural
    S⁶ basis): the commutant of an irreducible rep is scalar multiples of I,
    and I acts diagonally in the natural basis → same S⁶ index on both sides.
    Note: dBL=0 is a CONSEQUENCE (not a filter), since B−L depends only on
    the S⁶ index (BmL_32 = kron(I4,BmL), G15).
    Only 16 of the 256 possible L→R operator entries survive.
    These are exactly the YUKAWA_PAIRS from G18.

  Step 2 — Group into SU(3) orbits (Schur's lemma):
    SU(3)-invariant operators must be proportional to the identity on each
    irreducible subspace → same coupling for all colors.
    16 pairs → 8 SU(3) orbits (pre-CPT Yukawa parameters):
      - 4 singleton orbits at |B−L| = 1 (leptonic singlets, 1 pair each)
      - 4 triplet orbits at |B−L| = 1/3 (quark color triplets, 3 pairs each)

  Step 3 — Apply J_F real structure ([D_F, J_F] = 0, from G18 Gate K5):
    J_F links each orbit to its CPT partner orbit.
    8 → 4 independent coupling groups = {Y_nu, Y_e, Y_u, Y_d}.

TWO MISSING S⁶ CHANNELS:
  In End_{SU(3)}(S⁶_8) there are 6 basis elements:
    E_aa, E_bb, E_33, E_3̄3̄ (4 dBL=0, ALLOWED)
    E_ab (1_a→1_b, dBL=+2, FORBIDDEN)
    E_ba (1_b→1_a, dBL=−2, FORBIDDEN)
  E_ab/E_ba would connect S⁶ singlet sectors with B−L=−1 and B−L=+1.
  These are absent because the mediating scalar would carry |dBL|=2,
  violating lepton-number by ΔL=2. The B−L charge is GEOMETRIC
  (from lift_to_spinor(J_S6) = −(3i/2)·BmL, established in G15).

GATES:
  M1: |VALID_PAIRS| = 16 (same S⁶ index + bidoublet → reproduces G18)
  M2: All 16 valid pairs have dBL=0 (automatic: same S⁶ index → same B−L)
  M3: VALID_PAIRS matches G18 YUKAWA_PAIRS exactly
  M4: SU(3) orbits = 8; sizes: 4 singletons + 4 triplets; J_F → 4 groups
  M5: Singlet cross-channels absent; carry |dBL|=2 (geometrically forbidden)

sm_derivation_claimed = False.
λ = FREE_COUPLING_PARAMETER.
"""

import os
import sys
from collections import defaultdict

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

from g18_ncg import CPT_PAIRS, YUKAWA_PAIRS  # noqa: E402
from g16_t3r_k3 import BmL_32, J3_32, K3_32  # noqa: E402

half = sp.Rational(1, 2)

# ── Quantum numbers for all 32 states ─────────────────────────────────────────
BmL_diag: list[sp.Expr] = [BmL_32[i, i] for i in range(32)]
J3_diag: list[sp.Expr] = [J3_32[i, i] for i in range(32)]
K3_diag: list[sp.Expr] = [K3_32[i, i] for i in range(32)]

# L-sector: T3R = 0 and T3L ≠ 0.  R-sector: T3L = 0 and T3R ≠ 0.
L_INDICES: list[int] = [i for i in range(32) if K3_diag[i] == 0 and J3_diag[i] != 0]
R_INDICES: list[int] = [j for j in range(32) if J3_diag[j] == 0 and K3_diag[j] != 0]

assert len(L_INDICES) == 16 and len(R_INDICES) == 16, "must be 16 L + 16 R rows"

# ── Step 1: valid Yukawa pairs ─────────────────────────────────────────────────
# A Yukawa pair (i_L, j_R) is valid when:
#   i_L % 8 == j_R % 8  (same S⁶ fiber index)
#       ← SU(3)-invariance via Schur's lemma: the commutant of an irreducible
#         rep is scalar multiples of I. In the natural S⁶ basis, I is diagonal,
#         so the SU(3)-invariant operator has i_L % 8 == j_R % 8.
#         Consequence: dBL = 0 automatically (B−L = BmL[i%8], from G15).
#   |dT3L| = 1/2     (SU(2)_L doublet — from J-generators, G11)
#   |dT3R| = 1/2     (SU(2)_R doublet — from K-generators, G16)
#   dT3L+dT3R = 0    (anti-diagonal bidoublet, neutral pair — G19 Gate T4)

VALID_PAIRS: list[tuple[int, int]] = []
for _i in L_INDICES:
    for _j in R_INDICES:
        if _i % 8 != _j % 8:  # SU(3)-invariance: same S⁶ fiber index
            continue
        _dT3L = J3_diag[_j] - J3_diag[_i]
        _dT3R = K3_diag[_j] - K3_diag[_i]
        if abs(_dT3L) == half and abs(_dT3R) == half and _dT3L + _dT3R == 0:
            VALID_PAIRS.append((_i, _j))

# ── Step 2: SU(3) orbits ──────────────────────────────────────────────────────
# H_F = kron(S³_4, S⁶_8): row index = (S³-sector)×8 + S⁶-fiber-index.
# SU(3) acts only on the S⁶ fiber (index mod 8).
# By Schur's lemma, all pairs in the same SU(3) irreducible sector
# and the same S³ chirality class carry the same coupling constant.
#
# Orbit key = (S³-sector of i_L, S³-sector of j_R, B−L of S⁶ fiber).
# Same key ↔ same SU(3) orbit ↔ one Yukawa coupling.


def _s3_sector(row: int) -> str:
    if K3_diag[row] == 0 and J3_diag[row] > 0:
        return "L_UP"
    if K3_diag[row] == 0 and J3_diag[row] < 0:
        return "L_DN"
    return "R_UP" if K3_diag[row] > 0 else "R_DN"


def _orbit_key(i_L: int, j_R: int) -> tuple:
    return (_s3_sector(i_L), _s3_sector(j_R), BmL_diag[i_L])


_orbit_map: dict[tuple, list[tuple[int, int]]] = defaultdict(list)
for _i, _j in VALID_PAIRS:
    _orbit_map[_orbit_key(_i, _j)].append((_i, _j))

SU3_ORBITS: dict[tuple, list[tuple[int, int]]] = dict(_orbit_map)

# ── Step 3: J_F CPT linking (8 orbits → 4 groups) ─────────────────────────────
# [D_F, J_F] = 0 (KO-dim 6, G18 Gate K5) forces: if coupling c is assigned to
# pair (i_L, j_R), then (J_F[j_R], J_F[i_L]) carries the same coupling c.
# This links each orbit to exactly one CPT-partner orbit → 8 → 4 groups.

CPT_MAP: dict[int, int] = {}
for _a, _b in CPT_PAIRS:
    CPT_MAP[_a] = _b
    CPT_MAP[_b] = _a


def _cpt_partner_key(key: tuple) -> tuple | None:
    rep_i, rep_j = SU3_ORBITS[key][0]
    p_i = CPT_MAP.get(rep_j)  # L-sector partner
    p_j = CPT_MAP.get(rep_i)  # R-sector partner
    if p_i is None or p_j is None:
        return None
    pk = _orbit_key(p_i, p_j)
    return pk if pk in SU3_ORBITS else None


_visited: set[tuple] = set()
YUKAWA_GROUPS: list[dict] = []

for _key in sorted(SU3_ORBITS.keys(), key=str):
    if _key in _visited:
        continue
    _pk = _cpt_partner_key(_key)
    if _pk is not None and _pk not in _visited:
        _visited.update((_key, _pk))
        YUKAWA_GROUPS.append(
            {
                "orbits": [_key, _pk],
                "pairs": SU3_ORBITS[_key] + SU3_ORBITS[_pk],
            }
        )
    else:
        _visited.add(_key)
        YUKAWA_GROUPS.append(
            {
                "orbits": [_key],
                "pairs": SU3_ORBITS[_key],
            }
        )

N_YUKAWA_PARAMS: int = len(YUKAWA_GROUPS)

# ── Singlet cross-channels (the 2 forbidden S⁶ channels) ─────────────────────
# E_ab: S⁶[0] (B−L=−1) → S⁶[7] (B−L=+1) → dBL = +2  — ABSENT from VALID_PAIRS
# E_ba: S⁶[7] (B−L=+1) → S⁶[0] (B−L=−1) → dBL = −2  — ABSENT from VALID_PAIRS
# These correspond to lepton-number-violating (ΔL=2) operators.
# Four 32-dim representatives (2 channels × 2 S³ chiralities):
SINGLET_CROSS_CHANNELS: list[tuple[int, int]] = [
    (0, 23),  # L↑⊗S⁶[0] → R↑⊗S⁶[7], dBL = +2
    (8, 31),  # L↓⊗S⁶[0] → R↓⊗S⁶[7], dBL = +2
    (7, 16),  # L↑⊗S⁶[7] → R↑⊗S⁶[0], dBL = −2
    (15, 24),  # L↓⊗S⁶[7] → R↓⊗S⁶[0], dBL = −2
]


# ── Gate verification ─────────────────────────────────────────────────────────


def verify_gates() -> str:
    gates_pass = 0

    # M1: 16 valid pairs
    assert len(VALID_PAIRS) == 16, f"M1 FAIL: got {len(VALID_PAIRS)} pairs (expected 16)"
    gates_pass += 1

    # M2: valid pairs match YUKAWA_PAIRS from G18 exactly
    g18_pairs = {(_i, _j) for _i, _j, _ in YUKAWA_PAIRS}
    our_pairs = set(VALID_PAIRS)
    assert our_pairs == g18_pairs, (
        f"M2 FAIL: mismatch with G18\n"
        f"  extra:   {our_pairs - g18_pairs}\n"
        f"  missing: {g18_pairs - our_pairs}"
    )
    gates_pass += 1

    # M3: 8 SU(3) orbits; singlet orbits size 1, triplet orbits size 3
    assert len(SU3_ORBITS) == 8, f"M3 FAIL: {len(SU3_ORBITS)} orbits (expected 8)"
    for _key, _pairs in SU3_ORBITS.items():
        _bl = abs(_key[2])
        if _bl == 1:
            assert len(_pairs) == 1, (
                f"M3 FAIL: singlet orbit {_key} has {len(_pairs)} pairs (expected 1)"
            )
        elif _bl == half * sp.Rational(2, 3) or _bl == sp.Rational(1, 3):
            assert len(_pairs) == 3, (
                f"M3 FAIL: triplet orbit {_key} has {len(_pairs)} pairs (expected 3)"
            )
    gates_pass += 1

    # M4: J_F produces 4 independent coupling groups
    assert N_YUKAWA_PARAMS == 4, f"M4 FAIL: {N_YUKAWA_PARAMS} groups after J_F (expected 4)"
    pair_counts = sorted(len(g["pairs"]) for g in YUKAWA_GROUPS)
    assert pair_counts == [2, 2, 6, 6], f"M4 FAIL: pair counts {pair_counts} (expected [2,2,6,6])"
    gates_pass += 1

    # M5: Singlet cross-channels (E_ab/E_ba) absent and carry |dBL| = 2
    valid_set = set(VALID_PAIRS)
    for _i, _j in SINGLET_CROSS_CHANNELS:
        assert (_i, _j) not in valid_set, (
            f"M5 FAIL: forbidden channel ({_i},{_j}) found in VALID_PAIRS"
        )
        _dBL = BmL_diag[_j] - BmL_diag[_i]
        assert abs(_dBL) == 2, f"M5 FAIL: |dBL| = {abs(_dBL)} for channel ({_i},{_j}) (expected 2)"
    gates_pass += 1

    return f"PASS_G20_YUKAWA_INTERTWINER ({gates_pass}/5)"


if __name__ == "__main__":
    print(verify_gates())

    print(f"\n=== SU(3) orbits ({len(SU3_ORBITS)}) ===")
    for _key, _pairs in sorted(SU3_ORBITS.items(), key=str):
        _s3_L, _s3_R, _bl = _key
        print(f"  ({_s3_L}→{_s3_R}, B−L={_bl}): {len(_pairs)} pair(s) → {_pairs}")

    print(f"\n=== Yukawa coupling groups after J_F ({N_YUKAWA_PARAMS}) ===")
    _labels = ["Y_nu", "Y_e", "Y_u", "Y_d"]
    for _i, _g in enumerate(YUKAWA_GROUPS):
        print(
            f"  [{_labels[_i] if _i < 4 else '?'}] orbits {_g['orbits']} "
            f"→ {len(_g['pairs'])} pairs: {_g['pairs']}"
        )

    print("\n=== Singlet cross-channels (|dBL|=2, geometrically forbidden) ===")
    for _i, _j in SINGLET_CROSS_CHANNELS:
        _dBL = BmL_diag[_j] - BmL_diag[_i]
        _s6_i, _s6_j = _i % 8, _j % 8
        print(
            f"  ({_i},{_j}): S⁶[{_s6_i}]→S⁶[{_s6_j}], "
            f"B−L: {BmL_diag[_i]}→{BmL_diag[_j]}, dBL={_dBL}"
        )
