"""AV-2 E1 — Sparse Reconstruction over Mixed Bilinear Dictionary.

Gate: AV2-E1 (from claim_av2_angular.md, precondition: G2 PASS)
Pre-registration: experiments/.../claim_e1_sparse_reconstruction.md (written BEFORE this code)

Hypothesis: the two-component radial bilinear dictionary
{phi*phi, g*g, phi*g, g*phi} + const can reconstruct sin(2*alpha) (the
target eq.49 radial layer) with residual < 5% using <= 5 terms.

This would show the AV-1c' obstruction was an artifact of projecting out
the partner component g_nl.

Pre-registered pass criteria:
  STRONG_PASS: residual < 5% using <= 5 terms (both unweighted and sin²α-weighted)
  WEAK_PASS:   residual < 5% using <= 8 terms
  MIXED:       residual 5-10% OR 5-15 terms
  FAIL:        residual > 10%

Scope guards (enforced by tests):
  - No full angular verification
  - No claim "Tom's ansatz solved"
  - No H-T1 promotion
  - lambda = FREE_COUPLING_PARAMETER
  - safe_for_runtime = False
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import numpy as np

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import g_nl_hopf
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf


# --- Pre-registered mode set (written BEFORE fitting) ---
PREREGISTERED_MODES: Final[list] = [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1)]
# (3,2) excluded: boundary exponent too high, l=0 dominates

# Pass thresholds (pre-registered)
STRONG_PASS_RESIDUAL: Final[float] = 0.05  # 5%
WEAK_PASS_RESIDUAL: Final[float] = 0.05  # 5%
MIXED_UPPER: Final[float] = 0.10  # 10%
STRONG_PASS_MAX_TERMS: Final[int] = 5
WEAK_PASS_MAX_TERMS: Final[int] = 8

# Grid
N_ALPHA: Final[int] = 8001


@dataclass
class DictionaryAtom:
    """One element of the bilinear dictionary."""

    name: str
    n1: int
    ang_l1: int
    n2: int
    ang_l2: int
    atom_type: str  # "phi_sq", "g_sq", "mixed_phi_g", "mixed_g_phi", "constant"
    values: np.ndarray = field(repr=False)
    norm: float = 0.0


@dataclass
class GreedyStepResult:
    """One step of the greedy matching pursuit."""

    step: int
    atom_name: str
    atom_type: str
    residual_unweighted: float
    residual_weighted: float  # sin²α weight
    cumulative_residual_unweighted: float
    cumulative_residual_weighted: float
    pass_fail: str  # "STRONG_PASS", "WEAK_PASS", "MIXED", "FAIL", "PENDING"


@dataclass
class E1SparseReconstructionReport:
    """Full E1 gate report."""

    gate: str = "AV2-E1"
    date: str = "2026-06-10"
    preregistered_modes: list = field(default_factory=list)
    n_atoms: int = 0
    greedy_steps: list = field(default_factory=list)
    final_residual_unweighted: float = 1.0
    final_residual_weighted: float = 1.0
    n_terms_used: int = 0
    verdict: str = "PENDING"
    selected_atoms: list = field(default_factory=list)
    item40_max_status: str = "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED"
    scope: str = (
        "E1 sparse reconstruction over mixed bilinear dictionary only; "
        "no full angular verification; no physical promotion; "
        "no H-T1 promotion; no claim Tom ansatz solved"
    )
    forbidden_claims: Tuple = field(
        default_factory=lambda: (
            "full angular verification complete",
            "Tom ansatz solved",
            "H-T1 promoted",
            "lambda fixed",
            "safe_for_runtime",
            "physical V promoted",
        )
    )


def _build_dictionary(alpha_grid: np.ndarray) -> list[DictionaryAtom]:
    """Build the pre-registered mixed bilinear dictionary.

    Atoms: phi_sq, g_sq, mixed_phi_g, mixed_g_phi for each mode pair
    in the pre-registered mode set, plus a constant.
    """
    atoms: list[DictionaryAtom] = []
    modes = PREREGISTERED_MODES

    # Pre-compute radial functions
    phis = {(n, l): phi_nl_hopf(n, l, alpha_grid) for n, l in modes}  # noqa: E741
    gs = {(n, l): g_nl_hopf(n, l, alpha_grid) for n, l in modes}  # noqa: E741

    # --- Diagonal atoms (same mode) ---
    for n, l in modes:  # noqa: E741
        # phi^2
        v = phis[(n, l)] ** 2
        atoms.append(
            DictionaryAtom(
                name=f"phi_sq({n},{l})",
                n1=n,
                ang_l1=l,
                n2=n,
                ang_l2=l,
                atom_type="phi_sq",
                values=v,
            )
        )
        # g^2
        v = gs[(n, l)] ** 2
        atoms.append(
            DictionaryAtom(
                name=f"g_sq({n},{l})",
                n1=n,
                ang_l1=l,
                n2=n,
                ang_l2=l,
                atom_type="g_sq",
                values=v,
            )
        )
        # phi * g (mixed, same mode)
        v = phis[(n, l)] * gs[(n, l)]
        atoms.append(
            DictionaryAtom(
                name=f"phi_g({n},{l})",
                n1=n,
                ang_l1=l,
                n2=n,
                ang_l2=l,
                atom_type="mixed_phi_g",
                values=v,
            )
        )

    # --- Cross atoms (distinct mode pairs) ---
    for i, (n1, l1) in enumerate(modes):
        for n2, l2 in modes[i + 1 :]:
            # phi * phi cross
            v = phis[(n1, l1)] * phis[(n2, l2)]
            atoms.append(
                DictionaryAtom(
                    name=f"phi_phi({n1},{l1}x{n2},{l2})",
                    n1=n1,
                    ang_l1=l1,
                    n2=n2,
                    ang_l2=l2,
                    atom_type="cross_phi_phi",
                    values=v,
                )
            )
            # g * g cross
            v = gs[(n1, l1)] * gs[(n2, l2)]
            atoms.append(
                DictionaryAtom(
                    name=f"g_g({n1},{l1}x{n2},{l2})",
                    n1=n1,
                    ang_l1=l1,
                    n2=n2,
                    ang_l2=l2,
                    atom_type="cross_g_g",
                    values=v,
                )
            )
            # phi1 * g2
            v = phis[(n1, l1)] * gs[(n2, l2)]
            atoms.append(
                DictionaryAtom(
                    name=f"phi_g({n1},{l1}x{n2},{l2})",
                    n1=n1,
                    ang_l1=l1,
                    n2=n2,
                    ang_l2=l2,
                    atom_type="cross_phi_g",
                    values=v,
                )
            )
            # g1 * phi2
            v = gs[(n1, l1)] * phis[(n2, l2)]
            atoms.append(
                DictionaryAtom(
                    name=f"g_phi({n1},{l1}x{n2},{l2})",
                    n1=n1,
                    ang_l1=l1,
                    n2=n2,
                    ang_l2=l2,
                    atom_type="cross_g_phi",
                    values=v,
                )
            )

    # --- Constant ---
    v = np.ones_like(alpha_grid)
    atoms.append(
        DictionaryAtom(
            name="constant",
            n1=-1,
            ang_l1=-1,
            n2=-1,
            ang_l2=-1,
            atom_type="constant",
            values=v,
        )
    )

    # Normalize each atom to unit L2 norm
    for atom in atoms:
        nrm = float(np.linalg.norm(atom.values))
        if nrm > 1e-14:
            atom.norm = nrm
            atom.values = atom.values / nrm
        else:
            atom.norm = 0.0
            atom.values = np.zeros_like(atom.values)

    # Remove zero-norm atoms
    atoms = [a for a in atoms if a.norm > 1e-14]
    return atoms


def _greedy_matching_pursuit(
    target: np.ndarray,
    atoms: list[DictionaryAtom],
    weight: np.ndarray,
    max_steps: int = 10,
) -> tuple[list[GreedyStepResult], list[str]]:
    """Greedy matching pursuit with optional weight vector.

    At each step: select atom with max |inner product| with residual.
    Then refit all selected atoms via least-squares.
    Returns per-step results and list of selected atom names.
    """
    target_norm_uw = float(np.linalg.norm(target))
    target_norm_w = float(np.sqrt(np.sum(weight * target**2)))

    residual = target.copy()
    selected_indices: list[int] = []
    step_results: list[GreedyStepResult] = []

    for step in range(1, max_steps + 1):
        # Find atom with max correlation to current residual
        correlations = np.array([abs(float(np.dot(a.values, residual))) for a in atoms])
        best_idx = int(np.argmax(correlations))

        # Add to selected set (allow repeats to be deduped)
        if best_idx not in selected_indices:
            selected_indices.append(best_idx)
        else:
            # All remaining atoms already included, or convergence
            break

        # Least-squares fit over selected atoms
        A = np.column_stack([atoms[i].values for i in selected_indices])
        coeffs, _, _, _ = np.linalg.lstsq(A, target, rcond=None)
        approx = A @ coeffs
        residual = target - approx

        # Compute residual percentages
        res_uw = float(np.linalg.norm(residual)) / (target_norm_uw + 1e-300)
        res_w = float(np.sqrt(np.sum(weight * residual**2))) / (target_norm_w + 1e-300)

        # Classify this step
        n_terms = len(selected_indices)
        if (
            res_uw < STRONG_PASS_RESIDUAL
            and res_w < STRONG_PASS_RESIDUAL
            and n_terms <= STRONG_PASS_MAX_TERMS
        ):
            pf = "STRONG_PASS"
        elif (
            res_uw < WEAK_PASS_RESIDUAL
            and res_w < WEAK_PASS_RESIDUAL
            and n_terms <= WEAK_PASS_MAX_TERMS
        ):
            pf = "WEAK_PASS"
        elif res_uw < MIXED_UPPER or res_w < MIXED_UPPER:
            pf = "MIXED"
        else:
            pf = "FAIL"

        step_results.append(
            GreedyStepResult(
                step=step,
                atom_name=atoms[best_idx].name,
                atom_type=atoms[best_idx].atom_type,
                residual_unweighted=round(res_uw, 6),
                residual_weighted=round(res_w, 6),
                cumulative_residual_unweighted=round(res_uw, 6),
                cumulative_residual_weighted=round(res_w, 6),
                pass_fail=pf,
            )
        )

        # Early stop if STRONG_PASS achieved
        if pf == "STRONG_PASS":
            break

    selected_names = [atoms[i].name for i in selected_indices]
    return step_results, selected_names


def run_e1_sparse_reconstruction() -> E1SparseReconstructionReport:
    """Run the E1 gate measurement and return structured report."""

    report = E1SparseReconstructionReport(
        preregistered_modes=list(PREREGISTERED_MODES),
    )

    alpha_grid = np.linspace(0.01, np.pi / 2 - 0.001, N_ALPHA)
    target = np.sin(2.0 * alpha_grid)

    # C-H weight: sin²(2α) dα convention — simplified to sin²(α) for radial layer
    weight_sin2 = np.sin(alpha_grid) ** 2
    # Normalize weight to sum to 1 for consistent percentage
    weight_sin2 = weight_sin2 / (np.sum(weight_sin2) + 1e-300) * len(alpha_grid)

    atoms = _build_dictionary(alpha_grid)
    report.n_atoms = len(atoms)

    # Run greedy pursuit
    steps, selected = _greedy_matching_pursuit(
        target, atoms, weight_sin2, max_steps=WEAK_PASS_MAX_TERMS + 2
    )

    report.greedy_steps = steps
    report.selected_atoms = selected

    # Extract final result
    if steps:
        last = steps[-1]
        report.final_residual_unweighted = last.cumulative_residual_unweighted
        report.final_residual_weighted = last.cumulative_residual_weighted
        report.n_terms_used = last.step
        report.verdict = last.pass_fail
    else:
        report.verdict = "FAIL"

    # Determine item40 status based on verdict
    if report.verdict == "STRONG_PASS":
        report.item40_max_status = "RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED"
    elif report.verdict == "WEAK_PASS":
        report.item40_max_status = "RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED"
    else:
        # MIXED or FAIL — no upgrade beyond G2 status
        report.item40_max_status = "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED"

    return report


def e1_sparse_reconstruction_summary() -> dict:
    """Return compact summary for reports."""
    r = run_e1_sparse_reconstruction()
    return {
        "gate": r.gate,
        "verdict": r.verdict,
        "n_atoms": r.n_atoms,
        "n_terms_used": r.n_terms_used,
        "final_residual_unweighted": r.final_residual_unweighted,
        "final_residual_weighted": r.final_residual_weighted,
        "selected_atoms": r.selected_atoms,
        "item40_status": r.item40_max_status,
        "scope": r.scope,
    }
