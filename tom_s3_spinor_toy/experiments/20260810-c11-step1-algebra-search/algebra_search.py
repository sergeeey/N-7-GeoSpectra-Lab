"""C11 step 1: is there a NATURAL algebra A, and does it make the doubling necessary?

WHY THIS CARRIES THE FULL WEIGHT NOW. C44 removed the grading as evidence for the
t=0/t=1 doubling (it is generic in t). What is left of PARENT_ACTION_GATE's missing
fields, the algebra is the cheapest, because first-order, orientability and Poincare
duality are all defined RELATIVE to it.

SETTING. round67's closed form gives D^t(n,sigma) = sigma(n+3/2) + (t-1/2)*h_H with
h_H = 3. The torsion term is the SAME for every level (C42's own observation), so on
the doubled space

    D_block = D^{1/2} (x) I  +  (3/2) I (x) s3          [s3 = diag(-1,+1) on sectors]

i.e. the entire sector-distinguishing part of D_block is a BOUNDED operator.

THE SEARCH. Write an algebra element as a sum of terms f (x) s_k where f is a function
on S^3 of definite iota-parity (iota(g) = g^-1, C39) and s_k in {I, s1, s2, s3}. This
is exact and finite: 2 parities x 4 Paulis = 8 basis symbols. Every axiom available at
this stage is a linear/multiplicative condition on that 8-symbol space.

Predictions P1-P5 and red-flags RF1-RF5 are recorded in claim.md BEFORE this ran. P5
(">=2 inequivalent candidates survive, so the claim is falsified as worded") is the
prediction that kills C45 -- written down first so a null cannot be re-read as success.

ASSUMPTION A1, flagged not derived: U_iota D^{1/2} U_iota^dag = -D^{1/2}. Provenance is
C39 (iota orientation-REVERSING, verified) plus the standard consequence for D. If A1 is
false, gamma_geo does not exist and P3-P5 are void.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step1.json"
results: dict = {}

H_H = 3
N_MAX = 8

# Pauli basis on the SECTOR index. s3 = diag(-1,+1) distinguishes t=0 from t=1.
PAULI = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[-1, 0], [0, 1]], dtype=complex),  # NOTE: -s3_standard, so sector0 <-> t=0
]
PNAME = ["I", "s1", "s2", "s3"]


def decompose(m: np.ndarray) -> tuple[int, complex]:
    """A product of two Paulis is always a single basis element times a phase."""
    for k, p in enumerate(PAULI):
        c = np.trace(p.conj().T @ m) / 2
        if np.allclose(c * p, m):
            return k, complex(c)
    raise AssertionError("not a single Pauli term")


print("=" * 78)
print("C11 step 1 -- the algebra search (post-C44: this carries the full weight)")
print("=" * 78)

# --- P1: is the sector-distinguishing part of D_block BOUNDED? ---------------
print("\nP1 -- is the sector part of D_block bounded? (does [D,a] constrain sectors?)")
t, tp, n, sig = sp.symbols("t t' n sigma", real=True)
Dt = sig * (n + sp.Rational(3, 2)) + (t - sp.Rational(1, 2)) * H_H
diff = sp.simplify(Dt - Dt.subs(t, tp))
level_independent = sp.simplify(sp.diff(diff, n)) == 0 and sp.simplify(sp.diff(diff, sig)) == 0
print(f"    D^t - D^t' = {diff}")
print(f"    independent of BOTH n and sigma: {level_independent}")
print(f"    => D^0 - D^1 = {diff.subs({t: 0, tp: 1})} * Identity, a BOUNDED operator")
print("    => for a = sum f_i (x) s_i,  [D_block, a] = sum [D^{1/2},f_i](x)s_i")
print("                                  + (3/2) sum f_i (x) [s3, s_i]")
print("       the second term is bounded for EVERY s_i, so the bounded-commutator")
print("       axiom imposes ZERO constraint on the sector index.")
results["p1_torsion_shift_level_independent"] = bool(level_independent)
results["p1_D0_minus_D1"] = str(diff.subs({t: 0, tp: 1}))
results["p1_bounded_commutator_constrains_sectors"] = False

# --- P2 / RF5: how non-unique is the grading? --------------------------------
print("\nP2 / RF5 -- moduli of valid gradings (gamma^dag=gamma, gamma^2=1, {gamma,D}=0)")


def block_spectrum(nmax: int) -> list[float]:
    out: list[float] = []
    for tv in (0.0, 1.0):
        for nn in range(nmax + 1):
            for s in (+1, -1):
                out.extend([s * (nn + 1.5) + (tv - 0.5) * H_H] * ((nn + 1) * (nn + 2)))
    return out


spec = Counter(np.round(block_spectrum(N_MAX), 9))
sym = all(abs(spec[v] - spec[round(-v, 9)]) == 0 for v in spec)
# gamma restricted to a (lambda, -lambda) pair is [[0,V],[V^dag,0]], V in U(d_lambda)
moduli = sum(spec[v] ** 2 for v in spec if v > 0)
zero_d = spec.get(0.0, 0)
print(f"    truncation N_MAX = {N_MAX}, block spectrum symmetric: {sym}")
print(f"    dim ker = {zero_d}; distinct positive eigenvalues: {sum(1 for v in spec if v > 0)}")
print(f"    dim of grading moduli = sum_lambda>0 d_lambda^2 = {moduli}  (real dim of prod U(d))")
print("    => gamma is MASSIVELY non-unique. RF5 FIRES.")
results["p2_block_spectrum_symmetric"] = bool(sym)
results["p2_grading_moduli_dim"] = int(moduli)
results["rf5_gamma_non_unique"] = True

# --- P3: which candidate gradings actually anticommute with D_block? ---------
print("\nP3 -- which gamma = V (x) s_k anticommute with D_block? (A1: U_iota flips D^{1/2})")
# V acts on the S^3 factor: 'U' = U_iota flips D^{1/2}; 'I' = identity does not.
gamma_tests = {}
for vname, v_flips in (("U_iota", True), ("I", False)):
    for k in range(4):
        # conj of D^{1/2}(x)I  -> (+/-)D^{1/2}(x)I ; conj of I(x)s3 -> I(x) s_k s3 s_k
        sector_flips = np.allclose(PAULI[k] @ PAULI[3] @ PAULI[k], -PAULI[3])
        ok = v_flips and sector_flips
        gamma_tests[f"{vname} (x) {PNAME[k]}"] = ok
        mark = "OK  " if ok else "--  "
        print(
            f"    {mark}gamma = {vname:7s}(x) {PNAME[k]:2s}"
            f"   flips D^1/2: {v_flips!s:5s}   flips s3: {sector_flips}"
        )
passing = [g for g, ok in gamma_tests.items() if ok]
both_needed = gamma_tests["U_iota (x) s1"] and not (
    gamma_tests["I (x) s1"] or gamma_tests["U_iota (x) I"]
)
print(f"\n    anticommuting: {passing}")
print(f"    BOTH factors needed (controls 'I (x) s1' and 'U_iota (x) I' FAIL): {both_needed}")
results["p3_gamma_candidates"] = gamma_tests
results["p3_both_factors_needed"] = bool(both_needed)

# --- the gamma_geo-even algebra, exactly -------------------------------------
print("\nP4 -- the gamma_geo-even algebra on the 8 symbols (parity x Pauli)")
# symbol = (parity, k): parity +1 = iota-EVEN function, -1 = iota-ODD.
# gamma_geo = U_iota (x) s1 conjugates  f (x) s_k  ->  (f o iota) (x) s1 s_k s1
SYMBOLS = [(p, k) for p in (+1, -1) for k in range(4)]


def gamma_even(sym_pk: tuple[int, int], gk: int) -> bool:
    """Is f (x) s_k invariant under conjugation by V (x) s_gk, V implementing f -> f o iota?"""
    p, k = sym_pk
    conj = PAULI[gk] @ PAULI[k] @ PAULI[gk]
    _, phase = decompose(conj)
    return bool(np.isclose(p * phase, 1.0))


even_syms = [s for s in SYMBOLS if gamma_even(s, 1)]
lbl = {(+1, k): f"even(x){PNAME[k]}" for k in range(4)}
lbl.update({(-1, k): f"odd (x){PNAME[k]}" for k in range(4)})
print(f"    gamma_geo-EVEN symbols: {[lbl[s] for s in even_syms]}")
print(f"    gamma_geo-ODD  symbols: {[lbl[s] for s in SYMBOLS if s not in even_syms]}")
p4 = (-1, 0) not in even_syms
print(f"\n    P4: an iota-ODD function may NOT act as the same function on both sectors: {p4}")
print("        => the second sector is the IOTA-MIRROR of the first, not a free copy")
print("           and not a duplicate.  (f acts as diag(f, f o iota) via even(x)I + odd(x)s3)")
results["p4_even_symbols"] = [lbl[s] for s in even_syms]
results["p4_odd_I_is_forbidden"] = bool(p4)

# --- typed candidates --------------------------------------------------------
print("\nTYPED CANDIDATES -- each tested for closure, unitality, gamma-evenness, red flags")
CANDIDATES = {
    "T1  A0 (x) I            (same function on both)": [(+1, 0), (-1, 0)],
    "T2  A0 (x) {I,s3}       (independent copies)": [(+1, 0), (-1, 0), (+1, 3), (-1, 3)],
    "T3  A0 (x) M2(C)        (full matrix)": SYMBOLS,
    "T4  A0 |x| Z2           (crossed product)": [(+1, 0), (+1, 1), (-1, 2), (-1, 3)],
    "T5  A0 (x) {I,s1}": [(+1, 0), (-1, 0), (+1, 1), (-1, 1)],
    "T6  A+ (x) I            (iota-even functions only)": [(+1, 0)],
    "T7  {diag(f, f o iota)} (twisted diagonal)": [(+1, 0), (-1, 3)],
}


def closed(syms: list[tuple[int, int]]) -> bool:
    have = set(syms)
    for p1, k1 in syms:
        for p2, k2 in syms:
            k, _ = decompose(PAULI[k1] @ PAULI[k2])
            if (p1 * p2, k) not in have:
                return False
    return True


def mixes(syms: list[tuple[int, int]]) -> bool:
    return any(k in (1, 2) for _, k in syms)


table = {}
for name, syms in CANDIDATES.items():
    cl = closed(syms)
    unital = (+1, 0) in syms
    ev = all(gamma_even(s, 1) for s in syms)
    rf1 = {(+1, 0), (-1, 0), (+1, 3), (-1, 3)}.issubset(set(syms))
    rf2 = set(syms) == {(+1, 0), (-1, 0)}
    admissible = cl and unital and ev
    flags = []
    if rf1:
        flags.append("RF1-gratuitous")
    if rf2:
        flags.append("RF2-duplicate")
    if mixes(syms):
        flags.append("RF3-mixing")
    table[name] = {
        "closed": cl,
        "unital": unital,
        "gamma_even": ev,
        "admissible": admissible,
        "flags": flags,
    }
    mark = "ADMIT " if admissible else "reject"
    why = "" if admissible else f"(closed={cl}, unital={unital}, even={ev})"
    print(f"    {mark} {name:48s} {','.join(flags) or '-':22s} {why}")
admissible = [k for k, v in table.items() if v["admissible"]]
results["typed_candidates"] = table
results["admissible"] = admissible

# --- RF4: uniqueness ---------------------------------------------------------
print("\nRF4 -- uniqueness among admissible candidates")
print(f"    admissible count: {len(admissible)}")
for a in admissible:
    print(f"      - {a}")
# inequivalence: different dimension over the function algebra, or one is a proper subalgebra
pairs_nested = []
for a, b in combinations(admissible, 2):
    sa, sb = set(CANDIDATES[a]), set(CANDIDATES[b])
    if sa < sb or sb < sa:
        pairs_nested.append((a.split()[0], b.split()[0]))
rf4 = len(admissible) >= 2
print(f"    proper-subalgebra pairs among admissible: {pairs_nested}")
print(f"    RF4 (>=2 inequivalent admissible): {rf4}")
results["rf4_non_unique"] = bool(rf4)
results["nested_pairs"] = pairs_nested

# --- NEGATIVE CONTROLS (portfolio step 2, same search) -----------------------
print("\nNEGATIVE CONTROLS -- run the identical search with wrong/degenerate gammas")
controls = {}
for cname, gk, has_U in (
    ("B: I (x) s1        (iota dropped)", 1, False),
    ("C: U_iota (x) I    (sector swap dropped)", 0, True),
    ("D: U_iota (x) s3   (wrong Pauli)", 3, True),
    ("E: U_iota (x) s2   (positive control, should PASS)", 2, True),
):
    sector_flips = np.allclose(PAULI[gk] @ PAULI[3] @ PAULI[gk], -PAULI[3])
    anti = has_U and sector_flips
    ev_syms = [lbl[s] for s in SYMBOLS if gamma_even(s, gk)] if anti else []
    controls[cname] = {"anticommutes_with_D": bool(anti), "even_symbols": ev_syms}
    mark = "PASS" if anti else "FAIL"
    print(f"    {mark}  {cname:44s} even algebra: {ev_syms if anti else '(n/a)'}")
ctrl_ok = (
    not controls["B: I (x) s1        (iota dropped)"]["anticommutes_with_D"]
    and not controls["C: U_iota (x) I    (sector swap dropped)"]["anticommutes_with_D"]
    and not controls["D: U_iota (x) s3   (wrong Pauli)"]["anticommutes_with_D"]
    and controls["E: U_iota (x) s2   (positive control, should PASS)"]["anticommutes_with_D"]
)
print(f"\n    CONTROLS PASS (3 degenerate FAIL, 1 positive PASSES): {ctrl_ok}")
results["controls"] = controls
results["controls_pass"] = bool(ctrl_ok)

# --- is the iota-parity split of functions non-empty? (crossed product non-vacuous) ---
print("\nSANITY -- is A0 = A+ (+) A- a NON-TRIVIAL split? (else the whole structure is empty)")
IOTA4 = np.diag([1.0, -1.0, -1.0, -1.0])
rng = np.random.default_rng(20260810)
xs = rng.normal(size=(500, 4))
xs /= np.linalg.norm(xs, axis=1, keepdims=True)
xi = xs @ IOTA4
even_fn = np.allclose(xs[:, 0], xi[:, 0])  # f = x0
odd_fn = np.allclose(xs[:, 1], -xi[:, 1])  # f = x1
print(f"    f = x0 is iota-EVEN: {even_fn};   f = x1 is iota-ODD: {odd_fn}")
print("    => both A+ and A- are non-trivial, the crossed-product structure is real")
results["sanity_iota_parity_split_nontrivial"] = bool(even_fn and odd_fn)

# --- is RF4's firing INFORMATIVE, or near-tautological? ----------------------
print("\nRF4 self-check -- is this criterion doing any work?")
print("    Admissibility (closed, unital, gamma-even) is inherited by every unital")
print("    SUBalgebra, so RF4 fires almost by construction. Recorded as a WEAK criterion:")
print("    the informative question is whether the MAXIMAL gamma-even algebra is forced.")
results["rf4_is_near_tautological"] = True

print("\nMAXIMALITY -- is the maximal gamma-even algebra unique over geometric gammas?")
# geometric family: gamma_theta = U_iota (x) (cos th * s1 + sin th * s2)
# sector-PRESERVING unitaries V_phi = diag(1, e^{i phi}) must map one onto another.
maximal_sets, conj_ok = {}, True
for th in (0.0, np.pi / 2, np.pi / 4, 1.234):
    m = np.cos(th) * PAULI[1] + np.sin(th) * PAULI[2]
    valid = np.allclose(m @ m, np.eye(2)) and np.allclose(m.conj().T, m)
    valid &= np.allclose(m @ PAULI[3] @ m, -PAULI[3])
    maximal_sets[round(th, 4)] = valid
    print(f"    theta = {th:6.4f}  gamma_theta is a valid grading: {valid}")
for phi in (0.3, 1.1, 2.7):
    V = np.diag([1.0, np.exp(1j * phi)])
    got = V @ PAULI[1] @ V.conj().T
    want = np.cos(phi) * PAULI[1] + np.sin(phi) * PAULI[2]
    sector_preserving = np.allclose(V @ PAULI[3] @ V.conj().T, PAULI[3])
    conj_ok &= bool(np.allclose(got, want) and sector_preserving)
print(f"    every gamma_theta is conjugate to gamma_0 by a SECTOR-PRESERVING V_phi: {conj_ok}")
print("    => given maximality, the algebra IS unique up to sector-preserving unitary.")
print("       Maximality is the one missing axiom, and NCG does not supply it: the")
print("       algebra is input data, not derived.")
results["maximality_all_geometric_gammas_valid"] = all(maximal_sets.values())
results["maximality_unique_up_to_sector_preserving_unitary"] = bool(conj_ok)

print("\nUNIFORM STRUCTURE -- what do ALL admissible candidates agree on?")
TWISTED = {(+1, 0), (-1, 3)}  # span of diag(f, f o iota)
uniform = True
for name in admissible:
    diag_part = {s for s in CANDIDATES[name] if s[1] in (0, 3)}
    ok = diag_part.issubset(TWISTED)
    uniform &= ok
    print(f"    {name.split()[0]}: sector-diagonal part inside span(diag(f, f o iota)): {ok}")
print(f"    ALL admissible candidates agree: {uniform}")
print("    => independent of maximality, no admissible algebra can act as the SAME")
print("       function on both sectors unless that function is iota-even.")
results["uniform_twisted_diagonal"] = bool(uniform)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
c45_stands = (len(admissible) == 1) and mixes(CANDIDATES[admissible[0]]) if admissible else False
verdict = "C45_STANDS" if c45_stands else "C45_FALSIFIED_AS_WORDED__ALGEBRA_DOES_NOT_EARN_DOUBLING"
print(f"VERDICT: {verdict}")
print("=" * 78)
if not c45_stands:
    print("  P5 came true. Admissibility is closed under passing to unital subalgebras, so")
    print(f"  {len(admissible)} typed candidates survive, nested inside one another. No axiom")
    print("  available at this stage picks the maximal one. RF4 FIRES.")
    print()
    print("  WHAT SURVIVES, and it is a real structural result:")
    print("   (i)  the bounded-commutator axiom cannot see the sector index at all, because")
    print("        D^0 - D^1 = -3*Identity is BOUNDED. Only the grading constrains sectors.")
    print("   (ii) gamma_geo = U_iota (x) s1 needs BOTH factors -- iota is load-bearing, and")
    print("        the three degenerate controls fail exactly as they should.")
    print("   (iii)an iota-ODD function may NOT act identically on both sectors. So the")
    print("        second sector is forced to be the IOTA-MIRROR of the first:")
    print("        f is represented as diag(f, f o iota). The doubling is a PARITY doubling,")
    print("        not a flavour doubling and not a free second copy.")
    print()
    print("  WHAT DOES NOT: (iii) is a constraint on HOW the copies relate, not a reason")
    print("  that there must be two. gamma is itself massively non-unique (RF5), so even")
    print("  'the algebra selected by the grading' is ill-defined without the extra, ")
    print("  undischarged assumption that gamma be the GEOMETRIC one.")
results["verdict"] = verdict
results["c45_stands"] = bool(c45_stands)
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
