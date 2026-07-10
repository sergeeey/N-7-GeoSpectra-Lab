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

## Round 16 (2026-07-09, same session, user asked to "try the
## Lichnerowicz-Weitzenbock approach"): the FIRST candidate rho=7 verdict
## with a genuinely complete, multiply-verified construction -- STRICTLY
## POSITIVE eigenvalues on all 3 relevant SU(3) pieces, under BOTH
## interpretations of one remaining, honestly-flagged normalization
## ambiguity. Not yet independently reviewed/skeptic-checked -- see
## Promotion status at the end of this section.

### The route (per Round 15 continued's literature-search lead)

t=1/2 is exactly torsion-free Levi-Civita, so the STANDARD twisted
Schrodinger-Lichnerowicz-Weitzenbock formula applies with no torsion
machinery needed at all:
  D^2_{S(x)E} = nabla*nabla + (1/4)*Scal_g + R^E
This sidesteps Round 15's chirality-mismatch failure entirely: there is
no analog of the "-calH" linear term here (that term only arose from
building UP from t=0 via H; working directly at t=1/2 never needs it).

### Ingredient 1: the FULL Riemann curvature R^{1/2}(e_p,e_q)e_r

Found and used Agricola 2002's GENERAL curvature formula (Lemma 2.2, a
DIFFERENT, more complete statement than the sectional-curvature-only
contraction read in an earlier round):
  R^t(X,Y)Z = t^2[X,[Y,Z]_m]_m + t^2[Y,[Z,X]_m]_m + t[Z,[X,Y]_m]_m
              + [Z,[X,Y]_h]
Building this required pinning down a bracket-sign convention issue:
direct comparison against the ALREADY-CALIBRATED `LEVI_CIVITA_NOMIZU`
data showed `[e_p,e_q]_m = -sum_k T(p,q,k) e_k` -- a UNIFORM minus sign
relative to a naive reading of T as literally `<[e_p,e_q]_m,e_k>`
(confirmed exactly across 12 tested (p,i,j) triples, zero exceptions).
This is consistent with (not contradicting) the SAME kind of
convention-mismatch pattern already found and resolved earlier this
session for the G2 Casimir normalization -- AHL2023's own conventions
differ from Agricola 2002's in more than one place, and each mismatch
found so far has been a clean, uniform, resolvable sign/scale flip, not
an actual error in either source.

**Verified, non-trivially, three independent ways:**
1. R(p,q,r) = -R(q,p,r) (antisymmetry in the first two arguments) --
   holds for all tested triples.
2. <R(p,q)e_r,e_s> = -<R(p,q)e_s,e_r> (skew-symmetry as an so(6)
   operator, required for ANY genuine curvature 2-form) -- holds for all
   tested pairs.
3. **The Ricci tensor obtained by contracting R_half EXACTLY reproduces
   Agricola's OWN, separately-stated Ricci formula** (Lemma 2.2's second
   display, a genuinely different, independent formula from the R^t(X,Y)Z
   one): Ric(e_p,e_p)=5/3 (off-diagonal zero) for all tested p, matching
   `sum_i (t-t^2)<[X,Zi]_m,[Y,Zi]_m> + Qh([X,Zi],[Y,Zi])` computed
   DIRECTLY from T and curvature_h, with NO reference to R_half's own
   construction. Scal^(1/2)=10 (trace), matching a THIRD, even simpler
   scalar-only formula independently. This is the strongest calibration
   evidence in this round -- two structurally different formulas from
   the SAME primary source, cross-checked against each other via
   completely different code paths, agree exactly.

### Ingredient 2: R^E (64x64), the curvature-endomorphism term

R^E(eta(x)xi) := sum_{p<q} (e_p.e_q.eta)(x)(Rspin_half(p,q).xi), where
Rspin_half is R_half's spin(6)/Clifford lift via a general
`spin_lift_so6` function. This lift formula was ITSELF miscalibrated on
the first attempt (a double-counted 1/2 factor: an explicit (1/2)
prefactor stacked on top of `clifford_mult_bivector_direct`'s OWN
internal 1/2) -- caught immediately by a dedicated calibration test
(does `spin_lift_so6` applied to Lambda_m^{1/2}, built independently
from T, reproduce `nabla_g_action` exactly? First attempt: no, by a
uniform factor. Second attempt, correcting BOTH the double-counted 1/2
AND the bracket-sign issue found for Ingredient 1: yes, exactly, for all
tested (p, vec) pairs).

**Verified: R^E is exactly SU(3)-equivariant** (all 8 generators, zero
residual, `build_su3_matrix64`) -- non-automatic (a wrong sign or index
anywhere in the R_half/lift assembly would very plausibly have broken
this, the same way it has caught real errors elsewhere this session).

### The decisive calibration: L4B ground truth, again

Assembled formula, restricted to rho=trivial (Omega_g=0, so
nabla*nabla=0): D^2(v_a) "=" (1/4)*Scal*v_a + R^E(v_a). Computed:
**this equals EXACTLY (2/3) of the TRUE D^2(v_a)** (=v_a+3*v_b,
independently established via direct D_on_simple_tensor^2 matrix
squaring). Critically, this is a CLEAN, UNIFORM scale factor, not a
structural mismatch -- the v_a and v_b COMPONENTS of the result already
match the truth's own internal PROPORTIONS exactly (2/3 of 1 = 2/3, 2/3
of 3 = 2, matching the computed (2/3, 2) exactly). Independently
re-verified on v_b (a second, different test vector): the SAME (3/2)*
correction factor exactly reproduces D^2(v_b) too. This is strong
evidence the CONSTRUCTION is right and only a single overall
normalization constant remains unresolved -- a qualitatively different,
much safer situation than Round 15's structural failure (which gave a
residual in a component that couldn't be fixed by ANY scalar rescaling).

### The remaining ambiguity (honestly flagged) -- and why it doesn't matter here

Not yet resolved from first principles: does the missing 3/2 factor
apply ONLY to (Scal+R^E) [**Interpretation A**], leaving
nabla*nabla=C_2(G2;rho)-C_2(SU(3);sigma) UNSCALED (this rests on
Agricola's own proven Casimir-eigenvalue theorem for Omega_g, PLUS this
session's earlier independent finding that Ctilde_h's eigenvalues equal
C_2(SU(3);sigma) exactly with no rescaling needed -- giving no
particular reason to expect nabla*nabla needs the SAME empirical
correction that Scal/R^E turned out to need) -- or does it apply to the
WHOLE formula UNIFORMLY [**Interpretation B**] (plausible if the source
is a single Clifford-algebra normalization convention mismatch, which
would hit every term the same way). The rho=trivial calibration test
CANNOT distinguish these (nabla*nabla=0 there regardless of scale).

**Resolution used here: report BOTH interpretations and check whether
they agree qualitatively** -- exactly the right move when a genuine
ambiguity can't be resolved cheaply and the question at hand (sign of an
eigenvalue, not its precise value) may not require resolving it.

### The rho=7 result

For rho=7 (branching 7|SU(3) = 3(+)3bar(+)1), evaluated on all 3
relevant SU(3) pieces, using C_2(G2;7)=2 (this session's resolved
value) and C_2(SU(3);3)=C_2(SU(3);3bar)=4/3 (tool-verified earlier this
session):

| Piece | Interp A | Interp B |
|---|---|---|
| singlet (v_a,v_b space) | eigenvalues {2, 6} | eigenvalues {3, 7} |
| "3" / "3bar" (scalar, R^E=1/6) | 14/3 | 5 |

**Every single value, under BOTH interpretations, is strictly
positive.** As a structural sanity check, restoring rho=trivial in the
SAME singlet-piece formula reproduces the ORIGINAL L4B matrix
eigenvalues {0,4} exactly (confirming the rho=7 result is a clean
+C_2(G2;7)=+2 uniform SHIFT of the trivial-piece matrix, exactly the
mechanism argued for analytically much earlier this session, now
confirmed via the FULL, honest construction rather than an assumption).

### What this means, precisely (scope discipline)

**If this construction survives independent review:** rho=7 contributes
NO unwanted zero mode to ker(D+_S-) -- the preprint's existing
non-trivial-sector claim, currently caveated as conditional/open, would
be SUPPORTED for the rho=7 block specifically (the smallest, most
exposed non-trivial G2 Casimir gap; per the original Round 6 plan, if
rho=7 survives, rho=14 and all larger rho are progressively safer since
C_2(G2;rho) grows unboundedly while the algebraic correction terms stay
bounded).

**This is NOT yet a closed result.** Per this project's own Falsification
Ladder (Step 8a) and audit-verification-gate discipline, a claim of this
significance (first candidate resolution of a long-open danger-zone
question) requires independent, context-asymmetric review before being
promoted to preprint text. Not yet done as of this write-up -- see
Promotion status below.

### Promotion status: PENDING independent review

- [ ] reviewer agent pass (code correctness: R_half/spin_lift_so6/R^E
      construction, the two calibration claims, arithmetic in Step 4)
- [ ] skeptic pass (Falsification Ladder Step 8a, context-asymmetric --
      claim.md + code ONLY, no session history) -- specifically probe:
      is the standard twisted Lichnerowicz formula I recalled from a WEB
      SEARCH SUMMARY (not a directly-read, page-numbered primary source)
      actually correctly stated for THIS project's specific Clifford
      convention (Zi.Zj+Zj.Zi=-delta_ij, per Agricola's OWN stated
      convention, page 7)? Is there a cleaner, first-principles
      resolution of the Interpretation A/B ambiguity rather than "check
      both and see they agree"? Are there OTHER SU(3) pieces relevant to
      rho=7 not yet checked (the branching 7=3+3bar+1 is exhaustive per
      Round 12's own established fiber decomposition, but this should be
      independently re-confirmed, not just assumed)?
- [ ] IF both pass: update preprint.tex's existing caveat (currently:
      "conditional, not proved") to reflect this result, with language
      matching this project's own emphasis discipline (explicit,
      calibrated, multiply-cross-validated computation -- not a bare
      numeric claim) -- per the user's own standing instruction
      (l4b-rank-emphasis-for-writeups memory) applied by direct analogy.
- [ ] Task #7: stays in_progress until the above is complete; only

## Round 16 continued (2026-07-09, same session): review + skeptic results
## are IN. Reviewer confirms the code arithmetic is genuinely correct;
## skeptic found a DECISIVE, VALID flaw in the calibration logic. The
## rho=7 "no zero mode" conclusion is DOWNGRADED from candidate-positive
## to INCONCLUSIVE -- Task #7 stays open, honestly, not closed.

### Reviewer verdict: NEEDS_WORK, P1

Independently re-derived (not just re-run) the sign chain in
`build_R_half` (hand-traced p=1,q=2,r=3 through both bracket
applications, confirmed the double-minus-sign cancellation is correct;
also independently re-ran the antisymmetry/skew-symmetry checks on ALL
216 triples, not just the sampled few printed by main()), the
`spin_lift_so6` normalization (re-derived algebraically from the
all-indices form, corroborated by the scale-sensitive SU(3)-equivariance
pass), and ALL FOUR Step-4 headline numbers ({2,6}, {3,7}, 14/3, 5) by
hand from the raw `RE`/`D` matrices, not from main()'s own print
statements. **All of this checks out exactly.**

**One real P1 gap found:** `RE_3 = sp.Rational(1,6)` (the "3"/"3bar"
piece's R^E eigenvalue) is a bare hardcoded literal in the script,
justified only by an inline comment pointing to an earlier interactive
computation -- NOT re-derived live within the permanent script the way
the singlet-piece `M` matrix is (computed live from `RE*v_a`, `RE*v_b`).
The reviewer's own attempted independent spot-check (on a DIFFERENT,
non-equivalent set of basis vectors) was inconclusive, neither
confirming nor refuting 1/6 -- genuinely unverified within the file as
committed. **Fixed this round** (see below).

### Skeptic verdict: FALSIFIED (core predicate), Concern 3 decisive

Full context-asymmetric review (claim + code only, no session history),
per Falsification Ladder Step 8a. Five concerns raised; **Concern 3 is
correct and decisive, fully accepted, not dismissed:**

> The calibration is at rho=trivial. At rho=trivial, nabla*nabla = 0
> IDENTICALLY. Therefore the calibration constrains ONLY the coefficient
> in front of (Scal+R^E) -- it says NOTHING about the coefficient in
> front of nabla*nabla, because that term is identically zero at the
> calibration point. Interpretations A and B are two points in a
> ONE-PARAMETER FAMILY (D^2 = alpha*(nabla*nabla) + (3/2)(...)), where
> alpha is UNCONSTRAINED by the calibration. "Robust across both
> interpretations" is closer to "robust across two arbitrarily chosen
> points from a family where two convenient ones were picked."

This is EXACTLY correct and matches this project's OWN identified
pattern from earlier this session (the t=1/3 sign-bug calibration blind
spot) -- caught by the process working as intended, not a failure of
this round's effort. **Accepted in full, not disputed.**

The skeptic's other concerns:
- Concern 1 (same as Concern 3, restated) -- accepted, see above.
- Concern 2 (Lichnerowicz formula recalled from a web-search summary,
  not verified against a primary source in THIS project's specific
  Clifford convention Zi.Zj+Zj.Zi=-delta_ij) -- **accepted as a real
  gap.** The skeptic's own attempted explanation (Clifford-rescaling by
  1/sqrt(2) giving a uniform 1/2 factor) does NOT exactly match the
  observed 2/3 either (skeptic's own honest admission: "close to but not
  exactly 1/2") -- meaning the TRUE source of the 3/2 factor remains
  unexplained by either party. This is now the priority next step (see
  Task List below), not resolved this round.
- Concern 4 (sign-chain risk given 3 prior sign bugs this session) --
  **partially addressed by the reviewer's independent hand-verification**
  (Item 1 above, all 216 triples checked, not just the sampled ones) --
  downgrades this concern's likelihood substantially but does not, by
  itself, resolve Concern 3's structural gap (a correctly-signed
  ∇*∇=C_2(G2;rho)-C_2(SU(3);sigma) formula could STILL need an unknown
  overall rescaling that the calibration can't see).
- Concern 5 (Scal=10 vs the unit-round-S^6 value 30) -- **considered and
  NOT accepted as a live bug**, with reasoning: this experiment has
  consistently used ONE specific B_0-orthonormal metric normalization
  throughout (T, curvature_h, nabla_g_action all share it, unchanged
  this round), under which Scal=10 is simply this space's OWN curvature
  in THESE units (consistent with a "radius-squared=3" natural
  normalization for the Killing-form-derived G2/SU(3) metric) -- not
  inherently a bug, since nothing NEW was introduced that could break
  consistency with the ALREADY-VALIDATED L4B ground truth (which uses
  the SAME shared primitives). Documented as a caveat, not dismissed
  outright -- the skeptic's own suggested check (does 30/10=3 relate to
  the missing 3/2?) does NOT cleanly resolve to 3/2, so this is likely a
  red herring, but not proven to be one.

### Fixed this round: reviewer's P1 (RE_3 hardcoding)

Added an explicit in-script derivation to `g2su3_lichnerowicz_rho7.py`
computing R^E's action on all three "3"-piece basis vectors (y1(x)1,
y2(x)1, y3(x)1) live, asserting they give the IDENTICAL scalar (Schur's
lemma, matching the SAME pattern already used for the singlet-piece M
matrix), replacing the bare literal. Re-ran: confirms 1/6 exactly, now
tool-verified within the committed script itself, not just asserted.

### NOT fixed this round: skeptic's Concern 3 (the decisive one)

This requires either (a) an independent second calibration point with
nabla*nabla != 0 for a KNOWN rho, or (b) a from-first-principles
derivation of the twisted Lichnerowicz formula in THIS project's
specific Clifford convention (not recalled from a web search), pinning
down alpha directly rather than empirically guessing at two candidate
values. Investigated (a) this round: the most obvious candidate (the
UNTWISTED single-Sigma "3"-piece, where (D^{1/2})^2 is ALREADY known via
the earlier g2su3_delta_correction.py machinery) turns out to suffer
from the SAME "fiber slot doesn't correspond to a single rho" problem
Round 10 already identified for the TWISTED case -- Sigma's OWN "3"
piece could receive contributions from MULTIPLE G2-irreps (any rho with
a "3" in its SU(3)-branching, not just rho=7), so it does NOT give a
clean, independent second data point without ALSO solving a
representation-theoretic multiplicity question this experiment hasn't
addressed. No other readily-available candidate was found this round.

### Status: HONEST DOWNGRADE -- rho=7 remains OPEN, not resolved

**The "rho=7 has no unwanted zero mode" claim from earlier this round is
DOWNGRADED from candidate-positive-result to INCONCLUSIVE.** What
SURVIVES this round, genuinely:
- The construction itself (R_half, spin_lift_so6, R^E) is now MORE
  robustly verified than most artifacts in this experiment -- exact
  antisymmetry (216/216), exact skew-symmetry, EXACT agreement with
  Agricola's OWN independently-stated Ricci formula, exact SU(3)-
  equivariance, and (now) an in-script-verified R^E value on the "3"
  piece. The reviewer found ZERO arithmetic or sign errors in any of
  this after deep, independent re-derivation.
- What does NOT yet survive: the CONNECTION between this verified
  construction and the FINAL rho=7 verdict, specifically the overall
  scale relating (Scal+R^E) to nabla*nabla=C_2(G2;rho)-C_2(SU(3);sigma).
  This is a genuinely open normalization question, not a computational
  bug -- and per Concern 3, checking "two interpretations, both
  positive" does NOT constitute evidence against a THIRD, unchecked
  value of alpha that could flip the sign.

This is the Falsification Ladder working exactly as intended: a
construction survived deep code review, and was STILL correctly
identified by an adversarial, context-blind skeptic pass as
insufficient to support its headline claim, BEFORE that claim reached
the preprint. Per this project's Step 8a response matrix, this is
FALSIFIED-with-a-clear-fix-path, not a dead end -- but it is NOT yet a
result, and must not be reported as one.

### Task list (next session or continuation)

1. Resolve Concern 3's alpha ambiguity from first principles: read a
   primary source for the twisted Lichnerowicz-Weitzenbock formula in
   the EXACT Clifford convention Zi.Zj+Zj.Zi=-delta_ij (Agricola's own
   stated convention, page 7) -- Friedrich's "Dirac Operators in
   Riemannian Geometry" or Lawson-Michelsohn "Spin Geometry" are
   plausible sources, per the skeptic's own suggestion, but must be
   READ DIRECTLY (PyMuPDF, this session's established reliable method),
   not recalled from a web search summary.
2. Alternatively/additionally: find a genuinely independent second
   calibration point with nabla*nabla != 0 that is NOT subject to the
   "fiber slot = multiple rho's" ambiguity -- this may require actually
   building the V_7 multiplicity-space machinery (Hom_SU(3)(V_7,
   S+(x)S-)) that Round 6's original plan called for, rather than
   continuing to look for shortcuts.
3. Task #7 remains in_progress. Do NOT update preprint.tex based on this
   round's result. Do NOT report "rho=7 resolved" in any external
   communication until Concern 3 is genuinely closed.

## Round 16 continued v2 (2026-07-09, same session, user asked to "find
## an independent second calibration point"): FOUND ONE -- directly
## answers the skeptic's own suggested "cheapest test". Concern 3
## appears CLOSED, pending independent review (dispatched, not yet in).

### The idea (not a calibration-point hack -- a genuinely separate derivation)

Rather than search for another D^2 ground truth to compare against, used
DATA NEVER BEFORE USED FOR THIS PURPOSE: V_7's own representation
matrices (Round 14, rho_7(e_p) for p=1..6, the m-direction/"rolling"
action, restricted from the validated 8x8 nu_k matrices). For a
homogeneous-bundle section realized as a matrix-coefficient
psi_v(g):=iota(rho_V(g^{-1})v) (v in V_rho, iota an H-intertwiner into
the fiber F), a direct computation gives the GENERAL identity
  (e_p)^2(psi_v)|_e = iota(rho_V(e_p)^2 v)
-- re-derived twice, independently, with two DIFFERENT sign conventions
for psi_v (with/without the group-inverse), giving the IDENTICAL result
both times (a good robustness check: applying the SAME raw derivative
twice symmetrizes away the inverse-convention ambiguity).

Combined with Agricola's OWN definition (page 12, quoted verbatim
earlier this session) Omega_g := -sum_p Z_p^2 + Ctilde_h (Z_p = RAW
left-invariant vector fields, exactly matching what "(e_p)^2" computes
above -- NOT a new assumption, Agricola's own stated formula), this
gives Omega_g(psi_v)|_e = iota(-sum_p rho_V(e_p)^2 v) + Ctilde_h_twisted(iota(v)),
COMPUTABLE without ANY reference to R_half, R^E, or the L4B/Scal
calibration that the skeptic found insufficient.

### What was verified (tool, `g2su3_omega_g_independent_check.py`)

1. **General Casimir decomposition on V_7, a pure matrix identity, no
   eigenbasis needed:** -sum_p rho_7(e_p)^2 + (-sum_k rho_7(nu_k)^2) ==
   2*I_7 == C_2(G2;7)*I_7 EXACTLY. This is just splitting the
   ALREADY-VALIDATED identity C_2(G2;7)=-sum_{ALL 14}rho_7(nu_k)^2 (Round
   14) into su(3)-part + m-part -- no new assumption, pure algebra.
2. **-sum_k rho_7(nu_k)^2 (SU(3)-Casimir restricted to V_7) is EXACTLY
   block-scalar**: eigenvalues {0 (mult 1), 4/3 (mult 6)} -- matching
   C_2(SU(3);1)=0 and C_2(SU(3);3)=C_2(SU(3);3bar)=4/3 EXACTLY (this
   4/3 was independently tool-verified via a COMPLETELY DIFFERENT method
   earlier this session, su3_casimir_action_squared on Sigma's y1/y12 --
   now confirmed a SECOND, independent way, via V_7's own matrices).
   Hence -sum_p rho_7(e_p)^2 = {2 on singlet, 2/3 on "3"/"3bar"}.
3. **phi_2 (V_7's singlet, independently re-confirmed killed by all 8
   su(3) generators restricted to V_7) gives -sum_p rho_7(e_p)^2.phi_2 =
   2*phi_2 EXACTLY** (direct numeric computation, matches item 1's
   general result specialized to the singlet).
4. **Ctilde_h_twisted (Round 15's construction, built from curvature_h +
   su3_action -- COMPLETELY SEPARATE from R_half/R^E) gives EXACTLY
   (4/3)*(y1(x)1) on y1(x)1** -- a NEW check this round (Round 15 only
   verified it was zero on v_a,v_b) -- matching the UNTWISTED single-
   Sigma Ctilde_h's OWN eigenvalue (4/3) on the analogous "3" piece
   exactly, extending Round 15's partial verification.

### Assembly: BOTH relevant pieces confirmed

- Singlet: Omega_g = 2*iota(phi_2) + 0 = 2*iota(phi_2) =>
  nabla*nabla = Omega_g - Ctilde_h_twisted = 2 - 0 = 2, matching
  C_2(G2;7)-C_2(SU(3);1) = 2-0 = 2 EXACTLY.
- "3" (and by the identical argument, "3bar"): Omega_g = (2/3)*iota(v) +
  (4/3)*iota(v) = 2*iota(v) => nabla*nabla = 2 - 4/3 = 2/3, matching
  C_2(G2;7)-C_2(SU(3);3) = 2-4/3 = 2/3 EXACTLY.

**This independently confirms Interpretation A's nabla*nabla coefficient
(alpha=1, unscaled) is CORRECT for both pieces, via a route that never
touches the (Scal+R^E) calibration's mysterious 3/2 factor at all.**
Per Interpretation A's already-computed values: singlet eigenvalues
{2,6}, "3"/"3bar" piece = 14/3 -- both strictly positive, and NOW backed
by an independent derivation of the load-bearing term, not by "checking
two plausible interpretations."

### What this does NOT resolve

The (Scal+R^E) piece's own 3/2 normalization mystery (skeptic Concern 2)
is UNTOUCHED by this argument -- but it no longer needs to be fully
explained for the rho=7 QUALITATIVE conclusion, since nabla*nabla (the
ONLY rho-dependent piece) is now independently pinned down, and
Interpretation A (the one this round's argument supports) already gives
strictly positive eigenvalues using the EMPIRICALLY-fitted 3/2 factor
for (Scal+R^E) specifically. The 3/2 factor's ORIGIN remains an open,
lower-priority loose end (does not affect the sign of the answer either
way, since it multiplies a term added to an already-positive nabla*nabla
contribution).

### Promotion status: PENDING independent review (dispatched)

Given the significance (this would directly resolve the skeptic's
decisive Concern 3), a reviewer and a context-blind skeptic pass have
been dispatched on THIS NEW argument specifically, per the same
discipline applied to the original (falsified) Round 16 claim. NOT yet
promoted -- do not cite as resolved until those results are in.

## Round 16 continued v3 (2026-07-09, same session): second skeptic pass
## FALSIFIED this attempt too -- and a direct, tool-verified follow-up
## check CONFIRMS the skeptic's deeper concern has real substance, even
## though its specific framing was likely wrong. Task #7 STAYS OPEN.
## Recommending a pause on this specific sub-thread.

### The second skeptic's verdict: FALSIFIED, Concern 2

Full context-asymmetric review (claim + code only) of the v2 (Omega_g
independent check) argument. The skeptic's Concern 1 (the central
differentiation identity (e_p)^2(psi_v)|_e = iota(rho_V(e_p)^2 v)) was
independently re-derived from scratch and CONFIRMED CORRECT -- "no sign
trap" -- matching this round's own claim exactly. Concern 2, the
decisive one: is "Omega_g - Ctilde_h" (Agricola's own decomposition,
what this round computed) actually the SAME "nabla*nabla" that appears
in the GENERIC twisted Lichnerowicz formula D^2=nabla*nabla+(1/4)Scal+R^E
(the formula g2su3_lichnerowicz_rho7.py's R^E/Scal construction is
built on)? The skeptic argued these could differ because Omega_g is
tied to "the characteristic/canonical connection" while the generic
formula's nabla*nabla is tied to Levi-Civita specifically.

### Correction to the skeptic's specific framing (verified against the primary source)

The skeptic's Concern 2, AS STATED, rests on treating Omega_g as
CONNECTION-SPECIFIC (t=0 or t=1/3, not t=1/2). This is FACTUALLY
INCORRECT per Agricola's OWN Theorem 3.2, read directly and quoted
verbatim earlier this session: "(Dt)2psi = Omega_g(psi) +
1/2(1-3t)Sum...ZiZjZk(psi) - ..." -- Omega_g(psi) appears with NO
t-coefficient, IDENTICALLY for every value of t (canonical t=0, cubic
t=1/3, Levi-Civita t=1/2) -- this is the theorem's own, explicit,
already-multiply-verified structure (used throughout this whole
experiment, e.g. the earlier "(D^t)^2=Omega_g+2(1-3t)H+C̃h+t^2H^2"
derivation, cross-checked against Theorem 3.3's t=1/3 special case).
Omega_g is PROVABLY t-independent -- NOT specific to any one connection.

### But the DEEPER version of the concern is real -- confirmed by direct

### computation, not just plausible-sounding

Despite the above correction, tested whether "Omega_g - Ctilde_h" (my
assumed nabla*nabla) is actually consistent with matching Agricola's
OWN, fully-verified (D^{1/2})^2 = Omega_g - H + Ctilde_h + (1/4)*H^2
formula against the GENERIC untwisted Lichnerowicz formula
(D^{1/2})^2 = nabla*nabla + (1/4)*Scal (R^E=0 trivially for the
untwisted/E=trivial case). Setting these equal and substituting
nabla*nabla := Omega_g - Ctilde_h requires the identity
  -H + 2*Ctilde_h + (1/4)*H^2 == (1/4)*Scal
On the "3" piece, using ALL ALREADY-ESTABLISHED, TOOL-VERIFIED values
(H=0, Ctilde_h=4/3, H^2=0, Scal=10):
  LHS = -0 + 2*(4/3) + 0 = 8/3
  RHS = (1/4)*10 = 5/2
  **8/3 != 5/2, discrepancy = EXACTLY 1/6, tool-verified, not a
  hand-arithmetic slip.**

This is a REAL, CONCRETE inconsistency -- not the skeptic's specific
"wrong connection" diagnosis, but genuine evidence that "nabla*nabla :=
Omega_g - Ctilde_h" does NOT simply equal "the generic Lichnerowicz
nabla*nabla" (as recalled from a web search, never verified against a
primary source in THIS project's specific Clifford convention -- the
SAME root-cause concern the FIRST skeptic pass raised as Concern 2,
now independently confirmed to have real teeth via direct computation,
not just a plausible-sounding worry).

### Verdict: task #7 STAYS OPEN. Genuine partial progress, not resolution.

**What IS now solidly established** (survives BOTH skeptic passes,
confirmed via multiple independent routes): Omega_g's OWN eigenvalue
formula, C_2(G2;rho)-C_2(SU(3);sigma), is CORRECT and T-INDEPENDENT --
confirmed via Agricola's own theorem (primary source), via the untwisted
Ctilde_h construction, and now via V_7's own matrices (three independent
lines of evidence, matching this experiment's own L4B-methodology
standard). This is a genuine, reusable, well-verified building block.

**What is NOT established**: how this Omega_g piece correctly combines
with the (Scal+R^E) machinery to give the TRUE, physical D^2. The
"generic twisted Lichnerowicz formula" used for R^E/Scal was recalled
from a web search summary and has NOW been shown, via direct
computation (not speculation), to be INCONSISTENT with Agricola's own,
fully-verified machinery by a concrete, nonzero amount (1/6 on the
untwisted "3" piece) -- meaning the R^E/Scal construction itself likely
has an error or missing term, not just an unexplained overall scale
factor as previously believed.

### Recommendation: pause this specific sub-thread

This sub-problem (the twisted, non-trivial-rho danger-zone gap for
rho=7) has now survived 3 full attempts within this session alone
(twisted_Ch/Round 15, Lichnerowicz R^E/Round 16, Omega_g-independent-
check/Round 16 v2), each catching a real, substantive error in the
previous one via this project's own review+skeptic discipline -- exactly
as that discipline is designed to do, but also a signal that this
SPECIFIC derivation (twisted Kostant-Parthasarathy-type formula for a
naturally reductive space) is genuinely hard and not close to a quick
resolution via incremental fixes. Recommend NOT attempting a 4th
construction in this same session without a fundamentally different
strategy (e.g. building the FULL V_7 multiplicity-space Dirac operator
from scratch rather than trying to match a recalled generic formula, or
seeking a primary-source-verified twisted Lichnerowicz formula in
EXACTLY this project's Clifford convention before building anything
further on top of it).

Task #7 remains in_progress, explicitly OPEN. preprint.tex is NOT
updated. No external communication should describe rho=7 as resolved.

### Addendum: second reviewer's LGTM (received after the above was written)

The reviewer pass on `g2su3_omega_g_independent_check.py` returned
**LGTM** -- independently re-derived the central differentiation
identity from scratch (two different ways, both agreeing), confirmed
all of Step 1-4's arithmetic reproduces exactly, and confirmed
Omega_g's OWN eigenvalue formula (C_2(G2;rho)-C_2(SU(3);sigma)) is
internally solid. This does NOT contradict the honest downgrade above --
the reviewer correctly verified THIS FILE's own scope (that
Omega_g-C̃h telescopes correctly and matches C_2(G2;7)-C_2(SU(3);sigma)
within Agricola's OWN framework, which is true and was never in
question) -- it was not asked to check, and does not touch, the SEPARATE
question this round's follow-up computation found broken: whether
"Omega_g-C̃h" (verified solid) equals "the generic Lichnerowicz
nabla*nabla" used in the R^E/Scal construction (found NOT to, via the
tool-verified 1/6 discrepancy above). The reviewer's one substantive
observation (P2, not blocking): Step 4's "two independent confirmations"
of the "3"-piece value are algebraically the SAME equation (Omega_g:=
(-Σρ7(ep)²)+Ctilde_h_twisted telescopes trivially when subtracting
Ctilde_h_twisted back out) -- the REAL, independent agreement in that
file is between Step 1 (V_7's abstract matrices, giving 2/3) and Step 3
(the twisted Clifford construction, giving 4/3, summing to the
independently-known 2) -- worth tightening in a future revision, does
not change any number. Net effect: reinforces that g2su3_omega_g_independent_check.py
is itself correct and reusable -- but the OVERALL rho=7 verdict remains
open for the reason already documented (the 1/6 gap in connecting to
R^E/Scal), unaffected by this LGTM.

## Round 17 (2026-07-09, user asked to "build the V_7 multiplicity-space
## Dirac operator from scratch"): a genuinely first-principles
## construction, avoiding EVERY formula-matching trap of Rounds 15-16,
## reproduces the SAME {2,6} eigenvalues independently. Strongest result
## yet for rho=7's singlet piece -- pending independent review.

### The construction (no recalled formula, no closed-form substitution)

For a homogeneous vector bundle G x_H F with H-intertwiner w:V_rho->F,
matrix-coefficient sections psi_{v,w}(g):=w(rho_V(g^{-1})v) satisfy (via
Agricola's own equation 3, "grad_Z psi = Z(psi)+Lambda_tilde_m(Z)psi",
combined with the differentiation identity independently re-derived and
CONFIRMED CORRECT by the Round-16-v2 reviewer, "e_p(psi_v)|_e =
-iota(rho_V(e_p)v)"):

  D(psi_{v,w})|_e = -sum_p e_p . w(rho_V(e_p) v) + D_on_simple_tensor(w(v))

Verified this round, carefully, term-by-term: the SECOND term (built from
nabla_g^F(e_p)(eta⊗xi):=nabla_g(p,eta)⊗xi+eta⊗nabla_g(p,xi), the pure
Leibniz-extended CONNECTION with no Clifford mult yet, then Clifford-
multiplied on the LEFT factor per this experiment's established
convention) is EXACTLY D_on_simple_tensor(eta,xi) -- confirmed by direct
term-matching, not assumed. This means the construction uses ONLY
already-validated, already-calibrated pieces (V_7's matrices from Round
14, D_on_simple_tensor from Round 10-12, Clifford multiplication) --
NO recalled Lichnerowicz formula (Round 16's trap), NO naive
substitution into Agricola's UNTWISTED closed-form Theorem 3.2 (Round
15's trap).

By Schur's lemma, D acts on the rho=7-isotypic component as
Id_{V_7} (x) D_7 for a linear map D_7 on intertwiners -- the formula
above, applied to v ranging over ALL of V_7, literally DEFINES D_7(w)
as a new intertwiner w', directly computable and composable (apply
twice for D^2_7) without ever needing to differentiate a section at a
general group element g.

### The singlet piece, without solving for the "3"/"3bar" intertwiners

phi_2 (V_7's SU(3)-singlet) is COMPLETELY ISOLATED under su(3)
restricted to V_7 -- row AND column 0 EXACTLY zero for all 8 generators
(re-verified this round). This means "project v onto its phi_2-
component" is ITSELF SU(3)-equivariant, with NO need to explicitly
identify V_7's "3"/"3bar" pieces. w_a(v):=v[phi_2]*v_a, w_b(v):=
v[phi_2]*v_b -- VERIFIED SU(3)-equivariant SYMBOLICALLY (all 7
directions, all 8 generators, a single symbolic check covering every
case at once, not spot-checks).

### Result (`g2su3_v7_multiplicity_dirac.py`)

D_7(w_a)(phi_2) = -sqrt(3)*w exactly, matching D_on_simple_tensor(v_a)
from L4B (expected: w_a(rho_7(e_p)phi_2)=0, so the new term vanishes
here -- a real but limited consistency check, not new information by
itself).

D^2_7(w_a)(phi_2) and D^2_7(w_b)(phi_2), computed by applying the SAME
from-scratch formula TWICE, give:
  D^2_7|_{singlet block, basis v_a,v_b} = [[3,1],[3,5]]
  eigenvalues: {2, 6}

**Both eigenvalues strictly positive -- and this EXACTLY MATCHES
Interpretation A's prediction from the discredited Round 16 R^E/Scal
construction, via a route that shares NO machinery with it whatsoever**
(no Scal, no R^E, no R_half curvature tensor, no "generic Lichnerowicz"
assumption -- only V_7's matrices, D_on_simple_tensor, and Clifford
multiplication, all independently trusted before this round began).

### A real, non-trivial structural check that passed

D^2_7(w_a)(phi_2) and D^2_7(w_b)(phi_2) were checked for "leakage"
outside span(v_a,v_b) into other parts of the 64-dim fiber -- ZERO
leakage, exactly, for both. This is NOT automatic: an error anywhere in
the rho_7(e_p) matrices, the Clifford-left-factor convention, or the
V_7-basis bookkeeping would generically produce a result NOT confined
to span(v_a,v_b) (since D^2_7 must respect SU(3)-equivariance, and only
an actually-correct construction is GUARANTEED to preserve this) --
passing this check is meaningful evidence, not a tautology.

### What this does NOT yet cover

Only the singlet ("1") piece of rho=7's branching (7|SU(3)=3(+)3bar(+)1)
has been computed this way. The "3"/"3bar" pieces need explicit
intertwiners w_3, w_3bar (V_7's "3"-piece is NOT isolated the simple
way phi_2 is -- building these requires either solving the SU(3)-
intertwining linear system directly, or explicitly diagonalizing V_7's
complementary 6-dim su(3)-action) -- not yet attempted this round.

### Promotion status: reviewer LGTM, skeptic WEAKENED -- concerns
### addressed with follow-up evidence, not just argument

### Reviewer verdict: LGTM (P2, no blockers)

Independently re-derived the central formula from the standard theory
of matrix-coefficient sections (Wang's-theorem style), confirmed
`clifford_left_64`'s index arithmetic, `d7_apply`'s use of `w(rho_7(e_p)v)`
(not the wrong `rho_7(e_p)w(v)`), and all Step-4 arithmetic by hand from
raw printed entries -- all correct. Then ran an ADDITIONAL,
SELF-DEVISED test the script itself never performs: checked whether
`D_7(w_a)` and `D_7(w_b)` (the OUTPUTS of d7_apply, not just the inputs
w_a/w_b) are THEMSELVES SU(3)-equivariant, for all 8 generators. **Passed
exactly, both outputs, all 8 generators.** This is materially stronger
than the script's own "no leakage" check (see skeptic Concern 4 below)
since it stresses rho7_ep, clifford_left_64, and D64 jointly -- exactly
the class of cross-piece interaction that broke Round 15's construction.
One P2 (documentation): the "Agricola equation 3" citation is not
re-verified against a cached primary-source quote in this repo (unlike
several other citations this session that ARE verbatim-quoted) -- the
underlying math was independently re-derived by the reviewer from
first principles regardless, so this doesn't affect correctness, only
citation hygiene.

### Skeptic verdict: WEAKENED (not FALSIFIED) -- 5 concerns, addressed below

Full context-asymmetric review. Verdict: "directionally plausible... but
LOW confidence the specific numbers {2,6} are established independently
of the prior [Round 16] construction." Addressing each concern with
FOLLOW-UP EVIDENCE (not just counter-argument):

**Concern 1 (E_SIGN "unjustified, possibly calibrated against prior
construction"):** REFUTED WITH EVIDENCE. `git log` confirms E_SIGN
(and rho7_ep/rho7_nuk) originate in `g2su3_appendix_a_construction.py`
lines 37-38/129, explicitly commented "per Section 5.1's own
definition" -- i.e. AHL2023's OWN stated convention (e_i:=nu_{8+i} for
i=1,2,4,6, e_i:=-nu_{8+i} for i=3,5), committed in 9de3caa/d60e838,
BEFORE either Round 16 or Round 17 existed. It cannot have been
"calibrated against" either construction's output. (Reviewer separately
flags this as duplicated across 3 files -- a real DRY issue, P2, not a
correctness issue.)

**Concern 2 (does D_on_simple_tensor really equal the full, correct
connection term, with nothing missing?):** DIRECTLY VERIFIED, not just
argued. Built "Leibniz-extended nabla_g on F, then clifford_left_64"
independently from scratch and checked it EXACTLY equals
D_on_simple_tensor's own (already-validated) output, for 4 different
representative simple tensors (all zero residual). This is the EXACT
identity the whole Round-17 construction depends on, now tool-verified
directly rather than argued from the docstring's own claim.

**Concern 3 (phi_2 row/column-zero redundancy):** skeptic itself called
this a non-issue given orthonormal basis (confirmed: V_7's basis IS the
same orthonormal B_0 basis used throughout, per Round 14).

**Concern 4a ("no leakage" is a Schur tautology, not evidence):**
PARTIALLY ACCEPTED as a methodological framing point -- "no leakage"
alone only rules out errors that break SU(3)-block structure, not
errors preserving it (uniform sign/scale). But the REVIEWER's
additional, stronger test (D_7(w_a)/D_7(w_b) THEMSELVES being
SU(3)-equivariant, not assumed) is NOT tautological -- equivariance of
the intermediate result is a genuine, checkable property that a
cross-piece indexing bug (Round 15's failure mode) would very plausibly
break, and it passed. Going forward, "no leakage" should be described
as a necessary-but-not-sufficient sanity check, not standalone proof --
noted for future write-ups.

**Concern 4b (matrix [[3,1],[3,5]] is not symmetric -- suspicious for a
self-adjoint D^2):** DIRECTLY RESOLVED, not just asserted. Computed the
ACTUAL Gram matrix of {v_a,v_b} in the standard orthonormal-SUBSETS-
basis inner product on Sigma(x)Sigma: <v_a,v_a>=3 (three orthogonal
unit-coefficient terms), <v_b,v_b>=1, <v_a,v_b>=0 -- i.e. G=diag(3,1),
NOT the identity (v_a, v_b are valid basis vectors but NOT orthonormal).
Checked G.M == M^T.G for M=[[3,1],[3,5]]: **both sides give
[[9,3],[3,5]] EXACTLY.** The matrix IS self-adjoint w.r.t. the correct
inner product -- the apparent asymmetry was entirely an artifact of
v_a's larger norm, not a bug. This is a genuine, POSITIVE finding (the
construction respects a real physical constraint on D^2) that the
skeptic's own suggested test (Concern 4, "cheapest falsification test
1") directly confirms rather than refutes.

**Concern 5 (agreement with Round 16's R^E/Scal construction "not
independent" since both allegedly share NU, D64, v_a, v_b):**
PARTIALLY REFUTED. Round 16's R^E was built from `curvature_h` (which
uses the FULL 8x8 NU via `ad_nu_m_trusted`, for the su(3)-2-form
[e_p,e_q]_h) -- it does NOT use V_7's e_p-action (`rho_7(e_p)`, the
6-generator restriction to V_7) AT ALL. Round 17 uses rho_7(e_p)
DIRECTLY and never touches curvature_h/R_half. These ARE genuinely
different derived quantities computed via different paths, even though
both ultimately trace back to the same underlying `NU` dict (AHL2023's
Appendix A) and both use the SAME v_a,v_b (a real, acknowledged shared
input -- NOT fully independent, but LESS shared than the skeptic's
"both use NU, D64, v_a, v_b" framing suggested). Honest characterization:
MEDIUM independence, not full, not none.

**Concern 6c ("suspicious" that {2,6} might be a free Casimir-formula
consequence, guessing {2,6}={C_G2(V_7), Scal/5}):** the skeptic's own
guess used the GENERIC unit-round-sphere value Scal=30 -- this
project's OWN, already tool-verified value is Scal=10 (different metric
normalization, established Round 16), giving Scal/5=2, NOT 6 -- the
skeptic's specific numerology does not hold. The ACTUAL explanation for
{2,6} is more mundane and already independently derived much earlier
this session: {2,6} = {0,4} + 2*[1,1] -- i.e. EXACTLY the rho=trivial
L4B matrix [[1,1],[3,3]] (eigenvalues {0,4}) UNIFORMLY SHIFTED by
C_2(G2;7)=2, matching the "Omega_g contributes a uniform +C_2(G2;rho)
shift" structural argument made analytically before ANY of Rounds
15-17's constructions were built, and separately confirmed via the
Round-16-v2 Omega_g-independent-check. Three independent routes
(analytic prediction, Omega_g check, full D_7 construction) now agree
on this same shift structure -- reassuring convergence, not a
coincidence needing further explanation.

### Net assessment

This is now the best-supported rho=7 result of the session: a
genuinely from-scratch construction (sharing only V_7's matrices,
D_on_simple_tensor, and Clifford multiplication with prior work -- NOT
the broken R^E/Scal machinery), reviewed (LGTM, with a novel passing
equivariance-of-output test), and skeptic-reviewed with EVERY concern
addressed by concrete follow-up computation (not just counter-argument)
except the inherent, honestly-scoped limitation: **only the singlet
piece is done.** The "3"/"3bar" pieces of rho=7's branching still need
explicit w_3/w_3bar intertwiners (harder to construct than w_a/w_b,
since V_7's "3"-piece is not an isolated coordinate the way phi_2 is)
-- not yet attempted. Per this project's own skeptic-leaning default
under stage ambiguity, and because the "danger zone" claim is about ALL
of rho=7's branching, NOT just the singlet: still NOT promoting to
preprint.tex, still NOT declaring rho=7 fully resolved. Task #7 stays
in_progress, but with a real, solid, multiply-verified partial result
now in hand.

## Round 18 (2026-07-09, user asked to "попробуй построить w_3/w_3bar
## для 3/3bar части"): built the "3"/"3bar" intertwiners -- and found
## why this can't just extend Round 17's {2,6} the way it looked like
## it would

**Construction** (`g2su3_v7_3_3bar_intertwiners.py`): V_7's complementary
6-dim block (local indices 1..6, everything except phi_2) was, for the
first time this experiment, EXPLICITLY diagonalized under the commuting
Cartan pair (nu_7,nu_8) -- 6 weight eigenvectors found, grouped into two
genuine 3-dim su(3)-invariant subspaces via the "weights sum to zero"
criterion, closure-VERIFIED under all 8 generators (not just the Cartan
pair). Matched against Sigma's already-established y1,y2,y3 ("3") and
y12,y13,y23 ("3bar") via a SOLVED (sp.linsolve, not guessed) Schur
intertwiner T, T2 -- each returns EXACTLY a 1-parameter family (72
equations, 9 unknowns), confirming both irrep-match and irreducibility.
w_3, w_3bar built and VERIFIED SU(3)-equivariant (symbolic, generic v,
all 8 generators).

**The finding:** applying Round 17's own (already-reviewed) D_7 formula
to w_3 at v=phi_2 -- an input where w_3 is IDENTICALLY ZERO by
construction -- returns a NONZERO result (lands on a THIRD, previously
unused singlet of F, 1(x)1, distinct from v_a,v_b). Symmetrically,
D_7(w_a) [Round 17's phi_2-only map] is nonzero at v=e_1. This is
BIDIRECTIONAL leakage: D_7 does NOT respect "which SU(3)-sub-piece of
V_7 the domain of w is supported on" as an invariant grading of the
multiplicity space M := Hom_SU(3)(V_7,F). This is not a construction
bug -- there is no structural reason to expect otherwise (D is only
G2-equivariant; SU(3) is merely the isotropy group used to DEFINE M as
a vector space, nothing forces D_7 to be block-diagonal w.r.t. that
particular domain decomposition).

**Independently confirmed via SU(3) Casimir spectrum on the full 64-dim
F** (eigenvalues {0:mult6, 4/3:mult30, 3:mult16, 10/3:mult12}, textbook
Dynkin-label values, cross-checked): the TRUE multiplicity space is
dim M = 6 (trivial) + 10 ("3"+"3bar" combined) = 16 -- not the 2+1+1=4
dimensions explored so far (Round 17's v_a,v_b plus this round's
w_3,w_3bar). [The "5+5" 3-vs-3bar split is [INFERRED] from F's
self-conjugacy, not tool-verified -- Casimir alone can't distinguish
conjugate irreps of equal eigenvalue -- but dim M=16 itself is robust
to the exact split since 3x+3y=30 forces x+y=10 regardless.]

**Review:** reviewer LGTM (no correctness issues; independently
re-enumerated all C(6,3)=20 possible weight-vector groupings and
confirmed {B,C,D}/{A,E,F} is the UNIQUE zero-weight-sum pair, not a
cherry-pick; traced the phi_2-leak by hand through d7_apply and
confirmed it's a genuine, expected mechanism, not an index/zero-vector
bug; independently recomputed the Sigma-alone Casimir spectrum as a
second check on the 4/3 normalization). Flagged 2 minor P2 hardening
gaps -- both fixed same round: (a) `solve_intertwiner`'s
"exactly-1-solution" guard cannot structurally distinguish a real
1-param family from the trivial all-zero solution (sp.linsolve always
returns one tuple for a homogeneous system either way) -- added an
explicit `assert det(T) != 0` / `assert det(T2) != 0` right after
substitution, the actual non-degeneracy check; (b) removed an unused
`P_group_full_6dim` parameter from `build_w_cols`.

**Skeptic** (context-blind, claim+code only): verdict CONFIRMED, with
one WEAKENED aspect -- flagged that the file never re-verified, IN ITS
OWN SCOPE, that (FT1) D_7(w_3)/D_7(w_3bar)'s OUTPUTS are themselves
SU(3)-equivariant (the entire "leaks into phi_2" reading is only
meaningful if w3_prime is a genuine element of M, not some
non-equivariant artifact), and (FT4) that V_7 local index 0 is really
su(3)-isolated within this file's own scope (inherited from Round 17
without a local check). Both were [INFERRED] only, since the skeptic
had no Bash/execution access (static+hand-symbolic tracing only,
explicitly disclosed). Both closed THIS round by adding the checks and
running them: FT1 (`verify_equivariance` on w3_prime, w3bar_prime,
w3_double, w3bar_double) -> True for all four; FT4 (explicit re-check
that rho7_nuk(k) kills local index 0's row AND column for all 8
generators, asserted) -> True. Both [INFERRED] markers lifted to
[VERIFIED-tool]. Skeptic separately noted the CONCLUSION ("16x16
required, {2,6} alone insufficient") is doubly robust -- it follows
from dim M = 16 >> 4 alone via ordinary linear algebra (a
positive-definite 2x2 principal submatrix never implies positive-
definiteness of the full 16x16 matrix), independent of whether the
leakage computation itself is exactly right.

**Skeptic's Concern 1/2 (wrong grouping could pass by luck / "sum to
zero" insufficient criterion):** DEFUSED -- not merely "a" grouping,
the UNIQUE one (reviewer independently confirmed via exhaustive
enumeration), and even if the "sum to zero" heuristic admitted a
spurious triple, the closure test would still reject it (two
independent gates, not one).

**Skeptic's Concern 6 (smuggled unestablished assumptions):** none
found -- every reused piece (NU, D64, d7_apply, phi_2-is-singlet) traces
to a prior file that carries its own independent validation, and this
round added a fresh, local re-check (FT4) of the one inherited fact the
interpretation most depends on.

### Net assessment / SCOPE CORRECTION to Round 17

w_3, w_3bar are now built, Schur-verified, SU(3)-equivariant, and
reviewed+skeptic-CONFIRMED. But this is NOT the clean extension of
Round 17's {2,6} to the "3"/"3bar" pieces that the Round-16-v2
Omega_g-independent-check's "14/3" prediction had suggested was coming.
Instead, the attempt to build it surfaced a real, structural fact:
**Round 17's {2,6} eigenvalues remain a correctly-computed 2x2 matrix
sub-block (the v=phi_2-in, v=phi_2-out, {v_a,v_b} piece of D^2_7) -- but
they do NOT, by themselves, establish "no zero mode in the rho=7 danger
zone."** The true operator relevant to that question lives on the full
16-dim multiplicity space M, with off-block-diagonal couplings between
the singlet-support, "3"-support, and "3bar"-support pieces that are
NOT visible from any small sub-block explored so far (only 4 of 16
dimensions have been touched: 2 singlets + 1 "3"-copy + 1 "3bar"-copy).
A genuine zero mode of the full operator could in principle be a linear
combination spanning all three pieces simultaneously.

Per this project's NULL Retroactive Scan discipline (a new finding
changing the interpretation of a prior PROMOTE-leaning result must be
applied retroactively): Round 17's activeContext.md entry is corrected,
not retracted -- its computation stands, its scope is narrowed.

**Still NOT promoting anything to preprint.tex. Still NOT declaring
rho=7 resolved (danger zone remains genuinely OPEN).** Task #7 stays
in_progress. Next step, clearly scoped now for the first time: build
out the remaining 12 basis intertwiners (4 more singlets, 4 more "3"
copies, 4 more "3bar" copies -- or however the true 5+5 split falls)
and diagonalize the full 16x16 D^2_7 matrix -- a substantially larger
undertaking than anything done in Rounds 15-18, not attempted this
round.

## Round 19 (2026-07-09, user asked to "давай построй полную 16x16
## матрицу D^2_7"): built the FULL 16x16 matrix -- rho=7's danger zone
## CLOSED, no zero mode anywhere

**Construction** (`g2su3_v7_16dim_full_matrix.py`): built EXPLICIT basis
vectors for the full multiplicity space M = Hom_SU(3)(V_7,F), 16-dim:
- 6 singlets (Hom(1,F)): 4 simple 1a/1b tensor combos (1(x)1, y123(x)1,
  1(x)y123, y123(x)y123) + v_a (Round 17's 3(x)3bar contraction) + its
  tensor-factor swap. All VERIFIED SU(3)-invariant, rank 6.
- 5 "3"-copies (Hom(3,F)): 4 simple embeddings (1(x)y_i, y_i(x)1,
  y123(x)y_i, y_i(x)y123, each VERIFIED to match Sigma's own y1,y2,y3
  action pattern for all 8 generators) + a 5th extracted from the
  Casimir=4/3 eigenspace of Lambda^2(x)Lambda^2 (=3bar(x)3bar=6bar(+)3),
  reordered to match the canonical pattern -- VERIFIED IN-FILE (not just
  asserted) via `matches_reference_pattern`. Jointly rank 15.
- 5 "3bar"-copies (Hom(3bar,F)): mirror construction via Lambda^2=
  {y12,y13,y23}, 5th from Lambda^1(x)Lambda^1's Casimir=4/3 eigenspace,
  also in-file-verified. Jointly rank 15.
- EXHAUSTIVENESS (corrected mid-round, see Reviewer section): NOT simply
  "Casimir mult=30 => 5+5" (Casimir alone can't distinguish conjugate
  irreps sharing an eigenvalue -- only forces mult(3)+mult(3bar)=10). The
  real closing argument: Sigma = 1a(+)3(+)3bar(+)1b under SU(3) (already
  tool-verified elsewhere), so Sigma(x)Sigma's 16 cross-terms give EXACTLY
  5 "3"-sources and EXACTLY 5 "3bar"-sources, matching c1..c5/d1..d5
  one-for-one with no leftover cross-term. Docstring corrected to state
  this properly.

**The intertwiners**: reused Round 18's Schur T (V_7's "3"={B,C,D} ->
anything matching y1,y2,y3) applied to EACH of the 5 "3"-copies (since all
5 provably transform identically), and T2 similarly for "3bar" -- no new
intertwiner machinery, per the session's standing discipline of reusing
already-reviewed pieces.

**The 16x16 matrix**: applied `d7_apply` (Round 17's formula, reused
verbatim) TWICE to each of the 16 basis w_i, flattened to 448-dim,
extracted coefficients via Hermitian normal equations (c = (W^H W)^{-1}
W^H . target -- W^T W would be singular for this complex-entried W,
confirmed: det(W^T W)=0 exactly vs det(W^H W)=531441/256), and for EVERY
ONE of the 16, VERIFIED (not approximately -- EXACTLY, all 448 flattened
components) that D^2_7(w_i) lies precisely in span(basis). All 16 passed.

**RESULT: eigenvalues of the full 16x16 D^2_7 matrix = {4: mult 4, 2: mult
4, 20/3: mult 4, 10/3: mult 4}. ALL STRICTLY POSITIVE. Zero eigenvalue:
False.** Trace = 64, matching 4*4+2*4+(20/3)*4+(10/3)*4 = 64 exactly
(independent sanity check, both by me and by the reviewer).

**Reviewer:** verdict NEEDS_WORK (P1) on the FIRST pass -- correctly
caught that `build_3_fifth_copy`/`build_3bar_fifth_copy` hardcoded a
reordering (c5 reversed, d5 identity) with a docstring claiming "solved
(Schur, not guessed)... verified, tool" but NO actual verification in the
committed file (the solve had happened in an earlier interactive
exploration, not carried into the script). Reviewer independently
re-verified both reorderings correct via a from-scratch reimplementation
(all 10 pattern-match checks, 5 threes + 5 threebars x 8 generators,
passed exactly), but flagged this as unreproducible from the file alone.
Also flagged a P2 docstring overclaim (the "Casimir spectrum confirms
5+5" framing, see Exhaustiveness above) and P2 untracked scratch pickle
files. ALL THREE CLOSED same round: added `matches_reference_pattern` +
explicit asserts for c5 and d5 (independently, BEFORE the reviewer's
report even arrived -- same instinct as the P1 finding), corrected the
docstring's exhaustiveness justification, deleted the scratch pickles.
Reran end-to-end after all fixes: identical result, all asserts pass
silently, ruff clean.

**Skeptic** (context-blind, no Bash/execution access this round --
disclosed explicitly, did static + hand-symbolic rep-theory analysis):
verdict CONFIRMED-REAL, with 3 WEAKENED points, none fatal:
1. Exhaustiveness -- independently re-derived BY HAND via the same
   Sigma=1a(+)3(+)3bar(+)1b tensor-product accounting the reviewer used
   (two independent people/routes converging on the same closing
   argument). Confirmed dim M=16 exactly, no hidden 17th direction
   possible.
2. `.H` vs `.T` -- confirmed correct and, independently, confirmed the
   "exact-in-span" check cannot be fooled by coincidence (W has full
   column rank 16 => c<->target is a bijection, so residual=0 on all 448
   components means c is THE unique correct answer, not a lucky guess).
3. c5/d5 reordering not verified in-file -- same finding as reviewer's
   P1, independently arrived at. Closed the same way (see above).
Additionally verified: positivity of D^2_7's eigenvalues implies
ker(D_7)=ker(D^2_7)={0} REGARDLESS of whether the basis is orthonormal
(eigenvalues are similarity-invariant; kernel argument needs no
self-adjointness assumption) -- the "no zero mode" conclusion is
basis-independent and robust even before checking self-adjointness.

**Additional check (mine, closes skeptic's normalization scope caveat
entirely):** verified D_7 is genuinely self-adjoint w.r.t. the natural
L^2 inner product on M -- computed the Gram matrix G=W^H W (confirmed
Hermitian, eigenvalues {1:4, 3:4, 3/2:8}, all real positive => valid
inner product) and confirmed G.D^2_MAT is Hermitian. This upgrades the
eigenvalue VALUES {4,2,20/3,10/3} from "only their zero-vs-nonzero-ness
is meaningful" to "the full spectrum is physically meaningful," not just
a coordinate artifact of the non-orthonormal basis.

### Net assessment

This is the most thoroughly verified result of the whole rho=7
investigation (Rounds 15-19): a genuinely exhaustive 16-dim multiplicity
space (dimension-count closed via an independent tensor-product argument,
confirmed by BOTH reviewer and skeptic via separate routes), every basis
element's SU(3)-equivariance verified in-file (not asserted), the closure
of D^2_7 on this space verified EXACTLY for all 16 directions, the
resulting matrix's self-adjointness independently confirmed, and the
eigenvalue computation cross-checked via trace. **rho=7 introduces NO
unwanted zero mode anywhere in its danger zone -- this question, open
since Round 15, is now CLOSED.**

Per this project's discipline, updating preprint.tex is a separate,
deliberate decision -- not made unilaterally this round. The result is
ready for that decision whenever the user chooses to make it.

## Round 20 (2026-07-10, user asked to "попробуй теперь rho=14"): the
## LAST remaining danger-zone sector -- G2's own 14-dim adjoint
## representation. Strongly supported result, ONE concern not fully
## closed (honestly scoped, not overclaimed)

**Construction** (`g2su3_v14_adjoint_full_matrix.py`): V_14 = adjoint(g2),
restricted to isotropy SU(3): 14 = 8(adjoint of su(3)) (+) 3 (+) 3bar (the
standard reductive g2=h(+)m decomposition). Built the full 12-dim
multiplicity space M_14 = Hom_SU(3)(V_14,F): 2 copies of "8" (NEW --
extracted from Lambda^1(x)Lambda^2 and Lambda^2(x)Lambda^1's Casimir=3
eigenspaces, Casimir spectrum {0:1,3:8} confirmed matching 8(+)1 exactly,
Schur-solved against V_14's own su(3)-on-itself adjoint action) + 5
copies of "3" and 5 of "3bar" REUSED UNCHANGED from Round 19's F-side
basis (c1-c5, d1-d5) -- valid since these are abstract su(3) irreps
independent of which G2-rep intertwines with them (re-verified in-file
via STEP 6's equivariance check on the ACTUAL composed maps, not just
inherited from Round 19's historical claim).

**A genuine sign-convention bug caught and fixed DURING construction**
(before reaching any downstream result): matching V_14's own su(3)-action
(built from raw NU-matrix commutators) against Sigma's established
su3_action gave ONLY trivial Schur solutions for every candidate pairing
-- diagnosed via a from-scratch self-consistency check, fixed by using
the RAW (unsigned) commutator convention throughout V_14's construction
instead of the project's existing BRACKET_SIGN=-1 correction. A SECOND
bug (E_SIGN double-application in the Dirac-formula application step)
was also caught and fixed via an explicit self-consistency assertion.

**RESULT: eigenvalues of the full 12x12 D^2_14 matrix = {6: mult 4,
20/3: mult 4, 10/3: mult 4}. ALL STRICTLY POSITIVE.** All 12 basis
elements' D^2_14 images verified EXACTLY in span (genuine closure).
Trace=64, confirmed two independent ways. Self-adjointness w.r.t. the
natural L2 inner product confirmed (G.D2_MAT Hermitian).

**Reviewer:** verdict LGTM (ran the file end-to-end, independently
re-derived BOTH claimed bug-fixes from first principles -- confirmed the
E_SIGN fix by tracing exact algebra, confirmed the sign-convention fix's
downstream correctness via STEP 6's generic equivariance check). 2 P2
findings, both closed same round: (1) STEP 1's self-consistency check
was framed as "confirming RAW is correct" when it's actually convention-
invariant (any global sign flip of a Lie bracket gives an isomorphic,
equally self-consistent algebra) -- docstring reworded to correctly
attribute the REAL evidence to STEP 3/4's nonzero Schur intertwiners +
STEP 6's equivariance check, and an explicit in-file check added showing
BOTH conventions pass self-consistency independently (making the
non-discrimination empirically demonstrated, not just asserted); (2)
"both pairings tried" was claimed in prose but only the forward pairing
was actually executed (the reverse is EXCLUDED by Schur's lemma given a
nonzero forward result, but wasn't literally checked) -- added an
explicit `check_only_trivial_solution` call verifying the reverse
pairing genuinely gives only the trivial solution for both groups
(confirmed True x2).

**Skeptic** (context-blind, no Bash/execution access, static + hand-
symbolic rep-theory analysis): verdict **WEAKENED** -- found something
real, not a false alarm. Key findings:
1. Confirmed (independently arriving at the same conclusion as this
   round's own proactive fix) that STEP 1's self-consistency check is
   tautological (Jacobi identity, cannot fail for ANY valid
   representation) -- correctly identified this as non-load-bearing.
2. **Genuine factual error caught**: the docstring claimed su3_action was
   "always built via a RAW matrix slice or RAW commutator" -- FALSE.
   su3_action's SU3_GENERATORS table is IDENTICAL to AD_NU_M_BIVECTOR
   (the independently-sourced AHL2023 Remark-5.2 bivector formula,
   Clifford-lifted onto Sigma) -- neither "raw" nor "BRACKET_SIGN-
   corrected" in the nu-commutator sense, a third, independent
   construction. FIXED: docstring corrected to accurately describe what
   su3_action actually is and to rely only on the DIRECT empirical
   matching (STEP 3/4 nonzero Schur solve + STEP 6 equivariance), not a
   false claim about its provenance.
3. **The sharpest, only-partially-closed finding**: is ADE[p]'s sign
   (V_14's own e_p-action, used in D_14's term1 for the REP-ACTION half)
   correctly matched against e_action(p) (the Clifford-multiplication
   half, an independently-calibrated convention)? Neither STEP 6's
   equivariance check (which never touches ADE) nor self-adjointness
   (D=+A+B and D=-A+B are BOTH self-adjoint if A,B individually are --
   cannot discriminate a relative sign) constitute proof either way.
   Unlike V_7 (where rho7_ep is a validated matrix SLICE, already
   extensively cross-checked across Rounds 17-19), V_14's ADE is a NEW,
   COMMUTATOR-based construction with no direct precedent in this
   project to lean on.

**Response to the sharp finding (Concern 3): TESTED DIRECTLY, closed
STRUCTURALLY but not with full independent-derivation certainty.**
Flipped ADE's sign, rebuilt the full 12x12 matrix from scratch: gives a
DIFFERENT spectrum, {6, 5-sqrt(217)/3, 5+sqrt(217)/3} -- IRRATIONAL.
The ORIGINAL (used) sign gives clean RATIONAL eigenvalues {6,20/3,10/3},
sharing 20/3 and 10/3 EXACTLY with rho=7's own spectrum (Round 19). Every
Casimir-derived quantity found across this entire 20-round investigation
has been rational in this normalization -- Kostant-Parthasarathy-type
formulas produce Casimir DIFFERENCES, never generic algebraic
irrationals like sqrt(217). This is REAL, meaningful structural evidence
for the sign used in this file -- but it is a PLAUSIBILITY argument, NOT
a full independent re-derivation via an actual closed-form twisted
Kostant-Parthasarathy formula for rho=14 specifically (none was found in
Round 15's literature search for rho=7 either; deriving one for rho=14
was not attempted this round). This sign-flip test is now built into the
file itself (STEP 10, `d14_apply`'s new `ade_sign` diagnostic parameter),
not just recorded here -- reproducible by anyone re-running the script.

**Skeptic's other points, addressed:**
- E_SIGN double-application fix: skeptic confirmed `[INFERRED]` correct
  (consistent with the D_7 pattern) but noted the in-file cross-check is
  tautological (both routes bake in the same E_SIGN, so it can't catch a
  wrong E_SIGN itself -- E_SIGN's own correctness rests on Round 13's
  original 48-pair calibration, not this round's check). Accepted as an
  honest scope limitation, not a new gap -- E_SIGN itself is unchanged,
  unmodified, and outside this round's scope.
- Reuse of Round 19's c1-c5/d1-d5: skeptic independently confirmed sound
  (no hidden V_7-specific dependence), and additionally noted the
  reused-basis rank (12, forced to succeed only if the 5+5 split holds)
  makes exhaustiveness self-enforcing -- a successful run is itself
  evidence for Round 19's own [INFERRED] 5+5 split claim.
- Self-adjointness/zero-mode conclusions were previously only PRINTED,
  not ASSERTED (script would exit 0 even if false) -- FIXED: both are
  now hard `assert`s (STEP 9).
- "No zero modes anywhere" scope: correctly noted this rests on rho=7
  and rho=14 EXHAUSTING the danger-zone sectors, an external taxonomy
  claim inherited from prior rounds, not established in this file.

### Net assessment

This is a strongly-supported, extensively-verified result -- reviewer
LGTM (both findings closed with real fixes, not just reworded), skeptic
WEAKENED-then-substantially-addressed (the one sharp concern tested
directly, with a real, non-trivial, but not fully airtight structural
argument in its favor). This is deliberately NOT presented with the same
unqualified confidence as Round 19's rho=7 closure (which had a clean
CONFIRMED-REAL skeptic verdict) -- rho=14's term1-sign question is
STRONGLY SUPPORTED, not proven beyond all reasonable doubt. If a
genuinely decisive closure is wanted later, the concrete next step is
deriving (or finding in the literature) an actual closed-form twisted
Kostant-Parthasarathy formula for the adjoint representation on
G2/SU(3), and checking {6,20/3,10/3} against it directly -- not
attempted this round.

**With that honest caveat stated: all 12 eigenvalues of D^2_14 are
strictly positive under the sign this file uses, and that sign is the
one supported by every available piece of evidence (equivariance,
self-adjointness, and now the rationality/plausibility argument).
rho=14 shows no unwanted zero mode.** Combined with Round 19's rho=7
closure, both non-trivial G2-representation danger-zone sectors this
project has identified now show no zero mode -- stated with the scope
caveat that "rho=7 and rho=14 exhaust the danger zones" is itself an
inherited claim from earlier rounds' classification, not re-derived
here.

Per standing discipline: preprint.tex NOT touched this round. Updating
it, and deciding how to state rho=14's slightly-more-qualified
confidence level relative to rho=7's, is a separate decision for the
user.

## Round 20 continued (2026-07-10, user asked to "попробовать вывести
## Kostant-Parthasarathy формулу для rho=14"): the approach is
## STRUCTURALLY INAPPLICABLE to this specific operator -- a genuine,
## substantive finding, not a failed attempt

**Investigated whether an independent closed-form Kostant-Parthasarathy
formula could adjudicate the ADE-sign question.** Before investing in
the full G2 root-system / highest-weight machinery needed to derive it
(rank-2 root system, Weyl vector rho_G2/rho_su3, none of which exists
anywhere in this project yet), checked whether the comparison would even
be VALID -- and found it would not be, for a structural reason
independent of the sign question entirely:

**Kostant's cubic Dirac operator, by its own defining theorem, acts as a
SCALAR (a pure Casimir difference) on EVERY H-isotypic piece of
V(x)S(m), for ANY multiplicity -- i.e. it is BLOCK-DIAGONAL with respect
to which SU(3)-type appears, by construction, always.** But Round 18
ALREADY PROVED, independently of any sign question, that THIS
experiment's own operator (built via Agricola's naturally-reductive
Levi-Civita construction, t=1/2) does NOT have this property: D_7(w_a)
[phi_2-supported by construction] comes back NONZERO on the "3"-piece
domain (v=e_1) -- direct, tool-verified evidence of cross-SU(3)-piece
mixing that Kostant's canonical (t=1/3, "cubic") operator structurally
CANNOT exhibit.

**Consequence: this experiment's operator and Kostant's cubic Dirac
operator are provably DIFFERENT operators (different torsion, t=1/2 vs
t=1/3), not the same operator in different notation.** A Kostant-
Parthasarathy eigenvalue comparison would therefore be comparing the
wrong mathematical object: a MISMATCH would not indicate an error in
this round's construction (expected, since it's genuinely a different
operator), and a MATCH would itself be the suspicious, unexplained
result. Pursuing this comparison further would not have been
informative regardless of effort invested -- correctly identifying this
BEFORE building the full G2 Lie-theory machinery (which would have been
wasted effort) is itself the useful outcome of this sub-investigation.

**One genuine additional structural fact found along the way (sign-
independent, kept since it's free extra evidence, tool-verified):**
trace(D^2_14) = 64 under BOTH the used sign and the flipped sign
(checked directly). Since trace(AB)=trace(BA) always, trace(D^2) =
trace(term1^2) - 2*trace(term1.term2) + trace(term2^2), and flipping
ADE's sign flips the SIGN of the cross term trace(term1.term2) while
leaving trace(term1^2) unchanged -- so trace-invariance under the flip
means trace(term1.term2)=0 EXACTLY. Interesting (an unexpected
orthogonality between the two halves of the formula, in trace), but does
NOT discriminate the sign (both possibilities are consistent with it) --
recorded for completeness, not as resolving evidence.

**A genuinely decisive alternative would require deriving the CORRECT,
t=1/2-specific (torsion-corrected) Casimir-shift formula for this exact
operator** -- comparable in scope to correctly redoing Round 16's R^E/
Scal machinery (which was attempted for rho=7, found buggy, and
abandoned in favor of the direct matrix-coefficient-section construction
that has been used successfully since Round 17). This is a substantial,
separate undertaking, not a quick check -- not attempted this round.

**Status unchanged from the "Net assessment" above: rho=14 remains
STRONGLY SUPPORTED, not airtight.** This sub-investigation closes with a
genuine negative result (the natural-seeming verification path doesn't
apply here) rather than a resolution -- reported honestly rather than
silently abandoned.

## Round 21 (2026-07-10, user asked to "L4A попробуй", then chose the
## R^E-with-new-calibration-points route, then the bug-hunt route):
## three results, including a structural THEOREM explaining why Round
## 16's construction could never have been debugged into working

**The setup.** L4A (preprint sec:lichnerowicz) asks for spectral data of
the curvature endomorphism F_{S^-} in the twisted Weitzenbock identity
D^2 = nabla*nabla + Scal/4 + R^E. Round 16 built an explicit R^E and
failed calibration (2/3 mismatch, then a 1/6 inconsistency) with only
ONE calibration point available (rho=trivial, where nabla*nabla=0
identically -- the skeptic's decisive objection at the time was exactly
that this point cannot constrain the nabla*nabla coefficient). Rounds
17-20 have since produced what Round 16 lacked: independently validated
full multiplicity-space D^2 matrices for rho=7 and rho=14.

**RESULT 1 -- triangulation (POSITIVE).** The residual
  W := D^2 - nabla*nabla_can - Scal/4,
with nabla*nabla_can = C_2(G2;rho) - C_2(SU(3);sigma) (the canonical-
Casimir Laplacian used throughout Rounds 15-16) and Scal=10, evaluated
on the SU(3)-singlet fiber block {v_a, v_b} from TWO independent
calibration sources -- rho=trivial (D^2=[[1,1],[3,3]], nabla*nabla_can=0)
and rho=7's singlet-domain sub-block (D^2=[[3,1],[3,5]],
nabla*nabla_can=2) -- comes out EXACTLY IDENTICAL:
  W|_singlet = [[-3/2, 1], [3, 1/2]].
[VERIFIED-tool, g2su3_weitzenbock_type_obstruction.py STEPs 1-3, all
asserted.] Honest scoping: this agreement is algebraically equivalent to
Round 17's uniform-shift observation ({2,6}={0,4}+2), reframed as a
statement about W -- a consistency confirmation of the framework, not a
fully independent new measurement. Also note the agreement is
insensitive to the Scal normalization (a Scal error shifts both W's
equally), so what it validates is the C_2-shift structure, not Scal.

**RESULT 2 -- Round 16's build_RE() is definitively NOT W (NEGATIVE,
with a clean signature).** build_RE() on the same block gives
[[-11/6, 2/3], [2, -1/2]]: not equal, and NOT a uniform rescaling
(entry ratios 9/11, 3/2, 3/2, -1 -- kills the old "Interp A vs B"
framing for good, both interpretations assumed a uniform factor).
The discrepancy has an exact form: W - RE_computed = (1/3)*D^2|_trivial
-- recorded as an unexplained but suggestive signature. Negative
control: symmetrizing build_RE between the two tensor factors gives
EXACTLY 2x the original (both orderings contribute identically on this
block) and still fails. Components re-verified individually before the
bug-hunt was called off: R_half's Ricci contraction still reproduces
Agricola's own formula; spin_lift_so6 still calibrates against
nabla_g_action for all 6 directions. [VERIFIED-tool, STEPs 4-5.]

**RESULT 3 -- the structural obstruction (the actual explanation, and
the reason the bug-hunt framing was abandoned).** Round 19's validated
16x16 D^2_7 matrix on M = Hom_SU(3)(V_7, F) has NONZERO OFF-BLOCKS
between SU(3)-types -- re-verified this round by direct computation:
D^2(singlet_1) has threebar_1/threebar_2 coefficients 2i/3, with the
exact-in-span assert passing (so the expansion is unambiguous;
additionally the singlet-type and 3bar-type basis elements have disjoint
domain-slot support, slot 0 vs slots 1-6, so cross-type coefficients
cannot be a non-orthogonality artifact). But EVERY candidate right-hand-
side term of the Weitzenbock identity as interpreted in Rounds 15-16 is
TYPE-PRESERVING on M:
- Scal/4 is a scalar;
- any pointwise G2-invariant bundle endomorphism (= what any curvature-
  built fiber operator IS on a homogeneous space) acts on M by post-
  composition with an SU(3)-equivariant fiber map, which by Schur
  preserves each SU(3)-isotypic component of F;
- nabla*nabla_can is block-scalar by type.
THEREFORE no invariant fiber endomorphism R^E whatsoever can complete
the identity with nabla*nabla identified as the canonical-Casimir
Laplacian: the left side provably mixes types, every right-side term
provably does not. **Round 16's failure was never a coding bug -- the
formula AS INTERPRETED is structurally impossible.** [Off-blocks:
VERIFIED-tool, STEP 6. Schur argument: INFERRED -- standard operator
theory on the verified facts; under independent review as of this
write-up.]

**What this implies (the honest, useful conclusion):** the Lichnerowicz
/Weitzenbock identity itself is a theorem and not in question; what
fails is identifying its nabla*nabla with the CANONICAL-connection
Casimir Laplacian. The true Levi-Civita rough Laplacian differs from
the canonical one by Nomizu-map cross-terms (first-order, schematically
-sum_p [Z_p Lambda_p + Lambda_p Z_p + Lambda_p^2] corrections) -- which
are exactly the natural carrier of the observed type-mixing, and which
are DERIVABLE with machinery this project already has (Z_p action on
matrix-coefficient sections = -rho(e_p), Lambda_p = the calibrated
nabla_g spin lift plus twist). This converts L4A from "debug an
abandoned construction" (provably hopeless) into a well-defined
derivation with all ingredients in hand.

**Interpretation caveat on Result 1 (so it is not over-read):** the
triangulated [[-3/2,1],[3,1/2]] is the singlet-block of the RESIDUAL W,
which Result 3 proves is NOT a fiber operator globally (it has
off-blocks). Its rho-independence across {trivial, 7} is the verified
fact; whether the block equals genuine fiber-curvature data depends on
the cross-terms' singlet-block contribution -- exactly what the
derivation above would settle.

**Kill Analysis (what died, what survived):**
- KILLED: the "find the bug in build_RE()" framing (Result 3 proves no
  bug-fix can work); the "Interp A vs B uniform-scale" hypothesis space
  from Round 16 (Result 2's non-uniform ratios).
- SURVIVED: every individual component of Round 16 (R_half, spin lift,
  Scal=10) -- the parts were fine, the assembly formula was wrong;
  the Weitzenbock identity itself (as a theorem, with the correct
  LC Laplacian); the entire Rounds 17-20 edifice (used here as
  calibration data, internally consistent).
- OPENED: a concrete, tractable derivation path (LC cross-terms via
  matrix-coefficient machinery) that would (a) produce the correct
  Weitzenbock identity, (b) yield F_{S^-} spectral data = L4A's actual
  ask, and (c) as a side effect give an INDEPENDENT recomputation of
  D^2 that could cross-check rho=14's one flagged sign caveat.

**Review status:** reviewer + context-blind skeptic dispatched on
g2su3_weitzenbock_type_obstruction.py at write-up time; verdicts to be
appended in a follow-up commit. All numeric claims are asserted in the
committed script itself (a clean exit IS the numeric verification);
the Schur-argument interpretation is the piece under review.

**L4A status: still OPEN, but transformed** -- from "an abandoned
construction with an unexplained failure" to "a diagnosed structural
obstruction plus a concrete derivation path with all ingredients
already built and calibrated." preprint.tex NOT touched this round.

---

## Round 21 -- Reviewer + Skeptic verdicts (Step 8a, appended)

Both agents ran the committed script (`python
g2su3_weitzenbock_type_obstruction.py`, exit 0, all in-file asserts
pass) and independently re-derived the headline arithmetic by hand.
Skeptic given claim+code only, no session history (context asymmetry).

**Reviewer verdict: `LGTM`, severity P2, iteration 1/3.**
- Pass 1 (spec compliance): PASS -- delivers exactly what the docstring
  promises, no scope creep, reuses Rounds 16-19 machinery via import
  only, ruff clean.
- Pass 2 (quality): re-derived all four headline numbers by hand, all
  exact. Three P2 (cosmetic) findings, all fixed in this commit: garbled
  `SCAL` comment, missing local `det(T)!=0`/`det(T2)!=0` re-assert
  (Round 19's own `main()` has it; this file silently relied on the
  implicit singular-matrix check inside `(WH*Wmat).inv()`), duplicate
  import statement.
- Pass 3 (adversarial, 6 challenges targeting the Schur/type-
  preservation argument specifically): all 6 ACCEPT/REJECT-the-attack --
  the "non-orthogonal basis could fake the off-type coefficient" attack
  fails because the coefficient extraction is EXACT (residual asserted
  zero) against a FULL-COLUMN-RANK basis, making orthogonality
  irrelevant to uniqueness; the block-diagonal-RHS-vs-witnessed-non-
  block-diagonal-LHS argument is a complete modus tollens, not
  suggestive.

**Skeptic verdict: `CONFIRMED-REAL` (core claim), two `WEAKENED`
caveats (Results 1-2 framing). Could not execute code (no Bash access
in that context) -- flagged own numeric inputs as `[INFERRED]` from
static reading, distinct from the structural argument which is
basis-free and needed no execution.**
- **Result 3 (main claim): CONFIRMED-REAL, and found a STRONGER version
  of the argument than the docstring's own Schur framing.** The real
  reason R^E must be type-preserving isn't Schur's lemma -- it's that
  the SU(3)-type grading lives on the DOMAIN of M=Hom_SU(3)(V_7,F), and
  any invariant fiber endomorphism acts by POST-COMPOSITION (touches
  only the target), which trivially cannot move a map out of its
  domain-block. This survives every escape route tried: multiplicities
  (copy-mixing is target-side, irrelevant to domain grading), reality/
  3-vs-3bar conjugation (still post-composition), and nabla*nabla_can
  itself (a special case of "scalar minus post-composition by fiber
  Casimir", hence also domain-preserving). Independently re-derived the
  disjoint-support argument for the off-block being genuine (not a
  normal-equations artifact): singlet basis columns are literally zero
  outside rows 0-63, three/threebar columns are zero on rows 0-63 --
  D^2 of a phi_2-supported vector having nonzero support outside rows
  0-63 cannot be manufactured by the extraction method, only by real
  geometry.
- **Result 1 (triangulation): WEAKENED.** Genuine content, correctly
  scoped: the two-point agreement uniquely fixes the nabla*nabla_can
  coefficient at alpha=1 (something Round 16's single point could not
  do) and confirms rho-independence on the singlet DIAGONAL block --
  but does NOT independently validate the absolute entries
  `[[-3/2,1],[3,1/2]]`, which remain single-sourced in Scal=10 and
  C_2(G2;7)=2 (Scal/4 appears identically on both calibration points
  and cancels out of the agreement check). Docstring's own
  "INTERPRETATION CAVEAT" already partially covers this; the added
  scope note above sharpens it.
- **Result 2 (negative control): CONFIRMED as a control.** The exact
  `(1/3)*D^2_trivial` discrepancy signature is real but Scal-contingent
  numerology (would not land on that clean form if Scal were
  mis-normalized) -- correctly non-load-bearing, already hedged as a
  negative control rather than a positive finding.
- **Rhetoric note (non-fatal):** "small structural THEOREM" oversells
  slightly -- more precisely "a clean, tool-verified detector of the
  known fact that the canonical connection on nearly-Kahler S^6 is not
  torsion-free, made concrete on the rho=7 multiplicity space."
  Recommend keeping this framing in mind for any future write-up
  (preprint.tex NOT touched, so no immediate action needed).
- **Self-contained fallback offered by skeptic** (importing nothing
  beyond Rounds 18-19's own disjoint-support facts, in case anyone ever
  disputes the nabla*nabla_can formula import): *"D^2 of a
  domain-singlet intertwiner has nonzero non-phi_2-domain support; no
  zeroth-order fiber endomorphism, Scal/4, or the domain-block-diagonal
  canonical Laplacian can produce non-phi_2-domain support from a
  phi_2-supported map; therefore the L4A build_RE route is structurally
  dead."* Recorded here as the fallback framing if the imported-formula
  objection is ever raised.

**Response matrix (FL Step 8a):**
| Concern | Response |
|---|---|
| Garbled SCAL comment | **Fixed** (this commit) |
| Missing det(T)/det(T2) re-assert | **Fixed** (this commit, re-ran clean) |
| Duplicate import | **Fixed** (this commit) |
| Result 1 absolute-value single-sourcing in Scal/C2 | **Accepted limitation** -- documented above; does not touch Result 3 |
| "THEOREM" rhetoric slightly strong | **Accepted, noted for future write-ups** -- not changing the already-committed docstring wording, but flagging the more precise framing here for whoever drafts the eventual preprint text |
| Non-orthogonal-basis / basis-artifact attack on off-block | **Dismissed** (skeptic + reviewer both independently confirmed: exact residual + full column rank makes extraction unique regardless of orthogonality) |

**Net effect: Result 3 (the structural obstruction) is not just
survived but STRENGTHENED post-review** -- the post-composition argument
is more general and more robust than the original Schur framing, and
needs neither Scal normalization nor the nabla*nabla_can formula import
to hold in its fallback form. Results 1-2 keep their WEAKENED/negative-
control status, already correctly scoped in the original docstring.
No changes to the cross-terms derivation path recommended above.

---

## Round 22 (2026-07-10) -- L4A continued: explicit Nomizu cross-terms
## derived and quantitatively verified as the type-mixing carrier

**User instruction:** "го вариант 1, выводи cross-terms" (proceed with
option 1: derive the Levi-Civita vs canonical-Casimir Nomizu cross-terms
explicitly), following Round 21's own forward-pointing docstring.

**GOAL.** Round 21 proved no invariant fiber endomorphism can complete
D^2 = nabla*nabla_can + Scal/4 + R^E, and predicted the missing piece is
a Nomizu cross-term "schematically -sum_p[Z_p.Lambda_p + Lambda_p.Z_p +
Lambda_p^2]". This round derives it EXPLICITLY, in closed form, entirely
within the already-validated matrix-coefficient-section machinery, and
verifies it reproduces the observed type-mixing quantitatively (not just
qualitatively).

**DERIVATION (script: `g2su3_nomizu_crossterms.py`).** Writing
D_7 = TERM_A + TERM_B from Round 17's own defining formula and expanding
D_7^2 = (TERM_A+TERM_B)^2 by hand (Clifford relations + the
representation identity [rho_7(e_p),rho_7(e_q)]=rho_7([e_p,e_q])) splits
D_7^2 into FIVE closed-form pieces:
- CASIMIR (from T_A's p=q part) -- type-preserving
- D64-SQUARED (from T_B^2) -- type-preserving, F-side only
- SU(3)-CURVATURE (from T_A's p<q part, the su(3)-bracket half)
- TORSION CROSS-TERM (from T_A's p<q part, the m-bracket half, using the
  already-built torsion table T(p,q,r))
- MIXED A-B CROSS-TERM (from T_A.T_B + T_B.T_A, an anticommutator
  {e_p,D64} contracted against rho_7(e_p))

**TWO DEAD ENDS, both caught by the project's own verification discipline
before any claim was made (Kill Analysis below), not shipped as findings:**

1. **Vacuous domain-index-0-only test.** First verification attempt
   compared only the phi_2 (domain-index-0) slice of the reconstruction
   against ground truth. It passed trivially and appeared to show
   TORSION alone caused v_a/v_b's threebar leakage from Round 21's
   "singlet_1" -- but v_a/v_b turned out to be singlets s5/s2, NOT
   Round 21's actual "singlet_1"=s1 (F has 6 SU(3)-singlets total,
   `build_singlets()`), and separately the domain-index-0-only slice
   is structurally BLIND to Round 21's "three_i"/"threebar_i" basis
   elements (which are supported ONLY on domain indices 1-6) -- so any
   test restricted to index 0 trivially reports zero off-type
   coefficients regardless of what the real operator does. Caught by:
   (a) re-checking `build_singlets()`'s actual definitions against v_a/
   v_b, (b) a direct diagnostic confirming `D^2(singlet_1)` has 2
   nonzero F-components on EACH of domain indices 1-6, not just index 0.
2. **Sign convention mismatch between two independently-built
   representations.** The full 7-domain-index (448-dim) test, run with
   the naive assumption [rho_7(e_p),rho_7(e_q)] = +rho_7([e_p,e_q]),
   FAILED its own decisive assert with a uniform discrepancy of exactly
   4/3 at exactly one row per non-singlet domain index (i=1..6).
   Root-caused via a 4-step bisection (all tool-verified, not guessed):
   (i) confirmed TERM_A+TERM_B alone exactly reproduces a SINGLE
   application of D_7 for all 7 domain indices (rules out the
   primitives); (ii) isolated T_A(T_A(w)) computed directly via
   primitives vs via the algebraic casimir+su3curv+torsion split --
   mismatch localized to the p!=q (bracket) part specifically;
   (iii) directly compared `[rho_7(e_1),rho_7(e_2)]` (V_7's own
   representation, Round 14, `g2su3_v7_multiplicity_dirac.py`) against
   its reconstruction from the T(p,q,r)/curv_h(p,q,k) tables
   (`g2su3_H_element.py`/`g2su3_appendix_a_construction.py`) as explicit
   7x7 matrices: they are EXACT NEGATIVES of each other -- a genuine,
   tool-confirmed convention mismatch between two independently-built
   g2 representations, the same class of issue
   `g2su3_appendix_a_construction.py`'s own pre-existing
   `BRACKET_SIGN=-1` comment already flags for a DIFFERENT pairing.
   Fix: drop the leading minus sign in `su3_curvature_term` and
   `torsion_cross_term` (the two minus signs -- one from the p<q
   expansion, one from the convention mismatch -- cancel).

**RESULT (after the fix, script exits 0, all asserts pass,
[VERIFIED-tool]):**
- STEP 2 (decisive): sum of all 5 pieces == D^2(singlet_1) EXACTLY,
  over the FULL 448-dim (7-domain-index) object -- not a projection, not
  a slice.
- STEP 3/4: extracting coefficients via Round 21's own 16-dim basis
  (reused unmodified): CASIMIR, D64-SQUARED, and SU(3)-CURVATURE are
  each INDIVIDUALLY and EXACTLY type-preserving (zero off-type
  coefficients). TORSION alone gives `{threebar_2: -4i/3}` and
  MIXED_A-B alone gives `{threebar_1: 2i/3, threebar_2: 2i}` -- NEITHER
  alone matches Round 21's original leakage -- but their SUM gives
  EXACTLY `{threebar_1: 2i/3, threebar_2: 2i/3}`, matching Round 21's
  Result 3 finding to the letter.

**Original hypothesis (torsion alone) tested and FALSIFIED; corrected
finding is more precise, and matches the SHAPE of Round 21's own
prediction better than the original hypothesis did:** Round 21's
docstring predicted "schematically -sum_p[Z_p.Lambda_p + Lambda_p.Z_p +
Lambda_p^2]" -- THREE terms, not one. TORSION is the Lambda_p^2-type
piece (from T_A squared); MIXED_A-B is the Z_p.Lambda_p+Lambda_p.Z_p-type
piece (from T_A.T_B+T_B.T_A). The corrected result recovers exactly this
two-piece (three-term) structure, not a single-term one.

**What this establishes for L4A:** the Weitzenbock identity's correct
form on this multiplicity space is now EXPLICIT and closed-form:
  D_7^2 = [Scal/4 + nabla*nabla_can]  +  [SU(3)-CURVATURE]
        + [TORSION CROSS-TERM]  +  [MIXED A-B CROSS-TERM]
with every piece an explicit, computable operator built from
already-validated primitives (rho7_ep, rho7_nuk, T-table, curv_h-table,
D64, Clifford left-mult). The "R^E" of the ORIGINAL Weitzenbock identity
is not a single fiber endomorphism but the SUM of SU(3)-CURVATURE +
TORSION + MIXED_A-B -- genuinely NOT reducible to a pointwise fiber
operator alone (consistent with, and now explaining constructively,
Round 21's impossibility theorem). L4A's actual ask (F_{S^-} spectral
data) requires assembling this full operator over the SU(3)-singlet
domain block and diagonalizing it -- the ingredients now all exist and
are individually verified; the assembly + diagonalization is the natural
next step, NOT YET DONE this round (scope discipline: this round's
claim is the closed-form derivation + its quantitative verification on
ONE domain-singlet test case, not yet the full spectral computation).

**Kill Analysis:**
- KILLED: the "torsion alone carries the leakage" hypothesis (falsified
  directly, not merely unconfirmed); the domain-index-0-only test
  methodology (shown vacuous for THIS class of question; still valid
  for OTHER questions like Round 17's original single-application
  checks, which never claimed to test off-type content).
- SURVIVED: the overall 5-piece algebraic decomposition (exact, once
  the sign fix is applied); Round 21's Result 3 finding itself
  (re-derived independently via a completely different route -- direct
  term-by-term construction rather than coefficient-extraction on the
  full D^2 -- and matches to the letter, a strong independent
  cross-check of Round 21, not just a consequence of it); every
  already-existing primitive (rho7_ep, T-table, curv_h-table, D64,
  clifford_left_64) -- none needed modification, only correct combination.
- OPENED: the explicit closed-form Weitzenbock identity above; a natural
  path to L4A's actual spectral ask (assemble + diagonalize the full
  4-term operator on the singlet block, extending to "3"/"3bar" blocks);
  a NEW independent recomputation ROUTE for rho=14's flagged sign
  (same TERM_A/TERM_B decomposition technique applies verbatim to V_14,
  not yet attempted).

**Review status:** reviewer + context-blind skeptic dispatched on
g2su3_nomizu_crossterms.py; verdicts to be appended in a follow-up
commit, per the same Step 8a discipline as Round 21.

**L4A status: still OPEN, advanced further** -- from "a diagnosed
structural obstruction plus a concrete derivation path" (Round 21's
close) to "the derivation is done, closed-form, and quantitatively
verified on one test case; only the spectral assembly step remains."
preprint.tex NOT touched this round.

---

## Round 22 -- Reviewer + Skeptic verdicts (Step 8a) and STEP 5 fix

Both agents ran independently. **Reviewer: `NEEDS_WORK`, severity P1**
(executed the file, confirmed all printed numbers matched this doc
character-for-character). **Skeptic: `WEAKENED`** (no execution access
this pass, hand-traced instead; explicitly marked numeric inputs
`[INFERRED]`, consistent with its own prior-round discipline).

**Both independently converged on the SAME P1/CHALLENGE finding** (a
strong signal it is real, not reviewer noise): the docstring's claim
that "SU(3)-CURVATURE is individually type-preserving... settled below
by direct computation -- not assumed" was tested VACUOUSLY. On the only
input used (singlet_1), `su3_curvature_term` is not merely off-type-
clean but IDENTICALLY ZERO -- a structural fact true for ANY singlet-
supported input (su(3) generators never touch the SU(3)-isolated phi_2
direction, established Round 17), independent of whether the function
is even implemented correctly. The "VERIFIED" label given equal
confidence to this sub-claim as to the genuinely-tested torsion/mixed_AB
pieces was an overclaim -- the same class of gap the file's own dead-end
#1 (index-0-only slice) had already caught for a DIFFERENT piece, but
this one slipped through.

**Other, non-blocking findings from both reviews (addressed by response,
not by code change):**
- Skeptic Target 3: STEP 2 (sum-of-5-pieces-equals-ground-truth) is a
  *soundness check* on the derivation's bookkeeping (necessarily true
  once the algebra is right), not itself the novel content -- the real
  new information is STEP 3/4 (which pieces carry which off-type
  coefficients). **Response: accepted, reflected in this write-up's own
  framing; no code change needed, this was already how the file's own
  STEP labels were organized.**
- Skeptic Target 4: the schematic identification "TORSION <-> Lambda_p^2,
  MIXED_A-B <-> Z_p.Lambda_p+Lambda_p.Z_p" (matching Round 21's predicted
  shape) is **post-hoc** -- asserted by which algebraic step each piece
  came from, not independently verified against an explicit Lambda_p
  construction. **Response: accepted; the CONCLUSION block's wording was
  softened to explicitly say "NOT independently verified, offered as a
  natural reading only."**
- Skeptic Target 5 / reviewer P2: the CONCLUSION drifted toward general
  framing without a "verified on singlet_1 only" qualifier directly
  attached. **Response: fixed** -- CONCLUSION now states explicit scope
  ("verified on two specific test vectors... NOT yet a general theorem").
- Reviewer P2s (redundant `M_cas` recompute per loop iteration, inline
  16-dim-basis-construction duplication with Round 21's own script,
  missing standalone regression assert for the commutator-sign fact):
  **accepted as documented limitations, not fixed this round** -- none
  affect correctness, and the basis-construction duplication is a
  pre-existing pattern from Round 21 itself, not introduced here.

**Fix for the P1 (STEP 5, new):** added a second, genuinely non-vacuous
test input. Confirmed first that `su3_curvature_term` is NOT identically
zero as an operator (a fully-symbolic generic 7-tuple input gives 48
nonzero entries at domain index 1) -- so the function itself is fine,
only the CHOICE of test vector was degenerate. Scanned all 16 of Round
21's basis elements: `su3_curvature_term` is identically zero on ALL 6
singlets and on 2 of the 5 "three"/"threebar" copies each (three_1,
three_3, threebar_1, threebar_3), but genuinely nonzero on the other 6
(three_2/4/5, threebar_2/4/5) -- itself a notable, unexplained structural
pattern, not investigated further this round (out of scope). Picked
`three_5` (most nonzero entries: 12) as the new test input.

**A SECOND self-caught bug, found while building STEP 5:** the first
version of STEP 5's "off-type" filter used `k.startswith("three")` to
mean "same isotypic type as the three_5 input, exclude from leakage
count" -- but `"threebar_1".startswith("three")` is ALSO `True` (both
labels share the same 5-character prefix), so the filter silently
misclassified genuine "3 -> 3bar" cross-isotypic leakage as "same type,
different copy" and reported an empty off-type set. Caught by reading
the RAW (unfiltered) `full_coeffs_3` printout before trusting the
filtered result -- it showed nonzero `threebar_1`/`threebar_2`
coefficients that the filtered `full_offtype_3` had silently dropped.
Fixed: `k.startswith("three_")` (trailing underscore, which "threebar_*"
does not have).

**Corrected STEP 5 result (script re-run clean after both fixes, exit 0,
all asserts pass):**
- Sum of 5 pieces == D^2(three_5) EXACTLY, full 448-dim (second
  independent confirmation of the whole decomposition's soundness,
  addressing skeptic's Target 1 residual concern about STEP 2 only
  being tested on one input regime).
- `su3_curvature_term(three_5)` genuinely nonzero (real exercise, not
  structurally forced to 0).
- Full `D^2(three_5)` coefficients: `{three_5: 8/3, threebar_1: -2i/3,
  threebar_2: 2i/3}` -- a NEW, genuine cross-isotypic leakage finding
  (three_5 leaks into threebar_1/threebar_2), distinct from and not a
  repeat of singlet_1's leakage.
- `casimir`, `termB_sq`, `su3_curv` STILL have exactly zero off-type
  coefficients on three_5 -- now a genuine, non-vacuous confirmation
  (su3_curv's overall output IS nonzero here, but its off-isotypic-type
  part is exactly zero).
- `torsion` + `mixed_AB` jointly match the full off-type coefficients
  exactly on three_5 too (`{threebar_1: -2i/3, threebar_2: 2i/3}`),
  same pattern as singlet_1.

**Response matrix (FL Step 8a):**
| Concern | Response |
|---|---|
| su3_curv "type-preserving" verified vacuously (reviewer P1 + skeptic Target 2, CONFIRMED by both) | **Fixed** -- STEP 5 added, genuinely nonzero test case, re-verified clean |
| STEP 5's own off-type filter bug (self-caught during the fix) | **Fixed** -- `"three"` -> `"three_"` |
| Torsion<->Lambda_p^2 schematic mapping is post-hoc (skeptic Target 4) | **Accepted, softened wording** -- explicit "not independently verified" caveat added |
| CONCLUSION lacked explicit scope qualifier (skeptic Target 5, reviewer P2) | **Fixed** -- explicit scope line added |
| STEP 2 is a soundness check, not the novel content (skeptic Target 3) | **Accepted framing, no code change** |
| Redundant M_cas recompute, basis-construction duplication, missing standalone commutator-sign assert (reviewer P2s) | **Accepted as documented limitations** -- non-blocking, not fixed this round |

**Net effect:** the headline claim is now verified on TWO independent,
structurally different test inputs (a domain-singlet and a domain-"3"),
with the previously-vacuous su3_curv sub-claim now genuinely exercised
on the second. Two additional bugs were self-caught in the process of
addressing the review (identically-zero test input; a prefix-collision
filter bug), both fixed and re-verified. This is the fourth and fifth
dead-end this round (bringing the total to four documented in the
file's own docstring, per the "FOUR DEAD ENDS" section) -- consistent
with, not a departure from, this whole project's established pattern of
treating self-caught errors as evidence the verification discipline is
working, not as embarrassments to hide.

---

## Round 22 -- Second review round (Step 8a iteration 2/3, via Workflow)

Dispatched reviewer + context-blind skeptic in parallel via the Workflow
tool on commit 8ea4cd7. **Reviewer's agent run returned an empty result**
(no final answer produced -- a tool/agent-level failure, not a finding;
confirmed by reading the workflow's own journal.jsonl, which showed
`{"result":""}` for that agent). Not re-run immediately; instead the
skeptic's findings (which DID return, in full) were addressed first
since re-running review on soon-to-change code would waste the cycle.

**Skeptic verdict: `WEAKENED`.** Confirmed the P1 fix from iteration 1
is genuine, not cosmetic (Target 1: CONFIRMED-REAL -- su3_curvature_term
is structurally capable of being nonzero on three_5, no mechanism forces
it to 0 there the way phi_2's row/col-0 isolation forces it on
singlet_1). Confirmed the self-caught filter bug had real consequences
(Target 3: CONFIRMED-REAL -- `"threebar_1".startswith("three")` is
genuinely `True` in Python; the unfixed filter would have silently
reported "three_5 doesn't leak" when it does). Confirmed the CONCLUSION's
scope statement is honest (Target 5: CONFIRMED-REAL).

**Two new, real findings (both WEAKENED, neither fatal):**
- **Target 2 -- the "torsion+mixed_AB joint match" is ARITHMETIC
  NECESSITY, not independent evidence.** Given STEP 2's exact-sum assert
  (5 pieces sum to ground truth) PLUS the 3 individual off-type-zero
  claims (casimir, termB_sq, su3_curv), the joint match
  `full_offtype == torsion_offtype + mixed_AB_offtype` follows by pure
  arithmetic (subtract 3 zeros from the total, whatever remains is by
  definition the sum of the other two). The genuinely NEW, independent
  content per test input is 4 claims (STEP 2's soundness + 3 zero-
  claims), not the "6 confirmations" the CONCLUSION's tone implied.
  **Response: accepted, FIXED in CONCLUSION wording** (explicit note
  added: "given STEP 2's exact-sum assert plus the 3 individual zero-
  claims, this joint match is ARITHMETIC NECESSITY, not additional
  independent evidence").
- **Target 4 -- three_5 was picked as "most nonzero entries" among 6
  candidates (out of 16), an N=2-total-tests scope with a favorably-
  biased selection.** Selection direction favors catching leaks (more
  nonzero surface area = more chances for a bug to show), but a subtle
  bug manifesting only in a cancellation-heavy regime could in
  principle survive both of the 2 tested cases. Skeptic's own
  recommendation: "run all 6 nonzero cases + 1 null-control... cheap,
  machinery already built." **Response: FIXED, more thoroughly than
  recommended** -- STEP 6 added, checking casimir/termB_sq/su3_curv
  off-type-cleanliness on ALL 16 of Round 21's basis elements (not just
  6+1=7). Result: all 16 pass, closing the selection-bias concern
  completely for this specific 3-piece sub-claim (the full 5-piece
  decomposition including torsion/mixed_AB remains verified on 2 inputs
  only -- STEP 6 deliberately scoped to the cheaper 3-function check,
  not a 16x repeat of the expensive full ground-truth comparison).

**Response matrix (FL Step 8a, iteration 2):**
| Concern | Response |
|---|---|
| Target 2: joint match framed as extra evidence | **Fixed** -- CONCLUSION now explicitly states arithmetic necessity |
| Target 4: N=2 with favorable selection | **Fixed** -- STEP 6, all 16 basis elements checked, all pass |
| Target 1, 3, 5 | **Confirmed by skeptic as already correct, no change needed** |
| Reviewer agent empty result | **Deferred to iteration 3** -- re-dispatching reviewer (and a fresh skeptic pass, since the code changed again) on the STEP-6-updated version |

**Script re-run after STEP 6, exit 0, all 16 basis elements pass:**
singlet_1..6, three_1..5, threebar_1..5 -- casimir/termB_sq/su3_curv
off-type-clean on every one, no exceptions.

---

## Round 22 -- Third and FINAL review round (Step 8a iteration 3/3, FL cap)

Dispatched skeptic via Workflow and reviewer via Workflow (reviewer
returned empty AGAIN -- second consecutive empty result specifically
for `agentType: 'reviewer'` inside the Workflow tool, while the same
agent type worked cleanly via the direct Agent tool in iteration 1;
looks like a Workflow-layer quirk, not a content problem). Re-dispatched
reviewer via the direct Agent tool (the channel that worked before) as
a third attempt, in parallel with processing the skeptic's already-
returned verdict.

**Skeptic verdict: `CONFIRMED-REAL`, explicit recommendation: "Close
review. Do not open iteration 4."**
- Target 1 (STEP 6's `own_type_prefix` classifier -- does it repeat
  iteration 1's "three"/"threebar" prefix-collision bug?): CONFIRMED-
  REAL, no bug. Hand-traced all 16 labels against the 3-way classifier
  (`"singlet"`, `"three_"`, `"threebar_"`) -- the asymmetric prefixes
  (singlet has no trailing underscore, the other two do) are safe for
  this specific 16-label set (neither three_* nor threebar_* starts
  with "singlet"; each of the other two's trailing underscore correctly
  excludes the other).
- Target 2 (is "16/16 off-type-clean" fully non-vacuous?): WEAKENED,
  real but minor. Independently re-derived (not just citing iteration
  2's own enumeration): su3_curvature_term is structurally IDENTICALLY
  ZERO on 10 of 16 elements (all 6 singlets -- phi_2's row/col-0
  isolation applies to rho7_nuk too, same mechanism as casimir's
  singlet-zero -- plus three_1/three_3/threebar_1/threebar_3), so
  STEP 6's per-element "clean" verdict is TRIVIALLY true for su3_curv
  on those 10, and only genuinely empirically load-bearing on the
  remaining 6. casimir is similarly trivial-on-singlets (same
  structural reason) but genuinely nonzero-and-tested on the 10
  three/threebar cases; termB_sq's "off-type-clean" is close to
  structurally guaranteed by construction (D64 acts slot-by-slot,
  preserving support pattern) regardless of value, so its check is
  largely a wiring sanity check, not a deep empirical test. Net:
  the TRUE non-vacuous test count for the one function where this
  distinction matters most (su3_curv) went from iteration-1's 0, to
  iteration-2/STEP-5's 1 (three_5), to STEP 6's 6 -- a real
  strengthening, just not literally "16 independent confirmations" as
  the aggregate framing could be misread.
- Target 3 (arithmetic-necessity CONCLUSION wording): CONFIRMED-REAL,
  correctly and clearly stated -- properly hedged, does not walk back
  the real finding, correctly identifies what IS and is NOT
  independently novel.
- Target 4 (STEP 6's "closes the N=2/selection-bias concern" claim):
  WEAKENED, minor -- directionally correct (materially reduces the
  concern) but "no longer just 2 favorable cases" reads stronger than
  the true count (2 -> 6 non-vacuous for su3_curv specifically, not
  2 -> 16 uniformly across all three functions).
- **True kill condition (per FL Step 8a): NOT MET.** Core predicate
  intact: 5-piece decomposition sums exactly to ground truth on 2
  structurally different inputs; 3 pieces individually off-type-clean
  on all 16 basis elements (true, even if the DEPTH of evidence per
  element varies by function).

**Response (accepted, NOT another code-fix cycle -- FL cap is 3
iterations, already reached, and the skeptic's own recommendation is
to close):**
| Concern | Response |
|---|---|
| STEP 6 conflates trivially-zero-clean with genuinely-nonzero-clean per element | **Accepted as documented limitation** (recorded here). True non-vacuous count for su3_curv specifically: 6 of 16 (three_2/4/5, threebar_2/4/5), not 16. casimir: nonzero-and-tested on 10 of 16 (three_*, threebar_*), structurally-trivial on the other 6 (singlets). termB_sq: off-type-clean is close to a structural guarantee (D64 preserves domain-slot support by construction) rather than a deep empirical test on any of the 16 -- more a wiring check than new evidence. |
| "Closes the N=2/selection-bias concern" phrasing slightly overstates uniformity across the 3 functions | **Accepted as documented limitation** -- true direction, imprecise magnitude; if ever cited in a preprint, state the per-function non-vacuous counts explicitly (su3_curv: 6/16; casimir: 10/16 nonzero + Schur-structural on the rest; termB_sq: structural by construction) rather than a single "16/16" headline. |

**L4A Round 22 status: CLOSED for this round.** The explicit closed-form
Weitzenbock identity (D_7^2 = Scal/4+nabla*nabla_can + su3-curvature +
torsion + mixed_A-B) is derived, and its type-preservation/type-mixing
structure is verified with genuine (non-vacuous where it matters most --
su3_curv) empirical content on 2 fully-tested inputs plus a 16-element
sweep for the narrower 3-piece sub-claim. Three review iterations
completed (FL Evaluator-Optimizer cap reached); no further code-fix
cycles this round. Next steps (spectral assembly for L4A's actual
F_{S^-} ask; independent rho=14 cross-check via the same technique) are
natural follow-ups, not required to close this round's claim.
preprint.tex NOT touched this round.

**Reviewer verdict (iteration 3/3, direct Agent-tool dispatch after two
Workflow-layer empty results -- content confirmed, not a Workflow
finding): `LGTM`, severity P2.** Independently re-derived the
vacuous/genuine split for su3_curv (10/16 identically zero, 6/16
genuinely nonzero) via its own diagnostic, matching the skeptic's
finding exactly and independently confirming `casimir`/`termB_sq` are
genuinely nonzero-tested on all 16 (not affected by the same issue --
narrows the concern to su3_curv's share of the headline number only, as
the skeptic also concluded). One new, non-blocking, forward-looking
note: the `"singlet"` prefix (no trailing separator, unlike `"three_"`/
`"threebar_"`) doesn't apply the same trailing-underscore discipline
the iteration-1 fix established, though no current label collides with
it -- latent fragility for future rounds, not a present bug.

**Both independent reviews (skeptic: CONFIRMED-REAL, explicit "close
review, do not open iteration 4"; reviewer: LGTM/P2) agree on the same
version.** FL Step 8a review is CLOSED for Round 22. No further code
changes this round.

---

## Round 23 (2026-07-10) -- L4A's ACTUAL object: identifying and building
## D_{S^6} (x) S^-, STEP A (foundational verification)

**User instruction:** "собери спектр F_{S-} на singlet-блоке" (assemble the
F_{S^-} spectrum on the singlet block), directly attacking L4A.

**CRITICAL FINDING (before any computation): L4A's "$S^-$" is NOT V_7
(Round 14-22's whole apparatus) and NOT rho=trivial (L4B).** Read
preprint.tex sec:Sminus/sec:lichnerowicz/sec:schur carefully (lines
371-630) rather than guessing. $S^- \cong T^{1,0}S^6 \oplus \mathbf{1}$
(Lemma L1) -- the negative-chirality half of S^6's OWN spinor bundle
S=S^+(+)S^-, used as an AUXILIARY twisting bundle for the S^6-INTRINSIC
Dirac operator $D=\Dslash_{S^6}\otimes S^-:\Gamma(S^+\otimes S^-)\to
\Gamma(S^-\otimes S^-)$. This is a THIRD, genuinely different object from
both of the other two candidates -- confirmed with the user via
AskUserQuestion before committing effort (chose: build S^- from scratch,
full new round).

**Two navigational errors caught and corrected before any wrong claim
was made (both self-caught, neither shipped):**
1. First assumed D64 (=D_on_simple_tensor, this project's ALREADY-BUILT
   64-dim intrinsic operator on F=Sigma(x)Sigma since Round 10) acts on
   the LEFT tensor factor only, treating the RIGHT factor as a FIXED
   auxiliary twist -- WRONG. Read D_on_simple_tensor's actual formula:
   D(eta(x)xi) = sum_i[(e_i.nabla_{e_i}eta)(x)xi + (e_i.eta)(x)(nabla_{e_i}xi)]
   -- a genuine Leibniz-rule TWISTED Dirac operator, with nabla_g
   (Levi-Civita-calibrated spin connection) applied to the RIGHT factor
   too, not held fixed. This is EXACTLY the standard twisted-Dirac
   formula D_E = Dslash_S(x)1 + Clifford-contraction-with-nabla^E,
   confirming D64 (as already built) is directly usable -- it does NOT
   need to be "held fixed on the right", it needs nabla_g restricted to
   the right factor to PRESERVE the S^- sub-bundle, which is a
   different (and correct) requirement.
2. First check for (1) used an overly strict criterion (exact right-
   factor INDEX preservation), found "leaks", concluded the convention
   was broken. Root-caused: nabla_g is built from BIVECTOR (degree-2,
   EVEN Clifford-algebra) actions (spin-lift of the Levi-Civita Nomizu
   map), and the chirality/volume element PROVABLY COMMUTES with the
   even Clifford subalgebra (standard fact) -- so nabla_g preserves
   CHIRALITY (S^- to S^-) without preserving the exact index WITHIN
   that chirality class (it mixes {1},{2},{3},{123} among themselves,
   which is fine and expected -- S^- is 4-dim, not required to stay on
   a single basis vector). Re-checked with the CORRECT criterion
   (chirality-class preservation, not exact-index preservation) --
   passes cleanly.

**RESULT (script: `g2su3_Sminus_block_identify.py`, exit 0, all asserts
pass, [VERIFIED-tool]):**
- Chirality identification within the EXISTING 8-dim Sigma=Lambda*(C^3)
  basis (SUBSETS, already used throughout this whole 20+ round
  experiment), via gamma_7=e1.e2.e3.e4.e5.e6 (chirality operator,
  ALREADY built and verified in g2su3_skeptic_checks.py, Round 3-ish):
  S^+ = Lambda^even = {(), (1,2),(1,3),(2,3)}  ("1 (+) 3bar")
  S^- = Lambda^odd  = {(1,),(2,),(3,),(1,2,3)} ("3 (+) 1")
  matching Lemma L1 EXACTLY (T^{1,0}S^6 (+) 1 = "3 (+) 1").
- D64 restricted to Gamma(S^+(x)S^-) -> Gamma(S^-(x)S^-) (both 16-dim
  chirality sub-blocks of the 64-dim F): well-defined, D64^2 restricted
  to Gamma(S^+(x)S^-) is exactly Hermitian (self-adjoint 16x16
  endomorphism) -- confirms this IS the preprint's own
  $(D_{S^6}\otimes S^-)^2$ object.
- SU(3)-decomposition of the 16-dim fibre, computed independently
  from FIRST PRINCIPLES (su(3)-Casimir eigenvalues on this specific
  16-dim block, using the SAME su(3)-generator machinery as Round
  17-20): Casimir eigenvalues `{0: 2, 4/3: 6, 3: 8}` -- EXACTLY
  matching the preprint's own claimed decomposition
  `S^+(x)S^-|_{SU(3)} = (1,1)(+)(0,1)(+)(1,0)(+)2x(0,0)` = 8(+)3bar(+)3
  (+)1(+)1 (dim 8+3+3+1+1=16) -- an independent cross-check of the
  preprint's own Section sec:schur claim, not merely assumed.

**What this establishes:** L4A's object is now correctly identified,
built (not from scratch -- reusing D64, already validated since Round
10) and cross-checked against the preprint's own stated fibre content.
D64^2|_{S^+(x)S^-} (the 16x16 Hermitian matrix just extracted) IS
$(D_{S^6}\otimes S^-)^2$. The next step is the Weitzenbock decomposition
$= \nabla^*\nabla + R/4 + F_{S^-}$ -- structurally analogous to Round
22's TERM_A/TERM_B split (D=TERM1+TERM2 here, TERM1=intrinsic Dslash on
the LEFT factor, connecting to Agricola's OWN Theorem 3.2/3.3
untwisted-spinor formula and the ALREADY-BUILT H/Kostant-cubic
machinery in g2su3_H_element.py; TERM2=Clifford-contracted nabla_g on
the RIGHT/S^- factor) -- NOT YET DONE this step.

**Kill Analysis:**
- KILLED: the "F_{S^-}=SU3_CURV, V_7-singlet interpretation" hypothesis
  (Round 22's own object is NOT L4A's object -- a genuinely different
  fibre and operator); the "D64 is left-factor-only" assumption (D64 is
  a full Leibniz-rule twisted operator, not a simple left-mult).
- SURVIVED: D64 itself (already validated since Round 10, reused
  unmodified); the bivector/chirality-commutation argument (a general,
  provable Clifford-algebra fact, not specific to this construction);
  the overall "restrict the already-built 64-dim apparatus to the right
  chirality sub-block" strategy (validated by the exact SU(3)-content
  match).
- OPENED: a concrete, verified starting point (the 16x16 Hermitian
  D64^2|_{S^+(x)S^-}) for the actual Weitzenbock decomposition and
  F_{S^-} spectral computation L4A asks for.

**L4A status: object correctly identified and the operator built +
verified; Weitzenbock decomposition NOT YET done.** preprint.tex NOT
touched this round.

---

## Round 23 STEP B (2026-07-10): Weitzenbock decomposition attempt --
## HONEST NULL at its own first sanity check, not yet resolved

**Derivation (script: `g2su3_Sminus_weitzenbock.py`).** Expanded
D^2 = sum_{p,q} e_p.e_q . nabla_p nabla_q on Gamma(S^+(x)S^-) the SAME way
as Round 22 (Clifford-relation p=q/p<q split), using
nabla_p(eta(x)xi) := (nabla_p eta)(x)xi + eta(x)(nabla_p xi) (the full
tensor-product/Leibniz connection D_on_simple_tensor already implements).
Verified algebraically (by hand, not yet numerically re-derived from a
DIFFERENT angle) that: p=q part = nabla^{S(x)E,*}nabla^{S(x)E} exactly
(cross terms cancel by p<->q symmetry); p<q part splits into 4 pieces via
[nabla_p,nabla_q]v = R(e_p,e_q)v + nabla_{[e_p,e_q]}v, with (c) := the
E(=S^-)-side-only curvature term identified as F_{S^-} in the standard
BGV twisted-Dirac sense, and (a)+(b)+(d) grouped into nabla*nabla+R/4.
R(e_p,e_q) := [M_p,M_q] - nabla_{[e_p,e_q]}, where M_p=nabla_g(p,.) (the
ALREADY-CALIBRATED Levi-Civita spin connection on Sigma, same object
D_on_simple_tensor itself uses) and nabla_{[e_p,e_q]} splits via the
m-part (T-table, torsion) acting through nabla_g, and the h-part
(curv_h-table) acting through su3_action (ALREADY calibrated against
AHL2023 page 42) with a minus sign (standard canonical-connection-at-
base-point fact).

**STEP B1 (decisive sanity check, run BEFORE trusting anything
downstream): does -sum_{p<q} e_p.e_q.R(e_p,e_q) equal (Scal/4)*Id_8 on
Sigma (the textbook Lichnerowicz identity)? FAILS.** Result is diagonal
but NOT scalar: `diag(3/2, -7/6,-7/6,-7/6,-7/6,-7/6,-7/6, 3/2)` --
i.e. value 3/2 on the two SU(3)-trivial slots (degree 0 and degree 3 of
Lambda*(C^3)) and -7/6 uniformly on the six "3"/"3bar" slots. This IS
SU(3)-block-scalar (consistent with R(e_p,e_q) being SU(3)-equivariant,
a partial correctness signal -- an actually-broken construction would
more likely give a non-block-scalar mess), but it is NOT the uniform
scalar the Lichnerowicz identity requires. STOPPED HERE -- did NOT
proceed to build F_{S^-} (STEP B2/B3 code exists in the file but its
output was never reached/inspected, since the assert on B1 fails first
and the script exits before B2 runs).

**Kill Analysis:**
- KILLED (for now, pending re-derivation): the specific R(e_p,e_q)
  formula as constructed (`curvature_R` in g2su3_Sminus_weitzenbock.py)
  as a correct representation of the twisted-Dirac curvature operator
  needed for the standard Lichnerowicz identity to hold in this exact
  form.
- SURVIVED: STEP A's block identification and SU(3)-content match
  (untouched by this failure, a fully independent, already-verified
  result); the individual primitives reused (nabla_g, su3_action,
  T-table, curv_h-table) -- each independently calibrated/validated in
  EARLIER rounds, not newly built here, so the bug (if it is a bug) is
  most likely in HOW they are COMBINED in `curvature_R`/`nabla_bracket`,
  not in the primitives themselves.
- OPEN, NOT YET DIAGNOSED: (a) is the sign/coefficient convention on the
  h-part isotropy term (`-curv_h(p,q,k)*su3_action(k,.)`) exactly right,
  or does it need a different normalization specific to the SPIN
  representation (as opposed to Round 22's V_7 representation, where an
  analogous sign issue WAS found and fixed -- an genuine, real
  possibility this is the SAME class of bug recurring in a new context,
  not yet checked); (b) is "R(e_p,e_q) := [M_p,M_q] - nabla_{[e_p,e_q]}"
  the textbook-correct curvature FORMULA for a general (non-torsion-
  free-frame) invariant basis, or is there a missing torsion-dependent
  correction term specific to Levi-Civita's OWN torsion-free property
  applied to a NON-coordinate frame (i.e. possibly an extra term beyond
  the standard R(X,Y)=[nabla_X,nabla_Y]-nabla_{[X,Y]} formula is needed
  when X,Y are not coordinate vector fields and the connection itself
  has frame-dependent structure functions); (c) whether the DIAGONAL-
  BUT-NOT-SCALAR result (3/2 vs -7/6) is itself informative -- e.g. does
  it match some OTHER known quantity (Ricci scalar per SU(3)-type,
  rather than the full uniform Scal), suggesting the "Scal/4" I'm
  checking against needs to be REPLACED by a type-dependent quantity in
  this non-normal-frame setting, which would mean my ENTIRE assumption
  that "(a) alone equals a uniform R/4" is the wrong grouping, and (a)
  needs to be combined with PART of (b) before it becomes uniform.

**This is an honest, reported NULL at the FIRST decisive checkpoint --
not shipped as a finding, not silently patched. No further code changes
attempted this round; the root cause needs dedicated, careful
re-derivation (most likely re-checking hypothesis (c) above: whether
"R/4" should be understood as "the uniform PART of a type-dependent
quantity" with the type-DEPENDENT part correctly belonging to F_{S^-}
or to a torsion-correction term, not to a separately-verified-alone
"R/4"). STEP A's result (the 16x16 D64^2|_{S^+(x)S^-} matrix, exactly
matching the preprint's own SU(3) fibre content) remains solid and
reusable regardless of how STEP B's remaining issue resolves.**

preprint.tex NOT touched this round.
