"""
Round 30 (2026-07-11): STRUCTURAL derivation of Round 29's bonus finding
`Ch_tilde == Casimir_su3` (both equal `Id+X/3`), rather than treating it
as a verified numerical coincidence in this project's specific
normalization (Round 29's C5, explicitly flagged for follow-up).

Claim: `C~h == Casimir_su(3)` is a NECESSARY CONSEQUENCE of Agricola's OWN
definition of `C~h` (page 10, before Prop 3.3's coordinate simplification)
as the Casimir element of h=su(3), acting on spinors via Lemma 3.4's
algebraic representation, PROVIDED the specific su(3)-generator basis
{nu_1..nu_8} this project uses (AHL2023 Remark 5.2) is orthonormal with
respect to Agricola's invariant form Q_h -- NOT a numerical accident
specific to THIS S^6 geometry's numbers.

POST-SKEPTIC CORRECTION #1 (2026-07-11, FL Step 8a, two independent
context-blind skeptics + a tool-verified synthesis pass): the ORIGINAL
version of this argument used "uniqueness of the 8-dim irreducible
Clifford module" (S7 below) as the LOAD-BEARING step connecting Appendix
A's `nu(k)` to `su3_action(k,.)`. BOTH skeptics independently found this
is too weak: Clifford-module uniqueness only gives an ABSTRACT
isomorphism, not the SPECIFIC operator identity actually needed. Both
proposed the SAME fix: directly compute Parthasarathy's `ead(nu_k)` from
`SU3_GENERATORS` plus `e_action` and check it against `su3_action(k,.)`.
The synthesis agent implemented this (STEP C below): EXACT match for all
k=1..8.

POST-SKEPTIC CORRECTION #2 (2026-07-11, `/boyko-triangle-audit`, run
AFTER both skeptics + synthesis had already approved correction #1): the
triangle-audit found that STEP C's "exact match" is ALGEBRAICALLY FORCED
regardless of what numbers sit in `SU3_GENERATORS` -- verified directly
(see round30_claim.md "Skeptic Verdict" for the confirming computation
with a FAKE, arbitrary bivector table, which STILL produces an exact
match). `ead_parthasarathy(k,.)` and `su3_action(k,.)` are built from the
SAME `(sign,a,b)` list via two bookkeeping schemes (ordered-pair sum vs
antisymmetric-matrix sum) that Clifford anticommutation (Z_aZ_b=-Z_bZ_a)
forces to coincide for ANY input data -- so STEP C tests only that
`su3_action`'s coefficient convention (1/2, 1/(2sqrt3)) is a correctly-
normalized instance of the GENERAL Parthasarathy formula, NOT that
`SU3_GENERATORS`'s specific entries represent the SAME abstract `nu_k`
Appendix A's `nu(k)` represents. Neither skeptic caught this (a shared
blind spot -- both were same-model-family adversarial reviews; this is
exactly the kind of gap this project's own CLAUDE.md flags cross-model
review for). THE ACTUAL CONNECTING FACT, identified by the audit and
independently re-verified below (STEP C', re-running Round 13's own
calibration check inside this round's own script rather than merely
citing it from memory): Appendix A's `nu(i)` commutator action on its
own `e(p)` matches `SU3_GENERATORS`/`AD_NU_M_BIVECTOR`'s `ad(nu_i)|_m`
data EXACTLY (up to the already-documented sign convention), for all
48 (i,p) pairs -- THIS is what establishes Appendix A's `{nu_1..nu_8}`
(proven Qh-orthonormal, STEPs A/B) and `su3_action`'s generators are the
SAME abstract Lie algebra elements, not STEP C's normalization check.
STEP C is RETAINED (it is a true, non-vacuous fact about `su3_action`'s
internal consistency) but RELABELED from "primary proof mechanism" to
"internal consistency check" -- STEP C' is now the actual connecting
step.

Logical chain (each step below is either a STANDARD, textbook Lie-theory
fact -- cited, not re-derived -- or a computationally VERIFIED claim
specific to this project's own constructions):

  (S1) [Agricola 2002, page 10, cited -- standard] `C~h := -sum_i
       ead(X_i) o ead(Y_i)` for ANY Qh-DUAL bases {X_i},{Y_i} of h
       (Qh(X_i,Y_j)=delta_ij). If {X_i}={Y_i} is Qh-ORTHONORMAL (self-
       dual), this reduces to `C~h = -sum_i ead(X_i)^2`.

  (S2) [standard Lie theory, cited] g2 is SIMPLE => the space of
       Ad(G2)-invariant symmetric bilinear forms on g2 is exactly
       1-dimensional (Schur's lemma on the adjoint representation).
       Hence Agricola's Q (required Ad(G)-invariant, restricting to the
       metric <,> on m) is a SCALAR MULTIPLE of ANY OTHER Ad(G2)-invariant
       form -- in particular of B_0(X,Y):=Tr(rho(X)^T rho(Y)) for ANY
       faithful representation rho of g2 (trace forms are automatically
       Ad-invariant for any Lie algebra representation -- standard fact).

  (S3) [computationally VERIFIED below, STEP A/B] Using Appendix A's
       g2 <-> so(7) construction (rho/octonion generators,
       g2su3_appendix_a_construction.py, built in Round 13 via a
       DIFFERENT concrete matrix realization than su3_action/nabla_g --
       see caveat below on what "independent" does and does not mean
       here), the basis {nu_1,...,nu_14} (all of g2 = h[[8]] (+) m[[6]])
       is FULLY B_0-orthonormal: Tr(nu_k^T nu_l) = delta_kl for ALL
       14x14=196 pairs (not just the diagonal, which is all that was
       previously documented in this file's own docstring).

  (S4) Since {nu_9,...,nu_14} (= e_1,...,e_6 up to E_SIGN, Appendix A's
       own m-directions) are ALSO B_0-orthonormal with B_0(e_p,e_p)=1 --
       EXACTLY matching this project's metric convention <Z_p,Z_p>=1
       (baked into the Clifford relation Z_i^2=-1 used throughout) -- the
       scalar in (S2) is FIXED: Q = 1*B_0 exactly (not just proportional)
       on ALL of g2, hence Q_h = B_0|_h exactly.

  (S5) Combining (S3)+(S4): {nu_1,...,nu_8} IS Q_h-orthonormal -- a fact
       about the ABSTRACT Lie algebra elements nu_k in h subset g2,
       independent of which representation is used to compute it.

  (S6, INTERNAL CONSISTENCY CHECK, NOT the connecting step -- see
       correction #2 above) [computationally VERIFIED below, STEP C]
       `ead(nu_k)`, Parthasarathy's spin-lift formula `(1/4) sum_{j,l}
       M_jl Z_j Z_l` applied to the antisymmetrized matrix `M` built from
       `SU3_GENERATORS[k]`'s own `(sign,a,b)` list, equals
       `su3_action(k,.)` EXACTLY, for all k=1..8. VERIFIED (round30_claim
       .md) that this match is ALGEBRAICALLY FORCED for ANY `(sign,a,b)`
       table via Clifford anticommutation -- it confirms `su3_action`'s
       coefficient convention (1/2, 1/(2sqrt3)) is a correctly-normalized
       instance of the GENERAL Parthasarathy recipe, but does NOT test
       whether `SU3_GENERATORS`'s specific entries represent the SAME
       abstract `nu_k` Appendix A's `nu(k)` represents.

  (S6', THE ACTUAL CONNECTING STEP) [computationally RE-VERIFIED below,
       STEP C' -- re-running Round 13's own calibration inside this
       round's own script, not merely citing it] Appendix A's `nu(i)`
       commutator action on its own `e(p)` (`[nu(i),e(p)]`, decomposed in
       the `{e(1)..e(6)}` basis) matches `SU3_GENERATORS`/
       `AD_NU_M_BIVECTOR`'s `ad(nu_i)|_m` data EXACTLY, up to the already-
       documented sign convention, for ALL 8x6=48 (i,p) pairs. THIS is
       what establishes Appendix A's `{nu_1,...,nu_8}` (proven
       Q_h-orthonormal, S5) and `su3_action`'s generators are the SAME
       abstract Lie algebra elements of h subset g2 -- not S6.

  (S7, CORROBORATION) [standard fact: uniqueness of the irreducible
       Clifford module] dim(m)=6 (even) => C(m) tensor C has a UNIQUE
       irreducible complex representation of dimension 2^3=8, up to
       isomorphism. Consistent with S6' (both realize the same C(m)-
       module), additional structural context, not independently load-
       bearing.

  (S8, CORROBORATION) [computationally VERIFIED below, STEP D] `-sum_k
       nu(k)^2` (Appendix A, k=1..8, its OWN independently-built
       realization) and `Casimir_su3 := -sum_k su3_action(k,.)^2` have
       the IDENTICAL eigenvalue spectrum {0,0,4/3 x6} (same multiset,
       differing only by which basis index carries which eigenvalue).
       NOTE (post-skeptic): this spectrum match is EXPECTED from G2->
       SU(3) branching theory (Sigma decomposes as 1+3+3bar+1 on both
       sides regardless of realization details) and Casimir eigenvalues
       cannot distinguish 3 from 3bar -- so this is real, independent
       corroboration from a SECOND concrete construction, not proof of
       operator isomorphism by itself. The eigenvalue 4/3 matches the
       STANDARD, LITERATURE quadratic Casimir of SU(3)'s fundamental rep
       (external cross-check, independent of this project's conventions).

  (S9) CONCLUSION: by (S1)+(S5), `C~h = -sum_k ead(nu_k)^2` for
       Appendix A's Q_h-orthonormal `{nu_1..nu_8}`. By (S6', the
       calibration identity -- NOT S6's algebraically-automatic check),
       these `nu_k` are the SAME abstract elements `SU3_GENERATORS`
       encodes, hence `ead(nu_k) = su3_action(k,.)` for the RIGHT reason.
       Hence `C~h = -sum_k su3_action(k,.)^2 = Casimir_su3` -- a
       STRUCTURAL consequence of Agricola's own Casimir definition
       applied to a verified Qh-orthonormal basis of the SAME abstract
       Lie algebra elements `su3_action` uses, NOT a numerical
       coincidence specific to this S^6 geometry's numbers (though
       tethered to this project's specific realization of Sigma and its
       specific choice of su(3)-generator basis -- see Honest Scope
       below).

HONEST SCOPE: (S2) and (S7) are STANDARD, textbook Lie-theory/Clifford-
algebra facts, cited here rather than independently re-derived from first
principles. Caveats surfaced by skeptic review and the triangle-audit
pass, not previously stated: (a) `AD_NU_M_BIVECTOR` (Appendix A) and
`SU3_GENERATORS` (su3_action) are a BYTE-IDENTICAL copy of the SAME
AHL2023 Remark 5.2 literature table -- S3's "independent construction"
means independent CONCRETE MATRIX REALIZATION (rho/octonion products vs
direct bivector lift), NOT an independent literature/data source; S6'
(the calibration check) is therefore verifying that TWO DIFFERENT
CONSTRUCTIONS built FROM this shared table agree with each other, not
that the table itself is correct against some third, independent source
-- a genuine, non-trivial cross-construction check, but not a check
against external ground truth; (b) Appendix A's `nu_8` (unlike
`nu_1..nu_7`, verbatim page transcriptions) was BACK-SOLVED from
EXACTLY the calibration equation S6' now checks (`[nu_i,e_p]=-ad(nu_i)
(e_p)`, that file's own inline comment) -- for k=8 SPECIFICALLY, S6' is
closer to "consistent by construction" than an independent confirmation
(k=1..7's calibration IS independent: those `nu_i` were transcribed
directly from the source paper, not fitted to this equation); (c)
Appendix A's own internal bracket convention requires a global
`BRACKET_SIGN=-1` flip in ITS OWN [e_p,e_q] bracket construction (used
elsewhere, e.g. `build_curvature_h_table`) -- confirmed NOT to affect
S6' at all, which compares `[nu_i,e_p]` (an h-m commutator, unaffected
by that separate m-m bracket convention) directly against
`ad_nu_m_trusted`. What IS newly, computationally verified this round:
the FULL 14x14 B_0-orthonormality of Appendix A's {nu_k} (S3), the exact
m-normalization match fixing lambda=1 (S4), RE-VERIFICATION of Round 13's
own h-generator calibration as this round's actual connecting step (S6',
not S6), and the matching eigenvalue spectrum as corroboration (S8).
"""

import sympy as sp

from g2su3_appendix_a_construction import nu
from g2su3_explicit_clifford import DIM
from g2su3_twisted_kernel import SU3_GENERATORS, su3_action
from g2su3_explicit_clifford import e_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def ead_parthasarathy(k, vec):
    """Parthasarathy's spin-lift ead(nu_k), computed DIRECTLY from
    SU3_GENERATORS (the ad(nu_k)|_m data, AHL2023 Remark 5.2) via
    e_action -- ZERO reference to Appendix A's nu(k)/rho construction
    anywhere. ead(X) = (1/4) sum_{j,l} (ad(X)|_m)_{jl} Z_j Z_l, matching
    Agricola's page-10 formula (Parthasarathy's Lemma / Lemma 3.1)
    literally: (ad(nu_k)|_m)_{jl} is antisymmetric, read off directly
    from SU3_GENERATORS[k]'s (sign,a,b) bivector-term list."""
    coeff = sp.Rational(1, 2) if k != 8 else sp.Rational(1, 2) / sqrt(3)
    M = sp.zeros(6, 6)
    for sign, a, b in SU3_GENERATORS[k]:
        M[a - 1, b - 1] += sign * coeff
        M[b - 1, a - 1] -= sign * coeff
    out = sp.zeros(DIM, 1)
    for j in range(1, 7):
        for ll in range(1, 7):
            if M[j - 1, ll - 1] == 0:
                continue
            out += sp.Rational(1, 4) * M[j - 1, ll - 1] * e_action(j, e_action(ll, vec))
    return out


def main():
    print("=" * 70)
    print("STEP A: full B_0-orthonormality of {nu_1,...,nu_8} (h=su(3))")
    print("(all 64 pairs, not just the diagonal previously documented)")
    print("=" * 70)
    all_ortho_h = True
    for k in range(1, 9):
        row = []
        for ll in range(1, 9):
            val = sp.simplify(sp.trace(nu(k).conjugate().T * nu(ll)))
            row.append(val)
            expected = 1 if k == ll else 0
            if val != expected:
                all_ortho_h = False
        print(f"  k={k}: {row}")
    print(f"\n  Full 8x8 B_0-orthonormality of {{nu_1..nu_8}}? {all_ortho_h}")
    assert all_ortho_h, "STEP A: {nu_1..nu_8} is NOT fully B_0-orthonormal -- (S3) premise fails"

    print("\n" + "=" * 70)
    print("STEP B: full B_0-orthonormality of ALL of g2, {nu_1,...,nu_14}")
    print("(confirms B_0|_m matches the metric normalization <Zp,Zp>=1")
    print("EXACTLY, pinning lambda=1 in Q=lambda*B_0 -- (S4))")
    print("=" * 70)
    all_ortho_g2 = True
    for k in range(1, 15):
        for ll in range(1, 15):
            val = sp.simplify(sp.trace(nu(k).conjugate().T * nu(ll)))
            expected = 1 if k == ll else 0
            if val != expected:
                all_ortho_g2 = False
                print(f"  FAIL k={k},l={ll}: {val} (expected {expected})")
    print(f"  Full 14x14 B_0-orthonormality of all of g2? {all_ortho_g2}")
    assert all_ortho_g2, "STEP B: full g2 basis is NOT B_0-orthonormal -- (S4) premise fails"

    print("\n" + "=" * 70)
    print("STEP C (INTERNAL CONSISTENCY CHECK -- NOT the connecting step,")
    print("see STEP C' below and correction #2 in the module docstring):")
    print("ead(nu_k) [Parthasarathy, from SU3_GENERATORS + e_action] equals")
    print("su3_action(k,.) EXACTLY. VERIFIED (round30_claim.md) that this")
    print("match is ALGEBRAICALLY FORCED for ANY (sign,a,b) table -- it")
    print("confirms su3_action's normalization convention, not that")
    print("SU3_GENERATORS represents the same abstract nu_k Appendix A does.")
    print("=" * 70)
    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    all_match_exact = True
    for k in range(1, 9):
        cols = [ead_parthasarathy(k, unit_vec(i)) for i in range(DIM)]
        Ek = sp.Matrix.hstack(*cols)
        exact = sp.simplify(Ek - Ls[k]) == sp.zeros(DIM, DIM)
        negated = sp.simplify(Ek + Ls[k]) == sp.zeros(DIM, DIM)
        print(
            f"  k={k}: ead_Parthasarathy(k,.) == su3_action(k,.) exactly? {exact}   ==-su3_action? {negated}"
        )
        if not exact:
            all_match_exact = False
    print(f"\n  ALL k: ead(nu_k) == su3_action(k,.) EXACTLY (no sign ambiguity)? {all_match_exact}")
    assert all_match_exact, (
        "STEP C: su3_action does NOT literally implement Parthasarathy's ead(nu_k) -- (S6) fails"
    )

    print("\n" + "=" * 70)
    print("STEP C' (THE ACTUAL CONNECTING STEP, added after /boyko-triangle-")
    print("audit found STEP C is algebraically forced regardless of input")
    print("data): RE-VERIFY Round 13's own calibration -- does Appendix A's")
    print("nu(i) commutator action on its own e(p) match SU3_GENERATORS'/")
    print("AD_NU_M_BIVECTOR's ad(nu_i)|_m data, for all 48 (i,p) pairs?")
    print("=" * 70)
    from g2su3_appendix_a_construction import ad_nu_m_trusted, e

    all_calibration_match = True
    for i in range(1, 9):
        for p in range(1, 7):
            comm = sp.simplify(nu(i) * e(p) - e(p) * nu(i))
            coeffs6 = sp.zeros(6, 1)
            for q in range(1, 7):
                num = sp.trace(e(q).conjugate().T * comm)
                den = sp.trace(e(q).conjugate().T * e(q))
                coeffs6[q - 1] = sp.simplify(num / den)
            expected = ad_nu_m_trusted(i, p)
            match_pos = sp.simplify(coeffs6 - expected) == sp.zeros(6, 1)
            match_neg = sp.simplify(coeffs6 + expected) == sp.zeros(6, 1)
            if not (match_pos or match_neg):
                all_calibration_match = False
                print(f"  MISMATCH i={i},p={p}: got={coeffs6.T}, expected={expected.T}")
    print(
        f"  All 48 (i,p) pairs match (up to the documented sign convention)? {all_calibration_match}"
    )
    assert all_calibration_match, (
        "STEP C': Appendix A's nu(k) does NOT represent the same abstract "
        "generators as SU3_GENERATORS -- (S6') fails, the argument's actual "
        "connecting fact does not hold"
    )
    print("  (Note: for k=8, this re-verifies rather than independently")
    print("  confirms, since Appendix A's own nu_8 was BACK-SOLVED from")
    print("  exactly this equation -- see Honest Scope. k=1..7 ARE genuinely")
    print("  independent, verbatim-transcribed checks.)")

    print("\n" + "=" * 70)
    print("STEP D (CORROBORATION, not proof mechanism): eigenvalue-spectrum")
    print("cross-check against Appendix A's own, independently-built g2")
    print("realization -- consistent with S6', not a substitute for it")
    print("(spectrum match is expected from G2->SU(3) branching and cannot")
    print("by itself distinguish 3 from 3bar -- see (S8) caveat)")
    print("=" * 70)
    minus_sum_nu2 = sp.simplify(sum((-(nu(k) * nu(k)) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    mult_su3action = {ev: m for ev, m in Casimir_su3.eigenvals().items()}
    mult_appendixA = {ev: m for ev, m in minus_sum_nu2.eigenvals().items()}
    print(f"  Casimir_su3 (su3_action) eigenvalues+multiplicities: {mult_su3action}")
    print(f"  -sum nu(k)^2 (Appendix A) eigenvalues+multiplicities: {mult_appendixA}")
    spectra_match = mult_su3action == mult_appendixA
    print(f"  IDENTICAL eigenvalue spectrum (same multiset)? {spectra_match}")
    assert spectra_match, "STEP D: the two independent constructions give DIFFERENT Casimir spectra"

    fund_eigenvalue = sp.Rational(4, 3)
    assert fund_eigenvalue in mult_su3action, "fundamental-piece eigenvalue is not 4/3 as expected"
    print(f"  Fundamental-representation eigenvalue = {fund_eigenvalue}")
    print("  (matches the STANDARD, literature quadratic-Casimir value for")
    print("  SU(3)'s fundamental rep in the common Dynkin-index-1 normalization")
    print("  -- external cross-check, independent of this project's own conventions)")

    print("\n" + "=" * 70)
    print("STEP E: final sanity cross-check against Round 29's already-")
    print("established numeric fact (Ch_tilde == Casimir_su3), predicted")
    print("by the structural argument (S1)-(S9), via S6' -- above")
    print("=" * 70)
    from g2su3_appendix_a_construction import build_curvature_h_table
    from g2su3_round26_jach_derivation import build_quartic_matrix, jac_h

    curv_h = build_curvature_h_table()
    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    Ch_0 = sp.Rational(1, 8) * Qh_sum

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * sp.eye(DIM) + Ch_4)

    ch_eq_cas = sp.simplify(Ch_tilde - Casimir_su3) == sp.zeros(DIM, DIM)
    print(f"  Ch_tilde == Casimir_su3 (Round 29's numeric finding)? {ch_eq_cas}")
    assert ch_eq_cas, "the structural argument's prediction disagrees with Round 29's numeric fact"

    print("\n" + "=" * 70)
    print("CONCLUSION (twice-corrected post-skeptic + post-triangle-audit)")
    print("=" * 70)
    print("  C~h == Casimir_su(3) is a STRUCTURAL consequence of Agricola's")
    print("  own Casimir-operator definition (page 10) applied to Appendix")
    print("  A's Q_h-orthonormal {nu_1..nu_8} (STEPs A/B, via g2's")
    print("  simplicity + exact m-normalization matching). THE CONNECTING")
    print("  STEP is S6' (STEP C'): re-verified that Appendix A's nu(k) and")
    print("  SU3_GENERATORS represent the SAME abstract elements (Round 13's")
    print("  own calibration, re-checked here). STEP C (ead_Parthasarathy vs")
    print("  su3_action) is RETAINED as a true internal-consistency check on")
    print("  su3_action's own normalization, but is NOT the connecting step")
    print("  -- it was found (by /boyko-triangle-audit, AFTER both skeptics")
    print("  approved it as the fix) to be algebraically forced for ANY")
    print("  input table, hence unable to test whether SU3_GENERATORS'")
    print("  specific data matches Appendix A's nu(k). Appendix A's own")
    print("  eigenvalue spectrum (STEP D) remains CORROBORATION only.")
    print()
    print("  Two rounds of post-hoc correction on this SAME claim (FL Step")
    print("  8a skeptics, then an independent triangle-audit) both found")
    print("  real gaps and both gaps are now closed with tool-verified")
    print("  evidence -- see round30_claim.md's Skeptic Verdict for the")
    print("  full history.")
    print()
    print("  HONEST LIMIT: (S2) g2-simplicity and (S7) uniqueness of the")
    print("  2^3-dim irreducible Clifford module are STANDARD, textbook")
    print("  facts cited here, not independently re-derived from scratch.")
    print("  For k=8 specifically, S6' re-verifies rather than independently")
    print("  confirms (Appendix A's own nu_8 was back-solved from this same")
    print("  equation) -- k=1..7's calibration IS genuinely independent.")


if __name__ == "__main__":
    main()
    print("\nEXIT=0")
