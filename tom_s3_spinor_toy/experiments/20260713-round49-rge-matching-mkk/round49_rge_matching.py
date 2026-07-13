"""Round 49 (2026-07-13): forward 1-loop SM RGE running of g2^2/g3^2 from
M_Z to the geometrically-predicted compactification scale, to turn the
preprint's qualitative "requires threshold corrections or new particle
content... not computed" (Sec 2.2, RGE matching constraint paragraph) into
a quantitative number.

PRIOR RESULT GATE (run before writing this script, see decision.md for the
full report): confirmed OPEN. Two corrections to the Round 48 recommendation
that first proposed this round:
  1. GA2's "M_KK ~= 1.78e17 GeV" was a mislabeling -- 1.78e17 GeV is GA2's
     M_s (string scale); GA2's own M_KK is 1.9176e17 GeV (results_ga2.json).
  2. GA1 (lambda-sensitivity, ROBUST verdict) shows rho6_min shifts by
     <0.3% across lambda in [0.15,0.60] -- so neither M_s nor M_KK depends
     meaningfully on the free parameter lambda (Bottleneck 1) for RGE
     purposes; GA2's caveat 3 (does not map to SM coupling scale without
     lambda fixed) is real in principle but negligible in practice, per
     GA1's own quantification.

SCALE CHOICE: this script uses M_s (string scale, 1.78e17 GeV), not M_KK,
as the "coupling-matching" scale. G87 (2026-06-22, decision.md) already
established that G29's ratio (15/16pi, computed at the equal-radii
rho3=rho6=1 point) is naturally associated with the string scale
(rho6~1), not the physical moduli-minimum scale (rho6_min=1.179, where
G87 found the ratio evaluates instead to 0.230 on a DIFFERENT, since-
questioned trajectory formula -- see decision.md "G87 caveat" section).
Using M_s here sidesteps that unresolved question entirely; it is not
needed for this calculation.

METHOD (forward direction, the genuinely new part vs. the paper's existing
backward-solve paragraph): start from PDG-known SM values at M_Z (no free
parameters), run 1-loop RGE UP to M_s using the SAME beta coefficients
already cited in preprint.tex's RGE-matching paragraph (b3=-7, b2=-19/6,
MSbar), and read off the predicted ratio AT M_s. Compare to G29's
geometric prediction 15/(16*pi).

POSITIVE CONTROL (run first, must reproduce the paper's own already-
published numbers before the new M_s-scale result is trusted):
preprint.tex states the backward-solved M_KK~=130 GeV, and forward-checks
at 1 TeV -> ratio=0.362, at 10 TeV -> ratio=0.430. This script's own
forward-RGE function is run at those same three scales first; if it does
not reproduce those three numbers, the calculation is wrong and the new
M_s result must not be trusted.
"""

from __future__ import annotations

import json
from math import log, pi
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round49.json"

# PDG 2022 inputs at M_Z (same values implied by preprint.tex's own stated
# SM ratio at M_Z, 0.287 -- used here as a cross-check, see main()).
M_Z_GEV = 91.1876
ALPHA_EM_INV_MZ = (
    127.955  # PDG, MS-bar running QED coupling AT M_Z (not the low-energy 137.036 value)
)
SIN2_THETAW_MZ = 0.23122  # PDG, MS-bar

# SM one-loop beta coefficients, MS-bar scheme -- SAME values already cited
# in preprint.tex's "RGE matching constraint" paragraph (sec:coupling).
B2 = -19.0 / 6.0
B3 = -7.0

# Geometric inputs (existing gates, not recomputed here)
G29_RATIO = 15.0 / (
    16.0 * pi
)  # g2^2/g3^2 tree-level prediction, PROMOTE, experiments/20260620-g29-coupling-ratio
M_S_GEV = (
    1.7772044319035818e17  # GA2 string scale, results_ga2.json (this work does not recompute GA2)
)
M_KK_GEV = 1.917590396670688e17  # GA2 lightest S3 KK mode, results_ga2.json, for reference only (not used as the RGE scale here)


def alpha2_inv_mz() -> float:
    """alpha2^-1(M_Z) from PDG alpha_em(M_Z) and sin^2(theta_W)(M_Z): alpha2 = alpha_em/sin^2(theta_W)."""
    alpha_em_mz = 1.0 / ALPHA_EM_INV_MZ
    alpha2_mz = alpha_em_mz / SIN2_THETAW_MZ
    return 1.0 / alpha2_mz


def alpha3_inv_mz(alpha_s_mz: float = 0.1179) -> float:
    """alpha3^-1(M_Z) = 1/alpha_s(M_Z), PDG 2022 world average alpha_s(M_Z)=0.1179."""
    return 1.0 / alpha_s_mz


def run_ratio(mu_gev: float, a2inv_mz: float, a3inv_mz: float) -> dict:
    """One-loop RGE: alpha_i^-1(mu) = alpha_i^-1(M_Z) - (b_i/2pi) * ln(mu/M_Z).
    Returns g2^2/g3^2(mu) = alpha2(mu)/alpha3(mu) = alpha3^-1(mu)/alpha2^-1(mu)."""
    d_ln = log(mu_gev / M_Z_GEV)
    a2inv_mu = a2inv_mz - (B2 / (2 * pi)) * d_ln
    a3inv_mu = a3inv_mz - (B3 / (2 * pi)) * d_ln
    ratio = a3inv_mu / a2inv_mu
    return {
        "mu_GeV": mu_gev,
        "alpha2_inv": a2inv_mu,
        "alpha3_inv": a3inv_mu,
        "ratio_g2sq_g3sq": ratio,
    }


def main() -> None:
    a2inv_mz = alpha2_inv_mz()
    a3inv_mz = alpha3_inv_mz()
    ratio_mz = a3inv_mz / a2inv_mz

    print("=" * 70)
    print("STEP 0: cross-check PDG inputs against preprint.tex's own stated M_Z ratio")
    print("=" * 70)
    print(f"  alpha2^-1(M_Z) = {a2inv_mz:.4f}")
    print(f"  alpha3^-1(M_Z) = {a3inv_mz:.4f}")
    print(f"  g2^2/g3^2(M_Z) = {ratio_mz:.4f}  (preprint.tex states 0.287 / 0.2865)")
    assert abs(ratio_mz - 0.2865) < 0.01, (
        f"PDG-derived M_Z ratio {ratio_mz:.4f} does not match preprint.tex's stated "
        "0.2865 -- input values are wrong, STOP before trusting anything below"
    )
    print("  PASS: matches preprint.tex's stated SM value at M_Z within 0.01")

    print()
    print("=" * 70)
    print("STEP 1 (POSITIVE CONTROL): reproduce preprint.tex's own published")
    print("forward-check numbers (0.362 at 1 TeV, 0.430 at 10 TeV) before")
    print("trusting the new M_s-scale result")
    print("=" * 70)
    control_1tev = run_ratio(1.0e3, a2inv_mz, a3inv_mz)
    control_10tev = run_ratio(1.0e4, a2inv_mz, a3inv_mz)
    print(f"  ratio(1 TeV)  = {control_1tev['ratio_g2sq_g3sq']:.4f}  (preprint.tex states 0.362)")
    print(f"  ratio(10 TeV) = {control_10tev['ratio_g2sq_g3sq']:.4f}  (preprint.tex states 0.430)")
    assert abs(control_1tev["ratio_g2sq_g3sq"] - 0.362) < 0.01, (
        "FAILED positive control at 1 TeV -- STOP"
    )
    assert abs(control_10tev["ratio_g2sq_g3sq"] - 0.430) < 0.01, (
        "FAILED positive control at 10 TeV -- STOP"
    )
    print("  PASS: both positive-control values reproduced within 0.01")

    print()
    print("=" * 70)
    print("STEP 2: backward-solve for M_KK such that ratio(M_KK) = 15/(16*pi)")
    print("(reproduces preprint.tex's existing ~130 GeV figure, sanity check)")
    print("=" * 70)
    # bisection on ln(mu) since ratio is monotonic in mu here
    lo, hi = 10.0, 1.0e5  # GeV bracket
    # ratio increases monotonically with mu (0.287 at M_Z -> 0.362 at 1 TeV -> 0.430 at 10 TeV)
    for _ in range(200):
        mid = (lo * hi) ** 0.5  # geometric bisection (log-linear)
        r = run_ratio(mid, a2inv_mz, a3inv_mz)["ratio_g2sq_g3sq"]
        if r < G29_RATIO:
            lo = mid
        else:
            hi = mid
    mkk_backward_gev = (lo * hi) ** 0.5
    print(f"  Backward-solved M_KK = {mkk_backward_gev:.2f} GeV  (preprint.tex states ~130 GeV)")
    assert abs(mkk_backward_gev - 130.0) < 5.0, (
        "Backward-solved M_KK does not match preprint's ~130 GeV -- STOP"
    )
    print("  PASS: matches preprint.tex's stated ~130 GeV within 5 GeV")

    print()
    print("=" * 70)
    print("STEP 3 (THE NEW RESULT): forward-run from M_Z to the geometrically")
    print("predicted string scale M_s = 1.7772e17 GeV (GA2), read off the")
    print("predicted ratio there, compare to G29's tree-level prediction")
    print("=" * 70)
    at_ms = run_ratio(M_S_GEV, a2inv_mz, a3inv_mz)
    print(f"  M_s (GA2)               = {M_S_GEV:.4e} GeV")
    print(f"  alpha2^-1(M_s)          = {at_ms['alpha2_inv']:.3f}")
    print(f"  alpha3^-1(M_s)          = {at_ms['alpha3_inv']:.3f}")
    print(f"  Predicted g2^2/g3^2(M_s) [pure 1-loop SM running] = {at_ms['ratio_g2sq_g3sq']:.4f}")
    print(f"  G29 geometric prediction (tree-level, at rho=1)   = {G29_RATIO:.4f}")
    factor = at_ms["ratio_g2sq_g3sq"] / G29_RATIO
    print(f"  Factor mismatch (pure-SM-running-predicted / geometric) = {factor:.3f}x")

    print()
    print("=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print(
        f"  Pure 1-loop SM running from M_Z predicts a coupling ratio of "
        f"{at_ms['ratio_g2sq_g3sq']:.3f} at the geometrically-predicted string "
        f"scale M_s={M_S_GEV:.2e} GeV -- a factor of {factor:.2f}x away from "
        f"G29's tree-level geometric prediction of {G29_RATIO:.3f}. This is a "
        f"MUCH larger mismatch than the +4.3% gap at M_Z suggests: the two "
        f"couplings very nearly meet (ratio~1) around this scale under pure "
        f"SM running (the well-known approximate, non-SUSY gauge unification "
        f"region), while the geometric tree-level prediction stays fixed at "
        f"15/(16*pi)=0.298 independent of scale. Reconciling the two requires "
        f"either a large threshold correction / new intermediate-scale "
        f"particle content that substantially changes the running between "
        f"M_Z and M_s, or reconsidering whether M_s is the correct coupling-"
        f"matching scale for this comparison at all."
    )

    results = {
        "gate": "Round49-RGE",
        "inputs": {
            "M_Z_GeV": M_Z_GEV,
            "alpha_em_inv_MZ_PDG": ALPHA_EM_INV_MZ,
            "sin2_thetaW_MZ_PDG": SIN2_THETAW_MZ,
            "alpha_s_MZ_PDG": 0.1179,
            "b2": B2,
            "b3": B3,
            "G29_ratio_tree_level": G29_RATIO,
            "M_s_GeV_GA2": M_S_GEV,
            "M_KK_GeV_GA2_for_reference_only": M_KK_GEV,
        },
        "cross_check_mz_ratio": ratio_mz,
        "positive_controls": {
            "ratio_1TeV": control_1tev["ratio_g2sq_g3sq"],
            "ratio_10TeV": control_10tev["ratio_g2sq_g3sq"],
            "backward_solved_MKK_GeV": mkk_backward_gev,
        },
        "new_result_at_Ms": at_ms,
        "factor_mismatch_predicted_over_geometric": factor,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
