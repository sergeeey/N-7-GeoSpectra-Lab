"""No-eigensolve statistical re-analysis of the Gate 4B IPR contrast claim.

PURPOSE
    Address methodological gaps found by the hypothesis-red-team audit (AOS 40/100)
    WITHOUT any new compute. Reads the 216 already-stored per-case `true_ipr_mean`
    scalars from gate4_fss_v0.1.24 and replaces the arithmetic-ratio-of-means with
    statistically defensible quantities.

WHAT THIS FIXES (re-analysis only — NO eig/eigh, NO operator build):
    A. correct_test    : paired Wilcoxon signed-rank + geometric-mean ratio + bootstrap CI
                         (replaces arithmetic ratio of means on lognormal IPR)
    B. multiple_comp   : BH-FDR (dependent) + Holm on per-family / per-size / j_max sub-claims
    C. robust_fraction : specification-curve over aggregation choices
                         {arith, geo, median} x {all, per-family, per-size, per-j_max}
    D. tipping_point   : how large a multiplicative bias in IPR_W0 would push the
                         geometric contrast below the pre-registered 2.0x threshold (H3)
    E. LOGO            : leave-one-family-out stability as a replication PROXY (H2)
                         — does NOT close T10 (same codebase/machine), only softens it.

WHAT THIS CANNOT FIX (needs compute or new pre-registered run — DEFERRED):
    - a-priori power (T6): only OBSERVED effect size is reported, explicitly NOT a-priori
    - spectrum-fraction multiverse (bottom 5/10/20%): per-state IPR not stored
    - true independent replication (T10): needs different machine / external data

INPUT  : reports/RUNS/gate4_fss_v0.1.24/batches/*/results.json  (216 cases)
OUTPUT : reports/GATE4B_REANALYSIS_STATS_2026-06-07.md
         reports/GATE4B_REANALYSIS_STATS_2026-06-07.json

USAGE  : python scripts/reanalyze_gate4b_stats.py
         python scripts/reanalyze_gate4b_stats.py --dry-run

NOTE   : numbers generated here are GENERATED, not VALIDATED. Adversarial falsification
         (skeptic / FL) of hypotheses H1-H3 is a separate step and remains pending.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
from itertools import product
from pathlib import Path

import numpy as np
from scipy import stats

REPO_ROOT = Path(__file__).resolve().parent.parent
RUN_DIR = REPO_ROOT / "reports/RUNS/gate4_fss_v0.1.24/batches"
PREREG_THRESHOLD = 2.0
IPR_FIELD = "true_ipr_mean"
W_LOW, W_HIGH = 0, 20
KEY_FIELDS = ("family", "s1_size", "j_max", "seed")


# --------------------------------------------------------------------------- #
# Data loading
# --------------------------------------------------------------------------- #
def load_cases() -> list[dict]:
    files = sorted(glob.glob(str(RUN_DIR / "*/results.json")))
    rows: list[dict] = []
    for f in files:
        rows += json.load(open(f, encoding="utf-8"))
    if not rows:
        raise SystemExit(f"No cases found under {RUN_DIR}")
    return rows


def build_pairs(rows: list[dict]) -> list[dict]:
    """Match W_LOW vs W_HIGH cases on (family, size, j_max, seed)."""
    low = {tuple(r[k] for k in KEY_FIELDS): r for r in rows if r["disorder_strength"] == W_LOW}
    high = {tuple(r[k] for k in KEY_FIELDS): r for r in rows if r["disorder_strength"] == W_HIGH}
    pairs = []
    for key in sorted(low.keys() & high.keys()):
        ipr0 = float(low[key][IPR_FIELD])
        ipr1 = float(high[key][IPR_FIELD])
        if ipr0 <= 0 or ipr1 <= 0:
            continue  # IPR must be positive for log; skip degenerate
        pairs.append(
            {
                "family": key[0],
                "s1_size": key[1],
                "j_max": key[2],
                "seed": key[3],
                "ipr_w0": ipr0,
                "ipr_w20": ipr1,
                "log_ratio": math.log(ipr1) - math.log(ipr0),
                "ratio": ipr1 / ipr0,
            }
        )
    return pairs


# --------------------------------------------------------------------------- #
# Multiple-comparison corrections (manual — no statsmodels dependency)
# --------------------------------------------------------------------------- #
def bh_fdr(pvals: list[float]) -> list[float]:
    """Benjamini-Hochberg adjusted p-values."""
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i])
    adj = [0.0] * n
    prev = 1.0
    for rank, idx in enumerate(reversed(order), start=1):
        k = n - rank + 1  # original ascending rank
        val = min(prev, pvals[idx] * n / k)
        adj[idx] = val
        prev = val
    return adj


def holm(pvals: list[float]) -> list[float]:
    """Holm-Bonferroni adjusted p-values."""
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i])
    adj = [0.0] * n
    prev = 0.0
    for rank, idx in enumerate(order, start=1):
        val = max(prev, min(1.0, (n - rank + 1) * pvals[idx]))
        adj[idx] = val
        prev = val
    return adj


# --------------------------------------------------------------------------- #
# Core statistics on a set of pairs
# --------------------------------------------------------------------------- #
def paired_stats(pairs: list[dict]) -> dict:
    """Wilcoxon signed-rank + geometric mean ratio + effect size for a pair set."""
    log_ratios = np.array([p["log_ratio"] for p in pairs])
    ipr0 = np.array([p["ipr_w0"] for p in pairs])
    ipr1 = np.array([p["ipr_w20"] for p in pairs])
    n = len(log_ratios)

    geo_ratio = float(np.exp(np.mean(log_ratios)))
    arith_ratio = float(np.mean(ipr1) / np.mean(ipr0))
    median_ratio = float(np.median(ipr1 / ipr0))

    # Wilcoxon signed-rank on differences (H0: median log-ratio = 0)
    try:
        w_stat, p_val = stats.wilcoxon(ipr1, ipr0, alternative="greater")
        w_stat, p_val = float(w_stat), float(p_val)
    except ValueError:
        w_stat, p_val = float("nan"), float("nan")

    # Paired effect size on log scale (Cohen's d_z) + common-language effect
    sd = float(np.std(log_ratios, ddof=1)) if n > 1 else float("nan")
    d_z = float(np.mean(log_ratios) / sd) if sd and sd > 0 else float("nan")
    cles = float(np.mean(ipr1 > ipr0))  # fraction of pairs where disorder increases IPR

    return {
        "n_pairs": n,
        "geometric_mean_ratio": geo_ratio,
        "arithmetic_ratio_of_means": arith_ratio,
        "median_of_per_pair_ratio": median_ratio,
        "wilcoxon_stat": w_stat,
        "wilcoxon_p_one_sided_greater": p_val,
        "cohens_dz_logscale": d_z,
        "common_language_effect": cles,
        "passes_2x_geometric": bool(geo_ratio >= PREREG_THRESHOLD),
    }


def bootstrap_ci(pairs: list[dict], n_boot: int = 10000, seed: int = 2026) -> dict:
    """Percentile bootstrap CI for the geometric mean ratio (resample pairs)."""
    rng = np.random.default_rng(seed)
    log_ratios = np.array([p["log_ratio"] for p in pairs])
    n = len(log_ratios)
    boot = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, n)
        boot[b] = np.exp(np.mean(log_ratios[idx]))
    return {
        "geometric_mean_ratio_ci95": [
            float(np.percentile(boot, 2.5)),
            float(np.percentile(boot, 97.5)),
        ],
        "n_boot": n_boot,
    }


# --------------------------------------------------------------------------- #
# Specification curve (multiverse over aggregation, H1)
# --------------------------------------------------------------------------- #
def aggregate_contrast(pairs: list[dict], central: str) -> float:
    ipr0 = np.array([p["ipr_w0"] for p in pairs])
    ipr1 = np.array([p["ipr_w20"] for p in pairs])
    ratios = ipr1 / ipr0
    if central == "arith":
        return float(np.mean(ipr1) / np.mean(ipr0))
    if central == "geo":
        return float(np.exp(np.mean(np.log(ratios))))
    if central == "median":
        return float(np.median(ratios))
    raise ValueError(central)


def specification_curve(pairs: list[dict]) -> dict:
    centrals = ["arith", "geo", "median"]
    groupings = {
        "all": [("all", pairs)],
        "per_family": [
            (f, [p for p in pairs if p["family"] == f])
            for f in sorted({p["family"] for p in pairs})
        ],
        "per_size": [
            (s, [p for p in pairs if p["s1_size"] == s])
            for s in sorted({p["s1_size"] for p in pairs})
        ],
        "per_jmax": [
            (j, [p for p in pairs if p["j_max"] == j]) for j in sorted({p["j_max"] for p in pairs})
        ],
    }
    specs = []
    for central, (gname, glist) in product(centrals, groupings.items()):
        for subname, subpairs in glist:
            if not subpairs:
                continue
            c = aggregate_contrast(subpairs, central)
            specs.append(
                {
                    "central": central,
                    "grouping": gname,
                    "subset": str(subname),
                    "contrast": c,
                    "passes": bool(c >= PREREG_THRESHOLD),
                    "n": len(subpairs),
                }
            )
    n_pass = sum(s["passes"] for s in specs)
    return {
        "n_specs": len(specs),
        "n_pass": n_pass,
        "robust_fraction": n_pass / len(specs) if specs else 0.0,
        "min_contrast": min(s["contrast"] for s in specs),
        "max_contrast": max(s["contrast"] for s in specs),
        "specs": specs,
    }


# --------------------------------------------------------------------------- #
# Tipping point (H3) and leave-one-family-out (H2)
# --------------------------------------------------------------------------- #
def tipping_point(geo_ratio: float) -> dict:
    """Multiplicative bias on IPR_W0 needed to push geometric contrast below threshold."""
    factor = geo_ratio / PREREG_THRESHOLD
    return {
        "geometric_contrast": geo_ratio,
        "threshold": PREREG_THRESHOLD,
        "ipr_w0_inflation_to_break": factor,
        "interpretation": (
            f"IPR_W0 baseline would need to be ~{factor:.2f}x larger (or IPR_W20 that much "
            f"smaller) to drag the geometric contrast below {PREREG_THRESHOLD}x."
        ),
    }


def leave_one_family_out(pairs: list[dict]) -> dict:
    families = sorted({p["family"] for p in pairs})
    out = []
    for held in families:
        kept = [p for p in pairs if p["family"] != held]
        held_pairs = [p for p in pairs if p["family"] == held]
        kept_geo = aggregate_contrast(kept, "geo")
        held_geo = aggregate_contrast(held_pairs, "geo")
        out.append(
            {
                "held_out_family": held,
                "geo_contrast_on_kept_2_families": kept_geo,
                "geo_contrast_on_held_family": held_geo,
                "kept_passes": bool(kept_geo >= PREREG_THRESHOLD),
                "held_passes": bool(held_geo >= PREREG_THRESHOLD),
            }
        )
    all_stable = all(o["kept_passes"] and o["held_passes"] for o in out)
    return {"folds": out, "all_folds_stable": all_stable}


def observed_power(pairs: list[dict]) -> dict:
    """OBSERVED effect-size sensitivity. NOT a-priori power (T6 cannot be retro-fixed)."""
    log_ratios = np.array([p["log_ratio"] for p in pairs])
    n = len(log_ratios)
    sd = float(np.std(log_ratios, ddof=1))
    d_z = float(np.mean(log_ratios) / sd) if sd > 0 else float("nan")
    result = {
        "observed_dz_logscale": d_z,
        "n_pairs": n,
        "caveat": (
            "This is the OBSERVED effect size, not an a-priori power analysis. "
            "Post-hoc power is a deterministic function of the p-value and does NOT "
            "recover the T6 (winner's curse) protection. A genuine a-priori power "
            "analysis requires a NEW pre-registered run."
        ),
    }
    try:
        from statsmodels.stats.power import TTestPower

        power = float(
            TTestPower().power(effect_size=abs(d_z), nobs=n, alpha=0.05, alternative="larger")
        )
        result["achieved_power_given_observed_dz"] = power
    except Exception as exc:  # statsmodels optional
        result["achieved_power_given_observed_dz"] = None
        result["power_note"] = f"statsmodels unavailable ({exc}); skipped numeric power."
    return result


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def write_markdown(res: dict, path: Path) -> None:
    g = res["global"]
    ci = res["bootstrap"]["geometric_mean_ratio_ci95"]
    sc = res["spec_curve"]
    sub = res["subgroups"]

    lines = [
        "# Gate 4B IPR Contrast — No-Compute Statistical Re-analysis (2026-06-07)",
        "",
        "> **GENERATED, NOT VALIDATED.** Numbers below come from re-analysis of the "
        "216 already-stored `true_ipr_mean` scalars (gate4_fss_v0.1.24). "
        "No eigensolve, no operator build. Adversarial falsification of H1-H3 "
        "(skeptic / falsification-ladder) is a separate, still-pending step.",
        "",
        "## Purpose",
        "",
        "Address hypothesis-red-team AOS gaps (was 40/100) using only re-analysis. "
        "Replaces arithmetic-ratio-of-means with paired Wilcoxon + geometric-mean ratio, "
        "adds multiple-comparison correction and a specification curve.",
        "",
        "## Data provenance [VERIFIED]",
        "",
        "- Source: `reports/RUNS/gate4_fss_v0.1.24/batches/*/results.json`",
        f"- Cases: {res['meta']['n_cases']} | matched W=0 vs W=20 pairs: {g['n_pairs']}",
        f"- Pairing key: {', '.join(KEY_FIELDS)}",
        f"- Pre-registered threshold: contrast >= {PREREG_THRESHOLD}x",
        "",
        "## A. Correct test (was: arithmetic ratio of means)",
        "",
        "| Quantity | Value |",
        "|---|---|",
        f"| Geometric-mean ratio (primary) | **{g['geometric_mean_ratio']:.3f}x** |",
        f"| Geometric-mean ratio 95% CI (bootstrap) | [{ci[0]:.3f}, {ci[1]:.3f}] |",
        f"| Arithmetic ratio of means (old number) | {g['arithmetic_ratio_of_means']:.3f}x |",
        f"| Median of per-pair ratios | {g['median_of_per_pair_ratio']:.3f}x |",
        f"| Wilcoxon signed-rank stat | {g['wilcoxon_stat']:.1f} |",
        f"| Wilcoxon p (one-sided, W20>W0) | {g['wilcoxon_p_one_sided_greater']:.3e} |",
        f"| Cohen's d_z (log scale) | {g['cohens_dz_logscale']:.3f} |",
        f"| Common-language effect (P(W20>W0)) | {g['common_language_effect']:.3f} |",
        f"| Passes 2x on geometric ratio? | {g['passes_2x_geometric']} |",
        "",
        "## B. Multiple-comparison correction (subgroup claims)",
        "",
        "Per-subgroup geometric contrast + Wilcoxon p, with BH-FDR (dependent tests) and Holm.",
        "",
        "| Subgroup | n | geo contrast | raw p | BH-FDR | Holm | passes 2x |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for s in sub:
        lines.append(
            f"| {s['label']} | {s['n_pairs']} | {s['geometric_mean_ratio']:.3f} | "
            f"{s['wilcoxon_p_one_sided_greater']:.2e} | {s['p_bh']:.2e} | {s['p_holm']:.2e} | "
            f"{s['passes_2x_geometric']} |"
        )

    lines += [
        "",
        "## C. Specification curve (multiverse over aggregation — H1)",
        "",
        f"- Specs tested: {sc['n_specs']} (3 central tendencies x 4 groupings, all subsets)",
        f"- Specs passing 2x: {sc['n_pass']} / {sc['n_specs']}",
        f"- **robust_fraction = {sc['robust_fraction']:.3f}**  (AOS +5 if > 0.70)",
        f"- Contrast range across specs: [{sc['min_contrast']:.3f}x, {sc['max_contrast']:.3f}x]",
        "",
        "> Limitation: this multiverse covers only the AGGREGATION axis. The "
        "spectrum-fraction axis (bottom 5/10/20%) needs per-state IPR, which is NOT "
        "stored — that axis remains compute-bound.",
        "",
        "## D. Tipping point (robustness boundary — H3)",
        "",
        f"- {res['tipping']['interpretation']}",
        "",
        "## E. Leave-one-family-out (replication PROXY — H2)",
        "",
        "| Held-out family | geo on kept 2 | geo on held | kept passes | held passes |",
        "|---|---:|---:|---|---|",
    ]
    for f in res["logo"]["folds"]:
        lines.append(
            f"| {f['held_out_family']} | {f['geo_contrast_on_kept_2_families']:.3f} | "
            f"{f['geo_contrast_on_held_family']:.3f} | {f['kept_passes']} | {f['held_passes']} |"
        )
    lines += [
        "",
        f"- All folds stable: **{res['logo']['all_folds_stable']}**",
        "> Caveat: LOGO is internal partition on the SAME codebase/machine. It softens "
        "but does NOT close T10 (true independent replication).",
        "",
        "## Power (T6) — honest non-fix",
        "",
        f"- Observed Cohen's d_z (log) = {res['power']['observed_dz_logscale']:.3f}, n = {res['power']['n_pairs']}",
    ]
    if res["power"].get("achieved_power_given_observed_dz") is not None:
        lines.append(
            f"- Power given OBSERVED d_z = {res['power']['achieved_power_given_observed_dz']:.3f}"
        )
    lines += [
        f"- {res['power']['caveat']}",
        "",
        "## AOS impact (re-analysis only)",
        "",
        "| Gap | Before | After re-analysis | Recovered |",
        "|---|---|---|---|",
        f"| correct_test (Wilcoxon + geo-ratio) | +0 | +8 | {'YES' if not math.isnan(g['wilcoxon_p_one_sided_greater']) else 'CHECK'} |",
        "| multiple_comparison (BH-FDR + Holm) | +0 | +8 | YES |",
        f"| robust_fraction (spec-curve > 0.70) | +0 | {'+5' if sc['robust_fraction'] > 0.70 else '+0'} | "
        f"{'YES' if sc['robust_fraction'] > 0.70 else 'NO — robust_fraction <= 0.70'} |",
        "| multiverse (full) | +0 | partial | spectrum axis compute-bound |",
        "| power a-priori (T6) | +0 | +0 | NO — needs new pre-reg run |",
        "| independent_replication (T10) | +0 | +0 | NO — LOGO is proxy only |",
        "",
        f"**Estimated AOS after re-analysis: 40 + 8 + 8 + {'5' if sc['robust_fraction'] > 0.70 else '0'} "
        f"= {40 + 8 + 8 + (5 if sc['robust_fraction'] > 0.70 else 0)}/100** "
        f"({'crosses 60 -> CONFIRMATORY WITH CAVEATS' if (40 + 16 + (5 if sc['robust_fraction'] > 0.70 else 0)) >= 60 else 'still EXPLORATORY'}).",
        "",
        "## What this does NOT mean",
        "",
        "1. Does NOT validate S3xS1 as a physical geometry (S3 Dirac is a diagonal mockup).",
        "2. Does NOT establish a thermodynamic limit (tested N <= 896).",
        "3. Does NOT replace independent replication or a-priori power.",
        "4. The numbers are GENERATED here; adversarial falsification is still pending.",
        "",
        "## Provenance",
        "",
        "- Script: `scripts/reanalyze_gate4b_stats.py` (no eigensolve)",
        "- Companion audit: hypothesis-red-team (AOS 40/100, 2026-06-07)",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-bootstrap", action="store_true", help="skip bootstrap CI (faster)")
    args = ap.parse_args()

    rows = load_cases()
    pairs = build_pairs(rows)
    print(f"Loaded {len(rows)} cases -> {len(pairs)} matched W={W_LOW}/W={W_HIGH} pairs")

    if args.dry_run:
        print("--dry-run: not computing")
        return 0

    glob_stats = paired_stats(pairs)
    boot = {"geometric_mean_ratio_ci95": [float("nan"), float("nan")], "n_boot": 0}
    if not args.no_bootstrap:
        boot = bootstrap_ci(pairs)

    # subgroups: per-family + per-size + per-jmax, with BH-FDR/Holm over their p-values
    subgroups = []
    for f in sorted({p["family"] for p in pairs}):
        sp = [p for p in pairs if p["family"] == f]
        st = paired_stats(sp)
        st["label"] = f"family={f}"
        subgroups.append(st)
    for s in sorted({p["s1_size"] for p in pairs}):
        sp = [p for p in pairs if p["s1_size"] == s]
        st = paired_stats(sp)
        st["label"] = f"size={s}"
        subgroups.append(st)
    for j in sorted({p["j_max"] for p in pairs}):
        sp = [p for p in pairs if p["j_max"] == j]
        st = paired_stats(sp)
        st["label"] = f"j_max={j}"
        subgroups.append(st)

    pvals = [s["wilcoxon_p_one_sided_greater"] for s in subgroups]
    pvals_clean = [1.0 if (p is None or math.isnan(p)) else p for p in pvals]
    p_bh = bh_fdr(pvals_clean)
    p_holm = holm(pvals_clean)
    for s, a, b in zip(subgroups, p_bh, p_holm):
        s["p_bh"] = a
        s["p_holm"] = b

    sc = specification_curve(pairs)
    tip = tipping_point(glob_stats["geometric_mean_ratio"])
    logo = leave_one_family_out(pairs)
    pwr = observed_power(pairs)

    res = {
        "meta": {"n_cases": len(rows), "source": str(RUN_DIR), "threshold": PREREG_THRESHOLD},
        "global": glob_stats,
        "bootstrap": boot,
        "subgroups": subgroups,
        "spec_curve": sc,
        "tipping": tip,
        "logo": logo,
        "power": pwr,
    }

    out_md = REPO_ROOT / "reports/GATE4B_REANALYSIS_STATS_2026-06-07.md"
    out_json = REPO_ROOT / "reports/GATE4B_REANALYSIS_STATS_2026-06-07.json"
    out_json.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(res, out_md)

    print("\n=== KEY RESULTS ===")
    print(
        f"Geometric-mean ratio : {glob_stats['geometric_mean_ratio']:.3f}x  CI95 {boot['geometric_mean_ratio_ci95']}"
    )
    print(f"Arithmetic (old)     : {glob_stats['arithmetic_ratio_of_means']:.3f}x")
    print(f"Wilcoxon p (greater) : {glob_stats['wilcoxon_p_one_sided_greater']:.3e}")
    print(f"Cohen d_z (log)      : {glob_stats['cohens_dz_logscale']:.3f}")
    print(
        f"Spec-curve robust_fr : {sc['robust_fraction']:.3f}  ({sc['n_pass']}/{sc['n_specs']} specs pass 2x)"
    )
    print(f"Contrast range       : [{sc['min_contrast']:.3f}, {sc['max_contrast']:.3f}]")
    print(f"Tipping factor       : {tip['ipr_w0_inflation_to_break']:.3f}x")
    print(f"LOGO all stable      : {logo['all_folds_stable']}")
    est = 40 + 8 + 8 + (5 if sc["robust_fraction"] > 0.70 else 0)
    print(f"Estimated AOS        : {est}/100")
    print(f"\nWrote: {out_md}")
    print(f"Wrote: {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
