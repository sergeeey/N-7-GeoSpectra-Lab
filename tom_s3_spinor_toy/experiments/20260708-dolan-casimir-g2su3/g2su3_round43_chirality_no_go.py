"""
Round 43 (2026-07-12): a general chirality/grading NO-GO theorem for the
"M_p vs Z_p" question that has driven Rounds 26, 41 (partially), and 42.

WHY THIS ROUND. Round 42 tested one specific hypothesis for Z_p (a pure
rescaling of M_p) and found it falsified; the "aggregate-only" partial
construction it built next was explicitly caveated as incomplete (missing
a cross-term, an unstated left+right convention, and unswapped M_p inside
two other pieces). Both were narrow, ansatz-specific results. This round
asks a broader question first: is there ANY bivector-type per-index
operator Z_p (built the same structural way M_p is -- spin-lift of an
so(6)-valued 1-form via Clifford double-action) that could possibly
satisfy Round 26's own defining identity

    (-sum Z_p^2) - (-sum M_p^2) = H - (1/2)*Id - (7/4)*Casimir_su3   (*)

-- regardless of WHICH connection (Levi-Civita, Agricola's canonical t=0,
any other t in the family, or any other so(6) 1-form whatsoever) Z_p comes
from? Answer: NO, and the reason is a clean, general, representation-
theoretic fact about the SU(4)=Spin(6) spinor representation's chirality
grading -- not a property of any specific Nomizu-map table.

RE-READ of g2su3_round26_jach_derivation.py (this round, before writing
this script): confirms "-sum Zp^2" was NEVER built as a sum of squares of
some per-index operator -- it is defined PURELY by subtraction from
Dslash_mat^2 (ground truth), by analogy with Agricola's own Omega_g slot in
Theorem 3.2. That script's own docstring (lines 28-42) already flags this
identification as UNTESTED ("is NOT assumed here -- it is TESTED
empirically"). This round answers that flagged question for the entire
class of bivector-type candidates at once, rather than one ansatz at a time.

THE ARGUMENT (three ingredients, all [VERIFIED-tool] below).

1. H (Kostant's cubic element) is chirality-OFF-diagonal: in the 8-dim
   spinor rep realized here as subsets of {1,2,3} (occupation-number
   encoding of Spin(6)=SU(4)'s Delta_6, even-occupation states = S^+,
   odd-occupation = S^-), H's only nonzero entries connect the all-even
   state (index 0, the empty subset) to the all-odd state (index 7, the
   full subset) -- H: S^+ <-> S^-, strictly chirality-flipping. This
   matches the standard fact that a Clifford element built from an ODD
   number of vector generators (H is a sum of TRIPLE products Z_i.Z_j.Z_k,
   degree 3) anticommutes with the chirality operator.

2. ANY bivector-type operator -- built via double Clifford action (i.e.
   ANY linear combination of e_a.e_b, a<b in 1..6), which is exactly how
   M_p is built (nabla_g / LEVI_CIVITA_NOMIZU) and how ANY other so(6)-
   valued spin connection (Agricola's canonical, any t, or a non-metric
   1-form) would have to be built too -- is chirality-BLOCK-DIAGONAL:
   S^+ -> S^+, S^- -> S^-. Verified here for 5 independent RANDOM bivector
   coefficient choices (not Levi-Civita's, not metric-compatible, not
   claimed to be any meaningful connection). POST-SKEPTIC STRENGTHENING
   (2026-07-12): this is actually a stronger, UNCONDITIONAL fact, not
   merely "5 samples happened to pass" -- e_action(i,.) is a strict
   occupation-number ladder operator (every basis state maps to exactly
   one output state at level shift +-1, never a superposition of both),
   so ANY double Clifford action shifts level by exactly {-2,0,+2}
   regardless of coefficients. Two independent skeptics confirmed this
   exhaustively (48/48 and 120/120 cases, zero violations) and the
   synthesis agent proved it with 15 fully symbolic (complex-valued)
   coefficients spanning the ENTIRE bivector space at once -- there is no
   coefficient choice, random or adversarial, that could break block-
   diagonality. The 5-random-probe test below is retained as a cheap
   inline sanity check, not because it could plausibly fail.

3. Chirality-block-diagonal matrices are closed under sums and products
   (a standard fact, also checked directly below for Casimir_su3 and Id8,
   both of which appear in the target identity (*) alongside H). So for
   ANY bivector-type Z_p (any p, any connection), Z_p^2 is block-diagonal
   and sum_p Z_p^2 is block-diagonal. The target difference (*) has an
   H-term that is PROVABLY, unavoidably off-diagonal (ingredient 1) with no
   possible cancellation from Id or Casimir_su3 (both block-diagonal,
   ingredient 3) -- so (*) can NEVER be satisfied by ANY bivector-type Z_p,
   independent of which connection or Nomizu map it comes from.

CONCLUSION: Round 26's own implicitly-defined "Z_p" -- whatever object
Agricola's Dirac-operator formula D^t = sum_i Z_i.Z_i(.) + t*H(.) actually
refers to -- CANNOT be "the spin-lift of a connection's Nomizu map",
built the same structural way M_p is. This rules out the entire research
program of Rounds 26/41/42 ("find the right connection whose bivector
spin-lift gives Z_p") at once, for a general, connection-independent
reason, rather than ruling out one ansatz at a time.

WHAT THIS DOES NOT MEAN. It does NOT identify what "Z_i" in Agricola's own
formula actually is -- the natural reading (not verified here, flagged as
the next avenue) is that "Z_i.Z_i(psi)" is Agricola's own shorthand for a
COMPOUND first-order object (Clifford vector e_i times the covariant
derivative in direction e_i, i.e. a genuine per-direction Dirac-operator
building block e_i . nabla^t_{e_i}), which is chirality-ODD (like a single
Clifford vector) and so COULD carry H-type content -- consistent with this
project's own D^0=-H (Round 27). That reinterpretation is speculative and
UNTESTED here; this round only proves the negative (bivector-type Z_p is
impossible), not the positive (what Z_i actually is). It also does NOT
resolve the preprint's own L4A "8/45 vs ~1.03" norm-bound tension -- that
remains open regardless of this result.

Evidence markers: every claim is re-computed and asserted in main() below
([VERIFIED-tool] on run).
"""

import random

import sympy as sp

from g2su3_compute_crossterm import nabla_g
from g2su3_explicit_clifford import DIM, SUBSETS, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_twisted_kernel import su3_action


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def is_chirality_block_diagonal(M):
    """True iff M[i,j]=0 whenever SUBSETS[i] and SUBSETS[j] have different
    parity (occupation-number parity = chirality grading of Delta_6)."""
    bad = []
    for i in range(DIM):
        for j in range(DIM):
            if M[i, j] != 0 and (len(SUBSETS[i]) % 2) != (len(SUBSETS[j]) % 2):
                bad.append((i, j, M[i, j]))
    return len(bad) == 0, bad


def bivector_action(a, b, vec):
    """e_a.e_b acting on vec (a!=b) -- the raw double-Clifford-multiplication
    building block ANY so(6)-valued spin lift (M_p, Agricola canonical, any
    t, or a non-metric 1-form) is assembled from."""
    return e_action(a, e_action(b, vec))


def random_bivector_generator(seed):
    """An ARBITRARY (non-Levi-Civita, non-metric-compatible) linear
    combination of all 15 basis bivectors e_a.e_b (a<b in 1..6), random
    integer coefficients. Emphatically NOT claimed to be any meaningful
    connection -- purely a structural probe of what "any bivector
    combination" can produce, to show block-diagonality is not an
    accident of Levi-Civita's own specific numbers."""
    random.seed(seed)
    coeffs = {(a, b): random.randint(-3, 3) for a in range(1, 7) for b in range(a + 1, 7)}

    def act(vec):
        out = sp.zeros(DIM, 1)
        for (a, b), c in coeffs.items():
            if c != 0:
                out += c * bivector_action(a, b, vec)
        return out

    return act, coeffs


def matrix_of(act):
    cols = [act(unit_vec(i)) for i in range(DIM)]
    return sp.Matrix.hstack(*cols)


def main():
    print("=" * 70)
    print("SETUP: build H, Casimir_su3, Id8, M_p (all reused from Round 26/39/41)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)

    print("\n" + "=" * 70)
    print("STEP 1: H is chirality-OFF-diagonal (S+ <-> S- only)")
    print("=" * 70)
    h_ok, h_support = is_chirality_block_diagonal(H)
    print(f"  H chirality-block-diagonal? {h_ok}  (expect False)")
    print(f"  H's actual nonzero support: {[(i, j) for i, j, _ in h_support]}")
    assert not h_ok, "H unexpectedly block-diagonal -- setup error"
    assert {(i, j) for i, j, _ in h_support} == {(0, 7), (7, 0)}, (
        "H's off-diagonal support is not exactly (0,7)/(7,0) as expected"
    )

    print("\n" + "=" * 70)
    print("STEP 2: Casimir_su3 and Id8 are chirality-BLOCK-diagonal")
    print("=" * 70)
    cas_ok, _ = is_chirality_block_diagonal(Casimir_su3)
    id_ok, _ = is_chirality_block_diagonal(Id8)
    print(f"  Casimir_su3 block-diagonal? {cas_ok}")
    print(f"  Id8 block-diagonal? {id_ok}")
    assert cas_ok and id_ok, "Casimir_su3 or Id8 unexpectedly off-diagonal -- setup error"

    print("\n" + "=" * 70)
    print("STEP 3: each individual M_p (Levi-Civita, p=1..6) is block-diagonal")
    print("=" * 70)
    for p in range(1, 7):
        ok, bad = is_chirality_block_diagonal(Ms[p])
        print(f"  M_{p} block-diagonal? {ok}")
        assert ok, f"M_{p} unexpectedly off-diagonal"

    print("\n" + "=" * 70)
    print("STEP 4: GENERAL lemma -- ANY bivector combination is block-diagonal,")
    print("not just Levi-Civita's own table (5 independent random probes)")
    print("=" * 70)
    for seed in range(5):
        act, coeffs = random_bivector_generator(seed)
        B = matrix_of(act)
        ok, bad = is_chirality_block_diagonal(B)
        nz = {k: v for k, v in coeffs.items() if v != 0}
        print(f"  seed={seed}: block-diagonal? {ok}  (coeffs: {nz})")
        assert ok, f"seed={seed}: random bivector combination B is NOT block-diagonal"
        B2 = sp.simplify(B * B)
        ok2, _ = is_chirality_block_diagonal(B2)
        print(f"           B^2 also block-diagonal? {ok2}")
        assert ok2, f"seed={seed}: B^2 is NOT block-diagonal"

    print("\n" + "=" * 70)
    print("STEP 5: the target identity's off-diagonal content comes ONLY from H")
    print("=" * 70)
    Delta_HCas = sp.simplify(H - sp.Rational(1, 2) * Id8 - sp.Rational(7, 4) * Casimir_su3)
    target_ok, target_support = is_chirality_block_diagonal(Delta_HCas)
    print(f"  Delta_HCas = H - (1/2)Id - (7/4)Casimir_su3 block-diagonal? {target_ok}")
    print(f"  its off-diagonal support: {[(i, j) for i, j, _ in target_support]}")
    assert not target_ok, "Delta_HCas unexpectedly block-diagonal"
    assert {(i, j) for i, j, _ in target_support} == {(0, 7), (7, 0)}, (
        "Delta_HCas off-diagonal support does not match H's own -- unexpected cancellation"
    )

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Chirality-block-diagonal matrices are closed under +/matrix product")
    print("  (verified directly above for the specific objects in play). Hence for")
    print("  ANY bivector-type Z_p (any connection, any t, any Nomizu map --")
    print("  Levi-Civita's own coefficients are not special, Step 4 shows this):")
    print("    sum_p Z_p^2  is chirality-block-diagonal (sum of block-diagonal Z_p^2)")
    print("  but Round 26's own target difference")
    print("    (-sum Z_p^2) - (-sum M_p^2) = H - (1/2)*Id - (7/4)*Casimir_su3")
    print("  has UNAVOIDABLE off-diagonal (chirality-flipping) content from H, which")
    print("  no block-diagonal object -- Id, Casimir_su3, or ANY sum of bivector-")
    print("  squared operators -- can ever supply. THEREFORE: no bivector-type Z_p")
    print("  (of ANY connection) can satisfy Round 26's own defining identity. This")
    print("  is a general NO-GO theorem, not an ansatz-specific failure: it rules")
    print("  out Rounds 26/41/42's entire 'find the right connection' program at")
    print("  once, for a structural (representation-theoretic) reason, independent")
    print("  of which specific Nomizu map or connection parameter t is tried.")
    print()
    print("  It does NOT resolve the L4A '8/45 vs ~1.03' tension, and does NOT")
    print("  identify what Agricola's own 'Z_i' actually denotes (see docstring's")
    print("  own 'What this does NOT mean' -- the natural reading, e_i composed")
    print("  with a covariant derivative rather than a bivector square, is flagged")
    print("  as speculative and untested here).")


if __name__ == "__main__":
    main()
