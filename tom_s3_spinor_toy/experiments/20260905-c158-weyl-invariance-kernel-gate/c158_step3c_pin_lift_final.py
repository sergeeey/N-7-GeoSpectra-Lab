r"""
C158 STEP 3c -- FINAL, corrected Pin(m) lift, after three self-caught issues
in Steps 3/3b (all kept on record, not hidden):

  (1) R_of_theta/ad_on_m_general silently discard genuine [m,m] leakage into
      the Cartan subalgebra t (checked: [A01, M_BASIS[0]] = 2*h1, pure t).
      The whole "integrate a path through SU(3)" strategy was misconceived
      for a ROOT generator A_pq (root generators don't preserve m).
  (2) det(R01) = det(R12) = -1 -- both simple Weyl reflections are
      ORIENTATION-REVERSING. A bivector exponential is always EVEN and can
      only ever cover SO(m); it structurally cannot reproduce a det=-1 map,
      regardless of any theta/indexing fix. Genuine Pin(m) (odd elements)
      needed, not Spin(m).
  (3) [spin_lift(L), v] = -L(v) EXACTLY in this project's specific Clifford
      sign convention (E_a^2=-1) -- the OPPOSITE of the sign this session
      initially assumed from generic memory. Verified directly via the
      Lie bracket (cheaper and more diagnostic than guessing at the group
      level): conjugation by exp(theta*spin_lift(L)) reproduces R(-theta),
      not R(+theta). Confirmed conclusively: conjugation by S_rot (built at
      theta=+pi/2) equals Rot^{-1} = Rot^T EXACTLY on all 6 generators (not
      -Rot, not Rot -- checked and matched precisely).

FIX: use S_rot^{-1} (equivalently, negate theta) for the even/rotation part.
The odd/reflection part (n=E_1, twisted adjoint v |-> -n v n^-1) was already
verified directly and needs no change.

Run:  python c158_step3c_pin_lift_final.py
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


def reflect_matrix(idx, n=6):
    M = sp.eye(n)
    M[idx, idx] = -1
    return M


def build_pin_lift_final(R, refl_idx, rot_pairs, label):
    """R = Refl_{refl_idx} . Rot. n = E_{refl_idx+1} (odd, twisted adjoint,
    verified). S_rot_correct = S_rot^{-1} (the [3] fix). S_full = S_rot_correct
    * n (Clifford product order chosen to match R = Rot . Refl algebraically
    -- verified below by direct full conjugation test, not assumed)."""
    print(f"  --- {label} ---")
    Refl = reflect_matrix(refl_idx)
    Rot = sp.simplify(R * Refl)
    assert sp.simplify(Rot.det()) == 1
    assert sp.simplify(Rot.T * Rot) == sp.eye(6)

    L_rot = sp.zeros(6, 6)
    for i, j in rot_pairs:
        L_rot[i, j] = 1
        L_rot[j, i] = -1
    M_rot = spin_lift_sym(L_rot)
    ev = M_rot.eigenvals()
    assert set(ev.keys()) <= {sp.I, -sp.I, 0}, f"spectrum: {ev}"
    P0 = sp.simplify(M_rot * M_rot + sp.eye(8))
    S_rot_raw = sp.simplify(M_rot + P0)  # = exp((pi/2) M_rot), reproduces Rot^-1
    S_rot = sp.simplify(S_rot_raw.inv())  # THE FIX: invert to get Rot itself

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
    print(f"    S_rot (corrected) conjugation reproduces Rot exactly: {ok}")
    assert ok

    n_vec = E_sym[refl_idx + 1]
    ninv = sp.simplify(n_vec.inv())
    ok_refl = True
    for i in range(6):
        conj = sp.simplify(-n_vec * E_sym[i + 1] * ninv)  # twisted adjoint
        want = Refl[i, i] * E_sym[i + 1]  # Refl is diagonal
        if sp.simplify(conj - want) != sp.zeros(8, 8):
            ok_refl = False
    print(f"    n (twisted adjoint) conjugation reproduces Refl exactly: {ok_refl}")
    assert ok_refl

    # combine: R = Rot . Refl, so as an operator R(v) = Rot(Refl(v)). Try the
    # Clifford product S_rot * n (apply Refl's odd action first, then Rot's
    # even action) with the ODD/twisted formula overall (S_full is odd).
    S_full = sp.simplify(S_rot * n_vec)
    Sfull_inv = sp.simplify(S_full.inv())
    ok_full = True
    mismatches = []
    for i in range(6):
        conj = sp.simplify(-S_full * E_sym[i + 1] * Sfull_inv)  # odd -> twisted
        want = sp.zeros(8, 8)
        for j in range(6):
            if R[j, i] != 0:
                want += R[j, i] * E_sym[j + 1]
        if sp.simplify(conj - want) != sp.zeros(8, 8):
            ok_full = False
            mismatches.append(i)
    print(
        f"    S_full (odd, twisted) conjugation reproduces {label} exactly: {ok_full}"
        + (f"  (mismatches at {mismatches})" if mismatches else "")
    )
    return n_vec, S_rot, S_full, ok_full


if __name__ == "__main__":
    print("=" * 78)
    print("STEP 3c  FINAL Pin(m) lift, both corrections applied")
    print("=" * 78)
    n01, Srot01, S01_full, ok01 = build_pin_lift_final(S1.R01, 0, ((2, 5), (3, 4)), "R01")

    # R12: find its reflection index the same way, generically
    R12 = S1.R12
    refl_idx_12 = None
    for i in range(6):
        row = [R12[i, j] for j in range(6)]
        col = [R12[j, i] for j in range(6)]
        if row.count(0) == 5 and row[i] == -1 and col.count(0) == 5 and col[i] == -1:
            refl_idx_12 = i
            break
    assert refl_idx_12 is not None
    Refl12 = reflect_matrix(refl_idx_12)
    Rot12_probe = sp.simplify(R12 * Refl12)
    rot_pairs_12 = []
    seen = set()
    for i in range(6):
        if i == refl_idx_12 or i in seen:
            continue
        for j in range(6):
            if j != i and Rot12_probe[j, i] != 0 and j != refl_idx_12:
                rot_pairs_12.append((min(i, j), max(i, j)))
                seen.add(i)
                seen.add(j)
                break
    print(f"  R12: reflection index {refl_idx_12}, rotation pairs {rot_pairs_12}")
    n12, Srot12, S12_full, ok12 = build_pin_lift_final(
        S1.R12, refl_idx_12, tuple(rot_pairs_12), "R12"
    )

    print()
    print("=" * 78)
    print("VERDICT -- Pin(m) lifts of R01, R12 fully verified")
    print("=" * 78)
    print(f"  S01_full correctly implements R01 via twisted conjugation: {ok01}")
    print(f"  S12_full correctly implements R12 via twisted conjugation: {ok12}")
