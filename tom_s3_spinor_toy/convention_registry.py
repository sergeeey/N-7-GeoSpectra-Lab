"""Convention / normalization registry for the project.

This module centralizes the frozen conventions used by the validated S3/S6/SU4
scaffolds and the matrix-element oracle layers. It does not promote any
physical claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


CONVENTION_FIXED: Final[str] = "CONVENTION_FIXED"
CONVENTION_REGISTRY_FIXED: Final[str] = "CONVENTION_REGISTRY_FIXED"
SOURCE_SUPPORTED_GEOMETRY: Final[str] = "SOURCE_SUPPORTED_GEOMETRY"
PARTIAL_LOW_MODE_IMPLEMENTATION: Final[str] = "PARTIAL_LOW_MODE_IMPLEMENTATION"
BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE: Final[str] = "BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE"
BASIS_ORDERING_DEPENDENT: Final[str] = "BASIS_ORDERING_DEPENDENT"
FACTOR_ORDER_DEPENDENT: Final[str] = "FACTOR_ORDER_DEPENDENT"
PHASE_CONVENTION_DEPENDENT: Final[str] = "PHASE_CONVENTION_DEPENDENT"
NORMALIZATION_DEPENDENT: Final[str] = "NORMALIZATION_DEPENDENT"
RADIUS_DEPENDENT: Final[str] = "RADIUS_DEPENDENT"
SIGNATURE_DEPENDENT: Final[str] = "SIGNATURE_DEPENDENT"
SOURCE_CONVENTION_MISMATCH: Final[str] = "SOURCE_CONVENTION_MISMATCH"
MULTIPLICITY_CONVENTION_AMBIGUOUS: Final[str] = "MULTIPLICITY_CONVENTION_AMBIGUOUS"
CONVENTION_DRIFT_DETECTED: Final[str] = "CONVENTION_DRIFT_DETECTED"
PROMOTION_BLOCKED: Final[str] = "PROMOTION_BLOCKED"
FREE_COUPLING_PARAMETER: Final[str] = "FREE_COUPLING_PARAMETER"


@dataclass(frozen=True)
class ConventionRecord:
    gate_id: str
    basis_ordering: str
    factor_order: str
    matrix_convention: str
    trace_convention: str
    generator_normalization: str
    hypercharge_normalization: str
    radius_convention: str
    signature: str
    phase_convention: str
    multiplicity_convention: str
    source_convention: str
    status: str


CONVENTION_REGISTRY: tuple[ConventionRecord, ...] = (
    ConventionRecord(
        gate_id="BEN_ACHOUR_S3_ONE_FORM_CONVENTION_EXTRACTION",
        basis_ordering="Hopf coordinates alpha, phi, theta; scalar labels (L, m_plus, m_minus)",
        factor_order="one-form basis from exact and coexact modes on S3",
        matrix_convention="source-supported geometry basis only; no V promotion",
        trace_convention="not applicable; geometric one-form basis extraction",
        generator_normalization="Ben Achour scalar/vector harmonic normalization",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the displayed Hopf chart",
        signature="Euclidean",
        phase_convention="displayed scalar phase exp(i(S phi + D theta)); sign caveat tracked",
        multiplicity_convention="scalar labels (L, m_plus, m_minus)",
        source_convention="arXiv:1505.03426 Sec. II eqs. (1)-(5); scalar and one-form extraction",
        status=SOURCE_SUPPORTED_GEOMETRY,
    ),
    ConventionRecord(
        gate_id="P13A1_BEN_ACHOUR_ONE_FORM_MODE_IMPLEMENTATION",
        basis_ordering="Hopf coordinates alpha, theta, phi; low-mode scalar labels and one-form families",
        factor_order="scalar Phi -> Killing one-forms -> B/C -> E/E' low-mode chain",
        matrix_convention="symbolic one-form mode implementation only; no physical V promotion",
        trace_convention="not applicable; differential-form normalization audit",
        generator_normalization="Ben Achour source geometry; exact one-form normalization dependent",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the source-supported Hopf chart",
        signature="Euclidean",
        phase_convention="displayed scalar phase exp(i(S phi + D theta)); source sign caveat tracked",
        multiplicity_convention="low-mode scalar families and their E/E' descendants",
        source_convention="Ben Achour scalar harmonics + Killing one-forms + low-mode B/C/E construction",
        status=BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    ),
    ConventionRecord(
        gate_id="P13A_V_OPERATOR_ANSATZ_AND_CONVENTION_REGISTRY",
        basis_ordering="frozen P9/P10 basis ordering with Ben Achour Hopf S3 geometry map",
        factor_order="S3 one-form basis × frozen spinor basis × SU4 generators",
        matrix_convention="candidate symbolic V ansatz only; no promotion",
        trace_convention="inherits P7 SU4 and P11/P12 frozen trace conventions",
        generator_normalization="SU4 T_I normalization from P7; exact coefficient normalization unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the source-supported Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity until otherwise stated",
        source_convention="Ben Achour one-form basis + P7 SU4 + P11/P12 oracle contracts",
        status=SOURCE_SUPPORTED_GEOMETRY,
    ),
    ConventionRecord(
        gate_id="P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD",
        basis_ordering="P13A1 low-mode Ben Achour geometry bridge with frozen P9/P10 basis ordering",
        factor_order="P13A1 low-mode one-form basis × frozen spinor basis × SU4 generators",
        matrix_convention="symbolic zero/nonzero pattern only; exact coefficients normalization-dependent",
        trace_convention="inherits P11/P12 frozen trace conventions",
        generator_normalization="frozen P7 / P11 / P12 normalization; exact coefficients unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the source-supported Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity for the symbolic pattern build",
        source_convention="Ben Achour low-mode E/E' + P11/P12 frozen scaffold contracts",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT",
        basis_ordering="generalized Gell-Mann order: 6 symmetric off-diagonal, 6 antisymmetric off-diagonal, 3 diagonal",
        factor_order="not applicable; algebraic generator basis only",
        matrix_convention="Hermitian generators T_a = lambda_a / 2",
        trace_convention="Tr(T_a T_b) = 1/2 delta_ab",
        generator_normalization="lambda_15 = diag(1,1,1,-3)/sqrt(6)",
        hypercharge_normalization="Y_W candidate = T_15; physical scaling not promoted",
        radius_convention="not applicable",
        signature="algebraic / not applicable",
        phase_convention="fixed by local basis contract; no silent phase flips",
        multiplicity_convention="not applicable",
        source_convention="matches local P7 gauge audit contract",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P8_S3X_S6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES",
        basis_ordering="S3 basis × S6 labels × SU4 labels, lexicographic tensor order",
        factor_order="S3 basis × S6 labels × SU4 labels",
        matrix_convention="bridge metadata only; no new operator promoted",
        trace_convention="inherited from P7 and P9 contracts",
        generator_normalization="lambda_15 normalization inherited from P7",
        hypercharge_normalization="candidate Y_W not promoted",
        radius_convention="S3 unit radius; S6 unit round normalization",
        signature="Euclidean / algebraic",
        phase_convention="frozen by P11/P12 oracle comparison",
        multiplicity_convention="per-sign multiplicity for spectrum labels",
        source_convention="matches P8 bridge contract",
        status=BASIS_ORDERING_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P9_MATRIX_ELEMENT_SELECTION_RULES",
        basis_ordering="current working selection-rule scaffold labels",
        factor_order="tensor bridge order inherited from P8",
        matrix_convention="working Hermitian V scaffold with direct Haar normalization",
        trace_convention="direct Haar / unit-coframe convention",
        generator_normalization="working reduced matrix elements",
        hypercharge_normalization="final Ben Achour E/E' basis mapping unresolved",
        radius_convention="unit S3 radius unless explicitly parameterized",
        signature="Euclidean",
        phase_convention="fixed by the working reduced-matrix-element scaffold",
        multiplicity_convention="per-sign multiplicity unless marked total",
        source_convention="matches P9 selection-rule audit contract",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION",
        basis_ordering="frozen P9/P10 basis ordering",
        factor_order="S3 basis × S6 labels × SU4 labels via frozen bridge",
        matrix_convention="Hermitianized oriented Wigner/CG coefficient matrix",
        trace_convention="inherits frozen scaffold trace conventions",
        generator_normalization="oriented Wigner-Eckart reduced factor, exact coefficients normalization-dependent",
        hypercharge_normalization="not promoted",
        radius_convention="unit radius in the tested oracle comparison",
        signature="Euclidean / representation-theory scaffold",
        phase_convention="compatible with frozen scaffold; phase-sensitive coefficients remain classified",
        multiplicity_convention="per-sign multiplicity for the tested k_max values",
        source_convention="local Wigner/CG oracle compared against frozen scaffold",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT",
        basis_ordering="tested permutations preserve the pattern up to renumbering",
        factor_order="unchanged from P11 frozen bridge",
        matrix_convention="same Hermitianized external-oracle matrix-element scaffold",
        trace_convention="unchanged from P11 frozen bridge",
        generator_normalization="normalization-dependent exact coefficients",
        hypercharge_normalization="not promoted",
        radius_convention="unit radius in tested k_max range",
        signature="Euclidean / algebraic",
        phase_convention="phase-dependent coefficients; zero/nonzero pattern stable under tested transforms",
        multiplicity_convention="per-sign multiplicity",
        source_convention="inherits P11 oracle and P10 frozen scaffold contracts",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13B1_SPINOR_STATE_AND_SELECTION_RULE_REPAIR",
        basis_ordering="repaired spinor basis through k_max=3 with scalar tuple excluded from spinor tests",
        factor_order="spinor state inspection × P11/P12 pattern comparison × selection-rule repair audit",
        matrix_convention="repair audit only; no coefficient normalization",
        trace_convention="inherits P11/P12 frozen trace conventions",
        generator_normalization="pattern-level repair only; no new coefficient scale",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="spinor state multiplicities through k_max=3",
        source_convention="P13B0 invalid-state repair + frozen P11/P12 scaffold comparison",
        status=CONVENTION_FIXED,
    ),
    ConventionRecord(
        gate_id="P13C0_TOY_GRADIENT_FORMULA_AUDIT",
        basis_ordering="repaired spinor basis with toy gradient low-mode table",
        factor_order="toy gradient profile × reduced matrix element × repaired spinor basis",
        matrix_convention="toy gradient reduced-element audit only; exact Ben Achour formula pending",
        trace_convention="inherits repaired P11/P12 frozen trace conventions",
        generator_normalization="toy low-mode table normalization; final Ben Achour formula unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13B1 repaired spinor basis + toy gradient Y_{2,0,0} audit",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13C_BEN_ACHOUR_E_MODE_FORMULA_DERIVATION",
        basis_ordering="repaired spinor basis with source-fixed low-mode Ben Achour E/E' identities",
        factor_order="Ben Achour one-form chain × repaired spinor basis × frozen P11/P12 scaffold",
        matrix_convention="exact Ben Achour E_i / E'_i source formula only; reduced coefficients remain normalization-dependent",
        trace_convention="inherits repaired P11/P12 frozen trace conventions",
        generator_normalization="source-fixed E/E' identities; operator-level reduced-element normalization unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13A ansatz + P13A1 geometry + P13B1 repaired basis + P13C0 toy-gradient audit",
        status=SOURCE_SUPPORTED_GEOMETRY,
    ),
    ConventionRecord(
        gate_id="P13D_COEFFICIENT_NORMALIZATION_AND_HERMITICITY_AUDIT",
        basis_ordering="repaired spinor basis with source-fixed Ben Achour exact formula and reduced normalization audit",
        factor_order="Ben Achour E/E' chain × reduced coefficients × gamma/Clifford × SU4 trace convention",
        matrix_convention="coefficient normalization audit only; Hermiticity preserved, exact scale unresolved",
        trace_convention="inherits P11/P12 frozen trace conventions and P7 SU4 trace convention",
        generator_normalization="source-fixed exact E/E' identities; reduced-element normalization unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12; phase sensitivity audited",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13A ansatz + P13A1 geometry + P13B1 repaired basis + P13C exact formula + P13C0 toy audit + P13C reduced audit",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13E_REDUCED_COEFFICIENT_SCALE_FIXING_OR_NO_GO",
        basis_ordering="repaired spinor basis with exact Ben Achour source identities and reduced-scale no-go audit",
        factor_order="source identities × Haar/unit-coframe × Ben Achour one-form normalization × Clifford × SU4 trace",
        matrix_convention="scale-fixing or no-go audit only; exact scale remains unresolved",
        trace_convention="inherits P11/P12 frozen trace conventions and P7 SU4 trace convention",
        generator_normalization="source-fixed exact identities; reduced coefficient scale unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13A/P13B1/P13C/P13D fixed inputs; reduced-scale no-go audit",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13F_V_OPERATOR_DERIVATION_STATUS_AND_NO_GO_RECORD",
        basis_ordering="repaired spinor basis with frozen P13A-P13E status record",
        factor_order="status record over source identities, convention stack, Hermiticity, and reduced-scale no-go",
        matrix_convention="status/no-go record only; no new physical derivation",
        trace_convention="inherits P11/P12 frozen trace conventions and P7 SU4 trace convention",
        generator_normalization="source-fixed identities; no-go on reduced coefficient scale",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13A-P13E frozen stack status record",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE",
        basis_ordering="repaired spinor basis with frozen P13A-P13F handoff status record",
        factor_order="verified claims × not-verified claims × next evidence requirement",
        matrix_convention="handoff/limitations package only; no new physical derivation",
        trace_convention="inherits P11/P12 frozen trace conventions and P7 SU4 trace convention",
        generator_normalization="source-fixed stack status; no-go on reduced coefficient scale",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase from P11/P12",
        multiplicity_convention="per-sign multiplicity in the repaired basis",
        source_convention="P13A-P13F frozen stack handoff",
        status=CONVENTION_FIXED,
    ),
    ConventionRecord(
        gate_id="P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST",
        basis_ordering="lowest repaired spinor representative with Lawrence/Hopf low-mode integral audit",
        factor_order="lowest spinor state × Ben Achour E-mode × gamma/Clifford × Lawrence/Hopf measure × coupling lambda",
        matrix_convention="one explicit S3 matrix element integral audited; exact coefficient derived, lambda remains free",
        trace_convention="unit-radius Hopf measure and source-fixed spinor-frame normalization",
        generator_normalization="exact low-mode coefficient derived but absolute coupling not fixed",
        hypercharge_normalization="not promoted",
        radius_convention="rho^3 sin(alpha) cos(alpha) Lawrence/Hopf volume factor; unit-radius special case preserved",
        signature="Euclidean",
        phase_convention="global phase invariant; allowed normalized-state phases do not change the integral",
        multiplicity_convention="single lowest repaired spinor representative",
        source_convention="P13B1 repaired basis + P13C source-fixed Ben Achour E-mode + Lawrence/Hopf measure",
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P13C_NORM_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT",
        basis_ordering="frozen P9/P10 basis ordering with reduced-element normalization audit",
        factor_order=(
            "Wigner/CG coefficient × reduced matrix element × Ben Achour one-form "
            "normalization × gamma/Clifford × SU4 generator × coupling lambda"
        ),
        matrix_convention="normalization audit only; exact coefficients remain normalization-dependent",
        trace_convention="inherits P11/P12 frozen trace conventions and P7 SU4 trace convention",
        generator_normalization="SU4 T_I fixed; final physical lambda unresolved",
        hypercharge_normalization="not promoted",
        radius_convention="unit S3 radius in the Hopf chart",
        signature="Euclidean",
        phase_convention="frozen Wigner/CG phase; phase sensitivity classified separately",
        multiplicity_convention="per-sign multiplicity until physical coupling fixes absolute scale",
        source_convention=(
            "P13A ansatz + P13A1 geometry + P13B symbolic pattern + P11/P12 "
            "scaffold + P7 normalization + reduced matrix element metadata"
        ),
        status=NORMALIZATION_DEPENDENT,
    ),
    ConventionRecord(
        gate_id="P6K_S6_SPECTRUM_COMPUTATION",
        basis_ordering="k ascending; sign (+,-); multiplicity per signed level",
        factor_order="not applicable; spectrum labels only",
        matrix_convention="homogeneous Dirac operator with Casimir cross-check target",
        trace_convention="Casimir baseline D ~ C_G + (1/8) s",
        generator_normalization="round-sphere Dirac spectrum normalization",
        hypercharge_normalization="not promoted",
        radius_convention="R = 1 unless explicitly parameterized",
        signature="Euclidean",
        phase_convention="fixed by spectral label convention",
        multiplicity_convention="per-sign multiplicity",
        source_convention="matches local round S6 Dirac spectrum contract",
        status=CONVENTION_FIXED,
    ),
)


def convention_registry_summary() -> dict[str, object]:
    """Return a summary suitable for tests and report generation."""

    return {
        "registry_status": CONVENTION_REGISTRY_FIXED,
        "physics_status": PROMOTION_BLOCKED,
        "lambda_status": FREE_COUPLING_PARAMETER,
        "runtime_status": "research_only",
        "safe_for_runtime": False,
        "selection_rules": "smoke_only",
        "promotion": "forbidden_without_separate_gate",
        "records": tuple(CONVENTION_REGISTRY),
    }


def convention_record_by_gate(gate_id: str) -> ConventionRecord:
    for record in CONVENTION_REGISTRY:
        if record.gate_id == gate_id:
            return record
    raise KeyError(gate_id)
