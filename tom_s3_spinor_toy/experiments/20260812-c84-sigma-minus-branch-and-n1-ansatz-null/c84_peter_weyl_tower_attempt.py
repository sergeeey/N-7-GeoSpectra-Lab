"""C84 -- first step into the full Peter-Weyl tower: sigma=-1 branch at n=0
(a genuine extension), plus a numerically-verified NULL for the naive n=1
representation ansatz (the harder half, honestly not resolved this round).

Context: C80 and C83 both independently named "the full Peter-Weyl tower
(still S3's n=0, +-branch alone across every round in this arc)" as the one
genuinely untested direction for the S3xS6 coupling program. This round
takes that on directly.

SCOPING, done before writing this script (not smoothed over):

1. Re-read Agricola 2002 (arXiv:math/0202094, in this repo as
   Agricola_2002_Dirac_naturally_reductive.pdf) directly. Its own eq (5),
   D^t psi = sum_i Z_i.Z_i(psi) + t.H.psi, splits into a CLIFFORD piece
   (Z_i., a level-independent 2x2 matrix) and an ORBITAL piece (Z_i(psi),
   which is IDENTICALLY ZERO for constant/n=0 spinors -- Theorem 4.2 -- and
   otherwise requires the genuine Peter-Weyl representation structure that
   round67's own script never built explicitly; it only cites the resulting
   closed-form eigenvalues +-(n+3/2), multiplicity (n+1)(n+2), from an
   external source).

2. Traced C74's and C79's own WORKING CODE (not just docstrings) for exactly
   how "D_S3 at n=0" is realized as matrices. Finding: EVERY round in this
   arc (C74 through C83) represents "D_S3 restricted to the n=0, sigma=+1
   branch" as `d_s3_scalar * I2` (a bare scalar times the 2x2 identity on
   Delta_m) -- NOT the actual H=(3c/2)*omega matrix (which has two distinct
   eigenvalues +-1 on omega, verified via `omega_squared_is_identity=True`
   in round67's own script). This is a genuine, previously-undocumented-as-
   such SIMPLIFICATION baked into this entire arc: "sigma" labels which of
   TWO SEPARATE scalar constructions is used (mirror t<->1-t, per round67's
   own docstring), not two subspaces of one physical Delta_m. This is
   internally consistent with round67's own claim "dim of constant-spinor
   space = dim(V_0)*dim(Delta_m) = 1*2 = 2 ... for ONE sign" and with C74's
   own "n=0 total dim 4" (2+2, two SEPARATE copies, not 1+1 within one copy).

3. Given (2), extending to sigma=-1 at n=0 is a genuine but CHEAP addition:
   a second, independent scalar*I2 copy with d_s3_scalar=-3/2 (the mirror
   value), tested via C81's own `run_for_triple` (parametrized exactly by
   d_s3_scalar), reusing the SAME Z_i Clifford generators for the coupling
   term T (Z_i is level/branch-INDEPENDENT in this arc's own construction,
   exactly matching Agricola's eq 5 where the Clifford piece Z_i. never
   depends on n).

4. Extending to n=1 requires an EXPLICIT matrix realizing "Z_i(psi)", the
   orbital term, which this arc has NEVER built. This script attempts the
   most natural first guess -- Delta_m (x) V_1 (V_1 = the spin-1 Peter-Weyl
   level's own 2-dim carrier, standard angular momentum matrices L_i =
   sigma_i/2) -- and DIAGONALIZES it, comparing against round67's own cited
   target (eigenvalues +-5/2, multiplicity 6 each at n=1). Two independent
   PRIOR hand-derivation attempts (a naive tensor-product guess and a full
   Peter-Weyl-block guess) gave inconsistent dimension counts (4 and 8, resp.)
   neither matching 6 -- so this script does NOT trust either by hand; it
   builds the concrete 4-dim naive ansatz and checks it numerically.

Reuses round67's clifford_generators/calibrate_h_H, C79's
get_bridge_to_sigma/self_dual_anti_self_dual_triples/SO4MOD, C81's
run_for_triple/build_t_generator, and C73's build_numeric_dirac, all
unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c84.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C81 = load_module(
    "c81_raw_kernel_excluded_retest",
    HERE.parent / "20260811-c81-raw-kernel-excluded-retest" / "c81_raw_kernel_excluded_retest.py",
)
C79 = C81.C79
ROUND67 = C79.ROUND67


# ---------------------------------------------------------------------------
# Step 0: verify round67's Z_i bracket relations exactly (don't hand-derive)
# ---------------------------------------------------------------------------


def verify_z_bracket_relations() -> dict:
    """[VERIFIED-sympy] Confirm [Z_i,Z_j] = -2*epsilon_ijk*Z_k exactly, all
    cyclic triples -- needed to correctly calibrate any spin-j generalization
    of Z_i against the known j=1/2 case (round67's own Z_i)."""
    z = ROUND67.clifford_generators()
    cyclic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    report = {}
    for i, j, k in cyclic:
        comm = sp.simplify(z[i] * z[j] - z[j] * z[i])
        target = sp.simplify(-2 * z[k])
        matches = bool(sp.simplify(comm - target) == sp.zeros(2, 2))
        report[f"[Z{i + 1},Z{j + 1}]_eq_minus2_Z{k + 1}"] = matches
    report["all_match"] = all(report.values())
    return report


# ---------------------------------------------------------------------------
# Step 1: sigma=-1 branch at n=0 -- cheap, well-scoped extension
# ---------------------------------------------------------------------------


def sigma_minus_branch_test() -> dict:
    """Reuses C81's run_for_triple unmodified, with d_s3_scalar flipped to
    the mirror value -3/2 (sigma=-1 at n=0, per round67's own docstring:
    "the '-' branch just flips the overall sign of h_H"). Tests the SAME
    two candidates (round119's so(4)_1 self-dual/anti-self-dual triples)
    already tested for sigma=+1 throughout C79-C82, for direct comparison."""
    R59 = C79.R59
    C73 = C79.C73
    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)

    h_h = ROUND67.calibrate_h_H()
    d_s3_scalar_plus = float(sp.Rational(1, 2) * h_h)
    d_s3_scalar_minus = -d_s3_scalar_plus
    assert abs(d_s3_scalar_plus - 1.5) < 1e-9, "sanity: + branch must equal the known 3/2"

    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_1)

    results = {}
    for label, triple in (("self_dual", self_dual), ("anti_self_dual", anti_self_dual)):
        results[label] = C81.run_for_triple(triple, f"{label}_sigma_minus", d_s6, d_s3_scalar_minus)

    no_genuine_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in results.values()
    )
    return {
        "d_s3_scalar_plus_branch_reference": d_s3_scalar_plus,
        "d_s3_scalar_minus_branch_tested": d_s3_scalar_minus,
        "results": results,
        "no_genuine_signal_found": no_genuine_signal,
    }


# ---------------------------------------------------------------------------
# Step 2: naive n=1 ansatz -- build, diagonalize, compare to round67's target
# ---------------------------------------------------------------------------


def naive_n1_ansatz_eigenvalues() -> dict:
    """Builds D_orbit^(1) = sum_i Z_i (x) L_i on Delta_m (x) V_1 (4-dim),
    L_i = sigma_i/2 the standard spin-1/2 angular momentum matrices (the
    most natural, cheapest first guess for "the n=1 Peter-Weyl carrier").
    Diagonalizes i*D_orbit (Hermitian, since D_orbit is anti-Hermitian --
    Z_i is anti-Hermitian by construction) and compares against round67's
    OWN cited target at n=1: eigenvalues +-5/2, multiplicity 6 each
    (12-dim total). NOT hand-derived -- computed exactly, numpy + sympy."""
    z = [np.array(zi.tolist(), dtype=complex) for zi in ROUND67.clifford_generators()]
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    L = [sx / 2, sy / 2, sz / 2]

    d_orbit = sum(np.kron(z[i], L[i]) for i in range(3))
    anti_herm_residual = float(np.max(np.abs(d_orbit + d_orbit.conj().T)))

    d_herm = 1j * d_orbit
    herm_residual = float(np.max(np.abs(d_herm - d_herm.conj().T)))
    eigvals = np.linalg.eigvalsh(d_herm)
    eigvals_rounded = sorted(float(x) for x in np.round(eigvals, 6))

    # group into (eigenvalue, multiplicity) pairs
    unique_vals: list[tuple[float, int]] = []
    for v in eigvals_rounded:
        if unique_vals and abs(unique_vals[-1][0] - v) < 1e-4:
            unique_vals[-1] = (unique_vals[-1][0], unique_vals[-1][1] + 1)
        else:
            unique_vals.append((v, 1))

    target_eigenvalue = 5.0 / 2.0
    target_multiplicity = (1 + 1) * (1 + 2)  # round67's own (n+1)(n+2) at n=1

    matches_target = (
        len(unique_vals) == 2
        and all(mult == target_multiplicity for _, mult in unique_vals)
        and {round(abs(v), 4) for v, _ in unique_vals} == {round(target_eigenvalue, 4)}
    )

    return {
        "construction": "Delta_m (x) V_1, L_i = sigma_i/2, D_orbit = sum Z_i (x) L_i",
        "dim": int(d_orbit.shape[0]),
        "d_orbit_is_anti_hermitian": anti_herm_residual < 1e-9,
        "i_times_d_orbit_is_hermitian": herm_residual < 1e-9,
        "eigenvalues_with_multiplicity": unique_vals,
        "target_eigenvalue_n1": target_eigenvalue,
        "target_multiplicity_n1": target_multiplicity,
        "target_total_dim_n1": 2 * target_multiplicity,
        "matches_round67_target": matches_target,
    }


def main() -> None:
    print("=== Step 0: verify Z_i bracket relations exactly ===")
    bracket_check = verify_z_bracket_relations()
    print(bracket_check)
    assert bracket_check["all_match"], "Z_i bracket relations do not match -- stop, do not proceed"

    print("\n=== Step 1: sigma=-1 branch at n=0, tested against C79's candidates ===")
    sigma_minus = sigma_minus_branch_test()
    for label, r in sigma_minus["results"].items():
        print(
            f"  {label}: compressed_n_crossings={r['compressed_n_crossings']}, "
            f"non-artifact full-spectrum crossings="
            f"{len(r['full_spectrum_nonartifact_crossings'])}, "
            f"global_min={r['compressed_global_min']:.6f} "
            f"at eps={r['compressed_global_min_at_eps']:.3f}"
        )
    print(f"no_genuine_signal_found: {sigma_minus['no_genuine_signal_found']}")

    print("\n=== Step 2: naive n=1 ansatz -- Delta_m (x) V_1, diagonalize ===")
    n1_ansatz = naive_n1_ansatz_eigenvalues()
    print(f"dim: {n1_ansatz['dim']}")
    print(f"eigenvalues (value, multiplicity): {n1_ansatz['eigenvalues_with_multiplicity']}")
    print(
        f"target (round67, n=1): eigenvalue=+-{n1_ansatz['target_eigenvalue_n1']}, "
        f"multiplicity={n1_ansatz['target_multiplicity_n1']} each, "
        f"total_dim={n1_ansatz['target_total_dim_n1']}"
    )
    print(f"matches_round67_target: {n1_ansatz['matches_round67_target']}")

    results = {
        "z_bracket_relations": bracket_check,
        "sigma_minus_branch": sigma_minus,
        "naive_n1_ansatz": n1_ansatz,
        "conclusion": (
            "sigma=-1 branch at n=0: reused C81's exact methodology, tested against "
            "both candidates already tested at sigma=+1 throughout C79-C82. "
            + (
                "Clean NULL (no crossing), consistent with sigma=+1's own result -- "
                "n=0's full 4-dim level (both branches) now covered for these candidates."
                if sigma_minus["no_genuine_signal_found"]
                else "CROSSING FOUND -- requires the same extra scrutiny every unexpectedly "
                "positive result in this arc has received before being trusted."
            )
            + " Naive n=1 ansatz (Delta_m (x) V_1): "
            + (
                "MATCHES round67's own target exactly -- can be used as a verified basis "
                "for a genuine n=1 coupling test in a future round."
                if n1_ansatz["matches_round67_target"]
                else "does NOT match round67's own target (mult 3,1 vs required 6,6) -- "
                "this specific construction attempt is KILLED. The correct n>=1 Peter-Weyl "
                "representation structure remains unresolved; extending the coupling test "
                "beyond n=0 requires either a full outer(x)inner Clebsch-Gordan construction "
                "(not attempted here) or consulting the explicit construction in the project's "
                "own cited external source (Sire & Xu, arXiv:2005.01448) directly, neither of "
                "which was completed this round."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
