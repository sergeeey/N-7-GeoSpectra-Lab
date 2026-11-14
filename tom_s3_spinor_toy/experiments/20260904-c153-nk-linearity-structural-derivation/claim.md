# C153 — the twist-connection response factors per root plane

**Question type (EstimandOps L0): DESCRIPTIVE.** Structural characterisation
of an already-computed object (C152's corrected `SU(3)/T²` sector); no
counterfactual, no DAG required.

## ⚠️ CORRECTION 2026-09-04, same day — NOVELTY CHECK, run post-hoc before
## authorizing C154, per user instruction. Downgrades this file's headline.

A literature novelty check (`novelty_check.md`, `skeptic-auditor` + WebSearch)
found that **both** halves of this round's headline are classical, not new:

1. The 6-integrable/2-non-integrable split of the 8 invariant almost-complex
   structures on `SU(3)/T²`, via the Weyl-group `S₃` orbit, is **Borel–Hirzebruch
   (1958) §13.7** and **Burstall–Salamon (1987, Math. Ann. 277)** — exactly the
   "candidate C154" hypothesis this round's own caveat named as unverified.
   It did not need building; it already exists.
2. The per-plane multiplicative law `c((J_eps)|_plane k) = i^{eps_k} · c(v_k)`
   is **entailed by Schur's lemma alone**: `m` splits into pairwise-inequivalent
   root-plane summands (multiplicity one), the `±i`-per-root-plane action is
   the very definition of an invariant a.c.s. in Borel–Hirzebruch's own
   parametrization, and any `T²`-equivariant map — `c` is one, by construction —
   is therefore FORCED to respect the splitting. This was true before any
   computation in this round ran; it is not a fact about this operator, about
   twisted Dirac operators, or about nearly-Kähler geometry at all.

**What survives:** an independent exact verification that this specific
operator conforms to the generic pattern (real, but much weaker than
"headline structural discovery"), and the located classical references. The
Nijenhuis correlation (item 3 below) is now understood as the *composition*
of two already-known facts, not new evidence linking this operator to NK
geometry specifically.

**Kept in place below, corrected in place, per this project's discipline —
same class of correction as C144's "algebraically forced by total
antisymmetry".** Read every claim below as "verified, not discovered."

---

**Earlier revision, same day, still valid as a correction (kept for
continuity): after a context-blind FL Step 8a skeptic pass.** The original
version of this file claimed "24 direct tests" and a relabelling-based
Nijenhuis correlation. Both were real bugs in the *evidentiary weight*
claimed, not in the underlying arithmetic — see decision.md's Response
Matrix for the full account.

## Claim (falsifiable)

1. **Per-plane multiplicative law — 3 independent facts, not 24.** The
   6-dimensional connection family's basis (found by exact nullspace, not
   SVD) is **block-local**: columns `(0,1)`, `(2,3)`, `(4,5)` are supported
   *only* on root planes `1,2,3` respectively (verified directly — each
   column is zero outside its own pair of rows). `acs_from_eps` is *exactly*
   block-diagonal by construction (it only ever writes the `(2k,2k+1)` /
   `(2k+1,2k)` entries). Consequently, for a family vector supported on
   plane `k`, the result **cannot** depend on the other two planes' signs —
   this is forced by the two block structures, not a separately falsifiable
   fact. What genuinely required computation, and is genuinely confirmed,
   is **3 facts**, one per plane:

   ```
   c((J_{eps})|_plane 1 · v_1) = i^{eps_1} · c(v_1)      (eps_1 = +1 case computed;
   c((J_{eps})|_plane 2 · v_2) = i^{eps_2} · c(v_2)       eps_1 = -1 follows from
   c((J_{eps})|_plane 3 · v_3) = i^{eps_3} · c(v_3)       linearity + J(-eps)=-J(eps),
                                                           verified, not independent)
   ```

2. **The pre-registered 2-of-8 global C-linearity is a corollary** of these
   3 facts: a single global sign `c(J_eps·∇) = ±i·c(∇)` holds iff all three
   agree, i.e. `eps_1=eps_2=eps_3` — exactly 2 of `2^3` combinations, a
   combinatorial consequence requiring no separate explanation.

3. **Nearly-Kähler-ness (Nijenhuis ≠ 0) is exactly the "all-agree" set —
   confirmed NON-tautologically.** The Nijenhuis tensor was recomputed
   **directly in the aligned basis** (no relabelling from a raw-basis
   computation — a first version of this check *did* relabel, and a
   skeptic pass showed that construction gives `{(1,1,1),(−1,−1,−1)}` for
   **any** conjugate pair whatsoever, making it uninformative about
   Nijenhuis specifically; withdrawn, replaced). The direct, independent
   computation gives non-integrable exactly at `{(1,1,1),(−1,−1,−1)}`,
   matching the independently-computed C-linear set exactly.

4. **Exact, not floating-point**, for items 1–2 and the direct part of item
   3: a from-scratch exact-`sympy` reconstruction of the whole `SU(3)/T²`
   geometry (basis, Nomizu connection, `T²` Cartan generator, invariant
   sectors, 6-dim connection family, and now the Nijenhuis tensor — all via
   `sympy.Matrix.nullspace()` or direct exact bracket computation, no
   `numpy` SVD anywhere in this chain).

## Kill criterion

- a `(plane, eps_k=+1)` computation whose sign is not `+i`;
- the direct aligned-basis Nijenhuis non-integrable set differing from the
  independently-computed C-linear set;
- the exact reconstruction failing its exact-family-dimension `= 6`
  regression, or the direct Nijenhuis computation failing to reproduce
  Stage 1a's own `max|N|=4` (non-integrable) vs `0` (integrable) split.

**Explicitly NOT kill criteria (corrected — see Response Matrix):** the
`(3,3)` sector-dimension check and "Levi-Civita ∈ family" are **not**
sensitive to the `±T²` generator sign — proven algebraically (conjugation by
`diag(1,−1,1,−1,1,−1)` maps the `+T²` construction to the `−T²` one exactly,
so both give `(3,3)`), and confirmed empirically: C151's original (wrong-sign,
`+T2_M`) construction and C152/C153's corrected (`−T2_M`) construction both
independently found `(3,3)`. These remain useful code-correctness
regressions; they are not evidence for the sign choice.

## What this does NOT establish

1. ~~Does **not** derive, from a general Lie-theoretic argument, *why*
   "all-agree" coincides with non-integrability... Concrete next step
   (candidate C154), not asserted.~~ **SUPERSEDED by the novelty check above
   — this derivation already exists and did not need building: Borel–Hirzebruch
   (1958) §13.7 and Burstall–Salamon (1987) both give it. See `novelty_check.md`.**
2. Does **not** generalise beyond `SU(3)/T²`'s 8 invariant structures to
   arbitrary almost-complex structures, nor to other nearly-Kähler cosets.
3. Does **not** bear on `S⁶`, where there is no analogous multi-`J` question
   (isotropy `SU(3)` rigidifies `J` to a single one up to sign, C147).
4. Does **not** bear on `N_gen = 3` or any physical claim.
5. Does **not** claim the "24 tests" framing from the withdrawn first
   version — see decision.md for the full account of why that overclaimed.
