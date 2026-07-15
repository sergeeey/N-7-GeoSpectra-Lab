"""Round 61 — Route B: independent blind derivation of a B-L-like commutant T.

INDEPENDENCE PROTOCOL (see task instructions this script was generated under):
  - This script was written WITHOUT reading Route A's script
    (round61_route_a_commutant.py), which may or may not exist in this same
    experiment folder.
  - BmL_32 and Y_32 from g16_t3r_k3.py are NOT imported/used anywhere in the
    CONSTRUCTION of the 8-block decomposition, the real-structure reduction,
    or the anomaly-equation solve. They are imported ONLY in the final
    `step4_compare_to_bml()` function, strictly for after-the-fact comparison.
  - The only things read from SM_LH_UP / SM_LH_DN / SM_RH_FERMIONS /
    SM_RH_ANTIFERMIONS (in g17_electric_charge.py / g16_t3r_k3.py) are STATE
    NAMES and ROW INDICES (first tuple element). The second tuple element in
    those dicts (a charge value derived from Y_32/BmL_32) is never read into
    this file — the STATE_NAMES table below only records names+indices.
  - J3_32/K3_32/C32 (SU(2)_L, SU(2)_R, SU(3)_color generators) and CPT_PAIRS
    (from g18_ncg.py) are geometric bookkeeping, explicitly permitted by the
    task, and are rebuilt here from the low-level building blocks (J_S3,
    K_S3, su3_generators, lift_to_spinor) rather than importing the
    already-assembled 32x32 matrices from g16 — this keeps Route B's
    generator construction self-contained and avoids any accidental coupling
    to another script's already-built objects.

METHOD OVERVIEW
  Step 1: partition the 32 rows into 8 SU(3)xSU(2)_{L,R} blocks using ONLY
          state names + row indices (comments justify each block). Verify
          computationally: block closure (no leakage), non-triviality,
          doublet pairing, and check whether any two blocks are isomorphic
          as bare (SU(3),SU(2)) representations (Schur multiplicity check).
  Step 2: build J_F from CPT_PAIRS, verify each block maps entirely onto one
          partner block, derive the 8->4 parameter reduction from
          J_F T J_F = -T.
  Step 3: classify each of the 4 independent blocks by color/SU(2)_L/SU(2)_R
          content (read off the actual verified generator action, not the
          block name) and impose 5 anomaly conditions. Solve exactly.
  Step 4: ONLY NOW read BmL_32 and compare.
"""

from __future__ import annotations

import os
import sys

import sympy as sp
from sympy import Rational as Rat
from sympy import Matrix, kronecker_product as kron, symbols, zeros

# ── Path setup — import ONLY low-level structural building blocks ───────────
_EXP_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))
for _subdir in [
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g11_block_generators import J_S3, K_S3, I4, I8, lift_to_spinor  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402

half = Rat(1, 2)

# ── Rebuild 32x32 generators from first principles (independent of g16/g17) ──
su3_spin = [lift_to_spinor(C) for C in su3_generators()]

J32 = [kron(J_S3[a], I8) for a in range(3)]  # SU(2)_L on 32-dim (trivial on S6, S3-block only)
K32 = [kron(K_S3[a], I8) for a in range(3)]  # SU(2)_R on 32-dim
C32 = [kron(I4, C) for C in su3_spin]  # SU(3)_color on 32-dim (8 generators, trivial on S3)

J3_32, K3_32 = J32[2], K32[2]

assert len(C32) == 8, f"expected 8 su(3) generators, got {len(C32)}"


def _eps3(a: int, b: int, c: int) -> int:
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    if (a, b, c) in {(0, 2, 1), (2, 1, 0), (1, 0, 2)}:
        return -1
    return 0


# sanity: su(2)_L / su(2)_R algebras close on the 32-dim rebuild (re-derives
# G11 T1/T2 at 32-dim, on the freshly-rebuilt generators used below).
for _a in range(3):
    for _b in range(3):
        comm_J = J32[_a] * J32[_b] - J32[_b] * J32[_a]
        expected_J = sum((sp.I * _eps3(_a, _b, _c) * J32[_c] for _c in range(3)), zeros(32, 32))
        assert comm_J - expected_J == zeros(32, 32), f"su(2)_L algebra fails at ({_a},{_b})"
        comm_K = K32[_a] * K32[_b] - K32[_b] * K32[_a]
        expected_K = sum((sp.I * _eps3(_a, _b, _c) * K32[_c] for _c in range(3)), zeros(32, 32))
        assert comm_K - expected_K == zeros(32, 32), f"su(2)_R algebra fails at ({_a},{_b})"
print("Rebuilt J32 (3), K32 (3), C32 (8) as 32x32 matrices from first principles.")
print("  su(2)_L, su(2)_R algebra closure re-verified at 32-dim: PASS")

# ══════════════════════════════════════════════════════════════════════════
# STEP 1 — state names + row indices ONLY, block decomposition BY HAND
# ══════════════════════════════════════════════════════════════════════════

# State labels + row indices, transcribed from SM_LH_UP / SM_LH_DN
# (g17_electric_charge.py) and SM_RH_FERMIONS / SM_RH_ANTIFERMIONS
# (g16_t3r_k3.py). ONLY the name and the row index (first tuple element) are
# used below — the charge column (second tuple element) of those dicts is
# never transcribed here.
STATE_NAMES: dict[int, str] = {
    0: "nu_L", 1: "d_Lbar_1", 2: "d_Lbar_2", 3: "u_L_1", 4: "d_Lbar_3",
    5: "u_L_2", 6: "u_L_3", 7: "e_Lbar",
    8: "e_L", 9: "u_Lbar_1", 10: "u_Lbar_2", 11: "d_L_1", 12: "u_Lbar_3",
    13: "d_L_2", 14: "d_L_3", 15: "nu_Lbar",
    16: "nu_R", 17: "d_Rbar_1", 18: "d_Rbar_2", 19: "u_R_1", 20: "d_Rbar_3",
    21: "u_R_2", 22: "u_R_3", 23: "e_Rbar",
    24: "e_R", 25: "u_Rbar_1", 26: "u_Rbar_2", 27: "d_R_1", 28: "u_Rbar_3",
    29: "d_R_2", 30: "d_R_3", 31: "nu_Rbar",
}  # fmt: skip
assert len(STATE_NAMES) == 32 and set(STATE_NAMES) == set(range(32))

# Row = S3_sector*8 + S6_subindex.  S3 sectors (from G11: J32/K32 = kron(*, I8)
# act on the sector index only, block-structured in groups of 8 consecutive
# rows — this is visible directly from the STATE_NAMES pattern: names repeat
# their "family" (nu/e/u/d) with period 8, e.g. row0=nu_L, row8=e_L,
# row16=nu_R, row24=e_R all sit at S6-subindex 0).
L_UP, L_DN, R_UP, R_DN = (
    list(range(0, 8)),
    list(range(8, 16)),
    list(range(16, 24)),
    list(range(24, 32)),
)

# Within each 8-row sector, the S6-subindex-0 name is always a lone
# "neutrino-like" singlet (nu_L, e_L, nu_R, e_R) and subindex-7 is always its
# "bar" partner (e_Lbar, nu_Lbar, e_Rbar, nu_Rbar) — one singlet, one
# antisinglet. Subindices {1,2,4} always carry a 3-member family sharing one
# tag (d_Lbar/u_Lbar/d_Rbar/u_Rbar) and {3,5,6} another 3-member family
# (u_L/d_L/u_R/d_R) — matching G14's S6 spinor decomposition 1(SP_SINGLET=0)
# + 3bar(AQUARK={1,2,4}) + 3(QUARK={3,5,6}) + 1(SM_SINGLET=7).
SP_SINGLET, SM_SINGLET = 0, 7
QUARK, AQUARK = (3, 5, 6), (1, 2, 4)

# ── 8 candidate blocks, derived BY HAND from the name pattern ───────────────
# L-sector (chirality gamma_F=-1, rows 0-15), paired across L_UP<->L_DN at
# the SAME S6-subindex (this is exactly what J32[0]/J32[1] connect, since
# J32 = kron(J_S3, I8) only ever links S3-sector i with S3-sector j at
# matching S6-subindex k — see G11 kron structure read above).
block_A = [SP_SINGLET, 8 + SP_SINGLET]  # {nu_L, e_L}: lepton doublet, L
block_D = [SM_SINGLET, 8 + SM_SINGLET]  # {e_Lbar, nu_Lbar}: antilepton doublet, L
block_C = [*QUARK, *[8 + k for k in QUARK]]  # {u_L x3, d_L x3}: quark doublet, L (3 colors)
block_B = [*AQUARK, *[8 + k for k in AQUARK]]  # {d_Lbar x3, u_Lbar x3}: antiquark doublet, L

# R-sector (chirality +1, rows 16-31), paired across R_UP<->R_DN (K32 off-diag
# connects S3-sector 2<->3 at matching S6-subindex, per K_S3 structure read
# above), same S6-subindex logic as the L-sector.
block_Ap = [16 + SP_SINGLET, 24 + SP_SINGLET]  # {nu_R, e_R}
block_Dp = [16 + SM_SINGLET, 24 + SM_SINGLET]  # {e_Rbar, nu_Rbar}
block_Cp = [16 + k for k in QUARK] + [24 + k for k in QUARK]  # {u_R x3, d_R x3}
block_Bp = [16 + k for k in AQUARK] + [24 + k for k in AQUARK]  # {d_Rbar x3, u_Rbar x3}

BLOCKS = {
    "A": block_A, "B": block_B, "C": block_C, "D": block_D,
    "Ap": block_Ap, "Bp": block_Bp, "Cp": block_Cp, "Dp": block_Dp,
}  # fmt: skip

print("\nSTEP 1 — proposed blocks (from state names + row indices only):")
for name, rows in BLOCKS.items():
    labels = [STATE_NAMES[r] for r in rows]
    print(f"  {name:3s} rows={rows}  states={labels}")

# ── Verification: closure = complete, disjoint cover of {0..31} ────────────
_all_rows = sorted(r for rows in BLOCKS.values() for r in rows)
assert _all_rows == list(range(32)), f"block union is not a clean partition of 0..31: {_all_rows}"
print("\n[V1] Block union is an exact disjoint partition of rows 0..31: PASS")


def submatrix(M: Matrix, rows: list[int]) -> Matrix:
    return M[rows, rows]


def is_block_closed(G: Matrix, rows: list[int]) -> bool:
    """No leakage: G maps span(rows) into span(rows)."""
    rowset = set(rows)
    for r in rows:
        for c in range(32):
            if c not in rowset and G[r, c] != 0:
                return False
    return True


def acts_trivially(G: Matrix, rows: list[int]) -> bool:
    return all(G[r, c] == 0 for r in rows for c in range(32))


def is_nontrivial_on(G: Matrix, rows: list[int]) -> bool:
    return any(G[r, c] != 0 for r in rows for c in rows)


# [V2] Each L-block is closed under J32[0], J32[1], J32[2] and under all C32.
#      Each L-block is TRIVIAL (identically zero) under all K32 (SU(2)_R).
L_BLOCKS = ["A", "B", "C", "D"]
R_BLOCKS = ["Ap", "Bp", "Cp", "Dp"]

v2_ok = True
for name in L_BLOCKS:
    rows = BLOCKS[name]
    for a in range(3):
        if not is_block_closed(J32[a], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not closed under J32[{a}]")
        if not acts_trivially(K32[a], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not SU(2)_R-trivial (K32[{a}] nonzero)")
    for i in range(8):
        if not is_block_closed(C32[i], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not closed under C32[{i}]")
for name in R_BLOCKS:
    rows = BLOCKS[name]
    for a in range(3):
        if not is_block_closed(K32[a], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not closed under K32[{a}]")
        if not acts_trivially(J32[a], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not SU(2)_L-trivial (J32[{a}] nonzero)")
    for i in range(8):
        if not is_block_closed(C32[i], rows):
            v2_ok = False
            print(f"  [V2 FAIL] block {name} not closed under C32[{i}]")
print(
    f"[V2] Block closure under {{SU(3), own-chirality SU(2)}}, trivial under opposite SU(2): "
    f"{'PASS' if v2_ok else 'FAIL'}"
)
assert v2_ok, "block closure verification failed — block assignment is wrong"

# [V3] Doublet-pairing check: for A,D,Ap,Dp (dim 2) and for B,C,Bp,Cp (dim 6,
#      i.e. 3 colors x 2 doublet components), confirm the OFF-DIAGONAL
#      generator (J32[0] for L, K32[0] for R) genuinely connects the exact
#      partner rows claimed (same S6-subindex, opposite S3-sub-sector) with a
#      NONZERO matrix element, and confirm J32[2]/K32[2] gives the expected
#      +-1/2 eigenvalue split (a genuine doublet, not an accidental trivial
#      2-dim reducible rep).
PAIRING = {
    "A": [(0, 8)],
    "D": [(7, 15)],
    "C": [(3, 11), (5, 13), (6, 14)],
    "B": [(1, 9), (2, 10), (4, 12)],
    "Ap": [(16, 24)],
    "Dp": [(23, 31)],
    "Cp": [(19, 27), (21, 29), (22, 30)],
    "Bp": [(17, 25), (18, 26), (20, 28)],
}
v3_ok = True
for name, pairs in PAIRING.items():
    gen = J32[0] if name in L_BLOCKS else K32[0]
    gen3 = J3_32 if name in L_BLOCKS else K3_32
    for lo, hi in pairs:
        if gen[lo, hi] == 0 or gen[hi, lo] == 0:
            v3_ok = False
            print(f"  [V3 FAIL] {name}: off-diag generator has zero entry for pair ({lo},{hi})")
        if gen3[lo, lo] == 0 or gen3[hi, hi] == 0 or gen3[lo, lo] != -gen3[hi, hi]:
            v3_ok = False
            print(
                f"  [V3 FAIL] {name}: diag generator doesn't show +-1/2 doublet split "
                f"at ({lo},{hi}): {gen3[lo, lo]}, {gen3[hi, hi]}"
            )
print(
    f"[V3] Doublet pairing (off-diag nonzero + diag +-1/2 split) for all 8 blocks: "
    f"{'PASS' if v3_ok else 'FAIL'}"
)
assert v3_ok

# [V4] Color content check: A,D,Ap,Dp are SU(3)-singlets (all C32[i]==0 on
#      block rows); B,C,Bp,Cp are color-nontrivial (some C32[i] nonzero).
COLOR_TRIVIAL_EXPECTED = {
    "A": True,
    "D": True,
    "Ap": True,
    "Dp": True,
    "B": False,
    "C": False,
    "Bp": False,
    "Cp": False,
}
v4_ok = True
color_dim: dict[str, int] = {}
for name, rows in BLOCKS.items():
    trivial = all(acts_trivially(C32[i], rows) for i in range(8))
    if trivial != COLOR_TRIVIAL_EXPECTED[name]:
        v4_ok = False
        print(
            f"  [V4 FAIL] block {name}: color-trivial={trivial}, expected "
            f"{COLOR_TRIVIAL_EXPECTED[name]}"
        )
    color_dim[name] = 1 if trivial else 3
print(f"[V4] Color content matches expected singlet/triplet pattern: {'PASS' if v4_ok else 'FAIL'}")
assert v4_ok
print(f"     color_dim = {color_dim}")

su2_dim = {name: 2 for name in BLOCKS}  # every block verified as a genuine doublet (V3)

# ── Isomorphism / Schur multiplicity-1 check ────────────────────────────────
# Two blocks are isomorphic as SU(3)xSU(2) reps here iff they have the SAME
# (color_dim, su2_dim) SIGNATURE *and* (for color-nontrivial blocks) the SAME
# eigenvalue spectrum of every C32[i] restricted to the block (a necessary
# condition for the existence of an intertwiner using the SAME fixed
# generator matrices).
print("\n[V5] Multiplicity-1 / isomorphism check (Schur's lemma prerequisite):")


def eigenvalue_multiset(G: Matrix, rows: list[int]):
    sub = submatrix(G, rows)
    ev = sub.eigenvals()  # dict eigenvalue -> multiplicity
    return tuple(sorted(((sp.nsimplify(k), v) for k, v in ev.items()), key=lambda kv: str(kv[0])))


def blocks_isomorphic(n1: str, n2: str) -> bool:
    if (color_dim[n1], su2_dim[n1]) != (color_dim[n2], su2_dim[n2]):
        return False
    if color_dim[n1] == 1:
        # both SU(3)-trivial: as bare (SU(3),SU(2)) reps these are IDENTICAL
        # (trivial x doublet) — no invariant distinguishes them without
        # extra structure (e.g. a diagonal U(1) charge, which is exactly
        # what we are trying to construct, so it cannot be used here).
        return True
    # color-charged: compare eigenvalue spectra of a representative
    # SU(2)-doublet-component-worth of rows (3 color rows) under every C32[i]
    rows1 = [
        r
        for r in BLOCKS[n1]
        if r < (BLOCKS[n1][0] + 8 if BLOCKS[n1][0] < 16 else BLOCKS[n1][0] + 8)
    ]
    # simpler: take first 3 rows of each block (one doublet component)
    rows1 = BLOCKS[n1][:3]
    rows2 = BLOCKS[n2][:3]
    for i in range(8):
        if eigenvalue_multiset(C32[i], rows1) != eigenvalue_multiset(C32[i], rows2):
            return False
    return True


iso_pairs = []
names8 = list(BLOCKS.keys())
for i1 in range(len(names8)):
    for i2 in range(i1 + 1, len(names8)):
        n1, n2 = names8[i1], names8[i2]
        if blocks_isomorphic(n1, n2):
            iso_pairs.append((n1, n2))

print(f"     Isomorphic pairs found: {iso_pairs}")
expected_iso = {("A", "D"), ("Ap", "Dp")}
found_iso = set(iso_pairs)
multiplicity_one_holds = len(found_iso) == 0
print(f"     multiplicity-1 (no isomorphic pairs) holds: {multiplicity_one_holds}")
if found_iso == expected_iso:
    print("     MATCHES EXPECTATION: (A,D) and (Ap,Dp) are isomorphic as bare")
    print("     (SU(3)_color-singlet, SU(2)-doublet) representations — pure")
    print("     Schur's lemma on {SU(3),SU(2)} ALONE does not by itself forbid an")
    print("     off-diagonal A<->D (resp. Ap<->Dp) intertwiner term (a 2x2 flavor")
    print("     matrix instead of 2 independent scalars). B/C and Bp/Cp remain")
    print("     genuinely multiplicity-1 (3 vs 3bar, verified non-isomorphic by")
    print("     differing C32 eigenvalue spectra above).")
else:
    print("     UNEXPECTED isomorphism pattern — re-examine block assignment.")

CAVEAT_MULTIPLICITY = (
    "Blocks A/D (and Ap/Dp) are isomorphic as bare SU(3)xSU(2)_L reps "
    "(both color-singlet doublets). The literal 8-independent-scalar ansatz "
    "used below additionally assumes T is DIAGONAL in this row basis "
    "(no A<->D mixing term) — a standard, but SEPARATE, physical assumption "
    "for a U(1)-charge-like operator, not something pure Schur's-lemma-on-"
    "{SU(3),SU(2)} irreducibility+closure alone forces. B/C, Bp/Cp ARE "
    "genuinely multiplicity-1 (verified: differing C32 eigenvalue spectra "
    "-> 3 and 3bar are inequivalent), so no such gap exists for those 4."
)
print(f"\n[CAVEAT] {CAVEAT_MULTIPLICITY}")

# 8 free real parameters — one scalar per block, diagonal ansatz (see caveat).
t_A, t_B, t_C, t_D, t_Ap, t_Bp, t_Cp, t_Dp = symbols(
    "t_A t_B t_C t_D t_Ap t_Bp t_Cp t_Dp", real=True
)
T_SYMS = {"A": t_A, "B": t_B, "C": t_C, "D": t_D, "Ap": t_Ap, "Bp": t_Bp, "Cp": t_Cp, "Dp": t_Dp}

# ══════════════════════════════════════════════════════════════════════════
# STEP 2 — CPT_PAIRS (from g18_ncg.py construction), real-structure reduction
# ══════════════════════════════════════════════════════════════════════════
print("\nSTEP 2 — CPT pairing + real-structure reduction")

# CPT_PAIRS list, transcribed identically from g18_ncg.py (row pairs only —
# this defines J_F, explicitly permitted geometric bookkeeping).
CPT_PAIRS: list[tuple[int, int]] = [
    (0, 31), (15, 16), (8, 23), (7, 24),
    (3, 25), (5, 26), (6, 28),
    (9, 19), (10, 21), (12, 22),
    (11, 17), (13, 18), (14, 20),
    (1, 27), (2, 29), (4, 30),
]  # fmt: skip
assert len(CPT_PAIRS) == 16

J_F = zeros(32, 32)
for _i, _j in CPT_PAIRS:
    J_F[_i, _j] = 1
    J_F[_j, _i] = 1
assert J_F**2 == sp.eye(32), "J_F^2 != I"

ROW_TO_BLOCK: dict[int, str] = {r: name for name, rows in BLOCKS.items() for r in rows}

# Verify each block maps ENTIRELY onto exactly one partner block under J_F.
block_partner: dict[str, str] = {}
v6_ok = True
for name, rows in BLOCKS.items():
    partners = {ROW_TO_BLOCK[j] for r in rows for i, j in CPT_PAIRS if i == r} | {
        ROW_TO_BLOCK[i] for r in rows for i, j in CPT_PAIRS if j == r
    }
    if len(partners) != 1:
        v6_ok = False
        print(f"  [V6 FAIL] block {name} maps to multiple/zero partner blocks: {partners}")
        continue
    (partner,) = partners
    block_partner[name] = partner
print(f"[V6] Each block maps onto exactly one CPT-partner block: {'PASS' if v6_ok else 'FAIL'}")
assert v6_ok
print(f"     block_partner = {block_partner}")

expected_partner = {"A": "Dp", "D": "Ap", "C": "Bp", "B": "Cp",
                     "Dp": "A", "Ap": "D", "Bp": "C", "Cp": "B"}  # fmt: skip
assert block_partner == expected_partner, (
    f"CPT block-pairing differs from expectation: {block_partner} vs {expected_partner}"
)
print("     Matches by-hand expectation: A<->Dp, D<->Ap, C<->Bp, B<->Cp")

# J_F T J_F = -T (real-structure/KO-dim-6 anti-commutation with the scalar
# commutant): on a 2x2 subspace {row i in block X, row j in block Y=partner(X)}
# with J_F acting as the swap [[0,1],[1,0]] and T=diag(t_X,t_Y), we get
# J_F T J_F = diag(t_Y, t_X); setting this = -diag(t_X,t_Y) forces t_Y=-t_X.
real_structure_relations = {
    "t_Dp": -t_A,
    "t_Ap": -t_D,
    "t_Bp": -t_C,
    "t_Cp": -t_B,
}
print(f"     Real-structure relations: {real_structure_relations}")

# Sanity check with an explicit sympy matrix computation on a representative
# pair (row0=A, row31=Dp), confirming J_F T J_F + T = 0 forces t_Dp = -t_A
# for GENERIC diagonal T on this 2-row subspace (not assumed, derived).
_rows_check = [0, 31]
_Tsub = sp.diag(t_A, t_Dp)
_Jsub = J_F[_rows_check, _rows_check]
_cond = sp.expand(_Jsub * _Tsub * _Jsub + _Tsub)
_sol = sp.solve(list(_cond), [t_Dp], dict=True)
assert _sol and sp.simplify(_sol[0][t_Dp] - (-t_A)) == 0, (
    f"real-structure derivation mismatch: {_sol}"
)
print(
    f"     [V7] Explicit 2x2 check on (row0,row31): J_F T J_F = -T => t_Dp = {_sol[0][t_Dp]}  PASS"
)

num_free_parameters_after_real_structure = 4
print(
    f"\n8 parameters -> 4 independent parameters (t_A, t_B, t_C, t_D) after real-structure "
    f"constraint.  num_free_parameters_after_real_structure = "
    f"{num_free_parameters_after_real_structure}"
)

# ══════════════════════════════════════════════════════════════════════════
# STEP 3 — classify + impose 5 anomaly conditions, solve exactly
# ══════════════════════════════════════════════════════════════════════════
print("\nSTEP 3 — classification + anomaly conditions")

# Classify each of the 4 independent blocks by reading off the ACTUAL
# verified generator action (from V2/V4 above), not the block's name.
CLASSIFICATION = {
    name: {
        "color_charged": color_dim[name] == 3,
        "su2L_doublet": name in L_BLOCKS,  # verified in V2/V3: J32 nontrivial, K32 trivial
        "su2R_doublet": name in R_BLOCKS,  # verified in V2/V3: K32 nontrivial, J32 trivial
        "color_dim": color_dim[name],
    }
    for name in BLOCKS
}
for name in ["A", "B", "C", "D"]:
    print(f"  {name}: {CLASSIFICATION[name]}")

# Substitute real-structure relations so everything is in terms of t_A,t_B,t_C,t_D.
T_ALL = {
    "A": t_A, "B": t_B, "C": t_C, "D": t_D,
    "Ap": real_structure_relations["t_Ap"], "Bp": real_structure_relations["t_Bp"],
    "Cp": real_structure_relations["t_Cp"], "Dp": real_structure_relations["t_Dp"],
}  # fmt: skip

# Anomaly coefficients, built from VERIFIED multiplicities (color_dim, su2_dim)
# read off the block structure above — Dynkin index normalization T(fund)=1/2.
T_FUND = Rat(1, 2)


def grav_u1() -> sp.Expr:
    # linear, sum over the L-sector's 16 individual states (each block
    # contributes color_dim * su2_dim states, each carrying charge t_X)
    return sum(color_dim[n] * su2_dim[n] * T_ALL[n] for n in L_BLOCKS)


def cubic_u1() -> sp.Expr:
    return sum(color_dim[n] * su2_dim[n] * T_ALL[n] ** 3 for n in L_BLOCKS)


def su3_sq_u1() -> sp.Expr:
    return sum(
        T_FUND * su2_dim[n] * T_ALL[n] for n in L_BLOCKS if CLASSIFICATION[n]["color_charged"]
    )


def su2L_sq_u1() -> sp.Expr:
    return sum(
        T_FUND * color_dim[n] * T_ALL[n] for n in L_BLOCKS if CLASSIFICATION[n]["su2L_doublet"]
    )


def su2R_sq_u1() -> sp.Expr:
    return sum(
        T_FUND * color_dim[n] * T_ALL[n]
        for n in ["Ap", "Bp", "Cp", "Dp"]
        if CLASSIFICATION[n]["su2R_doublet"]
    )


eq_grav = sp.expand(grav_u1())
eq_cubic = sp.expand(cubic_u1())
eq_su3 = sp.expand(su3_sq_u1())
eq_su2L = sp.expand(su2L_sq_u1())
eq_su2R = sp.expand(su2R_sq_u1())

print(f"\n  grav^2-U(1)   : {eq_grav} = 0")
print(f"  U(1)^3        : {eq_cubic} = 0")
print(f"  SU(3)^2-U(1)  : {eq_su3} = 0")
print(f"  SU(2)_L^2-U(1): {eq_su2L} = 0")
print(f"  SU(2)_R^2-U(1): {eq_su2R} = 0")

# Check redundancy claimed by hand: grav, SU(2)_L^2 and SU(2)_R^2 conditions
# should all reduce to the SAME linear equation (up to overall sign), since
# every L-sector state sits in an SU(2)_L doublet and every R-sector state in
# an SU(2)_R doublet (verified in V2/V3 — no singlets under the "own" SU(2)).
ratio_L = sp.simplify(eq_grav - 4 * eq_su2L)
ratio_R = sp.simplify(eq_grav + 4 * eq_su2R)
print(f"\n  [V8] eq_grav - 4*eq_su2L == 0 identically: {ratio_L == 0}  ({ratio_L})")
print(f"  [V8] eq_grav + 4*eq_su2R == 0 identically: {ratio_R == 0}  ({ratio_R})")
redundancy_confirmed = (ratio_L == 0) and (ratio_R == 0)
assert redundancy_confirmed, "expected grav/SU(2)_L^2/SU(2)_R^2 to coincide as equations"

independent_linear_eqs = [eq_grav, eq_su3]  # eq_su2L, eq_su2R are redundant with eq_grav
sol = sp.solve([sp.Eq(e, 0) for e in independent_linear_eqs], [t_C, t_D], dict=True)
assert len(sol) == 1
sol0 = sol[0]
print(f"\n  Linear solve (t_C, t_D in terms of t_A, t_B): {sol0}")

# Verify cubic condition is AUTOMATICALLY satisfied on this linear solution
# (not an extra independent constraint) — substitute and simplify.
eq_cubic_reduced = sp.simplify(eq_cubic.subs(sol0))
print(
    f"  [V9] U(1)^3 condition after substituting linear solution: {eq_cubic_reduced}"
    f"  (should be identically 0 for ALL t_A,t_B)"
)
cubic_is_redundant = sp.expand(eq_cubic_reduced) == 0
assert cubic_is_redundant, "cubic condition is NOT automatically satisfied — real extra constraint!"

# Rank of the independent linear system among {grav, su3} (2 eqs, 4 unknowns).
# t_A, t_B remain free by construction of the solve() call above (solved for
# t_C, t_D only).
final_solution_dim = 4 - len(independent_linear_eqs)  # rank=2 (verified via solve() succeeding
# uniquely for t_C,t_D in terms of t_A,t_B), cubic adds no further rank (V9)
print(
    f"\n  final_solution_dim = 4 - rank(independent anomaly constraints) "
    f"= 4 - {len(independent_linear_eqs)} = {final_solution_dim}"
)
print(f"  General solution: t_A, t_B free; t_C = {sol0[t_C]}; t_D = {sol0[t_D]}")

final_generator_description = (
    "2-parameter family: t_C = -t_B, t_D = -t_A (t_A, t_B free). This is "
    "the standard anomaly-free-U(1)-for-one-SM(+nu_R)-generation family, "
    "spanned by any 2 linearly independent anomaly-free solutions (the "
    "textbook example being {Y, B-L})."
)
print(f"\n  {final_generator_description}")

# ══════════════════════════════════════════════════════════════════════════
# STEP 4 — ONLY NOW: read BmL_32 and compare
# ══════════════════════════════════════════════════════════════════════════
print("\nSTEP 4 — comparison against BmL_32 (read ONLY now)")

sys.path.insert(0, os.path.join(_REPO, "experiments/20260619-g15-hypercharge"))
sys.path.insert(0, os.path.join(_REPO, "experiments/20260619-g16-t3r-from-k3"))
from g16_t3r_k3 import BmL_32  # noqa: E402

# Verify BmL_32 is genuinely block-scalar on each of the 4 independent
# blocks (an independent sanity check of the block partition itself).
v10_ok = True
bml_val: dict[str, sp.Expr] = {}
for name in ["A", "B", "C", "D"]:
    rows = BLOCKS[name]
    vals = {BmL_32[r, r] for r in rows}
    if len(vals) != 1:
        v10_ok = False
        print(f"  [V10 FAIL] BmL_32 not constant on block {name}: {vals}")
        continue
    (bml_val[name],) = vals
print(f"[V10] BmL_32 is block-scalar on A,B,C,D: {'PASS' if v10_ok else 'FAIL'}")
assert v10_ok
print(f"      BmL_32 block values: {bml_val}")

matches_BmL32 = (
    sp.simplify(bml_val["C"] - (-bml_val["B"])) == 0
    and sp.simplify(bml_val["D"] - (-bml_val["A"])) == 0
)
print(
    f"\nmatches_BmL32 (BmL_32's (t_A,t_B,t_C,t_D) lies in the derived "
    f"2-parameter anomaly-free family): {matches_BmL32}"
)
print(f"  BmL_32: t_A={bml_val['A']}, t_B={bml_val['B']}, t_C={bml_val['C']}, t_D={bml_val['D']}")
print(
    f"  Family predicts: t_C=-t_B={-bml_val['B']} (actual {bml_val['C']}), "
    f"t_D=-t_A={-bml_val['A']} (actual {bml_val['D']})"
)

print("\n" + "=" * 70)
print("ROUND 61 ROUTE B — SUMMARY")
print("=" * 70)
print(f"blocks_identified: {list(BLOCKS.keys())}")
print(f"num_free_parameters_after_real_structure: {num_free_parameters_after_real_structure}")
print(f"final_solution_dim: {final_solution_dim}")
print(f"matches_BmL32: {matches_BmL32}")
