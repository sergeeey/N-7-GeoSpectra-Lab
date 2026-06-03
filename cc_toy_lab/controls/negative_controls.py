"""Negative control Hamiltonians for S³×S¹ specificity testing (v0.1.22).

⚠️ CRITICAL GUARDRAILS:
- These are FALSIFICATION controls, NOT validation operators
- DO NOT claim "negative controls validate S³×S¹"
- DO NOT claim "negative controls prove FL generalization"
- Purpose: test whether harness can reject non-geometric baselines

Control definitions:
- Control A: random_hermitian — Generic random matrix with disorder
- Control B: scrambled_geometry — Broken S³×S¹ coupling (permuted indices)
- Control C: broken_wilson — Wilson term disabled or scrambled

Expected outcome: All controls should FAIL to reproduce Gate 4B PASS pattern.
If any control false-passes → harness lacks specificity.

References:
- reports/S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md
- reports/NEGATIVE_CONTROLS_IMPLEMENTATION_PLAN_v0.1.22.md

Date: 2026-05-22
Status: IMPLEMENTATION (no pilot execution yet)
"""

from __future__ import annotations

import numpy as np

from cc_toy_lab.spectral.dirac_s3 import s3_dimension
from cc_toy_lab.spectral.s1_discretizations import build_s1_operator
from cc_toy_lab.spectral.s3_s1_product_discretized import _hermitize


def build_random_hermitian_control(
    *,
    j_max: int,
    s1_size: int,
    disorder_strength: float,
    seed: int | None,
    radius: float = 1.0,
) -> tuple[np.ndarray, dict]:
    """Control A: Random Hermitian baseline.

    Purpose:
        Check whether a generic random Hermitian matrix with disorder-like
        structure can fake the true IPR contrast.

    Construction:
        - Dimension: N = s3_dimension(j_max) × s1_size (same as S³×S¹)
        - Diagonal: U(r) ∈ [-W, W] (uniform disorder, same as Gate 4B)
        - Off-diagonal: Gaussian random couplings with scale ~ 1.0
        - NO geometric structure (no S³ harmonics, no S¹ twist)

    Expected outcome:
        Should NOT reproduce the full Gate 4B-like robust pattern.
        Random matrix ≠ geometric localization.

    False-pass danger:
        If this reproduces Gate 4B-like PASS pattern (≥2.0× contrast,
        stable/strengthening FSS, reproducible across seeds/sizes),
        Gate 4B signal is NOT geometry-specific.

    Args:
        j_max: S³ spin truncation (determines S³ dimension)
        s1_size: S¹ lattice size
        disorder_strength: Anderson disorder strength W
        seed: Random seed for reproducibility
        radius: Manifold radius (affects dimension via s3_dimension)

    Returns:
        operator: Hermitian matrix (dimension: s3_dim × s1_size)
        meta: Metadata dict with control parameters
    """
    if seed is None:
        raise ValueError("seed required for reproducibility")

    s3_dim = s3_dimension(int(j_max))
    total_dim = s3_dim * int(s1_size)

    rng = np.random.default_rng(int(seed))

    # Diagonal: uniform disorder U(r) ∈ [-W, W] (same as Gate 4B)
    diagonal = rng.uniform(
        low=-float(disorder_strength), high=float(disorder_strength), size=total_dim
    )

    # Off-diagonal: Gaussian random couplings with scale ~ 1.0
    # Scale chosen to match typical S³×S¹ off-diagonal magnitude
    # (empirically ~ O(1) for radius=1.0)
    off_diagonal_scale = 1.0
    random_matrix = rng.normal(loc=0.0, scale=off_diagonal_scale, size=(total_dim, total_dim))

    # Construct Hermitian: H = diag(diagonal) + (random + random†)/2
    operator = np.diag(diagonal.astype(complex)) + 0.5 * (random_matrix + random_matrix.conj().T)
    operator = _hermitize(operator)

    meta = {
        "control": "random_hermitian",
        "j_max": int(j_max),
        "s1_size": int(s1_size),
        "disorder_strength": float(disorder_strength),
        "seed": int(seed),
        "radius": float(radius),
        "s3_dimension": s3_dim,
        "total_dimension": total_dim,
        "off_diagonal_scale": off_diagonal_scale,
        "construction": "diagonal disorder + Gaussian off-diagonal",
        "status": "Control A: falsification baseline",
    }

    return operator, meta


def build_scrambled_geometry_control(
    *,
    j_max: int,
    s1_size: int,
    alpha: float,
    disorder_strength: float,
    seed: int | None,
    radius: float = 1.0,
    scramble_mode: str = "permutation",
) -> tuple[np.ndarray, dict]:
    """Control B: Scrambled geometry control.

    Purpose:
        Preserve some dimension and matrix scale but scramble geometric
        coupling so S³×S¹ structure is broken.

    Construction options (scramble_mode):
        - 'permutation': S³×S¹ block indices randomly permuted
        - 'decoupled': S³ and S¹ sectors independent (no cross-coupling)

    Expected outcome:
        Should weaken, randomize, or destabilize the localization signal.
        May show contrast in isolated seeds but NOT reproduce the full
        robust pattern with family/control consistency.

    False-pass danger:
        If scrambled geometry reproduces the full Gate 4B-like robustness
        pattern (not just isolated contrast), the signal is NOT sensitive
        to geometric details.

    Args:
        j_max: S³ spin truncation
        s1_size: S¹ lattice size
        alpha: S¹ flux parameter (0.0=PBC, 0.5=APBC)
        disorder_strength: Anderson disorder strength W
        seed: Random seed for reproducibility
        radius: Manifold radius
        scramble_mode: Scrambling strategy ('permutation' or 'decoupled')

    Returns:
        operator: Hermitian matrix (dimension: s3_dim × s1_size)
        meta: Metadata dict with control parameters
    """
    if seed is None:
        raise ValueError("seed required for reproducibility")

    if scramble_mode not in ("permutation", "decoupled"):
        raise ValueError(f"unknown scramble_mode: {scramble_mode}")

    s3_dim = s3_dimension(int(j_max))
    total_dim = s3_dim * int(s1_size)

    rng = np.random.default_rng(int(seed))

    if scramble_mode == "permutation":
        # Build standard S³×S¹ operator first
        from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator

        op, _, _ = build_s3_s1_product_operator(
            j_max=int(j_max),
            s1_size=int(s1_size),
            alpha=float(alpha),
            mode="clean" if disorder_strength == 0.0 else "geometric_weight",
            disorder_strength=float(disorder_strength),
            seed=seed,
            radius=float(radius),
            s1_family="spectral_circle",  # Use simplest family
        )

        # Scramble: random permutation of basis indices
        perm = rng.permutation(total_dim)
        operator = op[perm, :][:, perm]

    elif scramble_mode == "decoupled":
        # S³ and S¹ sectors independent (no cross-coupling)
        # H_decoupled = kron(H_S3, I_S1)  (drop S¹ contribution)

        from cc_toy_lab.spectral.dirac_s3 import build_s3_dirac_operator

        d_s3, _ = build_s3_dirac_operator(j_max=int(j_max), radius=float(radius))
        h_s3 = (d_s3.real @ d_s3.real).astype(complex)

        # Apply disorder to S¹ identity sector
        eye_s1 = np.eye(int(s1_size), dtype=complex)
        if disorder_strength > 0.0:
            disorder_diag = rng.uniform(
                low=-float(disorder_strength),
                high=float(disorder_strength),
                size=int(s1_size),
            )
            eye_s1_disordered = eye_s1 + np.diag(disorder_diag.astype(complex))
        else:
            eye_s1_disordered = eye_s1

        operator = np.kron(h_s3, eye_s1_disordered)
        operator = _hermitize(operator)

    meta = {
        "control": "scrambled_geometry",
        "j_max": int(j_max),
        "s1_size": int(s1_size),
        "alpha": float(alpha),
        "disorder_strength": float(disorder_strength),
        "seed": int(seed),
        "radius": float(radius),
        "scramble_mode": scramble_mode,
        "s3_dimension": s3_dim,
        "total_dimension": total_dim,
        "construction": f"S³×S¹ with {scramble_mode} scramble",
        "status": "Control B: broken geometric coupling",
    }

    return operator, meta


def build_broken_wilson_control(
    *,
    j_max: int,
    s1_size: int,
    alpha: float,
    disorder_strength: float,
    seed: int | None,
    radius: float = 1.0,
    wilson_mode: str = "disabled",
) -> tuple[np.ndarray, dict]:
    """Control C: Broken Wilson term control.

    Purpose:
        Specifically perturb or disable the Wilson-ring correction structure
        to test whether the Wilson family result depends on meaningful
        implementation.

    Construction options (wilson_mode):
        - 'disabled': Wilson coefficient = 0 (pure ring without correction)
        - 'scrambled': Wilson term structure randomized

    Expected outcome:
        Should NOT produce consistent Gate 4B-like robustness across the
        same decision rules. Wilson-ring family in Gate 4B showed 8.49×
        contrast with strengthening FSS — broken Wilson should fail to
        reproduce this robust pattern.

    False-pass danger:
        If broken Wilson term reproduces the wilson_ring robustness pattern
        (8.49× contrast with consistent FSS/r-stat, not isolated), the
        Wilson correction is NOT load-bearing.

    Args:
        j_max: S³ spin truncation
        s1_size: S¹ lattice size
        alpha: S¹ flux parameter (0.0=PBC, 0.5=APBC)
        disorder_strength: Anderson disorder strength W
        seed: Random seed for reproducibility
        radius: Manifold radius
        wilson_mode: Wilson breaking strategy ('disabled' or 'scrambled')

    Returns:
        operator: Hermitian matrix (dimension: s3_dim × s1_size)
        meta: Metadata dict with control parameters
    """
    if seed is None:
        raise ValueError("seed required for reproducibility")

    if wilson_mode not in ("disabled", "scrambled"):
        raise ValueError(f"unknown wilson_mode: {wilson_mode}")

    from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator

    if wilson_mode == "disabled":
        # Build S³×S¹ with pure ring (no Wilson term)
        # This is achieved by using s1_family='ring' instead of 'wilson_ring'
        op, _, _ = build_s3_s1_product_operator(
            j_max=int(j_max),
            s1_size=int(s1_size),
            alpha=float(alpha),
            mode="clean" if disorder_strength == 0.0 else "geometric_weight",
            disorder_strength=float(disorder_strength),
            seed=seed,
            radius=float(radius),
            s1_family="ring",  # Pure ring, Wilson disabled
        )
        operator = op

    elif wilson_mode == "scrambled":
        # Build wilson_ring, then randomize all off-diagonal elements while
        # preserving diagonal (disorder). WHY: avoids dimension mismatch from
        # op_wilson - op_ring subtraction (they use different internal dims).
        op_wilson, _, _ = build_s3_s1_product_operator(
            j_max=int(j_max),
            s1_size=int(s1_size),
            alpha=float(alpha),
            mode="clean" if disorder_strength == 0.0 else "geometric_weight",
            disorder_strength=float(disorder_strength),
            seed=seed,
            radius=float(radius),
            s1_family="wilson_ring",
        )

        op_ring, _, _ = build_s3_s1_product_operator(
            j_max=int(j_max),
            s1_size=int(s1_size),
            alpha=float(alpha),
            mode="clean" if disorder_strength == 0.0 else "geometric_weight",
            disorder_strength=float(disorder_strength),
            seed=seed,  # SAME seed for disorder (must match wilson_ring basis)
            radius=float(radius),
            s1_family="ring",
        )

        # Wilson term (approximately) = H_wilson - H_ring
        wilson_term_approx = op_wilson - op_ring

        # Scramble: multiply by random Hermitian sign pattern element-wise.
        # WHY THIS VERSION (vs the diagonal-preserve + RMS-replace alternative
        # in commit c744892): the element-wise approach was the one validated
        # in the v0.1.24 specificity cascade — see git commits
        #   bd24c1e fix(controls): element-wise scrambling instead of matmul
        #   862ecac fix(controls): use same seed for wilson_ring and ring
        #   c1e8ff4 fix(controls): correct seed parameter in broken_wilson scrambled
        # and the verdict in:
        #   reports/WILSON_SCRAMBLED_ANALYSIS_v0.1.24.md
        #   reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md (Level 5 "Wilson details")
        # The alternative implementation must not be reintroduced without
        # updating the protocol and rerunning the specificity cascade.
        rng = np.random.default_rng(int(seed))
        s3_dim = s3_dimension(int(j_max))
        total_dim = s3_dim * int(s1_size)
        random_signs = rng.choice([-1.0, 1.0], size=(total_dim, total_dim))
        scrambled_wilson = random_signs * wilson_term_approx  # Element-wise

        operator = op_ring + scrambled_wilson
        operator = _hermitize(operator)

    s3_dim = s3_dimension(int(j_max))
    total_dim = s3_dim * int(s1_size)

    meta = {
        "control": "broken_wilson",
        "j_max": int(j_max),
        "s1_size": int(s1_size),
        "alpha": float(alpha),
        "disorder_strength": float(disorder_strength),
        "seed": int(seed),
        "radius": float(radius),
        "wilson_mode": wilson_mode,
        "s3_dimension": s3_dim,
        "total_dimension": total_dim,
        "construction": f"Wilson term {wilson_mode}",
        "status": "Control C: broken Wilson correction",
    }

    return operator, meta


def build_spectral_circle_scrambled_control(
    *,
    j_max: int,
    s1_size: int,
    alpha: float,
    disorder_strength: float,
    seed: int | None,
    radius: float = 1.0,
) -> tuple[np.ndarray, dict]:
    """Control D: spectral_circle on scrambled geometry.

    Purpose:
        Diagnose whether spectral_circle's Gate 4B behavior (IPR(W=20) decreasing
        with N, in contrast to ring/wilson_ring plateau) is a structural artifact
        of the spectral_circle operator itself, or a genuine (weaker) geometric signal.

    Construction:
        Build the standard spectral_circle S³×S¹ operator (W=0), then permute
        row+column indices (same scramble as Control B), then add Anderson disorder.
        This preserves spectral_circle matrix structure but destroys S³×S¹ geometric
        coupling order.

    Expected outcomes (from SKEPTIC_AUDIT_GATE4B_v0.1.22.md):
        ARTIFACT verdict: scrambled IPR(W=20) trajectory ≈ S³×S¹ IPR(W=20) trajectory
            (both decreasing at same rate → structural, not geometric)
        GEOMETRIC SIGNAL verdict: scrambled IPR(W=20) is ≥2× higher than S³×S¹ at
            s1_size=64 or 128 (geometry was suppressing localization, scrambling releases it)

    Decision criterion:
        Compare with Gate 4B spectral_circle values:
            s1_size=16:  IPR(W=20) ≈ 0.175
            s1_size=32:  IPR(W=20) ≈ 0.150
            s1_size=64:  IPR(W=20) ≈ 0.087
            s1_size=128: IPR(W=20) ≈ 0.070

    References:
        - reports/SKEPTIC_AUDIT_GATE4B_v0.1.22.md (FT-2: spectral_circle diagnosis)
        - reports/ESTIMAND_v0.1.22.md (Secondary Estimand)
        - reports/CLAIM_v0.1.22.md (Claim C2)

    Args:
        j_max: S³ spin truncation
        s1_size: S¹ lattice size
        alpha: S¹ flux parameter (0.0=PBC, 0.5=APBC)
        disorder_strength: Anderson disorder strength W
        seed: Random seed (MUST match Gate 4B spectral_circle seed for fair comparison)
        radius: Manifold radius

    Returns:
        operator: Hermitian matrix (same dimension as spectral_circle S³×S¹)
        meta: Metadata dict with control parameters
    """
    if seed is None:
        raise ValueError("seed required for reproducibility")

    from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator

    s3_dim = s3_dimension(int(j_max))
    total_dim = s3_dim * int(s1_size)

    # WHY separate seeds: build W=0 clean structure, scramble, then add disorder
    # using the same seed as Gate 4B. This isolates the scramble effect cleanly.
    rng_scramble = np.random.default_rng(int(seed) + 99999)

    # Step 1: Build clean spectral_circle S³×S¹ operator (W=0, no disorder)
    op_clean, _, _ = build_s3_s1_product_operator(
        j_max=int(j_max),
        s1_size=int(s1_size),
        alpha=float(alpha),
        mode="clean",
        disorder_strength=0.0,
        seed=seed,
        radius=float(radius),
        s1_family="spectral_circle",
    )

    # Step 2: Permute row+column indices (destroys S³×S¹ geometric coupling order)
    perm = rng_scramble.permutation(total_dim)
    op_scrambled = op_clean[perm, :][:, perm]

    # Step 3: Add Anderson disorder (same amplitude as Gate 4B)
    if disorder_strength > 0.0:
        rng_disorder = np.random.default_rng(int(seed))
        disorder_diag = rng_disorder.uniform(
            low=-float(disorder_strength),
            high=float(disorder_strength),
            size=total_dim,
        )
        np.fill_diagonal(op_scrambled, np.diag(op_scrambled) + disorder_diag)

    operator = _hermitize(op_scrambled)

    meta = {
        "control": "spectral_circle_scrambled",
        "j_max": int(j_max),
        "s1_size": int(s1_size),
        "alpha": float(alpha),
        "disorder_strength": float(disorder_strength),
        "seed": int(seed),
        "radius": float(radius),
        "scramble_seed_offset": 99999,
        "s3_dimension": s3_dim,
        "total_dimension": total_dim,
        "construction": "spectral_circle W=0 + row/col permutation + Anderson disorder",
        "gate4b_reference_ipr_w20": {
            "s1_16": 0.175,
            "s1_32": 0.150,
            "s1_64": 0.087,
            "s1_128": 0.070,
        },
        "status": "Control D: spectral_circle artifact diagnostic",
        "verdict_criteria": {
            "ARTIFACT": "scrambled IPR(W=20) within 30% of S3xS1 values at each size",
            "GEOMETRIC_SIGNAL": "scrambled IPR(W=20) >= 2x S3xS1 at s1_size=64 or 128",
        },
    }

    return operator, meta
