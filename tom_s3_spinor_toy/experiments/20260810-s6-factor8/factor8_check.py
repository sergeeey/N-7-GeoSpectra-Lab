"""A1: is the S6-side "factor 8" the same mismatch as the S3-side factor 2?

WHAT I CLAIMED EARLIER TODAY, and am now testing rather than repeating. C38's
decision.md, its commit message, activeContext and a pearl all state:

    "the SAME rep-content-vs-kernel-dimension mismatch exists on the S6 side at
     ratio 8 (Spin(7) spinor = 8 vs ker(D_S6,twisted) = 1) with NO analogue of t
     there -- so the pattern is systematic and only one of its two instances now
     has a mechanism."

That was written from a table I typed, not from a computation. Two things in it
need checking, and if either fails the claim is mine to withdraw:

  (1) is the right S6-side comparison really 1-vs-8?
      G74A states the twist is by S^- = T^{1,0}S6 (+) trivial = 3 (+) 1 under
      SU(3) -- i.e. FOUR-dimensional. Framework A's 8 is the FULL Dirac spinor
      of Spin(6), which splits by chirality as 8 = 4 (+) 4bar = S^+ (+) S^-.
      If so, comparing ker(D (x) S^-) against 8 compares a kernel to a bundle
      the operator is not twisted by.

  (2) is there really "no analogue of t"?
      On S3 the kernel turned out to be the subspace of the fibre invariant
      under ONE of the two SU(2) factors (C38). If on S6 the kernel is likewise
      the SU(3)-singlet part of the twist bundle, then the two sides follow ONE
      rule and there is no unexplained residue at all.

METHOD. Build the Spin(6) spinor module from this repo's own s6-harm-g0
gammas, split it by chirality, restrict g10b's explicit su(3) subset of so(6),
and count singlets in each piece by joint-kernel dimension -- the same
technique C40 used on the octonion module.

PREDICTION, recorded before running (this is the point of the mode):
  8 = 4 (+) 4bar,  each half = 3 (+) 1 under SU(3),  so ONE singlet per half
  and TWO in the full 8. If that holds, "1 vs 8" is the wrong pairing and the
  correct one is 1 vs 4 -- ratio 4, matching the S3 side's structure (2 of 4)
  rather than standing apart from it.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_factor8.json"
results: dict = {}


def load(name: str, rel: str):
    d = (HERE.parent / rel).resolve()
    if str(d) not in sys.path:
        sys.path.insert(0, str(d))
    spec = importlib.util.spec_from_file_location(name, d / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


print("=" * 78)
print("A1 -- is the S6 'factor 8' a real mismatch, or did I pair the wrong objects?")
print("=" * 78)

# --- STEP 1: the Spin(6) spinor module, from this repo's own S6 gammas -------
print("\nSTEP 1 -- build the 8-dim Spin(6) spinor module and split it by chirality")
s6 = load("s6_harm_g0_clifford", "20260615-s6-harm-g0")
G = [np.array(m.tolist(), dtype=complex) for m in s6.G]
G7 = np.array((s6.G[0] * s6.G[1] * s6.G[2] * s6.G[3] * s6.G[4] * s6.G[5]).tolist(), dtype=complex)
# normalise the chirality operator to eigenvalues +-1
G7 = G7 / np.sqrt(np.abs(np.linalg.det(G7)) ** (1 / 8)) if False else G7
w = np.linalg.eigvals(G7)
print(f"  6 gammas, 8x8. chirality operator eigenvalues: {sorted(set(np.round(w, 6)))}")
evals, evecs = np.linalg.eig(G7)
plus = evecs[:, np.isclose(evals, evals[np.argmax(evals.real)])]
minus = evecs[:, ~np.isclose(evals, evals[np.argmax(evals.real)])]
print(f"  chirality split: dim S+ = {plus.shape[1]}, dim S- = {minus.shape[1]}")
results["dim_full_spinor"] = 8
results["dim_S_plus"] = int(plus.shape[1])
results["dim_S_minus"] = int(minus.shape[1])

# --- STEP 2: su(3) acting on the spinor module ------------------------------
print("\nSTEP 2 -- lift g10b's explicit su(3) c so(6) to the spinor module")
g10b = load("g10b_su3_explicit", "20260618-g10b-su3-in-so6")
su3_vec = [np.array(m.tolist(), dtype=complex) for m in g10b.su3_generators()]
print(f"  su(3) generators in the 6 (vector rep): {len(su3_vec)}  (expect 8)")


def spinor_lift(X6: np.ndarray) -> np.ndarray:
    """so(6) element X (6x6 antisym) -> its action on the 8-dim spinor module.

    sigma(X) = sum_{a<b} X_ab * (1/4)[Gamma_a, Gamma_b].

    WHY the exact factor matters and is not cosmetic: a SCALED representation is
    not a representation -- brackets scale quadratically while the map scales
    linearly, so lambda*sigma fails [sigma(X),sigma(Y)] = sigma([X,Y]) for any
    lambda != 1. The first version of this function carried an extra 1/2 and the
    homomorphism residual came back 5.0e-01, i.e. not a Lie map at all. The
    singlet counts happened to be unaffected (a joint kernel is invariant under
    scaling) AND happened to match the prediction written at the top of this
    file -- which is exactly the "right answer from broken machinery" mode this
    project pearled twice on 2026-08-10. Fixed, and the residual is asserted
    below rather than merely printed.
    """
    out = np.zeros((8, 8), dtype=complex)
    for a in range(6):
        for b in range(a + 1, 6):
            out += X6[a, b] * (G[a] @ G[b] - G[b] @ G[a]) / 4
    return out


su3_spin = [spinor_lift(X) for X in su3_vec]
# sanity: the lift must be a Lie homomorphism
res = 0.0
for i in range(len(su3_vec)):
    for j in range(len(su3_vec)):
        lhs = su3_spin[i] @ su3_spin[j] - su3_spin[j] @ su3_spin[i]
        rhs = spinor_lift(su3_vec[i] @ su3_vec[j] - su3_vec[j] @ su3_vec[i])
        res = max(res, float(np.max(np.abs(lhs - rhs))))
print(f"  bracket-homomorphism residual (must be ~0): {res:.2e}")
assert res < 1e-9, f"spinor lift is NOT a Lie homomorphism (residual {res:.2e}) -- singlet counts from it are meaningless"
results["lift_bracket_residual"] = res


def singlets(gens: list[np.ndarray], basis: np.ndarray | None = None) -> int:
    """dim of the joint kernel -- i.e. the number of singlets."""
    mats = gens if basis is None else [basis.conj().T @ g @ basis for g in gens]
    stacked = np.vstack(mats)
    sv = np.linalg.svd(stacked, compute_uv=False)
    n = mats[0].shape[1]
    return int(n - np.sum(sv > 1e-8))


# --- STEP 3: singlet counts -------------------------------------------------
print("\nSTEP 3 -- SU(3)-singlet counts (joint-kernel dimension)")
n_full = singlets(su3_spin)
n_plus = singlets(su3_spin, plus)
n_minus = singlets(su3_spin, minus)
print(f"  singlets in the FULL 8 (framework A's S6-side fibre): {n_full}")
print(f"  singlets in S+ (4):                                   {n_plus}")
print(f"  singlets in S- (4) -- THE BUNDLE THE TWIST USES:      {n_minus}")
results["su3_singlets_full_8"] = n_full
results["su3_singlets_S_plus"] = n_plus
results["su3_singlets_S_minus"] = n_minus

# --- STEP 4: NEGATIVE CONTROL ------------------------------------------------
print("\nSTEP 4 -- NEGATIVE CONTROL: the full so(6) has FEWER singlets than su(3)")
print("  (a bigger group cannot have more invariants; if this comes out equal or")
print("   larger the counting method is wrong)")
so6 = [np.array(M.tolist(), dtype=complex) for _, M in g10b.so6_generators()]
so6_spin = [spinor_lift(X) for X in so6]
n_so6 = singlets(so6_spin, minus)
ctrl_ok = n_so6 <= n_minus
print(
    f"  so(6)-singlets in S-: {n_so6}   vs su(3)'s {n_minus}   -> control {'PASSES' if ctrl_ok else 'FAILS'}"
)
results["so6_singlets_S_minus"] = n_so6
results["control_passes"] = bool(ctrl_ok)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
wrong_pairing = (n_minus == 1) and (minus.shape[1] == 4)
verdict = "MY_FACTOR8_CLAIM_WAS_A_WRONG_PAIRING" if (wrong_pairing and ctrl_ok) else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if verdict.startswith("MY_"):
    print("  The twist bundle is S- and it is FOUR-dimensional, not eight.")
    print(f"  ker(D (x) S-) = 1 sits inside a 4-dim bundle with exactly {n_minus} SU(3)-singlet.")
    print()
    print("  So the S6 comparison is 1-of-4, NOT 1-of-8. Framework A's 8 is the FULL")
    print("  Dirac spinor S+ (+) S-, a bundle the twisted operator is not twisted by.")
    print()
    print("  UNIFIED RULE, now holding on BOTH factors:")
    print("      kernel = the invariant/singlet subspace of the bundle actually used")
    print("      S3:  2 of 4   (invariant under one SU(2) factor)      -- C38")
    print("      S6:  1 of 4   (SU(3)-singlet of S-)                   -- here")
    print()
    print("  => there is NO unexplained systematic residue. My earlier statement")
    print("     that 'the pattern is confirmed on both factors and only one has a")
    print("     mechanism' is WITHDRAWN: I compared a kernel against a bundle the")
    print("     operator does not act on.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
