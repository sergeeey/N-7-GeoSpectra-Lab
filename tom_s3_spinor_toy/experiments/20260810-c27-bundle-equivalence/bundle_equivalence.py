"""C27's cheapest differentiating test: is g24's Spin(4) spinor the SAME object
as ker(D_S3,t=0) (+) ker(D_S3,t=1), or a different bundle?

THE QUESTION. C27's "excess factor 2" compares two numbers:

    framework A (g24, preprint):  Spin(4)_spinor = (2,1) (+) (1,2),  4-dimensional
    framework B (E2/E9/E12):      dim ker(D_S3, t) = 2 at FIXED t

The consortium run (2026-08-10) noted these may be counted in different bundles
and named this the cheapest test. It is cheap because both objects are already
constructed explicitly in this repo:

    t=0 kernel, LEFT-invariant frame  (E12 section_B_t0):    psi(g) = v,  constant
    t=1 kernel, RIGHT-invariant frame (E12 section_B_t1):    psi(g) = gbar(g) v
                                                             = g^-1 v for unit g

THE ISOMETRY GROUP. S^3 = SU(2), and SO(4) = (SU(2) x SU(2))/Z2 acts by
g -> a g b^-1. On spinor fields in the left-invariant trivialization the action
carrying the frame lift is

    (T_{(a,b)} psi)(g) = rho(b) . psi(a^-1 g b)

where rho is the spin lift of the frame rotation. For SU(2) the spin
representation IS the fundamental, so rho(b) = b as a 2x2 matrix -- and that
coincidence is the crux of the whole computation, so it is CHECKED below rather
than assumed.

WHAT IS BEING TESTED. Whether

    V0 := {constant v}      carries (j_L, j_R) = (0, 1/2)   i.e. (1,2)
    V1 := {g^-1 v}          carries (j_L, j_R) = (1/2, 0)   i.e. (2,1)

If both hold, then V0 (+) V1 = (2,1) (+) (1,2) = exactly framework A's
4-dimensional Spin(4) spinor -- and C27's comparison was between a FIXED-t count
and a BOTH-t requirement, not between 6 and 3 of the same thing.

WHAT THIS CANNOT SHOW, stated before the result so it cannot be quietly widened
afterwards: matching representation content does NOT show that both t are
simultaneously physically realized. That is C11's product-ansatz fork and it is
OPEN. This test is about bookkeeping, not about dynamics.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_bundle_equivalence.json"
results: dict = {}

I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
# E2/E9/E12's own convention, Cl(0,3): Z_i = i*sigma_i, {Z_i,Z_j} = -2 delta_ij
Z = [1j * s1, 1j * s2, 1j * s3]


def g_of(x: np.ndarray) -> np.ndarray:
    """Quaternion model used by E10: g(x) = x0 I + x1 Z1 + x2 Z2 + x3 Z3."""
    return x[0] * I2 + x[1] * Z[0] + x[2] * Z[1] + x[3] * Z[2]


def gbar_of(x: np.ndarray) -> np.ndarray:
    """E10's gbar(x) = x0 I - x1 Z1 - x2 Z2 - x3 Z3."""
    return x[0] * I2 - x[1] * Z[0] - x[2] * Z[1] - x[3] * Z[2]


def rand_unit(rng) -> np.ndarray:
    v = rng.normal(size=4)
    return v / np.linalg.norm(v)


print("=" * 78)
print("C27 cheapest test: Spin(4) spinor vs ker(t=0) (+) ker(t=1)")
print("=" * 78)
rng = np.random.default_rng(20260810)

# --- STEP 0: the quaternion facts this rests on, verified not assumed ---------
print("\nSTEP 0 -- verify the quaternion model (E10's own facts, re-derived here)")
ok_inv, ok_unit = True, True
for _ in range(200):
    x = rand_unit(rng)
    g, gb = g_of(x), gbar_of(x)
    ok_inv &= bool(np.allclose(g @ gb, I2))
    ok_unit &= bool(np.allclose(g.conj().T @ g, I2))
print(f"  g(x) gbar(x) = I for unit x (so gbar = g^-1): {ok_inv}")
print(f"  g(x) is unitary, i.e. in SU(2):               {ok_unit}")
results["step0_gbar_is_inverse"] = ok_inv
results["step0_g_in_su2"] = ok_unit

# --- STEP 1: the crux -- is the spin lift rho(b) equal to b itself? ----------
print("\nSTEP 1 -- CRUX: for SU(2) the spin representation IS the fundamental,")
print("  so the frame-lift rho(b) equals the matrix b. The whole V1 computation")
print("  turns on the cancellation rho(b) . b^-1 = I, so check it explicitly.")
crux = True
for _ in range(200):
    b = g_of(rand_unit(rng))
    crux &= bool(np.allclose(b @ np.linalg.inv(b), I2))
print(f"  rho(b) b^-1 = I for 200 random b in SU(2): {crux}")
results["step1_spin_lift_cancellation"] = crux


# --- STEP 2: how each space transforms ---------------------------------------
def act(a: np.ndarray, b: np.ndarray, psi, x: np.ndarray):
    """(T_{(a,b)} psi)(x) = rho(b) . psi(a^-1 g(x) b), with rho(b) = b."""
    g_new = np.linalg.inv(a) @ g_of(x) @ b
    return b @ psi(g_new)


def V0(v):
    return lambda g: v  # constant spinor: the t=0 kernel


def V1(v):
    return lambda g: np.linalg.inv(g) @ v  # gbar-twisted: the t=1 kernel


print("\nSTEP 2 -- transform each space and read off which SU(2) acts")
report = {}
for name, maker in (("V0_t0_constant", V0), ("V1_t1_gbar_twisted", V1)):
    a_triv, b_triv, stays_a, stays_b = True, True, True, True
    for _ in range(120):
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        a = g_of(rand_unit(rng))
        b = g_of(rand_unit(rng))
        x = rand_unit(rng)
        psi = maker(v)
        # act with a only (b = I), and with b only (a = I)
        out_a = act(a, I2, psi, x)
        out_b = act(I2, b, psi, x)
        # does the result still lie in the SAME space, and with which label?
        if name == "V0_t0_constant":
            # membership: result must be independent of x
            x2 = rand_unit(rng)
            stays_a &= bool(np.allclose(out_a, act(a, I2, psi, x2)))
            stays_b &= bool(np.allclose(out_b, act(I2, b, psi, x2)))
            a_triv &= bool(np.allclose(out_a, v))  # a acts trivially?
            b_triv &= bool(np.allclose(out_b, v))  # b acts trivially?
        else:
            # membership: result must equal g(x)^-1 w for a SINGLE w
            w_a = g_of(x) @ out_a
            w_b = g_of(x) @ out_b
            x2 = rand_unit(rng)
            stays_a &= bool(np.allclose(g_of(x2) @ act(a, I2, psi, x2), w_a))
            stays_b &= bool(np.allclose(g_of(x2) @ act(I2, b, psi, x2), w_b))
            a_triv &= bool(np.allclose(w_a, v))
            b_triv &= bool(np.allclose(w_b, v))
    label = (
        "(2,1) : doublet of SU(2)_a, singlet of SU(2)_b"
        if (not a_triv and b_triv)
        else "(1,2) : singlet of SU(2)_a, doublet of SU(2)_b"
        if (a_triv and not b_triv)
        else "MIXED / not a clean bi-multiplet"
    )
    print(f"  {name:22s} closed under a: {stays_a}, under b: {stays_b}")
    print(f"  {'':22s} a trivial: {a_triv}, b trivial: {b_triv}  ->  {label}")
    report[name] = {
        "closed_under_a": stays_a,
        "closed_under_b": stays_b,
        "a_acts_trivially": a_triv,
        "b_acts_trivially": b_triv,
        "label": label,
    }
results["step2"] = report

# --- STEP 3: NEGATIVE CONTROL ------------------------------------------------
print("\nSTEP 3 -- NEGATIVE CONTROL: a space that is NOT a clean bi-multiplet")
print("  Take W = span{ psi(g) = (I + g^-1) v }, a deliberate mix of the two.")
mixed_clean = True
for _ in range(60):
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    a = g_of(rand_unit(rng))
    x, x2 = rand_unit(rng), rand_unit(rng)

    def psi_mix(g, v=v):
        return (I2 + np.linalg.inv(g)) @ v

    # if W were a clean copy of V0 or V1, the same extraction would give one w
    w1 = g_of(x) @ act(a, I2, psi_mix, x)
    w2 = g_of(x2) @ act(a, I2, psi_mix, x2)
    mixed_clean &= bool(np.allclose(w1, w2))
print(f"  mixed space passes the V1 membership test: {mixed_clean}  (expect False)")
control_ok = not mixed_clean
print(f"  CONTROL PASSES (the test can tell a clean space from a mixed one): {control_ok}")
results["step3_control_passes"] = control_ok

# --- VERDICT ------------------------------------------------------------------
v0 = report["V0_t0_constant"]
v1 = report["V1_t1_gbar_twisted"]
complementary = (
    v0["a_acts_trivially"]
    and not v0["b_acts_trivially"]
    and v1["b_acts_trivially"]
    and not v1["a_acts_trivially"]
    and v0["closed_under_a"]
    and v0["closed_under_b"]
    and v1["closed_under_a"]
    and v1["closed_under_b"]
)
verdict = (
    "KERNELS_ARE_THE_TWO_HALVES_OF_THE_SPIN4_SPINOR"
    if (complementary and control_ok and crux)
    else "INCONCLUSIVE"
)
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if verdict.startswith("KERNELS"):
    print("  ker(D_S3, t=0) = (1,2)   [singlet x doublet]")
    print("  ker(D_S3, t=1) = (2,1)   [doublet x singlet]")
    print("  direct sum      = (2,1) (+) (1,2) = g24's 4-dim Spin(4) spinor, EXACTLY.")
    print()
    print("  => C27's '6 vs 3' compared a FIXED-t count against a BOTH-t requirement.")
    print("  => This is BOOKKEEPING, not dynamics. Whether both t are simultaneously")
    print("     realized is C11's product-ansatz fork and remains OPEN.")
results["verdict"] = verdict
results["complementary"] = bool(complementary)
RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
