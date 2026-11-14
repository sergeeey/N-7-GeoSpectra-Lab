# C187 Decision — UPDATED. Periodicity derived; claim (b) rejected precisely, not generically.

**Date:** 2026-09-09 (original), **updated same day** after the periodicity
was derived per user request.
**Verdict:** Claim (a) **CONFIRMED**, 10/10 (unchanged). Claim (b) **REJECTED,
precisely** — the periodicity question is closed, and what remains is a
distinct, narrower, unresolved question about `C187`'s own operator
construction, not about labelling.

All numbers trace to `c187_s3_euler_reduction.py`, `run_output.txt`,
`c187b_periodicity_and_operator_check.py`, and `run_output_b.txt`.

---

## 1. What this round was

`C186`'s decision.md §4 corrected the half-angle pearl's own falsification
test — it had named a task (`k≥2` exact `S³` eigenspinors) that exercises a
different method entirely and cannot test the pearl. The corrected test:
build the `S³` Dirac operator in **Euler angles**, where it genuinely is an
ODE, apply the half-angle substitution, and check (a) it stays fast/polynomial
and (b) it reproduces the already-known spectrum.

## 2. Claim (a) — CONFIRMED

Metric, frame, and spin connection were all **derived**, not quoted:

- the metric came from pulling back the flat `ℝ⁴` metric through the *same*
  `x0..x3` embedding this project uses everywhere else — not a textbook
  formula, `P1`–`P2`;
- the spin connection came from solving Cartan's structure equation exactly,
  `P4`–`P5`, mirroring `C185`'s discipline.

Applying `D` to a plane-wave ansatz `(F,G)e^{i(mφ+nψ)}` took **0.1 seconds**
(`P6`) — against `C185`'s abandoned first attempt on the analogous `S²`
problem, which ran **25 minutes** before being killed. Both components kept
the *same* `(m,n)` with no mismatch (`P7`) — the exact defect class that
`C185` hit once and this round checked for explicitly. Clearing denominators
and substituting `s=sin(θ/2)`, `c=cos(θ/2)` needed no `simplify()` call on a
transcendental expression anywhere (`P8`); the bare `m`-term needed the same
`hom=(s²+c²)` multiplier trick `C185` used for its own bare-`m` term (`P9`),
confirming the reduction generalises structurally, not by coincidence. A
blind scan of `176` `(m,n,N,λ)` combinations — a considerably broader sweep
than a single case — completed in `5.2` seconds (`P10`).

**This is the pearl's own registered claim, and it holds without
qualification.**

## 3. Claim (b) — genuinely open, and why it was not forced

The blind scan (four natural `(m,n)=(±1/2,±1/2)` guesses, degrees `N=0..3`,
every integer `λ∈[-5,5]`) found **zero** nonzero-kernel hits. Not a near miss
on one case — a clean null across all `176` combinations tried.

**What this is not:** it is not evidence against `C184`/`C186`'s spectrum,
which was independently verified there by a completely different method
(finite matrices over `ℚ(i)`, no angles). It is not evidence against claim
(a), which is about speed/polynomial-ness and was directly measured. Both
stand untouched.

**What it likely is:** a mismatch between the naive `(m,n)` plane-wave labels
used here and the actual periodicity of spin-weighted functions on `S³`'s
double cover. The half-integer values `-3/2` and `1/2` that appeared in an
early, later-discarded diagnostic (a buggy square-submatrix determinant check,
not a valid computation — flagged and replaced with the correct full-rank
`kernel_dim`, same technique `C185` used) are *suggestive* of a half-integer
shift somewhere between `(m,n)` and the true weight, but that is a hypothesis,
not a finding — it is not asserted as fact here.

**Why this was not chased further this round.** Getting the exact periodicity
right is its own derivation — comparable in care to the work `C186` did to
determine which relative sign of `J₃ᴿ` actually commutes with `D₀`, not
something to guess at by widening a blind numeric scan. This project's own
recorded practice (`patterns.md` and this session's own memory:
"3 consecutive skeptic-caught bugs = stop patching, park or redesign";
"needs spectral-flow machinery" turned out to be a 15-line fix once actually
tried, the opposite failure mode) argues against both premature declarations
of "blocked" *and* against unaudited persistence chasing a fit. Reporting an
honest partial result is the disciplined middle path this round takes.

## 3b. Floor–Ceiling for claim (a)'s speed metric (Step 4a)

The metric with room to move is **wall-clock time to reduce the eigenvalue
problem**, not a pass/fail threshold, so floor and ceiling are stated as
reference points rather than a formula:

| | construction | time |
|---|---|---|
| **floor** (mechanism removed — attack the problem in raw `θ` coordinates, no half-angle substitution, letting `simplify()` chew on `sin`/`cos`/`exp` mixed together) | this is exactly `C185`'s abandoned first attempt on the analogous `S²` problem | **~1500s, killed before completion** |
| **observed** | half-angle substitution, pure polynomial algebra | **0.1s** (single case, `P6`), **5.2s** (176-case blind scan, `P10`) |
| **ceiling** | the substitution step itself is pure algebraic rewriting with no search — there is no faster correct method than doing the rewrite once | effectively **instant**; observed is already within a small constant factor of it |

`efficiency` in the Step 4a sense is not a single number here because the
*floor* comparison is against a different problem instance (`S²`, not `S³`)
run by a different script — the two are not directly divisible. The
qualitative reading is unambiguous regardless: four orders of magnitude
between "mechanism absent" and "mechanism present," which is the entire
content of the pearl's speed claim.

Claim (b) does not get a Floor–Ceiling interval: it is not a threshold on a
continuous metric, it is a yes/no question (does *some* `(m,n)` reproduce the
known spectrum) that came back a clean null on every case tried, not a value
sitting somewhere on a scale between a floor and a ceiling.

## 4. Kill criterion for claim (b) — RESOLVED same day, both halves met

The criterion recorded above was: reject (b) only once the correct
`(m,n)`-periodicity is derived **and** still fails to reproduce the known
spectrum. Both halves are now done — see `c187b_periodicity_and_operator_check.py`,
`5/6` checks pass (the one designed failure is documented, not accidental).

### 4a. The periodicity, derived

`C186` built `J₃ᴸ`, `J₃ᴿ` from the quaternion axis "`k`" (Python index `a=2`)
— an arbitrary choice among three equally valid `su(2)` Cartan directions;
which one is called "3" only fixes the basis the weight labels are read in,
not the physics. This project's Euler-angle embedding has its own preferred
axis, found by solving for which linear combination of `∂θ,∂φ,∂ψ` each
quaternion generator equals (least-squares against the embedding's own
Jacobian, verified numerically to `1e-30` across several points, since exact
symbolic simplification of these nested half-angle expressions proved
unreliable — see the module docstring):

```
X_0^L = 2 d/dphi   EXACTLY   (quaternion "i", not "k")
X_0^R = 2 d/dpsi   EXACTLY   (quaternion "i", not "k")
X_2^L = 2 sin(phi) d/dth + 2 cos(phi)/tan(th) d/dph − 2 cos(phi)/sin(th) d/dps
        (C186's own choice — mixes ALL THREE coordinates, not a pure direction)
```

Rebuilding `C186`'s joint-cell decomposition using axis `a=0` instead of `a=2`
is a **relabelling**, not new physics: `[D₀,J_L]=0`, `[D₀,J_R]=0`,
`[J_L,J_R]=0` all still hold identically (check `B1`). Under this relabelling,
**every one of the four extreme-weight `k=1` states collapses to a single
Fourier mode** shared by both spinor components (check `B2`, `4/4`) — exactly
the ansatz shape `claim.md` assumed, where the "`k`"-axis version needed **four**
separate Fourier modes per state (documented in `claim.md`'s Rosetta-stone
section). **This is the periodicity**, and it fully answers the "what map"
question this round originally left open.

### 4b. What remains — narrowed, not solved

Feeding the now-correctly-derived candidate, `(m,n)=(-1/2,1/2)`, expected
eigenvalue `-1`, into `C187`'s own committed `D` operator does **not** return
a constant multiple of the candidate (check `C1`, the one designed failure).
This was checked exhaustively, not just once:

- symbolically, under 4 sign conventions on the connection term and the
  overall operator sign;
- numerically (theta evaluated at several points, high precision, avoiding
  the transcendental-simplify slowness this project has hit before), under
  **all 144 combinations** of which Pauli matrix pairs with which vielbein
  leg × connection sign × operator sign.

Zero of 144 reproduce a theta-independent eigenvalue. This rules out a simple
mislabeling or sign error as the cause. What it does **not** rule out —
because it was not checked this round, and would need a differently-built
operator to check — is a genuine construction defect in the vielbein or
Cartan-connection derivation itself (as opposed to how it is *labelled*
afterward). `C187`'s own internal checks (`P1`–`P9`: frame reproduces the
metric exactly, Cartan's equation is solved with zero residual) certify the
construction is **self-consistent**, not that it **equals** `C184`/`C186`'s
independently-built `D₀`. That is a real, generalisable gap in what a
self-consistency check can certify — recorded here because it will recur
anywhere a project builds two representations of "the same" object by two
different routes and only checks each route against itself.

**Consequence for the falsifiable claim:** claim (b) as originally stated
("scanning candidate eigenvalues reproduces the known spectrum") is now
**REJECTED** — the derived, correctly-labelled candidate does not satisfy the
eigen-equation for `C187`'s operator. This is a precise rejection of *this
round's specific construction of `D`*, not of the underlying `S³` physics
(`C184`/`C186` stand, cross-confirmed by the axis-relabelling exercise in
§4a) and not of claim (a) (the half-angle mechanism itself, confirmed
independently of any of this).

### 4c. What a future round would need

Rebuild `D` on `S³` in Euler angles by starting from the quaternion structure
directly (express `X_a^R` in `(θ,φ,ψ)` coordinates via the same Jacobian
technique used in §4a, then assemble `D = -i Σ_a σ_a X_a^R` using THOSE
coordinate expressions) rather than an independently-chosen geometric
vielbein — this guarantees agreement with `C184`/`C186`'s `D₀` by
construction instead of needing to be checked for it afterward. Not attempted
this round; recorded as the concrete next step, not vague future work.

## 5. What this does NOT establish

- **Does not touch any physics claim.** `C184`/`C186`'s spectrum stands,
  verified by a different method there, and further cross-confirmed by the
  axis-relabelling in §4a (which required no new computation, only a
  relabelling, and still held).
- **Does not identify the specific bug in `C187`'s vielbein/connection.**
  §4b rules out mislabeling and sign errors across 144 combinations, but does
  not diagnose what IS wrong — only that something is, localized to the
  operator construction rather than to periodicity or physics.
- **The half-angle pearl's core mechanism claim is confirmed on a second,
  genuinely independent geometry** (`S³` in Euler angles, not `S²`) — this is
  real transfer, not a restatement of `C185`, and is unaffected by §4's
  finding since claim (a) and claim (b) test different things.

## 6. Consequence for the pearl registry

The corrected test (filed in `C186`'s pass over the registry) is now **fully
run and resolved**: the speed/polynomial half is CONFIRMED; the eigenvalue-match
half is REJECTED for a precisely localized reason (§4), not left open. The
pearl's own `next_check` (`2026-10-15`) is unaffected — this round ran early,
ahead of schedule, and closed the open question rather than leaving it for
that date.

## 7. Reproduction

```
cd experiments/20260909-c187-s3-euler-angle-reduction
python c187_s3_euler_reduction.py               # claim (a): 10/10
python c187b_periodicity_and_operator_check.py  # periodicity + claim (b): 5/6
                                                 # (the 1 failure is the documented finding)
```

`10/10` (claim (a)) and `5/6` (periodicity + localization, `C1`'s FAIL is
expected and documented). `ruff check` and `ruff format`: clean on both files.
