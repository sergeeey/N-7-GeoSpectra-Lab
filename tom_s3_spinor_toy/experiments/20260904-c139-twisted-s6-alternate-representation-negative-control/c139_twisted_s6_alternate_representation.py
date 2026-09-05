"""C139 -- does a genuinely DIFFERENT twist bundle (not Sigma=Lambda^bullet(C^3),
not a symmetry-relabelling of it) give an S6 twisted Dirac operator with an
invariant-sector kernel != 1, supplying the first real wrong-twist negative
control for round59's kernel=1 result (four prior attempts, C73/C73b, all
failed to discriminate)?

PRE-REGISTERED CHOICE (see decision.md Section 2 for full justification,
written before this script computed any kernel): the twist bundle is
W' = m_C, the COMPLEXIFIED ISOTROPY (TANGENT) REPRESENTATION of S6=G2/SU(3)
-- i.e. the SAME 6-dim space NOMIZU is a connection ON, represented via the
STANDARD/VECTOR representation of so(6) (bivec_to_6x6), not the 8-dim SPIN
representation Sigma uses. As an su(3)-module, m = 3 (+) 3bar -- dimension 6
(not 8), NO trivial summand (unlike Sigma's 1+1+3+3bar) -- module type is
genuinely different, and (Section 3 below, verified computationally, not
just asserted) m is NOT isomorphic, as a representation of the six NOMIZU[i]
connection generators, to any subspace of Sigma: Sigma decomposes into two
IRREDUCIBLE 4-dim pieces (S+=EVEN_IDX, S-=ODD_IDX) under {NAB_i}, so no
6-dim {NAB_i}-invariant subspace exists in Sigma at all, and a direct
intertwiner search confirms zero nonzero equivariant maps Sigma->m.

Construction: D'(eta (x) w) = sum_i (e_i . nabla^Sigma_i eta) (x) w
                                    + (e_i . eta) (x) (nabla^{m}_i w)
-- the SAME Leibniz-rule twisted-Dirac structure round59's build_dirac uses
(Clifford multiplication acts on the FIRST/spinor factor only; the SECOND
/twist factor only sees its own connection) -- with nabla^{m}_i =
bivec_to_6x6(NOMIZU[i]), the tangent bundle's OWN Levi-Civita connection,
i.e. the SAME NOMIZU data round59 used, unmodified, represented in a
genuinely different (vector, not spin) representation of so(6).

Reuses round59_route_a_independent.py's build_clifford/spin_lift/ADNU/
NOMIZU/EVEN_IDX/ODD_IDX/kron/gram_schmidt/hip unmodified; C73's
build_numeric_dirac/su3_gens64/invariant_basis unmodified (as a TRUSTED
REFERENCE for the self-consistency check in Section 5); C73b's
bivec_to_6x6 unmodified.

AST self-audit: refuses to run if any check() call is passed a literal
constant (defends against unfailable checks) -- same pattern as
C130/C133/C134/C136/C138.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c139.json"
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
C73_PATH = HERE.parent / "20260811-c73-round59-real-twisted-dirac-battery" / "c73_dirac_battery.py"
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)
C73 = load_module("c73_dirac_battery", C73_PATH)
C73B = load_module("c73b_torsion_family", C73B_PATH)

RESULTS: dict[str, bool] = {}
DATA: dict[str, object] = {}
FAILURES: list[str] = []


def _self_audit_no_hardcoded_checks() -> int:
    """Reject any check(...) whose condition is a LITERAL constant in the
    source -- same discipline as C130/C133/C134/C136/C138 (a check whose
    condition is a literal True cannot fail)."""
    import ast

    src = Path(__file__).read_text(encoding="utf-8")
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


def check(name: str, cond: bool, detail: str = "") -> bool:
    RESULTS[name] = bool(cond)
    status = "PASS" if cond else "FAIL"
    if not cond:
        FAILURES.append(name)
    print(f"  [{status}] {name}" + (f"   {detail}" if detail else ""))
    return cond


TOL = 1e-8

# ----------------------------------------------------------------------
# Generic linear-algebra helpers (parameterized versions of R59/C73/C73b's
# own dim-64/dim-8-specific machinery, needed here because the twist bundle
# has a DIFFERENT dimension, 6, not 8).
# ----------------------------------------------------------------------


def nullspace_basis(stacked: np.ndarray, tol: float = TOL) -> np.ndarray:
    """Common nullspace of a vertically-stacked set of linear constraints,
    via SVD -- same pattern as C73's invariant_basis / C73b's
    equivariant_torsion_basis."""
    n_unk = stacked.shape[1]
    _, sv, vh = np.linalg.svd(stacked)
    padded = np.concatenate([sv, np.zeros(max(0, n_unk - len(sv)))])
    return vh.conj().T[:, np.abs(padded) < tol]


def block_global_gen(first_idx, second_idx, dim2: int) -> list[int]:
    """Generalization of R59.block_global to an arbitrary second-factor
    dimension dim2 (R59's own version hardcodes dim2=8)."""
    return [Ii * dim2 + Jj for Ii in first_idx for Jj in second_idx]


def invariant_basis_gen(
    gens: list[np.ndarray], block_idx: list[int], ambient_dim: int
) -> np.ndarray:
    """Generalization of C73's invariant_basis to an arbitrary ambient
    dimension (C73's own version hardcodes 64)."""
    dimb = len(block_idx)
    proj = np.zeros((ambient_dim, dimb), dtype=complex)
    for col, g in enumerate(block_idx):
        proj[g, col] = 1
    stacked = np.vstack([proj.conj().T @ gen @ proj for gen in gens])
    return proj @ nullspace_basis(stacked)


def commutant_nullspace(gens: list[np.ndarray], dim: int) -> np.ndarray:
    """dim(commutant) of a set of operators on C^dim -- by Schur's lemma,
    =1 for a single irreducible piece, =k for k pairwise-inequivalent
    irreducible constituents each with multiplicity 1."""
    ident = np.eye(dim, dtype=complex)
    stacked = np.vstack([np.kron(g.T, ident) - np.kron(ident, g) for g in gens])
    return nullspace_basis(stacked)


def intertwiner_nullspace(
    gens_a: list[np.ndarray], dim_a: int, gens_b: list[np.ndarray], dim_b: int
) -> np.ndarray:
    """All T (dim_b x dim_a) satisfying T@A = B@T for every paired
    (A,B) in zip(gens_a,gens_b) -- i.e. all equivariant maps intertwining
    the SAME set of abstract generators represented on two different
    spaces. Zero nullspace = no equivariant relation exists between the
    two representations under this generator set."""
    ident_a = np.eye(dim_a, dtype=complex)
    ident_b = np.eye(dim_b, dtype=complex)
    stacked = np.vstack(
        [np.kron(a.T, ident_b) - np.kron(ident_a, b) for a, b in zip(gens_a, gens_b)]
    )
    return nullspace_basis(stacked)


def build_twisted_dirac_np(
    e_np: dict[int, np.ndarray],
    nab_np: dict[int, np.ndarray],
    dim_w: int,
    conn_w_np: dict[int, np.ndarray],
) -> np.ndarray:
    """D'(eta (x) w) = sum_i (e_i.nabla^Sigma_i eta)(x)w + (e_i.eta)(x)(nabla^W_i w).
    Same Leibniz structure as R59.build_dirac, parameterized over an
    arbitrary twist-bundle dimension dim_w and connection conn_w_np."""
    iw = np.eye(dim_w, dtype=complex)
    dim = 8 * dim_w
    d_mat = np.zeros((dim, dim), dtype=complex)
    for i in range(1, 7):
        d_mat += np.kron(e_np[i] @ nab_np[i], iw) + np.kron(e_np[i], conn_w_np[i])
    return d_mat


def bivec_to_6x6_sympy(terms) -> sp.Matrix:
    """Exact-arithmetic sibling of C73b's bivec_to_6x6 (which uses python
    complex floats) -- same formula, sympy Rational/sqrt(3) coefficients."""
    mat = sp.zeros(6, 6)
    for coeff, a, b in terms:
        i, j = a - 1, b - 1
        mat[i, j] += coeff
        mat[j, i] -= coeff
    return mat


def rho_vector(terms) -> np.ndarray:
    """Vector/defining representation of an so(6) bivector, SIGN-CORRECTED
    for consistency with this project's own spin_lift/Clifford convention
    (e_k^2=-1). See decision.md Section 3d: C73b's own bivec_to_6x6 (reused
    UNMODIFIED for its formula) is internally consistent on its own (used
    self-contained in C73b, so its own dim-2-Hom-space finding is
    unaffected by an overall sign), but a DIRECT structure-constant
    comparison against spin_lift(ADNU) (this round's first-ever joint use
    of the two representations in a single Leibniz generator) shows they
    represent the SAME abstract so(6) generator with OPPOSITE sign under
    e_k^2=-1 (f_sigma = -f_m exactly, machine precision) -- a genuine,
    self-caught convention mismatch, the exact 'phase inventory' trap this
    project has hit before (G102's spin_lift anti-homomorphism fix, pearl
    row 85). Negating here (not touching C73b's own file) restores
    consistency; verified by the structure-constant regression check
    below, run BEFORE any invariant-sector computation."""
    return -C73B.bivec_to_6x6(terms)


def rho_vector_sympy(terms) -> sp.Matrix:
    """Exact-arithmetic, sign-corrected sibling of rho_vector -- same
    correction, sympy Rational/sqrt(3) coefficients."""
    return -bivec_to_6x6_sympy(terms)


def common_nullspace_in_block_sym(gens, block_gidx: list[int], ambient_dim: int):
    """Generalization of R59.common_nullspace_in_block to an arbitrary
    ambient dimension (R59's own version hardcodes 64)."""
    dimb = len(block_gidx)
    proj = sp.zeros(ambient_dim, dimb)
    for col, g in enumerate(block_gidx):
        proj[g, col] = 1
    stacked = sp.zeros(0, dimb)
    for gen in gens:
        gen_b = proj.T * gen * proj
        stacked = stacked.col_join(gen_b)
    ns = stacked.nullspace()
    return [proj * v for v in ns]


def build_twisted_dirac_sympy(e_sym, nab_sym, dim_w: int, conn_w_sym: dict[int, sp.Matrix]):
    iw = sp.eye(dim_w)
    dim = 8 * dim_w
    d_mat = sp.zeros(dim, dim)
    for i in range(1, 7):
        d_mat += R59.kron(e_sym[i] * nab_sym[i], iw) + R59.kron(e_sym[i], conn_w_sym[i])
    return d_mat


# ========================================================================
# 1. Build the unchanged (Sigma-side) machinery -- exactly round59's own.
# ========================================================================
print("=== 1. Sigma-side machinery (unchanged from round59) ===")

E_sym = R59.build_clifford(conj=False)
E_np = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}

NAB_sym = {i: R59.spin_lift(R59.NOMIZU[i], E_sym) for i in range(1, 7)}
NAB_np = {i: np.array(NAB_sym[i].evalf(), dtype=complex) for i in range(1, 7)}

su3_ops_sym = {a: R59.spin_lift(R59.ADNU[a], E_sym) for a in range(1, 9)}
su3_ops_np = {a: np.array(su3_ops_sym[a].evalf(), dtype=complex) for a in range(1, 9)}

# First-factor calibration is UNCHANGED (same Sigma/E/NOMIZU) -- re-verify
# as a regression check, not assumed.
calib_ok, _ = R59.run_calibration(E_sym, R59.NOMIZU)
check(
    "sigma_side_killing_spinor_calibration_still_passes_unchanged",
    calib_ok,
    "first factor (Sigma, Clifford action) is byte-identical to round59's own -- "
    "this is a regression check, not a new result",
)

DATA["nomizu_reused_unmodified"] = {str(i): [str(c) for c in R59.NOMIZU[i]] for i in range(1, 7)}

# ========================================================================
# 2. Build the alternate twist bundle W' = m_C (vector/tangent rep of
#    so(6)), pre-registered choice, see decision.md Section 2.
# ========================================================================
print("\n=== 2. Twist bundle W' = m_C (complexified tangent rep of S6) ===")

rho_m_nomizu_np = {i: rho_vector(R59.NOMIZU[i]) for i in range(1, 7)}
rho_m_adnu_np = {a: rho_vector(R59.ADNU[a]) for a in range(1, 9)}

# ------------------------------------------------------------------
# 2a. STRUCTURE-CONSTANT REGRESSION CHECK (self-caught defect, see
# decision.md Section 3d) -- run BEFORE any invariant-sector computation.
# C73b's own bivec_to_6x6 (reused unmodified in formula) and round59's own
# spin_lift represent the SAME abstract so(6) generator with OPPOSITE sign
# under this project's e_k^2=-1 Clifford convention (verified below by a
# from-scratch structure-constant extraction, independent of the a priori
# derivation in this file's docstring for rho_vector). rho_vector()
# negates bivec_to_6x6's output to restore consistency; this check
# confirms the fix, not just asserts it.
# ------------------------------------------------------------------
EVEN_IDX_local3 = R59.EVEN_IDX


def _structure_constants(gens_dict: dict[int, np.ndarray], n_gen: int = 8) -> np.ndarray:
    """Extract f_abc from [gens[a],gens[b]] = sum_c f_abc*gens[c] via least
    squares against the generator basis (any faithful rep of su(3) with 8
    linearly independent generators works as the extraction basis)."""
    basis = np.stack([gens_dict[c].flatten() for c in range(1, n_gen + 1)], axis=1)
    basis_pinv = np.linalg.pinv(basis)
    f = np.zeros((n_gen, n_gen, n_gen), dtype=complex)
    for a in range(1, n_gen + 1):
        for b in range(1, n_gen + 1):
            bracket = gens_dict[a] @ gens_dict[b] - gens_dict[b] @ gens_dict[a]
            f[a - 1, b - 1, :] = basis_pinv @ bracket.flatten()
    return f


su3_ops_even3_reference = {
    a: su3_ops_np[a][np.ix_(EVEN_IDX_local3, EVEN_IDX_local3)][1:, 1:] for a in range(1, 9)
}
f_sigma_ref = _structure_constants(su3_ops_even3_reference)
f_m_fixed = _structure_constants(rho_m_adnu_np)
mask_sig = np.abs(f_sigma_ref) > 1e-3
check(
    "rho_vector_sign_fix_matches_spin_lift_structure_constants",
    bool(np.max(np.abs((f_sigma_ref - f_m_fixed)[mask_sig])) < 1e-6),
    f"max|f_sigma - f_m_fixed| over nonzero entries = "
    f"{float(np.max(np.abs((f_sigma_ref - f_m_fixed)[mask_sig]))):.3e} (post-fix, expect ~0; "
    "pre-fix this was exactly -f_sigma, i.e. max|f_sigma+f_m|~1e-15 -- see decision.md Section 3d)",
)

check(
    "rho_m_nomizu_real_antisymmetric_all_i",
    all(
        np.max(np.abs(rho_m_nomizu_np[i].imag)) < TOL
        and np.max(np.abs(rho_m_nomizu_np[i] + rho_m_nomizu_np[i].T)) < TOL
        for i in range(1, 7)
    ),
    "nabla^m_i must be real+antisymmetric (=anti-Hermitian) to generate a genuine "
    "metric SO(6) connection -- true by construction (bivec_to_6x6), verified not assumed",
)
check(
    "rho_m_adnu_real_antisymmetric_all_a",
    all(
        np.max(np.abs(rho_m_adnu_np[a].imag)) < TOL
        and np.max(np.abs(rho_m_adnu_np[a] + rho_m_adnu_np[a].T)) < TOL
        for a in range(1, 9)
    ),
)

# m has NO su(3) singlet (module type has zero trivial summand, unlike
# Sigma's 1+1+3+3bar) -- verified via common nullspace of the 8 su(3)
# generators acting on C^6, not just asserted from the "3+3bar" label.
m_singlet_stacked = np.vstack([rho_m_adnu_np[a] for a in range(1, 9)])
m_singlet_basis = nullspace_basis(m_singlet_stacked)
check(
    "m_has_no_su3_singlet_dim_0",
    m_singlet_basis.shape[1] == 0,
    f"dim common nullspace of ADNU-action on C^6 = {m_singlet_basis.shape[1]} (expect 0)",
)

# m decomposes into exactly 2 pairwise-inequivalent su(3)-irreducible
# pieces (3 and 3bar, each multiplicity 1) -- Schur's lemma via commutant.
m_gens_adnu = [rho_m_adnu_np[a] for a in range(1, 9)]
comm_m = commutant_nullspace(m_gens_adnu, 6)
check(
    "m_commutant_under_su3_has_dim_2",
    comm_m.shape[1] == 2,
    f"dim(commutant)={comm_m.shape[1]} (expect 2, confirming 2 inequivalent "
    "irreducible su(3)-constituents each multiplicity 1 -- '3+3bar', not '6' "
    "irreducible or a higher-multiplicity structure)",
)
DATA["m_module_type_check"] = {
    "no_singlet": bool(m_singlet_basis.shape[1] == 0),
    "commutant_dim_under_su3": int(comm_m.shape[1]),
}

# ========================================================================
# 3. Undisclosed-symmetry check -- BEFORE computing any kernel (per
#    claim.md's explicit instruction and this project's own C73 "hidden
#    even/odd duality" trap): is W'=m secretly Sigma (or a piece of it) in
#    disguise?
# ========================================================================
print("\n=== 3. Undisclosed-symmetry check (done BEFORE the kernel computation) ===")

# 3a. Does spin_lift(bivector) preserve Sigma's even/odd parity for a
# GENERIC so(6) bivector (not just ADNU's su(3) subalgebra)? If NOT, the
# irreducibility argument below is invalid. Verified directly on NAB_i.
off_diag_max = max(
    float(np.max(np.abs(NAB_np[i][np.ix_(R59.EVEN_IDX, R59.ODD_IDX)]))) for i in range(1, 7)
)
check(
    "nab_i_preserves_sigma_even_odd_parity",
    off_diag_max < TOL,
    f"max|NAB_i[even,odd]| = {off_diag_max:.3e} (expect ~0 -- spin_lift of any "
    "so(6) bivector is quadratic in Clifford generators, hence parity-preserving)",
)

# 3b. Sigma's EVEN_IDX (dim4) and ODD_IDX (dim4) blocks are each
# IRREDUCIBLE under {NAB_i} (commutant dim 1) -- so the only
# {NAB_i}-invariant subspace dimensions achievable inside Sigma are
# {0,4,4,8}. 6 is not among them: NO {NAB_i}-invariant 6-dim subspace of
# Sigma can exist at all, independent of whether it would "look like" m.
nab_even_blocks = [NAB_np[i][np.ix_(R59.EVEN_IDX, R59.EVEN_IDX)] for i in range(1, 7)]
nab_odd_blocks = [NAB_np[i][np.ix_(R59.ODD_IDX, R59.ODD_IDX)] for i in range(1, 7)]
comm_even = commutant_nullspace(nab_even_blocks, 4)
comm_odd = commutant_nullspace(nab_odd_blocks, 4)
check(
    "sigma_even_block_irreducible_under_nab",
    comm_even.shape[1] == 1,
    f"dim(commutant)={comm_even.shape[1]} on S+ (expect 1 -- irreducible)",
)
check(
    "sigma_odd_block_irreducible_under_nab",
    comm_odd.shape[1] == 1,
    f"dim(commutant)={comm_odd.shape[1]} on S- (expect 1 -- irreducible)",
)

# 3c. Direct intertwiner search: no nonzero linear map T:Sigma(8)->m(6)
# equivariant under the SAME 6 connection generators {NAB_i} <-> {rho_m
# (NOMIZU_i)} exists. This is the most direct, construction-independent
# test of "is nabla^m secretly nabla^Sigma restricted to a subspace,
# under a change of basis" -- the exact shape of trap (b) in C73
# (a hidden duality reproducing IDENTICAL numbers under relabeling).
gens_a_sigma = [NAB_np[i] for i in range(1, 7)]
gens_b_m = [rho_m_nomizu_np[i] for i in range(1, 7)]
t_intertwiner = intertwiner_nullspace(gens_a_sigma, 8, gens_b_m, 6)
check(
    "no_equivariant_map_sigma_to_m_under_nomizu_connection",
    t_intertwiner.shape[1] == 0,
    f"dim(intertwiner space)={t_intertwiner.shape[1]} (expect 0 -- confirms nabla^m "
    "is NOT nabla^Sigma restricted to a 6-dim subspace under any change of basis; "
    "consistent with 3b: Sigma's only invariant-subspace dims are {0,4,8}, and "
    "with vector-6 / half-spin-4 / half-spin-4bar being pairwise-inequivalent "
    "irreducible representations of so(6)=su(4)) -- CATCHES THE EXACT UNDISCLOSED-"
    "SYMMETRY TRAP THAT INVALIDATED C73's ATTEMPT (b), CHECKED HERE BEFORE ANY "
    "KERNEL COMPUTATION",
)
DATA["undisclosed_symmetry_check"] = {
    "sigma_dims_achievable": [0, 4, 4, 8],
    "m_dim": 6,
    "intertwiner_nullspace_dim": int(t_intertwiner.shape[1]),
}

# ========================================================================
# 4. su(3)-invariant sector dimensions -- pre-registered representation-
#    theory prediction (decision.md Section 2), verified against the
#    independent SVD/nullspace computation.
# ========================================================================
print("\n=== 4. su(3)-invariant sector dimensions (domain, target) ===")

i8 = np.eye(8, dtype=complex)
i6 = np.eye(6, dtype=complex)
gens_leibniz_48 = [np.kron(su3_ops_np[a], i6) + np.kron(i8, rho_m_adnu_np[a]) for a in range(1, 9)]

domain_block = block_global_gen(R59.ODD_IDX, list(range(6)), 6)
target_block = block_global_gen(R59.EVEN_IDX, list(range(6)), 6)

domain_inv = invariant_basis_gen(gens_leibniz_48, domain_block, 48)
target_inv = invariant_basis_gen(gens_leibniz_48, target_block, 48)

check(
    "domain_inv_dim_matches_clebsch_gordan_prediction_1",
    domain_inv.shape[1] == 1,
    f"dim(ODD_IDX(x)m)_su3-inv = {domain_inv.shape[1]} (predicted 1, from "
    "(3(+)1)(x)(3(+)3bar) = 1(+)3(+)3bar(+)3bar(+)6(+)8, trivial multiplicity 1)",
)
check(
    "target_inv_dim_matches_clebsch_gordan_prediction_1",
    target_inv.shape[1] == 1,
    f"dim(EVEN_IDX(x)m)_su3-inv = {target_inv.shape[1]} (predicted 1, from "
    "(1(+)3bar)(x)(3(+)3bar) = 1(+)3(+)3(+)3bar(+)6bar(+)8, trivial multiplicity 1)",
)
DATA["invariant_sector_dims"] = {
    "domain_ODD_x_m": int(domain_inv.shape[1]),
    "target_EVEN_x_m": int(target_inv.shape[1]),
    "round59_comparison_domain_ODD_x_EVEN": 2,
    "round59_comparison_target_EVEN_x_EVEN": 1,
}

# ========================================================================
# 5. Verification-Substrate-Gate self-consistency: the SAME generalized
#    machinery, applied with W'=Sigma (dim 8) instead of W'=m (dim 6),
#    must reproduce round59/C73's own certified numbers EXACTLY.
# ========================================================================
print("\n=== 5. Self-consistency: generalized machinery reproduces round59 exactly ===")

d_selfcheck = build_twisted_dirac_np(E_np, NAB_np, 8, NAB_np)
d_c73_reference = C73.build_numeric_dirac(E_sym, R59.NOMIZU)
check(
    "generalized_dirac_matches_c73_reference_when_twist_equals_sigma",
    bool(np.allclose(d_selfcheck, d_c73_reference, atol=1e-8)),
    f"max|diff| = {float(np.max(np.abs(d_selfcheck - d_c73_reference))):.3e}",
)

gens64_reference = C73.su3_gens64(E_sym)
domain_inv_check = invariant_basis_gen(
    gens64_reference, block_global_gen(R59.ODD_IDX, R59.EVEN_IDX, 8), 64
)
target_inv_check = invariant_basis_gen(
    gens64_reference, block_global_gen(R59.EVEN_IDX, R59.EVEN_IDX, 8), 64
)
block_check = target_inv_check.conj().T @ d_selfcheck @ domain_inv_check
a_check, b_check = complex(block_check[0, 0]), complex(block_check[0, 1])
check(
    "generalized_machinery_reproduces_round59_certificate_a_b",
    bool(abs(abs(a_check) - 1.0) < 1e-6 and abs(abs(b_check) - np.sqrt(3)) < 1e-6),
    f"a={a_check}, b={b_check} (round59 certified: |a|=1, |b|=sqrt(3))",
)
check(
    "generalized_machinery_reproduces_round59_domain_target_dims",
    domain_inv_check.shape[1] == 2 and target_inv_check.shape[1] == 1,
    f"domain={domain_inv_check.shape[1]}, target={target_inv_check.shape[1]} "
    "(round59 certified: 2, 1)",
)
DATA["selfcheck_round59_reproduction"] = {
    "a": str(a_check),
    "b": str(b_check),
    "domain_dim": int(domain_inv_check.shape[1]),
    "target_dim": int(target_inv_check.shape[1]),
}

# ========================================================================
# 6. Main computation: D' with W' = m, restricted to the su(3)-invariant
#    domain/target sectors. This is the round's central result.
# ========================================================================
print("\n=== 6. Main computation: twisted Dirac certificate for W'=m ===")

d_prime = build_twisted_dirac_np(E_np, NAB_np, 6, rho_m_nomizu_np)

check(
    "d_prime_is_hermitian",
    bool(np.max(np.abs(d_prime - d_prime.conj().T)) < 1e-8),
    f"max|D' - D'^dagger| = {float(np.max(np.abs(d_prime - d_prime.conj().T))):.3e}",
)

block_prime = target_inv.conj().T @ d_prime @ domain_inv  # 1x1
c_value = complex(block_prime[0, 0])
rank_prime = int(np.sum(np.linalg.svd(block_prime, compute_uv=False) > 1e-8))
kernel_dim_prime = int(domain_inv.shape[1]) - rank_prime

print(f"  c = <w_hat, D' u_hat> = {c_value}")
print(f"  rank = {rank_prime}, kernel_dim (domain) = {kernel_dim_prime}")

# Genuine, failable quality check: the result must be UNAMBIGUOUS (either
# clearly zero or clearly bounded away from zero), not sitting in a
# numerically ambiguous middle zone -- a legitimate check on computation
# quality, NOT a check on which physics answer is "correct" (this script
# does not know or assume the answer).
c_mag = abs(c_value)
check(
    "c_value_is_numerically_unambiguous",
    c_mag < 1e-9 or c_mag > 1e-4,
    f"|c| = {c_mag:.3e} (must sit clearly on one side of the numerical-noise floor)",
)

# Chirality/Hermiticity cross-check (backward direction), same pattern as
# C73's test_chirality.
forward = block_prime
backward = domain_inv.conj().T @ d_prime @ target_inv
check(
    "forward_is_hermitian_adjoint_of_backward",
    bool(np.max(np.abs(forward - backward.conj().T)) < 1e-8),
    f"max|diff| = {float(np.max(np.abs(forward - backward.conj().T))):.3e}",
)
backward_rank = int(np.sum(np.linalg.svd(backward, compute_uv=False) > 1e-8))
backward_kernel_dim = int(target_inv.shape[1]) - backward_rank

DATA["main_result"] = {
    "c_value": str(c_value),
    "abs_c": c_mag,
    "domain_dim": int(domain_inv.shape[1]),
    "target_dim": int(target_inv.shape[1]),
    "forward_rank": rank_prime,
    "forward_kernel_dim": kernel_dim_prime,
    "backward_rank": backward_rank,
    "backward_kernel_dim": backward_kernel_dim,
    "matches_round59_pattern_kernel_eq_1": bool(kernel_dim_prime == 1),
}

# ------------------------------------------------------------------
# 6a. Term1/Term2 mechanistic decomposition -- mirrors round59's own
# analytic Route C (decision.md: "Term1 = the Killing eigenvalue piece,
# Term2 = 0 by pairwise cancellation AND by rep theory"). Checking whether
# an analogous clean mechanism (one term vanishing) is present here, or
# whether c is a genuinely two-term, non-decomposing number -- this bears
# directly on whether c!=0 reflects a real geometric mechanism (like
# round59's own b) or is comparatively unremarkable. NOT a check with a
# predetermined right answer -- recorded as DATA, interpreted in
# decision.md.
# ------------------------------------------------------------------
iw6 = np.eye(6, dtype=complex)
d_term1_only = np.zeros((48, 48), dtype=complex)
d_term2_only = np.zeros((48, 48), dtype=complex)
for i in range(1, 7):
    d_term1_only += np.kron(E_np[i] @ NAB_np[i], iw6)
    d_term2_only += np.kron(E_np[i], rho_m_nomizu_np[i])
block_term1 = target_inv.conj().T @ d_term1_only @ domain_inv
block_term2 = target_inv.conj().T @ d_term2_only @ domain_inv
c_term1 = complex(block_term1[0, 0])
c_term2 = complex(block_term2[0, 0])
check(
    "term1_plus_term2_equals_full_c",
    bool(abs((c_term1 + c_term2) - c_value) < 1e-8),
    f"term1={c_term1}, term2={c_term2}, sum={c_term1 + c_term2}, full c={c_value}",
)
DATA["term_decomposition"] = {
    "c_term1_killing_eigenvalue_piece": str(c_term1),
    "c_term2_twist_connection_piece": str(c_term2),
    "term2_is_zero": bool(abs(c_term2) < 1e-8),
    "term1_is_zero": bool(abs(c_term1) < 1e-8),
    "note": (
        "round59's own mechanism had Term2=0 (by su(3) rep theory: "
        "Lambda^2(x)Lambda^2 has no singlet) leaving Term1 (the Killing "
        "eigenvalue) as the sole contributor. Here BOTH terms are recorded "
        "so decision.md can state plainly whether the same clean single-"
        "term mechanism recurs, or whether c is a genuinely two-term sum "
        "-- both are legitimate outcomes, neither is assumed."
    ),
}
print(f"  term1 (Killing-eigenvalue piece) = {c_term1}")
print(f"  term2 (twist-connection piece)   = {c_term2}")

# ========================================================================
# 7. Deformation/robustness check: D'(t) should be exactly linear in the
#    NOMIZU scale t (same algebraic argument as C73's own test_deformation,
#    since build_twisted_dirac_np is linear in conn_w_np and nab_np, both
#    of which are linear in the nomizu argument).
# ========================================================================
print("\n=== 7. Deformation/linearity check (same discipline as C73's t-sweep) ===")

deform_sweep = {}
for t_val in [0.5, 2.0]:
    nomizu_t = {i: [(t_val * cf, aa, bb) for (cf, aa, bb) in R59.NOMIZU[i]] for i in R59.NOMIZU}
    nab_t_sym = {i: R59.spin_lift(nomizu_t[i], E_sym) for i in range(1, 7)}
    nab_t_np = {i: np.array(nab_t_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    rho_m_t_np = {i: rho_vector(nomizu_t[i]) for i in range(1, 7)}
    d_t = build_twisted_dirac_np(E_np, nab_t_np, 6, rho_m_t_np)
    block_t = target_inv.conj().T @ d_t @ domain_inv
    c_t = complex(block_t[0, 0])
    deform_sweep[str(t_val)] = {"c": str(c_t), "predicted_c": str(t_val * c_value)}
    check(
        f"d_prime_linear_in_nomizu_scale_t={t_val}",
        bool(abs(c_t - t_val * c_value) < 1e-6),
        f"c(t={t_val})={c_t}, t*c(1)={t_val * c_value}",
    )
DATA["deformation_sweep"] = deform_sweep

# ========================================================================
# 7b. ANGULAR SWEEP across C73b's own 2-dimensional admissible su(3)-
# equivariant torsion family Hom_su(3)(m_tangent, Lambda^2 m_tangent) --
# added in response to FL Step 8a skeptic pass 2, which correctly noted
# that Term2 is a LINEAR functional of the connection direction within
# this 2-dim (C73b-established) family, so a SINGLE point (NOMIZU) giving
# Term2!=0 does not by itself establish that Term2!=0 HOLDS ACROSS the
# admissible family (a linear functional on a real 2-dim space generically
# has a 1-dim zero locus) -- exactly the same concern C73b itself raised
# and answered, for round59's OWN kernel, via a 13-angle sweep (its own
# Part 3). This section runs the IDENTICAL sweep for the m-twisted
# operator, reusing C73b's own equivariant_torsion_basis/m_generators/
# vec_to_nomizu_dict UNMODIFIED, to determine whether kernel=0 holds
# ACROSS the whole admissible family (matching round59's own
# "topologically protected" finding) or only at NOMIZU's specific point
# (the skeptic's "single-direction accident" concern).
# ========================================================================
print("\n=== 7b. Angular sweep across the 2-dim admissible torsion family (skeptic-2 test) ===")

m_gens_for_sweep = C73B.m_generators()
torsion_basis = C73B.equivariant_torsion_basis(m_gens_for_sweep)
check(
    "torsion_family_is_2dim_matches_c73b",
    torsion_basis.shape[1] == 2,
    f"dim Hom_su3(m,Lambda^2 m) = {torsion_basis.shape[1]} (C73b certified: 2)",
)
t1_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 0])
t2_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 1])

# Confirm NOMIZU itself reconstructs in this basis (same check C73b did,
# re-run here as a regression/consistency guard before trusting the sweep).
nomizu_vec_check = C73B.nomizu_to_vec(R59.NOMIZU)
coeffs_check, *_ = np.linalg.lstsq(torsion_basis, nomizu_vec_check, rcond=None)
recon_residual = float(np.max(np.abs(torsion_basis @ coeffs_check - nomizu_vec_check)))
check(
    "nomizu_reconstructs_in_torsion_basis",
    recon_residual < 1e-8,
    f"residual={recon_residual:.3e} (C73b certified: 5.6e-16)",
)

angle_sweep: dict[str, dict] = {}
term1_ever_nonzero = False
c_ever_zero = False
abs_c_values = []
for theta_deg in [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270]:
    theta = np.deg2rad(theta_deg)
    combo_dict = {k: np.cos(theta) * t1_dict[k] + np.sin(theta) * t2_dict[k] for k in range(1, 7)}
    nomizu_theta = C73B.matdict_to_nomizu(combo_dict)
    nab_theta_sym = {i: R59.spin_lift(nomizu_theta[i], E_sym) for i in range(1, 7)}
    nab_theta_np = {i: np.array(nab_theta_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    rho_m_theta_np = {i: rho_vector(nomizu_theta[i]) for i in range(1, 7)}

    d_theta = build_twisted_dirac_np(E_np, nab_theta_np, 6, rho_m_theta_np)
    block_theta = target_inv.conj().T @ d_theta @ domain_inv
    c_theta = complex(block_theta[0, 0])

    d_theta_term1_only = np.zeros((48, 48), dtype=complex)
    for i in range(1, 7):
        d_theta_term1_only += np.kron(E_np[i] @ nab_theta_np[i], iw6)
    term1_theta = complex((target_inv.conj().T @ d_theta_term1_only @ domain_inv)[0, 0])

    calib_theta_ok, _ = R59.run_calibration(E_sym, nomizu_theta)
    angle_sweep[str(theta_deg)] = {
        "c": str(c_theta),
        "abs_c": abs(c_theta),
        "term1": str(term1_theta),
        "calibration_passes": bool(calib_theta_ok),
    }
    abs_c_values.append(abs(c_theta))
    if abs(term1_theta) > 1e-6:
        term1_ever_nonzero = True
    if abs(c_theta) < 1e-6:
        c_ever_zero = True

DATA["angular_sweep_torsion_family"] = angle_sweep
abs_c_arr = np.array(abs_c_values)
abs_c_spread = float(np.max(abs_c_arr) - np.min(abs_c_arr))
DATA["angular_sweep_summary"] = {
    "abs_c_min": float(np.min(abs_c_arr)),
    "abs_c_max": float(np.max(abs_c_arr)),
    "abs_c_spread": abs_c_spread,
    "term1_ever_nonzero_across_sweep": term1_ever_nonzero,
    "c_ever_zero_across_sweep": c_ever_zero,
}
print(
    f"  |c(theta)| range: [{np.min(abs_c_arr):.6f}, {np.max(abs_c_arr):.6f}]  spread={abs_c_spread:.3e}"
)
print(f"  Term1 nonzero anywhere in sweep: {term1_ever_nonzero}")
print(f"  c(theta) hits zero anywhere in sweep: {c_ever_zero}")

# Genuine, failable checks -- the sweep can go either way and both
# outcomes are informative (this is not tuned to force a particular
# answer):
check(
    "term1_remains_exactly_zero_across_whole_torsion_family",
    not term1_ever_nonzero,
    "Term1=0 forced by su(3)-equivariance + zero-singlet module type "
    "(Section 8b) -- should hold for EVERY admissible connection direction, "
    "not just NOMIZU's own point, since the forcing argument never used "
    "NOMIZU's specific numeric values",
)
check(
    "abs_c_is_constant_across_whole_torsion_family",
    abs_c_spread < 1e-6,
    f"|c(theta)| spread={abs_c_spread:.3e} across 13 angles -- if constant "
    "(matching C73b's OWN finding that |b|=sqrt(3) is constant for round59's "
    "kernel across its own 13-angle sweep), Term2 is C-LINEAR in a single "
    "complex parameter (not merely R-linear in 2 independent reals), and "
    "its zero locus is the single point 'zero connection', not a 1-dim "
    "line within the family -- directly answering skeptic pass 2's "
    "single-direction-accident concern. If NOT constant, that concern "
    "stands and is reported honestly, not hidden.",
)
check(
    "kernel_zero_holds_across_whole_torsion_family",
    not c_ever_zero,
    "if kernel=0 holds at every tested angle (not just NOMIZU's own point), "
    "this is 'topologically protected across the whole admissible family' "
    "in exactly the sense C73b certified for round59's OWN kernel=1 -- "
    "the direct, decisive answer to skeptic pass 2's central objection",
)

# ========================================================================
# 8. EXACT (sympy) cross-check of the headline number c -- same evidence
#    tier round59 itself used for (a,b,s), not just floating point.
# ========================================================================
print("\n=== 8. Exact sympy cross-check of c ===")

rho_m_nomizu_sym = {i: rho_vector_sympy(R59.NOMIZU[i]) for i in range(1, 7)}
rho_m_adnu_sym = {a: rho_vector_sympy(R59.ADNU[a]) for a in range(1, 9)}

gens_leibniz_48_sym = [
    R59.kron(su3_ops_sym[a], sp.eye(6)) + R59.kron(sp.eye(8), rho_m_adnu_sym[a])
    for a in range(1, 9)
]

domain_inv_sym = common_nullspace_in_block_sym(gens_leibniz_48_sym, domain_block, 48)
target_inv_sym = common_nullspace_in_block_sym(gens_leibniz_48_sym, target_block, 48)

check(
    "exact_domain_inv_dim_matches_numeric",
    len(domain_inv_sym) == domain_inv.shape[1],
    f"exact={len(domain_inv_sym)}, numeric={domain_inv.shape[1]}",
)
check(
    "exact_target_inv_dim_matches_numeric",
    len(target_inv_sym) == target_inv.shape[1],
    f"exact={len(target_inv_sym)}, numeric={target_inv.shape[1]}",
)

d_prime_sym = build_twisted_dirac_sympy(E_sym, NAB_sym, 6, rho_m_nomizu_sym)
domain_on_sym = R59.gram_schmidt(domain_inv_sym)
target_on_sym = R59.gram_schmidt(target_inv_sym)
c_exact = None
if domain_on_sym and target_on_sym:
    u_hat = domain_on_sym[0]
    w_hat = target_on_sym[0]
    c_exact = sp.simplify(R59.hip(w_hat, d_prime_sym * u_hat))
    c_exact_radsimp = sp.nsimplify(sp.radsimp(c_exact))
    print(f"  c_exact = {c_exact_radsimp}")
    c_exact_float = complex(sp.N(c_exact))
    # NOTE: since domain_inv/target_inv are each 1-DIMENSIONAL, the
    # orthonormal basis vector (u_hat, w_hat) is only defined up to an
    # independent overall PHASE in each of the two nullspace routes (SVD
    # numeric vs sympy exact) -- an expected U(1) gauge freedom, not a
    # discrepancy. The gauge-INVARIANT quantity is |c| (equivalently
    # s=|c|^2, the direct analogue of round59's own s=|a|^2+|b|^2
    # certificate) -- compared here, not the raw phase.
    check(
        "exact_abs_c_matches_numeric_abs_c",
        bool(abs(abs(c_exact_float) - abs(c_value)) < 1e-6),
        f"|exact|={abs(c_exact_float):.10f}, |numeric|={abs(c_value):.10f} -- raw phases "
        f"legitimately differ (exact={c_exact_float}, numeric={c_value}) because domain/target "
        "are each 1-dim, so the orthonormal-basis PHASE is a free gauge choice independent "
        "between the SVD-numeric and sympy-exact nullspace routes; |c| is gauge-invariant",
    )
    check(
        "exact_c_is_exactly_zero_or_clearly_nonzero",
        bool(sp.simplify(c_exact) == 0) or abs(complex(sp.N(c_exact))) > 1e-6,
        f"c_exact={c_exact_radsimp}, simplifies to zero: {sp.simplify(c_exact) == 0}",
    )
    s_exact = sp.simplify(c_exact * sp.conjugate(c_exact))
    s_exact_radsimp = sp.nsimplify(sp.radsimp(s_exact))
    print(f"  s_exact = |c_exact|^2 = {s_exact_radsimp}")
    DATA["c_exact"] = str(c_exact_radsimp)
    DATA["s_exact"] = str(s_exact_radsimp)
    DATA["c_exact_is_symbolically_zero"] = bool(sp.simplify(c_exact) == 0)
else:
    DATA["c_exact"] = None
    DATA["c_exact_note"] = "domain or target exact-nullspace empty -- see numeric result only"

# ------------------------------------------------------------------------
print("\n=== SUMMARY ===")
n_ok = sum(1 for v in RESULTS.values() if v)
print(
    f"  boolean checks : {len(RESULTS)} distinct names from {N_CHECK_CALLSITES} call sites  (passed {n_ok})"
)
print(f"  recorded data  : {len(DATA)}  -- NOT counted as checks")
print("  hardcoded-condition self-audit: PASS (no check() takes a literal)")
print(f"  failures       : {len(FAILURES)}  {FAILURES}")
print(f"\n  HEADLINE: c = {c_value}  |c| = {c_mag:.6e}")
print(f"  forward kernel_dim = {kernel_dim_prime}  (domain dim {domain_inv.shape[1]})")
print(f"  matches round59 pattern (kernel==1): {kernel_dim_prime == 1}")

with open(RESULTS_PATH, "w") as f:
    json.dump({"checks": RESULTS, "data": DATA}, f, indent=2, sort_keys=True, default=str)
print(f"  wrote {RESULTS_PATH}")
