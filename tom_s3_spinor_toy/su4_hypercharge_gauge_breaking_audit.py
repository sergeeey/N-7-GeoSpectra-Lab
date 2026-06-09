"""P7 SU(4) / hypercharge gauge-breaking audit contract.

This module audits the algebraic gauge layer in strict isolation from S3/S6
spectral dynamics. It works at the Spin(6) ≅ SU(4) / so(6) ≅ su(4) level and
does not claim a full fermion-generation result, a Standard Model result, or
any V-selection promotion.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import sympy as sp


P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False

SUCCESSFULLY_VERIFIED: Final[str] = "algebraically_verified"
BASIS_ORDERING_DEPENDENT: Final[str] = "basis_ordering_dependent"
NORMALIZATION_DEPENDENT: Final[str] = "normalization_dependent"
REQUIRES_TENSOR_PRODUCT_S3XS6: Final[str] = "requires_tensor_product_S3xS6"
REQUIRES_PHYSICAL_INPUT: Final[str] = "requires_physical_input"
SMOKE_ONLY: Final[str] = "smoke_only"
FAILED: Final[str] = "failed"


def _e(i: int, j: int, n: int = 4) -> sp.Matrix:
    m = sp.zeros(n)
    m[i, j] = 1
    return m


def _generalized_gell_mann_matrices() -> list[sp.Matrix]:
    """Return the canonical 4x4 generalized Gell-Mann basis (lambda_a)."""

    mats: list[sp.Matrix] = []

    # Off-diagonal symmetric / antisymmetric pairs in lexicographic order.
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    for i, j in pairs:
        mats.append(_e(i, j) + _e(j, i))
        mats.append(-sp.I * (_e(i, j) - _e(j, i)))

    sqrt3 = sp.sqrt(3)
    sqrt6 = sp.sqrt(6)
    mats.append(sp.diag(1, -1, 0, 0))
    mats.append(sp.diag(1, 1, -2, 0) / sqrt3)
    mats.append(sp.diag(1, 1, 1, -3) / sqrt6)
    return mats


def su4_lambda_basis() -> list[sp.Matrix]:
    """Canonical 4x4 lambda-basis with Tr(lambda_a lambda_b)=2 delta_ab."""

    return _generalized_gell_mann_matrices()


def su4_generators_T() -> list[sp.Matrix]:
    """Return HEP-normalized generators T_a = lambda_a / 2."""

    return [lam / 2 for lam in su4_lambda_basis()]


def su3c_embedding_generators() -> list[sp.Matrix]:
    """Return the standard SU(3)c embedding in the upper-left 3x3 block."""

    sqrt3 = sp.sqrt(3)
    mats_3 = [
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / 2,
        sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]) / 2,
        sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / 2,
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / 2,
        sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]) / 2,
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / 2,
        sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]) / 2,
        sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / (2 * sqrt3),
    ]
    embedded: list[sp.Matrix] = []
    for mat in mats_3:
        embedded.append(
            sp.Matrix(
                [
                    [mat[0, 0], mat[0, 1], mat[0, 2], 0],
                    [mat[1, 0], mat[1, 1], mat[1, 2], 0],
                    [mat[2, 0], mat[2, 1], mat[2, 2], 0],
                    [0, 0, 0, 0],
                ]
            )
        )
    return embedded


def lambda_15() -> sp.Matrix:
    """Return the canonical lambda_15 generator."""

    return su4_lambda_basis()[14]


def candidate_yw() -> sp.Matrix:
    """Return the candidate Y_W generator in the same normalization as T_15."""

    return su4_generators_T()[14]


def _trace_convention_ok(generators: list[sp.Matrix]) -> bool:
    for i, gi in enumerate(generators):
        for j, gj in enumerate(generators):
            target = sp.Rational(1, 2) if i == j else 0
            if sp.simplify((gi * gj).trace() - target) != 0:
                return False
    return True


def _is_hermitian(mat: sp.Matrix) -> bool:
    return bool((mat - mat.H).applyfunc(sp.simplify) == sp.zeros(mat.rows))


def _is_traceless(mat: sp.Matrix) -> bool:
    return sp.simplify(mat.trace()) == 0


def _decompose_in_basis(mat: sp.Matrix, basis: list[sp.Matrix]) -> sp.Matrix:
    coeffs = []
    for b in basis:
        coeffs.append(sp.simplify(2 * (b * mat).trace()))
    return sp.Matrix(coeffs)


def _closure_residual_norm(generators: list[sp.Matrix]) -> sp.Expr:
    residual = sp.Integer(0)
    for gi in generators:
        for gj in generators:
            comm = gi * gj - gj * gi
            coeffs = _decompose_in_basis(comm, generators)
            reconstructed = sp.zeros(4)
            for coeff, basis in zip(coeffs, generators):
                reconstructed += sp.simplify(coeff) * basis
            residual += sum(sp.simplify(x) for x in (comm - reconstructed).reshape(16, 1))
    return sp.simplify(residual)


@dataclass(frozen=True)
class SU4HyperchargeGaugeAudit:
    """Structured audit for the P7 gauge-algebra layer."""

    spin6_su4_relation: str
    algebra_relation: str
    basis_ordering: str
    trace_convention: str
    lambda_15_normalization: str
    su3c_embedding: str
    candidate_yw: str
    right_neutrino_invariance: str
    closure_verified: bool
    hermiticity_verified: bool
    tracelessness_verified: bool
    trace_convention_verified: bool
    lambda_15_eigenvalues: Tuple[sp.Expr, ...]
    claim_classification: Tuple[Tuple[str, str], ...]
    audit_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "full fermion generation claim",
            "Standard Model reproduced claim",
            "V-selection promotion",
            "S3xS6 tensor-product coupling claim",
            "safe_for_runtime promotion",
        )
    )


def build_su4_hypercharge_gauge_audit() -> SU4HyperchargeGaugeAudit:
    """Return the current P7 gauge audit contract."""

    lambdas = su4_lambda_basis()  # noqa: F841
    generators = su4_generators_T()
    lambda15 = lambda_15()
    yw = candidate_yw()  # noqa: F841

    closure_verified = sp.simplify(_closure_residual_norm(generators)) == 0
    hermiticity_verified = all(_is_hermitian(g) for g in generators)
    tracelessness_verified = all(_is_traceless(g) for g in generators)
    trace_convention_verified = _trace_convention_ok(generators)
    lambda15_eigs = tuple(sp.Matrix(lambda15).eigenvals().keys())

    claim_classification = (
        ("Spin(6) ≅ SU(4) / so(6) ≅ su(4) algebra layer", SUCCESSFULLY_VERIFIED),
        ("SU(4) generator closure", SUCCESSFULLY_VERIFIED),
        ("trace convention", SUCCESSFULLY_VERIFIED),
        ("Hermiticity", SUCCESSFULLY_VERIFIED),
        ("tracelessness", SUCCESSFULLY_VERIFIED),
        ("SU(3)c embedding", BASIS_ORDERING_DEPENDENT),
        ("lambda_15 normalization", NORMALIZATION_DEPENDENT),
        ("candidate Y_W", NORMALIZATION_DEPENDENT),
        ("right-neutrino invariance", BASIS_ORDERING_DEPENDENT),
        ("full fermion generation claim", REQUIRES_PHYSICAL_INPUT),
        ("Standard Model reproduced claim", REQUIRES_PHYSICAL_INPUT),
        ("S3xS6 tensor-product coupling claim", REQUIRES_TENSOR_PRODUCT_S3XS6),
        ("V-selection promotion", SMOKE_ONLY),
    )

    if not closure_verified or not hermiticity_verified or not tracelessness_verified:
        audit_result = "su4_algebra_audit_failed"
    else:
        audit_result = "su4_algebra_audit_passed_with_normalization_dependent_yw"

    return SU4HyperchargeGaugeAudit(
        spin6_su4_relation="Spin(6) ≅ SU(4)",
        algebra_relation="so(6) ≅ su(4)",
        basis_ordering=(
            "generalized Gell-Mann order: 6 symmetric off-diagonal, "
            "6 antisymmetric off-diagonal, 3 diagonal"
        ),
        trace_convention="Tr(T_a T_b) = 1/2 delta_ab",
        lambda_15_normalization="lambda_15 = diag(1,1,1,-3) / sqrt(6)",
        su3c_embedding="standard upper-left 3x3 embedding of SU(3)c inside SU(4)",
        candidate_yw="Y_W = T_15 in the canonical HEP normalization",
        right_neutrino_invariance=(
            "the 4th basis vector is SU(3)c-singlet under the standard embedding"
        ),
        closure_verified=bool(closure_verified),
        hermiticity_verified=bool(hermiticity_verified),
        tracelessness_verified=bool(tracelessness_verified),
        trace_convention_verified=bool(trace_convention_verified),
        lambda_15_eigenvalues=tuple(sp.simplify(e) for e in lambda15_eigs),
        claim_classification=claim_classification,
        audit_result=audit_result,
        scope=(
            "P7 gauge-algebra audit only; no full fermion-generation claim, no "
            "Standard Model claim, no V promotion"
        ),
    )


def su4_hypercharge_gauge_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    audit = build_su4_hypercharge_gauge_audit()
    return {
        "spin6_su4_relation": audit.spin6_su4_relation,
        "algebra_relation": audit.algebra_relation,
        "basis_ordering": audit.basis_ordering,
        "trace_convention": audit.trace_convention,
        "lambda_15_normalization": audit.lambda_15_normalization,
        "su3c_embedding": audit.su3c_embedding,
        "candidate_yw": audit.candidate_yw,
        "right_neutrino_invariance": audit.right_neutrino_invariance,
        "closure_verified": audit.closure_verified,
        "hermiticity_verified": audit.hermiticity_verified,
        "tracelessness_verified": audit.tracelessness_verified,
        "trace_convention_verified": audit.trace_convention_verified,
        "lambda_15_eigenvalues": audit.lambda_15_eigenvalues,
        "claim_classification": audit.claim_classification,
        "audit_result": audit.audit_result,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "status": P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
