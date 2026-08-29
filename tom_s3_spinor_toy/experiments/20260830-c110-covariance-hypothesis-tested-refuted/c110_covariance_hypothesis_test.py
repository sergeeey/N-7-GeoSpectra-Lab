"""C110 -- tests C109's own pearl (does "covariance" -- correspondence
to a genuine real quaternion coordinate -- predict whether a k=1
coupling preserves the real-spectrum property?). Reuses only certified
c85/C99 machinery. See claim.md's Counterfactual Frame for the disclosed
scratch-exploration (including a mid-round refutation, reported
honestly) that preceded this formal script.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import I as SI
from sympy import Rational, S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c110.json"

AW, AX, BW, BX = sp.symbols("aw ax bw bx", real=True)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_M_ab(c85_mod, k: int, a, b) -> sp.Matrix:
    j1 = S(k) / 2
    j2 = S(1) / 2
    j_target = j1 + S(1) / 2
    dim_k = k + 1
    dim_kp1 = k + 2

    m_q_k, m_p_k = magnetic_labels(c85_mod, k)
    m_q_kp1, m_p_kp1 = magnetic_labels(c85_mod, k + 1)
    q_index_at_m = {v: idx for idx, v in enumerate(m_q_kp1)}
    p_index_at_m = {v: idx for idx, v in enumerate(m_p_kp1)}

    M = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
    for q in range(dim_k):
        for p in range(dim_k):
            m_q_target = m_q_k[q] + a
            m_p_target = m_p_k[p] + b
            if m_q_target not in q_index_at_m or m_p_target not in p_index_at_m:
                continue
            Q = q_index_at_m[m_q_target]
            P = p_index_at_m[m_p_target]
            val_q = CG(j1, m_q_k[q], j2, a, j_target, m_q_target).doit()
            val_p = CG(j1, m_p_k[p], j2, b, j_target, m_p_target).doit()
            M[Q * dim_kp1 + P, q * dim_k + p] = sp.simplify(val_q * val_p)
    return M


def symbolic_value(c1, c2, c3, c4):
    """The exact (aw,ax,bw,bx) decomposition of c1*Mpp+c2*Mpm+c3*Mmp+c4*Mmm,
    using Mpp=aw+i*ax, Mpm=bw+i*bx, Mmp=-bw+i*bx, Mmm=aw-i*ax."""
    e = c1 * (AW + SI * AX) + c2 * (BW + SI * BX) + c3 * (-BW + SI * BX) + c4 * (AW - SI * AX)
    e = sp.expand(e)
    return e, sp.expand(sp.re(e)), sp.expand(sp.im(e))


def eigen_max_imag(matrix_numeric: np.ndarray) -> float:
    eigvals = np.linalg.eigvals(matrix_numeric)
    return float(np.max(np.abs(np.imag(eigvals))))


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(k: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D1 = dbar_full(1)
    D2 = dbar_full(2)
    n1, n2 = D1.shape[0], D2.shape[0]
    nt = n1 + n2
    D1_np = np.array(D1.evalf().tolist(), dtype=np.float64)
    D2_np = np.array(D2.evalf().tolist(), dtype=np.float64)

    half = S(1) / 2
    M_pp = build_M_ab(c85, 1, half, half)
    M_pm = build_M_ab(c85, 1, half, -half)
    M_mp = build_M_ab(c85, 1, -half, half)
    M_mm = build_M_ab(c85, 1, -half, -half)

    def test(c1, c2, c3, c4):
        M = c1 * M_pp + c2 * M_pm + c3 * M_mp + c4 * M_mm
        Bs = sp.Matrix(sp.kronecker_product(M, sp.eye(2)))
        Bs_np = np.array(Bs.evalf().tolist(), dtype=complex)
        DPW = np.zeros((nt, nt), dtype=complex)
        DPW[:n1, :n1] = D1_np
        DPW[n1:, n1:] = D2_np
        DPW[n1:, :n1] = Bs_np
        DPW[:n1, n1:] = Bs_np.conj().T
        return eigen_max_imag(DPW)

    half_i = Rational(1, 2) * SI
    CASES = {
        "M_sum (1,1,1,1)": (1, 1, 1, 1),
        "aw (1/2,0,0,1/2)": (half, 0, 0, half),
        "ax (i/2,0,0,-i/2)": (half_i, 0, 0, -half_i),
        "bw (0,1/2,-1/2,0)": (0, half, -half, 0),
        "bx (0,i/2,i/2,0)": (0, half_i, half_i, 0),
        "aw+bw (1/2,1/2,-1/2,1/2)": (half, half, -half, half),
        "aw+i*bw (1/2,i/2,-i/2,1/2)": (half, half_i, -half_i, half),
        "aw+bx (1/2,-i/2,-i/2,1/2)": (half, -half_i, -half_i, half),
        "i*aw (i/2,0,0,i/2)": (half_i, 0, 0, half_i),
        "arbitrary (1,2,3,4)": (1, 2, 3, 4),
        "alternating (1,-1,1,-1)": (1, -1, 1, -1),
        "(2,1,1,2)": (2, 1, 1, 2),
        "Mmp-flipped (1,1,-1,1)": (1, 1, -1, 1),
    }

    rows = {}
    for label, (c1, c2, c3, c4) in CASES.items():
        value, re_part, im_part = symbolic_value(c1, c2, c3, c4)
        max_imag = test(c1, c2, c3, c4)
        imag_is_zero = im_part == 0
        rows[label] = {
            "value": str(value),
            "real_part": str(re_part),
            "imag_part": str(im_part),
            "imag_part_is_zero": bool(imag_is_zero),
            "max_imag_eig": max_imag,
            "spectrum_real": bool(max_imag < 1e-6),
        }
        print(
            f"{label}: value={value} | imag_part={im_part} (zero={imag_is_zero}) "
            f"| max|Im(eig)|={max_imag:.6f}"
        )

    # --- P0: reproduce Stage 1 exactly ---
    p0_ok = (
        rows["aw (1/2,0,0,1/2)"]["spectrum_real"]
        and rows["ax (i/2,0,0,-i/2)"]["spectrum_real"]
        and rows["bw (0,1/2,-1/2,0)"]["spectrum_real"]
        and rows["bx (0,i/2,i/2,0)"]["spectrum_real"]
        and abs(rows["M_sum (1,1,1,1)"]["max_imag_eig"] - 0.10592470995283362) < 1e-6
    )

    # --- P1: aw+bw real, aw+i*bw ALSO real (the counter-example) ---
    p1_ok = (
        rows["aw+bw (1/2,1/2,-1/2,1/2)"]["spectrum_real"]
        and rows["aw+i*bw (1/2,i/2,-i/2,1/2)"]["spectrum_real"]
    )

    # --- P2: zero-imag_part cases are ALWAYS real (no false negatives) ---
    zero_imag_cases = [r for r in rows.values() if r["imag_part_is_zero"]]
    p2_ok = all(r["spectrum_real"] for r in zero_imag_cases)

    # --- P3: specific nonzero-imag_part cases that are STILL real (false positives for naive hypothesis) ---
    false_positive_labels = [
        "aw+i*bw (1/2,i/2,-i/2,1/2)",
        "i*aw (i/2,0,0,i/2)",
    ]
    p3_ok = all(rows[label]["spectrum_real"] for label in false_positive_labels) and all(
        not rows[label]["imag_part_is_zero"] for label in false_positive_labels
    )

    # --- P4: at least one nonzero-imag_part case genuinely breaks reality ---
    breaking_labels = [
        "M_sum (1,1,1,1)",
        "arbitrary (1,2,3,4)",
        "alternating (1,-1,1,-1)",
        "(2,1,1,2)",
    ]
    p4_ok = all(
        (not rows[label]["imag_part_is_zero"]) and (not rows[label]["spectrum_real"])
        for label in breaking_labels
    )

    print(f"\nP0: {p0_ok}  P1: {p1_ok}  P2: {p2_ok}  P3: {p3_ok}  P4: {p4_ok}")

    all_predictions_ok = p0_ok and p1_ok and p2_ok and p3_ok and p4_ok

    if all_predictions_ok:
        verdict = "COVARIANCE_HYPOTHESIS_REFUTED__NO_SINGLE_CRITERION_FOUND_THIS_ROUND"
    else:
        verdict = "UNEXPECTED_PATTERN__SEE_DETAILS"

    out = {
        "rows": rows,
        "p0_ok": p0_ok,
        "p1_ok": p1_ok,
        "p2_ok": p2_ok,
        "p3_ok": p3_ok,
        "p4_ok": p4_ok,
        "all_predictions_ok": all_predictions_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert p0_ok, "P0 failed -- did not reproduce Stage 1 baseline"
    assert p2_ok, "P2 failed -- some zero-imag_part case unexpectedly non-real"


if __name__ == "__main__":
    main()
