"""C101 -- assembles the smallest possible 2-level (k=1,2) D_PW using
C85's certified D-bar (per level, on (p,r)) and C100's certified
multiplication matrix M_1 (on (q,p)), under the EXPLICITLY UNVERIFIED
"r-untouched" hypothesis (M_1 (x) I_r as the off-diagonal coupling --
see claim.md's Counterfactual Frame for why this is a postulated
ansatz, not a derived fact). Tests whether this coupling produces a
genuine spectral shift relative to the uncoupled (block-diagonal)
union -- the smallest possible instance of the truncation-convergence
/ spectral-flow test C90's own decision.md scoped as the final step.
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
RESULTS_PATH = HERE / "results_c101.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99/C100's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99/C100's own m_q, m_p extraction exactly (physical
    spin units, j1=k/2)."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_multiplication_matrix(c85_mod, k: int) -> sp.Matrix:
    """Reproduces C100's own M_k assembly exactly (single D^1_{1/2,1/2}
    component, level k -> k+1, (q,p)-only)."""
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
    """General (non-Hermitian-assuming) eigenvalue solver, matching
    C85's own established convention (np.linalg.eigvals, NOT eigvalsh
    -- see decision.md: D-bar itself is real-spectrum but NOT
    symmetric/Hermitian as a raw matrix, so eigvalsh would silently
    read only one triangle and produce wrong values. This was a
    genuine self-caught bug in an earlier draft of this script, caught
    because P0's own reuse-sanity check against C85's certified
    eigenvalues failed for k=2 (k=1 happened to still work, by
    coincidence of eigvalsh being closer to correct there -- see
    decision.md). Returns (grouped eigenvalues, max |imaginary part|)."""
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
        """D-bar tensored with identity on q -- the FULL level-k
        operator on (q,p,r)."""
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], right_mult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D1_full = dbar_full(1)
    D2_full = dbar_full(2)

    # P0: reuse sanity -- individually reproduce C85's own certified
    # eigenvalues before combining anything. Uses the GENERAL
    # eigenvalue solver (matching C85's own np.linalg.eigvals
    # convention) -- D-bar is real-SPECTRUM but NOT Hermitian/symmetric
    # as a raw matrix (verified directly, e.g. entry (1,2)=-2 but
    # (2,1)=-4 in the k=2 case); an earlier draft used np.linalg.eigvalsh
    # (Hermitian-only, silently reads one triangle) and got WRONG
    # eigenvalues for k=2 specifically -- self-caught because THIS
    # exact P0 check failed, exactly as it was designed to catch.
    D1_np = np.array(D1_full.evalf().tolist(), dtype=complex).real
    D2_np = np.array(D2_full.evalf().tolist(), dtype=complex).real
    eigs_D1, imag_D1 = eigen_multiplicities_general(D1_np)
    eigs_D2, imag_D2 = eigen_multiplicities_general(D2_np)
    expected_D1 = {-1.0: 6, 3.0: 2}
    expected_D2 = {-2.0: 12, 4.0: 6}
    found_D1 = {round(v): m for v, m in eigs_D1}
    found_D2 = {round(v): m for v, m in eigs_D2}
    p0_ok = (found_D1 == expected_D1) and (found_D2 == expected_D2)
    print(f"P0: D1_full eigs {found_D1} (expect {expected_D1}), max|Im|={imag_D1:.2e}")
    print(f"P0: D2_full eigs {found_D2} (expect {expected_D2}), max|Im|={imag_D2:.2e}")
    print(f"P0 ok: {p0_ok}")

    # Build M_1 (q,p)-only, then extend trivially to r (I_2) -- the
    # explicitly unverified "r-untouched" ansatz.
    M1 = build_multiplication_matrix(c85, 1)
    B = sp.Matrix(sp.kronecker_product(M1, sp.eye(2)))
    print(f"B shape: {B.shape} (expect (18,8))")

    dim_total = D1_full.shape[0] + D2_full.shape[0]
    D_PW = sp.zeros(dim_total, dim_total)
    n1 = D1_full.shape[0]
    D_PW[:n1, :n1] = D1_full
    D_PW[n1:, n1:] = D2_full
    D_PW[n1:, :n1] = B
    D_PW[:n1, n1:] = B.H

    # P1 (RENAMED from an earlier "Hermiticity guaranteed by
    # construction" framing -- that reasoning was WRONG, discovered
    # while fixing P0: D-bar itself is NOT Hermitian, so [[A,B^H],[B,C]]
    # is NOT automatically Hermitian when A,C aren't Hermitian to begin
    # with. This is now a genuinely open, non-trivial question: does
    # this specific construction still produce a real spectrum?
    D_PW_np = np.array(D_PW.evalf().tolist(), dtype=complex)
    coupled_eigs, coupled_max_imag = eigen_multiplicities_general(D_PW_np)
    p1_real_spectrum = coupled_max_imag < 1e-6
    print(
        f"P1 (genuine check, NOT guaranteed): real spectrum = {p1_real_spectrum} (max|Im|={coupled_max_imag:.2e})"
    )

    # P2: the actual test -- does coupling shift the spectrum relative
    # to the uncoupled union?
    uncoupled_union = sorted(eigs_D1 + eigs_D2, key=lambda x: x[0])
    coupled_values = sorted(round(v, 6) for v, _m in coupled_eigs)
    uncoupled_values = sorted(round(v, 6) for v, m in uncoupled_union for _ in range(m))
    max_abs_shift = max(abs(c - u) for c, u in zip(coupled_values, uncoupled_values))
    p2_shift_found = max_abs_shift > 1e-6

    print(f"\nUncoupled union eigenvalues: {[(v, m) for v, m in uncoupled_union]}")
    print(f"Coupled D_PW eigenvalues: {coupled_eigs}")
    print(f"Max |coupled - uncoupled| (paired by rank): {max_abs_shift}")
    print(f"P2 shift found: {p2_shift_found}")

    if not p0_ok:
        verdict = "P0_REUSE_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif not p1_real_spectrum:
        verdict = "P1_COMPLEX_SPECTRUM__R_UNTOUCHED_ANSATZ_PLUS_THIS_B_DAGGER_CHOICE_DOES_NOT_YIELD_REAL_EIGENVALUES"
    elif p2_shift_found:
        verdict = "SPECTRAL_SHIFT_FOUND__CONSTRUCTION_NOT_INERT_R_UNTOUCHED_ANSATZ_UNVERIFIED"
    else:
        verdict = "NO_SPECTRAL_SHIFT__CONSTRUCTION_SPECTRALLY_INERT_AT_THIS_SCALE"

    out = {
        "p0_reuse_ok": p0_ok,
        "found_D1_eigs": found_D1,
        "found_D2_eigs": found_D2,
        "B_shape": list(B.shape),
        "p1_real_spectrum": p1_real_spectrum,
        "p1_max_imag": coupled_max_imag,
        "uncoupled_union_eigs": [[v, m] for v, m in uncoupled_union],
        "coupled_eigs": [[v, m] for v, m in coupled_eigs],
        "max_abs_shift": max_abs_shift,
        "p2_shift_found": p2_shift_found,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
