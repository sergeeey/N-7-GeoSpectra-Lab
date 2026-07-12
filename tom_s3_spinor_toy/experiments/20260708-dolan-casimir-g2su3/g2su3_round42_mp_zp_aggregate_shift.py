"""
Round 42 (2026-07-12): investigate the M_p-vs-Z_p L4A convention
question (Rounds 23-26) -- the user's own detailed follow-up to Round
41 proposed determining which combination of Round 25's 5 known Delta
pieces correctly groups into R/4, nabla*nabla, and F_{S^-}, hoping to
finally resolve the "8/45 vs ~1" tension. Investigation surfaced a
genuine, deeper research gap than initially scoped -- reported here
HONESTLY rather than papered over.

INVESTIGATION SUMMARY (research agents + own reads, no fabrication):
Round 26 isolated `-sum Z_p^2` (Agricola's canonical, t=0, connection)
ONLY as a single AGGREGATE 8x8 quantity, via subtraction from
Dslash_mat^2 -- established: `(-sum Zp^2) - (-sum Mp^2) = H -
(1/2)*Id - (7/4)*Casimir_su3` (call this `Delta_HCas`). Individual
Z_p matrices (analogous to this project's own `M_p`, built via
`nabla_g`) were NEVER constructed anywhere in this project.

A "pure rescaling" hypothesis (Z_p := 2t*M_p literally, giving Z_p=0
at t=0) was tested and COMPUTATIONALLY FALSIFIED against Round 26's
own aggregate identity (would require sum M_p^2 == Delta_HCas, which
is false -- confirmed directly, sum M_p^2 = -(1/2)*Id+(1/4)*Casimir_su3
in closed form, a completely different expression).

Two research agents read Agricola 2002 ("Connections on Naturally
Reductive Spaces...", arXiv:math/0202094v1) and Agricola-Hofmann-Lawn
2023 ("invariant spinors") DIRECTLY. Found: the connection family
nabla^t_X Y = nabla^0_X Y + t*[X,Y]_m, with Lambda^0_m=0 (canonical)
and Lambda^{1/2}_m = Lambda^g (Levi-Civita, THIS project's own
LEVI_CIVITA_NOMIZU table). Did NOT find an explicit per-index SPIN-LIFT
formula for the canonical connection specific to S^6=G2/SU(3) -- only
the AGGREGATE Dirac operator D^0=-H (already established, Round 27).
Building genuine individual Z_p matrices would require either reading
further into the primary sources (AHL2023's own "Example 4.18",
flagged but not read due to research-agent budget) or original
derivation work with its own dedicated skeptic review -- correctly
identified by the user as a task NOT to force within this round.

SCOPE CHOSEN (via AskUserQuestion, user chose the safer, well-scoped
option): compute ONLY the piece of a hypothetical "Z_p-based nabla*nabla"
that IS expressible from the ALREADY-KNOWN aggregate `-sum Zp^2`
(equivalently, from `Delta_HCas`) -- WITHOUT needing individual Z_p --
leaving the genuine `sum_p Z_p tensor Z_p` cross-term EXPLICITLY,
PROMINENTLY open (it structurally cannot be computed from the
aggregate alone; this is not a numerical gap, it is a missing
ingredient).

FINDING (compute-first, verified before writing this docstring): the
"aggregate-only" shift makes Delta's traceless (non-scalar) part
LARGER, not smaller -- Frobenius-norm^2 of the traceless part goes
from 160/9 (original, M_p-based) to 116/3 (Z_p aggregate-shifted,
missing cross-term). This does NOT mean switching to Z_p makes
Delta "more non-scalar" in any final sense -- the missing cross-term
could easily reverse this, or could be even larger. This result is
SUGGESTIVE/DIRECTIONAL ONLY, reported honestly, NOT a resolution.

HONEST LIMIT: this round does NOT resolve the M_p-vs-Z_p L4A
convention question, does NOT establish which connection is the
"physically correct" one for the preprint's own R/4 argument, does
NOT resolve the 8/45-vs-~1 L4A tension, and does NOT touch
preprint.tex. Building genuine individual Z_p matrices remains a
larger, separate research task for a future round (or requires
returning to the primary literature).
"""

import sympy as sp

from g2su3_explicit_clifford import DIM
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def kron(A, B):
    rA, cA = A.shape
    rB, cB = B.shape
    out = sp.zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            if A[i, j] != 0:
                out[i * rB : (i + 1) * rB, j * cB : (j + 1) * cB] += A[i, j] * B
    return out


def compress_2x2(op, va, vb):
    """LINEAR compression, matching Round 25's own compress_2x2 exactly."""
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def main():
    print("=" * 70)
    print("SETUP: rebuild H, Casimir_su3 (all via ALREADY-established")
    print("Rounds 4-41 constructions)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    print("\n" + "=" * 70)
    print("STEP A: Delta_HCas := H - (1/2)*Id - (7/4)*Casimir_su3, Round 26's")
    print("own established aggregate identity: (-sum Zp^2)-(-sum Mp^2) =")
    print("Delta_HCas. Cited unchanged (individual Z_p unavailable, see")
    print("module docstring); this is an 8x8 object, no per-p Z_p needed.")
    print("=" * 70)
    Delta_HCas = sp.simplify(H - sp.Rational(1, 2) * Id8 - sp.Rational(7, 4) * Casimir_su3)
    print("  Delta_HCas built.")

    print("\n" + "=" * 70)
    print("STEP B: compress kron(Delta_HCas,Id8) and kron(Id8,Delta_HCas)")
    print("on span(w_a,w_b) (Round 23/24/25's own 2-dim SU(3)-invariant")
    print("subspace) -- the ONLY part of a 'Z_p-based nabla*nabla' that")
    print("is expressible from the aggregate alone")
    print("=" * 70)
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    piece_left = kron(Delta_HCas, Id8)
    piece_right = kron(Id8, Delta_HCas)
    left_2x2 = compress_2x2(piece_left, w_a, w_b)
    right_2x2 = compress_2x2(piece_right, w_a, w_b)
    print(f"  compress(kron(Delta_HCas,Id8))|_2dim = {list(left_2x2)}")
    print(f"  compress(kron(Id8,Delta_HCas))|_2dim = {list(right_2x2)}")
    expected_left = sp.Matrix([[sp.Rational(-17, 6), 0], [0, sp.Rational(-1, 2)]])
    left_ok = left_2x2 == expected_left
    right_ok = right_2x2 == expected_left
    print(f"  left matches verified value [[-17/6,0],[0,-1/2]]? {left_ok}")
    print(f"  right matches verified value [[-17/6,0],[0,-1/2]]? {right_ok}")
    assert left_ok, f"left piece changed from verified value: {left_2x2}"
    assert right_ok, f"right piece changed from verified value: {right_2x2}"

    shift_2x2 = sp.simplify(left_2x2 + right_2x2)
    print(f"  shift (left+right) = {list(shift_2x2)}")

    print("\n" + "=" * 70)
    print("STEP C: assemble Delta^(Z,partial)_2x2 using Round 41's own")
    print("cross_casimir_2x2 (re-derived in-script) and Round 24/25's")
    print("Delta_2x2 (cited) -- MISSING the genuine sum Z_p(x)Z_p term")
    print("=" * 70)
    Delta_2x2 = sp.Matrix([[sp.Rational(5, 2), sp.Rational(4, 3)], [4, sp.Rational(5, 2)]])
    cross_casimir_2x2 = sp.Matrix([[0, sp.Rational(-1, 3)], [-1, 0]])
    print(f"  Delta_2x2 (Round 24/25's own known value) = {list(Delta_2x2)}")
    print(f"  cross_casimir_2x2 (Round 41's own known value) = {list(cross_casimir_2x2)}")

    Delta_Z_partial = sp.simplify(Delta_2x2 - cross_casimir_2x2 - shift_2x2)
    print(f"\n  Delta^(Z,partial)_2x2 := Delta_2x2 - cross_casimir_2x2 - shift")
    print(f"  = {list(Delta_Z_partial)}")
    print("  NOTE: this subtracts the M_p-based cross term entirely and")
    print("  does NOT add back any Z_p-based cross term (unavailable) --")
    print("  so Delta^(Z,partial) is NOT the true Z_p-based Delta. It")
    print("  answers only: 'what if we replaced JUST the aggregate")
    print("  Casimir-type contribution, holding the cross-term at zero')")

    print("\n" + "=" * 70)
    print("STEP D: compare non-scalarity magnitude (Frobenius norm^2 of")
    print("the traceless part) -- original M_p-based Delta vs the")
    print("aggregate-only Z-partial version")
    print("=" * 70)

    def offscale(M):
        tr = M.trace() / 2
        traceless = sp.simplify(M - tr * sp.eye(2))
        return traceless, tr

    tl_orig, tr_orig = offscale(Delta_2x2)
    tl_zp, tr_zp = offscale(Delta_Z_partial)
    norm2_orig = sp.simplify(sum(x**2 for x in tl_orig))
    norm2_zp = sp.simplify(sum(x**2 for x in tl_zp))
    print(f"  Original Delta: trace/2={tr_orig}, traceless={list(tl_orig)}")
    print(f"  Z-partial Delta: trace/2={tr_zp}, traceless={list(tl_zp)}")
    print(f"  Frobenius norm^2 of traceless part (original) = {norm2_orig}")
    print(f"  Frobenius norm^2 of traceless part (Z-partial) = {norm2_zp}")
    more_nonscalar = norm2_zp > norm2_orig
    print(f"  Z-partial version is MORE non-scalar than original? {more_nonscalar}")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  The aggregate-only shift (replacing M_p's own Casimir-type")
    print("  contribution with Z_p's, per Round 26's established")
    print("  difference, while leaving the cross-term unchanged/absent)")
    print(f"  makes Delta's traceless part LARGER: {norm2_orig} -> {norm2_zp}.")
    print()
    print("  HONEST LIMIT: this is SUGGESTIVE, NOT DEFINITIVE. Both FL Step 8a")
    print("  skeptics + synthesis found the incompleteness here is actually")
    print("  THREE missing ingredients, not one: (1) the sum_p Z_p(x)Z_p")
    print("  cross-term (requires individual Z_p, unavailable); (2) the")
    print("  left+right shift convention used here is an UNSTATED assumption")
    print("  not directly derivable from Round 41's own left-only Delta")
    print("  decomposition -- a 'left-only' alternative gives 61/2 instead of")
    print("  116/3 (direction-robust, magnitude-fragile); (3) M_p ALSO appears")
    print("  unswapped inside T12+T21 and TORSION_E, not just the aggregate")
    print("  Casimir-type piece shifted here. This round does NOT resolve the")
    print("  M_p-vs-Z_p L4A convention question, does NOT establish which")
    print("  connection is 'physically correct', does NOT resolve the")
    print("  8/45-vs-~1 L4A tension, and does NOT touch preprint.tex.")


if __name__ == "__main__":
    main()
