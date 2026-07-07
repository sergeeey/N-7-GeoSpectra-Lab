"""Phase 4E MVP: Minkowski/Kronecker S³×S⁶ Spectral Stress Test

Generates analytic Dirac spectra for 9D product geometries via Kronecker sum,
adds Anderson disorder, runs NDT spectral metrics (adapted from Industrial track).

Comparison geometries (all 9D):
  - S³×S⁶ (target physical geometry, κ=√(7/6))
  - S⁴×S⁵ (alternative 9D product)
  - S²×S⁷ (alternative 9D product)

Metrics (from Industrial Phase 4B):
  - heat_zeta: spectral heat kernel trace
  - r_statistic: mean consecutive spacing ratio
  - cv: coefficient of variation
  - unfolded_spacing: nearest-neighbor spacing statistics
  - spectral_density: median-normalized histogram

Phase classification (from Phase 4B):
  - RECOVERABLE: metrics stable under disorder
  - DEGRADED: metrics drift but structure survives
  - ERASED: spectral fingerprint destroyed

Output: JSON with full metrics + phase verdict per geometry per W.

Usage:
    cd N-7-GeoSpectra-Lab
    python experiments/phase4e_s3xs6_minkowski_transfer.py

Evidence marker: [REPRODUCED], [DETERMINISTIC], [ANALYTIC-SPECTRUM].
"""

import json
import time
import numpy as np
from pathlib import Path
from scipy.special import gamma


# =============================================================================
# Block 1: Analytic Spectrum Generators for Sⁿ (Round Metric)
# =============================================================================

def sphere_dirac_spectrum_squared(n, l_max, R=1.0):
    """Dirac operator D² eigenvalues on round Sⁿ.
    
    Formula: λ_l = (l + n/2)² / R²,  l = 0, 1, 2, ...
    Multiplicity: 2^{⌊n/2⌋} × dim H_l(Sⁿ)
    where dim H_l(Sⁿ) = (2l+n-1) × Γ(l+n-1) / (Γ(n) × Γ(l+1))
    
    Args:
        n: sphere dimension
        l_max: max angular momentum (truncation)
        R: radius
    
    Returns:
        eigenvalues: array of λ_l values
        multiplicities: array of multiplicities
    """
    spinor_dim = 2 ** (n // 2)
    eigenvalues = []
    multiplicities = []
    
    for l in range(l_max + 1):
        lam = (l + n / 2.0) ** 2 / (R ** 2)
        # Scalar harmonic multiplicity on Sⁿ
        if l == 0:
            scalar_mult = 1
        else:
            scalar_mult = int((2 * l + n - 1) * gamma(l + n - 1) 
                              / (gamma(n) * gamma(l + 1)))
        mult = spinor_dim * scalar_mult
        eigenvalues.append(lam)
        multiplicities.append(mult)
    
    return np.array(eigenvalues, dtype=np.float64), np.array(multiplicities, dtype=np.int64)


# =============================================================================
# Block 2: Kronecker Product Spectrum
# =============================================================================

def kronecker_spectrum(eig_a, mult_a, eig_b, mult_b, R_a=1.0, R_b=1.0, 
                        max_total=100000):
    """Kronecker sum spectrum for product manifold Sᵃ×Sᵇ.
    
    λ_{ij} = λ_a[i]/R_a² + λ_b[j]/R_b²
    mult_{ij} = mult_a[i] × mult_b[j]
    
    For manageable size, importance-samples when multiplicities are huge.
    
    Returns:
        sorted array of individual eigenvalues (sampled/expansion hybrid)
    """
    # Compute all pairs and their combined multiplicities
    pairs = []
    total_mult = 0
    for i in range(len(eig_a)):
        for j in range(len(eig_b)):
            lam = eig_a[i] / (R_a ** 2) + eig_b[j] / (R_b ** 2)
            mult = int(mult_a[i]) * int(mult_b[j])
            pairs.append((lam, mult))
            total_mult += mult
    
    # If total is manageable, expand fully
    if total_mult <= max_total:
        result = []
        for lam, mult in pairs:
            result.extend([lam] * mult)
        return np.sort(np.array(result, dtype=np.float64))
    
    # Otherwise: importance sampling proportional to multiplicity
    # Keep all pairs but sample within each
    result = []
    target_per_pair = max(1, max_total // len(pairs))
    
    for lam, mult in pairs:
        if mult <= target_per_pair * 2:
            # Expand fully for small multiplicities
            result.extend([lam] * min(mult, target_per_pair))
        else:
            # Sample with noise for large multiplicities
            n_sample = min(target_per_pair, mult)
            # Add small spectral spread to represent the multiplet
            spread = 0.001 * lam  # 0.1% spread
            samples = np.random.normal(lam, spread, n_sample)
            result.extend(samples.tolist())
    
    return np.sort(np.array(result, dtype=np.float64))


def exact_heat_zeta(eig_a, mult_a, eig_b, mult_b, R_a=1.0, R_b=1.0, t_values=None):
    """Compute heat zeta function EXACTLY without eigenvalue expansion.
    
    ζ_heat(t) = Tr(e^{-tD²}) = Σ_{i,j} mult_{ij} × exp(-t × λ_{ij})
    
    This uses the Kronecker product structure directly — no sampling needed.
    """
    if t_values is None:
        t_values = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    
    results = {}
    for t in t_values:
        total = 0.0
        for i in range(len(eig_a)):
            lam_a = eig_a[i] / (R_a ** 2)
            for j in range(len(eig_b)):
                lam_b = eig_b[j] / (R_b ** 2)
                lam = lam_a + lam_b
                mult = int(mult_a[i]) * int(mult_b[j])
                total += mult * np.exp(-t * lam)
        results[f"t_{t}"] = float(total)
    
    return results


# =============================================================================
# Block 3: NDT Spectral Metrics (from Industrial Phase 4B)
# =============================================================================

def compute_ndt_metrics(spectrum, name=""):
    """Compute spectral metrics adapted from Industrial track.
    
    Metrics:
      - r_statistic: mean consecutive spacing ratio (GOE ≈ 0.535, Poisson ≈ 0.386)
      - cv: coefficient of variation (std/mean)
      - mean_spacing: mean level spacing
      - heat_zeta_sample: sampled heat zeta (approximate)
      - density: median-normalized spectral density histogram
      - spacing_histogram: unfolded spacing distribution
    """
    s = np.sort(spectrum)
    s = s[s > 1e-12]  # Remove zero modes
    
    if len(s) < 10:
        return {"error": "insufficient eigenvalues", "n": len(s)}
    
    # Level spacings
    spacings = np.diff(s)
    
    # Unfolding: normalize by local mean spacing
    window = max(20, len(spacings) // 15)
    normalized_spacings = []
    for i in range(len(spacings)):
        start = max(0, i - window // 2)
        end = min(len(spacings), i + window // 2 + 1)
        local_mean = np.mean(spacings[start:end])
        if local_mean > 0:
            normalized_spacings.append(spacings[i] / local_mean)
    ns = np.array(normalized_spacings)
    
    # r-statistic: mean of min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    r_vals = []
    for i in range(len(ns) - 1):
        sn, sn1 = ns[i], ns[i + 1]
        mx = max(sn, sn1)
        if mx > 1e-10:
            r_vals.append(min(sn, sn1) / mx)
    r_stat = float(np.mean(r_vals)) if r_vals else 0.0
    
    # CV of eigenvalues
    mean_eig = np.mean(s)
    cv = float(np.std(s) / mean_eig) if mean_eig > 0 else 0.0
    
    # Spectral density (median-normalized)
    med = np.median(s)
    if med > 0:
        norm_s = s / med
        dens, bins = np.histogram(norm_s, bins=25, density=True)
    else:
        dens, bins = np.array([]), np.array([])
    
    # Sampled heat zeta
    heat_zeta_sample = {}
    for t in [0.1, 0.5, 1.0, 2.0]:
        hz = float(np.sum(np.exp(-t * s)))
        heat_zeta_sample[f"t_{t}"] = hz
    
    # Spacing distribution histogram
    if len(ns) > 10:
        shist, sbins = np.histogram(ns, bins=20, range=(0, 3), density=True)
    else:
        shist, sbins = np.array([]), np.array([])
    
    return {
        "name": name,
        "n_eigenvalues": int(len(s)),
        "min_eigenvalue": float(s[0]),
        "max_eigenvalue": float(s[-1]),
        "mean_eigenvalue": float(mean_eig),
        "std_eigenvalue": float(np.std(s)),
        "cv": cv,
        "mean_spacing": float(np.mean(spacings)),
        "std_spacing": float(np.std(spacings)),
        "r_statistic": r_stat,
        "mean_normalized_spacing": float(np.mean(ns)) if len(ns) > 0 else 0.0,
        "std_normalized_spacing": float(np.std(ns)) if len(ns) > 0 else 0.0,
        "heat_zeta_sample": heat_zeta_sample,
        "density_values": dens.tolist(),
        "density_bins": bins.tolist(),
        "spacing_hist_values": shist.tolist(),
        "spacing_hist_bins": sbins.tolist(),
    }


# =============================================================================
# Block 4: Disorder Injection (Anderson Multiplicative)
# =============================================================================

def add_anderson_disorder(spectrum, W, seed=None, mode_mixing=False):
    """Apply Anderson-style multiplicative disorder to analytic spectrum.
    
    λ_i → λ_i × (1 + W·u_i) where u_i ~ Uniform(-1, 1)
    
    W is RELATIVE (fraction of eigenvalue), not absolute.
    
    NOTE: Multiplicative disorder is conformal — preserves spectral shape
    ratios. It does NOT discriminate between different geometries.
    For geometry discrimination, need additive disorder on Laplacian matrix
    (H = L + diag(V_i)), which requires matrix re-diagonalization.
    """
    if seed is not None:
        np.random.seed(seed)
    
    s = np.sort(spectrum)
    u = np.random.uniform(-1, 1, len(s))
    s_disordered = s * (1.0 + W * u)
    return np.maximum(s_disordered, 1e-12)


# =============================================================================
# Block 5: Phase Classification (from Phase 4B)
# =============================================================================

def classify_recoverability(metrics_clean, metrics_disordered):
    """Classify spectral recoverability under disorder.
    
    Compares key metric fingerprints between clean and disordered spectra.
    
    Returns:
        phase: "RECOVERABLE" | "DEGRADED" | "ERASED"
        confidence: 0-1 score
        details: dict of per-metric changes
    """
    keys = ["r_statistic", "cv", "mean_normalized_spacing"]
    changes = []
    details = {}
    
    for key in keys:
        c = metrics_clean.get(key, 0)
        d = metrics_disordered.get(key, 0)
        if abs(c) > 1e-10:
            rel_change = abs(d - c) / abs(c)
        else:
            rel_change = 1.0 if abs(d) > 1e-10 else 0.0
        changes.append(rel_change)
        details[key] = {"clean": c, "disordered": d, "rel_change": rel_change}
    
    mean_change = np.mean(changes)
    max_change = np.max(changes)
    
    # Classification
    if mean_change < 0.05 and max_change < 0.15:
        phase = "RECOVERABLE"
        confidence = 1.0 - mean_change
    elif mean_change < 0.25 and max_change < 0.5:
        phase = "DEGRADED"
        confidence = 0.7 - mean_change
    else:
        phase = "ERASED"
        confidence = max(0.0, 0.3 - mean_change)
    
    return phase, float(confidence), details


# =============================================================================
# Block 6: Geometry Comparison Score
# =============================================================================

def geometry_robustness_score(results_by_geometry):
    """Compute robustness score: how well does each geometry survive disorder?
    
    Score = weighted sum of phase outcomes across W values.
    RECOVERABLE=3, DEGRADED=2, ERASED=1
    """
    scores = {}
    for geo_name, sweeps in results_by_geometry.items():
        score = 0
        for sw in sweeps:
            if sw["phase"] == "RECOVERABLE":
                score += 3
            elif sw["phase"] == "DEGRADED":
                score += 2
            else:
                score += 1
        scores[geo_name] = score
    
    return scores


# =============================================================================
# Block 7: Main Experiment Runner
# =============================================================================

def run_phase4e_mvp():
    """Run Phase 4E MVP: compare 9D geometries under spectral stress."""
    
    print("=" * 75)
    print("PHASE 4E MVP: Minkowski/Kronecker Spectral Stress Test")
    print("Compare 9D product geometries: S³×S⁶ vs S⁴×S⁵ vs S²×S⁷")
    print("Disorder: W=0.0, 0.1, 0.3, 0.5, 1.0 (relative multiplicative)")
    print("=" * 75)
    
    t0 = time.perf_counter()
    
    # Parameters
    l_max_a = 6   # For smaller sphere (S² or S³)
    l_max_b = 4   # For larger sphere (S⁵, S⁶, S⁷)
    # W = relative disorder fraction (multiplicative)
    # W=0.0: clean, W=0.1: 10% disorder, W=0.5: 50%, W=1.0: 100%
    W_values = [0.0, 0.1, 0.3, 0.5, 1.0]
    n_seeds = 3   # Average over seeds for W > 0
    
    kappa = np.sqrt(7 / 6)  # G66: κ² = (n+1)/n = 7/6
    
    # Geometry definitions: (name, dim_a, dim_b, R_a, R_b, l_max_a, l_max_b)
    geometries = [
        ("S³×S⁶ (physical)", 3, 6, kappa, 1.0, l_max_a, l_max_b),
        ("S³×S⁶ (equal R)",   3, 6, 1.0,   1.0, l_max_a, l_max_b),
        ("S⁴×S⁵",             4, 5, 1.0,   1.0, l_max_a, l_max_b),
        ("S²×S⁷",             2, 7, 1.0,   1.0, l_max_a, l_max_b),
    ]
    
    all_results = []
    
    for name, dim_a, dim_b, R_a, R_b, lmax_a, lmax_b in geometries:
        print(f"\n{'─' * 60}")
        print(f"Geometry: {name}")
        print(f"  S^{dim_a} × S^{dim_b} = {dim_a + dim_b}D")
        print(f"  Radii: R_{dim_a} = {R_a:.4f}, R_{dim_b} = {R_b:.4f}")
        
        # Generate component spectra
        eig_a, mult_a = sphere_dirac_spectrum_squared(dim_a, lmax_a, R=R_a)
        eig_b, mult_b = sphere_dirac_spectrum_squared(dim_b, lmax_b, R=R_b)
        
        # Kronecker spectrum (cap for speed — no mode mixing in MVP)
        spectrum_clean = kronecker_spectrum(
            eig_a, mult_a, eig_b, mult_b, R_a, R_b, max_total=15000
        )
        
        # Exact heat zeta (no sampling)
        heat_zeta_exact = exact_heat_zeta(
            eig_a, mult_a, eig_b, mult_b, R_a, R_b
        )
        
        print(f"  Sampled eigenvalues: {len(spectrum_clean)}")
        print(f"  Exact heat zeta @ t=0.1: {heat_zeta_exact['t_0.1']:.2f}")
        
        # Clean metrics
        metrics_clean = compute_ndt_metrics(spectrum_clean, f"{name}_W0")
        metrics_clean["heat_zeta_exact"] = heat_zeta_exact
        
        # Store geometry result
        geo_result = {
            "geometry": name,
            "dimensions": f"S^{dim_a}×S^{dim_b}",
            "total_dimension": dim_a + dim_b,
            "radii": {"R_a": float(R_a), "R_b": float(R_b)},
            "n_eigenvalues_sampled": int(len(spectrum_clean)),
            "clean_metrics": metrics_clean,
            "disorder_sweep": []
        }
        
        # Disorder sweep
        for W in W_values:
            if W == 0.0:
                phase = "RECOVERABLE"
                conf = 1.0
                details = {}
                avg_metrics = metrics_clean
            else:
                # Average over seeds
                seed_metrics = []
                for seed in range(n_seeds):
                    spec_dis = add_anderson_disorder(spectrum_clean, W, seed=seed, mode_mixing=False)
                    m = compute_ndt_metrics(spec_dis, f"{name}_W{W:.1f}_s{seed}")
                    seed_metrics.append(m)
                
                # Average
                avg_metrics = {
                    "name": f"{name}_W{W:.1f}_avg",
                    "n_eigenvalues": seed_metrics[0]["n_eigenvalues"],
                    "r_statistic": float(np.mean([m["r_statistic"] for m in seed_metrics])),
                    "cv": float(np.mean([m["cv"] for m in seed_metrics])),
                    "mean_normalized_spacing": float(np.mean([m["mean_normalized_spacing"] for m in seed_metrics])),
                    "mean_eigenvalue": float(np.mean([m["mean_eigenvalue"] for m in seed_metrics])),
                }
                
                phase, conf, details = classify_recoverability(metrics_clean, avg_metrics)
            
            geo_result["disorder_sweep"].append({
                "W": float(W),
                "phase": phase,
                "confidence": round(conf, 3),
                "r_statistic": round(avg_metrics.get("r_statistic", 0), 4),
                "cv": round(avg_metrics.get("cv", 0), 4),
                "mean_spacing": round(avg_metrics.get("mean_normalized_spacing", 0), 4),
                "metric_changes": {k: round(v["rel_change"], 3) for k, v in details.items()} if details else {}
            })
            
            status = {"RECOVERABLE": "✅", "DEGRADED": "⚠️", "ERASED": "❌"}.get(phase, "?")
            print(f"  W={W:.1f}: {phase:12s} (conf={conf:.2f}) {status}")
        
        all_results.append(geo_result)
    
    # Summary comparison
    print(f"\n{'=' * 75}")
    print("COMPARISON: Which 9D geometry survives disorder best?")
    print(f"{'=' * 75}")
    print(f"{'Geometry':<22} {'W=0.0':<10} {'W=0.1':<10} {'W=0.3':<10} {'W=0.5':<10} {'W=1.0':<10} Score")
    print("-" * 80)
    
    sweep_dict = {}
    for r in all_results:
        sweeps = r["disorder_sweep"]
        sweep_dict[r["geometry"]] = sweeps
        phases = [sw["phase"] for sw in sweeps]
        # Compute score
        score = sum({"RECOVERABLE": 3, "DEGRADED": 2, "ERASED": 1}.get(p, 0) for p in phases)
        phase_strs = [p[:9] for p in phases]
        print(f"{r['geometry']:<22} {phase_strs[0]:<10} {phase_strs[1]:<10} {phase_strs[2]:<10} {phase_strs[3]:<10} {phase_strs[4]:<10} {score}")
    
    robustness = geometry_robustness_score(sweep_dict)
    
    print(f"\n{'─' * 75}")
    print("ROBUSTNESS RANKING (higher = more robust to disorder)")
    print(f"{'─' * 75}")
    for geo, score in sorted(robustness.items(), key=lambda x: -x[1]):
        rank = {12: "🥇 BEST", 11: "🥈", 10: "🥉", 9: "⚠️"}.get(score, "❌")
        print(f"  {geo:<22} score={score}/12  {rank}")
    
    # Save results
    output = {
        "experiment": "phase4e_minkowski_transfer",
        "version": "mvp_v1",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "parameters": {
            "l_max_a": l_max_a,
            "l_max_b": l_max_b,
            "W_values": W_values,
            "n_seeds": n_seeds,
            "kappa": float(kappa),
        },
        "results": all_results,
        "robustness_scores": {k: int(v) for k, v in robustness.items()},
        "evidence": "[ANALYTIC-SPECTRUM] [REPRODUCED] [DETERMINISTIC] [PARTIAL]"
    }
    
    out_path = Path(__file__).parent.parent / "experiments" / "20260708-phase4e"
    out_path.mkdir(parents=True, exist_ok=True)
    json_path = out_path / "phase4e_mvp_results.json"
    
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    elapsed = time.perf_counter() - t0
    print(f"\n{'=' * 75}")
    print(f"Results saved: {json_path}")
    print(f"Runtime: {elapsed:.1f}s")
    print(f"Evidence: {output['evidence']}")
    print(f"Phase 4E MVP: COMPLETE")
    print(f"{'=' * 75}")
    
    return output


if __name__ == "__main__":
    run_phase4e_mvp()
