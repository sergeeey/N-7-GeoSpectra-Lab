"""C191 -- test P5's induced pairing rule under an EXPLICIT POSTULATE.

P5 (route (c), C132 2026-09-02 survey, CDT rank =5/14, 4.3, flagged in
OPEN_BLOCKERS.md as "high AOG-5 risk -- no motivation beyond wanting to
unblock OB1"): identify ONE so(4) summand of the already-built, already-
verified SO(4)xSO(4) subset Spin(8) block-chirality construction
(pearl_registry rows dated 2026-07-15; reused here via
experiments/20260715-l3b-so4xso4-candidate/so4xso4_branching.py, NOT
rebuilt) with S3's OWN isometry group SO(4)=SU(2)_L x SU(2)_R.

THIS IS A POSTULATE, NOT A DERIVATION. Nothing in this project's own
G2/SU(3)+S3 geometric content forces this identification -- it is an
external assumption about how S3's isometry sits inside the internal
Spin(8) fiber structure, exactly why C132/C173 flagged it "route (c)"
and high AOG-5 risk. This round does not attempt to justify the
identification. It takes the identification AS GIVEN and asks a
narrower, answerable question: granted the postulate, does it produce a
DEFINITE pairing rule between "which block chirality" (Gamma_A=Gamma_B
i.e. 8_s, vs Gamma_A=-Gamma_B i.e. 8_c) and "which t-sector" (C38's own
established kernel content: ker D^{t=0}=(1,2), ker D^{t=1}=(2,1) as
SU(2)_L x SU(2)_R representations of S3's isometry, C38 verified this
under "the SO(4) isometry action with the frame lift")?

C132's own text (decision.md line 456-458): "'which block chirality' --
the datum separating 8_s from 8_c -- becomes 'which SU(2) factor', i.e.
which t-sector... That is a pairing rule." This round checks whether
that sentence survives contact with the actual representation content,
which nobody had computed yet (the pearl_registry's own row 58 SU(2)^4
branching -- 8_s=(2,1,2,1)+(1,2,1,2), 8_c=(2,1,1,2)+(1,2,2,1) -- exists,
but nobody had RESTRICTED it to a single so(4) factor and compared
against C38 before this round).

Novelty check: grep -rl "C38" experiments/ null_results/ parked/
pearl_registry/ (run before writing this script) finds C38's own
kernel-content claim and its many downstream USES, but no computation
restricting the SO(4)xSO(4) branching to one factor and comparing. P5's
own Zero-Signal-Gate entry in C132 ("PASS (H -- V1)") is a well-posedness
screen, not a computed result -- P5 was explicitly gated behind user
authorization to accept a route-(c) postulate (C132's own Relaxation Map:
"then, if a route-(c) postulate or a boundary is ever granted: P5 -> ..."),
which is what this session's user instruction supplies.

Run:  python c191_p5_postulate_pairing.py
"""

import os
import sys

import numpy as np

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "20260715-l3b-so4xso4-candidate"),
)
from so4xso4_branching import GAMMA, GAMMA_9, GAMMA_A, GAMMA_B

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------------------
print("=" * 78)
print("A  reuse (not rebuild) the 2026-07-15 Cl(8) / block-chirality construction")
print("=" * 78)

check(
    "P1 GAMMA_A, GAMMA_B, GAMMA_9 imported from the existing, already-verified"
    " so4xso4_branching.py",
    GAMMA_A.shape == (16, 16)
    and GAMMA_B.shape == (16, 16)
    and GAMMA_9.shape == (16, 16),
)
check(
    "P2 [Gamma_A, Gamma_B] = 0 (re-confirmed, not re-derived)",
    np.allclose(GAMMA_A @ GAMMA_B - GAMMA_B @ GAMMA_A, 0, atol=1e-8),
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("B  build so(4)_1's su(2)_L x su(2)_R generators (indices 1-4, the H-block)")
print("=" * 78)


def m(i, j):
    """Hermitian so(8) spin-lift generator: (i/4)[Gamma_i,Gamma_j].

    [Gamma_i,Gamma_j] is anti-Hermitian for Hermitian Gamma's, so the bare
    (1/4)[.,.] combination is anti-Hermitian -- an extra i is needed to get
    the physical (Hermitian, non-negative Casimir) angular-momentum
    convention, same as spin operators S_i = (i/4) eps_ijk [gamma_j,gamma_k].
    """
    return 0.25j * (GAMMA[i] @ GAMMA[j] - GAMMA[j] @ GAMMA[i])


M12, M13, M14 = m(1, 2), m(1, 3), m(1, 4)
M23, M24, M34 = m(2, 3), m(2, 4), m(3, 4)

# Standard so(4) = su(2)_L (+) su(2)_R self-dual / anti-self-dual split.
L1, L2, L3 = (M23 + M14) / 2, (-M13 + M24) / 2, (M12 + M34) / 2
R1, R2, R3 = (M23 - M14) / 2, (-M13 - M24) / 2, (M12 - M34) / 2


def comm(a, b):
    return a @ b - b @ a


EPS = {
    (0, 1, 2): 1,
    (1, 2, 0): 1,
    (2, 0, 1): 1,
    (0, 2, 1): -1,
    (2, 1, 0): -1,
    (1, 0, 2): -1,
}
L_OPS, R_OPS = [L1, L2, L3], [R1, R2, R3]

# NOTE: direct check found comm(L1,L2) = -1j*L3 exactly (not +1j*L3) -- an
# overall handedness/orientation convention in the self-dual/anti-self-dual
# split (equivalent to swapping which combination is called "L" vs "R"),
# harmless: it does not affect L^2=L1^2+L2^2+L3^2 (P6-P11 below use only the
# quadratic Casimir, insensitive to the sign of the structure constants).
# Verified with a standalone diagnostic (scratch script) before fixing here,
# not guessed.
su2_l_ok = all(
    np.allclose(
        comm(L_OPS[a], L_OPS[b]), -1j * EPS.get((a, b, c), 0) * L_OPS[c], atol=1e-8
    )
    for a in range(3)
    for b in range(3)
    for c in range(3)
    if (a, b, c) in EPS
)
su2_r_ok = all(
    np.allclose(
        comm(R_OPS[a], R_OPS[b]), -1j * EPS.get((a, b, c), 0) * R_OPS[c], atol=1e-8
    )
    for a in range(3)
    for b in range(3)
    for c in range(3)
    if (a, b, c) in EPS
)
cross_zero = all(
    np.allclose(comm(L_OPS[a], R_OPS[b]), 0, atol=1e-8)
    for a in range(3)
    for b in range(3)
)

check("P3 [L_a, L_b] = -i eps_abc L_c -- su(2)_L closes", su2_l_ok)
check("P4 [R_a, R_b] = -i eps_abc R_c -- su(2)_R closes", su2_r_ok)
check(
    "P5 [L_a, R_b] = 0 for all a,b -- L and R commute (genuine so(4)=su(2)+su(2) split)",
    cross_zero,
)

CASIMIR_L = L1 @ L1 + L2 @ L2 + L3 @ L3
CASIMIR_R = R1 @ R1 + R2 @ R2 + R3 @ R3
check(
    "P6 [Casimir_L, Casimir_R] = 0 (independent quantum numbers, can be jointly diagonalized)",
    np.allclose(comm(CASIMIR_L, CASIMIR_R), 0, atol=1e-8),
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("C  THE POSTULATE (stated explicitly, not derived): this so(4)_1's su(2)_L,")
print("   su(2)_R IS identified with S3's own SU(2)_L, SU(2)_R (the isometry group")
print("   C186-C190 built explicitly as X_a^L, X_a^R). Nothing below tests whether")
print("   this identification is TRUE -- only what it PREDICTS if granted.")
print("=" * 78)


def chirality_eigenbasis():
    evals, evecs = np.linalg.eigh(GAMMA_9)
    v_s = evecs[:, evals > 0.5]
    v_c = evecs[:, evals < -0.5]
    return v_s, v_c


V_S, V_C = chirality_eigenbasis()
check(
    "P7 8_s (Gamma_9=+1) and 8_c (Gamma_9=-1) each have dimension 8",
    V_S.shape[1] == 8 and V_C.shape[1] == 8,
)


def restricted_casimirs(basis):
    cl = basis.conj().T @ CASIMIR_L @ basis
    cr = basis.conj().T @ CASIMIR_R @ basis
    return cl, cr


def spin_content(casimir_matrix):
    """Diagonalize a Casimir j(j+1) operator, return {j: multiplicity}."""
    evals = np.linalg.eigvalsh(casimir_matrix)
    content = {}
    for lam in evals:
        lam_r = round(lam.real, 4)
        j = round((-1 + np.sqrt(1 + 4 * lam_r)) / 2, 4) if lam_r > -1e-6 else 0.0
        content[j] = content.get(j, 0) + 1
    return content


cl_s, cr_s = restricted_casimirs(V_S)
cl_c, cr_c = restricted_casimirs(V_C)

j_l_s, j_r_s = spin_content(cl_s), spin_content(cr_s)
j_l_c, j_r_c = spin_content(cl_c), spin_content(cr_c)

print(
    f"  8_s (same block chirality, Gamma_A=Gamma_B): j_L content = {j_l_s}, j_R content = {j_r_s}"
)
print(
    f"  8_c (opposite block chirality, Gamma_A=-Gamma_B): j_L content = {j_l_c}, j_R content = {j_r_c}"
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("D  the actual (j_L,j_R) joint content -- does 8_s differ from 8_c?")
print("=" * 78)


def joint_content(basis):
    cl = basis.conj().T @ CASIMIR_L @ basis
    cr = basis.conj().T @ CASIMIR_R @ basis
    # Simultaneously diagonalize: since [Casimir_L, Casimir_R]=0 (P6), build a
    # random Hermitian combination to resolve joint eigenspaces without
    # assuming an eigenbasis order, then read off (j_L,j_R) per eigenvector.
    combo = (
        cl + np.pi * cr
    )  # irrational relative weight avoids accidental degeneracy collisions
    _evals, evecs = np.linalg.eigh(combo)
    content: dict[tuple[float, float], int] = {}
    for k in range(combo.shape[0]):
        vec = evecs[:, k]
        jl = vec.conj() @ cl @ vec
        jr = vec.conj() @ cr @ vec
        jl_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * jl.real))) / 2, 3)
        jr_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * jr.real))) / 2, 3)
        key = (jl_val, jr_val)
        content[key] = content.get(key, 0) + 1
    return content


joint_s = joint_content(V_S)
joint_c = joint_content(V_C)
print(f"  8_s joint (j_L,j_R) content: {joint_s}")
print(f"  8_c joint (j_L,j_R) content: {joint_c}")

EXPECTED_FROM_ROW58 = {
    (0.5, 0.0): 4,
    (0.0, 0.5): 4,
}  # 2x(2,1)+2x(1,2), dim 2 each = 4+4=8
check(
    "P8 8_s matches the row-58 SU(2)^4-branching prediction restricted to (L1,R1):"
    " 4-dim (j_L=1/2,j_R=0) + 4-dim (j_L=0,j_R=1/2)",
    joint_s == EXPECTED_FROM_ROW58,
    f"got {joint_s}",
)
check(
    "P9 8_c ALSO matches the same restricted content (this is the actual test --"
    " does the postulate distinguish s from c, or not?)",
    joint_c == EXPECTED_FROM_ROW58,
    f"got {joint_c}",
)

IDENTICAL_CONTENT = joint_s == joint_c
check(
    "P10 [the actual finding] 8_s and 8_c have IDENTICAL (j_L,j_R) content under"
    " so(4)_1 ALONE -- the postulate as naively stated does NOT produce a pairing",
    IDENTICAL_CONTENT,
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("E  compare against C38's established content (S3's OWN Dirac-kernel result)")
print("=" * 78)

C38_T0 = {(0.0, 0.5): 1}  # ker D^{t=0} = (1,2): j_L=0 (dim1), j_R=1/2 (dim2)
C38_T1 = {(0.5, 0.0): 1}  # ker D^{t=1} = (2,1): j_L=1/2 (dim2), j_R=0 (dim1)
print(
    f"  C38 (already established, this project's own S3 result): t=0 kernel = (1,2)"
    f" i.e. {C38_T0}, t=1 kernel = (2,1) i.e. {C38_T1}"
)
print(
    "  Note: C38's kernel is a single IRREP (dim 2 each); 8_s/8_c are 8-dim REDUCIBLE"
)
print(
    "  spaces containing MULTIPLE copies of both (1,2)-type and (2,1)-type content --"
)
print("  a dimension mismatch the postulate's own sentence ('which SU(2) factor... is")
print("  which t-sector') does not address, independent of P10's finding above.")

check(
    "P11 C38's kernel content (single irrep per t-sector) is a STRICT SUBSET of"
    " each of 8_s's and 8_c's full (multi-copy) content -- consistent with"
    " EITHER being 'the' t-sector rep, which is exactly why P10 is decisive:"
    " nothing here picks one over the other",
    set(C38_T0) <= set(joint_s)
    and set(C38_T1) <= set(joint_s)
    and set(C38_T0) <= set(joint_c)
    and set(C38_T1) <= set(joint_c),
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("F  steelman: does FIXING so(4)_2's (L2,R2) quantum number rescue the pairing?")
print("   (checked, not just asserted, before writing this round's verdict)")
print("=" * 78)

M56, M57, M58 = m(5, 6), m(5, 7), m(5, 8)
M67, M68, M78 = m(6, 7), m(6, 8), m(7, 8)
L1b, L2b, L3b = (M67 + M58) / 2, (-M57 + M68) / 2, (M56 + M78) / 2
R1b, R2b, R3b = (M67 - M58) / 2, (-M57 - M68) / 2, (M56 - M78) / 2
CASIMIR_L2 = L1b @ L1b + L2b @ L2b + L3b @ L3b
CASIMIR_R2 = R1b @ R1b + R2b @ R2b + R3b @ R3b

check(
    "P12 so(4)_2's Casimirs commute with so(4)_1's (independent quantum numbers)",
    all(
        np.allclose(comm(op1, op2), 0, atol=1e-8)
        for op1 in (CASIMIR_L, CASIMIR_R)
        for op2 in (CASIMIR_L2, CASIMIR_R2)
    ),
)


def full_joint_content(basis):
    """(j_L1,j_R1,j_L2,j_R2) content, resolved via one irrational-weighted combo."""
    ops = [CASIMIR_L, CASIMIR_R, CASIMIR_L2, CASIMIR_R2]
    restricted = [basis.conj().T @ op @ basis for op in ops]
    weights = [1.0, np.pi, np.e, np.pi * np.e]
    combo = sum(w * r for w, r in zip(weights, restricted))
    _evals, evecs = np.linalg.eigh(combo)
    content: dict[tuple[float, float, float, float], int] = {}
    for k in range(combo.shape[0]):
        vec = evecs[:, k]
        js = []
        for r in restricted:
            val = (vec.conj() @ r @ vec).real
            js.append(round((-1 + np.sqrt(max(0.0, 1 + 4 * val))) / 2, 3))
        key = tuple(js)
        content[key] = content.get(key, 0) + 1
    return content


full_s = full_joint_content(V_S)
full_c = full_joint_content(V_C)
print(f"  8_s full (j_L1,j_R1,j_L2,j_R2) content: {full_s}")
print(f"  8_c full (j_L1,j_R1,j_L2,j_R2) content: {full_c}")

EXPECTED_S_ROW58 = {(0.5, 0.0, 0.5, 0.0): 4, (0.0, 0.5, 0.0, 0.5): 4}
EXPECTED_C_ROW58 = {(0.5, 0.0, 0.0, 0.5): 4, (0.0, 0.5, 0.5, 0.0): 4}
check(
    "P13 full 4-Casimir content reproduces row 58's SU(2)^4 branching exactly"
    " (8_s=(2,1,2,1)+(1,2,1,2), 8_c=(2,1,1,2)+(1,2,2,1))",
    full_s == EXPECTED_S_ROW58 and full_c == EXPECTED_C_ROW58,
    f"got 8_s={full_s}, 8_c={full_c}",
)


def restrict_to_l2r2(content, l2, r2):
    return {
        (jl1, jr1): n
        for (jl1, jr1, jl2, jr2), n in content.items()
        if (jl2, jr2) == (l2, r2)
    }


s_at_A = restrict_to_l2r2(full_s, 0.5, 0.0)
c_at_A = restrict_to_l2r2(full_c, 0.5, 0.0)
s_at_B = restrict_to_l2r2(full_s, 0.0, 0.5)
c_at_B = restrict_to_l2r2(full_c, 0.0, 0.5)
print(
    f"  Fixing (L2,R2)=(1/2,0): 8_s gives (L1,R1)={s_at_A}, 8_c gives (L1,R1)={c_at_A}"
)
print(
    f"  Fixing (L2,R2)=(0,1/2): 8_s gives (L1,R1)={s_at_B}, 8_c gives (L1,R1)={c_at_B}"
)

pairing_at_A_clean = bool(s_at_A) and bool(c_at_A) and set(s_at_A) != set(c_at_A)
pairing_at_B_clean = bool(s_at_B) and bool(c_at_B) and set(s_at_B) != set(c_at_B)
check(
    "P14 the REFINED postulate (fix a specific (L2,R2) 'internal' sector too) DOES"
    " produce a clean s-vs-c pairing at each fixed (L2,R2) value individually",
    pairing_at_A_clean and pairing_at_B_clean,
)

pairing_flips = (
    bool(s_at_A)
    and bool(s_at_B)
    and set(s_at_A) == set(c_at_B)
    and set(c_at_A) == set(s_at_B)
)
check(
    "P15 [the real content of the steelman] -- but the two (L2,R2) choices give the"
    " OPPOSITE pairing to each other: at (1/2,0), 8_s<->(1/2,0); at (0,1/2),"
    " 8_s<->(0,1/2) -- i.e. 8_s tracks (L2,R2) SELF-consistently (matches at both),"
    " which means the 'pairing' is just relabelling L2R2 as L1R1, not new information",
    set(s_at_A) == {(0.5, 0.0)}
    and set(s_at_B) == {(0.0, 0.5)}
    and set(c_at_A) == {(0.0, 0.5)}
    and set(c_at_B) == {(0.5, 0.0)},
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("G  role-swap check: does it matter WHICH so(4) factor plays 'S3's role'?")
print("   (claim.md flagged this as untested; cheap to check with what's already")
print("   built -- so(4)_2's own Casimirs, CASIMIR_L2/CASIMIR_R2, exist from")
print("   Section F. Checked, not assumed by symmetry.)")
print("=" * 78)


def joint_content_pair(basis, cas_a, cas_b):
    ra = basis.conj().T @ cas_a @ basis
    rb = basis.conj().T @ cas_b @ basis
    combo = ra + np.pi * rb
    _evals, evecs = np.linalg.eigh(combo)
    content: dict[tuple[float, float], int] = {}
    for k in range(combo.shape[0]):
        vec = evecs[:, k]
        ja = (vec.conj() @ ra @ vec).real
        jb = (vec.conj() @ rb @ vec).real
        ja_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * ja))) / 2, 3)
        jb_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * jb))) / 2, 3)
        key = (ja_val, jb_val)
        content[key] = content.get(key, 0) + 1
    return content


joint_s_swap = joint_content_pair(V_S, CASIMIR_L2, CASIMIR_R2)
joint_c_swap = joint_content_pair(V_C, CASIMIR_L2, CASIMIR_R2)
print(f"  8_s restricted to (L2,R2) [S3 = SECOND factor instead]: {joint_s_swap}")
print(f"  8_c restricted to (L2,R2) [S3 = SECOND factor instead]: {joint_c_swap}")

check(
    "P16 role-swap reproduces the SAME structure as P8 (by the construction's"
    " own H<->Hl symmetry, not assumed): 4x(1/2,0)+4x(0,1/2), matching P8 exactly",
    joint_s_swap == EXPECTED_FROM_ROW58,
    f"got {joint_s_swap}",
)
check(
    "P17 role-swap gives IDENTICAL 8_s/8_c content too -- naive P5 REJECTED"
    " regardless of which so(4) factor is postulated to be S3's isometry,"
    " not just for the one choice tested in Section D",
    joint_s_swap == joint_c_swap,
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"C191: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
