# C168 Claim — P4 Step 2: does the diagonal ℤ₃ orbifold induce an exclusive
# or non-exclusive channel↔t-sector pairing rule?

**Date:** 2026-09-06
**FL tier:** [x] Full
**Question type:** [x] descriptive (a representation-theoretic/topological
fact about a specific group action either holds or does not; no
intervention, no counterfactual population)

---

## Prior Result Gate (MANDATORY — filled BEFORE computation)

1. **Exact claim under test:** does the DIAGONAL ℤ₃ action `(g,c) ↦
   (ζ₃·g, τ(c))` on `S³ × {v,s,c}` — built from C167's `ζ₃` (left
   translation on `S³`, order 3, freeness and holonomy `Ad(ζ₃)`
   already certified) and `pearl_registry` row 33 / C133 / G75's `τ`
   (the order-3 cyclic permutation of the three `Spin(8)` triality
   channels `{8_v,8_s,8_c}`, already certified to cyclically permute
   the channels, `C135 §5d [VERIFIED]`) — induce, at the
   representation-theoretic/classification level, an EXCLUSIVE
   (each channel → exactly one `t`-sector) or NON-EXCLUSIVE
   (`all→both`) pairing between channel content and the two `t`-sector
   spinor holonomies `H_{t=0}=Id`, `H_{t=1}=ζ₃` (the spin-level lift of
   `Ad(ζ₃)`, unambiguous since `p=3` is odd, `H¹(L(3,1);ℤ₂)=0`,
   per C167's own spin-structure finding)?
2. `decision.md` grep across `experiments/**/decision.md`,
   `null_results/INDEX.md`, `parked/INDEX.md`,
   `pearl_registry/INDEX.md` for "diagonal ℤ₃", "diagonal action",
   "triality correlation", "channel.*t-sector pairing",
   "Ad(zeta).*tau", "regular representation.*channel": **done.**
   Hits: (a) C132's own P4 sketch (source document, not a prior
   attempt at THIS computation); (b) C167 (Step 1, holonomy only, this
   round's own direct predecessor, explicitly scoped OUT the
   triality-correlation question — see its "What this does NOT mean"
   #1); (c) C133 (`decision.md` §9) derives, via an UNRELATED
   mechanism (assumed `Spin(8)+ℤ₃`-invariance of a channel-uniform
   *coupling*, Schur's lemma, no geometry/orbifold), that the space of
   nonzero support patterns of such a coupling is exactly
   `{all→t=0, all→t=1, all→both}` — i.e. non-exclusive survives. This
   is a DIFFERENT mechanism (abstract coupling-invariance vs.
   geometric quotient-equivariance) reaching a structurally similar
   question; non-transfer is addressed explicitly in this round's
   analysis (§5 below), not assumed. (d) C135 establishes `τ`
   cyclically permutes the three channel *sectors* (not merely a
   convenient basis), `[VERIFIED]`, and flags that canonicity of the
   underlying basis choice and the physical (spinor-level, Dirac-
   operator-coupled) realization remain open — exactly the open items
   this round's construction must not silently assume closed.
3. `round*_claim.md` + scripts grep: done. 0 hits for "diagonal
   ℤ₃ orbifold" as a computed (not sketched) object outside C132/C167.
4. `null_results/` + `parked/` grep: done. G27-ℤ₃ (S⁶, not S³,
   non-transferable per C167's own Gate-1 finding) is the only nearby
   hit; re-confirmed non-transferable here for the same reason.
5. `git log -S "diagonal"` restricted to this experiment family:
   not re-run (C167 already ran the equivalent search for the
   holonomy half; this round's specific object — the tensored
   spinor⊗channel action — has no prior hits per items 2–3 above).
6. Primary sources re-read in full this session: C167 `claim.md` +
   `decision.md` (Step 1, holonomy result and its own explicit
   "NOT this round" scope note); C132 `decision.md` §`P4` (mechanism,
   costs, circularity warning) and its CDT table row (line ~708);
   `pearl_registry/INDEX.md` rows 33 (τ's origin, Baez `S₃⊂F₄`,
   dated 2026-07-15) and 41 (the `so(4)+so(4)` `T`, `T³=I`, dated
   2026-07-15, a DIFFERENT object from τ — see §5); C133
   `decision.md` (the `9→3→1` ladder and §9's `{all→t0,all→t1,
   all→both}` support-pattern result); C135 `decision.md` in full
   (τ's certified action on the three channel *sectors*, §5d,
   and its own honest limits, §6a — spin lift and basis bridge
   NOT established there either); C159 `decision.md` (the
   exclusive-pairing-is-arithmetically-impossible-for-odd-N_gen
   result this round's classification is checked against);
   `experiments/20260622-g75-triality-independence/decision.md` +
   `.py` (an independent, earlier, 2026-06-22 realization of τ
   directly on the physical zero-mode space, diagonal with
   eigenvalues `{1,ω,ω²}` — reused as a cross-check, not the sole
   construction of τ, see §5).
7. **Status:** [x] NEW — this is the first round to build the
   TENSORED diagonal action and ask what it forces on channel
   content, as opposed to (i) the bare holonomy alone (C167) or
   (ii) an unrelated coupling-invariance argument for the same
   support-pattern question (C133).

Not CLOSED/SUPERSEDED/DUPLICATE/RETRACTED/PARKED → proceeding.

---

## Estimand

**Population:** the diagonal ℤ₃ action on `S³ × {v,s,c}` and the induced
action on `(spinor bundle of S³, holonomy H_t) ⊗ (channel label space,
action τ)`, for `t∈{0,1}`, as a REPRESENTATION-THEORETIC/classification
object — not the physical Dirac operator itself.

**Intervention:** none — descriptive, not interventional.

**Comparator:** C133's abstract `Spin(8)+ℤ₃`-invariant-coupling result
(§9, `{all→t0, all→t1, all→both}`), used as the standard this round's
geometric construction is checked for consistency against, and C159's
"exclusive is arithmetically impossible for `N_gen=3` odd" result, used
as the discriminating filter.

**Endpoint:** for each `t∈{0,1}`, the dimension of the eigenvalue-1
(invariant) subspace of `H_t ⊗ τ`, and — for each invariant eigenvector,
decomposed back into the `{v,s,c}` channel basis — whether all three
channels have nonzero weight (non-exclusive) or a strict subset
(exclusive / partial).

**Summary measure:** categorical — one of the five verdict strings in the
Kill criterion table below.

**MCID:** not applicable (categorical classification, not a continuous
effect size).

**ICE:** none — closed-form algebraic/representation-theoretic
computation, no sampled process.

---

## Claim

**C1 (primary):** the diagonal ℤ₃ action's induced spinor⊗channel
representation `H_t ⊗ τ` has a well-defined, computable invariant
subspace for both `t=0` and `t=1`, and decomposing that subspace back
into `{v,s,c}` shows all three channels participate (non-exclusive) in
BOTH sectors — consistent with, and structurally continuous with,
C133's abstract `all→both` result and C159's survival criterion.

**C2 (the honesty check this round exists to run, per the task's own
instruction to verify the AOG-5 argument rather than accept it):** the
qualitative shape of C1's result (dimension of invariant subspace = 2 in
both sectors; all three channels participate in both) is **forced by τ
being a REGULAR representation of ℤ₃ on 3 letters, independent of the
specific holonomy value `H_t`** — a standard representation-theory fact
(`V ⊗ (regular rep) ≅ dim(V)` copies of the regular rep, for ANY `V`).
This round computes this generality directly (by substituting `H_1` with
a generic order-3 element and with the identity) rather than asserting
it. If confirmed, C1's finding carries LOW independent discriminating
power beyond C133 — a result this round is obligated to report honestly,
not one that would be convenient to omit.

**C3 (AOG-5 anti-circularity, verified not merely asserted):** the
order-3 nature of τ traces to an EXTERNAL, pre-existing mathematical
fact (`Spin(8)` triality: the outer automorphism group of `D₄` is `S₃`,
order 6, containing an order-3 element — a fact of Lie theory since
Cartan/Élie's triality work, cited here via Baez arXiv:math/0105155,
`pearl_registry` row 33) — NOT tuned within this project to match
`N_gen=3`. The project's OWN use of this fact (G75, 2026-06-22; row 33,
2026-07-15) was already in service of explaining `N_gen=3`, so
independence holds at the level of "why is the group order 3"
(external, pre-project, physics-independent), not at the level of
"why did this project reach for triality at all" (internal,
generation-motivated) — both halves are stated explicitly, not
conflated.

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| K1 — the diagonal action is not free | `∃k∈{1,2}: (ζ₃^k, τ^k) fixes some (g,c)` while `ζ₃^k≠I` → would need separate proof; if the action is non-free `NO-WELL-DEFINED-PAIRING-INDUCED` |
| K2 — invariant subspaces of `H_t⊗τ` have dimension 0 for some `t` | no nonzero invariant vector exists → the construction admits NO surviving field in that sector → `NO-WELL-DEFINED-PAIRING-INDUCED` |
| K3 — invariant subspace decomposes onto a STRICT SUBSET of `{v,s,c}` for some `t` (some channel has exactly zero weight in every invariant vector of that sector) | → `EXCLUSIVE-PAIRING-INDUCED` (or a partial/mixed pattern, reported as found) — per C159, this would need re-examination for arithmetic (im)possibility, not an automatic kill of P4, but a route-narrowing finding |
| K4 — all three channels have nonzero weight in the invariant subspace for BOTH `t=0` and `t=1` | → `NON-EXCLUSIVE-PAIRING-INDUCED` |
| K5 — the AOG-5 provenance trace shows τ's order-3 status was in fact tuned/selected to match `N_gen=3` (i.e. no independent, pre-existing, physics-unrelated mathematical source for "order 3" can be cited) | → `AOG-5-CIRCULARITY-CONFIRMED`, regardless of K1–K4's outcome |
| K6 — the generality check (C2) shows the invariant-subspace classification depends on the SPECIFIC value of `H_t` (not forced by τ alone) | if this fires, C1's finding would carry independent discriminating power (upgrades the finding's weight, does not change the verdict category) |
| K7 — the spin-lift / basis-bridge step (flagged open by C135 §6a and by C132's own `ι`/well-posedness caveat) turns out to be load-bearing for this round's specific computation and is not resolvable by direct computation this round | → `BLOCKED-NEEDS-KERNEL-COMPUTATION` |

**Verdict table (pre-registered):**
- `NON-EXCLUSIVE-PAIRING-INDUCED` — K4 fires, K1/K2/K5 do not. Survives
  C159's filter. PROMOTE CANDIDATE at the classification level only —
  explicitly NOT equivalent to a `dim ker D^t` computation.
- `EXCLUSIVE-PAIRING-INDUCED` — K3 fires with a genuine 1-channel-only
  pattern in some sector. Per C159, re-examine arithmetic; likely
  narrows or kills the route pending that check.
- `NO-WELL-DEFINED-PAIRING-INDUCED` — K1 or K2 fires. The construction
  itself is degenerate; REJECT this specific tensoring model (does not
  necessarily kill P4 as a whole — see "what this does NOT mean").
- `AOG-5-CIRCULARITY-CONFIRMED` — K5 fires. Overrides all other
  verdicts; PARK, flag circular per AOG-5, regardless of K1–K4.
- `BLOCKED-NEEDS-KERNEL-COMPUTATION` — K7 fires and cannot be resolved
  by direct computation this round. Classification-level result (if
  any) is reported as informative but insufficient; Step 3 required.

Multiple verdicts may co-fire (e.g. `NON-EXCLUSIVE-PAIRING-INDUCED` +
K6-negative, i.e. forced/low-power) — the table above gives the primary
categorical verdict; qualifying flags (K6, K7-partial) are reported
alongside it in decision.md, not silently dropped.

---

## Checks planned

- T1: reproduce `ζ₃` and `Ad(ζ₃)` exactly (re-derive via Pauli-basis
  conjugation, cross-check against C167's cited closed form, do not
  copy-paste without independent re-derivation).
- T2: build `τ` as the explicit 3×3 cyclic permutation matrix on
  `{v,s,c}` (matching G75's channel-index convention `v=0,s=1,c=2`
  and C133's `P: 1→2→3→1` slot map); verify `τ³=I` exactly, verify
  eigenvalues `{1,ω,ω²}` exactly via direct diagonalization (not
  assumed as in G75's diagonal-by-construction shortcut).
- T3: freeness of the diagonal action — direct consequence of `ζ₃`
  alone being free (already certified, C167 T5); re-verify the
  logical step explicitly (not just cite).
- T4: build spin-level holonomies `H_0=I_2`, `H_1=ζ₃` (the natural
  `SU(2)` lift, order exactly 3, unambiguous since `p=3` is odd per
  C167's spin-structure finding); state explicitly that `H_0=I_2` is a
  MODELING ASSUMPTION (spinor parallel transport trivial when the frame
  parallel transport is trivial), not independently re-derived from
  the Dirac operator this round.
- T5: compute `H_t ⊗ τ` for `t=0,1`, exact eigenvalues, invariant
  (eigenvalue-1) subspace dimension and explicit eigenvectors.
- T6: decompose each invariant eigenvector into per-channel weight
  (sum of squared magnitudes over the spinor index, per channel);
  classify exclusive vs non-exclusive per K3/K4.
- T7 (generality/forced-ness check, C2): repeat T5–T6 with `H_1`
  replaced by (a) a generic other order-3 `SU(2)` element (conjugate
  of `ζ₃` by a random unitary) and (b) the identity (degenerate
  control) — confirm whether the invariant-subspace dimension and
  channel-participation pattern are IDENTICAL regardless of `H_1`
  (forced by τ alone) or genuinely depend on `H_1`'s value.
- T8 (AOG-5 provenance): state and check the external-mathematical-fact
  argument (C3) explicitly; does NOT require new computation beyond
  citing Baez arXiv:math/0105155 and the dates already on record
  (row 33: 2026-07-15; G75: 2026-06-22; C132/P4 sketch: 2026-09-02).

---

## What this does NOT mean

1. Does NOT compute `dim ker D^t` on the actual quotient
   `(S³×S⁶)/ℤ₃_diag` — this round works at the representation-
   theoretic/classification level (spinor holonomy ⊗ abstract channel
   label), explicitly NOT the coupled Dirac operator itself. Per the
   task's own scoping permission, this is named as the honest limit,
   not silently assumed away.
2. Does NOT establish that `H_0=I_2`/`H_1=ζ₃` is the UNIQUE or even the
   physically correct way the actual Dirac zero-mode field transforms
   under the quotient — this is a MODELING CHOICE, consistent with
   C167's frame-level result but not independently re-derived from the
   spinor bundle's own transition functions this round.
3. Does NOT resolve C135 §6a's open items (the precise spin lift when a
   choice exists, and the basis bridge between the octonion-covariance
   and gamma-matrix `Cl(8)` realizations) — for `p=3` odd the spin lift
   is unambiguous per C167, which narrows but does not eliminate the
   basis-bridge question, left open here as it was there.
4. Does NOT constitute new evidence beyond C133 if C2/K6 is negative
   (forced-by-τ-alone) — this round is required to report that
   outcome plainly rather than present a forced consequence as a
   discovery (Perelman-audit / AOG discipline).
5. Does NOT resolve OB1 or reopen it — even under the strongest
   possible verdict (`NON-EXCLUSIVE-PAIRING-INDUCED`, K6 positive),
   this is Step 2 of a multi-round investment; OB1 remains
   `PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT` at the project level
   unless and until a future round's actual kernel computation
   produces something meeting that bar.
6. Does NOT re-litigate C133, C135, or C159's own verdicts — their
   results are cited and built upon, not re-run or re-derived from
   scratch beyond what is needed for this round's own tensored object.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False
- Do NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
  `null_results/INDEX.md`, `CLAIM_LEDGER.yaml` this round.
- Do NOT run git operations this round.

---

## Verdict

[FILLED IN decision.md]
