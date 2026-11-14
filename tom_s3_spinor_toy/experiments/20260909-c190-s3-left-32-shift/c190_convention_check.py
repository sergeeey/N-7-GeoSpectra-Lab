"""Independent re-check of the C180 vs C189/C190 sign-convention question.

Builds D0^R = -i sum_a sigma_a (x) X_a^R and D0^L = -i sum_a sigma_a (x) X_a^L directly on the
harmonic degree-k polynomials of R^4 (k=0..3), X_a^R(f)(q) = d/dt f(q e^{t e_a}),
X_a^L(f)(q) = d/dt f(e^{t e_a} q), with e_a = i, j, k quaternion units.  No spin connection,
no literature value.  Then asks, for each handedness, which constant c makes D0 - c equal the
physical Dirac spectrum +-(l+3/2), mult (l+1)(l+2) per sign (C180 convention), and what the
additive shift s = D_full - D0 = -c is (C189/C190 convention).
"""

from __future__ import annotations

import itertools
from collections import Counter

import numpy as np
import sympy as sp

x = sp.symbols("x0:4")
# quaternion q = x0 + x1 i + x2 j + x3 k as a 4-vector; left/right multiplication matrices by unit e_a


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    )


units = [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
q = tuple(x)
right_fields = [qmul(q, e) for e in units]  # vector field at q is q*e_a
left_fields = [qmul(e, q) for e in units]  # vector field at q is e_a*q


def apply_field(field, f):
    return sp.expand(sum(field[m] * sp.diff(f, x[m]) for m in range(4)))


def laplacian(f):
    return sp.expand(sum(sp.diff(f, x[m], 2) for m in range(4)))


def harmonic_basis(k):
    monos = [
        sp.Mul(*[x[i] ** e[i] for i in range(4)])
        for e in itertools.product(range(k + 1), repeat=4)
        if sum(e) == k
    ]
    cs = sp.symbols(f"c0:{len(monos)}")
    f = sum(c * m for c, m in zip(cs, monos))
    lap = sp.Poly(laplacian(f), *x)
    eqs = list(lap.coeffs()) if lap.coeffs() else []
    sol = sp.linsolve(eqs, *cs) if eqs else None
    if sol:
        (s,) = list(sol)
        free = sorted(
            set().union(*[sp.sympify(v).free_symbols for v in s]), key=lambda z: str(z)
        )
        basis = []
        for fv in free:
            sub = {z: (1 if z == fv else 0) for z in free}
            vec = [sp.sympify(v).subs(sub) for v in s]
            basis.append(sp.expand(sum(c * m for c, m in zip(vec, monos))))
        return basis
    return monos


def coeff_vec(f, k, mono_index):
    p = sp.Poly(f, *x)
    v = np.zeros(len(mono_index))
    for mon, c in p.terms():
        v[mono_index[mon]] = float(c)
    return v


def operator_matrices(fields, k):
    basis = harmonic_basis(k)
    mons = sorted(
        {m for f in basis for m, _ in sp.Poly(f, *x).terms()}
        | {
            m
            for f in basis
            for fld in fields
            for m, _ in sp.Poly(apply_field(fld, f), *x).terms()
        }
    )
    idx = {m: i for i, m in enumerate(mons)}
    B = np.stack(
        [coeff_vec(f, k, idx) for f in basis], axis=1
    )  # monomial coords of basis
    mats = []
    for fld in fields:
        img = np.stack([coeff_vec(apply_field(fld, f), k, idx) for f in basis], axis=1)
        M, *_ = np.linalg.lstsq(B, img, rcond=None)
        assert np.allclose(B @ M, img, atol=1e-10), (
            "X_a does not preserve the harmonic space"
        )
        mats.append(M)
    return mats


sigma = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def d0_spectrum(fields, k):
    mats = operator_matrices(fields, k)
    D = sum(np.kron(sigma[a], -1j * mats[a]) for a in range(3))
    # the monomial basis is not orthonormal in L2(S^3), so D need not look Hermitian here; the
    # spectrum is basis independent, and must be real
    ev = np.linalg.eigvals(D)
    assert np.max(np.abs(ev.imag)) < 1e-8, "complex eigenvalues"
    ev = np.sort(ev.real)
    return Counter(np.round(ev, 6))


def physical(kmax):
    """+-(l+3/2), multiplicity (l+1)(l+2) per sign, l = 0..kmax"""
    out = Counter()
    for l in range(kmax + 1):
        out[round(l + 1.5, 6)] += (l + 1) * (l + 2)
        out[round(-(l + 1.5), 6)] += (l + 1) * (l + 2)
    return out


KMAX = 3
specs = {"R": Counter(), "L": Counter()}
per_k = {}
for k in range(KMAX + 1):
    for name, flds in (("R", right_fields), ("L", left_fields)):
        sp_k = d0_spectrum(flds, k)
        per_k[(name, k)] = sp_k
        specs[name].update(sp_k)
for name in "RL":
    print(f"D0^{name} per level:", {k: dict(per_k[(name, k)]) for k in range(KMAX + 1)})

# truncation: compare only eigenvalues with |value| <= KMAX+1/2.  For the CORRECT shift that window is
# complete (all l<=KMAX).  For the WRONG shift, mismatching values just outside the window (e.g. -2.5,
# -3.5 need levels k=4,5) are not examined, so the reported mismatch count is a lower bound; the 0-versus-7
# contrast is unaffected (the spectrum of D0 is not symmetric under negation).
phys = physical(KMAX)


def match(spec, shift):
    shifted = Counter()
    for v, m in spec.items():
        shifted[round(v + shift, 6)] += m
    lim = KMAX + 0.5 + 1e-9
    keys = [v for v in set(shifted) | set(phys) if abs(v) <= lim]
    bad = {
        v: (shifted.get(v, 0), phys.get(v, 0))
        for v in keys
        if shifted.get(v, 0) != phys.get(v, 0)
    }
    return bad


results = {}
for name in "RL":
    for shift in (-1.5, +1.5):
        bad = match(specs[name], shift)
        results[(name, shift)] = len(bad)
        print(
            f"D0^{name} + ({shift:+.1f}): mismatching eigenvalue values within |lambda|<={KMAX + 0.5}: {len(bad)}"
        )

# mirror check: spectrum of D0^L is the negation of D0^R, level by level
for k in range(KMAX + 1):
    neg = Counter({round(-v, 6): m for v, m in per_k[("R", k)].items()})
    print(f"k={k}: spec(D0^L) == -spec(D0^R): {neg == per_k[('L', k)]}")

print()
print(
    "shift s = D_full - D0 that reproduces +-(l+3/2):",
    {n: s for (n, s), bad in results.items() if bad == 0},
)
print(
    "so c = D0 - D_phys = -s:", {n: -s for (n, s), bad in results.items() if bad == 0}
)
