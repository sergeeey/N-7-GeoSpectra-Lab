import json, glob, math, statistics as st
from collections import defaultdict
rows=[(r["s1_size"],r["seed"],r["true_ipr_mean"]) for r in (json.load(open(f,encoding="utf-8")) for f in sorted(glob.glob("reports/RUNS/spectral_circle_extended_v0.1.22/batch_*/case_*.json"))) if r["disorder_strength"]==20]
by=defaultdict(dict)
for n,s,v in rows: by[s][n]=v
Ns=[16,64,128]; xs=[math.log(n) for n in Ns]
def slope(ys):
    mx=sum(xs)/3; my=sum(ys)/3
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
per_seed=[slope([math.log(by[s][n]) for n in Ns]) for s in sorted(by)]
print("per-seed slopes:", [round(b,4) for b in per_seed])
m=st.mean(per_seed); sd=st.stdev(per_seed)
print(f"mean={m:.4f} sd(seeds)={sd:.4f} SE=sd/sqrt(3)={sd/math.sqrt(3):.4f}  (report SE 0.0546)")
