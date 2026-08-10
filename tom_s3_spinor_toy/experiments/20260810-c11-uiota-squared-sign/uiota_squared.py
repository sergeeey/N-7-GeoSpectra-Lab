"""U_iota^2 = +-1: the last named unknown in the C11 line.

WHAT WAS FLAGGED. C45 recorded: "OPEN, flagged not assumed: whether the Pin-lift satisfies
U_iota^2 = +1, needed for gamma^dag = gamma." It has been carried for ten rounds, and
after C55 discharged A1 it is the ONLY named unknown left. The worry has a real basis:
gamma = U_iota (x) s1 gives gamma^2 = U_iota^2 (x) I, so U_iota^2 = -1 would make
gamma^2 = -1 and C43's whole construction would collapse.

WHAT I EXPECT, stated in claim.md before running: that the question is MIS-SCOPED. gamma
is only ever used up to a phase, and a phase absorbs the sign --
    U_iota^2 = +1  =>  U_iota self-adjoint       =>  gamma = +- U_iota (x) s1
    U_iota^2 = -1  =>  U_iota anti-self-adjoint  =>  gamma = +- i U_iota (x) s1,
                                                     and then gamma^2 = (i^2)(-1) = +1
                                                     and gamma^dag = gamma BOTH hold.
If so, the flag has been a false alarm for ten rounds, and this file should say that
plainly rather than dress a null as a discovery.

WHY THE PHASE FREEDOM EXISTS. By C55, U_iota maps the isotypic piece (j, j+-1/2) onto
(j+-1/2, j). Since j != j+-1/2 always, U_iota is PURELY OFF-DIAGONAL on the mirror pairs
-- no fixed blocks -- so U_iota^2 = +1 iff U_iota is self-adjoint, U_iota^2 = -1 iff
anti-self-adjoint, and multiplying by i moves between them.

Predictions U1, U2, U3, U3-DISC, U4, U5 are recorded in claim.md BEFORE this ran.
"""

from __future__ import annotations

import json
from itertools import pairwise
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_uiota.json"
results: dict = {}

I2 = np.eye(2, dtype=complex)
SIG = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
S1_SEC = SIG[0]

print("=" * 78)
print("U_iota^2 = +-1 -- the last named unknown in the C11 line")
print("=" * 78)

# --- U1/U2: the volume element, in BOTH conventions -------------------------
print("\nU1/U2 -- the volume element omega = e1 e2 e3, in both Clifford conventions")
print("        canonical for S^3 per docs/clifford_convention_registry.md:")
print("        Z_i = i*sigma_i, e^2 = -1, labelled Cl(0,3) -- registry marks this CORRECT")
conv = {}
for name, gens in (
    ("Cl(0,3): Z_i = i*sigma_i  [CANONICAL for S^3]", [1j * s for s in SIG]),
    ("Cl(3,0): Gamma_i = sigma_i", list(SIG)),
):
    e_sq = [np.trace(g @ g) / 2 for g in gens]
    omega = gens[0] @ gens[1] @ gens[2]
    conv[name] = {
        "e_squared": complex(e_sq[0]).real,
        "omega": np.array2string(omega, precision=1),
        "omega_sq_is_plus_I": bool(np.allclose(omega @ omega, I2)),
    }
    print(f"    {name}")
    print(
        f"      e_i^2 = {complex(e_sq[0]).real:+.0f}   omega = {np.array2string(omega, precision=1)}"
        f"   omega^2 = +I: {conv[name]['omega_sq_is_plus_I']}"
    )
u1 = conv["Cl(0,3): Z_i = i*sigma_i  [CANONICAL for S^3]"]["omega_sq_is_plus_I"]
u2 = not conv["Cl(3,0): Gamma_i = sigma_i"]["omega_sq_is_plus_I"]
print("\n    U1: in the CANONICAL S^3 convention omega = +I, so the FIBRE part of the")
print(f"        lift of d(iota)|_p = -Id at a fixed point squares to +1: {u1}")
print("    U2: the opposite convention gives omega^2 = -I -- so the sign of omega^2 IS")
print(f"        the convention, exactly as C34's registry says, not a geometric fact: {u2}")
results["u1_canonical_omega_sq_plus"] = bool(u1)
results["u2_other_convention_flips"] = bool(u2)
results["conventions"] = conv

# --- the block model: D and the two candidate lifts --------------------------
print("\nBLOCK MODEL -- mirror pairs (n,+) <-> (n,-) with lambda = +-(n+3/2)  [C55]")
N_MAX = 6
lv = [s * (n + 1.5) for n in range(N_MAX + 1) for s in (+1, -1)]
D_M = np.diag(lv).astype(complex)
swap = np.zeros_like(D_M)
for n in range(N_MAX + 1):
    swap[2 * n, 2 * n + 1] = swap[2 * n + 1, 2 * n] = 1.0
LIFTS = {"U^2 = +1 (self-adjoint)": swap, "U^2 = -1 (anti-self-adjoint)": 1j * swap}
for name, v in LIFTS.items():
    sq = "+I" if np.allclose(v @ v, np.eye(len(lv))) else "-I"
    flips = np.allclose(v @ D_M @ v.conj().T, -D_M)
    print(f"    {name:32s} V^2 = {sq}   V D V^dag = -D: {flips}   (C55's A1, either way)")
    assert flips, "both lifts must implement iota"

# --- U3 + U3-DISC: does a phase rescue gamma in BOTH cases? -----------------
print("\nU3 -- gamma = c * V (x) s1 : which (V, c) pairs give gamma^dag = gamma AND gamma^2 = +1?")
dim = len(lv)
D_block = (
    np.kron(np.diag([-1.0, 1.0]), D_M) * 0
    + np.kron(np.eye(2), D_M)
    + 1.5 * np.kron(np.array([[-1, 0], [0, 1]], dtype=complex), np.eye(dim))
)
table = {}
for vname, v in LIFTS.items():
    for cname, c in (("c = 1", 1.0 + 0j), ("c = -1", -1.0 + 0j), ("c = i", 1j), ("c = -i", -1j)):
        g = c * np.kron(S1_SEC, v)
        herm = bool(np.allclose(g, g.conj().T))
        sq = bool(np.allclose(g @ g, np.eye(2 * dim)))
        anti = bool(np.allclose(g @ D_block + D_block @ g, 0))
        table[f"{vname} | {cname}"] = {"hermitian": herm, "square_is_I": sq, "anticommutes": anti}
        mark = "OK  " if (herm and sq and anti) else "--  "
        print(
            f"    {mark}{vname:32s} {cname:7s} gamma^dag=gamma: {herm!s:5s}"
            f"  gamma^2=I: {sq!s:5s}  {{gamma,D}}=0: {anti}"
        )
ok_plus = table["U^2 = +1 (self-adjoint) | c = 1"]
ok_minus = table["U^2 = -1 (anti-self-adjoint) | c = i"]
u3 = all(ok_plus.values()) and all(ok_minus.values())
bad1 = table["U^2 = +1 (self-adjoint) | c = i"]
bad2 = table["U^2 = -1 (anti-self-adjoint) | c = 1"]
u3_disc = (not all(bad1.values())) and (not all(bad2.values()))
print(f"\n    U3: a valid gamma exists for BOTH signs (c = +-1 resp. c = +-i): {u3}")
print(f"    U3-DISC: the MISMATCHED pairings FAIL, so the test is not vacuous: {u3_disc}")
results["u3_table"] = table
results["u3_gamma_exists_either_sign"] = bool(u3)
results["u3_disc_mismatch_fails"] = bool(u3_disc)

# --- U4: is the C50-C55 chain phase-independent? ----------------------------
print("\nU4 -- is the C50-C55 chain phase-independent? ([D_M, cV] = c [D_M, V])")
norms = {}
for vname, v in LIFTS.items():
    per_cut = {}
    for nmax in (4, 8, 16, 32):
        lvv = [s * (n + 1.5) for n in range(nmax + 1) for s in (+1, -1)]
        d = np.diag(lvv).astype(complex)
        sw = np.zeros_like(d)
        for n in range(nmax + 1):
            sw[2 * n, 2 * n + 1] = sw[2 * n + 1, 2 * n] = 1.0
        vv = sw if "+1" in vname else 1j * sw
        per_cut[nmax] = float(np.linalg.norm(d @ vv - vv @ d, 2))
    norms[vname] = per_cut
    grows = all(per_cut[b] > per_cut[a] for a, b in pairwise([4, 8, 16, 32]))
    print(
        f"    {vname:32s} ||[D_M,V]|| = "
        f"{[round(per_cut[k], 1) for k in (4, 8, 16, 32)]}   grows: {grows}"
    )
u4 = all(
    abs(norms["U^2 = +1 (self-adjoint)"][k] - norms["U^2 = -1 (anti-self-adjoint)"][k]) < 1e-9
    for k in (4, 8, 16, 32)
)
print(f"    U4: IDENTICAL for both signs -- C50/C51/C53/C54's 'V not in B' is untouched: {u4}")
results["u4_norms"] = norms
results["u4_phase_independent"] = bool(u4)

# --- U5: where the sign DOES matter -- J is ANTILINEAR ----------------------
print("\nU5 -- where the sign DOES matter: J is ANTILINEAR, so J(cX)J^-1 = conj(c) J X J^-1")
u5 = {}
for cname, c in (("c = 1 (real)", 1.0 + 0j), ("c = i (imaginary)", 1j)):
    ratio = complex(np.conj(c) / c)
    u5[cname] = {"conj(c)/c": str(ratio)}
    print(f"    {cname:20s} conj(c)/c = {ratio:+.0f}   -> eps'' picks up this factor")
u5_ok = bool(
    np.isclose(complex(np.conj(1.0) / 1.0), 1) and np.isclose(complex(np.conj(1j) / 1j), -1)
)
print(f"    U5: the eps'' sign of the KO tuple FLIPS with the choice: {u5_ok}")
print("        That is EXACTLY the combination C48 declined to make -- and now the reason")
print("        is visible: it depends on a choice nothing in the chain fixes.")
results["u5"] = u5
results["u5_epsilon_flips"] = bool(u5_ok)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = u1 and u2 and u3 and u3_disc and u4 and u5_ok
verdict = "QUESTION_MIS_SCOPED__SIGN_IS_A_CHOICE_AND_NOT_LOAD_BEARING" if ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  The C45 flag was a FALSE ALARM, carried for ten rounds. Saying so plainly:")
    print("  nothing was discovered here except that the worry did not apply.")
    print()
    print("  gamma = c * U_iota (x) s1 is a valid grading for EITHER sign of U_iota^2 --")
    print("  c = +-1 when U_iota^2 = +1, c = +-i when U_iota^2 = -1. In the second case")
    print("  gamma^2 = (i^2)(-1) = +1 and gamma^dag = gamma both hold, because a unitary")
    print("  with U^2 = -1 is ANTI-self-adjoint and the imaginary phase compensates.")
    print("  The mismatched pairings genuinely fail, so this is not a vacuous rescue.")
    print()
    print("  THE PHASE FREEDOM IS AVAILABLE because U_iota is purely OFF-DIAGONAL on the")
    print("  mirror pairs (C55: (j,j+-1/2) -> (j+-1/2,j), and j != j+-1/2 always). An")
    print("  operator with no fixed blocks has U^2 = +1 iff self-adjoint, and i moves")
    print("  between the two cases.")
    print()
    print("  WHAT THE SIGN DOES NOT AFFECT: C50, C51, C53, C54, C55. ||[D_M, cV]|| is")
    print("  identical for both lifts, so 'V is not in B' is untouched; {gamma,D} = 0 is")
    print("  phase-blind; C55's L<->R swap argument never sees the phase.")
    print()
    print("  WHAT IT DOES AFFECT: the KO-dimension sign tuple. J is ANTILINEAR, so")
    print("  J(cX)J^-1 = conj(c) J X J^-1, and conj(c)/c is +1 for real c and -1 for")
    print("  imaginary c -- the eps'' sign flips with the choice. That is precisely the")
    print("  combination C48 declined to make, and the reason is now visible: it depends")
    print("  on a choice nothing in the construction fixes.")
    print()
    print("  GEOMETRICALLY: in the project's CANONICAL S^3 convention (Z_i = i sigma_i,")
    print("  e^2 = -1, Cl(0,3), per docs/clifford_convention_registry.md) omega = +I, so")
    print("  the fibre part of the lift squares to +1. The OPPOSITE convention gives")
    print("  omega^2 = -I. So the sign of omega^2 IS the convention -- C34's point again.")
    print("  Pinning U_iota^2 globally is a Pin+ / Pin- CHOICE; S^3 admits both, and")
    print("  nothing in this chain requires one. Recorded as a choice, not a fact.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
