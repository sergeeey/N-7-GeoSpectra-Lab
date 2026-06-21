"""G72: chirality audit for triality-related bundles over S6.

The gate separates three statements that had been conflated:

1. Spin(8) triality supplies three representation labels: 8_v, 8_s, 8_c.
2. A twisted Dirac index requires actual complex bundles E_i over S6.
3. Three chiral generations require sum_i index(D_{E_i}) = 3.

On S6, H^2 = H^4 = 0 and the relevant A-hat contribution is one, so for a
complex bundle with even third Chern number:

    index(D_E) = integral ch_3(E) = c3(E) / 2.

The current triality code does not construct E_v, E_s, E_c, derive their
third Chern numbers, or prove that all three occur in one physical action.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

TARGET_INDEX = 3
REQUIRED_TOTAL_C3 = 2 * TARGET_INDEX


@dataclass(frozen=True)
class TwistBundle:
    """Minimal evidence record for a proposed twisting bundle on S6."""

    name: str
    rank: int | None
    c3: int | None
    g2_equivariant: bool | None = None
    appears_in_action: bool = False
    evidence: str = "not derived"

    def __post_init__(self) -> None:
        if self.rank is not None and self.rank <= 0:
            raise ValueError("rank must be positive when known")
        if self.c3 is not None and self.c3 % 2:
            raise ValueError("c3 must be even so that c3/2 is an integer index")


@dataclass(frozen=True)
class TrialityAssessment:
    status: str
    total_c3: int | None
    index: Fraction | None
    reason: str


def bundle_index(bundle: TwistBundle) -> Fraction | None:
    """Return the Atiyah-Singer index when c3 is known."""
    if bundle.c3 is None:
        return None
    return Fraction(bundle.c3, 2)


def total_index(bundles: Iterable[TwistBundle]) -> Fraction:
    """Add indices for a fully specified collection of twisting bundles."""
    indices = [bundle_index(bundle) for bundle in bundles]
    if any(index is None for index in indices):
        raise ValueError("all c3 values must be known before summing indices")
    return sum((index for index in indices if index is not None), Fraction(0))


def classify_triality_claim(bundles: Iterable[TwistBundle]) -> TrialityAssessment:
    """Classify whether a proposed three-channel construction supports index 3."""
    candidates = list(bundles)
    if len(candidates) != 3:
        return TrialityAssessment(
            "UNRESOLVED",
            None,
            None,
            "exactly three explicitly identified triality bundles are required",
        )
    if any(bundle.c3 is None for bundle in candidates):
        return TrialityAssessment(
            "UNRESOLVED",
            None,
            None,
            "triality labels do not determine third Chern numbers",
        )
    if any(not bundle.appears_in_action for bundle in candidates):
        return TrialityAssessment(
            "UNRESOLVED",
            None,
            None,
            "not all proposed bundles are proven to occur in one physical action",
        )

    total_c3 = sum(bundle.c3 for bundle in candidates if bundle.c3 is not None)
    index = Fraction(total_c3, 2)
    if index == TARGET_INDEX:
        return TrialityAssessment(
            "CONDITIONAL_INDEX_3",
            total_c3,
            index,
            "index 3 follows from the supplied c3 values; their triality origin remains to be derived",
        )
    if index == 0:
        return TrialityAssessment(
            "VECTORLIKE",
            total_c3,
            index,
            "the specified channel indices cancel",
        )
    return TrialityAssessment(
        "INDEX_OTHER",
        total_c3,
        index,
        "the specified bundles are chiral but do not give three net generations",
    )


# Positive control already present in G13.  The canonical almost-complex tangent
# bundle is homogeneous under the G2 action on S6 = G2/SU(3).  Its top Chern
# class equals the Euler class, whose integral is chi(S6) = 2.
CANONICAL_TANGENT_BUNDLE = TwistBundle(
    name="T^(1,0)S6",
    rank=3,
    c3=2,
    g2_equivariant=True,
    appears_in_action=False,
    evidence="G13: top Chern number equals chi(S6)=2",
)

# This explicit counterexample invalidates the unqualified local statement
# "every G2-equivariant bundle on S6 has index zero."  A narrower no-go may
# exist for a particular representation class, connection, or Dirac induction
# convention, but it must be stated and proved separately.
G30_UNIVERSAL_NO_GO_SURVIVES = bundle_index(CANONICAL_TANGENT_BUNDLE) == 0


# Current state of the triality proposal.  Representation names are known, but
# no corresponding complex twisting bundles or characteristic classes have
# been derived from the physical action.
TRIALITY_CHANNELS = [
    TwistBundle("8_v", rank=None, c3=None),
    TwistBundle("8_s", rank=None, c3=None),
    TwistBundle("8_c", rank=None, c3=None),
]


TOM_QUESTIONS = [
    (
        "Can 8_v, 8_s, and 8_c be realized as three distinct complex twisting "
        "bundles E_v, E_s, E_c over S6=G2/SU(3)?"
    ),
    "What are the third Chern numbers integral c3(E_i) and their orientation signs?",
    "Do all three bundles occur simultaneously in one S3xS6 Dirac action?",
    "Does coupling to the S3 spin connection preserve or pair their zero modes?",
]
