"""Smoke tests for the S6 / G2 / SU(3) formula-spec contract."""

from __future__ import annotations

from s6_g2_su3_formula_spec import s6_formula_spec, s6_formula_spec_metadata


def test_s6_formula_spec_has_the_expected_identity_and_baseline() -> None:
    """The S6 track starts from the homogeneous-space identity and Casimir baseline."""

    spec = s6_formula_spec()
    assert spec.identity == "S6 ≅ G2 / SU(3)"
    assert spec.reductive_split == "g2 = su(3) ⊕ m"
    assert spec.dirac_baseline == "D ~ C_G + (1/8) s"
    assert "formula spec only" in spec.scope


def test_s6_formula_spec_remains_separate_from_s3_and_su4() -> None:
    """The S6 contract is intentionally a separate track."""

    metadata = s6_formula_spec_metadata()

    assert metadata["scope"] == "S6 formula spec only; no implementation or spectrum claim"
    assert metadata["metric_normalization"] == "undecided"
    assert metadata["connection_choice"] == "undecided"
    assert metadata["spinor_bundle_convention"] == "undecided"
    assert metadata["selection_rules_status"] == "not started"

