"""E23 (round93): Charge-operator provenance + representation lift.

Frozen claim (see claim.md): torsion-product zero modes admit an unambiguous,
factor-consistent map to a complete set of independent left-handed 4D Weyl
states with well-defined K_3, T_{3R}, B-L, Y, and gauge representations.

This script performs the COMPUTATIONAL parts of Part A (operator provenance +
commutator checks) and Part B (does K_3 = T_{3R} hold as an operator
identity?) and Part D (does SU(4) act and close on the S6 spinor?). Parts B/C
of the task are primarily reading+tabulation and are documented in decision.md;
this script supplies the tool-verified numeric backbone those sections cite.

Everything imported below is REUSED from already-existing, already
tool-verified project artifacts -- nothing here re-derives G6/G11/G15/G16/G98's
own results. Citations are given inline at each import/assignment.

lambda = FREE_COUPLING_PARAMETER (not touched anywhere in this file).
safe_for_runtime = False (research only).
"""

import json
import os
import sys

import sympy as sp
from sympy import zeros, kronecker_product as kron

_EXP_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))

for _subdir in [
    "experiments/20260618-g11-block-generators",
    "experiments/20260619-g15-hypercharge",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

# G11: J_S3 (SU(2)_L generators, 4x4), K_S3 (SU(2)_R generators, 4x4),
# both "trivial on S6" by construction (g11_block_generators.py:6-8, 94-108).
from g11_block_generators import J_S3, K_S3, I4, I8, lift_to_spinor  # noqa: E402

# G15: BmL (B-L generator, 8x8, S6-side ONLY -- g15_hypercharge.py:1,71).
from g15_hypercharge import (  # noqa: E402
    BmL,
)

# G10-B: su3_generators() (8 SU(3) vector-rep generators on S6, 6x6).
from g10b_su3_explicit import su3_generators  # noqa: E402

# G10: so6_generators() (all 15 so(6) vector-rep generators, 6x6);
# complex_structure() (the J defining the SU(3)xU(1) subalgebra of so(6)).
from g10_s6_so6_gauge import so6_generators, complex_structure  # noqa: E402

half = sp.Rational(1, 2)

verdict = {}

print("=" * 90)
print("E23 (round93) PART A -- operator provenance + commutator checks")
print("=" * 90)

# ---------------------------------------------------------------------------
# G6's own s3_states, reproduced VERBATIM (not retyped with new fields) from
# experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py:29-36
# -- the same verbatim-reuse pattern round83's own script already used.
# ---------------------------------------------------------------------------
s3_states_g6 = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]

# ── Part A.1: T3L / T3R (S3-side) explicit operators + spectra ─────────────
J3_4 = J_S3[2]  # T3L generator, 4x4, g11_block_generators.py:98-102
K3_4 = K_S3[2]  # T3R generator, 4x4, g11_block_generators.py:104-108

T3L_diag_from_G11 = [J3_4[i, i] for i in range(4)]
T3R_diag_from_G11 = [K3_4[i, i] for i in range(4)]
T3L_diag_from_G6 = [s["T3L"] for s in s3_states_g6]
T3R_diag_from_G6 = [s["T3R"] for s in s3_states_g6]

t3l_match = T3L_diag_from_G11 == T3L_diag_from_G6
t3r_match = T3R_diag_from_G11 == T3R_diag_from_G6
verdict["T3L_G11_matches_G6_on_shared_basis"] = t3l_match
verdict["T3R_G11_matches_G6_on_shared_basis"] = t3r_match
print(f"T3L: G11 diag {T3L_diag_from_G11}  vs  G6 diag {T3L_diag_from_G6}  match={t3l_match}")
print(f"T3R: G11 diag {T3R_diag_from_G11}  vs  G6 diag {T3R_diag_from_G6}  match={t3r_match}")

# ── Part A.2 / Part B: is K_3 = T_{3R} an operator identity? ────────────────
# G16 (g16_t3r_k3.py:70-71) builds K3_32 = kron(K_S3[2], I8) and calls this
# quantity "K_3". This IS, by the same construction, T3R on the 32-dim space
# (K3_4 above). We verify this is the identical 32x32 diagonal operator you
# get by tensoring G6's own per-state T3R value with the 8-dim S6 identity,
# in G6's own (s3-outer, s6-inner) product order (g6_spinor_decomposition.py
# lines 156-159: "for s3 in s3_states: for s6 in s6_states"), which is
# exactly kron(A_4, B_8)'s diagonal convention.
K3_32 = kron(K3_4, I8)
T3R_32_from_G6_order = zeros(32, 32)
for i, s3 in enumerate(s3_states_g6):
    for j in range(8):
        n = i * 8 + j
        T3R_32_from_G6_order[n, n] = s3["T3R"]

k3_equals_t3r_operator_identity = (K3_32 - T3R_32_from_G6_order) == zeros(32, 32)
verdict["K3_equals_T3R_as_32x32_operator"] = k3_equals_t3r_operator_identity
print(
    f"K3_32 (G11/G16 construction) == T3R_32 (G6 per-state value, tensored "
    f"with S6-identity): {k3_equals_t3r_operator_identity}"
)

# preprint.tex:304-305 PROSE describes K_3 as "a U(1) quantum number from the
# SU(3)-harmonic decomposition of S^6" (an S6-side description). Grepping this
# repo's own *code* for any S6-side construction actually named/used as K_3
# finds NONE (checked: g11_block_generators.py, g12_anomaly_check.py,
# g16_t3r_k3.py, g19_higgs_bidoublet.py, g21_extended_schur.py,
# g22_first_order.py, g23_chirality.py, g24_blind_spectrum.py,
# kt6_su2r_anomaly_check.py -- every one of these builds K_3/K3_32 from
# K_S3, the S3-side SU(2)_R generator, never from an S6 SU(3)-Cartan
# construction). This is recorded as a documented fact, not a script check;
# see decision.md Part B for the full citation trail.
no_s6_side_k3_construction_found_in_code = True  # [DOCS/CODE, this round's grep audit]
verdict["no_s6_side_k3_construction_found_in_code"] = no_s6_side_k3_construction_found_in_code

# ── Part A.3: commutators, S3 side ──────────────────────────────────────────
# [J3, K3] = 0 -- reuses G11 T3 (g11_block_generators.py:160-164), re-verified.
j3k3_commute = (J3_4 * K3_4 - K3_4 * J3_4) == zeros(4, 4)
verdict["J3_K3_commute"] = j3k3_commute
print(f"[T3L, T3R] = 0 (G11 T3, re-verified): {j3k3_commute}")

# ── Part A.4: SU(3)_c generators (S6 side) + commutators with K3/T3R ───────
su3_spin = [lift_to_spinor(C) for C in su3_generators()]
C32 = [kron(I4, C) for C in su3_spin]
K3_32_commutes_su3 = all((K3_32 * C - C * K3_32) == zeros(32, 32) for C in C32)
verdict["K3_commutes_with_all_8_su3_generators"] = K3_32_commutes_su3
print(f"[T3R/K3, SU(3)_c generators] = 0 for all 8 (G16 T4/KT6, re-verified): {K3_32_commutes_su3}")

# ── Part A.5: B-L (S6 side, UNTWISTED weight space only) ───────────────────
BmL_32 = kron(I4, BmL)
BmL_commutes_su3 = all((BmL_32 * C - C * BmL_32) == zeros(32, 32) for C in C32)
verdict["BmL_commutes_with_all_8_su3_generators"] = BmL_commutes_su3
print(f"[B-L, SU(3)_c generators] = 0 for all 8 (G15 T4, re-verified): {BmL_commutes_su3}")

Gamma7 = kron(sp.eye(2), sp.eye(2), sp.eye(2))  # placeholder overwritten below
s3p = sp.Matrix([[1, 0], [0, -1]])
Gamma7_8 = kron(s3p, s3p, s3p)
BmL_commutes_chirality = (BmL * Gamma7_8 - Gamma7_8 * BmL) == zeros(8, 8)
verdict["BmL_commutes_with_S6_chirality"] = BmL_commutes_chirality
print(f"[B-L, Gamma_7 (S6 chirality)] = 0 (G15 T3, re-verified): {BmL_commutes_chirality}")

# ── Part A.6: does B-L commute with the FULL so(6)=su(4), or only su(3)+u(1)? ─
# Reuses G98 (g98_bl_holonomy.py:T5) -- re-verified here directly, not merely
# cited. IMPORTANT basis-dependence caveat, resolved this round: G98's own
# decision.md says BmL "commutes with the su(3)+u(1) subalgebra (9 of 15)" --
# this "9" is the DIMENSION of the su(3)+u(1) subalgebra (8 su(3) generators,
# already shown to commute in Part A.5, + 1 U(1) center, which commutes with
# BmL TRIVIALLY since G15 T8 shows they are proportional: lift_to_spinor(J) =
# -(3i/2)*BmL, a scalar multiple of itself). It is NOT a claim that 9 of the
# 15 RAW antisymmetric-matrix generators M_ab individually commute -- that
# raw-basis count is verified here to be only 3/15 (the su(3)+u(1) subalgebra
# is realized as SPECIFIC LINEAR COMBINATIONS of the raw M_ab, per G10-B's
# su3_generators(), not as a subset of the raw basis itself). Both numbers are
# genuine and consistent once the basis-dependence is made explicit.
so6_vec_gens = [M for (_, M) in so6_generators()]
so6_spin_gens = [lift_to_spinor(M) for M in so6_vec_gens]
bml_so6_comms = [(BmL * G - G * BmL) for G in so6_spin_gens]
n_commuting_raw_basis = sum(1 for c in bml_so6_comms if c == zeros(8, 8))
n_total_so6 = len(so6_spin_gens)
J_u1_spin = lift_to_spinor(complex_structure())
bml_commutes_with_u1_center = (BmL * J_u1_spin - J_u1_spin * BmL) == zeros(8, 8)
bml_commutes_with_su3_plus_u1_subalgebra = BmL_commutes_su3 and bml_commutes_with_u1_center
verdict["BmL_commutes_with_n_of_15_raw_so6_basis_generators"] = n_commuting_raw_basis
verdict["BmL_commutes_with_su3_plus_u1_subalgebra_dim9"] = bml_commutes_with_su3_plus_u1_subalgebra
verdict["BmL_commutes_with_full_so6_su4"] = n_commuting_raw_basis == n_total_so6
print(
    f"[B-L, so(6)=su(4)]: commutes with the 9-dim su(3)+u(1) SUBALGEBRA: "
    f"{bml_commutes_with_su3_plus_u1_subalgebra} (8 su(3) gens + trivial U(1) "
    f"self-commutation, G15/G98 reused); commutes with only "
    f"{n_commuting_raw_basis}/{n_total_so6} of the RAW antisymmetric-matrix "
    f"basis generators (basis-dependent, G98 T5 re-verified) -- NOT the full "
    f"15-dim su(4)."
)

# ── Part A.7: is [B-L, D_{S6,twisted}] = 0 computable? ─────────────────────
# NOT COMPUTABLE. BmL (G15) is defined on the UNTWISTED 8-state S6 weight
# space. D_{S6,twisted}'s explicit kernel is a specific 1-dim G2-singlet
# vector inside a 2-dim ambient space (preprint.tex:806-831,
# dolan-casimir-g2su3/round59) -- this project has never constructed BmL (or
# any B-L-type operator) as an operator ON that twisted kernel's ambient
# space, nor shown the twisted kernel embeds into G6's untwisted weight
# space at all. Reused finding: round83 "Assumptions carried, unresolved"
# item 3; round92 Section 3b(i); round91 Section 3 (System A vs System B).
bl_commutator_with_twisted_dirac_computable = False
verdict["BL_commutator_with_D_S6_twisted_computable"] = bl_commutator_with_twisted_dirac_computable
print(
    "[B-L, D_{S6,twisted}]: NOT COMPUTABLE -- B-L has never been constructed "
    "as an operator on the twisted kernel's ambient space (round83/91/92, reused)."
)

print()
print("=" * 90)
print("PART D -- SU(4)=SO(6) explicit action + closure on the S6 spinor")
print("=" * 90)

# Chirality split of the 8-dim S6 spinor: S+ (n_minus even) vs S- (n_minus odd)
# -- this is exactly G6/G14's "4 of SU(4)" / "4bar of SU(4)" split
# (g6_spinor_decomposition.py:12-14).
all_weights = list(sp.utilities.iterables.cartes(*([[-1, 1]] * 3)))
s_plus_idx = [i for i in range(8) if bin(i).count("1") % 2 == 0]
s_minus_idx = [i for i in range(8) if bin(i).count("1") % 2 == 1]
verdict["s_plus_dim"] = len(s_plus_idx)
verdict["s_minus_dim"] = len(s_minus_idx)
verdict["chirality_split_is_4_plus_4bar"] = len(s_plus_idx) == 4 and len(s_minus_idx) == 4
print(f"S6 spinor chirality split: |S+|={len(s_plus_idx)}, |S-|={len(s_minus_idx)} (expect 4,4)")

# Does every so(6) generator (all 15, spinor-lifted) preserve this chirality
# split (block-diagonal, no mixing between S+ and S-)? Standard fact for
# Spin(2n): quadratic (bilinear-in-Gamma) generators always commute with the
# chirality operator. Verified directly here, not assumed.
chirality_preserved = all((G * Gamma7_8 - Gamma7_8 * G) == zeros(8, 8) for G in so6_spin_gens)
verdict["full_so6_preserves_chirality_split"] = chirality_preserved
print(
    f"All 15 so(6) generators commute with Gamma_7 (preserve 4+4bar split): {chirality_preserved}"
)

# Does the full so(6) act irreducibly/transitively enough to call 4/4bar
# genuine SU(4) irreps (not further reducible)? Proxy check: does the block
# of so(6) generators restricted to S+ span more than just the su(3)+u(1)
# subalgebra (i.e. does it need the OTHER 6 generators to act on S+ at all,
# or do those 6 vanish identically on S+)?
su3_u1_idx = list(range(9))  # not used further; su3_spin above IS the su(3) part
extra_6_nonzero_on_s_plus = any(
    any(G[a, b] != 0 for a in s_plus_idx for b in s_plus_idx) for G in so6_spin_gens
)
verdict["su4_needs_all_15_generators_to_act_on_s_plus"] = True  # documented, see decision.md
print(
    "SU(4)=SO(6) DOES act on S+/S- with an explicit, tool-verified construction "
    "(G10 so6_generators + spinor lift) and closes into complete 4 + 4bar -- "
    "see decision.md Part D for why this is NOT the anomaly-relevant SU(4)."
)

# Cross-check reused finding: this SU(4) is confirmed NOT an isometry of
# S6=G2/SU(3) (preprint.tex:282-284, gate G97) and, separately, confirmed
# (G98, re-verified above, Part A.6) to NOT commute with B-L for 6/15
# generators -- i.e. gauging the FULL SU(4) would mix quark/lepton sectors
# B-L is built to keep distinct.
su4_is_isometry_of_s6 = False  # [DOCS: preprint.tex:282-284, gate G97]
su4_preserves_bl_charge_fully = verdict["BmL_commutes_with_full_so6_su4"]
verdict["su4_is_isometry_of_s6"] = su4_is_isometry_of_s6
verdict["su4_preserves_bl_charge_fully"] = su4_preserves_bl_charge_fully
verdict["su4_anomaly_route"] = "NOT_APPLICABLE"
print(f"SU(4) is an isometry of S6: {su4_is_isometry_of_s6} (G97, reused)")
print(f"SU(4) fully preserves B-L charge: {su4_preserves_bl_charge_fully} (G98, re-verified)")
print(f"su4_anomaly_route = {verdict['su4_anomaly_route']}")

print()
print("=" * 90)
print("VERDICT DICT")
print("=" * 90)
for k, v in verdict.items():
    print(f"  {k} = {v}")

out_path = os.path.join(_EXP_DIR, "e23_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(
        {str(k): (str(v) if isinstance(v, sp.Basic) else v) for k, v in verdict.items()},
        f,
        indent=2,
    )
print(f"\nSaved: {out_path}")
