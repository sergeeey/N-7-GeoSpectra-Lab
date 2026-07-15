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

## 4. PASS / FAIL criteria (for whoever evaluates a candidate construction)

| Outcome | Condition |
|---|---|
| **PASS — L3b closes** | An object $(F, U, \rho)$ satisfying all five conditions in §3 is exhibited, with $\rho$ genuinely extending $U$ to a full Spin(8) action that commutes with the physical dynamics (not just the bare $S^6$ Dirac operator), and condition 5 (projectors survive compactification) is argued explicitly, not assumed. |
| **PARTIAL** | Conditions 1–3 hold (a genuine Spin(8) symmetry commuting with $D$ exists) but condition 4 or 5 is not established — e.g. the symmetry exists but no argument shows the three sectors remain distinguishable after compactification, or no physical coupling actually depends on the label. This would be a real step forward but not yet a closure of L3b. |
| **NO — Spin(8) is not physically realized** | The physical construction's fermions are strictly associated to the $S^6$ frame bundle alone (i.e. no symmetry beyond what geometry already supplies) — this would CONFIRM G102's implication rather than contradict it, and means the third channel needs a fundamentally different mechanism, not a Spin(8) postulate. This is itself a useful, publishable answer (see §5). |

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
