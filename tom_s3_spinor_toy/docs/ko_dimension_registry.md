# KO-dimension registry

**Status:** canonical. Opened 2026-08-10 by C36's fallout.

**Why this file exists.** `J_F² = −1` propagated through 11 documents including
the manuscript because it sat next to the phrase *"KO-dim 6 relations verified"*
— and that phrase conflated two different things:

```
the three SIGNS          <- computed here, in this repo, from J_F itself
the KO-dimension NUMBER  <- inherited from CCM, never derived here
```

Once the sign was corrected, the second half had no independent support left to
lean on. This registry keeps the two levels apart permanently: a sign tuple is
recorded when it is computed; a KO number is recorded only when the mapping from
tuple to number is stated with its convention and its source.

**Rule (from `clifford_convention_registry.md` rule 4, enforced by
`hooks/claim_scope_gate.py`):** no document in this project may write a bare
`KO-dim N` unless a row below carries that `N` with `mapping_status: RESOLVED`.

---

## Entry 1 — the finite spectral triple `(A_F, H_F, D_F, J_F, γ_F)`

| field | value |
|---|---|
| **object** | G18's finite geometry, `H_F = ℂ³²`, one generation |
| **`J` definition** | antilinear `J = J_F ∘ conj`, where `J_F` is 16 real transpositions (CPT pairs) |
| **grading definition** | `γ_F = diag(−I₁₆, +I₁₆)`, L-sector `−1` / R-sector `+1` |
| **`D` definition** | off-diagonal Yukawa block, `Y_ν, Y_e, Y_u, Y_d` symbolic |
| **`J²`** | **`+1`** — `J_F conj(J_F) = +I₃₂` [VERIFIED-sympy, C36] |
| **`J D J⁻¹` vs `D`** | **`+1`** — `[D_F, J_F] = 0` [VERIFIED, G18 T7] |
| **`J γ J⁻¹` vs `γ`** | **`−1`** — `{J_F, γ_F} = 0` [VERIFIED, G18 T6] |
| **sign tuple** | **`(+1, +1, −1)`** |
| **KO number** | ✅ **`6`** (mod 8) — `mapping_status: RESOLVED`, see below |
| **claimed elsewhere as** | `KO-dim 6`, attributed to CCM (Chamseddine–Connes–Marcolli, arXiv:hep-th/0610241) |

### Resolution (C160, 2026-09-05)

`mapping_status: RESOLVED`. Closed via the cheap citation route (option 1 below),
not the internal derivation route (option 2) — see
`experiments/20260905-c160-ob12-ko-dimension-table-citation/decision.md` for the
full search record, verbatim quotes, and convention-matching reasoning.

- **KO number:** `6` (mod 8)
- **Primary source:** A. Chamseddine, A. Connes, M. Marcolli, "Gravity and the
  standard model with neutrino mixing," arXiv:hep-th/0610241, §2.4, eq. (2.19)
  — CCM's own finite geometry `H_F` (their `N=3`-generation object) is shown to
  satisfy `J_F² = 1`, `J_F` commutes with the Dirac operator, and
  `J_F γ_F = −γ_F J_F`, which their own text calls "characteristic of
  KO-dimension equal to 6 modulo 8." This instantiates the general axiom
  (their own Definition 2.7, restating A. Connes, "Gravity coupled with matter
  and the foundation of non-commutative geometry," arXiv:hep-th/9603053, axiom
  7 "Reality") stating `J²=ε`, `JD=ε′DJ`, `Jγ=ε″γJ` as a function of `n mod 8`.
- **Convention the source uses:** `ε = J²`; `ε′` ties `JDJ⁻¹` vs `D`
  (`JD=ε′DJ`); `ε″` ties `JγJ⁻¹` vs `γ` (`Jγ=ε″γJ`). This ordering is
  **identical** to this repo's own `(J², JDJ⁻¹/D, JγJ⁻¹/γ)` ordering — checked
  explicitly, not assumed; the ordering-mismatch risk flagged below did not
  materialize for this object.
- **Convention non-transfer note:** the general `n`-mod-8 table's third row
  (`ε″`) rendered incomplete past `n=3` in both arXiv-HTML fetches used for this
  resolution (a rendering artifact, not extrapolated or trusted past what was
  legible) — the resolution instead rests on CCM's own explicit, direct
  statement of all three signs for their own `H_F` at `n=6` (eq. 2.19 + its
  surrounding prose), which does not depend on the damaged table row.

### Why the number *was* blocked, historically

Mapping `(+1, +1, −1)` to a KO-dimension requires a table of the eight sign
triples. Before C160, this repository contained **no such table**, **no CCM
source file**, and **no internal derivation** of the mapping. `G26`'s own
comparison table recorded CCM's KO-6 as `[DOCS] postulated` — so the number had
been inherited on both sides of that comparison, and "same KO-dim
independently" (its original wording, corrected 2026-08-10) was never
supported. Recording the number from memory was precisely the move this
registry existed to stop; C160 closed the gap by fetching and quoting the
actual primary source instead (see Resolution above).

### What closed it

Option 1 of the two possible routes (option 2 remains untaken, not needed):

1. **A cited primary source** for the sign-triple ↔ KO-dimension table
   (Connes' axioms, or CCM §2 / Connes–Marcolli), transcribed here with its own
   convention stated — in particular *which* of the three signs the source calls
   `ε`, `ε′`, `ε″`, since G18's docstring and the common literature ordering do
   not obviously agree. **— DONE, see Resolution above.**
2. **An internal derivation** computing the triple for the model Clifford
   spectral triple in each `n mod 8` and matching. Feasible with machinery
   already built this week (`label_vs_code_check.py` does the `n=6,7` reality
   types), but the finite-geometry conventions for how `J` relates to `D` are
   subtle enough that the derivation must be written carefully, not assembled by
   analogy. **— not attempted, not needed now that option 1 is closed.**

### Scope note — the geometric side is a different object

`C32`/`C33` computed reality types for the **geometric** `S³×S⁶` spinor module
(REAL as a module; quaternionic on the zero mode). Those are **not** entries in
this table and must not be combined with it without an explicit product rule —
the finite and geometric KO-dimensions are separate data, and adding them is a
real theorem with real hypotheses, not arithmetic. `OB10`'s original
`3+6=9 ≡ 1 mod 8` reasoning is exactly the shape that needs that care.

---

## How to add an entry

Never add a row with a KO number filled in from recollection. Fill the tuple
first (it is computable), then leave `mapping_status: BLOCKED_BY_EXTERNAL_INPUT`
until a source or a derivation exists. A blocked row is information; a guessed
row is the C36 failure again.

```
object | J definition | grading definition | D definition
J^2 | JDJ^-1/D | JgJ^-1/g | sign tuple
mapping_status: RESOLVED | BLOCKED_BY_EXTERNAL_INPUT
KO number (only if RESOLVED) | primary source | convention the source uses
```
