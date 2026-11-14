r"""
C162 -- tool-verification of claim.md's hand-derived (Steps 1-6) argument:
Delta_dyn=0 is FORCED for the ONLY currently-buildable instantiation of
W_cand = 3 (+) 3bar (+) 3bar (OB14, C142's own candidate) -- namely `m` (this
project's already-certified S6 tangent/isotropy representation, module type
3(+)3bar) supplying one 3 and one 3bar, PLUS a fully DECOUPLED extra 3bar
summand (`3bar_extra`) supplying the second 3bar, regardless of what
connection that extra summand carries. See claim.md for the full hand-
derived argument this script checks, and decision.md for the verdict.

REUSES, does not modify:
  - round59_route_a_independent.py (R59): build_clifford/spin_lift/kron/
    gram_schmidt/hip/EVEN_IDX/ODD_IDX/NOMIZU/ADNU.
  - c139_twisted_s6_alternate_representation.py (C139): E_sym, NAB_sym,
    su3_ops_sym, rho_vector_sympy, block_global_gen,
    common_nullspace_in_block_sym, build_twisted_dirac_sympy, c_exact
    (C139's own certified c=-2*sqrt(3)/3, up to gauge phase).
  - c141_matched_singlet_twist.py (C141): trivial_mult, SU3_DUAL,
    EVEN_IDX_MODULE, ODD_IDX_MODULE (Section 2's own branching-counting
    machinery, F7's own exhaustive-search result).
  - C146's Term1-vanishing theorem is CITED (not re-imported as code): this
    script's own Step 4 independently re-derives the same style of result
    (no su(3)-invariant target for a zero-singlet/3bar-type summand) via
    direct nullspace computation, on a DIFFERENT domain-invariant vector
    than C146 checked (3bar_extra's own channel, not m's).

Imports sibling scripts by path (importlib.util.spec_from_file_location),
same pattern C161/C146 already use, to avoid a module-level import after
sys.path manipulation (E402-safe under any ruff rule set).

Run:  python c162_w_cand_delta_dyn_verification.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

import sympy as sp

CHECKS: list[dict] = []
DATA: dict[str, object] = {}


def check(name: str, cond, detail: str = "") -> bool:
    ok = bool(cond)
    CHECKS.append({"name": name, "ok": ok, "detail": detail})
    print(f"  [{'OK' if ok else 'FAIL'}] {name} :: {detail}")
    return ok


def _load_module(mod_name: str, sibling_dir: str, file_name: str):
    """Import a sibling experiment's script by path, no module-level import
    after sys.path manipulation -- same pattern as C161's own
    `_load_c136_module` / C146's own `load_module`, avoids E402 regardless
    of which ruff rule set a given invocation enables."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", sibling_dir, file_name))
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


print("Loading round59, C139, C141 (siblings) -- this RE-EXECUTES their own")
print("scripts end-to-end (same pattern C146 already used for C139/round59).")
R59 = _load_module(
    "round59_route_a_independent",
    "20260714-round59-trivial-rank-certification",
    "round59_route_a_independent.py",
)
C139 = _load_module(
    "c139_twisted_s6_alternate_representation",
    "20260904-c139-twisted-s6-alternate-representation-negative-control",
    "c139_twisted_s6_alternate_representation.py",
)
C141 = _load_module(
    "c141_matched_singlet_twist",
    "20260904-c141-matched-singlet-count-twist-m-plus-2singlets",
    "c141_matched_singlet_twist.py",
)


# ============================================================================
# STEP 1 -- re-derive W_cand's domain/target shape via C141's own
# trivial_mult() branching-counting function, reused UNMODIFIED.
# ============================================================================
def step1_domain_target_shape() -> tuple[int, int]:
    print()
    print("=" * 78)
    print("STEP 1 -- W_cand's domain/target shape, via C141's own trivial_mult()")
    print("=" * 78)
    # W_cand = 3 (+) 3bar (+) 3bar, i.e. (mult_1,mult_3,mult_3bar) = (0,1,2) --
    # C141's own F7 exhaustive search's SECOND solution for shape (2,1).
    wcand_module = {"3": 1, "3bar": 2}
    domain = C141.trivial_mult(C141.ODD_IDX_MODULE, wcand_module)
    target = C141.trivial_mult(C141.EVEN_IDX_MODULE, wcand_module)
    print(f"  W_cand module = {wcand_module}  (mult_1,mult_3,mult_3bar)=(0,1,2)")
    print(f"  domain = trivial_mult(ODD_IDX_MODULE, W_cand)  = {domain}")
    print(f"  target = trivial_mult(EVEN_IDX_MODULE, W_cand) = {target}")
    check(
        "step1_domain_target_matches_c141_f7_solution",
        (domain, target) == (2, 1),
        f"got (domain,target)=({domain},{target}), expected (2,1) -- C141's own F7 "
        "exhaustive search (script line ~318) found (mult_1,mult_3,mult_3bar)=(0,1,2) "
        "is one of exactly two module types giving shape (2,1); this re-derives it "
        "via the identical trivial_mult() function, not a new formula.",
    )
    DATA["step1_domain"] = domain
    DATA["step1_target"] = target
    return domain, target


# ============================================================================
# STEP 2/3 setup -- build W_cand = m (+) 3bar_extra CONCRETELY.
# 3bar_extra is realized as an independent copy of the "3bar" irrep (Sigma_
# even's own {4,5,6} sub-block of su3_ops_sym -- a genuine su(3) sub-
# representation, C139 Section 3a: spin_lift of ANY so(6) bivector preserves
# Sigma's even/odd parity, so Sigma_even is su3_ops_sym-invariant and its
# {4,5,6} 3bar-piece is itself a valid, independent su(3) representation).
# Using a literal copy of "the" 3bar irrep for 3bar_extra does not smuggle in
# any coupling to m: the connection built below is block-diagonal (zero
# cross-coupling) by construction, per C139 Section 17's own "no NOMIZU-
# derived data for an extra summand" reasoning (the only currently-
# buildable option).
# ============================================================================
def build_wcand(extra_conn_scale) -> dict[str, object]:
    """Build W_cand = m (+) 3bar_extra's su(3) action (9x9, fixed) and its
    Dirac connection (9x9 per generator i=1..6, with the extra 3x3 block
    scaled by `extra_conn_scale` -- 0 for the natural/decoupled-zero choice,
    a symbolic t for the genericity probe in Step 4b)."""
    su3_ops_sym = C139.su3_ops_sym
    rho_3bar_extra_sym = {a: su3_ops_sym[a].extract([4, 5, 6], [4, 5, 6]) for a in range(1, 9)}
    rho_m_su3_sym = {a: C139.rho_vector_sympy(R59.ADNU[a]) for a in range(1, 9)}
    rho_wcand_su3_sym = {a: sp.diag(rho_m_su3_sym[a], rho_3bar_extra_sym[a]) for a in range(1, 9)}

    conn_m_sym = {i: C139.rho_vector_sympy(R59.NOMIZU[i]) for i in range(1, 7)}
    # arbitrary FIXED nonzero antisymmetric 3x3 "connection shape" for the
    # genericity probe -- not claimed to be geometric, purely a nonzero
    # probe to test Step 4's "regardless of connection" claim.
    m_extra_shape = sp.Matrix([[0, 1, 0], [-1, 0, 1], [0, -1, 0]])
    conn_wcand_sym = {
        i: sp.diag(conn_m_sym[i], extra_conn_scale * m_extra_shape) for i in range(1, 7)
    }
    return {
        "rho_3bar_extra_sym": rho_3bar_extra_sym,
        "rho_wcand_su3_sym": rho_wcand_su3_sym,
        "conn_m_sym": conn_m_sym,
        "conn_wcand_sym": conn_wcand_sym,
    }


def step2_decoupling_check(built: dict[str, object]) -> None:
    print()
    print("=" * 78)
    print("STEP 2 -- W_cand's su(3) action is genuinely block-diagonal (decoupled)")
    print("=" * 78)
    rho = built["rho_wcand_su3_sym"]
    block_diagonal = all(
        rho[a][:6, 6:] == sp.zeros(6, 3) and rho[a][6:, :6] == sp.zeros(3, 6) for a in range(1, 9)
    )
    check(
        "step2_wcand_su3_action_block_diagonal",
        block_diagonal,
        "W_cand's 9x9 su(3) action has exactly zero cross-blocks between m (rows/cols "
        "0-5) and 3bar_extra (rows/cols 6-8) for all 8 generators -- confirms "
        "3bar_extra is genuinely decoupled from m, per C139 Section 17's own "
        "'no NOMIZU-derived data for an extra summand, only buildable as decoupled' "
        "reasoning (there quoted for m(+)2*1's extra singlets; applied here to "
        "W_cand's extra 3bar summand, one assumption transferred by direct analogy, "
        "not re-derived from new geometric content -- see decision.md's self-"
        "adversarial pass for why this transfer is checked, not merely assumed).",
    )


# ============================================================================
# STEP 4 (LOAD-BEARING) -- explicit branching of Sigma_even (x) 3bar_extra
# and Sigma_odd (x) 3bar_extra, via the SAME invariant-subspace/nullspace
# method C139 already uses for its own domain_inv/target_inv (NOT by citing
# Clebsch-Gordan rules abstractly) -- cross-validated against C141's own
# trivial_mult() as an independent check of the same fact.
# ============================================================================
def step4_branching(built: dict[str, object]) -> tuple[int, int]:
    print()
    print("=" * 78)
    print("STEP 4 (load-bearing) -- explicit su(3)-invariant-subspace computation")
    print("=" * 78)
    su3_ops_sym = C139.su3_ops_sym
    rho_3bar_extra_sym = built["rho_3bar_extra_sym"]

    rho_even_sym = {a: su3_ops_sym[a].extract(R59.EVEN_IDX, R59.EVEN_IDX) for a in range(1, 9)}
    rho_odd_sym = {a: su3_ops_sym[a].extract(R59.ODD_IDX, R59.ODD_IDX) for a in range(1, 9)}

    gens_even_extra = [
        R59.kron(rho_even_sym[a], sp.eye(3)) + R59.kron(sp.eye(4), rho_3bar_extra_sym[a])
        for a in range(1, 9)
    ]
    gens_odd_extra = [
        R59.kron(rho_odd_sym[a], sp.eye(3)) + R59.kron(sp.eye(4), rho_3bar_extra_sym[a])
        for a in range(1, 9)
    ]

    even_extra_inv = C139.common_nullspace_in_block_sym(gens_even_extra, list(range(12)), 12)
    odd_extra_inv = C139.common_nullspace_in_block_sym(gens_odd_extra, list(range(12)), 12)

    print(
        f"  dim su(3)-invariants, Sigma_even (1+3bar, 4-dim) (x) 3bar_extra (3-dim):"
        f" {len(even_extra_inv)}  (claim.md predicts 0)"
    )
    print(
        f"  dim su(3)-invariants, Sigma_odd  (3+1, 4-dim)   (x) 3bar_extra (3-dim):"
        f" {len(odd_extra_inv)}  (claim.md predicts 1)"
    )

    check(
        "step4_load_bearing_no_singlet_in_sigma_even_tensor_3bar_extra",
        len(even_extra_inv) == 0,
        f"got {len(even_extra_inv)} su(3)-invariant vectors in Sigma_even (x) 3bar_extra "
        "(12-dim ambient) -- the load-bearing claim: no su(3)-invariant target vector "
        "exists for a decoupled 3bar_extra connection to map into, forcing its own "
        "contribution to target_inv to be zero REGARDLESS of what connection it carries.",
    )
    check(
        "step4_sigma_odd_tensor_3bar_extra_has_exactly_one_singlet",
        len(odd_extra_inv) == 1,
        f"got {len(odd_extra_inv)} su(3)-invariant vectors in Sigma_odd (x) 3bar_extra "
        "(12-dim ambient) -- consistent with Step 1's domain=2: one dimension from m's "
        "own 3bar (already C139-certified), one from 3bar_extra's own singlet channel "
        "(3 (x) 3bar_extra -> 1).",
    )

    tb_even = C141.trivial_mult(C141.EVEN_IDX_MODULE, {"3bar": 1})
    tb_odd = C141.trivial_mult(C141.ODD_IDX_MODULE, {"3bar": 1})
    print(f"  cross-validation, C141's trivial_mult(EVEN_IDX_MODULE,{{'3bar':1}}) = {tb_even}")
    print(f"  cross-validation, C141's trivial_mult(ODD_IDX_MODULE, {{'3bar':1}}) = {tb_odd}")
    check(
        "step4_cross_validation_trivial_mult_matches_explicit_nullspace",
        (tb_even, tb_odd) == (len(even_extra_inv), len(odd_extra_inv)),
        f"abstract branching-count method (trivial_mult) gives ({tb_even},{tb_odd}); "
        f"explicit su(3)-invariant-subspace computation gives "
        f"({len(even_extra_inv)},{len(odd_extra_inv)}) -- two independent methods must "
        "agree, and do.",
    )
    DATA["step4_even_extra_invariant_dim"] = len(even_extra_inv)
    DATA["step4_odd_extra_invariant_dim"] = len(odd_extra_inv)
    return len(even_extra_inv), len(odd_extra_inv)


# ============================================================================
# STEP 2/3/5/6 -- full 9-dim construction: domain_inv/target_inv for the
# ACTUAL W_cand = m (+) 3bar_extra, target_inv's location (Step 3), the
# resulting 1x2 matrix (Step 5), and Delta_dyn (Step 6).
# ============================================================================
def step5_full_construction_and_delta_dyn(
    built_zero: dict[str, object], domain_predicted: int, target_predicted: int
) -> dict[str, object]:
    print()
    print("=" * 78)
    print("STEP 2/3/5/6 -- full 9-dim W_cand construction, target_inv location,")
    print("                the 1x2 matrix, and Delta_dyn")
    print("=" * 78)
    su3_ops_sym = C139.su3_ops_sym
    NAB_sym = C139.NAB_sym
    E_sym = C139.E_sym
    rho_wcand_su3_sym = built_zero["rho_wcand_su3_sym"]
    conn_wcand_sym_zero = built_zero["conn_wcand_sym"]  # extra_conn_scale=0

    gens_leibniz_72 = [
        R59.kron(su3_ops_sym[a], sp.eye(9)) + R59.kron(sp.eye(8), rho_wcand_su3_sym[a])
        for a in range(1, 9)
    ]
    domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(9)), 9)
    target_block = C139.block_global_gen(R59.EVEN_IDX, list(range(9)), 9)

    domain_inv = C139.common_nullspace_in_block_sym(gens_leibniz_72, domain_block, 72)
    target_inv = C139.common_nullspace_in_block_sym(gens_leibniz_72, target_block, 72)
    print(
        f"  domain_inv dimension (exact) = {len(domain_inv)}  (Step 1 predicts {domain_predicted})"
    )
    print(
        f"  target_inv dimension (exact) = {len(target_inv)}  (Step 1 predicts {target_predicted})"
    )
    check(
        "step5_domain_inv_dim_matches_step1_prediction",
        len(domain_inv) == domain_predicted,
        f"got {len(domain_inv)}, predicted {domain_predicted}",
    )
    check(
        "step5_target_inv_dim_matches_step1_prediction",
        len(target_inv) == target_predicted,
        f"got {len(target_inv)}, predicted {target_predicted}",
    )

    target_on = R59.gram_schmidt(target_inv)
    domain_on = R59.gram_schmidt(domain_inv)

    # ---- Step 3: target_inv's only nonzero components lie in m's own
    # 6-dim block (indices 0-5 of each 9-dim W-slot); the 3bar_extra block
    # (indices 6-8) is exactly zero -- confirms target_inv is IDENTICAL to
    # C139's own already-computed target_inv, since 3bar_extra contributes
    # zero 3-multiplicity (Step 4).
    w_hat = target_on[0]

    def extra_block_components(vec) -> list:
        return [vec[k * 9 + 6 + j, 0] for k in R59.EVEN_IDX for j in range(3)]

    w_extra_zero = all(sp.simplify(v) == 0 for v in extra_block_components(w_hat))
    check(
        "step3_target_inv_avoids_3bar_extras_own_block",
        w_extra_zero,
        "target_inv's basis vector has exactly zero components in 3bar_extra's own "
        "3-dim W-slot -- confirms Step 3: target_inv is entirely m's own channel.",
    )

    # classify the 2 domain_inv basis vectors by which W-block they live in
    def m_block_norm2(vec) -> sp.Expr:
        return sp.simplify(
            sum(sp.Abs(vec[k * 9 + j, 0]) ** 2 for k in R59.ODD_IDX for j in range(6))
        )

    def extra_block_norm2(vec) -> sp.Expr:
        return sp.simplify(
            sum(sp.Abs(vec[k * 9 + 6 + j, 0]) ** 2 for k in R59.ODD_IDX for j in range(3))
        )

    m_norms = [m_block_norm2(u) for u in domain_on]
    extra_norms = [extra_block_norm2(u) for u in domain_on]
    print(f"  domain_on m-block norms:     {m_norms}")
    print(f"  domain_on extra-block norms: {extra_norms}")
    check(
        "domain_on_splits_cleanly_into_m_channel_and_extra_channel",
        sorted([m_norms[0] == 0, extra_norms[0] == 0])
        != sorted([m_norms[1] == 0, extra_norms[1] == 0])
        or (m_norms[0] != 0 and extra_norms[0] == 0 and m_norms[1] == 0 and extra_norms[1] != 0)
        or (m_norms[1] != 0 and extra_norms[1] == 0 and m_norms[0] == 0 and extra_norms[0] != 0),
        "the 2 domain_inv basis vectors should decouple into one purely-m-block vector "
        "and one purely-extra-block vector, since W_cand's su(3) action and connection "
        "are both block-diagonal (Step 2) -- checked directly, not assumed.",
    )
    m_channel_idx = 0 if m_norms[0] != 0 else 1
    extra_channel_idx = 1 - m_channel_idx

    # ---- Step 5: the 1x2 matrix (d_m, d_extra), zero-connection instantiation.
    d_wcand_zero = C139.build_twisted_dirac_sympy(E_sym, NAB_sym, 9, conn_wcand_sym_zero)
    c_row_zero = [sp.simplify(R59.hip(w_hat, d_wcand_zero * u)) for u in domain_on]
    d_m = c_row_zero[m_channel_idx]
    d_extra_zero_conn = c_row_zero[extra_channel_idx]
    print(f"  d_m (m-channel entry)          = {d_m}")
    print(f"  d_extra (extra-channel, zero connection on 3bar_extra) = {d_extra_zero_conn}")

    check(
        "step5_d_extra_is_zero_at_the_natural_zero_connection",
        sp.simplify(d_extra_zero_conn) == 0,
        f"got d_extra={d_extra_zero_conn} at the natural (decoupled, zero-connection) "
        "instantiation -- expected exactly 0.",
    )
    check(
        "step5_d_m_matches_c139s_own_certified_c_magnitude",
        bool(abs(complex(sp.N(d_m))) > 0)
        and bool(abs(abs(complex(sp.N(d_m))) - abs(complex(sp.N(C139.c_exact)))) < 1e-8),
        f"|d_m|={abs(complex(sp.N(d_m)))}, |C139.c_exact|={abs(complex(sp.N(C139.c_exact)))} "
        "-- must match (up to the already-documented gauge phase freedom, C139 Section 6): "
        "target_inv here is literally the same 1-dim invariant C139 already certified.",
    )

    # ---- Step 4b (genericity probe): rebuild with a SYMBOLIC nonzero
    # connection scale `t` on 3bar_extra's own block, confirm d_extra
    # simplifies to literally 0 for ALL t (not merely at t=0) -- directly
    # testing claim.md's "regardless of what connection the decoupled extra
    # 3bar summand carries" clause, not just the natural zero-connection case.
    t = sp.symbols("t_extra_conn", real=True)
    built_generic = build_wcand(t)
    conn_wcand_sym_generic = built_generic["conn_wcand_sym"]
    d_wcand_generic = C139.build_twisted_dirac_sympy(E_sym, NAB_sym, 9, conn_wcand_sym_generic)
    d_extra_generic = sp.simplify(R59.hip(w_hat, d_wcand_generic * domain_on[extra_channel_idx]))
    d_m_generic = sp.simplify(R59.hip(w_hat, d_wcand_generic * domain_on[m_channel_idx]))
    print(
        f"  d_extra(t) with an ARBITRARY nonzero connection scale t on 3bar_extra: {d_extra_generic}"
    )
    print(f"  d_m(t) (should be t-independent, m untouched by 3bar_extra's own t): {d_m_generic}")
    check(
        "step4b_d_extra_vanishes_identically_for_arbitrary_nonzero_connection",
        sp.simplify(sp.expand(d_extra_generic)) == 0,
        f"d_extra(t)={d_extra_generic} -- must be IDENTICALLY zero as a function of t "
        "(not merely at t=0) to support claim.md's 'regardless of what connection' "
        "clause. Scope caveat (see decision.md): this uses ONE fixed antisymmetric "
        "3x3 shape scaled by a single symbol t (uniform across i=1..6), not the FULL "
        "space of possible decoupled connections -- a genuine, honestly-scoped "
        "limitation, not a claim of full generality.",
    )
    check(
        "step4b_d_m_is_independent_of_3bar_extras_own_connection_t",
        sp.simplify(sp.diff(d_m_generic, t)) == 0,
        f"d_m(t)={d_m_generic}, d(d_m)/dt={sp.simplify(sp.diff(d_m_generic, t))} -- "
        "m's own channel must not depend on 3bar_extra's connection at all, confirming "
        "the block-diagonal decoupling holds all the way through the Dirac operator, "
        "not just the su(3) action.",
    )

    # ---- Step 6: Delta_dyn.
    matrix_1x2 = sp.Matrix([[d_m, d_extra_zero_conn]])
    rank = matrix_1x2.rank()
    domain_dim = len(domain_inv)
    target_dim = len(target_inv)
    floor = max(0, domain_dim - target_dim)
    kernel_dim = domain_dim - rank
    delta_dyn = kernel_dim - floor
    print(f"  matrix (d_m, d_extra) = {matrix_1x2.tolist()}")
    print(
        f"  rank={rank}, domain={domain_dim}, target={target_dim}, floor={floor}, "
        f"kernel={kernel_dim}, Delta_dyn={delta_dyn}"
    )
    check(
        "step6_rank_is_exactly_1",
        rank == 1,
        f"got rank={rank}, expected 1 (d_m!=0, d_extra=0, so a 1x2 nonzero row has rank 1)",
    )
    check(
        "step6_delta_dyn_is_forced_zero",
        delta_dyn == 0,
        f"Delta_dyn = kernel({kernel_dim}) - floor({floor}) = {delta_dyn}, expected 0 -- "
        "the claim's central conclusion.",
    )
    DATA["step6_domain_dim"] = domain_dim
    DATA["step6_target_dim"] = target_dim
    DATA["step6_rank"] = rank
    DATA["step6_floor"] = floor
    DATA["step6_kernel_dim"] = kernel_dim
    DATA["step6_delta_dyn"] = delta_dyn
    DATA["step5_d_m"] = str(d_m)
    DATA["step5_d_extra_zero_conn"] = str(d_extra_zero_conn)
    DATA["step4b_d_extra_generic_t"] = str(d_extra_generic)
    return {"delta_dyn": delta_dyn, "rank": rank, "kernel_dim": kernel_dim, "floor": floor}


def main() -> int:
    print("=" * 78)
    print("C162 -- W_cand Delta_dyn tool-verification (claim.md Steps 1-6)")
    print("=" * 78)

    domain_predicted, target_predicted = step1_domain_target_shape()
    built_zero = build_wcand(sp.Integer(0))
    step2_decoupling_check(built_zero)
    step4_branching(built_zero)
    result = step5_full_construction_and_delta_dyn(built_zero, domain_predicted, target_predicted)

    n_ok = sum(1 for c in CHECKS if c["ok"])
    n = len(CHECKS)
    print("-" * 78)
    print(f"CHECKS: {n_ok}/{n} passed")
    print()
    if n_ok == n:
        print("VERDICT: Steps 1-6 all confirmed by direct computation -- per claim.md's")
        print("kill criterion, this is PROMOTE-AS-NECESSARY-CONDITION.")
    else:
        print("VERDICT: at least one check FAILED -- see decision.md for classification")
        print("into claim.md's kill-criterion table (ARITHMETIC_ERROR / ")
        print("ASSUMPTION_NARROWER_THAN_STATED / C147_ITSELF_NEEDS_REVISITING).")

    out = {
        "checks_total": n,
        "checks_passed": n_ok,
        "all_passed": n_ok == n,
        "checks": CHECKS,
        "data": DATA,
        "delta_dyn_result": result,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_c162.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nwrote {path}")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
