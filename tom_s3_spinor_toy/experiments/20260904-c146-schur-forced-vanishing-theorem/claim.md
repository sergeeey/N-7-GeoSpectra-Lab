# C146 — Term1's vanishing (C145) is a forced Schur's-lemma consequence, not a fact about `m` specifically

## L0 gate (EstimandOps)

**Question type:** Descriptive (algebraic mechanism / general theorem, same class as C144/C145). Not causal, not predictive.

## Trigger, and a scope correction to the user's own C146 proposal

User proposed (after C145) deriving `E_W := D'_phys - D_Kostant^W` analytically,
proving its `SU(3)`-equivariance, and recovering C139's `c=1.154701`
analytically rather than by matrix computation — framed as the new
low-hanging fruit after C145's finding that the twist bundle's own
connection term carries the entire physical signal on the invariant sector.

**Before building this as proposed, a novelty/duplication check (this
project's own Mechanism-Transfer Gate discipline) found most of steps 1–3
of the user's own plan are ALREADY DONE, not new work:**
- `E_W`'s exact closed form is literally `Σᵢ eᵢ⊗conn_W[i]`, already computed
  symbolically in C145's own script (`EXTRA_TERM`).
- The exact scalar value is ALREADY in C139's own registered results
  (`results_c139.json`, field `c_exact`), computed via sympy exact
  arithmetic: **`c_exact = -2√3/3`** — not something needing new derivation,
  only re-attribution (since C145 already showed `Term1=0` on this sector,
  `c_exact` for the *full* operator `D'` already equals `E_W`'s own value).

**What is genuinely open, and what this round actually does instead:** WHY
does Term1 (Kostant's part) vanish on the invariant sector — is this a
numerical fact about `m` specifically, or a FORCED, general consequence
provable from already-certified branching data alone? This is the
substantive question worth a new round, and it is a stronger, more
general result than deriving `E_W`'s value for one specific `W`.

## Falsifiable claim

1. `D_Σ` (round59's own untwisted Dirac operator) is `SU(3)`-equivariant:
   `[D_Σ, ρ_Σ(a)] = 0` for all 8 generators `a` of `su(3)` acting on `Σ`.
2. Given (1) and the already-certified branching `Σ_odd = 3⊕1`,
   `Σ_even = 1⊕3̄` (`ODD_IDX`/`EVEN_IDX`, cited from C139/C143's own
   registered content), Schur's lemma FORCES `D_Σ`'s matrix restricted to
   `Σ_odd`'s "3"-part (columns `y1,y2,y3`) to be exactly zero — a nonzero
   equivariant map `3→Y` requires `Y` to contain a "3" constituent, and
   `Σ_even` has none (`3` and `3̄` are inequivalent `su(3)` irreps).
3. Any twist bundle `W` with NO `su(3)` singlet forces every element of
   `(Σ_odd⊗W)^{SU(3)}` to have zero component along `Σ_odd`'s own "1"-part
   (that "1" can only pair with a "1" in `W`, and `W` has none) — so
   C139's own domain-invariant vector must live entirely in the "3"-part,
   where `D_Σ` vanishes by (2).
4. **Consequence: Term1's vanishing (C145's finding) is FORCED for ANY
   zero-singlet twist bundle, not a numerical accident specific to `m`.**
5. Complementary check: `D_Σ`'s "1-block" (`Σ_odd`'s `y123` column) exactly
   reproduces round59's own certified `b=-√3` — the value ANY singlet
   summand of a twist bundle inherits directly (already implicit in C141's
   own Section 8 direct-sum decomposition, verified here directly from
   `D_Σ` alone, not merely cited).

**Kill criterion:** if any of (1)/(2)/(3)/(5) fails when checked
symbolically, the "forced, general" claim is FALSIFIED and C139's `Term1=0`
reverts to being a numerical fact about `m` specifically, not a theorem.

## What this does NOT mean

1. Does NOT give a general closed-form `E_W = f(W)` for arbitrary `W` — the
   SPECIFIC value `-2√3/3` remains geometry-specific to `m`'s own connection
   data on its "`3̄`-isotypic" piece; only the VANISHING of Term1 is shown
   general, not Term2's specific value. A general formula for Term2 across
   all possible non-singlet twists is explicitly NOT attempted here (per
   the user's own stop-rule: too large a task to fold into this round).
2. Does NOT resolve C142's `W_cand=3⊕3̄⊕3̄` question (that candidate has NO
   singlet AND is not simply "3̄" either — Hom-dimension 2, a case this
   round's binary singlet/non-singlet dichotomy does not directly cover;
   see "what remains open" in decision.md).
3. Does NOT change `N_gen=3`'s CONDITIONAL status, or any of round59/C139/
   C141's own already-computed kernel values.
4. Does NOT retract C143's Lemma 1/2 or C144/C145's own findings — this
   round EXPLAINS one of the empirical facts underlying C143's Lemma 1
   (why C139's own scalar could be predicted, in sign of vanishing/non-
   vanishing, before computing) more deeply than C143 itself was able to.
