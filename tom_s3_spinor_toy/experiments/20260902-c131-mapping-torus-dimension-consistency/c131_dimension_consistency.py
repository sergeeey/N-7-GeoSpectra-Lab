"""C131 -- dimensional-consistency checks for the mapping-torus object.

This round's CENTRAL conclusion is a convention/citation question and is settled
in `decision.md` by two primary sources read this session, NOT by this script.
What this script does is verify the two *constructive* mathematical claims the
round makes on top of that conclusion, because both are cheap and both would
otherwise be `[INFERRED]`:

  PART 1  The factorisation lemma.  If `f = id_A x h` on `X = A x B`, then the
          mapping torus `M_f` is `A x M_h`.  Consequence used in decision.md:
          the mapping torus of the internal transformation, pulled back to the
          13D parent, is `M4 x S6 x M_iota` -- dimension 4+6+4 = 14 = 13+1 --
          so `M_iota` is a 4-dimensional FACTOR of the correct object, not the
          object.  Checked here on a nontrivial instance (A = S^1, B = S^1,
          h = the flip), where the lemma predicts `S^1 x Klein bottle`.

  PART 2  Kuenneth.  `H^2(M4 x S6 x M_iota; F2)` is NOT zero in general, so
          C129/C130's "the obstruction group is zero, hence everything exists
          for dimension reasons, uniformly in G" is a property of `M_iota`
          alone and does not transfer to the 14-manifold.

  PART 3  Stiefel-Whitney classes of the 14-manifold via the product formula,
          and the two Pin obstructions on it.  For `M4 = CP^2` and for
          `M4 = RP^4` the product admits NEITHER `Pin^+` NOR `Pin^-`.
          ⚠ SCOPE, corrected after the FL Step 8a skeptic passes: a probe
          admitting neither structure is simply NOT AN ELEMENT of the bordism
          group, so this is NOT "the conclusion flips" (the first draft's
          wording, withdrawn).  What it shows is that existence on the
          14-manifold is a real, probe-dependent condition rather than
          automatic -- and for SPIN probes (`S^4`, `T^4`) nothing changes.

  PART 4  Controls and injections.

Inputs taken from elsewhere, and labelled so:
  * `H^*(M_iota; F2) = (1,1,0,1,1)`, `w_1(M_iota) != 0`, `w_2(M_iota) = 0`
    -- [CITED] C129 sec.3/sec.4 (five routes, two CW models) and C130 sec.5.
    Re-derived by hand in decision.md sec.5 via the Wang sequence; NOT
    re-derived by this script.
  * Total SW classes of the sample `M4`s -- textbook.

No project code is imported.  Pure stdlib.
"""

from __future__ import annotations

import json
import os
from itertools import product as iproduct

# ---------------------------------------------------------------------------
# F2 linear algebra
# ---------------------------------------------------------------------------


def f2_rank(rows: list[list[int]]) -> int:
    """Rank over F2 of a matrix given as a list of rows."""
    mat = [r[:] for r in rows]
    if not mat or not mat[0]:
        return 0
    n_cols = len(mat[0])
    rank = 0
    pivot_row = 0
    for col in range(n_cols):
        piv = None
        for r in range(pivot_row, len(mat)):
            if mat[r][col] & 1:
                piv = r
                break
        if piv is None:
            continue
        mat[pivot_row], mat[piv] = mat[piv], mat[pivot_row]
        for r in range(len(mat)):
            if r != pivot_row and mat[r][col] & 1:
                mat[r] = [(a ^ b) for a, b in zip(mat[r], mat[pivot_row])]
        pivot_row += 1
        rank += 1
    return rank


def betti_f2(cells: list[int], bnd: dict[int, list[list[int]]]) -> list[int]:
    """F2 Betti numbers of a chain complex.

    `cells[n]` = rank of C_n.  `bnd[n]` = matrix of d_n : C_n -> C_{n-1},
    with `cells[n-1]` rows and `cells[n]` columns.  Missing => zero map.
    """
    top = len(cells) - 1
    ranks = {}
    for n in range(top + 2):
        m = bnd.get(n)
        if not m or not m[0]:
            ranks[n] = 0
        else:
            ranks[n] = f2_rank(m)
    out = []
    for n in range(top + 1):
        out.append(cells[n] - ranks[n] - ranks[n + 1])
    return out


# ---------------------------------------------------------------------------
# PART 1 -- the factorisation lemma, checked on a nontrivial instance
# ---------------------------------------------------------------------------
#
# The lemma itself is an explicit diffeomorphism, stated in decision.md sec.4:
#     M_{id_A x h}  ->  A x M_h ,   [ (a, b, t) ]  |-->  ( a, [ (b, t) ] )
# well defined because the gluing (a,b,1) ~ (a,h(b),0) does not move the A
# coordinate.  This PART checks the resulting HOMOLOGY prediction on a case
# where both sides are nontrivial and different from a product of spheres.


def mapping_torus_complex(
    cells: list[int],
    bnd: dict[int, list[list[int]]],
    fmap: dict[int, list[list[int]]],
) -> tuple[list[int], dict[int, list[list[int]]]]:
    """Chain complex of the mapping torus, over F2.

    D_n = C_n (+) C_{n-1};  d(x, y) = (d x + (f_# - id) y, - d y).
    Over F2 all signs are 1.
    """
    top = len(cells) - 1

    # WHY: the mapping torus has one more dimension than the fibre, so index
    # arithmetic must tolerate n = top + 1, where C_n itself is empty.  The
    # first draft wrote `cells[n]` unguarded and raised IndexError at n = top+1.
    def c(n: int) -> int:
        return cells[n] if 0 <= n <= top else 0

    dcells = [c(n) + c(n - 1) for n in range(top + 2)]
    dbnd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 2):
        n_rows = dcells[n - 1]
        n_cols = dcells[n]
        if n_rows == 0 or n_cols == 0:
            continue
        mat = [[0] * n_cols for _ in range(n_rows)]
        a_dim = c(n)
        b_dim = c(n - 1)
        pa_dim = c(n - 1)
        # block (1,1): d_n on the C_n summand
        m = bnd.get(n)
        if m and a_dim and pa_dim:
            for i in range(pa_dim):
                for j in range(a_dim):
                    mat[i][j] ^= m[i][j] & 1
        # block (1,2): (f_# - id) on the C_{n-1} summand, landing in C_{n-1}
        fm = fmap.get(n - 1)
        if fm and b_dim and pa_dim:
            for i in range(pa_dim):
                for j in range(b_dim):
                    delta = (fm[i][j] - (1 if i == j else 0)) & 1
                    mat[i][a_dim + j] ^= delta
        # block (2,2): d_{n-1} on the C_{n-1} summand, landing in C_{n-2}
        m2 = bnd.get(n - 1)
        pb_dim = c(n - 2)
        if m2 and b_dim and pb_dim:
            for i in range(pb_dim):
                for j in range(b_dim):
                    mat[pa_dim + i][a_dim + j] ^= m2[i][j] & 1
        dbnd[n] = mat
    return dcells, dbnd


def mapping_torus_complex_z(
    cells: list[int],
    bnd: dict[int, list[list[int]]],
    fmap: dict[int, list[list[int]]],
) -> tuple[list[int], dict[int, list[list[int]]]]:
    """Integral chain complex of the mapping torus (algebraic cone of f_# - id).

    D_n = C_n (+) C_{n-1};  d(x, y) = (dx + (f_# - id) y,  -d y).
    d^2 = 0 because f_# is a chain map, so (f-1) d = d (f-1) and the two
    cross terms cancel.

    WHY a separate integral routine: the F2 version below cannot tell T^3 from
    S^1 x Klein bottle -- both have F2 Betti (1,3,3,1).  The first draft used
    the F2 version for the negative control of PART 1 and the control could not
    fail; gate G02 caught it.  The distinguishing information is torsion.
    """
    top = len(cells) - 1

    def c(n: int) -> int:
        return cells[n] if 0 <= n <= top else 0

    dcells = [c(n) + c(n - 1) for n in range(top + 2)]
    dbnd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 2):
        n_rows, n_cols = dcells[n - 1], dcells[n]
        if n_rows == 0 or n_cols == 0:
            continue
        mat = [[0] * n_cols for _ in range(n_rows)]
        a_dim, b_dim, pa_dim, pb_dim = c(n), c(n - 1), c(n - 1), c(n - 2)
        m = bnd.get(n)
        if m and a_dim and pa_dim:
            for i in range(pa_dim):
                for j in range(a_dim):
                    mat[i][j] += m[i][j]
        fm = fmap.get(n - 1)
        if fm and b_dim and pa_dim:
            for i in range(pa_dim):
                for j in range(b_dim):
                    mat[i][a_dim + j] += fm[i][j] - (1 if i == j else 0)
        m2 = bnd.get(n - 1)
        if m2 and b_dim and pb_dim:
            for i in range(pb_dim):
                for j in range(b_dim):
                    mat[pa_dim + i][a_dim + j] -= m2[i][j]
        dbnd[n] = mat
    return dcells, dbnd


def smith_invariants(rows: list[list[int]]) -> list[int]:
    """Nonzero invariant factors (Smith normal form diagonal) of an integer matrix."""
    mat = [r[:] for r in rows]
    if not mat or not mat[0]:
        return []
    n_rows, n_cols = len(mat), len(mat[0])
    invs: list[int] = []
    t = 0
    while t < min(n_rows, n_cols):
        # find a nonzero pivot with minimal absolute value
        piv = None
        best = None
        for i in range(t, n_rows):
            for j in range(t, n_cols):
                if mat[i][j] != 0 and (best is None or abs(mat[i][j]) < best):
                    best, piv = abs(mat[i][j]), (i, j)
        if piv is None:
            break
        pi, pj = piv
        mat[t], mat[pi] = mat[pi], mat[t]
        for r in range(n_rows):
            mat[r][t], mat[r][pj] = mat[r][pj], mat[r][t]
        again = True
        while again:
            again = False
            for i in range(t + 1, n_rows):
                if mat[i][t] % mat[t][t] != 0:
                    q = mat[i][t] // mat[t][t]
                    mat[i] = [a - q * b for a, b in zip(mat[i], mat[t])]
                    mat[t], mat[i] = mat[i], mat[t]
                    again = True
            for j in range(t + 1, n_cols):
                if mat[t][j] % mat[t][t] != 0:
                    q = mat[t][j] // mat[t][t]
                    for r in range(n_rows):
                        mat[r][j] -= q * mat[r][t]
                    for r in range(n_rows):
                        mat[r][t], mat[r][j] = mat[r][j], mat[r][t]
                    again = True
        for i in range(t + 1, n_rows):
            q = mat[i][t] // mat[t][t]
            if q:
                mat[i] = [a - q * b for a, b in zip(mat[i], mat[t])]
        for j in range(t + 1, n_cols):
            q = mat[t][j] // mat[t][t]
            if q:
                for r in range(n_rows):
                    mat[r][j] -= q * mat[r][t]
        invs.append(abs(mat[t][t]))
        t += 1
    return invs


def homology_z(cells: list[int], bnd: dict[int, list[list[int]]]) -> list[str]:
    """Integral homology of a chain complex, as printable strings."""
    top = len(cells) - 1
    inv = {}
    for n in range(top + 2):
        m = bnd.get(n)
        inv[n] = smith_invariants(m) if (m and m[0]) else []
    out = []
    for n in range(top + 1):
        rank_n = len(inv[n])
        rank_n1 = len(inv[n + 1])
        free = cells[n] - rank_n - rank_n1
        tors = [d for d in inv[n + 1] if d > 1]
        parts = []
        if free > 0:
            parts.append("Z" if free == 1 else f"Z^{free}")
        parts += [f"Z/{d}" for d in tors]
        out.append(" + ".join(parts) if parts else "0")
    return out


def circle_complex() -> tuple[list[int], dict[int, list[list[int]]]]:
    """Minimal CW S^1: one 0-cell, one 1-cell, zero boundary."""
    return [1, 1], {1: [[0]]}


def torus_complex() -> tuple[list[int], dict[int, list[list[int]]]]:
    """Product CW T^2 = S^1 x S^1: cells 1, 2, 1; all boundaries zero."""
    return [1, 2, 1], {1: [[0, 0]], 2: [[0], [0]]}


def torus_id_times_flip() -> dict[int, list[list[int]]]:
    """(id x h)_# on the product CW structure of T^2, h = complex conjugation.

    Cells: e0 ; a (first circle), b (second circle) ; a*b.
    h fixes e0, sends b -> -b, hence a*b -> -(a*b), and fixes a.
    Over F2 the signs vanish, which is exactly why the F2 answer below is a
    check on the CONSTRUCTION rather than on the sign convention -- the
    integral statement is not claimed here.
    """
    return {0: [[1]], 1: [[1, 0], [0, -1]], 2: [[-1]]}


def klein_bottle_complex() -> tuple[list[int], dict[int, list[list[int]]]]:
    """Klein bottle as the mapping torus of the flip on S^1."""
    cells, bnd = circle_complex()
    fmap = {0: [[1]], 1: [[-1]]}
    return mapping_torus_complex(cells, bnd, fmap)


def tensor_complex(
    ca: list[int], ba: dict, cb: list[int], bb: dict
) -> tuple[list[int], dict[int, list[list[int]]]]:
    """Tensor product of two F2 chain complexes (Kuenneth over a field)."""
    top = (len(ca) - 1) + (len(cb) - 1)
    index: dict[int, list[tuple[int, int, int, int]]] = {n: [] for n in range(top + 1)}
    for i, ni in enumerate(ca):
        for j, nj in enumerate(cb):
            for p in range(ni):
                for q in range(nj):
                    index[i + j].append((i, p, j, q))
    cells = [len(index[n]) for n in range(top + 1)]
    pos = {n: {t: k for k, t in enumerate(index[n])} for n in range(top + 1)}
    bnd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 1):
        if cells[n] == 0 or cells[n - 1] == 0:
            continue
        mat = [[0] * cells[n] for _ in range(cells[n - 1])]
        for col, (i, p, j, q) in enumerate(index[n]):
            ma = ba.get(i)
            if ma and i - 1 >= 0 and ca[i - 1]:
                for r in range(ca[i - 1]):
                    if ma[r][p] & 1:
                        mat[pos[n - 1][(i - 1, r, j, q)]][col] ^= 1
            mb = bb.get(j)
            if mb and j - 1 >= 0 and cb[j - 1]:
                for r in range(cb[j - 1]):
                    if mb[r][q] & 1:
                        mat[pos[n - 1][(i, p, j - 1, r)]][col] ^= 1
        bnd[n] = mat
    return cells, bnd


def tensor_complex_z(
    ca: list[int], ba: dict, cb: list[int], bb: dict
) -> tuple[list[int], dict[int, list[list[int]]]]:
    """Integral tensor product of two chain complexes, with Koszul signs."""
    top = (len(ca) - 1) + (len(cb) - 1)
    index: dict[int, list[tuple[int, int, int, int]]] = {n: [] for n in range(top + 1)}
    for i, ni in enumerate(ca):
        for j, nj in enumerate(cb):
            for p in range(ni):
                for q in range(nj):
                    index[i + j].append((i, p, j, q))
    cells = [len(index[n]) for n in range(top + 1)]
    pos = {n: {t: k for k, t in enumerate(index[n])} for n in range(top + 1)}
    bnd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 1):
        if cells[n] == 0 or cells[n - 1] == 0:
            continue
        mat = [[0] * cells[n] for _ in range(cells[n - 1])]
        for col, (i, p, j, q) in enumerate(index[n]):
            ma = ba.get(i)
            if ma and i - 1 >= 0 and ca[i - 1]:
                for r in range(ca[i - 1]):
                    if ma[r][p]:
                        mat[pos[n - 1][(i - 1, r, j, q)]][col] += ma[r][p]
            mb = bb.get(j)
            if mb and j - 1 >= 0 and cb[j - 1]:
                sign = -1 if (i % 2) else 1
                for r in range(cb[j - 1]):
                    if mb[r][q]:
                        mat[pos[n - 1][(i, p, j - 1, r)]][col] += sign * mb[r][q]
        bnd[n] = mat
    return cells, bnd


def part1() -> dict:
    """Mapping torus of id_{S^1} x flip on T^2  ==?==  S^1 x Klein bottle."""
    tc, tb = torus_complex()
    lhs_cells, lhs_bnd = mapping_torus_complex(tc, tb, torus_id_times_flip())
    lhs = betti_f2(lhs_cells, lhs_bnd)
    lz_cells, lz_bnd = mapping_torus_complex_z(tc, tb, torus_id_times_flip())
    lhs_z = homology_z(lz_cells, lz_bnd)

    kc, kb = klein_bottle_complex()
    sc, sb = circle_complex()
    rc, rb = tensor_complex(sc, sb, kc, kb)
    rhs = betti_f2(rc, rb)
    kzc, kzb = mapping_torus_complex_z(*circle_complex(), {0: [[1]], 1: [[-1]]})
    rz_cells, rz_bnd = tensor_complex_z(sc, sb, kzc, kzb)
    rhs_z = homology_z(rz_cells, rz_bnd)

    # Negative control: the mapping torus of id x id is T^3, which must differ.
    ctrl_fmap = {0: [[1]], 1: [[1, 0], [0, 1]], 2: [[1]]}
    cc, cb2 = mapping_torus_complex(tc, tb, ctrl_fmap)
    ctrl = betti_f2(cc, cb2)
    cz_cells, cz_bnd = mapping_torus_complex_z(tc, tb, ctrl_fmap)
    ctrl_z = homology_z(cz_cells, cz_bnd)

    return {
        "lhs_mapping_torus_of_id_times_flip_on_T2_betti_F2": lhs,
        "rhs_S1_times_Klein_bottle_betti_F2": rhs,
        "agree_F2": lhs == rhs,
        "lhs_integral_homology": lhs_z,
        "rhs_integral_homology": rhs_z,
        "agree_Z": lhs_z == rhs_z,
        "klein_bottle_integral_homology": homology_z(kzc, kzb),
        "control_mapping_torus_of_identity_is_T3_betti_F2": ctrl,
        "control_T3_integral_homology": ctrl_z,
        "control_differs_from_lhs_over_F2_EXPECTED_FALSE": ctrl != lhs,
        "control_differs_from_lhs_over_Z": ctrl_z != lhs_z,
    }


# ---------------------------------------------------------------------------
# PART 2 -- Kuenneth for the 14-manifold
# ---------------------------------------------------------------------------

# F2 Poincare polynomials (as Betti vectors), all [CITED]/textbook.
POINCARE_F2 = {
    "S4": [1, 0, 0, 0, 1],
    "CP2": [1, 0, 1, 0, 1],
    "T4": [1, 4, 6, 4, 1],
    "K3": [1, 0, 22, 0, 1],
    "RP4": [1, 1, 1, 1, 1],
    "S6": [1, 0, 0, 0, 0, 0, 1],
    # [CITED] C129 sec.4 / C130 sec.5a -- five routes, two CW models.
    "M_iota": [1, 1, 0, 1, 1],
    "point": [1],
    # WHY the alias: PART 3 uses the key "point" for point x point x M_iota
    # (4-dimensional).  Reusing it in PART 2 for point x S6 x M_iota
    # (10-dimensional) overloaded one name onto two objects -- the very defect
    # this round records at decision.md sec.7(d).  Skeptic pass 3 caught it.
    "S6_and_M_iota_only": [1],
}


def convolve(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def part2() -> dict:
    rows = {}
    for m4 in ("S4", "CP2", "T4", "K3", "RP4", "S6_and_M_iota_only"):
        pv = convolve(
            convolve(POINCARE_F2[m4], POINCARE_F2["S6"]), POINCARE_F2["M_iota"]
        )
        rows[m4] = {
            "dim_total": len(pv) - 1,
            "betti_F2": pv,
            "dim_H2_F2": pv[2] if len(pv) > 2 else 0,
            # The Kuenneth cross term H^1(M4) (x) H^1(M_iota) on its own.  It is
            # the ONLY part of dim H^2 that the product structure contributes,
            # and gating only "dim H^2 > 0" would not test it -- skeptic pass 2
            # found that dropping it entirely still leaves every entry > 0.
            "dim_H2_without_cross_term": POINCARE_F2[m4][2]
            if len(POINCARE_F2[m4]) > 2
            else 0,
            "cross_term_contribution": POINCARE_F2[m4][1] * POINCARE_F2["M_iota"][1]
            if len(POINCARE_F2[m4]) > 1
            else 0,
        }
    return rows


# ---------------------------------------------------------------------------
# PART 3 -- Stiefel-Whitney classes of the 14-manifold, and the Pin obstructions
# ---------------------------------------------------------------------------
#
# A cohomology ring is (degrees, multiplication table) on an explicit F2 basis.
# A class is a frozenset of basis keys (F2 coefficients).


class Ring:
    def __init__(self, name: str, deg: dict, mul):
        self.name = name
        self.deg = deg
        self._mul = mul

    def mul(self, x, y):
        return self._mul(x, y)


def ring_S4() -> Ring:
    deg = {"1": 0, "v": 4}

    def mul(x, y):
        if x == "1":
            return y
        if y == "1":
            return x
        return None

    return Ring("S4", deg, mul)


def ring_CP2() -> Ring:
    deg = {"1": 0, "h": 2, "h2": 4}

    def mul(x, y):
        if x == "1":
            return y
        if y == "1":
            return x
        if x == "h" and y == "h":
            return "h2"
        return None

    return Ring("CP2", deg, mul)


def ring_RP4() -> Ring:
    deg = {f"a{k}": k for k in range(5)}
    deg["1"] = 0
    deg.pop("a0")

    def mul(x, y):
        dx = 0 if x == "1" else int(x[1:])
        dy = 0 if y == "1" else int(y[1:])
        s = dx + dy
        if s == 0:
            return "1"
        return f"a{s}" if s <= 4 else None

    return Ring("RP4", deg, mul)


def ring_T4() -> Ring:
    deg = {}
    for r in range(5):
        for s in iproduct(*[range(2)] * 4):
            if sum(s) == r:
                deg["x" + "".join(map(str, s))] = r

    def mul(x, y):
        sx = [int(c) for c in x[1:]]
        sy = [int(c) for c in y[1:]]
        if any(a & b for a, b in zip(sx, sy)):
            return None
        return "x" + "".join(str(a | b) for a, b in zip(sx, sy))

    r = Ring("T4", deg, mul)
    r.unit = "x0000"
    return r


def ring_S6() -> Ring:
    deg = {"1": 0, "s": 6}

    def mul(x, y):
        if x == "1":
            return y
        if y == "1":
            return x
        return None

    return Ring("S6", deg, mul)


def ring_point() -> Ring:
    """H^*(pt;F2) = F2 in degree 0.

    WHY this exists: the first draft reproduced C129/C130's M_iota-only verdict
    in a hand-written branch that read `TOTAL_SW["M_iota"]` back and reported
    it -- a tautology, since that tuple has no degree-2 element by
    construction.  Both skeptic passes caught it.  Substituting a point for
    BOTH other factors sends the M_iota-only case through the SAME tensor3 +
    Whitney-product machinery as every other row, so it is a reproduction
    rather than a readback.
    """
    deg = {"1": 0}

    def mul(x, y):
        return "1"

    return Ring("point", deg, mul)


def ring_M_iota_H2_nonzero_probe() -> Ring:
    """A fibre-like ring with H^2 != 0 -- used only to exercise the machinery."""
    return ring_M_iota(h2_is_zero=False)


def ring_M_iota(h2_is_zero: bool = True) -> Ring:
    """H^*(M_iota;F2) = (1,1,0,1,1), generators 1, b (deg 1), c (deg 3), d (deg 4).

    b^2 = 0 is FORCED by H^2 = 0.  `h2_is_zero=False` is the negative control:
    it adds a degree-2 class e with b^2 = e, i.e. a manifold that is NOT
    M_iota, to show the Pin verdict below is sensitive to that input.
    """
    deg = {"1": 0, "b": 1, "c": 3, "d": 4}
    if not h2_is_zero:
        deg["e"] = 2

    def mul(x, y):
        if x == "1":
            return y
        if y == "1":
            return x
        if x == "b" and y == "b":
            return None if h2_is_zero else "e"
        if {x, y} == {"b", "c"}:
            return "d"
        return None

    return Ring("M_iota", deg, mul)


def unit(r: Ring) -> str:
    return getattr(r, "unit", "1")


def tensor3(ra: Ring, rb: Ring, rc: Ring):
    """Cohomology ring of the product of three spaces (F2: no signs)."""
    deg = {}
    for x, dx in ra.deg.items():
        for y, dy in rb.deg.items():
            for z, dz in rc.deg.items():
                deg[(x, y, z)] = dx + dy + dz

    def mul(t1, t2):
        px = ra.mul(t1[0], t2[0])
        if px is None:
            return None
        py = rb.mul(t1[1], t2[1])
        if py is None:
            return None
        pz = rc.mul(t1[2], t2[2])
        if pz is None:
            return None
        return (px, py, pz)

    return Ring("prod", deg, mul)


def cmul(ring: Ring, u: frozenset, v: frozenset) -> frozenset:
    out: set = set()
    for x in u:
        for y in v:
            p = ring.mul(x, y)
            if p is not None:
                out ^= {p}
    return frozenset(out)


def graded_part(ring: Ring, cls: frozenset, k: int) -> frozenset:
    return frozenset(x for x in cls if ring.deg[x] == k)


# Total SW classes of the sample manifolds, as sets of basis keys. Textbook.
TOTAL_SW = {
    "S4": ("1",),  # parallelizable-stably-trivial: w = 1
    "CP2": ("1", "h", "h2"),  # w = (1+h)^3 = 1 + h + h^2 mod 2
    "T4": ("x0000",),  # parallelizable: w = 1
    "RP4": ("1", "a1", "a4"),  # w = (1+a)^5 = 1 + a + a^4 mod 2
    "S6": ("1",),
    "point": ("1",),
    # w_1(M_iota) = b != 0 [CITED C128 sec.6b / C129 sec.3]; w_2(M_iota) = 0
    # [CITED C129 sec.4].  Degrees >= 3 are irrelevant to w_1, w_2 of a product
    # and are omitted deliberately.
    "M_iota": ("1", "b"),
}


def pin_obstructions_on_product(
    m4_name: str, drop_cross_term: bool = False, h2_zero: bool = True
):
    rings = {
        "S4": ring_S4,
        "CP2": ring_CP2,
        "T4": ring_T4,
        "RP4": ring_RP4,
        "point": ring_point,
    }
    ra = rings[m4_name]()
    rb = ring_point() if m4_name == "point" else ring_S6()
    rc = ring_M_iota(h2_is_zero=h2_zero)
    prod = tensor3(ra, rb, rc)

    ua, ub, uc = unit(ra), unit(rb), unit(rc)
    wa = frozenset((x, ub, uc) for x in TOTAL_SW[m4_name])
    wb = frozenset(
        (ua, y, uc) for y in TOTAL_SW["S6" if m4_name != "point" else "point"]
    )
    wc = frozenset((ua, ub, z) for z in TOTAL_SW["M_iota"])

    if drop_cross_term:
        # INJECTION: keep only the "diagonal" terms of w(A)w(B)w(C), i.e. drop
        # every genuine cross term but keep the unit exactly once.  This is the
        # corruption that would make the transfer look automatic.
        # WHY the explicit unit handling: the first draft wrote
        #   `w ^= frozenset({(ua,ub,uc)}) if len({wa,wb,wc}) else frozenset()`
        # whose condition is a set of three frozensets and therefore ALWAYS
        # truthy -- a dead conditional, and it subtracted one unit where three
        # factors need two.  Skeptic pass 2 caught it.  Rebuilt explicitly.
        one = frozenset({(ua, ub, uc)})
        w = one
        for s in (wa, wb, wc):
            w ^= s - one
    else:
        w = cmul(prod, cmul(prod, wa, wb), wc)

    w1 = graded_part(prod, w, 1)
    w2 = graded_part(prod, w, 2)
    w1sq = cmul(prod, w1, w1)
    pin_plus_obstruction = w2
    pin_minus_obstruction = frozenset(w2 ^ w1sq)
    return {
        "w1": sorted("*".join(t) for t in w1),
        "w2": sorted("*".join(t) for t in w2),
        "w1_squared": sorted("*".join(t) for t in w1sq),
        "pin_plus_obstruction_w2": sorted("*".join(t) for t in pin_plus_obstruction),
        "pin_minus_obstruction_w2_plus_w1sq": sorted(
            "*".join(t) for t in pin_minus_obstruction
        ),
        "Pin_plus_exists": len(pin_plus_obstruction) == 0,
        "Pin_minus_exists": len(pin_minus_obstruction) == 0,
        "non_orientable": len(w1) > 0,
    }


def part3() -> dict:
    out = {}
    for name in ("S4", "CP2", "T4", "RP4"):
        out[name] = pin_obstructions_on_product(name)
    # The M_iota-only case, i.e. what C129/C130 actually computed.  Run through
    # the SAME tensor3 + Whitney machinery with a point in both other slots, so
    # this is a reproduction, not a readback of TOTAL_SW["M_iota"] (which is
    # what the first draft did -- both skeptic passes caught it).
    out["M_iota_alone_C129_C130_case"] = pin_obstructions_on_product("point")
    return out


# ---------------------------------------------------------------------------
# PART 4 -- injections
# ---------------------------------------------------------------------------


def part4() -> dict:
    inj = {}
    # Injection 1: drop the Kuenneth cross term in the SW product formula.
    inj["drop_cross_term_RP4"] = pin_obstructions_on_product(
        "RP4", drop_cross_term=True
    )
    inj["drop_cross_term_RP4_moves_headline"] = (
        inj["drop_cross_term_RP4"]["Pin_plus_exists"]
        != pin_obstructions_on_product("RP4")["Pin_plus_exists"]
    )
    # Injection 2: give M_iota a nonzero H^2 (b^2 = e).  Then w_1^2 != 0 and
    # the Pin^- verdict must move even for a spin M4.
    inj["M_iota_with_nonzero_H2_S4"] = pin_obstructions_on_product("S4", h2_zero=False)
    inj["M_iota_with_nonzero_H2_moves_headline"] = (
        inj["M_iota_with_nonzero_H2_S4"]["Pin_minus_exists"]
        != pin_obstructions_on_product("S4")["Pin_minus_exists"]
    )
    # Injection 3 (skeptic pass 2, finding 12): drop the Kuenneth cross term in
    # PART 2.  The first draft's G07 ("all > 0") could not see this.
    p2 = part2()
    inj["kunneth_cross_term_dropped"] = {
        m: p2[m]["dim_H2_without_cross_term"] for m in ("S4", "CP2", "T4", "K3", "RP4")
    }
    inj["kunneth_cross_term_changes_T4_and_RP4"] = (
        p2["T4"]["dim_H2_F2"] != p2["T4"]["dim_H2_without_cross_term"]
        and p2["RP4"]["dim_H2_F2"] != p2["RP4"]["dim_H2_without_cross_term"]
    )
    # Injection 4 (skeptic pass 2, finding 11): the F2 mapping-torus monodromy
    # block was never exercised -- every self-map of S^3 has deg = +-1 == 1
    # (mod 2), so (f_# - id) vanishes mod 2 identically.  Exercise it with a
    # degree-2 map, where it does not.  This is a check on the ROUTINE, not on
    # any manifold: the mapping torus of a degree-2 map of S^3 is not a manifold.
    sc, sb = [1, 0, 0, 1], {}
    deg2 = {0: [[1]], 3: [[2]]}
    c2, b2 = mapping_torus_complex(sc, sb, deg2)
    inj["F2_monodromy_block_exercised_deg2"] = betti_f2(c2, b2)
    c1, b1 = mapping_torus_complex(sc, sb, {0: [[1]], 3: [[1]]})
    inj["F2_monodromy_block_deg1_control"] = betti_f2(c1, b1)
    inj["F2_monodromy_block_discriminates"] = (
        inj["F2_monodromy_block_exercised_deg2"]
        != inj["F2_monodromy_block_deg1_control"]
    )
    return inj


# ---------------------------------------------------------------------------


def main() -> None:
    p1 = part1()
    p2 = part2()
    p3 = part3()
    p4 = part4()

    gates: dict[str, bool] = {}
    gates["G01_factorisation_lemma_homology_agrees_F2_AND_Z"] = (
        p1["agree_F2"] and p1["agree_Z"]
    )
    # WHY integral: over F2 the control CANNOT fail -- T^3 and S^1 x Klein have
    # the same F2 Betti vector (1,3,3,1).  The first draft gated on the F2
    # version and G02 fired.  Recorded in decision.md sec.9 rather than
    # silently swapped.
    gates["G02_factorisation_control_T3_differs_over_Z"] = p1[
        "control_differs_from_lhs_over_Z"
    ]
    gates["G02b_control_provably_CANNOT_differ_over_F2"] = not p1[
        "control_differs_from_lhs_over_F2_EXPECTED_FALSE"
    ]
    gates["G02c_klein_bottle_torsion_reproduced"] = p1[
        "klein_bottle_integral_homology"
    ] == [
        "Z",
        "Z + Z/2",
        "0",
    ]
    gates["G03_product_is_14_dimensional"] = all(
        p2[m]["dim_total"] == 14 for m in ("S4", "CP2", "T4", "K3", "RP4")
    )
    gates["G04_14_equals_13_plus_1"] = (4 + 6 + 4) == 14 and 14 == 13 + 1
    gates["G05_M_iota_alone_is_4_dimensional"] = (
        p2["S6_and_M_iota_only"]["dim_total"] == 10 and (len(POINCARE_F2["M_iota"]) - 1) == 4
    )
    gates["G06_H2_of_product_vanishes_for_S4"] = p2["S4"]["dim_H2_F2"] == 0
    gates["G07_H2_of_product_NONZERO_for_CP2_T4_K3_RP4"] = all(
        p2[m]["dim_H2_F2"] > 0 for m in ("CP2", "T4", "K3", "RP4")
    )
    gates["G08_M_iota_alone_reproduces_C129_both_Pin_exist"] = (
        p3["M_iota_alone_C129_C130_case"]["Pin_plus_exists"]
        and p3["M_iota_alone_C129_C130_case"]["Pin_minus_exists"]
        and p3["M_iota_alone_C129_C130_case"]["non_orientable"]
    )
    gates["G09_product_with_CP2_admits_NEITHER_Pin"] = (
        not p3["CP2"]["Pin_plus_exists"] and not p3["CP2"]["Pin_minus_exists"]
    )
    gates["G10_product_with_RP4_admits_NEITHER_Pin"] = (
        not p3["RP4"]["Pin_plus_exists"] and not p3["RP4"]["Pin_minus_exists"]
    )
    gates["G11_product_with_spin_M4_still_admits_BOTH"] = (
        p3["S4"]["Pin_plus_exists"]
        and p3["S4"]["Pin_minus_exists"]
        and p3["T4"]["Pin_plus_exists"]
        and p3["T4"]["Pin_minus_exists"]
    )
    gates["G12_product_is_non_orientable_for_every_orientable_M4"] = all(
        p3[m]["non_orientable"] for m in ("S4", "CP2", "T4")
    )
    gates["G13_injection_drop_cross_term_moves_headline"] = p4[
        "drop_cross_term_RP4_moves_headline"
    ]
    gates["G14_injection_nonzero_H2_moves_headline"] = p4[
        "M_iota_with_nonzero_H2_moves_headline"
    ]
    # --- gates added after the two FL Step 8a skeptic passes -------------------
    # G15: the two encodings of H^2(M_iota;F2) = 0 were independent and could
    # drift apart (skeptic pass 1, finding 10).  Link them.
    gates["G15_two_encodings_of_H2_M_iota_agree"] = (POINCARE_F2["M_iota"][2] == 0) == (
        2 not in ring_M_iota().deg.values()
    )
    # G16: gate the EXACT H^2 dimensions, not merely "> 0" -- only these read
    # the Kuenneth cross term (skeptic pass 2, finding 12).
    gates["G16_exact_H2_dims_include_the_cross_term"] = [
        p2[m]["dim_H2_F2"] for m in ("S4", "CP2", "T4", "K3", "RP4")
    ] == [0, 1, 10, 22, 2]
    gates["G17_cross_term_is_load_bearing_for_T4_and_RP4"] = p4[
        "kunneth_cross_term_changes_T4_and_RP4"
    ]
    # G18: the F2 monodromy block is now actually exercised (skeptic pass 2, 11).
    gates["G18_F2_monodromy_block_discriminates_on_deg2"] = p4[
        "F2_monodromy_block_discriminates"
    ]
    # G19 (skeptic pass 3, finding 9): w_2(M_iota) = 0 is encoded a THIRD time in
    # TOTAL_SW["M_iota"], which G15 did not cover.  Link it to the other two.
    gates["G19_third_encoding_of_w2_M_iota_agrees"] = (
        all(ring_M_iota().deg[k] != 2 for k in TOTAL_SW["M_iota"])
        and POINCARE_F2["M_iota"][2] == 0
    )

    verdict_inputs = {
        "M_iota_is_a_4_dimensional_FACTOR_of_a_14_dimensional_object": gates[
            "G01_factorisation_lemma_homology_agrees_F2_AND_Z"
        ]
        and gates["G03_product_is_14_dimensional"]
        and gates["G04_14_equals_13_plus_1"],
        "H2_vanishing_does_NOT_transfer_to_the_14_manifold": gates[
            "G07_H2_of_product_NONZERO_for_CP2_T4_K3_RP4"
        ],
        "PIN_EXISTENCE_ON_14_MANIFOLD_IS_PROBE_DEPENDENT_NOT_AUTOMATIC": gates[
            "G09_product_with_CP2_admits_NEITHER_Pin"
        ]
        and gates["G10_product_with_RP4_admits_NEITHER_Pin"],
        "non_orientability_DOES_transfer_so_C128_6b_survives": gates[
            "G12_product_is_non_orientable_for_every_orientable_M4"
        ],
    }

    n_ok = sum(1 for v in gates.values() if v)
    result = {
        "PART1_factorisation_lemma": p1,
        "PART2_kunneth_betti": p2,
        "PART3_pin_obstructions": p3,
        "PART4_injections": p4,
        "GATES": gates,
        "GATES_PASSED": f"{n_ok} / {len(gates)}",
        "ALL_OK": n_ok == len(gates),
        "VERDICT_INPUTS": verdict_inputs,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "results_c131.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)

    for k, v in gates.items():
        print(f"{'PASS' if v else 'FAIL'}  {k}")
    print(f"\nGATES: {n_ok} / {len(gates)}   ALL_OK = {n_ok == len(gates)}")
    print("\nVERDICT_INPUTS:")
    for k, v in verdict_inputs.items():
        print(f"  {k}: {v}")
    print("\nH^2(M4 x S6 x M_iota; F2) dimension by choice of M4:")
    for m in ("S4", "CP2", "T4", "K3", "RP4"):
        print(
            f"  M4 = {m:5s}  dim H^2 = {p2[m]['dim_H2_F2']:3d}   (total dim {p2[m]['dim_total']})"
        )
    print("\nPin verdicts on the 14-manifold:")
    for m in ("S4", "CP2", "T4", "RP4"):
        r = p3[m]
        print(
            f"  M4 = {m:5s}  Pin+ {r['Pin_plus_exists']!s:5s}  "
            f"Pin- {r['Pin_minus_exists']!s:5s}  w2 = {r['w2']}"
        )
    r = p3["M_iota_alone_C129_C130_case"]
    print(
        f"  M_iota alone  Pin+ {r['Pin_plus_exists']}  Pin- {r['Pin_minus_exists']}  (C129/C130)"
    )


if __name__ == "__main__":
    main()
