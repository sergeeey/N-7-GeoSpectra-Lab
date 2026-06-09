"""P14 lambda fixing options feasibility note.

This module does not derive or fix lambda. It records a structured decision
note for plausible next-step interpretations after the S3-only no-go result.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Final, Tuple

from convention_registry import convention_registry_summary
from p13h_s3_absolute_normalization_integral_test import (
    p13h_s3_absolute_normalization_integral_test_summary,
)


P14_LAMBDA_FIXING_OPTIONS_FEASIBILITY_NOTE_STATUS: Final[str] = "passed"
LAMBDA_FREE_PARAMETER: Final[str] = "FREE_COUPLING_PARAMETER"
S3X_S6_SCALE_RADIUS_RELATION: Final[str] = "S3X_S6_SCALE_RADIUS_RELATION"
PHENOMENOLOGICAL_CALIBRATION: Final[str] = "PHENOMENOLOGICAL_CALIBRATION"
TOPOLOGICAL_CHERN_SIMONS_WINDING: Final[str] = "TOPOLOGICAL_CHERN_SIMONS_WINDING"
ACTION_PRINCIPLE_REQUIREMENT: Final[str] = "ACTION_PRINCIPLE_REQUIREMENT"
FRGE_UV_FIXED_POINT: Final[str] = "FRGE_UV_FIXED_POINT"
ML_ASSISTED_PATTERN_SEARCH: Final[str] = "ML_ASSISTED_PATTERN_SEARCH"


@dataclass(frozen=True)
class LambdaFixingOptionAssessment:
    """Structured feasibility record for one lambda-option."""

    key: str
    title: str
    required_new_assumptions: Tuple[str, ...]
    required_equations_or_missing_formalism: Tuple[str, ...]
    minimal_test: str
    failure_condition: str
    expected_cost: str
    risk_of_overfitting_or_ad_hoc_fitting: str
    lambda_effect: str
    recommended_priority: int


@dataclass(frozen=True)
class P14LambdaFixingOptionsFeasibilityNote:
    """Decision note for possible lambda-fixing / lambda-interpreting routes."""

    registry_status: str
    physics_status: str
    lambda_status: str
    p13h_status: str
    p13h_lambda_status: str
    p13h_anchor_coefficient: object
    p13h_anchor_matrix_element: object
    p13h_anchor_verdict: str
    lambda_fixed: bool
    fixed_inputs: Tuple[str, ...]
    options: Tuple[LambdaFixingOptionAssessment, ...]
    best_priority_key: str
    overall_conclusion: str
    overall_recommendation: str
    scope: str = (
        "P14 feasibility note only; ranks candidate routes for fixing or "
        "interpreting lambda after the S3-only no-go result"
    )
    fence: Tuple[str, ...] = field(
        default_factory=lambda: (
            "runtime = research_only",
            "safe_for_runtime = no",
            "selection_rules = smoke_only",
            "promotion = forbidden_without_separate_gate",
        )
    )
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "lambda fixed",
            "physical V-operator proof",
            "V-selection promotion",
            "fermion generation claim",
            "Standard Model reproduction",
        )
    )


def build_p14_lambda_fixing_options_feasibility_note() -> P14LambdaFixingOptionsFeasibilityNote:
    """Return the frozen feasibility note for lambda-fixing options."""

    registry = convention_registry_summary()
    p13h = p13h_s3_absolute_normalization_integral_test_summary()

    options = (
        LambdaFixingOptionAssessment(
            key=S3X_S6_SCALE_RADIUS_RELATION,
            title="S3×S6 scale / radius relation",
            required_new_assumptions=(
                "The effective coupling is controlled by a shared scale relation between the S3 and S6 sectors.",
                "The current tensor bridge corresponds to a physical compactification rather than a label bridge only.",
            ),
            required_equations_or_missing_formalism=(
                "An explicit reduction formula linking lambda to the S3/S6 radius ratio or total volume normalization.",
                "A normalization map between the P6K S6 conventions and the P13H S3 integral coefficient.",
            ),
            minimal_test=(
                "Derive one explicit S3×S6 scale relation from the existing bridge and check whether it reproduces "
                "the P13H low-mode coefficient without post hoc tuning."
            ),
            failure_condition=(
                "The relation is introduced after seeing the coefficient, or it requires ad hoc rescaling to fit."
            ),
            expected_cost="medium",
            risk_of_overfitting_or_ad_hoc_fitting="medium-high",
            lambda_effect="conditional_fix_candidate",
            recommended_priority=1,
        ),
        LambdaFixingOptionAssessment(
            key=ACTION_PRINCIPLE_REQUIREMENT,
            title="Action-principle requirement",
            required_new_assumptions=(
                "A variational action exists for the candidate operator stack.",
                "Lambda appears as the unique coefficient of the only symmetry-allowed invariant term.",
            ),
            required_equations_or_missing_formalism=(
                "An explicit action functional, symmetry classification, and Euler-Lagrange derivation.",
                "A normalization convention that makes the operator coefficient unambiguous.",
            ),
            minimal_test=(
                "Derive the candidate operator from an action and verify whether the coefficient is uniquely fixed "
                "by symmetry and normalization alone."
            ),
            failure_condition=(
                "Multiple invariant terms exist, or the action leaves a free overall prefactor after normalization."
            ),
            expected_cost="medium",
            risk_of_overfitting_or_ad_hoc_fitting="medium",
            lambda_effect="conditional_fix_candidate",
            recommended_priority=2,
        ),
        LambdaFixingOptionAssessment(
            key=TOPOLOGICAL_CHERN_SIMONS_WINDING,
            title="Topological / Chern-Simons / winding quantization feasibility",
            required_new_assumptions=(
                "The relevant background or coupling admits a nontrivial topological sector.",
                "Lambda enters a topological charge, winding, or quantized action term rather than a continuous deformation only.",
            ),
            required_equations_or_missing_formalism=(
                "An explicit topological functional, quantization condition, or charge formula that includes lambda.",
                "A proof that the quantization is not convention- or patch-dependent.",
            ),
            minimal_test=(
                "Show whether lambda multiplies an integer-valued topological quantity after the full normalization is fixed."
            ),
            failure_condition=(
                "Lambda stays continuously adjustable, or the purported topological invariant collapses under convention changes."
            ),
            expected_cost="high",
            risk_of_overfitting_or_ad_hoc_fitting="medium-high",
            lambda_effect="conditional_fix_candidate",
            recommended_priority=3,
        ),
        LambdaFixingOptionAssessment(
            key=FRGE_UV_FIXED_POINT,
            title="FRGE / UV fixed-point feasibility",
            required_new_assumptions=(
                "Lambda can be treated as a running effective coupling in a controlled truncation.",
                "The model is stable enough for a renormalization-group analysis with a meaningful beta function.",
            ),
            required_equations_or_missing_formalism=(
                "A beta function, truncation scheme, and fixed-point analysis for the candidate coupling.",
                "A scheme-stability check so the result is not an artifact of the chosen truncation.",
            ),
            minimal_test=(
                "Compute or borrow a minimal beta function and check whether a UV fixed point narrows or selects lambda."
            ),
            failure_condition=(
                "The flow is too scheme-dependent, or lambda remains unconstrained across admissible truncations."
            ),
            expected_cost="high",
            risk_of_overfitting_or_ad_hoc_fitting="medium-high",
            lambda_effect="conditional_fix_or_reinterpret",
            recommended_priority=4,
        ),
        LambdaFixingOptionAssessment(
            key=PHENOMENOLOGICAL_CALIBRATION,
            title="Phenomenological calibration",
            required_new_assumptions=(
                "An external observable or benchmark exists that can be used to fit lambda.",
                "The goal is calibration / interpretation rather than a microscopic derivation."
            ),
            required_equations_or_missing_formalism=(
                "A map from lambda to one observed quantity and a separate independent check quantity.",
                "A validation protocol that prevents single-point fitting from being treated as proof."
            ),
            minimal_test=(
                "Fit lambda to one observable and require at least one independent cross-check before accepting the calibration."
            ),
            failure_condition=(
                "The fit only reproduces the calibration point and does not generalize to an independent check."
            ),
            expected_cost="low",
            risk_of_overfitting_or_ad_hoc_fitting="high",
            lambda_effect="reinterpret_only",
            recommended_priority=5,
        ),
        LambdaFixingOptionAssessment(
            key=ML_ASSISTED_PATTERN_SEARCH,
            title="ML-assisted pattern search",
            required_new_assumptions=(
                "Sufficient labeled examples or symbolic features exist to search for candidate relations.",
                "The output is hypothesis generation only, not a proof or a parameter-fixing rule."
            ),
            required_equations_or_missing_formalism=(
                "A validation layer that can reject any ML-suggested relation with exact symbolic checks.",
                "A clear separation between candidate generation and mathematical verification."
            ),
            minimal_test=(
                "Use ML only to propose candidate relations and require each one to survive an exact symbolic check."
            ),
            failure_condition=(
                "The proposal collapses under exact math, or the search simply rediscoveries the already-frozen pattern."
            ),
            expected_cost="low-to-medium",
            risk_of_overfitting_or_ad_hoc_fitting="very high",
            lambda_effect="hypothesis_generation_only",
            recommended_priority=6,
        ),
    )

    overall_conclusion = (
        "No option fixes lambda on the current S3-only evidence. The most "
        "promising next route is a direct S3×S6 scale/radius relation, followed "
        "by an action-principle check. Phenomenological calibration remains a "
        "fallback reinterpretation, and ML is only for hypothesis generation."
    )
    overall_recommendation = (
        "Start with S3×S6 scale/radius relation if the goal is to constrain lambda "
        "without changing the frozen S3-only result; otherwise move to an action "
        "principle check. Do not treat calibration or ML search as physical proof."
    )

    return P14LambdaFixingOptionsFeasibilityNote(
        registry_status=str(registry["registry_status"]),
        physics_status=str(registry["physics_status"]),
        lambda_status=str(registry["lambda_status"]),
        p13h_status=str(p13h["status"]),
        p13h_lambda_status=str(p13h["lambda_status"]),
        p13h_anchor_coefficient=p13h["coefficient_symbolic"],
        p13h_anchor_matrix_element=p13h["matrix_element_symbolic"],
        p13h_anchor_verdict=str(p13h["verdict"]),
        lambda_fixed=False,
        fixed_inputs=(
            "P13A registry and ansatz freeze",
            "P13A1 Ben Achour low-mode implementation",
            "P13B symbolic pattern match",
            "P13B0 state / measure / selection repair",
            "P13B1 spinor-state repair",
            "P13C source-fixed E-mode derivation",
            "P13C_NORM reduced-coefficient normalization audit",
            "P13D coefficient normalization and Hermiticity audit",
            "P13E reduced coefficient no-go",
            "P13F no-go record",
            "P13G handoff / limitations package",
            "P13H exact low-mode integral audit",
            "Convention / Normalization Registry",
        ),
        options=options,
        best_priority_key=S3X_S6_SCALE_RADIUS_RELATION,
        overall_conclusion=overall_conclusion,
        overall_recommendation=overall_recommendation,
    )


def p14_lambda_fixing_options_feasibility_note_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and report generation."""

    note = build_p14_lambda_fixing_options_feasibility_note()
    return {
        "status": P14_LAMBDA_FIXING_OPTIONS_FEASIBILITY_NOTE_STATUS,
        "registry_status": note.registry_status,
        "physics_status": note.physics_status,
        "lambda_status": note.lambda_status,
        "p13h_status": note.p13h_status,
        "p13h_lambda_status": note.p13h_lambda_status,
        "p13h_anchor_coefficient": note.p13h_anchor_coefficient,
        "p13h_anchor_matrix_element": note.p13h_anchor_matrix_element,
        "p13h_anchor_verdict": note.p13h_anchor_verdict,
        "lambda_fixed": note.lambda_fixed,
        "fixed_inputs": note.fixed_inputs,
        "options": tuple(asdict(option) for option in note.options),
        "best_priority_key": note.best_priority_key,
        "overall_conclusion": note.overall_conclusion,
        "overall_recommendation": note.overall_recommendation,
        "scope": note.scope,
        "fence": note.fence,
        "forbidden_claims": note.forbidden_claims,
    }
