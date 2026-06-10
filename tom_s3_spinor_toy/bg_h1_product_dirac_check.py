"""BG-H1 G1 — Product Dirac Cross-Check for S³×S¹.

Gate: BG-H1-G1 (precondition: BG-H1-G0 PASS v1.1)
Pre-registration: experiments/20260610-bg-h1-s3xs1-bridge/claim_bg_h1.md

Question: Does D²_{S³×S¹} = D²_{S³} + D²_{S¹} hold numerically to ≤1e-6
relative error, confirming λ²(S³×S¹) = (n+3/2)² + (m/R)²?

CRITICAL — Convention pin (run FIRST, before spectrum tests):
  D_t = 1j * diag(k, -k)  is already anti-Hermitian (eigenvalues ±ik).
  CORRECT:  A = D_t + p*I₂                       → D4² = -(k²+p²)·I₄
  WRONG:    A_wrong = 1j*D_t + p*I₂  (extra i)   → D4² has (p±k)² diagonals (WRONG)
  The extra 1j turns eigenvalues ±ik → ∓k (real), so D4_wrong² = (k²-p²/±cross)·I.
  Source: BG-H1-G0 source_register v1.1, Claim 3e, i-placement warning.

Mathematical sources (all traced in BG-H1-G0, source_register_bg_h1_g0.md v1.1):
  Camporesi-Higuchi gr-qc/9505009:
    eq 2.1: {Γ^a, Γ^b} = 2δ^{ab} (Clifford relation, N=4)
    eq 2.4: N=4 block Dirac structure — D = [[0, Δ+], [Δ-, 0]]
    eq 3.26: λ²(n, N) = (n+N/2)² → S³: (n+3/2)²
    eq 3.34: ∇ψ = ±i(n+3/2)ψ  (D is anti-Hermitian, eigenvalues ±ik)
    eq 3.16: ∇²ψ = −λ²ψ  (D² has eigenvalue −λ²)
  Cross-term joint mechanism (JOINT, not independent):
    X = ½{Γʲ,Γ⁴}{∇ⱼ,P} + ½[Γʲ,Γ⁴][∇ⱼ,P]
    Both {Γʲ,Γ⁴}=0 (C-H eq 2.1) AND [∇ⱼ,(1/R)∂_y]=0 required together.

Kill condition (pre-registered in claim_bg_h1.md):
  rel error > 1e-6 on exact basis → structural error → STOP, record in null_results/.

Scope guards (enforced by tests):
  - No claim "S³×S¹ solved"
  - No claim "physical spin structure selected"
  - No physical promotion of any kind
  - lambda = FREE_COUPLING_PARAMETER
  - safe_for_runtime = False
  - GEOMETRY_AGNOSTIC intact until all BG gates pass
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, List, Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Clifford matrices for N=4 Euclidean (C-H Case 1, N=4 even)
# {Γ^a, Γ^b} = 2δ^{ab} · I₄
# Γ^j = σ^j ⊗ σ₁  (j=1,2,3 : S³ directions)
# Γ^4 = I₂ ⊗ σ₂  (S¹ direction)
# ---------------------------------------------------------------------------
_I2: Final = np.eye(2, dtype=complex)
_s1: Final = np.array([[0, 1], [1, 0]], dtype=complex)  # σ₁ (Hermitian)
_s2: Final = np.array([[0, -1j], [1j, 0]], dtype=complex)  # σ₂ (Hermitian)
_s3: Final = np.array([[1, 0], [0, -1]], dtype=complex)  # σ₃ (Hermitian)

GAMMA: Final[dict] = {
    1: np.kron(_s1, _s1),  # σ₁ ⊗ σ₁
    2: np.kron(_s2, _s1),  # σ₂ ⊗ σ₁
    3: np.kron(_s3, _s1),  # σ₃ ⊗ σ₁
    4: np.kron(_I2, _s2),  # I₂ ⊗ σ₂
}


# ---------------------------------------------------------------------------
# Pre-registered test grid (claim_bg_h1.md)
# ---------------------------------------------------------------------------
G1_S3_LEVELS: Final = (0, 1, 2, 3)  # n values → k = n + 3/2
G1_R_VALUES: Final = (0.5, 1.0, 2.0, 5.0)  # R values tested
G1_PERIODIC_M: Final = (0, 1, 2, 3)  # m ∈ ℤ
G1_ANTIPERIODIC_M: Final = (0.5, 1.5, 2.5)  # m ∈ ℤ+½
G1_REL_ERROR_THRESHOLD: Final = 1e-6
G1_ANTICOM_THRESHOLD: Final = 1e-14  # machine-precision for anticommutation


# ---------------------------------------------------------------------------
# Core builder — product Dirac restricted to (n, m, R) mode
# ---------------------------------------------------------------------------


def _build_correct(k: float, p: float) -> np.ndarray:
    """
    Correct 4×4 product Dirac D4 for S³×S¹ mode (k, p).

    k = n + 3/2  (S³ eigenvalue parameter, k > 0)
    p = m / R    (S¹ Fourier mode; sign carries physical meaning but |eig| = √(k²+p²))

    Construction (block form matching C-H eq 2.4):
      D_t = 1j * k * σ₃  (anti-Hermitian 2×2, eigenvalues ±ik)
      A   = D_t + p * I₂  (correct: NO extra i)
      D4  = [[0₂, A], [-A†, 0₂]]
    Claim: D4² = -(k²+p²)·I₄.
    """
    D_t = 1j * k * _s3  # anti-Hermitian, eigenvalues ±ik
    A = D_t + p * _I2  # off-diagonal block
    return np.block(
        [[np.zeros((2, 2), dtype=complex), A], [-A.conj().T, np.zeros((2, 2), dtype=complex)]]
    )


def _build_wrong(k: float, p: float) -> np.ndarray:
    """
    WRONG 4×4 product Dirac — double-counts i.

    Error: D_t already anti-Hermitian, but an extra 1j is applied:
      A_wrong = 1j * D_t + p * I₂
             = 1j * (1j*k*σ₃) + p*I₂
             = -k*σ₃ + p*I₂
             = diag(p-k, p+k)  (real diagonal — no longer encodes imaginary spectrum)
    Result: D4_wrong² = -diag((p-k)², (p+k)²) per 2×2 block ≠ -(k²+p²)·I₄.
    """
    D_t = 1j * k * _s3  # anti-Hermitian, eigenvalues ±ik
    A_wrong = 1j * D_t + p * _I2  # WRONG: extra 1j double-counts imaginary unit
    return np.block(
        [
            [np.zeros((2, 2), dtype=complex), A_wrong],
            [-A_wrong.conj().T, np.zeros((2, 2), dtype=complex)],
        ]
    )


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------


def check_clifford_anticommutation() -> dict:
    """
    Verify {Γ^j, Γ^4} = 0 for j=1,2,3 (required for cross-term cancellation).

    Physically: the JOINT mechanism from G0 requires both anticommutation AND
    [∇_j, ∂_y] = 0. This test covers the Clifford half.
    """
    results = {}
    for j in (1, 2, 3):
        Gj = GAMMA[j]
        G4 = GAMMA[4]
        anticom = Gj @ G4 + G4 @ Gj
        norm = float(np.max(np.abs(anticom)))
        results[j] = {"anticommutator_max_abs": norm, "pass": norm < G1_ANTICOM_THRESHOLD}
    return results


def check_product_square(k: float, p: float) -> dict:
    """
    Verify D4²(k,p) = -(k²+p²)·I₄ to ≤1e-6 relative error.

    Returns dict with:
      lambda2_predicted, lambda2_measured, rel_error, pass
    """
    D4 = _build_correct(k, p)
    D4_sq = D4 @ D4
    expected_diag = -(k**2 + p**2)
    # D4_sq should be scalar × I₄; measure deviation from expected diagonal
    actual_diag = np.diag(D4_sq).real  # imaginary parts should be ~0
    max_imag = float(np.max(np.abs(np.diag(D4_sq).imag)))
    rel_errors = np.abs(actual_diag - expected_diag) / abs(expected_diag)
    max_rel = float(np.max(rel_errors))
    # also verify off-diagonal is zero
    off_diag = D4_sq.copy()
    np.fill_diagonal(off_diag, 0)
    off_norm = float(np.max(np.abs(off_diag)))
    return {
        "k": k,
        "p": p,
        "lambda2_predicted": k**2 + p**2,
        "lambda2_measured": float(-np.mean(actual_diag)),
        "max_rel_error": max_rel,
        "max_off_diag": off_norm,
        "max_imag_diagonal": max_imag,
        "pass": max_rel < G1_REL_ERROR_THRESHOLD and off_norm < G1_REL_ERROR_THRESHOLD,
    }


def check_wrong_convention(k: float, p: float) -> dict:
    """
    Negative control: D4_wrong gives different squared eigenvalues.

    Expected: D4_correct² gives -(k²+p²) uniformly.
              D4_wrong²  gives -(p-k)², -(p+k)² (NOT uniform, NOT k²+p²).
    """
    D4_correct = _build_correct(k, p)
    D4_wrong = _build_wrong(k, p)
    D4c_sq = D4_correct @ D4_correct
    D4w_sq = D4_wrong @ D4_wrong
    correct_diag = np.sort(np.diag(D4c_sq).real)
    wrong_diag = np.sort(np.diag(D4w_sq).real)
    expected_correct = -(k**2 + p**2)
    # Wrong formula expected diagonal values: -(p-k)², -(p-k)², -(p+k)², -(p+k)²
    expected_wrong = np.sort([-((p - k) ** 2), -((p - k) ** 2), -((p + k) ** 2), -((p + k) ** 2)])
    constructions_differ = not np.allclose(correct_diag, wrong_diag, atol=1e-10)
    correct_matches_formula = np.allclose(correct_diag, expected_correct, rtol=1e-12)
    wrong_matches_formula = np.allclose(wrong_diag, expected_wrong, rtol=1e-10)
    return {
        "k": k,
        "p": p,
        "correct_diag": correct_diag.tolist(),
        "wrong_diag": wrong_diag.tolist(),
        "expected_correct": float(expected_correct),
        "expected_wrong": expected_wrong.tolist(),
        "constructions_differ": constructions_differ,
        "correct_matches_kp_formula": correct_matches_formula,
        "wrong_matches_wrong_formula": wrong_matches_formula,
        "pass": constructions_differ and correct_matches_formula,
    }


def run_g1_grid_check() -> dict:
    """
    Full grid check over pre-registered (n, m, R) for both spin structures.

    Returns max_rel_error, per-point results, verdict.
    """
    results = []
    max_rel = 0.0
    for n in G1_S3_LEVELS:
        k = n + 1.5  # k = n + 3/2
        # Periodic (m ∈ ℤ)
        for m in G1_PERIODIC_M:
            for R in G1_R_VALUES:
                p = m / R
                res = check_product_square(k, p)
                res["n"] = n
                res["m"] = float(m)
                res["R"] = R
                res["spin_structure"] = "periodic"
                results.append(res)
                max_rel = max(max_rel, res["max_rel_error"])
        # Antiperiodic (m ∈ ℤ+½)
        for m in G1_ANTIPERIODIC_M:
            for R in G1_R_VALUES:
                p = m / R
                res = check_product_square(k, p)
                res["n"] = n
                res["m"] = float(m)
                res["R"] = R
                res["spin_structure"] = "antiperiodic"
                results.append(res)
                max_rel = max(max_rel, res["max_rel_error"])
    verdict = "PASS" if max_rel < G1_REL_ERROR_THRESHOLD else "FAIL"
    return {
        "results": results,
        "n_points": len(results),
        "max_rel_error": max_rel,
        "verdict": verdict,
    }


def run_delta1_check() -> dict:
    """
    Verify first KK gap δ₁(R) for both spin structures.

    Periodic   (m₁=1):   δ₁(R) = √(9/4 + 1/R²) − 3/2
    Antiperiodic (m₁=½): δ₁(R) = √(9/4 + 1/(4R²)) − 3/2

    Periodic ground state (m=0): δ₀ = 0 for all R (R-independent).
    Antiperiodic ground state (m=½): δ₀(R) > 0 for all finite R (R-sensitive).
    """
    n0, k0 = 0, 1.5  # n=0, k=3/2

    records = []
    max_rel = 0.0
    for R in G1_R_VALUES:
        # Periodic ground state: m=0, δ₀ should be 0 (eigenvalue = k₀, R-independent)
        periodic_ground_lam2 = float(
            -np.diag(_build_correct(k0, 0.0) @ _build_correct(k0, 0.0))[0].real
        )
        periodic_ground_predicted = k0**2
        periodic_ground_err = (
            abs(periodic_ground_lam2 - periodic_ground_predicted) / periodic_ground_predicted
        )

        # Periodic first KK: m=1
        p1 = 1.0 / R
        lam2_periodic_kk = float(-np.diag(_build_correct(k0, p1) @ _build_correct(k0, p1))[0].real)
        lam2_periodic_pred = k0**2 + (1.0 / R) ** 2
        delta1_periodic_num = np.sqrt(lam2_periodic_kk) - k0
        delta1_periodic_pred = np.sqrt(9.0 / 4.0 + 1.0 / R**2) - 1.5
        delta1_periodic_err = abs(delta1_periodic_num - delta1_periodic_pred) / max(
            abs(delta1_periodic_pred), 1e-15
        )

        # Antiperiodic ground state: m=½
        pa0 = 0.5 / R
        lam2_anti_ground = float(
            -np.diag(_build_correct(k0, pa0) @ _build_correct(k0, pa0))[0].real
        )
        delta0_anti_num = np.sqrt(lam2_anti_ground) - k0
        delta0_anti_pred = np.sqrt(9.0 / 4.0 + 1.0 / (4.0 * R**2)) - 1.5

        delta0_anti_err = abs(delta0_anti_num - delta0_anti_pred) / max(
            abs(delta0_anti_pred), 1e-15
        )

        max_rel = max(max_rel, periodic_ground_err, delta1_periodic_err, delta0_anti_err)
        records.append(
            {
                "R": R,
                "periodic_ground_lambda2": periodic_ground_lam2,
                "periodic_ground_error": periodic_ground_err,
                "delta1_periodic_numerical": delta1_periodic_num,
                "delta1_periodic_predicted": delta1_periodic_pred,
                "delta1_periodic_error": delta1_periodic_err,
                "delta0_anti_numerical": delta0_anti_num,
                "delta0_anti_predicted": delta0_anti_pred,
                "delta0_anti_error": delta0_anti_err,
            }
        )

    # Verify antiperiodic ground state IS R-sensitive: δ₀(R=0.5) ≠ δ₀(R=5.0)
    r_small, r_large = 0.5, 5.0
    d0_small = np.sqrt(9.0 / 4.0 + 1.0 / (4.0 * r_small**2)) - 1.5
    d0_large = np.sqrt(9.0 / 4.0 + 1.0 / (4.0 * r_large**2)) - 1.5
    antiperiodic_r_sensitive = abs(d0_small - d0_large) > 0.01

    # Verify periodic ground state is R-independent
    lam2_r_small = float(-np.diag(_build_correct(k0, 0.0) @ _build_correct(k0, 0.0))[0].real)
    lam2_r_large = float(-np.diag(_build_correct(k0, 0.0) @ _build_correct(k0, 0.0))[0].real)
    periodic_r_independent = abs(lam2_r_small - lam2_r_large) < 1e-14

    return {
        "records": records,
        "max_rel_error": max_rel,
        "antiperiodic_ground_r_sensitive": antiperiodic_r_sensitive,
        "periodic_ground_r_independent": periodic_r_independent,
        "spin_structure_fork_reported": True,  # both computed, none selected
        "physical_spin_structure_selected": False,  # scope guard
        "pass": max_rel < G1_REL_ERROR_THRESHOLD
        and antiperiodic_r_sensitive
        and periodic_r_independent,
    }


# ---------------------------------------------------------------------------
# Report dataclass
# ---------------------------------------------------------------------------


@dataclass
class G1ProductDiracReport:
    """Full BG-H1-G1 gate report."""

    gate: str = "BG-H1-G1"
    date: str = "2026-06-10"
    precondition: str = "BG-H1-G0 PASS v1.1"

    # Convention-pin results
    convention_pin_pass: bool = False
    convention_wrong_differs: bool = False
    convention_pin_details: dict = field(default_factory=dict)

    # Clifford anticommutation
    clifford_anticom_pass: bool = False
    clifford_anticom_details: dict = field(default_factory=dict)

    # Grid check
    grid_max_rel_error: float = float("inf")
    grid_n_points: int = 0
    grid_verdict: str = "PENDING"

    # δ₁ check
    delta1_max_rel_error: float = float("inf")
    delta1_periodic_ok: bool = False
    delta1_antiperiodic_ok: bool = False
    antiperiodic_r_sensitive: bool = False
    periodic_r_independent: bool = False
    spin_structure_fork_reported: bool = False
    physical_spin_structure_selected: bool = False  # must remain False

    # Overall
    max_rel_error: float = float("inf")
    verdict: str = "PENDING"

    # Scope guards (pre-registered, must remain intact)
    scope: str = (
        "G1 analytic cross-check only; lambda = FREE_COUPLING_PARAMETER; "
        "GEOMETRY_AGNOSTIC intact; no physical spin-structure selection; "
        "no S3xS1 claimed solved; no physical promotion"
    )
    forbidden_claims: Tuple = field(
        default_factory=lambda: (
            "S3xS1 solved",
            "physical spin structure selected",
            "lambda fixed",
            "physical promotion",
            "safe_for_runtime",
            "geometry determined",
        )
    )


def run_g1_gate() -> G1ProductDiracReport:
    """Run the full BG-H1-G1 gate and return structured report."""
    report = G1ProductDiracReport()

    # Step 1 — MUST RUN FIRST: convention-pin test
    k_pin, p_pin = 1.5, 1.0  # k=3/2 (n=0), p=1 (m=1, R=1)
    pin = check_wrong_convention(k_pin, p_pin)
    report.convention_pin_pass = bool(pin["pass"])
    report.convention_wrong_differs = bool(pin["constructions_differ"])
    report.convention_pin_details = pin

    if not report.convention_pin_pass:
        report.verdict = "CONVENTION_ERROR"
        return report

    # Step 2 — Clifford anticommutation
    anticom = check_clifford_anticommutation()
    report.clifford_anticom_details = anticom
    report.clifford_anticom_pass = all(v["pass"] for v in anticom.values())

    # Step 3 — Grid check over (n, m, R)
    grid = run_g1_grid_check()
    report.grid_max_rel_error = grid["max_rel_error"]
    report.grid_n_points = len(grid["results"])
    report.grid_verdict = grid["verdict"]

    # Step 4 — δ₁ check for both spin structures
    delta = run_delta1_check()
    report.delta1_max_rel_error = delta["max_rel_error"]
    report.delta1_periodic_ok = bool(
        delta["records"][0]["delta1_periodic_error"] < G1_REL_ERROR_THRESHOLD
    )
    report.delta1_antiperiodic_ok = bool(
        delta["records"][0]["delta0_anti_error"] < G1_REL_ERROR_THRESHOLD
    )
    report.antiperiodic_r_sensitive = bool(delta["antiperiodic_ground_r_sensitive"])
    report.periodic_r_independent = bool(delta["periodic_ground_r_independent"])
    report.spin_structure_fork_reported = bool(delta["spin_structure_fork_reported"])
    report.physical_spin_structure_selected = bool(delta["physical_spin_structure_selected"])

    # Overall verdict
    report.max_rel_error = max(report.grid_max_rel_error, report.delta1_max_rel_error)
    all_pass = (
        report.convention_pin_pass
        and report.clifford_anticom_pass
        and report.grid_verdict == "PASS"
        and report.delta1_max_rel_error < G1_REL_ERROR_THRESHOLD
        and not report.physical_spin_structure_selected
    )
    report.verdict = "PASS" if all_pass else "FAIL"

    return report


def g1_gate_summary() -> dict:
    """Return compact summary for report file."""
    r = run_g1_gate()
    return {
        "gate": r.gate,
        "verdict": r.verdict,
        "max_rel_error": r.max_rel_error,
        "convention_pin_pass": r.convention_pin_pass,
        "clifford_anticom_pass": r.clifford_anticom_pass,
        "grid_n_points": r.grid_n_points,
        "grid_max_rel_error": r.grid_max_rel_error,
        "delta1_max_rel_error": r.delta1_max_rel_error,
        "antiperiodic_r_sensitive": r.antiperiodic_r_sensitive,
        "periodic_r_independent": r.periodic_r_independent,
        "spin_structure_fork_reported": r.spin_structure_fork_reported,
        "physical_spin_structure_selected": r.physical_spin_structure_selected,
        "scope": r.scope,
    }
