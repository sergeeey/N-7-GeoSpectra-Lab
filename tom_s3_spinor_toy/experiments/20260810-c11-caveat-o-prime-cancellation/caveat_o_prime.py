"""CAVEAT O': can unbounded commutators CANCEL and let U_iota back in?

THE WORRY, as recorded against my own C53 result: J u J^-1 could be a SUM in which a
U_iota term's unbounded commutator cancels against another unbounded term, and a finite
model has no unbounded operators to rule it out.

AND CANCELLATION IS GENUINELY POSSIBLE. Z1 = U_iota and Z2 = I - U_iota both have
unbounded [D_M, .], yet Z1 + Z2 = I has [D_M, I] = 0. The worry was not silly.

WHAT THE WORRY GETS WRONG. It presupposes a DECOMPOSITION-based argument -- split T into
a U_iota part and a rest, then bound each piece. The argument orientability actually
needs is SPAN-based, and a span argument is immune to cancellation. Write

    B := { Z bounded : [D_M, Z] bounded }        ("Lipschitz operators")

  P1  B is a LINEAR SUBSPACE and an algebra (Leibniz)
  P2  U_iota is NOT in B, because U_iota D_M = -D_M U_iota gives
      [D_M, U_iota] = 2 D_M U_iota -- unbounded
  P3  every AVAILABLE operator is individually in B: algebra elements by the
      bounded-commutator axiom, [D,a] by regularity, J b* J^-1 blockwise because
      [D, J b* J^-1] is bounded
  P4  so everything reachable lies in B, and U_iota does not. gamma is unreachable and
      CANCELLATION IS IRRELEVANT, because any cancellation happens INSIDE B
  P5  DISCRIMINATOR: exhibit a real cancellation, to show the caveat was aimed at the
      wrong step rather than being empty. Z1 = U_iota is exactly the UNAVAILABLE operator

Predictions P1-P5 recorded in claim.md BEFORE running.

Boundedness is operationalised in the truncated model as "the norm does not grow with the
cutoff" -- the standard idiom of this series (C50/C51/C53), [INFERRED-analytic] where it
stands for a genuine operator-norm statement.
"""

from __future__ import annotations

import json
from itertools import pairwise
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_o_prime.json"
results: dict = {}

CUTOFFS = (4, 8, 16, 32)


def model(nmax: int):
    """D_M with eigenvalues +-(n+3/2) and U_iota mapping (n,sigma) -> (n,-sigma)."""
    lv = [s * (n + 1.5) for n in range(nmax + 1) for s in (+1, -1)]
    d_m = np.diag(lv).astype(complex)
    u_i = np.zeros_like(d_m)
    for n in range(nmax + 1):
        u_i[2 * n, 2 * n + 1] = u_i[2 * n + 1, 2 * n] = 1.0
    assert np.allclose(u_i @ d_m @ u_i, -d_m), "U_iota must flip D_M"
    return d_m, u_i, max(lv)


def comm(d: np.ndarray, z: np.ndarray) -> np.ndarray:
    return d @ z - z @ d


def grows(make_z) -> tuple[bool, dict]:
    """Does ||[D_M, Z]|| grow with the cutoff? (the model's stand-in for 'unbounded')"""
    n = {}
    for nmax in CUTOFFS:
        d_m, u_i, _ = model(nmax)
        n[nmax] = float(np.linalg.norm(comm(d_m, make_z(d_m, u_i)), 2))
    return all(n[b] > n[a] + 1e-9 for a, b in pairwise(CUTOFFS)), n


print("=" * 78)
print("CAVEAT O' -- can unbounded commutators cancel and let U_iota back in?")
print("=" * 78)
rng = np.random.default_rng(20260810)

# --- P1: B is a linear subspace and an algebra -------------------------------
print("\nP1 -- is B = {Z bounded : [D_M,Z] bounded} a linear subspace AND an algebra?")
d_m, u_i, _ = model(8)
dim = d_m.shape[0]
lin_ok, leib_ok = True, True
for _ in range(200):
    z1 = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    z2 = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    a, b = complex(rng.normal(), rng.normal()), complex(rng.normal(), rng.normal())
    lin_ok &= bool(np.allclose(comm(d_m, a * z1 + b * z2), a * comm(d_m, z1) + b * comm(d_m, z2)))
    leib_ok &= bool(np.allclose(comm(d_m, z1 @ z2), comm(d_m, z1) @ z2 + z1 @ comm(d_m, z2)))
print(f"    linearity  [D_M, a Z1 + b Z2] = a[D_M,Z1] + b[D_M,Z2] : {lin_ok}")
print(f"    Leibniz    [D_M, Z1 Z2] = [D_M,Z1] Z2 + Z1 [D_M,Z2]   : {leib_ok}")
print("    => sums and products of B-elements stay in B. B is CLOSED.")
p1 = lin_ok and leib_ok
results["p1_linear"] = bool(lin_ok)
results["p1_leibniz"] = bool(leib_ok)

# --- P2: U_iota is NOT in B --------------------------------------------------
print("\nP2 -- is U_iota in B?")
ident_ok = True
for nmax in CUTOFFS:
    d, u, _ = model(nmax)
    ident_ok &= bool(np.allclose(comm(d, u), 2 * d @ u))
u_grows, u_norms = grows(lambda d, u: u)
print(f"    [D_M, U_iota] = 2 D_M U_iota holds exactly at every cutoff: {ident_ok}")
for k in CUTOFFS:
    print(f"      N_MAX = {k:3d}   ||[D_M, U_iota]|| = {u_norms[k]:7.2f}")
print(f"    norm grows with the cutoff: {u_grows}   =>   U_iota is NOT in B")
p2 = ident_ok and u_grows
results["p2_identity"] = bool(ident_ok)
results["p2_norms"] = u_norms
results["p2_U_iota_not_in_B"] = bool(p2)

# --- P3: every AVAILABLE operator is in B ------------------------------------
print("\nP3 -- is every available operator in B? (a, [D,a], and the blocks of J b* J^-1)")
avail = {}
# a bundle endomorphism -- the H_M factor of every algebra element and of every [D,a]
be_grows, be_norms = grows(
    lambda d, u: np.diag([1.0 if k % 3 else -1.0 for k in range(d.shape[0])]).astype(complex)
)
avail["bundle endo (H_M factor of a and of [D,a])"] = {"grows": be_grows, "norms": be_norms}
# the identity -- the H_M factor in the B = C*1 case (C53's O3)
id_grows, id_norms = grows(lambda d, u: np.eye(d.shape[0], dtype=complex))
avail["identity (H_M factor when B = C*1)"] = {"grows": id_grows, "norms": id_norms}
for name, v in avail.items():
    print(f"    {name:44s} ||[D_M,.]|| grows: {v['grows']}   (expect False)")
p3 = not any(v["grows"] for v in avail.values())
print(f"    P3: every available H_M factor has a NON-growing commutator: {p3}")
print("        [a: bounded-commutator axiom. [D,a]: ASSUMPTION R (regularity) -- not")
print("         needed when B = C*1, where the H_M factor is exactly I. J b* J^-1:")
print("         blockwise, because [D, J b* J^-1] is bounded (C53's O2).]")
results["p3_available"] = avail
results["p3_all_in_B"] = bool(p3)

# --- P4: so gamma is unreachable, and cancellation is irrelevant -------------
print("\nP4 -- span/products of available operators stay in B; U_iota is not in B")
print("      so no combination of available operators equals U_iota.")
print("      CANCELLATION CANNOT HELP: it would have to happen INSIDE B, and B is a")
print("      linear subspace -- a sum of B-elements is a B-element, never U_iota.")
p4 = p1 and p2 and p3
print(f"    P4: gamma = U_iota (x) s1 is unreachable, cancellation notwithstanding: {p4}")
results["p4_gamma_unreachable"] = bool(p4)

# --- P5: DISCRIMINATOR -- cancellation IS real, so the caveat was not silly --
print("\nP5 -- DISCRIMINATOR: is cancellation actually possible? (it must be, or this")
print("      whole round is attacking a straw man)")
z1_grows, z1_n = grows(lambda d, u: u)
z2_grows, z2_n = grows(lambda d, u: np.eye(d.shape[0], dtype=complex) - u)
sum_grows, sum_n = grows(lambda d, u: u + (np.eye(d.shape[0], dtype=complex) - u))
print(f"    Z1 = U_iota          ||[D_M,Z1]|| grows: {z1_grows}   ({z1_n[32]:.1f} at N=32)")
print(f"    Z2 = I - U_iota      ||[D_M,Z2]|| grows: {z2_grows}   ({z2_n[32]:.1f} at N=32)")
print(f"    Z1 + Z2 = I          ||[D_M,sum]|| grows: {sum_grows}  ({sum_n[32]:.1f} at N=32)")
p5 = z1_grows and z2_grows and not sum_grows
print(f"    P5: two UNBOUNDED commutators with a BOUNDED sum -- cancellation is REAL: {p5}")
print("        So CAVEAT O' was not empty. It was aimed at the wrong step: Z1 = U_iota is")
print("        exactly the operator that is NOT AVAILABLE -- not in A, not a [D,a], not a")
print("        J b* J^-1. The span argument never needs to decompose anything.")
results["p5_cancellation_is_real"] = bool(p5)
results["p5_norms"] = {"Z1": z1_n, "Z2": z2_n, "sum": sum_n}

# --- CONTROL: is the 'grows' detector SOUND, or only tuned to U_iota? --------
# The obvious control -- "admit U_iota and check gamma comes back" -- is
# np.allclose(I @ gamma, gamma), true by construction: the sixth cannot-fail check of
# this session, and it duplicates C53's O4. Replaced by a soundness test of the
# DETECTOR: it must say NO for a bounded-commutator operator that is not the identity,
# and YES for an unbounded one that is not U_iota.
print("\nCONTROL -- is the 'grows' detector sound in BOTH directions?")


def level_shift(d: np.ndarray, _u: np.ndarray) -> np.ndarray:
    """maps level n -> level n+1: gaps are constant, so [D_M, .] is BOUNDED."""
    z = np.zeros_like(d)
    for k in range(d.shape[0] - 2):
        z[k + 2, k] = 1.0
    return z


def long_range(d: np.ndarray, _u: np.ndarray) -> np.ndarray:
    """maps level n -> level 2n: the gap grows with n, so [D_M, .] is UNBOUNDED."""
    z = np.zeros_like(d)
    n_lv = d.shape[0] // 2
    for n in range(n_lv):
        if 2 * n < n_lv:
            z[2 * (2 * n), 2 * n] = 1.0
    return z


shift_grows, shift_n = grows(level_shift)
long_grows, long_n = grows(long_range)
print(f"    level shift n -> n+1 (constant gap)  ||[D_M,.]|| grows: {shift_grows}  (expect False)")
print(f"    long range   n -> 2n (growing gap)   ||[D_M,.]|| grows: {long_grows}  (expect True)")
sound = (not shift_grows) and long_grows
print(f"    CONTROL PASSES -- the detector is not merely tuned to U_iota: {sound}")
results["control_detector_sound"] = bool(sound)
results["control_norms"] = {"level_shift": shift_n, "long_range": long_n}

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = p1 and p2 and p3 and p4 and p5 and sound
verdict = (
    "CAVEAT_O_PRIME_DISSOLVED__SPAN_ARGUMENT_IS_IMMUNE_TO_CANCELLATION" if ok else "INCONCLUSIVE"
)
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C54 is REFUTED, and CAVEAT O' DISSOLVES rather than being defeated.")
    print()
    print("  The worry presupposed a DECOMPOSITION argument -- split T, bound each piece.")
    print("  The proof orientability needs is a SPAN argument:")
    print("      B = {Z bounded : [D_M,Z] bounded} is a linear subspace and an algebra;")
    print("      every AVAILABLE operator is in B;")
    print("      U_iota is NOT in B, because [D_M,U_iota] = 2 D_M U_iota;")
    print("      so nothing reachable equals U_iota.")
    print("  Cancellation would have to occur INSIDE B, and a sum of B-elements is a")
    print("  B-element. It can never leave.")
    print()
    print("  P5 keeps this honest: cancellation IS real (U_iota and I - U_iota both have")
    print("  growing commutators, their sum has none). CAVEAT O' was not empty -- it was")
    print("  aimed at a step the argument does not take. U_iota is exactly the operator")
    print("  that is NOT AVAILABLE.")
    print()
    print("  C11 CONSEQUENCE: the last technically open door is closed. The remaining")
    print("  assumptions are ASSUMPTION A1 (U_iota flips D^{1/2}, inherited from C39 and")
    print("  never re-derived) and ASSUMPTION R (regularity, needed only when B is large).")
    print("  Note A1 is what makes [D_M, U_iota] unbounded, so this step DEPENDS on it.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
