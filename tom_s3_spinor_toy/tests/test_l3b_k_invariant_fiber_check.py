"""L3b tests: K=Spin(4)xSpin(4) has no invariant vector in 8_v, 8_s, or 8_c.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5, the K-equivariant Lemma B attempt.
This is a fiber-representation fact only -- it does NOT license a kernel
upper bound the way the analogous G2-singlet count did in G74A's Lemma B,
because Lemma B's Frobenius-reciprocity argument requires a symmetry acting
on the BASE S6, and K here acts only on the fiber. See the module docstring
and the spec for the full reasoning; these tests cover only the verified
fiber computation, not any (unavailable) kernel-bound conclusion.
"""

import os
import sys

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260715-l3b-k-equivariant-lemma-b-attempt"
)
_candidate_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260715-l3b-so4xso4-candidate"
)
sys.path.insert(0, _candidate_dir)
sys.path.insert(0, _exp_dir)

from k_invariant_fiber_check import (  # noqa: E402
    chirality_eigenbasis,
    k_invariant_dim_8v,
    k_invariant_dim_spinor,
)
from so4xso4_branching import GAMMA_9  # noqa: E402


def test_gamma_9_is_a_genuine_chirality_operator():
    """Sanity: Gamma_9 has 8 +1 and 8 -1 eigenvalues (splits the 16-dim Dirac spinor)."""
    import numpy as np

    evals = np.linalg.eigvalsh(GAMMA_9)
    assert sum(1 for e in evals if e > 0) == 8
    assert sum(1 for e in evals if e < 0) == 8


def test_8v_has_no_k_invariant_vector():
    """SO(4)xSO(4)'s action on the vector rep has zero invariant vectors --
    each SO(4) block's own vector rep (2,2) is nontrivial and irreducible.
    """
    assert k_invariant_dim_8v() == 0


def test_8s_has_no_k_invariant_vector():
    """Matches the branching computed earlier: no (1,1;1,1) piece in 8_s."""
    v_s, _v_c = chirality_eigenbasis()
    assert k_invariant_dim_spinor(v_s) == 0


def test_8c_has_no_k_invariant_vector():
    """Matches the branching computed earlier: no (1,1;1,1) piece in 8_c."""
    _v_s, v_c = chirality_eigenbasis()
    assert k_invariant_dim_spinor(v_c) == 0
