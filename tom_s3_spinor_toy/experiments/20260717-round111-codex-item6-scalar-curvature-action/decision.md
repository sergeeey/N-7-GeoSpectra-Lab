# Round111 (Codex item 6) — Decision

**Date:** 2026-07-17
**Verdict:** `WEAKENED__MATH_CONFIRMED_SCAL_T_EQUALS_6_MINUS_6_TIMES_TORSION_SQUARED__PHYSICS_CONCLUSION_NARROWED`
(skeptic verdict — math CONFIRMED-analytic, physics scope corrected)
**Go/no-go:** the actual scalar curvature of `∇^t` (not a norm-squared
toy, per Codex's own item-6 request) is computed exactly and
cross-validated two independent ways. A clean Einstein-Cartan-type
decomposition falls out of the numbers. The PHYSICS conclusion is
narrower than first drafted — this does not settle whether a genuine
gravitational/spectral action prefers `t=0,1` or `t=1/2`; it settles
what the BARE curvature-scalar-of-the-torsionful-connection does, which
is a different, narrower question.

## What was computed [VERIFIED-tool: sympy + independent hand re-derivation
by skeptic]

1. **Metric:** `⟨X,Y⟩:=-½Tr(XY)` confirmed to make `{Z_1,Z_2,Z_3}`
   orthonormal.
2. **`Ricci^t(Z_a,Z_b)`**, from round99's own established
   `R^t(X,Y)Z=t(t-1)[[X,Y],Z]`: found proportional to the metric
   (`8t(1-t)·δ_{ab}`, an Einstein metric, exactly as symmetry predicts).
   `Scal(t)=24t(1-t)`.
3. **Mandatory cross-check, independent route** [textbook formula,
   `Ric_LC(X,Y)=-¼·Killing-form(X,Y)`, confirmed standard (Milnor 1976)
   by skeptic]: gives `Scal_LC=6` at the Levi-Civita point — **matches
   `Scal(t=1/2)=24·¼=6` from the completely independent `R^t`-based
   route exactly.** Two unrelated derivations agreeing is strong
   evidence the computation itself is correct.
4. **Shape:** `Scal(0)=Scal(1)=0` (flat, matching the already-established
   fact), single MAXIMUM at `t=1/2` (value 6) — a downward parabola,
   the OPPOSITE shape from round99's hoped-for double well.

## The decomposition the skeptic found, worth keeping as the actual
headline of this round

**`Scal(t) = Scal_LC - 6·(2t-1)² = 6 - 6·(2t-1)²`** — i.e. the bare
curvature scalar of `∇^t` decomposes EXACTLY into the (constant,
`t`-independent) Levi-Civita scalar curvature of the fixed metric, MINUS
a term proportional to `(2t-1)²` — and `(2t-1)` is exactly the
coefficient in this project's own established torsion formula
(`T^t=(2t-1)c·vol`). **This is a genuine, physically-recognizable
Einstein-Cartan-style split** (curvature-of-metric minus torsion-
squared), not a coincidence — a clean, useful structural fact.

## Skeptic correction — the physics conclusion, narrowed

**First-draft overreach:** claimed this refutes round99's double-well
hope for "any gravitational or spectral action." **Skeptic correctly
rejected this as too strong:** the genuine Einstein-Hilbert term of the
metric ALONE is the CONSTANT `Scal_LC=6` (the metric itself does not
change with `t` — only the connection does) — NOT the `t`-dependent
`Scal(∇^t)=24t(1-t)` this round computed. A physically-motivated
Einstein-Cartan-type action treats the metric-curvature piece and the
torsion-squared piece as SEPARATE terms with INDEPENDENTLY-determined
coefficients (`S~∫(Scal_LC + α|T|²)` for some coefficient `α` this
project has never derived from an actual physical action, e.g. the real
Chamseddine-Connes-Marcolli spectral action's own heat-kernel
coefficients). **The naive Ricci-scalar-of-the-torsionful-connection
computed here happens to correspond to one SPECIFIC choice of `α`** (the
one built into treating `∇^t` as if it were itself the whole story) —
a DIFFERENT, independently-signed `α` (which this project has not
ruled out, since it has never actually derived the real action's
coefficients) could still produce a double well. **Corrected scope:**
this round establishes that `Scal(∇^t)` ITSELF (the bare curvature
scalar of the torsionful connection, naively read as "the" curvature
term) is single-humped — it does NOT establish that no real
gravitational/spectral action could have a double well; that remains
exactly as open as round99 left it, now with a precise, well-motivated
target (`α`'s actual sign and value) for what a full derivation would
need to determine.

## Applying the pre-registered criteria (claim.md Section 3)

**SINGLE DIP / OPPOSITE SHAPE**, exactly as pre-registered for the bare
`Scal(∇^t)` quantity — but the pre-registered framing's implication
("refutes round99's hope at the standard-leading-term level" in full
generality) is narrowed, per skeptic review, to "refutes it for THIS
SPECIFIC combination, not for every possible Einstein-Cartan coefficient
choice."

## Kill Analysis

- **What this kills:** treating `Scal(∇^t)` (the bare curvature scalar
  of the torsionful connection, without separating out the torsion-
  squared piece's own independent coefficient) as automatically "the"
  gravitational action term — it is one specific, not obviously
  privileged, combination.
- **What this does NOT kill:** round99's own `WEAKENED` (not refuted)
  double-well hope — the genuine question (does the REAL spectral action
  prefer `t=0,1`) still depends on a coefficient (`α` above) this project
  has never derived.
- **What survives, sharper than before:** the exact decomposition
  `Scal(t)=Scal_LC-6(2t-1)²` is a clean, useful, physically-recognizable
  structural fact, independently double-checked — it precisely
  identifies WHAT would need deriving (the torsion-squared coefficient
  `α` in a genuine action) to settle the question either way, replacing
  a vague "compute the full spectral action" task with a much narrower,
  well-defined one.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Derive `α` (the torsion-squared coefficient) from an actual physical action | Requires committing to a specific action principle (Einstein-Cartan, spectral action heat-kernel expansion, or similar) and deriving its coefficients from first principles — substantially larger undertaking than this round |
| Check whether the sign of `α` in any STANDARD Einstein-Cartan-type gravity action (as used in the broader literature) is known/fixed | A literature check, not attempted here |

## Assumptions carried, unresolved

- `R^t(X,Y)Z=t(t-1)[[X,Y],Z]` (round99) — reused, not re-derived.
- The metric `⟨X,Y⟩=-½Tr(XY)` making `{Z_i}` orthonormal — a natural,
  but not independently-forced, normalization choice consistent with how
  prior rounds (E2/E7/E9/round99) implicitly used `{Z_i}`.

## What this does NOT mean

1. Does NOT establish that a real gravitational/spectral action prefers
   `t=1/2` over `t=0,1` either — only that the BARE, naively-read
   curvature scalar of `∇^t` does; a genuine action's actual torsion-
   coefficient sign is undetermined here.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round111-codex-item6-scalar-curvature-action
python e34_scalar_curvature_action.py
```
Expect: `metric_orthonormal_confirmed=True`,
`Ricci_t_proportional_to_metric=True`, `Scal_t_formula='24*t*(1 - t)'`,
`crosscheck_two_independent_routes_agree_at_t_half=True`, `Scal_0=0`,
`Scal_1=0`, `Scal_half=6`, `unique_critical_point_is_t_half=True`.
