---
experiment_id: 20260708-dolan-casimir-g2su3
date: 2026-07-08
status: IN_PROGRESS (unparked same session — concrete 5-step plan below)
---

## Third resource found: Charbonneau-Harland 2016 ("Deformations of nearly Kahler instantons")

Directly relevant precedent: this paper explicitly computes kernels of twisted
Dirac operators on the same 4 homogeneous nearly-Kahler 6-manifolds (incl.
S^6=G2/SU(3)), for the deformation-theory operator (different specific bundle
than our S+⊗S- -> S-⊗S-, but same methodological family: explicit kernel
computation on this exact coset). Important calibration signal from their own
abstract: "a proof of the rigidity of the canonical connection on S^6 was
previously claimed in [63, Thm 3.5]. The proof given in that paper was
unfortunately incorrect" -- i.e. a PUBLISHED theorem on this exact kind of
computation was wrong once already. This validates today's caution (2 skeptic
rounds before trusting any claim here) rather than being a discouraging sign.

## Concrete 5-step verification plan (not abstract -- executing now)

1. **Assemble explicit data**: express the two origin-pieces of the trivial
   SU(3)-multiplicity space (v_a from the singlet inside (0,1)⊗(1,0), v_b from
   (0,0)⊗(0,0)) as explicit elements in AHL2023's Section 5.1 basis/notation
   (Sigma ≅ Lambda^bullet(m) via their Lagrangian-subspace spin representation,
   Section 2.1).
2. **Apply the true Levi-Civita Dirac operator**: D = sum_i e_i . nabla^g_{e_i},
   using AHL2023's explicit Nomizu map Lambda^g(e_i) (Remark 5.2) -- NOT the
   simplified t=1/3 cubic-Dirac shortcut.
3. **Compute the number**: <v_b, D v_a> = 0 or != 0?
4. **Calibration check BEFORE trusting step 3**: reproduce AHL2023 Theorem 5.1's
   known result (Killing spinors psi_+- = 1 +- y1^y2^y3, eigenvalue
   +-1/(2 sqrt 3)) on the SAME machinery first. If this sanity check fails,
   there is an implementation error to fix before trusting the harder twisted
   computation.
5. **Independent verification**: skeptic review (context-asymmetric, same
   protocol as today's 2 rounds), and if feasible a second independent method
   (Dolan-Casimir, already flagged in preprint.tex as untried for G2/SU(3)) on
   the same number.

**Decision criteria:** cross-term != 0 -> rank=1 confirmed (restore Corollary
to proved, new citable explicit result). cross-term = 0 -> rank=0, dim ker=2,
requires reworking Sec 2.2 / Lemma L5 / Yukawa Degeneracy sections.

**Unparked 2026-07-08 (same session, continued) -- beginning step 1 now.**

## PRELIMINARY RESULT 2026-07-08 (steps 1-4 executed, step 5 skeptic pending)

Implemented explicit Clifford module Sigma (8-dim) + real Levi-Civita
connection using AHL2023 Section 2.1 + Section 5.1 data (see
g2su3_explicit_clifford.py, g2su3_twisted_kernel.py, g2su3_find_invariant.py,
g2su3_compute_crossterm.py in this directory).

**Step 4 calibration: PASSED exactly** -- reproduced AHL2023 Theorem 5.1's
Killing spinor eigenvalue 1/(2 sqrt3) for all 6 basis directions, symbolic
exact match (sympy, not floating point).

**v_a found explicitly** (unique 1-dim common kernel of all 8 su(3)
generators' Leibniz action on the 9-dim tensor space, verified by direct
linear algebra, not guessed): v_a = y1(x)y23 - y2(x)y13 + y3(x)y12.
v_b = y123(x)1 (singlet x singlet, immediate).
Dimension check: dim(S+ x S-) = 4x4 = 16, matches kp_zero_mode.py branching.

**Step 3 (the actual cross-term): computed.**
D(v_a) = -sqrt(3) * w, D(v_b) = -sqrt(3) * w, where w=1(x)1 is the unique
SU(3)-invariant of S-(x)S-. BOTH exactly proportional to w with ZERO leftover
components in any other slot -- and the two coefficients are EXACTLY equal.

**Implied conclusion (PENDING SKEPTIC VERIFICATION, step 5, in progress):**
rank(D+|_trivial) = 1 (not 0) -- this would CONFIRM the preprint's original
dim ker(D+_{S^-})=1 claim via a genuine independent explicit computation, and
give the explicit kernel vector psi_0 = v_a - v_b.

**DO NOT yet update preprint.tex from this.** Skeptic review requested
(context-asymmetric, mode=artifact) specifically probing: (a) whether the
calibration check actually stress-tests the harder computation's code paths,
(b) whether "suspiciously exact, zero leftover" is a red flag for a
coincidental bug rather than a green flag, (c) whether the Leibniz-rule
tensor-product Dirac formula used is the mathematically correct definition
matching the index-theorem context, (d) given Charbonneau-Harland 2016's own
warning that a similar computation on this exact space was once published
wrong, what specific failure mode to check for.

## Skeptic verdict (round 3): WEAKENED, with 2 concrete cheap tests requested

Skeptic did NOT confirm outright. Key points:
- Rep-theory forces D(v_a), D(v_b) to be pure multiples of w regardless of
  whether the coefficients are numerically right -- "zero leftover" is a
  weak green flag, not proof.
- c_b=-sqrt(3) independently matches the known Killing-spinor eigenvalue
  formula (D psi = -n*lambda*psi = -6/(2sqrt3) = -sqrt(3) for n=6,
  lambda=1/(2sqrt3)) -- this is a real, if implicit, second confirmation of
  c_b specifically.
- c_a is the load-bearing, NOT independently forced by anything already
  checked. Calibration only exercises bivector-lift + a chirality-symmetric
  target (psi_+-); never exercises the tensor-product Leibniz rule or
  iterated (6-fold) Clifford products -- both of which the real computation
  needs.
- Requested test 1: compute D on each UNSYMMETRIZED term of v_a individually
  (y1(x)y23, -y2(x)y13, y3(x)y12) and check each gives exactly -sqrt(3)/3 *
  w, not a mismatched-magnitude cancellation.
- Requested test 2: chirality operator gamma_7=e1.e2.e3.e4.e5.e6 on "1" and
  "y123" must give +-i with opposite sign (tests 6-fold iterated Clifford
  product, unexercised by calibration).

## Round 3 checks executed (g2su3_skeptic_checks.py) -- BOTH PASSED

Test 1: each of the 3 individual terms gave EXACTLY -sqrt(3)/3 (with correct
signs, sum = -sqrt(3) exactly, no mismatched-magnitude cancellation). Found
an additional representation-theoretic explanation for why "zero leftover"
holds per-term (not just for the sum): the domain piece (0,1)(x)(1,0) =
(1,1)+(0,0) has NO (1,1)=8 counterpart in the codomain branching
(2,0)+(0,1)+2x(1,0)+(0,0) -- so by Schur's lemma the "8-part" of ANY vector
in this domain slice, including each unsymmetrized single term, is FORCED
to map to zero under any SU(3)-equivariant operator, leaving only the
v_a-component contribution. This explains the clean pattern as structural,
not coincidental -- but note it validates the SU(3)-equivariance bookkeeping,
not independently the numeric value -sqrt(3)/3 itself.

Test 2: gamma_7 . 1 = -i * 1, gamma_7 . y123 = +i * y123 -- exactly opposite
signs as required. This DOES exercise a genuinely different code path
(6-fold iterated Clifford product) than anything in calibration or the main
computation, and passed cleanly.

## Residual risk assessment

Even in the skeptic's specific worried failure mode (a sign error specific
to the Levi-Civita connection's action on the S- factor, which could flip
c_a's sign), the QUALITATIVE conclusion (rank=1, i.e. BOTH c_a and c_b
nonzero, vs rank=0 requiring BOTH to vanish) is unaffected -- c_b is
independently anchored to the calibrated Killing-spinor formula, and c_a's
magnitude (if not sign) is now checked via 2 additional independent code
paths. The only remaining ambiguity a sign error could produce is WHICH
combination of v_a, v_b is the exact kernel vector (v_a-v_b vs v_a+v_b),
not whether dim ker(D+_{S^-}) is 1 or 2.

**Status: promotable to "confirmed via explicit calibrated computation,
pending external peer review" -- NOT yet "fully externally verified".**
Decision on whether to update preprint.tex now vs. wait: handed to user
(2026-07-08), given the document is already public (Zenodo DOI
10.5281/zenodo.21263563) and already sent to Ali Chamseddine for
endorsement review.

# decision.md

## Convergent finding (2 independent skeptic rounds, mode=artifact, context-asymmetric)

**Round 1 (on preprint.tex's original argument):** CONFIRMED, HIGH confidence.
"index=1 ⟹ rank 1" at kp_zero_mode.py:426 is a non-sequitur — index of any
linear map C^2→C^1 is automatically dim(domain)-dim(codomain)=1 regardless of
rank (0 or 1). Both scenarios are equally compatible with everything the
preprint actually establishes.

**Round 2 (on the escalated hypothesis that D^2 might be identically zero,
forcing rank=0):** WEAKENED. The "sum of eigenvalue-0 eigenvectors is
eigenvalue-0" linear algebra step is valid, but G-equivariance + Schur's
lemma only forces D^2 to act as Id_{V_rho}⊗M for SOME operator M on the
2-dim multiplicity space — it does NOT force M to be diagonal in the
V_a/V_b split (V_a = singlet in (0,1)⊗(1,0), V_b = singlet in (0,0)⊗(0,0)).
Diagonality of the naive per-summand Casimir formula lambda^2=C2(G)-C2(H)
is a THEOREM for symmetric spaces and for Kostant's cubic Dirac operator on
reductive G/H — but S^6=G2/SU(3) is naturally reductive, NOT symmetric, and
the physically relevant operator is the Levi-Civita Dirac D^g, which differs
from the cubic/characteristic-connection Dirac D^c by a TORSION term
(Clifford multiplication by the G2-invariant associative 3-form). This
torsion term could produce a non-zero off-diagonal coupling M_{ab} between
V_a and V_b that the naive Casimir-difference argument does not see either
way (it neither proves nor disproves the coupling).

## Kill Analysis (per Anti-Overfitting Gate / OSA)

**What was killed:** The claim that "L4B is proved" via the argument given in
kp_zero_mode.py / preprint.tex §4.2 as currently written. Neither rank=0 nor
rank=1 is established by the stated argument (global index + KP gap on
non-trivial components + naive per-summand Casimir diagonality assumption).

**What was NOT killed:** The possibility that rank=1 (the paper's claim) is
actually correct — it may well be, but for a DIFFERENT reason than currently
stated (an explicit non-vanishing torsion cross-term, or an explicit
non-degeneracy of the relevant spinor pairing), not yet computed.

**Relaxation map:** the crux question has been narrowed from "is dim ker
1 or 2, for unspecified reasons" (Round 1) to the single, well-posed,
computable question: "does Clifford multiplication by the G2-invariant
3-form T produce a non-zero matrix element between the V_a-derived and
V_b-derived basis vectors of the 2-dim trivial multiplicity space?" This is
a concrete, finite computation (not a fishing expedition) — it requires the
explicit torsion tensor / associative 3-form on G2/SU(3) (already used
elsewhere in this project's KP-formula infrastructure, e.g. Agricola 2002
cited in kp_zero_mode.py) and explicit spinor harmonic representatives for
V_a and V_b.

## Why PARKED, not pursued further today

This computation requires real differential-geometric care (explicit
torsion 3-form action on specific Clifford-module elements) beyond what can
be responsibly rushed in one sitting without risking a THIRD layer of
unverified claims stacked on the first two. Cost/benefit: the preprint's
public-facing claim can and should be fixed NOW (downgrade "L4B, proved" to
explicitly open, matching the honesty standard already applied to L3b/L4A
today) independent of whether the deeper torsion computation ultimately
vindicates rank=1 or not.

## MAJOR UPDATE 2026-07-08 (same session, continued): root cause found in primary source

Read Agricola 2002 pages 1-4, 12-14 directly (via doc_bridge parse, not Read-tool PDF
rendering which failed — no poppler installed). CONFIRMED from the abstract itself:

"the one-parameter family of connections nabla^t joining the canonical and the
LEVI-CIVITA connection (t=0, 1/2). ... the Dirac operator D^t corresponding to
t=1/3 is the so-called 'cubic' Dirac operator ... introduced by B. Kostant."

Theorem 3.3's clean scalar formula (D^t)^2 = Omega_G + const — the ONE our
kp_zero_mode.py code implicitly uses — is proved ONLY at t=1/3 (cubic Dirac),
because the coefficient (1-3t) multiplying an extra Clifford-multiplication term
vanishes exactly there. At t=1/2 (Levi-Civita, the physically relevant connection
for actual fermion fields), (1-3t) = -1/2 != 0, so this extra term does NOT vanish
in general. This is the precise, sourced identity of the "torsion correction"
E-KP1's own claim.md flagged as HYPOTHESIS: our code has been computing spectral
data for Kostant's cubic Dirac operator, not the Levi-Civita Dirac operator, and
the two need not have the same kernel dimension (though by general index theory
they DO share the same INDEX, since index is a homotopy/topological invariant
across this connection family — this is why the paper's global index=1 claim
remains solid regardless).

Scope broadened: this extra term does not obviously vanish on non-trivial
G2-isotypic components either, so the "safe" KP-gap conclusion (no zero modes
outside the trivial component) also technically needs re-examination for t=1/2,
not just the trivial-component rank question. Not yet checked whether the gap
(currently >=1 in Casimir units) is large enough to absorb this extra term's
magnitude.

**Directly relevant resource found:** Agricola-Hofmann-Lawn 2023 ("Invariant
Spinors on Homogeneous Spheres"), Section 5.1, is titled literally "S^6 = G2/SU(3)"
and gives, for the genuine Levi-Civita connection:
- Theorem 5.1: the G2-invariant (untwisted) spinors form Sigma_inv =
  span_C{1, y1^y2^y3} (2-dimensional), and psi_+- = 1 +- y1^y2^y3 are explicit
  Riemannian Killing spinors: nabla^g_X psi_+- = +-(1/2sqrt3) X . psi_+-.
- Explicit orthonormal basis e_1..e_6, explicit su(3) action (ad(nu_i)|_m),
  explicit Levi-Civita Nomizu map Lambda^g(e_i) (Remark 5.2).
- Proposition 5.4: explicit Ambrose-Singer torsion T^AS =
  (1/sqrt3)(-e_136 - e_145 - e_235 + e_246).

This is concrete, usable data for the actual twisted-bundle computation (not the
untwisted case Theorem 5.1 covers directly, but the same explicit structure
constants and torsion form apply). Adapting it to the S+⊗S- -> S-⊗S- twisted
Dirac operator is a genuine, multi-hour piece of careful Clifford-algebra work,
not a quick add-on — recommend a dedicated future session using this exact
page-42 data as the starting point, rather than re-deriving structure constants
from scratch.

## Revival condition
Resume when: (a) explicit torsion/Clifford-multiplication formulas for
G2/SU(3) spinor harmonics are set up carefully (dedicated session, not a
rushed addendum), or (b) Dolan's Casimir-operator method (already cited in
preprint.tex as untried for G2/SU(3)) is implemented as a full independent
cross-check, whichever is cheaper once scoped properly.

## Pearl
observation: the paper's own pre-existing "torsion correction" open item
(E-KP1 claim.md) was more consequential than its own author (this project,
in a past session) realized — it is not a minor correction to an established
result, it is the actual open crux determining whether the central kernel
count is 1 or 2.
falsifiable_prediction: an explicit torsion cross-term computation will
either (a) vanish, vindicating rank=1 as claimed, or (b) be non-zero,
forcing dim ker(D+)=2 and requiring re-derivation of the "one zero mode per
triality channel" picture underlying N_gen=3's whole framing.
trigger_condition: next dedicated session on this specific computation.
next_check: before any further public claim building on L4B's current
"proved" status.

## Round 4-5 (2026-07-08, continuation): L4B rank RESOLVED, but skeptic
## re-check surfaces a BIGGER issue affecting the "proved" non-trivial part

Session resumed same day (L4B was not actually left parked). Built and
calibrated an explicit Clifford-module framework (g2su3_explicit_clifford.py,
g2su3_twisted_kernel.py, g2su3_find_invariant.py, g2su3_compute_crossterm.py,
g2su3_skeptic_checks.py) using AHL2023 Sec 5.1/2.1 data. Calibration against
AHL2023 Thm 5.1's Killing-spinor eigenvalue: EXACT match, all 6 directions.
v_a = y1(x)y23 - y2(x)y13 + y3(x)y12 found as the unique SU(3)-invariant in
span{y1,y2,y3}(x)span{y12,y13,y23} (solved via nullspace, not guessed).
Decisive computation: D(v_a) = D(v_b) = -sqrt(3)*w exactly (v_b=y123(x)1),
zero leftover components -> rank(D+|trivial)=1, dim ker(D+_S-)=1 CONFIRMED
via genuinely independent computation (not the "index=1=>rank=1" non-sequitur).

Skeptic round 3 (WEAKENED, 2 tests requested) -- both PASSED cleanly:
individual-term decomposition (all 3 terms of v_a give exactly -sqrt(3)/3,
zero leftover each) and chirality operator gamma_7=e1..e6 (eigenvalues -i,+i
on "1","y123", opposite signs as required).

Skeptic round 4 (re-check with complete non-trivial-component argument
included): confirmed the "uniform Casimir bound closes the infinite
rho-tower at once" logic is valid (resolves round-3's per-lambda concern
legitimately) -- BUT found that preprint.tex's non-trivial-component
argument (lines 604-630/719, currently "proved") uses the SAME naive
Casimir-difference formula that is only exact for Kostant's cubic Dirac
(t=1/3, Agricola 2002 Thm 3.3), not the Levi-Civita operator (t=1/2) used
for the physical interpretation elsewhere. The correction term (coefficient
(1-3t)=-1/2 at t=1/2) is not accounted for on non-trivial isotypic pieces --
the preprint only flags this for the trivial piece. Same root cause as L4B,
one level up, affecting text currently marked unconditional.

## Investigating the danger zone (rho=7 fundamental, smallest non-trivial)

Read Agricola 2002 Theorem 3.2 verbatim (exact general (D^t)^2 formula, n>=5):
  (D^t)^2 psi = Omega_g psi + (1/2)(1-3t) sum_ijk <[Zi,Zj]_m,Zk> ZiZjZk psi
              - (1/2) sum_{i<j<k<l} [<Zi,Jac_m(Zj,Zk,Zl)> + 9t^2 Jac_h(Zj,Zk,Zl)] ZiZjZkZl psi
              + scalar terms (Q_h, Q_m sums, t-dependent)
Key structural fact: Omega_g (2nd-order differential Casimir) acts as the
KNOWN scalar C_2(G2;rho) on any rho-isotypic section. ALL OTHER terms
(cubic + quartic + scalar) are PURELY ALGEBRAIC Clifford operators on the
FIBER, rho-independent -- computable without touching G2's rep theory on
V_7/V_14 at all.

Progress (g2su3_H_element.py): cubic term at t=1/2 simplifies exactly to
-H, H := (1/4) sum T(i,j,k) Zi.Zj.Zk (Kostant's cubic element), T(i,j,k) =
<[Zi,Zj]_m,Zk> extracted (factor-of-2) from the calibrated
LEVI_CIVITA_NOMIZU data: T(1,3,6)=T(1,4,5)=T(2,3,5)=-sqrt(3)/3,
T(2,4,6)=+sqrt(3)/3 (others by verified total antisymmetry). **This
independently matches AHL2023 Prop 5.4's stated Ambrose-Singer torsion
T^AS=(1/sqrt3)(-e_136-e_145-e_235+e_246) exactly** (1/sqrt3 = sqrt(3)/3,
same signs) -- strong cross-check that the torsion extraction is correct.
H built as explicit 8x8 Clifford operator on Sigma (single copy), H^2
computed by direct matrix squaring: H^2 = 3*Id + degree-4 part, giving
H^2=12 on the trivial-multiplicity-2 piece (span{1,y123}), H^2=0 on the
3 + 3bar piece (span{y1,y2,y3},{y12,y13,y23}). Matches Schur's lemma
(H commutes with SU(3) since T is G2-invariant, hence block-scalar per
irreducible SU(3) piece) and cross-checks against Agricola's closed-form
(H^2)_0=(3/8)*sum(T^2)=3 (the uniform scalar; +9/-3 split is the
non-scalar degree-4 piece).

STILL MISSING before rho=7/14 danger-zone check can be closed:
1. The SEPARATE "9t^2 Jac_h(Zj,Zk,Zl)" quartic piece -- su(3)-valued
   curvature [Zi,Zj]_h, not captured by H^2 (which only gives the
   Jac_m/torsion-squared part). Needs either full g2 structure constants,
   or back-solving from the known round-S^6 curvature formula
   R(X,Y)Z=(1/rho_6^2)(<Y,Z>X-<X,Z>Y) minus the torsion-squared
   contribution (Agricola Section 2 likely has the exact naturally-
   reductive curvature-torsion relation; not yet read this session).
2. This computation was on SINGLE-copy Sigma. The actual relevant operator
   is on the TWISTED fiber Sigma(x)Sigma (matching D_on_simple_tensor's
   domain) -- needs a Leibniz-rule generalization of H to the tensor
   product, same pattern D_on_simple_tensor already implements for D.

Status: task #7 (rho=7,14 torsion correction on non-trivial blocks)
IN PROGRESS -- real, checkpointed partial progress (cubic term fully
resolved and cross-validated against an independent primary-source
formula), 2 concrete, scoped remaining sub-steps identified. Task #6
(honesty caveat on the non-trivial-component "proved" claim) still
PENDING -- recommended regardless of how far #7 goes, since the gap in
the preprint's current text is real independent of whether the
correction eventually turns out to be harmless.

## Decision (2026-07-09): Caveat added; next gate is explicit rho=7 computation

### Status

Task #6 CLOSED. preprint.tex no longer overclaims non-trivial G2-sector
vanishing for the Levi-Civita twisted Dirac operator. Caveat added in 4
locations: SS4 intro (lines ~565-568), SS4.2 after the Casimir-gap
derivation (new paragraph after line 630), the L5 Summary paragraph
(~line 739-745), and the L4B Open Problems entry (~line 1079). Each now
distinguishes:
- Kostant/cubic Dirac normalization (t=1/3): naive Casimir-gap formula
  lambda^2=C_2(G2;rho)-C_2(SU(3);sigma) applies directly (Agricola 2002
  Thm 3.3) -- this part genuinely IS proved.
- Levi-Civita twisted Dirac operator (t=1/2), used for the physical
  zero-mode count everywhere else in the paper: an additional torsion
  correction (coefficient (1-3t)=-1/2, Agricola 2002 Thm 3.2) must be
  controlled on every non-trivial isotypic component, not yet done.
Recompiled twice (pdflatex), 0 errors (grep -cE "^!" preprint.log), no
undefined refs, 21 pages.

### Current mathematical status

Fibre-level trivial-sector computation remains strong:
  D(v_a) = -sqrt(3) w,  D(v_b) = -sqrt(3) w
giving candidate zero mode psi_0 = v_a - v_b, rank(D+|trivial)=1,
confirmed via calibration + 2 independent skeptic-requested stress tests
(individual-term decomposition, chirality operator) -- see rounds 3-3.5
above. Status: [HYPOTHESIS-STRONG] / "strong computational evidence,
pending independent sign-off" (not yet [CONFIRMED-REAL] -- no external
reviewer has seen this).

Global statement dim ker(D+_S-)=1 remains CONDITIONAL until non-trivial
G2-isotypic sectors are verified for the Levi-Civita operator specifically
(not merely the Kostant/cubic operator, which is where the existing
"proved" Casimir-gap argument actually lives).

### Next critical task: rho=7 (fundamental, smallest non-trivial G2 rep)

Lowest non-trivial G2 Casimir gap (C_2=4 vs max fibre C_2=3, margin exactly
1 in Casimir units) -- the single most exposed block to a bounded torsion
correction of comparable size. If rho=7 survives, rho=14 (adjoint) and all
larger rho are progressively safer (Casimir gap grows unboundedly while
the torsion correction is a fixed, bounded fibre operator).

Planned computation (10 steps, next session, fresh context -- do NOT rush
this at the end of a long session):
1. Build an explicit octonion/Fano-plane model of V_7 (the 7-dim G2 rep),
   using Im(O) = R^7 with G2 = Aut(O).
2. Verify its multiplication table against the ALREADY-computed torsion
   coefficients: T(1,3,6)=T(1,4,5)=T(2,3,5)=-sqrt(3)/3, T(2,4,6)=+sqrt(3)/3.
   [Promising lead found this session, NOT yet fully verified: treating
   these 4 triples as 4 of the 7 Fano-plane lines on points {1,...,6,p},
   the 3 "missing" pairs among {1,...,6} (not covered by any of the 4
   known lines) come out to exactly {1,2},{3,4},{5,6} -- which are
   EXACTLY the (e_{2j-1},e_{2j}) pairs already used throughout
   g2su3_explicit_clifford.py's j=(i+1)//2 indexing (the y1,y2,y3
   Lagrangian-subspace grouping). This suggests the octonion realization
   is naturally compatible with the existing basis, not an independent
   coordinate system requiring re-derivation from scratch -- but this
   compatibility is only a strong hint from index-matching so far, not a
   verified fact; step 2 above must confirm it numerically before
   anything downstream depends on it.]
3. Check the missing Fano pairs {1,2},{3,4},{5,6} match the existing
   Clifford grouping used for y1,y2,y3 (formal version of the check in
   step 2's bracket).
4. Construct the G2 action on V_7 explicitly (matrices for all 14
   generators: 8 su(3) + 6 m-directions, acting on the 7-dim rep).
5. Decompose V_7|_{SU(3)} into 3 (+) 3bar (+) 1 with EXPLICIT basis
   vectors (not just abstract multiplicities).
6. Build the relevant multiplicity space Hom_{SU(3)}(V_7, Sigma tensor
   Sigma) explicitly.
7. Extend the torsion/cubic correction H from Sigma to Sigma tensor Sigma
   via the Leibniz rule (same pattern D_on_simple_tensor already
   implements for D itself in g2su3_compute_crossterm.py).
8. Assemble the torsion-corrected Levi-Civita block matrix D_7 (Omega_g
   contributes the KNOWN scalar C_2(G2;7)=4; the correction terms are
   the rho-independent fibre operators from steps 4-7).
9. Compute ker(D_7). If empty -- rho=7 is safe, matching the paper's
   existing claim; if non-empty -- the "proved" non-trivial vanishing is
   FALSIFIED for at least this block, a serious finding requiring
   re-deriving the whole N_gen=3 zero-mode count.
10. If ker(D_7)=0: proceed to rho=14, or derive a safe Casimir-cutoff
    argument bounding the correction operator's norm uniformly (so all
    rho >= 14, or some explicit threshold, are automatically safe without
    a case-by-case check).

Still outstanding from the earlier round (not resolved by this plan
alone, needs explicit attention in step 8): the SEPARATE "9t^2
Jac_h(Zj,Zk,Zl)" quartic piece (su(3)-valued curvature [Zi,Zj]_h, not
captured by H^2 alone) -- may be resolvable via the octonion structure
constants built in steps 1-4 (curvature of a naturally reductive space is
expressible via the same Lie bracket data), avoiding the need to
separately back-solve from the round-sphere curvature formula.

### Promotion rule

Do NOT promote "dim ker(D+_S-)=1" (or the non-trivial-sector vanishing)
back to unconditional "proved" in preprint.tex until ALL of:
- the rho=7 block is explicitly checked (steps 1-9 above);
- the torsion/curvature correction (both cubic H-term AND the Jac_h
  quartic piece) is included, not just the torsion-squared part;
- operator conventions are confirmed to match the Levi-Civita twisted
  Dirac operator used for the physical zero-mode count (not silently
  drifting back to the cubic/Kostant convention);
- EITHER rho=14 is checked OR a valid Casimir-cutoff argument excludes
  all higher non-trivial G2-types uniformly.

### Current verdict

Local trivial-sector zero-mode: [HYPOTHESIS-STRONG / CONFIRMED-COMPUTATIONAL]
(calibrated, 2 independent stress tests passed, no external sign-off yet).
Global full L^2-kernel count dim ker(D+_S-)=1: [CONDITIONAL] -- gated on
the rho=7 computation above.

### Pearl (process-level, not physics-level)

observation: an adversarial skeptic pass, run with an intentionally
restricted context (claim + code only, no reasoning chain), caught that a
spectral-gap argument already labeled "proved" in the preprint used the
Casimir formula for the WRONG Dirac-operator normalization (cubic t=1/3
instead of the physically-used Levi-Civita t=1/2) -- a bug in the
argument, not in the arithmetic, that a same-context reviewer would very
plausibly have waved through since the formula "looked standard."
falsifiable_prediction: the rho=7 computation (steps 1-10 above) either
confirms the gap survives the correction (paper's existing claim vindicated
via a genuinely independent route) or finds a counterexample (kernel
appears on a non-trivial block, forcing re-derivation of N_gen=3's
zero-mode count from scratch).
trigger_condition: next dedicated session on this experiment.
next_check: before any further public claim building on the non-trivial-
sector "proved" status, and before any arXiv re-submission that touches
SS4 of the preprint.

## Round 6 (2026-07-09, autonomous continuation): V_7 ansatz NULL, then a
## real simplification found + validated for the UNTWISTED case; twisted
## case's remaining gap now precisely scoped

Self-imposed exit condition (per CLAUDE.md /goal-mode discipline, since the
literal /goal UI command cannot be invoked programmatically): explicit
torsion-corrected ker(D_7) computation, OR a precisely-scoped honest
blocker if genuinely stuck, with mandatory cross-checks and no forced
"safe" conclusions. Result below is the latter -- real, validated partial
progress, blocker precisely identified, nothing forced.

### Step 1 attempt (steps 1-4 of the plan): NULL result, abandoned per protocol

Built a "rolling map" ansatz for how m (isotropy-complement, 6 of g2's 14
generators) acts on the ambient 7-dim representation V_7 = Rp (+) m:
  e_i . p = e_i,   e_i . e_j = -delta_ij p + [e_i,e_j]_m
(g2su3_V7_construction.py). This is NOT lifted from a cited theorem --
[INFERRED] from general reasoning about naturally reductive spaces, and
therefore mandatorily calibrated before use (session-standing rule).

Calibration (g2su3_V7_calibration_check.py): computed [M_i,M_j] for all 15
pairs i<j in 1..6 as explicit 7x7 matrix commutators, decomposed each
against the 8-dim image of su(3)'s vector-action generators (reusing the
SAME calibrated SU3_GENERATORS/bivector data). Since dim(g2)=14=dim(su3)+
dim(m) exactly (no extra u(1)), h=su(3) exactly -- [M_i,M_j]'s image
should lie ENTIRELY within su(3)'s 8-dim span, no residual.

RESULT: ALL 15 pairs showed a residual outside su(3)'s image (rank of
augmented system = rank(su3_basis)+1 for every single pair, not isolated
noise on 1-2 pairs). This is a systematic, structural failure, not a
rounding/sign slip -- the ansatz formula itself is wrong or incomplete.
Per the pre-committed anti-cheating rule ("do NOT force a fit"), this
ansatz is ABANDONED. Task #8 closed as a NULL result (see Kill Analysis:
what was killed = this SPECIFIC unverified ansatz formula; what was NOT
killed = the underlying goal, or the validity of T(i,j,k) itself, which
remains independently cross-checked against AHL2023 Prop 5.4).

### Step back: read Agricola 2002 Section 2 (pages 3-6, not read earlier
### this session) for the primary-source curvature/bracket relations

Key finds, all directly quoted/paraphrased from the paper (not re-derived
from memory):
- Lemma 2.2: general curvature R^t(X,Y)Z = t^2[X,[Y,Z]_m]_m +
  t^2[Y,[Z,X]_m]_m + t[Z,[X,Y]_m]_m + [Z,[X,Y]_h].
- Section 2 remark (p.5-6, in the proof leading to Lemma 2.3): "the
  summands of Jac_h(X,Y,Z) automatically lie in m ... The Jacobi identity
  for g implies <Jac_m(X,Y,Z)+Jac_h(X,Y,Z), m> = 0" -- since both Jac_m
  and Jac_h are m-valued and their sum is orthogonal to all of m, the sum
  is IDENTICALLY ZERO: **Jac_h = -Jac_m always**, for any naturally
  reductive space, not just at t=1/3.

### Consequence: the full Theorem 3.2 correction reduces to H, H^2 alone

Using Jac_h=-Jac_m, Theorem 3.2's cubic + quartic terms both become
expressible purely via H (already built, cross-validated) and H^2
(already computed by direct matrix squaring):
  cubic(t)   = 2(1-3t) H
  quartic(t) = (1-9t^2) * (1/9) * (H^2 - 3*Id)      [(H^2)_0=3, established]
  scalar(t)-scalar(1/3) = 3*(t^2-1/9)                [Q_h piece cancels,
                                                        it's t-independent]

Defined Delta(t) := (D^t)^2 - (D^{1/3})^2 -- the correction beyond the
naive Casimir-difference formula (which IS exact at t=1/3, Kostant cubic
Dirac, per Agricola Thm 3.3 -- this is precisely what the preprint's
current, un-caveated non-trivial-component argument implicitly uses).

MANDATORY sanity check before trusting the t=1/2 result: Delta(1/3) must
be EXACTLY the zero matrix (Theorem 3.3 says both correction terms vanish
there). Computed (g2su3_delta_correction.py): **Delta(1/3) = 0, exactly,
all 64 entries of the 8x8 matrix** -- PASSED. This independently validates
the Jac_h=-Jac_m derivation and the coefficient bookkeeping (a real,
non-trivial check -- if the derivation had a sign or factor error, this
would almost certainly have shown a nonzero residual).

### Delta(1/2) result (untwisted Sigma, single copy -- NOT yet the physically
### relevant twisted operator, see gap below)

  On the 3 (+) 3bar piece (y1,y2,y3,y12,y13,y23): Delta(1/2) = +5/6
  exactly, scalar, no off-diagonal mixing (as expected per Schur, distinct
  irreps).
  On the trivial-multiplicity-2 piece (span{1,y123}):
    Delta(1/2) = [[-5/6, -2*sqrt(3)], [-2*sqrt(3), -5/6]]
  (a genuine 2x2 matrix, not scalar -- allowed since the trivial rep has
  multiplicity 2, consistent with Schur only forcing block structure, not
  diagonality, exactly the L4B ambiguity's own origin).

This is a real, validated, standalone result for the UNTWISTED Dirac
operator D^t on a single copy of Sigma. It is NOT yet the answer to the
rho=7 question, because...

### The remaining gap for the TWISTED operator (honest, precisely scoped)

The relation D^t = D^0 + tH (untwisted) generalizes EXACTLY via the
Leibniz rule to D^t_twisted = D^0_twisted + t*H_twisted, with
H_twisted = H (x) Id + Id (x) H (rigorously derived, not assumed -- direct
consequence of the connection's Leibniz rule, no new assumption).

BUT: Delta_twisted(t) = (D^t_twisted)^2 - (D^{1/3}_twisted)^2 expands to
  (t-1/3)*{D^0_twisted, H_twisted} + (t^2-1/9)*H_twisted^2
and the ANTICOMMUTATOR {D^0_twisted, H_twisted} is NOT simply obtainable
from H_twisted alone -- in the untwisted case, Agricola's Theorem 3.2
proof (Lemma 3.3: computing {H,Z_l} explicitly, then combining with the
Casimir operator Omega_g) is what supplies this; that derivation has not
been redone for the twisted (Leibniz-squared) setting. This is exactly
the same category of gap the V_7 ansatz was trying to close from a
different angle (representation-theoretic access to how sections
genuinely vary, i.e. the true-derivative/Omega_g piece for non-constant,
non-trivial-isotype sections) -- both routes converge on the same missing
ingredient.

**Two remaining options, both real work, neither attempted yet this round:**
1. Re-derive Agricola's Theorem 3.2 proof technique (Lemma 3.3-style
   anticommutator computation) for the TWISTED/Leibniz-squared operator
   directly -- stays entirely within the H/H^2-only toolkit that just
   passed a real validation (Delta(1/3)=0), so is the lower-risk option,
   but is a genuine new derivation, not a mechanical extension.
2. Fix the V_7 ansatz (task #8's failure) with a correctly-verified
   formula for g2's action on the fundamental 7 (the octonion/Fano-plane
   route remains promising -- the missing-pairs match to the existing
   {e1e2,e3e4,e5e6} grouping is still a good lead -- but needs the ACTUAL
   octonion multiplication table checked directly against T(i,j,k),
   rather than the guessed "rolling map" formula which is now known wrong).

### Status: task #7 still OPEN, real progress made and cross-validated,
### remaining gap precisely identified (not vague)

- Delta(t) formula for the UNTWISTED operator: validated, usable result.
- Delta_twisted(t) for the operator that actually matters for rho=7: NOT
  yet computable with current tools -- needs option 1 or 2 above.
- Given this, the rho=7 kernel question remains OPEN. Per the /goal's
  anti-cheating constraint, NOT forcing a "kernel=0, paper's claim
  survives" conclusion from the untwisted-only result -- the untwisted
  Delta(1/2) values (+5/6 on 3+3bar, and the 2x2 matrix on trivial) are
  suggestive (same order of magnitude as the Casimir gap of 1, neither
  overwhelmingly larger nor obviously negative) but NOT a substitute for
  the actual twisted computation.
- preprint.tex's caveat (added earlier this session, task #6) remains the
  correct, honest state of the paper -- no further edit needed or
  justified by this round's findings.

Next session: attempt option 1 (twisted Lemma-3.3-style anticommutator
derivation) first -- lower risk, reuses validated H/H^2 toolkit, doesn't
require fixing the V_7 ansatz.

## Round 7 (2026-07-09, same autonomous continuation): independent
## cross-check of Delta(1/2) surfaces a DEEPER, but ENCOURAGING, subtlety

Before extending to the twisted operator, ran one more independent check
of the untwisted Delta(1/2) result using data already fully trusted this
session: the calibrated Killing-spinor relation D^{1/2}psi_+ = -sqrt(3)
psi_+ (psi_+ = 1+y123, matches the skeptic-verified c_b=-sqrt(3) result
from Round 3). Direct hand+tool computation: (D^{1/2})^2 psi_+ = 3 psi_+
(exactly, since (-sqrt3)^2=3). Also: psi_+ is su(3)-invariant (annihilated
by all 8 su3_action generators, confirmed by construction), so on psi_+
the true-derivative terms vanish AND the su(3)-Casimir piece of Omega_g
vanishes too (su(3)-invariant vector is killed by the lifted su(3)
Casimir C_h, by definition of "invariant") -- so Omega_g psi_+ = 0
directly, no assumption needed.

Combined with Delta(1/2)|_trivial = [[-5/6,-2sqrt3],[-2sqrt3,-5/6]] (from
Round 6): Delta(1/2)*psi_+ = (-5/6-2sqrt3)*psi_+ (psi_+ is an eigenvector,
as expected -- it respects the +/- Killing-spinor split). This gives, by
definition Delta(1/2):=(D^{1/2})^2-(D^{1/3})^2:
  (D^{1/3})^2 psi_+ = 3 - (-5/6-2sqrt3) = 23/6 + 2*sqrt(3) ≈ 7.29

This is NOT zero -- meaning (D^{1/3})^2 on the trivial isotype does NOT
equal the "naive Casimir formula" C_2(G2;0)-C_2(SU(3);0)=0 that the
preprint cites as "Kostant-Parthasarathy formula". At first this looked
like a possible new problem (does the preprint's ENTIRE "proved"
non-trivial-component claim, even at t=1/3, also need this correction?).

## RETRACTED 2026-07-09 (later same session, "Round 14 continued" section
## near the end of this file): the ~7.29 number and the "Delta(1/2) on
## 3(+)3bar = +5/6" claim below were computed with a sign-bugged
## quartic_term() (Jac_h/Jac_m swapped from a mistranscription of
## Agricola's Theorem 3.2). CORRECTED value: Delta(1/2) on 3(+)3bar is
## EXACTLY 0, not +5/6. The Weyl-vector-shift ~7.29 identification below
## is consequently also unverified/likely wrong and needs recomputing
## with the corrected trivial-piece matrix [[5/3,-2sqrt3],[-2sqrt3,5/3]]
## (was [[-5/6,-2sqrt3],[-2sqrt3,-5/6]]) if this interpretation is still
## wanted -- not redone here, low priority (L4B does not depend on it).
## Kept below for historical record, NOT as current status -- see the
## "Round 14 continued" section for the full correction and why it does
## NOT affect L4B.
## Resolution: this matches the STANDARD Weyl-vector-shift Casimir formula,
## not a new bug -- and it is POSITIVE, so it does not threaten the gap
## [RETRACTED, see note immediately above]

The standard Kostant/Parthasarathy-Vogan cubic-Dirac formula (well known
in the literature, e.g. Kostant 1999, Huang-Pandzic) is actually
  D_cubic^2 = C_2(G;rho) - C_2(H;sigma) + ||rho_G||^2 - ||rho_H||^2
i.e. it has a FIXED additive shift (difference of squared Weyl-vector
norms for G and H), NOT just the bare Casimir difference. This shift is
UNIFORM -- the same constant for every (rho,sigma) pair, a property of
the pair (G2,SU(3)) alone, not of the specific representations. The
value found here (~7.29) is consistent with this being that shift
(computed indirectly, via the trivial isotype, rather than looked up).

**Why this is encouraging, not alarming:** since the shift is POSITIVE and
UNIFORM, it makes the non-trivial-component gap LARGER everywhere, not
smaller -- if anything the preprint's existing "proved" (at t=1/3) claim
has MORE margin than the bare Casimir-difference calculation shows, not
less. This does not need to be fixed in the preprint for correctness (the
qualitative conclusion "gap>0 for all non-trivial rho" is unaffected,
probably strengthened) -- but SHOULD eventually be added as a precision
note if the paper is revised further (currently harmless-but-imprecise,
not wrong).

## Consequence for rho=7: Delta(1/2) on the RELEVANT sigma pieces
## [RETRACTED -- see note above the "Resolution" heading; corrected value
## is EXACTLY ZERO, not positive. Text below is the ORIGINAL, WRONG claim,
## kept for historical record only.]

Critically, Delta(1/2) on the 3 (+) 3bar piece (the SU(3)-types that
rho=7's branching 7|SU(3)=3(+)3bar(+)1 actually uses) is exactly **+5/6**
(Round 6 result) -- POSITIVE. Combined with the uniform positive shift
just found, this means: for rho=7, the t=1/2 correction, AS FAR AS THE
UNTWISTED-OPERATOR MODEL CAPTURES IT, does not threaten the gap -- it
helps. This is genuinely encouraging evidence, not a forced conclusion.
[RETRACTED -- corrected value is EXACTLY 0, not +5/6 -- see "Round 14
continued" section near the end of this file.]

## What this does NOT yet establish (still open, being precise about scope)

1. This is STILL the untwisted (single-Sigma) operator's Delta, not the
   physically relevant twisted operator on Sigma(x)Sigma -- the Round 6
   gap (need {D^0_twisted,H_twisted}, or a fixed V_7 construction) is
   UNCHANGED by this round's finding.
2. The twisted fiber's SU(3) content includes an "8"=(1,1) piece (from
   S+(x)S-|SU(3)=(1,1)+(0,1)+(1,0)+2x(0,0)) that does NOT appear in the
   single-copy Sigma module at all (Sigma is only 1+3+3bar+1, no 8) --
   this round's Delta(1/2) values say NOTHING about the 8-piece, which
   still needs separate treatment once the twisted extension is built.
3. The "Weyl-vector shift" identification is a plausible, standard-physics
   explanation for the ~7.29 number, not independently verified against a
   citation -- flagged as [WEAK] pending an actual literature check
   (e.g. Huang-Pandzic's book, or Kostant 1999 directly) if this number
   needs to be relied on precisely rather than just its sign.

## Status update

Local trivial-sector zero-mode: unchanged, [HYPOTHESIS-STRONG].
rho=7 danger-zone verdict: still OPEN (twisted operator not yet built),
but the untwisted-operator proxy computed this round is genuinely
encouraging (Delta(1/2)>0 on the relevant sigma pieces, plus an
apparently-positive uniform shift) rather than neutral or alarming. Not
strong enough alone to update preprint.tex or claim resolution -- the
gap identified in Round 6 (twisted anticommutator, or a corrected V_7
construction) is still the binding blocker for a definitive answer.

## Round 8 (2026-07-09): 3 parallel literature-search agents (PVF /
## Using-Wheels-First check before further from-scratch derivation)

Per user request, ran 3 background verifier agents to check whether any
of the remaining work is already solved in the literature, before
spending more compute on original derivation.

**Agent 1 (twisted KP-formula search) -- HIGH confidence NEGATIVE result:**
No twisted Kostant-Parthasarathy-type formula (torsion(M) x curvature(E)
cross terms, for a general naturally reductive non-symmetric M) exists in
Kostant 1999, Huang-Pandzic's book, or D. Renard's survey
(perso.pages.math.cnrs.fr/users/david.renard/paderborn.pdf, grepped in
full, zero matches for "naturally reductive"/"Agricola"). Huang-Pandzic
Ch.7-8 DOES treat twisted D on symmetric G/K (equal rank) via an INDEX
formula (Hirzebruch proportionality + Weyl dimension formula), not an
operator-square formula -- wrong setting (S^6=G2/SU(3) is non-symmetric)
and wrong output type (we need the operator, not just its index, which
we already have via Atiyah-Singer). **Genuine open gap, not just our
blind spot** -- re-deriving Theorem-3.2-style for the twisted case is
original work, no shortcut available.

**BUT: confirmed the Weyl-vector-shift formula IS real and standard**
(Renard survey Eq 9.4, Huang-Pandzic Thm 2.16/4.2.2, both [VERIFIED] by
direct read): D^2 = -Omega_g (x) 1 + Delta(Omega_r) + (||rho_r||^2 -
||rho||^2)*1(x)1 for the ALGEBRAIC Kostant operator (V a g-module, not a
geometric bundle) -- confirms the FORM of the shift found empirically in
Round 7 is a known, real phenomenon, not a computational artifact.
Exact numeric cross-check pending agent 3.

**Agent 2 (octonion/G2-on-V7 construction) -- mixed, but the key source
is solid:**
J. Baez, "The Octonions" (Bull. AMS 39 (2002), 145-205) [VERIFIED,
read directly, Table 1 + Fano-plane section] is THE standard, citable
octonion multiplication table. Bor-Montgomery's explicit G2 table
[VERIFIED but WRONG SETTING -- split real form / split octonions,
signature (3,4), not compact G2/SU(3) -- flagged do-not-transfer].
Fakhri et al. 2016 (arXiv:1603.05606) [VERIFIED, wrong basis -- pure
Cartan-Weyl, no su(3)+m isotropy split, not useful here].

Fetched Baez's Table 1 directly (this session) and extracted the exact
multiplication table:
  e1e2=e4, e1e3=e7, e1e4=-e2, e1e5=e6, e1e6=-e5, e1e7=-e3,
  e2e3=e5, e2e4=e1, e2e5=-e3, e2e6=e7, e2e7=-e6,
  e3e4=e6, e3e5=e2, e3e6=-e4, e3e7=e1,
  e4e5=e7, e4e6=e3, e4e7=-e5,
  e5e6=e1, e5e7=e4, e6e7=e2
giving the 7 Fano lines (cyclic): {1,2,4},{1,3,7},{1,5,6},{2,3,5},
{2,6,7},{3,4,6},{4,5,7}.

**Correction to Round 6's "promising lead":** since there is only ONE
Fano plane up to isomorphism (168 automorphisms, PSL(2,7)), ANY valid
totally-antisymmetric 3-form on a 6(+1)-point structure is AUTOMATICALLY
isomorphic to Baez's table under SOME relabeling -- so the earlier
observation ("our torsion's missing pairs = the existing e1e2|e3e4|e5e6
grouping") does NOT independently validate anything beyond "T(i,j,k) is a
consistent antisymmetric 3-form", which was already known. The actual
V_7-ansatz failure (Round 6, task #8) was in the ACTION FORMULA (how a
Lie algebra element of m acts on the ambient V_7), not in the Fano/torsion
structure itself, which remains solid. Octonion multiplication itself
(Baez Table 1) is NOT the same thing as the g2=Der(O) Lie-algebra action
needed -- using the table directly would require the standard but
separate "derivations of the octonion algebra" construction, not yet
attempted.

**Both agent 1 and agent 2 independently flagged prompt-injection content**
in fetched web/tool results (fake "system-reminder" blocks claiming date
changes and fabricated MCP instructions). Both correctly ignored and
flagged rather than acting on them -- noted here per the project's
security-awareness practice, not otherwise relevant to the math.

**Agent 3 (Weyl-vector-shift verification) -- PARTIAL, with a useful
correction to how the shift should be understood:**

Found the shift formula directly in Agricola 2002 Theorem 3.1 itself
(quoting Parthasarathy 1972 Prop 3.1): "D^2 = Omega_G + (1/8)Scal, Scal =
8(<rho_g,rho_g>-<rho_h,rho_h>)" -- confirms the Weyl-shift form is real
and traces to Kostant 1999 Thm 2.13 (per Agricola's own citation).

**Critical caveat correctly raised:** Theorem 3.1's CLEAN shift form only
holds for SYMMETRIC spaces. G2/SU(3) is a nearly-Kahler coset, NOT
symmetric -- so the raw ||rho_G2||^2-||rho_SU3||^2 does not directly
apply. The correct object for our (non-symmetric) case is Agricola's own
Theorem 3.2/3.3, which has EXTRA structure-constant (Q_m) and
scalar-curvature terms beyond the bare root-system quantity. This is
exactly the formula our own Delta(t) derivation (Round 6) already used --
independent confirmation that going through Theorem 3.2 rather than the
naive symmetric-space shortcut was the right call.

Independent numeric cross-check (Bourbaki-normalized Weyl vectors,
rescaled to Agricola's C_2(G2;7)=4, C_2(SU3;8)=3 convention):
||rho_G2||^2_rescaled - ||rho_SU3||^2_rescaled = 14/3 - 1 = 11/3 ~ 3.67.
Our derived value (Round 7): 23/6+2*sqrt(3) ~ 7.297. Note: 2*(11/3) =
22/3 ~ 7.33, within 0.5% of our number -- an intriguing but UNEXPLAINED
factor-of-2 relationship (agent's own words: "suggestive... not proof").
**Status: [WEAK] consistency signal, not a confirmation** -- our Round 7
value stands on the Delta(1/3)=0 sanity check (Theorem 3.2 itself, exact,
already validated) independent of whether this symmetric-space analogy
fully explains the number.

## Round 8 synthesis and decision

**No literature shortcut exists** for either open item (twisted KP
formula: confirmed absent by direct search across the standard
references; V_7/octonion action: Baez's table is the right raw
ingredient but doesn't itself supply the g2=Der(O) action, which is a
separate, well-known-but-unimplemented construction). Both search
directions returned real, useful context (confirms our Theorem-3.2-based
approach was correctly targeted, rules out chasing a nonexistent
citation) but not a shortcut.

**Decision:** proceed with Option 3 (re-derive the Lemma-3.3-style
anticommutator {D^0_twisted, H_twisted} directly) as the next concrete
step, since:
- It stays entirely within the H/H^2 toolkit already built and validated
  (Delta(1/3)=0 exact match, cross-checked against AHL2023's independent
  torsion data, and now loosely consistent with the standard Weyl-shift
  phenomenology).
- The V_7/octonion route, even with Baez's verified table in hand, still
  needs the SEPARATE Der(O) construction and would face the SAME
  calibration-failure risk as Round 6's attempt, with no literature
  shortcut to lean on either.
- Two independent literature agents confirm this is genuinely open,
  original-derivation territory, not a known-solved problem we missed --
  the effort is justified, not redundant.

Task #9 (synthesize 3 agents) CLOSED. Next: attempt the twisted
anticommutator derivation directly, following Agricola's own Lemma 3.3
proof technique (compute {H_twisted, e_i(x)1 + 1(x)e_i} explicitly using
the calibrated Leibniz-rule machinery already in
g2su3_compute_crossterm.py) as a dedicated next step.

## Round 9 (2026-07-09): anticommutator attempt surfaces a SERIOUS,
## UNRESOLVED foundational question about nabla_g's validity -- flagging
## honestly rather than pushing past it

Attempted the twisted anticommutator derivation (g2su3_twisted_anticommutator.py).
Hand-derived: {D^0_twisted,H_twisted}(eta(x)xi) decomposes into pieces
each containing an explicit e_i(eta) or e_i(xi) factor; PREDICTED that for
eta,xi both trivial-G2-isotype (SU(3)-invariant), all pieces vanish, so
(D^t_twisted)^2 = t^2 * H_twisted^2 EXACTLY on trivial isotype.

**Direct test against the ALREADY-COMPUTED L4B result: FAILED.**
Computed (D^{1/2}_twisted)^2(v_a) two ways:
  (a) D_on_simple_tensor applied TWICE directly (fully independent of the
      new derivation) -> v_a + 3*v_b (both terms present, non-scalar)
  (b) (1/4)*H_twisted^2(v_a), using H_twisted=H(x)I+I(x)H -> ZERO
      (since H itself is 0 on the individual 3/3bar pieces -- H^2=0 there
      per Round 6, and Schur's lemma forces H=0, not just H^2=0, on a
      multiplicity-1 irrep with square zero)
These DISAGREE. The prediction is falsified by direct computation.

## Root cause investigation: v_a is a SUM of non-invariant simple tensors

v_a = y1(x)y23 - y2(x)y13 + y3(x)y12 is SU(3)-invariant only as the WHOLE
combination -- each individual term (y1(x)y23 etc.) is NOT SU(3)-invariant
(y1 alone transforms in the "3", not the trivial rep). My "e_i(eta)=0 for
trivial isotype" argument was derived for a SINGLE simple tensor eta(x)xi
with BOTH factors individually invariant (like psi_+=1+y123, where BOTH
"1" and "y123" are separately SU(3)-invariant) -- it does NOT obviously
extend to v_a's term-by-term decomposition, where the individual factors
(y1, y23, y2, y13, y3, y12) are NOT invariant.

## The unresolved question (genuinely open, not yet settled by hand-reasoning)

Does `nabla_g(i, vec)` -- implemented as ONLY the Nomizu-map/Lambda-term
formula, with NO explicit "e_i(vec)" true-derivative term -- correctly
compute the FULL covariant derivative for ANY vec (via a standard
"moving frame at the basepoint" construction, valid regardless of whether
vec individually corresponds to a globally-defined section), OR is it
ONLY valid when vec corresponds to a genuinely GLOBALLY CONSTANT
(H-invariant) section, with the missing true-derivative term happening to
vanish ONLY in that specific case?

Two lines of reasoning were tried this session, reaching OPPOSITE
conclusions at different points (self-contradicting -- flagged explicitly,
not resolved):
- Argument FOR "always valid": nabla_g computes d/dt|_0 of the local
  section s_v(gH):=[sigma(gH),v] using a local slice sigma with
  sigma(o)=e; this is a well-defined POINTWISE quantity regardless of
  whether s_v extends to a global section, giving Lambda(e_i)v ALWAYS.
  Leibniz rule + linearity would then make term-by-term decomposition of
  v_a valid REGARDLESS of individual-piece invariance.
- Argument AGAINST: the "e_i(psi)" in Agricola's own D^t formula is the
  derivative of psi AS AN EQUIVARIANT FUNCTION ON G at the identity --
  this depends on how psi is defined NEAR e, not just its value AT e
  ("vec" alone under-determines this). The ONLY canonical extension
  where this vanishes automatically is the literal constant function,
  valid ONLY for H-invariant vec.

**These two arguments cannot both be right, and this session's reasoning
went back and forth between them without a decisive resolution.** Given
the L4B result (D(v_a)=-sqrt(3)w) has ALREADY been reported to the user
as "strong computational evidence" and used to justify NOT reverting
preprint.tex's honest-downgrade of the Corollary -- and given this
specific validity question was NEVER put to skeptic (Rounds 3-4's checks
tested INTERNAL consistency of the computation, not this FOUNDATIONAL
premise about what nabla_g computes for non-invariant inputs) -- this is
flagged as a **genuinely open, unresolved, important question**, not
swept aside.

## What is NOT in doubt

- The CALIBRATION (nabla_g reproducing AHL2023 Theorem 5.1's Killing
  spinor eigenvalue exactly) IS solid -- but only tests INVARIANT input
  (psi_+ = 1+y123, both terms individually SU(3)-invariant).
- T(i,j,k) torsion data remains independently cross-validated against
  AHL2023 Prop 5.4's published Ambrose-Singer torsion -- unaffected by
  this question.
- H, H^2 (built from T(i,j,k) via pure Clifford-algebra bookkeeping, no
  "vec" ambiguity involved) remain solid.

## Immediate next step (before ANY further computation building on L4B)

Send this SPECIFIC, PRECISE question to skeptic (context-asymmetric,
mode=artifact) -- NOT re-litigating the whole L4B computation, but
isolating exactly this one foundational premise: is nabla_g(i,vec) =
Lambda^{1/2}_m(e_i).vec (Nomizu-map term only, no separate derivative
term) the mathematically correct FULL covariant derivative for a
homogeneous vector bundle section, for a GENERAL (not necessarily
H-invariant) fiber vector vec, under the standard associated-bundle
"natural local frame" construction -- or does it require vec to be
H-invariant for the missing true-derivative term to vanish?

This gates everything else in this experiment (L4B's already-reported
strength AND any further twisted-operator work) -- resolve this FIRST.

## Round 10 (2026-07-09, continued autonomous work): Round 9's "crisis"
## resolved -- mechanical formula error, NOT a foundational nabla_g flaw.
## L4B re-confirmed with NEW evidence. rho=7 gap re-scoped more precisely.

### Decisive test 1: SU(3)-equivariance of the full 64x64 D matrix

Built D^{1/2}_twisted explicitly as a 64x64 matrix (D_on_simple_tensor
applied to all 64 basis vectors of Sigma(x)Sigma), then checked [D,su3_i]=0
for all 8 su(3) generators (g2su3_equivariance_check.py). **Result: exact
equivariance holds for all 8 generators, zero residual.** This is a
necessary property of ANY correctly-constructed geometric Dirac-type
operator; failure would have been decisive proof of a broken construction.
Passing is strong (not 100% sufficient alone, since H itself is ALSO
SU(3)-equivariant -- see below) supporting evidence.

### Diagnosing Round 9's failed test: found a MECHANICAL formula error

Round 9 assumed the twisted "H"-analog is H_twisted = H(x)Id + Id(x)H
(symmetric Kronecker sum). Directly checked: **D != (1/2)*H_twisted**
(80 nonzero differences out of 4096 entries) -- this formula was WRONG,
not evidence of a deeper nabla_g problem.

Re-derived correctly by expanding D^t_twisted(eta(x)xi) term by term from
the ACTUAL formula used throughout this experiment (D(eta(x)xi) =
sum_i(e_i.nabla_{e_i}eta)(x)xi + sum_i(e_i.eta)(x)(nabla_{e_i}xi) --
Clifford multiplication acts ONLY on the LEFT/eta factor, matching the
standard twisted-Dirac-operator convention D_{S(x)E} where E is a
coefficient bundle without its own Clifford action, consistent with the
preprint's own L4A Weitzenbock setup "(D_{S^6}(x)S^-)^2"). The correct
t-linear ("H-like") coefficient operator is ASYMMETRIC:
  calH(eta(x)xi) = (H eta)(x)xi + sum_i (e_i.eta)(x)(Lambda_m^1(e_i)xi)
(the SECOND term genuinely entangles eta and xi via the shared index i --
it does NOT factor as eta(x)(H xi)). Verified numerically: **D equals
this corrected calH EXACTLY** (trivially, since D_on_simple_tensor's own
code IS this formula with nabla_g already carrying the t=1/2 scaling --
this check confirms the bookkeeping, not an independent fact).

### The REAL question restated and resolved: does D include an Omega_g piece?

Neither the equivariance check nor the calH match distinguishes "D is the
FULL D^{1/2} operator" from "D is only its algebraic part, missing a
true-differential Omega_g contribution" -- both would look identical on
these two tests (H and calH are themselves SU(3)-equivariant, and calH
literally IS D_on_simple_tensor's own formula by construction).

Resolved by REASONING (not a new computation) about what v_a, v_b
actually represent, correcting Round 9's confusion:
- v_a, v_b are EACH individually SU(3)-invariant (this was verified
  earlier: su3_action gives 0 on both). By Frobenius reciprocity, for
  rho=G2-trivial specifically, V_rho=C (1-dim), so
  Hom_SU(3)(V_rho|_SU(3)=trivial, fiber) = fiber^{SU(3)} EXACTLY (the
  WHOLE 2-dim invariant subspace, unambiguously) -- v_a, v_b span this
  space and correspond UNAMBIGUOUSLY to the rho=trivial isotypic piece,
  not a mixture. Since C_2(G2;trivial)=0, Omega_g's contribution is ZERO
  on this piece REGARDLESS of whether it is "included" in D's
  construction or not -- the L4B computation cannot distinguish the two
  interpretations, but ALSO does not need to: the answer is the same
  either way. **L4B stands, fully re-confirmed**, now with the
  equivariance check as an ADDITIONAL positive signal beyond the original
  calibration + skeptic stress tests.
- By contrast, individual NON-invariant fiber vectors (y1 alone, or the
  "3"/"3bar"/"8" SU(3)-irreducible pieces of the full twisted fiber) do
  NOT correspond to a single rho via Frobenius reciprocity -- MULTIPLE
  different G2-irreps rho (any rho whose SU(3)-branching contains that
  sigma-type) can contribute to the SAME fixed fiber subspace. This means
  **D^2's eigenvalues restricted to the fiber-level 3/3bar/8 pieces
  (computed directly, e.g. via Schur-forced block-scalars) do NOT
  isolate rho=7's (or rho=14's) specific Casimir contribution** -- they
  reflect whatever the algebraic (calH-based) operator gives, mixed
  across all rho sharing that sigma-type. This was Round 6-9's implicit,
  uncorrected assumption when attempting to read rho=7 data directly off
  fiber-level SU(3) blocks -- now explicitly identified as invalid.

### Net effect on the rho=7 gap

Unchanged in substance from Round 6/8's conclusion (still needs either
correct V_7 representation-theoretic data, or a properly-rederived
twisted-Theorem-3.2 that correctly isolates Omega_g^{(rho=7)}=4 from the
algebraic calH-type corrections) -- but now precisely understood WHY the
"just read it off the fiber matrix" shortcut does not work, rather than
vaguely gestured at. No further progress on closing this gap this round;
this round's value is entirely in (a) correcting a real mechanical error
that was about to propagate into a wrong twisted-anticommutator formula,
and (b) re-confirming L4B's validity with independent, additional
evidence (SU(3)-equivariance of the full operator) rather than leaving
Round 9's foundational worry unresolved.

### Given repeated self-correction this session (flagging honestly)

This round involved reasoning back and forth between contradictory
conclusions about nabla_g's validity multiple times before reaching the
above resolution by hand. Per this project's own audit-verification-gate
discipline (agent's/session's own [VERIFIED] often deserves re-checking),
this specific resolution -- "L4B is unaffected by the nabla_g ambiguity
because Omega_g=0 on rho=trivial regardless" -- is flagged for one
independent skeptic pass before being treated as final, given the
session's demonstrated tendency to self-contradict on this exact question.

## Round 11 (2026-07-09): skeptic pass finds a REAL gap in how the claim
## was DESCRIBED, then direct verification shows the actual computation
## was correctly scoped all along -- L4B fully re-confirmed, closed

Sent Round 10's resolution to skeptic (context-asymmetric). Verdict:
WEAKENED, with one concrete, correct objection: the prompt described the
fiber as "the full 8x8=64-dim Sigma(x)Sigma" and claimed this has a
2-dimensional SU(3)-invariant subspace spanned by v_a, v_b. Skeptic
computed the FULL Sigma(x)Sigma actually has **6** SU(3)-invariants
(1x1, 1xy123, y123x1=v_b, y123xy123, the 3x3bar invariant=v_a, and the
3barx3 invariant), not 2 -- a real, correctly-derived arithmetic fact.
Skeptic could not tell from the prompt alone whether this invalidates the
L4B claim, since the prompt didn't specify which SUBSPACE of the full
64-dim space the operator actually acts on.

**Resolution (verified directly, not asserted):** computed the chirality
(gamma_7 = e1.e2...e6 eigenvalue) of all 8 Sigma basis elements
explicitly. Result: eigenvalue is EXACTLY determined by degree parity --
odd degree (y1,y2,y3,y123) get +i (call this S^+), even degree
(1,y12,y13,y23) get -i (S^-). Checking v_a, v_b, w directly:
  v_a = y1(x)y23 - y2(x)y13 + y3(x)y12  -> y1,y2,y3 in S^+, y23,y13,y12
        in S^-  => v_a IN S^+(x)S^-
  v_b = y123(x)1                        -> y123 in S^+, "1" in S^-
        => v_b IN S^+(x)S^-
  w   = 1(x)1                           -> both factors in S^-
        => w IN S^-(x)S^-
This EXACTLY matches the preprint's own operator, D^+ :
Gamma(S^+(x)S^-) -> Gamma(S^-(x)S^-) (SS4.2) -- NOT the full,
chirality-unrestricted Sigma(x)Sigma the skeptic was (correctly, given
what it was told) evaluating. Within S^+(x)S^- specifically (16-dim, NOT
64-dim), SU(3) branching is (3+1)(x)(3bar+1) = (3(x)3bar)+(3(x)1)+
(1(x)3bar)+(1(x)1) = (8+1)+3+3bar+1 = 8+3+3bar+2x1 -- **exactly matching
preprint.tex's own stated branching** "(1,1)+(0,1)+(1,0)+2x(0,0)"
(SS4.2, already in the paper, used throughout this whole experiment).
The "2x(0,0)" piece is EXACTLY 2-dimensional, and v_a, v_b are EXACTLY
this piece.

**Verdict: the skeptic's "6 invariants" finding is arithmetically correct
for the full, chirality-unrestricted Sigma(x)Sigma, but not the relevant
space -- it does not apply to D^+'s actual domain S^+(x)S^-, where the
original "2-dimensional, v_a+v_b span it" claim is exactly right.** The
gap was in how Round 10's skeptic prompt DESCRIBED the setup (said "full
Sigma(x)Sigma" when the actual, always-used domain was the chirality-
restricted S^+(x)S^-), not in the underlying L4B computation itself,
which has been correctly scoped to S^+(x)S^- since it was first built
(matching preprint.tex SS4.2's own stated branching, which predates this
session).

### L4B status: fully re-confirmed, now via THREE independent lines of
### evidence (calibration + 2 skeptic stress tests from Round 3, the
### SU(3)-equivariance check from Round 10, and this chirality/branching
### verification from Round 11). No further re-litigation planned unless
### new evidence surfaces.

### rho=7 status: UNCHANGED, still open (see Round 6/8/10) -- this whole
### Round 9-11 detour was about verifying L4B's foundations, not about
### making progress on rho=7 itself. Next session should resume directly
### at Round 8's decision: attempt the twisted anticommutator via
### Agricola's Lemma 3.3 technique (now with the CORRECT asymmetric
### calH formula from Round 10, not the wrong symmetric H_twisted guess),
### or pursue a corrected V_7 construction.

## Round 12 (2026-07-09): re-derived the twisted anticommutator with the
## CORRECT asymmetric calH -- real progress (calH^2 now fully known per
## SU(3) piece), but the anticommutator itself unifies onto the SAME
## missing curvature ingredient that blocked the V_7 route -- not solved,
## but now precisely characterized as ONE blocker instead of two.

### Key structural fact confirmed: D_on_simple_tensor = (1/2)*calH EXACTLY,
### D^0_twisted is COMPLETELY ABSENT from what has been computed so far

Re-derived D^t_twisted = D^0_twisted + t*calH carefully (asymmetric calH,
Round 10): calH(eta(x)xi) = (H eta)(x)xi + sum_i(e_i.eta)(x)(Lambda_m^1(e_i)xi).
Since `nabla_g(i,vec)` computes ONLY Lambda_m^{1/2}(e_i).vec = (1/2)Lambda_m^1(e_i).vec
(no e_i(vec) true-derivative term anywhere in the code), D_on_simple_tensor
computes EXACTLY (1/2)*calH -- D^0_twisted is not merely "hard to compute",
it is LITERALLY ABSENT from every computation done in this experiment so
far, including the L4B result. (This does not invalidate L4B -- Round
10/11 already established D^0_twisted=0 on rho=trivial specifically,
independent of this fact. But it means: for rho != trivial, essentially
ALL of D^2's true content beyond the algebraic calH^2 piece is still
completely unknown, not just "the correction term".)

### calH^2 = 4*D^2 computed directly (safe -- pure matrix square of the
### already-built, already-equivariance-verified D), decomposed per
### SU(3)-irreducible piece within S+(x)S- (the physically relevant domain)

Using explicit basis vectors adapted to each SU(3) irrep within the 16-dim
S+(x)S- (matching preprint.tex's own branching 8+3+3bar+2x1):
  "3"  piece {y1(x)1, y2(x)1, y3(x)1}:               D^2 = 2/3  (scalar, verified block-scalar)
  "3bar" piece {y123(x)y12, y123(x)y13, y123(x)y23}: D^2 = 10/3 (scalar, verified block-scalar)
  "8"  piece (complement of v_a in the 9-dim {y1,y2,y3}(x){y12,y13,y23}):
       D^2 = 0 EXACTLY -- computed the full 9x9 submatrix, confirmed rank-1
       structure with v_a as the ONLY nonzero-eigenvalue direction (matching
       the already-known D^2(v_a)=v_a+3v_b when projected back onto this
       9-dim slice); the 8-dimensional complement is annihilated identically
       by the algebraic (calH-only) part of D^2.
  "1"x2 (trivial-mult-2): D^2(v_a)=v_a+3v_b (already known, Round 6-9);
       D^2(v_b) not yet separately computed this round.

These are REAL, computed, algebraic-part-only numbers -- useful building
blocks, but do NOT by themselves answer the rho=7 question (see next
section for why).

### The anticommutator {D^0_twisted, calH}: re-derived carefully, unifies
### onto the SAME missing ingredient as the V_7 route

Expanded {D^0_twisted,calH}(eta(x)xi) term-by-term (8 pieces, tracked
individually this time, not shortcut). Two of the eight terms combine
cleanly via Agricola's own Lemma 3.3 (the UNTWISTED anticommutator
{e_p,H} = -(3/2)*sum_{jk}T(j,k,p)*e_j.e_k, itself PURELY algebraic and
already computable from T(i,j,k)): this piece resolves to
sum_p K_p . e_p(eta) (x) xi, K_p:=-(3/2)sum_jk T(j,k,p)e_j.e_k -- still
containing the bare true-derivative e_p(eta), not yet eliminated.

Found a genuinely useful NEW tool for the DIAGONAL part of second
derivatives: Agricola's own definition Omega_g := -sum_p e_p^2 + C_h
(page 9-10) rearranges to sum_p e_p^2(psi) = C_h(psi) - Omega_g(psi).
Since Omega_g(psi)=C_2(G2;rho)*psi is KNOWN for any given rho (e.g. 4 for
rho=7), and C_h (the su(3)-Casimir lifted into the Clifford algebra) is
ITSELF purely algebraic and computable the SAME way H was built --
via SU3_GENERATORS structure constants instead of torsion T(i,j,k) --
this gives sum_p e_p^2(psi) EXPLICITLY in terms of already-computable
data, for ANY rho, once C_h is built (not yet built this round, but
confirmed tractable -- same technique as g2su3_H_element.py, swapping
the input structure-constant table).

**But this only resolves the DIAGONAL sum sum_p e_p^2.** Fully expanding
(D^0_twisted)^2 and the REMAINING six anticommutator terms requires
individual OFF-DIAGONAL second-derivative commutators e_p(e_q(psi)) for
p!=q, which decompose (standard Lie-group fact) as
  e_p(e_q(psi)) - e_q(e_p(psi)) = [e_p,e_q](psi) = [e_p,e_q]_m(psi) + [e_p,e_q]_h(psi)
The m-part is a computable first-derivative direction (via T(p,q,k)) --
fine. The h-part, [e_p,e_q]_h(psi) = -ad([e_p,e_q]_h)~.psi (Lemma 3.4),
requires the INDIVIDUAL su(3)-valued curvature element [e_p,e_q]_h for
EACH pair (p,q) -- this is EXACTLY the "Jac_h-as-a-2-form" curvature data
that the failed V_7 ansatz (Round 6/8) was also trying to reach, and
which Round 6's Jac_h=-Jac_m identity does NOT supply (that identity is
about the totally-antisymmetric TRIPLE bracket Jac_h(X,Y,Z), a different
object from the single bilinear curvature 2-form [e_p,e_q]_h needed here).

**Conclusion: the twisted-anticommutator route and the V_7 route were not
actually independent alternatives -- both terminate at the SAME missing
ingredient (the su(3)-valued curvature 2-form of the canonical connection,
[e_p,e_q]_h for individual pairs p,q). This is genuine progress: the
problem is now precisely localized to ONE well-defined missing object,
not vaguely gestured at across two different unsuccessful approaches.**

### Most promising concrete next step identified (not yet attempted)

The Ambrose-Singer theorem states the CANONICAL (t=0) connection's
curvature is PARALLEL, with the standard relation R^0(X,Y) = -ad([X,Y]_h)|_m
for X,Y in m -- i.e. the canonical curvature IS essentially [e_p,e_q]_h
(up to the sign/ad-embedding already used throughout this experiment).
AHL2023 Proposition 5.4 (already read this session, gave the explicit
Ambrose-Singer TORSION T^AS) may adjacent-ly give or imply this curvature
data for exactly S^6=G2/SU(3) -- this was not fully extracted when the
paper was read earlier this session (only the torsion 3-form was pulled
out). Re-reading AHL2023's Section 5.1 / Proposition 5.4 specifically for
the CURVATURE (not just torsion) statement is the most promising next
step -- lower risk than re-deriving [e_p,e_q]_h from scratch via a new
V_7 ansatz, since it reuses an ALREADY-VERIFIED primary source rather than
introducing new unverified structure.

### Status: task #7 still OPEN. Real, concrete progress this round
### (calH^2 fully known per irrep; the two previously-separate blockers
### unified into one precisely-identified missing object; a concrete,
### lower-risk next step identified). No forced conclusion on rho=7.

## Round 13 (2026-07-09): BREAKTHROUGH -- the missing su(3)-curvature
## 2-form [e_p,e_q]_h is now fully known and independently validated,
## closing Round 12's precisely-identified blocker. rho=7's final
## numeric answer is NOT yet computed (that assembly step remains), but
## the last missing INGREDIENT is now in hand.

### Found the actual source: AHL2023 Appendix A (not Proposition 5.4 itself)

Proposition 5.4 gives ONLY the Ambrose-Singer torsion (already known,
matches T(i,j,k) exactly). The curvature data lives in **Appendix A**
(Lemma A.1, Remark A.2, Proposition A.3) -- an explicit construction of
g2 (and su(3)) as the stabilizer of spinors in spin(7)'s real 8-dim spin
representation, giving ALL 14 g2 generators nu_1..nu_14 as EXPLICIT 8x8
matrices (products of 7 Clifford generators rho(eps_1)..rho(eps_7), each
itself an explicit sum of antisymmetric elementary matrices). This gives
FULL g2 structure constants via ordinary matrix commutators [nu_i,nu_j] --
not just the isotropy action or the torsion, but everything.

### First transcription attempt failed calibration -- caught, not covered up

Initial OCR-based extraction (via the same doc_bridge tool used all
session) of the nu_9..nu_14 formulas had MULTIPLE sign errors (nu_5,
nu_8, nu_9, nu_10, nu_11, nu_12, nu_13, nu_14 all had at least one wrong
sign). Caught immediately by the SAME calibration discipline used
throughout this whole experiment: built [nu_i,nu_{8+p}] (i=1..8 su(3)
generator, p=1..6 m-direction) and checked against Remark 5.2's ad(nu_i)|_m
formulas (already trusted and used throughout this session as
SU3_GENERATORS) -- ALL 48 pairs failed. Re-extracted via PyMuPDF's direct
PDF text layer (fitz library, available on this machine) instead of
doc_bridge's OCR-style parsing -- much cleaner, and the corrected formulas
are documented verbatim in g2su3_appendix_a_construction.py's docstring
for future reference (do not revert to the OCR version).

### Second calibration round: found a clean, uniform sign-convention flip

With corrected formulas, 7 of 8 su(3) generators (i=1..7) calibrated
EXACTLY once a single global sign flip was applied: [nu_i,e_p] =
-ad(nu_i)(e_p) (verified: the ratio comm/expected was EXACTLY -1 at every
nonzero matrix entry, not an inconsistent pattern -- a clean orientation-
convention difference, not a data error). Generator i=8 (the su(3) Cartan
element) still did not calibrate even with this flip -- diagnosed as a
genuine, separate residual issue (not simply explained), but this
generator is NOT needed as an INPUT for the actual computation (it only
appears as one possible OUTPUT component when decomposing brackets), so
this was not chased further -- flagged honestly rather than silently
ignored (g2su3_appendix_a_construction.py's calibration output records
this explicitly).

### The decisive check: [e_p,e_q] computed directly, decomposed against
### the full 14-dim g2 basis, m-part cross-checked against trusted T(p,q,k)

Computed the bracket [e_p,e_q] for all 15 pairs p<q in 1..6 directly as
8x8 matrix commutators (using the validated nu_9..nu_14), decomposed
against ALL 14 basis elements via Tr(nu_k^T M) (using the independently-
confirmed fact that Tr(nu_k^T nu_k)=1 exactly for all k=1..14, i.e. the
B_0-orthonormality Appendix A claims). Applying the SAME uniform sign
correction found above (BRACKET_SIGN=-1): **the m-part (su(3)-irrelevant
components, nu_9..nu_14) reconstructs T(p,q,k) EXACTLY for all 15 pairs,
100% match, zero exceptions.** This is strong, independent validation
that the whole nu_9..nu_14 construction (and hence the h-part extracted
alongside it) is correct -- the m-part cross-check uses ALREADY-TRUSTED
data (T(i,j,k), itself independently matched against AHL2023 Prop 5.4's
published torsion earlier this session) as the ground truth, and the
SAME decompose_g2 machinery produces both the m-part and h-part
simultaneously, so a correct m-part is strong evidence the h-part is
correct too.

### Result: the full su(3)-valued curvature 2-form, validated

  [e_1,e_2]_h = -1/2 nu_1 + (sqrt(3)/18) nu_8
  [e_1,e_3]_h = -1/2 nu_7
  [e_1,e_4]_h = 1/2 nu_6
  [e_1,e_5]_h = 1/2 nu_5
  [e_1,e_6]_h = -1/2 nu_4
  [e_2,e_3]_h = -1/2 nu_6
  [e_2,e_4]_h = -1/2 nu_7
  [e_2,e_5]_h = 1/2 nu_4
  [e_2,e_6]_h = 1/2 nu_5
  [e_3,e_4]_h = 1/2 nu_1 - (5 sqrt(3)/18) nu_8
  [e_3,e_5]_h = -1/2 nu_2
  [e_3,e_6]_h = 1/2 nu_3
  [e_4,e_5]_h = -1/2 nu_3
  [e_4,e_6]_h = -1/2 nu_2
  [e_5,e_6]_h = (2 sqrt(3)/9) nu_8

Saved as `build_curvature_h_table()` in g2su3_appendix_a_construction.py,
returning {(p,q,k): coeff} for reuse. This is EXACTLY the missing
ingredient identified in Round 12 -- the individual su(3)-curvature
2-form needed for the off-diagonal second-derivative commutators in
{D^0_twisted, calH} and (D^0_twisted)^2.

### What this does NOT yet give: the final rho=7 numeric answer

Having [e_p,e_q]_h closes the LAST missing ingredient, but assembling it
into a final (D^{1/2}_twisted)^2 eigenvalue on the rho=7 isotypic
component still requires carefully completing the FULL twisted analog of
Agricola's Theorem 3.2 derivation (all 8 anticommutator terms from Round
12, now with e_p(e_q(psi))-type off-diagonal commutators resolvable via
this curvature data plus the T(p,q,k)-based m-part) -- a genuine, careful
assembly task, not yet attempted. This is the concrete next step for the
next session: use curvature_h (this round) + T(p,q,k) (already known) +
C_h (buildable the same way as H, per Round 12's note) to complete the
derivation, OR alternatively use curvature_h directly to build G2's
action on V_7 properly this time (Round 6/8's failed rolling-map ansatz
can likely now be FIXED using this validated curvature data, since the
missing piece there was exactly this same su(3)-curvature information).

### Status: task #7 still OPEN, but the blocker identified in Round 12 is
### CLOSED. This is the deepest this investigation has gotten -- all
### structural ingredients (T, H, calH, curvature_h) are now validated
### and available; only the final assembly into a numeric rho=7 verdict
### remains.

## Round 14 (2026-07-09, same day, user asked to assemble the final rho=7
## answer): V_7 (Round 6/8's original blocker) is NOW FIXED using the
## validated Appendix A data -- a SECOND major breakthrough -- but a
## genuine normalization ambiguity was found and must be resolved before
## a final numeric verdict can be trusted. NOT YET the final answer.

### V_7 correctly constructed, two independent validations passed

AHL2023 Lemma A.1 states g2 = stab_{spin(7)}{phi_1}, su(3) = stab{phi_1,phi_2}
for phi_1,phi_2 the FIRST TWO STANDARD BASIS VECTORS of the real spin
representation Sigma_7=R^8 (not something requiring separate solving).
Verified DIRECTLY: phi_1=(1,0,...,0) is killed by all 14 g2 generators
nu_1..nu_14 (confirmed only after fixing an additional nu_8 transcription
error, see below); phi_2=(0,1,0,...,0) is killed by exactly the 8 su(3)
generators nu_1..nu_8 (not by nu_9..nu_14, as expected).

Given this, **V_7 := phi_1^perp (7-dimensional) is G2's fundamental
representation**, with G2's FULL action given by simply restricting the
already-validated nu_1..nu_14 matrices to this 7-dim subspace (rows/cols
2-8) -- since every nu_k kills phi_1, each nu_k automatically preserves
phi_1^perp too (antisymmetric matrices with a zero column automatically
have a zero row, by antisymmetry). **This directly fixes Round 6/8's
failed "rolling map" ansatz** -- no guessing required, just restriction
of already-calibrated data.

### Found and fixed a SECOND independent nu_8 transcription error

phi_1 was NOT killed by the ORIGINAL Round 13 nu_8 formula
(-rho1rho2-2rho3rho4+rho5rho6) -- diagnosed as yet another stacked-
fraction transcription ambiguity from the PDF (same failure mode as
Round 13's first nu_9..14 attempt, now hitting nu_8 specifically, which
had ALREADY shown a separate calibration anomaly in Round 13 that was
set aside at the time as "not needed as an input"). **Solved directly
via a linear system** (not guessed): treating nu_8 = a*rho1rho2 +
b*rho3rho4 + c*rho5rho6 as unknowns and requiring [nu_8,e_p] =
-ad(nu_8)(e_p) for all p=1..6 (the SAME trusted Remark 5.2 data used
throughout) gives the UNIQUE solution a=c=-1, b=+2 (up to overall
1/(4sqrt3) scale): nu_8 = (1/(4sqrt3))(-rho1.rho2 + 2.rho3.rho4 - rho5.rho6).
With this correction: **all 8/8 su(3) generators now calibrate exactly**
(comm=-expected, zero exceptions, up from 7/8 in Round 13), the m-part
cross-check against T(p,q,k) still passes 100% (unaffected, as expected),
AND phi_1 is now killed by all 14 generators. The curvature_h table
values also became visibly cleaner (e.g. nu_8 coefficients now
sqrt(3)/6, sqrt(3)/6, -sqrt(3)/3 instead of the messier sqrt(3)/18,
-5sqrt(3)/18, 2sqrt(3)/9) -- clean fractions after a correction is itself
a mild positive signal, though not proof on its own.

### Cross-check via the Casimir operator -- structure confirmed, and the
### apparent normalization discrepancy found here is RESOLVED below

(Committed as `g2su3_V7_calibration_check.py` -- phi_1/phi_2 kill checks
+ both Casimir computations, re-runnable.) Computed C_2 := -sum_{k=1}^{14}
(nu_k restricted to V_7)^2 directly.
**Result: EXACTLY 2*Identity_7x7** (a clean scalar -- a real, non-trivial
structural validation, since an incorrectly-built representation would
generically NOT give a pure scalar here; strictly, a scalar Casimir is
CONSISTENT with irreducibility via Schur's lemma, not independently
sufficient to prove it in general, since a reducible sum of
non-isomorphic irreps with coincidentally equal Casimir eigenvalues would
also give one -- but for THIS specific case it does establish
irreducibility, because G2's next-smallest nontrivial irrep after the
trivial IS the 7 itself, so no other combination of small G2-irreps could
sum to dimension 7). As a further check, computed
the analogous Casimir for su(3) acting on its OWN adjoint (8-dim, via
ad(nu_i) for i=1..8 on span{nu_1..nu_8}): **result EXACTLY 3*Identity_8x8**,
matching the preprint's own cited C_2(SU(3);adjoint)=3 EXACTLY, no
rescaling needed.

**The discrepancy (as first found):** the preprint (and this whole
experiment, following Agricola 2002's stated convention) uses
C_2(G2;7)=4, but my direct computation in AHL2023's own B_0-orthonormal
basis gives C_2(G2;7)=2 -- a factor-of-2 difference. Critically, this is
NOT a uniform rescaling between the two papers' conventions (which would
also show up in the su(3) check, and it did NOT -- su(3)'s Casimir
matched 3=3 exactly with zero rescaling needed).

### RESOLVED (same round, follow-up): root-system Casimir check confirms
### C_2(G2;7)=2 is CORRECT in this experiment's own units -- Agricola's
### "4" uses a different, but standard and fully identifiable, convention

Rather than trust memory about which convention Agricola 2002 uses,
computed BOTH C_2(G2;7) and C_2(G2;14) completely independently, from
G2's abstract root system (Cartan matrix, fundamental weights, Weyl
dimension formula + Casimir formula (lambda,lambda+2*delta)), in the
explicit, standard "long root^2=2" convention
(`g2su3_casimir_convention_check.py`, tool-verified via sympy, not
recalled from memory). Result: **dim(1,0)=7 with C_2=4, dim(0,1)=14 with
C_2=8** in that convention -- confirming Agricola's "(1,0)" label
genuinely does mean the 7-dimensional representation (no labeling
mismatch), and her "C_2=4" is exactly the standard "long root^2=2"
value.

Separately, re-deriving what convention AHL2023's B_0-orthonormal basis
implicitly uses: the su(3) check (C_2(adjoint)=3 in the nu-basis,
TOOL-VERIFIED both via `g2su3_casimir_convention_check.py`'s ad(nu_i)
computation and independently again in `g2su3_V7_calibration_check.py`)
matches the STANDARD PHYSICS convention Tr(T^aT^b)=(1/2)delta^ab (where
C_2(adjoint SU(N))=N, giving 3 for N=3) -- NOT the "long root^2=2"
convention (which would give C_2(adjoint SU(3))=2*h^v=6 for su(3)'s dual
Coxeter number h^v=3 -- **this "6" figure itself is [MEMORY]/[INFERRED]
from the standard Lie-theory relation C_2(adjoint)=2*(dual Coxeter
number), not independently computed by any script this round**; it is
not load-bearing for the resolution, which only needs the ALREADY
tool-verified 3-vs-6-would-be relationship's DIRECTION, not this exact
value). The "physicist" convention is exactly HALF of
"long root^2=2" uniformly across ALL representations of a given algebra
(root length^2=1 instead of 2 rescales every Casimir eigenvalue by
1/2, since C_2 is linear in the bilinear form used to define it). Halving
G2's own "long root^2=2" values: C_2(7): 4/2=**2** (matches my direct
8x8-matrix computation EXACTLY), C_2(14): 8/2=**4**.

**Conclusion: the "discrepancy" is a real, now fully-explained, uniform
factor-of-2 convention mismatch between Agricola 2002 (long root^2=2,
the common math-literature/Killing-form convention) and AHL2023's B_0
basis (the standard physics Tr(T^aT^b)=delta^ab/2 convention) -- NOT a
labeling confusion, NOT an error in either source, and NOT specific to
G2 vs SU(3) (SU(3) simply happened not to expose it because the preprint
already re-states SU(3)'s Casimir in the halved/physics convention,
while its citation of Agricola's G2 figure was left in her original
un-halved convention -- an internal citation-convention mismatch inside
the preprint's own text, now identified precisely). This is exactly a
Type-1 error in the research-methodology.md classifier ("symbolic
overload": the SAME symbol C_2(G2;7) denoting two numerically different
but both-legitimate quantities in the two source papers).

**Resolution for this experiment: use C_2(G2;7)=2, C_2(G2;14)=4** (the
AHL2023/B_0-basis values) for ALL further computation here, since T, H,
calH, calH^2, and curvature_h are already built in that exact basis --
using Agricola's "4"/"8" here would silently mix conventions.

C_2(SU(3);3) was ALSO independently tool-verified in this same basis
(not just recalled from the standard (N^2-1)/(2N) formula): applying
`su3_casimir_action_squared` (the project's own already-calibrated su(3)
action, `g2su3_twisted_kernel.py`, same machinery used for Round 12's
calH^2-per-irrep decomposition) to y1 and y12 gives
sum_i rho(nu_i)^2 = -4/3 * (eigenvector) exactly on BOTH the "3" (y1) and
"3bar" (y12) pieces, i.e. C_2(SU(3);3) = C_2(SU(3);3bar) = -(-4/3) =
**4/3**, matching the standard formula AND consistent with
C_2(SU(3);adjoint)=3 in the same convention.

The non-trivial-component worst-case gap for rho=7 (against sigma=3,
using Round 12's calH^2 value of 2/3 on that piece) is
C_2(G2;7) - C_2(SU(3);3) + [correction] = 2 - 4/3 + 2/3 = **4/3 > 0**
in the algebraic part alone (still positive, smaller margin than the
uncorrected-convention "4-4/3+2/3=10/3" naive read [reviewer-caught
arithmetic slip, 2026-07-09: this parenthetical originally said "8/3",
which is wrong; 4-4/3=8/3, +2/3=10/3 -- corrected, does not affect the
4/3 result actually used above, which was independently verified
correct], but a real, now internally-consistent, tool-verified number
rather than an unresolved question) -- NOTE this is only the
algebraic/calH contribution to the gap and is NOT yet the full rho=7
answer (see below, the rho-dependent true-derivative piece via V_7
sections is still not included in this number).

### Status: V_7 blocker (Round 6/8) now CLOSED via validated Appendix A
### restriction -- a real, second major breakthrough this round, with two
### independent structural validations (phi_1 annihilation, exact scalar
### Casimir). The C_2(G2;7)=2-vs-4 puzzle is ALSO now CLOSED (root-system
### computation, `g2su3_casimir_convention_check.py`) -- a clean,
### fully-explained convention mismatch, not a bug. The FINAL rho=7
### numeric verdict is STILL NOT computed -- what remains is assembling
### the actual 4-dim multiplicity space Hom_SU(3)(V_7, S+(x)S-) and
### extending calH/nabla_g to it via the SAME Leibniz pattern already
### used to build D_on_simple_tensor from H (V_7 provides the missing
### rho-dependent true-derivative piece; Round 10 established that
### reading rho=7 data directly off fiber-level 3/3bar/8 blocks, as
### attempted in Rounds 6-9, is NOT valid -- multiple rho's share each
### fiber sigma-type, so the isolation must go through V_7 explicitly).
### This is a well-defined, scoped next step, not an open-ended search --
### but it is a genuinely new construction (not yet done), so no final
### kernel verdict is claimed this round.

## Round 14 continued (2026-07-09, same session): found and fixed a REAL
## sign error in Theorem 3.2's transcription -- RETRACTS Round 11's
## "encouraging" Delta(1/2)>0 finding for rho=7. L4B is UNAFFECTED
## (independent computation). This is a correction, not a new blocker.

### What happened

Attempting to build the twisted quartic (curvature) term needed for the
FULL rho=7 assembly (see task list above), re-read Agricola 2002
Theorem 3.2 directly from the PDF via PyMuPDF (the reliable method
established this session), specifically to pin down the exact
definition of Jac_h needed to use curvature_h correctly. Found the PDF's
actual quartic-term bracket is:
  <Zi, Jac_h(Zj,Zk,Zl) + 9t^2 Jac_m(Zj,Zk,Zl)>
(Jac_h carries NO t-factor, Jac_m carries the 9t^2 factor). Compared
against what an EARLIER round (Round 6, "Investigating the danger zone")
had transcribed into this file: "<Zi,Jac_m(Zj,Zk,Zl)> + 9t^2
Jac_h(Zj,Zk,Zl)" -- Jac_h and Jac_m are SWAPPED relative to the actual
paper. That earlier transcription was made before PyMuPDF was
established as more reliable than doc_bridge OCR this session (see
Round 13's own note about doc_bridge introducing sign errors elsewhere).

### Independent confirmation (not just re-reading more carefully)

Rather than trust a second reading of the same page, built (Ctilde_h)_4
-- Agricola's Proposition 3.3 degree-4 term of the su(3)-Casimir lifted
into the Clifford algebra -- DIRECTLY from curvature_h (Round 13's data,
built from AHL2023 Appendix A, a COMPLETELY SEPARATE source/computation
from H/torsion) via the PDF's own Jac_h definition
(Jac_h(X,Y,Z):=[X,[Y,Z]_h]+[Y,[Z,X]_h]+[Z,[X,Y]_h]), and checked whether
it satisfies the identity forced by Jac_h=-Jac_m (already established,
Agricola Section 2): (Ctilde_h)_4 = -(1/9)(H^2)_4. **Confirmed exactly,
zero residual, sympy-verified** (`g2su3_delta_correction.py` docstring
now documents the check inline). Since this identity only holds under
the CORRECTED sign convention, and it was verified via curvature_h data
that has NOTHING to do with the original transcription error, this is
genuine independent confirmation, not just "read the PDF again and
believe it more."

### Why the t=1/3 sanity check didn't catch this

`g2su3_delta_correction.py`'s existing calibration ("Delta(1/3) must be
EXACTLY ZERO") passes for BOTH the old (buggy) and new (corrected) sign,
because the quartic term's prefactor (1-9t^2) is IDENTICALLY ZERO at
t=1/3 regardless of the sign in front of it -- the calibration point
is structurally insensitive to exactly the bug it exists to catch. A
real example of "a passing test doesn't mean the tested thing is right
at OTHER points" -- worth remembering for any future t-dependent
calibration in this experiment.

### Corrected result -- RETRACTS the Round 11 "encouraging" claim

Fixed `quartic_term()` in `g2su3_delta_correction.py`
((1-9t^2)->(9t^2-1), both /9 * H2_4). Re-ran: Delta(1/3)=0 still holds
(uninformative here, as explained above). **Delta(1/2) on the 3(+)3bar
piece is now EXACTLY 0** (was wrongly reported as +5/6 in Round 11/the
"Consequence for rho=7" section above -- that number is WRONG, computed
with the sign-bugged code, and is hereby retracted). Delta(1/2) on the
trivial-mult-2 piece {1,y123} is now the 2x2 matrix [[5/3,-2sqrt3],
[-2sqrt3,5/3]] (was [[-5/6,-2sqrt3],[-2sqrt3,-5/6]] -- also wrong,
retracted).

### Does this affect L4B? NO -- confirmed independent

L4B's rank(D+|trivial)=1 result was computed via a COMPLETELY SEPARATE
method (D_on_simple_tensor/calH applied directly to v_a, v_b in the
TWISTED Sigma(x)Sigma space, g2su3_twisted_kernel.py /
g2su3_find_invariant.py / g2su3_compute_crossterm.py) and cross-validated
4 independent ways (calibration vs AHL2023 Thm 5.1, 2 skeptic stress
tests, SU(3)-equivariance, chirality/branching) -- NONE of these used
g2su3_delta_correction.py or its quartic_term function. L4B stands,
fully unaffected by this bug.

### Does this affect the rho=7 gap conclusion reached earlier this round?
### Partially -- one piece of supporting evidence is retracted, the other
### (independent) piece is unaffected

The algebraic worst-case gap computed earlier THIS round (2-4/3+2/3=4/3>0,
via Round 12's calH^2 on the TWISTED "3" fiber piece) is UNAFFECTED --
that computation used D_on_simple_tensor/calH on Sigma(x)Sigma directly,
never g2su3_delta_correction.py's untwisted Delta(t). It is ALSO,
however, per this file's own earlier caution, INCOMPLETE on its own
(missing the twisted quartic/curvature correction, which is exactly what
this round was attempting to build when this bug was found -- see next
section).

The RETRACTED claim was Round 11's SEPARATE, untwisted-operator PROXY
computation ("Delta(1/2)>0 on 3(+)3bar, doesn't threaten the gap") --
this was always flagged as only a proxy for the real twisted operator,
never load-bearing on its own, but it WAS cited (by this session, in the
status report to the user) as one of two pieces of "positive partial
evidence" for rho=7 being safe. That specific claim is now corrected to:
the untwisted proxy is NEUTRAL (exactly zero), not positive. Neither
alarming nor reassuring -- genuinely uninformative on its own now.

### Net effect on rho=7 status

No change to the OPEN status of the final verdict (task #7 remains
in_progress). What DID change: one of two "no red flags" data points
softens from "actively positive" to "exactly neutral" -- still zero red
flags, but weaker margin of comfort than previously stated. The
TWISTED quartic/curvature term (needed to complete the REAL rho=7
computation, not just this untwisted proxy) is now the concrete next
step, and this round's work directly supplies what's needed for it:
curvature_h (Round 13) plus the now-verified (Ctilde_h)_4=-(1/9)(H^2)_4
identity, EXTENDED via the same Leibniz pattern used to build calH from
H (calH_twisted's quartic analog, not yet built).

### Session lesson (Pearl, process-level)

Attempting to build downstream twisted machinery forced a careful
re-read of upstream formula details that had been transcribed 5+ rounds
earlier and never re-verified -- catching a real bug that a SEPARATE,
purely algebraic sanity check (Delta(1/3)=0) was structurally unable to
catch. This is the SAME class of lesson as nu_8's three-round correction
saga: a calibration that passes is evidence FOR the calibrated point,
not proof of correctness elsewhere in a t-dependent (or otherwise
parametrized) formula -- especially when the calibration point makes the
buggy coefficient vanish identically. Any future t-dependent or
parameter-dependent formula in this experiment should be checked at (at
least) two DIFFERENT, non-degenerate parameter values, or via an
independent data path as done here (curvature_h vs H^2), not just the
one "nice" value where most terms cancel.

## Round 15 (2026-07-09, same session, user asked to "build the twisted
## quartic term"): built and equivariance-verified a genuine new
## component (twisted_Ch), but the ASSEMBLY into the final D^2 formula
## FAILS a direct L4B calibration check -- a real structural blocker,
## not a sign slip, documented honestly rather than forced.

### What was built (`g2su3_twisted_Ch_attempt.py`, committed)

Leibniz-extended Agricola's C_tilde_h (Proposition 3.3, the su(3)-Casimir
lifted into the Clifford algebra -- the ingredient identified in Round
14 continued as the missing twisted-curvature piece) to Sigma(x)Sigma:
  twisted_Ch(eta(x)xi) := (Ch.eta)(x)xi
      + (1/4) sum_{p,q=1..6,p!=q} (Zp.Zq.eta)(x)([Zp,Zq]_h.xi)
using curvature_h (Round 13) for [Zp,Zq]_h and the already-trusted
su3_action (the SAME Clifford-algebra lift used throughout this whole
experiment) for its action on xi. This is a NEW 64x64 matrix, not a
restatement of anything already computed.

### Two genuine passes (real evidence the construction itself is sound)

1. **SU(3)-equivariance: EXACT, zero residual, all 8 generators**
   ([twisted_Ch,su3_i]=0 for i=1..8) -- a non-trivial, non-automatic
   check (this is NOT guaranteed by construction; a wrong sign or index
   anywhere in the curvature_h/su3_action assembly would very likely
   have broken it, the same way earlier equivariance checks this session
   caught real errors).
2. **twisted_Ch(v_a) = 0 and twisted_Ch(v_b) = 0 EXACTLY** -- clean,
   and structurally consistent with the UNTWISTED C_h ALSO being exactly
   zero on the analogous {1,y123} singlet-pair piece (independently
   re-verified this round: untwisted Ch diagonal is
   [0,4/3,4/3,4/3,4/3,4/3,4/3,0], zero on the 1st and last (singlet)
   slots, 4/3 -- matching the tool-verified C_2(SU(3);3)=4/3 -- on the
   "3"/"3bar" slots).

### The failure (the actual finding this round)

Naively assembling the twisted analog of Agricola's UNTWISTED closed
formula (D^{1/2})^2 = Omega_g - H + Ctilde_h + (1/4)H^2 TERM-BY-TERM
(H->calH, Ctilde_h->twisted_Ch, H^2->calH^2) and testing against the
L4B ground truth (D^2(v_a)=D^2(v_b)=v_a+3*v_b, independently verified
this round by direct matrix squaring of the ALREADY-VALIDATED
D_on_simple_tensor, no new assumptions):

  0(Omega_g,rho=trivial) - calH(v_a) + twisted_Ch(v_a) + (1/4)calH^2(v_a)
  = 0 - (-2*sqrt(3)*w) + 0 + (v_a+3*v_b)
  = v_a + 3*v_b + 2*sqrt(3)*w   != v_a + 3*v_b (the TRUE, known answer)

A clean, nonzero, exactly-computed residual of +2*sqrt(3)*w -- not a
near-miss or a rounding artifact, a definite mismatch, entirely
attributable to the "-calH(v_a)" linear term (which independently equals
-2*sqrt(3)*w, exactly matching calH=2*D_on_simple_tensor's own
already-established action on v_a).

### Diagnosis: a real structural mismatch, not a sign bug

Agricola's H (untwisted) is a chirality-flipping ENDOMORPHISM WITHIN the
single 8-dim Sigma (Sigma=S+(+)S- as ONE space containing both
chiralities together) -- H:S+->S- and S-->S+ both stay inside the SAME
8-dim Sigma, so "-H" is a well-defined additive term in an endomorphism
of Sigma, and D^2 (an endomorphism of Sigma) can legitimately include it.

The TWISTED calH, by contrast, maps the 16-dim S+(x)S- slice to the
DIFFERENT 16-dim S-(x)S- slice of the 64-dim Sigma(x)Sigma (only the
LEFT tensor factor's chirality flips, per this whole experiment's own
established D_on_simple_tensor Leibniz convention -- Clifford
multiplication acts on the left/eta factor only). "-calH(v_a)" therefore
genuinely lands in a DIFFERENT subspace (S-(x)S-, specifically the
w=1(x)1 slot) than v_a+3*v_b (which lives in S+(x)S-) -- it cannot
simply cancel additively against terms (Omega_g, twisted_Ch, calH^2)
that all correctly preserve S+(x)S-.

This means Theorem 3.2's closed-form decomposition does not carry over
via a naive term-by-term Leibniz substitution: the paper's PROOF (not
just its stated result) is specific to a single Clifford module C(m)
acting on one spinor bundle S, and does not address a Leibniz-twisted
operator D_{S(x)E} mapping between two different slices of a
tensor-product bundle. Properly generalizing Theorem 3.2 to this setting
needs its own derivation from the index-level manipulations in
Agricola's proof (Lemma 3.3/3.4, Proposition 3.4's computation), NOT a
substitution into the already-closed-form single-bundle result -- a
genuinely new, nontrivial piece of work, not yet attempted.

### Status: BLOCKED, honestly, not forced

This is qualitatively DIFFERENT from every other correction this session
(nu_8's three attempts, the Jac_h/Jac_m sign swap) -- those were
transcription/sign errors with a definite right answer waiting to be
found. This is a genuine open QUESTION about how a proven single-bundle
theorem generalizes to a twisted operator, which the cited literature
does not directly answer. Per this project's Stuck Detection protocol
(Tier 1: quick retry -- done, found the equivariance pass; Tier 2:
context refresh via re-reading the primary source -- done, this IS how
Round 14's sign bug was found; Tier 3: strategy switch needed), this is
flagged for a dedicated future round with a FRESH derivation strategy
(e.g. redo Agricola's Proposition 3.4-style index computation directly
for D_{S(x)E}, or search for literature on twisted Kostant-Parthasarathy
formulas specifically), rather than pushed further here at risk of a
4th silent error this session.

Task #7 (rho=7,14 torsion correction) remains explicitly in_progress,
NOT closed, NOT falsified -- genuinely open, with a clearly diagnosed
blocker and a preserved, reusable partial artifact (twisted_Ch, equivariant
and correctly zero on the singlet pieces) for whoever picks this up next.

### Pearl (process-level)

observation: a construction can pass EVERY individual verification
available (equivariance, clean zero on an expected piece) and still fail
when assembled into the target formula -- individual-component
correctness does not imply assembly correctness, especially when
combining objects that live in structurally different spaces (a single
bundle vs. a twisted tensor-product bundle). The L4B ground truth (a
FULLY independently established fact, not derived from Theorem 3.2 at
all) was exactly the right tool to catch this: an assembly-level
calibration check, not just component-level ones.
falsifiable_prediction: a correctly-generalized twisted Theorem 3.2 must
reproduce D^2(v_a)=v_a+3*v_b EXACTLY when restricted to rho=trivial
(Omega_g=0) -- this is now a hard, already-available acceptance test for
any future attempt at this derivation.
trigger_condition: next dedicated session attempting the twisted
quartic/curvature term for rho=7.
next_check: whenever this task is resumed.

## Round 15 continued (2026-07-09, same session): literature search for a
## "twisted Kostant-Parthasarathy formula" -- no ready-made citable result
## found for the exact combination needed, BUT surfaced a genuinely
## better, standard alternative framework not previously used in this
## experiment: t=1/2 IS torsion-free (Levi-Civita), so the STANDARD
## twisted Lichnerowicz-Weitzenbock formula applies directly.

### What was searched (PVF: literature before more computation)

~10 targeted web searches covering: "twisted Kostant-Parthasarathy
formula", Agricola/Friedrich's own later papers on twisted Dirac
operators with torsion, Kostant's own 1999 Dirac-cohomology framework
(twisted cubic operator D_V for arbitrary g-modules V, on equal-rank
reductive G/H), Mehdi-Zierau's "Principal series representations and
harmonic spinors" / "Harmonic spinors on reductive homogeneous spaces"
(explicitly twist Kostant's CUBIC Dirac operator by a finite-dim rep of
H), and Semmelmann-Weingart's "Weitzenbock machine" (general twisted
Dirac operators via generalized gradients).

Two source PDFs (Kostant's own "Dirac Cohomology for the Cubic Dirac
Operator", arXiv:math/0208048, and Agricola-Friedrich's "The Casimir
operator of a metric connection with skew-symmetric torsion",
arXiv:math/0305233) were fetched and read directly via PyMuPDF (WebFetch
itself failed to decode both PDFs' text streams -- consistent with this
whole session's earlier finding that PyMuPDF is more reliable than other
extraction methods for these older LaTeX-generated PDFs).

### Findings

1. **The twisted CUBIC (t=1/3) Kostant-Parthasarathy formula IS
   well-established** (Kostant 1999 "A cubic Dirac operator and the
   emergence of Euler number multiplets", Duke Math J. 100; Mehdi-Zierau
   2006/2014) -- for EQUAL-RANK reductive G/H (G2 and SU(3) both have
   rank 2, so this condition IS satisfied here) and V any finite-dim
   G-module, D_V^2 reduces to a clean Casimir-difference-plus-constant
   formula. This is exactly the "naive KP formula" ALREADY used
   throughout this experiment for t=1/3 (Theorem 3.3's specialization,
   already proved/trusted) -- the literature CONFIRMS this base point,
   it does not give anything NEW beyond what's already in hand.

2. **No paper was found combining torsion (Agricola's general-t Theorem
   3.2) WITH twisting by a coefficient bundle E.** Agricola-Friedrich's
   OWN follow-up paper on the Casimir operator with skew torsion (2003)
   was checked directly and confirmed (via WebFetch's model, then
   independently by reading the fetched PDF) to stay entirely in the
   UNTWISTED (spinor-bundle-only) setting -- no coefficient-bundle
   generalization. Kostant's Dirac-cohomology framework is purely
   Lie-algebraic (no metric/torsion/geometry at all -- it works with
   abstract reductive Lie subalgebras, not naturally reductive metrics).
   This is a genuine, not-yet-searched-around gap, consistent with (not
   contradicting) Round 15's own finding of a real structural obstacle.

3. **Better lead: t=1/2 is EXACTLY the torsion-free Levi-Civita
   connection** (Agricola's torsion form T^t(X,Y,Z)=(2t-1)<[X,Y]_m,Z>
   vanishes identically at t=1/2 -- already knew this, but had not
   previously drawn the consequence). This means the PHYSICALLY relevant
   operator for this whole experiment (t=1/2, used throughout for the
   zero-mode count) is the ORDINARY, torsion-free Riemannian Dirac
   operator on S^6 -- meaning the STANDARD, well-established, textbook
   twisted Schrodinger-Lichnerowicz-Weitzenbock formula applies directly,
   with NO need for Agricola's torsion machinery at t=1/2 specifically:
     D^2_{S(x)E} = nabla*nabla + (1/4)Scal_g + R^E
   where nabla*nabla is the Bochner/rough Laplacian of the FULL twisted
   connection, Scal_g is the (constant, known) scalar curvature of round
   S^6, and R^E is a PURELY ALGEBRAIC, pointwise Clifford-contracted
   curvature-endomorphism term built from E's OWN curvature (E=V_7 here)
   -- this is the standard formula physics/geometry literature states for
   ANY twisted Dirac operator on ANY Riemannian manifold (not
   naturally-reductive-specific, no torsion-family machinery needed).

### Why this is a genuinely different, more promising angle than Round 15's attempt

Round 15's failed attempt tried to Leibniz-extend Agricola's t-FAMILY
decomposition (Omega_g + cubic-H + quartic + scalar, built around the
CANONICAL/torsion connection as the base point, t=0) to the twisted
case -- and hit a real structural mismatch (the cubic H-term's
chirality-flip behavior doesn't respect the twisted bundle's slice
structure). The Lichnerowicz-Weitzenbock route instead takes the
LEVI-CIVITA connection itself (t=1/2, torsion-free) as the base point --
avoiding the "H term" entirely (H only enters when relating DIFFERENT
values of t; if we work directly at t=1/2 rather than building up from
t=0, we never need it). nabla*nabla (Bochner Laplacian) for a HOMOGENEOUS
bundle is standardly known (via Frobenius reciprocity, e.g. Wallach's
book on harmonic analysis on homogeneous spaces) to reduce to a
Casimir-of-G-minus-Casimir-of-isotropy-rep formula -- the SAME kind of
representation-theoretic reduction already used throughout this
experiment, just for a DIFFERENT (torsion-free, Levi-Civita-native)
starting point. R^E is then the ONLY new ingredient needed, and it is
PURELY ALGEBRAIC (pointwise, no derivatives) -- computable, in
principle, from V_7's OWN curvature via the SAME curvature_h data
already validated in Round 13, contracted through V_7's representation
matrices (Round 14) rather than through su3_action's spin-representation
lift.

### Status: NOT attempted this round (time-bounded, avoiding a rushed

### 4th derivation in one session) -- flagged as the recommended next
### strategy, with concrete starting ingredients already in hand:
- V_7's explicit matrices (Round 14, `g2su3_appendix_a_construction.py`
  restricted to rows/cols 2..8)
- curvature_h (Round 13)
- Scal_g for round S^6 of radius rho_6 (should already be known/derivable
  from this experiment's existing S^6 geometry conventions)
- The general formula for R^E on a naturally reductive homogeneous
  bundle at the LEVI-CIVITA connection specifically (needs care: the
  Levi-Civita curvature of an associated bundle on a space with torsion
  at OTHER t-values is NOT simply "-rho_E([X,Y]_h)" -- Agricola's own
  Theorem 2.1 curvature formula, already read this session, gives the
  FULL R^t(X,Y) including the (t-t^2)Qm term, which at t=1/2 gives a
  nonzero (1/4)Qm contribution IN ADDITION to the Qh/isotropy piece --
  this t-dependent piece must be included, not just the naive
  isotropy-curvature guess)

Task #7 remains in_progress. This is a literature-grounded, standard-
framework lead, not a new derivation attempt -- the actual computation
is still future work.
