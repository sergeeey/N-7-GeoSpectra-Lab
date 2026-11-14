"""C172: plug the REAL twisted D_S6 (round59's own build_dirac, 64x64 on
Sigma(x)Sigma) into E3's Cl(9) product-Dirac framework together with D_S3(t)
(E2/E3/C170's 2x2 torsion family), instead of E3's flat Clifford-algebra
stand-ins. Answers C169 escalation item 2.

Four pre-registered checks (see claim.md):
  1. chi6_twisted = chi6(x)I_8 anticommutes with round59's own D exactly.
  2. Sire-Xu decoupling D_full^2 = D^2(x)I_2 + I_64(x)D_S3(t)^2 holds exactly.
  3. D itself has an exact zero eigenvalue, multiplicity checked against
     round59's own claimed dim ker=1 (an independent full-matrix diagonalization,
     round59 itself never diagonalized the full 64x64 matrix).
  4. An EXPLICIT combined vector v(x)w (v in ker(D), w in ker(D_S3(0 or 1)))
     satisfies D_full.(v(x)w) = 0 exactly, by direct matrix-vector multiplication.

round59's own E/NOMIZU/build_dirac are imported verbatim (importlib against the
actual committed file, not re-transcribed) -- same discipline as C171.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

ROUND59_PATH = (
    Path(__file__).parent.parent
    / "20260714-round59-trivial-rank-certification"
    / "round59_route_a_independent.py"
)


def load_round59_module():
    spec = importlib.util.spec_from_file_location("round59_module", ROUND59_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# chi6_twisted = chi6(x)I_8, built from round59's OWN E[1..6] (not E3's
# separately-built Jordan-Wigner generators -- chi6 must anticommute with
# round59's ACTUAL D, which is built from round59's own E).
# ---------------------------------------------------------------------------
def build_chi6_from_round59_E(E: dict) -> sp.Matrix:
    omega = E[1]
    for k in range(2, 7):
        omega = omega * E[k]
    chi6 = sp.I * omega
    return chi6


def check_chi6_properties(chi6: sp.Matrix, E: dict) -> dict:
    I8 = sp.eye(8)
    hermitian = sp.simplify(chi6 - chi6.conjugate().T) == sp.zeros(8, 8)
    sq_is_I = sp.simplify(chi6 * chi6 - I8) == sp.zeros(8, 8)
    anticommutes = {}
    all_anticommute = True
    for k in range(1, 7):
        ac = sp.simplify(chi6 * E[k] + E[k] * chi6)
        is_zero = ac == sp.zeros(8, 8)
        anticommutes[k] = is_zero
        if not is_zero:
            all_anticommute = False
    return {
        "hermitian": bool(hermitian),
        "chi6_squared_is_I": bool(sq_is_I),
        "anticommutes_with_each_E": anticommutes,
        "all_anticommute": all_anticommute,
    }


def kron_sp(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(A, B))


# ---------------------------------------------------------------------------
# Check 1: {chi6_twisted, D} = 0 exactly (symbolic)
# ---------------------------------------------------------------------------
def check1_anticommutation(chi6: sp.Matrix, D: sp.Matrix) -> dict:
    I8 = sp.eye(8)
    chi6_twisted = kron_sp(chi6, I8)
    anticomm = chi6_twisted * D + D * chi6_twisted
    is_zero = sp.simplify(anticomm) == sp.zeros(64, 64)
    return {
        "chi6_twisted_shape": list(chi6_twisted.shape),
        "D_shape": list(D.shape),
        "anticommutator_is_exactly_zero": bool(is_zero),
    }, chi6_twisted


# ---------------------------------------------------------------------------
# Check 2: decoupling identity D_full^2 = D^2(x)I_2 + I_64(x)D_S3(t)^2
# ---------------------------------------------------------------------------
def d_s3_matrix(t, h_H=None, d_lc_n0=None) -> sp.Matrix:
    """Reused closed form from E2/E3/C170: D_S3(t) = d_lc_n0*sigma_z + (t-1/2)*h_H*I2."""
    h_H = sp.Integer(3) if h_H is None else h_H
    d_lc_n0 = sp.Rational(3, 2) if d_lc_n0 is None else d_lc_n0
    sz = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    return d_lc_n0 * sz + (t - sp.Rational(1, 2)) * h_H * I2


def build_d_full(D: sp.Matrix, chi6_twisted: sp.Matrix, d_s3: sp.Matrix) -> sp.Matrix:
    I2 = sp.eye(2)
    return kron_sp(D, I2) + kron_sp(chi6_twisted, d_s3)


def check2_decoupling(D: sp.Matrix, chi6_twisted: sp.Matrix, t) -> dict:
    d_s3 = d_s3_matrix(t)
    d_full = build_d_full(D, chi6_twisted, d_s3)
    I2 = sp.eye(2)
    I64 = sp.eye(64)
    lhs = d_full * d_full
    rhs = kron_sp(D * D, I2) + kron_sp(I64, d_s3 * d_s3)
    diff = sp.simplify(lhs - rhs)
    is_zero = diff == sp.zeros(128, 128)
    max_abs_entry = max(
        (abs(complex(x.evalf())) for x in diff) if not is_zero else [0.0], default=0.0
    )
    return {
        "t": str(t),
        "decoupling_holds_exactly": bool(is_zero),
        "max_abs_residual_entry": float(max_abs_entry),
    }


# ---------------------------------------------------------------------------
# Check 3: D's own exact kernel (direct full-matrix nullspace, numeric cross-check)
# ---------------------------------------------------------------------------
def check3_kernel_of_D(D: sp.Matrix) -> dict:
    ns_exact = D.nullspace()
    dim_ker_exact = len(ns_exact)

    D_np = np.array(D.evalf(), dtype=complex)
    eigvals_np = np.linalg.eigvals(D_np)
    near_zero_count = int(np.sum(np.abs(eigvals_np) < 1e-9))
    max_near_zero_resid = float(np.min(np.abs(eigvals_np))) if len(eigvals_np) > 0 else float("nan")

    return {
        "dim_ker_exact_sympy_nullspace": dim_ker_exact,
        "dim_ker_matches_round59_claim_of_1": dim_ker_exact == 1,
        "numeric_eigvals_near_zero_count": near_zero_count,
        "numeric_smallest_abs_eigval": max_near_zero_resid,
        "numeric_matches_exact": near_zero_count == dim_ker_exact,
    }, (ns_exact[0] if dim_ker_exact >= 1 else None)


# ---------------------------------------------------------------------------
# Check 4: explicit combined kernel vector v(x)w, D_full.(v(x)w) = 0 exactly
# ---------------------------------------------------------------------------
def check4_explicit_combined_kernel(
    D: sp.Matrix, chi6_twisted: sp.Matrix, v: sp.Matrix, t_label: str, t
) -> dict:
    d_s3 = d_s3_matrix(t)
    ns_s3 = d_s3.nullspace()
    if not ns_s3:
        return {"t_label": t_label, "t": str(t), "d_s3_has_kernel": False}
    w = ns_s3[0]

    d_full = build_d_full(D, chi6_twisted, d_s3)
    v_norm = v / sp.sqrt((v.conjugate().T * v)[0, 0])
    w_norm = w / sp.sqrt((w.conjugate().T * w)[0, 0])
    combined = kron_sp(v_norm, w_norm)  # 128x1
    result = sp.simplify(d_full * combined)
    is_exactly_zero = result == sp.zeros(128, 1)
    max_abs_entry = max((abs(complex(x.evalf())) for x in result), default=0.0)

    return {
        "t_label": t_label,
        "t": str(t),
        "d_s3_has_kernel": True,
        "d_s3_kernel_dim": len(ns_s3),
        "combined_vector_dim": combined.shape[0],
        "d_full_times_combined_is_exactly_zero": bool(is_exactly_zero),
        "max_abs_residual_entry": float(max_abs_entry),
    }


# ---------------------------------------------------------------------------
# Check 5 (added after skeptic pass): directly diagonalize/nullspace the
# FULL 128x128 D_full -- this is what E3's own decision.md actually asked
# for ("confirm min|eig(D_full)|=0 exactly at t=0/t=1" by diagonalizing,
# not by pre-selecting a vector and multiplying it through). Also verifies
# the ker(D_full)=ker(D)(x)ker(D_S3(t)) identity the skeptic derived
# analytically (from D_full Hermitian + decoupling => D^2(x)I and
# I(x)D_S3(t)^2 are commuting PSD summands), rather than asserting it.
# ---------------------------------------------------------------------------
def check5_full_dfull_kernel_dimension(
    D: sp.Matrix, chi6_twisted: sp.Matrix, dim_ker_D: int, t_label: str, t
) -> dict:
    d_s3 = d_s3_matrix(t)
    dim_ker_d_s3 = len(d_s3.nullspace())
    d_full = build_d_full(D, chi6_twisted, d_s3)
    ns_full_exact = d_full.nullspace()
    dim_ker_full_exact = len(ns_full_exact)
    predicted = dim_ker_D * dim_ker_d_s3
    return {
        "t_label": t_label,
        "t": str(t),
        "dim_ker_D_S3_at_this_t": dim_ker_d_s3,
        "dim_ker_D_full_exact_nullspace": dim_ker_full_exact,
        "predicted_dim_ker_D_x_ker_D_S3": predicted,
        "matches_tensor_product_prediction": dim_ker_full_exact == predicted,
    }


# ---------------------------------------------------------------------------
# Regression sanity: re-derive round59's own headline numbers via the SAME
# imported module, to confirm the importlib reuse didn't silently break
# anything (same discipline as C171's own T3 cross-check).
# ---------------------------------------------------------------------------
def regression_check_round59(mod) -> dict:
    E = mod.build_clifford(conj=False)
    su3_ops = [mod.spin_lift(mod.ADNU[a], E) for a in range(1, 9)]
    gens = [mod.leibniz(N) for N in su3_ops]
    _amps, s, res_zero, ndom, ntgt = mod.certificate(
        E,
        mod.NOMIZU,
        gens,
        domain_first=mod.ODD_IDX,
        domain_second=mod.EVEN_IDX,
        target_first=mod.EVEN_IDX,
        target_second=mod.EVEN_IDX,
    )
    return {
        "s_positive": bool(sp.simplify(s) > 0),
        "residual_zero": bool(res_zero),
        "ndom": ndom,
        "ntgt": ntgt,
    }


# ---------------------------------------------------------------------------
# Reconciliation check: is check3's 36-dim UNRESTRICTED ker(D) genuinely
# consistent with round59's own dim=1 claim, which is the kernel of a
# RESTRICTED map (su(3)-invariant odd(x)even -> even(x)even sector, domain
# dim 2, rank 1, so kernel-within-that-restricted-domain = 1)? Reconstruct
# round59's own restricted-sector kernel vector explicitly (from its own
# `certificate` amplitudes a, b: the domain combination b*u0 - a*u1 maps to
# zero under the compressed map) and check whether it is ALSO an element of
# the full, unrestricted ker(D) -- i.e. whether "36" and "1" are the same
# kind of quantity (a real contradiction) or genuinely different quantities
# (round59's own vector should be ONE specific element of the 36).
#
# HONESTY NOTE (added after an independent context-blind skeptic pass, per
# this project's Step 8a discipline): this check has ZERO discriminating
# power given round59's own already-published numbers. round59's own
# decision.md reports residual_zero=True (D*u0=a*w, D*u1=b*w EXACTLY) and
# s=|a|^2+|b|^2=4>0. Given those two already-established facts alone,
# D*(b*u0-a*u1) = ba*w - ab*w = 0 identically, for ANY a,b with at least
# one nonzero -- the only way this check could fail is a=b=0, which
# round59's own s=4>0 already excludes. So "passing" here is not new
# evidence; it is a re-statement of round59's own rank-1 computation in
# different notation (b*u0-a*u1 IS the standard kernel vector of a rank-1
# linear map from a 2-dim domain). Kept in the script (fixing a real
# tuple-unpacking bug the skeptic found in its unreachable early-return
# branch) because it is still a correct, honest EXPLICIT-VECTOR
# construction (useful in its own right, see decision.md), not because it
# discriminates anything.
# ---------------------------------------------------------------------------
def reconcile_round59_vector_against_full_kernel(mod, D: sp.Matrix) -> dict:
    E = mod.build_clifford(conj=False)
    su3_ops = [mod.spin_lift(mod.ADNU[a], E) for a in range(1, 9)]
    gens = [mod.leibniz(N) for N in su3_ops]
    dom_g = mod.block_global(mod.ODD_IDX, mod.EVEN_IDX)
    dom_inv = mod.common_nullspace_in_block(gens, dom_g)
    dom_on = mod.gram_schmidt(dom_inv)

    tgt_g = mod.block_global(mod.EVEN_IDX, mod.EVEN_IDX)
    tgt_inv = mod.common_nullspace_in_block(gens, tgt_g)
    tgt_on = mod.gram_schmidt(tgt_inv)

    amps = []
    for u in dom_on:
        Du = D * u
        comps = [sp.simplify(mod.hip(w, Du)) for w in tgt_on]
        amps.append(comps)

    if len(dom_on) != 2 or len(amps[0]) != 1:
        return {"applicable": False, "reason": "unexpected domain/target dims"}, None

    a = amps[0][0]
    b = amps[1][0]
    # kernel-of-restricted-map combination: b*u0 - a*u1
    v_round59 = b * dom_on[0] - a * dom_on[1]
    Dv = sp.simplify(D * v_round59)
    is_in_full_kernel = Dv == sp.zeros(64, 1)
    norm2 = sp.simplify((v_round59.conjugate().T * v_round59)[0, 0])
    is_nonzero_vector = norm2 != 0

    report = {
        "applicable": True,
        "round59_own_restricted_kernel_vector_is_nonzero": bool(is_nonzero_vector),
        "round59_own_vector_D_times_v": "computed",
        "round59_own_vector_is_in_full_unrestricted_ker_D": bool(is_in_full_kernel),
        "max_abs_residual_D_times_v": float(
            max((abs(complex(x.evalf())) for x in Dv), default=0.0)
        ),
    }
    return report, (v_round59 if is_in_full_kernel and is_nonzero_vector else None)


def check_hermiticity(D: sp.Matrix, chi6_twisted: sp.Matrix) -> dict:
    """Honesty item: is D (round59's own twisted operator) actually Hermitian?
    Not needed for check4's validity (that's a direct multiplication check,
    not a Hermitian-operator deduction), but explains WHY any v in ker(D)
    combined with any w in ker(D_S3(t)) lands in ker(D_full): if D_full is
    Hermitian, ker(D_full^2)=ker(D_full) exactly, which is the structural
    reason check2 (decoupling) + individual kernels together imply check4
    (explicit product kernel) for ANY choice of v, w -- not a coincidence
    tied to one specific vector.
    """
    d_s3_lc = d_s3_matrix(sp.Rational(1, 2))
    d_full_lc = build_d_full(D, chi6_twisted, d_s3_lc)
    D_hermitian = sp.simplify(D - D.conjugate().T) == sp.zeros(64, 64)
    d_full_hermitian = sp.simplify(d_full_lc - d_full_lc.conjugate().T) == sp.zeros(128, 128)
    return {
        "D_is_hermitian": bool(D_hermitian),
        "D_full_is_hermitian_at_t_0.5": bool(d_full_hermitian),
    }


def main() -> dict:
    result: dict = {}

    mod = load_round59_module()
    E = mod.build_clifford(conj=False)
    D = mod.build_dirac(E, mod.NOMIZU)

    result["regression_check_round59_reimport"] = regression_check_round59(mod)

    chi6 = build_chi6_from_round59_E(E)
    chi6_props = check_chi6_properties(chi6, E)
    result["chi6_properties"] = chi6_props

    check1, chi6_twisted = check1_anticommutation(chi6, D)
    result["check1_anticommutation"] = check1

    result["check2_decoupling"] = {}
    for t_label, t in {
        "t=0": sp.Integer(0),
        "t=1": sp.Integer(1),
        "t=0.5_LC": sp.Rational(1, 2),
    }.items():
        result["check2_decoupling"][t_label] = check2_decoupling(D, chi6_twisted, t)

    check3, v_kernel_arbitrary = check3_kernel_of_D(D)
    result["check3_kernel_of_D"] = check3

    recon, v_round59 = reconcile_round59_vector_against_full_kernel(mod, D)
    result["reconciliation_round59_vs_full_kernel"] = recon

    result["hermiticity"] = check_hermiticity(D, chi6_twisted)

    result["check4_explicit_combined_kernel"] = {"arbitrary_kernel_vector": {}}
    if v_kernel_arbitrary is not None:
        for t_label, t in {"t=0": sp.Integer(0), "t=1": sp.Integer(1)}.items():
            result["check4_explicit_combined_kernel"]["arbitrary_kernel_vector"][t_label] = (
                check4_explicit_combined_kernel(D, chi6_twisted, v_kernel_arbitrary, t_label, t)
            )

    result["check4_explicit_combined_kernel"]["round59_own_physical_kernel_vector"] = {}
    if v_round59 is not None:
        for t_label, t in {"t=0": sp.Integer(0), "t=1": sp.Integer(1)}.items():
            result["check4_explicit_combined_kernel"]["round59_own_physical_kernel_vector"][
                t_label
            ] = check4_explicit_combined_kernel(D, chi6_twisted, v_round59, t_label, t)
    else:
        result["check4_explicit_combined_kernel"]["round59_own_physical_kernel_vector"] = {
            "skipped": "reconciliation did not confirm round59's own vector"
        }

    result["check5_full_dfull_kernel_dimension"] = {}
    dim_ker_D = check3["dim_ker_exact_sympy_nullspace"]
    for t_label, t in {
        "t=0": sp.Integer(0),
        "t=1": sp.Integer(1),
        "t=0.5_LC": sp.Rational(1, 2),
    }.items():
        result["check5_full_dfull_kernel_dimension"][t_label] = check5_full_dfull_kernel_dimension(
            D, chi6_twisted, dim_ker_D, t_label, t
        )

    # ---- Verdict ----
    # HONESTY NOTE (rewritten after an independent context-blind skeptic
    # pass; see skeptic_verdict.md). The first version of this section
    # replaced the FROZEN kill-criterion (claim.md: "Check 3 fails: direct
    # full-matrix diagonalization disagrees with round59's own claimed
    # dim ker=1" -> BLOCKED-KERNEL-MULTIPLICITY-MISMATCH) with a different,
    # unfalsifiable criterion AFTER seeing the 36-vs-1 result -- exactly the
    # post-hoc criterion-shift this project's own AOG-1 rule exists to
    # catch. The skeptic caught it. This version honors the FROZEN
    # criterion: check3 (dim_ker==1) is what claim.md pre-registered, it
    # FAILED (36!=1), so BLOCKED-KERNEL-MULTIPLICITY-MISMATCH fires,
    # co-firing with PARTIAL (claim.md's own convention allows co-firing).
    #
    # The skeptic also found checks 1, 2, 4 are algebraically FORCED given
    # {chi6,E_i}=0 (a dimension-general fact E3's own decision.md already
    # stated in prose, lines 16-20/91-93) and given Dv=0, D_S3(t)w=0 (check
    # 4 is one line of tensor algebra, needs neither check1 nor check2 nor
    # Hermiticity) -- they would pass identically for E3's own flat
    # stand-ins or any Hermitian matrix with a kernel. They are NOT
    # discriminating tests and are reported here as structural facts, not
    # as evidence for the headline claim.
    c1_ok = check1["anticommutator_is_exactly_zero"]
    c2_ok = all(v["decoupling_holds_exactly"] for v in result["check2_decoupling"].values())
    c3_matches_frozen_criterion = check3["dim_ker_matches_round59_claim_of_1"]
    c5 = result["check5_full_dfull_kernel_dimension"]
    c5_tensor_product_confirmed = all(v["matches_tensor_product_prediction"] for v in c5.values())

    verdicts_firing = []
    if not c1_ok:
        verdicts_firing.append("BLOCKED-CHIRALITY-ANTICOMMUTATION-FAILS")
    if not c3_matches_frozen_criterion:
        verdicts_firing.append("BLOCKED-KERNEL-MULTIPLICITY-MISMATCH")
    if c1_ok and c2_ok:
        verdicts_firing.append("PARTIAL-STRUCTURE-HOLDS-NO-EXPLICIT-ZERO")
    if not verdicts_firing:
        verdicts_firing.append("REAL-TWISTED-KERNEL-VERIFIED-IN-CL9-FRAMEWORK")

    result["verdict"] = {
        "check1_chirality_anticommutes": c1_ok,
        "check2_decoupling_holds": c2_ok,
        "check3_dim_ker_matches_round59_claim_of_1_FROZEN_CRITERION": c3_matches_frozen_criterion,
        "check5_ker_dfull_equals_ker_D_tensor_ker_ds3": c5_tensor_product_confirmed,
        "non_discriminating_checks_note": (
            "checks 1, 2, and 4 (all variants) are algebraically forced given "
            "the dimension-general chirality/generator anticommutation fact "
            "(E3 decision.md L16-20, L91-93) plus plain tensor algebra "
            "(Dv=0, D_S3(t)w=0 => D_full(v(x)w)=0, needs no other property) "
            "-- they would pass identically for E3's own flat Clifford-"
            "algebra stand-ins. They are reported as confirmed STRUCTURAL "
            "FACTS about this construction, not as discriminating evidence "
            "for any claim about the REAL twisted operator specifically."
        ),
        "label": " + ".join(verdicts_firing),
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = Path(__file__).parent / "results_c172.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
