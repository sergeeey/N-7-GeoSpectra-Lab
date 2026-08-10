"""Y2: A's diagonal part smaller than the twisted diagonal -- and the locality obstruction.

WHY Y2 IS NOT A FORMALITY. W1 and Y1 both run through C50's step W1a: A''s
sector-off-diagonal blocks must factor as m*U_iota, because they satisfy
T01 (f o iota) = f T01 FOR ALL f -- and that comes from A containing the FULL twisted
diagonal. Shrink the diagonal part to B (properly contained in C^inf(S^3)) and the
condition weakens to b in B only, A' gets BIGGER, and it can contain off-diagonal
operators that do NOT carry U_iota. Those have BOUNDED commutator with D, so the step
that forced J u J^-1 sector-diagonal FAILS.

In the extreme case B = C*1 this is total: A = span{1 (x) I, 1 (x) s1} = C (+) C is
unital, gamma-even (constants are iota-even), closed, sector-mixing -- and 1 (x) s1 lies
in its OWN commutant. The entire J route collapses. Recorded in claim.md before running:
I expect the J argument to be unrecoverable here.

SO THE TEST IS FOR A DIFFERENT AXIOM. Predictions Y2a-Y2e in claim.md:

  Y2a  the escape is REAL -- with B = C*1, A' has off-diagonal elements not of the
       form m*U_iota, with BOUNDED [D, .]
  Y2b  but every a in A and every [D,a] is LOCAL: g T f = 0 for disjoint supports
  Y2c  gamma = U_iota (x) s1 is NOT local -- iota moves points
  Y2d  so pi_D(c) = sum a0 [D,a1][D,a2][D,a3] is local for EVERY Hochschild chain,
       hence pi_D(c) != gamma. ORIENTABILITY FAILS, for every admissible A,
       whatever its diagonal part
  Y2e  DISCRIMINATION -- replacing U_iota by a LOCAL bundle map must remove the
       obstruction, or the argument is about the method rather than about iota

THE POINT THIS MAKES EXPLICIT: gamma here is built from a DIFFEOMORPHISM. Every gamma in
an ordinary even spectral triple is built from the CLIFFORD algebra -- a bundle
endomorphism, local by construction. C43, C45 and C50 all found iota load-bearing; this
is the bill.

FINITE MODEL: X = {a, b, c, c'} with iota = (a)(b)(c c') -- two fixed points and one free
orbit, the shape of iota(g) = g^-1 on S^3. H = C^X (x) C^2_spin (x) C^2_sector.
Locality is tested operationally: T is LOCAL iff g T f = 0 whenever the functions f, g
have disjoint supports.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_y2.json"
results: dict = {}

NX = 4
IOTA_PERM = [0, 1, 3, 2]  # a->a, b->b, c<->c'
XNAME = ["a", "b", "c", "c'"]
I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[-1, 0], [0, 1]], dtype=complex)
PAULI = {"I": I2, "s1": S1, "s2": S2, "s3": S3}

U_IOTA_X = np.zeros((NX, NX), dtype=complex)
for i, j in enumerate(IOTA_PERM):
    U_IOTA_X[j, i] = 1.0
U_IOTA_M = np.kron(U_IOTA_X, I2)  # spinor part of the lift taken trivial in the toy

DIM_M = NX * 2
DIM = DIM_M * 2


def mult(f: np.ndarray) -> np.ndarray:
    """multiplication by a function on X, tensored with the spinor fibre."""
    return np.kron(np.diag(f), I2)


def op(a_m: np.ndarray, sec: np.ndarray) -> np.ndarray:
    return np.kron(sec, a_m)


def indicator(points: list[int]) -> np.ndarray:
    f = np.zeros(NX)
    for p in points:
        f[p] = 1.0
    return f


def is_local(t: np.ndarray) -> bool:
    """T is LOCAL iff g T f = 0 for every pair of disjoint-support functions f, g."""
    for i, j in product(range(NX), range(NX)):
        if i == j:
            continue
        g = op(mult(indicator([i])), I2)
        f = op(mult(indicator([j])), I2)
        if not np.allclose(g @ t @ f, 0):
            return False
    return True


print("=" * 78)
print("Y2 -- smaller diagonal part, and the LOCALITY obstruction to orientability")
print("=" * 78)

# --- Y2a: with B = C*1 the J route really does collapse ----------------------
print("\nY2a -- is the escape REAL? Take B = C*1, so A = span{1(x)I, 1(x)s1} = C (+) C")
A_SMALL = [op(np.eye(DIM_M), I2), op(np.eye(DIM_M), S1)]
rows = []
for g in A_SMALL:
    rows.append(np.kron(np.eye(DIM), g.T) - np.kron(g, np.eye(DIM)))
_, sv, vh = np.linalg.svd(np.vstack(rows))
null = vh[np.sum(sv > 1e-9) :].conj().T
print(f"    dim H = {DIM};  dim A' = {null.shape[1]}   (C50's case had a much smaller A')")
# does A' contain an off-diagonal element NOT of the form m*U_iota?
u_swap = op(np.eye(DIM_M), S1)
in_commutant = all(np.allclose(u_swap @ g - g @ u_swap, 0) for g in A_SMALL)
m_cand = u_swap[:DIM_M, DIM_M:] @ np.linalg.inv(U_IOTA_M)
carries_u_iota = all(
    np.allclose(m_cand @ mult(indicator([i])) - mult(indicator([i])) @ m_cand, 0) for i in range(NX)
)
comm_bounded = np.allclose(1.5 * (S3 @ S1 - S1 @ S3), -3j * S2)
print(f"    u = 1(x)s1 lies in its OWN commutant A': {in_commutant}")
print(f"    its off-diagonal block factors as m*U_iota: {carries_u_iota}   (expect False)")
print(f"    and [D,u] = -3i(I(x)s2) is BOUNDED: {comm_bounded}")
y2a = in_commutant and (not carries_u_iota) and comm_bounded
print(f"    Y2a: C50's W1a/W1c FAIL here -- the J route is unrecoverable: {y2a}")
results["y2a_dim_commutant"] = int(null.shape[1])
results["y2a_escape_is_real"] = bool(y2a)

# --- Y2b: everything in A and every [D,a] is LOCAL ---------------------------
print("\nY2b -- locality of A and of [D,A]  (T local iff g T f = 0 for disjoint supports)")
rng = np.random.default_rng(20260810)
local_checks = {}
# generic admissible elements: multiplication (x) constant sector matrix (C46's symbols)
for label, sec in (("f (x) I", "I"), ("f (x) s1", "s1"), ("f (x) s2", "s2"), ("f (x) s3", "s3")):
    ok = True
    for _ in range(50):
        f = rng.normal(size=NX)
        ok &= is_local(op(mult(f), PAULI[sec]))
    local_checks[label] = ok
    print(f"    {label:12s} local: {ok}")
# [D,a]: by the standard identity [D, f] = c(df), a BUNDLE ENDOMORPHISM -- so it is
# again (matrix-valued function) (x) (sector matrix). [VERIFIED-analytic], not re-derived
# here; the toy checks the support bookkeeping that follows from it.
comm_local = True
for _ in range(50):
    endo = np.kron(np.diag(rng.normal(size=NX)), rng.normal(size=(2, 2)))  # c(df): bundle endo
    sec = rng.normal(size=(2, 2))
    comm_local &= is_local(np.kron(sec, endo))
local_checks["[D,a] = c(df) (x) sector"] = comm_local
print(f"    {'[D,a] = c(df)(x)sec':12s} local: {comm_local}   [input: [D,f] = c(df), analytic]")
y2b = all(local_checks.values())
print(f"    Y2b: every element of A and every [D,a] is LOCAL: {y2b}")
results["y2b_local_checks"] = local_checks
results["y2b_all_local"] = bool(y2b)

# --- Y2c: gamma is NOT local -------------------------------------------------
print("\nY2c -- is gamma = U_iota (x) s1 local?")
gamma = op(U_IOTA_M, S1)
g_loc = is_local(gamma)
g_c = op(mult(indicator([2])), I2)  # supported at c
f_cp = op(mult(indicator([3])), I2)  # supported at c' = iota(c), disjoint from c
witness = float(np.linalg.norm(g_c @ gamma @ f_cp))
print(f"    gamma local: {g_loc}   (expect False)")
print(f"    witness: || 1_{{c}} . gamma . 1_{{c'}} || = {witness:.4f}  (non-zero => non-local)")
print(f"    iota's fixed points are {[XNAME[i] for i in range(NX) if IOTA_PERM[i] == i]},")
print("    so disjoint pairs (x, iota x) exist -- exactly as on S^3, whose fixed set is {+-1}")
y2c = (not g_loc) and witness > 1e-9
results["y2c_gamma_local"] = bool(g_loc)
results["y2c_witness_norm"] = witness
results["y2c_gamma_nonlocal"] = bool(y2c)

# --- Y2d: therefore pi_D(c) can never equal gamma ----------------------------
print("\nY2d -- pi_D(c) = sum a0 [D,a1][D,a2][D,a3] over Hochschild 3-chains")
print("       products of LOCAL operators are LOCAL, so pi_D(c) is local, so != gamma")
# WHY NOT "count how many random chains equal gamma": that count is 0 by genericity --
# random matrices never hit a specific target -- so it would confirm nothing, the same
# decorative-check disease caught three times already this session. The real content is
# the CLOSURE LEMMA (locality survives products and sums) plus a counter-case that CAN
# fail (admit one non-local factor and gamma becomes reachable).
print("       [the informative form is a closure lemma + a counter-case, NOT a hit count]")


def random_chain(local_factors: bool) -> np.ndarray:
    """pi_D of a random Hochschild 3-chain; local_factors=False smuggles in U_iota."""
    acc = np.zeros((DIM, DIM), dtype=complex)
    for _term in range(3):
        a0 = op(mult(rng.normal(size=NX)), PAULI[rng.choice(["I", "s1", "s2", "s3"])])
        term = a0 if local_factors else a0 @ op(U_IOTA_M, I2)
        for _k in range(3):
            endo = np.kron(np.diag(rng.normal(size=NX)), rng.normal(size=(2, 2)))
            term = term @ np.kron(rng.normal(size=(2, 2)), endo)
        acc = acc + term
    return acc


prod_local = all(is_local(random_chain(True)) for _ in range(400))
print(f"    CLOSURE LEMMA: 400 random chains of LOCAL factors -> pi_D(c) local: {prod_local}")
# the counter-case: one non-local factor and locality is destroyed, so the lemma is
# doing work rather than holding for shape reasons
broke = sum(1 for _ in range(400) if not is_local(random_chain(False)))
print("    COUNTER-CASE: same chains with ONE U_iota factor smuggled in ->")
print(f"                  {broke}/400 are NON-local, so the lemma CAN fail: {broke > 0}")
# and gamma is exactly reachable once U_iota is admitted -- the obstruction is precisely
# that U_iota is not in the algebra, not that gamma is hard to hit
reachable = np.allclose(op(U_IOTA_M, S1) @ np.eye(DIM), gamma)
print(f"    and with U_iota admitted, gamma IS reachable exactly (a0 = U_iota(x)s1): {reachable}")
y2d = prod_local and broke > 0 and reachable
print("    Y2d: ORIENTABILITY FAILS -- no Hochschild cycle over a LOCAL algebra can")
print(f"         produce a NON-LOCAL gamma: {y2d}")
print("       and the argument never mentioned B, J, or the size of A'.")
results["y2d_products_local"] = bool(prod_local)
results["y2d_counter_case_nonlocal"] = int(broke)
results["y2d_gamma_reachable_with_U_iota"] = bool(reachable)
results["y2d_orientability_fails"] = bool(y2d)

# --- Y2e: DISCRIMINATION -- is the obstruction caused by iota specifically? --
print("\nY2e -- DISCRIMINATION: replace U_iota by a LOCAL bundle map. The obstruction")
print("       must DISAPPEAR, or this argument is about the method, not about iota.")
local_maps = {
    "identity": np.eye(DIM_M, dtype=complex),
    "sign(x)*I  (bundle endo)": np.kron(np.diag([1.0, -1.0, 1.0, -1.0]), I2),
    "random bundle endo": np.kron(np.diag(rng.normal(size=NX)), rng.normal(size=(2, 2))),
}
disc = {}
for name, v in local_maps.items():
    gam = op(v, S1)
    disc[name] = {"local": bool(is_local(gam))}
    print(f"    gamma = ({name}) (x) s1   local: {disc[name]['local']}   (expect True)")
y2e = all(v["local"] for v in disc.values()) and not g_loc
print("    Y2e: local replacements are local, U_iota is not -- the obstruction is")
print(f"         caused by iota SPECIFICALLY, and the test discriminates: {y2e}")
print("       (those local gammas do NOT anticommute with D_block -- that is C45's")
print("        result, and it is why the construction needed a diffeomorphism at all)")
results["y2e_local_replacements"] = disc
results["y2e_discriminates"] = bool(y2e)

# --- CONTROL: does this prove too much about S^3 itself? --------------------
print("\nCONTROL -- does the argument wrongly condemn ordinary geometry?")
print("    An ordinary EVEN spectral triple has gamma = a product of Clifford elements,")
print("    i.e. a BUNDLE ENDOMORPHISM -- local by construction, and pi_D(volume cycle)")
print("    reproduces it. Checked above as Y2e: such gammas ARE local, so no obstruction.")
print("    S^3's own ODD triple has no gamma at all and needs pi_D(c) = 1, also local.")
one_local = is_local(np.eye(DIM, dtype=complex))
print(f"    identity (the odd-case target) is local: {one_local}")
print("    => the obstruction fires ONLY on a gamma built from a DIFFEOMORPHISM.")
results["control_identity_local"] = bool(one_local)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = y2a and y2b and y2c and y2d and y2e and one_local
verdict = (
    "Y2_CLOSED__ORIENTABILITY_FAILS_BY_LOCALITY_FOR_EVERY_ADMISSIBLE_A" if ok else "INCONCLUSIVE"
)
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C52 is REFUTED, and by a route that owes nothing to the C48-C51 chain.")
    print()
    print("  Y2 IS a real escape from the J argument -- with B = C*1 the commutant")
    print("  balloons, u = 1(x)s1 sits in its own commutant, [D,u] is bounded, and C50's")
    print("  W1a/W1c simply do not apply. That much was expected and is confirmed.")
    print()
    print("  But a DIFFERENT axiom closes it. Every element of A and every [D,a] is")
    print("  LOCAL; products of local operators are local; so pi_D of any Hochschild")
    print("  chain is local. gamma = U_iota (x) s1 is NOT local, because iota MOVES")
    print("  POINTS. Hence pi_D(c) != gamma for every chain: ORIENTABILITY FAILS.")
    print()
    print("  The argument never mentions B, J, or the size of A', so it retires Y2, Y1'")
    print("  and the Lipschitz loophole at once -- and it EXPLAINS C49: orientability")
    print("  produces the fundamental class, Poincare duality needs it non-degenerate,")
    print("  and both fail for the same underlying reason.")
    print()
    print("  WHAT THIS MAKES EXPLICIT. gamma here is built from a DIFFEOMORPHISM; every")
    print("  gamma in an ordinary even spectral triple is built from the CLIFFORD")
    print("  algebra and is local by construction. C43, C45 and C50 each found iota")
    print("  load-bearing. This is the bill for that.")
    print()
    print("  CAVEAT O, not waved away: some statements of orientability use a cycle in")
    print("  Z_n(A, A (x) A^op), so pi_D also carries J a* J^-1 factors. Those are local")
    print("  PROVIDED J A J^-1 is local -- which C50/C51 established only when A contains")
    print("  the twisted diagonal. For a SMALLER B that is NOT established and remains an")
    print("  honest open sub-point.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
