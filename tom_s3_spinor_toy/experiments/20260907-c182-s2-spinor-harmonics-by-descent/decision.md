# C182 — Decision

**Date:** 2026-09-07
**Verdict:** `DESCENT-CONFIRMED`, but **with the evidential structure
substantially corrected after a context-blind skeptic pass** (§6). The
numbers were right; the round's account of *why they counted as evidence*
was not, and two checks had to be replaced or downgraded.

---

## 0. Summary

The last outstanding half of Tom Lawrence's §3.3 request — harmonics of
`S²` forming a basis for a **two-component spinor** — obtained by the
route C179 recommended: **descent from `S³`**, not an independent attack
on `S²`.

`S² = S³/U(1)` (Hopf). Decomposing the `S³` harmonic spaces `H_k` by the
`U(1) ⊂ SU(2)_R` weight splits `L²(S³)` by **spin weight**: weight `0` is
ordinary functions on `S²`, weight `±½` is the two-component spinor.

| `k` | `dim H_k` | weight ladder (weight, multiplicity) |
|---|---|---|
| 0 | 1 | `(0, 1)` |
| 1 | 4 | `(−½, 2)`, `(+½, 2)` |
| 2 | 9 | `(−1, 3)`, `(0, 3)`, `(+1, 3)` |
| 3 | 16 | `(−3/2, 4)`, `(−½, 4)`, `(+½, 4)`, `(+3/2, 4)` |
| 4 | 25 | `(−2, 5)` … `(+2, 5)` |
| 5 | 36 | `(−5/2, 6)` … `(+5/2, 6)` |

Exactly `k+1` weights, spaced by 1, symmetric about 0, each of
multiplicity `k+1`.

**Sector dimensions:** weight `0` (even `k`) gives 1, 3, 5 = `2l+1`, the
scalar spherical-harmonic count. Weight `±½` (odd `k` only) gives 2, 4, 6
= `2(l+1)`, the standard `S²` Dirac multiplicity. Both chiralities.

**So Tom's `S²` request is answerable — just not the way he framed it,**
and it comes *after* `S³`, not before.

---

## 1. What the skeptic corrected: these are NOT two independent checks

The round originally billed the scalar column as "the positive control,
and the stronger of the two checks." **That is false, and the skeptic was
right to call it.**

- `ladder_ok` — checked *first*, and gating everything else — already
  asserts that **every** weight sector has multiplicity `k+1`.
- For `k` even, `l = k/2`, so `2l+1 = k+1`.
- For `k` odd, `l = (k−1)/2`, so `2(l+1) = k+1`.

Both "targets" are **the same number, `k+1`**, and both follow from the
ladder rather than testing anything beyond it. Consequence: the
pre-registered verdict branch `SCALAR-OK-SPINOR-FAILS` was **structurally
unreachable** — the code could never return it. A verdict branch that
cannot fire is the same defect this project catalogued as
"a test that cannot fail is not a test" (C172, and again in C178/C181).

The verdict logic has been rewritten to say this out loud, and
`results_c182.json` now carries the field
`scalar_and_spinor_targets_are_the_same_number_k_plus_1: true` rather than
presenting two green ticks as independent corroboration.

**What survives:** the ladder itself is a real, falsifiable structural
fact (see §2), and the numbers displayed are correct. What does not
survive is the claim that they were confirmed twice.

---

## 2. The normalisation IS genuinely pinned (this attack did not land)

The weight conversion uses `−(i/2)·X₃^R`. The factor `½` is not fitted:
C180 independently verifies `[X_a, X_b] = −2ε_abc X_c`, and requiring the
standard `so(3)` relations then forces `J_a = −(i/2)X_a` uniquely. The
ladder check is genuinely discriminating here — with `−i·X₃^R` (no half)
the ladder step would be 2, not 1, and `ladder_ok` would fail.

---

## 3. The no-go check was a tautology — replaced with a real one

The first version tested, for each weight `w`,
`|w| ≈ 0.5 AND |w| < 1e-9` — a logically impossible conjunction, so its
offender list was empty **for any input whatsoever**. It could not fail.
The decision.md text calling it "checked, not assumed" was wrong.

**Replaced** by `fibre_invariance_check()`, which tests the group action
instead of the weight labels. The `U(1)` fibre acts by
`U(θ) = exp(θ·X₃^R)`. A weight-0 vector must be fixed for *every* `θ`
(that is what "descends to a function on `S²`" means); a weight-`½` vector
must not be, and must pick up exactly `−1` at the half-turn `θ = π`.

| sector | drift under generic rotation | phase after half-turn | expected | result |
|---|---|---|---|---|
| `k=2`, weight `0` | `1.2e-15` | `+1` | invariant, `+1` | ✓ |
| `k=3`, weight `½` | `0.686` | **`−1`** | moves, `−1` | ✓ |

Both halves can genuinely fail; neither did. **That `−1` is the actual
content** — a spin-weight-`½` object reverses sign on a half-turn around
the Hopf fibre, which is precisely why it is a section and not a function.
C179's no-go and C182's construction are the same fact from two sides,
and now that is demonstrated rather than asserted.

---

## 4. Kill Analysis

**What this establishes:** the `S²` half of the request is delivered at
the level of harmonic *spaces*, their multiplicities, and — after the
correction — a genuine demonstration that the weight-`±½` sectors do not
descend to functions.

**What this does NOT establish:**
1. **The `S²` Dirac eigenvalues `±(l+1)` are NOT derived.** Only
   multiplicities. The `S²` Dirac operator was not built. Dimension
   agreement is consistent with these being the Dirac eigenspaces but does
   not prove it — flagged by the skeptic and repeated here.
2. Explicit closed-form `_{±½}Y_{jm}` expressions were not written out.
3. Nothing about `S⁶`, `N_gen=3`, or any open blocker.

**Relaxation Map:** build the `S²` Dirac operator on the weight-`±½`
sections and check its eigenvalues are `±(l+1)` — which would close the
`S²` side the way C180's connection-constant check closed the `S³` side.

---

## 5. Floor–Ceiling (revised down after §1)

Summary line: floor = 0, observed = 2, ceiling = 2, efficiency = 1.000.

The original version claimed "6 matching levels". That over-counted:
the six sector dimensions are not six independent facts (§1). The honest
discriminating quantity is the number of **genuinely independent** checks
that pass:

- **floor = 0.** With the mechanism removed — a misidentified `U(1)`
  generator, or the tautological no-go check the first version shipped —
  **0** independent checks would carry information (the tautology passes
  regardless of input, which is exactly a floor-level result).
- **observed = 2:** (i) the weight ladder, `k+1` values at unit spacing
  (falsifiable — a wrong normalisation gives spacing 2); (ii) the fibre
  invariance check, weight-0 fixed / weight-`½` picking up `−1`
  (falsifiable in both directions).
- **ceiling = 2** — the number of independent checks this round's design
  contains. Interval 0 to 2, non-degenerate.
- **efficiency = 1.000**, exact algebraic agreement.

---

## 6. Independent skeptic pass (Step 8a) — RUN, verdict `WEAKENED`, both findings accepted

Context-blind (claim.md + script + results; both `decision.md` files
withheld). No Bash available to it; it hand-derived and read the code
line by line, and said so.

| Attack | Outcome | Response |
|---|---|---|
| Is the weight normalisation fitted? | **Did not break.** Independently solved the constraint and confirmed `−i/2` is forced, and that the ladder-step check really would catch a wrong factor. | No change (§2). |
| **Are the scalar control and the spinor deliverable the same fact?** | **BROKE IT.** Both targets are identically `k+1`; `ladder_ok` already implies them; the `SCALAR-OK-SPINOR-FAILS` branch is unreachable. | **Accepted in full.** Verdict logic rewritten, docstring corrected, §1 added, Floor–Ceiling revised from 6 to 2 (§5). |
| Are the numbers right? | **Did not break** — reproduced the whole ladder by hand from Peter–Weyl for `k=0..3`. | No change. |
| **The no-go check** | **BROKE IT.** Logically impossible condition; empty by construction; "checked, not assumed" was false. | **Accepted in full.** Replaced with `fibre_invariance_check()` (§3), which passes and can genuinely fail. |
| Scope honesty | **Did not break** — limits stated repeatedly — but noted the round did not realise its own "stronger check" carried no extra information. | Now stated explicitly (§1). |

**Net:** the construction and every number in it stand; the round's
*self-assessment* did not, and has been corrected in three places
(verdict logic, the replaced check, the Floor–Ceiling count). This is the
second round in this sequence where the substantive error was in a check
rather than in a computation (C181 §3 was the first).

---

## 7. Status

`experiments/20260907-c182-s2-spinor-harmonics-by-descent/` — DONE,
INCLUDING independent skeptic pass, whose two findings were both accepted
and fixed rather than argued down. The `S²` half of Tom's §3.3 request is
answered at the level of spaces, multiplicities and fibre behaviour; the
`S²` Dirac operator itself remains unbuilt (§4). **Downstream fix
required:** `DRAFT_REPLY_TO_TOM_2026-09-07.md` describes the scalar column
as "the control", which §1 shows is misleading — that wording must be
corrected before the draft is sent. Registry not yet updated for this
round. No git operations run.
