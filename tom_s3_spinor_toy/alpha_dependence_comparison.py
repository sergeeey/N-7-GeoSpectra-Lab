"""Key comparison: weighted vs unweighted L² α-dependence on S³.

Central result: √sin(2α) is proportional to √(volume_measure),
appearing as a Sturm-Liouville normalization artifact in unweighted L².
In the correct weighted L²(S³, sinα cosα dα), eigenfunctions are Jacobi polynomials.

Run directly to generate report + plot:
    python alpha_dependence_comparison.py
"""

from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
from pathlib import Path

from geometry_s3_hopf import (
    volume_measure,
    weighted_inner_product,
    s3_volume_numerical,
    s3_volume_analytical,
)
from reference_spinor_harmonics import (
    phi_nl_hopf,
    tom_ansatz,
    unweighted_mode,
    eigenvalue_s3,
)


def check_tom_is_sqrt_measure(alpha: np.ndarray) -> dict:
    """Verify: √sin(2α) = √2 · √(sinα cosα) = √2 · (√g)^{1/2}."""
    tom = tom_ansatz(alpha)
    sqrt_g_half = np.sqrt(volume_measure(alpha))
    diff = np.max(np.abs(tom - np.sqrt(2.0) * sqrt_g_half))
    return {
        "max_abs_diff": float(diff),
        "is_sqrt_measure": bool(diff < 1e-12),
        "formula": "sqrt(sin(2a)) == sqrt(2) * sqrt(sin(a)*cos(a))",
    }


def check_orthogonality(alpha: np.ndarray) -> dict:
    """Overlaps <Tom's ansatz | φ_{n,0}>_weighted for n=0,1,2,3."""
    tom = tom_ansatz(alpha)
    overlaps = {}
    for n in range(4):
        phi = phi_nl_hopf(n, 0, alpha)
        norm_sq = weighted_inner_product(phi, phi, alpha)
        norm = np.sqrt(abs(norm_sq))
        phi_normed = phi / norm if norm > 1e-12 else phi
        overlap = weighted_inner_product(tom, phi_normed, alpha)
        overlaps[f"n={n}"] = float(abs(overlap))
    nonzero = sum(1 for v in overlaps.values() if v > 1e-6)
    return {"overlaps": overlaps, "nonzero_count": nonzero}


def check_eigenfunction_equation(alpha: np.ndarray) -> dict:
    """Numerically check if √sin(2α) is an eigenfunction of Δ_S³.

    Laplace-Beltrami on α-functions in Hopf coords:
        Δ_α f = f'' + (cotα - tanα) f' = f'' + cos(2α)/(sinα cosα) f'

    Eigenfunction condition: Δ_α f / f = const (= eigenvalue).
    """
    da = alpha[1] - alpha[0]
    f = tom_ansatz(alpha)
    f_prime = np.gradient(f, da)
    f_double_prime = np.gradient(f_prime, da)
    coeff = np.cos(2.0 * alpha) / (np.sin(alpha) * np.cos(alpha) + 1e-30)
    delta_f = f_double_prime + coeff * f_prime
    inner = slice(5, -5)  # avoid boundary effects
    ratio = delta_f[inner] / (f[inner] + 1e-30)
    finite = np.isfinite(ratio)
    ratio_mean = float(np.mean(ratio[finite]))
    ratio_std = float(np.std(ratio[finite]))
    return {
        "mean_ratio": ratio_mean,
        "std_ratio": ratio_std,
        "is_eigenfunction": bool(ratio_std < 0.01 * abs(ratio_mean)),
        "note": "eigenfunction iff std_ratio << |mean_ratio|",
    }


def generate_plot(save_path: Path) -> None:
    """Generate comparison plot: weighted vs unweighted L²."""
    alpha = np.linspace(0.05, np.pi / 2 - 0.05, 500)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        "S³ Spinor-Harmonic α-Dependence: Weighted vs Unweighted L²\n"
        "Camporesi-Higuchi 1996 [VERIFIED_FROM_PDF] | Ben Achour 2016 [VERIFIED_FROM_PDF]",
        fontsize=11,
    )

    colors = ["#2196F3", "#4CAF50", "#FF9800", "#9C27B0"]

    # LEFT: correct weighted L²
    ax = axes[0]
    ax.set_title("Correct: Weighted L²(S³, sinα cosα dα)\n[Camporesi-Higuchi eq 3.25]")
    for n, c in zip(range(3), colors):
        phi = phi_nl_hopf(n, 0, alpha)
        norm = np.sqrt(abs(np.trapz(phi**2 * volume_measure(alpha), alpha)))
        phi_n = phi / norm if norm > 1e-12 else phi
        lam = eigenvalue_s3(n)
        ax.plot(alpha, phi_n, color=c, lw=2, label=f"φ_{{n={n}}} (λ=±{lam:.1f}), Jacobi")
    tom = tom_ansatz(alpha)
    tom_n = tom / np.sqrt(np.trapz(tom**2 * volume_measure(alpha), alpha))
    ax.plot(alpha, tom_n, "r--", lw=2.5, label="√sin(2α) — Tom's ansatz")
    ax.axhline(0, color="black", lw=0.5)
    ax.set_xlabel("α (Hopf angle)")
    ax.set_ylabel("Normalized amplitude")
    ax.legend(fontsize=9)
    ax.set_xlim(0, np.pi / 2)
    ax.grid(alpha=0.3)

    # RIGHT: unweighted L² — where √sin(2α) appears naturally
    ax = axes[1]
    ax.set_title("Unweighted L²(S³, dα)\n[√sin(2α) ∝ √(measure) lives here]")
    for n, c in zip(range(3), colors):
        f = unweighted_mode(n, 0, alpha)
        mask = np.isfinite(f)
        if mask.sum() < 10:
            continue
        norm = np.sqrt(abs(np.trapz(f[mask] ** 2, alpha[mask])))
        f_n = f / norm if norm > 1e-12 else f
        ax.plot(alpha[mask], f_n[mask], color=c, lw=2, label=f"φ_{{n={n}}}/√(sinα cosα)")
    tom_unw_norm = np.sqrt(np.trapz(tom**2, alpha))
    ax.plot(alpha, tom / tom_unw_norm, "r--", lw=2.5, label="√sin(2α) (Tom's ansatz)")
    sqrt_g = np.sqrt(volume_measure(alpha))
    sqrt_g_norm = np.sqrt(np.trapz(sqrt_g**2, alpha))
    ax.plot(alpha, sqrt_g / sqrt_g_norm, "k:", lw=1.5, label="√(sinα cosα) [=√g^{1/2}]")
    ax.axhline(0, color="black", lw=0.5)
    ax.set_xlabel("α (Hopf angle)")
    ax.legend(fontsize=9)
    ax.set_xlim(0, np.pi / 2)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    save_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Plot saved: {save_path}")


def run_report() -> None:
    """Run all checks and print report."""
    alpha = np.linspace(0.02, np.pi / 2 - 0.02, 3000)

    print("=" * 60)
    print("Tom S³ Spinor-Harmonic Sanity Tester — Phase 2 Report")
    print("=" * 60)

    r = check_tom_is_sqrt_measure(alpha)
    print(f"\n[1] √sin(2α) == √2 · √(sinα cosα)?")
    print(f"    max diff : {r['max_abs_diff']:.2e}")
    print(f"    VERIFIED : {r['is_sqrt_measure']}")
    print(f"    Formula  : {r['formula']}")

    r = check_eigenfunction_equation(alpha)
    print(f"\n[2] Is √sin(2α) eigenfunction of Δ_S³?")
    print(f"    Δf/f mean  : {r['mean_ratio']:.4f}")
    print(f"    Δf/f std   : {r['std_ratio']:.4f}")
    print(f"    Is eigen   : {r['is_eigenfunction']}  (expect False)")
    print(f"    Note       : {r['note']}")

    r = check_orthogonality(alpha)
    print(f"\n[3] Overlaps |<Tom | φ_n>|_weighted:")
    for k, v in r["overlaps"].items():
        print(f"    {k}: {v:.6f}")
    print(f"    Nonzero overlaps: {r['nonzero_count']} (eigenfunction → 0 or 1)")

    vol_num = s3_volume_numerical()
    vol_ana = s3_volume_analytical()
    print(f"\n[4] S³ volume sanity:")
    print(f"    Numerical  : {vol_num:.8f}")
    print(f"    Analytical : {vol_ana:.8f} (= 2π²)")
    print(f"    Rel error  : {abs(vol_num - vol_ana) / vol_ana:.2e}")

    print("\nGenerating plot...")
    generate_plot(Path("reports/ALPHA_COMPARISON_PHASE2.png"))
    print("Done.")


if __name__ == "__main__":
    run_report()
