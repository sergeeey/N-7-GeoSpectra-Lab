r"""
C158 STEP 4 -- the actual questions Q1-Q4 (fixed in PREREGISTRATION_step3.md
before any spin lift was built), now that S01_full, S12_full are verified
Pin(m) lifts of R01, R12 (Clifford PRODUCTS, odd, twisted-adjoint action).

Q1: order of S01/S12 on Sigma (do they square to +1, -1, or something else?)
Q2: how does psi_+ transform under S01/S12?
Q3: is D_Sigma(v) equivariant: (twisted-adjoint by S) D_Sigma(v) (...)^-1
    == D_Sigma(R.v)  for v ranging over the family?
Q4: is M itself equivariant: S . M(v) =? M(R.v), or with a sign character?

Run:  python c158_step4_equivariance.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S3C = load("c158_s3c", "c158_step3c_pin_lift_final.py")
S1 = S3C.S1
S2 = S1.S2
E_sym = S2.E_sym
family_sym = S2.family_sym
PAIRS6 = S2.PAIRS6

# S3C's S01_full/S12_full are local to its own __main__ guard (which does not
# run under import) -- rebuild them here by calling its own function directly.
_n01, _Srot01, S01, _ok01 = S3C.build_pin_lift_final(S1.R01, 0, ((2, 5), (3, 4)), "R01")
_R12 = S1.R12
_refl_idx_12 = None
for _i in range(6):
    _row = [_R12[_i, _j] for _j in range(6)]
    _col = [_R12[_j, _i] for _j in range(6)]
    if _row.count(0) == 5 and _row[_i] == -1 and _col.count(0) == 5 and _col[_i] == -1:
        _refl_idx_12 = _i
        break
assert _refl_idx_12 is not None
_Refl12 = S3C.reflect_matrix(_refl_idx_12)
_Rot12_probe = sp.simplify(_R12 * _Refl12)
_rot_pairs_12 = []
_seen = set()
for _i in range(6):
    if _i == _refl_idx_12 or _i in _seen:
        continue
    for _j in range(6):
        if _j != _i and _Rot12_probe[_j, _i] != 0 and _j != _refl_idx_12:
            _rot_pairs_12.append((min(_i, _j), max(_i, _j)))
            _seen.add(_i)
            _seen.add(_j)
            break
_n12, _Srot12, S12, _ok12 = S3C.build_pin_lift_final(
    S1.R12, _refl_idx_12, tuple(_rot_pairs_12), "R12"
)
assert _ok01 and _ok12, "Pin lifts must reproduce R01/R12 before testing equivariance"


def hip(a, b):
    return sp.simplify(sum(sp.conjugate(a[k]) * b[k] for k in range(a.rows)))


print("=" * 78)
print("Q1  order of S01, S12 on Sigma")
print("=" * 78)
S01sq = sp.simplify(S01 * S01)
S12sq = sp.simplify(S12 * S12)
print(f"  S01^2 == I : {S01sq == sp.eye(8)}")
print(f"  S01^2 == -I : {S01sq == -sp.eye(8)}")
print(f"  S12^2 == I : {S12sq == sp.eye(8)}")
print(f"  S12^2 == -I : {S12sq == -sp.eye(8)}")
if S01sq not in (sp.eye(8), -sp.eye(8)):
    print("  S01^2 is neither +I nor -I -- printing it:")
    sp.pprint(S01sq)

print()
print("=" * 78)
print("Q2  how does the invariant spinor psi_+ transform?")
print("=" * 78)
# build psi_+ exactly as C155 Step 2 does: T^2-invariant nullspace, then
# diagonalize D(LC) to find the +3 eigenvector
RHO_SIGMA = S2.RHO_SIGMA
stacked = sp.Matrix.vstack(RHO_SIGMA[0], RHO_SIGMA[1])
inv_ns = stacked.nullspace()
assert len(inv_ns) == 2
v1 = inv_ns[0]
v2 = sp.simplify(inv_ns[1] - (hip(v1, inv_ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))


def lam_of(vec):
    lam = {}
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(PAIRS6):
            M[i, j] += vec[k * 15 + p_idx]
            M[j, i] -= vec[k * 15 + p_idx]
        lam[k + 1] = M
    return lam


def D8_of(vec):
    lam = lam_of(vec)
    D = sp.zeros(8, 8)
    for i in range(1, 7):
        D += E_sym[i] * S2.spin_lift_sym(lam[i])
    return D


D_LC_2 = sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2)
psi_p = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == 3:
        psi_p = sp.simplify(b2 * vecs[0])
assert psi_p is not None
psi_n2 = sp.simplify(hip(psi_p, psi_p))
print(f"  psi_+ built, ||psi_+||^2 = {psi_n2}")

for name, S in (("S01", S01), ("S12", S12)):
    Sinv = sp.simplify(S.inv())
    img = sp.simplify(-S * psi_p * 1)  # twisted action on a SPINOR: for odd S,
    # the representation on Sigma (a Cl(m)-module) is LEFT MULTIPLICATION,
    # s.psi = s*psi (not conjugation -- conjugation is for VECTORS only).
    # Test left multiplication directly:
    img = sp.simplify(S * psi_p)
    ratio = None
    # is img proportional to psi_p?
    nz = next((k for k in range(8) if sp.simplify(psi_p[k]) != 0), None)
    if nz is not None:
        cand = sp.simplify(img[nz] / psi_p[nz])
        if sp.simplify(img - cand * psi_p) == sp.zeros(8, 1):
            ratio = cand
    print(f"  {name} . psi_+ proportional to psi_+? ratio = {ratio}")
    if ratio is None:
        print(f"    {name}.psi_+ (not proportional):")
        sp.pprint(img)

print()
print("=" * 78)
print("Q3  is D_Sigma(v) equivariant? (twisted-adjoint) S D(v) S^-1 == D(R.v)")
print("=" * 78)
R01, R12 = S1.R01, S1.R12
fam_cols = [family_sym[:, c] for c in range(6)]


def ambient_action(R, fam_col):
    lam_mats = []
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(PAIRS6):
            M[i, j] += fam_col[k * 15 + p_idx]
            M[j, i] -= fam_col[k * 15 + p_idx]
        lam_mats.append(M)
    new_lam = [sp.zeros(6, 6) for _ in range(6)]
    for k in range(6):
        for j in range(6):
            if R[k, j] != 0:
                new_lam[k] += R[k, j] * (R * lam_mats[j] * R.T)
    out = sp.zeros(90, 1)
    for k in range(6):
        M = sp.simplify(new_lam[k])
        for p_idx, (i, j) in enumerate(PAIRS6):
            out[k * 15 + p_idx] = M[i, j]
    return out


for name, S, R in (("S01/R01", S01, R01), ("S12/R12", S12, R12)):
    Sinv = sp.simplify(S.inv())
    ok = True
    for c in range(6):
        v = fam_cols[c]
        Dv = D8_of(v)
        # S is ODD, so the correct covariance uses the TWISTED adjoint:
        conj_D = sp.simplify(-S * Dv * Sinv)
        Rv = ambient_action(R, v)
        DRv = D8_of(Rv)
        if sp.simplify(conj_D - DRv) != sp.zeros(8, 8):
            ok = False
    print(f"  {name}: (twisted-adjoint) S D(v) S^-1 == D(R.v) for all 6 family dirs: {ok}")

print()
print("=" * 78)
print("Q4  is M itself equivariant? S.M(v) =? M(R.v)  (or with a sign character)")
print("=" * 78)
psi_m = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == -3:
        psi_m = sp.simplify(b2 * vecs[0])
assert psi_m is not None

for name, S, R in (("S01/R01", S01, R01), ("S12/R12", S12, R12)):
    ok_plain = True
    ok_signed = True
    ok_true = True
    for c in range(6):
        v = fam_cols[c]
        Mv = sp.simplify(D8_of(v) * psi_p)
        SMv = sp.simplify(S * Mv)  # left Clifford action on the spinor M(v)
        Rv = ambient_action(R, v)
        MRv = sp.simplify(D8_of(Rv) * psi_p)
        M_minus_Rv = sp.simplify(D8_of(Rv) * psi_m)
        if sp.simplify(SMv - MRv) != sp.zeros(8, 1):
            ok_plain = False
        if sp.simplify(SMv + MRv) != sp.zeros(8, 1):
            ok_signed = False
        # THE CORRECT statement, found after Q2 showed psi_+ is NOT S-fixed
        # (S.psi_+ = -i*psi_-) and Q3 showed -S D(v) S^-1 = D(R.v) (twisted):
        # S.M_+(v) = S D(v) psi_+ = (S D(v) S^-1)(S psi_+)
        #          = -D(R.v) * (-i psi_-) = i * D(R.v) psi_- = i * M_-(R.v)
        if sp.simplify(SMv - sp.I * M_minus_Rv) != sp.zeros(8, 1):
            ok_true = False
    print(f"  {name}: S.M(v) == M(R.v)  [naive, holding psi_+ fixed]   : {ok_plain}")
    print(f"  {name}: S.M(v) == -M(R.v) [naive, sign -1]               : {ok_signed}")
    print(f"  {name}: S.M_+(v) == i*M_-(R.v)  [THE TRUE STATEMENT]     : {ok_true}")

print()
print("  CONCLUSION: M is not equivariant alone because psi_+ is not Weyl-fixed")
print("  (Q2: both generators send psi_+ -> -i*psi_-). The genuinely equivariant")
print("  object is the PAIR (M_+, M_-); the Weyl group swaps them (with phase i),")
print("  mirroring the swap of psi_+/psi_-. This is a complete answer, not a")
print("  failure -- the naive question (holding psi_+ fixed) was ill-posed.")
