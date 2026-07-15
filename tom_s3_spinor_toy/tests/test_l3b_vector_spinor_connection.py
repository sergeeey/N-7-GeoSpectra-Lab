"""L3b tests: the vector-rep and spinor-rep SO(4)xSO(4) constructions are the
same representation, connected by an explicit Cl(8)-to-Cl(8) isomorphism.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5. Corrects an earlier finding in
this same thread (commit f63b992): a degenerate Casimir spectrum for the
triality-transported so(4)_1 was read as "no invariant block split" -- but
this module shows directly (via the intertwiner + a chirality-operator
commutation test) that the H/Hl split IS preserved, consistently across the
vector representation and both spinor representations (8_s and 8_c).
"""

import os
import sys

import numpy as np

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260715-l3b-vector-spinor-connection"
)
sys.path.insert(0, _exp_dir)

from cl8_isomorphism import (  # noqa: E402
    block_sign_operator,
    build_intertwiner,
    chirality_eigenbasis,
    transported_gamma_a_on_s_minus,
    transported_gamma_a_on_s_plus,
    transported_gamma_b_on_s_minus,
    transported_gamma_b_on_s_plus,
    transported_so4xso4_generators,
)


def test_intertwiner_p_is_unique_and_exact():
    """P (8_s <-> S+) exists, is unique up to scalar (nullity=1), and satisfies
    the intertwining relation to machine precision over the FULL so(8) (28
    generators) -- not just the so(4)+so(4) subalgebra.
    """
    v_s, _v_c = chirality_eigenbasis()
    _p, residual, nullity = build_intertwiner(lambda m16: v_s.conj().T @ m16 @ v_s, "b")
    assert nullity == 1
    assert residual < 1e-10


def test_intertwiner_q_is_unique_and_exact():
    """Q (8_c <-> S-) exists, is unique up to scalar, and satisfies the
    intertwining relation to machine precision over the full so(8).
    """
    _v_s, v_c = chirality_eigenbasis()
    _q, residual, nullity = build_intertwiner(lambda m16: v_c.conj().T @ m16 @ v_c, "c")
    assert nullity == 1
    assert residual < 1e-10


def test_gamma_a_transports_to_block_sign_operator_on_s_plus():
    """Gamma_A, transported via P, is exactly D_A=diag(1,1,1,1,-1,-1,-1,-1)
    on S+ -- the spinor-level chirality operator IS the vector-level H/Hl
    block-sign operator, under the explicit isomorphism.
    """
    transported = transported_gamma_a_on_s_plus()
    d_a = block_sign_operator()
    assert np.allclose(transported.imag, 0, atol=1e-8)
    assert np.allclose(transported.real, d_a, atol=1e-6)


def test_gamma_a_transports_to_negative_block_sign_operator_on_s_minus():
    """On S-, Gamma_A transports to -D_A -- the sign flip matches Gamma_A
    distinguishing 'opposite chirality' (8_c) from 'same chirality' (8_s).
    """
    transported = transported_gamma_a_on_s_minus()
    d_a = block_sign_operator()
    assert np.allclose(transported.imag, 0, atol=1e-8)
    assert np.allclose(transported.real, -d_a, atol=1e-6)


def test_gamma_b_is_consistent_with_gamma_a_on_both_sectors():
    """Gamma_B transports to +D_A on BOTH S+ (Gamma_A=Gamma_B there, same
    chirality) and S- (Gamma_A=-Gamma_B there, so Gamma_B=+D_A while
    Gamma_A=-D_A) -- internal consistency check on the whole construction.
    """
    d_a = block_sign_operator()
    transported_b_plus = transported_gamma_b_on_s_plus()
    transported_b_minus = transported_gamma_b_on_s_minus()
    assert np.allclose(transported_b_plus.real, d_a, atol=1e-6)
    assert np.allclose(transported_b_minus.real, d_a, atol=1e-6)


def test_block_sign_operator_commutes_with_full_triality_transported_algebra():
    """D_A commutes with ALL 12 transported so(4)_1(+)so(4)_2 generators --
    the H/Hl block split IS an invariant structure of the triality-
    transported algebra, not merely a coincidental basis artifact.

    This is the corrected finding: the earlier commit (f63b992) found a
    degenerate Casimir spectrum and read it as "no split" -- but degenerate
    Casimir is also produced by two ISOTYPIC invariant blocks, which is what
    this direct commutation test confirms is actually the case.
    """
    d_a = block_sign_operator()
    generators = transported_so4xso4_generators()
    for g in generators:
        commutator = d_a @ g - g @ d_a
        assert np.max(np.abs(commutator)) < 1e-8
