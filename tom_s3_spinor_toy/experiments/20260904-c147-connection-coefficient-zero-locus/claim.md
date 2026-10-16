# C147 — the connection coefficient `c_W(∇)` vanishes ONLY at the zero connection, over the whole admissible family

## L0 gate (EstimandOps)

**Question type:** Descriptive (exact zero-locus of an explicitly-constructed
algebraic functional). Not causal, not predictive.

## Trigger, and what is genuinely new versus already known

User (consortium message, post-C146) named this as the single highest-value
next round: *"c_W(∇)=0 — when?"* for the invariant-connection class C139
already used, arguing both outcomes are scientifically useful (a nonvanishing
theorem = robustness result; a nontrivial zero locus = a genuine geometric
zero-mode mechanism).

**Novelty check before building (Mechanism-Transfer discipline):** part of
this is already answered. C139's own Section 7b swept **13 angles** across
C73b's certified 2-dimensional admissible torsion family and found
`|c(θ)|` constant (spread 6.7e-16) with `Term1` zero at every sample. But
C139's own code comment states the residual gap precisely: *"a linear
functional on a real 2-dim space GENERICALLY has a 1-dim zero locus"* — 13
samples cannot exclude a zero locus the sampling missed.

**What this round adds:** the continuum statement, using C146's theorem to
make it cheap. By C146, `Term1 ≡ 0` identically (not just at sampled
angles), so `c(∇) = Term2(∇)`, which is `R`-linear in `∇` by construction.
Therefore **two** evaluations — one per basis direction of the 2-dim family
— determine `c` on the ENTIRE continuum, and the zero locus is decided by a
single basis-independent criterion: whether the real 2×2 matrix
`[[Re c₁, Re c₂],[Im c₁, Im c₂]]` is nonsingular.

## Falsifiable claim

1. `Term1 = 0` at both basis directions of C73b's admissible family
   (hence, by `R`-linearity, identically on the whole family — the
   continuum version of C139's 13-sample finding, and independently
   predicted by C146's theorem).
2. The `R`-linear map `(α,β) ↦ α·c₁ + β·c₂` from `R²` to `C` is
   **nonsingular** — so `c_W(∇) = 0` holds ONLY at `∇ = 0` (the zero
   connection, which is the degenerate non-metric point, not an admissible
   geometry).
3. `c₂ = ±i·c₁` exactly (equal magnitude, orthogonal in `C`) — which is
   precisely the structural reason C139 observed `|c(θ)|` constant on the
   unit circle, and means `c` is `C`-linear (holomorphic) in the natural
   complex coordinate `α+iβ` on the torsion family.
4. Linearity, applied at NOMIZU's own coordinates in that basis,
   reproduces C139's own registered `|c_exact| = 2√3/3` exactly.

**Kill criterion:** if the real 2×2 matrix is SINGULAR (det = 0 within
numerical tolerance, with condition number blowing up), then a nontrivial
1-dimensional zero locus exists inside the admissible family — claim 2 is
FALSIFIED and the "geometrically tunable zero mode" the user hoped for
would be real.

## What this does NOT mean

1. Does NOT establish anything outside C73b's certified 2-dimensional
   `Hom_{su(3)}(m, Λ²m)` family — a larger connection space (non-equivariant
   connections, or a different twist bundle's own family) is untouched.
2. Does NOT give `c` for twist bundles other than `m` — the specific
   coefficient `c₁` is `m`-specific; only the METHOD (2 evaluations +
   linearity ⟹ continuum) generalizes.
3. Does NOT change `N_gen=3`'s CONDITIONAL status, or C139's own
   already-registered kernel=0 value (this round strengthens the latter's
   status from "verified at 13 sampled angles" to "theorem over the
   family", it does not alter the number).
4. Does NOT resolve C142's `W_cand` question (Hom-dimension 2 in the
   OPERATOR sense — a different, still-open case) — this round's
   2-dimensionality is that of the CONNECTION family, a different object;
   the two must not be conflated.
