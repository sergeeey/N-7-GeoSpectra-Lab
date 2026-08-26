"""Regression coverage for c85_certification.py -- the Peter-Weyl
representation-certification module that C86, C88, C92-C102 all load
dynamically via importlib.util.spec_from_file_location (fan-in=13,
verified via grep across the repo). It has been the reused,
"certified" foundation for the entire C-series since 2026-08-12, but
had zero automated regression coverage until now (boyko-project-radar
scan finding, Chain 1).

Loaded the same way downstream experiment scripts load it (dynamic
import from its experiments/ path), matching the project's own
established convention rather than introducing a new import mechanism
as a side effect of adding tests.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest
import sympy as sp

REPO_ROOT = Path(__file__).parent.parent
C85_PATH = (
    REPO_ROOT
    / "experiments"
    / "20260812-c85-peter-weyl-representation-certification"
    / "c85_certification.py"
)


def _load_c85():
    spec = importlib.util.spec_from_file_location("c85_certification", C85_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def c85():
    return _load_c85()


def test_quaternion_relations_hold(c85) -> None:
    """i^2=j^2=k^2=-1, ij=k, ji=-k -- the algebraic foundation every
    downstream L_i/R_i generator derivation (C91-C102) assumes."""
    checks = c85.verify_quaternion_relations()
    assert checks["all_match"], checks


def test_right_mult_matrix_correctly_represents_hamilton_product(c85) -> None:
    """right_mult_matrix_on_ab already asserts complex-linearity
    internally on construction (c85_certification.py:122-124); this
    independently re-derives the SAME correctness property from
    scratch via hamilton_product directly, for a symbolic quaternion,
    so a future edit that removes/weakens the internal assert doesn't
    go unnoticed. (An earlier draft of this test only checked
    `M.shape == (2, 2)`, which passes regardless of whether M actually
    represents the right-multiplication map -- reviewer-caught,
    fixed: shape alone does not test linearity or correctness.)"""
    aw, ax, bw, bx = sp.symbols("aw ax bw bx", real=True)
    q = (aw, ax, bw, bx)
    a = aw + sp.I * ax
    b = bw + sp.I * bx
    for unit in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)):
        M = c85.right_mult_matrix_on_ab(unit)
        w, x, y, z = c85.hamilton_product(q, unit)
        expected_a = sp.expand(w + sp.I * x)
        expected_b = sp.expand(y + sp.I * z)
        got_a = sp.expand(M[0, 0] * a + M[0, 1] * b)
        got_b = sp.expand(M[1, 0] * a + M[1, 1] * b)
        assert sp.simplify(got_a - expected_a) == 0, unit
        assert sp.simplify(got_b - expected_b) == 0, unit


@pytest.mark.parametrize("k", [0, 1, 2, 3, 4])
def test_repaired_l_matrices_satisfy_su2_bracket(c85, k: int) -> None:
    """[l_{e1},l_{e2}]=2*l_{e3} (cyclic) for the REPAIRED (p-k) variant
    -- the literal (6.3)-as-printed variant is known to fail this for
    k>=2 (that's precisely why "repaired" exists); this test guards
    the variant every downstream round actually uses."""
    l1, l2, l3 = c85.build_l_matrices(k, "repaired")
    brackets = c85.bracket_residuals(l1, l2, l3)
    assert brackets["all_brackets_hold"], (k, brackets)


@pytest.mark.parametrize("k", [1, 2, 3])
def test_dbar_eigenvalues_match_meier_eq64(c85, k: int) -> None:
    """(D-bar+k)(D-bar-(k+2))=0 exactly, with eigenvalue -k at
    multiplicity k+2 and k+2 at multiplicity k (one q-copy) -- the
    exact certified spectrum every C90+ round's D_PW diagonal block
    assumes without re-deriving."""
    right_mult = [
        c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    ]
    result = c85.certify_level(k, right_mult, "repaired")
    assert result["certification_passes"], result


def test_dbar_is_not_symmetric_but_has_real_eigenvalues(c85) -> None:
    """Regression guard for the bug class that recurred 3x in this
    lineage (C86, C87, C101, per sci-code-audit's boyko-project-radar
    finding): D-bar is real-SPECTRUM but NOT symmetric/Hermitian as a
    raw matrix. Any future eigen-decomposition of D-bar (or an
    operator built from it) MUST use a general solver
    (np.linalg.eigvals), never np.linalg.eigvalsh -- eigvalsh silently
    reads only one triangle and produces wrong eigenvalues on a
    genuinely non-symmetric input. This test pins down the two facts
    that make that distinction matter, so a future "helpful" switch to
    eigvalsh gets caught immediately by CI rather than by a round's own
    P0 check three separate times."""
    l1, l2, l3 = c85.build_l_matrices(2, "repaired")
    right_mult = [
        c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    ]
    dbar = c85.build_dbar([l1, l2, l3], right_mult)

    assert dbar != dbar.T, "D-bar unexpectedly symmetric -- update this test's own premise"

    dbar_np = np.array(dbar.evalf().tolist(), dtype=complex)
    eigvals_general = np.linalg.eigvals(dbar_np)
    max_imag = float(np.max(np.abs(np.imag(eigvals_general))))
    assert max_imag < 1e-8, f"D-bar's spectrum should be real, max|Im|={max_imag}"

    # eigvalsh (Hermitian-assuming) gives a DIFFERENT, wrong answer on
    # this non-symmetric input -- demonstrated directly, not asserted.
    eigvals_wrong = np.linalg.eigvalsh(dbar_np)
    assert not np.allclose(sorted(eigvals_general.real), sorted(eigvals_wrong), atol=1e-6), (
        "eigvalsh happened to agree with eigvals here -- this test's own premise needs revisiting"
    )


def test_build_l_matrices_repaired_diagonal_is_pure_imaginary(c85) -> None:
    """l_{e1}(k)[p,p] = i*(2p-k) exactly -- the Cartan-direction
    diagonal every C99+ round's magnetic-number extraction
    (m_q, m_p := L_1/R_1 diagonal / i) depends on."""
    k = 3
    l1, _l2, _l3 = c85.build_l_matrices(k, "repaired")
    for p in range(k + 1):
        assert sp.simplify(l1[p, p] - sp.I * (2 * p - k)) == 0
