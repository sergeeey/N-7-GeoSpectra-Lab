"""C219 audit A3: (1) which test files fit the S^6 heat-kernel coefficients, and how far off are they;
(2) how much do the downstream scripts that hard-code rho6*=1.090 move when it is replaced by the exact 1.1541.

Nothing in the repo is modified: each downstream script is copied to a temp dir, run unchanged and with the
constant replaced, and the printed numbers are compared (crude: any number on a differing line). Scripts that
embed OTHER hard-coded reference values from the old run (e.g. G92's G91 minimum) give invalid patched output;
those are flagged by the reader in decision.md, not by this script.
"""

from __future__ import annotations

import importlib
import re
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
EXP = HERE.parent
NEW_RHO = "1.1541"

# ------------------------------------------------------------------ (1) fit audit
EXACT = {
    "B0": 2 / 15,
    "B2": -1 / 3,
    "B4": 4 / 15,
    "B6": -0.0505291,
    "B8": -0.0076455,
    "B10": -0.0029521,
}
FIT_USERS = {
    "g54b": ("test_g54b_casimir_pole", "_sw_s6_coefficients"),
    "g54c": ("test_g54c_effective_potential", "_sw_s6_full"),
    "g54d": ("test_g54d_hadamard_fp", "_sw"),
    "g54e": ("test_g54e_zeta_fp_structure", "_sw"),
    "g54f": ("test_g54f_4d_eh_frame", "_sw"),
    "g55": ("test_g55_two_flux_2d", "_sw"),
    "g56": ("test_g56_kklt_like_np", "_sw"),
    "g57": ("test_g57_uv_selection", "_sw"),
    "g58": ("test_g58_curvature_casimir", "_sw"),
    "g60": ("test_g60_geometric_np_parameters", "_sw"),
}


def fit_audit() -> None:
    warnings.filterwarnings("ignore")
    sys.path.insert(0, str(ROOT / "tests"))
    sys.path.insert(0, str(ROOT))
    print(
        "A. S^6 heat-kernel coefficients as fitted by each test file vs exact (Mellin)"
    )
    print(f"{'file':6} " + " ".join(f"{k:>10}" for k in EXACT))
    print(f"{'exact':6} " + " ".join(f"{v:10.6f}" for v in EXACT.values()))
    for key, (mod, fn) in FIT_USERS.items():
        try:
            d = getattr(importlib.import_module(mod), fn)()
            print(
                f"{key:6} "
                + " ".join(
                    f"{float(d[b]):10.6f}" if b in d else f"{'-':>10}" for b in EXACT
                )
            )
        except Exception as exc:  # noqa: BLE001 -- audit must continue past one broken import
            print(key, "ERR", type(exc).__name__, str(exc)[:80])


# ------------------------------------------------------------------ (2) sensitivity
TARGETS = [
    "20260621-g70-functional-form/vary_exponent.py",
    "20260622-g77-uplift-solver/g77_uplift_solver.py",
    "20260622-g82-canonical-mass/g82_canonical_mass.py",
    "20260622-g84c-functional-form-degeneracy/g84c_functional_form_degeneracy.py",
    "20260622-g85b-spectral-saddle/g85b_spectral_saddle.py",
    "20260623-g88a-canonical-radion-normalization/g88a_canonical_radion_normalization.py",
    "20260623-g88b-kk-scale-consistency/g88b_kk_scale_consistency.py",
    "20260623-g88d-full-4d-reduced-action-mass-extraction/g88d_full_4d_reduced_action_mass_extraction.py",
    "20260623-g88e-kk-scale-frame-consistency/g88e_kk_scale_frame_consistency.py",
    "20260623-g88f-full-reduced-action-reconstruction/g88f_full_reduced_action_reconstruction.py",
    "20260624-g91-full-4d-reduction/g91_full_4d_reduction.py",
    "20260626-g92-s3-casimir-stabilization/g92_s3_casimir.py",
    "20260626-g93-flux-quantization-path/g93_flux_path.py",
    "20260626-g94-s3-np-instanton/g94_s3_np_instanton.py",
    "20260626-ga1-lambda-sensitivity/ga1_lambda_sensitivity.py",
    "20260705-g103-kk-lambda-blindness/g103_kk_lambda_blindness.py",
    "20260705-g104-h1-h2-s2xs6/g104_h1_h2_s2xs6.py",
    "20260715-round63-wrapped-s3-instanton-channel/round63_corrected_v2.py",
    "20260715-round63-wrapped-s3-instanton-channel/round63_route_b_independent_check.py",
]
NUM = re.compile(r"[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?")
ASSIGN = re.compile(r"=\s*(mp\.mpf\(\")?1\.090")


def run_copy(text: str, tmp: Path, tag: str):
    d = tmp / tag
    d.mkdir(parents=True, exist_ok=True)
    f = d / "s.py"
    f.write_text(text, encoding="utf-8")
    try:
        r = subprocess.run(
            [sys.executable, str(f)],
            capture_output=True,
            text=True,
            timeout=240,
            cwd=d,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return -9, ""
    return r.returncode, r.stdout


def sensitivity() -> None:
    print()
    print(
        f"B. Replace the hard-coded rho6*=1.090 by {NEW_RHO} (copies in a temp dir; repo untouched)"
    )
    tmp = Path(tempfile.mkdtemp(prefix="s"))
    for i, t in enumerate(TARGETS):
        text = (EXP / t).read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        idx = [
            k
            for k, line in enumerate(lines)
            if ASSIGN.search(line) and not line.lstrip().startswith("#")
        ]
        if not idx:
            print(f"  {t.split('/')[-1]}: no assignment found")
            continue
        new = lines[:]
        for k in idx:
            new[k] = lines[k].replace("1.090", NEW_RHO, 1)
        ra, oa = run_copy(text, tmp, f"{i}o")
        rb, ob = run_copy("".join(new), tmp, f"{i}n")
        if ra != 0 or rb != 0:
            print(f"  {t.split('/')[-1]}: did not run cleanly (rc {ra}/{rb})")
            continue
        worst, nd = 0.0, 0
        for x, y in zip(oa.splitlines(), ob.splitlines(), strict=False):
            if x != y:
                nd += 1
                for u, v in zip(
                    (float(a) for a in NUM.findall(x)),
                    (float(b) for b in NUM.findall(y)),
                    strict=False,
                ):
                    if abs(u) > 1e-12 and u != v:
                        worst = max(worst, abs(v - u) / abs(u))
        print(
            f"  {t.split('/')[-1]}: differing output lines={nd}, max relative change of any number={worst:.3f}"
        )


if __name__ == "__main__":
    fit_audit()
    sensitivity()
