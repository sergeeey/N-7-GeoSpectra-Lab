# C158 — Decision

**Date:** 2026-09-05. **Tier:** FL Full. **L0:** descriptive.

**Verdict: TRUE, FULLY VERIFIED, COMPLETELY FORCED. Not a discovery — this is
the honest, complete self-audit outcome, arrived at by the round's own
internal cross-checking plus one independent skeptic pass.**

## The arc, in order

1. **G4 (Step 1):** built the genuine geometric `W(A_2)=S_3` action on `m`
   via `SU(3)` conjugation; verified `ker(M)` (C155's exact 4-dim kernel) is
   invariant under it. PASSED, exactly as pre-registered.
2. **Isotypic decomposition (Step 2):** `V_conn = trivial+sign+2*standard`,
   `ker(M) = 2*standard`, quotient `= trivial+sign`. Computed as data, no
   irrep pre-registered for the quotient (avoiding a post-hoc fit).
3. **Pin lift (Steps 3-3c):** lifting the SAME action to `Sigma` required
   Pin(m), not Spin(m), because `det(R01)=det(R12)=-1`. Three self-caught
   errors (t-leakage from a misconceived path-through-SU(3) strategy; the
   det=-1 discovery itself; a sign-convention error in `[spin_lift(L),v]`),
   all documented and fixed. Final construction verified by direct
   conjugation match on all 6 Clifford generators, both Weyl elements.
4. **Equivariance (Step 4):** `D_Sigma` fully equivariant (twisted adjoint).
   `psi_+` is NOT Weyl-fixed: `S.psi_+ = -i*psi_-` (both generators, same
   result). True equivariance statement: `S.M_+(v) = i*M_-(R.v)`, verified
   exactly on all 6 family directions, both generators.
5. **Self-caught forcing (this session, before dispatching the skeptic):**
   `Q_mu_plus = Q_mu_minus` identically as quadratic forms on the 6-dim
   family (verified symbolically). Combined with Step 4's equivariance and
   `S` unitary (verified), this FORCES `Q_mu(R.v)=Q_mu(v)` — meaning **G4,
   this round's own original "decisive test," is a necessary consequence of
   facts proved LATER in the same round**, not an independent finding.
6. **Novelty audit:** found direct hits. Steps 3-4's Pin-cover-of-Weyl-group
   construction (order-4 lifted generators) is Ciubotaru 2010 / Schur 1911 /
   Morris ~1980 classical representation theory. The `psi_+`/`psi_-` swap
   under a Pin lift of an orientation-reversing map is classical Atiyah-Singer
   -style Pin-cobordism index theory (Wang/Freed).
7. **Skeptic (FL Step 8a):** context-blind, no shell access in its own
   session (did everything by hand-algebra), independently re-derived the
   forcing chain, the Pin-lift sign conventions (confirmed standard
   Chevalley/Meinrenken twisted adjoint), and the null-model argument (a
   random 4-dim subspace of `R^6` is invariant under a given involution with
   probability 0 — G4 is genuinely non-generic, but still forced by items
   3-6). Verdict: **[CONFIRMED-REAL]** on every point, and suggested the
   round's own novelty verdict was if anything too conservative — proposed
   that `Q_mu_plus = Q_mu_minus` (the one fact left "open" in
   `novelty_check.md`) is itself likely forced by a charge-conjugation-type
   operator already implicit in the setup.
8. **Full closure (Step 5, this session, directly testing the skeptic's
   suggestion):** the chirality operator `omega = i^3*E_1...E_6` — **already
   in use since C156**, nothing new built — satisfies `omega.psi_+ = psi_-`
   EXACTLY (`c=1`), is unitary, and anticommutes with every `E_i` (hence with
   `D_Sigma(v)` for any `v`, same mechanism as C156's own chirality-oddness
   proof). This closes the chain completely: `Q_-(v) = ||omega D(v) psi_+||^2
   = ||D(v)psi_+||^2 = Q_+(v)` for every `v`, no new object required.

## Final state: nothing in this round is new

Per `audit-verification-gate.md`, the skeptic's `[CONFIRMED-REAL]` was treated
as `[HYPOTHESIS]` until independently tool-verified — done directly (Step 5),
not taken on the skeptic's word. Every link in the chain is now traced back to
objects that existed BEFORE C158 started (C156's chirality operator, C154/
C155's `psi_+`/`psi_-` as eigenvectors of `D(LC)`, C155's own `ker(M)`) plus
one classical 100+-year-old fact (Pin cover of the Weyl group) that this round
independently rediscovered. **C158 verified, in one worked example, that a
pile of already-known structure fits together exactly as general theory says
it must. It found nothing beyond that.**

## What survives as genuinely useful (not discoveries, but real assets)

1. A verified, general-purpose construction: given any `T`-equivariant family
   on a homogeneous space plus its Weyl group, build the genuine Pin lift and
   test equivariance — reusable machinery (`c158_general`-style), with the
   three sign/leakage pitfalls now named and fixed once.
2. Confirmation that this project's own `D_Sigma`, `psi_+`/`psi_-`,
   `omega` machinery (built piecemeal across C144-C157) is INTERNALLY FULLY
   CONSISTENT with 100-year-old classical representation theory — a strong
   correctness signal for the whole research line, even though it yields no
   new physics or mathematics on its own.
3. A clean worked pedagogical example of the "forced not discovered" pattern,
   now documented as occurring a fifth time (pearl_registry), including the
   sharpest version yet: forced WITHIN a single round's own two halves.

## What this does NOT establish

1. Not a discovery. Confirmed by the user's own five-gate mandate: novelty
   audit fails decisively, on top of the internal forcing.
2. Nothing about `N_gen=3`, `lambda` (still `FREE_COUPLING_PARAMETER`),
   triality, or any physical claim.
3. One homogeneous space (`SU(3)/T^2`), fixed conventions.
4. The skeptic's "documentation drift" note (`claim_step3_4.md` states
   `R=Refl.Rot`, code effectively uses `Rot.Refl`) is accurate but harmless
   here — reflection axis and rotation planes are disjoint for both `R01`
   and `R12`, so the two orders coincide. Left as a minor prose imprecision,
   not fixed, since fixing it would not change any number.

## Reproduce

```
python c158_step1_weyl_action.py             # G1(corrected)-G4
python c158_step2_isotypic_decomposition.py   # isotypic decomposition
python c158_step3c_pin_lift_final.py          # final correct Pin lift
python c158_step4_equivariance.py             # Q1-Q4, true equivariance
python c158_step5_full_closure.py             # full closure via omega
```
