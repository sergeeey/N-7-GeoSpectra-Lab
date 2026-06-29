"""
Phase 3: Geometry Fingerprint Core — Analytic Spectra
Compares clean W=0 analytic spectra of 4 compact product geometries.
Metrics: r-statistic, spectral density, Weyl dimension
Pre-registered: H0=all indistinguishable vs H1=>=2 metrics discriminate
"""
import json, sys, warnings
from pathlib import Path
from collections import Counter
import numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.analytic_spectra import product_spectrum, sphere_scalar_curvature

def torus_spectrum(radii, n_max):
    from itertools import product as iterprod
    seen = {}
    ranges = [range(-n_max, n_max + 1) for _ in range(len(radii))]
    for mode in iterprod(*ranges):
        lam = sum((2 * np.pi * mode[i] / radii[i]) ** 2 for i in range(len(radii)))
        key = round(lam, 12)
        if key not in seen: seen[key] = []
        seen[key].append(mode)
    rows = []
    for lam_rounded, modes in sorted(seen.items(), key=lambda x: x[0]):
        actual_lam = sum((2 * np.pi * modes[0][i] / radii[i]) ** 2 for i in range(len(radii)))
        rows.append((tuple(modes[0]), actual_lam, len(modes)))
    return rows

def get_spectrum(name, ell_max=8):
    if name == "T4": return torus_spectrum((1.0, 1.0, 1.0, 1.0), n_max=ell_max)
    elif name == "S3xS1": return product_spectrum(3, 1, ell_max, ell_max, 1.0, 1.0)
    elif name == "S2xS2": return product_spectrum(2, 2, ell_max, ell_max, 1.0, 1.0)
    elif name == "S3xS2": return product_spectrum(3, 2, ell_max, ell_max, 1.0, 1.0)
    raise ValueError(f"Unknown: {name}")

def compute_r_statistic(eigenvalues):
    ev = sorted(eigenvalues)
    rs = []
    for i in range(1, len(ev) - 1):
        s_minus = ev[i] - ev[i-1]
        s_plus = ev[i+1] - ev[i]
        if s_minus + s_plus > 0: rs.append(min(s_minus, s_plus) / max(s_minus, s_plus))
    return float(np.mean(rs)) if rs else 0.0

def extract_fingerprint(name, ell_max=8):
    spec = get_spectrum(name, ell_max)
    if name == "T4":
        eigenvalues = [row[1] for row in spec if row[1] > 0]
        degeneracies = [row[2] for row in spec if row[1] > 0]
    else:
        eigenvalues = [row.eigenvalue for row in spec if row.eigenvalue > 0]
        degeneracies = [row.degeneracy for row in spec if row.eigenvalue > 0]
    N = min(100, len(eigenvalues))
    eigenvalues = eigenvalues[:N]
    degeneracies = degeneracies[:N]
    hist, _ = np.histogram(eigenvalues, bins=20) if len(eigenvalues) > 1 else (np.array([0]), None)
    rs = []
    for i in range(1, len(eigenvalues) - 1):
        sm = eigenvalues[i] - eigenvalues[i-1]
        sp = eigenvalues[i+1] - eigenvalues[i]
        if max(sm, sp) > 0: rs.append(min(sm, sp) / max(sm, sp))
    curv_map = {"S3xS1": 6.0, "S2xS2": 4.0, "S3xS2": 8.0, "T4": 0.0}
    return {
        "geometry": name, "n_levels": len(eigenvalues),
        "mean_r": float(np.mean(rs)) if rs else 0.0,
        "degeneracy_counter": dict(Counter(degeneracies)),
        "spectral_density_bins": hist.tolist(),
        "mean_level_spacing": float(np.mean(np.diff(eigenvalues))) if len(eigenvalues) > 1 else 0.0,
        "scalar_curvature": curv_map.get(name, 0.0),
        "eigenvalues": [float(x) for x in eigenvalues[:20]],
    }

def classify(fingerprints):
    names = [fp["geometry"] for fp in fingerprints]
    discriminators = []
    # r-statistic spread
    mean_rs = [fp["mean_r"] for fp in fingerprints]
    if max(mean_rs) - min(mean_rs) > 0.1: discriminators.append("r_statistic")
    # degeneracy overlap
    degs = [set(fp["degeneracy_counter"].keys()) for fp in fingerprints]
    overlap = len(set.intersection(*degs)) / len(set.union(*degs)) if set.union(*degs) else 0
    if overlap < 0.8: discriminators.append("degeneracy_fingerprint")
    # spectral density correlation
    densities = [np.array(fp["spectral_density_bins"]) for fp in fingerprints]
    cors = [float(np.corrcoef(densities[i], densities[j])[0,1]) for i in range(len(densities)) for j in range(i+1, len(densities)) if np.std(densities[i]) > 0 and np.std(densities[j]) > 0]
    mean_cor = np.mean(cors) if cors else 0
    if mean_cor < 0.8: discriminators.append("spectral_density")
    classification = "GEOMETRY_DISTINCT" if len(discriminators) >= 2 else "GEOMETRY_INDISTINCT"
    confidence = "HIGH" if len(discriminators) >= 3 else "MEDIUM" if len(discriminators) == 2 else "FAIL"
    return {"classification": classification, "confidence": confidence, "discriminators": discriminators, "mean_r_values": {n: r for n, r in zip(names, mean_rs)}}

def main():
    print("="*60); print("GEOMETRY FINGERPRINT CORE (Phase 3)"); print("="*60)
    geometries = ["S3xS1", "T4", "S2xS2", "S3xS2"]
    fingerprints = [extract_fingerprint(g, ell_max=8) for g in geometries]
    for fp in fingerprints:
        print(f"{fp['geometry']}: r={fp['mean_r']:.3f}, curvature={fp['scalar_curvature']}")
    result = classify(fingerprints)
    print(f"\nClassification: {result['classification']} ({result['confidence']})")
    print(f"Discriminators: {result['discriminators']}")
    out = Path(__file__).parent.parent / "data" / "geometry_fingerprint_results.json"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w") as f: json.dump({"fingerprints": {fp["geometry"]: fp for fp in fingerprints}, "classification": result}, f, indent=2, default=str)
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
