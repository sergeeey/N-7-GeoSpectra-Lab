"""Numeric check: reading C of C229, (U_C(g) f)(xi) = f(g^T xi), equals reading A,
(U_A(g) f)(xi) = f(g^{-1} xi), conjugated by S: (S f)(xi) = f(sigma2 xi).
Claim: U_C(g) = S U_A(g) S for every g in SU(2) and every f.
Also: both are homomorphism/anti-homomorphism? (order of multiplication) -- reported, not assumed.
"""
import numpy as np

rng = np.random.default_rng(5)
s2 = np.array([[0, -1j], [1j, 0]])
P = [np.array([[0,1],[1,0]],complex), s2, np.array([[1,0],[0,-1]],complex)]
def su2():
    x = rng.normal(size=4); x /= np.linalg.norm(x)
    return x[0]*np.eye(2) + 1j*sum(x[k+1]*P[k] for k in range(3))
def rand_f():
    c = rng.normal(size=6) + 1j*rng.normal(size=6)
    return lambda z: c[0]*z[0]**2 + c[1]*z[0]*z[1] + c[2]*z[1]**2 + c[3]*z[0] + c[4]*z[1] + c[5]
UA = lambda g, f: (lambda z: f(np.linalg.inv(g) @ z))
UC = lambda g, f: (lambda z: f(g.T @ z))
S  = lambda f: (lambda z: f(s2 @ z))
passes = fails = 0
def check(name, ok):
    global passes, fails
    passes += ok; fails += (not ok); print(("PASS " if ok else "FAIL ") + name)
w1 = w2 = w3 = 0.0
rel = []
for _ in range(300):
    g, h, f = su2(), su2(), rand_f()
    z = rng.normal(size=2) + 1j*rng.normal(size=2)
    w1 = max(w1, abs(UC(g, f)(z) - S(UA(g, S(f)))(z)))
    w2 = max(w2, np.abs(g.T - s2 @ np.linalg.inv(g) @ s2).max())
    # composition: U(gh) vs U(g)U(h) and U(h)U(g)
    for name, U in (("A", UA), ("C", UC)):
        l = U(g @ h, f)(z); a = U(g, U(h, f))(z); b = U(h, U(g, f))(z)
        rel.append((name, abs(l - a) < 1e-10, abs(l - b) < 1e-10))
check(f"R1 U_C(g) = S U_A(g) S on random quadratic f (worst {w1:.1e})", w1 < 1e-10)
check(f"R2 g^T = sigma2 g^-1 sigma2 (worst {w2:.1e})", w2 < 1e-12)
for name in "AC":
    r = [x for x in rel if x[0] == name]
    print(f"INFO reading {name}: U(gh)=U(g)U(h) in {sum(x[1] for x in r)}/300; U(gh)=U(h)U(g) in {sum(x[2] for x in r)}/300")
# generators: d/dt U(exp(i t sigma_a/2)) at 0 via central difference on f at a point
def gen(U, a, f, z, t=1e-5):
    g = lambda s: np.cos(s/2)*np.eye(2) + 1j*np.sin(s/2)*P[a]
    return (U(g(t), f)(z) - U(g(-t), f)(z)) / (2*t)
wg = 0.0
for a in range(3):
    f = rand_f(); z = rng.normal(size=2) + 1j*rng.normal(size=2)
    wg = max(wg, abs(gen(UC, a, f, z) - gen(UA, a, S(f), s2 @ z)))
check(f"R3 generator of reading C = generator of reading A in S-rotated variables (worst {wg:.1e} < 1e-6)", wg < 1e-6)
print(f"\n{passes} PASS, {fails} FAIL")
print("FAILS: none" if not fails else f"FAILS: {fails}")
