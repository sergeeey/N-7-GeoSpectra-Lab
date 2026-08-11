# L3b Interface Specification — what a Spin(8) fibre-symmetry input must provide

**Status:** drafted 2026-07-14, NOT sent. Per this project's own standing
constraint, contact with Tom Lawrence is not initiated proactively — he
reaches out when Part 4/5 are ready. This document exists so that, when
contact happens, the single open technical question can be handed over as a
precise specification instead of a vague "we need Spin(8) symmetry."

**Queued follow-up (2026-07-15, Project 360° Scientific Red Team audit —
`reports/PROJECT_360_ROUND3_SYNTHESIS.md`):** KT-3 in that audit's kill-table is
exactly this document's condition 1 — whether the diagonal 𝔤₂⊂F₄ (24-dim,
acting on 𝕆³, §1.5 below) is actually identifiable with the geometric G₂
acting on S⁶'s single 8-dim fibre — flagged there as *assumed, not yet
constructed* (a differential-geometry lens found the 24-dim vs 8-dim rep
mismatch is a real gap, not just a labeling issue). That audit also closed
KT-2 the same day: triality acts as the literal identity on S⁶ as a base
isometry (verified over the full 28-dim 𝔰𝔬(8), Fix(T)=𝔤₂ exactly) — this
does not close the F4/fibre route below, but it does mean the "symmetric
escape at the base level" some readers might reach for is foreclosed; the
remaining question really is the fibre-level one this document specifies.
KT-3 itself is queued, not run — it needs Tom's own framework input, not more
internal compute (see this file's own §1.5 close: "conditions 2-5... require
an object that is not already implicit in S³×S⁶ geometry").

**Purpose:** this is the ONE remaining gap in the paper's headline claim
$N_{\mathrm{gen}}=3$. Everything else in the three-generation argument is
either proved or internally certified (see status table below). This
document does not ask "is $N_{\mathrm{gen}}=3$ true" — it asks a narrower,
answerable question: *does a specific mathematical object exist in Tom's
framework, and if so, what are its defining equations?*

---

## 1. What is already established (no further internal work needed here)

| Result | Status | Where |
|---|---|---|
| $\ind(D^{(\alpha)}) = 1$ for each of the three triality channels $\alpha \in \{v,s,c\}$, identically | **Proved** (L3a) | §3.4, experiment `E-L3-PARTIAL` |
| The three channels' $G_2$-equivariant bundles are pairwise isomorphic: $E_v \cong E_s \cong E_c$ | **Proved** (Theorem `thm:elb3`, "Bundle Obstruction, E-L3B") | §3.5 |
| No $G_2$-invariant operation — including nearly-Kähler instanton connections — can distinguish the three channels | **Proved**, same theorem | §3.5 |
| No continuous symmetry inside $\mathfrak{so}(8)$ at all commutes with the geometric $G_2$ action on the octonion fibre: $\dim\,\mathfrak{c}_{\mathfrak{so}(8)}(\mathfrak{g}_2) = 0$ exactly | **Proved** (gate G102, this work) | Open Problems, item L3b |
| Trivial-block kernel rank $\dim\ker(D^+_{S^-})=1$ per channel | **Internally certified**, 3 independent routes, external review outstanding | §sec:kernel, experiment `20260714-round59-trivial-rank-certification` |
| No single irreducible $\mathrm{SU}(3)$ representation-theoretic twist gives index exactly $3$ (index jumps $1\to 7\to 27\to\dots$), and no standard $G_2$-invariant-connection reducible bundle combining twists gives an exact $(3,0)$ kernel without extra mirror zero modes — block-diagonality is *forced*, not chosen, for any such connection | **Proved** | experiments `20260715-index-formula-s-tensor-t-candidate`, `20260715-round-su3-index-map-audit` |

**The consequence of G102 specifically:** this is not a limitation of the
$G_2$-equivariant framework alone — the *entire* internal search space
(every continuous symmetry available inside the octonion fibre's $\mathfrak{so}(8)$,
not just the $G_2$-equivariant subcase) has been exhausted and contains no
candidate. Distinguishing the three channels is therefore **not a computation
this framework can be pushed further to produce internally.** It requires an
object that is not already implicit in $S^3\times S^6$ geometry.

**A second, independent route is now also closed (2026-07-15).** G102 ruled
out a hidden *symmetry* (centralizer) route; the representation-ring /
index-arithmetic route is a logically separate possibility — could some
$\mathrm{SU}(3)$-equivariant twist bundle, built from the representation ring
alone rather than from any new symmetry, realize a clean index-3 construction
by numerology? This is now also closed: no single irreducible twist gives
index 3 (the index sequence jumps straight from $1$ to $7$), and no standard
reducible combination realizes an exact $(3,0)$ kernel without extra mirror
zero modes for any $G_2$-invariant connection. Symmetric to G102's exhaustion
of the centralizer route, this exhausts the invariant-connection
representation-ring route. **The only remaining door is a genuinely
non-invariant, symmetry-breaking extension** (an explicit background field or
coupling $\Phi$ with its own physical justification) — which is exactly the
external input this document specifies.

---

## 1.5. A specific candidate route not yet explored: F4 (added 2026-07-15)

Section 1 above states that no continuous symmetry inside $\mathfrak{so}(8)$ can
distinguish the three channels (G102: $\dim\,\mathfrak{c}_{\mathfrak{so}(8)}(\mathfrak{g}_2)=0$,
and even the weaker $\dim\,\mathfrak{c}_{\mathfrak{so}(8)}(\mathfrak{su}(3))=2$ consists
of generators that are themselves inner to $\mathfrak{so}(8)$ and hence cannot
implement triality's *outer* automorphism action). A `/cross-domain` +
`skeptic` pass (2026-07-15) on this exact argument found that this conclusion,
while correct, is **narrower than it first appears**: it only rules out
mechanisms built purely from $\mathfrak{so}(8)$ itself. It says nothing about
a strictly larger ambient Lie algebra containing $\mathfrak{so}(8)$.

**Verified (arithmetic, this round):**
$F_4 = \mathrm{Aut}(J_3(\mathbb{O}))$ — the automorphism group of the
exceptional Jordan algebra, the same object at the center of Singh
(arXiv:2508.10131, §pearl_registry) — contains $\mathrm{Spin}(8)$ via the chain
$F_4 \supset \mathrm{Spin}(9) \supset \mathrm{Spin}(8)$, with adjoint branching
$52 = 28 + 8_v + 8_s + 8_c$ (dimension count confirmed exactly: $\dim\mathfrak{so}(9)=36=28+8$,
$\dim(\text{spinor}(9))=16=8+8$, total $28+8+8+8=52$). Independently,
$|W(F_4)|/|W(D_4)| = 1152/192 = 6 = |S_3|$ **exactly** — triality is realized
as part of $F_4$'s own Weyl group, i.e. by honest conjugation with $F_4$
elements. This means triality **is** an inner automorphism once the ambient
algebra is enlarged from $\mathfrak{so}(8)$ to $\mathfrak{f}_4$. This is
standard, textbook Lie theory (the $F_4$/$D_4$ folding relationship) — not
speculative — and $\mathfrak{f}_4=\mathrm{Der}(J_3(\mathbb{O}))$ is a natural
extension of $\mathfrak{g}_2=\mathrm{Der}(\mathbb{O})$ already used throughout
this project ($\mathbb{O}\to J_3(\mathbb{O})$ is exactly the octonion →
exceptional-Jordan-algebra extension).

**Upgraded to an EXPLICIT construction (2026-07-15, follow-up check):**
Two independent verifications, not just the abstract Weyl-group argument above:

1. **From scratch (this round):** built the octonion multiplication table via
   Cayley-Dickson doubling, solved the derivation equation
   $D(xy)=D(x)y+xD(y)$ as a linear system over the 64 entries of an $8\times8$
   real matrix $D$ — the null space is exactly 14-dimensional
   (rank 50 of 64, confirmed by SVD), i.e. $\mathfrak{g}_2=\mathrm{Der}(\mathbb{O})$
   computed directly, not cited. Every one of the 14 basis derivations
   annihilates the real unit $e_0$ exactly (residual $\sim10^{-15}$) and acts
   skew-symmetrically on $\mathrm{Im}(\mathbb{O})$: confirms
   $\mathbf{8}_v = \mathbf{1}\oplus\mathbf{7}$ under $\mathfrak{g}_2$ directly,
   matching G102's own $\mathrm{Hom}_{\mathfrak{g}_2}=2$ finding by Schur-count
   ($1^2+1^2=2$, multiplicity-free two-irrep decomposition).

2. **Primary source (Baez, "The Octonions," arXiv:math/0105155, §3.4/4.2 —
   read in full, pymupdf extraction):** confirms, verbatim, that
   $J_3(\mathbb{O})\cong\RR^3\oplus V_8\oplus S_8^+\oplus S_8^-$ (his eq. 7 —
   exactly the $\mathbf{8}_v\oplus\mathbf{8}_s\oplus\mathbf{8}_c$ split via the
   three off-diagonal octonion entries $x,y,z$), that
   $\mathrm{Spin}(8)\subseteq\mathrm{Aut}(J_3(\mathbb{O}))$, that $\dim\,\mathrm{Aut}(J_3(\mathbb{O}))=52$
   ("it goes by the name of $F_4$"), and — the load-bearing sentence —
   *"there are other automorphisms coming from the permutation group on 3
   letters, which acts on $(\alpha,\beta,\gamma)\in\RR^3$ and $(x,y,z)\in\mathbb{O}^3$
   in an obvious way."* This is an **explicit, named, primary-source-confirmed**
   $S_3\subset F_4$ permuting the three octonion slots $(x,y,z)$ that literally
   host $\mathbf{8}_v,\mathbf{8}_s,\mathbf{8}_c$ — not an abstract existence
   argument from Weyl-group order division.

**Direct consequence (this project's own deduction, not stated by Baez):**
define a "diagonal" $\mathfrak{g}_2\subset F_4$ by applying the *same*
automorphism $g\in\mathrm{Aut}(\mathbb{O})$ to each of $x,y,z$ simultaneously.
Since the $S_3$ slot-permutation and this diagonal action operate on
independent structures (which slot vs. what happens inside each slot), they
commute *by construction* — the permutation does not merely normalize this
$\mathfrak{g}_2$, it **centralizes** it. Condition 1 below (a $U$ with $U^3=1$)
is therefore explicitly realized: $U$ = cyclic permutation of $(x,y,z)$,
$U^3=\mathbb{1}$ exactly, and $U$ commutes with the diagonal $\mathfrak{g}_2$
already present in this project's own $S^6=G_2/\mathrm{SU}(3)$ construction.

**What STILL remains genuinely open (this is a candidate ROUTE, not a
solution — conditions 2–5 of §3, not condition 1):** whether this abstract
$U$ (an automorphism of the algebraic object $J_3(\mathbb{O})$) corresponds to
an operator on the *physical* field content of this project's actual
$S^3\times S^6$ Dirac construction, and whether it commutes with the *physical*
Dirac operator $D$ — conditions 2–5 are entirely about this translation from
algebra to physics, and none of it is done. Condition 1 is now closed;
conditions 2–5 are the real remaining work.

**Kill criterion (narrowed accordingly):** if no explicit physical
realization of $U$ (acting on actual zero-mode wavefunctions, not just the
abstract $J_3(\mathbb{O})$ automorphism) commuting with $D$ can be produced
within a bounded effort, this route closes at condition 2, not condition 1 —
still alongside the closed $\mathfrak{so}(8)$-internal search, but one step
further along than previously recorded.

**Attempted 2026-07-15 (same day) — hit an ALREADY-PROVEN wall, and the
reason why is itself the useful result.** The naive approach — build $U$ as a
map $\Phi_{v\to s}: E_v \to E_s$ between the three *separately labeled*
canonical zero-mode bundles, and check $[D,\Phi]=0$ — is not merely
unconstructed, it is **provably impossible**, by a theorem this project
already proved before the F4 exploration began: **E-L3B**
(`experiments/20260625-l3b-bundle-obstruction/`, 2026-06-25). Its proof:
$\mathbf{8}_v,\mathbf{8}_s,\mathbf{8}_c$ restrict to the *identical*
$\mathrm{SU}(3)$-module ($3\oplus\bar3\oplus1\oplus1$); by the homogeneous
bundle correspondence theorem, $E_v\cong E_s\cong E_c$ as $G_2$-equivariant
bundles *with identical canonical connections* — "the twisted Dirac operators
$D\otimes E_v, D\otimes E_s, D\otimes E_c$ (with canonical connections) are
THE SAME OPERATOR." Working through *why* a naive $\Phi$ fails clarifies the
real obstruction precisely: any such $\Phi$ built purely from this canonical,
$G_2$-only data is automatically **not** $\mathrm{Spin}(8)$-equivariant — if
it were, it would be a nonzero element of
$\mathrm{Hom}_{\mathrm{Spin}(8)}(\mathbf{8}_v,\mathbf{8}_s)$, which Schur's
lemma forces to be exactly zero (§2 below), since $\mathbf{8}_v,\mathbf{8}_s$
are inequivalent as $\mathrm{Spin}(8)$-representations. So a $\Phi$ satisfying
$[D,\Phi]=0$ *can* be built at the $G_2$-only level (E-L3B's own corollary
already gives one, trivially, since the operators are literally identical) —
but that very success is exactly why it fails condition 3: it is a
"coincidental" intertwiner that exists **because** $G_2$ cannot tell the
channels apart, not evidence that a genuine $\mathrm{Spin}(8)$/$F_4$ structure
is present. It is condition 4's "bookkeeping, not physics" concern, made concrete.

**This reframes what "realizing $U$" actually requires.** $U$ must NOT be
modeled as a map *between* three separately-labeled Hilbert spaces (that
model is Schur-forbidden the moment it's asked to be genuinely
$\mathrm{Spin}(8)$/$F_4$-equivariant, and physically empty the moment it
isn't). The $F_4$/Jordan-algebra picture in this section models $U$ correctly:
as an automorphism of *one* combined 24-real-dimensional object
$F=\mathbf{8}_v\oplus\mathbf{8}_s\oplus\mathbf{8}_c$, permuting its three
summands *as summands of a single representation* — not as an intertwiner
between separate copies. This is not Schur-forbidden (permuting summands of
one bigger representation is a different question from mapping between
inequivalent irreps). But it requires the physical fiber to genuinely **be**
this combined 24-dimensional $F_4$-natural object — which is a structural
change from the current construction (three separately-labeled copies of one
8-dimensional canonical bundle), not a re-derivation from what is already there.

**Kill criterion, revised again:** the open question is no longer "does an
intertwining $\Phi$ exist" (a wrong question — E-L3B answers it, and the
answer doesn't help). It is: **does this project's physical construction
have any independent reason to combine the three channels into one physical
fiber object (rather than three separate sectors)** — e.g. from the
$S^3$-spin-connection extension to $S^3\times S^6$, or Part 5's SU(4)
transformations. Absent such a reason, this route is closed at the same
place the $\mathfrak{so}(8)$-internal search closed: it requires new physical
input, not a computation this framework can supply internally.

**Attempted 2026-07-15 (same day, continued) — the S³-spin-connection +
Part-5-SU(4) combination was tried directly. It sharpens the obstruction
further rather than closing it, and finds a NEW, more general reason the
naive version fails — one that subsumes E-L3B's own canonical-connection
argument.**

*Setup.* Part 5 is unpublished (per this project's own standing rule, not
solicited), so the only thing that can be checked is: does *this project's
own already-established* $S^3$ spin-connection $\cong \mathrm{SU}(2)_L\times
\mathrm{SU}(2)_R$ result (Tom-confirmed, G6–G9), combined with the
Spin(6)$\cong$SU(4) structure Part 5 is expected to relate to (per this
project's own G10/G10b $\mathrm{SO}(6)\cong\mathrm{SU}(4)\to
\mathrm{SU}(3)\times\mathrm{U}(1)$ embedding, and already used explicitly in
this project's own `20260621-g69-csdr-coset` CSDR argument: "Spin(6)=SU(4):
spinor $4+\bar4$ under SU(3) $\to 3+1+\bar3+1$"), supply the missing
"genuine reason to combine."

*Finding, verified this round:* it cannot, for a reason stronger than E-L3B.

$\mathrm{Spin}(6)\subset\mathrm{Spin}(7)$ (stabilizer of a point/vector — the
*same* embedding CSDR already uses to restrict $S^6$'s tangent-frame spinor)
is a **subgroup of $\mathrm{Spin}(7)$**. E-L3B already proved $\mathbf8_s
\cong \mathbf8_c$ as $\mathrm{Spin}(7)$-representations (Spin(7) has a
*unique* 8-dim spinor rep). Restriction of an identical representation to
*any* subgroup stays identical — so $\mathbf8_s|_{\mathrm{Spin}(6)} \cong
\mathbf8_c|_{\mathrm{Spin}(6)}$ is **inherited automatically**, with no
further computation needed. Concretely (checked against this project's own
G69 numbers): $\mathbf8_v|_{\mathrm{Spin}(6)} = \mathbf6\oplus\mathbf1\oplus
\mathbf1$, while $\mathbf8_s|_{\mathrm{Spin}(6)} = \mathbf8_c|_{\mathrm{Spin}(6)}
= \mathbf4\oplus\bar{\mathbf4}$ (matching G69's own $4+\bar4$ line) — SU(4)
distinguishes $v$ from $\{s,c\}$ (different rep type), same partial result
SO(7) already gave, but **cannot** distinguish $s$ from $c$.

**This is a stronger obstruction than E-L3B's, not a repeat of it.** E-L3B's
theorem was specifically about the *canonical* $G_2$-equivariant connection
(it leaves open, in principle, whether a *non-canonical* connection could
differ). The argument here does not depend on which connection is chosen at
all — canonical, or an independent dynamical gauge field exactly as "Part
5's local SU(4) transformations with nonzero field strength" would be. A
gauge field valued in $\mathfrak{su}(4)$ couples to a mode through *which
representation* that mode sits in; since $\mathbf8_s$ and $\mathbf8_c$ are
the *same* $\mathrm{SU}(4)$-representation (not merely connected by the same
canonical connection), **any** $\mathrm{SU}(4)$ gauge field — dynamical or
geometric — necessarily acts on them identically. The obstruction is
representation-theoretic, not connection-theoretic.

This also explains, from a different angle, this project's own prior NULL
result `null_results/INDEX.md` entry **G39-B1** ("Spin(6)≅SU(4): $\Lambda^2
(T^{0,1})$ has $c_3=2$, not 6; factor 3 unaccounted") — that gate killed an
$\mathrm{SU}(4)$ Pati-Salam gauge-bundle-on-$S^6$ construction via an
index/Chern-class mismatch. The finding here is a different, more general
argument against the same class of construction: even setting the
Chern-class problem aside entirely, $\mathrm{SU}(4)$ alone on the $S^6$ side
cannot carry the needed information regardless of bundle topology, because
the *representation content* is already identical.

**Does tensoring with the $S^3$ factor rescue it?** No, not in the simplest
(product-manifold, block-diagonal Dirac operator $D = D_{S^3}\otimes
\mathbb{1} + \gamma\otimes D_{S^6}$) case. Tensoring a fixed $\mathrm{SU}(2)_L
\times\mathrm{SU}(2)_R$ representation onto an $S^6$-sector that is already
$\mathrm{SU}(4)$-blind to the $s/c$ distinction leaves that blindness
untouched — the operator's action on the $S^6$ factor is unchanged by what
it is tensored with on the $S^3$ factor. The obstruction is not "not enough
quantum numbers," it is "the two specific quantum numbers this construction
supplies ($v/\{s,c\}$ split from Spin(6), and whatever $S^3$ contributes) do
not, and structurally cannot, resolve $\{s,c\}$ regardless of how they are
combined multiplicatively." Combining the two known ingredients through a
plain tensor product is therefore ruled out as a route, not merely
unconstructed.

**What remains genuinely open, and cannot be settled without Part 5's
(unpublished) content:** if the actual $S^3\times S^6$ construction is *not*
a simple product — i.e. the physical connection/Dirac operator genuinely
entangles the $S^3$ frame index with the $S^6$ triality index in a way that
does not factor as above (a nontrivial fibration, a Chern-Simons-type
coupling linking the two curvatures, or similar) — this specific argument
does not apply, since it assumes the block-diagonal/product structure.

**Checked directly this round: does `G86B` (warp factor $\Omega(y)$ on
$S^6$, `experiments/20260622-g86b-warp-factor/`) provide grounds for or
against such an entangling structure?** Read the experiment's own script and
decision.md. Two findings, one narrow and one broader:

1. *Categorical mismatch.* $\Omega(y)=e^{2A(y)}$ is a pure scalar rescaling
   of the 10D metric ($ds^2 = e^{2A(y)}\eta_{\mu\nu}dx^\mu dx^\nu +
   g_{mn}(y)dy^mdy^n$), not indexed by representation at all — it multiplies
   $\mathbf8_v,\mathbf8_s,\mathbf8_c$ identically by construction, the same
   categorical problem as G32-B1/G39. As literally defined, it could never
   have been the entangling ingredient regardless of its $y$-dependence.

2. *A broader, more relevant point, from G86B's own G1 gate.* G86B's warp
   equation is $\nabla^2_{S^6}e^{4A(y)} = |F(y)|^2 - \langle|F|^2\rangle$.
   Under this project's standing assumption of $G_2$-invariant flux,
   $|F(y)|^2=\text{const}$, so the RHS vanishes identically and $e^{4A}$ is
   *harmonic* on compact $S^6$ — hence constant (Hopf/Liouville: a harmonic
   function on a compact, boundaryless Riemannian manifold is constant; this
   step needs compactness alone, not $G_2$-invariance specifically —
   $G_2$-invariance is what forces the *source* to be constant in the first
   place). This is not a fact about warp factors specifically: **any scalar
   quantity on $S^6$ sourced by a $G_2$-invariant background is forced
   constant by the same argument.** Combined with E-L3B/G102 (no
   $G_2$-equivariant *tensorial* structure — bundle map or connection —
   distinguishes the channels either, since their canonical connections are
   identical and $\dim\mathfrak{c}_{\mathfrak{so}(8)}(\mathfrak{g}_2)=0$),
   this closes the **entire $G_2$-invariant class** of candidate entangling
   structures, scalar or tensorial, not merely the specific warp-factor
   instance G86B checked.

**Consequence for the kill criterion:** an entangling structure that
survives this can only come from a construction that explicitly **breaks**
$G_2$-invariance (an ansatz that is not $G_2$-symmetric). This is a
qualitatively larger ask than "find some $y$-dependence" — every index-theorem
result this project's $N_{\mathrm{gen}}=3$ claim currently rests on (G73,
E-L3B, G102, and §1's whole table) assumes $G_2$-equivariant bundles
throughout. A $G_2$-breaking entangling term would need its own justification
that it does not simultaneously invalidate that machinery — it is not a free
escape route, and nothing checked so far (G86B included) says whether one
exists; G86B addressed a different question (the $\lambda$-origin) using a
$G_2$-invariant ansatz throughout, so it neither rules a $G_2$-breaking
construction in nor out.

**Kill criterion, narrowed a third time:** this route requires the physical
$S^3\times S^6$ construction to be **non-product AND $G_2$-symmetry-breaking**
— mixing the $S^3$ frame index with the $S^6$ triality index at the level of
the Dirac operator itself, in a way that is not itself forced constant by
the same Hopf/Liouville argument that kills every $G_2$-invariant candidate
(scalar or tensorial) checked so far. Absent Part 5's actual content
(unpublished, not solicited per standing project constraint), this cannot be
checked further from inside this project, and any candidate meeting it would
need to independently justify not undermining the $G_2$-equivariant
index-theorem machinery (G73, E-L3B, G102) the rest of $N_{\mathrm{gen}}=3$
rests on. The naive product-structure version of "S³ spin-connection + Part
5 SU(4)" is now closed, for a reason (representation inheritance from SO(7),
sharpened by the $G_2$-invariant-class closure above) that is strictly more
general than — and supersedes for this specific combination — the earlier
$\mathfrak{so}(8)$-centralizer (G102) and canonical-connection (E-L3B)
closures.

**Attempted 2026-07-15 (same day, continued further) — tested the single
most natural, minimal-assumption candidate for a genuinely entangling,
$G_2$-breaking construction. It is dead too, and for a sharper reason than
expected: it inherits $G_2$'s blindness rather than escaping it.**

*Candidate:* $\mathbb{O}$ is built from $\mathbb{H}$ by Cayley-Dickson
doubling ($\mathbb{O}=\mathbb{H}\oplus\mathbb{H}\ell$), so the most natural,
parameter-free way to identify "$S^3$'s own $\mathrm{SU}(2)_L\times
\mathrm{SU}(2)_R}$" with something already inside the octonion structure used
for $S^6$ is: let $H=\mathrm{span}(e_0,e_1,e_2,e_3)\subset\mathbb{O}$ be the
quaternion subalgebra, and take the $S^3$ gauge group to be
$\mathrm{Stab}_{G_2}(H)$ — the subgroup of $G_2$ that maps $H$ to itself.

*Checked this round, `[VERIFIED]` by direct computation* (using the same
from-scratch $\mathfrak{g}_2$ basis built earlier this session — the
14-dimensional null space of the derivation equation): the subspace of
$\mathfrak{g}_2$ mapping $H$ into itself is exactly
**6-dimensional** — matching $\dim\mathfrak{so}(4)=6$ exactly, confirming
$\mathrm{Stab}_{G_2}(H)\cong\mathrm{SO}(4)$ (a standard fact, here computed,
not cited).

*Why this fails, and fails worse than the SO(6) case above:*
$\mathrm{Stab}_{G_2}(H)$ is, by construction, a **subgroup of $G_2$**. Since
$G_2=\mathrm{Fix}(\mathbb{Z}_3)$ (triality-invariant by definition) and
E-L3B already proved $\mathbf8_v,\mathbf8_s,\mathbf8_c$ restrict to
*identical* $G_2$-modules ($\mathbf7\oplus\mathbf1$ in all three cases, not
just the $\mathrm{SU}(3)$-level content), **any** subgroup of $G_2$
automatically inherits this identical restriction — restriction of an
identical representation to a subgroup stays identical, the same inheritance
principle used against the $\mathrm{Spin}(6)$ case above, one level further
down. So this specific candidate does not merely fail to distinguish $s$
from $c$ (the SO(6) case's failure) — it fails to distinguish **any** of the
three channels from each other, a strictly weaker result than SO(6) alone
already gave.

**Consequence:** the single most natural, assumption-free way to embed
$S^3$'s quaternionic structure into the octonion algebra already used for
$S^6$ is closed. For the Pati-Salam/$\mathrm{Spin}(10)$ idea to survive at
all, $S^3$'s $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ must be realized as
something that is **not** a subgroup of $G_2$ — i.e. a structure visible
only at the level of the full $\mathrm{Spin}(8)$ (or larger), genuinely
entangled with the $\mathrm{SO}(6)$ that already distinguishes $v$ from
$\{s,c\}$. Nothing in this project's current geometry specifies such a
structure; this narrows "what Part 5 would need to supply" one step further
without resolving it.

**Attempted 2026-07-15 (same day, continued further) — found the FIRST
candidate this entire investigation that mathematically distinguishes all
three channels, not just $v$ from $\{s,c\}$.** This is a genuine, non-trivial
advance at the pure representation-theory level — but not yet a physical
solution; the gap between the two is now precisely localized.

*Construction, `[VERIFIED]` this round by explicit Clifford-algebra
computation* (built 8 anticommuting $16\times16$ matrices $\Gamma_1,\dots,
\Gamma_8$ realizing $\mathrm{Cl}(8)$, verified $\{\Gamma_i,\Gamma_j\}=2\delta_{ij}$
directly): split $\mathbb{O}=\mathbb{R}^8$ into two 4-dimensional blocks
($H=\mathrm{span}(e_0,\dots,e_3)$, $H\ell=\mathrm{span}(e_4,\dots,e_7)$) and
take the *full* $\mathrm{SO}(4)\times\mathrm{SO}(4)$ (rotating each block
independently — **not** restricted to octonion automorphisms, unlike every
candidate above). Defining the block-chirality operators
$\Gamma_A=\Gamma_1\Gamma_2\Gamma_3\Gamma_4$,
$\Gamma_B=\Gamma_5\Gamma_6\Gamma_7\Gamma_8$ (verified $\Gamma_A\Gamma_B=
\Gamma_9$, the full Spin(8) chirality operator, and $[\Gamma_A,\Gamma_B]=0$),
direct diagonalization gives, with all four sectors confirmed
4-dimensional numerically:

$$\mathbf8_v=(\mathbf4,\mathbf1)\oplus(\mathbf1,\mathbf4), \qquad
\mathbf8_s=(\mathbf2,\mathbf1;\mathbf2,\mathbf1)\oplus(\mathbf1,\mathbf2;\mathbf1,\mathbf2),
\qquad
\mathbf8_c=(\mathbf2,\mathbf1;\mathbf1,\mathbf2)\oplus(\mathbf1,\mathbf2;\mathbf2,\mathbf1)$$

— i.e. $\mathbf8_s$ is the *same-block-chirality* ($\Gamma_A=\Gamma_B$)
sector, $\mathbf8_c$ is the *opposite-block-chirality* ($\Gamma_A=-\Gamma_B$)
sector. **This genuinely distinguishes $s$ from $c$**, the first candidate
in this entire document to do so at the representation-theory level.

*Why this succeeds where every earlier candidate failed:*
$\mathrm{SO}(4)\times\mathrm{SO}(4)$ has rank $2+2=4$, equal to
$\mathrm{rank}(\mathrm{SO}(8))=4$. $\mathrm{SO}(7)$ (which contained every
earlier candidate — $G_2$, the $\mathrm{SO}(6)$ tangent-frame group,
$\mathrm{Stab}_{G_2}(H)$) has rank 3. A rank-4 subgroup cannot embed inside a
rank-3 one (a subgroup's maximal torus must fit inside the ambient group's),
so $\mathrm{SO}(4)\times\mathrm{SO}(4)$ is **structurally incapable** of
being a subgroup of $\mathrm{SO}(7)$ — it escapes the "Spin(7) has a unique
8-dim spinor" argument that killed everything above, categorically, not by
degree.

*The honest price, verified consistent with everything found so far:*
$\mathrm{SO}(4)\times\mathrm{SO}(4)$ intersects $G_2$ only in the
already-dead 6-dimensional $\mathrm{Stab}_{G_2}(H)$ found above — so using
the full 12-dimensional group **necessarily breaks $G_2$-invariance**. This
is not a new problem; it is exactly the door the kill criterion already
identified as the only remaining live option, now given a concrete,
computable shape instead of an abstract requirement.

**What remains completely open (this is a mathematical existence result,
not a physical one):**
1. *Physical identification.* Nothing establishes that either
   $\mathrm{SO}(4)$ factor corresponds to $S^3$'s actual $\mathrm{SU}(2)_L
   \times\mathrm{SU}(2)_R}$ gauge fields — this is a hypothesis about how the
   two known ingredients (S³ gauge fields, S⁶ octonion fiber) would need to
   relate, not a derivation. What the *other* $\mathrm{SO}(4)$ factor would
   correspond to physically is entirely unaddressed.
2. *Dynamics.* No argument shows the actual physical Dirac operator, once
   $G_2$ is broken this way, remains consistent with the index-theorem
   results (G73, E-L3B, G102) the rest of $N_{\mathrm{gen}}=3$ rests on —
   this needs independent verification, not assumption.
3. *Triality consistency.* Not yet checked: whether the known $\mathbb{Z}_3$
   triality action (which must send $v\to s\to c\to v$) is compatible with
   this specific $(\Gamma_A,\Gamma_B)$ sign structure — i.e. whether a single
   order-3 symmetry actually cyclically permutes these three sectors, or
   whether this $\mathrm{SO}(4)\times\mathrm{SO}(4)$-adapted description is
   merely a convenient basis with no such symmetry manifest in it.

**Attempted 2026-07-15 (same day, continued further) — checked point 3
directly. Result: `[VERIFIED]` positive, at the vector-representation
level — the SO(4)×SO(4) subalgebra itself is genuinely triality-invariant,
not merely a convenient basis.**

*Construction* (Baez, "The Octonions," §2.4 "Spinors and Trialities" —
read from the primary source already extracted this session): for $n=8$,
the normed triality trilinear map is realized by octonion multiplication
itself, $t_8:V_8\times S_8^+\times S_8^-\to\mathbb{R}$. Differentiating the
corresponding group-level covariance relation gives the infinitesimal
condition: for $a,b,c\in\mathfrak{so}(8)$ acting respectively on $V=S^+=
S^-=\mathbb{O}$,
$$a(x)\cdot y + x\cdot b(y) = c(x\cdot y) \quad \forall\, x,y\in\mathbb{O}.$$
For any fixed $a$, this is a linear system in $(b,c)$, solved numerically
using this session's own octonion multiplication table.

*Sanity check, `[VERIFIED]`:* for a known $\mathfrak{g}_2$ element (a
derivation, satisfying $a(xy)=a(x)y+xa(y)$ by definition), the equation is
solved by $b=c=a$ — reproducing $G_2=\mathrm{Fix}(\text{triality})$ exactly
(residual $\sim10^{-15}$), confirming the construction before trusting it on
new cases.

*Main result, `[VERIFIED]`:* solved for $(b,c)$ for all 12 basis generators
of $\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ (the vector-representation
version of the candidate found above). **All 12 partners $b$ (and $c$) land
back inside the same 12-dimensional subalgebra** (residual $\sim10^{-15}$ in
every case) — i.e. $\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ is mapped to
itself by triality, not to some unrelated subalgebra. Built the explicit
$12\times12$ matrix $T$ representing the $a\mapsto b$ assignment restricted
to this subalgebra: its eigenvalues are exactly $\{+1$ (×6)$,\ \omega$
(×3)$,\ \bar\omega$ (×3)$\}$ ($\omega=e^{2\pi i/3}$), and $T^3=I$ exactly
(residual $\sim10^{-15}$) — a genuine order-3 automorphism, not an artifact.
The 6-dimensional $+1$-eigenspace matches, dimension-for-dimension, the
already-computed $\dim\,\mathrm{Stab}_{G_2}(H)=6$ (consistent cross-check:
$G_2$-elements must be triality-fixed, i.e. eigenvalue $+1$ under this map).

**Consequence:** $\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$, *as it acts on
the vector representation*, is not an arbitrary or convenient basis choice —
it is a genuinely triality-*compatible* structure: the $G_2$-part (6-dim) is
fixed pointwise as required, and the remaining, non-$G_2$ 6 dimensions
organize into three independent 120°-rotation planes under the SAME order-3
symmetry already used throughout this project. This substantially
strengthens point 3 of the prior "what remains open" list, at the
vector-rep level specifically — see below for why it does **not** yet
license any claim about the spinor-rep ($\Gamma_A,\Gamma_B$) structure.

**What is still NOT done, honestly:**
- The precise cyclic bookkeeping across all three roles simultaneously
  (does relabeling $(a,b,c)\to(b,c,a)$ satisfy the *same* covariance
  equation) was not resolved — naive relabeling failed, and the correct
  fix (almost certainly an octonion-conjugation twist) was not tracked
  down. This does not affect the main finding (order-3 invariance of the
  subalgebra, verified independently via the $a\mapsto b$ matrix $T$
  alone), but the full three-role symmetry bookkeeping remains open.
- This check was done at the **vector representation** level (how the
  Lie algebra $\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ itself transforms
  under triality). It has NOT yet been connected back to the **spinor-level**
  finding above ($\Gamma_A,\Gamma_B$ same-vs-opposite chirality distinguishing
  $8_s$ from $8_c$) — i.e. whether this order-3 symmetry, expressed on the
  spinor side, is what actually correlates with (or explains) the
  same/opposite chirality split. That connection is the natural next step.
- Points 1 and 2 of the "what remains open" list above (physical
  identification with $S^3$, dynamical consistency with G73/E-L3B/G102) are
  entirely unaffected by this check and remain fully open.

**Attempted 2026-07-15 (same day, continued once more) — tried to connect
the vector-rep triality-invariance result above to the spinor-rep
$(\Gamma_A,\Gamma_B)$ finding directly. First pass found an apparent
obstruction (below); a follow-up pass the same round corrected it. Read
both — the correction is the standing result.**

*First pass (superseded below, kept for the record):* computed the
triality-*transported* image of $\mathfrak{so}(4)_1$ (the 6-dim span of the
$b$-partners of its basis generators — confirmed a genuine closed Lie
subalgebra) and found its Casimir eigenvalues *degenerate* (all 8 equal),
unlike the untransported $\mathfrak{so}(4)_1$ on $V$ (2 distinct
eigenvalues: nonzero on $H$, zero on $H\ell$). This was read as "the
transported algebra does not preserve the $H/H\ell$ split." **That reading
was wrong** — a degenerate Casimir is exactly what two *isotypic* (same
representation type) invariant 4-dim blocks would also produce, and this
was not checked before concluding "no split."

*Corrected result, `[VERIFIED]` via explicit isomorphism:* the two Cl(8)
realizations used today — Pauli-tensor ($\Gamma_1,\dots,\Gamma_8$, used for
$\Gamma_A,\Gamma_B$) and octonion-covariance (V=S+=S-=$\mathbb{O}$, used for
the triality map) — are representations of the *same* abstract
$\mathfrak{so}(8)$. By Schur's lemma, if "$8_s$" and "$S^+$ (via $b$)" are
genuinely the same real-type irrep, there is a **unique** (up to scalar)
intertwiner. Built it directly: solved $P\,M_a = b_a\,P$ for all **28**
basis generators of the *full* $\mathfrak{so}(8)$ (not just the
$\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ subalgebra, to pin down
uniqueness genuinely) — found nullity exactly 1, residual $\sim10^{-16}$
over all 28 generators. Built the analogous $Q$ for "$8_c$"$\leftrightarrow$"$S^-$
(via $c$)", same result.

Used $P,Q$ to transport $\Gamma_A$ (which commutes with $\Gamma_9$, hence
genuinely acts within each of $8_s,8_c$ separately) into the octonion
language:
$$P\,(\Gamma_A|_{8_s})\,P^{-1} = D_A := \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1),
\qquad Q\,(\Gamma_A|_{8_c})\,Q^{-1} = -D_A,$$
exactly (residual $\sim10^{-15}$, both real to machine precision) — i.e.
$\Gamma_A$ *is*, under this explicit identification, precisely the $H$-vs-$H\ell$
block-sign operator. $\Gamma_B$ transports to $+D_A$ on **both** $S^+$ and
$S^-$ (consistent with $\Gamma_A=\Gamma_B$ on $8_s$ and $\Gamma_A=-\Gamma_B$
on $8_c$ by construction — a clean internal consistency check).

**Then, checked directly whether $D_A$ commutes with all 12 transported
$\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ generators — the test the first
pass skipped.** It does, exactly (residual $\sim10^{-15}$ for every
generator). This means the $H/H\ell$ block split **is** an invariant
structure of the triality-transported algebra — confirmed by direct
commutation, not inferred from a Casimir spectrum that could not
distinguish "irreducible" from "two isotypic blocks."

**Consequence — this closes the gap the prior "honest correction" left
open.** The vector-rep triality-invariance finding and the spinor-rep
$(\Gamma_A,\Gamma_B)$ finding are now shown, via an explicit, machine-verified
isomorphism, to be **the same structure**: the $H/H\ell$ block-sign operator
$D_A$ (equivalently, $\Gamma_A/\Gamma_B$) is preserved by the entire
triality-invariant $\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ — both its
$G_2$-fixed part and its order-3-rotating part — consistently across $V$,
$S^+$, and $S^-$.

**What this does NOT yet establish:** the connection is now solid at the
representation-theory level, but points 1–2 from before (physical
identification of either $\mathrm{SO}(4)$ factor with $S^3$'s actual gauge
fields; dynamical consistency with G73/E-L3B/G102 once $G_2$ is broken this
way) remain exactly as open as before — this round closed a mathematical
bookkeeping gap, not a physical one. The precise cyclic $(a,b,c)\to(b,c,a)$
bookkeeping across all three roles (flagged earlier as unresolved) also
remains open, though it did not block this result (only pairwise $a\to b$
and $a\to c$ relations were needed).

**Kill criterion, narrowed a fourth time (now on solid combined footing):**
the mathematical obstacle (no subgroup can distinguish $s$ from $c$) is no
longer absolute, and this is now a **single, unified** finding, not two
separately-solid ones: $\mathrm{SO}(4)\times\mathrm{SO}(4)$ genuinely
distinguishes $s$ from $c$ (via $\Gamma_A,\Gamma_B$ $\equiv$ $D_A$), is a
genuine order-3-triality-invariant subalgebra of $\mathfrak{so}(8)$, and
these are verified to be the same object across $V,S^+,S^-$ via an explicit
intertwiner. The remaining gap is entirely points 1–2: physical realization
and dynamical consistency — not representation-theoretic possibility, and
not (any longer) a bookkeeping gap between two unconnected pictures. This is
the most promising open thread from today's work, and the most concrete
starting point if/when Part 5's content becomes available.

**Attempted 2026-07-15 (same day, checked against an external literature-search
proposal) — tried to verify whether an "exact-kernel-stability radius" argument
(index invariance + this project's own existing spectral gap) could upgrade
the lower bound $N_{\mathrm{gen}}\ge3$ to an exact $N_{\mathrm{gen}}=3$ under a
$G_2$-breaking $\mathrm{SO}(4)\times\mathrm{SO}(4)$ perturbation. Found this
does NOT work as hoped, for a reason specific to this project's own prior
result, not a new derivation.**

*Index-invariance half (sound, cheap):* for a continuous deformation of the
connection on a fixed bundle, $\mathrm{ind}\,D_{\alpha,t}^+$ is homotopy-invariant
(standard index theory — the index depends only on the stable symbol class,
not the connection). This gives, for free, that $\dim\ker D_{\alpha,t}^+\ge1$
per channel survives any continuous $\mathrm{SO}(4)\times\mathrm{SO}(4)$-type
deformation — $N_{\mathrm{gen}}\ge3$ is robust.

*Exact-kernel half (does NOT survive, `[VERIFIED]` by re-reading this
project's own G74A):* this project already has a Lichnerowicz-type spectral
gap establishing $\dim\ker=1$ *exactly* per channel (not just $\ge1$) — see
`experiments/20260621-g74a-lichnerowicz-gap/decision.md`. But that result is
**two independent lemmas**, not one: Lemma A (Lichnerowicz/Weitzenböck gap,
safety factor $45/8$) bounds *accidental* zero modes and is the kind of
spectral-gap argument expected to survive small perturbations; Lemma B
(G$_2$-Schur cap, giving $\dim\ker\le1$ — the part that makes the bound
*exact*, not just a lower bound) is explicitly recorded in that same
decision.md as depending on **exact** $G_2$-symmetry: *"Does NOT apply if
$S^6$ is deformed away from the round metric... Lemma B depends on exact
$G_2$ symmetry"* (G74A's own "What this does NOT mean," point 2, written
2026-06-21, a month before today's $\mathrm{SO}(4)\times\mathrm{SO}(4)$ work).

**Consequence:** the moment a $G_2$-breaking perturbation is turned on — which
is not optional, it is the entire mechanism's premise — Lemma B's proof
method (Schur's lemma applied to an *exact* symmetry) does not degrade
gradually with perturbation size; it simply no longer applies, at any
nonzero perturbation. This is not a "stability radius" question (as the
external proposal framed it) — there is no radius to compute, because the
tool itself requires exactness. So: $N_{\mathrm{gen}}\ge3$ survives (via
index invariance, cheaply); the "$=3$, not more" upper bound does **not**
automatically survive, and would need an independent argument (e.g. a
$K=\mathrm{Spin}(4)\times\mathrm{Spin}(4)$-equivariant analogue of Lemma B,
not yet attempted) before this project could claim the exact zero-mode count
is protected under the very perturbation this whole route requires.

**Attempted 2026-07-15 (same day, continued) — tried to build the
$K$-equivariant analogue of Lemma B directly. Found a structural obstruction
to the whole approach, not a number.**

*Computed, `[VERIFIED]`:* the joint kernel of all 12
$\mathfrak{so}(4)_1\oplus\mathfrak{so}(4)_2$ generators, acting on each of
$\mathbf8_v$ (directly, vector rep) and $\mathbf8_s,\mathbf8_c$ (via the
spin-lift, i.e. restricting $\sigma_{ij}=\tfrac14[\Gamma_i,\Gamma_j]$ to each
chirality eigenspace) is **zero-dimensional in all three channels** —
$\mathrm{SO}(4)\times\mathrm{SO}(4)$ has no invariant vector anywhere in the
fiber (consistent with the branching computed earlier: none of the pieces
$(4,1),(1,4),(2,1;2,1),\dots$ is the fully trivial $(1,1;1,1)$).

*Why this number does NOT give an upper bound the way it did for $G_2$
(the actual finding):* Lemma B's mechanism is not "count singlets in the
fiber" in the abstract — it relies on a specific fact about **homogeneous
bundles**: since $G_2$ acts *transitively on the base* $S^6=G_2/\mathrm{SU}(3)$,
Frobenius reciprocity gives $\{G_2\text{-invariant sections}\}\cong
\{\mathrm{SU}(3)\text{-invariant vectors in the fiber}\}$ — this is what
turns a fiber-representation count into a statement about zero modes (which
are sections). $K=\mathrm{Spin}(4)\times\mathrm{Spin}(4)$, as constructed
today, acts **only on the fiber, uniformly at every point of $S^6$** — it
does not act on the base at all. Without a $K$-action on the base, there is
no analogous invariant-sections-to-invariant-fiber-vectors correspondence to
invoke, so the computed "$0$" above is a real, verified fact about the fiber
but does **not** translate into "$\dim\ker\le0$" (or any other bound) for a
hypothetical $K$-equivariant Dirac operator — the inference step itself is
unavailable, not merely the number.

**Consequence:** a direct $K$-equivariant analogue of Lemma B does not exist
with current tools — not from insufficient computation, but because Lemma
B's proof technique structurally requires a symmetry acting on the *base*,
and $K$ currently does not. This sharpens (again) exactly what "Global
$K$-reduction" (§6, Round 67 in the literature-search proposal) would need
to supply: not merely *some* base action, but one specific enough that a
Frobenius-reciprocity-type argument applies — and even then, the relevant
invariant-counting question would be relative to whatever isotropy subgroup
of that base action is, not to $K$ itself. This is not resolvable without
new input (Part 5, or an explicit choice of how $K$ might act on $S^3\times
S^6$ jointly) and is not attempted further here.

**Update, 2026-08-11 (C75/C77/C78, `tom_s3_spinor_toy/experiments/20260811-c7[578]-*/decision.md`)
— the "Dynamics" open item above (point 2 of the "what remains completely
open" list, and the follow-up attempt just above) is now answered
directly and exhaustively, not merely narrowed further.** This project
did not have a real, non-surrogate physical Dirac operator when this
section was written (round59's twisted $D_{S^6}$, characterized in C73/
C73b, postdates this section by three weeks) nor a verified bridge into
its representation space (C70's $U_v$, also later). With both now
available: C75 tested round124's $\mathfrak{su}(3)+\mathfrak u(1)+
\mathfrak u(1)$ candidate directly against the physical $D$ — fails. C77
tested this section's own $\mathrm{SO}(4)\times\mathrm{SO}(4)$ candidate
(§1.5 above) the same way — fails, all 12/12 generators, large clean
violations. **C78 then computed the full commutant of $D$ within all 28
dimensions of $\mathfrak{so}(8)$ at once (not a third candidate, an
exhaustive search): the commutant equals $\mathfrak{su}(3)$ exactly,
dimension 8.** This is the answer to "does the actual physical Dirac
operator remain consistent, once $G_2$ is broken" that this section
correctly identified as needed and could not supply: **no — breaking
$G_2$ to reach any larger subalgebra of $\mathfrak{so}(8)$, including
this section's own $\mathrm{SO}(4)\times\mathrm{SO}(4)$ candidate, is
never consistent with the physical $D$**. The route closes for the same
reason this section's own final kill criterion already anticipated
(non-product, $G_2$-breaking construction needed) — now confirmed
computationally rather than left as an open requirement.

---

## 2. The precise question

$S^6 = G_2/\mathrm{SU}(3)$'s triality automorphism $\ZZ_3 \subset \mathrm{Aut}(\mathrm{SO}(8))$
gives three zero-mode bundles $E_v, E_s, E_c$, proved pairwise isomorphic as
$G_2$-equivariant objects (§1 above). If the physical compactification
carries **Spin(8) fibre symmetry** (not just $G_2$) acting on the octonion
fibre, the three representations $\mathbf{8}_v, \mathbf{8}_s, \mathbf{8}_c$
are pairwise non-isomorphic *as Spin(8) representations* (this is the
definition of triality), so Schur's lemma gives
$\mathrm{Hom}_{\mathrm{Spin}(8)}(\mathbf{8}_\alpha,\mathbf{8}_\beta) = 0$ for
$\alpha \ne \beta$ — the three channels become Spin(8)-invariantly
orthogonal, and $N_{\mathrm{gen}}=3$ follows as three *physically* distinct
generations, not merely three orthogonal copies of one structure.

**The question for Tom's framework:** does the physical construction (the
Kaluza-Klein mechanism of the S³ spin-connection framework, extended to
$S^3\times S^6$, or any successor construction — Part 5's local SU(4)
transformations are the most likely candidate) carry an internal Spin(8)
fibre symmetry acting on the octonion fibre of $S^6$? If yes, this section
specifies exactly what data closes L3b. If no, the question becomes "what
IS the external input, if not Spin(8)" — see §5.

---

## 3. What the input object must be, precisely

An explicit answer providing L3b closure should specify a real vector bundle
(or fibre object) $E$ over the compactification with a fibre
$F \cong \mathbf{8}_v \oplus \mathbf{8}_s \oplus \mathbf{8}_c$ (24-real-dimensional,
matching the fibre already implicit in the three triality channels), such
that:

1. **A unitary triality operator exists on the fibre:**
   $$U : F \to F, \qquad U^3 = \mathbb{1}.$$
   $U$ implements the order-3 automorphism that cyclically permutes
   $\mathbf{8}_v \to \mathbf{8}_s \to \mathbf{8}_c \to \mathbf{8}_v$ (the same
   $\ZZ_3 \subset \mathrm{Aut}(\mathrm{SO}(8))$ already used to define the three
   channels — this operator is not new, it is the geometric input already in
   the paper).

2. **The relevant Dirac-type operator commutes with $U$ on the physical construction:**
   $$[D, U] = 0.$$
   This is the condition that makes $U$-eigenspaces (equivalently, the three
   triality channels) invariant subspaces of the physical dynamics, not just
   of the bare geometry.

3. **A Spin(8) action on $F$ exists, extending $U$**, i.e. a representation
   $\rho : \mathrm{Spin}(8) \to \mathrm{GL}(F)$ under which $F$ decomposes as
   $\mathbf{8}_v \oplus \mathbf{8}_s \oplus \mathbf{8}_c$ genuinely (three
   pairwise-non-isomorphic Spin(8)-irreps), and such that $\rho$ commutes with
   whatever plays the role of the physical Hamiltonian/Dirac operator on the
   full compactification (not just the bare $S^6$ operator — this is the
   step that goes beyond what pure $S^6$ geometry, per G102, can supply).

4. **The three sectors are physically inequivalent, not just mathematically
   distinct**: some physical structure (a coupling, a boundary condition, a
   choice of frame/gauge bundle) must actually depend on which Spin(8) irrep a
   mode sits in — otherwise the Spin(8) label is bookkeeping, not physics, and
   would not license calling the three modes three separate generations.

5. **The corresponding projectors survive compactification.** Concretely: if
   $P_v, P_s, P_c$ are the $U$-eigenspace projectors on $F$, there must exist
   an argument (dimensional reduction, KK mode decomposition, or an explicit
   construction) that these projectors remain well-defined, mutually
   orthogonal projectors on the actual 4D physical spectrum after
   compactification — not merely on the abstract 6D or 10D fibre. This is the
   step that turns "three orthogonal zero modes on $S^6$" into "three
   generations observed in 4D."

---

## 3.5. Anti-circularity screening (added 2026-07-15, after reviewing Furey–Hughes arXiv:2409.17948)

A candidate can *look* like it satisfies §3 while actually begging the
question. Before evaluating anything against §3/§4, apply this screening
test first:

> Does the candidate **derive** three distinguishable sectors as a
> *consequence* of acting on the single, already-existing $S^3\times S^6$
> structure — via the triality automorphism $U$ already fixed in condition 1
> — or does it **postulate** $N$ separate copies/sectors matching the desired
> generation count from the outset, and merely check that each copy's
> *content* looks right?

Only the first kind can close L3b. The second kind answers a different
question (representation-**content** matching per generation-slot, the same
category as this project's own G69/G24 results) and must not be mistaken for
channel-**distinguishability**, however similar the algebra looks.

**Concrete case this test catches:** Furey & Hughes, "Three Generations and a
Trio of Trialities" (arXiv:2409.17948, *Phys. Lett. B* 2025) build three
generations from three *separately postulated* copies of $\CC\otimes\HH\otimes\OO$
— $(\CC_+\otimes\HH_+\otimes\OO_+)\oplus(\CC_-\otimes\HH_-\otimes\OO_-)\oplus(\CC_V\otimes\HH_V\otimes\OO_V)$
— each copy carrying its *own* internal $(V,\Psi_+,\Psi_-)$ triality triple
(9 total pieces across the 3 copies), with **no operator relating the three
copies to each other**. The authors state plainly that they adopt this
three-copy structure "as a working hypothesis" motivated by the observed fact
of three generations, not derived from a deeper symmetry principle. This is
the same ansatz-driven circularity this project already identified and
rejected once before, in gate G33-A1 (`null_results/INDEX.md`: "A1 requires
$N_{\mathrm{gen}}=3$ as input, circular"). It is a genuine, peer-reviewed
result about representation content — not a counterexample to §1's
established facts, and not a closure (or even a partial closure) of L3b.

**Rule:** an object $(F,U,\rho)$ only counts toward §3/§4 if the "three" in
$F=\mathbf{8}_v\oplus\mathbf{8}_s\oplus\mathbf{8}_c$ refers to the *same*
three channels this project already derived from $S^3\times S^6$'s own
triality automorphism (condition 1) — not to three independently-introduced
copies of a similarly-shaped algebraic structure.

---

## 4. PASS / FAIL criteria (for whoever evaluates a candidate construction)

| Outcome | Condition |
|---|---|
| **PASS — L3b closes** | An object $(F, U, \rho)$ satisfying all five conditions in §3 is exhibited, with $\rho$ genuinely extending $U$ to a full Spin(8) action that commutes with the physical dynamics (not just the bare $S^6$ Dirac operator), and condition 5 (projectors survive compactification) is argued explicitly, not assumed. Must also pass the §3.5 anti-circularity screen. |
| **PARTIAL** | Conditions 1–3 hold (a genuine Spin(8) symmetry commuting with $D$ exists) but condition 4 or 5 is not established — e.g. the symmetry exists but no argument shows the three sectors remain distinguishable after compactification, or no physical coupling actually depends on the label. This would be a real step forward but not yet a closure of L3b. |
| **NO — Spin(8) is not physically realized** | The physical construction's fermions are strictly associated to the $S^6$ frame bundle alone (i.e. no symmetry beyond what geometry already supplies) — this would CONFIRM G102's implication rather than contradict it, and means the third channel needs a fundamentally different mechanism, not a Spin(8) postulate. This is itself a useful, publishable answer (see §5). |
| **DISQUALIFIED — fails anti-circularity screen (§3.5)** | The candidate postulates $N$ separate copies/sectors matching the desired generation count instead of deriving them from the single existing structure. Answers a content-matching question, not this document's question. Not a PASS, PARTIAL, or NO — it simply does not address L3b. |

---

## 5. If the answer is "no Spin(8)"

This is not a dead end for the collaboration — it is itself informative. Per
gate G102, the *entire* internal geometric search space is exhausted; if
Tom's framework also does not supply Spin(8) fibre symmetry, that is strong
joint evidence that the third-generation mechanism (if one exists at all)
requires new physics beyond both frameworks as currently constructed — a
genuine open problem in beyond-geometric model building, worth stating
precisely as such rather than leaving implicit.

---

## 6. Scope note

This specification concerns **only** L3b (channel independence). It does
**not** ask about, and is not affected by, the separate $\mathrm{U}(1)_{B-L}$
open problem (gate G97 — B-L is not among the isometries of $S^3\times S^6$)
or the $\lambda$ non-perturbative-origin open problem — those are independent
questions, not entangled with this one.

---

## 7. Reference checklist for when Part 5 (or any physical input) becomes
available — "when is a projector physical, not just a math label?"

Recorded 2026-07-15 from an external methodology review of today's
$\mathrm{SO}(4)\times\mathrm{SO}(4)$ candidate. Not a new result — a
checklist to apply *once physical input exists*, since most of its gates
(2, 5, 6 below) are unanswerable from pure geometry and were the reason
today's pure-math thread on this candidate stopped here.

**Core principle:** a mathematical projector $P_k$ (however elegant its
Hilbert-space splitting) is *physical* only if the splitting survives gauge
identification and has an operational (measurable) consequence — not merely
because $U^3=1$, $[D,U]=0$, and the $P_k$ are orthogonal. An arbitrary
$V\in\mathrm{U}(3)$ would produce an equally "valid" set of projectors
unless something pins the basis down.

**Two architectures — do not conflate them:**
- *Architecture I, exact triality:* $U^3=1$, $[D_{\mathrm{full}},U]=0$
  throughout. Requires proving $U$ is not a gauge redundancy, is
  non-anomalous, and is compatible with masses/mixing (risk: exact
  conservation can forbid CKM/PMNS-type mixing).
- *Architecture II, triality as a high-energy organizer:* $[D_0,U]=0$ at the
  geometric level, but $[D_{\mathrm{full}},U]\ne0$ once an order parameter or
  Yukawa coupling is turned on. $U$ explains the *origin* of the
  3-dimensional space; physical distinguishability then comes from the
  *broken*-symmetry spectral projectors of the mass/Yukawa operators instead
  ($M_uM_u^\dagger$, $M_dM_d^\dagger$, $M_eM_e^\dagger$), not from $U$ itself.
  This project's own G74A finding (Lemma B needs *exact* $G_2$, does not
  survive breaking) is a concrete instance of exactly this tension — Note:
  if $\Phi=\sum_k\phi_kP_k$ where $P_k$ are $U$'s *own* spectral projectors,
  $\Phi$ trivially commutes with $U$ (it is a function of $U$) — a genuine
  breaking term must be off-diagonal in $U$'s eigenbasis or permute distinct
  slot-projectors, not merely be diagonal with unequal eigenvalues.

**Gates to check once physical input exists (not attemptable from pure
geometry alone):**

| Gate | Question |
|---|---|
| 1 | Are $\mathbf8_v,\mathbf8_s,\mathbf8_c$ algebraically distinguished as $K=\mathrm{Spin}(4)^2$-branchings? — **already done today**, verified. |
| 2 | Does $K$ act *globally* (a principal-bundle reduction over the actual compactification, not just the fiber)? — **the blocker**, needs Part 5. |
| 3 | Gauge-orbit audit: is $K$ (or $U$) a gauge redundancy or a genuine global symmetry? |
| 4 | Zero-mode map: does $P_k\cap\ker D$ have the right dimension *and* chirality once $K$ acts on the full construction? |
| 5 | Is a 4D effective action (Yukawa operators $Y_u,Y_d,Y_e$ or equivalent) *derived*, not postulated? |
| 6 | Basis-invariant observables only: $\mathrm{spec}(Y_fY_f^\dagger)$, not raw matrix entries. |
| 7 | Anti-circularity: is "three" ever hand-inserted (three copies, $\mathbb{Z}_3^{\mathrm{family}}$, three Yukawa coefficients) rather than derived? |

**Caution carried over from today's own work:** do *not* require a
nontrivial common commutant of $Y_u,Y_d,Y_e$ as a success criterion — CKM/PMNS
mixing exists precisely *because* $[Y_uY_u^\dagger,Y_dY_d^\dagger]\ne0$; a
family symmetry exact enough to force a shared eigenbasis for all Yukawa
matrices risks forbidding the observed mixing entirely.
