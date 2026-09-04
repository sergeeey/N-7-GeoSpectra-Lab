r"""
C153 STEP 2 -- verify O(eps) = c(J_eps.grad) - i*c(grad) is EXACTLY zero for
the 2 C-linear eps, and EXACTLY nonzero (rational, not float noise) for the
other 6, using EXACT rational arithmetic throughout, not floating point.

FIRST ATTEMPT (kept as a documented dead end, not deleted): rationalising the
ALREADY-COMPUTED numeric dom/tgt/family vectors (from the SVD-based C151/C152
pipeline) via sympy.nsimplify. This FAILED its own honesty check --
residual 2.1e-4, far above the 1e-9 floating noise floor -- because SVD
orthonormalisation of a rational null space generically introduces irrational
(square-root) entries into the CHOSEN BASIS VECTORS even though the SPAN
itself is exactly rational. Lowering the tolerance to make the check pass
would have been exactly the kind of self-serving threshold this project's
own rules forbid; the fix is a different METHOD, not a looser bound.

THIS VERSION rebuilds the entire SU(3)/T^2 construction from scratch in
EXACT sympy rational arithmetic: M_BASIS, the Killing form, the Levi-Civita
Nomizu operators, the T^2 Cartan generator, the invariant sector (via
sympy's exact Matrix.nullspace(), not numpy SVD), and the 6-dim equivariant
connection family (same nullspace method, replacing C73b's SVD). Nothing
here is rationalised from a float; every number is exact from the start.
round59's Clifford algebra (E_sym) is reused unmodified -- it is already
exact sympy, built independently of this reconstruction.

Run:  python c153_step2_exact_rational_verification.py
"""

import importlib.util
from itertools import combinations, product
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)
E_sym = R59.build_clifford(conj=False)  # dict i=1..6 -> exact sympy 8x8 Clifford matrix
ODD_IDX, EVEN_IDX = R59.ODD_IDX, R59.EVEN_IDX
EPS_NK = (-1, 1, -1)  # C151 Stage 1a's pinned value, reused verbatim
PAIRS_M = [(0, 1), (0, 2), (1, 2)]
PAIRS6 = list(combinations(range(6), 2))  # C73b's PAIRS, rebuilt to avoid importing numpy code

print("=" * 78)
print("STEP 2a  exact M_BASIS (J-aligned), exact B-orthonormality check")
print("=" * 78)

M_BASIS = []
for k, (p, q) in enumerate(PAIRS_M):
    X = sp.zeros(3, 3)
    X[p, q], X[q, p] = 1, -1
    Y = sp.zeros(3, 3)
    Y[p, q], Y[q, p] = sp.I, sp.I
    M_BASIS.extend([X, Y] if EPS_NK[k] > 0 else [Y, X])


def killing_B(A, B):
    return sp.Rational(-1, 2) * (A * B).trace()


gram = sp.Matrix(6, 6, lambda r, c: killing_B(M_BASIS[r], M_BASIS[c]))
gram = sp.simplify(gram)
print(f"  gram - I is exactly zero: {gram == sp.eye(6)}")
assert gram == sp.eye(6), "exact basis is not B-orthonormal -- STOP"


def to_m(mat):
    coords = [sp.re(sp.simplify(killing_B(mat, b))) for b in M_BASIS]
    imag_residual = max(abs(sp.im(sp.simplify(killing_B(mat, b)))) for b in M_BASIS)
    assert imag_residual == 0, f"to_m picked up an exact nonzero imaginary part: {imag_residual}"
    return coords


print()
print("=" * 78)
print("STEP 2b  exact Levi-Civita Nomizu operators and T^2 Cartan generator")
print("=" * 78)

NOMIZU_LC = {}
for i in range(6):
    L = sp.zeros(6, 6)
    for j in range(6):
        comm = M_BASIS[i] * M_BASIS[j] - M_BASIS[j] * M_BASIS[i]
        col = to_m(comm)
        for r in range(6):
            L[r, j] = sp.Rational(1, 2) * col[r]
    NOMIZU_LC[i + 1] = L
antisym = max(
    abs((NOMIZU_LC[i] + NOMIZU_LC[i].T)[r, c])
    for i in range(1, 7)
    for r in range(6)
    for c in range(6)
)
print(f"  Nomizu operators exactly antisymmetric: {antisym == 0}")
assert antisym == 0


def cartan_on_m(h):
    A = sp.I * sp.diag(*h)
    out = sp.zeros(6, 6)
    for j in range(6):
        comm = A * M_BASIS[j] - M_BASIS[j] * A
        col = to_m(comm)
        for r in range(6):
            out[r, j] = col[r]
    return out


T2_M = [cartan_on_m((1, -1, 0)), cartan_on_m((0, 1, -1))]
print("  T^2 Cartan generators built exactly")

print()
print("=" * 78)
print("STEP 2c  exact spin_lift (Clifford), exact invariant sector via nullspace")
print("=" * 78)


def spin_lift_sym(L):
    out = sp.zeros(8, 8)
    for a in range(6):
        for b in range(a + 1, 6):
            if L[a, b] != 0:
                out += L[a, b] * sp.Rational(1, 2) * (E_sym[a + 1] * E_sym[b + 1])
    return out


def kron_sym(A, B):
    m, n, p, q = A.rows, A.cols, B.rows, B.cols
    out = sp.zeros(m * p, n * q)
    for i in range(m):
        for j in range(n):
            if A[i, j] != 0:
                out[i * p : (i + 1) * p, j * q : (j + 1) * q] = A[i, j] * B
    return out


I6, I8 = sp.eye(6), sp.eye(8)
RHO_SIGMA = [spin_lift_sym(g) for g in T2_M]
# CORRECTED sign (C152 Step 6's finding: [D,G]=0 for -T2_M, not +T2_M).
GENS48 = [kron_sym(RHO_SIGMA[k], I6) + kron_sym(I8, -T2_M[k]) for k in range(2)]


def sector_basis_exact(idx):
    block = [i * 6 + j for i in idx for j in range(6)]
    proj = sp.zeros(48, len(block))
    for col, g in enumerate(block):
        proj[g, col] = 1
    stacked = sp.Matrix.vstack(*[proj.T * g * proj for g in GENS48])
    ns = stacked.nullspace()
    basis = sp.zeros(48, len(ns))
    for col, v in enumerate(ns):
        basis[:, col] = proj * v
    return basis


dom_sym = sector_basis_exact(ODD_IDX)
tgt_sym = sector_basis_exact(EVEN_IDX)
print(
    f"  exact sector dims: domain {dom_sym.cols}, target {tgt_sym.cols}  (Stage 1b predicted 3,3)"
)
assert dom_sym.cols == 3 and tgt_sym.cols == 3

print()
print("=" * 78)
print("STEP 2d  exact equivariant connection family (nullspace, not SVD)")
print("=" * 78)


def equivariant_torsion_basis_exact(m_gens):
    n_unk = 90

    def unk(k, p_idx):
        return k * 15 + p_idx

    rows = []
    for ma in m_gens:
        for k in range(6):
            for i, j in PAIRS6:
                row = [sp.Integer(0)] * n_unk
                p = PAIRS6.index((i, j))
                for ell in range(6):
                    if ma[ell, k] != 0:
                        row[unk(ell, p)] += ma[ell, k]
                for m_ in range(6):
                    if m_ == i or ma[i, m_] == 0:
                        continue
                    ii, jj, sgn = m_, j, 1
                    if ii == jj:
                        continue
                    if ii > jj:
                        ii, jj, sgn = jj, ii, -1
                    pp = PAIRS6.index((ii, jj))
                    row[unk(k, pp)] -= sgn * ma[i, m_]
                for m_ in range(6):
                    if m_ == j or ma[j, m_] == 0:
                        continue
                    ii, jj, sgn = i, m_, 1
                    if ii == jj:
                        continue
                    if ii > jj:
                        ii, jj, sgn = jj, ii, -1
                    pp = PAIRS6.index((ii, jj))
                    row[unk(k, pp)] -= sgn * ma[j, m_]
                rows.append(row)
    mat = sp.Matrix(rows)
    ns = mat.nullspace()
    basis = sp.zeros(n_unk, len(ns))
    for col, v in enumerate(ns):
        basis[:, col] = v
    return basis


family_sym = equivariant_torsion_basis_exact(T2_M)
print(f"  exact family dimension: {family_sym.cols}  (Stage 0 predicted 6)")
assert family_sym.cols == 6

# regression: the Levi-Civita connection itself must lie in this exact family.
lc_vec = sp.zeros(90, 1)
for k in range(6):
    for p_idx, (i, j) in enumerate(PAIRS6):
        lc_vec[k * 15 + p_idx] = NOMIZU_LC[k + 1][i, j]
aug = family_sym.row_join(lc_vec)
in_family = aug.rank() == family_sym.rank()
print(f"  Levi-Civita connection lies exactly in the exact family: {in_family}")
assert in_family

print()
print("=" * 78)
print("STEP 2e  c_of, exact, built purely from the objects above")
print("=" * 78)


def c_of_exact(vec):
    lam = {}
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(PAIRS6):
            M[i, j] += vec[k * 15 + p_idx]
            M[j, i] -= vec[k * 15 + p_idx]
        lam[k + 1] = M
    D = sp.zeros(48, 48)
    for i in range(1, 7):
        D += kron_sym(E_sym[i] * spin_lift_sym(lam[i]), I6)
        D += kron_sym(E_sym[i], -lam[i])
    return tgt_sym.conjugate().T * D * dom_sym


c_lc = sp.simplify(c_of_exact(lc_vec))
print(f"  exact c(Levi-Civita), entry (0,0) = {c_lc[0, 0]}")
print(
    f"  entrywise |.|: {[sp.Abs(c_lc[r, c]) for r in range(3) for c in range(3) if c_lc[r, c] != 0]}"
)

print()
print("=" * 78)
print("STEP 2f  O(eps) = c(J_eps.v) - i*c(v), EXACT, for all 8 eps x 6 family directions")
print("=" * 78)


def acs_from_eps(eps):
    Jm = sp.zeros(6, 6)
    for k, e in enumerate(eps):
        Jm[2 * k, 2 * k + 1], Jm[2 * k + 1, 2 * k] = -e, e
    return Jm


# The claim is +-i (a NK structure and its conjugate give opposite
# orientation), so a direction "holds" if EITHER sign gives the exact zero
# matrix. A first pass here checked +i only and wrongly flagged (-1,-1,-1)
# as failing -- caught by re-reading the pre-registration's own "+-i"
# wording before trusting the result, fixed to check both signs.
exact_zero, exact_nonzero, sign_used = [], [], {}
for eps in product((1, -1), repeat=3):
    Jm = acs_from_eps(eps)
    per_dir_sign = []
    worst = sp.Integer(0)
    for k in range(family_sym.cols):
        v = family_sym[:, k]
        Jv = Jm.T * sp.Matrix(6, 15, lambda r, c, v=v: v[r * 15 + c])
        Jv_flat = sp.zeros(90, 1)
        for r in range(6):
            for c in range(15):
                Jv_flat[r * 15 + c] = Jv[r, c]
        cv = c_of_exact(v)
        cJv = c_of_exact(Jv_flat)
        Op = sp.simplify(cJv - sp.I * cv)
        Om = sp.simplify(cJv + sp.I * cv)
        zero_p = all(Op[r, c] == 0 for r in range(3) for c in range(3))
        zero_m = all(Om[r, c] == 0 for r in range(3) for c in range(3))
        if zero_p:
            per_dir_sign.append("+i")
        elif zero_m:
            per_dir_sign.append("-i")
        else:
            per_dir_sign.append(None)
            # this direction does not match EITHER sign exactly -- record
            # the actual +i-residual entry of largest magnitude as the
            # concrete witness (not the smaller-of-two, which was
            # confusingly close to zero and misleading to print).
            for r in range(3):
                for c in range(3):
                    if sp.Abs(Op[r, c]) > sp.Abs(worst):
                        worst = Op[r, c]
    signs_seen = set(per_dir_sign)
    all_zero = None not in signs_seen and len(signs_seen) == 1
    if all_zero:
        tag = f"EXACTLY ZERO on ALL 6 directions, uniform sign {signs_seen.pop()}"
    elif None not in signs_seen:
        # every direction individually holds, but with a MIXED sign pattern
        # -- a genuinely different structural finding, not a generic nonzero.
        tag = f"per-direction split, signs = {per_dir_sign}"
    else:
        tag = f"nonzero on >=1 direction, witness (+i-residual) = {worst}, signs = {per_dir_sign}"
    print(f"  eps={eps!s:>14}  {tag}")
    (exact_zero if all_zero else exact_nonzero).append(eps)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  exactly zero for   : {sorted(exact_zero)}")
print(f"  exactly nonzero for: {sorted(exact_nonzero)}")
matches = set(exact_zero) == {(1, 1, 1), (-1, -1, -1)}
print(f"  matches C152 Step 8's floating-point 2-of-8 pattern: {matches}")
if matches:
    print()
    print("  CONFIRMED EXACTLY. O(eps) is the identically zero linear map on the")
    print("  6-dim family for precisely the nearly-Kahler pair, built here from")
    print("  scratch in exact rational arithmetic with no floats anywhere.")

# ---------------------------------------------------------------------------
# STEP 2g -- NON-TAUTOLOGICAL Nijenhuis check, added after a context-blind
# FL Step 8a skeptic pass showed Step 1's relabelling test is VACUOUS: for
# ANY conjugate pair {b,-b}, relabelling by b itself ALWAYS gives
# {(1,1,1),(-1,-1,-1)} regardless of what b actually is (verified directly:
# relabel({(1,-1,1),(-1,1,-1)}, by=(1,-1,1)) and relabel({(1,1,1),(-1,-1,-1)},
# by=(1,1,1)) both give {(1,1,1),(-1,-1,-1)}). So Step 1 never actually
# tested whether non-integrability predicts the C-linear set -- it tested an
# identity of the relabelling arithmetic. This step computes the Nijenhuis
# tensor DIRECTLY in the ALIGNED basis (M_BASIS, already built above for
# eps=EPS_NK's alignment) for all 8 aligned eps, with NO relabelling step at
# all, and compares its zero-set DIRECTLY against the independently-known
# C-linear set. This can fail; the Step 1 version could not have.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 2g  NON-TAUTOLOGICAL check: Nijenhuis computed DIRECTLY in the")
print("         ALIGNED basis (no relabelling), for all 8 aligned eps")
print("=" * 78)


def make_J_aligned(eps):
    Jm = sp.zeros(6, 6)
    for k, e in enumerate(eps):
        Jm[2 * k, 2 * k + 1], Jm[2 * k + 1, 2 * k] = -e, e
    return Jm


def bracket_m_aligned(x, y):
    A = sum((x[i] * M_BASIS[i] for i in range(6)), sp.zeros(3, 3))
    B = sum((y[i] * M_BASIS[i] for i in range(6)), sp.zeros(3, 3))
    return to_m(A * B - B * A)


def nijenhuis_aligned(Jm):
    worst = sp.Integer(0)
    for i in range(6):
        for j in range(i + 1, 6):
            x = [sp.Integer(1) if k == i else sp.Integer(0) for k in range(6)]
            y = [sp.Integer(1) if k == j else sp.Integer(0) for k in range(6)]
            Jx = list(Jm[:, i])
            Jy = list(Jm[:, j])
            n = [
                a - b - c - d
                for a, b, c, d in zip(
                    bracket_m_aligned(Jx, Jy),
                    [sum(Jm[r, s] * bracket_m_aligned(Jx, y)[s] for s in range(6)) for r in range(6)],
                    [sum(Jm[r, s] * bracket_m_aligned(x, Jy)[s] for s in range(6)) for r in range(6)],
                    bracket_m_aligned(x, y),
                )
            ]
            for v in n:
                if abs(v) > abs(worst):
                    worst = v
    return worst


aligned_non_integrable = set()
for eps in product((1, -1), repeat=3):
    Jm = make_J_aligned(eps)
    n = nijenhuis_aligned(Jm)
    tag = "non-integrable" if n != 0 else "integrable"
    print(f"  aligned eps={eps!s:>14}  Nijenhuis (worst component) = {n!s:>6}   {tag}")
    if n != 0:
        aligned_non_integrable.add(eps)

print()
print(f"  aligned non-integrable set (computed DIRECTLY, no relabelling) : {sorted(aligned_non_integrable)}")
print(f"  aligned C-linear set (Step 2f, independent computation)        : {sorted(exact_zero)}")
direct_match = aligned_non_integrable == set(exact_zero)
print(f"  DIRECT MATCH (non-tautological): {direct_match}")
if direct_match:
    print("  CONFIRMED, non-tautologically: computed independently in the SAME")
    print("  coordinate system with NO relabelling step, non-integrability and")
    print("  global C-linearity pick out the exact same 2 of 8 structures.")
else:
    print("  Step 1's relabelling 'confirmation' does NOT survive a direct,")
    print("  non-tautological test. WITHDRAW the Nijenhuis-correlation claim.")
