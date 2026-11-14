r"""
C183 -- one criterion for all four Butruille spaces.

Round70 computed, space by space, whether Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0})
carries an isotropy-trivial component, and got PASS/PASS/PASS/FAIL. It did not
ask WHY exactly one of the four fails. This script asks that.

THE CRITERION (stated before it was run; see claim.md's Mechanism Claim Gate):

    dim (V (x) W)^H = dim Hom_H(V^*, W)

so the H-trivial component is absent exactly when Lambda^2 shares no constituent
with its own dual. Duality on any compact group negates torus weights, which
gives a cheap PROXY at the level of the maximal torus T <= H:

    is there a pair of weights of Lambda^2(m^{1,0}) summing to zero?

THE PROXY IS STRICTLY STRONGER THAN THE H-LEVEL CONDITION, and this file says so
in code, not only in prose. H-invariants sit inside T-invariants, so

    T-count = 0  =>  H-count = 0        (a real proof of PASS)
    T-count > 0  =/=>  H-count > 0      (NOT a proof of FAIL)

An adversarial review of the first draft found that draft advertising an H-level
"exactly when" while computing only the T-level check, and supplied the
separating example (H = SU(3), Lambda^2 = 3 (+) 6: T-count > 0 while H-count =
0). That example is now run below, and the one space where the two levels could
diverge has its H-level multiplicity computed here rather than imported from
round70.

WHAT IS AN INPUT AND WHAT IS COMPUTED -- the pre-registered no-per-space-branch
condition depends on this line being honest:

  INPUT, per space   : the weight multiset of m^{1,0} (3 weights), transcribed
                       from Round65's and Round70's committed scripts.
  COMPUTED, uniformly: Lambda^2 (all pairwise sums), the top-wedge invariance
                       check, the negation, the intersection, the verdict.

`verdict()` takes a weight multiset and nothing else; it does not know which
space it is looking at, nor even the rank of the torus.

Run:  python c183_duality_criterion.py
"""

from itertools import combinations

# ---------------------------------------------------------------------------
# INPUTS: weight multisets of m^{1,0}, transcribed with their provenance.
# Nothing else about the four spaces enters this file.
# ---------------------------------------------------------------------------
SPACES = [
    {
        "name": "S^6 = G2/SU(3)",
        "isotropy": "SU(3)",
        # 3 = fundamental of su(3); weights of e1,e2,e3 under the same Cartan
        # basis round65 uses, H1 = i*diag(1,-1,0), H2 = i*diag(0,1,-1).
        "m10": [(1, 0), (-1, 1), (0, -1)],
        "provenance": "round70 PART 3: m10 = (1,0) dim3, i.e. the fundamental 3",
        "round70_verdict": "PASS",
    },
    {
        "name": "SU(3)/T^2",
        "isotropy": "T^2 = U(1)xU(1)",
        # round65_t2_weight_check.py STEP 2: weights of {E12,E23,E31}
        "m10": [(2, -1), (-1, 2), (-1, -1)],
        "provenance": "round65 STEP 2 (CH2016 eq.35 basis), W10 printed verbatim",
        "round70_verdict": "PASS",
    },
    {
        "name": "CP^3 = Sp(2)/(Sp(1)xU(1))",
        "isotropy": "Sp(1)xU(1)",
        # round70 chose m10_pieces = [V(1,1), V(0,-2)] (the mixed_sign split,
        # the only one of its two candidates whose Lambda^3 is isotropy-trivial).
        # Expanding each V(m,n) into (sp(1) weight, U(1) charge):
        # V(1,1) -> (1,1),(-1,1);  V(0,-2) -> (0,-2).
        "m10": [(1, 1), (-1, 1), (0, -2)],
        "provenance": "round70 PART 2: m10_pieces = [(1,1),(0,-2)], expanded to weights",
        "round70_verdict": "PASS",
    },
    {
        "name": "S^3xS^3 = SU(2)^3/SU(2)_diag",
        "isotropy": "SU(2)_diag",
        # round70 PART 1: m10 = [2], a single copy of V2 (spin 1, dim 3),
        # whose weights are 2, 0, -2. Rank-1 torus, written as 1-tuples.
        "m10": [(2,), (0,), (-2,)],
        "provenance": "round70 PART 1: m10 = [2] i.e. one copy of V2 (spin 1)",
        "round70_verdict": "FAIL",
    },
]


# ---------------------------------------------------------------------------
# THE UNIFORM DECISION PATH. Takes weights. Knows nothing else.
# ---------------------------------------------------------------------------
def wsum(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(w):
    return tuple(-x for x in w)


def wedge2(weights):
    """Weights of Lambda^2 of a torus-diagonalisable space: sums over pairs."""
    return [wsum(a, b) for a, b in combinations(weights, 2)]


def verdict(m10_weights):
    """PASS iff Lambda^2 shares no weight with its own negation.

    Returns (verdict, lambda2, zero_sum_pairs, top_wedge_is_invariant).
    No argument other than the weight multiset; no knowledge of the space.
    """
    lam2 = wedge2(m10_weights)
    zero_pairs = [(a, b) for a in lam2 for b in lam2 if all(x == 0 for x in wsum(a, b))]
    total = m10_weights[0]
    for w in m10_weights[1:]:
        total = wsum(total, w)
    return (
        "PASS" if not zero_pairs else "FAIL",
        lam2,
        zero_pairs,
        all(x == 0 for x in total),
    )


# ---------------------------------------------------------------------------
# MAIN COMPARISON
# ---------------------------------------------------------------------------
print("=" * 78)
print("C183  one criterion, four spaces -- compared against Round70's verdicts")
print("=" * 78)

agree = 0
rows = []
for sp in SPACES:
    v, lam2, zpairs, top_ok = verdict(sp["m10"])
    ok = v == sp["round70_verdict"]
    agree += ok
    rows.append((sp["name"], sp["isotropy"], v, sp["round70_verdict"], ok))
    print(f"\n{sp['name']}   (isotropy {sp['isotropy']})")
    print(f"   source            : {sp['provenance']}")
    print(f"   m^(1,0) weights   : {sp['m10']}")
    print(f"   sum = 0 (top wedge invariant) : {top_ok}")
    print(f"   Lambda^2 weights  : {lam2}")
    print(f"   negated Lambda^2  : {[neg(w) for w in lam2]}")
    print(f"   zero-sum pairs    : {len(zpairs)}")
    print(
        f"   criterion         : {v}     Round70 : {sp['round70_verdict']}     agree: {ok}"
    )
    assert top_ok, (
        f"{sp['name']}: top wedge not invariant -- input transcription is wrong"
    )

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print(f"{'space':<30}{'isotropy':<18}{'C183':<8}{'Round70':<10}{'agree'}")
for n, iso, v, r70, ok in rows:
    print(f"{n:<30}{iso:<18}{v:<8}{r70:<10}{ok}")
print(f"\nagreement: {agree} of 4")
print("floor (a criterion that always says PASS): 3 of 4")
print(
    f"efficiency = (observed - floor)/(ceiling - floor) = ({agree} - 3)/(4 - 3) = {agree - 3}"
)

# ---------------------------------------------------------------------------
# THE STRUCTURAL READING, checked rather than asserted:
# the criterion fails exactly where Lambda^2's weight multiset is invariant
# under negation as a SET.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("WHY exactly one space fails: is Lambda^2's weight set negation-invariant?")
print("=" * 78)
for sp in SPACES:
    _, lam2, _, _ = verdict(sp["m10"])
    inv = set(lam2) == {neg(w) for w in lam2}
    print(
        f"  {sp['name']:<30} negation-invariant: {inv}   (Round70: {sp['round70_verdict']})"
    )

# ---------------------------------------------------------------------------
# HOW STRONG IS THE TORUS PROXY? Demonstrated with the reviewer's own
# separating example rather than asserted.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("How strong is the torus proxy? -- an SU(3) example separating T from H")
print("=" * 78)
W_3 = [(1, 0), (-1, 1), (0, -1)]
W_6 = sorted({wsum(a, b) for a in W_3 for b in W_3})  # Sym^2(3) = 6
probe = W_3 + W_6
t_pairs = [(a, b) for a in probe for b in probe if all(x == 0 for x in wsum(a, b))]
print(f"  take Lambda^2 = 3 (+) 6, weights {probe}")
print(f"  T-level zero-sum pairs : {len(t_pairs)}   (the proxy alone would say FAIL)")
print("  H-level singlets       : 0   (3* = 3bar and 6* = 6bar, neither is in {3,6})")
assert len(t_pairs) > 0, "the example does not actually separate the two levels"
print("  => the torus proxy is STRICTLY STRONGER than the H-level condition:")
print("     T-count 0 proves PASS; T-count above 0 does NOT by itself prove FAIL.")

# ---------------------------------------------------------------------------
# COMPLETING THE ONE FAIL AT H-LEVEL, computed here rather than imported.
# Rank 1, so the multiplicity of the trivial representation in a weight
# multiset is m(0) - m(2): the standard highest-weight peel.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("The one FAIL, completed at H-level (SU(2), rank 1) -- computed, not cited")
print("=" * 78)
lam2_s3s3 = wedge2([(2,), (0,), (-2,)])
mult = {}
for a in lam2_s3s3:
    for b in lam2_s3s3:
        k = wsum(a, b)[0]
        mult[k] = mult.get(k, 0) + 1
mult_trivial = mult.get(0, 0) - mult.get(2, 0)
print(f"  Lambda^2 (x) Lambda^2 weight multiplicities: {dict(sorted(mult.items()))}")
print(
    f"  mult(V0) = m(0) - m(2) = {mult.get(0, 0)} - {mult.get(2, 0)} = {mult_trivial}"
)
assert mult_trivial == 1, "the H-level trivial multiplicity is not 1"
print("  => an H-trivial component genuinely exists on S^3xS^3 (multiplicity 1),")
print("     so the cheap argument really does fail there, not merely 'unproven'.")
print("     This reproduces round70's V2 (x) V2 = V0+V2+V4 from weights alone.")

# ---------------------------------------------------------------------------
# NEGATIVE CONTROL / injected-error catch, pre-registered in claim.md.
# The INPUT is corrupted; the decision path is untouched.
#
# Both controls also satisfy the top-wedge invariance the script demands of the
# four real inputs. The first draft's control (b) did not: it added a uniform
# U(1) charge, giving top-wedge sum (0,3) != (0,0), so it flipped an input that
# could not correspond to any almost-complex structure at all. An adversarial
# review caught that; it is replaced here, not merely noted.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("NEGATIVE CONTROL -- corrupt the input, the verdict must flip")
print("=" * 78)


def control(label, weights, was, must_become):
    v, lam2, zp, top_ok = verdict(weights)
    print(f"  {label} input {weights}")
    print(
        f"      top-wedge sum zero: {top_ok}   (demanded of the four real inputs too)"
    )
    print(f"      Lambda^2 = {lam2}, zero-sum pairs = {len(zp)}  ->  {v}   (was {was})")
    assert top_ok, (
        f"{label}: control input is not top-wedge invariant, not an admissible shape"
    )
    assert v == must_become, (
        f"{label}: did not flip -- the criterion is not reading its input"
    )


# (a) the S^6 shape, perturbed so Lambda^2 meets its own negation. PASS -> FAIL.
control("(a) S^6 shape, dual-closed:", [(1, -1), (-1, 1), (0, 0)], "PASS", "FAIL")

# (b) the rank-1 shape, perturbed off the negation-symmetric axis while keeping
#     the weights summing to zero. FAIL -> PASS. This multiset is NOT the weight
#     set of any SU(2) representation (those are negation-symmetric by
#     construction) -- it is a corruption designed to move the decision, and it
#     satisfies the one structural constraint the script actually enforces.
control("(b) rank-1 shape, off-axis:", [(3,), (-1,), (-2,)], "FAIL", "PASS")

print("\n  both controls flipped, and both are top-wedge invariant")

# ---------------------------------------------------------------------------
# IS THE S^3xS^3 FAILURE REPAIRABLE BY A DIFFERENT CHOICE OF J?
# The first draft asserted this with a check that fed ONE hard-coded multiset to
# verdict() and confirmed the singleton output -- it could not have failed.
# Replaced with a real enumeration: m_C = V2 (+) V2 has weights [2,0,-2,2,0,-2],
# and any SU(2)-submodule's weight multiset is invariant under negation. Search
# all 3-element sub-multisets with that property; check every one that turns up.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("Is S^3xS^3's failure an artefact of the particular J?")
print("=" * 78)
mc_weights = [(2,), (0,), (-2,), (2,), (0,), (-2,)]
candidates = []
for combo in combinations(range(6), 3):
    sub = [mc_weights[i] for i in combo]
    # dedup on the MULTISET, not the ordering -- otherwise the same single
    # candidate is reported five times, once per permutation, which reads as
    # five distinct admissible choices when there is only one.
    if sorted(sub) == sorted(neg(w) for w in sub) and sorted(sub) not in candidates:
        candidates.append(sorted(sub))
print(f"  negation-symmetric 3-element sub-multisets of m_C: {candidates}")
verdicts = {verdict(c)[0] for c in candidates}
print(f"  verdicts over all of them: {verdicts}")
assert candidates, "the enumeration found nothing -- it is not searching"
assert verdicts == {"FAIL"}, "some admissible choice escapes -- claim.md overstates"
print("  -> every admissible choice fails. Forced by the isotropy group SU(2)_diag,")
print("     not by the particular J.")

# ---------------------------------------------------------------------------
# THE MIRROR QUESTION ON CP^3, where round70 DID have to choose between two
# splits: does its PASS survive the other admissible one? (Raised by the same
# review. Round70 rejected `same_sign` because its Lambda^3 was not invariant,
# but the conjugate split V(1,-1)+V(0,2) is equally admissible.)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("Does CP^3's PASS survive the other admissible split?")
print("=" * 78)
for label, w in [
    ("round70 choice V(1,1)+V(0,-2)", [(1, 1), (-1, 1), (0, -2)]),
    ("conjugate      V(1,-1)+V(0,2)", [(1, -1), (-1, -1), (0, 2)]),
]:
    v, lam2, zp, top_ok = verdict(w)
    print(f"  {label}   top-wedge zero: {top_ok}   Lambda^2 = {lam2}   -> {v}")
    assert top_ok and v == "PASS", (
        "CP^3's PASS is split-dependent -- report that instead"
    )
print(
    "  -> both admissible splits PASS; CP^3's verdict is not an artefact of the choice."
)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if agree == 4:
    print("  4 of 4, no per-space branch, both injected-error controls flip.")
    print(
        "  The Term2-vanishing step of Round59/65 holds exactly when Lambda^2(m^(1,0))"
    )
    print("  shares no constituent with its own dual. Among the four Butruille spaces")
    print(
        "  that fails only for S^3xS^3, whose isotropy SU(2)_diag is the one group of"
    )
    print("  the four with no representation NOT isomorphic to its own dual.")
    print()
    print("  Standing of each verdict, stated so it is not read past:")
    print("    the three PASSes are proofs (T-count 0 forces H-count 0);")
    print("    the FAIL is a proof too, but only because its H-level multiplicity")
    print("    was computed above (mult(V0)=1) -- the torus proxy alone would not")
    print("    have established it, as the 3 (+) 6 example demonstrates.")
else:
    print(f"  {agree} of 4 -- see claim.md's kill-criterion table.")
