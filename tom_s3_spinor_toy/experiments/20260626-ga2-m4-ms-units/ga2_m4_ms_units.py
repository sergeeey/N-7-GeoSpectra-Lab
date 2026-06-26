"""GA2: M4/Ms units map — express G91 masses in physical units.

G91 gave m_mod/m_KK = 0.198% in string units (M_s = 1).
GA2 answers:
  - What is M_s in terms of M_Pl(4D)?
  - What is m_mod in GeV if M_s is fixed?
  - Is the modulus cosmologically safe? (Coughlan bound: m_mod > ~30 TeV)
  - What M_s is needed for TeV-scale KK modes?

Standard KK reduction D=13 -> D=4:
  M_Pl^2(4) = M_s^11 * V_9 / (2*pi)^9   [in natural units hbar=c=1]

Internal volume at G91 minimum (rho3 = rho6^2):
  V_9 = Vol(S3) * Vol(S6) = 2*pi^2*rho3^3 * 16*pi^3/15*rho6^6
      = (32*pi^5/15) * rho6^12   [= Omega^2 * (32*pi^5/15)]
"""

from __future__ import annotations

import json
from math import pi, sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ga2.json"

# G91 minimum values (string units, M_s = 1)
RHO6_MIN = 1.1790613418407443
RHO3_MIN = RHO6_MIN**2  # = 1.3902, from path constraint rho3 = rho6^2
M_MOD_STRING = 0.002134275055586503  # from G91 results_g91.json
M_KK_STRING = 1.0789925808460523  # S3 lightest, from G91
RATIO = M_MOD_STRING / M_KK_STRING  # = 0.001978 (= 0.198%)

# Physical constants
M_PL_GEV = 1.220e19  # Planck mass in GeV (M_Pl = sqrt(8*pi*G)^-1 = 1.22e19 GeV)
M_PL_REDUCED_GEV = 2.435e18  # Reduced Planck mass M_Pl/sqrt(8*pi)

# Kaluza-Klein reduction: D=13 total, d=9 extra dimensions (S3 x S6)
D_TOTAL = 13
D_EXT = 9

VOL_S3_UNIT = 2 * pi**2  # Vol(S^3, r=1)
VOL_S6_UNIT = 16 * pi**3 / 15  # Vol(S^6, r=1)


def compute_units() -> dict:
    # Internal volume at G91 minimum (in string units ls=1)
    vol_s3 = VOL_S3_UNIT * RHO3_MIN**3
    vol_s6 = VOL_S6_UNIT * RHO6_MIN**6
    v9 = vol_s3 * vol_s6

    # M_Pl^2 = M_s^(D-2) * V_d / (2*pi)^d
    # Simple KK convention (Duff-Nilsson-Pope): M_Pl^2 = M_s^(D-2) * V_d
    # In string units M_s=1: M_Pl^2/M_s^2 = V_9
    # WHY no (2pi): using geometric volume without momentum-space factors;
    # consistent with G91 potential normalisation (same convention throughout)
    ratio_mpl_ms_sq = v9
    ratio_mpl_ms = sqrt(ratio_mpl_ms_sq)  # M_Pl / M_s  (dimensionless)

    # String scale in GeV
    ms_gev = M_PL_GEV / ratio_mpl_ms

    # Physical masses in GeV
    m_mod_gev = M_MOD_STRING * ms_gev
    m_kk_gev = M_KK_STRING * ms_gev

    # Coughlan bound: moduli lighter than ~30 TeV overclosure universe
    coughlan_bound_gev = 3e4  # 30 TeV
    cosmologically_safe = m_mod_gev > coughlan_bound_gev

    # What M_s needed for m_KK ~ 1 TeV? (large extra dimensions scenario)
    tev_in_gev = 1e3
    ms_for_tev_kk = tev_in_gev / M_KK_STRING  # GeV
    # Then what radius? rho6 * (1/ms_for_tev_kk) in meters
    ls_for_tev = 1.0 / ms_for_tev_kk  # in GeV^-1
    ls_for_tev_m = ls_for_tev * 0.197e-15  # convert GeV^-1 to meters (hbar*c = 0.197 GeV*fm)
    rho6_for_tev_m = RHO6_MIN * ls_for_tev_m

    return {
        "geometry": {
            "rho6_min_string_units": RHO6_MIN,
            "rho3_min_string_units": RHO3_MIN,
            "vol_s3_string_units": vol_s3,
            "vol_s6_string_units": vol_s6,
            "v9_total_string_units": v9,
        },
        "planck_ratio": {
            "M_Pl_over_M_s": ratio_mpl_ms,
            "M_s_over_M_Pl": 1.0 / ratio_mpl_ms,
            "interpretation": f"String scale is M_s = M_Pl / {ratio_mpl_ms:.1f}",
        },
        "physical_masses": {
            "M_s_GeV": ms_gev,
            "m_KK_GeV": m_kk_gev,
            "m_mod_GeV": m_mod_gev,
            "m_KK_TeV": m_kk_gev / 1e3,
            "m_mod_TeV": m_mod_gev / 1e3,
            "ratio_check": m_mod_gev / m_kk_gev,
        },
        "cosmology": {
            "coughlan_bound_TeV": coughlan_bound_gev / 1e3,
            "m_mod_TeV": m_mod_gev / 1e3,
            "cosmologically_safe": cosmologically_safe,
            "verdict": (
                "SAFE — modulus heavier than Coughlan bound"
                if cosmologically_safe
                else "PROBLEM — modulus lighter than Coughlan bound (moduli problem)"
            ),
        },
        "tev_scenario": {
            "ms_needed_for_tev_kk_GeV": ms_for_tev_kk,
            "string_length_meters": ls_for_tev_m,
            "rho6_physical_meters": rho6_for_tev_m,
            "interpretation": (
                "For TeV-scale KK modes, need rho6 ~ {:.2e} m — "
                "sub-mm extra dimensions (ADD scenario, not our case)"
            ).format(rho6_for_tev_m),
        },
    }


def main() -> None:
    data = compute_units()

    g = data["geometry"]
    p = data["planck_ratio"]
    m = data["physical_masses"]
    c = data["cosmology"]
    t = data["tev_scenario"]

    print("\n=== GA2: M4/Ms Units Map ===\n")
    print(f"Internal volume V9 = {g['v9_total_string_units']:.4f} ls^9")
    print(f"M_Pl / M_s        = {p['M_Pl_over_M_s']:.2f}")
    print(f"M_s               = {m['M_s_GeV']:.3e} GeV  = {m['M_s_GeV']/1e16:.3f} x 10^16 GeV")
    print()
    print(f"m_KK (physical)   = {m['m_KK_GeV']:.3e} GeV  = {m['m_KK_TeV']:.3e} TeV")
    print(f"m_mod (physical)  = {m['m_mod_GeV']:.3e} GeV  = {m['m_mod_TeV']:.3e} TeV")
    print(f"ratio check       = {m['ratio_check']*100:.4f}%  (should be 0.1978%)")
    print()
    print(f"Coughlan bound    : m_mod > {c['coughlan_bound_TeV']:.0f} TeV")
    print(f"Our m_mod         : {c['m_mod_TeV']:.3e} TeV")
    print(f"Cosmological verdict: {c['verdict']}")
    print()
    print(
        f"For TeV KK: need M_s = {t['ms_needed_for_tev_kk_GeV']:.2e} GeV, rho6 = {t['rho6_physical_meters']:.2e} m"
    )

    results = {"gate": "GA2", **data}
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
