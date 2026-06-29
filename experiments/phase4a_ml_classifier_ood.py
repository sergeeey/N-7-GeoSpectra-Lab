"""
Phase 4A ML: Train on Clean (W=0), Test OOD (W>0)
FIXED: per-W accuracy computed from actual data, not configs
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

W_TRAIN = [0]
W_TEST = [1, 5, 10, 20]
SEEDS = [42, 123, 999, 777, 100, 200, 300, 400, 500, 600]
K_EIG = 15

def t4_lap(N):
    m, o = 2.0*np.ones(N), -1.0*np.ones(N-1)
    L = sparse.diags([o,m,o],[-1,0,1],format="csr")
    L[0,-1],L[-1,0] = -1.0,-1.0
    I = sparse.eye(N,format="csr")
    return sparse.kron(sparse.kron(sparse.kron(L,I),I),I)+sparse.kron(sparse.kron(sparse.kron(I,L),I),I)+sparse.kron(sparse.kron(sparse.kron(I,I),L),I)+sparse.kron(sparse.kron(sparse.kron(I,I),I),L)

def sphere(dim,N,seed):
    rng=np.random.default_rng(seed)
    p=rng.standard_normal((N,dim+1))
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

PAIRS = [("T4","S3xS1",1),("T4","S2xS2",1),("S3xS1","S2xS2",1),("T4","T4",0),("S3xS1","S3xS1",0),("S2xS2","S2xS2",0)]

def collect_data(seed_list, W_list):
    """Collect (features, label, W) for given seeds and W values."""
    data = []
    for s in seed_list:
        for W in W_list:
            for n1,n2,lb in PAIRS:
                L1 = ad(laps[n1], W, s) if W > 0 else laps[n1]
                L2 = ad(laps[n2], W, s) if W > 0 else laps[n2]
                fp1 = get_fp(L1, n1, K_EIG)
                fp2 = get_fp(L2, n2, K_EIG)
                if fp1 and fp2:
                    data.append((fe(fp1, fp2), lb, W, f"{n1}_vs_{n2}"))
    return data

# Train
train_data = collect_data(SEEDS, W_TRAIN)
Xtr = np.array([d[0] for d in train_data])
ytr = np.array([d[1] for d in train_data])

# Test
test_data = collect_data(SEEDS, W_TEST)
Xte = np.array([d[0] for d in test_data])
yte = np.array([d[1] for d in test_data])
test_W = [d[2] for d in test_data]

clf = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
clf.fit(Xtr, ytr)

print("="*50)
print("PHASE 4A ML: CLASSIFIER + OOD (FIXED)")
print("="*50)
print(f"Train: {len(Xtr)} samples")
print(f"Test:  {len(Xte)} samples")

print(f"\nOOD Results:")
print(f"  {'W':>5} | {'Acc':>8} | {'N':>4}")
for W in W_TEST:
    idx = [i for i in range(len(test_data)) if test_W[i] == W]
    if idx:
        acc = clf.score(Xte[idx], yte[idx])
        print(f"  {W:5.1f} | {acc:7.1%} | {len(idx):4}")

# Feature importance
fi = clf.feature_importances_
fn = ["r1","r2","deff1","deff2","cv1","cv2","sd_dist","r_spread","deff_spread","cv_spread","d1_1","d1_2","d1_3","d1_4","d1_5","d2_1","d2_2","d2_3","d2_4","d2_5"]
print(f"\nTop 5 features:")
for idx in np.argsort(fi)[::-1][:5]:
    print(f"  {fn[idx]}: {fi[idx]:.3f}")

# Save
summary = {"train_acc": float(clf.score(Xtr, ytr)), "ood": []}
for W in W_TEST:
    idx = [i for i in range(len(test_data)) if test_W[i] == W]
    if idx:
        summary["ood"].append({"W": W, "acc": float(clf.score(Xte[idx], yte[idx])), "n": len(idx)})
summary["feature_importance"] = {fn[i]: float(fi[i]) for i in range(len(fn))}

out = Path(__file__).parent.parent / "data" / "phase4a_ml_ood.json"
out.parent.mkdir(exist_ok=True)
with open(out, "w") as f:
    json.dump(summary, f, indent=2, default=str)
print(f"\nSaved: {out}")
