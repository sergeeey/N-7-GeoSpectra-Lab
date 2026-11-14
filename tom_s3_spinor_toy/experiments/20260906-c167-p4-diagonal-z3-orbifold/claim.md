# C167 Claim — P4 diagonal ℤ_p orbifold: holonomy-descent test (Step 1 only)

**Date:** 2026-09-06
**FL tier:** [x] Full
**Question type:** [x] descriptive (a topological/holonomy fact either holds or
does not; no intervention, no counterfactual population — this is NOT a causal
or predictive claim)

---

## Prior Result Gate (MANDATORY — filled BEFORE computation)

1. **Exact claim:** does the ∇^{t=0} (left-invariant) canonical connection on
   S³ descend to L(p,1)=S³/ℤ_p (ℤ_p ⊂ U(1) ⊂ SU(2) acting by LEFT translation)
   with trivial holonomy, while the ∇^{t=1} (right-invariant) connection does
   not — for p = 2,3,4,5?
2. `decision.md` grep (formula + synonyms "lens space", "L(3,1)", "S3/Z3",
   "diagonal ℤ₃ orbifold", "orbifold"): **done, hits reviewed.** Only hit
   besides C132's own survey text is `null_results/INDEX.md` row `G27-ℤ₃`
   (2026-06-19) — that round quotiented **S⁶**, not S³, by a free ℤ₃ and was
   REJECTed on `χ(S⁶)=2` / Smith theory, a completely different manifold and
   a completely different obstruction (Smith theory on S⁶ has nothing to say
   about S³). Non-transfer stated explicitly per Gate 1 (artifact-provenance):
   **the G27-ℤ₃ verdict does NOT transfer to this claim** — different
   manifold, different group action, different kill mechanism.
3. `round*_claim.md` + scripts grep: done, 0 hits for "lens space"/"L(p,1)"/
   "Ad(zeta)" outside C132's own survey prose.
4. `null_results/` + `parked/` grep: done — only the G27-ℤ₃ row above,
   non-transferable (see #2).
5. `git log -S "L(3,1)"` / `-S "Ad(zeta)"`: done — only hit is C132's own
   survey commit (`aa55383`), which is the source document for this round,
   not a prior attempt at the computation itself.
6. Primary source re-read (not from memory): `experiments/20260902-c132-13d-
   parent-action-survey/decision.md` §`P4` (lines ~404–440) and §5 CDT table
   (line 708) re-read in full this session. round72/E7's H1b proof
   (`experiments/20260717-round72-e7-t-selection-principle/decision.md`
   lines 27–57) re-read in full — this is the proof whose precondition
   (π₁(S³)=0) this round's quotient removes for exactly one endpoint.
7. **Status:** [x] NEW

Not CLOSED/SUPERSEDED/DUPLICATE/RETRACTED/PARKED → proceeding.

---

## Estimand

**Population:** the two Cartan–Schouten canonical connections ∇^{t=0}
(left-invariant parallel frame) and ∇^{t=1} (right-invariant parallel frame)
on S³=SU(2), as classified in round72/E7 and round99/111 (already-certified
in this project).

**Intervention:** none — this is descriptive, not interventional. The
"treatment" (quotienting by a free left ℤ_p action) is a mathematical
construction being examined, not an intervention on a population of units.

**Comparator:** the un-quotiented S³ (π₁=0), where round72/E7's H1b already
proved BOTH ∇^0 and ∇^1 have trivial holonomy (both parallel frames exist
globally) — that is the baseline this round modifies.

**Endpoint:** the holonomy representation of ∇^{t=0} and of ∇^{t=1} on
π₁(L(p,1))=ℤ_p, computed as an element of SO(3) (frame bundle) and, where
nontrivial, its lift to Spin(3)=SU(2).

**Summary measure:** binary per connection per p — trivial holonomy (Id) or
not — plus, where nontrivial, the explicit holonomy matrix/rotation angle.

**MCID:** not applicable (binary/exact result, no continuous effect size to
threshold).

**ICE:** none — no post-hoc events, this is a closed-form algebraic
computation, not a sampled/observed process.

---

## Claim

**C1 (primary, AOG-5 general form — this is the claim actually being tested,
not the p=3 instance alone):** for every p≥1, ζ_p = diag(e^{2πi/p},e^{-2πi/p})
generates a free ℤ_p action on S³=SU(2) by left translation; the
left-invariant frame of ∇^{t=0} descends to L(p,1) with trivial holonomy for
**every** p (structural — left-invariance is invariance under ALL left
translations, so it holds independent of p); the right-invariant frame of
∇^{t=1} descends with trivial holonomy **iff** ζ_p is central in SU(2), i.e.
iff p∈{1,2}, and with nontrivial Ad(ζ_p)-holonomy (rotation by 4π/p in SO(3),
lifting to a non-±Id element of Spin(3)=SU(2)) for every p≥3.

Supporting sub-claims:
1. The action g↦ζ_p·g is free for every p≥1 (standard: nonidentity element
   acting by left translation on a group has no fixed points).
2. (L_ζ)_* X_A(g) = X_A(ζg) EXACTLY (no twist) for left-invariant X_A, for
   every ζ∈SU(2), every p — this is the defining property of left-invariance,
   not p-dependent.
3. (L_ζ)_* Y_A(g) = Y_{Ad(ζ)A}(ζg) for right-invariant Y_A — a general
   identity for any Lie group, verified here as an exact matrix identity on
   SU(2), not merely asserted.
4. Ad(ζ_p) = Id_{su(2)} iff ζ_p ∈ {±I} (center of SU(2)) iff p∈{1,2}; for
   p≥3, Ad(ζ_p) is rotation by angle 4π/p ≠ 0 mod 2π, hence ≠ Id.
5. **AOG-5 discipline:** claim C1 is stated and tested for the GENERAL
   mechanism (all p, or a representative sweep p=2,3,4,5) BEFORE any
   privileging of p=3. p=3 is reported as one row of that sweep, not as the
   headline result in isolation.

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| K1 — asymmetry fails to appear at ANY tested p≥3 | Ad(ζ_p) computed = Id for some p∈{3,4,5} → `NO-ASYMMETRY-FOUND` |
| K2 — asymmetry appears ONLY at p=3, not at p=4,5 | Ad(ζ_p)≠Id at p=3 but =Id at p=4 or p=5 → `HOLONOMY-ASYMMETRY-ONLY-AT-P3` (red flag: likely the circular pattern AOG-5 warns against — choosing 3 because N_gen=3) |
| K3 — the left-invariant frame fails to descend trivially for some p (i.e. (L_ζ)_*X_A(g) ≠ X_A(ζg) as a matrix identity) | any nonzero residual in the direct matrix check → claim is internally inconsistent, STOP and re-derive |
| K4 — the p=2 case behaves like p≥3 (i.e. Ad(ζ_2)≠Id) | would contradict "ζ_p central iff p∈{1,2}" and needs explanation, not silent reporting | 
| K5 — well-posedness subtlety (ι / left-vs-right coset ambiguity) cannot be resolved by direct computation on the SAME quotient | if the direct (L_ζ)_* computation above is genuinely ambiguous (depends on an unstated choice) → `WELL-POSEDNESS-SUBTLETY-BLOCKS-CONCLUSION` |

**Verdict table (pre-registered):**
- `HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P` — asymmetry (Ad(ζ_p)≠Id) holds for
  ALL tested p≥3 (general mechanism, tied to non-centrality, not to p=3
  specifically) → PROMOTE candidate, proceed toward P4's step 2 in a future
  round.
- `HOLONOMY-ASYMMETRY-ONLY-AT-P3` — K2 fires → red flag, DO NOT PROMOTE,
  flag as likely circular per AOG-5, park.
- `NO-ASYMMETRY-FOUND` — K1 fires → mechanism fails, REJECT.
- `WELL-POSEDNESS-SUBTLETY-BLOCKS-CONCLUSION` — K5 fires → the question as
  posed is ill-defined, needs reformulation before any verdict, PARKED not
  REJECTed.

If FAIL (`NO-ASYMMETRY-FOUND` or K3 internal-inconsistency) → kills P4's
entire step-1 mechanism as stated in C132; P4 drops out of the Relaxation Map
without a step-2 attempt.
If PASS (`HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P`) → survives: P4 remains alive
for a future round attempting step 2 (triality-correlation/pairing).
If `HOLONOMY-ASYMMETRY-ONLY-AT-P3` → neither cleanly kills nor promotes —
routed to `parked/` with the circularity explicitly named, per AOG-5.

---

## Checks planned

- T1: symbolic/exact computation of Ad(ζ_p) as a 3×3 real matrix (via
  conjugation on the Pauli/su(2) basis) for p=2,3,4,5, plus a general
  symbolic-p derivation of the "Ad(ζ_p)=Id iff p|2" claim.
- T2: exact matrix-identity check of (L_ζ)_*X_A(g)=X_A(ζg) and
  (L_ζ)_*Y_A(g)=Y_{Ad(ζ)A}(ζg) on concrete SU(2) matrices (adversarial: pick
  non-diagonal, non-identity sample points g, not just g=I).
- T3 (adversarial/edge case): p=1 (trivial group, sanity: must give Ad=Id,
  “quotient” = S³ itself) and p=2 (degenerate: ζ=-I central, both
  connections must show trivial holonomy — this is the case most likely to
  be mishandled if the "non-centrality" argument is applied carelessly).
- T4: verify π₁(L(p,1))=ℤ_p (cited, standard) against π₁(S³)=0, to state
  explicitly which precondition of round72/E7's H1b proof is removed at
  which endpoint.
- T5: freeness check — ζ_p^k ≠ I for 0<k<p, for each tested p (exact, via
  sympy roots of unity, not floating point).

---

## What this does NOT mean

1. Does NOT establish that the t=0/t=1 asymmetry found here is the same
   object as (or feeds into) any triality-correlation / generation-pairing
   mechanism — that is P4's separate "step 2," explicitly out of scope this
   round per the task brief.
2. Does NOT establish that a Dirac zero mode actually disappears at t=1 on
   L(p,1) — this round tests holonomy of the CONNECTION/FRAME, not the
   Dirac operator's kernel dimension on the quotient directly (`dim ker D^t`
   on the quotient, named in C132's own P4 row, is NOT computed here).
3. Does NOT resolve which spin structure (for p even, where H¹(L(p,1);ℤ₂)=ℤ₂
   admits TWO inequivalent spin structures) the "trivially descending"
   left-invariant frame corresponds to — flagged as an open caveat for p
   even (p=2,4) specifically, not silently assumed away.
4. Does NOT constitute evidence for p=3 specifically unless the sweep shows
   the asymmetry is p=3-specific (K2) rather than general (see AOG-5
   discipline above) — a general result across p is evidence for a
   topological MECHANISM, not for N_gen=3.
5. Does NOT complete OB1 — even under `HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P`,
   this is Step 1 of a multi-round investment C132 itself flagged; OB1
   remains open pending step 2 and pending the Dirac-kernel computation on
   the actual quotient.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False
- Do NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
  `null_results/INDEX.md`, `CLAIM_LEDGER.yaml` this round (explicit scope
  boundary from the task brief — registry updates deferred to the calling
  session).
- Do NOT run git operations this round.

---

## Verdict

[FILLED IN decision.md]
