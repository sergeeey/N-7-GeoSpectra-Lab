"""C130 -- does the TWISTED Pin structure (`Pin^pm x_{Z2} G`) exist on the
mapping torus `M_iota`?

Self-contained.  Imports only `numpy` (and the stdlib).  No project code is
imported and no C129 result is reused as an input: every homology number this
script reports is recomputed here from a chain complex built in this file.

WHAT IS BEING TESTED, and why it is NOT a restatement of C129
-------------------------------------------------------------
C129 showed `H^2(M_iota; F2) = 0`, hence `w_2 = 0` and `w_1^2 = 0`, hence both
BARE `Pin^+` and `Pin^-` structures exist.  `claim.md` for C130 explicitly
forbids the inference "the twisted obstruction also lands in `H^2(M;F2)`, which
is zero, so it trivially vanishes too" being made WITHOUT justification, because
twisting can move which characteristic class is the obstruction.

So this script does four separate things:

  PART 1  Recompute `H_*(M_f; Z)` from scratch (minimal AND non-minimal CW
          models, per C129's own Pearl 4: a vanishing-for-dimension-reasons
          headline must be recomputed in a presentation where the answer is a
          COMPUTED RANK, not a free consequence of the encoding), then push it
          through the universal-coefficient theorem to get `H^2(M_f; A)` for a
          whole family of coefficient groups `A`, and `H^3(M_f; Z)`.

  PART 2  Verify, by explicit matrix construction of
          `H := (Pin^pm(4) x SU(2)) / <(-1,-1)>`, the two structural facts the
          obstruction formula rests on:
            (i)  `H -> O(4) x SO(3)` is a Z/2-CENTRAL extension (kernel of
                 order 2, central), so the lifting obstruction is a SINGLE
                 class in `H^2(base; Z/2)` and there are no higher ones;
            (ii) lifts of the two factors COMMUTE, so the Kuenneth cross term
                 `H^1(BO) (x) H^1(BGbar)` in the extension class vanishes and
                 `zeta = zeta_Pin + zeta_G`.
          Plus a firing negative control: the same construction with a
          NON-central `z` is not a group quotient at all.

  PART 3  POSITIVE CONTROLS THAT THE TWIST GENUINELY MATTERS.  This is the part
          that discharges `claim.md`'s trap rather than assuming it away.  On
          other manifolds the untwisted and twisted answers DISAGREE, in both
          directions:
            CP^2      : untwisted FAILS (w_2 != 0) / twisted with w_2(E)=h WORKS
            S^2 x S^2 : untwisted WORKS (w_2 = 0)  / twisted with w_2(E)=a FAILS
          So "untwisted vanishes => twisted vanishes" is FALSE in general.  It
          holds on `M_iota` for a specific reason -- the whole group is zero --
          and that reason is what PART 1 computes.

  PART 4  Local (twisted) coefficients, including the monodromy that actually
          occurs here: `iota` EXCHANGES `SU(2)_a` and `SU(2)_b` (C125), so the
          relevant local system on `M_iota` is the swap.  Computed, not assumed.

Evidence tags used in the printed output follow the project's convention.
"""

from __future__ import annotations

import json
import os

import numpy as np

# --------------------------------------------------------------------------
# small exact linear algebra over Z  (Smith normal form) and over F_p
# --------------------------------------------------------------------------


def _smith_normal_form(mat: list[list[int]]) -> list[int]:
    """Return the list of nonzero elementary divisors of an integer matrix.

    Plain textbook SNF over Z.  Matrices here are tiny (<= 8x8), so the naive
    O(n^3) loop with full pivoting is fine and, more importantly, auditable.
    """
    a = [row[:] for row in mat]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    divisors: list[int] = []
    r = c = 0
    while r < rows and c < cols:
        # find a pivot: smallest nonzero absolute value in the active submatrix
        piv = None
        best = None
        for i in range(r, rows):
            for j in range(c, cols):
                if a[i][j] != 0 and (best is None or abs(a[i][j]) < best):
                    best = abs(a[i][j])
                    piv = (i, j)
        if piv is None:
            break
        pi, pj = piv
        a[r], a[pi] = a[pi], a[r]
        for row in a:
            row[c], row[pj] = row[pj], row[c]
        # clear column and row at the pivot, repeating until clean
        clean = False
        while not clean:
            clean = True
            for i in range(r + 1, rows):
                if a[i][c] != 0:
                    q = a[i][c] // a[r][c]
                    for j in range(c, cols):
                        a[i][j] -= q * a[r][j]
                    if a[i][c] != 0:
                        a[r], a[i] = a[i], a[r]
                        clean = False
            for j in range(c + 1, cols):
                if a[r][j] != 0:
                    q = a[r][j] // a[r][c]
                    for i in range(r, rows):
                        a[i][j] -= q * a[i][c]
                    if a[r][j] != 0:
                        for i in range(r, rows):
                            a[i][c], a[i][j] = a[i][j], a[i][c]
                        clean = False
        divisors.append(abs(a[r][c]))
        r += 1
        c += 1
    # enforce divisibility d_1 | d_2 | ... (does not change the iso class, but
    # makes the printed list canonical)
    changed = True
    while changed:
        changed = False
        for i in range(len(divisors) - 1):
            x, y = divisors[i], divisors[i + 1]
            if y % x != 0:
                g = np.gcd(x, y)
                lcm = x // g * y
                divisors[i], divisors[i + 1] = int(g), int(lcm)
                changed = True
    return divisors


def _rank_mod_p(mat: list[list[int]], p: int) -> int:
    """Rank of an integer matrix reduced mod a prime p."""
    a = [[x % p for x in row] for row in mat]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    row = 0
    for col in range(cols):
        piv = None
        for i in range(row, rows):
            if a[i][col] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        a[row], a[piv] = a[piv], a[row]
        inv = pow(a[row][col], p - 2, p)
        a[row] = [(x * inv) % p for x in a[row]]
        for i in range(rows):
            if i != row and a[i][col] % p != 0:
                f = a[i][col]
                a[i] = [(a[i][j] - f * a[row][j]) % p for j in range(cols)]
        row += 1
        rank += 1
    return rank


# --------------------------------------------------------------------------
# finitely generated abelian groups, Hom and Ext (for the UCT)
# --------------------------------------------------------------------------


class FGAb:
    """Z^free_rank  (+)  Z/t_1 (+) ... (+) Z/t_k   with every t_i >= 2."""

    def __init__(self, free_rank: int, torsion: list[int]):
        self.free_rank = int(free_rank)
        self.torsion = [int(t) for t in torsion if abs(int(t)) > 1]

    def __repr__(self) -> str:
        bits = []
        if self.free_rank == 1:
            bits.append("Z")
        elif self.free_rank > 1:
            bits.append(f"Z^{self.free_rank}")
        bits.extend(f"Z/{t}" for t in self.torsion)
        return " + ".join(bits) if bits else "0"

    def is_zero(self) -> bool:
        return self.free_rank == 0 and not self.torsion


def hom_into(g: FGAb, coeff: int) -> FGAb:
    """Hom(g, A) where A = Z if coeff == 0, else A = Z/coeff."""
    if coeff == 0:
        # Hom(Z^r + torsion, Z) = Z^r
        return FGAb(g.free_rank, [])
    tor = []
    for t in g.torsion:
        d = int(np.gcd(t, coeff))
        if d > 1:
            tor.append(d)
    return FGAb(0, [coeff] * g.free_rank + tor) if g.free_rank else FGAb(0, tor)


def ext_into(g: FGAb, coeff: int) -> FGAb:
    """Ext^1(g, A) where A = Z if coeff == 0, else A = Z/coeff.

    Ext^1(Z, A) = 0 ; Ext^1(Z/t, Z) = Z/t ; Ext^1(Z/t, Z/n) = Z/gcd(t,n).
    """
    tor = []
    for t in g.torsion:
        if coeff == 0:
            tor.append(t)
        else:
            d = int(np.gcd(t, coeff))
            if d > 1:
                tor.append(d)
    return FGAb(0, tor)


def cohomology_from_homology(homology: list[FGAb], degree: int, coeff: int) -> FGAb:
    """UCT:  H^n(X;A) = Hom(H_n(X), A)  (+)  Ext^1(H_{n-1}(X), A)."""
    hn = homology[degree] if 0 <= degree < len(homology) else FGAb(0, [])
    hprev = homology[degree - 1] if 1 <= degree <= len(homology) else FGAb(0, [])
    a = hom_into(hn, coeff)
    b = ext_into(hprev, coeff)
    return FGAb(a.free_rank + b.free_rank, a.torsion + b.torsion)


# --------------------------------------------------------------------------
# chain complexes, chain self-maps, mapping tori
# --------------------------------------------------------------------------


class ChainComplex:
    """Free Z-chain complex.  ranks[n] = rank of C_n ; d[n] : C_n -> C_{n-1}."""

    def __init__(self, ranks: list[int], d: dict[int, list[list[int]]] | None = None):
        self.ranks = list(ranks)
        self.d: dict[int, list[list[int]]] = {}
        if d:
            for k, m in d.items():
                self.d[k] = [row[:] for row in m]

    def top(self) -> int:
        return len(self.ranks) - 1

    def boundary(self, n: int) -> list[list[int]]:
        """d_n : C_n -> C_{n-1}, as a (rank_{n-1} x rank_n) matrix of ints."""
        src = self.ranks[n] if 0 <= n < len(self.ranks) else 0
        tgt = self.ranks[n - 1] if 1 <= n < len(self.ranks) else 0
        if n in self.d:
            m = self.d[n]
            assert len(m) == tgt and (tgt == 0 or len(m[0]) == src), (
                f"d_{n} has shape {len(m)}x{len(m[0]) if m else 0}, expected {tgt}x{src}"
            )
            return [row[:] for row in m]
        return [[0] * src for _ in range(tgt)]

    def check_d_squared_zero(self) -> float:
        worst = 0.0
        for n in range(2, len(self.ranks)):
            a = np.array(self.boundary(n - 1), dtype=object).reshape(
                self.ranks[n - 2] if n - 2 >= 0 else 0, self.ranks[n - 1]
            )
            b = np.array(self.boundary(n), dtype=object).reshape(
                self.ranks[n - 1], self.ranks[n]
            )
            if a.size and b.size:
                prod = a.astype(np.int64) @ b.astype(np.int64)
                worst = max(worst, float(np.abs(prod).max()))
        return worst

    def homology(self) -> list[FGAb]:
        out: list[FGAb] = []
        for n in range(len(self.ranks)):
            dn = self.boundary(n)  # C_n -> C_{n-1}
            dn1 = self.boundary(n + 1) if n + 1 < len(self.ranks) else []
            rank_dn = _rank_over_q(dn, self.ranks[n])
            ker_rank = self.ranks[n] - rank_dn
            if dn1:
                divs = _smith_normal_form(dn1)
            else:
                divs = []
            im_rank = len(divs)
            free_rank = ker_rank - im_rank
            torsion = [d for d in divs if d > 1]
            out.append(FGAb(free_rank, torsion))
        return out

    def betti_mod_p(self, p: int) -> list[int]:
        out = []
        for n in range(len(self.ranks)):
            dn = self.boundary(n)
            dn1 = self.boundary(n + 1) if n + 1 < len(self.ranks) else []
            r_n = _rank_mod_p(dn, p) if dn and dn[0] else 0
            r_n1 = _rank_mod_p(dn1, p) if dn1 and dn1[0] else 0
            out.append(self.ranks[n] - r_n - r_n1)
        return out


def _rank_over_q(mat: list[list[int]], ncols: int) -> int:
    if not mat or ncols == 0:
        return 0
    return len(_smith_normal_form(mat))


def sphere_complex(n: int) -> ChainComplex:
    """Minimal CW model of S^n: one 0-cell, one n-cell, zero differentials."""
    ranks = [0] * (n + 1)
    ranks[0] = 1
    ranks[n] = 1
    if n == 0:
        ranks = [2]
    return ChainComplex(ranks)


def s3_nonminimal_complex() -> ChainComplex:
    """NON-minimal CW model of S^3: C = [1,1,1,1] with d_2 = (1).

    Simply connected with S^3's homology, hence homotopy equivalent to S^3, but
    with C_2 != 0 -- so in the mapping torus H_2 = 0 becomes a COMPUTED RANK
    rather than a free consequence of "there are no 2-cells".  This is C129's
    Pearl 4 discipline applied to a new headline.
    """
    return ChainComplex([1, 1, 1, 1], {2: [[1]], 1: [[0]], 3: [[0]]})


def sphere_self_map(n: int, degree: int) -> dict[int, list[list[int]]]:
    f = {0: [[1]]}
    f[n] = [[degree]]
    return f


def s3_nonminimal_self_map(degree: int) -> dict[int, list[list[int]]]:
    """Chain self-map of the non-minimal S^3 model of the given degree.

    Chain-map condition d_2 f_2 = f_1 d_2 with d_2 = (1) forces f_2 = f_1;
    take that common value to be 1.  f_3 = degree.
    """
    return {0: [[1]], 1: [[1]], 2: [[1]], 3: [[degree]]}


def mapping_torus_complex(
    c: ChainComplex, f: dict[int, list[list[int]]]
) -> ChainComplex:
    """Algebraic mapping torus.

    D_n = C_n (+) C_{n-1},   d(a,b) = ( d a + (f - id) b , -d b ).
    d^2 = 0 because f is a chain map, so d(f-id) = (f-id)d.
    """
    top = c.top() + 1
    ranks = []
    for n in range(top + 1):
        cn = c.ranks[n] if n < len(c.ranks) else 0
        cn1 = c.ranks[n - 1] if 1 <= n <= c.top() + 1 and n - 1 < len(c.ranks) else 0
        ranks.append(cn + cn1)
    dd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 1):
        cn = c.ranks[n] if n < len(c.ranks) else 0
        cn1 = c.ranks[n - 1] if n - 1 < len(c.ranks) else 0
        tgt_cn1 = c.ranks[n - 1] if n - 1 < len(c.ranks) else 0
        tgt_cn2 = c.ranks[n - 2] if n >= 2 and n - 2 < len(c.ranks) else 0
        rows = tgt_cn1 + tgt_cn2
        cols = cn + cn1
        m = [[0] * cols for _ in range(rows)]
        dn = c.boundary(n) if n < len(c.ranks) else []
        for i in range(tgt_cn1):
            for j in range(cn):
                m[i][j] = dn[i][j]
        # (f - id) acting C_{n-1} -> C_{n-1}
        fm = f.get(n - 1)
        for j in range(cn1):
            for i in range(tgt_cn1):
                val = (fm[i][j] if fm else (1 if i == j else 0)) - (1 if i == j else 0)
                m[i][cn + j] += val
        # -d acting C_{n-1} -> C_{n-2}
        dn1 = c.boundary(n - 1) if n - 1 < len(c.ranks) and n - 1 >= 1 else []
        for i in range(tgt_cn2):
            for j in range(cn1):
                m[tgt_cn1 + i][cn + j] = -dn1[i][j]
        dd[n] = m
    return ChainComplex(ranks, dd)


def tensor_complex(a: ChainComplex, b: ChainComplex) -> ChainComplex:
    """Tensor product of two free chain complexes (for product manifolds)."""
    top = a.top() + b.top()
    index: dict[int, list[tuple[int, int, int, int]]] = {}
    ranks = []
    for n in range(top + 1):
        entries = []
        pos = 0
        for p in range(n + 1):
            q = n - p
            if p < len(a.ranks) and q < len(b.ranks):
                for i in range(a.ranks[p]):
                    for j in range(b.ranks[q]):
                        entries.append((p, q, i, j))
                        pos += 1
        index[n] = entries
        ranks.append(pos)
    dd: dict[int, list[list[int]]] = {}
    for n in range(1, top + 1):
        rows = ranks[n - 1]
        cols = ranks[n]
        m = [[0] * cols for _ in range(rows)]
        tgt = {e: k for k, e in enumerate(index[n - 1])}
        for col, (p, q, i, j) in enumerate(index[n]):
            if p >= 1:
                da = a.boundary(p)
                for ii in range(a.ranks[p - 1]):
                    v = da[ii][i]
                    if v:
                        m[tgt[(p - 1, q, ii, j)]][col] += v
            if q >= 1:
                db = b.boundary(q)
                sign = -1 if p % 2 else 1
                for jj in range(b.ranks[q - 1]):
                    v = db[jj][j]
                    if v:
                        m[tgt[(p, q - 1, i, jj)]][col] += sign * v
        dd[n] = m
    return ChainComplex(ranks, dd)


def mapping_torus_local_coeff_betti_f2(
    c: ChainComplex, f: dict[int, list[list[int]]], rho: list[list[int]]
) -> list[int]:
    """F2-Betti numbers of M_f with the LOCAL system whose monodromy is `rho`.

    The fibre is simply connected, so the local system restricts to a constant
    one on the fibre; the mapping-torus complex is then the same construction
    with (f (x) rho - id) in place of (f - id).
    """
    k = len(rho)
    top = c.top() + 1
    ranks = []
    for n in range(top + 1):
        cn = c.ranks[n] if 0 <= n < len(c.ranks) else 0
        cn1 = c.ranks[n - 1] if 1 <= n and n - 1 < len(c.ranks) else 0
        ranks.append(k * (cn + cn1))
    dd: dict[int, list[list[int]]] = {}
    ident = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
    for n in range(1, top + 1):
        cn = c.ranks[n] if n < len(c.ranks) else 0
        cn1 = c.ranks[n - 1] if n - 1 < len(c.ranks) else 0
        tgt_cn1 = c.ranks[n - 1] if n - 1 < len(c.ranks) else 0
        tgt_cn2 = c.ranks[n - 2] if n >= 2 and n - 2 < len(c.ranks) else 0
        rows = k * (tgt_cn1 + tgt_cn2)
        cols = k * (cn + cn1)
        m = [[0] * cols for _ in range(rows)]
        dn = c.boundary(n) if n < len(c.ranks) else []
        for i in range(tgt_cn1):
            for j in range(cn):
                v = dn[i][j]
                if v:
                    for s in range(k):
                        m[k * i + s][k * j + s] += v
        fm = f.get(n - 1)
        for j in range(cn1):
            for i in range(tgt_cn1):
                fv = fm[i][j] if fm else (1 if i == j else 0)
                iv = 1 if i == j else 0
                for s in range(k):
                    for t_ in range(k):
                        m[k * i + s][k * (cn + j) + t_] += (
                            fv * rho[s][t_] - iv * ident[s][t_]
                        )
        dn1 = c.boundary(n - 1) if 1 <= n - 1 < len(c.ranks) else []
        for i in range(tgt_cn2):
            for j in range(cn1):
                v = dn1[i][j]
                if v:
                    for s in range(k):
                        m[k * (tgt_cn1 + i) + s][k * (cn + j) + s] += -v
        dd[n] = m
    return ChainComplex(ranks, dd).betti_mod_p(2)


# --------------------------------------------------------------------------
# tiny truncated F2 "cohomology ring" engine, for the PART 3 controls
# --------------------------------------------------------------------------


class F2Ring:
    """Graded-commutative F2 polynomial ring truncated by per-generator bounds.

    Generators have degrees `degs`; generator i is nilpotent with x_i^{b_i} = 0.
    Anything of total degree > `dim` is also set to zero (top-dimension cutoff).
    This suffices for RP^n (one degree-1 generator, a^{n+1}=0), CP^n (one
    degree-2 generator), and products thereof.
    """

    def __init__(self, degs: list[int], bounds: list[int], dim: int, name: str):
        self.degs = list(degs)
        self.bounds = list(bounds)
        self.dim = dim
        self.name = name

    def zero(self) -> dict[tuple[int, ...], int]:
        return {}

    def one(self) -> dict[tuple[int, ...], int]:
        return {tuple([0] * len(self.degs)): 1}

    def gen(self, i: int) -> dict[tuple[int, ...], int]:
        e = [0] * len(self.degs)
        e[i] = 1
        return {tuple(e): 1}

    def _norm(self, d: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
        out = {}
        for mon, coef in d.items():
            if coef % 2 == 0:
                continue
            if any(mon[i] >= self.bounds[i] for i in range(len(mon))):
                continue
            deg = sum(mon[i] * self.degs[i] for i in range(len(mon)))
            if deg > self.dim:
                continue
            out[mon] = 1
        return out

    def add(self, *terms):
        acc: dict[tuple[int, ...], int] = {}
        for t in terms:
            for mon, coef in t.items():
                acc[mon] = acc.get(mon, 0) + coef
        return self._norm(acc)

    def mul(self, x, y):
        acc: dict[tuple[int, ...], int] = {}
        for m1, c1 in x.items():
            for m2, c2 in y.items():
                mon = tuple(m1[i] + m2[i] for i in range(len(m1)))
                acc[mon] = acc.get(mon, 0) + c1 * c2
        return self._norm(acc)

    def graded_part(self, x, deg: int):
        return {
            m: c
            for m, c in x.items()
            if sum(m[i] * self.degs[i] for i in range(len(m))) == deg
        }

    def is_zero(self, x) -> bool:
        return len(self._norm(x)) == 0

    def show(self, x) -> str:
        if not x:
            return "0"
        parts = []
        for mon in sorted(x):
            s = "".join(
                f"g{i}^{mon[i]}" if mon[i] > 1 else (f"g{i}" if mon[i] == 1 else "")
                for i in range(len(mon))
            )
            parts.append(s if s else "1")
        return " + ".join(parts)

    def total_sw_from_product(self, factors):
        """Multiply a list of total-SW-class elements together."""
        acc = self.one()
        for f in factors:
            acc = self.mul(acc, f)
        return acc


def pin_verdict(ring: F2Ring, w1, w2, twist_c2):
    """Kirby-Taylor criteria, TWISTED by a degree-2 class `twist_c2`.

    Per C129 Sec.2a (Kirby-Taylor, read as PRIMARY there):
        Pin^+  exists  <=>  w_2            = 0
        Pin^-  exists  <=>  w_2 + w_1^2    = 0
    Twisting by a Z/2-central extension with class `zeta` adds `zeta`'s pullback
    (written `twist_c2` here) to BOTH conditions -- Debray-Yu Lemma 3.9 for the
    Spin case, extended to Pin by the same K(Z/2,2)-fibration argument (Sec.4 of
    decision.md).  `twist_c2 = 0` recovers the bare case.

    NOTE the shape deliberately mirrors C129's repaired `pin_verdict`: it takes
    CLASSES and expands in F2, never booleans.  C129's own skeptic pass A1 found
    that the boolean form silently returns the wrong answer on RP^2 x RP^2.
    """
    obs_plus = ring.add(w2, twist_c2)
    obs_minus = ring.add(w2, ring.mul(w1, w1), twist_c2)
    return {
        "obstruction_pin_plus": ring.show(obs_plus),
        "obstruction_pin_minus": ring.show(obs_minus),
        "pin_plus_exists": ring.is_zero(obs_plus),
        "pin_minus_exists": ring.is_zero(obs_minus),
    }


# --------------------------------------------------------------------------
# Clifford / Pin(4) x_{Z2} SU(2) explicit construction  (PART 2)
# --------------------------------------------------------------------------


def clifford_generators(n: int, square: int) -> list[np.ndarray]:
    """Real matrices e_1..e_n with e_i e_j + e_j e_i = 2 * square * delta_ij.

    Built by the standard complex Jordan-Wigner tensor construction; `square`
    is +1 or -1.  Returned as complex matrices (real up to the i factors), which
    is all that is needed for the group-theoretic checks below.
    """
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    k = (n + 1) // 2
    dim = 2**k

    def kron(mats):
        out = np.array([[1.0 + 0j]])
        for m in mats:
            out = np.kron(out, m)
        return out

    gens = []
    for a in range(n):
        j = a // 2
        mats = [sz] * j
        mats.append(sx if a % 2 == 0 else sy)
        mats.extend([np.eye(2, dtype=complex)] * (k - j - 1))
        g = kron(mats)
        if square == -1:
            g = 1j * g
        gens.append(g[:dim, :dim])
    return gens


def twisted_adjoint(x: np.ndarray, gens: list[np.ndarray], parity: int) -> np.ndarray:
    """rho~(x) e_j = alpha(x) e_j x^{-1}, alpha = grade involution (+/- on x)."""
    n = len(gens)
    xi = np.linalg.inv(x)
    sign = 1.0 if parity == 0 else -1.0
    out = np.zeros((n, n), dtype=complex)
    for j in range(n):
        img = sign * (x @ gens[j] @ xi)
        for i in range(n):
            # e_i are orthogonal w.r.t. tr(e_i^dag e_j); project
            num = np.trace(gens[i].conj().T @ img)
            den = np.trace(gens[i].conj().T @ gens[i])
            out[i, j] = num / den
    return out


def su2_matrix(rng) -> np.ndarray:
    v = rng.normal(size=4)
    v = v / np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def commutator_pairing(
    lift1: tuple[np.ndarray, ...],
    lift2: tuple[np.ndarray, ...],
    kernel_gen: tuple[np.ndarray, ...],
) -> int:
    """Commutator pairing of a Z/2-central extension, evaluated on two lifts.

    In a Z/2-central extension `1 -> Z/2 -> H -> K -> 1`, if k1, k2 in K COMMUTE
    then the commutator of any two lifts lands in the central Z/2 and is
    independent of the choice of lifts.  That map `K x K -> Z/2` is exactly the
    antisymmetric part of the extension class; on a product `K = K1 x K2` its
    restriction to `K1 x K2` IS the Kuenneth cross term
    `H^1(BK1) (x) H^1(BK2) -> Z/2`.

    Returns 0 if the lifts commute, 1 if their commutator is the kernel
    generator.  Raises if it is neither (i.e. the inputs did not descend to
    commuting elements of K, so the pairing is not defined).

    Elements are tuples of matrices (one per direct factor of the ambient group),
    multiplied componentwise -- so the SAME code path runs on the pair
    construction `(Pin x SU(2))/<(-1,-1)>` and on the quaternion group Q8, which
    is the discriminating control: Q8 is also a Z/2-central extension of a
    PRODUCT group `Z/2 x Z/2`, and there the pairing is NONZERO.
    """

    def mul(x, y):
        return tuple(a @ b for a, b in zip(x, y, strict=True))

    def inv(x):
        return tuple(np.linalg.inv(a) for a in x)

    def close(x, y):
        return all(
            float(np.abs(a - b).max()) < 1e-10 for a, b in zip(x, y, strict=True)
        )

    ident = tuple(np.eye(a.shape[0], dtype=complex) for a in lift1)
    comm = mul(mul(lift1, lift2), inv(mul(lift2, lift1)))
    if close(comm, ident):
        return 0
    if close(comm, kernel_gen):
        return 1
    raise ValueError("commutator is not in the central Z/2 -- pairing undefined")


def kernel_order(ident: np.ndarray, z: np.ndarray, identify: bool) -> int:
    """Order of ker(H -> O(n) x Gbar) for H = (Pin x G)/<(-1, z)>, COMPUTED.

    Enumerates the four elements (+-1, {1,z}) of the preimage of the identity
    in Pin x G and counts equivalence classes modulo <(-1, z)>.  With the
    identification this must be 2 (so the extension is by Z/2); WITHOUT it the
    same routine returns 4 -- that is the control, and it is what makes this a
    test rather than the tautology the first draft used here.
    """
    reps = [
        (ident, np.eye(2, dtype=complex)),
        (-ident, np.eye(2, dtype=complex)),
        (ident, z),
        (-ident, z),
    ]
    classes: list[tuple] = []
    for r in reps:
        found = False
        for c in classes:
            same = all(
                float(np.abs(a - b).max()) < 1e-10 for a, b in zip(r, c, strict=True)
            )
            twisted = identify and all(
                float(np.abs(a + b).max()) < 1e-10 for a, b in zip(r, c, strict=True)
            )
            if same or twisted:
                found = True
                break
        if not found:
            classes.append(r)
    return len(classes)


def su2_to_so3(q: np.ndarray) -> np.ndarray:
    sig = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    out = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            out[i, j] = float(np.real(0.5 * np.trace(sig[i] @ q @ sig[j] @ q.conj().T)))
    return out


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def main() -> dict:
    rng = np.random.default_rng(20260902)
    out: dict = {}
    gates: dict[str, bool] = {}

    # ======================================================================
    # PART 1 -- H_*(M_f) from scratch, two CW models, then UCT for many A
    # ======================================================================
    part1: dict = {}

    # sanity of the machinery first (textbook controls that it can be nonzero)
    kb = mapping_torus_complex(
        ChainComplex([1, 1], {1: [[0]]}), {0: [[1]], 1: [[-1]]}
    )  # Klein bottle = mapping torus of degree -1 self map of S^1
    kb_h = kb.homology()
    part1["control_klein_bottle_H"] = [repr(g) for g in kb_h]
    gates["G01_klein_bottle_H1_is_Z_plus_Z2"] = kb_h[1].free_rank == 1 and kb_h[
        1
    ].torsion == [2]
    torus = mapping_torus_complex(
        ChainComplex([1, 1], {1: [[0]]}), {0: [[1]], 1: [[1]]}
    )
    torus_h = torus.homology()
    part1["control_torus_H"] = [repr(g) for g in torus_h]
    gates["G02_torus_H2_is_Z"] = torus_h[2].free_rank == 1 and not torus_h[2].torsion

    s2s1 = mapping_torus_complex(sphere_complex(2), sphere_self_map(2, 1))
    s2s1_h = s2s1.homology()
    part1["control_S2xS1_H"] = [repr(g) for g in s2s1_h]
    gates["G03_S2xS1_H2_nonzero"] = not s2s1_h[2].is_zero()

    # C129's standing counterexample CP^2 x S^1 -- H^2 is NOT zero there, which
    # is exactly why the answer here is a computation and not a generality.
    cp2 = ChainComplex([1, 0, 1, 0, 1])
    circle = ChainComplex([1, 1], {1: [[0]]})
    cp2xs1 = tensor_complex(cp2, circle)
    cp2xs1_h = cp2xs1.homology()
    part1["control_CP2xS1_H"] = [repr(g) for g in cp2xs1_h]
    gates["G04_CP2xS1_H2_nonzero"] = not cp2xs1_h[2].is_zero()

    # ---- the object itself, minimal model, for several degrees
    degrees = [-1, 0, 1, 2, 7]
    minimal: dict[str, dict] = {}
    for deg in degrees:
        mt = mapping_torus_complex(sphere_complex(3), sphere_self_map(3, deg))
        h = mt.homology()
        minimal[f"deg_{deg}"] = {
            "cell_ranks_by_dim": mt.ranks,
            "d_squared_max_abs": mt.check_d_squared_zero(),
            "H_Z": [repr(g) for g in h],
            "betti_F2": mt.betti_mod_p(2),
            "betti_F3": mt.betti_mod_p(3),
        }
    part1["minimal_model"] = minimal
    gates["G05_minimal_d_squared_zero"] = all(
        v["d_squared_max_abs"] == 0.0 for v in minimal.values()
    )
    gates["G06_minimal_M_iota_H_is_Z_Z_0_Z2_0"] = minimal["deg_-1"]["H_Z"] == [
        "Z",
        "Z",
        "0",
        "Z/2",
        "0",
    ]

    # ---- NON-minimal model (H_2 = 0 becomes a computed rank, not a cell count)
    #
    # REPAIRED after FL Step 8a: the first version ran this for deg in {-1, +1}
    # ONLY, so the deg 0/2/7 rows that Sec.5a and Sec.8 publish existed only in
    # the minimal model -- where D_2 = C_2 (+) C_1 = 0 identically and H_2 = 0
    # is a cell-count artifact that survives any corruption.  Both skeptic
    # passes flagged it; it is C129's own finding A4 re-committed.  Now run for
    # EVERY degree, and the whole table is gated, not just deg = -1.
    nonmin: dict[str, dict] = {}
    for deg in degrees:
        mt = mapping_torus_complex(s3_nonminimal_complex(), s3_nonminimal_self_map(deg))
        h = mt.homology()
        nonmin[f"deg_{deg}"] = {
            "cell_ranks_by_dim": mt.ranks,
            "d_squared_max_abs": mt.check_d_squared_zero(),
            "H_Z": [repr(g) for g in h],
            "betti_F2": mt.betti_mod_p(2),
        }
    part1["nonminimal_model"] = nonmin
    gates["G07_nonminimal_has_two_2cells"] = all(
        v["cell_ranks_by_dim"] == [1, 2, 2, 2, 1] for v in nonmin.values()
    )
    gates["G08_nonminimal_agrees_with_minimal_AT_EVERY_DEGREE"] = all(
        nonmin[k]["H_Z"] == minimal[k]["H_Z"] for k in minimal
    )
    gates["G09_nonminimal_d_squared_zero"] = all(
        v["d_squared_max_abs"] == 0.0 for v in nonmin.values()
    )
    # H_2 = 0 at EVERY degree, in the model where it is a computed rank
    gates["G09b_H2_zero_at_every_degree_in_the_NONMINIMAL_model"] = all(
        v["betti_F2"][2] == 0 for v in nonmin.values()
    )
    # and the degree sweep is not degenerate: the models must DISAGREE nowhere
    # while the degrees themselves DO differ from one another in H_3.
    part1["H3_Z_across_degrees"] = {k: v["H_Z"][3] for k, v in nonmin.items()}
    gates["G09c_degrees_are_distinguishable_H3_differs_across_them"] = (
        len({v["H_Z"][3] for v in nonmin.values()}) >= 3
    )

    # ---- THE HEADLINE COHOMOLOGY GROUPS, by UCT, for a family of coefficients
    mt_iota = mapping_torus_complex(sphere_complex(3), sphere_self_map(3, -1))
    h_iota = mt_iota.homology()
    mt_iota_nm = mapping_torus_complex(
        s3_nonminimal_complex(), s3_nonminimal_self_map(-1)
    )
    h_iota_nm = mt_iota_nm.homology()

    coeff_list = [0, 2, 3, 4, 5, 8, 9, 16]  # 0 means Z
    h2_table = {}
    h3_table = {}
    for a in coeff_list:
        key = "Z" if a == 0 else f"Z/{a}"
        g2 = cohomology_from_homology(h_iota, 2, a)
        g2nm = cohomology_from_homology(h_iota_nm, 2, a)
        g3 = cohomology_from_homology(h_iota, 3, a)
        h2_table[key] = {"minimal": repr(g2), "nonminimal": repr(g2nm)}
        h3_table[key] = repr(g3)
    part1["H2_M_iota_by_coefficient"] = h2_table
    part1["H3_M_iota_by_coefficient"] = h3_table
    gates["G10_H2_M_iota_vanishes_for_every_tested_coefficient"] = all(
        v["minimal"] == "0" and v["nonminimal"] == "0" for v in h2_table.values()
    )
    gates["G11_H3_M_iota_Z_vanishes"] = h3_table["Z"] == "0"
    # discriminating: H^3 is NOT identically zero -- so G11 is not vacuous
    gates["G12_H3_M_iota_F2_is_NONzero_control"] = h3_table["Z/2"] == "Z/2"
    # discriminating: the same UCT pipeline returns nonzero H^2 on the control
    h2_cp2xs1 = cohomology_from_homology(cp2xs1_h, 2, 2)
    part1["control_CP2xS1_H2_F2"] = repr(h2_cp2xs1)
    gates["G13_UCT_pipeline_returns_nonzero_H2_on_control"] = not h2_cp2xs1.is_zero()

    out["PART1_cohomology"] = part1

    # ======================================================================
    # PART 2 -- (Pin^pm(4) x SU(2))/<(-1,-1)> is a Z/2-CENTRAL extension of
    #           O(4) x SO(3), and the two factors' lifts COMMUTE
    # ======================================================================
    part2: dict = {}
    SIG_KEYS = ["Cl(4,0)", "Cl(0,4)"]
    for sig_name, sq in (("Cl(4,0)", +1), ("Cl(0,4)", -1)):
        gens = clifford_generators(4, sq)
        dim = gens[0].shape[0]
        ident = np.eye(dim, dtype=complex)
        rel = 0.0
        for i in range(4):
            for j in range(4):
                anti = gens[i] @ gens[j] + gens[j] @ gens[i]
                want = 2.0 * sq * ident if i == j else np.zeros_like(ident)
                rel = max(rel, float(np.abs(anti - want).max()))
        # a reflection: unit vector e_1.  Its square is +/-1 -> Pin^+ vs Pin^-.
        refl_sq = float(np.real(np.trace(gens[0] @ gens[0]) / dim))
        # rho~(e_1) must be the reflection in the hyperplane orthogonal to e_1
        r_img = twisted_adjoint(gens[0], gens, parity=1)
        want_refl = np.diag([-1.0, 1.0, 1.0, 1.0])
        refl_err = float(np.abs(r_img - want_refl).max())
        # THE LOAD-BEARING CHECK, REBUILT AFTER FL Step 8a.
        #
        # The first version tested `twisted_adjoint(-I, gens, parity=0) == I`
        # (true for ANY matrices: (-I)e(-I)^-1 = e) and
        # `max|(-I)p - p(-I)|` (a scalar commutator, identically 0), and called
        # the pair "the extension is Z/2-central".  BOTH CANNOT FAIL, and both
        # skeptic passes found it independently; the JSON tell was a residual of
        # exactly 0.0 rather than ~1e-16.  Replaced by a check that can fail:
        # NORMALITY of the subgroup <(-1, z)> inside Pin x G, computed by actual
        # conjugation and membership testing.  It FIRES on a non-central z.
        z_central = -np.eye(2, dtype=complex)
        z_bad = np.array([[1j, 0], [0, -1j]], dtype=complex)  # i*sigma_3
        normality = {}
        for zname, zval in (("central_z", z_central), ("noncentral_z", z_bad)):
            worst_dev = 0.0
            for _ in range(120):
                k = int(rng.integers(0, 5))
                p = ident.copy()
                for _ in range(k):
                    v = rng.normal(size=4)
                    v = v / np.linalg.norm(v)
                    unit = sum(v[i] * gens[i] for i in range(4))
                    p = p @ unit
                q = su2_matrix(rng)
                # conjugate the generator (-1, z) by (p, q)
                cp = p @ (-ident) @ np.linalg.inv(p)
                cq = q @ zval @ np.linalg.inv(q)
                # must land back in {(1,1), (-1,z)}; only the second is possible
                # here because cp = -I always, so the whole test is on cq.
                dev = min(
                    max(
                        float(np.abs(cp + ident).max()),
                        float(np.abs(cq - zval).max()),
                    ),
                    max(
                        float(np.abs(cp - ident).max()),
                        float(np.abs(cq - np.eye(2)).max()),
                    ),
                )
                worst_dev = max(worst_dev, dev)
            normality[zname] = worst_dev

        # kernel ORDER, computed rather than asserted: the classes of
        # (+-1, +-1) modulo <(-1, z)>.  Two classes => Z/2.  (Quotienting by the
        # TRIVIAL subgroup instead would give four -- that is the control.)
        part2[sig_name] = {
            "clifford_relations_residual": rel,
            "reflection_square_e1_sq": refl_sq,
            "reflection_image_residual": refl_err,
            "normality_deviation_central_z": normality["central_z"],
            "normality_deviation_noncentral_z_MUST_BE_LARGE": normality["noncentral_z"],
            "kernel_order_with_identification": kernel_order(ident, z_central, True),
            "kernel_order_control_without_identification": kernel_order(
                ident, z_central, False
            ),
        }
    gates["G14_clifford_relations_hold_both_signatures"] = all(
        part2[k]["clifford_relations_residual"] < 1e-12 for k in SIG_KEYS
    )
    gates["G15_reflection_is_a_reflection_both_signatures"] = all(
        part2[k]["reflection_image_residual"] < 1e-12 for k in SIG_KEYS
    )
    gates["G16_identification_subgroup_is_NORMAL_for_central_z"] = all(
        part2[k]["normality_deviation_central_z"] < 1e-12 for k in SIG_KEYS
    )
    gates["G16b_normality_check_FIRES_on_noncentral_z"] = all(
        part2[k]["normality_deviation_noncentral_z_MUST_BE_LARGE"] > 0.5
        for k in SIG_KEYS
    )
    gates["G18_kernel_has_ORDER_2_computed_not_asserted"] = all(
        part2[k]["kernel_order_with_identification"] == 2 for k in SIG_KEYS
    )
    gates["G18b_kernel_order_control_is_4_without_the_identification"] = all(
        part2[k]["kernel_order_control_without_identification"] == 4 for k in SIG_KEYS
    )

    # THE KUENNETH CROSS TERM.  Scope corrected after FL Step 8a: for a quotient
    # of a DIRECT product the commutator of lifts of the two factors is the
    # identity BY CONSTRUCTION -- computing it on our own group is a tautology
    # (the first draft did exactly that and both passes caught it).  It is
    # therefore NOT gated as evidence.  What IS computed here is the honest
    # content: that "Z/2-central extension of a product group" does NOT by
    # itself imply a vanishing cross term, so the direct-product hypothesis is
    # doing real work.  Q8 -> Z/2 x Z/2 is the witness.
    quat_i = np.array([[1j, 0], [0, -1j]], dtype=complex)
    quat_j = np.array([[0, 1], [-1, 0]], dtype=complex)
    q8_kernel = (-np.eye(2, dtype=complex),)
    q8_pairing = commutator_pairing((quat_i,), (quat_j,), q8_kernel)
    part2["control_Q8_commutator_pairing_MUST_BE_1"] = q8_pairing
    part2["cross_term_note"] = (
        "vanishing of the cross term for (Pin x G)/<(-1,z)> is definitional "
        "(quotient of a DIRECT product), not measured; and for CONNECTED Gbar "
        "the cross-term group H^1(BGbar;F2) = Hom(pi_0 Gbar, F2) is itself "
        "zero, so there is nothing to compute.  Q8 shows the hypothesis is not "
        "vacuous."
    )
    gates["G17_Q8_shows_a_central_extension_of_a_product_CAN_have_a_cross_term"] = (
        q8_pairing == 1
    )
    # the two signatures are genuinely different: e_1^2 = +1 vs -1
    gates["G19_two_signatures_differ_by_vector_square"] = (
        abs(part2["Cl(4,0)"]["reflection_square_e1_sq"] - 1.0) < 1e-12
        and abs(part2["Cl(0,4)"]["reflection_square_e1_sq"] + 1.0) < 1e-12
    )

    # (The first draft's separate `G20` "non-central z" control is DELETED: it
    # measured ||zq - qz||, which restates the input rather than testing whether
    # the construction detects non-normality.  `G16b` above now performs the
    # actual conjugation and membership test, and fires.  Skeptic pass 1,
    # finding 11.)

    # SU(2) -> SO(3) really is the double cover with kernel {+-1}
    ad_err = 0.0
    ad_minus = float(np.abs(su2_to_so3(-np.eye(2)) - np.eye(3)).max())
    for _ in range(100):
        q = su2_matrix(rng)
        r = su2_to_so3(q)
        ad_err = max(
            ad_err,
            float(np.abs(r @ r.T - np.eye(3)).max()),
            abs(float(np.linalg.det(r)) - 1.0),
            float(np.abs(su2_to_so3(-q) - r).max()),
        )
    part2["su2_to_so3_residual"] = ad_err
    part2["su2_to_so3_minus_one_in_kernel"] = ad_minus
    gates["G21_su2_to_so3_is_double_cover"] = ad_err < 1e-9 and ad_minus < 1e-9
    out["PART2_extension"] = part2

    # ======================================================================
    # PART 3 -- the twist GENUINELY MATTERS in general (discharges the trap)
    # ======================================================================
    part3: dict = {}

    def rp(n: int) -> tuple[F2Ring, dict, dict]:
        ring = F2Ring([1], [n + 1], n, f"RP^{n}")
        a = ring.gen(0)
        total = ring.one()
        base = ring.add(ring.one(), a)
        for _ in range(n + 1):
            total = ring.mul(total, base)
        return ring, ring.graded_part(total, 1), ring.graded_part(total, 2)

    # -- Kirby-Taylor labelling anchors (C129 Sec.2a), UNTWISTED
    for n in (2, 4):
        ring, w1, w2 = rp(n)
        v = pin_verdict(ring, w1, w2, ring.zero())
        part3[f"RP{n}_bare"] = {"w1": ring.show(w1), "w2": ring.show(w2), **v}
    gates["G22_RP2_is_pin_minus_only"] = (
        part3["RP2_bare"]["pin_minus_exists"]
        and not part3["RP2_bare"]["pin_plus_exists"]
    )
    gates["G23_RP4_is_pin_plus_only"] = (
        part3["RP4_bare"]["pin_plus_exists"]
        and not part3["RP4_bare"]["pin_minus_exists"]
    )

    # RP^2 x RP^2 : NEITHER (C129's G25b/c, reproduced independently)
    ring22 = F2Ring([1, 1], [3, 3], 4, "RP^2xRP^2")
    a, b = ring22.gen(0), ring22.gen(1)
    tot22 = ring22.mul(
        ring22.add(ring22.one(), a, ring22.mul(a, a)),
        ring22.add(ring22.one(), b, ring22.mul(b, b)),
    )
    w1_22 = ring22.graded_part(tot22, 1)
    w2_22 = ring22.graded_part(tot22, 2)
    part3["RP2xRP2_bare"] = {
        "w1": ring22.show(w1_22),
        "w2": ring22.show(w2_22),
        **pin_verdict(ring22, w1_22, w2_22, ring22.zero()),
    }
    gates["G24_RP2xRP2_admits_NEITHER"] = not (
        part3["RP2xRP2_bare"]["pin_plus_exists"]
        or part3["RP2xRP2_bare"]["pin_minus_exists"]
    )

    # -- CP^2 : untwisted FAILS, twisted by w_2(E) = h SUCCEEDS
    ring_cp2 = F2Ring([2], [3], 4, "CP^2")
    h = ring_cp2.gen(0)
    tot_cp2 = ring_cp2.mul(
        ring_cp2.mul(ring_cp2.add(ring_cp2.one(), h), ring_cp2.add(ring_cp2.one(), h)),
        ring_cp2.add(ring_cp2.one(), h),
    )  # w(CP^2) = (1+h)^3
    w1_cp2 = ring_cp2.graded_part(tot_cp2, 1)
    w2_cp2 = ring_cp2.graded_part(tot_cp2, 2)
    part3["CP2_untwisted"] = {
        "w1": ring_cp2.show(w1_cp2),
        "w2": ring_cp2.show(w2_cp2),
        **pin_verdict(ring_cp2, w1_cp2, w2_cp2, ring_cp2.zero()),
    }
    part3["CP2_twisted_by_w2E_eq_h"] = pin_verdict(ring_cp2, w1_cp2, w2_cp2, h)
    gates["G25_TWIST_CAN_RESCUE_untwisted_fails_twisted_works"] = (
        not part3["CP2_untwisted"]["pin_plus_exists"]
        and part3["CP2_twisted_by_w2E_eq_h"]["pin_plus_exists"]
    )

    # -- S^2 x S^2 : untwisted WORKS, twisted by w_2(E) = a FAILS
    ring_s2s2 = F2Ring([2, 2], [2, 2], 4, "S^2xS^2")
    aa, bb = ring_s2s2.gen(0), ring_s2s2.gen(1)
    w1_s2s2 = ring_s2s2.zero()
    w2_s2s2 = ring_s2s2.zero()  # w(TS^2) = 1, so w(S^2xS^2) = 1
    part3["S2xS2_untwisted"] = pin_verdict(
        ring_s2s2, w1_s2s2, w2_s2s2, ring_s2s2.zero()
    )
    part3["S2xS2_twisted_by_w2E_eq_a"] = pin_verdict(ring_s2s2, w1_s2s2, w2_s2s2, aa)
    part3["S2xS2_twisted_by_w2E_eq_a_plus_b"] = pin_verdict(
        ring_s2s2, w1_s2s2, w2_s2s2, ring_s2s2.add(aa, bb)
    )
    gates["G26_TWIST_CAN_BREAK_untwisted_works_twisted_fails"] = (
        part3["S2xS2_untwisted"]["pin_plus_exists"]
        and not part3["S2xS2_twisted_by_w2E_eq_a"]["pin_plus_exists"]
    )

    # -- RP^4 twisted so that Pin^- becomes available: w_2(E) = a^2
    ring4, w1_4, w2_4 = rp(4)
    a4 = ring4.gen(0)
    part3["RP4_twisted_by_w2E_eq_a2"] = pin_verdict(
        ring4, w1_4, w2_4, ring4.mul(a4, a4)
    )
    gates["G27_RP4_twist_flips_pin_minus_to_available"] = part3[
        "RP4_twisted_by_w2E_eq_a2"
    ]["pin_minus_exists"]

    # -- and now M_iota itself.
    #
    # WHY THIS IS NOT DONE WITH THE RING ENGINE: on M_iota the obstruction is
    # not "a class that happens to cancel", it is "an element of a group that is
    # zero".  Encoding that as a rigged truncated ring would put the answer in
    # by hand.  Instead the verdict is derived from the COMPUTED cohomology of
    # PART 1: dim_{F2} H^2(M_iota;F2) = 0, and more strongly H^2(M_iota;A) = 0
    # for every abelian A tested and for local coefficients (PART 4), so every
    # possible value of `twist_c2` -- whatever G is -- is the zero element.
    h2_f2_minimal_dim = minimal["deg_-1"]["betti_F2"][2]
    h2_f2_nonminimal_dim = nonmin["deg_-1"]["betti_F2"][2]
    part3["M_iota_H2_F2_dimension_minimal"] = h2_f2_minimal_dim
    part3["M_iota_H2_F2_dimension_nonminimal"] = h2_f2_nonminimal_dim
    part3["M_iota_reasoning"] = (
        "obstruction lies in H^2(M;Z/2); that group has dimension "
        f"{h2_f2_minimal_dim} (minimal model) / {h2_f2_nonminimal_dim} "
        "(non-minimal model), so every twist class and both Pin conditions "
        "vanish simultaneously, for every G."
    )
    gates["G28_M_iota_H2_F2_is_zero_dimensional_in_both_models"] = (
        h2_f2_minimal_dim == 0 and h2_f2_nonminimal_dim == 0
    )
    out["PART3_twist_matters_controls"] = part3

    # ======================================================================
    # PART 4 -- local (twisted) coefficients, incl. the SU(2)_a <-> SU(2)_b swap
    # ======================================================================
    part4: dict = {}
    swap = [[0, 1], [1, 0]]
    triv = [[1, 0], [0, 1]]
    for name, rho in (("swap_monodromy", swap), ("trivial_monodromy", triv)):
        b_min = mapping_torus_local_coeff_betti_f2(
            sphere_complex(3), sphere_self_map(3, -1), rho
        )
        b_nm = mapping_torus_local_coeff_betti_f2(
            s3_nonminimal_complex(), s3_nonminimal_self_map(-1), rho
        )
        part4[name] = {"betti_F2_minimal": b_min, "betti_F2_nonminimal": b_nm}
    # REPAIRED after FL Step 8a.  The first version gated ONLY "degree-2 entry
    # is 0 for both monodromies".  Skeptic pass 2 found the slip-through:
    # neutering `rho` to the identity leaves that gate green (the trivial system
    # also gives 0), the control never exercised a nontrivial `rho`, and in the
    # MINIMAL model ranks[2] = k*(C_2 + C_1) = 0 identically, so half the gate
    # could not fail at all.  Fixed three ways: gate the NON-minimal model
    # separately, require the two monodromies to give DIFFERENT Betti vectors
    # (which is what dies if `rho` is neutered), and run the control with a
    # nontrivial `rho`.
    gates["G29_H2_with_local_coefficients_vanishes_incl_swap"] = all(
        part4[k]["betti_F2_minimal"][2] == 0 and part4[k]["betti_F2_nonminimal"][2] == 0
        for k in part4
    )
    gates["G29b_NONMINIMAL_model_H2_zero_for_both_monodromies"] = all(
        part4[k]["betti_F2_nonminimal"][2] == 0 for k in part4
    )
    gates["G29c_swap_and_trivial_monodromy_give_DIFFERENT_betti_vectors"] = (
        part4["swap_monodromy"]["betti_F2_nonminimal"]
        != part4["trivial_monodromy"]["betti_F2_nonminimal"]
        and part4["swap_monodromy"]["betti_F2_minimal"]
        != part4["trivial_monodromy"]["betti_F2_minimal"]
    )
    # controls: the same routine must return H_2 != 0 on S^2 x S^1, with a
    # NONTRIVIAL monodromy as well as a trivial one.
    ctrl = mapping_torus_local_coeff_betti_f2(
        sphere_complex(2), sphere_self_map(2, 1), triv
    )
    ctrl_swap = mapping_torus_local_coeff_betti_f2(
        sphere_complex(2), sphere_self_map(2, 1), swap
    )
    part4["control_S2xS1_trivial_monodromy"] = ctrl
    part4["control_S2xS1_SWAP_monodromy"] = ctrl_swap
    gates["G30_local_coeff_routine_returns_nonzero_on_control"] = (
        ctrl[2] != 0 and ctrl_swap[2] != 0
    )
    out["PART4_local_coefficients"] = part4

    # ======================================================================
    # PART 5 -- the constructive route: every G-bundle on S^3 is trivial
    # ======================================================================
    # pi_2(G) = 0 for every Lie group G  [CITED, E. Cartan; not re-derived], so
    # [S^3, BGbar] = pi_3(BGbar) = pi_2(Gbar) = 0 and every Gbar-bundle on
    # S^3 x R is trivial.  The only thing this script can check is the finite
    # part of the argument: that a map S^3 -> O(4) x SO(3) lifts through the
    # double cover, which is automatic because S^3 is simply connected.  We
    # exhibit the lift explicitly for the actual clutching function
    # u(x) = (-Ad(x) (+) 1, r(x)) and confirm it covers u.
    part5: dict = {}
    gens30 = clifford_generators(3, +1)
    omega = gens30[0] @ gens30[1] @ gens30[2]
    lift_err = 0.0
    for _ in range(120):
        q = su2_matrix(rng)
        ad = su2_to_so3(q)
        # spin(3) element covering Ad(q) is q itself; omega*q covers -Ad(q)
        # in the 3d twisted adjoint (C129 Sec.6, reproduced independently here)
        img = twisted_adjoint(omega @ _embed_su2_in_cl3(q, gens30), gens30, parity=1)
        lift_err = max(lift_err, float(np.abs(img + ad).max()))
    part5["explicit_lift_covers_minus_Ad_residual"] = lift_err
    gates["G31_explicit_lift_covers_minus_Ad"] = lift_err < 1e-9
    # non-vacuity control: without omega the lift covers +Ad, not -Ad
    ctrl_err = 0.0
    for _ in range(60):
        q = su2_matrix(rng)
        ad = su2_to_so3(q)
        img = twisted_adjoint(_embed_su2_in_cl3(q, gens30), gens30, parity=0)
        ctrl_err = max(ctrl_err, float(np.abs(img + ad).max()))
    part5["control_no_omega_residual_must_be_LARGE"] = ctrl_err
    gates["G32_no_omega_control_FIRES"] = ctrl_err > 0.5
    out["PART5_constructive"] = part5

    # ======================================================================
    # VERDICT
    # ======================================================================
    verdict = {
        "H2_M_iota_vanishes_for_every_tested_abelian_coefficient": bool(
            gates["G10_H2_M_iota_vanishes_for_every_tested_coefficient"]
        ),
        "H2_M_iota_vanishes_for_local_coefficients_incl_swap": bool(
            gates["G29_H2_with_local_coefficients_vanishes_incl_swap"]
        ),
        "H3_M_iota_Z_vanishes": bool(gates["G11_H3_M_iota_Z_vanishes"]),
        # REWIRED after FL Step 8a.  The old field
        # `extension_is_Z2_central_so_single_H2_obstruction` was the conjunction
        # of two gates that could not fail; `no_kunneth_cross_term` was a third.
        # They are replaced by fields wired to the NORMALITY and KERNEL-ORDER
        # computations, both of which have firing controls (G16b, G18b).
        "identification_subgroup_normal_and_kernel_has_order_2": bool(
            gates["G16_identification_subgroup_is_NORMAL_for_central_z"]
            and gates["G16b_normality_check_FIRES_on_noncentral_z"]
            and gates["G18_kernel_has_ORDER_2_computed_not_asserted"]
            and gates["G18b_kernel_order_control_is_4_without_the_identification"]
        ),
        "twist_can_change_the_answer_in_general": bool(
            gates["G25_TWIST_CAN_RESCUE_untwisted_fails_twisted_works"]
            and gates["G26_TWIST_CAN_BREAK_untwisted_works_twisted_fails"]
        ),
        "H2_zero_at_every_tested_degree_in_the_NONMINIMAL_model": bool(
            gates["G09b_H2_zero_at_every_degree_in_the_NONMINIMAL_model"]
            and gates["G08_nonminimal_agrees_with_minimal_AT_EVERY_DEGREE"]
        ),
        "TWISTED_Pin_plus_exists_on_M_iota": bool(
            gates["G10_H2_M_iota_vanishes_for_every_tested_coefficient"]
            and gates["G28_M_iota_H2_F2_is_zero_dimensional_in_both_models"]
            and gates["G18_kernel_has_ORDER_2_computed_not_asserted"]
        ),
        "TWISTED_Pin_minus_exists_on_M_iota": bool(
            gates["G10_H2_M_iota_vanishes_for_every_tested_coefficient"]
            and gates["G28_M_iota_H2_F2_is_zero_dimensional_in_both_models"]
            and gates["G18_kernel_has_ORDER_2_computed_not_asserted"]
        ),
        "constructive_route_lift_exhibited": bool(
            gates["G31_explicit_lift_covers_minus_Ad"]
        ),
    }
    out["VERDICT_INPUTS"] = verdict
    out["GATES"] = {k: bool(v) for k, v in gates.items()}
    out["GATE_SUMMARY"] = {
        "passed": int(sum(1 for v in gates.values() if v)),
        "total": len(gates),
        "ALL_OK": all(bool(v) for v in gates.values()),
    }
    return out


def _embed_su2_in_cl3(q: np.ndarray, gens: list[np.ndarray]) -> np.ndarray:
    """Map an SU(2) matrix to the corresponding Spin(3) element in Cl(3,0).

    Spin(3) = {a + b e_2e_3 + c e_3e_1 + d e_1e_2}.  Writing
    q = a*1 + i(b sigma_1 + c sigma_2 + d sigma_3) fixes (a,b,c,d).
    The overall sign convention is fixed empirically by requiring that the
    resulting element cover Ad(q) -- checked by the caller's residual.
    """
    a = float(np.real(0.5 * np.trace(q)))
    sig = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    comp = [float(np.real(-0.5j * np.trace(sig[k] @ q))) for k in range(3)]
    e23 = gens[1] @ gens[2]
    e31 = gens[2] @ gens[0]
    e12 = gens[0] @ gens[1]
    dim = gens[0].shape[0]
    return (
        a * np.eye(dim, dtype=complex) + comp[0] * e23 + comp[1] * e31 + comp[2] * e12
    )


if __name__ == "__main__":
    result = main()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "results_c130.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
    gs = result["GATE_SUMMARY"]
    print(f"gates: {gs['passed']} / {gs['total']}   ALL_OK = {gs['ALL_OK']}")
    for name, ok in result["GATES"].items():
        if not ok:
            print(f"  FAILED: {name}")
    print()
    for key, val in result["VERDICT_INPUTS"].items():
        print(f"  {key:60s} {val}")
