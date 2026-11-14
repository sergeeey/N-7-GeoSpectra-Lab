# C145 — Decision

## Structural argument (derived before computing, from Landweber's own equations)

Kostant/Landweber's twisted operator `Ð_μ`, restricted to `λ=0` (trivial G2-rep
— the block round59/C139/C141 actually compute, since their objects are
elements of `Σ⊗W` alone with no `V_λ` tensor factor), reduces to `c(v)⊗Id_W`
exactly: `r(Xᵢ)` differentiates only the `L²(G)` factor, and its restriction
to constant functions is zero regardless of the twist representation `μ=W`
chosen. Kostant's own twisted operator, at `λ=0`, therefore gives `W` NO
connection of its own — it is a passive identity factor, full stop, in HIS
construction.

## Computation (symbolic, exact, SymPy — `c145_twisted_vs_kostant.py`)

1. Imported round59's own Clifford algebra + Nomizu machinery directly
   (`round59_route_a_independent.py`, the SAME module C139 itself imports),
   re-verified the Killing-spinor calibration on import (regression gate).
2. Rebuilt C144's own `c(v)` and `α=√3/4` from the same raw `Lam` data,
   re-verified the `D_Σ = α·c(v)` identity as a regression gate BEFORE
   proceeding (would have stopped here if it failed) — passed.
3. Built `W`'s own Nomizu connection (`conn_W[i]`) from C139's own
   `bivec_to_6x6`/`rho_vector` formula (sign-corrected vector representation
   of the SAME `NOMIZU` data), transcribed verbatim, not re-derived.
4. Built `D' = D_Σ⊗Id_W + Σᵢ eᵢ⊗conn_W[i]` (C139's own Leibniz construction)
   and the Kostant candidate `α·c(v)⊗Id_W`.
5. **Result: `D' ≠ α·c(v)⊗Id_W`.** Residual is nonzero at 192 of 2304 (48×48)
   entries. Independently confirmed the residual EXACTLY equals
   `Σᵢ eᵢ⊗conn_W[i]` (not just asserted from the algebra — checked directly),
   confirming the structural prediction of WHERE the mismatch comes from.
6. Size check (exact Frobenius-norm-squared, no floating point):
   `‖α·c(v)⊗Id_W‖²_F = 36`, `‖extra term‖²_F = 16` — ratio `4/9`. The extra
   term is not a small correction; it is comparable in magnitude to the
   matched part.

## Verdict: **REJECT** (of the specific identification claim)

The claim — that C139/C141's twisted Dirac operator is literally an instance
of Kostant/Landweber's algebraic `Ð_μ|_{V_0}` — is FALSIFIED, cleanly and
symbolically, not by a near-miss. C139/C141's construction is a genuinely
MORE GENERAL "physicist-style" twisted Dirac operator (both `Σ` and `W`
carry their own Levi-Civita connection) than Kostant's group-theoretic one
(where `W`, at `λ=0`, carries no connection at all).

## Kill Analysis (mandatory for REJECT, per FL)

**What this kills:** the specific hypothesis that Slebarski's closed-form
kernel theorem (`Ker(Ð_μ) = V_{w(μ+ρ_H)−ρ_G}` or `0`) directly applies to
C139/C141's own twisted-Dirac construction. It does NOT — the operators are
different objects, not merely differently-normalized versions of the same one
(C144's untwisted case WAS a clean normalization relationship; this is not).

**What this does NOT kill:**
- C144's own untwisted-case result (`D_Σ = α·c(v)`) — re-verified here as an
  unmodified regression, still holds.
- C139's or C141's own computed kernel values — both independently
  established by their own machinery, untouched by this round.
- C143's Lemma 1/2 (the Schur's-lemma graded-floor mechanism) — this remains
  the correct, self-contained explanation for this project's OWN twisted-
  Dirac family; it was never claimed to itself be Kostant's theorem, only
  that Kostant's theorem happened to cover a NEIGHBORING case (round59's
  untwisted operator).
- The POSSIBILITY that C139/C141's `D'` corresponds to Kostant's `Ð` for
  some `λ≠0` (see Relaxation Map below) — genuinely untested, not ruled out.

**Relaxation Map (one option, NOT pursued this round — Minimal Relaxation
Rule, AOG discipline: would need its own pre-registration and experiment ID
if picked up):**

| Assumption changed | New claim | Status |
|---|---|---|
| `λ=0` → `λ≠0`, some specific G2-representation | `D'` restricted to `Σ⊗W`'s invariant sector equals Kostant's `Ð` for a `V_λ` whose isotropy branching happens to reproduce the extra `Σᵢ eᵢ⊗conn_W[i]` term via `r(Xᵢ)` acting on `V_λ` | Not attempted — would require reverse-engineering which `λ` (if any) makes this work, a genuinely different and harder problem than this round's direct comparison |

**Anti-Overfitting Gate self-check (before naming the above as anything more
than a listed option):** AOG-1 (pre-registered before the null?) — NO, it
occurred to me only after seeing the null result, so it is correctly logged
as a Relaxation Map ROW, not chased as a live variant this session. AOG-5
(independent motivation beyond rescuing the hypothesis)? — none currently
offered. Correctly parked, not promoted.

## Follow-up check (self-raised, before the skeptic pass): does the mismatch
## survive on the actual physics-relevant sector, or only on the full 48-dim space?

The round's own claim.md left this open as a real question (any 48×48
comparison could in principle mismatch only in directions that don't matter
for the kernel test C139/C141 actually run). Checked directly
(`c145b_residual_on_invariant_sector.py`), reusing C139's own
`su3_ops_np`/`rho_m_adnu_np`/`block_global_gen`/`invariant_basis_gen`
machinery unmodified, projecting onto the exact 1-dimensional
`(Σ_odd⊗m)^{SU(3)} → (Σ_even⊗m)^{SU(3)}` sector C139's own headline number
comes from.

**Result: not only does the mismatch survive — the Kostant candidate
`α·c(v)⊗Id_W` evaluates to EXACTLY ZERO on this sector** (`0j`, machine
precision), while C139's own `D'` gives the full nonzero value
`c = (−1.1336…−0.2196…j)`, `|c|=1.154701` — reproducing C139's own already-
registered headline number exactly (cross-check: this script's independent
reconstruction of `D'` and the invariant sectors matches C139's own reported
value to machine precision, confirming the reconstruction is faithful).
**The entire physical signal C139 measures on this sector comes from the
"extra" twist-bundle-connection term; Kostant's own operator contributes
NOTHING to it at this sector.** This does not weaken the REJECT — it
strengthens its practical import: the mismatch is not confined to some
physically-irrelevant corner of the 48-dim space, it IS the whole
physically-relevant number.

## Skeptic pass (Step 8a, context-blind: claim.md + script only)

**Verdict: CONFIRMED-REAL.** The REJECT is trustworthy. No fatal concern.

The skeptic (no Bash access, hand-verified the algebra) independently re-
derived `α=√3/4` from scratch (same "each unordered triple hit exactly 3
times" argument as C144), confirmed the transcription of `bivec_to_6x6_sympy`/
`rho_vector_sympy`/the Leibniz-rule build is byte-identical to C139's own
code, and — most decisively — found that **C139's own script (Sections 6a/
7b) already computes this exact decomposition internally**: `d_term1_only`
(= `D_Σ⊗Id_W` = `α·c(v)⊗Id_W`) and `d_term2_only` (= `Σᵢeᵢ⊗connᵂᵢ`, the
"extra" term), and C139's own Section 7b explicitly states
`term1_remains_exactly_zero_across_whole_torsion_family` — meaning C139
ITSELF already established, independently of this round, that its whole
headline signal comes from `term2` alone. This is a stronger, doubly-
independent confirmation of the same fact my own follow-up check
(`c145b_residual_on_invariant_sector.py`) found numerically — three
independent routes (this round's symbolic 48×48 comparison, my own numeric
invariant-sector projection, and C139's own pre-existing internal Section
7b decomposition) now agree.

**One hardening note (not fatal, addressed below):** the skeptic could not,
from the evidence set given to it (no session history), independently verify
that Landweber's own twisted-operator formula truly gives `W` no action at
all on `λ=0` — this premise was stated in claim.md as a structural argument,
not cited to a specific equation. **Closed here, using content already
directly fetched and read from the primary source earlier in this session
(math/0005056, Section 3 "Homogeneous Differential Operators"):**
Landweber defines the twisted operators explicitly as restrictions,
`D_μ : Hom_H(U_μ*, L²(G)⊗M) → Hom_H(U_μ*, L²(G)⊗N)`, obtained from the SAME
homogeneous operator `D` (built entirely from `L²(G)⊗M`, no separate action
on `U_μ`) by projecting onto the `H`-equivariant subspace transforming like
`U_μ*`. `U_μ` (here, `W`) enters ONLY as a projection/selection label — there
is no term in Landweber's own construction giving it an independent
connection. The structural premise is confirmed directly against the primary
source, not merely inherited from an unverified summary.

### Response Matrix (per FL Step 8a)

| Concern | Skeptic severity | Response |
|---|---|---|
| Landweber's `D_μ` W-passivity premise not cited to a specific equation | scope (hardening note) | **Fixed.** Direct citation to Landweber Section 3's own `D_μ` definition added above, confirming the premise from the primary source itself. |
| Everything else (transcription, C144 regression, residual identity, nonzero-ness, invariant-sector survival) | none found | No action — independently re-confirmed by the skeptic via a route (C139's own internal `term1`/`term2` split) this round's own script did not even reference. |

**True kill condition (per FL): NOT met — but this time the KILL is the
verdict.** The claim being tested (identification with Kostant/Landweber)
was FALSIFIED, and that FALSIFICATION itself survived context-blind adversarial
review without a single fatal concern. REJECT stands.

## What remains open

Whether ANY reformulation connects C139/C141's family to Kostant/Landweber's
framework (via the `λ≠0` route above, or otherwise) is now a **materially
different, harder question** than the one C144 raised — not simply "finish
checking the twisted case." C142's `W_cand` question remains BLOCKED-INTERNAL
(OB14), unresolved by the Kostant/Landweber literature connection after all.
