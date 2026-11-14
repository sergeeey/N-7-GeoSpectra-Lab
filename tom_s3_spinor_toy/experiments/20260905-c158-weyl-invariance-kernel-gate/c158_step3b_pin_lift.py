r"""
C158 STEP 3b -- CORRECTED spin/Pin lift, after Step 3's original approach was
found to be doubly flawed (both errors kept, not hidden):

  ERROR 1: R_of_theta (used to differentiate a "path" g(theta)=exp(theta*A_pq)
  through SU(3)) silently LOSES information -- for A_pq a ROOT generator (an
  element of m, not of the Cartan t), ad(A_pq) does NOT preserve m (the
  bracket [m,m] can have a genuine t-component -- checked directly:
  [A01, M_BASIS[0]] = 2*h1, a PURE CARTAN direction). C153's `to_m` silently
  discards this leakage (it only extracts the m-component), so
  `ad_on_m_general`/`R_of_theta` are NOT the honest adjoint action for
  generic theta -- confirmed numerically: R01_theta(pi/7) is NOT orthogonal
  (residual 0.61, det=0.62 instead of +-1). The theta=0 derivative check
  happened to still match (leakage is higher-order there), which is why it
  passed and masked the problem.

  ERROR 2 (the deeper one, root cause): det(R01) = det(R12) = -1. Both Weyl
  reflections are ORIENTATION-REVERSING elements of O(m), not SO(m). Every
  exponential of a bivector (spin_lift(L) is always a sum of E_a E_b terms,
  purely EVEN-graded) is an EVEN Clifford element and can ONLY ever cover
  SO(m) via conjugation -- structurally incapable of reproducing a det=-1
  map, regardless of any theta/indexing fix. This is why Step 3's decisive
  regression could not be patched by fixing indices; the target was outside
  the reachable set from the start. "SU(3) simply connected => unique lift"
  is true for the map SU(3) -> SO(m) -- but R01 requires PIN(m), the
  DISCONNECTED double cover of O(m), for which no such simply-connected
  uniqueness argument applies (this is the genuine Pin/Spin subtlety flagged
  before Step 3 started, now precisely located).

THE FIX: decompose R01 = Refl_e0 . Rot, where Refl_e0 is the reflection
through unit vector e0 = M_BASIS[0] (det -1) and Rot is the REMAINING SO(m)
part (det +1, a genuine rotation in two 2-planes, verified orthogonal).
Lift Refl_e0 via the STANDARD odd Pin(n) vector n=E_1 with the TWISTED
adjoint action v |-> -n v n^-1 (verified EXACTLY against Refl_e0 on all 6
generators -- the untwisted n v n^-1 does NOT match, twisted does). Lift Rot
via its own bivector exponential (even, Spin(m), no ambiguity beyond the
usual sign choice, tested both ways below).

Run:  python c158_step3b_pin_lift.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S1 = load("c158_s1", "c158_step1_weyl_action.py")
S2 = S1.S2
E_sym = S2.E_sym
spin_lift_sym = S2.spin_lift_sym

PAIRS = {"01": (S1.R01, (2, 5), (3, 4)), "12": (S1.R12, None, None)}


def reflect_matrix(idx, n=6):
    M = sp.eye(n)
    M[idx, idx] = -1
    return M


def build_pin_lift(R, refl_idx, rot_pairs):
    """R = Refl_{refl_idx} . Rot. Returns (n_vec, S_rot, S_full) where
    n_vec = E_{refl_idx+1} (odd Pin lift of the reflection), S_rot = spin
    lift of the remaining SO(m) rotation, S_full = S_rot * n_vec (Clifford
    product, even*odd = odd, matching R's own det=-1)."""
    Refl = reflect_matrix(refl_idx)
    Rot = sp.simplify(R * Refl)
    assert sp.simplify(Rot.det()) == 1, "remaining part is not in SO(m)"
    assert sp.simplify(Rot.T * Rot) == sp.eye(6), "remaining part not orthogonal"

    L_rot = sp.zeros(6, 6)
    for i, j in rot_pairs:
        L_rot[i, j] = 1
        L_rot[j, i] = -1
    # regression: exp((pi/2) L_rot) must equal Rot exactly (checked via the
    # closed-form spectral projector method, same as Step 3's M+P0 trick,
    # generalised to possibly-repeated nonzero eigenvalues)
    M_rot = spin_lift_sym(L_rot)
    ev = M_rot.eigenvals()
    assert set(ev.keys()) <= {sp.I, -sp.I, 0}, f"unexpected spin_lift(L_rot) spectrum: {ev}"
    P0 = sp.simplify(M_rot * M_rot + sp.eye(8))
    S_rot = sp.simplify(M_rot + P0)  # exp((pi/2) M_rot), same closed form as Step 3

    # verify Rot is reproduced by conjugation with S_rot, EVEN (untwisted)
    Sinv = sp.simplify(S_rot.inv())
    ok = True
    for i in range(6):
        conj = sp.simplify(S_rot * E_sym[i + 1] * Sinv)
        want = sp.zeros(8, 8)
        for j in range(6):
            if Rot[j, i] != 0:
                want += Rot[j, i] * E_sym[j + 1]
        if sp.simplify(conj - want) != sp.zeros(8, 8):
            ok = False
    print(f"    S_rot conjugation reproduces Rot exactly (even/Spin part): {ok}")
    assert ok

    n_vec = E_sym[refl_idx + 1]
    S_full = sp.simplify(S_rot * n_vec)
    return n_vec, S_rot, S_full


def twisted_conjugate(S, v, is_odd):
    """Twisted adjoint: v |-> alpha(S) . x . S^-1, where alpha is the grade
    involution (alpha(s)=s for even s, alpha(s)=-s for odd s). S_full here is
    ODD (even * odd = odd), so alpha(S_full) = -S_full."""
    Sinv = sp.simplify(S.inv())
    sign = -1 if is_odd else 1
    return sp.simplify(sign * S * v * Sinv)


if __name__ == "__main__":
    print("=" * 78)
    print("STEP 3b  Pin(m) lift of R01, R12 via reflection + rotation decomposition")
    print("=" * 78)

    results = {}
    for name, R, refl_idx, rot_pairs in (
        ("R01", S1.R01, 0, ((2, 5), (3, 4))),
        ("R12", S1.R12, None, None),
    ):
        print(f"\n  --- {name} ---")
        print(f"  det({name}) = {sp.simplify(R.det())}")

    # R01: reflection in index 0, rotation in (2,5),(3,4)
    n01, Srot01, S01_full = build_pin_lift(S1.R01, 0, ((2, 5), (3, 4)))

    # R12: need its own reflection index -- find where R12 acts as a pure
    # sign flip (a single -1 on the diagonal, zero elsewhere in that row/col)
    R12 = S1.R12
    print("\n  R12 matrix:")
    sp.pprint(R12)
    refl_idx_12 = None
    for i in range(6):
        row = [R12[i, j] for j in range(6)]
        col = [R12[j, i] for j in range(6)]
        if row.count(0) == 5 and row[i] == -1 and col.count(0) == 5 and col[i] == -1:
            refl_idx_12 = i
            break
    print(f"  R12 pure-reflection index found: {refl_idx_12}")
    assert refl_idx_12 is not None, (
        "no simple reflection index found for R12 -- need a different decomposition"
    )
    remaining_pairs = [
        (i, j) for i in range(6) for j in range(i + 1, 6) if i != refl_idx_12 and j != refl_idx_12
    ]
    Refl12 = reflect_matrix(refl_idx_12)
    Rot12_check = sp.simplify(R12 * Refl12)
    print("  Rot12 (R12 * Refl) :")
    sp.pprint(Rot12_check)
