import json, glob, math, statistics as st
from collections import defaultdict
def load_ext():
    return [dict(fam="spectral_circle", W=r["disorder_strength"], N=r["s1_size"], seed=r["seed"], ipr=r["true_ipr_mean"]) for r in (json.load(open(f,encoding="utf-8")) for f in sorted(glob.glob("reports/RUNS/spectral_circle_extended_v0.1.22/batch_*/case_*.json")))]
def load_v24(fam_want):
    out=[]
    for f in sorted(glob.glob("reports/RUNS/gate4_fss_v0.1.24/batches/batch_*/results.json")):
        for r in json.load(open(f,encoding="utf-8")):
            if r["family"]==fam_want: out.append(dict(fam=r["family"],W=r["disorder_strength"],N=r["s1_size"],seed=r["seed"],ipr=r["true_ipr_mean"],j=r["j_max"]))
    return out
def ols(xs,ys):
    k=len(xs); mx=sum(xs)/k; my=sum(ys)/k
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
def estimators(rows, label):
    rows=[r for r in rows if r["W"]==20 and (r.get("j",3)==3)]
    Ns=sorted({r["N"] for r in rows}); seeds=sorted({r["seed"] for r in rows})
    by=defaultdict(list)
    for r in rows: by[(r["N"],r["seed"])].append(r["ipr"])
    xs=[math.log(n) for n in Ns]
    A=ols(xs,[math.log(st.mean(v for s in seeds for v in by[(n,s)])) for n in Ns])
    B=ols(xs,[st.mean(math.log(v) for s in seeds for v in by[(n,s)]) for n in Ns])
    C=st.mean(ols(xs,[math.log(st.mean(by[(n,s)])) for n in Ns]) for s in seeds)
    med=ols(xs,[math.log(st.median(v for s in seeds for v in by[(n,s)])) for n in Ns])
    print(f"{label} sizes={Ns} seeds={seeds}\n  A log(mean IPR) slope={A:.4f}\n  B mean(log IPR) slope={B:.4f}\n  C avg per-seed slope={C:.4f}\n  D log(median) slope={med:.4f}")
estimators(load_ext(), "v0.1.22 extended, W=20, jmax3 (18 cases)")
estimators(load_v24("spectral_circle"), "v0.1.24 raw spectral_circle, W=20, jmax3 (4 sizes)")
