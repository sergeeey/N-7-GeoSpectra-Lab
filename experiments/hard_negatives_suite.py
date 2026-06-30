"""
Hard Negatives Suite v6 — 4 kill-tests for spectral recoverability

Tests designed to verify the model doesn't hallucinate differences.
ML trained on SAME (label=0) + DIFF (label=1) geometry pairs.

1. Same-geometry: T4 vs T4 (diff seeds) -> classified as SAME
2. False positive: same-geometry misclassified as diff -> LOW
3. Curved boundary: S3xS1 vs S2xS2 at W=15,20 -> degrades
4. Feature ablation: without sd_dist -> accuracy drops
"""
import json, sys, warnings
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian

SEEDS = [42, 123, 999, 777, 100]
K = 15
OUT = Path(__file__).parent / "20260629-hard-negatives"
OUT.mkdir(exist_ok=True)

def t4_lap(N):
    m, o = 2.0*np.ones(N), -1.0*np.ones(N-1)
    L = sparse.diags([o,m,o],[-1,0,1],format="csr")
    L[0,-1],L[-1,0] = -1.0,-1.0
    I = sparse.eye(N,format="csr")
    return sparse.kron(sparse.kron(sparse.kron(L,I),I),I)+sparse.kron(sparse.kron(sparse.kron(I,L),I),I)+sparse.kron(sparse.kron(sparse.kron(I,I),L),I)+sparse.kron(sparse.kron(sparse.kron(I,I),I),L)

def sphere(d,N,s):
    rng=np.random.default_rng(s); p=rng.standard_normal((N,d+1))
    return p/np.linalg.norm(p,axis=1,keepdims=True)

def s31(n3,n1,s):
    s3=sphere(3,n3,s); rng=np.random.default_rng(s+1)
    a=rng.uniform(0,2*np.pi,n1)
    s1=np.column_stack([np.cos(a),np.sin(a)])
    return np.array([np.concatenate([x,y]) for x in s3 for y in s1])

def s22(na,nb,s):
    sa,sb=sphere(2,na,s),sphere(2,nb,s+1)
    return np.array([np.concatenate([x,y]) for x in sa for y in sb])

def ad(L,W,s):
    rng=np.random.default_rng(s)
    return L+sparse.diags(rng.uniform(-W,W,L.shape[0]),format="csr")

def get_fp(L,n,k=15):
    n0=L.shape[0]; k=min(k,n0-2)
    try: ev=eigsh(L,k=k,which="SM",return_eigenvectors=False,tol=1e-8)
    except: return None
    ev=np.sort(np.real(ev)); ev=ev[ev>1e-10]
    if len(ev)<3: return None
    rs=[]
    for i in range(1,len(ev)-1):
        sm,sp=ev[i]-ev[i-1],ev[i+1]-ev[i]
        if max(sm,sp)>0: rs.append(min(sm,sp)/max(sm,sp))
    r=float(np.mean(rs)) if rs else 0.0
    th=np.linspace(ev[len(ev)//10],ev[-1],min(12,len(ev)//2))
    c=np.array([np.sum(ev<=t) for t in th])
    mask=(th>0)&(c>0)
    deff=0.0
    if mask.sum()>=4:
        lt,lc=np.log(th[mask]),np.log(c[mask])
        A=np.vstack([lt,np.ones_like(lt)]).T
        deff=2.0*np.linalg.lstsq(A,lc,rcond=None)[0][0]
    dens,_=np.histogram(ev,bins=5,density=True) if len(ev)>5 else (np.zeros(5),None)
    cv=float(np.std(ev)/np.mean(ev)) if np.mean(ev)>0 else 0
    return {"n":n,"r":r,"d":float(deff),"cv":cv,"ds":dens.tolist(),"ev":ev.tolist()}

def sd(e1,e2,nb=15):
    if len(e1)<2 or len(e2)<2: return 1.0
    mn,mx=min(min(e1),min(e2)),max(max(e1),max(e2))
    if mx<=mn: return 0.0
    b=np.linspace(mn,mx,nb+1)
    h1,_=np.histogram(e1,bins=b,density=True)
    h2,_=np.histogram(e2,bins=b,density=True)
    return float(np.sum(np.abs(h1-h2))/2.0)

def fe(a,b):
    return [a["r"],b["r"],a["d"],b["d"],a["cv"],b["cv"],sd(a["ev"],b["ev"]),abs(a["r"]-b["r"]),abs(a["d"]-b["d"]),abs(a["cv"]-b["cv"]),*a["ds"],*b["ds"]]

laps = {"T4": t4_lap(6)}
for n,p in [("S3xS1",s31(50,8,42)),("S2xS2",s22(50,8,42))]:
    gl=build_knn_graph_laplacian(p,k=min(12,len(p)-1),normalized=True)
    laps[n]=gl.laplacian

# SAME (label=0) + DIFF (label=1) pairs
PAIRS_MIX = [
    ("T4","S3xS1",1),("T4","S2xS2",1),("S3xS1","S2xS2",1),
    ("T4","T4",0),("S3xS1","S3xS1",0),("S2xS2","S2xS2",0)
]

def collect(pairs,W_list,seeds,k=15):
    d=[]
    for s in seeds:
        for W in W_list:
            for n1,n2,lb in pairs:
                L1=ad(laps[n1],W,s) if W>0 else laps[n1]
                L2=ad(laps[n2],W,s) if W>0 else laps[n2]
                p1=get_fp(L1,n1,k); p2=get_fp(L2,n2,k)
                if p1 and p2: d.append((fe(p1,p2),lb))
    return d

print("="*60)
print("HARD NEGATIVES SUITE v6")
print("="*60)
res={}

# Train: W=0,5 mix of same+diff
data=collect(PAIRS_MIX,[0,5],SEEDS[:4],K)
X=np.array([x[0] for x in data]); y=np.array([x[1] for x in data])
n=len(X)//2
clf=RandomForestClassifier(30,max_depth=4,random_state=42)
clf.fit(X[:n],y[:n])
print(f"Train: {len(X)} samples, base acc: {clf.score(X[n:],y[n:]):.1%}")

# T1: Same-geometry accuracy
same_test=collect([("T4","T4",0),("S3xS1","S3xS1",0),("S2xS2","S2xS2",0)],[5],SEEDS[4:],K)
if same_test:
    Xs=np.array([x[0] for x in same_test]); ys=np.array([x[1] for x in same_test])
    a_same=clf.score(Xs,ys)
    print(f"[T1] Same-geometry accuracy: {a_same:.1%} {'PASS' if a_same>0.8 else 'FAIL'}")
    res["t1_same_acc"] = {"acc":float(a_same),"v":"PASS" if a_same>0.8 else "FAIL"}

# T2: False positive rate
yp=clf.predict(Xs)
fp_rate=float(np.mean(yp==1))
print(f"[T2] False positive rate: {fp_rate:.1%} {'PASS' if fp_rate<0.3 else 'FAIL'}")
res["t2_fp_rate"] = {"fp_rate":fp_rate,"v":"PASS" if fp_rate<0.3 else "FAIL"}

# T3: Curved boundary
print(f"[T3] Curved boundary (ML):")
boundary=[]
for W in [0,5,10,15,20]:
    d=collect([("S3xS1","S2xS2",1)],[W],SEEDS[:5],K)
    if d:
        Xw=np.array([x[0] for x in d]); yw=np.array([x[1] for x in d])
        acc=clf.score(Xw,yw)
        boundary.append((W,float(acc)))
        print(f"  W={W:2d}: {acc:.1%}")
degrades=any(a<0.75 for W,a in boundary if W>10)
print(f"  Degrades W>10: {degrades} {'PASS' if degrades else 'FAIL'}")
res["t3_curved_boundary"] = {"by_W":{str(W):a for W,a in boundary},"degrades":degrades,"v":"PASS" if degrades else "FAIL"}

# T4: Feature ablation (remove sd_dist = index 6)
X_ab=np.delete(X,6,axis=1)
clf_ab=RandomForestClassifier(30,max_depth=4,random_state=42)
clf_ab.fit(X_ab[:n],y[:n]); a_ab=clf_ab.score(X_ab[n:],y[n:])
a_base=clf.score(X[n:],y[n:])
drop=a_base-a_ab
print(f"[T4] Ablation: full={a_base:.1%} no-sd={a_ab:.1%} drop={drop:.1%} {'PASS' if drop>0.1 else 'FAIL'}")
res["t4_ablation"] = {"full":float(a_base),"no_sd":float(a_ab),"drop":float(drop),"v":"PASS" if drop>0.1 else "FAIL"}

# Summary
print("="*60)
p=sum(1 for r in res.values() if r["v"]=="PASS")
for k,v in res.items():
    s="G" if v["v"]=="PASS" else "R"
    print(f"  [{s}] {k:22s}: {v['v']}")
print(f"  Score: {p}/{len(res)} PASS — {'BULLETPROOF' if p>=3 else 'NEEDS WORK'}")
with open(OUT/"hard_negatives_results.json","w") as f:
    json.dump(res,f,indent=2)
print(f"  Saved: {OUT/'hard_negatives_results.json'}")
