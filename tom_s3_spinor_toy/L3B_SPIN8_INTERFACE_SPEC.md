# L3b Interface Specification — what a Spin(8) fibre-symmetry input must provide

**Status:** drafted 2026-07-14, NOT sent. Per this project's own standing
constraint, contact with Tom Lawrence is not initiated proactively — he
reaches out when Part 4/5 are ready. This document exists so that, when
contact happens, the single open technical question can be handed over as a
precise specification instead of a vague "we need Spin(8) symmetry."

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
