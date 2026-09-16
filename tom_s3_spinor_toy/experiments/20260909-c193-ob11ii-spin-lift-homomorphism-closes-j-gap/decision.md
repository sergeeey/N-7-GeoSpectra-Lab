# C193 Decision — `spin_lift` is a genuine ANTI-homomorphism `so(6)→spin(6)` (verified, exact, 5+48+28 pairs). Narrows, does NOT close, OB11(ii)'s "J remains unchecked" prerequisite (C149) — corrected after skeptic review from an initial overclaim.

**Date:** 2026-09-09
**Verdict:** **PROMOTE (WEAKENED)** on the algebraic identity itself;
**NOT-CLOSED / NARROWED-ONLY** on the OB11(ii) prerequisite it was meant to
resolve. `16 of 16` checks pass (after two corrections made before this
verdict was finalized — see below).

All numbers trace to `c193_spin_lift_homomorphism.py`, `diag_scale.py`, and
`run_output.txt`.

---

## 0. Priority context (why this round, this session)

Priority survey (before computing anything, `claim.md` § Priority context):
`OB1` `PARKED` (exhausted, `C191`/`C192` today); `OB14` `BLOCKED-INTERNAL`
(reconfirmed 4 ways: `C142`, `C164`/`C165`, `C166`, `C175`); `OB13`'s
residual not concretely scoped; `OB4` has a screening gate, no live
proposal. `OB11(ii)` was the ONE open blocker with a concretely scoped,
unblocked next step, per `C149` (2026-09-04): "`J` remains unchecked... a
prerequisite" for resuming the planned transport test.

## 1. What was tested, and why not build `J` geometrically

Whether `round59_route_a_independent.py`'s `spin_lift` function is a genuine
Lie-algebra homomorphism `so(6)→spin(6)`. **Cheapest Differentiating Test
Protocol**: before paying the real cost of cross-referencing `G96`'s
octonion basis against round59's `NOMIZU`/`ADNU` convention to build `J`
explicitly (real risk of a new convention bug), check whether the answer is
already decided by `spin_lift`'s own general algebraic structure.

## 2. What was found (two corrections made in-round, before this verdict)

**Correction 1 (self-caught, before skeptic):** the pre-registered identity
(coefficient `+1`) failed on every generic pair and `34/48` `NOMIZU`/`ADNU`
pairs. Diagnosed (`diag_scale.py`): the entrywise ratio was exactly `−1`,
sympy-exact — same shape as this session's own `C192` (`comm(L1,L2)=−2·L3`
in the pygae/clifford round earlier today). The by-hand derivation of
WHY it should be exactly `−1` did not actually reproduce that constant
(predicted an additional `1/2` on top of a sign the derivation didn't
settle either) — flagged as genuinely unresolved, not papered over.

**Correction 2 (skeptic pass, Step 8a, context-blind — read only `claim.md`
+ script + `diag_scale.py` + `run_output.txt`, no reasoning chain):**
**verdict WEAKENED**, 5 concerns, all accepted (full text: `claim.md`
§ Correction 2). Summary:

| # | Concern | Severity | Response |
|---|---|---|---|
| 1 | `J`-corollary is a pure existence statement — no `spin_lift(J)` matrix ever produced, nothing enters the actual transport-test code | **HIGH** | **Accepted, title/verdict corrected.** No longer reported as "closing" anything. |
| 2 | `spin_lift` is an ANTI-homomorphism, not "a homomorphism up to sign" — materially different, `RHO` carries FLIPPED `su(3)` structure constants | **HIGH** | **Accepted, verified concretely** (`Q4b`, added same round): `28/28` non-degenerate `ADNU`-generator pairs confirm the flip exactly. Flagged as a downstream-audit item, not silently absorbed. |
| 3 | The `−1` vs. `+1/2` scale discrepancy is itself a red flag — nobody currently derives `spin_lift`'s exact normalization from first principles | **HIGH** | **Accepted, left explicitly UNRESOLVED** — not needed for this round's own corollary (any constant times zero is zero), but flagged before further reuse. |
| 4 | `SU(3)`-stabilizes-`J` is coordinate-free; doesn't identify `J` in round59's OWN basis, nor its sign (`J` vs `−J`) | **MEDIUM** | **Accepted.** `claim.md` corollary reworded to "there exists a `J`-in-this-basis," not "`J` is verified." |
| 5 | `Q4`'s sign match is NOT independent of `Q2`'s `−1` — same underlying convention, not two confirmations | **MEDIUM** | **Accepted.** `Q4`'s check label corrected in the script. |

**New check added in response (`Q4b`):** confirms concretely (not left
abstract) that `RHO=spin_lift(ADNU)` satisfies the FLIPPED `su(3)`
structure constants — `28/28` non-degenerate pairs, with the `3/28`
apparent "also-matches-standard" cases verified to be exactly the
degenerate `[ADNU[a],ADNU[b]]=0` pairs (both predictions trivially agree at
zero there — checked directly, not assumed, so this isn't miscounted as a
real conflict).

## 3. Verdict, precisely

**The algebraic identity itself: PROMOTE.** `[spin_lift(X,E),
spin_lift(Y,E)] = −spin_lift([X,Y]_so6, E)` holds exactly for 5 generic
random pairs, 48 `NOMIZU`/`ADNU` pairs, and 28 `ADNU`-generator pairs — a
real, previously-untested, non-trivial fact about `spin_lift` as coded in
round59's unusual `Λ•L'` (abstract exterior algebra) presentation of `Σ`,
used throughout `C139`/`C141`/`C142`/`C146`/`C149`/`C162`/`C164`/`C165`.

**OB11(ii)'s "`J` remains unchecked" prerequisite: NARROWED, NOT CLOSED.**
Corrected framing, per skeptic Concerns 1 and 4: this round shows that
*if* an explicit `J`-in-round59's-basis is ever constructed, its
`su(3)`-equivariance on `Σ` would be automatic (given the standard,
coordinate-free fact that `SU(3)` stabilizes `J`) — it does **not**
construct that `J`, does **not** produce `spin_lift(J)` as a usable
operator, and does **not** advance OB11(ii)'s actual planned transport
step (transporting `D`, `J`, `γ`, `B-L` through `U`) in any way that
enters real code. The honest characterization: this round reduces one
unknown (does `J`'s equivariance need checking at all, once built?) to a
known-in-principle fact, while leaving the actually-expensive step
(constructing `J` explicitly from `G96`'s octonion data, cross-referenced
against round59's basis) completely untouched.

## 4. Kill Analysis

**What this round establishes:** `spin_lift`'s anti-homomorphism property
(real, general, reusable — flagged for downstream audit, see § 5).
**What this round does NOT establish:** OB11(ii)'s closure of any kind;
an explicit `J`; that `spin_lift(J)` (once `J` exists) is actually the
operator the planned transport test needs (as opposed to some other
natural lift).
**Revival condition:** not applicable — this is a PROMOTE (on the
algebraic fact) with an explicitly narrowed, not rejected, application.

## 5. Consequence for OPEN_BLOCKERS.md / OB11 tracking, and a flagged audit item

To be added (append-only) to `OPEN_BLOCKERS.md` OB11(ii): `J`'s
equivariance is now known to be automatic ONCE `J` is constructed
explicitly in round59's basis — construction itself remains the
open, expensive step. Separately: **`spin_lift`'s anti-homomorphism
property (not the standard homomorphism it might be assumed to be) is
flagged as a downstream-audit item** for any future round that reuses
`RHO`/`spin_lift` output under an assumption of standard `su(3)`
structure constants (e.g. Casimir-sign, weight-label, or orientation
arguments) — none of `C139`/`C141`/`C142`/`C146`/`C149`/`C162`/`C164`/
`C165` appear to have depended on the SIGN of the structure constants
specifically (their own load-bearing facts are Casimir eigenvalues,
which are quadratic and sign-insensitive, or direct equivariance
`[O,ρ(a)]=0` checks, also sign-insensitive) — but this has not been
individually re-audited round-by-round here, and is named as a
pearl-registry-worthy open item, not silently assumed safe.

## 5.5 Floor–Ceiling (Step 4a)

Discrete metric (does the identity hold exactly, for how many independent
pair-classes: yes/no per class), not continuous. **Floor = 0**: the
identity failing on generic random pairs (it did, at the pre-registered
`+1` coefficient — a real floor-level failure, not assumed) would mean
`spin_lift` carries no clean bracket-preserving structure at all, making
any downstream reuse (including `C146`'s equivariance argument for `D_Σ`)
suspect. **Ceiling = 3**: the identity holding on all three independent
test classes — generic random pairs (`Q2`, structure-agnostic), the
geometrically-meaningful `NOMIZU`/`ADNU` pairs (`Q3`), and the `ADNU`-only
generator pairs that determine `RHO`'s own `su(3)` structure constants
(`Q4b`). **Observed = 3** (all three classes pass, at the corrected `−1`
coefficient) — lands exactly on the ceiling for the ALGEBRAIC identity.
**Separately, and NOT covered by this same interval:** the OB11(ii)
prerequisite has its OWN, much lower, ceiling — this round's own § 3
verdict is explicit that reaching that ceiling (an actual usable
`spin_lift(J)` operator) was never attempted, so no floor/ceiling claim is
made about the prerequisite itself, only about the algebraic fact that
narrows it.

## 6. What this does NOT establish

See `claim.md` § What this round does NOT establish + § Correction 2
(post-skeptic) for the full list.

## 7. Reproduction

```
cd experiments/20260909-c193-ob11ii-spin-lift-homomorphism-closes-j-gap
python c193_spin_lift_homomorphism.py
python diag_scale.py   # the scale-diagnosis probe that found the -1
```

`16/16`. `ruff check` and `ruff format`: clean.
