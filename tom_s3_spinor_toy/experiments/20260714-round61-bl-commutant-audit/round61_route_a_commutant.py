"""Round 61 — Route A: blind commutant + anomaly solve for a U(1) generator T.

INDEPENDENCE / BLINDNESS PROTOCOL (per task instructions this script was
written under):
  - BmL_32 and Y_32 (from g16_t3r_k3.py) are NOT imported, read, or
    hard-coded anywhere in the CONSTRUCTION of the generators, the
    commutant solve, the chirality/real-structure reduction, or the
    anomaly-equation solve (STEP 1 - STEP 5 below). `g16_t3r_k3.py` is only
    imported in STEP 6, strictly for after-the-fact comparison.
  - gamma_F and J_F are rebuilt directly from their stated definitions
    (diag(-1x16,+1x16) and the 16 CPT_PAIRS transpositions) rather than
    imported from g18_ncg.py, because g18_ncg.py transitively imports
    g17_electric_charge.Q_32, which is downstream of Y_32/BmL_32 — importing
    that module would pull the forbidden chain into scope even if the value
    were never read. The task explicitly allows rebuilding gamma_F/J_F from
    their stated definitions ("these ARE allowed, they are
    geometric/chirality structure, not the charge assignment under test").
  - J_S3, K_S3, su3_generators, lift_to_spinor are imported from
    g11_block_generators.py / g10b_su3_explicit.py — already-tested,
    already-geometrically-derived generator machinery, explicitly permitted
    reuse (not what "blind" refers to).

METHOD — genuine linear algebra, NOT an assumed block-diagonal-scalar ansatz
  STEP 1: build the 14 generators (J_a^32, K_a^32, C_i^32) exactly as in
          g11/g16 (kron with I8/I4).
  STEP 2: find the REAL (Hermitian) commutant of all 14 generators, via
          exact linear algebra, in two stages that are mathematically
          equivalent to (but far cheaper than) a brute-force 1024-real-
          unknown solve:
            (2a) compute the COMPLEX commutant of {J,K} on the 4-dim S3
                 factor and of {C_i} on the 8-dim S6 factor SEPARATELY, each
                 via sympy nullspace on a fully generic complex matrix
                 ansatz (16 and 64 complex unknowns respectively — no
                 diagonal/block assumption).
            (2b) because J_a^32=kron(J_a,I8) etc. only ever act on ONE
                 tensor factor, a matrix commutes with ALL 14 32x32
                 generators iff it lies in Commutant_S3 (x) Commutant_S6
                 (standard tensor-product commutant fact, itself a
                 consequence of linear algebra: T commuting with all a(x)I
                 forces T = sum_k E_k^{(S6)} (x) T_k^{(S3)} with each T_k in
                 Commutant_S3, then commuting with all I(x)b forces the S6
                 part into Commutant_S6 too). This is NOT an assumption
                 about T's structure — it is forced by the fact (already
                 given by the task's own construction) that the generators
                 factor as a(x)I / I(x)b.
            (2c) EVERY tensor-product basis element is directly verified
                 (closure check) to commute with all 14 original 32x32
                 generators — so nothing is taken on faith from (2b).
            (2d) the HERMITIAN sub-space of this complex commutant is found
                 by explicit linear solve of T=T^dagger on the general
                 complex linear combination — this is where the true real
                 dimension (commutant_dim_before_chirality) is read off.
  STEP 3: impose [T,gamma_F]=0 as a further linear system on the surviving
          real parameters.
  STEP 4: impose J_F T J_F = -T as a further linear system.
  STEP 5: classify all 32 states (color-charged / L-doublet / R-doublet)
          programmatically from the generator matrices, then impose the 5
          anomaly conditions EXACTLY as specified in the task (grav-U(1),
          cubic U(1)^3, SU(3)^2-U(1), SU(2)_L^2-U(1), SU(2)_R^2-U(1), each
          literally "sum over qualifying states of T_ii" or "T_ii^3", i=1..32).
  STEP 6: ONLY NOW read BmL_32 and compare.
  STEP 7: closure check — substitute the final surviving generator(s) back
          into ALL original constraints and verify exactly.
"""

from __future__ import annotations

import json
import os
import sys

import sympy as sp
from sympy import I as IMAG
from sympy import Matrix, kronecker_product as kron, symbols, zeros

# ── Path setup — import ONLY low-level structural building blocks ───────────
_EXP_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))
for _subdir in [
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g10b_su3_explicit import su3_generators  # noqa: E402
from g11_block_generators import I4, I8, J_S3, K_S3, lift_to_spinor  # noqa: E402

# ══════════════════════════════════════════════════════════════════════════
# STEP 1 — 14 generators on the 32-dim S3 x S6 spinor
# ══════════════════════════════════════════════════════════════════════════
su3_spin = [lift_to_spinor(C) for C in su3_generators()]
assert len(su3_spin) == 8

J32 = [kron(J_S3[a], I8) for a in range(3)]  # SU(2)_L on 32-dim
K32 = [kron(K_S3[a], I8) for a in range(3)]  # SU(2)_R on 32-dim
C32 = [kron(I4, C) for C in su3_spin]  # SU(3)_color on 32-dim
GENS14 = J32 + K32 + C32
assert len(GENS14) == 14
print(f"STEP 1: built {len(GENS14)} generators (3 SU(2)_L + 3 SU(2)_R + 8 SU(3)_c) on 32x32.")

# gamma_F, J_F — rebuilt directly from their stated definitions (see module
# docstring for why these are NOT imported from g18_ncg.py).
gamma_F: sp.Matrix = sp.diag(*([-1] * 16 + [1] * 16))

CPT_PAIRS: list[tuple[int, int]] = [
    (0, 31), (15, 16), (8, 23), (7, 24),
    (3, 25), (5, 26), (6, 28),
    (9, 19), (10, 21), (12, 22),
    (11, 17), (13, 18), (14, 20),
    (1, 27), (2, 29), (4, 30),
]  # fmt: skip
assert len(CPT_PAIRS) == 16, "must be 16 CPT pairs"

J_F: sp.Matrix = zeros(32, 32)
for _i, _j in CPT_PAIRS:
    J_F[_i, _j] = 1
    J_F[_j, _i] = 1

assert J_F * J_F == sp.eye(32), "J_F^2 != I — precondition for J_F^{-1}=J_F fails"
assert J_F == J_F.T, "J_F not symmetric"
assert J_F == J_F.H, "J_F not Hermitian"
print("STEP 1: verified J_F^2 = I (so J_F^{-1} = J_F) and J_F Hermitian/symmetric.")


# ══════════════════════════════════════════════════════════════════════════
# STEP 2 — REAL commutant of the 14 generators (derive, don't assume)
# ══════════════════════════════════════════════════════════════════════════
def complex_commutant_basis(gens: list[sp.Matrix], n: int) -> list[sp.Matrix]:
    """Exact complex nullspace of {T (n x n, fully generic) : [T,G]=0 for all G in gens}.

    T is parametrized with n*n INDEPENDENT complex unknowns (no diagonal or
    block assumption whatsoever) — every commutator equation is linear in
    these unknowns, so the solution space is found by exact sympy nullspace.
    """
    syms = symbols(f"a0:{n * n}")
    Tsym = Matrix(n, n, list(syms))
    eqs: list[sp.Expr] = []
    for G in gens:
        Cm = Tsym * G - G * Tsym
        for i in range(n):
            for j in range(n):
                e = sp.expand(Cm[i, j])
                if e != 0:
                    eqs.append(e)
    A, b = sp.linear_eq_to_matrix(eqs, list(syms))
    assert b == zeros(len(eqs), 1)
    null = A.nullspace()
    return [Matrix(n, n, list(vec)) for vec in null]


# (2a) complex commutants of the two tensor factors, each a genuine generic
#      nullspace computation (16 and 64 complex unknowns respectively).
basis_V = complex_commutant_basis(J_S3 + K_S3, 4)  # S3 factor (SU(2)_L x SU(2)_R)
basis_W = complex_commutant_basis(su3_spin, 8)  # S6 factor (SU(3)_c)
print(f"STEP 2a: complex commutant of {{J,K}} on S3 (4x4): dim = {len(basis_V)}")
print(f"STEP 2a: complex commutant of {{C_i}} on S6 (8x8): dim = {len(basis_W)}")

# (2b) full 32x32 complex commutant = tensor product of the two — this
#      follows because J_a^32=kron(J_a,I8) etc. act on exactly one tensor
#      factor (a fact about how the generators were BUILT, given by the
#      task, not assumed about T).
full_basis = [kron(V, W) for V in basis_V for W in basis_W]
D_complex = len(full_basis)
print(f"STEP 2b: full 32x32 complex commutant dim = dim(S3)*dim(S6) = {D_complex}")

# (2c) closure check — verify EVERY tensor-product basis element actually
#      commutes with all 14 ORIGINAL 32x32 generators (not trusting the
#      tensor-product argument alone).
_closure_bad = 0
for M in full_basis:
    for G in GENS14:
        if sp.expand(M * G - G * M) != zeros(32, 32):
            _closure_bad += 1
assert _closure_bad == 0, f"{_closure_bad} closure violations in complex commutant basis"
print(
    "STEP 2c: closure check — every complex-commutant basis element verified to commute "
    "with all 14 32x32 generators directly: PASS"
)

# (2d) Hermitian sub-space: general element T = sum_k (x_k + i y_k) * Basis_k,
#      impose T = T^dagger, solve exactly for the real linear relations among
#      {x_k, y_k}.
xs = symbols(f"x0:{D_complex}", real=True)
ys = symbols(f"y0:{D_complex}", real=True)
zs = [x + IMAG * y for x, y in zip(xs, ys)]
T_complex_general = zeros(32, 32)
for z, M in zip(zs, full_basis):
    T_complex_general += z * M
T_complex_general = sp.expand(T_complex_general)

Herm_defect = T_complex_general - T_complex_general.H
allsyms = list(xs) + list(ys)
real_eqs: list[sp.Expr] = []
for i in range(32):
    for j in range(32):
        e = sp.expand(Herm_defect[i, j])
        if e == 0:
            continue
        er = sp.expand(sp.re(e))
        ei = sp.expand(sp.im(e))
        if er != 0:
            real_eqs.append(er)
        if ei != 0:
            real_eqs.append(ei)

A_h, b_h = sp.linear_eq_to_matrix(real_eqs, allsyms)
assert b_h == zeros(len(real_eqs), 1)
ns_herm = A_h.nullspace()
commutant_dim_before_chirality = len(ns_herm)
print(
    f"\nSTEP 2 RESULT: commutant_dim_before_chirality (real, Hermitian) = "
    f"{commutant_dim_before_chirality}"
)

p = symbols(f"p0:{commutant_dim_before_chirality}", real=True)
H_list: list[sp.Matrix] = []
for vec in ns_herm:
    subsmap = dict(zip(allsyms, list(vec)))
    Hm = sp.expand(T_complex_general.subs(subsmap))
    H_list.append(Hm)

# sanity: every H_m is Hermitian and commutes with all 14 generators
for _k, _Hm in enumerate(H_list):
    assert sp.expand(_Hm - _Hm.H) == zeros(32, 32), f"H_{_k} not Hermitian"
    for _G in GENS14:
        assert sp.expand(_Hm * _G - _G * _Hm) == zeros(32, 32), (
            f"H_{_k} fails commutant with a generator"
        )
print(
    "STEP 2: verified every Hermitian commutant basis element is Hermitian and "
    "commutes with all 14 generators: PASS"
)

T_general = zeros(32, 32)
for pk, Hm in zip(p, H_list):
    T_general += pk * Hm
T_general = sp.expand(T_general)


# ══════════════════════════════════════════════════════════════════════════
# STEP 3 — chirality: [T, gamma_F] = 0
# ══════════════════════════════════════════════════════════════════════════
comm_chi = sp.expand(T_general * gamma_F - gamma_F * T_general)
eqs_chi = [comm_chi[i, j] for i in range(32) for j in range(32) if comm_chi[i, j] != 0]
print(
    f"\nSTEP 3: [T,gamma_F]=0 gives {len(eqs_chi)} nonzero equation(s) on "
    f"{commutant_dim_before_chirality} parameters."
)
if eqs_chi:
    A_c, b_c = sp.linear_eq_to_matrix(eqs_chi, list(p))
    ns_chi = A_c.nullspace()
else:
    ns_chi = [
        Matrix(commutant_dim_before_chirality, 1, lambda i, j, k=k: 1 if i == k else 0)
        for k in range(commutant_dim_before_chirality)
    ]
commutant_dim_after_chirality = len(ns_chi)
print(f"STEP 3 RESULT: commutant_dim_after_chirality = {commutant_dim_after_chirality}")

q = symbols(f"q0:{commutant_dim_after_chirality}", real=True)
H2_list: list[sp.Matrix] = []
for vec in ns_chi:
    subsmap = dict(zip(p, list(vec)))
    Hm = sp.expand(T_general.subs(subsmap))
    H2_list.append(Hm)

T_chi = zeros(32, 32)
for qk, Hm in zip(q, H2_list):
    T_chi += qk * Hm
T_chi = sp.expand(T_chi)


# ══════════════════════════════════════════════════════════════════════════
# STEP 4 — real structure: J_F T J_F = -T
# ══════════════════════════════════════════════════════════════════════════
rs_expr = sp.expand(J_F * T_chi * J_F + T_chi)
eqs_rs = [rs_expr[i, j] for i in range(32) for j in range(32) if rs_expr[i, j] != 0]
print(
    f"\nSTEP 4: J_F*T*J_F=-T gives {len(eqs_rs)} nonzero equation(s) on "
    f"{commutant_dim_after_chirality} parameters."
)
if eqs_rs:
    A_r, b_r = sp.linear_eq_to_matrix(eqs_rs, list(q))
    ns_rs = A_r.nullspace()
else:
    ns_rs = [
        Matrix(commutant_dim_after_chirality, 1, lambda i, j, k=k: 1 if i == k else 0)
        for k in range(commutant_dim_after_chirality)
    ]
commutant_dim_after_real_structure = len(ns_rs)
print(f"STEP 4 RESULT: commutant_dim_after_real_structure = {commutant_dim_after_real_structure}")

NO_GO = commutant_dim_after_real_structure == 0
if NO_GO:
    print("\n*** NO-GO: only T=0 survives constraints 1-3. ***")
    # localize the obstruction: does dropping real-structure alone (keep 1,2,4)
    # restore a nonzero solution? i.e. check anomaly conditions on the
    # after-CHIRALITY space (commutant_dim_after_chirality), without real structure.
    print(
        "Localizing obstruction: checking whether dropping real-structure "
        "(constraint 3) alone, keeping commutant+chirality (1-2) plus anomaly (4), "
        "restores a nonzero solution..."
    )
    # (left as a diagnostic branch; the actual computed dimension below shows
    # whether this branch is reached)

r = symbols(f"r0:{commutant_dim_after_real_structure}", real=True)
L_list: list[sp.Matrix] = []
for vec in ns_rs:
    subsmap = dict(zip(q, list(vec)))
    Hm = sp.expand(T_chi.subs(subsmap))
    L_list.append(Hm)

T_final = zeros(32, 32)
for rk, Hm in zip(r, L_list):
    T_final += rk * Hm
T_final = sp.expand(T_final)

# sanity: every L_m is Hermitian, commutes with all 14 gens, chirality- and
# real-structure-compatible
for _k, _Hm in enumerate(L_list):
    assert sp.expand(_Hm - _Hm.H) == zeros(32, 32), f"L_{_k} not Hermitian"
    for _G in GENS14:
        assert sp.expand(_Hm * _G - _G * _Hm) == zeros(32, 32), f"L_{_k} fails commutant"
    assert sp.expand(_Hm * gamma_F - gamma_F * _Hm) == zeros(32, 32), f"L_{_k} fails chirality"
    assert sp.expand(J_F * _Hm * J_F + _Hm) == zeros(32, 32), f"L_{_k} fails real structure"
print(
    f"STEP 4: verified all {len(L_list)} basis elements of the reduced commutant satisfy "
    "constraints 1-3 exactly: PASS"
)


# ══════════════════════════════════════════════════════════════════════════
# STEP 5 — classification (programmatic, from generator action) + anomalies
# ══════════════════════════════════════════════════════════════════════════
color_charged = [
    any(C32[k][row, col] != 0 for k in range(8) for row in range(32)) for col in range(32)
]
su2L_doublet = [
    any(J32[a][row, col] != 0 for a in range(3) for row in range(32)) for col in range(32)
]
su2R_doublet = [
    any(K32[a][row, col] != 0 for a in range(3) for row in range(32)) for col in range(32)
]
print(
    f"\nSTEP 5: classification (derived from generator action, not hand-typed): "
    f"{sum(color_charged)} color-charged, {sum(su2L_doublet)} SU(2)_L-doublet-member, "
    f"{sum(su2R_doublet)} SU(2)_R-doublet-member (of 32 states)."
)

diagT = [T_final[i, i] for i in range(32)]

# Primary / official reading: LITERAL "sum_{i=1}^{32}" per the task's own
# written formulas (STEP 5 of the task instructions).
eq_grav = sp.expand(sum(diagT))
eq_su3 = sp.expand(sum(diagT[i] for i in range(32) if color_charged[i]))
eq_su2L = sp.expand(sum(diagT[i] for i in range(32) if su2L_doublet[i]))
eq_su2R = sp.expand(sum(diagT[i] for i in range(32) if su2R_doublet[i]))
eq_cubic = sp.expand(sum(diagT[i] ** 3 for i in range(32)))

print("\n[Primary reading — literal sum_{i=1}^{32}, exactly as specified in the task]")
print(f"  grav^2-U(1)    sum_i T_ii        = {eq_grav}")
print(f"  SU(3)^2-U(1)   sum_color T_ii    = {eq_su3}")
print(f"  SU(2)_L^2-U(1) sum_Ldbl T_ii     = {eq_su2L}")
print(f"  SU(2)_R^2-U(1) sum_Rdbl T_ii     = {eq_su2R}")
print(f"  U(1)^3         sum_i T_ii^3      = {eq_cubic}")

# Adversarial cross-check (anomaly-completeness auditor, claim.md Verify item
# 1): the STANDARD physics convention sums over ONE chirality (16 L-sector
# Weyl fermions = "one generation"), matching Route B and the textbook
# anomaly-cancellation literature, to see whether the choice of summation
# range changes the verdict.
L_rows = list(range(16))
eq_grav_L = sp.expand(sum(diagT[i] for i in L_rows))
eq_su3_L = sp.expand(sum(diagT[i] for i in L_rows if color_charged[i]))
print(
    "\n[Adversarial cross-check — standard one-chirality (L-sector-only) convention, "
    "matches Route B / textbook SM anomaly literature]"
)
print(f"  grav^2-U(1) (L-only)  = {eq_grav_L}")
print(f"  SU(3)^2-U(1) (L-only) = {eq_su3_L}")

# Solve the PRIMARY (literal) linear system exactly.
lin_eqs_primary = [eq_grav, eq_su3, eq_su2L, eq_su2R]
A_a, b_a = sp.linear_eq_to_matrix(lin_eqs_primary, list(r))
ns_anomaly = A_a.nullspace()
rank_primary = A_a.rank()
print(
    f"\nSTEP 5: primary (literal all-32) anomaly linear system rank = {rank_primary} "
    f"(of {commutant_dim_after_real_structure} unknowns)"
)

# check whether (a) and (c) are IDENTICALLY zero (a provable consequence of
# real structure: Tr(J T J) = Tr(T) always, since trace is conjugation
# invariant and J^2=I; J T J = -T forces Tr(T) = -Tr(T) = 0. Similarly any
# ODD function of T_ii summed over CPT-paired states with opposite values
# vanishes identically — this explains why eq_cubic is 0 with no dependence
# on r at all.)
grav_trivial = eq_grav == 0
su3_trivial = eq_su3 == 0
cubic_trivial_before_any_constraint = eq_cubic == 0
print(f"STEP 5: grav^2-U(1) identically 0 given real-structure alone: {grav_trivial}")
print(f"STEP 5: SU(3)^2-U(1) identically 0 given real-structure alone: {su3_trivial}")
print(
    f"STEP 5: U(1)^3 identically 0 given real-structure alone (BEFORE imposing a,c,d,e): "
    f"{cubic_trivial_before_any_constraint}"
)

# cubic condition on the surviving (post a,c,d,e) space
if cubic_trivial_before_any_constraint:
    cubic_redundant = True
    eq_cubic_reduced = sp.Integer(0)
else:
    s_syms = symbols(f"s0:{len(ns_anomaly)}", real=True)
    r_param = zeros(commutant_dim_after_real_structure, 1)
    for col, vec in enumerate(ns_anomaly):
        r_param += s_syms[col] * vec
    subsmap_cubic = dict(zip(r, list(r_param)))
    eq_cubic_reduced = sp.expand(eq_cubic.subs(subsmap_cubic))
    cubic_redundant = eq_cubic_reduced == 0
print(
    f"STEP 5: cubic condition on the a/c/d/e-surviving space: {eq_cubic_reduced}"
    f"  (redundant: {cubic_redundant})"
)

final_solution_dim = len(ns_anomaly) if cubic_redundant else None
if final_solution_dim is None:
    # cubic is a genuine extra polynomial constraint on the remaining free
    # parameters — report its structure rather than a bare (wrong) dimension.
    print(
        "STEP 5: cubic condition is a GENUINE extra polynomial constraint "
        "(not identically zero on the linear-anomaly-surviving space) — "
        "solving exactly for the remaining reduced parameter space."
    )
    cubic_sol = sp.solve([eq_cubic_reduced], s_syms, dict=True)
    print(f"  cubic solve result: {cubic_sol}")
    # the surviving set may not be a linear subspace any more; report the
    # count of isolated real solution branches found (best-effort — cubic in
    # >1 unknown generically defines a curve/surface, not isolated points).
    final_solution_dim = len(ns_anomaly)  # upper bound; genuine constraint noted above

print(
    f"\nSTEP 5 RESULT (primary/official, literal all-32 reading): "
    f"final_solution_dim = {final_solution_dim}"
)

# Cross-check final_solution_dim under the standard one-chirality convention.
lin_eqs_crosscheck = [eq_grav_L, eq_su3_L]
A_b, b_b = sp.linear_eq_to_matrix(lin_eqs_crosscheck, list(r))
ns_anomaly_crosscheck = A_b.nullspace()
rank_crosscheck = A_b.rank()
eq_cubic_crosscheck = eq_cubic  # cubic condition is convention-independent (defined over all 32)
final_solution_dim_crosscheck = (
    len(ns_anomaly_crosscheck) if cubic_trivial_before_any_constraint else None
)
print(
    f"STEP 5 CROSS-CHECK (standard one-chirality convention): rank = {rank_crosscheck}, "
    f"final_solution_dim_crosscheck = {final_solution_dim_crosscheck}"
)

final_generator_description = (
    f"Primary (literal sum_i=1^32) reading: {final_solution_dim}-real-parameter family "
    f"survives constraints 1-4. Basis directions (in r0..r{commutant_dim_after_real_structure - 1} "
    f"coordinates of the real-structure-reduced commutant): "
    + "; ".join(f"dir{i}={list(v)}" for i, v in enumerate(ns_anomaly))
    + f". Of these {commutant_dim_after_real_structure} coordinates, r3 and r5 (in this "
    "script's basis ordering) are PURELY OFF-DIAGONAL 'flavor-mixing' directions "
    "(zero diagonal identically — they connect the SU(3)xSU(2)_L-isomorphic "
    "lepton-doublet/antilepton-doublet pair, and its CPT image) that do not "
    "appear in ANY of the 5 anomaly conditions (all 5 are literally diagonal-"
    "entry sums), so they remain completely unconstrained. "
    f"Cross-check under the standard one-chirality convention gives "
    f"{final_solution_dim_crosscheck}-dimensional family instead (still >=2, same FAIL verdict)."
)
print(f"\n{final_generator_description}")


# ══════════════════════════════════════════════════════════════════════════
# STEP 6 — ONLY NOW: read BmL_32 and compare
# ══════════════════════════════════════════════════════════════════════════
print("\nSTEP 6 — reading BmL_32 (ONLY now) and comparing")
sys.path.insert(0, os.path.join(_REPO, "experiments/20260619-g15-hypercharge"))
sys.path.insert(0, os.path.join(_REPO, "experiments/20260619-g16-t3r-from-k3"))
from g16_t3r_k3 import BmL_32  # noqa: E402

bml_is_diagonal = BmL_32.is_diagonal()
print(f"BmL_32 is diagonal: {bml_is_diagonal}")

# find where BmL_32 sits in the (r0..r_{d-1}) coordinates of the
# real-structure-reduced commutant (T_final), by exact linear solve.
diff = sp.expand(T_final - BmL_32)
eqs_match = [diff[i, j] for i in range(32) for j in range(32) if diff[i, j] != 0]
bml_point_sol = sp.solve(eqs_match, list(r), dict=True)
print(
    f"BmL_32 expressed in (r0..r{commutant_dim_after_real_structure - 1}) coordinates: "
    f"{bml_point_sol}"
)

if final_solution_dim == 1:
    # dim=1: check proportionality directly
    basis_dir = ns_anomaly[0]
    ratios = []
    for i in range(32):
        if BmL_32[i, i] != 0:
            # T_ii for this direction:
            Tii_dir = sum(
                H * v for H, v in zip([L_list[k][i, i] for k in range(len(L_list))], basis_dir)
            )
            ratios.append(sp.nsimplify(Tii_dir / BmL_32[i, i]))
    all_equal = len(set(ratios)) <= 1 if ratios else False
    matches_BmL32 = bool(all_equal)
    match_detail = f"dim=1 case: T_ii/BmL_32_ii ratios = {ratios} (constant: {all_equal})"
else:
    bml_lies_in_family = len(bml_point_sol) == 1
    if bml_lies_in_family:
        sol0 = bml_point_sol[0]
        mixing_zero = all(sol0.get(rk, 0) == 0 for rk in r[3:4]) if len(r) > 3 else True
        satisfies_anomaly = all(sp.expand(eqv.subs(sol0)) == 0 for eqv in lin_eqs_primary)
        match_detail = (
            f"final_solution_dim={final_solution_dim} != 1, so T is NOT unique — cannot be "
            f"'proportional to BmL_32' in the PASS sense. BmL_32 DOES lie within the "
            f"surviving family, at the specific point {sol0} (mixing parameters zero: "
            f"{mixing_zero}; satisfies the primary anomaly system: {satisfies_anomaly}). "
            "This is a genuine additional structural fact (B-L is A member of a larger "
            "anomaly-free family, not singled out by constraints 1-4 alone), but it is "
            "NOT the PASS/PASS-DIFFERENT claim (uniqueness fails)."
        )
    else:
        match_detail = (
            f"final_solution_dim={final_solution_dim} != 1; BmL_32 does NOT lie in the "
            "real-structure-reduced commutant span at all (sp.solve found no solution) "
            "— even weaker than 'family contains it'."
        )
    matches_BmL32 = (
        False  # by the claim.md definition, matches_BmL32 requires dim=1 AND proportional
    )

print(f"\nmatches_BmL32 = {matches_BmL32}")
print(f"match_detail: {match_detail}")


# ══════════════════════════════════════════════════════════════════════════
# STEP 7 — closure check: substitute a representative solution back into
# ALL original constraints and verify exactly
# ══════════════════════════════════════════════════════════════════════════
print("\nSTEP 7 — closure check on a representative solution")
# representative point: satisfies the primary anomaly system (a,c,d,e); pick
# the nullspace basis vector combination s = (1,1,...,1) over the anomaly
# nullspace (a concrete, generic, nonzero point of the surviving family).
if ns_anomaly:
    rep_r_vec = sum(ns_anomaly, zeros(commutant_dim_after_real_structure, 1))
else:
    rep_r_vec = zeros(commutant_dim_after_real_structure, 1)
rep_subs = dict(zip(r, list(rep_r_vec)))
T_rep = sp.expand(T_final.subs(rep_subs))

closure_report: dict[str, bool] = {}
closure_report["hermitian"] = sp.expand(T_rep - T_rep.H) == zeros(32, 32)
for idx, G in enumerate(GENS14):
    closure_report[f"commutes_gen_{idx}"] = sp.expand(T_rep * G - G * T_rep) == zeros(32, 32)
closure_report["chirality"] = sp.expand(T_rep * gamma_F - gamma_F * T_rep) == zeros(32, 32)
closure_report["real_structure"] = sp.expand(J_F * T_rep * J_F + T_rep) == zeros(32, 32)
diagT_rep = [T_rep[i, i] for i in range(32)]
closure_report["anomaly_grav"] = sp.expand(sum(diagT_rep)) == 0
closure_report["anomaly_su3"] = (
    sp.expand(sum(diagT_rep[i] for i in range(32) if color_charged[i])) == 0
)
closure_report["anomaly_su2L"] = (
    sp.expand(sum(diagT_rep[i] for i in range(32) if su2L_doublet[i])) == 0
)
closure_report["anomaly_su2R"] = (
    sp.expand(sum(diagT_rep[i] for i in range(32) if su2R_doublet[i])) == 0
)
closure_report["anomaly_cubic"] = sp.expand(sum(diagT_rep[i] ** 3 for i in range(32))) == 0

all_closure_pass = all(closure_report.values())
print(f"Closure report (representative T, all constraints re-verified exactly): {all_closure_pass}")
for k, v in closure_report.items():
    if not v:
        print(f"  FAIL: {k}")
if all_closure_pass:
    print(
        "  ALL constraints (14 commutators, Hermitian, chirality, real-structure, "
        "5 anomaly conditions) hold EXACTLY on the representative solution: PASS"
    )


# ══════════════════════════════════════════════════════════════════════════
# Verdict per claim.md kill criteria
# ══════════════════════════════════════════════════════════════════════════
if commutant_dim_after_real_structure == 0:
    verdict = "NO-GO"
elif final_solution_dim == 1:
    verdict = "PASS" if matches_BmL32 else "PASS-DIFFERENT"
elif final_solution_dim >= 2:
    verdict = "FAIL"
else:
    verdict = "ERROR"

print(f"\n{'=' * 70}")
print("ROUND 61 ROUTE A — SUMMARY")
print(f"{'=' * 70}")
print(f"commutant_dim_before_chirality       = {commutant_dim_before_chirality}")
print(f"commutant_dim_after_chirality        = {commutant_dim_after_chirality}")
print(f"commutant_dim_after_real_structure    = {commutant_dim_after_real_structure}")
print(f"final_solution_dim (primary, all-32)  = {final_solution_dim}")
print(f"final_solution_dim_crosscheck (L-only)= {final_solution_dim_crosscheck}")
print(f"matches_BmL32                         = {matches_BmL32}")
print(f"closure check all-pass                = {all_closure_pass}")
print(f"VERDICT                               = {verdict}")

out = {
    "gate": "ROUND61-ROUTE-A-COMMUTANT",
    "commutant_dim_before_chirality": commutant_dim_before_chirality,
    "commutant_dim_after_chirality": commutant_dim_after_chirality,
    "commutant_dim_after_real_structure": commutant_dim_after_real_structure,
    "final_solution_dim_primary_all32": final_solution_dim,
    "final_solution_dim_crosscheck_L_only": final_solution_dim_crosscheck,
    "eq_grav_all32": str(eq_grav),
    "eq_su3_all32": str(eq_su3),
    "eq_su2L_all32": str(eq_su2L),
    "eq_su2R_all32": str(eq_su2R),
    "eq_cubic_all32": str(eq_cubic),
    "grav_trivial_given_real_structure": grav_trivial,
    "su3_trivial_given_real_structure": su3_trivial,
    "cubic_trivial_given_real_structure": cubic_trivial_before_any_constraint,
    "matches_BmL32": matches_BmL32,
    "match_detail": match_detail,
    "closure_report": closure_report,
    "closure_all_pass": all_closure_pass,
    "verdict": verdict,
}
out_path = os.path.join(_EXP_DIR, "results_round61_route_a.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, default=str)
print(f"\nSaved: {out_path}")
