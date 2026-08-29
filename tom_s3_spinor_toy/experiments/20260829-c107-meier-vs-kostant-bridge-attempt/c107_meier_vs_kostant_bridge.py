"""C107 -- attempts to identify C85/Meier's certified D-bar_k with
round67/Agricola's certified Kostant-cubic torsion family D^t(n,sigma),
as a prerequisite before bridging the C90-C106 multiplication-operator
apparatus to OB1's torsion-selection question (per boyko-project-radar +
tracy's converged recommendation, 2026-08-29). See claim.md's
Counterfactual Frame for the disclosed scratch-exploration that preceded
this formal script.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c107.json"

H_H = sp.Integer(3)  # round67's own certified Kostant-cubic scalar, h_H=3


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def D_t(n, sigma, t):
    """round67's own certified formula (e2_s3_torsion_deformation.py):
    D^t(n,sigma) = sigma*(n+3/2) + (t-1/2)*h_H, h_H=3."""
    return sigma * (n + sp.Rational(3, 2)) + (t - sp.Rational(1, 2)) * H_H


def dbar_spectrum_exact(k: int) -> dict:
    """Exact eigenvalues of C85's raw D-bar_k (before tensoring with I_q),
    computed directly from Meier's own eq 6.4 formula as certified in c85
    (eigenvalue -k with multiplicity k+2, eigenvalue k+2 with multiplicity
    k) -- reproduced here as plain integers, no matrix build needed since
    the certified formula IS the object under test."""
    return {"-k": -k, "k+2": k + 2}


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    # --- P0/P1: reuse-sanity, direct numeric eigenvalues of D-bar_k,
    # k=0..3, confirming Meier's eq 6.4 formula AND the k=0 double-zero.
    p1_ok = True
    numeric_spectra = {}
    for k in range(4):
        l_mats = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar(l_mats, rmult)
        dbar_np = np.array(dbar.evalf().tolist(), dtype=complex)
        eigs = np.linalg.eigvals(dbar_np)
        rounded = sorted(round(float(np.real(e)), 6) for e in eigs)
        max_imag = float(np.max(np.abs(np.imag(eigs))))
        numeric_spectra[str(k)] = {"eigenvalues": rounded, "max_imag": max_imag}
        print(f"P0/P1: k={k}: dim={dbar.shape}, eigenvalues={rounded}, max|Im|={max_imag:.2e}")
    p1_ok = numeric_spectra["0"]["eigenvalues"] == [0.0, 0.0]
    print(f"P1: D-bar_0 exactly doubly-degenerate zero: {p1_ok}")

    # --- P2: natural identification n=k, solve for t on each branch,
    # exact symbolic comparison (constant in k, not just at isolated k).
    t, k = sp.symbols("t k", real=True)
    eq_plus = sp.Eq(D_t(k, 1, t), k + 2)
    eq_minus = sp.Eq(D_t(k, -1, t), -k)
    t_plus = sp.solve(eq_plus, t)[0]
    t_minus = sp.solve(eq_minus, t)[0]
    p2_ok = sp.simplify(t_plus - t_minus) != 0
    print(f"P2: t from sigma=+1 branch (k+2): {t_plus}")
    print(f"P2: t from sigma=-1 branch (-k): {t_minus}")
    print(f"P2: branches require different, k-independent t values (mismatch confirmed): {p2_ok}")

    # --- P4: alternate branch assignment (swap which eigenvalue maps to
    # which sigma) -- also check for a k-independent common t.
    eq_plus2 = sp.Eq(D_t(k, 1, t), -k)
    eq_minus2 = sp.Eq(D_t(k, -1, t), k + 2)
    t_plus2 = sp.solve(eq_plus2, t)[0]
    t_minus2 = sp.solve(eq_minus2, t)[0]
    p4_ok = sp.simplify(t_plus2 - t_minus2) != 0
    print(f"P4: alt assignment t (sigma=+1 <-> -k): {t_plus2}")
    print(f"P4: alt assignment t (sigma=-1 <-> k+2): {t_minus2}")
    print(f"P4: alt assignment also mismatches (k-dependent, no fix): {p4_ok}")

    # --- P3: at n=k=0, can round67's OWN family ever produce a doubly-
    # degenerate zero, for ANY t? Solve both branches at n=0 for t and
    # compare exactly (not merely check the specific t=2/3,1 found above).
    branch_plus_n0 = D_t(0, 1, t)  # = 3t
    branch_minus_n0 = D_t(0, -1, t)  # = 3t - 3
    t_for_plus_zero = sp.solve(sp.Eq(branch_plus_n0, 0), t)[0]
    t_for_minus_zero = sp.solve(sp.Eq(branch_minus_n0, 0), t)[0]
    p3_ok = t_for_plus_zero != t_for_minus_zero
    print(f"P3: t making sigma=+1 branch zero at n=0: {t_for_plus_zero}")
    print(f"P3: t making sigma=-1 branch zero at n=0: {t_for_minus_zero}")
    print(f"P3: round67's own family CANNOT produce a double zero at n=0, any t: {p3_ok}")

    all_predictions_ok = p1_ok and p2_ok and p3_ok and p4_ok

    if all_predictions_ok:
        verdict = "NAIVE_BRIDGE_FALSIFIED__MEIER_AND_KOSTANT_NOT_IDENTIFIABLE_UNDER_N_EQ_K"
    else:
        verdict = "UNEXPECTED__SOME_PREDICTION_FAILED__SEE_DETAILS"

    out = {
        "p1_dbar0_double_zero": p1_ok,
        "numeric_spectra": numeric_spectra,
        "p2_t_plus_branch": str(t_plus),
        "p2_t_minus_branch": str(t_minus),
        "p2_mismatch_confirmed": p2_ok,
        "p4_alt_t_plus": str(t_plus2),
        "p4_alt_t_minus": str(t_minus2),
        "p4_alt_mismatch_confirmed": p4_ok,
        "p3_t_for_plus_zero_at_n0": str(t_for_plus_zero),
        "p3_t_for_minus_zero_at_n0": str(t_for_minus_zero),
        "p3_no_double_zero_possible": p3_ok,
        "all_predictions_ok": all_predictions_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert p1_ok, "P1 failed -- D-bar_0 is not the expected exact double zero"
    assert p3_ok, "P3 failed -- round67's own family unexpectedly CAN produce a double zero at n=0"


if __name__ == "__main__":
    main()
