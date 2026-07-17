"""E3: Does the KT-8 product-decoupling formula survive once S3's factor uses the
torsion-deformed operator D_S3(t) (E2) instead of the Levi-Civita operator D_S3^{LC}
(KT-8's original construction) -- and if so, does the full 9D operator on S3xS6
actually acquire ker != 0 at t=0 (where E2 found ker(D_S3(0)) != 0 at the n=0 level)?

Context (see claim.md for full framing):

  KT-8 (experiments/20260615-g8-chirality-obstruction/, reports/PROJECT_360_ROUND3_SYNTHESIS.md
  "KT-8" section, cross-checked against Sire & Xu arXiv:2005.01448 eq. 2.2-2.3) established, for
  the LEVI-CIVITA (torsion-free) connection on S3:

    D_full = D_S6,twisted (x) Id_{S3}  +  chi6 (x) D_S3^{LC}          (Sire-Xu product formula,
                                                                        M1=S6 even factor, M2=S3)
    D_full^2 = D_S6,twisted^2 (x) Id_{S3}  +  Id_{S6} (x) (D_S3^{LC})^2      (cross term vanishes
                                                                        because {chi6, D_S6}=0
                                                                        is a GENERAL fact about
                                                                        a chirality operator and
                                                                        its OWN factor's Dirac
                                                                        operator -- it does not
                                                                        involve D_S3 at all)

  and S3's own Levi-Civita spectrum +-(n+3/2)/rho3 never reaches 0 -> ker(D_full) = 0.

  E2 (experiments/20260717-round67-e2-s3-torsion-deformation/) then found: replacing S3's
  Levi-Civita connection with Agricola's torsion-deformed one-parameter family D_S3(t) gives
  D_S3(t) = D_S3^{LC} + (t-1/2)*h_H  (h_H=3, an EXACT scalar shift of the whole spectrum, because
  Kostant's cubic torsion element H collapses to a scalar multiple of the identity for S3
  specifically). This has exact zero eigenvalues at e.g. t=0 and t=1 (n=0 level).

  E2 explicitly flagged (claim.md "What this does NOT mean" #1, decision.md item 1) that whether
  the KT-8 decoupling formula still holds once D_S3 is torsion-deformed was NOT verified -- Sire &
  Xu's own literature source only covers Levi-Civita-on-both-factors. THIS experiment closes that
  specific gap: it builds the actual 16-dim Cl(9) representation from scratch (independent of, and
  not reusing, whatever script produced KT-8's own from-scratch numbers -- that script was never
  committed to the repo, confirmed by grep; this is a fresh, from-scratch build) and checks:

  (a) does D_full^2 = D_S6^2 (x) I + I (x) D_S3(t)^2 still hold to machine precision once D_S3 is
      replaced by the torsion-deformed matrix, for t=0, t=1 (E2's crossings), t=0.5 (Levi-Civita,
      regression check against KT-8's own already-published numbers), and one generic non-crossing
      t (0.25), and even for an arbitrary random Hermitian D_S3 (to test the STRUCTURAL claim that
      the decoupling never depended on any special property of D_S3 at all)?
  (b) what happens to min|eig(D_full)| once D_S3(0) has an exact zero eigenvalue -- does the S3
      floor (1.5, per KT-8) actually disappear, and does D_full's spectrum get driven towards
      whatever small eigenvalue the S6-side test operator has?

Construction (mirrors KT-8's own from-scratch style, per the description in
reports/PROJECT_360_ROUND3_SYNTHESIS.md "KT-8" section -- rebuilt independently since no script
survives in the repo for the original KT-8 second pass):
  - Cl(3) (S3 generators): Pauli matrices sigma_x, sigma_y, sigma_z (Cl(3,0) convention,
    Gamma_i^2 = +I, matches the convention used for the Cl(6) generators below for uniformity).
  - Cl(6) (S6 generators): Jordan-Wigner construction on 3 qubits (8-dim), 6 Hermitian gammas,
    Gamma_i^2 = +I, mutually anticommuting -- verified exactly (entries of these matrices are in
    {0,+-1,+-i}, so floating-point residuals are exactly 0.0, not just epsilon).
  - chi6 = i * Gamma6_1...Gamma6_6 (standard chirality/volume element construction for Cl(6,0):
    the raw product omega=Gamma6_1...Gamma6_6 is anti-Hermitian with omega^2=-I for this
    signature/dimension, so i*omega is Hermitian with (i*omega)^2=+I) -- verified to anticommute
    with each of the 6 generators (general fact for a top-degree Clifford element in an even
    dimension), which is the ONLY property the KT-8/Sire-Xu decoupling proof actually uses.
  - Cl(9) assembly (16-dim, S6-spinor (x) S3-spinor): Gamma_full_i = Gamma6_i (x) I2 for the 6 S6
    directions, Gamma_full_{6+j} = chi6 (x) Gamma3_j for the 3 S3 directions -- the unique
    assignment making the full 9-generator set close into a genuine Cl(9) representation
    (verified: all 45 unordered pairs, i.e. the full 9x9 grid of anticommutators).
  - D_S3(t): NOT built from the Gamma3_j generators -- substituted directly as a 2x2 Hermitian
    matrix, exactly as KT-8's own second pass did for D_S3^{LC} ("D1 = 1.5*sigma_z"). Using E2's
    own closed form: D_S3(t) = 1.5*sigma_z + (t-0.5)*3*I2 (1.5 = G8's established n=0 eigenvalue,
    3 = E2's calibrated h_H). This directly reuses E2's numbers rather than re-deriving Kostant's
    torsion element from scratch (E2 already did that derivation and it is not repeated here).
  - D_S6 (twisted, test operator): two independent constructions, both anticommuting with chi6 by
    construction (this is the only property the decoupling proof needs):
      (i) "single-generator" (matches KT-8's own style): D_S6 = sum c_i*Gamma6_i, scaled so that
          sum(c_i^2) = 0.185^2 -- this FORCES D_S6^2 = 0.185^2 * I exactly (an algebraic fact
          about any linear combination of anticommuting square-root-of-identity generators), so
          its eigenvalues are exactly +-0.185, matching KT-8's own reported near-zero test value.
      (ii) "projector" (richer, non-degenerate spectrum, not restricted to the single-generator
          special case): D_S6 = (M - chi6 M chi6^-1)/2 for a fixed (seeded, reproducible) random
          Hermitian M -- this projection ALWAYS anticommutes with chi6 for ANY Hermitian M (general
          fact, verified below), and generically has a non-degenerate spectrum (not forced to
          +-const), giving a less special stress-test of the decoupling identity.

Honesty ledger:
  - Cl(3)/Cl(6) Clifford relations, chi6 properties, Cl(9) assembly, D_full^2 decoupling residual,
    min|eig(D_full)|: [VERIFIED-tool], exact/machine-precision numeric linear algebra, this script.
  - D_S3(t) = 1.5*sigma_z + (t-0.5)*3*I2, and specifically that D_S3(0) has an exact zero
    eigenvalue: [VERIFIED-sympy, reused from E2] -- NOT re-derived here, E2 already established it.
  - That the REAL (curvature-twisted, differential) S6 operator has an established exact zero
    eigenvalue elsewhere in this project (G73/G74A, ind=1 per channel): [VERIFIED-sympy, cited,
    NOT reconstructed here] -- this script's own D_S6 test operators are flat Clifford-algebra
    stand-ins (KT-8's own methodology), not a rebuild of the actual differential twisted operator;
    the conclusion that ker(D_full) != 0 at t=0 given BOTH exact zero eigenvalues is a logical
    consequence of the verified decoupling identity plus these two externally-established facts,
    not a fresh from-scratch computation of the physical D_S6,twisted operator's kernel.
  - Whether the product-decoupling formula generalizes to an arbitrary D_S3 (not just the specific
    torsion family): [VERIFIED-tool] this script explicitly tests this with a random Hermitian
    D_S3 unrelated to the torsion family, confirming the structural claim in the prompt/claim.md.
"""

from __future__ import annotations

import json

import numpy as np

# ---------------------------------------------------------------------------
# Step 1: Cl(3) -- S3 generators (Pauli matrices, Cl(3,0) convention: Gamma_i^2 = +I)
# ---------------------------------------------------------------------------


def s3_generators() -> list[np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return [sx, sy, sz]


# ---------------------------------------------------------------------------
# Step 2: Cl(6) -- S6 generators via Jordan-Wigner on 3 qubits (8-dim rep)
# ---------------------------------------------------------------------------


def _kron_list(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def s6_generators() -> list[np.ndarray]:
    """Standard Jordan-Wigner construction: 3 fermionic modes -> 6 Hermitian gammas
    on an 8-dim rep. Gamma_{2i-1} = Z^(x)(i-1) (x) X (x) I^(x)(2-i)
    Gamma_{2i}   = Z^(x)(i-1) (x) Y (x) I^(x)(2-i),  i=1,2,3.
    """
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    gens = []
    for i in range(3):
        left = [sz] * i
        right = [I2] * (2 - i)
        gens.append(_kron_list(left + [sx] + right))
        gens.append(_kron_list(left + [sy] + right))
    return gens  # 6 matrices, 8x8


# ---------------------------------------------------------------------------
# Generic Clifford-relation / Hermiticity checkers
# ---------------------------------------------------------------------------


def check_clifford_relations(gens: list[np.ndarray], tol: float = 1e-10) -> dict:
    n = len(gens)
    dim = gens[0].shape[0]
    id_dim = np.eye(dim, dtype=complex)
    report = {}
    ok = True
    max_resid = 0.0
    for a in range(n):
        for b in range(a, n):
            anticomm = gens[a] @ gens[b] + gens[b] @ gens[a]
            expected = 2 * id_dim if a == b else np.zeros((dim, dim), dtype=complex)
            resid = float(np.max(np.abs(anticomm - expected)))
            report[f"{a}_{b}"] = resid
            max_resid = max(max_resid, resid)
            if resid > tol:
                ok = False
    return {"pairwise_residuals": report, "all_ok": ok, "max_residual": max_resid}


def is_hermitian(m: np.ndarray, tol: float = 1e-10) -> bool:
    return bool(np.max(np.abs(m - m.conj().T)) < tol)


# ---------------------------------------------------------------------------
# Step 3: chirality operator chi6
# ---------------------------------------------------------------------------


def build_chi6(gens6: list[np.ndarray]) -> tuple[np.ndarray, dict]:
    omega = gens6[0]
    for g in gens6[1:]:
        omega = omega @ g
    dim = omega.shape[0]
    id_dim = np.eye(dim, dtype=complex)

    omega_anti_hermitian = bool(np.max(np.abs(omega + omega.conj().T)) < 1e-10)
    omega_sq = omega @ omega
    omega_sq_is_minus_I = bool(np.max(np.abs(omega_sq + id_dim)) < 1e-10)

    chi6 = 1j * omega
    chi_hermitian = is_hermitian(chi6)
    chi_sq = chi6 @ chi6
    chi_sq_is_I = bool(np.max(np.abs(chi_sq - id_dim)) < 1e-10)

    anticommutes_with_each = []
    max_ac_resid = 0.0
    for g in gens6:
        ac = chi6 @ g + g @ chi6
        resid = float(np.max(np.abs(ac)))
        max_ac_resid = max(max_ac_resid, resid)
        anticommutes_with_each.append(resid < 1e-10)

    report = {
        "omega_anti_hermitian": omega_anti_hermitian,
        "omega_squared_is_minus_I": omega_sq_is_minus_I,
        "chi6_hermitian": chi_hermitian,
        "chi6_squared_is_I": chi_sq_is_I,
        "chi6_anticommutes_with_all_6_generators": all(anticommutes_with_each),
        "max_anticommutator_residual_vs_generators": max_ac_resid,
        "all_ok": (
            omega_anti_hermitian
            and omega_sq_is_minus_I
            and chi_hermitian
            and chi_sq_is_I
            and all(anticommutes_with_each)
        ),
    }
    return chi6, report


# ---------------------------------------------------------------------------
# Step 4: assemble the 16-dim Cl(9) representation, check ALL Clifford relations
# ---------------------------------------------------------------------------


def assemble_cl9(
    gens3: list[np.ndarray], gens6: list[np.ndarray], chi6: np.ndarray
) -> list[np.ndarray]:
    I2 = np.eye(2, dtype=complex)
    full = [np.kron(g, I2) for g in gens6]  # 6 S6-direction generators
    full += [np.kron(chi6, g) for g in gens3]  # 3 S3-direction generators
    return full  # 9 matrices, 16x16


# ---------------------------------------------------------------------------
# Step 5: D_S3(t) (torsion-deformed, reusing E2's calibrated closed form)
#          and two D_S6 test operators (single-generator, projector)
# ---------------------------------------------------------------------------


def d_s3_matrix(t: float, h_H: float = 3.0, d_lc_n0: float = 1.5) -> np.ndarray:
    """D_S3(t) = d_lc_n0*sigma_z + (t - 1/2)*h_H*I2  -- E2's closed form at the n=0
    level, d_lc_n0=1.5 (G8's established n=0 eigenvalue), h_H=3 (E2's calibration).
    """
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    return d_lc_n0 * sz + (t - 0.5) * h_H * I2


def d_s6_single_generator(gens6: list[np.ndarray], target_abs_eig: float = 0.185) -> np.ndarray:
    """D_S6 = sum c_i*Gamma6_i, scaled so sum(c_i^2) = target_abs_eig^2. Any such
    combination satisfies D_S6^2 = sum(c_i^2)*I exactly (Clifford relations), so its
    eigenvalues are exactly +-target_abs_eig -- matches KT-8's own reported test value.
    Fixed (not literally random) direction vector for reproducibility.
    """
    v = np.array([1.0, 2.0, -1.0, 3.0, -2.0, 1.0])
    v = v / np.linalg.norm(v) * target_abs_eig
    d = np.zeros((8, 8), dtype=complex)
    for c, g in zip(v, gens6):
        d = d + c * g
    return d


def d_s6_projector(chi6: np.ndarray, seed: int = 20260717) -> np.ndarray:
    """D_S6 = (M - chi6 @ M @ chi6) / 2 for a fixed-seed random Hermitian M. This
    ALWAYS anticommutes with chi6 for any Hermitian M (chi6^2=I so chi6@chi6=I):
      chi6 @ D @ chi6 = (chi6 M chi6 - M) / 2 = -D   =>   {chi6, D} = 0.
    Generically gives a non-degenerate spectrum (not forced to +-const), a richer,
    less special stress-test than the single-generator construction above.
    """
    rng = np.random.default_rng(seed)
    dim = chi6.shape[0]
    A = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    M = (A + A.conj().T) / 2  # Hermitian
    D = (M - chi6 @ M @ chi6) / 2
    return D


# ---------------------------------------------------------------------------
# Step 6: D_full, decoupling residual, spectrum
# ---------------------------------------------------------------------------


def build_d_full(chi6: np.ndarray, d_s6: np.ndarray, d_s3: np.ndarray) -> np.ndarray:
    """D_full = D_S6 (x) I2 + chi6 (x) D_S3   (Sire-Xu formula, M1=S6, M2=S3)."""
    I2 = np.eye(2, dtype=complex)
    return np.kron(d_s6, I2) + np.kron(chi6, d_s3)


def decoupling_residual(d_full: np.ndarray, d_s6: np.ndarray, d_s3: np.ndarray) -> float:
    I2 = np.eye(2, dtype=complex)
    I8 = np.eye(8, dtype=complex)
    lhs = d_full @ d_full
    rhs = np.kron(d_s6 @ d_s6, I2) + np.kron(I8, d_s3 @ d_s3)
    return float(np.max(np.abs(lhs - rhs)))


def spectrum_report(d_full: np.ndarray) -> dict:
    w = np.linalg.eigvalsh(d_full)
    return {
        "min_abs_eig": float(np.min(np.abs(w))),
        "max_abs_eig": float(np.max(np.abs(w))),
        "full_spectrum_sorted": sorted(float(x) for x in w),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    result: dict = {}

    # --- Step 1-2: Clifford relations for Cl(3), Cl(6) ---
    gens3 = s3_generators()
    gens6 = s6_generators()
    cl3_check = check_clifford_relations(gens3)
    cl6_check = check_clifford_relations(gens6)
    result["step1_cl3_clifford"] = cl3_check
    result["step2_cl6_clifford"] = cl6_check

    # --- Step 3: chirality operator ---
    chi6, chi6_report = build_chi6(gens6)
    result["step3_chi6"] = chi6_report

    # --- Step 4: assemble Cl(9), check all 45 pairwise relations ---
    full9 = assemble_cl9(gens3, gens6, chi6)
    cl9_check = check_clifford_relations(full9)
    result["step4_cl9_assembly_clifford"] = cl9_check

    construction_ok = (
        cl3_check["all_ok"]
        and cl6_check["all_ok"]
        and chi6_report["all_ok"]
        and cl9_check["all_ok"]
    )
    result["construction_verified"] = construction_ok

    # --- Step 5-6: D_full decoupling + spectrum, for a range of t and two D_S6 stand-ins ---
    d_s6_variants = {
        "single_generator_0.185": d_s6_single_generator(gens6, target_abs_eig=0.185),
        "projector_seed20260717": d_s6_projector(chi6, seed=20260717),
    }
    # sanity: report D_S6's own spectrum for each variant (flat Clifford-algebra stand-in,
    # NOT the real curvature-twisted operator -- see module docstring honesty ledger)
    d_s6_spectra = {
        name: sorted(float(x) for x in np.linalg.eigvalsh(d)) for name, d in d_s6_variants.items()
    }
    result["d_s6_test_operator_spectra"] = d_s6_spectra

    t_values = {
        "t=0.5_LevCivita_regression_check": 0.5,
        "t=0_E2_crossing_n0": 0.0,
        "t=1_E2_crossing_n0": 1.0,
        "t=0.25_generic_noncrossing": 0.25,
    }

    per_t_results = {}
    for t_label, t in t_values.items():
        d_s3 = d_s3_matrix(t)
        d_s3_eigs = sorted(float(x) for x in np.linalg.eigvalsh(d_s3))
        row = {"t": t, "d_s3_eigenvalues": d_s3_eigs}
        for d_s6_name, d_s6 in d_s6_variants.items():
            d_full = build_d_full(chi6, d_s6, d_s3)
            residual = decoupling_residual(d_full, d_s6, d_s3)
            spec = spectrum_report(d_full)
            d_s6_min_abs = min(abs(x) for x in d_s6_spectra[d_s6_name])
            d_s3_min_abs = min(abs(x) for x in d_s3_eigs)
            predicted_min = float(np.sqrt(d_s3_min_abs**2 + d_s6_min_abs**2))
            row[d_s6_name] = {
                "decoupling_residual": residual,
                "min_abs_eig_d_full": spec["min_abs_eig"],
                "max_abs_eig_d_full": spec["max_abs_eig"],
                "predicted_min_from_decoupling_formula": predicted_min,
                "prediction_matches_actual": bool(abs(predicted_min - spec["min_abs_eig"]) < 1e-9),
            }
        per_t_results[t_label] = row
    result["per_t_results"] = per_t_results

    # --- Structural generality check: decoupling for an ARBITRARY (non-torsion-family) D_S3 ---
    rng = np.random.default_rng(999)
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    d_s3_random = (A + A.conj().T) / 2
    random_check = {}
    for d_s6_name, d_s6 in d_s6_variants.items():
        d_full = build_d_full(chi6, d_s6, d_s3_random)
        residual = decoupling_residual(d_full, d_s6, d_s3_random)
        random_check[d_s6_name] = {"decoupling_residual": residual}
    result["arbitrary_d_s3_structural_check"] = {
        "d_s3_random_matrix_real": np.real(d_s3_random).tolist(),
        "d_s3_random_matrix_imag": np.imag(d_s3_random).tolist(),
        "per_d_s6_variant": random_check,
        "all_residuals_negligible": all(
            v["decoupling_residual"] < 1e-9 for v in random_check.values()
        ),
    }

    # --- Regression check against KT-8's own published numbers (t=0.5, single-generator D_S6) ---
    kt8_baseline = per_t_results["t=0.5_LevCivita_regression_check"]["single_generator_0.185"]
    kt8_expected_min = 1.5113689
    result["kt8_regression_check"] = {
        "reproduced_min_abs_eig": kt8_baseline["min_abs_eig_d_full"],
        "kt8_published_value": kt8_expected_min,
        "abs_diff": abs(kt8_baseline["min_abs_eig_d_full"] - kt8_expected_min),
        "matches_kt8_within_1e-4": abs(kt8_baseline["min_abs_eig_d_full"] - kt8_expected_min)
        < 1e-4,
    }

    # --- Verdict ---
    all_decoupling_residuals = []
    for row in per_t_results.values():
        for name in d_s6_variants:
            all_decoupling_residuals.append(row[name]["decoupling_residual"])
    for v in random_check.values():
        all_decoupling_residuals.append(v["decoupling_residual"])
    decoupling_survives = all(r < 1e-9 for r in all_decoupling_residuals)

    floor_removed_single_gen = (
        per_t_results["t=0_E2_crossing_n0"]["single_generator_0.185"]["min_abs_eig_d_full"]
        < per_t_results["t=0.5_LevCivita_regression_check"]["single_generator_0.185"][
            "min_abs_eig_d_full"
        ]
        - 1e-6
    )
    floor_value_at_t0 = per_t_results["t=0_E2_crossing_n0"]["single_generator_0.185"][
        "min_abs_eig_d_full"
    ]

    result["verdict"] = {
        "construction_verified": construction_ok,
        "decoupling_survives_torsion_deformation": decoupling_survives,
        "kt8_regression_matches": result["kt8_regression_check"]["matches_kt8_within_1e-4"],
        "s3_floor_removed_at_t0": floor_removed_single_gen,
        "min_abs_eig_d_full_at_t0_single_gen_test": floor_value_at_t0,
        "logical_conclusion_ker_d_full_nonzero_at_t0": (
            "IF the decoupling formula holds (verified above) AND D_S3(0) has an exact zero "
            "eigenvalue (E2, [VERIFIED-sympy]) AND the real curvature-twisted D_S6 operator has "
            "an exact zero eigenvalue (G73/G74A, [VERIFIED-sympy], NOT reconstructed in this "
            "script), THEN D_full has an exact zero eigenvalue too (0^2+0^2=0). This script "
            "verifies the first conjunct in full generality; the second and third conjuncts are "
            "cited from prior gates, not re-derived here."
        ),
        "label": (
            "PASS_DECOUPLING_SURVIVES_TORSION_DEFORMATION"
            if (construction_ok and decoupling_survives)
            else "FAIL"
        ),
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e3.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
