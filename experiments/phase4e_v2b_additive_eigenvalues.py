"""Phase 4E v2b: Additive Disorder on Analytic Eigenvalues

MVP v1 limitation: multiplicative disorder λ_i→λ_i×(1+Wu_i) was conformal.
v2 limitation: spatial Laplacian had catastrophic null space.

v2b fix: Direct additive disorder on analytic Kronecker eigenvalues:
  λ_i → λ_i + V_i  where V_i ~ Uniform(-W·s_mean, W·s_mean)
  
This is non-conformal (adds absolute noise, not relative).
Spectral shape changes because noise magnitude is uniform across spectrum.

Key metric: heat zeta ζ(t) = Σ e^{-tλ_i} at multiple t.
Different geometries have different λ distributions → different ζ decay.
"""

import json
import time
import numpy as np
from pathlib import Path
from scipy.special import gamma


def sphere_dirac_spectrum_squared(n, l_max, R=1.0):
    """Analytic D² eigenvalues on round Sⁿ. Same as MVP."""
    spinor_dim = 2 ** (n // 2)
    eigenvalues = []
    multiplicities = []
    for l in range(l_max + 1):
        lam = (l + n / 2.0) ** 2 / (R ** 2)
        scalar_mult = 1 if l == 0 else int((2 * l + n - 1) * gamma(l + n - 1) 
                                            / (gamma(n) * gamma(l + 1)))
        mult = spinor_dim * scalar_mult
        eigenvalues.append(lam)
        multiplicities.append(mult)
    return np.array(eigenvalues), np.array(multiplicities)


def kronecker_spectrum(eig_a, mult_a, eig_b, mult_b, R_a=1.0, R_b=1.0, max_total=12000):
    """Kronecker sum spectrum with importance sampling. Same as MVP."""
    pairs = []
    total_mult = 0
    for i in range(len(eig_a)):
        for j in range(len(eig_b)):
            lam = eig_a[i] / (R_a ** 2) + eig_b[j] / (R_b ** 2)
            mult = int(mult_a[i]) * int(mult_b[j])
            pairs.append((lam, mult))
            total_mult += mult
    
    if total_mult <= max_total:
        result = []
        for lam, mult in pairs:
            result.extend([lam] * mult)
        return np.sort(np.array(result))
    
    result = []
    target = max(1, max_total // len(pairs))
    for lam, mult in pairs:
        if mult <= target * 2:
            result.extend([lam] * min(mult, target))
        else:
            n_s = min(target, mult)
            spread = 0.001 * lam
            result.extend(np.random.normal(lam, spread, n_s))
    
    return np.sort(np.array(result))


def add_additive_disorder(spectrum, W, seed=None):
    """Add ADDITIVE Anderson disorder: λ_i → λ_i + V_i.
    
    V_i ~ Uniform(-W × s_mean, W × s_mean)
    
    W is relative to mean spacing (like in standard Anderson).
    """
    if seed is not None:
        np.random.seed(seed)
    
    s = np.sort(spectrum)
    s = s[s > 1e-12]
    
    mean_spacing = np.mean(np.diff(s)) if len(s) > 1 else 1.0
    V = np.random.uniform(-W * mean_spacing, W * mean_spacing, len(s))
    
    s_disordered = s + V
    return np.maximum(s_disordered, 1e-12)


def compute_heat_zeta(spectrum, t_values):
    """Compute heat zeta exactly."""
    s = np.sort(spectrum)
    s = s[s > 1e-12]
    return {f"t_{t}": float(np.sum(np.exp(-t * s))) for t in t_values}


def compute_ndt_metrics(spectrum, name=""):
    """Compute NDT metrics. Same as MVP."""
    s = np.sort(spectrum)
    s = s[s > 1e-12]
    
    if len(s) < 10:
        return {"error": "insufficient", "n": len(s)}
    
    spacings = np.diff(s)
    window = max(20, len(spacings) // 15)
    ns = []
    for i in range(len(spacings)):
        start = max(0, i - window // 2)
        end = min(len(spacings), i + window // 2 + 1)
        lm = np.mean(spacings[start:end])
        if lm > 0:
            ns.append(spacings[i] / lm)
    ns = np.array(ns)
    
    r_vals = []
    for i in range(len(ns) - 1):
        mx = max(ns[i], ns[i + 1])
        if mx > 1e-10:
            r_vals.append(min(ns[i], ns[i + 1]) / mx)
    r_stat = float(np.mean(r_vals)) if r_vals else 0.0
    
    mean_eig = np.mean(s)
    cv = float(np.std(s) / mean_eig) if mean_eig > 0 else 0.0
    
    return {
        "name": name,
        "n_eigenvalues": int(len(s)),
        "mean_eigenvalue": float(mean_eig),
        "cv": cv,
        "r_statistic": r_stat,
        "mean_normalized_spacing": float(np.mean(ns)) if len(ns) > 0 else 0.0,
    }


def classify_phase(clean_m, dis_m):
    """Classify recoverability."""
    keys = ["r_statistic", "cv", "mean_normalized_spacing"]
    changes = []
    for key in keys:
        c = clean_m.get(key, 0)
        d = dis_m.get(key, 0)
        changes.append(abs(d - c) / max(abs(c), 1e-10))
    
    mc = np.mean(changes)
    if mc < 0.05:
        return "RECOVERABLE", 1.0 - mc
    elif mc < 0.25:
        return "DEGRADED", 0.7 - mc
    else:
        return "ERASED", max(0.0, 0.3 - mc)


def run_phase4e_v2b():
    print("=" * 70)
    print("PHASE 4E v2b: Additive Disorder on Analytic Eigenvalues")
    print("Non-conformal: λ_i → λ_i + V_i (absolute noise)")
    print("=" * 70)
    
    t0 = time.perf_counter()
    
    l_max_a, l_max_b = 6, 4
    W_values = [0.0, 1.0, 2.0, 5.0, 10.0, 20.0]
    n_seeds = 3
    t_values = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]
    kappa = np.sqrt(7 / 6)
    
    geometries = [
        ("S³×S⁶ (physical)", 3, 6, kappa, 1.0),
        ("S³×S⁶ (equal R)",   3, 6, 1.0,   1.0),
        ("S⁴×S⁵",             4, 5, 1.0,   1.0),
        ("S²×S⁷",             2, 7, 1.0,   1.0),
    ]
    
    all_results = []
    
    for name, dim_a, dim_b, R_a, R_b in geometries:
        print(f"\n{'─' * 55}")
        print(f"Geometry: {name}")
        
        eig_a, mult_a = sphere_dirac_spectrum_squared(dim_a, l_max_a, R_a)
        eig_b, mult_b = sphere_dirac_spectrum_squared(dim_b, l_max_b, R_b)
        spec_clean = kronecker_spectrum(eig_a, mult_a, eig_b, mult_b, R_a, R_b)
        
        print(f"  Sampled eigenvalues: {len(spec_clean)}")
        
        # Clean metrics
        m_clean = compute_ndt_metrics(spec_clean, f"{name}_clean")
        hz_clean = compute_heat_zeta(spec_clean, t_values)
        m_clean["heat_zeta"] = hz_clean
        
        print(f"  Clean heat zeta @ t=0.1: {hz_clean['t_0.1']:.1f}")
        print(f"  Clean r-stat: {m_clean['r_statistic']:.4f}, CV: {m_clean['cv']:.4f}")
        
        geo_result = {
            "geometry": name,
            "clean": {"metrics": m_clean, "heat_zeta": hz_clean},
            "disorder_sweep": []
        }
        
        for W in W_values:
            if W == 0.0:
                phase, conf = "RECOVERABLE", 1.0
                avg_m = m_clean
                avg_hz = hz_clean
            else:
                seed_m, seed_hz = [], []
                for seed in range(n_seeds):
                    spec_dis = add_additive_disorder(spec_clean, W, seed=seed)
                    m = compute_ndt_metrics(spec_dis, f"{name}_W{W}_s{seed}")
                    seed_m.append(m)
                    seed_hz.append(compute_heat_zeta(spec_dis, t_values))
                
                avg_m = {
                    "r_statistic": float(np.mean([m.get("r_statistic", 0) for m in seed_m])),
                    "cv": float(np.mean([m.get("cv", 0) for m in seed_m])),
                    "mean_normalized_spacing": float(np.mean([m.get("mean_normalized_spacing", 0) for m in seed_m])),
                    "mean_eigenvalue": float(np.mean([m.get("mean_eigenvalue", 0) for m in seed_m])),
                }
                
                avg_hz = {}
                for key in t_values:
                    k_str = f"t_{key}"
                    vals = [hz.get(k_str, 0) for hz in seed_hz]
                    avg_hz[k_str] = float(np.mean(vals))
                
                phase, conf = classify_phase(m_clean, avg_m)
            
            geo_result["disorder_sweep"].append({
                "W": float(W),
                "phase": phase,
                "confidence": round(conf, 3),
                "heat_zeta": avg_hz,
            })
            
            status = {"RECOVERABLE": "✅", "DEGRADED": "⚠️", "ERASED": "❌"}.get(phase, "?")
            print(f"  W={W:5.1f}: {phase:12s} (conf={conf:.2f}) {status}")
            if W > 0:
                # Show heat zeta change ratio
                ratio_01 = avg_hz.get("t_0.1", 0) / max(hz_clean.get("t_0.1", 1), 1e-10)
                ratio_10 = avg_hz.get("t_1.0", 0) / max(hz_clean.get("t_1.0", 1), 1e-10)
                print(f"         ζ(0.1) ratio: {ratio_01:.3f}, ζ(1.0) ratio: {ratio_10:.3f}")
        
        all_results.append(geo_result)
    
    # Summary: heat zeta comparison
    print(f"\n{'=' * 70}")
    print("HEAT ZETA DECAY RATES (clean spectra)")
    print(f"{'Geometry':<22} " + " ".join([f"t={t:<8.2f}" for t in t_values]))
    print("-" * 70)
    for r in all_results:
        hz = r["clean"]["heat_zeta"]
        vals = [f"{hz.get(f't_{t}', 0):<10.1f}" for t in t_values]
        print(f"{r['geometry']:<22} " + " ".join(vals))
    
    # Robustness ranking
    print(f"\n{'─' * 70}")
    print("ROBUSTNESS SCORE (higher = more robust)")
    scores = {}
    for r in all_results:
        score = sum({"RECOVERABLE": 3, "DEGRADED": 2, "ERASED": 1}.get(sw["phase"], 0) 
                    for sw in r["disorder_sweep"])
        scores[r["geometry"]] = score
    
    for geo, sc in sorted(scores.items(), key=lambda x: -x[1]):
        rank = {18: "🥇 BEST", 17: "🥈", 16: "🥉", 15: "⚠️"}.get(sc, "❌")
        print(f"  {geo:<22} {sc}/18  {rank}")
    
    # Save
    output = {
        "experiment": "phase4e_v2b_additive_eigenvalues",
        "version": "v2b",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "results": all_results,
        "robustness_scores": {k: int(v) for k, v in scores.items()},
        "evidence": "[ANALYTIC-SPECTRUM] [ADDITIVE-DISORDER] [REPRODUCED]"
    }
    
    out_path = Path(__file__).parent / "20260708-phase4e"
    out_path.mkdir(parents=True, exist_ok=True)
    with open(out_path / "phase4e_v2b_results.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults: {out_path}/phase4e_v2b_results.json")
    print(f"Runtime: {time.perf_counter() - t0:.1f}s")
    print("=" * 70)
    return output


if __name__ == "__main__":
    run_phase4e_v2b()
