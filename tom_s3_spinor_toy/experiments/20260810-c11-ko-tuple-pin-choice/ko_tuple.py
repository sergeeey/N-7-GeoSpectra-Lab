"""The KO-dimension tuple of the doubled triple -- and whether the Pin choice changes it.

WHAT IS BEING CLOSED. C48 computed the sector-factor signs and then wrote: "NOT a
KO-dimension claim ... combining them with S^3's own tuple is exactly the step C36 showed
is easy to get wrong. Left OPEN rather than asserted." C56 then reported that the eps''
sign FLIPS with the Pin+/Pin- choice, leaving the tuple as the one item still open.

WORTH SAYING UP FRONT: C49 showed the index pairing vanishes and Poincare duality fails;
C52 showed orientability fails. The doubled triple is ALREADY KNOWN not to be a spectral
geometry. This is bookkeeping on a non-geometry -- closure and correction, not discovery.

ANTILINEAR OPERATORS. J(v) = M conj(v) for a matrix M. Then, as linear operators,
    J X J^-1 = M conj(X) M^-1        and        J^2 = M conj(M).
Both are used below; nothing else about J is assumed.

PREDICTIONS K1-K5 and CTRL are recorded in claim.md BEFORE this ran. K4 is the one I
expect to fire, i.e. to CORRECT my own C56 claim: C56's U5 looked only at
J(cX)J^-1 = conj(c) J X J^-1 and never asked what J_M does to U_iota -- which carries the
same phase in the opposite direction.

THE KO TABLE IS NOT RE-DERIVED. The identification of a sign tuple with a KO-dimension
mod 8 follows CCM 2006 / Connes and is used as [DOCS] -- the same handling preprint.tex
now gives J_F after C36.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ko.json"
results: dict = {}

N_MAX = 3
I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[-1, 0], [0, 1]], dtype=complex)  # sector s3 = diag(-1,+1)
EPS2 = np.array([[0, 1], [-1, 0]], dtype=complex)  # i*sigma_2, REAL

# --- KO table, [DOCS] -- CCM 2006 / Connes. NOT re-derived here. -------------
KO_TABLE = {  # n mod 8 : (eps = J^2, eps' = JD/DJ, eps'' = J gamma / gamma J or None)
    0: (+1, +1, +1),
    1: (+1, -1, None),
    2: (-1, +1, -1),
    3: (-1, +1, None),
    4: (-1, +1, +1),
    5: (-1, -1, None),
    6: (+1, +1, -1),
    7: (+1, +1, None),
}


def lookup(eps: int, eps_p: int, eps_pp: int | None) -> list[int]:
    return [n for n, tpl in KO_TABLE.items() if tpl == (eps, eps_p, eps_pp)]


# --- the S^3 factor ----------------------------------------------------------
lv = [(n, s) for n in range(N_MAX + 1) for s in (+1, -1)]
DM = np.kron(np.diag([s * (n + 1.5) for n, s in lv]), I2).astype(complex)
W = np.kron(
    np.kron(np.eye(N_MAX + 1), S1), I2
)  # real swap of sigma within each level, x multiplicity
MM = np.kron(np.eye(2 * (N_MAX + 1)), EPS2)  # J_M = MM . conj  (quaternionic structure)
DIM_M = DM.shape[0]


def conj_ad(m: np.ndarray, x: np.ndarray) -> np.ndarray:
    """J X J^-1 for J(v) = M conj(v)."""
    return m @ x.conj() @ np.linalg.inv(m)


print("=" * 78)
print("KO tuple of the doubled triple -- does the Pin choice change it?")
print("=" * 78)

# --- CTRL: does the machinery recover S^3's own KO-dim 3? --------------------
print("\nCTRL -- recover the S^3 factor's own tuple (declared input: KO-dim 3)")
eps_M = MM @ MM.conj()
e_M = +1 if np.allclose(eps_M, np.eye(DIM_M)) else (-1 if np.allclose(eps_M, -np.eye(DIM_M)) else 0)
dm_conj = conj_ad(MM, DM)
ep_M = +1 if np.allclose(dm_conj, DM) else (-1 if np.allclose(dm_conj, -DM) else 0)
print(f"    J_M^2 = {e_M:+d};  J_M D_M J_M^-1 = {ep_M:+d} * D_M;  no gamma (odd)")
print(
    f"    table lookup for (eps, eps') = ({e_M:+d}, {ep_M:+d}), eps'' = None -> KO {lookup(e_M, ep_M, None)}"
)
ctrl = e_M == -1 and ep_M == +1 and lookup(e_M, ep_M, None) == [3]
print(f"    CTRL PASSES -- machinery reproduces the declared KO-dim 3: {ctrl}")
results["ctrl_s3_ko"] = lookup(e_M, ep_M, None)
results["ctrl_passes"] = bool(ctrl)

# --- K4 first: is gamma actually Pin-dependent? ------------------------------
print("\nK4 -- is gamma Pin-dependent at all?  U_iota = c' * W,  gamma = c * U_iota (x) s1")
print("      C56: gamma^dag=gamma and gamma^2=I need c*c' = +-1, so gamma = +-(W (x) s1).")
k4_rows = {}
for pin, cp in (("Pin+ : U^2 = +1", 1.0 + 0j), ("Pin- : U^2 = -1", 1j)):
    c = 1.0 / cp  # c*c' = 1
    u_iota = cp * W
    gamma = np.kron(S1, c * u_iota)
    eta_op = conj_ad(MM, u_iota)
    eta = complex(np.trace(eta_op @ np.linalg.inv(u_iota)) / DIM_M)
    k4_rows[pin] = {
        "U_iota_sq": "+I" if np.allclose(u_iota @ u_iota, np.eye(DIM_M)) else "-I",
        "c": str(c),
        "eta = J_M U_iota J_M^-1 / U_iota": f"{eta:+.0f}",
        "conj(c)/c": f"{complex(np.conj(c) / c):+.0f}",
        "gamma is real": bool(np.allclose(gamma.imag, 0)),
    }
    print(
        f"    {pin}:  c = {c!s:6s}  U^2 = {k4_rows[pin]['U_iota_sq']}"
        f"   conj(c)/c = {complex(np.conj(c) / c):+.0f}   eta = {eta:+.0f}"
        f"   gamma real: {k4_rows[pin]['gamma is real']}"
    )
g_plus = np.kron(S1, (1.0 / 1.0) * (1.0 * W))
g_minus = np.kron(S1, (1.0 / 1j) * (1j * W))
same_gamma = bool(np.allclose(g_plus, g_minus))
print(f"\n    gamma is the SAME operator for both Pin choices: {same_gamma}")
print("    and it is REAL, so J gamma J^-1 = M gamma M^-1 carries NO phase at all.")
print("    => the conj(c)/c flip C56 noted is exactly compensated by the eta flip.")
print("    K4: THE PIN CHOICE CANCELS. C56's U5 was an incomplete accounting.")
results["k4_rows"] = k4_rows
results["k4_pin_cancels"] = same_gamma

GAMMA = g_plus  # = +-(W (x) s1), Pin-independent

# --- K1 / K2 / K3: which sector matrices k survive each axiom? --------------
print("\nK1/K2/K3 -- which k survive J D = eps' D J, J gamma = eps'' gamma J, J^2 = eps?")
D_BLOCK = np.kron(I2, DM) + 1.5 * np.kron(S3, np.eye(DIM_M))
KS = {
    "I": I2,
    "s3": S3,
    "diag(1,i)": np.diag([1, 1j]).astype(complex),
    "diag(1,-1)": np.diag([1, -1]).astype(complex),
    "s1": S1,
    "s2": S2,
}
rows = {}
for kname, k in KS.items():
    m = np.kron(k, MM)
    d_img = conj_ad(m, D_BLOCK)
    ep = +1 if np.allclose(d_img, D_BLOCK) else (-1 if np.allclose(d_img, -D_BLOCK) else 0)
    g_img = conj_ad(m, GAMMA)
    epp = +1 if np.allclose(g_img, GAMMA) else (-1 if np.allclose(g_img, -GAMMA) else 0)
    sq = m @ m.conj()
    e = (
        +1
        if np.allclose(sq, np.eye(m.shape[0]))
        else (-1 if np.allclose(sq, -np.eye(m.shape[0])) else 0)
    )
    ko = lookup(e, ep, epp) if (ep and epp and e) else []
    rows[kname] = {"eps": e, "eps_prime": ep, "eps_pp": epp, "KO": ko}
    mark = "OK  " if (e and ep and epp) else "--  "
    print(
        f"    {mark}k = {kname:11s} eps = {e:+d}  eps' = {ep:+d}  eps'' = {epp:+d}"
        f"   -> KO {ko if ko else '(no definite sign)'}"
    )
k1 = rows["s1"]["eps_prime"] == 0 and rows["s2"]["eps_prime"] == 0
k2 = rows["diag(1,i)"]["eps_pp"] == 0
# SCOPE FIX, recorded rather than quietly adjusted: claim.md predicted eps = -1 for
# "k unitary DIAGONAL", but the first version of this line tested it over ALL k and
# reported False -- because s2 is IMAGINARY, so s2*conj(s2) = -s2^2 = -I and
# eps = (k k-bar) (x) J_M^2 = (-1)(-1) = +1. The claim was right, the test was wider
# than the claim. s2 is excluded anyway by eps' (K1), so nothing downstream moves.
DIAGONAL_K = ["I", "s3", "diag(1,i)", "diag(1,-1)"]
k3 = all(rows[kn]["eps"] == -1 for kn in DIAGONAL_K)
print(f"\n    K1: non-diagonal k (s1, s2) FAIL J D = eps' D J -- the constraint bites: {k1}")
print(f"    K2: diag(1,i) FAILS J gamma = eps'' gamma J: {k2}")
print(f"    K3: eps = J^2 = -1 for every DIAGONAL k, inherited from J_M^2 = -1: {k3}")
print(f"        (s2 gives eps = {rows['s2']['eps']:+d} because it is IMAGINARY:")
print("         s2 conj(s2) = -I, so the two minus signs cancel. It fails eps' anyway.)")
results["k_rows"] = rows
results["k1_nondiagonal_fails"] = bool(k1)
results["k2_diag1i_fails"] = bool(k2)
results["k3_eps_always_minus"] = bool(k3)

# --- K5: the surviving tuples ------------------------------------------------
print("\nK5 -- the surviving tuples and their KO-dimensions")
surv = {kn: r for kn, r in rows.items() if r["KO"]}
for kn, r in surv.items():
    print(
        f"    k = {kn:11s} (eps, eps', eps'') = ({r['eps']:+d}, {r['eps_prime']:+d},"
        f" {r['eps_pp']:+d})  ->  KO-dim {r['KO'][0]}"
    )
kos = sorted({r["KO"][0] for r in surv.values()})
k5 = kos == [2, 4]
print(f"    achievable KO-dimensions: {kos}")
print(f"    K5: selected by an INTERNAL choice of k in J, not by anything geometric: {k5}")
print("    metric dimension is 3 (Weyl asymptotics of D_block on S^3 (+) S^3), so the")
print(
    f"    KO - metric mismatch is {[(n - 3) % 8 for n in kos]} mod 8 -- reported, not interpreted."
)
results["k5_achievable_ko"] = kos
results["k5_two_choices"] = bool(k5)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = ctrl and same_gamma and k1 and k2 and k3 and k5
verdict = "C57_REFUTED_AS_WORDED__PIN_CHOICE_CANCELS__C56_U5_CORRECTED" if ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C57 is REFUTED AS WORDED, and the correction is to MY OWN C56.")
    print()
    print("  C56's U5 said the eps'' sign flips with the Pin+/Pin- choice. It does not.")
    print("  U5 looked only at J(cX)J^-1 = conj(c) J X J^-1 and never asked what J_M does")
    print("  to U_iota. Writing U_iota = c' W with W the real swap, C56's own condition")
    print("  c*c' = +-1 makes gamma = +-(W (x) s1) -- the SAME REAL operator for both Pin")
    print("  choices. The conj(c)/c flip is exactly compensated by")
    print("  eta = J_M U_iota J_M^-1 / U_iota = conj(c')/c'. Two flips, no net effect.")
    print("  So the Pin choice was a red herring -- the second one this session, after")
    print("  U_iota^2 itself.")
    print()
    print("  WHAT THE TUPLE ACTUALLY IS. eps = J^2 = -1 for every admissible k, inherited")
    print("  from J_M^2 = -1. eps' = +1 is FORCED (the D_M part cannot flip), and it")
    print("  forces k diagonal -- s1 and s2 fail outright. J gamma = eps'' gamma J then")
    print("  narrows k to {I, s3} up to phase; diag(1,i) fails. So:")
    print("      k = I   ->  (-1, +1, +1)  ->  KO-dimension 4")
    print("      k = s3  ->  (-1, +1, -1)  ->  KO-dimension 2")
    print("  and the choice between them is INTERNAL to J, not geometric.")
    print()
    print("  SCOPE, and it matters here more than usual: C49 (PD fails) and C52")
    print("  (orientability fails) already showed this object is NOT a spectral geometry.")
    print("  A KO-dimension does not make it one. The KO table itself is [DOCS], not")
    print("  re-derived -- the same handling preprint.tex gives J_F after C36. The")
    print("  control confirms the machinery recovers S^3's own KO-dim 3 from its declared")
    print("  inputs, which is the least it must do before its other outputs are trusted.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
