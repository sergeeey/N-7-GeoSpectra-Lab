---
experiment_id: 20260708-dolan-casimir-g2su3
round: 27
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C2_confirmed_C3-C4_corrected_post_skeptic
parent: round26 (Jac_h/Jac_m derived, M_p-vs-Zp correction found and bug-fixed)
---

# claim.md — Round 27: Dslash_mat = -H/2 exactly (a cleaner, cross-
confirmed route to Round 26's correction, found while attempting a
"first principles" derivation of its coefficients)

## Background

User asked to derive Round 26's `H - (1/2)Id - (7/4)Casimir_su3`
correction (the exact gap between this project's own Levi-Civita `M_p`
and Agricola's canonical `Z_p`) from first principles, rather than
leaving it as a verified-but-unexplained numeric fact (both skeptics'
standing kill condition on Round 26). While investigating this, found
that `Dslash_mat` (`:= sum_p e_p·M_p`, this project's own S⁶-intrinsic
twisted Dirac operator, the central object of Rounds 14-26) equals
`-H/2` EXACTLY as an operator — not merely `Dslash_mat² ∝ H²` (already
implicit in prior rounds), but `Dslash_mat` ITSELF.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — algebraic identity between two independently-
constructed matrices, tested directly. NOT empirical, NOT causal.

## Why this is NOT just Round 26 restated (REVISED post-skeptic — see
"Skeptic Verdict" below; the original "independent sources" framing was
wrong and is retracted)

`g2su3_explicit_clifford.py`'s own docstring documents that `nabla_g`
(`M_p`) is calibrated against the Killing spinor equation on the nearly-
Kähler S⁶=G₂/SU(3) from Agricola-Hofmann-Lawn 2023: `ψ_± = 1 ± y₁y₂y₃`
are Killing spinors with `∇^g_X ψ_± = ±(1/(2√3)) X·ψ_±`. **However**,
`H` (via the T-table, via `lambda_half`) uses the SAME `LEVI_CIVITA_
NOMIZU` data `nabla_g`/`M_p` uses — they are NOT independently anchored;
both trace to one source (AHL2023 page 42). Finding `Dslash_mat=-H/2`
exactly is therefore a **verified numerical realization** of what
Agricola 2002 eq. 5 (at t=1/2) predicts given this shared data — a
genuine, clean, previously-unknown matrix identity — but NOT a "cross-
confirmation between independent sources" as originally claimed.

## Falsifiable Claims

**C1 (the headline finding):** `Dslash_mat == -H/2` exactly, computed by
direct matrix composition on both sides (`Dslash_mat := Σ_p E_p·M_p`,
`H` via `build_H_matrix` from the T-table) — no subtraction from any
other identity anywhere in this construction.

RESULT: `[VERIFIED-tool]` — confirmed exactly (sympy exact equality,
asserted in-script).

**C2 (trivial consequence, re-verified independently as a sanity gate):**
`Dslash_mat² == H²/4` exactly.

RESULT: `[VERIFIED-tool]` — confirmed exactly, re-derived via direct
matrix squaring on both sides (not assumed from C1 alone).

**C3 (REVISED post-skeptic — downgraded from "independent cross-check"
to "consistency rewrite"):** re-deriving `Ω_g` via `H²/4 + H -
degree4_term - scalar_term·Id` (built entirely from `H`, `C~h`, and
Round 26's `Jac_h`/`Jac_m`-derived pieces) reproduces Round 26's original
`H - (1/2)Id - (7/4)Casimir_su3` correction exactly.

RESULT: `[VERIFIED-tool]` — confirmed exactly, but this is a
**consistency rewrite under C1/C2, NOT an independent cross-check**: per
skeptic review, since `Dslash² = H²/4` follows identically from C1, this
route is algebraically Round 26's own route with `Dslash²` substituted
by `H²/4` — the same derivation, not a second independent one. It
confirms no arithmetic slip was introduced, nothing more.

**C4 (CORRECTED post-skeptic — the original sign-convention argument was
wrong):** combining C1 with Agricola's own `D^t = D^0 + t·H_Agricola`
(eq. 5, page 8), and the CORRECT sign convention `H_ours = H_Agricola`
(no flip — re-verified via `torsion_T`'s own docstring, which matches
Agricola's eq. 1 convention directly; the original claim `H_ours =
-H_Agricola` did not algebraically follow from the stated premises and
is retracted), gives `D^0 = -H_ours` (NOT zero), IF `Dslash_mat` is
identified with Agricola's `D^{1/2}`.

RESULT: `[VERIFIED-tool]` for the CORRECTED arithmetic (`D^0 = -H_ours`,
re-derived and asserted in-script) — still explicitly NOT an independent
geometric derivation of WHY `D^0` takes this value. No separate
construction of `D^0` exists in this codebase to check against; this
remains a logical consequence, not a first-principles explanation.

## Kill Conditions

- C1 killed if: skeptic finds the `-H/2` match is coincidental for the
  SPECIFIC basis/index chosen (e.g. only holds up to some hidden
  normalization ambiguity) — skeptic should independently re-verify by
  computing `Dslash_mat` and `H` via completely independent re-reads of
  `build_Mp`/`build_H_matrix`, not trusting the claim doc's framing.
- C1/C2 killed if: skeptic finds `Es[p]` or `Ms[p]` in THIS script's
  local rebuild differ from Round 24-26's own established versions
  (e.g. an import or index-order slip) — compare against
  `g2su3_Sminus_weitzenbock.py`'s own `Dslash_mat` construction line by
  line.
- C3 killed if: skeptic finds the two "independent" routes are not
  actually independent (e.g. `degree4_term`/`Ch_tilde` secretly already
  encode `Mp`-derived information via a shared import) — verify
  `g2su3_round26_jach_derivation.py`'s `jac_h`/`jac_m`/`build_quartic_
  matrix` genuinely take no `Mp`-derived input (they should only need
  `curv_h` and the T-table).
- C4's "D^0=-H_ours" framing killed (downgraded) if: skeptic finds the
  identification "Dslash_mat = Agricola's D^{1/2}" is itself unjustified
  (e.g. finds a normalization mismatch between this project's Clifford-
  algebra convention `Zi·Zj+Zj·Zi=-δij` — page 7 of the source PDF — and
  what THIS project's `e_action` actually implements) — if so, C1-C3's
  ARITHMETIC still stands (they don't depend on the D^{1/2} identification
  at all), but C4's "D^0=-H_ours" interpretation should be marked
  unsupported. (Already once corrected — see Skeptic Verdict — the sign
  of this specific value is exactly the kind of thing a second
  independent check should re-verify, not just trust this round's fix.)

## What this does NOT mean

- Does NOT supply an independent GEOMETRIC reason for why `D^0=-H_ours`
  — this is the genuinely still-open part of "first principles,"
  explicitly not resolved here. A full answer would likely require
  directly constructing Agricola's canonical (t=0) connection
  independently and checking its own twisted Dirac operator against this
  value — not attempted this round.
- Does NOT change any previously-established spectrum, index, or
  eigenvalue result from Rounds 4-26 — `Dslash_mat=-H/2` is a REFRAMING
  of an already-existing, unchanged object, not a new computation that
  alters it.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension.
- Does NOT establish which of `M_p`/`Z_p` is the object the preprint's
  own L4A norm-bound convention intends — same standing question as
  Round 26, unresolved.
- Does NOT claim `M_p` and `H` are independently anchored — retracted,
  see Skeptic Verdict below.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics, one without code-execution access — still caught a real error
from algebra/code inspection alone)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both) | `Dslash_mat=-H/2` matrix identity stands, unaffected by the framing/sign issues below |
| C2 | CONFIRMED-REAL (both) | trivial consequence of C1, independently re-verified |
| C3 | WEAKENED (both) → downgraded, rewritten above | "two independent routes" was tautological given C1+C2; fixed |
| C4 | WEAKENED (both) → **real error found and fixed** | sign-convention chain `H_ours=-H_Agricola` did not algebraically follow; corrected to `H_ours=H_Agricola`, giving `D^0=-H_ours` (not zero) |

**Additional correction** (both skeptics, independently): the module's
own "genuine cross-confirmation between two independent sources"
framing overstated independence — `M_p` and `H` share the same
`LEVI_CIVITA_NOMIZU` data source. Retracted throughout, see above.

**How the C4 error was found and fixed:** one skeptic, working from code
inspection alone (no execution access), noticed that matching "cubic
term = `-H_ours`" against Agricola's own "cubic term = `-H_Agricola`"
algebraically gives `H_ours=H_Agricola` directly, not the negated
relation the docstring asserted. Independently re-verified by reading
`torsion_T`'s own docstring (`g2su3_H_element.py`): its formula matches
Agricola's eq. 1 convention with no sign flip, confirming the skeptic's
correction. Re-derived `D^0` with the fixed sign: `D^0 = -H_ours`,
re-verified exactly in-script. This is a cleaner result than the
original (wrong) claim — both `D^0` and `D^{1/2}` are proportional to
the same `H`, with coefficients `-1` and `-1/2` respectively.
