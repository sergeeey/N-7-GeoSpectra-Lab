import json, glob, math
from collections import defaultdict
recs = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob("reports/RUNS/spectral_circle_extended_v0.1.22/batch_*/case_*.json"))]
print("cases:", len(recs), "| W values:", sorted({r["disorder_strength"] for r in recs}), "| sizes:", sorted({r["s1_size"] for r in recs}), "| seeds:", sorted({r["seed"] for r in recs}), "| jmax:", sorted({r["j_max"] for r in recs}))
for W in sorted({r["disorder_strength"] for r in recs}):
    d = defaultdict(list)
    for r in recs:
        if r["disorder_strength"] == W: d[r["s1_size"]].append(r["true_ipr_mean"])
    sizes = sorted(d); m = {n: sum(d[n])/len(d[n]) for n in sizes}
    xs = [math.log(n) for n in sizes]; ys = [math.log(m[n]) for n in sizes]
    k = len(xs); mx = sum(xs)/k; my = sum(ys)/k
    b = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs)
    print(f"W={W}: mean IPR {({n: round(m[n],4) for n in sizes})} slope(all sizes)={b:.4f}")
