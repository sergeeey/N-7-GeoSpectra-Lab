"""C103 -- the first genuinely block-tridiagonal D_PW (k=1,2,3), the
literal construction C90's own decision.md named as this arc's final
step. Reuses C101/C102's own dbar_full(k) and build_multiplication_matrix
verbatim (no new construction logic) to test:

P1: does the exactly-real-spectrum property found at 2 independent
    2-level pairs (C101: k=1,2; C102: k=2,3) survive a genuine 3-level
    system with an INDIRECT 1<->3 correlation neither prior round
    tested (M_k only connects adjacent levels -- the (1,3) block is
    exactly zero by construction, so any 1<->3 effect is purely
    level-2-mediated)?
P2: truncation convergence -- do the lowest-magnitude eigenvalues of
    the 3-level system stay close to the 2-level (k=1,2) system's own
    lowest eigenvalues, or does adding level 3 substantially reshuffle
    them?

Still under the same explicitly-unverified "r-untouched" ansatz as
C101/C102 (M_k (x) I_r) -- see those files' own Counterfactual Frame.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c103.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99-C102's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99-C102's own m_q, m_p extraction exactly (physical
    spin units, j1=k/2)."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_multiplication_matrix(c85_mod, k: int) -> sp.Matrix:
    """Reproduces C100-C102's own M_k assembly exactly (single
    D^1_{1/2,1/2} component, level k -> k+1, (q,p)-only)."""
    j1 = S(k) / 2
    j2 = S(1) / 2
    j_target = j1 + S(1) / 2
    a = S(1) / 2
    b = S(1) / 2
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


def eigen_multiplicities_general(
    matrix_numeric: np.ndarray,
) -> tuple[list[tuple[float, int]], float]:
    """General (non-Hermitian-assuming) eigenvalue solver -- see C101's
    own decision.md for why eigvalsh must never be used on D-bar or
    operators built from it (self-caught bug there, recurred 3x in
    this lineage per boyko-project-radar's sci-code-audit finding)."""
    eigvals = np.linalg.eigvals(matrix_numeric)
    max_imag = float(np.max(np.abs(np.imag(eigvals))))
    rounded = sorted(float(np.real(v)) for v in eigvals)
    grouped: list[list[float | int]] = []
    for v in rounded:
        if grouped and abs(grouped[-1][0] - v) < 1e-6:
            grouped[-1][1] += 1
        else:
            grouped.append([v, 1])
    return [(v, m) for v, m in grouped], max_imag


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    right_mult = [
        c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    ]

    def dbar_full(k: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], right_mult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D1_full = dbar_full(1)
    D2_full = dbar_full(2)
    D3_full = dbar_full(3)

    # P0: reuse sanity.
    expected = {
        1: {-1.0: 6, 3.0: 2},
        2: {-2.0: 12, 4.0: 6},
        3: {-3.0: 20, 5.0: 12},
    }
    blocks = {1: D1_full, 2: D2_full, 3: D3_full}
    found = {}
    p0_ok = True
    for k, D in blocks.items():
        D_np = np.array(D.evalf().tolist(), dtype=complex).real
        eigs, imag = eigen_multiplicities_general(D_np)
        f = {round(v): m for v, m in eigs}
        found[k] = f
        ok = f == expected[k]
        p0_ok = p0_ok and ok
        print(f"P0: D{k}_full eigs {f} (expect {expected[k]}), max|Im|={imag:.2e}, ok={ok}")
    print(f"P0 overall ok: {p0_ok}")

    M1 = build_multiplication_matrix(c85, 1)
    M2 = build_multiplication_matrix(c85, 2)
    B1 = sp.Matrix(sp.kronecker_product(M1, sp.eye(2)))
    B2 = sp.Matrix(sp.kronecker_product(M2, sp.eye(2)))
    print(f"B1 shape: {B1.shape} (expect (18,8))")
    print(f"B2 shape: {B2.shape} (expect (32,18))")

    n1, n2, n3 = D1_full.shape[0], D2_full.shape[0], D3_full.shape[0]
    dim_total = n1 + n2 + n3
    D_PW = sp.zeros(dim_total, dim_total)
    D_PW[:n1, :n1] = D1_full
    D_PW[n1 : n1 + n2, n1 : n1 + n2] = D2_full
    D_PW[n1 + n2 :, n1 + n2 :] = D3_full
    D_PW[n1 : n1 + n2, :n1] = B1
    D_PW[:n1, n1 : n1 + n2] = B1.H
    D_PW[n1 + n2 :, n1 : n1 + n2] = B2
    D_PW[n1 : n1 + n2, n1 + n2 :] = B2.H
    # (1,3) and (3,1) blocks left exactly zero -- M_k only connects
    # adjacent levels; any 1<->3 effect is purely level-2-mediated.
    print(f"D_PW total shape: {D_PW.shape} (expect (58,58))")

    D_PW_np = np.array(D_PW.evalf().tolist(), dtype=complex)
    coupled_eigs, coupled_max_imag = eigen_multiplicities_general(D_PW_np)
    p1_real_spectrum = coupled_max_imag < 1e-6
    print(
        f"P1 (genuinely new territory -- indirect 1<->3 correlation untested by C101/C102): "
        f"real spectrum = {p1_real_spectrum} (max|Im|={coupled_max_imag:.2e})"
    )

    # P2: truncation convergence -- compare lowest-magnitude eigenvalues
    # of the 3-level system against the 2-level (k=1,2) system (C101's
    # own certified result, hardcoded here from results_c101.json to
    # avoid re-running C101 as a side effect of this round).
    c101_results_path = (
        HERE.parent
        / "20260812-c101-smallest-two-level-dpw-spectral-shift-test"
        / "results_c101.json"
    )
    c101_data = json.loads(c101_results_path.read_text())
    two_level_eigs = sorted(v for v, m in c101_data["coupled_eigs"] for _ in range(m))
    three_level_eigs = sorted(v for v, m in coupled_eigs for _ in range(m))

    n_compare = min(5, len(two_level_eigs))
    two_level_lowest = sorted(two_level_eigs, key=abs)[:n_compare]
    three_level_lowest = sorted(three_level_eigs, key=abs)[:n_compare]
    lowest_shift = max(
        abs(a - b) for a, b in zip(sorted(two_level_lowest), sorted(three_level_lowest))
    )
    convergence_tolerance = 1.0  # O(1) tolerance -- eigenvalues here span -k..k+2, a shift
    # smaller than 1 is "close" relative to that scale; larger is a real reshuffle.
    p2_converges = lowest_shift < convergence_tolerance

    print(f"\n2-level (k=1,2) lowest-|value| eigenvalues: {sorted(two_level_lowest)}")
    print(f"3-level (k=1,2,3) lowest-|value| eigenvalues: {sorted(three_level_lowest)}")
    print(f"Max shift among lowest {n_compare}: {lowest_shift}")
    print(f"P2 converges (shift < {convergence_tolerance}): {p2_converges}")

    if not p0_ok:
        verdict = "P0_REUSE_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif not p1_real_spectrum:
        verdict = "P1_COMPLEX_SPECTRUM__REAL_SPECTRUM_DOES_NOT_SURVIVE_3_LEVEL_INDIRECT_COUPLING"
    elif p2_converges:
        verdict = "TRUNCATION_APPEARS_TO_CONVERGE__LOWEST_EIGENVALUES_STABLE_ACROSS_2_TO_3_LEVELS"
    else:
        verdict = (
            "TRUNCATION_DOES_NOT_CONVERGE__LOWEST_EIGENVALUES_SHIFT_SUBSTANTIALLY_ADDING_LEVEL_3"
        )

    out = {
        "p0_reuse_ok": p0_ok,
        "found_per_level": found,
        "B1_shape": list(B1.shape),
        "B2_shape": list(B2.shape),
        "D_PW_shape": list(D_PW.shape),
        "p1_real_spectrum": p1_real_spectrum,
        "p1_max_imag": coupled_max_imag,
        "coupled_eigs": [[v, m] for v, m in coupled_eigs],
        "two_level_lowest": two_level_lowest,
        "three_level_lowest": three_level_lowest,
        "lowest_shift": lowest_shift,
        "convergence_tolerance": convergence_tolerance,
        "p2_converges": p2_converges,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    # Hard invariant gate (boyko-project-radar Chain 1 convention,
    # placed AFTER the JSON write so a genuine future failure still
    # persists the P0/verdict data first).
    assert coupled_max_imag < 1e-6, (
        f"D_PW (3-level) spectrum is not real (max|Im|={coupled_max_imag:.2e}) -- "
        f"see {RESULTS_PATH} for the persisted verdict before investigating"
    )


if __name__ == "__main__":
    main()
