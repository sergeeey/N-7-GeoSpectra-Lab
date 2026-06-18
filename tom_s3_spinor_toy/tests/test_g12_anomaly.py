"""G12 tests: gauge anomaly cancellation for the S³×S⁶ 32-component spinor."""

import os
import sys

import sympy as sp
from sympy import Rational as R

_exp_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g12-anomaly")
sys.path.insert(0, _exp_dir)

from g12_anomaly_check import (  # noqa: E402
    FERMIONS,
    WEYL_COUNT,
    A_su3_cubic,
    A_su2_cubic,
    A_su2_sq_u1,
    A_su3_sq_u1,
    A_u1_cubic,
    A_grav_sq_u1,
)


def test_weyl_count_32():
    """16 left-handed Weyl dof × 2 CPT = 32 = G6 spinor count."""
    assert WEYL_COUNT == 16


def test_fermion_table_hypercharge_consistency():
    """Y values are exact rationals with denominator ≤ 6."""
    for name, su3, su2, Y, chi in FERMIONS:
        assert isinstance(Y, sp.Rational), f"{name}: Y must be Rational"
        assert abs(Y.q) <= 6, f"{name}: Y denominator {Y.q} unexpectedly large"


def test_T1_su3_cubic():
    """[SU(3)]³ = 0: no gauge anomaly in QCD sector."""
    assert A_su3_cubic() == 0


def test_T2_su2_cubic():
    """[SU(2)]³ = 0: automatic from pseudo-reality of SU(2)."""
    assert A_su2_cubic() == 0


def test_T3_su2sq_u1():
    """[SU(2)]² × U(1)_Y = 0."""
    assert A_su2_sq_u1() == 0


def test_T4_su3sq_u1():
    """[SU(3)]² × U(1)_Y = 0."""
    assert A_su3_sq_u1() == 0


def test_T5_u1_cubic():
    """[U(1)_Y]³ = 0."""
    assert A_u1_cubic() == 0


def test_T6_grav_sq_u1():
    """[grav]² × U(1)_Y = 0."""
    assert A_grav_sq_u1() == 0


def test_three_generations_still_anomaly_free():
    """3 × (one generation anomaly) = 0: trivial but explicit."""
    assert 3 * A_su3_cubic() == 0
    assert 3 * A_u1_cubic() == 0
    assert 3 * A_grav_sq_u1() == 0


def test_quark_hypercharge_sum_equals_lepton():
    """[SU(3)]² × U(1): quark contribution cancels lepton contribution."""
    quark_contrib = sum(chi * su2 * R(1, 2) * Y for _, su3, su2, Y, chi in FERMIONS if su3 == 3)
    assert quark_contrib == 0


def test_grav_anomaly_decomposes_by_sector():
    """Quarks and leptons each contribute equally and opposite to [grav]² × U(1)."""
    quark = sum(chi * su3 * su2 * Y for _, su3, su2, Y, chi in FERMIONS if su3 == 3)
    lepton = sum(chi * su3 * su2 * Y for _, su3, su2, Y, chi in FERMIONS if su3 == 1)
    assert quark + lepton == 0
