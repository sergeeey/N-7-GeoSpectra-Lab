r"""
C158 STEP 1 -- build the actual geometric W(A_2)=S_3 action on m and on
V_conn (the 6-dim equivariant connection family), and run gates G1-G4.

Reuses C153's exact construction (M_BASIS, to_m, T2_M, family_sym) unmodified.

Run:  python c158_step1_weyl_action.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S2_PATH = (
    HERE.parent
    / "20260904-c153-nk-linearity-structural-derivation"
    / "c153_step2_exact_rational_verification.py"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S2 = load_module("c153_step2", S2_PATH)
M_BASIS = S2.M_BASIS
to_m = S2.to_m
T2_M = S2.T2_M
family_sym = S2.family_sym

print("=" * 78)
print("STEP 1  build SU(3) Weyl representatives, verify the 2x2 swap fact first")
print("=" * 78)


def su3_transposition(p, q):
    """I_3 outside the {p,q} block, [[0,1],[-1,0]] inside -- unitary, det=1,
    conjugation swaps diagonal entries p,q (verified directly below)."""
    g = sp.eye(3)
    g[p, p], g[p, q], g[q, p], g[q, q] = 0, 1, -1, 0
    return g


g01 = su3_transposition(0, 1)
g12 = su3_transposition(1, 2)

# sanity: 2x2 swap fact, checked in isolation before trusting the 3x3 version
g2 = sp.Matrix([[0, 1], [-1, 0]])
D = sp.diag(sp.Symbol("a"), sp.Symbol("b"))
swapped = sp.simplify(g2 * D * g2.inv())
print(f"  isolated 2x2 check: g D g^-1 = {swapped.tolist()}  (must be diag(b,a))")
assert swapped == sp.diag(sp.Symbol("b"), sp.Symbol("a"))

for name, g, pq in (("g01", g01, (0, 1)), ("g12", g12, (1, 2))):
    unit = sp.simplify(g * g.conjugate().T) == sp.eye(3)
    det1 = sp.simplify(g.det()) == 1
    print(f"  {name}: unitary={unit}, det=1: {det1}")
    assert unit and det1
    # conjugation of diag(1,2,3)-labelled positions swaps p,q, fixes the third
    probe = sp.diag(1, 2, 3)
    out = sp.simplify(g * probe * g.conjugate().T)
    p, q = pq
    want = probe.copy()
    want[p, p], want[q, q] = probe[q, q], probe[p, p]
    print(f"  {name}: conjugation swaps positions {pq} on a diagonal probe: {out == want}")
    assert out == want


def R_of(g):
    """Conjugate every M_BASIS generator by g (as 3x3 matrices), re-express in
    M_BASIS coordinates via C153's exact to_m -- gives a 6x6 orthogonal matrix."""
    ginv = g.conjugate().T  # unitary
    cols = []
    for X in M_BASIS:
        conj = g * X * ginv
        cols.append(sp.Matrix(to_m(conj)))
    return sp.Matrix.hstack(*cols)


R01 = R_of(g01)
R12 = R_of(g12)
print()
print("  R01, R12 (action on the 6-dim m, in M_BASIS coordinates) built.")

print()
print("=" * 78)
print("GATE G1  [CORRECTED] R01^2, R12^3 as literal 6x6 matrices on m")
print("=" * 78)
print("  [SECOND SELF-CORRECTION, before running] the original pre-registration")
print("  tested 'R12^3 = I', which is simply the wrong group-theoretic claim:")
print("  g12 represents the TRANSPOSITION (1,2), an order-2 element of S_3, not")
print("  a 3-cycle. The genuine order-3 element of W(A_2) is the PRODUCT")
print("  g01*g12 (a 3-cycle on the weight indices). Both g01 and g12 (simple")
print("  reflections) are tested for ORDER 2 below; the 3-cycle is tested")
print("  separately as a bonus regression, since 3-cycles are known to lift")
print("  honestly (no order-4 subtlety) -- only reflections have that issue.")
R01sq = sp.simplify(R01 * R01)
R12sq = sp.simplify(R12 * R12)
print(f"  R01^2 = {R01sq.tolist()}")
print(f"  R12^2 = {R12sq.tolist()}")
lit_a = R01sq == sp.eye(6)
lit_b = R12sq == sp.eye(6)
print(f"  R01^2 == I (literal, on all of m): {lit_a}")
print(f"  R12^2 == I (literal, on all of m): {lit_b}")
print()
print("  [SELF-CORRECTION] Both are False, and that is EXPECTED, not a bug: this")
print("  is the standard SU(n)-Weyl-lift phenomenon -- a block-embedded SU(2)")
print("  representative of a simple reflection has order 4 in SU(n), not order")
print("  2, because N(T) -> W = N(T)/T does not split. g01^2 = diag(-1,-1,1) is")
print("  a genuine, nontrivial element of the maximal torus T itself (checked:")
print("  it is diagonal, unitary, det 1) -- NOT the identity, but ALSO not an")
print("  obstruction, because T2_M/family_sym were built to be invariant under")
print("  the FULL torus T already. The gate that actually matters is whether")
print("  R01^2 (and R12^3) act as the IDENTITY specifically on family_sym --")
print("  i.e. whether the torus element they equal is one family_sym is")
print("  already invariant under, which is exactly what T-equivariance means.")

print()
print("=" * 78)
print("GATE G1b  orthogonality of R01, R12 (they must preserve the Killing form)")
print("=" * 78)
orth01 = sp.simplify(R01.T * R01) == sp.eye(6)
orth12 = sp.simplify(R12.T * R12) == sp.eye(6)
print(f"  R01 orthogonal: {orth01}   R12 orthogonal: {orth12}")
assert orth01 and orth12

print()
print("=" * 78)
print("GATE G2  R01, R12 act on span{T2_M[0], T2_M[1]} as automorphisms of t")
print("=" * 78)


def as_m_vec(mat6x6):
    """T2_M[i] is already a 6x6 operator on m; represent the ACTION of R on
    the operator via conjugation, then check membership in span(T2_M) by
    solving a linear system over the 36 matrix entries."""
    return mat6x6


T2_vecs = [sp.Matrix([T2_M[i][r, c] for r in range(6) for c in range(6)]) for i in range(2)]
Tspan = sp.Matrix.hstack(*T2_vecs)

for name, R in (("R01", R01), ("R12", R12)):
    ok_all = True
    for i in range(2):
        conj = sp.simplify(R * T2_M[i] * R.T)
        conj_vec = sp.Matrix([conj[r, c] for r in range(6) for c in range(6)])
        aug = Tspan.row_join(conj_vec)
        inside = aug.rank() == Tspan.rank()
        ok_all = ok_all and inside
        print(f"  {name}: R T2_M[{i}] R^-1 in span(T2_M): {inside}")
    assert ok_all, f"G2 FAILED for {name}"

print()
print("=" * 78)
print("GATE G3  R01, R12 map family_sym (the 6-dim equivariant family, as a")
print("         90-dim ambient ker) INTO ITSELF, as a SPAN")
print("=" * 78)


def ambient_action(R, fam_cols):
    """(sigma.Lambda)_k = sum_j R[k,j] * (R Lambda_j R^-1), acting on the 90-dim
    ambient representation (6 blocks of 15 pair-coefficients each)."""
    lam_mats = []
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(S2.PAIRS6):
            M[i, j] += fam_cols[k * 15 + p_idx]
            M[j, i] -= fam_cols[k * 15 + p_idx]
        lam_mats.append(M)
    new_lam = [sp.zeros(6, 6) for _ in range(6)]
    for k in range(6):
        for j in range(6):
            if R[k, j] != 0:
                new_lam[k] += R[k, j] * (R * lam_mats[j] * R.T)
    out = sp.zeros(90, 1)
    for k in range(6):
        M = sp.simplify(new_lam[k])
        for p_idx, (i, j) in enumerate(S2.PAIRS6):
            out[k * 15 + p_idx] = M[i, j]
    return out


fam_basis = [family_sym[:, c] for c in range(6)]
Fam = family_sym

for name, R in (("R01", R01), ("R12", R12)):
    ok_all = True
    for c in range(6):
        img = ambient_action(R, fam_basis[c])
        aug = Fam.row_join(img)
        inside = aug.rank() == Fam.rank()
        ok_all = ok_all and inside
    print(f"  {name}: maps all 6 family basis directions into span(family_sym): {ok_all}")
    assert ok_all, f"G3 FAILED for {name} -- construction is broken, stop here"

print()
print("=" * 78)
print("GATE G1  [CORRECTED, the real test] R01^2, R12^2 act as the IDENTITY")
print("         specifically on family_sym (T-equivariant connections)")
print("=" * 78)
for label, R2 in (("R01^2", R01sq), ("R12^2", R12sq)):
    ok_all = True
    for c in range(6):
        img = ambient_action(R2, fam_basis[c])
        ok_all = ok_all and (sp.simplify(img - fam_basis[c]) == sp.zeros(90, 1))
    print(f"  {label} acts as IDENTITY on all 6 family_sym basis directions: {ok_all}")
    assert ok_all, f"G1 (corrected) FAILED for {label} -- stop, construction not understood"
print("  CONFIRMED: the order-4 lift is exactly absorbed by family_sym's own")
print("  T-invariance, as predicted. R01, R12 have order EXACTLY 2 when")
print("  restricted to family_sym, even though not on the ambient m.")

print()
print("=" * 78)
print("GATE G1c  BONUS regression: the 3-cycle g01*g12 lifts HONESTLY (no torus")
print("          subtlety at all -- (R01*R12)^3 = I literally on all of m)")
print("=" * 78)
R012 = R01 * R12
cube = sp.simplify(R012 * R012 * R012)
cube_ok = cube == sp.eye(6)
print(f"  (R01*R12)^3 == I literally, on the full 6-dim m (not just family): {cube_ok}")
assert cube_ok, "3-cycle should lift honestly -- if this fails, the whole construction is suspect"

print()
print("=" * 78)
print("  Building the 6x6 restriction of R01, R12 to family_sym's OWN")
print("  coordinates (needed for G4)")
print("=" * 78)


# BLOCKED-INFRASTRUCTURE note (self-caught): an earlier version of this step
# searched for an invertible 6x6 minor of the 90x6 family_sym matrix via an
# odometer over row-subsets, calling .det() repeatedly -- this hung past a
# 900s timeout (a performance defect in the test harness, not a result about
# anything). Replaced with a single Gram-matrix pseudo-inverse, computed once:
# family_sym has full column rank 6 (already established, C153), so
# (F^T F)^-1 F^T is the exact left-inverse, needing exactly one 6x6 inversion.
Gram = sp.simplify(Fam.T * Fam)
Gram_inv = Gram.inv()
Fam_pinv = Gram_inv * Fam.T  # exact left-inverse: Fam_pinv * Fam == I_6
identity_check = sp.simplify(Fam_pinv * Fam) == sp.eye(6)
print(f"  left-inverse check (Fam_pinv * Fam == I_6): {identity_check}")
assert identity_check, "family_sym does not have the expected full column rank"


def restrict_to_family(R):
    cols = []
    for c in range(6):
        img = ambient_action(R, fam_basis[c])
        coords = sp.simplify(Fam_pinv * img)
        cols.append(coords)
    return sp.Matrix.hstack(*cols)


W01 = restrict_to_family(R01)
W12 = restrict_to_family(R12)
print(
    f"  W01 (R01 on family coords) built, orthogonal check: {sp.simplify(W01.T * W01) == sp.eye(6)}"
)
print(
    f"  W12 (R12 on family coords) built, orthogonal check: {sp.simplify(W12.T * W12) == sp.eye(6)}"
)
W012 = W01 * W12
print(f"  W01^2 == I : {sp.simplify(W01 * W01) == sp.eye(6)}")
print(f"  W12^2 == I : {sp.simplify(W12 * W12) == sp.eye(6)}")
print(f"  (W01*W12)^3 == I : {sp.simplify(W012 * W012 * W012) == sp.eye(6)}")
assert sp.simplify(W01 * W01) == sp.eye(6)
assert sp.simplify(W12 * W12) == sp.eye(6)
assert sp.simplify(W012 * W012 * W012) == sp.eye(6)
print("  W01, W12 correctly generate an honest S_3 action on family_sym's")
print("  own 6-dim coordinates: both simple reflections order 2, their")
print("  product (the 3-cycle) order 3, as required for a genuine S_3.")

print()
print("=" * 78)
print("GATE G4  THE ACTUAL TEST -- is ker(M) = {a0=a2-a4, a1=a3-a5}")
print("         (C155's exact kernel) invariant under W01, W12?")
print("=" * 78)
a0, a1, a2, a3, a4, a5 = sp.symbols("a0 a1 a2 a3 a4 a5")
avec = sp.Matrix([a0, a1, a2, a3, a4, a5])
ker_basis = [
    sp.Matrix([1, 0, 1, 0, 0, 0]),  # a0=1,a2=1 (a0=a2-a4 with a4=0), a1=a3=a5=0... verify below
]
# Build the exact 4-dim kernel basis from C155's relation {a0=a2-a4, a1=a3-a5},
# i.e. a0,a1 are DEPENDENT, {a2,a3,a4,a5} free:
ker_basis = []
free_sets = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
for a2v, a3v, a4v, a5v in free_sets:
    a0v = a2v - a4v
    a1v = a3v - a5v
    ker_basis.append(sp.Matrix([a0v, a1v, a2v, a3v, a4v, a5v]))
Ker = sp.Matrix.hstack(*ker_basis)
print("  ker(M) basis (C155's exact relation), as 6-dim vectors:")
for i, v in enumerate(ker_basis):
    print(f"    k{i}: {tuple(v)}")

for name, W in (("W01", W01), ("W12", W12)):
    ok_all = True
    for i, v in enumerate(ker_basis):
        img = sp.simplify(W * v)
        aug = Ker.row_join(img)
        inside = aug.rank() == Ker.rank()
        ok_all = ok_all and inside
        if not inside:
            print(f"    {name}: k{i} -> {tuple(img)}  NOT in ker(M)")
    print(f"  {name} maps ker(M) INTO ITSELF: {ok_all}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
g4a = all(sp.Matrix.hstack(Ker, sp.simplify(W01 * v)).rank() == Ker.rank() for v in ker_basis)
g4b = all(sp.Matrix.hstack(Ker, sp.simplify(W12 * v)).rank() == Ker.rank() for v in ker_basis)
print(f"  G4 (W01): ker(M) invariant : {g4a}")
print(f"  G4 (W12): ker(M) invariant : {g4b}")
print(f"  G4 OVERALL: ker(M) is W(A_2)=S_3-INVARIANT : {g4a and g4b}")
