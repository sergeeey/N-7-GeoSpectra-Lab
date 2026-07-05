import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260705-g102-spin8-fiber-obstruction"
    / "g102_spin8_fiber.py"
)
SPEC = importlib.util.spec_from_file_location("g102_spin8_fiber", SCRIPT)
assert SPEC and SPEC.loader
G102 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G102)

DER = G102.derivation_basis()  # computed once: SVD of the 512x64 Leibniz operator
SU3 = G102.stabilizer_basis(DER)
REPS = G102.spin_rep_blocks()  # (vector, spin+, spin-) so(8) generator triples


def test_derivation_algebra_is_g2():
    """Leibniz kernel of the octonion product has dim 14 = dim g2 — no formula
    assumed, computed directly from the verified G68 multiplication table."""
    assert len(DER) == 14
    assert G102.check_leibniz(DER) < 1e-9
    assert G102.max_asymmetry(DER) < 1e-9  # Der(O) c so(8)


def test_stabilizer_is_su3():
    """Stabilizer of a point of S^6 inside Der(O) has dim 8 = dim su(3)
    (matches the coset S^6 = G2/SU(3): 14 - 6 = 8)."""
    assert len(SU3) == 8


def test_no_hidden_continuous_symmetry_beyond_g2():
    """CORE RESULT: the centralizer of g2 in so(8) is ZERO — no continuous
    fiber symmetry can coexist with the geometric G2 action on the octonion
    fiber. Path A's Spin(8) cannot be hiding inside the existing geometry."""
    dim, _ = G102.centralizer_dim(DER)
    assert dim == 0


def test_holonomy_centralizer_is_small_abelian():
    """Centralizer of the su(3) holonomy in so(8) is 2-dimensional and abelian
    (inner u(1)-type directions; triality is OUTER — these cannot permute
    the three channel labels)."""
    dim, cent = G102.centralizer_dim(SU3)
    assert dim == 2
    assert G102.is_abelian(cent)


def test_cl08_clifford_relations():
    """The doubled gammas satisfy {G_a, G_b} = -2 delta_ab on the 16-dim module."""
    assert G102.check_clifford(G102.cl8_gammas()) < 1e-12


def test_spin_rep_is_a_homomorphism():
    """Convention control: sigma([X,Y]) = [sigma(X), sigma(Y)] on random so(8)
    elements. The first run of this experiment failed exactly here (residual 9.4,
    anti-homomorphism from the +1/2 G_a G_b sign) — this test pins the fix."""
    assert G102.check_bracket_homomorphism() < 1e-9


def test_so8_distinguishes_all_three_channels():
    """Negative control for the Hom solver AND the triality statement: the three
    genuine so(8) reps (vector, spin+, spin-) are pairwise inequivalent (Hom = 0),
    while each is irreducible (Schur: Hom(X,X) = 1)."""
    vec, sp, sm = REPS
    assert G102.hom_dim(vec, sp) == 0
    assert G102.hom_dim(vec, sm) == 0
    assert G102.hom_dim(sp, sm) == 0
    assert G102.hom_dim(vec, vec) == 1
    assert G102.hom_dim(sp, sp) == 1
    assert G102.hom_dim(sm, sm) == 1


def test_g2_cannot_distinguish_any_pair():
    """Restricted to g2 (all that acts geometrically on S^6), every pair of
    channels is isomorphic: Hom_g2 = 2 for all 9 pairs (7+1 vs 7+1) —
    E-L3B's bundle-isomorphism theorem reconfirmed at the explicit so(8) level."""
    reps = G102.restrict_to_subalgebra(DER)
    for i in range(3):
        for j in range(3):
            assert G102.hom_dim(reps[i], reps[j]) == 2


def test_su3_holonomy_cannot_distinguish_any_pair():
    """Restricted to the su(3) holonomy: Hom = 6 for all 9 pairs
    (3+3bar+1+1 against itself) — the associated-bundle construction collapses
    the three channels to one and the same bundle-with-connection."""
    reps = G102.restrict_to_subalgebra(SU3)
    for i in range(3):
        for j in range(3):
            assert G102.hom_dim(reps[i], reps[j]) == 6
