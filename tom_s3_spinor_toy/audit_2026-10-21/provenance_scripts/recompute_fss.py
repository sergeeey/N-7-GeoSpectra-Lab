import json, glob, math, sys
from collections import defaultdict
base = sys.argv[1]
recs = []
for f in sorted(glob.glob(base + "/batches/batch_*/results.json")):
    recs.extend(json.load(open(f, encoding="utf-8")))
print("records:", len(recs))
print("ipr versions:", sorted({r.get("ipr_metric_version") for r in recs}, key=str))
print("errors:", sum(1 for r in recs if r.get("error")))
def cell(fam, W, j):
    d = defaultdict(dict)
    for r in recs:
        if r["family"] == fam and r["disorder_strength"] == W and r["j_max"] == j:
            d[r["s1_size"]][r["seed"]] = r["true_ipr_mean"]
    return d
def ols(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    sxx = sum((x-mx)**2 for x in xs); sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    b = sxy/sxx; a = my - b*mx
    rss = sum((y-(a+b*x))**2 for x, y in zip(xs, ys)); syy = sum((y-my)**2 for y in ys)
    se = math.sqrt(rss/(n-2)/sxx) if n > 2 else float("nan")
    return b, se, 1-rss/syy
for fam in ["spectral_circle", "ring"]:
    for j in [2, 3]:
        d = cell(fam, 20, j)
        sizes = sorted(d)
        means = {n: sum(d[n].values())/len(d[n]) for n in sizes}
        print(f"\n{fam} W=20 jmax={j} sizes={sizes} seeds_per_size={[len(d[n]) for n in sizes]}")
        print("  mean IPR:", {n: round(means[n], 4) for n in sizes})
        for sub in [sizes, [n for n in sizes if n in (16, 64, 128)]]:
            if len(sub) >= 3:
                b, se, r2 = ols([math.log(n) for n in sub], [math.log(means[n]) for n in sub])
                print(f"  sizes {sub}: slope={b:.4f} se={se:.4f} R2={r2:.4f}")
