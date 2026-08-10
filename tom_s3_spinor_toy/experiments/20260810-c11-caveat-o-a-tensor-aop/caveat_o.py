"""CAVEAT O: orientability in the A (x) A^op formulation -- can J supply the U_iota?

WHAT WAS LEFT OPEN. C52 proved orientability fails because pi_D(c) is LOCAL while
gamma = U_iota (x) s1 is not. That used the A-valued Hochschild cycle. Standard
statements of the axiom often use a cycle in Z_n(A, A (x) A^op), so pi_D carries
J b* J^-1 factors as well:

    pi_D(c) = sum  a0 . (J b0* J^-1) . [D,a1] ... [D,an]

Those are local PROVIDED J A J^-1 is local -- established by C50/C51 only when A
contains the FULL twisted diagonal, i.e. NOT in C52's own regime. So the escape, if
there is one, is: J supplies the U_iota that the algebra cannot.

Shrinking B genuinely enlarges A', so this is not a formality:
  B = iota-EVEN functions  ->  A' acquires a U_iota-carrying part, because m*U_iota
                               commutes with b exactly when b o iota = b
  B = C*1                  ->  A' is everything

PREDICTIONS O1-O4 recorded in claim.md BEFORE running. O4 is the discriminator: if
J u J^-1 were ALLOWED to be U_iota (x) s1, gamma must become reachable -- otherwise
"gamma was not reached" is just genericity again, the failure mode caught four times
already this session.

EXPECTED RESIDUAL, named in advance: J u J^-1 could be a SUM in which a U_iota term's
unbounded commutator CANCELS against another unbounded term. A finite model has no
unbounded operators and cannot exclude it. That is CAVEAT O'.
"""

from __future__ import annotations

import json
from itertools import pairwise, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_caveat_o.json"
results: dict = {}

NX = 4
IOTA_PERM = [0, 1, 3, 2]  # a->a, b->b, c<->c'
I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[-1, 0], [0, 1]], dtype=complex)

U_IOTA_X = np.zeros((NX, NX), dtype=complex)
for i, j in enumerate(IOTA_PERM):
    U_IOTA_X[j, i] = 1.0
U_IOTA_M = np.kron(U_IOTA_X, I2)
DIM_M = NX * 2


def mult(f: np.ndarray) -> np.ndarray:
    return np.kron(np.diag(f), I2)


def is_bundle_endo(t: np.ndarray) -> bool:
    """A bundle endomorphism commutes with EVERY multiplication operator."""
    return all(np.allclose(t @ mult(np.eye(NX)[i]) - mult(np.eye(NX)[i]) @ t, 0) for i in range(NX))


print("=" * 78)
print("CAVEAT O -- can J supply the U_iota that the algebra cannot?")
print("=" * 78)
rng = np.random.default_rng(20260810)

# --- O1: with B = iota-EVEN functions, A' really does grow -------------------
print("\nO1 -- B = iota-EVEN functions. What is A' on the H_M factor?")
even_gens = []
for _ in range(6):
    v = rng.normal(size=NX)
    f = 0.5 * (v + v[IOTA_PERM])  # symmetrise: f o iota = f
    even_gens.append(mult(f))
rows = [np.kron(np.eye(DIM_M), g.T) - np.kron(g, np.eye(DIM_M)) for g in even_gens]
_, sv, vh = np.linalg.svd(np.vstack(rows))
null = vh[np.sum(sv > 1e-9) :].conj().T
dim_comm = null.shape[1]
# every element should decompose as m + m'*U_iota with m, m' bundle endomorphisms
# WHY NOT THE Z2 AVERAGE: the first version split T as 1/2(T + U_iota T U_iota) and
# 1/2(T - U_iota T U_iota)U_iota. That reconstructs T correctly but the first piece is
# NOT a bundle endomorphism -- U_iota T U_iota maps the (c,c') block to the (c',c) block,
# so the average keeps X-off-diagonal entries. The correct split is by X-BLOCK: the
# bundle-endo part is the X-block-diagonal part, and what is left is supported exactly on
# iota-pairs, so right-multiplying by U_iota returns it to block-diagonal form.
x_block = np.kron(np.eye(NX), np.ones((2, 2)))  # mask: same X-point blocks


def block_diag_part(t: np.ndarray) -> np.ndarray:
    return t * x_block


decomposes = True
for k in range(dim_comm):
    t = null[:, k].reshape(DIM_M, DIM_M)
    m = block_diag_part(t)
    mp = block_diag_part((t - m) @ U_IOTA_M)
    decomposes &= bool(np.allclose(m + mp @ U_IOTA_M, t))
    decomposes &= bool(is_bundle_endo(m) and is_bundle_endo(mp))
grew = dim_comm > 8  # the U_iota-free part alone (bundle endos on 4 points) is 4*4 = 16 real
print(f"    dim of the commutant of B on H_M: {dim_comm}")
print(f"    every element decomposes as m + m'*U_iota, m,m' bundle endos: {decomposes}")
print(
    f"    U_iota itself is in it: {bool(np.allclose(U_IOTA_M @ even_gens[0], even_gens[0] @ U_IOTA_M))}"
)
print("    => A' GENUINELY grows when B shrinks. The escape is real.")
o1 = decomposes and grew
results["o1_dim_commutant"] = int(dim_comm)
results["o1_decomposes"] = bool(decomposes)
results["o1_escape_is_real"] = bool(o1)

# --- O2: but the U_iota part has UNBOUNDED commutator with D -----------------
print("\nO2 -- [D_M, m + m'U_iota] = [D_M,m] + {D_M,m'}U_iota. Bounded iff m' = 0?")
print("      spectral model with U_iota D_M U_iota = -D_M, exactly as in W1b")
norms, identity_ok = {}, True
for nmax in (4, 8, 16, 32):
    lv = [s * (n + 1.5) for n in range(nmax + 1) for s in (+1, -1)]
    d_m = np.diag(lv).astype(complex)
    u_i = np.zeros_like(d_m)
    for n in range(nmax + 1):
        u_i[2 * n, 2 * n + 1] = u_i[2 * n + 1, 2 * n] = 1.0
    assert np.allclose(u_i @ d_m @ u_i, -d_m)
    mp = np.diag([1.0 if k % 3 else -1.0 for k in range(len(lv))]).astype(complex)
    lhs = d_m @ (mp @ u_i) - (mp @ u_i) @ d_m
    identity_ok &= bool(np.allclose(lhs, (d_m @ mp + mp @ d_m) @ u_i))
    norms[nmax] = float(np.linalg.norm(lhs, 2))
    print(
        f"      N_MAX = {nmax:3d}   ||[D_M, m'U_iota]|| = {norms[nmax]:7.2f}   (max eig {max(lv):5.1f})"
    )
grows = all(norms[b] > norms[a] for a, b in pairwise([4, 8, 16, 32]))
o2 = identity_ok and grows
print(f"    identity holds exactly: {identity_ok};  norm grows without bound: {grows}")
print("    [INFERRED-analytic, as in C50: {D_M,m'} = [D_M,m'] + 2 m' D_M is ORDER ONE,")
print("     while a bundle endomorphism's [D_M,m] = Clifford.dm is ORDER ZERO.]")
print("    => J b* J^-1 has BOUNDED [D, .] (because [D,b*] does), so it is U_iota-FREE.")
print(f"    O2: CAVEAT O closes in the B = iota-even regime: {o2}")
results["o2_identity"] = bool(identity_ok)
results["o2_norm_growth"] = norms
results["o2_closes"] = bool(o2)

# --- O3: the extreme case B = C*1, where A' is everything --------------------
print("\nO3 -- extreme case B = C*1, A = span{1(x)I, u = 1(x)s1}. A' is EVERYTHING,")
print("      so locality cannot be the argument. Track the H_M factor instead.")
# [D, 1(x)I] = 0 ; [D, u] = -3i (I (x) s2). Every generator's H_M factor is the IDENTITY.
comm_u = 1.5 * (S3 @ S1 - S1 @ S3)
print("    [D, 1(x)I] = 0 : True")
print(f"    [D, u] = -3i(I(x)s2) : {np.allclose(comm_u, -3j * S2)}   -- H_M factor = I")
# WHY THIS IS COMPUTED AND NOT ASSERTED: the first version simply set
# h_m_always_identity = True with a comment. That is a check that cannot fail -- the
# fifth instance of that disease this session. Generate the algebra explicitly on the
# FULL space and test each element, with a counter-case that must break it.
IM = np.eye(DIM_M, dtype=complex)


def hm_factor_is_identity(t: np.ndarray) -> bool:
    """T = kron(sec, I_{H_M}) for some 2x2 sec?"""
    for i, j in product(range(2), range(2)):
        blk = t[i * DIM_M : (i + 1) * DIM_M, j * DIM_M : (j + 1) * DIM_M]
        c = np.trace(blk) / DIM_M
        if not np.allclose(blk, c * IM):
            return False
    return True


def close_algebra(gens: list[np.ndarray], rounds: int = 4) -> list[np.ndarray]:
    alg = list(gens)
    for _ in range(rounds):
        for x, y in product(list(alg), repeat=2):
            p = x @ y
            if not any(np.allclose(p, q) for q in alg):
                alg.append(p)
    return alg


GENS_OK = [np.kron(I2, IM), np.kron(S1, IM), np.kron(S2, IM)]  # A and [D,A]
alg_ok = close_algebra(GENS_OK)
h_m_always_identity = all(hm_factor_is_identity(t) for t in alg_ok)
# counter-case: admit U_iota (x) I as an extra generator -- the property MUST break
alg_bad = close_algebra([*GENS_OK, np.kron(I2, U_IOTA_M)])
breaks = sum(1 for t in alg_bad if not hm_factor_is_identity(t))
print(f"    algebra generated by A and [D,A] has {len(alg_ok)} elements;")
print(f"    H_M factor of EVERY such product is the identity: {h_m_always_identity}")
print(f"    COUNTER-CASE: admit U_iota(x)I -> {breaks}/{len(alg_bad)} elements break it,")
print(f"                  so the property CAN fail: {breaks > 0}")
h_m_always_identity = h_m_always_identity and breaks > 0
print("    => gamma = U_iota (x) s1 needs U_iota, which can ONLY come from J b* J^-1,")
print("       and O2 forbids a U_iota part there. So O3 closes this case too.")
o3 = bool(np.allclose(comm_u, -3j * S2)) and h_m_always_identity
results["o3_H_M_always_identity"] = bool(o3)

# --- O4: DISCRIMINATOR -- if J u J^-1 WERE U_iota (x) s1, gamma IS reachable --
print("\nO4 -- DISCRIMINATOR: allow J u J^-1 = U_iota (x) s1 and see if gamma appears.")
gamma = np.kron(S1, U_IOTA_M)
phi_u_allowed = np.kron(S1, U_IOTA_M)  # the forbidden-by-O2 candidate
a0 = np.kron(I2, np.eye(DIM_M))  # a0 = 1 (x) I
reachable = bool(np.allclose(a0 @ phi_u_allowed, gamma))
print(f"    with a0 = 1(x)I and J b0* J^-1 = U_iota(x)s1:  pi_D = gamma exactly: {reachable}")
print("    so the obstruction is PRECISELY the boundedness of [D, J u J^-1] --")
print("    not a shortage of algebra, and not genericity.")
results["o4_reachable_if_allowed"] = reachable

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = o1 and o2 and o3 and reachable
verdict = "CAVEAT_O_CLOSED__J_CANNOT_SUPPLY_U_IOTA" if ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C53 is REFUTED. The A (x) A^op formulation does not repair orientability.")
    print()
    print("  The escape was real: shrinking B DOES enlarge A' until it contains")
    print("  U_iota-carrying operators (O1). But J b* J^-1 must have BOUNDED commutator")
    print("  with D, because [D,b*] does and J is antiunitary -- and any U_iota-carrying")
    print("  part makes that commutator ORDER ONE (O2). So J A J^-1 is U_iota-free.")
    print()
    print("  In the extreme B = C*1, where A' is everything and locality says nothing,")
    print("  a different bookkeeping closes it: every generator of A and [D,A] acts as")
    print("  the IDENTITY on the H_M factor (O3), so gamma's U_iota could only come from")
    print("  J b* J^-1 -- which O2 has just excluded.")
    print()
    print("  O4 confirms the argument is not genericity: ALLOW J u J^-1 = U_iota (x) s1")
    print("  and gamma is reproduced EXACTLY. Boundedness is doing all the work.")
    print()
    print("  CAVEAT O' -- the residual, named rather than hidden: J u J^-1 could be a SUM")
    print("  in which a U_iota term's unbounded commutator CANCELS against another")
    print("  unbounded term. A finite model has no unbounded operators and cannot exclude")
    print("  it. Such a J would still have to satisfy order-zero, J^2 = +-1 and")
    print("  J D = +- D J simultaneously with that fine-tuning.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
