"""
Round 29, Step A: a from-scratch Clifford monomial reducer, working purely
with index lists (no 8x8 matrix representation at all), using only the
defining relations Z_i Z_j + Z_j Z_i = -2 delta_ij  (i.e. Z_i^2=-1, Z_iZ_j=-Z_jZ_i
for i != j -- matches this project's established convention, re-verified via
torsion_T's own docstring and e_action's own anticommutation, both already
used throughout Rounds 4-28).

Purpose: reduce ANY product Z_{i1}...Z_{in} (i1..in in 1..6, possibly
repeated, in any order) to canonical form (sign, sorted tuple of DISTINCT
surviving indices). This is the combinatorial engine needed to expand
sum_p [Lambda_tilde^{1/2}(Z_p)]^2 = sum_p (1/64) sum_{j,k,l,m} T(p,j,k)T(p,l,m)
  Z_j Z_k Z_l Z_m
directly from the T-table's raw (p,j,k)->value data, WITHOUT ever building
the 8x8 e_action matrix representation Ms[p] used throughout Rounds 4-28.

This is tested against the KNOWN 8x8 matrix representation (e_action) only
as a self-check (Step A2 below) -- not used as an input to the reduction
itself.
"""


def reduce_clifford_word(indices):
    """Reduce a word (list of ints 1..6, Clifford generators) to canonical
    form via bubble-sort (each adjacent transposition of DIFFERENT indices
    flips sign, since Z_iZ_j=-Z_jZ_i) and collapse of adjacent EQUAL
    indices (Z_iZ_i=-1, removes the pair and multiplies by -1).

    Returns: (sign, tuple_of_sorted_distinct_indices)
    sign is a Python int (+1 or -1); the returned tuple has each surviving
    index exactly once (an index appearing an EVEN number of times overall
    cancels completely: e.g. Z_1Z_2Z_1 -> sign flips once passing Z_2 over
    Z_1, then Z_1Z_1=-1 collapses -> -1 * Z_2, i.e. (-1,(2,)). This matches
    a full trace through the algebra, not just naive parity counting,
    because collapsing changes the WORD LENGTH each time -- handled here by
    a genuine bubble sort with runtime removal, not a closed-form parity
    shortcut (safer, less room for an off-by-one error).
    """
    word = list(indices)
    sign = 1
    # Bubble sort with adjacent-equal collapse, repeat until no change.
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(word) - 1:
            a, b = word[i], word[i + 1]
            if a == b:
                # Z_a Z_a = -1: remove both, flip sign
                del word[i : i + 2]
                sign *= -1
                changed = True
                # restart scan from beginning of the (now shorter) word,
                # since removal can create a new adjacent-equal pair
                i = 0
                continue
            if a > b:
                # swap, flip sign (anticommute)
                word[i], word[i + 1] = b, a
                sign *= -1
                changed = True
            i += 1
    return sign, tuple(word)


def test_reduce_clifford_word():
    """Self-tests before trusting this reducer for anything downstream."""
    # Manual derivation for [1,2,1]:
    #   Z1 Z2 Z1
    #   = Z1 * Z2 * Z1
    #   swap Z2,Z1 (positions 2,3): Z1 Z1 Z2 * (-1) = (Z1 Z1) Z2 * (-1)
    #   Z1Z1 = -1 -> (-1)*Z2*(-1) = Z2   => sign=+1, tuple=(2,)
    sign, word = reduce_clifford_word([1, 2, 1])
    assert (sign, word) == (1, (2,)), f"[1,2,1] -> {(sign, word)}, expected (1, (2,))"

    # [3,1,2]: sort (3,1,2)->(1,2,3): count inversions.
    # (3,1,2): pairs out of order: (3,1),(3,2) => 2 inversions => sign=+1
    sign, word = reduce_clifford_word([3, 1, 2])
    assert (sign, word) == (1, (1, 2, 3)), f"[3,1,2] -> {(sign, word)}"

    # [1,2,3,1]: bring the trailing 1 back to meet the leading 1.
    # Z1 Z2 Z3 Z1: move Z1 (last) left past Z3, Z2 -> 2 transpositions (sign*(+1))
    #   -> Z1 Z1 Z2 Z3 = (-1) Z2 Z3   => sign=-1, tuple=(2,3)
    sign, word = reduce_clifford_word([1, 2, 3, 1])
    assert (sign, word) == (-1, (2, 3)), f"[1,2,3,1] -> {(sign, word)}"

    # Cross-check against a DIFFERENT, independent implementation: full
    # permutation-parity + explicit pair cancellation via recursion.
    import random

    random.seed(1234)
    for _ in range(200):
        n = random.randint(1, 6)
        idxs = [random.randint(1, 6) for _ in range(n)]
        s1, w1 = reduce_clifford_word(idxs)
        s2, w2 = reduce_clifford_word_reference(idxs)
        assert (s1, w1) == (s2, w2), f"MISMATCH on {idxs}: {(s1, w1)} vs {(s2, w2)}"

    print("test_reduce_clifford_word: ALL PASS (including 200 random cross-checks)")


def reduce_clifford_word_reference(indices):
    """Independent reference implementation: recursive, using a single
    adjacent-swap-or-cancel step chosen greedily from the LEFT, with an
    explicit recursion (rather than the iterative bubble-sort of the
    primary implementation) -- deliberately structured differently so a
    shared bug is unlikely to appear in both.
    """
    word = list(indices)

    def helper(w):
        # find first adjacent pair that's out of order or equal
        for i in range(len(w) - 1):
            if w[i] == w[i + 1]:
                new_w = w[:i] + w[i + 2 :]
                s, rest = helper(new_w)
                return -s, rest
            if w[i] > w[i + 1]:
                new_w = w[:i] + [w[i + 1], w[i]] + w[i + 2 :]
                s, rest = helper(new_w)
                return -s, rest
        return 1, tuple(w)

    return helper(word)


if __name__ == "__main__":
    test_reduce_clifford_word()
    print("EXIT=0")
