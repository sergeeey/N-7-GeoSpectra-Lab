"""
Round 37 (2026-07-12): close Round 30's (S2) -- "g2 is SIMPLE => the
space of Ad(G2)-invariant symmetric bilinear forms on g2 is exactly
1-dimensional (Schur's lemma on the adjoint representation)" -- cited
there as a STANDARD, textbook Lie-theory fact, not independently
re-derived. This round replaces the citation with a DIRECT
computational verification, specific to Appendix A's own concrete
14-generator matrix realization of g2 (Round 13), using ONLY the
already-established `nu(k)`/`decompose_g2` machinery -- no new
primitive data, no citation of Schur's lemma or g2's abstract
simplicity.

CORE FINDING: build the FULL adjoint action ad(nu_i), i=1..14, as
14x14 matrices in the {nu_1,...,nu_14} basis (via matrix commutators
[nu_i,nu_j] decomposed back into the g2 basis, `decompose_g2` -- this
machinery has existed since Round 13, just never used to build the
FULL 14x14 adjoint representation before). Solve the linear system
`ad(nu_i)^T Q + Q ad(nu_i) = 0` for ALL i=1..14 simultaneously, over
symmetric 14x14 matrices Q (105 independent entries, 1362 linear
equations after full expansion) -- the DEFINING condition for an
Ad(g2)-invariant symmetric bilinear form. RESULT: the solution space is
EXACTLY 1-dimensional (verified via `sympy.linsolve`'s own free-
parameter count, not assumed), and the UNIQUE (up to scale) solution,
normalized, is EXACTLY the identity matrix in the {nu_1,...,nu_14}
basis -- i.e. EXACTLY `B_0` (Round 30's own trace form,
`Tr(nu_k^T nu_l)=delta_kl`, already verified B_0-orthonormal in Round
30 STEPs A/B). This directly confirms Round 30's own (S2)+(S4)
conclusion ("Q = 1*B_0 exactly") from first principles specific to
this realization, not from citing g2's abstract simplicity.

WHY THIS MATTERS: Round 30's logical chain used (S2) as a LOAD-BEARING
step (needed to conclude Agricola's metric-defining form Q is
PROPORTIONAL to B_0, before (S4) pins the proportionality constant to
1). (S2) was previously "cited, not re-derived" (Round 30's own Honest
Scope). This round closes that specific gap for THIS project's own
concrete realization -- not a claim about the ABSTRACT Lie algebra g2
in general (that remains a standard fact, still true regardless), but
a direct verification that the SPECIFIC 14-generator matrix
realization this whole project's Phase 2 derivation chain rests on
(Rounds 13-36) actually HAS this property, checked, not assumed.

SECOND INVESTIGATION (post-skeptic: FALSIFIED then FIXED into a REAL
closure, not a null result -- see STEP E below): does this round ALSO
close Round 30's OTHER remaining caveat -- that Appendix A's `nu_8`
(unlike `nu_1..nu_7`, verbatim page transcriptions) was BACK-SOLVED
from the SAME calibration equation Round 30's S6' now checks? FIRST
ATTEMPT (Approach A): re-derive `nu_8` as "the B_0-orthogonal
complement of span{nu_1..nu_7} within h=su(3)" -- VERIFIED VACUOUS,
this specific approach IS circular (B_0-orthonormality of ALL of
{nu_1..nu_14}, Round 30 STEP A/B, already used nu_8's own formula to
verify its row/column). BOTH FL Step 8a skeptics independently caught
that this does NOT mean no independent path exists -- and both
proposed, and the synthesis agent implemented and verified, a genuinely
different, cheap, ALREADY-project-native approach (Approach B,
"bracket-closure"): su(3) has NO 7-dimensional subalgebra (standard
classification: dims 0,1,2,3,4,8 only), so {nu_1..nu_7} (mutually
B_0-orthonormal, nu_8-FREE -- 28 pairs, verified STEP E below) CANNOT
be bracket-closed; computing all C(7,2)=21 raw matrix commutators
[nu_i,nu_j] and B_0-projecting each onto span{nu_1..nu_7} (using ONLY
i,j<=7, nu_8-free) finds the escaping residual -- EXACTLY 2 of 21 pairs
escape ((2,3) and (4,5), both norm^2=3/4), normalizing either gives a
vector `hbar_8` that equals `nu_8` EXACTLY (up to overall sign, STEP
E below) -- a COMPLETE, independent re-derivation of nu_8 using ZERO
reference to its own formula, closing the k=8 back-solve caveat FULLY.
Round 34's octonion route (originally flagged as "necessary") was
NEVER needed -- an overclaim in this docstring's original version,
caught by both skeptics independently and fixed here.

HONEST SCOPE: closes BOTH of Round 30's remaining gaps -- (S2)'s
citation (STEPs A-D) AND the k=8 back-solve caveat (STEP E) -- for this
specific project realization. Does NOT close the (S7) corroboration-
only citation (uniqueness of the 8-dim irreducible Clifford module) --
Round 30's own docstring already marks S7 as "not independently load-
bearing", so it does not require closing for the S9 conclusion to
hold. Does NOT change any previously-established numeric value from
Rounds 4-36 -- this round only STRENGTHENS the justification for
ALREADY-established, ALREADY-used facts (Q=B_0, and nu_8's own value),
using zero new primitive data beyond what Appendix A (Round 13)
already provides.
"""

import sympy as sp

from g2su3_appendix_a_construction import decompose_g2, nu

N = 14


def main():
    print("=" * 70)
    print("STEP A: build the FULL adjoint action ad(nu_i), i=1..14, as 14x14")
    print("matrices in the {nu_1,...,nu_14} basis (matrix commutators")
    print("decomposed via decompose_g2 -- existing Round 13 machinery, never")
    print("used to build the FULL adjoint representation before)")
    print("=" * 70)
    AD = {}
    for i in range(1, N + 1):
        M = sp.zeros(N, N)
        for j in range(1, N + 1):
            comm = sp.simplify(nu(i) * nu(j) - nu(j) * nu(i))
            coeffs = decompose_g2(comm)
            for k, v in coeffs.items():
                M[k - 1, j - 1] = v
        AD[i] = M
    print(f"  built ad(nu_1)..ad(nu_{N}) as {N}x{N} matrices.")

    print("\n" + "=" * 70)
    print("STEP B (sanity check): each ad(nu_i) is antisymmetric in this")
    print("basis -- a NECESSARY consequence if an Ad-invariant form exists")
    print("and this basis is orthonormal w.r.t. it (checked directly, not")
    print("assumed)")
    print("=" * 70)
    all_antisym = all(sp.simplify(AD[i] + AD[i].T) == sp.zeros(N, N) for i in range(1, N + 1))
    print(f"  all ad(nu_i) antisymmetric in the {{nu_k}} basis? {all_antisym}")
    assert all_antisym, "ad(nu_i) is not antisymmetric -- unexpected structure"

    print("\n" + "=" * 70)
    print("STEP C: solve ad(nu_i)^T Q + Q ad(nu_i) = 0 for ALL i=1..14")
    print("simultaneously, over symmetric 14x14 Q (105 free entries) --")
    print("the DEFINING linear condition for an Ad(g2)-invariant symmetric")
    print("bilinear form on THIS specific realization")
    print("=" * 70)
    Qsyms = sp.symbols("q0:105")
    Q = sp.zeros(N, N)
    idx = 0
    for a in range(N):
        for b in range(a, N):
            Q[a, b] = Qsyms[idx]
            Q[b, a] = Qsyms[idx]
            idx += 1
    print(f"  {idx} free symmetric-matrix entries")

    eqs = []
    for i in range(1, N + 1):
        cond = sp.simplify(AD[i].T * Q + Q * AD[i])
        for a in range(N):
            for b in range(a, N):
                e = cond[a, b]
                if e != 0:
                    eqs.append(e)
    print(f"  {len(eqs)} nonzero linear equations (before solving)")

    sol = sp.linsolve(eqs, Qsyms)
    sol_list = list(sol)[0]
    free_syms = set()
    for expr in sol_list:
        free_syms |= expr.free_symbols
    print(f"  solution space dimension = {len(free_syms)}")
    assert len(free_syms) == 1, (
        f"expected the Ad(g2)-invariant-form space to be 1-dimensional "
        f"(closing Round 30's (S2) citation), got {len(free_syms)}"
    )
    print("  => (S2) CLOSED: 1-dimensional, verified DIRECTLY for this")
    print("  realization, not cited from g2's abstract simplicity.")

    print("\n" + "=" * 70)
    print("STEP D: normalize the unique solution and verify it equals")
    print("EXACTLY the identity matrix in the {nu_k} basis -- i.e. EXACTLY")
    print("B_0 (Round 30's own already-verified trace form), confirming")
    print("(S2)+(S4)'s conclusion 'Q=1*B_0 exactly' from first principles")
    print("=" * 70)
    (free_sym,) = free_syms
    Qconcrete = sp.zeros(N, N)
    idx = 0
    for a in range(N):
        for b in range(a, N):
            v = sp.simplify(sol_list[idx].subs({free_sym: 1}))
            Qconcrete[a, b] = v
            Qconcrete[b, a] = v
            idx += 1
    q_is_identity = Qconcrete == sp.eye(N)
    print(f"  unique invariant form (normalized) == Identity == B_0? {q_is_identity}")
    assert q_is_identity, "the unique invariant form does not equal B_0=Identity"

    print("\n" + "=" * 70)
    print("STEP E (post-skeptic FIX, both FL Step 8a skeptics independently")
    print("proposed this -- 'bracket-closure' approach): re-derive nu_8")
    print("using ONLY nu_1..nu_7 (verbatim page transcriptions, nu_8-free)")
    print("-- su(3) has NO 7-dim subalgebra, so {nu_1..nu_7} cannot be")
    print("bracket-closed; the escaping residual pins down nu_8 exactly,")
    print("with ZERO reference to nu_8's own formula anywhere")
    print("=" * 70)
    from itertools import combinations

    from g2su3_appendix_a_construction import nu as nu_fn

    all_ortho_17 = True
    for i, j in combinations(range(1, 8), 2):
        if sp.simplify(sp.trace(nu_fn(i).T * nu_fn(j))) != 0:
            all_ortho_17 = False
    for i in range(1, 8):
        if sp.simplify(sp.trace(nu_fn(i).T * nu_fn(i))) != 1:
            all_ortho_17 = False
    print(f"  nu_1..nu_7 mutually B_0-orthonormal (nu_8-FREE check)? {all_ortho_17}")
    assert all_ortho_17, "nu_1..nu_7 are not B_0-orthonormal -- STEP E premise fails"

    def project_and_residual(i, j):
        comm = sp.simplify(nu_fn(i) * nu_fn(j) - nu_fn(j) * nu_fn(i))
        proj = sp.zeros(8, 8)
        for k in range(1, 8):
            c = sp.simplify(sp.trace(nu_fn(k).T * comm))
            proj += c * nu_fn(k)
        return sp.simplify(comm - proj)

    escaping = []
    for i, j in combinations(range(1, 8), 2):
        residual = project_and_residual(i, j)
        normsq = sp.simplify(sp.trace(residual.T * residual))
        if normsq != 0:
            escaping.append((i, j, residual, normsq))
    print("  of C(7,2)=21 raw commutators [nu_i,nu_j] (i,j<=7), pairs escaping")
    print(f"  span{{nu_1..nu_7}}: {len(escaping)} -- {[(i, j) for i, j, _, _ in escaping]}")
    assert len(escaping) == 2, f"expected exactly 2 escaping pairs, got {len(escaping)}"

    i0, j0, res0, normsq0 = escaping[0]
    hbar8 = sp.simplify(res0 / sp.sqrt(normsq0))
    matches_pos = sp.simplify(hbar8 - nu_fn(8)) == sp.zeros(8, 8)
    matches_neg = sp.simplify(hbar8 + nu_fn(8)) == sp.zeros(8, 8)
    print(f"  hbar_8 (from pair {i0},{j0}, normalized) == +nu_8? {matches_pos}")
    print(f"  hbar_8 (from pair {i0},{j0}, normalized) == -nu_8? {matches_neg}")
    assert matches_pos or matches_neg, (
        "independently re-derived hbar_8 does not match nu_8 up to sign -- "
        "k=8 back-solve caveat NOT closed"
    )

    i1, j1, res1, normsq1 = escaping[1]
    hbar8_alt = sp.simplify(res1 / sp.sqrt(normsq1))
    cross_check = sp.simplify(hbar8 - hbar8_alt) == sp.zeros(8, 8) or sp.simplify(
        hbar8 + hbar8_alt
    ) == sp.zeros(8, 8)
    print(f"  cross-check: pair ({i1},{j1})'s own hbar_8 agrees (up to sign)? {cross_check}")
    assert cross_check, "the two escaping pairs give inconsistent hbar_8 candidates"

    closure_ok = True
    for i in range(1, 8):
        comm = sp.simplify(nu_fn(i) * hbar8 - hbar8 * nu_fn(i))
        proj = sp.zeros(8, 8)
        for k in range(1, 8):
            c = sp.simplify(sp.trace(nu_fn(k).T * comm))
            proj += c * nu_fn(k)
        c8 = sp.simplify(sp.trace(hbar8.T * comm))
        proj += c8 * hbar8
        if sp.simplify(comm - proj) != sp.zeros(8, 8):
            closure_ok = False
    print(f"  {{nu_1..nu_7, hbar_8}} genuinely bracket-closed (Lie subalgebra)? {closure_ok}")
    assert closure_ok, "{nu_1..nu_7, hbar_8} is not bracket-closed"

    print("  => k=8 back-solve caveat FULLY CLOSED: nu_8 independently")
    print("  re-derived using ONLY nu_1..nu_7 + bracket-closure + trace-form")
    print("  projection -- ZERO reference to nu_8's own formula. Round 34's")
    print("  octonion route was NEVER needed for this (an overclaim in this")
    print("  round's original version, caught by both FL Step 8a skeptics).")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Round 30's (S2) -- 'g2 simple => 1-dim invariant-form space,'")
    print("  previously cited as a standard textbook Lie-theory fact -- is")
    print("  now DIRECTLY VERIFIED for Appendix A's own 14-generator matrix")
    print("  realization: the space of Ad(g2)-invariant symmetric bilinear")
    print("  forms is EXACTLY 1-dimensional (1362 linear equations, solved")
    print("  exactly), and the unique solution IS B_0 exactly -- closing")
    print("  this citation with a project-specific computational proof.")
    print()
    print("  ALSO CLOSED (STEP E, post-skeptic fix): the k=8 back-solve")
    print("  caveat -- nu_8 independently re-derived from nu_1..nu_7 alone")
    print("  via bracket-closure, matching Appendix A's own nu_8 EXACTLY.")
    print()
    print("  Round 30's ENTIRE remaining dependency chain for Ch_4's own")
    print("  c=1 (hence the whole degree-4 story since Round 29) is now")
    print("  either directly verified (S2, S6', and now k=8) or explicitly")
    print("  marked non-load-bearing (S7).")


if __name__ == "__main__":
    main()
