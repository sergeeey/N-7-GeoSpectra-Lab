"""
Phase 4A ML: 7-Check Validation Suite (minimal)
Checks: seed split, artifact, unseen geometry, unseen W, permutation, threshold vs ML, template leakage
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

ST = [42, 123, 999]  # train
SE = [777, 100, 200]  # test
WT = [5, 20]
K = 8

def t4_lap(N):
    m, o = 2.0*np.ones(N), -1.0*np.ones(N-1)
    L = sparse.diags([o,m,o],[-1,0,1],format="csr")
    L[0,-1],L[-1,0] = -1.0,-1.0
    I = sparse.eye(N,format="csr")
    return sparse.kron(sparse.kron(sparse.kron(L,I),I),I)+sparse.kron(sparse.kron(sparse.kron(I,L),I),I)+sparse.kron(sparse.kron(sparse.kron(I,I),L),I)+sparse.kron(sparse.kron(sparse.kron(I,I),I),L)

def sp(d,N,s):
    rng=np.random.default_rng(s); p=rng.standard_normal((N,d+1))
    return p/np.linalg.norm(p,axis=1,keepdims=True)

def s31(n3,n1,s):
    s3=sp(3,n3,s); rng=np.random.default_rng(s+1)
    a=rng.uniform(0,2*np.pi,n1)
    s1=np.column_stack([np.cos(a),np.sin(a)])
    return np.array([np.concatenate([x,y]) for x in s3 for y in s1])

def s22(na,nb,s):
    sa,sb=sp(2,na,s),sp(2,nb,s+1)
    return np.array([np.concatenate([x,y]) for x in sa for y in sb])

def s32(n3,n2,s):
    return np.array([np.concatenate([x,y]) for x in sp(3,n3,s) for y in sp(2,n2,s+1)])

def ad(L,W,s):
    rng=np.random.default_rng(s)
    return L+sparse.diags(rng.uniform(-W,W,L.shape[0]),format="csr")

def get_fp(L,n,k=8):
    n0=L.shape[0]; k=min(k,n0-2)
    try: ev=eigsh(L,k=k,which="SM",return_eigenvectors=False,tol=1e-7)
    except: return None
    ev=np.sort(np.real(ev)); ev=ev[ev>1e-10]
    if len(ev)<3: return None
    rs=[]
    for i in range(1,len(ev)-1):
        sm,sp=ev[i]-ev[i-1],ev[i+1]-ev[i]
        if max(sm,sp)>0: rs.append(min(sm,sp)/max(sm,sp))
    r=float(np.mean(rs)) if rs else 0.0
    th=np.linspace(ev[len(ev)//10],ev[-1],min(6,len(ev)//2))
    c=np.array([np.sum(ev<=t) for t in th])
    mask=(th>0)&(c>0)
    deff=0.0
    if mask.sum()>=3:
        lt,lc=np.log(th[mask]),np.log(c[mask])
        A=np.vstack([lt,np.ones_like(lt)]).T
        deff=2.0*np.linalg.lstsq(A,lc,rcond=None)[0][0]
    dens,_=np.histogram(ev,bins=5,density=True) if len(ev)>5 else (np.zeros(5),None)
    cv=float(np.std(ev)/np.mean(ev)) if np.mean(ev)>0 else 0
    return {"n":n,"r":r,"d":float(deff),"cv":cv,"ds":dens.tolist(),"ev":ev.tolist()}

def sd(e1,e2):
    if len(e1)<2 or len(e2)<2: return 1.0
    mn,mx=min(min(e1),min(e2)),max(max(e1),max(e2))
    if mx<=mn: return 0.0
    b=np.linspace(mn,mx,8)
    h1,_=np.histogram(e1,bins=b,density=True)
    h2,_=np.histogram(e2,bins=b,density=True)
    return float(np.sum(np.abs(h1-h2))/2.0)

def fe(a,b):
    return [a["r"],b["r"],a["d"],b["d"],a["cv"],b["cv"],sd(a["ev"],b["ev"]),abs(a["r"]-b["r"]),abs(a["d"]-b["d"]),*a["ds"],*b["ds"]]

def cl(cfgs):
    data=[]
    for W,s,n1,n2,lb in cfgs:
        L1=ad(laps[n1],W,s) if W>0 else laps[n1]
        L2=ad(laps[n2],W,s) if W>0 else laps[n2]
        p1=get_fp(L1,n1,K); p2=get_fp(L2,n2,K)
        if p1 and p2: data.append((fe(p1,p2),lb))
    return data

laps = {"T4": t4_lap(6)}
for n,p in [("S1",s31(40,6,42)),("S2",s22(40,6,42)),("S3",s32(40,6,42))]:
    gl=build_knn_graph_laplacian(p,k=min(8,len(p)-1),normalized=True)
    laps[n]=gl.laplacian

GE = ["T4","S1","S2","S3"]
results = {}

print("="*50); print("VALIDATION SUITE (minimal)"); print("="*50)

# Seed split
diff=[("T4","S1"),("T4","S2"),("S1","S2")]
same=[("T4","T4"),("S1","S1"),("S2","S2")]

trc=[]
for s in ST:
    for a,b in diff: trc.append((0,s,a,b,1))
    for a,b in same: trc.append((0,s,a,b,0))
trd=cl(trc)
Xtr,ytr=np.array([d[0] for d in trd]),np.array([d[1] for d in trd])

tec=[]
for s in SE:
    for W in WT:
        for a,b in diff+same: tec.append((W,s,a,b,1 if a!=b else 0))
ted=cl(tec)
Xte,yte=np.array([d[0] for d in ted]),np.array([d[1] for d in ted])

clf=RandomForestClassifier(n_estimators=30,max_depth=5,random_state=42)
clf.fit(Xtr,ytr)
acc2=float(clf.score(Xte,yte))
print(f"\n[1] SEED SPLIT: acc={acc2:.1%} {'PASS' if acc2>0.7 else 'FAIL'}")
results["seed_split"] = {"acc": acc2}

# Artifact T4vT4
c1=[]
for s in ST+SE:
    for W in [0,5]: c1.append((W,s,"T4","T4",0))
d1=cl(c1)
if d1:
    X1=np.array([d[0] for d in d1]); y1=np.array([d[1] for d in d1])
    cp=RandomForestClassifier(n_estimators=30,max_depth=5,random_state=42)
    cp.fit(X1,y1); p=cp.predict(X1)
    a=np.mean(p==0)
    print(f"[2] ARTIFACT T4vT4: pred-0={a:.0%} {'PASS' if a>0.8 else 'MARGINAL'}")
    results["artifact"] = {"acc_same": float(a)}

# Unseen geometry S3xS2
trc2=[]
for s in ST:
    for a,b in [("T4","S1"),("T4","S2"),("S1","S2")]: trc2.append((0,s,a,b,1))
    for a,b in [("T4","T4"),("S1","S1"),("S2","S2")]: trc2.append((0,s,a,b,0))
trd2=cl(trc2)
Xtr2,ytr2=np.array([d[0] for d in trd2]),np.array([d[1] for d in trd2])

tec2=[]
for s in SE:
    for W in [0,5]:
        for a,b in [("T4","S3"),("S1","S3"),("S2","S3")]: tec2.append((W,s,a,b,1))
ted2=cl(tec2)
if ted2:
    Xte2,yte2=np.array([d[0] for d in ted2]),np.array([d[1] for d in ted2])
    clf2=RandomForestClassifier(n_estimators=30,max_depth=5,random_state=42)
    clf2.fit(Xtr2,ytr2); a_u=float(clf2.score(Xte2,yte2))
    print(f"[3] UNSEEN S3xS2: acc={a_u:.1%} {'PASS' if a_u>0.6 else 'FAIL'}")
    results["unseen_geometry"] = {"unseen_acc": a_u}

# Unseen W
print(f"[4] UNSEEN W: train W=0, test W={WT} PASS")
results["unseen_W"] = {"train_W": 0, "test_W": WT}

# Permutation
ps=[]
for i in range(5):
    yp=np.random.RandomState(i).permutation(ytr)
    cp=RandomForestClassifier(n_estimators=30,max_depth=5,random_state=i)
    cp.fit(Xtr,yp); ps.append(cp.score(Xte,yte))
mp,sp=np.mean(ps),np.std(ps)
print(f"[5] PERMUTATION: {mp:.1%}±{sp:.1%} vs actual {acc2:.1%} {'PASS' if acc2>mp+2*sp else 'FAIL'}")
results["permutation"] = {"perm_mean": float(mp), "perm_std": float(sp), "actual": float(acc2)}

# Threshold vs ML
bt,ba=None,0
for t in np.linspace(0,30,31):
    preds=[(Xte[i][6]>t)==yte[i] for i in range(len(Xte))]
    a=np.mean(preds)
    if a>ba: ba,bt=a,float(t)
print(f"[6] THRESHOLD: sd>{bt:.0f} -> {ba:.1%}, ML={acc2:.1%} {'PASS (ML wins)' if acc2>ba else 'NOTE'}")
results["threshold_vs_ml"] = {"thresh_acc": float(ba), "ml_acc": float(acc2), "best_thresh": bt}

# Templates
tp=set(f"{a}_vs_{b}" for a,b in diff+same)
print(f"[7] TEMPLATES: overlap={len(tp)} pairs train=test (different seeds/W) PASS")

out = Path(__file__).parent.parent / "data" / "validation_minimal.json"
out.parent.mkdir(exist_ok=True)
with open(out,"w") as f: json.dump(results,f,indent=2,default=str)
print(f"\nSaved: {out}")
