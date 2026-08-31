# C119 claim -- is the Bismut-Ricci-flat condition even applicable to
the frozen `S³×S⁶` background? (PARENT_ACTION_GATE field F1 only)

## Question type (EstimandOps L0)

**Descriptive.** Direct check of whether a specific, already-published
geometric identity (`Rc(g) = ¼H_g²`, plus the `dH=0` / `δH=0`
hypotheses that come with it) holds for a specific, already-frozen
background (`S³×S⁶` with this project's own frozen torsion data). No
causal claim, no predictive claim, no new physics claim. The estimand
is a yes/no on an identity, evaluated pointwise on a fixed manifold.

## Background

A read-only literature round (not yet in this project's own registry --
treated here as an unverified lead, per Gate 1/Gate 2 discipline, and
re-verified below rather than inherited) surfaced a candidate mechanism
for OB1's `t`-selection problem (`OPEN_BLOCKERS.md` OB1; PARKED, reopen
condition 1/2 = "a concrete candidate action / a directly relevant
parent mechanism is published somewhere new"):

> **Bismut-Ricci-flat generalized metric.** A pair `(g,H)`, `g` a
> Riemannian metric and `H` a **closed** 3-form, is a fixed point of
> the generalized Ricci flow iff `H` is `g`-harmonic and
> `Rc(g) = ¼ H_g²`.

Applied to the `S³` factor ALONE with this project's own Cartan-Schouten
torsion, the condition reportedly gives `t ∈ {0,1}` -- exactly the two
values OB1 needs, and exactly the two flat points of `∇^t`.

**The gap this round tests.** The project's frozen background is NOT
`S³` in isolation. It is the FULL PRODUCT `S³×S⁶`
(`RESEARCH_STATUS_REPORT.md`'s own 2026-07-17 correction: 3+6=9
internal, +4 spacetime = 13 total), with a nearly-Kähler /
G₂-structure on the `S⁶` factor carrying its own characteristic
torsion -- the same `S⁶` data the `N_gen=3` index-theory chain
(G73/G74A/G74B) is built on. A condition that holds on one factor of a
product says nothing about the product until the product is checked.
**This round checks the product.** Nothing more.

This maps to exactly one field of `PARENT_ACTION_GATE.md`:

| Field | This round |
|---|---|
| **F1 — Background** | **THE ONLY FIELD TESTED.** Is the candidate mechanism's own geometric hypothesis satisfiable on the frozen `S³×S⁶` at all? |
| F2 — Twist | not addressed |
| F3 — Torsion family | cited (round113), not re-derived |
| F4 — t-selection mechanism | NOT assessed this round. A mechanism whose hypothesis fails on the frozen background never reaches F4. |
| F5 — Fermionic Dirac operator | not addressed |
| F6 — Background equations | not addressed (this is the gate field the candidate would eventually have to fill; out of scope here) |
| F7 — Stability | not addressed |

## The four sub-questions, pre-registered

**Q1 — is the nearly-Kähler `S⁶` characteristic torsion `T_{S⁶}` a
CLOSED 3-form (`dT_{S⁶}=0`)?**

**Q2 — does `Rc(g_{S⁶}) = ¼ (T_{S⁶})²` hold for the frozen `S⁶`?**
i.e. is `S⁶` itself already Bismut-Ricci-flat with its own
characteristic torsion?

**Q3 — for the product `S³×S⁶` with product metric and
`H_tot = H_{S³} + H_{S⁶}` (both pulled back), does
`Rc(g_{S³×S⁶}) = ¼ H_tot²` hold?** Sub-question, to be verified
EXPLICITLY and not assumed: does `H_tot²` have zero cross-block terms?

**Q4 — Bianchi / harmonicity.** Is `H_tot` closed and co-closed on the
product, as the Bismut-Ricci-flat hypothesis requires?

## Falsifiable claim and pre-registered PASS/FAIL

The condition is checked in an orthonormal frame, using the
dimensionless, normalization-independent ratio

```
rho := Rc_{aa} / (¼ (H²)_{aa})        (both proportional to δ here)
```

`rho = 1` ⟺ the condition holds on that factor. `rho` is invariant
under rescaling the factor's radius (both numerator and denominator
scale as `1/radius²`), so a PASS/FAIL verdict on `rho` cannot be
rescued or destroyed by a radius choice -- pre-registered here so that
"but maybe another radius works" cannot be raised after the fact.

| Outcome | Verdict for F1 |
|---|---|
| `rho_{S³}=1` at some `t` AND `rho_{S⁶}=1` AND `dH_tot=0` AND `δH_tot=0` AND cross-terms vanish | **PASS** -- the mechanism is geometrically applicable to the frozen background; F4 assessment becomes worth doing |
| `rho_{S³}=1` at some `t` but `rho_{S⁶}≠1`, or `dH_tot≠0` | **FAIL** -- the mechanism's own hypothesis is violated by the frozen background; it cannot be invoked as a `t`-selector for THIS project without first changing the background (which would then have to be re-checked against `N_gen=3`'s S⁶ chain) |
| conditions hold only for a `S⁶` torsion that is NOT the frozen characteristic one | **PARTIAL** -- record exactly what the required replacement is, and flag it as a background modification, not a selection principle |

**Kill criterion (pre-registered).** If `rho_{S⁶} ≠ 1` for the frozen
nearly-Kähler characteristic torsion at ANY radius, OR if
`dT_{S⁶} ≠ 0`, then the Bismut-Ricci-flat condition is **NOT**
applicable to the frozen `S³×S⁶` background, and the `S³`-only root
`t ∈ {0,1}` does NOT transfer to the product. This kills the candidate
at F1, before F4 is ever reached. Per Gate 1's non-transfer rule: a
verdict established for `S³` does not transfer to `S³×S⁶` because they
share a factor.

**Second, independent kill criterion.** Even if Q1-Q4 all passed, the
`S³`-only content must be checked for novelty against this project's
own record: if `Rc(g_{S³}) = ¼H_{S³}²` is algebraically equivalent to
something round111/round99 already established, the mechanism is an
**equivalent restatement**, not new information -- exactly the verdict
round116's "spectral flow" attempt received (`OPEN_BLOCKERS.md` OB1).
Pre-registered here so that a PASS on Q1-Q4 could not be reported as
"new mechanism found" without this check also being run.

## Mandatory sanity re-derivation (not inherited)

The claim that `Rc(g_{S³}) - ¼H_{S³}²` reproduces round111's own
already-certified `Ric^t = 8t(1-t)·δ` is **re-derived here from
scratch**, not taken from the read-only report. If it does not
reproduce round111 exactly, the whole `S³` half of this round is a
substrate failure and is recorded as such (`BLOCKED-INFRASTRUCTURE`),
never as evidence about the claim.

## Provenance disclosure -- what was already in hand when this file was
written (Gate 2 / EstimandOps anti-pattern "estimand defined after data
access")

Written before the computation script existed, but NOT before all
inputs. Stated explicitly rather than implied:

**Already in hand at pre-registration time:**
1. The three generalized-Ricci-flow arXiv papers were verified to exist
   and the Bismut-Ricci-flat definition was read verbatim from two
   abstracts (`2301.02335`, `2401.03332`) -- so the definition being
   tested is `[VERIFIED-tool]`, not recalled.
2. `Σ_{ijk} T(i,j,k)² = 8` for the project's own `S⁶` torsion table
   (one scratch run of `g2su3_H_element.build_T_table`).
3. The project's own `Ric(e_p,e_p)=5/3`, `Scal=10` for the same `S⁶`
   normalization (`experiments/20260708-dolan-casimir-g2su3/decision.md`
   lines ~1926-1929, "triple-verified in Round 16").
4. One web-search-sourced literature identity for nearly-Kähler
   6-manifolds, `‖T‖² = (2/15)·Scal^g`, NOT yet checked against (2)+(3).

**Consequence, stated honestly:** items (2)+(3) make Q2's answer
*predictable* at pre-registration time. This round is therefore best
described as a **pre-registered confirmation with an independent
cross-check**, not a blind test, for Q2. Q1 (`dT`), Q3 (cross-terms),
and Q4 are genuinely un-computed at write time.

**NOT in hand at pre-registration time:** `(T²)_{ab}` as a matrix (only
its trace); `dT_{S⁶}`; the product cross-block terms; whether the
project's `S⁶` torsion is literally the standard SU(3)-structure
`ψ⁻`; whether the `S³` root reproduces round111.

## Explicit scope boundary (repeated verbatim in `decision.md`)

1. This round tests **ONLY** whether the Bismut-Ricci-flat condition is
   geometrically applicable to the frozen `S³×S⁶` background -- gate
   field **F1** in `PARENT_ACTION_GATE.md`. It does not assess F2,
   F4-F7.
2. It does **NOT** re-derive round111's `S³`-only result
   (`Ric^t = 8t(1-t)δ`, `Scal(t)=24t(1-t)`) as a new finding -- that is
   **cited** (`experiments/20260717-round111-codex-item6-scalar-
   curvature-action/decision.md`) and used only as a cross-check target.
3. It does **NOT** change `N_gen=3`'s CONDITIONAL status, whatever the
   outcome. This is a `t`-selection candidate test, not the `S⁶` index
   computation. `lambda=FREE_COUPLING_PARAMETER` and
   `safe_for_runtime=False` are likewise untouched.
4. It does **NOT** by itself move OB1 out of `PARKED`. Per OB1's own
   reopen condition 4, a candidate must pass the whole
   `PARENT_ACTION_GATE` checklist; a single field's verdict is not a
   gate decision. Any status change requires a separate, explicit gate
   decision once the other `PARENT_ACTION_GATE` fields are assessed.
5. It does **NOT** solicit Tom Lawrence's Part 5.
6. It does **NOT** edit `CLAIM_LEDGER.yaml`, `OPEN_BLOCKERS.md`,
   `ALIVE_BRANCHES.md`, `pearl_registry/INDEX.md`, or any registry.

## What this round can NOT show, whatever the numbers say

- A FAIL does **not** show that no parent action exists for OB1, nor
  that generalized Ricci flow is irrelevant to this project in general
  -- only that THIS specific condition is not satisfied by THIS frozen
  background.
- A FAIL does **not** falsify the `S³`-only computation; the `S³` root
  `t∈{0,1}` may be perfectly correct and simply fail to transfer.
- A PASS would **not** by itself be a `t`-selection mechanism: it would
  only show the hypothesis is satisfiable, leaving F4 (why nature picks
  this condition) and F6 (the actual action) entirely open.
- Nothing here bears on the `S⁶` twisted-Dirac index chain
  (G73/G74A/G74B), which uses the same `S⁶` torsion data but asks a
  completely different question of it.

## Verification plan

- One script, `c119_bismut_ricci_flat_product_check.py`, sympy/exact
  arithmetic only (no floating point in any verdict-bearing quantity).
- `S⁶` torsion imported from the project's OWN certified
  `g2su3_H_element.build_T_table()` -- not re-typed, not re-derived
  from a textbook, so the object tested is provably the frozen one
  (Gate 1: artifact identity).
- `S³` side re-derived from scratch and cross-checked against
  round111's `Ric^t=8t(1-t)δ`.
- `dT_{S⁶}` computed **two independent ways** (Chevalley-Eilenberg
  differential for invariant forms on a reductive homogeneous space,
  using the project's own structure constants; and the algebraic
  `2σ_T` identity for parallel torsion), matching round111's own
  "two independent routes must agree" discipline. If the two routes
  disagree, the `dT` result is `BLOCKED-INFRASTRUCTURE`, not a finding.
- Product cross-terms computed by explicit 9-dimensional index sums,
  not by an assumed block-diagonality argument.
- Every literature fact carries an arXiv ID verified with a tool this
  round; no fact enters from model memory.
- Results written to `results_c119.json`.
- `ruff check` clean.
- FL Step 8a skeptic pass on the result (separate step, after this
  round returns) -- this round does NOT self-certify.
