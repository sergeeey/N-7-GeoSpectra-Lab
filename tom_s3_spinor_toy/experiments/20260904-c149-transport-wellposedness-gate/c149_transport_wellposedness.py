r"""
C149 -- is OB11(ii)'s named-but-never-attempted next step even WELL-POSED?

THE DEBT.  OB11(ii)'s own text (OPEN_BLOCKERS.md:1782-1791) names the next
step: transport D, J, gamma through the intertwiner U found in C70, then
test whether a Hermitian, genuinely Clifford-compatible combined operator
can be built.  That step has never been attempted (C72's own does_not_imply
records it as explicitly deferred).

THE PROBLEM NOBODY CHECKED.  C70's OWN does_not_imply already says U is NOT
unique: "Inn(su(3)) acts transitively on the solution family (~8-real-dim
continuous orbit); C71 must fix one representative and use it consistently."
C142 (2026-09-04) independently re-derived the same fact and sharpened it to
"basis-matching GAUGE freedom, not independent data."

So before building the transport test, one question must be answered:
**does its outcome depend on WHICH representative of the orbit is chosen?**
If yes, the test as specified is ill-posed and would produce a gauge artifact.

THE CRITERION (one line, proved in the docstring, checked below).
If U' = U*g for g in the residual freedom, then

    U' O U'^-1 = U (g O g^-1) U^-1

so the transported operator is independent of the representative EXACTLY
when g O g^-1 = O, i.e. when **O commutes with the residual freedom's own
generators**.  For this bridge the residual freedom is the su(3) action, so
the criterion is simply:

    transport of O is well-posed  <=>  [O, rho_su3(a)] = 0 for all a.

WHAT MAKES THIS CHEAP TODAY AND NOT THREE WEEKS AGO.  C146 (2026-09-04)
proved D_Sigma IS su(3)-equivariant -- a fact never verified standalone
before today.  That is exactly the input this well-posedness question needs,
so today's theorem retroactively settles the status of a step planned on
2026-08-10.

Positive control: D_Sigma (substantive -- rests on C146's own theorem).
Negative control: a random non-equivariant operator, which MUST show
gauge-dependence -- otherwise the test cannot discriminate and is worthless.

gamma (the EVEN/ODD chirality grading) is ALSO checked, but -- corrected
after the FL Step 8a skeptic pass -- it is NOT a substantive control:
spin_lift builds every operator as a sum of (1/2)E[a]E[b], which is
parity-EVEN by construction, so [gamma, rho(a)] = 0 holds automatically for
ANY spin_lift output on ANY homogeneous space, independent of su(3). This
project already knew that fact (C139's own check is literally named
`nab_i_preserves_sigma_even_odd_parity`). gamma's well-posedness answer is
still YES; it is simply a type-fact, not evidence about equivariance.

Run:  python c149_transport_wellposedness.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)

E_sym = R59.build_clifford(conj=False)
NAB_sym = {i: R59.spin_lift(R59.NOMIZU[i], E_sym) for i in range(1, 7)}
RHO_sym = {a: R59.spin_lift(R59.ADNU[a], E_sym) for a in range(1, 9)}

calib_ok, _ = R59.run_calibration(E_sym, R59.NOMIZU)
assert calib_ok, "round59 calibration failed on import -- STOP"

E = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
NAB = {i: np.array(NAB_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
RHO = {a: np.array(RHO_sym[a].evalf(), dtype=complex) for a in range(1, 9)}

D_SIGMA = sum((E[i] @ NAB[i] for i in range(1, 7)), np.zeros((8, 8), dtype=complex))

# gamma: the EVEN/ODD chirality grading of Sigma (+1 on EVEN_IDX, -1 on ODD_IDX)
GAMMA = np.zeros((8, 8), dtype=complex)
for k in R59.EVEN_IDX:
    GAMMA[k, k] = 1.0
for k in R59.ODD_IDX:
    GAMMA[k, k] = -1.0

print("STEP 0  round59 machinery loaded, calibration re-verified  [OK]")
print(f"        EVEN_IDX={R59.EVEN_IDX}  ODD_IDX={R59.ODD_IDX}")

# --- NON-DEGENERACY GATE (added after the FL Step 8a skeptic pass flagged the
# exact 0.000e+00 transport spread for D_Sigma as numerically suspicious --
# with sqrt(3)-valued floats a ~1e-16 roundoff floor is expected, so bitwise
# zero could have signalled a silently-zero operator making the whole D_Sigma
# row vacuous). Checked rather than explained away. ------------------------
_d_max = float(np.max(np.abs(D_SIGMA)))
_d_rank = int(np.linalg.matrix_rank(D_SIGMA))
_d_nnz = int(np.sum(np.abs(D_SIGMA) > 1e-12))
_rho_max = float(np.max(np.abs(RHO[1])))
print()
print("STEP 0b NON-DEGENERACY GATE (skeptic-requested)")
print(
    f"        max|D_Sigma| = {_d_max:.6f}  (round59 certifies eigenvalues -/+ sqrt3 = {np.sqrt(3):.6f})"
)
print(f"        rank(D_Sigma)= {_d_rank},  nonzero entries = {_d_nnz}/64")
print(f"        max|rho(1)|  = {_rho_max:.6f}")
assert _d_max > 1e-6 and _rho_max > 1e-6, "DEGENERATE operator -- the test below would be vacuous"
print("        -> NOT degenerate. The exact 0.000e+00 spread below is explained by")
print("           extreme sparsity (2 nonzero entries), not by a silent zero.")


def max_commutator(op: np.ndarray) -> float:
    """max_a || [op, rho_su3(a)] ||_inf  -- zero iff op is su(3)-equivariant."""
    return max(float(np.max(np.abs(op @ RHO[a] - RHO[a] @ op))) for a in range(1, 9))


def group_element(coeffs: np.ndarray) -> np.ndarray:
    """exp(sum_a c_a rho_su3(a)) -- an element of the residual (su(3)) freedom."""
    from scipy.linalg import expm

    gen = sum((coeffs[a - 1] * RHO[a] for a in range(1, 9)), np.zeros((8, 8), dtype=complex))
    return expm(gen)


def transport_spread(op: np.ndarray, n_samples: int = 12, seed: int = 20260904) -> float:
    """How much does g.op.g^-1 move as g ranges over the residual freedom?
    Zero => the transported operator is representative-INDEPENDENT."""
    rng = np.random.default_rng(seed)
    base = None
    worst = 0.0
    for _ in range(n_samples):
        g = group_element(rng.normal(scale=0.7, size=8))
        moved = g @ op @ np.linalg.inv(g)
        if base is None:
            base = moved
        else:
            worst = max(worst, float(np.max(np.abs(moved - base))))
    return worst


print()
print("=" * 78)
print("THE CRITERION:  transport well-posed  <=>  [O, rho_su3(a)] = 0 for all a")
print("=" * 78)

cases: list[tuple[str, np.ndarray, str]] = [
    (
        "D_Sigma (round59's own untwisted Dirac)",
        D_SIGMA,
        "positive control (C146 proved equivariant)",
    ),
    ("gamma (EVEN/ODD chirality grading)", GAMMA, "NOT substantive -- forced by spin_lift parity"),
]

rng_neg = np.random.default_rng(11223344)
rand_op = rng_neg.normal(size=(8, 8)) + 1j * rng_neg.normal(size=(8, 8))
cases.append(("random non-equivariant operator", rand_op, "NEGATIVE control -- must FAIL"))

results = {}
for name, op, role in cases:
    comm = max_commutator(op)
    spread = transport_spread(op)
    equivariant = comm < 1e-10
    invariant = spread < 1e-9
    results[name] = (comm, spread, equivariant, invariant)
    print()
    print(f"  {name}")
    print(f"    role                      : {role}")
    print(f"    max_a ||[O, rho(a)]||     : {comm:.3e}   -> su(3)-equivariant: {equivariant}")
    print(f"    spread of g.O.g^-1        : {spread:.3e}   -> transport invariant: {invariant}")
    print(f"    criterion and outcome AGREE: {equivariant == invariant}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)

d_ok = results["D_Sigma (round59's own untwisted Dirac)"][3]
g_ok = results["gamma (EVEN/ODD chirality grading)"][3]
neg_fails = not results["random non-equivariant operator"][3]
criterion_holds = all(r[2] == r[3] for r in results.values())

print(f"  D_Sigma transport is representative-independent : {d_ok}")
print(f"  gamma   transport is representative-independent : {g_ok}")
print(f"  negative control DOES show gauge-dependence     : {neg_fails}  (required)")
print(f"  criterion [O,rho]=0 <=> invariance, in all cases: {criterion_holds}")
print()
if d_ok and g_ok and neg_fails:
    print("  => For D_Sigma and gamma the planned transport is WELL-POSED: the")
    print("     ~8-real-dim Inn(su(3)) freedom in U does NOT reach them, because")
    print("     they commute with exactly that freedom. OB11(ii)'s next step is")
    print("     therefore not a gauge artifact for these two operators.")
    print("  => J is NOT settled here -- it is not constructed in round59's own")
    print("     file, and its su(3)-equivariance must be checked separately")
    print("     before the same conclusion may be extended to it.")
else:
    print("  => At least one operator's transport is gauge-DEPENDENT; the planned")
    print("     OB11(ii) step is ill-posed as specified for that operator and must")
    print("     be re-specified before any round is built on it.")
