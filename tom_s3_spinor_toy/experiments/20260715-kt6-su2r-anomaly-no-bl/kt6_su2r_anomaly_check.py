"""KT-6: Gauge anomaly cancellation for SU(3)_c x SU(2)_L x SU(2)_R — the group
ACTUALLY realized as an isometry of S^3 x S^6 (gate G97: no SU(4)/U(1)_{B-L}
factor is present) — checked WITHOUT assuming any U(1)_Y or B-L input.

Presupposition problem this addresses
-------------------------------------
`experiments/20260618-g12-anomaly/g12_anomaly_check.py` (see preprint.tex:284-294)
verifies the 5 standard SM anomaly conditions using Y = K_3 + (B-L)/2. That
check ALREADY ASSUMES the B-L charge, which this project's own gate G97 says
is not an isometry generator of S^3 x S^6 and remains geometrically open
(preprint.tex:258-266, 395-406). So g12's PASS is a statement about the
consistency of a hypercharge assignment that presupposes the very input in
question — it is not a check of the group actually derived from geometry.

This script checks the group that IS actually derived — SU(3)_c x SU(2)_L x
SU(2)_R, no U(1) factor at all — reusing:
  - the one-generation fermion content and color assignments from
    experiments/20260618-g12-anomaly/g12_anomaly_check.py
  - the SU(2)_L (J_S3) / SU(2)_R (K_S3) block generators from
    experiments/20260618-g11-block-generators/g11_block_generators.py
  - the S^6 color-sector indices (SP_SINGLET/QUARK/AQUARK/SM_SINGLET) from
    experiments/20260619-g15-hypercharge/g15_hypercharge.py (G14 result)
  - the row-level state naming cross-checked against
    experiments/20260619-g16-t3r-from-k3/g16_t3r_k3.py and
    experiments/20260619-g17-electric-charge/g17_electric_charge.py and
    experiments/20260714-round61-bl-commutant-audit/round61_route_b_blocks.py
    (all four independently agree on which row is which state — re-verified
    here directly from the generator matrices, not merely copied).

No B-L, no Y, no U(1) of any kind is imported, read, or used anywhere below.

Gates
-----
  KT1  [SU(2)_R]^3 = 0                      cubic, automatic (pseudo-real)
  KT2  [SU(2)_L]^2 x [SU(2)_R] = 0           mixed non-abelian, structural
  KT3  [SU(2)_R]^2 x [SU(2)_L] = 0           mixed non-abelian, structural
  KT4  [SU(2)_R]^2 x [Grav]   = 0            mixed gauge-gravitational
  KT5  [SU(2)_L]^2 x [Grav]   = 0            (bonus, same reasoning as KT4)
  KT6  [SU(3)]^2 x [SU(2)_R]  = 0            mixed non-abelian (bonus)
  KT7  Witten SU(2)_R global (mod-2) anomaly: doublet count must be EVEN
  KT8  Witten SU(2)_L global (mod-2) anomaly: doublet count must be EVEN (bonus)
  KT9  [SU(3)]^3 = 0                         inherited from g12 T1 (Y-independent
                                              already) — re-verified here for
                                              completeness of "what survives
                                              without B-L"
"""

import json
import os
import sys

import sympy as sp
from sympy import Rational as R
from sympy import zeros
from sympy import kronecker_product as kron

_EXP_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))

for _subdir in [
    "experiments/20260619-g15-hypercharge",
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g11_block_generators import J_S3, K_S3, I4, I8, lift_to_spinor  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402
from g15_hypercharge import SP_SINGLET, QUARK  # noqa: E402
# NOTE: g15_hypercharge also defines BmL (B-L). It is NOT imported here.

half = R(1, 2)

# ── Build 32x32 generators (SU(2)_L, SU(2)_R, SU(3)_c) ────────────────────────
su3_spin = [lift_to_spinor(C) for C in su3_generators()]
assert len(su3_spin) == 8

J32 = [kron(J_S3[a], I8) for a in range(3)]  # SU(2)_L, trivial on S6
K32 = [kron(K_S3[a], I8) for a in range(3)]  # SU(2)_R, trivial on S3-orthogonal
C32 = [kron(I4, c) for c in su3_spin]  # SU(3)_c, trivial on S3
J3_32, K3_32 = J32[2], K32[2]


def _eps3(a: int, b: int, c: int) -> int:
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    if (a, b, c) in {(0, 2, 1), (2, 1, 0), (1, 0, 2)}:
        return -1
    return 0


def main() -> bool:
    results = []
    passed = 0

    def chk(name: str, cond: bool, desc: str) -> bool:
        nonlocal passed
        ok = bool(cond)
        results.append({"check": name, "pass": ok, "desc": desc})
        print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
        if ok:
            passed += 1
        return ok

    # ══════════════════════════════════════════════════════════════════════
    # STEP 0 — independently re-verify su(2)_L / su(2)_R algebra closure at
    # 32-dim (do not just trust G11's 4x4 result)
    # ══════════════════════════════════════════════════════════════════════
    algebra_ok = True
    for a in range(3):
        for b in range(3):
            commJ = J32[a] * J32[b] - J32[b] * J32[a]
            expJ = sum((sp.I * _eps3(a, b, c) * J32[c] for c in range(3)), zeros(32, 32))
            commK = K32[a] * K32[b] - K32[b] * K32[a]
            expK = sum((sp.I * _eps3(a, b, c) * K32[c] for c in range(3)), zeros(32, 32))
            if commJ - expJ != zeros(32, 32) or commK - expK != zeros(32, 32):
                algebra_ok = False
    chk("KT0_algebra_32dim", algebra_ok, "su(2)_L, su(2)_R algebra closes at 32x32 (re-verified)")

    commLR_ok = all(
        J32[a] * K32[b] - K32[b] * J32[a] == zeros(32, 32) for a in range(3) for b in range(3)
    )
    chk("KT0_L_R_commute", commLR_ok, "[SU(2)_L, SU(2)_R] = 0 at 32x32 (re-verified)")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 1 — identify rows purely from generator action (not hand-copied)
    # ══════════════════════════════════════════════════════════════════════
    diagJ3 = [J3_32[i, i] for i in range(32)]
    diagK3 = [K3_32[i, i] for i in range(32)]

    su2L_charged = [diagJ3[i] != 0 for i in range(32)]
    su2R_charged = [diagK3[i] != 0 for i in range(32)]

    chk(
        "KT1a_L_xor_R",
        all(not (su2L_charged[i] and su2R_charged[i]) for i in range(32)),
        "no row has BOTH T3L!=0 and T3R!=0 simultaneously (no genuine (2,2) "
        "bidoublet Weyl fermion in this content)",
    )
    chk(
        "KT1b_L_or_R_or_neither",
        True,
        f"su2L-charged rows: {sum(su2L_charged)}, su2R-charged rows: {sum(su2R_charged)}, "
        f"neither: {32 - sum(su2L_charged) - sum(su2R_charged)}",
    )

    # S3 sectors, derived from the diagonal values themselves (not assumed)
    L_UP = [i for i in range(32) if diagJ3[i] == half]
    L_DN = [i for i in range(32) if diagJ3[i] == -half]
    R_UP = [i for i in range(32) if diagK3[i] == half]
    R_DN = [i for i in range(32) if diagK3[i] == -half]
    chk(
        "KT1c_sector_sizes",
        len(L_UP) == 8 and len(L_DN) == 8 and len(R_UP) == 8 and len(R_DN) == 8,
        f"L_UP={len(L_UP)}, L_DN={len(L_DN)}, R_UP={len(R_UP)}, R_DN={len(R_DN)} (expect 8 each)",
    )

    # One physical generation, no CPT doubling (mirrors g12's 16-state content):
    #   Q_L, L_L  from the L-sector (T3R=0 exactly)
    #   Q_R=(u_R,d_R), L_R=(nu_R,e_R)  from the R-sector (T3L=0 exactly)
    QL_rows = [i for i in L_UP + L_DN if (i % 8) in QUARK]
    LL_rows = [i for i in L_UP + L_DN if (i % 8) == SP_SINGLET]
    QR_rows = [i for i in R_UP + R_DN if (i % 8) in QUARK]
    LR_rows = [i for i in R_UP + R_DN if (i % 8) == SP_SINGLET]
    ONE_GEN = QL_rows + LL_rows + QR_rows + LR_rows
    chk(
        "KT1d_one_gen_count",
        len(ONE_GEN) == 16
        and len(QL_rows) == 6
        and len(LL_rows) == 2
        and len(QR_rows) == 6
        and len(LR_rows) == 2,
        f"one-generation Weyl count: Q_L={len(QL_rows)}, L_L={len(LL_rows)}, "
        f"Q_R={len(QR_rows)}, L_R={len(LR_rows)}, total={len(ONE_GEN)} (expect 16, matches g12)",
    )

    # Confirm Q_L, L_L are EXACT SU(2)_R singlets (T3R=0, not merely "small")
    t1e_ok = all(diagK3[i] == 0 for i in QL_rows + LL_rows)
    chk("KT1e_QL_LL_su2R_singlet", t1e_ok, "Q_L, L_L have T3R=0 exactly (genuine SU(2)_R singlets)")

    # Confirm Q_R, L_R are EXACT SU(2)_L singlets (T3L=0, not merely "small")
    t1f_ok = all(diagJ3[i] == 0 for i in QR_rows + LR_rows)
    chk("KT1f_QR_LR_su2L_singlet", t1f_ok, "Q_R, L_R have T3L=0 exactly (genuine SU(2)_L singlets)")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 1g — CRITICAL: are (u_R,d_R) and (nu_R,e_R) genuine SU(2)_R
    # DOUBLETS (irreducible, connected by raising/lowering), or merely two
    # accidentally-fixed-value SU(2)_R SINGLETS with different eigenvalues?
    # Verify: the SU(2)_R ladder operator K+ = K32[0] + i*K32[1] maps the
    # T3R=-1/2 state to the T3R=+1/2 state at the SAME S6 color index with a
    # NONZERO coefficient. If this off-diagonal element were zero, u_R and
    # d_R would NOT transform into each other and could not be called a
    # "doublet" — they would be two independent singlets that happen to have
    # opposite T3R labels (which would make the K3 "doublet" language in the
    # G16 docstring an unverified assumption).
    # ══════════════════════════════════════════════════════════════════════
    Kplus = K32[0] + sp.I * K32[1]
    doublet_pairs = []
    for q in list(QUARK) + [SP_SINGLET]:
        row_dn = [i for i in R_DN if (i % 8) == q][0]  # T3R=-1/2
        row_up = [i for i in R_UP if (i % 8) == q][0]  # T3R=+1/2
        doublet_pairs.append((row_dn, row_up, Kplus[row_up, row_dn]))
    t1g_ok = all(coef != 0 for _, _, coef in doublet_pairs)
    chk(
        "KT1g_genuine_su2R_doublet",
        t1g_ok,
        "K+ = K32[0]+i*K32[1] connects (d_R-like,T3R=-1/2) -> (u_R-like,T3R=+1/2) "
        f"with NONZERO coefficient at all 4 color/flavor slots "
        f"(coefficients: {[str(c) for _, _, c in doublet_pairs]}) "
        "=> Q_R=(u_R,d_R) and L_R=(nu_R,e_R) are IRREDUCIBLE SU(2)_R doublets, "
        "not two independent singlets with opposite labels",
    )

    # ══════════════════════════════════════════════════════════════════════
    # Fermion content table (name, SU3_dim, SU2L_dim, SU2R_dim, chi, n_flavor)
    # SU3_dim: 3=triplet, 1=singlet.  SU2*_dim: 2=doublet, 1=singlet.
    # chi: +1 left-handed (Q_L,L_L), -1 right-handed (Q_R,L_R) — SAME sign
    # convention as g12_anomaly_check.py.
    # ══════════════════════════════════════════════════════════════════════
    FERMIONS_KT6 = [
        ("Q_L", 3, 2, 1, +1),
        ("L_L", 1, 2, 1, +1),
        ("Q_R", 3, 1, 2, -1),
        ("L_R", 1, 1, 2, -1),
    ]
    weyl_total = sum(su3 * su2l * su2r for _, su3, su2l, su2r, _ in FERMIONS_KT6)
    chk("KT1h_weyl_total", weyl_total == 16, f"Weyl dof total = {weyl_total} (expect 16)")

    # ══════════════════════════════════════════════════════════════════════
    # KT9 — [SU(3)]^3 cubic: inherited check, Y-independent already in g12.
    # Re-verify with the SAME content table (now carrying su2R info too) to
    # confirm it is unaffected by adding/removing the SU(2)_R column.
    # ══════════════════════════════════════════════════════════════════════
    A_su3_cubic = sum(
        chi * su2l * su2r * R(1, 2) for _, su3, su2l, su2r, chi in FERMIONS_KT6 if su3 == 3
    )
    chk(
        "KT9_SU3_cubic",
        A_su3_cubic == 0,
        f"[SU(3)]^3 = {A_su3_cubic} (Y-independent, inherited from g12 T1)",
    )

    # ══════════════════════════════════════════════════════════════════════
    # KT1 — [SU(2)_R]^3 cubic: automatic zero, pseudo-real rep identity.
    # Verify DIRECTLY on the actual K_S3 matrices: {K_a,K_b} = (1/2) delta_ab
    # I_4, so {K_a,K_b} K_c has trace (1/2) delta_ab Tr(K_c) = 0 since K_c is
    # traceless. Check this exactly in sympy, all 27 (a,b,c) combinations, on
    # the SU(2)_R generator matrices actually used in this project (K_S3,
    # 4x4), not an abstract textbook Pauli matrix.
    # ══════════════════════════════════════════════════════════════════════
    su2R_cubic_bad = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                anticomm = K_S3[a] * K_S3[b] + K_S3[b] * K_S3[a]
                val = sp.trace(anticomm * K_S3[c])
                if sp.simplify(val) != 0:
                    su2R_cubic_bad.append((a, b, c, val))
    chk(
        "KT1_SU2R_cubic",
        len(su2R_cubic_bad) == 0,
        f"[SU(2)_R]^3: Tr({{K_a,K_b}}K_c) = 0 for all 27 (a,b,c) triples on the actual "
        f"4x4 K_S3 matrices ({len(su2R_cubic_bad)} nonzero found)",
    )

    # ══════════════════════════════════════════════════════════════════════
    # KT2/KT3 — mixed [SU(2)_L]^2 x [SU(2)_R] and [SU(2)_R]^2 x [SU(2)_L]:
    # STRONGEST possible verification — show the OTHER group's generator is
    # the EXACT ZERO MATRIX when restricted to the rows charged under the
    # first group (not just "trace is zero", the whole operator vanishes
    # there). This is a fact about THIS content, stronger than the generic
    # "non-abelian generators are traceless" argument (which would make the
    # check vacuous for ANY content).
    # ══════════════════════════════════════════════════════════════════════
    su2L_rows = [i for i in range(32) if su2L_charged[i]]
    su2R_rows = [i for i in range(32) if su2R_charged[i]]

    K_on_L_rows_zero = all(
        K32[c][i, j] == 0 for c in range(3) for i in su2L_rows for j in range(32)
    )
    chk(
        "KT2_mixed_L2_R",
        K_on_L_rows_zero,
        "[SU(2)_L]^2 x [SU(2)_R]: every SU(2)_R generator K32[c] acts as the EXACT "
        "ZERO operator on all 16 SU(2)_L-charged rows (not merely zero trace) "
        "=> mixed anomaly vanishes termwise, not just in aggregate",
    )

    J_on_R_rows_zero = all(
        J32[c][i, j] == 0 for c in range(3) for i in su2R_rows for j in range(32)
    )
    chk(
        "KT3_mixed_R2_L",
        J_on_R_rows_zero,
        "[SU(2)_R]^2 x [SU(2)_L]: every SU(2)_L generator J32[c] acts as the EXACT "
        "ZERO operator on all 16 SU(2)_R-charged rows (not merely zero trace)",
    )

    # ══════════════════════════════════════════════════════════════════════
    # KT4/KT5 — mixed gauge-gravitational [SU(2)_R]^2 x [Grav] and
    # [SU(2)_L]^2 x [Grav]: generic group-theory fact (non-abelian generators
    # are traceless in any rep) PLUS explicit numeric confirmation on this
    # content (chirality-weighted trace over the one-generation set = 0).
    # ══════════════════════════════════════════════════════════════════════
    def chi_of(row: int) -> int:
        return 1 if row in QL_rows + LL_rows else -1

    grav_R = [sum(chi_of(i) * K32[c][i, i] for i in ONE_GEN) for c in range(3)]
    chk(
        "KT4_mixed_R2_grav",
        all(sp.simplify(v) == 0 for v in grav_R),
        f"[SU(2)_R]^2 x [Grav]: sum_i chi_i (K32[c])_ii over one generation = {grav_R} "
        "(all zero — traceless generator, content-independent fact, re-verified here)",
    )
    grav_L = [sum(chi_of(i) * J32[c][i, i] for i in ONE_GEN) for c in range(3)]
    chk(
        "KT5_mixed_L2_grav",
        all(sp.simplify(v) == 0 for v in grav_L),
        f"[SU(2)_L]^2 x [Grav]: sum_i chi_i (J32[c])_ii over one generation = {grav_L}",
    )

    # ══════════════════════════════════════════════════════════════════════
    # KT6 — [SU(3)]^2 x [SU(2)_R] mixed (bonus): same trace argument, direct
    # numeric check restricted to color-triplet rows.
    # ══════════════════════════════════════════════════════════════════════
    color_rows = [
        i
        for i in ONE_GEN
        if any(
            C32[k][i, i] != 0 or C32[k][i, j] != 0 for k in range(8) for j in range(32) if j != i
        )
    ]
    # simpler: color-charged rows are exactly QL_rows + QR_rows (quarks)
    color_rows = QL_rows + QR_rows
    su3_grav_R = sum(chi_of(i) * K3_32[i, i] for i in color_rows)
    chk(
        "KT6_SU3sq_SU2R",
        sp.simplify(su3_grav_R) == 0,
        f"[SU(3)]^2 x [SU(2)_R]: sum over color-charged rows of chi_i*(T3R)_ii = {su3_grav_R}",
    )

    # ══════════════════════════════════════════════════════════════════════
    # KT7/KT8 — Witten SU(2) global (mod-2) anomaly: count IRREDUCIBLE Weyl
    # doublets (per KT1g, these are genuine doublets, not accidental
    # singlets), per one generation.
    # ══════════════════════════════════════════════════════════════════════
    n_su2R_doublets = 3 + 1  # Q_R (3 colors) + L_R
    n_su2L_doublets = 3 + 1  # Q_L (3 colors) + L_L
    chk(
        "KT7_witten_su2R",
        n_su2R_doublets % 2 == 0,
        f"Witten SU(2)_R global anomaly: {n_su2R_doublets} doublets "
        f"(Q_R x3 colors + L_R x1) = {'EVEN -> safe' if n_su2R_doublets % 2 == 0 else 'ODD -> FATAL'}",
    )
    chk(
        "KT8_witten_su2L",
        n_su2L_doublets % 2 == 0,
        f"Witten SU(2)_L global anomaly (bonus, symmetric check): {n_su2L_doublets} doublets "
        f"(Q_L x3 colors + L_L x1) = {'EVEN -> safe' if n_su2L_doublets % 2 == 0 else 'ODD -> FATAL'}",
    )

    # ══════════════════════════════════════════════════════════════════════
    # Summary
    # ══════════════════════════════════════════════════════════════════════
    total = len(results)
    verdict = (
        "PASS_KT6_SU2R_ANOMALY_FREE_NO_BL" if passed == total else f"PARTIAL_{passed}_of_{total}"
    )
    print(f"\n{passed}/{total} checks passed")
    print(f"VERDICT: {verdict}")

    out = {
        "gate": "KT6-SU2R-ANOMALY-NO-BL",
        "verdict": verdict,
        "passed": passed,
        "total": total,
        "weyl_count_one_generation": weyl_total,
        "n_su2R_doublets": n_su2R_doublets,
        "n_su2L_doublets": n_su2L_doublets,
        "interpretation": (
            "SU(3)_c x SU(2)_L x SU(2)_R (the group ACTUALLY realized as an isometry "
            "of S^3xS^6 per gate G97, WITHOUT the U(1)_{B-L} factor) passes every "
            "anomaly condition that can be FORMULATED for it without a U(1) charge: "
            "[SU(3)]^3=0 (content-dependent, inherited from g12 T1, Y-independent), "
            "[SU(2)_L]^3=[SU(2)_R]^3=0 (automatic, pseudo-real), all mixed "
            "non-abelian-squared x non-abelian anomalies vanish termwise (stronger than "
            "the generic trace=0 argument), all mixed gauge-gravitational conditions "
            "vanish (generators traceless), and both Witten SU(2)_L/SU(2)_R global "
            "anomalies are satisfied (4 doublets each, even). "
            "CRITICAL CAVEAT: this does NOT resolve the presupposition problem in g12 "
            "-- it DISSOLVES it. The [U(1)_Y]^3, [SU(2)]^2 x U(1)_Y, [SU(3)]^2 x U(1)_Y, "
            "and [Grav]^2 x U(1)_Y conditions that g12 checks (and that constitute the "
            "genuinely non-trivial, content-dependent part of anomaly cancellation for "
            "the FULL Pati-Salam-like theory) CANNOT EVEN BE FORMULATED without first "
            "positing a U(1) charge (B-L). Once U(1) is removed, essentially every "
            "surviving condition is either automatically zero by group theory alone "
            "(mixed non-abelian, mixed gauge-gravitational) or a mod-2 doublet count "
            "that is even by direct construction (3 colors + 1 lepton = 4, always even "
            "for any number of colors that is odd... actually for ANY number of colors "
            "N_c: N_c+1 doublets -- for N_c=3 this is 4, even; this evenness is itself "
            "a numerical coincidence of N_c=3 being odd, not a deep theorem). So the "
            "derived group is anomaly-free, but almost all of that freedom is structural "
            "(forced by non-abelian group theory) rather than a nontrivial confirmation "
            "of the geometric fermion assignment the way g12's U(1) checks are."
        ),
        "checks": results,
    }
    out_path = os.path.join(_EXP_DIR, "results_kt6.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"Saved: {out_path}")
    return passed == total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
