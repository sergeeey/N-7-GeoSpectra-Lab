r"""
C152 STEP 1 -- elementary root/weight path enumeration for Term2, on BOTH
nearly-Kahler spaces, in ONE common language. This is the H1 test.

THE COMMON LANGUAGE, and why it is genuinely common (not a re-labelling)
  t^2 subset su(3) subset g_2. The SAME rank-2 torus sits inside the isotropy
  of BOTH spaces: it IS the isotropy of SU(3)/T^2, and it is the maximal
  torus of S^6's isotropy SU(3). So T^2-weights are a uniform coordinate on
  both, and a (Sigma_odd (x) W)^{T^2} sector exists on both. On S^6 the
  su(3)-invariant sector C139/C145/C147 actually use is a SUBSPACE of the
  T^2-invariant one measured here -- so a nonzero value on the smaller space
  implies the T^2-sector is nonzero too, and the comparison is valid in the
  direction it is used.

  Cartan basis, fixed once: H1 = i*diag(1,-1,0), H2 = i*diag(0,1,-1).
  Defining rep 3 has weights w(e_k) = ((h1)_k, (h2)_k).

  m for SU(3)/T^2  = root spaces         (adjoint type)
  m for S^6        = 3 (+) 3bar          (fundamental type)   <- the structural difference
  Sigma            = Lambda^bullet V     in BOTH cases, V = the (1,0) space of J_NK

WHAT A "PATH" IS
  Term2 = sum_i e_i (x) Lambda(e_i) shifts BOTH factors. Equivariance forces
  the two shifts to be opposite: a domain invariant (sigma, -sigma) can only
  reach a target invariant (sigma', -sigma') if

        delta := sigma' - sigma   is a weight of m (x) C,

  because the Clifford factor e_i carries a weight of m and the Nomizu factor
  Lambda(e_i) carries the opposite one. Enumerating admissible delta is
  therefore exactly the H1 test:

        NO admissible path anywhere  ->  H1 (zero is representation-forced)
        paths exist                  ->  H1 REFUTED; go to H2/H3

DISCLOSURE: per PREREGISTRATION.md, this particular enumeration was carried
out by hand before being scripted. It is a deterministic finite integer
computation with no free parameters; the script is authoritative and must
reproduce the hand result.

Run:  python c152_step1_paths.py
"""

from itertools import combinations

Weight = tuple[int, int]

H1 = (1, -1, 0)
H2 = (0, 1, -1)
FUND = [(H1[k], H2[k]) for k in range(3)]  # weights of the defining rep 3


def add(*ws: Weight) -> Weight:
    return (sum(w[0] for w in ws), sum(w[1] for w in ws))


def neg(w: Weight) -> Weight:
    return (-w[0], -w[1])


def sigma_from_V(V: list[Weight]) -> tuple[list[Weight], list[Weight]]:
    """Sigma = Lambda^bullet V, split into even and odd parts."""
    lam = {
        0: [(0, 0)],
        1: list(V),
        2: [add(V[i], V[j]) for i, j in combinations(range(3), 2)],
        3: [add(*V)],
    }
    return lam[0] + lam[2], lam[1] + lam[3]


def analyse(name: str, V: list[Weight], W: list[Weight]) -> dict:
    sig_even, sig_odd = sigma_from_V(V)
    Wset = set(W)
    dom = [s for s in sig_odd if neg(s) in Wset]
    tgt = [s for s in sig_even if neg(s) in Wset]

    print()
    print("=" * 78)
    print(f"  {name}")
    print("=" * 78)
    print(f"  V = (1,0) space of J_NK   : {V}")
    print(f"  m (x) C weights           : {W}")
    print(f"  Sigma_even weights        : {sig_even}")
    print(f"  Sigma_odd  weights        : {sig_odd}")
    print(f"  domain  (Sigma_odd  (x) W)^T2 : dim {len(dom)}  at Sigma-weights {dom}")
    print(f"  target  (Sigma_even (x) W)^T2 : dim {len(tgt)}  at Sigma-weights {tgt}")

    # ---- Term1 test (control: we already know the answer, it must reproduce)
    overlap = [s for s in dom if s in set(sig_even)]
    print()
    print(f"  [Term1] shared weight domain n Sigma_even : {overlap if overlap else 'EMPTY'}")
    print(f"  [Term1] verdict : {'not forced' if overlap else 'FORCED ZERO by weights alone'}")

    # ---- Term2 path enumeration (the H1 test)
    paths = []
    for s in dom:
        for sp_ in tgt:
            d = add(sp_, neg(s))
            if d in Wset:
                paths.append((s, sp_, d))
    print()
    print("  [Term2] admissible paths (sigma -> sigma', delta = sigma'-sigma in m):")
    if not paths:
        print("           NONE")
    for s, sp_, d in paths:
        print(f"           {s} -> {sp_}   delta = {d}")
    per_dom = {s: sum(1 for p in paths if p[0] == s) for s in dom}
    print(f"  [Term2] total paths = {len(paths)}   per domain vector = {per_dom}")
    print(
        f"  [Term2] H1 verdict : "
        f"{'H1 HOLDS -- no path, zero is weight-forced' if not paths else 'H1 REFUTED -- paths exist'}"
    )
    return {"dom": dom, "tgt": tgt, "paths": paths, "n_paths": len(paths)}


# ---------------------------------------------------------------------------
# SU(3)/T^2 : m = root spaces.  J_NK = eps (-1,1,-1), pinned in C151 Stage 1a.
# ---------------------------------------------------------------------------
ROOTS = [
    add(FUND[0], neg(FUND[1])),  # E_12
    add(FUND[0], neg(FUND[2])),  # E_13
    add(FUND[1], neg(FUND[2])),  # E_23
]
assert ROOTS == [(2, -1), (1, 1), (-1, 2)], f"root convention drifted: {ROOTS}"
EPS_NK = (-1, 1, -1)
V_FLAG = [r if e > 0 else neg(r) for e, r in zip(EPS_NK, ROOTS)]
W_FLAG = ROOTS + [neg(r) for r in ROOTS]
flag = analyse("SU(3)/T^2   (m = root spaces, ADJOINT type)", V_FLAG, W_FLAG)

# ---------------------------------------------------------------------------
# S^6 = G2/SU(3) : m = 3 (+) 3bar.  V = 3 (the (1,0) space of the NK J).
# ---------------------------------------------------------------------------
V_S6 = list(FUND)
W_S6 = list(FUND) + [neg(w) for w in FUND]
s6 = analyse("S^6 = G2/SU(3)   (m = 3 (+) 3bar, FUNDAMENTAL type)", V_S6, W_S6)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 1 CONCLUSION")
print("=" * 78)
print(f"  admissible Term2 paths : SU(3)/T^2 = {flag['n_paths']}   S^6 = {s6['n_paths']}")
if flag["n_paths"] == 0:
    print("  -> H1 CONFIRMED on SU(3)/T^2: the zero needs no geometry at all.")
else:
    print("  -> H1 REFUTED on SU(3)/T^2: admissible paths exist, so the zero is")
    print("     NOT a pure weight selection rule. The coefficients along those")
    print("     paths must cancel -> H2 or H3. Step 2 computes them; Step 3's")
    print("     perturbation control decides between representation and geometry.")
if flag["n_paths"] == s6["n_paths"] and flag["n_paths"] > 0:
    print()
    print("  NOTE: the two spaces have the SAME number of admissible paths")
    print(f"  ({flag['n_paths']} each, {flag['n_paths'] // len(flag['dom'])} per domain vector), despite m being")
    print("  adjoint-type on one and fundamental-type on the other. So the path")
    print("  COUNT does not discriminate them -- whatever separates S^6 from")
    print("  SU(3)/T^2 lives in the COEFFICIENTS, not in the weight combinatorics.")
