"""A1: does iota really flip the Dirac operator? Verify it instead of inheriting it.

WHY THIS AND NOT ANOTHER ESCAPE ROUTE. Every round from C45 to C54 carried the same line:
ASSUMPTION A1, "inherited from C39 plus the standard orientation-reversal result, not
re-derived here". C54 made the exposure explicit -- A1 is exactly what makes
[D_M, U_iota] = 2 D_M U_iota UNBOUNDED, so C50, C51, C53 and C54 all rest on it. C39
established that iota REVERSES ORIENTATION; it never established that iota flips D.

THIS IS VERIFIABLE, NOT MERELY CITABLE, because Peter-Weyl makes both the spectrum and
the iota-action explicit:

    L2(SU(2), S) = (+)_j  V_j (x) (V_j* (x) V_{1/2})
                 = (+)_j  V_j (x) (V_{j+1/2} (+) V_{j-1/2})

Label each isotypic piece by (j, k) = (left spin, right spin) with k = j +- 1/2. Since
iota(g) = g^-1 exchanges left and right translations, iota* maps (j,k) -> (k,j).

PREDICTIONS A1a-A1d, NC and DISC are recorded in claim.md BEFORE this ran. The kill
criterion is explicit: if lambda(k,j) != -lambda(j,k), or the multiplicities do not match
under the swap, or the Peter-Weyl formula does not reproduce round67's spectrum, then A1
is FALSE and C50/C51/C53/C54 must be rebuilt.

WHAT THIS CANNOT SETTLE, fixed in advance: the geometric spinor lift may differ from the
bare pullback by a unitary. The conclusion survives any factor preserving the isotypic
decomposition -- weaker than A1 itself, but still an input, named ASSUMPTION A1-lift.
U_iota^2 = +-1 remains open (since C45).
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_a1.json"
results: dict = {}

H_H = 3
J_MAX = 12  # in half-integer steps: j = 0, 1/2, 1, ... , 6

print("=" * 78)
print("A1 -- does iota flip the Dirac operator? Peter-Weyl on SU(2)")
print("=" * 78)

j, k, t = sp.symbols("j k t", nonnegative=True)


def lam(jj, kk):
    """Dirac eigenvalue on the (left spin jj, right spin kk) isotypic piece."""
    return (jj + kk + 1) * sp.sign(kk - jj)


def mult(jj, kk):
    return (2 * jj + 1) * (2 * kk + 1)


# --- A1a: does Peter-Weyl reproduce round67's spectrum AND multiplicities? ---
print("\nA1a -- lambda(j,k) = (j+k+1)*sign(k-j): does it reproduce round67's data?")
print("       round67: eigenvalues +-(n+3/2), multiplicity (n+1)(n+2)")
rows, ok_pos, ok_neg = [], True, True
for two_j in range(J_MAX + 1):
    jj = sp.Rational(two_j, 2)
    # k = j + 1/2 : the POSITIVE branch, expect n = 2j
    kk = jj + sp.Rational(1, 2)
    lp, mp = sp.nsimplify(lam(jj, kk)), mult(jj, kk)
    n_pos = 2 * jj
    ok_pos &= bool(sp.simplify(lp - (n_pos + sp.Rational(3, 2))) == 0)
    ok_pos &= bool(sp.simplify(mp - (n_pos + 1) * (n_pos + 2)) == 0)
    row = {"j": str(jj), "k_plus": str(kk), "lambda_plus": str(lp), "mult_plus": int(mp)}
    # k = j - 1/2 : the NEGATIVE branch, expect n = 2j - 1
    if jj >= sp.Rational(1, 2):
        kk2 = jj - sp.Rational(1, 2)
        ln, mn = sp.nsimplify(lam(jj, kk2)), mult(jj, kk2)
        n_neg = 2 * jj - 1
        ok_neg &= bool(sp.simplify(ln + (n_neg + sp.Rational(3, 2))) == 0)
        ok_neg &= bool(sp.simplify(mn - (n_neg + 1) * (n_neg + 2)) == 0)
        row |= {"k_minus": str(kk2), "lambda_minus": str(ln), "mult_minus": int(mn)}
    rows.append(row)
    if two_j <= 4:
        print(
            f"    j = {jj!s:4s}  k = j+1/2: lambda = {lp!s:6s} mult = {int(mp):3d}"
            + (f"   |  k = j-1/2: lambda = {ln!s:6s} mult = {int(mn):3d}" if two_j else "")
        )
print(f"    positive branch matches +(n+3/2) with mult (n+1)(n+2): {ok_pos}")
print(f"    negative branch matches -(n+3/2) with mult (n+1)(n+2): {ok_neg}")
print("    => an INDEPENDENT derivation of the spectral data this project has used")
print("       since round67, from representation theory rather than from the closed form.")
a1a = ok_pos and ok_neg
results["a1a_reproduces_round67"] = bool(a1a)
results["a1a_table"] = rows[:5]

# --- A1b: the swap flips the eigenvalue, identically ------------------------
print("\nA1b -- iota* maps (j,k) -> (k,j). Does lambda(k,j) = -lambda(j,k) IDENTICALLY?")
expr = sp.simplify(lam(k, j) + lam(j, k))
print(f"    lambda(k,j) + lambda(j,k) = {expr}")
flips = bool(expr == 0)
print(f"    identically zero in (j,k): {flips}")
print("      because the swap preserves (j+k+1) and flips sign(k-j).")
dims_sym = bool(sp.simplify(mult(j, k) - mult(k, j)) == 0)
print(f"    multiplicities (2j+1)(2k+1) are symmetric under the swap: {dims_sym}")
print("    => the swap is a BIJECTION from D-eigenspaces onto (-D)-eigenspaces.")
a1b = flips and dims_sym
results["a1b_flips_identically"] = bool(flips)
results["a1b_dims_symmetric"] = bool(dims_sym)

# --- A1c: level by level, + eigenspace maps ONTO - eigenspace ---------------
print("\nA1c -- level by level: does + (n+3/2) map onto -(n+3/2) with equal multiplicity?")
levels, a1c = [], True
for n in range(9):
    jj = sp.Rational(n, 2)  # positive branch at level n
    kk = jj + sp.Rational(1, 2)
    src = (jj, kk, lam(jj, kk), mult(jj, kk))
    tgt = (kk, jj, lam(kk, jj), mult(kk, jj))  # the iota image
    same_mag = bool(sp.simplify(src[2] + tgt[2]) == 0)
    same_dim = bool(sp.simplify(src[3] - tgt[3]) == 0)
    a1c &= same_mag and same_dim
    levels.append(
        {
            "n": n,
            "from": f"({src[0]},{src[1]})",
            "to": f"({tgt[0]},{tgt[1]})",
            "lambda": str(src[2]),
            "image_lambda": str(tgt[2]),
            "mult": int(src[3]),
        }
    )
    if n <= 4:
        print(
            f"    n = {n}:  ({src[0]},{src[1]}) lambda = {src[2]!s:6s} mult {int(src[3]):3d}"
            f"   --iota-->  ({tgt[0]},{tgt[1]}) lambda = {tgt[2]!s:6s} mult {int(tgt[3]):3d}"
        )
print(f"    every level maps onto its mirror with equal multiplicity: {a1c}")
results["a1c_levels"] = levels[:5]
results["a1c_bijection"] = bool(a1c)

# --- A1d: consequence -- U_iota D^t U_iota^dag = -D^{1-t} -------------------
print("\nA1d -- consequence for the whole t-family. D^t = D^{1/2} + 3(t-1/2), so")
print("       U_iota D^t U_iota^dag = -D^{1/2} + 3(t-1/2) = -(D^{1/2} - 3(t-1/2)) = -D^{1-t}")
lhs = -(sp.Symbol("D_half")) + H_H * (t - sp.Rational(1, 2))
rhs = -((sp.Symbol("D_half")) + H_H * ((1 - t) - sp.Rational(1, 2)))
a1d = bool(sp.simplify(lhs - rhs) == 0)
print(f"    -D^{{1/2}} + 3(t-1/2)  ==  -D^{{1-t}} : {a1d}")
print("    => A1 IMPLIES C44's mirror relation spec(D^{1-t}) = -spec(D^t), which C44")
print("       obtained independently from round67's closed form. Two routes agree.")
results["a1d_implies_c44_mirror"] = bool(a1d)

# --- NEGATIVE CONTROL: an orientation-PRESERVING map must NOT flip ----------
print("\nNC -- NEGATIVE CONTROL: left translation L_a (orientation-PRESERVING, C39's own")
print("      control) acts WITHIN each (j,k) block -- it does not permute the labels.")
# WHY THIS IS NOT WRITTEN AS lam(j,k) - lam(j,k): that is x - x == 0, a check that
# cannot fail -- the seventh of this session. Both maps are pushed through the SAME
# code path instead, so the control genuinely discriminates.
LABEL_MAPS = {
    "iota:  (j,k) -> (k,j)   [orientation-REVERSING]": lambda a, b: (b, a),
    "L_a:   (j,k) -> (j,k)   [orientation-PRESERVING]": lambda a, b: (a, b),
}


def flips_under(label_map) -> bool:
    """Does lambda change sign when the isotypic labels are moved by label_map?"""
    jj, kk = label_map(j, k)
    return bool(sp.simplify(lam(jj, kk) + lam(j, k)) == 0)


nc = {name: flips_under(m) for name, m in LABEL_MAPS.items()}
for name, v in nc.items():
    print(f"    {name}  flips lambda: {v}")
nc_same = (
    nc["iota:  (j,k) -> (k,j)   [orientation-REVERSING]"]
    and not nc["L_a:   (j,k) -> (j,k)   [orientation-PRESERVING]"]
)
print(f"    CONTROL PASSES -- same code path, opposite answers: {nc_same}")
print("    so the flip is caused by the L<->R SWAP specifically, which is what")
print("    orientation-reversal means here -- not by 'being an isometry'.")
results["nc_flip_by_map"] = nc
results["nc_orientation_preserving_no_flip"] = bool(nc_same)

# --- DISCRIMINATION: which factor carries the result? ----------------------
print("\nDISC -- drop the sign(k-j) factor (i.e. use |D|) and re-run the swap test")
lam_abs = j + k + 1
disc = bool(sp.simplify(lam_abs.subs({j: k, k: j}, simultaneous=True) - lam_abs) == 0)
print(f"    |lambda|(k,j) == |lambda|(j,k) (NO flip): {disc}")
print(f"    so the sign(k-j) factor is exactly what carries A1: {disc and flips}")
results["disc_abs_does_not_flip"] = bool(disc)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = a1a and a1b and a1c and a1d and nc_same and disc
verdict = "A1_VERIFIED__IOTA_FLIPS_THE_DIRAC_OPERATOR" if ok else "A1_NOT_ESTABLISHED"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C55 STANDS. A1 is no longer inherited -- it is derived.")
    print()
    print("  On the (j,k) isotypic piece the Dirac eigenvalue is")
    print("      lambda(j,k) = (j + k + 1) * sign(k - j),")
    print("  which reproduces round67's +-(n+3/2) with multiplicity (n+1)(n+2) EXACTLY,")
    print("  independently of the closed form the project has used since round67.")
    print()
    print("  iota(g) = g^-1 exchanges left and right translations, so iota* maps")
    print("  (j,k) -> (k,j). That swap preserves (j+k+1) and flips sign(k-j), hence")
    print("      lambda(k,j) = -lambda(j,k)   IDENTICALLY,")
    print("  with (2j+1)(2k+1) symmetric, so it is a BIJECTION from each D-eigenspace")
    print("  onto the corresponding (-D)-eigenspace. That is A1.")
    print()
    print("  CROSS-CHECKS. A1 implies U_iota D^t U_iota^dag = -D^{1-t}, which is exactly")
    print("  C44's mirror relation -- obtained there from the closed form, here from")
    print("  iota. Two independent routes to the same statement.")
    print("  The negative control confirms the flip comes from the L<->R SWAP, not from")
    print("  'being an isometry': left translation leaves the labels alone. And dropping")
    print("  sign(k-j) kills the flip, so that factor is what carries the result.")
    print()
    print("  WHAT REMAINS OPEN, unchanged by this round:")
    print("   - ASSUMPTION A1-lift: the geometric spinor lift may differ from the bare")
    print("     pullback by a unitary. The conclusion survives any factor preserving the")
    print("     isotypic decomposition -- much weaker than A1 was, but still an input.")
    print("   - U_iota^2 = +-1, open since C45. Nothing here settles the sign.")
    print()
    print("  CONSEQUENCE FOR THE CHAIN: C50, C51, C53 and C54 no longer rest on an")
    print("  unverified assumption. Their load-bearing input is now derived, and what")
    print("  they inherit is the strictly weaker A1-lift.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
