"""S³ Dirac eigenspinors — radial component in Hopf coordinates.

Reference: Camporesi & Higuchi 1996 (gr-qc/9505009) — VERIFIED_FROM_PDF.

Eq 3.25 in geodesic polar θ, converted to Hopf α = θ/2:
    φ_{nl}(α) = (cosα)^{l+1} (sinα)^l P^{(l+1/2, l+3/2)}_{n-l}(cos 2α)
    condition: n ≥ l ≥ 0

Eigenvalues (Eq 3.26, VERIFIED):
    λ = ±(n + 3/2) for S³ (N=3)

Degeneracy per branch (Eq 3.58, VERIFIED):
    D₃(n) = (n+1)(n+2)
"""

from __future__ import annotations

import numpy as np
from scipy.special import eval_jacobi


def phi_nl_hopf(n: int, l: int, alpha: np.ndarray) -> np.ndarray:
    """Radial Dirac eigenspinor on S³ in Hopf coordinates (unnormalized).

    Camporesi-Higuchi eq 3.25 with α = θ/2:
        φ_{nl}(α) = cosα^{l+1} · sinα^l · P^{(l+1/2, l+3/2)}_{n-l}(cos 2α)

    Args:
        n: principal quantum number (n ≥ l ≥ 0)
        l: angular quantum number
        alpha: Hopf angle values, array in [0, π/2]

    Returns:
        Unnormalized radial eigenfunction values.
    """
    if n < l or l < 0:
        raise ValueError(f"Require n ≥ l ≥ 0, got n={n}, l={l}")
    # Jacobi indices for S³ (N=3): a = N/2+l-1 = l+0.5, b = N/2+l = l+1.5
    a = l + 0.5
    b = l + 1.5
    poly_order = n - l
    x = np.cos(2.0 * alpha)
    jacobi_vals = eval_jacobi(poly_order, a, b, x)
    return (np.cos(alpha) ** (l + 1)) * (np.sin(alpha) ** l) * jacobi_vals


def eigenvalue_s3(n: int) -> float:
    """Positive Dirac eigenvalue on S³: λ = +(n + 3/2).

    Camporesi-Higuchi eq 3.26 (VERIFIED): λ²_{n,N} = (n + N/2)², N=3.
    """
    return float(n) + 1.5


def tom_ansatz(alpha: np.ndarray) -> np.ndarray:
    """Tom's ansatz candidate: √sin(2α) = √(2 sinα cosα).

    This function appears in Tom Lawrence's framework.
    Numerical analysis shows it equals √2 · (volume_measure)^{1/2},
    i.e. the square root of the Riemannian volume density, not an eigenfunction.
    """
    return np.sqrt(np.sin(2.0 * alpha))


def unweighted_mode(n: int, l: int, alpha: np.ndarray) -> np.ndarray:
    """Mode in unweighted L²: f_{nl} = φ_{nl}(α) / √(sinα cosα).

    This is what you compute when using unweighted L²(S³, dα dθ dφ)
    instead of weighted L²(S³, sinα cosα dα dθ dφ).
    The √(sinα cosα) factor = √(volume_measure) appears as an artifact.

    Sturm-Liouville connection: substituting u = v/√w in Lu = λwu
    gives L̃v = λv — and √w becomes the 'trivial vacuum state'.
    """
    phi = phi_nl_hopf(n, l, alpha)
    weight_sqrt = np.sqrt(np.sin(alpha) * np.cos(alpha))
    safe_weight = np.where(weight_sqrt > 1e-10, weight_sqrt, np.nan)
    return phi / safe_weight
