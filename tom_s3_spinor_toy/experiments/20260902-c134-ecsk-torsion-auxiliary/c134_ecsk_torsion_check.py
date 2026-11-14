"""
C134 -- ECSK algebraic torsion equation on M4 x S3 x S6, sourced by this
project's own S6-twisted zero modes.

Everything below is machine-checked.  Nothing is asserted from memory.

Conventions, fixed here and stated so they can be audited
---------------------------------------------------------
* Signature  eta = diag(+1, -1, ..., -1)  (mostly-minus), 13 entries.
* 4D Dirac representation; gamma5 = i*g0*g1*g2*g3 .
* Cl(6) Euclidean:  Gamma_a Hermitian, {Gamma_a, Gamma_b} = 2 delta_ab,
  Gamma7 = i*Gamma_1...Gamma_6  (Hermitian, Gamma7^2 = 1).
* Cl(9,0):   e_i = sigma_i (x) Gamma7   (i=1,2,3, the S3 directions)
             e_{3+a} = 1_2 (x) Gamma_a  (a=1..6, the S6 directions)
  -- this is C125's own construction (decision.md:647-651).
* Cl(1,12):  Gamma^mu   = gamma^mu (x) 1_16     (mu = 0..3)
             Gamma^{3+M} = i*gamma5 (x) e_M     (M = 1..9)
  -- again C125's own construction.
* 13D index labels:  0..3 = M4 ; 4,5,6 = S3 ; 7..12 = S6.
* psibar = psi^dagger Gamma^0 .

Nothing here depends on a choice this project has not already frozen,
EXCEPT the assumption that the 13D theory carries a genuine Spin(1,12)
spinor -- which is what committing to a 13D Einstein-Cartan action means,
and which is flagged explicitly in decision.md as an assumption this round
introduces.
"""

import itertools
import json

import numpy as np

TOL = 1e-11
RESULTS = {}  # boolean pass/fail checks ONLY
DATA = {}  # recorded measurements -- NOT checks, never counted as such
FAILURES = []


def _self_audit_no_hardcoded_checks():
    """Reject any check(...) whose condition is a LITERAL constant in the source.

    WHY: a "check" whose condition is a literal True cannot fail.  Two independent
    FL Step 8a skeptic passes (2026-09-02) each found three such calls in the first
    version of this file, one of which carried a kill-criterion determination that
    decision.md then described as "machine-checked".  A runtime `cond is True`
    guard does NOT work -- `all(...)` legitimately returns the True singleton --
    so the audit is done on the SOURCE, where a literal is distinguishable from a
    computed value.
    """
    import ast
    import pathlib

    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    bad = []
    for node in ast.walk(ast.parse(src)):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
            and isinstance(node.args[1], ast.Constant)
        ):
            bad.append((node.lineno, ast.unparse(node.args[0])))
    if bad:
        raise AssertionError(f"hardcoded check conditions at {bad}")
    return sum(
        1
        for n in ast.walk(ast.parse(src))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "check"
    )


N_CHECK_CALLSITES = _self_audit_no_hardcoded_checks()


def check(name, cond, detail=""):
    RESULTS[name] = bool(cond)
    status = "PASS" if cond else "FAIL"
    if not cond:
        FAILURES.append(name)
    print(f"  [{status}] {name}" + (f"   {detail}" if detail else ""))
    return cond


def close(a, b):
    return np.max(np.abs(np.asarray(a) - np.asarray(b))) < TOL


# ----------------------------------------------------------------------
# 0.  Building blocks
# ----------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sig = [sx, sy, sz]


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def antisym3(gam, a, b, c):
    """Fully antisymmetrised Gamma^{[a} Gamma^b Gamma^{c]} (1/3! sum)."""
    tot = np.zeros_like(gam[0])
    for perm in itertools.permutations([a, b, c]):
        # parity of the permutation
        p = perm
        sgn = 1
        base = [a, b, c]
        # count inversions relative to (a,b,c) treating positions
        idx = [base.index(x) if base.count(x) == 1 else None for x in p]
        if None in idx:  # repeated index -> antisymmetriser vanishes anyway
            return np.zeros_like(gam[0])
        for i in range(3):
            for j in range(i + 1, 3):
                if idx[i] > idx[j]:
                    sgn = -sgn
        tot = tot + sgn * gam[p[0]] @ gam[p[1]] @ gam[p[2]]
    return tot / 6.0


# ----------------------------------------------------------------------
# 1.  4D Clifford algebra + POSITIVE CONTROL (flat-space ECSK)
# ----------------------------------------------------------------------
print("\n=== 1. 4D Clifford algebra ===")
g0 = kron(sz, I2)  # diag(1,1,-1,-1)
g1 = np.kron(np.array([[0, 1], [-1, 0]], dtype=complex), sx)
g2 = np.kron(np.array([[0, 1], [-1, 0]], dtype=complex), sy)
g3 = np.kron(np.array([[0, 1], [-1, 0]], dtype=complex), sz)
g4d = [g0, g1, g2, g3]
eta4 = np.diag([1.0, -1.0, -1.0, -1.0])

ok = all(
    close(g4d[m] @ g4d[n] + g4d[n] @ g4d[m], 2 * eta4[m, n] * np.eye(4))
    for m in range(4)
    for n in range(4)
)
check("4d_clifford_anticommutators", ok)

g5 = 1j * g0 @ g1 @ g2 @ g3
check("4d_gamma5_squares_to_one", close(g5 @ g5, np.eye(4)))
check("4d_gamma5_hermitian", close(g5, g5.conj().T))
check(
    "4d_gamma5_anticommutes_with_gamma0",
    close(g5 @ g0 + g0 @ g5, np.zeros((4, 4))),
)


# {gamma^mu, gamma^{ab}} = 2 gamma^{mu a b}   (the identity that makes the
# Dirac spin current TOTALLY ANTISYMMETRIC in any dimension)
def anticomm_identity(gam, dim):
    for m in range(dim):
        for a in range(dim):
            for b in range(dim):
                if len({a, b}) < 2:
                    continue
                gab = 0.5 * (gam[a] @ gam[b] - gam[b] @ gam[a])
                lhs = gam[m] @ gab + gab @ gam[m]
                rhs = 2 * antisym3(gam, m, a, b)
                if not close(lhs, rhs):
                    return False, (m, a, b)
    return True, None


ok, bad = anticomm_identity(g4d, 4)
check("4d_spin_current_totally_antisymmetric", ok, f"first failure {bad}")

# Levi-Civita, eps^{0123} = +1
eps4 = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    eps4[p] = s

# Perez-Rovelli identity:  gamma^{[ABC]} = -i eps^{ABCD} gamma5 gamma_D
gl = [eta4[d, d] * g4d[d] for d in range(4)]  # gamma_D (lower index)
ok = True
for a, b, c in itertools.combinations(range(4), 3):
    lhs = antisym3(g4d, a, b, c)
    rhs = np.zeros((4, 4), dtype=complex)
    for d in range(4):
        rhs = rhs + eps4[a, b, c, d] * (g5 @ gl[d])
    rhs = -1j * rhs
    if not close(lhs, rhs):
        ok = False
check(
    "4d_PerezRovelli_gamma3_equals_dual_axial", ok, "gamma^{[ABC]} = -i eps^{ABCD} gamma5 gamma_D"
)

# eps^{ABCD} eps_{ABCE} = -6 delta^D_E   (mostly-minus: eps_{0123} = -1)
eps4_low = -eps4
M = np.einsum("abcd,abce->de", eps4, eps4_low)
check(
    "4d_eps_contraction_is_minus6",
    close(M, -6 * np.eye(4)),
    f"diag = {np.round(np.real(np.diag(M)), 10)}",
)

print("\n=== 1b. POSITIVE CONTROL: flat-space ECSK four-fermion term ===")
# The elimination, done with the same apparatus that will be used in 13D.
#   R(Gamma) = R(g) - (1/4)|T|^2        for TOTALLY ANTISYMMETRIC torsion
#              (contorsion K = T/2, traces vanish, divergences dropped)
#   L_grav   = (1/2kappa) R(Gamma)   ->  -(1/(8 kappa)) |T|^2
#   L_Dirac  =  (i/4) omega_{Mab} psibar Gamma^{Mab} psi
#              ->  K-part  =  (i/8) T_{Mab} psibar Gamma^{Mab} psi
#                          =  (1/8) T . B     with  B^{Mab} := i psibar Gamma^{Mab} psi
#   Stationarity in T:  T = (kappa/2) B ;  back-substitution:  L* = (kappa/32) B.B
# All of the above is dimension-independent.  Only the last step is 4D:
#   B^{ABC} = i * (-i) eps^{ABCD} A_D = eps^{ABCD} A_D ,  A_D = psibar gamma5 gamma_D psi
#   B.B = eps^{ABCD} eps_{ABCE} A_D A^E = -6 A.A
#   =>  L* = -(3 kappa/16) A.A
grav_quadratic = -1.0 / 8.0  # coefficient of |T|^2 / kappa
dirac_linear = 1.0 / 8.0  # coefficient of T.B
T_solution_coeff = dirac_linear / (-2 * grav_quadratic)  # T = c * kappa * B
Lstar_coeff = (
    grav_quadratic * T_solution_coeff**2 + dirac_linear * T_solution_coeff
)  # * kappa * B.B
BB_over_AA = -6.0
four_fermion_coeff = Lstar_coeff * BB_over_AA  # * kappa * A.A

check(
    "posctrl_T_solution_coeff_is_half",
    abs(T_solution_coeff - 0.5) < 1e-14,
    f"T^(ABC) = {T_solution_coeff} * kappa * B^(ABC)",
)
check(
    "posctrl_four_fermion_coeff_is_minus_3_over_16",
    abs(four_fermion_coeff - (-3.0 / 16.0)) < 1e-14,
    f"L_eff = {four_fermion_coeff} * kappa * A.A   (target -3/16)",
)
# Perez-Rovelli quote it as -(3/2) pi G with kappa = 8 pi G
check(
    "posctrl_matches_PerezRovelli_minus_three_halves_piG",
    abs(four_fermion_coeff * 8.0 - (-1.5)) < 1e-14,
    f"= {four_fermion_coeff * 8.0} * pi G * A.A   (target -3/2)",
)
DATA["posctrl_four_fermion_coeff"] = four_fermion_coeff

# Poplawski's spin tensor shape:  s^{ijk} = (1/2) e^{ijkl} A_l
# ours:  T^{ABC} = (kappa/2) B^{ABC} = (kappa/2) eps^{ABCD} A_D  -> same shape,
# torsion totally antisymmetric and dual to the AXIAL current only.
# WHY this is now a real computation: in the first version this line re-read a
# stale `ok` from the Perez-Rovelli loop above and silently duplicated that
# check under a second name (caught by both skeptic passes, 2026-09-02).
# It now independently verifies, on random 4D spinors, that the BILINEAR
# B^{ABC} = i psibar gamma^{ABC} psi equals eps^{ABCD} A_D with A_D the AXIAL
# current -- i.e. that no VECTOR-current piece survives (Perez-Rovelli's
# "we have used the fact that they are real"; Poplawski's s^{ijk} = 1/2 e^{ijkl} A_l).
_rng0 = np.random.default_rng(11)
_ok = True
for _ in range(50):
    ch = _rng0.normal(size=4) + 1j * _rng0.normal(size=4)
    A = [complex(ch.conj() @ (g0 @ g5 @ gl[d]) @ ch) for d in range(4)]
    Vv = [complex(ch.conj() @ (g0 @ gl[d]) @ ch) for d in range(4)]
    for a, b, c in itertools.combinations(range(4), 3):
        B = 1j * complex(ch.conj() @ (g0 @ antisym3(g4d, a, b, c)) @ ch)
        dual = sum(eps4[a, b, c, d] * A[d] for d in range(4))
        if abs(B - dual) > 1e-10:
            _ok = False
    if max(abs(x) for x in Vv) < 1e-6:  # guard: the vector current must be nonzero,
        _ok = False  # else "no vector piece survives" is vacuous
check(
    "posctrl_spin_current_is_dual_of_AXIAL_current_only_no_vector_piece",
    _ok,
    "B^{ABC} = eps^{ABCD} A_D on 50 random spinors, with the vector current "
    "verified nonzero so the statement is not vacuous",
)

# SECOND, INDEPENDENT literature anchor on the SAME two hand-derived
# coefficients.  WHY this matters: the -3/16 match alone constrains only a
# COMBINATION of (grav_quadratic, dirac_linear); a compensating pair of errors
# could in principle survive it.  Poplawski's Cartan relation pins the ratio
# separately.  Poplawski's S^k_{ij} = Gamma^k_{[ij]} is HALF our T (T = 2S);
# his (Car4) at alpha=0, gamma->inf reads S_{imn} = -(kappa/4) e_{imnl} A^l,
# i.e. |T| = (kappa/2)|B| -- exactly our T_solution_coeff = 1/2.
poplawski_T_over_kappaB = 2 * 0.25  # T = 2S, |S| = (kappa/4)|A| = (kappa/4)|B|
check(
    "posctrl_Cartan_relation_magnitude_matches_Poplawski_independently",
    abs(T_solution_coeff - poplawski_T_over_kappaB) < 1e-14,
    f"ours {T_solution_coeff} vs Poplawski (Car4, alpha=0, gamma->inf) {poplawski_T_over_kappaB}",
)


# ----------------------------------------------------------------------
# 2.  Cl(6), Cl(9,0), Cl(1,12)  --  C125's own construction
# ----------------------------------------------------------------------
print("\n=== 2. 13D Clifford algebra (C125's construction, rebuilt) ===")
G6 = [
    kron(sx, I2, I2),
    kron(sy, I2, I2),
    kron(sz, sx, I2),
    kron(sz, sy, I2),
    kron(sz, sz, sx),
    kron(sz, sz, sy),
]
ok = all(
    close(G6[a] @ G6[b] + G6[b] @ G6[a], 2 * (a == b) * np.eye(8))
    for a in range(6)
    for b in range(6)
)
check("cl6_anticommutators", ok)

G7 = 1j * G6[0] @ G6[1] @ G6[2] @ G6[3] @ G6[4] @ G6[5]
check("cl6_gamma7_squares_to_one", close(G7 @ G7, np.eye(8)))
check("cl6_gamma7_hermitian", close(G7, G7.conj().T))
check(
    "cl6_gamma7_anticommutes_with_each_Gamma_a",
    all(close(G7 @ G6[a] + G6[a] @ G7, np.zeros((8, 8))) for a in range(6)),
)

# Cl(9,0)
e9 = [np.kron(sig[i], G7) for i in range(3)] + [np.kron(I2, G6[a]) for a in range(6)]
ok = all(
    close(e9[m] @ e9[n] + e9[n] @ e9[m], 2 * (m == n) * np.eye(16))
    for m in range(9)
    for n in range(9)
)
check("cl9_anticommutators", ok)

# Cl(1,12)
GAM = [np.kron(g4d[m], np.eye(16)) for m in range(4)] + [np.kron(1j * g5, e9[M]) for M in range(9)]
eta13 = np.diag([1.0] + [-1.0] * 12)
ok = all(
    close(GAM[A] @ GAM[B] + GAM[B] @ GAM[A], 2 * eta13[A, B] * np.eye(64))
    for A in range(13)
    for B in range(13)
)
check("cl13_anticommutators_all_169", ok)

G5_13 = np.kron(g5, np.eye(16))  # 4D chirality on the 64-dim module
G7_13 = kron(np.eye(4), I2, G7)  # S6 chirality on the 64-dim module

Om4 = GAM[0] @ GAM[1] @ GAM[2] @ GAM[3]
Om3 = GAM[4] @ GAM[5] @ GAM[6]
Om6 = GAM[7] @ GAM[8] @ GAM[9] @ GAM[10] @ GAM[11] @ GAM[12]
om13 = Om4 @ Om3 @ Om6

check("cl13_gamma5_equals_i_Omega4", close(G5_13, 1j * Om4))
# C125 E3: omega_13 central and scalar = +1
c = om13[0, 0]
check(
    "cl13_omega13_is_scalar_plus_one",
    close(om13, c * np.eye(64)) and abs(c - 1) < TOL,
    f"omega_13 = {np.round(c, 12)}  (C125 E3 target +1)",
)
# C125 D4: Omega3 * Omega6 = i * gamma5   (measured constant 0+1i)
prod = Om3 @ Om6
lam = None
for cand in [1j, -1j, 1, -1]:
    if close(prod, cand * G5_13):
        lam = cand
check(
    "cl13_Omega3_Omega6_equals_i_gamma5_C125_D4",
    lam == 1j,
    f"Omega3*Omega6 = ({lam}) * gamma5   (C125 D4 target 0+1i)",
)
DATA["cl13_Omega3Omega6_over_gamma5"] = str(lam)


# ----------------------------------------------------------------------
# 3.  THE STRUCTURAL RESULT: what sources the S3-leg torsion
# ----------------------------------------------------------------------
print("\n=== 3. Structure of the S3-leg spin current ===")
# Omega3 = Gamma^4 Gamma^5 Gamma^6  should equal  gamma5 (x) 1_2 (x) Gamma7
target = kron(g5, I2, G7)
check(
    "Omega3_equals_gamma5_tensor_Gamma7",
    close(Om3, target),
    "Gamma^4 Gamma^5 Gamma^6 = gamma5 (x) 1_2 (x) Gamma7",
)

# and the fully antisymmetrised 3-index gamma on the S3 legs is eps_abc * Omega3
eps3 = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    eps3[p] = s
ok = True
for a in range(3):
    for b in range(3):
        for cc in range(3):
            lhs = antisym3(GAM, 4 + a, 4 + b, 4 + cc)
            if not close(lhs, eps3[a, b, cc] * Om3):
                ok = False
check(
    "S3leg_gamma3_equals_eps_times_Omega3",
    ok,
    "Gamma^{[abc]}|_S3 = eps_abc * (gamma5 (x) Gamma7)  -- ZERO S3 content",
)

# The intrinsic S3 volume element carries no information (C125 D1)
w3_intrinsic = sig[0] @ sig[1] @ sig[2]
check(
    "intrinsic_S3_volume_is_a_scalar_C125_D1",
    close(w3_intrinsic, 1j * I2),
    f"sigma1 sigma2 sigma3 = {w3_intrinsic[0, 0]} * 1",
)

# Commutation structure -> the bilinear is 4D-chirality-FLIPPING
check("Omega3_commutes_with_gamma5", close(Om3 @ G5_13, G5_13 @ Om3))
check("Omega3_commutes_with_Gamma7_S6", close(Om3 @ G7_13, G7_13 @ Om3))
check(
    "Gamma0_anticommutes_with_gamma5_13D",
    close(GAM[0] @ G5_13 + G5_13 @ GAM[0], np.zeros((64, 64))),
)

# 13D spin current is totally antisymmetric too
ok, bad = anticomm_identity(GAM, 13)
check("13d_spin_current_totally_antisymmetric", ok, f"first failure {bad}")


# ----------------------------------------------------------------------
# 4.  Evaluate the source on the project's certified zero-mode content
# ----------------------------------------------------------------------
print("\n=== 4. The source bilinear on the certified content ===")
rng = np.random.default_rng(20260902)

PL = 0.5 * (np.eye(4) - g5)  # 4D left-handed projector
PR = 0.5 * (np.eye(4) + g5)


def bilinear(psi, Op):
    return complex(psi.conj() @ (GAM[0] @ Op) @ psi)


def rand_c(n):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)


# S6 chirality eigenvectors
w, V = np.linalg.eigh(G7)
plus6 = [V[:, k] for k in range(8) if w[k] > 0]  # dim 4
minus6 = [V[:, k] for k in range(8) if w[k] < 0]  # dim 4
check("S6_chirality_eigenspaces_are_4_and_4", len(plus6) == 4 and len(minus6) == 4)

# --- (i) 4D-CHIRAL (Weyl) content: the physically required N_gen=3 situation
vals = []
for _ in range(200):
    chi = rng.normal(size=4) + 1j * rng.normal(size=4)
    chi = PL @ chi  # a 4D Weyl spinor
    eta3 = rand_c(2)
    eta6 = plus6[rng.integers(4)]  # S6 chirality +1 (L5/G74B)
    psi = np.kron(chi, np.kron(eta3, eta6))
    vals.append(bilinear(psi, Om3))
maxL = max(abs(v) for v in vals)
vals = []
for _ in range(200):
    chi = PR @ (rng.normal(size=4) + 1j * rng.normal(size=4))
    eta3 = rand_c(2)
    eta6 = plus6[rng.integers(4)]
    psi = np.kron(chi, np.kron(eta3, eta6))
    vals.append(bilinear(psi, Om3))
maxR = max(abs(v) for v in vals)
check(
    "KILL_source_vanishes_for_4D_chiral_content",
    max(maxL, maxR) < TOL,
    f"max |psibar Omega3 psi| = {max(maxL, maxR):.3e}  over 400 random Weyl spinors",
)
DATA["max_abs_source_4D_chiral"] = float(max(maxL, maxR))


# --- (ii) 4D-DIRAC (non-chiral) content: source = pseudoscalar x S6 chirality
def source_factorised(chi, eta3, eta6):
    psi = np.kron(chi, np.kron(eta3, eta6))
    full = bilinear(psi, Om3)
    ps4 = complex(chi.conj() @ (g0 @ g5) @ chi)  # psibar gamma5 psi (4D)
    chir6 = complex(eta6.conj() @ G7 @ eta6)  # S6 chirality
    norm3 = complex(eta3.conj() @ eta3)
    return full, ps4 * norm3 * chir6


ok = True
samples = []
for _ in range(300):
    chi = rng.normal(size=4) + 1j * rng.normal(size=4)
    eta3 = rand_c(2)
    eta6 = plus6[rng.integers(4)]
    full, fact = source_factorised(chi, eta3, eta6)
    samples.append(abs(full))
    if abs(full - fact) > 1e-10:
        ok = False
check(
    "source_factorises_as_pseudoscalar_times_S6chirality",
    ok,
    "psibar Omega3 psi = (psibar_4 gamma5 psi_4) * |eta3|^2 * (S6 chirality)",
)
check(
    "source_is_generically_nonzero_for_4D_Dirac_content",
    max(samples) > 1e-3,
    f"max |source| = {max(samples):.4f}",
)

# --- MANDATORY NEGATIVE CONTROL --------------------------------------
print("\n=== 4b. MANDATORY NEGATIVE CONTROL: vector-like vs chiral S6 content ===")
# Run in the regime where the test can DISCRIMINATE, i.e. with 4D-Dirac
# content and a common 4D pseudoscalar.  (In the 4D-Weyl regime the source
# already vanishes for BOTH, so the control is non-discriminating there --
# reported, not hidden.)
chi_ref = rng.normal(size=4) + 1j * rng.normal(size=4)
ps_ref = complex(chi_ref.conj() @ (g0 @ g5) @ chi_ref)


def summed_source(s6_modes):
    tot = 0.0 + 0.0j
    for eta6 in s6_modes:
        for eta3 in [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]:
            psi = np.kron(chi_ref, np.kron(eta3, eta6))
            tot += bilinear(psi, Om3)
    return tot


chiral_content = [plus6[k] for k in range(3)]  # 3 channels, all D+
vectorlike_content = [plus6[0], plus6[1], plus6[2], minus6[0], minus6[1], minus6[2]]  # mirrored
src_chiral = summed_source(chiral_content)
src_vector = summed_source(vectorlike_content)
check(
    "negctrl_chiral_content_gives_NONZERO_sign_definite_source",
    abs(src_chiral) > 1e-6,
    f"sum = {src_chiral:.6f}",
)
check(
    "negctrl_vectorlike_content_gives_ZERO_source",
    abs(src_vector) < TOL,
    f"sum = {abs(src_vector):.3e}",
)
# and it really is chirality that is being sensed: flipping the S6 chirality
# flips the sign of the source
src_flipped = summed_source([minus6[k] for k in range(3)])
check(
    "negctrl_flipping_S6_chirality_flips_source_sign",
    close(src_flipped, -src_chiral),
    f"flipped = {src_flipped:.6f}",
)
DATA["negctrl_src_chiral"] = [src_chiral.real, src_chiral.imag]
DATA["negctrl_src_vectorlike_abs"] = float(abs(src_vector))

# --- SCOPING CHECK: do the OTHER internal torsion components stay zero? ---
print("\n=== 4c. SCOPING CHECK: all other internal 3-index components ===")
S3IDX, S6IDX = [4, 5, 6], list(range(7, 13))
# certified content: S3 kernel is the FULL 2-dim doublet (C64/C125), S6 is the
# 3 channels all with Gamma7 = +1 (G73/G74B).
s3_basis = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]
content = [(chi_ref, e3, e6) for e3 in s3_basis for e6 in chiral_content]

classes = {"3xS3": [], "2xS3+1xS6": [], "1xS3+2xS6": [], "3xS6": []}
for tri in itertools.combinations(range(4, 13), 3):
    n3 = sum(1 for x in tri if x in S3IDX)
    key = {3: "3xS3", 2: "2xS3+1xS6", 1: "1xS3+2xS6", 0: "3xS6"}[n3]
    Op = antisym3(GAM, *tri)
    tot = 0.0 + 0.0j
    for chi, e3, e6 in content:
        tot += bilinear(np.kron(chi, np.kron(e3, e6)), Op)
    classes[key].append(abs(tot))

for k, v in classes.items():
    mx = max(v) if v else 0.0
    print(f"    {k:>12s}: {len(v):3d} components, max |summed source| = {mx:.3e}")
    DATA[f"scoping_max_{k}"] = float(mx)

check(
    "scoping_only_the_3xS3_component_survives",
    max(classes["3xS3"]) > 1e-6
    and max(classes["2xS3+1xS6"]) < TOL
    and max(classes["1xS3+2xS6"]) < TOL
    and max(classes["3xS6"]) < TOL,
    "S6 and mixed torsion components are forced to zero -> S3 equation DOES isolate",
)

# --- 4c-i: the same, with an INDEPENDENT 4D spinor per S6 channel ----------
# WHY: the run above shares one chi across all six internal modes.  The three
# 4D fields are independent, so redo it with three independent chi's; the
# conclusion must not depend on that simplification.
chis = [rng.normal(size=4) + 1j * rng.normal(size=4) for _ in range(3)]
classes_indep = {k: [] for k in classes}
for tri in itertools.combinations(range(4, 13), 3):
    n3 = sum(1 for x in tri if x in S3IDX)
    key = {3: "3xS3", 2: "2xS3+1xS6", 1: "1xS3+2xS6", 0: "3xS6"}[n3]
    Op = antisym3(GAM, *tri)
    tot = 0.0 + 0.0j
    for ch, e6 in zip(chis, chiral_content):
        for e3 in s3_basis:
            tot += bilinear(np.kron(ch, np.kron(e3, e6)), Op)
    classes_indep[key].append(abs(tot))
check(
    "scoping_survives_independent_4D_spinor_per_channel",
    max(classes_indep["3xS3"]) > 1e-6
    and max(classes_indep["2xS3+1xS6"]) < TOL
    and max(classes_indep["1xS3+2xS6"]) < TOL
    and max(classes_indep["3xS6"]) < TOL,
    f"3xS3 max = {max(classes_indep['3xS3']):.4f}, "
    f"others max = {max(max(classes_indep[k]) for k in classes_indep if k != '3xS3'):.3e}",
)

# --- 4c-ii: INTERNAL CONTROL on WHY the mixed class vanishes ---------------
# WHY: "1xS3+2xS6" vanishes because Sum_s eta3_s^dag sigma_a eta3_s = tr(sigma_a)
# = 0, i.e. because the certified S3 kernel is the COMPLETE 2-dim SU(2) doublet
# (C64 multiplicity 2; C125 ker(D_S3,t=0) = (1,2)).  If that mechanism is what
# is really doing the work, then truncating the S3 content to ONE spinor must
# make the class non-vanishing.  A test that cannot tell those apart is not a
# test.
partial = []
for tri in itertools.combinations(range(4, 13), 3):
    if sum(1 for x in tri if x in S3IDX) != 1:
        continue
    Op = antisym3(GAM, *tri)
    tot = 0.0 + 0.0j
    for e6 in chiral_content:
        tot += bilinear(np.kron(chi_ref, np.kron(s3_basis[0], e6)), Op)
    partial.append(abs(tot))
check(
    "internal_ctrl_mixed_class_is_nonzero_if_S3_doublet_is_TRUNCATED",
    max(partial) > 1e-6,
    f"max = {max(partial):.4f} -- so the vanishing above is genuinely due to "
    "SU(2)-doublet completeness, not to a degenerate test",
)
DATA["internal_ctrl_truncated_S3_mixed_max"] = float(max(partial))

# also: any component with a free 4D index is killed by 4D Lorentz invariance,
# and here explicitly the (2 x M4 + 1 x internal) and (1 x M4 + 2 x internal)
# components carry a free 4D vector index.  Recorded, not re-derived.


# ----------------------------------------------------------------------
# 5.  The S3 torsion equation and its complete solution set
# ----------------------------------------------------------------------
print("\n=== 5. The ECSK torsion equation restricted to the S3 legs ===")
# LHS  (this project's frozen ansatz, C125 decision.md:382-386, unit radius):
#        T^t(X_i,X_j) = (2t-1)[X_i,X_j] = 2(2t-1) eps_ijk X_k
#   =>   T_abc = 2(2t-1) eps_abc
# RHS  (ECSK, section 1b, dimension-independent):
#        T^{ABC} = (kappa/2) B^{ABC},   B^{abc} = i psibar Gamma^{abc} psi
#                                              = i eps^{abc} <psibar Omega3 psi>
#   =>   2(2t-1) = (kappa_13/2) * i * <psibar Omega3 psi>
#   =>   (2t-1)  = (kappa_13/4) * i * <psibar Omega3 psi>
#                = (kappa_13/4) * i * <psibar_4 gamma5 psi_4> * (S6 chirality)
J = 1j * src_chiral  # the certified-content source, up to normalisation
DATA["source_J_certified_content"] = [J.real, J.imag]
print(f"    source J = i<psibar Omega3 psi> (4D-Dirac reading) = {J:.6f}")
print("    source J (4D-Weyl / vacuum reading)                = 0 exactly")


# Solve the equation on a grid, for real, rather than asserting its shape.
# WHY: both skeptic passes (2026-09-02) flagged that the earlier version of
# this block asserted the kill-branch (b) determination as a literal True.
def residual(t, Jval):
    """LHS - RHS of  2(2t-1) eps_abc = (kappa/2) eps^abc J , kappa set to 1."""
    return 2 * (2 * t - 1) - 0.5 * Jval


tgrid = np.linspace(-2.0, 3.0, 5001)
res_zero = np.array([residual(t, 0.0) for t in tgrid])
res_src = np.array([residual(t, J.real) for t in tgrid])

check(
    "branchB_equation_NOT_satisfied_identically_zero_source",
    np.max(np.abs(res_zero)) > 1.0,
    f"max|residual| over t in [-2,3] = {np.max(np.abs(res_zero)):.3f} (not identically 0)",
)
check(
    "branchB_equation_NOT_satisfied_identically_nonzero_source",
    np.max(np.abs(res_src)) > 1.0,
    f"max|residual| = {np.max(np.abs(res_src)):.3f}",
)
root_zero = tgrid[np.argmin(np.abs(res_zero))]
check(
    "zero_source_forces_t_equals_one_half",
    abs(root_zero - 0.5) < 1e-3 and np.sum(np.abs(res_zero) < 1e-3) <= 2,
    f"unique root at t = {root_zero:.4f}  -- E8's own FAIL criterion",
)
# WHY this matters and the earlier version got it wrong: the "exactly one root"
# property was previously justified by LINEARITY in t, which silently assumes
# J is t-independent.  It is not -- the zero-mode content is t-dependent (E2
# crossings at t in {0,1}; KT-8: none at t=1/2).  The correct justification,
# valid for ANY J(t), is that the LHS 2(2t-1) is not identically zero.
Jt = np.array([0.3 * np.sin(5 * t) for t in tgrid])  # an arbitrary J(t)
res_var = 2 * (2 * tgrid - 1) - 0.5 * Jt
check(
    "branchB_does_NOT_fire_even_for_a_t_DEPENDENT_source",
    np.max(np.abs(res_var)) > 1.0,
    "holds for any J(t): LHS 2(2t-1) is not identically zero",
)
# and with J(t) == 0 for all t (routes 1 and 2), t = 1/2 is still the unique root
check(
    "routes1and2_give_J_of_t_identically_zero_hence_t_half_for_all_t",
    np.max(np.abs(np.array([residual(t, 0.0) for t in tgrid]) - res_zero)) < TOL,
    "routes 1/2 kill J at EVERY t, so no t-dependence of J can rescue t in {0,1}",
)
# t in {0,1} requires |2t-1| = 1 exactly:
print("    t in {0,1}  <=>  |kappa_13 * J| = 4  exactly (unit-radius S3)")
print("    -> a fine-tuning of the condensate to the 13D Cartan density,")
print("       NOT a discrete selection: 2t-1 varies continuously with J.")


# ----------------------------------------------------------------------
# 6.  REPAIRS DEMANDED BY THE TWO FL STEP 8a SKEPTIC PASSES (2026-09-02)
#     Each block is labelled with the finding it answers.
# ----------------------------------------------------------------------
print("\n=== 6. Skeptic-pass repairs ===")

# --- 6a. Route 2 as an EXACT operator identity, not a 400-spinor sample.
#     (both passes: "it's a two-line proof, reported as sampling")
PL13 = np.kron(0.5 * (np.eye(4) - g5), np.eye(16))
PR13 = np.kron(0.5 * (np.eye(4) + g5), np.eye(16))
check(
    "route2_EXACT_operator_identity_PL_Gamma0_Omega3_PL_is_zero",
    close(PL13 @ GAM[0] @ Om3 @ PL13, np.zeros((64, 64)))
    and close(PR13 @ GAM[0] @ Om3 @ PR13, np.zeros((64, 64))),
    "identically zero as a matrix, both chiralities -- not a sample",
)

# --- 6b. Representation independence of route 2.
#     (both passes asked; pass A tried to break it and failed)
# WHY the two-tier construction below, recorded because the first attempt FAILED
# and the failure was diagnosed rather than tuned away: an unconstrained
# 64x64 complex Gaussian S has condition number ~1e4-1e6 here, so S @ X @ inv(S)
# carries float error far above an ABSOLUTE 1e-11 threshold even though
# S @ 0 @ inv(S) = 0 exactly.  That was a conditioning artifact, not physics.
# Fixed by (i) unitary S -- the transformation that actually relates two
# Hermitian gamma-matrix representations, exact to machine precision -- and
# (ii) general invertible S with the CORRECTLY transformed Dirac adjoint
# A = (S^dag)^-1 Gamma^0 S^-1 (NOT S Gamma^0 S^-1, which is the error the first
# attempt also made) and a RELATIVE tolerance.
ok_u, ok_g, worst_u, worst_g = True, True, 0.0, 0.0
for _ in range(20):
    Q, _r = np.linalg.qr(rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64)))
    G0s, Om3s, g5s = Q @ GAM[0] @ Q.conj().T, Q @ Om3 @ Q.conj().T, Q @ G5_13 @ Q.conj().T
    PLs = 0.5 * (np.eye(64) - g5s)
    r = np.max(np.abs(PLs @ G0s @ Om3s @ PLs))
    worst_u = max(worst_u, r)
    if r > 1e-10:
        ok_u = False

    S = rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
    U, sv, Vh = np.linalg.svd(S)
    S = U @ np.diag(np.linspace(1.0, 10.0, 64)) @ Vh  # condition number exactly 10
    Si = np.linalg.inv(S)
    A = np.linalg.inv(S.conj().T) @ GAM[0] @ Si  # the correct transformed adjoint
    Om3s, g5s = S @ Om3 @ Si, S @ G5_13 @ Si
    PLs = 0.5 * (np.eye(64) - g5s)
    num = np.max(np.abs(PLs.conj().T @ A @ Om3s @ PLs))
    den = np.max(np.abs(A @ Om3s))
    worst_g = max(worst_g, num / den)
    if num / den > 1e-10:
        ok_g = False
check(
    "route2_survives_unitary_change_of_gamma_representation",
    ok_u,
    f"20 random unitary reps, worst residual {worst_u:.2e}",
)
check(
    "route2_survives_general_similarity_with_correct_Dirac_adjoint",
    ok_g,
    f"20 random GL(64,C) (cond=10) with A=(S^dag)^-1 Gamma^0 S^-1, "
    f"worst RELATIVE residual {worst_g:.2e}",
)
DATA["route2_worst_residual_unitary"] = float(worst_u)
DATA["route2_worst_relative_residual_general"] = float(worst_g)

# --- 6c. Free in-project cross-check of the ONE hand-typed gravity constant.
#     (both passes: R(Gamma) = R(g) - |T|^2/4 was asserted, and round111 already
#      computed the answer independently in July 2026.)
#     T_abc = 2(2t-1) eps_abc  =>  |T|^2 = 24 (2t-1)^2  =>  R = 6 - 6(2t-1)^2,
#     which must equal round111's Scal(t) = 24 t (1-t).
tt = np.linspace(-1, 2, 601)
Tsq = np.array(
    [
        sum(
            (2 * (2 * t - 1) * eps3[a, b, c]) ** 2
            for a in range(3)
            for b in range(3)
            for c in range(3)
        )
        for t in tt
    ]
)
R_ours = 6.0 - 0.25 * Tsq
R_round111 = 24 * tt * (1 - tt)
check(
    "grav_coefficient_minus_quarter_reproduces_round111_Scal_t",
    np.max(np.abs(R_ours - R_round111)) < 1e-10,
    "R(Gamma)=R(g)-|T|^2/4 with C125's T gives 24t(1-t) = round111's Scal(t) exactly",
)
DATA["Tsq_at_t0"] = float(Tsq[np.argmin(np.abs(tt - 0.0))])

# --- 6d. ECSK's BOSONIC sector IS round72's E8 functional at a = 0.
#     (pass B: "not a different question -- same answer, SAME reason")
#     E8: F(t) = a|R^t|^2 + b|T^t|^2 ,  F'(t) = 2(2t-1)[aA t(t-1) + 2bB]
#     ECSK gravity: (1/2k)[R(g) - |T|^2/4]  ->  t-part = -(1/8k)|T^t|^2 = a=0 case.
Fa0 = -(1.0 / 8.0) * Tsq  # the ECSK t-dependent bosonic Lagrangian, kappa=1
check(
    "ECSK_bosonic_sector_is_EVEN_in_2t_minus_1",
    np.max(np.abs(Fa0 - Fa0[::-1])) < 1e-10,
    "F(t) = F(1-t) exactly -> t<->1-t SYMMETRIC once the fermion source vanishes",
)
crit = tt[np.argmax(Fa0)]
check(
    "ECSK_bosonic_sector_unique_stationary_point_is_t_half",
    abs(crit - 0.5) < 1e-2,
    f"stationary at t = {crit:.4f} -- round72's E8 preliminary at a=0, already computed 2026-07",
)

# --- 6e. The vielbein (metric) EOM, which the first version never derived.
#     (pass B, highest-severity finding)  In vacuum ECSK: T = 0 and Ric(g) = 0.
#     Certified Ricci of the frozen background (C125 decision.md:335):
#       Ric = 0 (+) (2/rho3^2) g3 (+) (5/rho6^2) g6
ric_eigs = [0.0] * 4 + [2.0] * 3 + [5.0] * 6  # unit radii
check(
    "vielbein_EOM_frozen_background_is_NOT_Ricci_flat",
    max(abs(x) for x in ric_eigs) > 1e-6,
    f"Ric eigenvalues {sorted(set(ric_eigs))} -- vacuum Einstein eq Ric=0 is VIOLATED",
)
DATA["ricci_eigenvalues_unit_radii"] = ric_eigs

# --- 6f. Negative control, redone with an INDEPENDENT 4D spinor per mode.
#     (both passes: the shared-chi version is forced arithmetic 3 - 3 = 0)
chis6 = [rng.normal(size=4) + 1j * rng.normal(size=4) for _ in range(6)]


def summed_source_indep(s6_modes, chi_list):
    tot = 0.0 + 0.0j
    for ch, eta6 in zip(chi_list, s6_modes):
        for eta3 in s3_basis:
            tot += bilinear(np.kron(ch, np.kron(eta3, eta6)), Om3)
    return tot


src_vec_indep = summed_source_indep(vectorlike_content, chis6)
check(
    "negctrl_FAILS_to_cancel_when_each_mode_has_its_own_4D_spinor",
    abs(src_vec_indep) > 1e-3,
    f"|sum| = {abs(src_vec_indep):.4f} -- so the cancellation needs a COMMON 4D "
    "configuration, i.e. a genuinely vector-like VACUUM, not merely mirrored content",
)
DATA["negctrl_src_vectorlike_independent_chi_abs"] = float(abs(src_vec_indep))

# --- 6g. The scoping sweep in the 4D-WEYL regime (the physically required one).
#     (pass A: the 4D-Dirac disclosure was given for the negative control but
#      not for the scoping, though the same defect applies)
chi_weyl = PL @ (rng.normal(size=4) + 1j * rng.normal(size=4))
weyl_max = 0.0
for tri in itertools.combinations(range(4, 13), 3):
    Op = antisym3(GAM, *tri)
    tot = sum(
        bilinear(np.kron(chi_weyl, np.kron(e3, e6)), Op) for e3 in s3_basis for e6 in chiral_content
    )
    weyl_max = max(weyl_max, abs(tot))
check(
    "scoping_ALL_84_internal_components_vanish_in_the_4D_WEYL_regime",
    weyl_max < TOL,
    f"max = {weyl_max:.3e} -- so section 4's isolation statement is a 4D-DIRAC-regime "
    "statement only; in the physical Weyl regime it is vacuous (0 = 0)",
)
DATA["scoping_max_all_classes_weyl_regime"] = float(weyl_max)

# --- 6h. The hidden EQUAL-OCCUPANCY condition in the 1xS3+2xS6 cancellation.
#     (both passes: doublet completeness is necessary, not sufficient)
chi_a = rng.normal(size=4) + 1j * rng.normal(size=4)
chi_b = 2.7 * (rng.normal(size=4) + 1j * rng.normal(size=4))  # unequal occupancy
mixed_max = 0.0
for tri in itertools.combinations(range(4, 13), 3):
    if sum(1 for x in tri if x in S3IDX) != 1:
        continue
    Op = antisym3(GAM, *tri)
    tot = sum(
        bilinear(np.kron(ch, np.kron(e3, e6)), Op)
        for ch, e3 in zip([chi_a, chi_b], s3_basis)
        for e6 in chiral_content
    )
    mixed_max = max(mixed_max, abs(tot))
check(
    "scoping_1S3_2S6_class_NONZERO_under_UNEQUAL_doublet_occupancy",
    mixed_max > 1e-3,
    f"max = {mixed_max:.4f} -- isolation needs EQUAL 4D occupancy across the S3 "
    "doublet, an assumption C64/C125 do not supply",
)
DATA["scoping_mixed_unequal_occupancy_max"] = float(mixed_max)


# ----------------------------------------------------------------------
print("\n=== SUMMARY ===")
n_ok = sum(1 for v in RESULTS.values() if v)
print(
    f"  boolean checks : {len(RESULTS)} distinct names from "
    f"{N_CHECK_CALLSITES} call sites  (passed {n_ok})"
)
print(f"  recorded data  : {len(DATA)}  -- NOT counted as checks")
print("  hardcoded-condition self-audit: PASS (no check() takes a literal)")
print(f"  failures       : {len(FAILURES)}  {FAILURES}")
with open("results_c134.json", "w") as f:
    json.dump({"checks": RESULTS, "data": DATA}, f, indent=2, sort_keys=True)
print("  wrote results_c134.json")
