# Round70-E5-Universality-CP3-S3xS3 Decision

**Date:** 2026-07-17

**Canonical status correction (same day):** Part A's verdict must be read as
`ROUTE_C_PASS`, not as an exact-kernel/full-universality PASS — Route C is a
necessary-condition/isotropy-Schur-bound-style check (a specific structural
criterion, already used for S⁶/SU(3)-T², that bounds `dim ker ≤ 1` and rules
out one obstruction to `Term2=0`); it is NOT equivalent to establishing
`(dim ker D⁺, dim ker D⁻)=(1,0)` for the physically-relevant Levi-Civita
twisted operator, which remains a separate, unclosed L4A/L4B-style
calculation for CP³ (see "explicitly OUT OF SCOPE" section below, which
already stated this — this note exists because a downstream summary of this
experiment collapsed the distinction to a bare "PASS," which is imprecise
and should not be repeated).

**Verdicts:**
- **Part A (CP3): `ROUTE_C_PASS`** (corrects Round 64's framing without
  overturning its literal finding — see "Diagnosis of Round 64" below).
  Isotropy-Schur bound `dim ker <= 1`. Full L4A/L4B Lichnerowicz-norm-bound
  number: explicitly OUT OF SCOPE (see below). **"Universality" for CP³
  currently means "passes the same Route-C structural test as S⁶/SU(3)-T²,"
  not "exact kernel independently established."**
- **Part B (S3xS3): `OPEN_STRUCTURALLY_DISTINCT`** (the simple no-singlet
  argument does NOT go through — an isotropy-trivial slot IS available in
  `Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})`, unlike S6 and `SU(3)/T^2`). This is
  a genuine, new, structural difference for S3xS3, not a failure of this
  round's method. Isotropy-Schur bound `dim ker <= 1` still holds
  independently (robust, does not depend on the Route-C outcome).

All numbers below trace to `round70_universality_check.py` and its saved
output `run_output.txt` — none hand-typed independently of that file.

---

## Diagnosis of Round 64's CP3 finding (Part A of the task)

**Was it a structural fact about CP3, or a fixable setup error?**

**Both, in a precise sense — Round 64's literal finding survives, but its
scope was narrower than its own prose suggested, and a genuinely different,
correctly-posed mechanism (Route C) DOES work on CP3.**

1. **What Round 64 actually tested and correctly killed:** whether
   Charbonneau-Harland 2016's own INSTANTON-DEFORMATION machinery (their
   Proposition 7/8, Theorem 3, Lemma 5 — the whole apparatus built around
   `epsilon in Omega^1(M) (x) AdP` mapped via `epsilon -> epsilon . psi`
   into a subbundle of `S (x) E`) could be reused, with `E` substituted for
   this project's `S^- = T^{1,0}(+)1` instead of their own `E = h_C` /
   `su(3)_C`, to answer THIS project's zero-mode-counting question. This
   round independently confirms Round 64's finding and adds a SECOND,
   independent reason it fails, not previously identified:

   Re-reading CH2016 pages 11-12 directly (this session): their operator
   `D^{1/3,A}` acts on sections built by Clifford-multiplying a 1-form-valued
   `epsilon in m* (x) E` by the Killing spinor `psi`. Since Clifford
   multiplication by a 1-form shifts the spinor bundle's `Lambda`-degree by
   exactly +-1, and `psi` (the Killing spinor itself) lives in the
   `Lambda^0 (+) Lambda^3` piece of `S = Lambda^*(m^{1,0})`, the image
   `epsilon . psi` lands ONLY in `(Lambda^1 (+) Lambda^2) (x) E` — a
   rank-6-per-`dim(E)` subbundle of the FULL rank-8-per-`dim(E)` bundle
   `S (x) E`. This project's own `D_{S^6} (x) S^-` (G73/G74A) acts on the
   FULL `S (x) S^-`, not this restricted `Lambda^1(+)Lambda^2` piece. So even
   substituting `E = S^-` into CH2016's own formalism would NOT reconstruct
   this project's actual operator — there is an OPERATOR-TYPE mismatch on
   top of the REPRESENTATION-TYPE mismatch Round 64 already found. This
   reinforces (does not merely repeat) Round 64's finding: CH2016's own
   framework is not the right tool for this project's mechanism, for two
   independent, stackable reasons.

2. **What Round 64 overstated:** its decision.md says "the twisting bundle E
   CH2016 would need to supply (E= fundamental "3") is never instantiated
   anywhere in the paper" and concludes "There is no number to report."
   This conflates two distinct objects: (a) `E`, the twisting representation
   CH2016 chooses for its OWN instanton problem (never the fundamental — true,
   confirmed again here), and (b) the raw isotropy-representation DECOMPOSITION
   of `m*_C` itself (needed as the base ingredient for ANY twisted-bundle
   construction on this coset, regardless of which `E` one twists by). CH2016
   DOES state (b) explicitly and completely for CP3 — eq. (27)-(28), page 15,
   transcribed and independently Casimir-cross-checked in this round's script
   (`part_cp3()`, `cas_values_on_m_star_C == {-4}`, matching CH2016's own
   stated single eigenvalue -4 on `m*_C`). Round 64's "no number to report"
   was correct for the INSTANTON-deformation mechanism specifically, but
   incorrectly generalized to "no computation is possible on CP3 at all" —
   a DIFFERENT mechanism (Route C), needing only (b) and not CH2016's own
   `E`-twisted instanton machinery, is directly computable from data CH2016
   already states.

**Conclusion:** Round 64's verdict is corrected from a blanket "ILL-POSED, no
computation possible" to "ILL-POSED specifically for the CH2016-instanton-
deformation route; a DIFFERENT route (Route C, this round) is well-posed and
computable using only already-published isotropy data." This is not a
reversal of Round 64 (its literal finding about CH2016's own machinery stands,
reinforced) — it is a scope correction, exactly analogous to how Round 65
itself found CP3's Round-64 ILL-POSED verdict did not exclude CP3 from Route C
(claim.md's own "explicit risk flagged" section, carried over unchanged from
Round 65's text).

---

## Part A: CP3 Route-C computation (script `part_cp3()`)

**Step 1 — isotropy data (cross-checked against CH2016 eq. 27-28, pages
14-15):** `m*_C ~= V(1,1) (+) V(1,-1) (+) V(0,2) (+) V(0,-2)` under
`Sp(1)xU(1)`, using CH2016's own `(m,n)` convention (`V(m,n)` = `(m+1)`-dim
`sp(1)` irrep, `U(1)` charge `n`). Independent Casimir recomputation via
CH2016's own stated formula `rho_(m,n)(Cas_h) = -m(m+2)-n^2` gives a single
value `-4` on all four pieces of `m*_C` — matches CH2016's own stated single
eigenvalue exactly (`cas_values_on_m_star_C: [-4]` in `run_output.txt`).

**Step 2 — determining `m^{1,0}` (NOT assumed, checked):** two candidate
same-conjugate-pair-avoiding splits were tested:
  - `same_sign = {V(1,1), V(0,2)}` -> `Lambda^3(m^{1,0})` computed as `V(0,4)`
    — NOT isotropy-invariant. **Rejected.**
  - `mixed_sign = {V(1,1), V(0,-2)}` -> `Lambda^3(m^{1,0})` computed as
    `V(0,0)` — isotropy-invariant. **Accepted.**

  (This is a genuine, checkable correction over a naive first guess — this
  session's own first hand-derivation initially assumed `same_sign` before
  running the `Lambda^3`-invariance check and finding it fails; the script's
  `lambda3_candidates` output records both candidates and the assertion that
  exactly one passes.)

  So `m^{1,0} = V(1,1) (+) V(0,-2)` for CP3 (Sp(1) doublet at U(1) charge +1,
  the horizontal/twistor-fibration-base direction, plus an Sp(1)-singlet at
  U(1) charge -2, the vertical/fibre direction — consistent with CP3's
  standard description as the twistor space of S4, CH2016 page 22).

**Step 3 — Route-C crux (`Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0})`):**
`Lambda^2(m^{1,0}) = V(0,2) (+) V(1,-1)` (dim `1+2=3`, correct). Full tensor
square: `{(0,-2), (0,4), (1,1), (2,-2)}` — **no `(0,0)` component.**
**Route C's crux step holds for CP3**, by the same style of argument as
`SU(3)`'s "`3bar(x)3bar` has no singlet" and `T^2`'s "no zero-weight in
`Lambda^2(x)Lambda^2`" — re-derived here from Sp(1)xU(1) representation
theory directly, not copy-pasted.

**Step 4 — isotropy-Schur bound (Lemma B analog):** `S^- = m^{1,0}(+)1 =
V(1,1) (+) V(0,-2) (+) V(0,0)`. Trivial-multiplicity count: exactly 1 (from
the explicit `V(0,0)` summand only — `V(1,1)` has nonzero `Sp(1)` spin AND
nonzero `U(1)` charge; `V(0,-2)` has zero `Sp(1)` spin but nonzero `U(1)`
charge, so neither is isotropy-trivial). **`dim ker <= 1`, same bound as S6
and `SU(3)/T^2`.**

**Part A verdict: PASS on Route C.** Both the crux singlet-absence check and
the Schur bound hold, by the SAME frozen argument structure used for S6 and
`SU(3)/T^2`, using ONLY already-published CH2016 representation data plus
general Clebsch-Gordan arithmetic — no new machinery invented, no
CH2016-instanton-deformation formulas reused (avoiding Round 64's confirmed
operator-mismatch trap entirely).

---

## Part B: S3xS3 Route-C computation (script `part_s3xs3()`)

**Step 1 — isotropy data (cross-checked against CH2016 page 14):**
`m*_C ~= 2 x V2` under `SU(2)_diag` (two copies of the 3-dim adjoint/spin-1
representation). Independent Casimir recomputation via CH2016's own formula
`rho_m(Cas_h) = -(1/2)m(m+2)` gives `-4` for `V2`, matching CH2016's stated
single eigenvalue on `m*_C` exactly.

**Step 2 — determining `m^{1,0}`:** CH2016 page 18 states explicitly, in its
own words: "the almost complex structure sends `X_i` to `Y_i` and `Y_i` to
`-X_i`" for its own basis `X_i, Y_i` of `m` (two real copies of the adjoint).
This directly gives the `+i`-eigenspace: `Z_i := X_i - i*Y_i` satisfies
`J(Z_i) = Y_i + i*X_i = i*Z_i`, so `m^{1,0}` is spanned by `{Z_i}`, a SINGLE
copy of `V2` (since `X_i, Y_i` transform identically under `ad(su(2))`).
`Lambda^3(V2)` (the 1-dimensional top wedge of the 3-dim adjoint/vector rep
of `so(3)`) is the standard Levi-Civita-tensor invariant — `SO(3)`-trivial,
confirmed (`lambda3_m10_is_trivial: True`).

**Step 3 — Route-C crux:** `Lambda^2(m^{1,0}) = Lambda^2(V2) = V2` (standard
fact: the antisymmetric square of the 3-dim vector/adjoint rep of `so(3)` is
isomorphic to itself, via the cross product). Full tensor square:
`V2 (x) V2 = V0 (+) V2 (+) V4` (standard `SU(2)` Clebsch-Gordan,
`spin1 (x) spin1 = spin0 (+) spin1 (+) spin2`). **This DOES contain `V0`
(the isotropy-trivial representation)** — `contains_trivial: True`.

**This is the OPPOSITE finding from S6 and `SU(3)/T^2`.** For both of those
spaces, the corresponding tensor square structurally excludes an
isotropy-trivial component, which is exactly what FORCES `<w, Term2(v_b)> = 0`
by weight/representation arithmetic alone, with no need to compute Term2's
actual coefficient. For `S^3xS^3`, an isotropy-trivial SLOT IS available in
`Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` — so the simple argument does **not**
force `Term2 = 0`. This does **not** mean `Term2 != 0` is established either
— only that the cheap representation-theoretic shortcut that settled the
question outright for the other two spaces does not settle it here. Deciding
the actual sign/value of `Term2` on `S^3xS^3` would require the explicit
torsion 3-form / Nomizu-connection structure constants for this specific
coset (CH2016 does give an explicit basis, `X_i = (1+sqrt2)J_i,
(1-sqrt2)J_i, -2J_i`, `Y_i = sqrt6(J_i,-J_i,0)`, page 18 — usable in a FUTURE
round, but reconstructing the exact connection/curvature formula and
re-implementing Round 65's full `Term1`/`Term2` bookkeeping for a
non-abelian, differently-normalized isotropy group is a genuinely NEW,
non-trivial derivation step, not a substitution into already-proven general
formulas the way the crux check above was) — **out of this session's scope**,
per the pre-registered kill criterion.

**Step 4 — isotropy-Schur bound (Lemma B analog):** `S^- = m^{1,0}(+)1 =
V2(+)V0`. Trivial multiplicity: exactly 1 (from the explicit `V0` summand;
`V2` — spin-1, dim 3 — has no `SU(2)`-invariant vector). **`dim ker <= 1`,
same bound as S6, `SU(3)/T^2`, and CP3.** This part of the finding is
INDEPENDENT of the Route-C crux-step outcome and holds regardless.

**Part B verdict: INCONCLUSIVE-BY-ROUTE-C** (not STRUCTURAL-NULL — the crux
argument does not force vanishing OR non-vanishing; it simply does not apply
the same way it did for the other two spaces). The isotropy-Schur bound
(Lemma B analog) independently holds and is reported as a genuine, robust
finding regardless of the Route-C outcome.

---

## Euler characteristics (script `part_euler_characteristics()`, general
## Chern-Gauss-Bonnet fact: `c_3(T^{1,0}M) = chi(M)` for any almost-complex
## 6-manifold — no new derivation, standard characteristic-class theory)

| Space | chi(M) |
|---|---|
| S6 | 2 |
| S3xS3 | 0 (`chi(S3)^2 = 0*0`, Kunneth product formula) |
| CP3 | 4 (`chi(CP^n) = n+1`) |
| SU(3)/T^2 (flag manifold) | 6 (`chi(G/T) = \|Weyl(G)\|`, `\|W(SU(3))\| = 3! = 6`) |

**This is a necessary, NOT sufficient, ingredient for a full Atiyah-Singer
index** (G73's own index computation for S6 needed BOTH `c_3(S^-) = chi(S^6)`
AND `Â(S^6) = 1`, which itself required `H^4(S^6) = 0`; the FULL index
formula `ind = integral[Â(TM) . ch(S^-)]` needs the complete Chern character
of `S^-`, i.e. also `c_1`, `c_2`, not just `c_3`). Computing this fully for
CP3 (`H^4(CP^3;Z) = Z`, nonzero — unlike S6 and S3xS3 where `H^4 = 0` — so
`Â(CP^3)` genuinely requires `p_1(CP^3) = 4h^2 != 0` to be tracked, not
simply `=1` by the `H^4=0` shortcut G73 used) is explicitly **out of scope**
for this round. `chi(S3xS3) = 0` is at least CONSISTENT WITH (not proof of) a
vanishing index via this specific mechanism, reinforcing the Route-C
INCONCLUSIVE finding above (a second, independent hint pointing the same
direction for `S3xS3` — less topologically favorable than the other three
spaces on this axis); `chi(CP3) = 4 != 0` is at least NOT excluded, consistent
with the Route-C PASS above. Neither Euler-characteristic fact alone proves
anything about `dim ker`.

---

## Lichnerowicz-norm-bound / Kostant-Parthasarathy (L4A/L4B analog) — explicitly OUT OF SCOPE, reported qualitatively only

This project's OWN internal audit (`experiments/20260708-dolan-casimir-g2su3/`,
21 rounds) found the Kostant-Parthasarathy Casimir-difference formula is a
THEOREM only for Kostant's cubic Dirac operator (`t=1/3`), NOT proven for the
physically-relevant Levi-Civita operator (`t=1/2`) used throughout
`preprint.tex` — and separately documents an unresolved numerical tension
between the original norm-bound estimate (`8/45`) and a later, more careful
direct computation (`~1.03`) on the SAME S6 reference case
(`preprint.tex` \S\ref{sec:schur}, "Caveat: which Dirac operator this argument
proves invertibility for"). Given this project's own reference case is not
yet settled, this round does NOT attempt to produce a calibrated, exact
Lichnerowicz/Kostant-Parthasarathy number for CP3 or S3xS3 — doing so would
require (a) resolving the S6 tension first, and (b) re-deriving the
normalization conversion between CH2016's own B-form-based Casimir
normalization and this project's physics-normalized convention (`C_2(SU(3)
fund) = 4/3`) for TWO NEW ambient/isotropy group pairs (`Sp(2)`/`Sp(1)xU(1)`
and `SU(2)^3`/`SU(2)`) — the ratio between CH2016's Cartan-Killing-based `B`
normalization and this project's own physics-normalized convention is a
group-dependent quantity (fixed by each Lie algebra's own dual Coxeter
number / trace normalization, which is NOT the same across `SU(3)`, `Sp(2)`,
and `SU(2)`), so the single conversion factor found for the S6/`SU(3)` case
(`4/(4/3)=3`) cannot simply be reused for the other two isotropy groups
without an independent re-derivation per group. This is
comparable in scope to a meaningful fraction of the original 21-round
`dolan-casimir-g2su3` investigation — matching Round 51's own cost re-estimate
that a full L4A/L4B-equivalent derivation for the remaining spaces is
"comparable in scope to the original L4A/L4B derivation itself... not a
30-minute follow-on."

For transparency, CH2016's own internally-consistent Casimir data (their OWN
units, not calibrated to this project's convention) is recorded here as a
directional-only data point, from the primary-source pages already
transcribed above: ambient-group Casimir eigenvalues (`Cas_g`) are tabulated
by CH2016 for `SU(2)^3` (page 14: smallest non-trivial value `-9/2` at
`(1,0,0)`) and `Sp(2)` (page 19: smallest non-trivial value `-5` at `(0,1)`),
against isotropy-fibre Casimir values (`Cas_h = -4` on the relevant `S^-`
component for both spaces, computed above). No claim is made about what these
numbers mean for the physically-relevant operator — this is explicitly
flagged as a non-actionable data point pending the S6 reference-case
resolution.

---

## Kill Analysis (OSA — required for the Part B non-PASS verdict)

**What was killed:** The hope that Route C's SPECIFIC "no-singlet-in-
`Lambda^2(x)Lambda^2`" shortcut trivially generalizes to `S3xS3` the same way
it did for `SU(3)/T^2`. This is killed cleanly: `V2(x)V2 = V0(+)V2(+)V4`
DOES contain the trivial representation, an exact, computed,
non-ambiguous fact (standard `SU(2)` Clebsch-Gordan), unlike the other two
spaces checked so far.

**What was NOT killed:**
- The isotropy-Schur bound (`dim ker <= 1`) — this holds independently for
  `S3xS3`, using only the trivial-summand-counting argument, unaffected by
  the Route-C crux-step outcome.
- The POSSIBILITY that `Term2` still vanishes on `S3xS3` by an ACCIDENTAL
  (non-representation-theoretically-forced) cancellation — this round's
  method cannot distinguish "no available slot" (S6, `SU(3)/T^2`, CP3) from
  "slot available but coefficient happens to be zero" (an open possibility
  for `S3xS3`) from "slot available and coefficient is nonzero" (the other
  open possibility). All three remain live until the explicit torsion/Nomizu
  computation is done.
- CH2016's own explicit basis for `m` on `S3xS3` (`X_i`, `Y_i` in terms of
  `J_i`, page 18) — directly reusable as a starting point for that future
  computation, not re-derived from scratch here.

**Relaxation Map (one assumption at a time, per the Minimal Relaxation
Rule):** the ONE relaxation that would resolve Part B's INCONCLUSIVE status
is: replace "check whether an isotropy-trivial slot EXISTS in
`Lambda^2(x)Lambda^2`" (this round's cheap necessary-condition check) with
"compute the ACTUAL value of `Term2`'s coefficient on that slot, using the
canonical connection's explicit Nomizu formula for `S3xS3`'s own basis" (a
genuinely new derivation, not a substitution into an already-proven general
formula) — this is the SAME kind of escalation Round 51 already correctly
scoped as comparable to the original multi-round L4A/L4B derivation, now
narrowed specifically to the `Term2` coefficient rather than the full
Lichnerowicz-norm-bound machinery (a smaller, but still non-trivial, future
step).

---

## Pearl Gate scan (mandatory, per Falsification Ladder)

**Unexpected but testable insight:** the three spaces split 2-1 on the
Route-C crux step (S6, `SU(3)/T^2`, CP3 all PASS; `S3xS3` alone has an
available singlet slot) in a pattern that correlates exactly with which
spaces have `H^4(M) = 0` vs `H^4(M) != 0`... actually the correlation that DOES
hold cleanly is with `chi(M)`: the three PASS spaces have `chi != 0`
(`2, 6, 4`) while the one INCONCLUSIVE space has `chi = 0`. This is a
falsifiable, checkable pattern-candidate (not yet elevated beyond a
candidate): **does "isotropy-trivial slot absent in `Lambda^2(m^{1,0})(x)
Lambda^2(m^{1,0})`" correlate with (or follow from) "`chi(M) != 0`" for
homogeneous nearly-Kahler 6-manifolds in general?** This is recorded as a
`[CANDIDATE]` pearl (impact_score 4/10 — narrow, affects only how this
project frames the Route-C mechanism's domain of applicability, not the
project's core claims) rather than promoted, since `n=4` spaces is too small
a sample to distinguish a real structural link from coincidence, and no
mechanism connecting `chi(M)` (a purely topological invariant of `M`) to a
representation-theoretic fact about `Lambda^2(m^{1,0})` has been identified —
`next_check`: if a 5th homogeneous (or even non-homogeneous) nearly-Kahler
example is ever checked by this project, re-test this correlation then.

---

## What this does NOT mean (carried from claim.md, unchanged)

- A PASS verdict on Route C for CP3 does NOT establish `dim ker=1` for the
  physically-relevant Levi-Civita twisted Dirac operator — see the explicit
  L4A/L4B out-of-scope section above.
- The INCONCLUSIVE verdict for `S3xS3` does NOT mean Universality fails there
  — only that this specific, cheap mechanism does not decide it.
- Neither verdict touches or overturns S6's own established `N_gen=3` result
  (G73, G74A) or `preprint.tex`'s own open caveats about the Levi-Civita vs
  cubic-Dirac tension for S6 itself.
- This round does NOT edit Round 64's `decision.md` — the correction to its
  framing is recorded here only, per the task's explicit constraint.

---

## Files

- `claim.md` — frozen before this round's computation.
- `round70_universality_check.py` — from-scratch verification script:
  independent Casimir recomputation for `SU(2)_diag` and `Sp(1)xU(1)`
  isotropy (cross-checked against CH2016's own stated values), `Lambda^3`-
  invariance-based determination of `m^{1,0}`, `Lambda^2(x)Lambda^2`
  singlet check (Route-C crux), isotropy-Schur bound, Euler characteristics.
- `run_output.txt` — actual run output; every number in this decision traces
  to this file, none hand-typed independently of it.
