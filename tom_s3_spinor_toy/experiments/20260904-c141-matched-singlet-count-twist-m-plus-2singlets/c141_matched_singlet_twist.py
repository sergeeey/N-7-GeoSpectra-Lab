"""C141 -- twist bundle W'' = m_C (+) 2*1 (dim 8, module type 3+3bar+1+1, TWO
su(3) singlets -- matching Sigma's own 1+1+3+3bar singlet count), using the
precheck-cleared "decoupled extra singlets" connection
(conn_i = rho_vector(NOMIZU[i]) (+) 0_2). Does D_S6's invariant-sector kernel
still differ from 1 for this shape-matched (by singlet COUNT) alternative?

This is the direct, both-skeptic-recommended follow-up to C139
(20260904-c139-twisted-s6-alternate-representation-negative-control), which
found kernel=0 (not 1) for W'=m (dim 6, ZERO singlets) but was qualified: the
(1,1)-shaped invariant sector there is a FORCED consequence of m's
zero-singlet module type (C139 Sec 8b), not evidence D_S6 prefers Sigma's
specific geometric content over ANY alternative. Both skeptic passes on C139
converged on testing a twist bundle with Sigma's OWN singlet count (two) as
the decisive follow-up.

PRE-REGISTRATION (see decision.md Section 2 for the full derivation, done BY
HAND before any code in this file was run): claim.md's own naive expectation
("singlet count matches two, so shape should match Sigma's own (2,1)") is
CHECKED here via careful Clebsch-Gordan bookkeeping, not merely assumed. The
derivation (decision.md Sec 2) finds the naive expectation is WRONG: matching
singlet COUNT does not imply matching invariant-sector SHAPE, because in
Sigma the two singlets are split one-into-EVEN_IDX, one-into-ODD_IDX, whereas
in W''=m(+)2*1 BOTH extra singlets sit together in the SAME twist bundle that
gets tensored into BOTH the domain (ODD_IDX(x)W'') and target (EVEN_IDX(x)W'')
computations -- by-hand CG bookkeeping predicts domain=target=3, NOT (2,1).
This is verified computationally below (Section 4), not merely asserted.

Reuses UNMODIFIED: C139's build_twisted_dirac_np, rho_vector, rho_vector_sympy,
invariant_basis_gen, block_global_gen, nullspace_basis, commutant_nullspace,
intertwiner_nullspace, common_nullspace_in_block_sym, build_twisted_dirac_sympy
(all dim-agnostic, per claim.md's explicit instruction); C139's own
precheck script's EXACT connection construction
(conn_m_plus_2singlets, the "decoupled extra singlets" object itself, not a
re-typed formula) via direct import; R59's build_clifford/spin_lift/NOMIZU/
ADNU/EVEN_IDX/ODD_IDX/gram_schmidt/hip/kron/run_calibration (via C139.R59);
C73B's m_generators/equivariant_torsion_basis/vec_to_nomizu_dict/
matdict_to_nomizu (via C139.C73B), for the angular-family robustness sweep.

AST self-audit: refuses to run if any check() call is passed a literal
constant -- same pattern as C130/C133/C134/C136/C138/C139.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c141.json"
C139_DIR = HERE.parent / "20260904-c139-twisted-s6-alternate-representation-negative-control"
C139_MAIN_PATH = C139_DIR / "c139_twisted_s6_alternate_representation.py"
C139_PRECHECK_PATH = C139_DIR / "c139_precheck_m_plus_2singlets.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("Loading C139's own main module (reuses build_twisted_dirac_np, rho_vector, ...)...")
C139 = load_module("c141_c139_main", C139_MAIN_PATH)
print("\nLoading C139's own precheck module (reuses conn_m_plus_2singlets construction)...")
PRECHECK = load_module("c141_c139_precheck", C139_PRECHECK_PATH)

R59 = C139.R59
C73B = C139.C73B

RESULTS: dict[str, bool] = {}
DATA: dict[str, object] = {}
FAILURES: list[str] = []


def _self_audit_no_hardcoded_checks() -> int:
    """Reject any check(...) whose condition is a LITERAL constant in the
    source -- same discipline as C130/C133/C134/C136/C138/C139."""
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

# ========================================================================
# 0. Substrate-Gate regression: confirm C139's own module loaded clean
#    (all its own checks passed) before trusting anything reused from it.
# ========================================================================
print("\n=== 0. Substrate-Gate regression: C139's own checks all passed on (re)load ===")
check(
    "c139_module_all_own_checks_passed_on_fresh_reload",
    len(C139.FAILURES) == 0 and len(C139.RESULTS) > 0,
    f"C139 fresh-reloaded {len(C139.RESULTS)} checks, {len(C139.FAILURES)} failures "
    f"(expect 0 -- confirms the reused substrate (build_twisted_dirac_np, rho_vector, "
    "R59/C73/C73B data) is sound in THIS round's own execution context, not merely "
    "cited from a stale prior run)",
)
check(
    "c139_own_headline_kernel_still_zero_on_fresh_reload",
    C139.DATA["main_result"]["forward_kernel_dim"] == 0,
    f"C139's own kernel = {C139.DATA['main_result']['forward_kernel_dim']} (expect 0, "
    "regression-checked here, not merely cited from decision.md prose)",
)

# ========================================================================
# 1. PRE-REGISTRATION -- Clebsch-Gordan derivation done BY HAND before any
#    invariant-sector computation below, per claim.md's explicit instruction.
#    See this file's own module docstring and decision.md Section 2 for the
#    full derivation; encoded here as data to check against, not invented
#    after seeing the numeric answer.
# ========================================================================
print("\n=== 1. Pre-registered CG prediction (derived by hand BEFORE computing) ===")
# EVEN_IDX = 1 (+) 3bar, ODD_IDX = 3 (+) 1 (C139 Sec 2, reused unmodified).
# W'' = m (+) 2*1 = 3 (+) 3bar (+) 1 (+) 1.
# mult(trivial in A(x)B) = sum over irreducible constituents a of A of
#   mult_A(a) * mult_B(a*)  [Frobenius reciprocity / Schur orthogonality].
# Encoded as an explicit, GENUINELY COMPUTED function below (not asserted by
# prose) so the round59 cross-validation and the new W'' prediction are both
# real, failable checks -- not a hardcoded "trust me" literal.

SU3_DUAL = {"1": "1", "3": "3bar", "3bar": "3", "6": "6bar", "6bar": "6", "8": "8"}


def trivial_mult(module_a: dict[str, int], module_b: dict[str, int]) -> int:
    """mult(trivial rep in A(x)B) via Frobenius reciprocity: sum over
    irreducible constituents `a` of A of mult_A(a) * mult_B(dual(a))."""
    return sum(mult_a * module_b.get(SU3_DUAL[irrep], 0) for irrep, mult_a in module_a.items())


EVEN_IDX_MODULE = {"1": 1, "3bar": 1}  # C139 Sec 2, reused unmodified
ODD_IDX_MODULE = {"3": 1, "1": 1}  # C139 Sec 2, reused unmodified
W2_MODULE = {"3": 1, "3bar": 1, "1": 2}  # this round's own W''=m(+)2*1

# Cross-validate the METHOD ITSELF against round59's OWN already-certified
# (domain=2, target=1), computed via the SAME trivial_mult() function, before
# trusting it for the new W'' prediction (same discipline C139 Sec 4 used
# before trusting its own (1,1) prediction for W'=m).
cg_domain_round59_predicted = trivial_mult(ODD_IDX_MODULE, EVEN_IDX_MODULE)
cg_target_round59_predicted = trivial_mult(EVEN_IDX_MODULE, EVEN_IDX_MODULE)
check(
    "cg_method_reproduces_round59_own_certified_domain_2_via_trivial_mult_function",
    cg_domain_round59_predicted == 2,
    f"trivial_mult(ODD_IDX_MODULE, EVEN_IDX_MODULE) = {cg_domain_round59_predicted} "
    "(round59 certified domain_inv = 2)",
)
check(
    "cg_method_reproduces_round59_own_certified_target_1_via_trivial_mult_function",
    cg_target_round59_predicted == 1,
    f"trivial_mult(EVEN_IDX_MODULE, EVEN_IDX_MODULE) = {cg_target_round59_predicted} "
    "(round59 certified target_inv = 1)",
)

PREREGISTERED_DOMAIN_INV = trivial_mult(ODD_IDX_MODULE, W2_MODULE)
PREREGISTERED_TARGET_INV = trivial_mult(EVEN_IDX_MODULE, W2_MODULE)
CLAIM_MD_NAIVE_DOMAIN = 2
CLAIM_MD_NAIVE_TARGET = 1
print(
    f"  By-hand CG prediction (this round's own derivation, via trivial_mult()): "
    f"domain={PREREGISTERED_DOMAIN_INV}, target={PREREGISTERED_TARGET_INV}"
)
print(
    f"  claim.md's own naive expectation (singlet-COUNT heuristic, not full CG): "
    f"domain={CLAIM_MD_NAIVE_DOMAIN}, target={CLAIM_MD_NAIVE_TARGET}"
)
check(
    "preregistered_prediction_computed_before_any_invariant_sector_numerics",
    PREREGISTERED_DOMAIN_INV == 3 and PREREGISTERED_TARGET_INV == 3,
    f"trivial_mult()-computed prediction = ({PREREGISTERED_DOMAIN_INV},{PREREGISTERED_TARGET_INV}) "
    "-- this is what decision.md's Section 2 states was derived by hand BEFORE this "
    "script existed; this check confirms the CODE's independent computation of the same "
    "formula agrees with the hand derivation, not the other way around",
)
DATA["preregistration"] = {
    "by_hand_cg_prediction": {
        "domain": PREREGISTERED_DOMAIN_INV,
        "target": PREREGISTERED_TARGET_INV,
    },
    "claim_md_naive_expectation": {
        "domain": CLAIM_MD_NAIVE_DOMAIN,
        "target": CLAIM_MD_NAIVE_TARGET,
    },
    "derivation": (
        "mult(1 in A(x)B) = sum over irreducible constituents a of A of "
        "mult_A(a)*mult_B(a*) (Frobenius reciprocity). W''=m(+)2*1 has BOTH a 3 "
        "AND a 3bar AND two singlets in the SAME bundle that both domain and "
        "target tensor against -- unlike Sigma, whose two singlets are split "
        "one into EVEN_IDX, one into ODD_IDX, which are tensored with DIFFERENT "
        "'other' factors (EVEN(x)EVEN for target, ODD(x)EVEN for domain). "
        "Matching TOTAL singlet count does not imply matching invariant-sector "
        "SHAPE because shape depends on the full branching pattern relative to "
        "which factor is paired with which, not just a count."
    ),
}

# ------------------------------------------------------------------------
# 1b. Skeptic-pass-1-triggered corrections (F5, F6, F7) to the Section 1
# derivation above. The ORIGINAL text ("Sigma's two singlets are split
# asymmetrically...") is left in place, unchanged (per this project's
# Hindsight Distortion Gap Heuristic -- wrong-but-corrected reasoning stays
# on record, not silently replaced) -- this subsection SUPERSEDES it with a
# cleaner, more general, independently verified formula.
# ------------------------------------------------------------------------
print("\n=== 1b. Skeptic-triggered correction: general domain-target formula ===")

# F5: for ANY twist module W, domain-target = mult_W(3bar) - mult_W(3) EXACTLY
# (not merely "singlets contribute symmetrically when split together") --
# derivable directly from trivial_mult()'s own definition:
#   domain = mult_W(3bar) + mult_W(1),  target = mult_W(1) + mult_W(3)
#   => domain - target = mult_W(3bar) - mult_W(3)   for EVERY W, unconditionally.
F5_TEST_MODULES = {
    # NOTE (skeptic-pass-2 F-finding "H", fixed not merely disclosed): the
    # first version of this dict listed "m+2*1" and "full Sigma self-twist"
    # as two separate entries with IDENTICAL module dicts {"1":2,"3":1,
    # "3bar":1} -- true (that IS the whole point of the precheck's non-
    # redundancy analysis: same su(3)-module type, different {NAB_i}-level
    # action) but presenting it as "4 independently tested modules" for the
    # formula check below overstated the count -- 3 DISTINCT abstract module
    # types are tested, listed once each.
    "EVEN_IDX (round59's own twist bundle, dim4)": {"1": 1, "3bar": 1},
    "m (C139)": {"3": 1, "3bar": 1},
    "m+2*1 == full Sigma, as an ABSTRACT su(3)-module (this round + T1)": {
        "1": 2,
        "3": 1,
        "3bar": 1,
    },
}
f5_formula_holds = True
for name, module in F5_TEST_MODULES.items():
    d = trivial_mult(ODD_IDX_MODULE, module)
    t = trivial_mult(EVEN_IDX_MODULE, module)
    predicted_diff = module.get("3bar", 0) - module.get("3", 0)
    actual_diff = d - t
    print(
        f"  {name}: module={module}, domain={d}, target={t}, domain-target={actual_diff}, "
        f"mult(3bar)-mult(3)={predicted_diff}"
    )
    if actual_diff != predicted_diff:
        f5_formula_holds = False
check(
    "f5_general_domain_minus_target_formula_holds_for_all_test_modules",
    f5_formula_holds,
    "domain-target = mult_W(3bar)-mult_W(3) holds exactly for every tested module "
    "(round59's own EVEN_IDX, m, m+2*1, full Sigma) -- confirms this general formula, "
    "not a 'singlets split asymmetrically across EVEN/ODD' story, is what actually "
    "governs the shape",
)

# F6 (AGGREGATE bound only -- superseded by Section 10's GRADED/per-summand
# analysis, which is the version that actually matters; kept here, NOT as
# check() calls, per skeptic-pass-2 finding "G": the two check()s originally
# here compared only hardcoded module-level constants (CLAIM_MD_NAIVE_DOMAIN
# - CLAIM_MD_NAIVE_TARGET == 1, etc.), which are unfailable by construction
# and evade the AST self-audit's Constant-only detection via name binding --
# a real gap, fixed here by removing the unfailable checks entirely rather
# than defending them, matching how F13 was fixed. The AGGREGATE bound's own
# conclusion -- "the kernel difference is therefore fully real content,
# STRENGTHENS the Section 9 comparison" -- is furthermore WRONG once the
# GRADED (per-summand, not aggregate) bound is computed in Section 10: the
# graded bound is NOT trivial, and it exactly predicts the observed kernel
# difference. Do not draw conclusions from the aggregate-only reasoning
# below; it is retained only as an intermediate step superseded by Section 10.)
print(
    "  (F6 aggregate-only analysis retained as prose, not check()s -- see Section 10 "
    "for the GRADED per-summand version, which supersedes it)"
)
print(
    f"  round59's own (domain,target)=({CLAIM_MD_NAIVE_DOMAIN},{CLAIM_MD_NAIVE_TARGET}) "
    f"forces kernel>={max(0, CLAIM_MD_NAIVE_DOMAIN - CLAIM_MD_NAIVE_TARGET)} by AGGREGATE "
    "rank-nullity alone (a weaker, coarser bound than Section 10's graded one)"
)

# F7: brute-force check that (domain,target)=(2,1) requires (mult_1,mult_3,mult_3bar)
# in {(1,0,1),(0,1,2)} -- confirms no internally-graded "2-singlet" bundle can
# achieve Sigma's own restricted (2,1) shape (the speculative construction this
# round's FIRST DRAFT proposed in a since-withdrawn Section 11.4 was, per this
# check, PROVABLY incapable of the shape it was proposed to achieve).
f7_solutions = []
for m1 in range(4):
    for m3 in range(4):
        for m3b in range(4):
            wmod = {"1": m1, "3": m3, "3bar": m3b}
            if trivial_mult(ODD_IDX_MODULE, wmod) == 2 and trivial_mult(EVEN_IDX_MODULE, wmod) == 1:
                f7_solutions.append((m1, m3, m3b))
check(
    "f7_2_1_shape_requires_exactly_these_two_module_types",
    sorted(f7_solutions) == [(0, 1, 2), (1, 0, 1)],
    f"(mult_1,mult_3,mult_3bar) solutions for (domain,target)=(2,1), searched over "
    f"{{0,1,2,3}}^3: {sorted(f7_solutions)} -- (1,0,1) is EVEN_IDX itself; (0,1,2) is "
    "a DIFFERENT, not-yet-tried module type. NEITHER has 2 singlets split across an "
    "internal even/odd grading -- any 2-singlet proposal (mult_1=2) provably CANNOT "
    "achieve (2,1), since both solutions have mult_1<=1",
)
DATA["skeptic_pass_1_corrections"] = {
    "f5_general_formula": "domain - target = mult_W(3bar) - mult_W(3), verified for all tested modules",
    "f6_round59_kernel_bound": {
        "domain_minus_target": CLAIM_MD_NAIVE_DOMAIN - CLAIM_MD_NAIVE_TARGET,
        "forced_kernel_floor": max(0, CLAIM_MD_NAIVE_DOMAIN - CLAIM_MD_NAIVE_TARGET),
    },
    "f7_2_1_shape_solutions": sorted(f7_solutions),
}

# ========================================================================
# 2. Build W'' = m (+) 2*1 connection -- REUSE precheck's own construction
#    object directly (not a re-typed formula), per claim.md's explicit
#    instruction to use "that exact, already-cleared construction."
# ========================================================================
print("\n=== 2. Twist bundle W'' = m(+)2*1 connection (reused from precheck, unmodified) ===")

conn_w2_np: dict[int, np.ndarray] = PRECHECK.conn_m_plus_2singlets  # 8x8, i=1..6, reused object
check(
    "conn_w2_is_the_precheck_own_object_dim8",
    all(conn_w2_np[i].shape == (8, 8) for i in range(1, 7)),
    "conn_w2_np is literally PRECHECK.conn_m_plus_2singlets, not re-typed",
)
# Independent sanity re-check (not merely trusting the import): extra 2
# singlets have ZERO self-connection (full 2x2 block [6:8,6:8], not just the
# off-diagonal coupling to m) -- re-verified here, fresh, on the reused object.
check(
    "conn_w2_extra_singlets_fully_decoupled_full_2x2_block_zero",
    all(
        np.abs(conn_w2_np[i][6:8, 6:8]).max() < 1e-12
        and np.abs(conn_w2_np[i][:6, 6:8]).max() < 1e-12
        and np.abs(conn_w2_np[i][6:8, :6]).max() < 1e-12
        for i in range(1, 7)
    ),
    "re-verified fresh in THIS round's own script, not merely cited from precheck's own assert",
)
check(
    "conn_w2_top_left_6x6_matches_c139_rho_vector_m_exactly",
    all(
        np.max(np.abs(conn_w2_np[i][:6, :6] - C139.rho_vector(R59.NOMIZU[i]))) < 1e-12
        for i in range(1, 7)
    ),
    "confirms the reused connection's m-block is C139's own rho_vector(NOMIZU[i]), "
    "unmodified -- re-derived fresh here, not merely cited",
)

# ADNU (su(3)-generator) action on W'' -- NOT present in precheck (which only
# built the NOMIZU-based Dirac connection), built fresh here: rho_vector on
# the m-block, exact ZERO on the two extra (trivial-by-construction) singlets.
rho_w2_adnu_np: dict[int, np.ndarray] = {}
for a in range(1, 9):
    full8 = np.zeros((8, 8), dtype=complex)
    full8[:6, :6] = C139.rho_vector(R59.ADNU[a])
    rho_w2_adnu_np[a] = full8

check(
    "w2_adnu_action_is_real_antisymmetric_all_a",
    all(
        np.max(np.abs(rho_w2_adnu_np[a].imag)) < TOL
        and np.max(np.abs(rho_w2_adnu_np[a] + rho_w2_adnu_np[a].T)) < TOL
        for a in range(1, 9)
    ),
)

# Module-type check: W'' should decompose as 3(+)3bar(+)1(+)1 under su(3) --
# commutant dimension should be 1^2+1^2+2^2=6 (three PAIRWISE-INEQUIVALENT
# constituents 3,3bar,1, the LAST with multiplicity 2), NOT 4 (which would be
# the naive "4 orthogonal pieces, each irreducible with multiplicity 1" guess).
w2_adnu_gens = [rho_w2_adnu_np[a] for a in range(1, 9)]
comm_w2 = C139.commutant_nullspace(w2_adnu_gens, 8)
check(
    "w2_commutant_dim_6_matches_3_plus_3bar_plus_1mult2",
    comm_w2.shape[1] == 6,
    f"dim(commutant)={comm_w2.shape[1]} (expect 6 = 1^2+1^2+2^2, confirming module "
    "type 3+3bar+1(mult 2), NOT a naive 4-orthogonal-pieces guess)",
)
w2_singlet_stacked = np.vstack([rho_w2_adnu_np[a] for a in range(1, 9)])
w2_singlet_basis = C139.nullspace_basis(w2_singlet_stacked)
check(
    "w2_has_exactly_2_su3_singlets",
    w2_singlet_basis.shape[1] == 2,
    f"dim common nullspace of ADNU-action on C^8 = {w2_singlet_basis.shape[1]} (expect 2, "
    "matching Sigma's own singlet count exactly -- this IS matched, only the SHAPE "
    "downstream (Sec 4) is not)",
)
DATA["w2_module_type_check"] = {
    "commutant_dim": int(comm_w2.shape[1]),
    "n_singlets": int(w2_singlet_basis.shape[1]),
}

# ========================================================================
# 3. Re-verification (not mere citation) of the precheck's equivalence
#    result -- per claim.md's explicit instruction and this round's own
#    house rule #6: re-run an equivalent intertwiner-nullspace check here,
#    inside THIS round's own script, using freshly-loaded data.
# ========================================================================
print("\n=== 3. Re-verification of precheck's equivalence-to-Sigma result (fresh, in-round) ===")

gens_a_sigma6 = [C139.NAB_np[i] for i in range(1, 7)]
gens_b_w2 = [conn_w2_np[i] for i in range(1, 7)]
t_intertwiner_w2 = C139.intertwiner_nullspace(gens_a_sigma6, 8, gens_b_w2, 8)
check(
    "no_equivariant_map_sigma_to_w2_reverified_fresh_in_c141",
    t_intertwiner_w2.shape[1] == 0,
    f"dim(intertwiner space)={t_intertwiner_w2.shape[1]} (expect 0 -- re-derived HERE, "
    f"fresh, matching precheck's own null_dim={PRECHECK.null_dim}, NOT merely importing "
    "that number)",
)
check(
    "c141_reverification_matches_precheck_own_null_dim",
    t_intertwiner_w2.shape[1] == PRECHECK.null_dim,
    f"c141 fresh={t_intertwiner_w2.shape[1]}, precheck={PRECHECK.null_dim}",
)
DATA["equivalence_reverification"] = {
    "intertwiner_nullspace_dim_sigma_to_w2": int(t_intertwiner_w2.shape[1]),
    "precheck_own_null_dim": int(PRECHECK.null_dim),
}

# ========================================================================
# 4. su(3)-invariant sector dimensions -- verify the pre-registered (Sec 1)
#    prediction against numeric SVD nullspace.
# ========================================================================
print("\n=== 4. su(3)-invariant sector dimensions (domain, target) -- verify Sec 1 prediction ===")

i8 = np.eye(8, dtype=complex)
gens_leibniz_64 = [
    np.kron(C139.su3_ops_np[a], i8) + np.kron(i8, rho_w2_adnu_np[a]) for a in range(1, 9)
]

domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(8)), 8)
target_block = C139.block_global_gen(R59.EVEN_IDX, list(range(8)), 8)

domain_inv = C139.invariant_basis_gen(gens_leibniz_64, domain_block, 64)
target_inv = C139.invariant_basis_gen(gens_leibniz_64, target_block, 64)

check(
    "domain_inv_matches_this_rounds_own_hand_prediction_3",
    domain_inv.shape[1] == PREREGISTERED_DOMAIN_INV,
    f"dim(ODD_IDX(x)W'')_su3-inv = {domain_inv.shape[1]} (this round's own hand-CG "
    f"prediction: {PREREGISTERED_DOMAIN_INV})",
)
check(
    "target_inv_matches_this_rounds_own_hand_prediction_3",
    target_inv.shape[1] == PREREGISTERED_TARGET_INV,
    f"dim(EVEN_IDX(x)W'')_su3-inv = {target_inv.shape[1]} (this round's own hand-CG "
    f"prediction: {PREREGISTERED_TARGET_INV})",
)
# The genuinely important, failable comparison against claim.md's OWN stated
# expectation -- both outcomes are legitimate and reported honestly either way.
shape_matches_claim_md_naive_21 = (
    domain_inv.shape[1] == CLAIM_MD_NAIVE_DOMAIN and target_inv.shape[1] == CLAIM_MD_NAIVE_TARGET
)
check(
    "shape_matches_claim_md_naive_2_1_expectation",
    shape_matches_claim_md_naive_21,
    f"computed ({domain_inv.shape[1]},{target_inv.shape[1]}) vs claim.md's naive "
    f"({CLAIM_MD_NAIVE_DOMAIN},{CLAIM_MD_NAIVE_TARGET}) -- per claim.md's own kill "
    "criterion (b), a FAIL here means: report the actual shape and why the naive "
    "prediction failed, BEFORE interpreting any kernel value (done in decision.md)",
)
DATA["invariant_sector_dims"] = {
    "domain_ODD_x_W2": int(domain_inv.shape[1]),
    "target_EVEN_x_W2": int(target_inv.shape[1]),
    "preregistered_hand_cg_prediction": [PREREGISTERED_DOMAIN_INV, PREREGISTERED_TARGET_INV],
    "claim_md_naive_expectation": [CLAIM_MD_NAIVE_DOMAIN, CLAIM_MD_NAIVE_TARGET],
    "shape_matches_claim_md_naive": bool(shape_matches_claim_md_naive_21),
    "round59_comparison": {"domain": 2, "target": 1},
}

# ========================================================================
# 5. Main computation: D'' restricted to the (actual, computed) invariant
#    domain/target sectors.
# ========================================================================
print("\n=== 5. Main computation: twisted Dirac certificate for W''=m(+)2*1 ===")

d_dprime2 = C139.build_twisted_dirac_np(C139.E_np, C139.NAB_np, 8, conn_w2_np)
check(
    "d_dprime2_is_hermitian",
    bool(np.max(np.abs(d_dprime2 - d_dprime2.conj().T)) < 1e-8),
    f"max|D''-D''^dagger| = {float(np.max(np.abs(d_dprime2 - d_dprime2.conj().T))):.3e}",
)

block2 = target_inv.conj().T @ d_dprime2 @ domain_inv  # target_dim x domain_dim
sv2 = np.linalg.svd(block2, compute_uv=False)
rank2 = int(np.sum(sv2 > 1e-8))
domain_dim2 = int(domain_inv.shape[1])
target_dim2 = int(target_inv.shape[1])
kernel_dim2 = domain_dim2 - rank2

print(f"  block shape = {block2.shape}, singular values = {sv2}")
print(f"  rank = {rank2}, forward kernel_dim (domain side) = {kernel_dim2}")

check(
    "block2_singular_values_numerically_unambiguous",
    bool(np.all((sv2 < 1e-9) | (sv2 > 1e-4))),
    f"singular values = {sv2} (each must sit clearly on one side of the noise floor)",
)

backward2 = domain_inv.conj().T @ d_dprime2 @ target_inv
check(
    "forward_is_hermitian_adjoint_of_backward_w2",
    bool(np.max(np.abs(block2 - backward2.conj().T)) < 1e-8),
    f"max|diff| = {float(np.max(np.abs(block2 - backward2.conj().T))):.3e}",
)
sv2_back = np.linalg.svd(backward2, compute_uv=False)
rank2_back = int(np.sum(sv2_back > 1e-8))
kernel2_back = target_dim2 - rank2_back

DATA["main_result"] = {
    "block_shape": list(block2.shape),
    "singular_values": [float(s) for s in sv2],
    "domain_dim": domain_dim2,
    "target_dim": target_dim2,
    "forward_rank": rank2,
    "forward_kernel_dim": kernel_dim2,
    "backward_rank": rank2_back,
    "backward_kernel_dim": kernel2_back,
    "matches_round59_pattern_kernel_eq_1": bool(kernel_dim2 == 1),
}

# ========================================================================
# 5b. Term1/Term2 mechanistic decomposition -- informational (mirrors C139
# Sec 8), NOT the load-bearing shape/kernel finding. Since W'' HAS 2
# singlets (unlike C139's zero-singlet m), C139 Sec 8b's Schur-forcing
# argument for Term1=0 does NOT apply here (explicitly noted in claim.md) --
# recorded as data, not assumed to vanish.
# ========================================================================
print("\n=== 5b. Term1/Term2 decomposition (informational, mechanism not forced here) ===")

d_term1_only = np.zeros((64, 64), dtype=complex)
d_term2_only = np.zeros((64, 64), dtype=complex)
for i in range(1, 7):
    d_term1_only += np.kron(C139.E_np[i] @ C139.NAB_np[i], i8)
    d_term2_only += np.kron(C139.E_np[i], conn_w2_np[i])
block_term1 = target_inv.conj().T @ d_term1_only @ domain_inv
block_term2 = target_inv.conj().T @ d_term2_only @ domain_inv
check(
    "term1_plus_term2_equals_full_block_w2",
    bool(np.max(np.abs((block_term1 + block_term2) - block2)) < 1e-8),
    f"max|term1+term2-block| = {float(np.max(np.abs((block_term1 + block_term2) - block2))):.3e}",
)
term1_frob = float(np.max(np.abs(block_term1)))
DATA["term_decomposition"] = {
    "term1_max_abs_entry": term1_frob,
    "term1_is_zero_matrix": bool(term1_frob < 1e-8),
    "note": (
        "unlike C139's W'=m (zero singlets, Term1=0 FORCED by Schur's lemma per "
        "C139 Sec 8b), W''=m+2*1 HAS two singlets -- the forcing argument's own "
        "premise (domain singlet must draw entirely from ODD's 3-piece because "
        "EVEN has no 3-constituent) does not directly apply in the same form "
        "once EVEN_IDX(x)W'' contains MULTIPLE trivial channels (Sec 4: dim 3, "
        "not 1) -- Term1's vanishing or non-vanishing here is recorded as an "
        "honest computed fact, not assumed either way."
    ),
}

# ========================================================================
# 6. EXACT (sympy) cross-check of domain/target dims AND the block matrix's
#    rank/kernel -- same evidence tier C139/round59 used.
# ========================================================================
print("\n=== 6. Exact sympy cross-check ===")

conn_w2_sym: dict[int, sp.Matrix] = {}
rho_w2_adnu_sym: dict[int, sp.Matrix] = {}
for i in range(1, 7):
    m6 = C139.rho_vector_sympy(R59.NOMIZU[i])
    full8 = sp.zeros(8, 8)
    full8[:6, :6] = m6
    conn_w2_sym[i] = full8
for a in range(1, 9):
    m6a = C139.rho_vector_sympy(R59.ADNU[a])
    full8a = sp.zeros(8, 8)
    full8a[:6, :6] = m6a
    rho_w2_adnu_sym[a] = full8a

gens_leibniz_64_sym = [
    R59.kron(C139.su3_ops_sym[a], sp.eye(8)) + R59.kron(sp.eye(8), rho_w2_adnu_sym[a])
    for a in range(1, 9)
]
domain_inv_sym = C139.common_nullspace_in_block_sym(gens_leibniz_64_sym, domain_block, 64)
target_inv_sym = C139.common_nullspace_in_block_sym(gens_leibniz_64_sym, target_block, 64)

check(
    "exact_domain_inv_dim_matches_numeric_w2",
    len(domain_inv_sym) == domain_inv.shape[1],
    f"exact={len(domain_inv_sym)}, numeric={domain_inv.shape[1]}",
)
check(
    "exact_target_inv_dim_matches_numeric_w2",
    len(target_inv_sym) == target_inv.shape[1],
    f"exact={len(target_inv_sym)}, numeric={target_inv.shape[1]}",
)

d_dprime2_sym = C139.build_twisted_dirac_sympy(C139.E_sym, C139.NAB_sym, 8, conn_w2_sym)
domain_on_sym = R59.gram_schmidt(domain_inv_sym)
target_on_sym = R59.gram_schmidt(target_inv_sym)

block2_exact = sp.zeros(len(target_on_sym), len(domain_on_sym))
for ti, w in enumerate(target_on_sym):
    for di, u in enumerate(domain_on_sym):
        block2_exact[ti, di] = sp.simplify(R59.hip(w, d_dprime2_sym * u))

rank2_exact = block2_exact.rank()
kernel2_exact = len(domain_on_sym) - rank2_exact
print(f"  exact block matrix rank = {rank2_exact}, exact kernel_dim = {kernel2_exact}")

check(
    "exact_kernel_dim_matches_numeric_kernel_dim",
    kernel2_exact == kernel_dim2,
    f"exact kernel_dim={kernel2_exact}, numeric kernel_dim={kernel_dim2}",
)
# NOTE (skeptic-pass-1 F13 fix): the prior version of this check used a
# `True if <shape==0> else bool(...)` guard for the degenerate empty-matrix
# case. That guard is dead code here (block2_exact is always 3x3, never
# 0-sized, given domain_dim2=target_dim2=3 established in Section 4) --
# removed rather than disguised, so the check has exactly one live branch
# and the AST self-audit's "no literal constant" guarantee is not silently
# narrower than it looks.
check(
    "block2_exact_is_nonempty_before_eigenvalue_check",
    block2_exact.shape[0] > 0 and block2_exact.shape[1] > 0,
    f"block2_exact shape = {block2_exact.shape} (must be nonempty for the next check to be meaningful)",
)
check(
    "exact_singular_values_of_block_numerically_unambiguous",
    bool(
        all(
            abs(complex(v)) < 1e-9 or abs(complex(v)) > 1e-4
            for v in (block2_exact.conjugate().T * block2_exact).eigenvals()
        )
    ),
    "eigenvalues of block^dagger @ block (exact) sit clearly away from the noise floor",
)

DATA["exact_crosscheck"] = {
    "domain_inv_dim_exact": len(domain_inv_sym),
    "target_inv_dim_exact": len(target_inv_sym),
    "block_exact": [
        [str(sp.nsimplify(sp.radsimp(v))) for v in row] for row in block2_exact.tolist()
    ],
    "rank_exact": int(rank2_exact),
    "kernel_dim_exact": int(kernel2_exact),
}

# ========================================================================
# 6b. EXACT mechanistic explanation of the block structure -- block2_exact's
#    entries (see printed matrix above) show exactly ONE nonzero entry per
#    row and per column (a permutation pattern) -- suggesting the 3-dim
#    invariant sector DECOMPOSES into 3 mutually orthogonal 1-dim channels,
#    each carrying EITHER Term1 alone OR Term2 alone, not a genuine mix.
#    Verified here exactly (not merely observed from the printed matrix),
#    against independently-derivable reference values: Term1's nonzero
#    entries should equal the SAME "Killing eigenvalue" round59/C139
#    independently established (the coefficient of A's action on ODD_IDX's
#    singlet), and Term2's single nonzero entry should equal C139's OWN
#    c_exact EXACTLY (since Term2 is zero on the two extra, unconnected
#    singlets, so the only surviving Term2 channel is literally C139's own
#    isolated m-twist computation, embedded unchanged inside this bigger
#    invariant sector).
# ========================================================================
print("\n=== 6b. Exact mechanistic decomposition of the 3x3 block (Term1 vs Term2) ===")

d_term1_only_sym = sp.zeros(64, 64)
d_term2_only_sym = sp.zeros(64, 64)
i8_sym = sp.eye(8)
for i in range(1, 7):
    d_term1_only_sym += R59.kron(C139.E_sym[i] * C139.NAB_sym[i], i8_sym)
    d_term2_only_sym += R59.kron(C139.E_sym[i], conn_w2_sym[i])

block_term1_exact = sp.zeros(len(target_on_sym), len(domain_on_sym))
block_term2_exact = sp.zeros(len(target_on_sym), len(domain_on_sym))
for ti, w in enumerate(target_on_sym):
    for di, u in enumerate(domain_on_sym):
        block_term1_exact[ti, di] = sp.simplify(R59.hip(w, d_term1_only_sym * u))
        block_term2_exact[ti, di] = sp.simplify(R59.hip(w, d_term2_only_sym * u))

check(
    "exact_term1_plus_term2_equals_exact_block",
    bool(sp.simplify(block_term1_exact + block_term2_exact - block2_exact) == sp.zeros(3, 3)),
    "block_term1_exact + block_term2_exact == block2_exact, entrywise, exactly",
)

term1_nonzero_vals = sorted(
    {sp.nsimplify(sp.radsimp(v)) for v in block_term1_exact if sp.simplify(v) != 0},
    key=str,
)
term2_nonzero_vals = sorted(
    {sp.nsimplify(sp.radsimp(v)) for v in block_term2_exact if sp.simplify(v) != 0},
    key=str,
)
n_term1_nonzero = sum(1 for v in block_term1_exact if sp.simplify(v) != 0)
n_term2_nonzero = sum(1 for v in block_term2_exact if sp.simplify(v) != 0)

check(
    "term1_exact_has_exactly_2_nonzero_entries",
    n_term1_nonzero == 2,
    f"Term1_exact has {n_term1_nonzero} nonzero entries out of 9 -- consistent with "
    "'A kills ODD's 3-piece entirely, and only connects ODD's singlet to EVEN's "
    "singlet, once per extra W'' singlet' (2 extra singlets -> 2 nonzero entries)",
)
check(
    "term2_exact_has_exactly_1_nonzero_entry",
    n_term2_nonzero == 1,
    f"Term2_exact has {n_term2_nonzero} nonzero entries out of 9 -- consistent with "
    "'Term2 is zero on the 2 decoupled extra singlets, so only the single m-embedded "
    "channel (ODD's 3 (x) W'''s 3bar-piece of m) survives'",
)
check(
    "term1_nonzero_entries_are_a_single_common_value",
    len(term1_nonzero_vals) == 1,
    f"distinct Term1 nonzero values = {[str(v) for v in term1_nonzero_vals]} -- both "
    "channels should carry the SAME Killing-eigenvalue-type coefficient",
)
check(
    "term2_single_nonzero_entry_matches_c139_own_c_exact",
    bool(term2_nonzero_vals) and sp.simplify(term2_nonzero_vals[0] - C139.c_exact) == 0,
    f"Term2_exact's sole nonzero entry = {term2_nonzero_vals[0] if term2_nonzero_vals else None}, "
    f"C139's own c_exact = {C139.c_exact} -- EXACT match confirms this channel is literally "
    "C139's own isolated m-twist result, embedded unchanged",
)
DATA["exact_mechanistic_decomposition"] = {
    "term1_exact": [
        [str(sp.nsimplify(sp.radsimp(v))) for v in row] for row in block_term1_exact.tolist()
    ],
    "term2_exact": [
        [str(sp.nsimplify(sp.radsimp(v))) for v in row] for row in block_term2_exact.tolist()
    ],
    "term1_n_nonzero": n_term1_nonzero,
    "term2_n_nonzero": n_term2_nonzero,
    "term1_nonzero_values": [str(v) for v in term1_nonzero_vals],
    "term2_nonzero_values": [str(v) for v in term2_nonzero_vals],
    "term2_matches_c139_c_exact": bool(
        term2_nonzero_vals and sp.simplify(term2_nonzero_vals[0] - C139.c_exact) == 0
    ),
    "interpretation": (
        "The 3x3 block is, up to a basis permutation, EXACTLY DIAGONAL: 2 channels "
        "carry ONLY Term1 (the Killing-eigenvalue mechanism, identical in both, "
        "reflecting the 2 extra decoupled singlets each independently reproducing "
        "round59's OWN untwisted mechanism), and 1 channel carries ONLY Term2 "
        "(C139's own m-twist Term2 result, embedded unchanged). kernel=0 here is "
        "the DIRECT SUM of two ALREADY-ESTABLISHED nonvanishing facts (round59's "
        "own Killing eigenvalue, appearing twice, and C139's own Term2 finding, "
        "appearing once) -- not a new, independent nonvanishing mechanism this "
        "round discovered on its own terms."
    ),
}
print(
    f"  Term1_exact nonzero entries (n={n_term1_nonzero}): {[str(v) for v in term1_nonzero_vals]}"
)
print(
    f"  Term2_exact nonzero entries (n={n_term2_nonzero}): {[str(v) for v in term2_nonzero_vals]}"
)
print(f"  C139's own c_exact for comparison: {C139.c_exact}")

# ------------------------------------------------------------------------
# 6c. BASIS-INDEPENDENT restatement (skeptic-pass-1 F10/F11 response): the
# "exactly one nonzero entry per row/column" pattern above is a fact about
# the SPECIFIC orthonormal basis common_nullspace_in_block_sym/gram_schmidt
# happen to return -- a different (e.g. rotated) choice of orthonormal
# basis for the 3-dim domain_inv/target_inv would generally NOT preserve
# that sparse pattern. What IS basis-independent is each term's RANK and
# SINGULAR VALUE SPECTRUM (invariant under U(n) changes of basis on each
# side separately). Verified here directly, not merely inferred from the
# sparse pattern.
# ------------------------------------------------------------------------
print("\n=== 6c. Basis-independent restatement: rank + singular values of Term1, Term2 ===")

sv_term1 = np.linalg.svd(block_term1, compute_uv=False)
sv_term2 = np.linalg.svd(block_term2, compute_uv=False)
rank_term1 = int(np.sum(sv_term1 > 1e-8))
rank_term2 = int(np.sum(sv_term2 > 1e-8))
print(f"  Term1 (numeric) singular values = {sv_term1}, rank = {rank_term1}")
print(f"  Term2 (numeric) singular values = {sv_term2}, rank = {rank_term2}")

check(
    "term1_rank_is_exactly_2_basis_independent",
    rank_term1 == 2,
    f"Term1 rank = {rank_term1} (basis-independent -- Term1 is Sigma-only, identity on "
    "the twist factor, so its rank cannot exceed the number of extra decoupled singlets)",
)
check(
    "term1_nonzero_singular_values_both_equal_sqrt3",
    bool(np.allclose(np.sort(sv_term1[:rank_term1]), [np.sqrt(3), np.sqrt(3)], atol=1e-6)),
    f"Term1's {rank_term1} nonzero singular values = {sv_term1[:rank_term1]} "
    "(expect both exactly sqrt(3), the Killing eigenvalue's magnitude, basis-independent)",
)
check(
    "term2_rank_is_exactly_1_basis_independent",
    rank_term2 == 1,
    f"Term2 rank = {rank_term2} (basis-independent -- Term2 is zero on both decoupled "
    "extra singlets, so its image cannot exceed the 1-dimensional m-embedded channel)",
)
check(
    "term2_sole_nonzero_singular_value_equals_c139_abs_c_exact",
    bool(np.isclose(sv_term2[0], abs(complex(C139.c_exact)), atol=1e-6)),
    f"Term2's sole nonzero singular value = {sv_term2[0]:.10f}, |C139.c_exact| = "
    f"{abs(complex(C139.c_exact)):.10f} -- basis-independent match (rank + singular value, "
    "not a specific matrix entry's phase-dependent value), addressing the concern that "
    "an entrywise comparison could be a gauge-phase artifact",
)
DATA["basis_independent_term_decomposition"] = {
    "term1_singular_values": [float(s) for s in sv_term1],
    "term1_rank": rank_term1,
    "term2_singular_values": [float(s) for s in sv_term2],
    "term2_rank": rank_term2,
    "note": (
        "Rank and singular-value spectrum are invariant under any U(n) change of "
        "orthonormal basis on domain_inv/target_inv separately -- unlike the specific "
        "matrix entries reported in Section 6b, which depend on the particular basis "
        "sympy's nullspace()/gram_schmidt returned. Term1 has rank 2 (both nonzero "
        "singular values exactly sqrt(3)); Term2 has rank 1 (its sole nonzero singular "
        "value exactly |C139's c_exact|). These are the basis-independent, load-bearing "
        "facts; Section 6b's exact entries are a stronger, but basis-DEPENDENT, "
        "supporting observation."
    ),
}

# ========================================================================
# 7. Deformation/linearity check -- same algebraic argument as C139's own
#    (build_twisted_dirac_np is linear in both nab_np and conn_w_np).
# ========================================================================
print("\n=== 7. Deformation/linearity check ===")

deform_sweep: dict[str, dict] = {}
for t_val in [0.5, 2.0]:
    nomizu_t = {i: [(t_val * cf, aa, bb) for (cf, aa, bb) in R59.NOMIZU[i]] for i in R59.NOMIZU}
    nab_t_sym = {i: R59.spin_lift(nomizu_t[i], C139.E_sym) for i in range(1, 7)}
    nab_t_np = {i: np.array(nab_t_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    conn_w2_t_np = {}
    for i in range(1, 7):
        m6_t = C139.rho_vector(nomizu_t[i])
        full8_t = np.zeros((8, 8), dtype=complex)
        full8_t[:6, :6] = m6_t
        conn_w2_t_np[i] = full8_t
    d_t = C139.build_twisted_dirac_np(C139.E_np, nab_t_np, 8, conn_w2_t_np)
    block_t = target_inv.conj().T @ d_t @ domain_inv
    predicted = t_val * block2
    resid = float(np.max(np.abs(block_t - predicted)))
    deform_sweep[str(t_val)] = {"max_abs_residual": resid}
    check(
        f"d_dprime2_linear_in_nomizu_scale_t={t_val}",
        resid < 1e-6,
        f"max|block(t={t_val}) - t*block(1)| = {resid:.3e}",
    )
DATA["deformation_sweep"] = deform_sweep

# ========================================================================
# 8. Angular sweep across C73b's own 2-dim admissible su(3)-equivariant
#    torsion family -- is kernel_dim(theta) constant across the whole
#    admissible family (robust, "topologically protected" as C139/C73b
#    found for their own results), or does it vary?
# ========================================================================
print("\n=== 8. Angular sweep across the 2-dim admissible torsion family ===")

m_gens_for_sweep = C73B.m_generators()
torsion_basis = C73B.equivariant_torsion_basis(m_gens_for_sweep)
check(
    "torsion_family_is_2dim_matches_c73b_w2",
    torsion_basis.shape[1] == 2,
    f"dim Hom_su3(m,Lambda^2 m) = {torsion_basis.shape[1]} (C73b certified: 2)",
)
t1_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 0])
t2_dict = C73B.vec_to_nomizu_dict(torsion_basis[:, 1])

angle_sweep: dict[str, dict] = {}
kernel_dims_seen = set()
rank_dims_seen = set()
for theta_deg in [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270]:
    theta = np.deg2rad(theta_deg)
    combo_dict = {k: np.cos(theta) * t1_dict[k] + np.sin(theta) * t2_dict[k] for k in range(1, 7)}
    nomizu_theta = C73B.matdict_to_nomizu(combo_dict)
    nab_theta_sym = {i: R59.spin_lift(nomizu_theta[i], C139.E_sym) for i in range(1, 7)}
    nab_theta_np = {i: np.array(nab_theta_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    conn_w2_theta_np = {}
    for i in range(1, 7):
        m6_theta = C139.rho_vector(nomizu_theta[i])
        full8_theta = np.zeros((8, 8), dtype=complex)
        full8_theta[:6, :6] = m6_theta
        conn_w2_theta_np[i] = full8_theta

    d_theta = C139.build_twisted_dirac_np(C139.E_np, nab_theta_np, 8, conn_w2_theta_np)
    block_theta = target_inv.conj().T @ d_theta @ domain_inv
    sv_theta = np.linalg.svd(block_theta, compute_uv=False)
    rank_theta = int(np.sum(sv_theta > 1e-8))
    kernel_theta = domain_dim2 - rank_theta

    angle_sweep[str(theta_deg)] = {
        "singular_values": [float(s) for s in sv_theta],
        "rank": rank_theta,
        "kernel_dim": kernel_theta,
    }
    kernel_dims_seen.add(kernel_theta)
    rank_dims_seen.add(rank_theta)

DATA["angular_sweep_torsion_family"] = angle_sweep
DATA["angular_sweep_summary"] = {
    "kernel_dims_seen_across_sweep": sorted(kernel_dims_seen),
    "rank_dims_seen_across_sweep": sorted(rank_dims_seen),
    "kernel_dim_constant_across_family": len(kernel_dims_seen) == 1,
}
print(f"  kernel_dim(theta) values seen across 13 angles: {sorted(kernel_dims_seen)}")
print(f"  rank(theta) values seen across 13 angles: {sorted(rank_dims_seen)}")

check(
    "kernel_dim_constant_across_whole_admissible_family",
    len(kernel_dims_seen) == 1,
    f"kernel_dim(theta) in {sorted(kernel_dims_seen)} across all 13 swept angles "
    "-- constant means the result (whatever it is) is 'topologically protected' "
    "across the whole admissible connection family, matching the discipline "
    "C73b/C139 established for their own certificates; non-constant is reported "
    "honestly, not hidden",
)
check(
    "at_nomizu_own_point_theta0_kernel_matches_main_computation",
    angle_sweep["0"]["kernel_dim"] == kernel_dim2,
    f"sweep theta=0 kernel={angle_sweep['0']['kernel_dim']}, main computation kernel={kernel_dim2} "
    "-- sanity check that the sweep's own theta=0 point reproduces Section 5's main result "
    "(NOMIZU is theta=0 in this basis by construction, per C73b's own convention)",
)

# ========================================================================
# 9. SKEPTIC-PASS-1-TRIGGERED: the genuine apples-to-apples comparison.
#
# Skeptic pass 1 (context-blind, run on the first draft of this round)
# identified a critical flaw: comparing C141's W''=m(+)2*1 (computed with
# an UNRESTRICTED, full-8-dim second factor -- domain/target span the WHOLE
# twist bundle) against round59's OWN certified (2,1) (computed with the
# second factor RESTRICTED to EVEN_IDX specifically, dim 4 of Sigma's own
# 8) is not apples-to-apples: the two use DIFFERENT conventions for how
# much of the second factor enters the domain/target blocks.
#
# The methodologically CONSISTENT comparison applies the SAME "unrestricted
# full second factor" convention this round already uses for W''=m(+)2*1
# to Sigma's OWN self-twist (W'=Sigma, i.e. round59's own twist bundle,
# WITHOUT restricting to EVEN_IDX). C139's own decision.md Section 3d
# already recorded, as a byproduct of an unrelated bug-hunt, that this
# configuration gives shape (3,3) -- but never computed or reported its
# KERNEL. That computation is done here, for the first time, in direct
# response to the skeptic.
#
# T0 = positive control: reproduce round59's OWN certified (2,1)/kernel=1
#      EXACTLY, using the EVEN_IDX-restricted second factor (sanity check
#      on this section's own methodology before trusting T1).
# T1 = the genuine apples-to-apples comparison: Sigma self-twisted, with
#      the SAME unrestricted-second-factor convention this round uses for
#      W''=m(+)2*1. Expect shape (3,3), matching C141's own W'' shape
#      EXACTLY -- this is the correct reference point, not round59's own
#      restricted (2,1).
# ========================================================================
print("\n=== 9. T0/T1: the genuine apples-to-apples comparison (skeptic-1-triggered) ===")

gens64_selftwist = [
    np.kron(C139.su3_ops_np[a], i8) + np.kron(i8, C139.su3_ops_np[a]) for a in range(1, 9)
]
d_selftwist = C139.build_twisted_dirac_np(C139.E_np, C139.NAB_np, 8, C139.NAB_np)

# --- T0: positive control, EVEN_IDX-restricted (round59's OWN definition) ---
domain_block_t0 = C139.block_global_gen(R59.ODD_IDX, R59.EVEN_IDX, 8)
target_block_t0 = C139.block_global_gen(R59.EVEN_IDX, R59.EVEN_IDX, 8)
domain_inv_t0 = C139.invariant_basis_gen(gens64_selftwist, domain_block_t0, 64)
target_inv_t0 = C139.invariant_basis_gen(gens64_selftwist, target_block_t0, 64)
block_t0 = target_inv_t0.conj().T @ d_selftwist @ domain_inv_t0
sv_t0 = np.linalg.svd(block_t0, compute_uv=False)
rank_t0 = int(np.sum(sv_t0 > 1e-8))
kernel_t0 = int(domain_inv_t0.shape[1]) - rank_t0

check(
    "t0_positive_control_reproduces_round59_shape_2_1",
    domain_inv_t0.shape[1] == 2 and target_inv_t0.shape[1] == 1,
    f"T0 (EVEN_IDX-restricted self-twist) domain={domain_inv_t0.shape[1]}, "
    f"target={target_inv_t0.shape[1]} (round59 certified: 2, 1)",
)
check(
    "t0_positive_control_reproduces_round59_kernel_1",
    kernel_t0 == 1,
    f"T0 kernel = {kernel_t0} (round59 certified: 1) -- confirms this section's own "
    "methodology before trusting T1's result",
)

# --- T1: the apples-to-apples comparison, unrestricted second factor ---
domain_block_t1 = C139.block_global_gen(R59.ODD_IDX, list(range(8)), 8)
target_block_t1 = C139.block_global_gen(R59.EVEN_IDX, list(range(8)), 8)
domain_inv_t1 = C139.invariant_basis_gen(gens64_selftwist, domain_block_t1, 64)
target_inv_t1 = C139.invariant_basis_gen(gens64_selftwist, target_block_t1, 64)

check(
    "t1_shape_matches_c141_own_w2_shape_3_3",
    domain_inv_t1.shape[1] == domain_dim2 and target_inv_t1.shape[1] == target_dim2,
    f"T1 (Sigma self-twist, UNRESTRICTED 2nd factor) domain={domain_inv_t1.shape[1]}, "
    f"target={target_inv_t1.shape[1]} vs C141's own W''=m+2*1: domain={domain_dim2}, "
    f"target={target_dim2} -- MATCH confirms T1 is the genuine, shape-consistent "
    "reference point, not round59's own EVEN_IDX-restricted (2,1)",
)

block_t1 = target_inv_t1.conj().T @ d_selftwist @ domain_inv_t1
sv_t1 = np.linalg.svd(block_t1, compute_uv=False)
rank_t1 = int(np.sum(sv_t1 > 1e-8))
kernel_t1 = int(domain_inv_t1.shape[1]) - rank_t1
print(f"  T1 singular values = {sv_t1}")
print(f"  T1 rank = {rank_t1}, T1 kernel_dim = {kernel_t1}")

check(
    "t1_singular_values_numerically_unambiguous",
    bool(np.all((sv_t1 < 1e-9) | (sv_t1 > 1e-4))),
    f"T1 singular values = {sv_t1}",
)

# Exact sympy cross-check of T1
gens64_selftwist_sym = [
    R59.kron(C139.su3_ops_sym[a], sp.eye(8)) + R59.kron(sp.eye(8), C139.su3_ops_sym[a])
    for a in range(1, 9)
]
domain_inv_t1_sym = C139.common_nullspace_in_block_sym(gens64_selftwist_sym, domain_block_t1, 64)
target_inv_t1_sym = C139.common_nullspace_in_block_sym(gens64_selftwist_sym, target_block_t1, 64)
d_selftwist_sym = C139.build_twisted_dirac_sympy(C139.E_sym, C139.NAB_sym, 8, C139.NAB_sym)
domain_on_t1 = R59.gram_schmidt(domain_inv_t1_sym)
target_on_t1 = R59.gram_schmidt(target_inv_t1_sym)
block_t1_exact = sp.zeros(len(target_on_t1), len(domain_on_t1))
for ti, w in enumerate(target_on_t1):
    for di, u in enumerate(domain_on_t1):
        block_t1_exact[ti, di] = sp.simplify(R59.hip(w, d_selftwist_sym * u))
rank_t1_exact = block_t1_exact.rank()
kernel_t1_exact = len(domain_on_t1) - rank_t1_exact

check(
    "t1_exact_kernel_matches_numeric",
    kernel_t1_exact == kernel_t1,
    f"T1 exact kernel = {kernel_t1_exact}, numeric = {kernel_t1}",
)
check(
    "t1_kernel_is_1_not_0",
    kernel_t1 == 1,
    f"T1 kernel = {kernel_t1} -- if 1, this is the genuine reference point against which "
    f"C141's own W''=m+2*1 kernel ({kernel_dim2}) is now a VALID, shape-controlled "
    "comparison (SAME shape (3,3), consistent unrestricted-second-factor methodology)",
)

# --- Robustness: does T1's kernel=1 hold across the whole admissible family? ---
t1_angle_sweep: dict[str, dict] = {}
t1_kernel_dims_seen = set()
for theta_deg in [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270]:
    theta = np.deg2rad(theta_deg)
    combo_dict = {k: np.cos(theta) * t1_dict[k] + np.sin(theta) * t2_dict[k] for k in range(1, 7)}
    nomizu_theta = C73B.matdict_to_nomizu(combo_dict)
    nab_theta_sym = {i: R59.spin_lift(nomizu_theta[i], C139.E_sym) for i in range(1, 7)}
    nab_theta_np = {i: np.array(nab_theta_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
    d_theta_t1 = C139.build_twisted_dirac_np(C139.E_np, nab_theta_np, 8, nab_theta_np)
    block_theta_t1 = target_inv_t1.conj().T @ d_theta_t1 @ domain_inv_t1
    sv_theta_t1 = np.linalg.svd(block_theta_t1, compute_uv=False)
    rank_theta_t1 = int(np.sum(sv_theta_t1 > 1e-8))
    kernel_theta_t1 = int(domain_inv_t1.shape[1]) - rank_theta_t1
    t1_angle_sweep[str(theta_deg)] = {
        "singular_values": [float(s) for s in sv_theta_t1],
        "kernel_dim": kernel_theta_t1,
    }
    t1_kernel_dims_seen.add(kernel_theta_t1)

check(
    "t1_kernel_constant_across_whole_admissible_family",
    len(t1_kernel_dims_seen) == 1,
    f"T1 kernel_dim(theta) in {sorted(t1_kernel_dims_seen)} across all 13 swept angles",
)

# --- Subspace-embedding consistency: T0's (domain,target) exactly embed in T1's ---
proj_d, *_ = np.linalg.lstsq(domain_inv_t1, domain_inv_t0, rcond=None)
resid_d = float(np.max(np.abs(domain_inv_t1 @ proj_d - domain_inv_t0)))
proj_t, *_ = np.linalg.lstsq(target_inv_t1, target_inv_t0, rcond=None)
resid_t = float(np.max(np.abs(target_inv_t1 @ proj_t - target_inv_t0)))
check(
    "t0_domain_and_target_embed_exactly_in_t1",
    resid_d < 1e-8 and resid_t < 1e-8,
    f"max residual (domain)={resid_d:.3e}, (target)={resid_t:.3e} -- confirms T1 is a "
    "consistent ENLARGEMENT of round59's own certified sector (T0), not an unrelated "
    "construction: round59's own (2,1)/kernel=1 sits inside T1's (3,3)/kernel=1 as an "
    "exact subspace",
)

DATA["t0_t1_apples_to_apples_comparison"] = {
    "t0_domain": int(domain_inv_t0.shape[1]),
    "t0_target": int(target_inv_t0.shape[1]),
    "t0_kernel": kernel_t0,
    "t1_domain": int(domain_inv_t1.shape[1]),
    "t1_target": int(target_inv_t1.shape[1]),
    "t1_kernel_numeric": kernel_t1,
    "t1_kernel_exact": int(kernel_t1_exact),
    "t1_block_exact": [
        [str(sp.nsimplify(sp.radsimp(v))) for v in row] for row in block_t1_exact.tolist()
    ],
    "t1_kernel_constant_across_sweep": len(t1_kernel_dims_seen) == 1,
    "t0_embeds_in_t1_residuals": {"domain": resid_d, "target": resid_t},
    "c141_w2_kernel_for_comparison": kernel_dim2,
    "shape_matched_discrimination": bool(kernel_t1 != kernel_dim2),
    "note": (
        "T1 (Sigma self-twisted, unrestricted 2nd factor) is the METHODOLOGICALLY "
        "CONSISTENT reference point for C141's own W''=m+2*1 computation (SAME "
        "unrestricted-2nd-factor convention, SAME resulting shape (3,3)) -- NOT "
        "round59's own EVEN_IDX-restricted (2,1). T0 confirms this section's own "
        "machinery against round59's certified values before trusting T1. "
        "SUPERSEDED by Section 10 below (skeptic-pass-2-triggered): the kernel "
        "difference (1 vs 0) found here is shown there to be FULLY EXPLAINED by a "
        "graded/per-connection-summand rank-nullity floor, computable from pure "
        "su(3) branching data alone with NO reference to the specific Dirac/NOMIZU "
        "geometry -- NOT a genuine dynamical discrimination. Kept here, unedited, "
        "per this project's Hindsight Distortion Gap Heuristic; do not read this "
        "note in isolation, read Section 10."
    ),
}
print(
    f"  T0 (positive control): domain={domain_inv_t0.shape[1]}, target={target_inv_t0.shape[1]}, kernel={kernel_t0}"
)
print(
    f"  T1 (apples-to-apples): domain={domain_inv_t1.shape[1]}, target={target_inv_t1.shape[1]}, kernel={kernel_t1}"
)
print(f"  C141 W''=m+2*1:        domain={domain_dim2}, target={target_dim2}, kernel={kernel_dim2}")
print(f"  SHAPE-MATCHED DISCRIMINATION (T1 kernel != C141 kernel): {kernel_t1 != kernel_dim2}")

# ========================================================================
# 10. SKEPTIC-PASS-2-TRIGGERED: the graded rank-nullity floor -- is the
# kernel difference (T1=1 vs C141=0) genuine dynamical/geometric content,
# or is it FULLY predictable from pure su(3) branching data alone (per
# {connection}-invariant summand of the twist bundle), given only the
# ALREADY-ESTABLISHED (by round59/C139) fact that each individual channel's
# connection data is nonzero?
#
# Both T1 and C141's own W'' are DIRECT SUMS over {connection}-invariant
# summands of the twist bundle (Section 8 already concedes this for W'';
# NAB's own EVEN/ODD-preservation, Section 3a-equivalent fact reused from
# C139, gives the same for T1's twist=Sigma). Rank-nullity, applied PER
# SUMMAND (not to the aggregate (3,3) shape), gives a LOWER BOUND on the
# aggregate kernel: sum over summands W_k of max(0, domain_k - target_k).
# This section checks whether the OBSERVED kernel, in every twist bundle
# computed in this project's history, exactly equals this floor -- using
# ONLY trivial_mult() (pure representation theory), with NO Dirac operator,
# NO NOMIZU, NO connection data of any kind.
# ========================================================================
print("\n=== 10. Graded rank-nullity floor (skeptic-pass-2-triggered) ===")


def graded_floor(summand_modules: list[dict[str, int]]) -> int:
    """Sum over {connection}-invariant summands of max(0, domain_k-target_k),
    each computed via trivial_mult against ODD_IDX_MODULE/EVEN_IDX_MODULE --
    PURE su(3) representation theory, no geometric/Dirac data whatsoever."""
    total = 0
    for w in summand_modules:
        d = trivial_mult(ODD_IDX_MODULE, w)
        t = trivial_mult(EVEN_IDX_MODULE, w)
        total += max(0, d - t)
    return total


# The {connection}-invariant summand decomposition of each twist bundle
# actually used in this project, stated as pure su(3)-module data:
GRADED_FLOOR_CASES = {
    "T0 / round59 (twist = EVEN_IDX alone, dim4, single summand)": {
        "summands": [{"1": 1, "3bar": 1}],
        "observed_kernel": kernel_t0,
    },
    "C139 (twist = m, dim6, SINGLE connection block, not decoupled)": {
        "summands": [{"3": 1, "3bar": 1}],
        "observed_kernel": C139.DATA["main_result"]["forward_kernel_dim"],
    },
    "C141 (twist = m+2*1, connection DECOUPLED into m-block + 2 zero-conn singlets)": {
        "summands": [{"3": 1, "3bar": 1}, {"1": 1}, {"1": 1}],
        "observed_kernel": kernel_dim2,
    },
    "T1 (twist = Sigma self-twist, NAB preserves EVEN/ODD exactly -> 2 summands)": {
        "summands": [{"1": 1, "3bar": 1}, {"3": 1, "1": 1}],
        "observed_kernel": kernel_t1,
    },
}

floor_matches_all = True
graded_floor_summary = {}
for name, d in GRADED_FLOOR_CASES.items():
    floor = graded_floor(d["summands"])
    match = floor == d["observed_kernel"]
    floor_matches_all = floor_matches_all and match
    graded_floor_summary[name] = {
        "summands": d["summands"],
        "graded_floor": floor,
        "observed_kernel": d["observed_kernel"],
        "matches": match,
    }
    print(f"  {name}")
    print(
        f"    summands={d['summands']}, graded_floor={floor}, observed_kernel={d['observed_kernel']}, matches={match}"
    )

check(
    "graded_rank_nullity_floor_exactly_predicts_observed_kernel_in_all_4_cases",
    floor_matches_all,
    "the graded/per-summand rank-nullity floor -- computable from pure su(3) "
    "branching data alone, NO Dirac/NOMIZU/connection geometry -- exactly equals "
    "the OBSERVED kernel in all 4 twist-bundle constructions computed in this "
    "project's history (T0/round59, C139, C141, T1). This means the KERNEL "
    "DIFFERENCE found in Section 9 (T1=1 vs C141=0) is FULLY EXPLAINED by pure "
    "representation theory (which {connection}-invariant summands each twist "
    "bundle has, and their individual domain-target imbalance), GIVEN ONLY the "
    "separately-established (by round59/C139, not new to this round) fact that "
    "each individual channel's connection data does not accidentally vanish -- "
    "NOT by any new geometric/dynamical fact this round's own computation "
    "contributes. Section 8's claim that the rank DIFFERENCE (as opposed to the "
    "individual decompositions) is 'not forced by shape alone' is THEREBY "
    "WITHDRAWN: the difference IS forced by shape alone (the graded floor "
    "difference is 1-0=1, exactly the observed kernel difference), once shape is "
    "correctly understood as the PER-SUMMAND (not merely aggregate) domain-target "
    "imbalance.",
)
DATA["graded_rank_nullity_floor"] = {
    "cases": graded_floor_summary,
    "all_match": floor_matches_all,
    "interpretation": (
        "For every twist bundle tested in this project's history (4/4), the "
        "observed kernel EXACTLY equals a graded rank-nullity floor computable "
        "from pure su(3) branching data (per {connection}-invariant summand), "
        "with NO reference to the specific Dirac operator/NOMIZU/connection "
        "geometry beyond the ALREADY-ESTABLISHED (by round59/C139) fact that "
        "each individual channel is nonzero. This means the T1-vs-C141 kernel "
        "DIFFERENCE (Section 9) is a pure representation-theory/branching "
        "artifact, not new dynamical/geometric content this round contributes -- "
        "it could have been predicted, without running ANY of this round's own "
        "Dirac-operator computation, purely from knowing each twist bundle's "
        "decomposition into connection-invariant summands and their individual "
        "domain-target shape imbalance (mult_W(3bar)-mult_W(3) per summand). "
        "This directly undermines claim.md's own kill criterion premise that a "
        "genuine discrimination 'cannot be attributed to a bare singlet-count/"
        "shape effect' -- it can, in every case tested so far, be so attributed, "
        "in a stronger (graded, per-summand) sense than claim.md's own literal "
        "kill criterion (b) anticipated (which only checked the AGGREGATE shape)."
    ),
}

# ------------------------------------------------------------------------
print("\n=== SUMMARY ===")
n_ok = sum(1 for v in RESULTS.values() if v)
print(
    f"  boolean checks : {len(RESULTS)} distinct names from {N_CHECK_CALLSITES} call sites  (passed {n_ok})"
)
print(f"  recorded data  : {len(DATA)}  -- NOT counted as checks")
print("  hardcoded-condition self-audit: PASS (no check() takes a literal)")
print(f"  failures       : {len(FAILURES)}  {FAILURES}")
print(
    f"\n  HEADLINE: domain={domain_dim2}, target={target_dim2}  (predicted by hand: "
    f"{PREREGISTERED_DOMAIN_INV},{PREREGISTERED_TARGET_INV}; claim.md naive: "
    f"{CLAIM_MD_NAIVE_DOMAIN},{CLAIM_MD_NAIVE_TARGET})"
)
print(
    f"  forward kernel_dim = {kernel_dim2}  (matches round59 pattern kernel==1: {kernel_dim2 == 1})"
)
print(f"  kernel_dim constant across whole admissible family: {len(kernel_dims_seen) == 1}")

with open(RESULTS_PATH, "w") as f:
    json.dump({"checks": RESULTS, "data": DATA}, f, indent=2, sort_keys=True, default=str)
print(f"  wrote {RESULTS_PATH}")
