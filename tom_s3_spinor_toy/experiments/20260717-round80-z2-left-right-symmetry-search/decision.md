# E14 (round80) — Decision

**Date:** 2026-07-17
**Verdict:** `PASS_GEOMETRIC_Z2_CONFIRMED__PHYSICAL_MECHANISM_STILL_OPEN`
**Go/no-go:** The geometric half of the hypothesis (Sections A-C: `iota: g -> g^{-1}`
is a genuine isometry of `S^3` that exchanges left- and right-invariant structure,
and pulls back the WHOLE Cartan-Schouten connection family `Nabla^t` to `Nabla^{1-t}`
exactly, not merely at `t=0,1`) is **PASS, tool-verified, a real strengthening of
E7**. The physical half (Section D: does this force BOTH `t=0` and `t=1` to be
simultaneously present, closing E12/E13's multiplicity gap) is **NOT established** —
on the two most concrete ways this project could operationalize "requiring
invariance under this Z2," both point AWAY from the hoped-for doubling, not toward
it. This is reported as the honest, expected-to-be-hard outcome the task
anticipated, not a forced resolution.

## Bottom line, stated plainly first

**Geometric fact, new to this project, tool-verified:** `iota(g):=g^{-1}` on
`S^3=SU(2)`, concretely `Phi(x0,x1,x2,x3)=(x0,-x1,-x2,-x3)` on the unit quaternion
model this project already uses, is (a) an isometry of the round metric, (b) an
exact realization of the abstract group-inversion map (`Phi(x)` literally equals
the coordinates of `g(x)^{-1}`), (c) a map that sends the left-invariant frame
`{Z_i^L}` to `{-Z_i^R}` and vice versa (exact vector-field pushforward identity,
all `i`), and (d) — combining (a)-(c) with one new computed identity (Section C) —
pulls back the Cartan-Schouten torsion tensor `T^t` to `T^{1-t}` EXACTLY, for
**every** `t`, not just `t=0,1`. Since the shared Levi-Civita part of the family is
pulled back to itself (isometry), this gives `iota^*(Nabla^t) = Nabla^{1-t}` as an
honest operator identity on the whole connection family — a genuine strengthening
of E7's `t(t-1)`-curvature-formula symmetry (which only showed the algebraic
*eigenvalue equation* is symmetric under `t<->1-t`) to an actual geometric map
realizing that symmetry.

**Physical fact, explored honestly, not established:** this does **not**, on
either of the two concrete readings tried here, supply a mechanism forcing BOTH
`t=0` and `t=1` to be simultaneously present. One reading argues for
*under*-counting (only one sector should be counted, the other being a relabeling
of the same physics); the other reading (gauging `iota` as an orbifold
identification) collapses the connection back to `t=1/2` — the Levi-Civita,
torsion-free, zero-mode-free value the entire torsion-escape-route program exists
to avoid. A third, more speculative reading (borrowing "both L and R doublets
required by parity" from Left-Right-symmetric model building) is flagged but shown
to sit in tension with this project's own established, explicitly ASYMMETRIC
chirality mechanism (Lemma L5, `preprint.tex:884-912`). **E12/E13's multiplicity
gap is not resolved by this experiment.**

## Section A — isometry, verified [VERIFIED-tool]

Script: `e14_z2_left_right_symmetry.py`, `run_part_a`. Realizing `S^3=SU(2)` via
this project's own `g(x)=x0*I+x1*Z1+x2*Z2+x3*Z3` (`Z_i=i*sigma_i`, identical to
E9/round76), and `Phi(x):=(x0,-x1,-x2,-x3)`:

```
J = diag(1,-1,-1,-1)          (constant Jacobian of Phi, Phi is linear)
isometry_check_JtJ_eq_I        = True
Phi_maps_sphere_to_itself       = True
Phi_realizes_group_conjugate_gbar = True   (g(Phi(x)) == gbar(x), exactly)
g_times_gbar_equals_norm2_I     = True     (re-verified, self-contained)
det(J)                          = -1        (orientation-REVERSING)
fixed points on S^3             = {(x0,0,0,0,) : x0 = +-1}   (exactly 2)
```

`J^T J = I` is the direct statement that `Phi` pulls back the ambient flat `R^4`
metric to itself (hence the induced round metric on `S^3` to itself) — this is the
complete, elementary content of "`Phi` is an isometry" for a linear map of a sphere
embedded in Euclidean space, verified here rather than merely cited. Separately,
`g(Phi(x))` (literal substitution into the SAME formula this project uses for
`g(x)`) is checked to equal `gbar(x)` exactly — this is what licenses calling
`Phi` "the concrete coordinate realization of group inversion," not merely an
analogous-looking sign flip: since `g(x)*gbar(x)=|x|^2*I` (re-verified here,
originally established in round76), on the unit sphere `gbar(x) = g(x)^{-1}`
exactly, so `g(Phi(x)) = g(x)^{-1}` literally.

`det(J)=-1`: `Phi` is **orientation-reversing** on `S^3`. Combined with
`preprint.tex:274,279,422` (`Iso(S^3\times S^6) = SO(4)\times SO(7)`, and the
paper's gauge group `SU(2)_L\times SU(2)_R\times SU(3)_c` is built from this
CONNECTED isometry group), `iota` lies in the **disconnected** component
`O(4)\SO(4) \cong Z_2` — i.e. `iota` is a genuinely NEW discrete symmetry, not
already contained in, or overlapping with, the continuous `SO(4)` gauge symmetry
this project already uses. This is a structural point worth recording precisely:
the paper's own gauge group construction explicitly restricts to the connected
component, so `iota` sits outside anything currently gauged.

Two fixed points on `S^3`: `g=+1` and `g=-1` (the group identity and its
antipode). This is load-bearing for Section D's orbifold-descent discussion below.

## Section B — frame exchange, verified [VERIFIED-tool]

Script: `run_part_b`. Since `Phi` is linear, its pushforward at any point is just
"apply the constant Jacobian `J` to the vector field's coordinate values." Checked,
for `i=1,2,3`, both directions, as an **exact symbolic identity in `x0..x3`** (not
a numerical spot-check):

```
J * X_i^L(x)  ==  -X_i^R(Phi(x))     for all i          [all_L_to_minus_R_ok = True]
J * X_i^R(x)  ==  -X_i^L(Phi(x))     for all i          [all_R_to_minus_L_ok = True]
```

i.e. `iota` sends the left-invariant frame to (minus) the right-invariant frame
and vice versa, exactly. This directly answers the task's step 2 ("does this map
send left-invariant vector fields to right-invariant vector fields") — done here
by explicit computation on this project's own concrete Pauli/quaternion
realization, not by citing the general Lie-theory fact (`d(iota)_g(V) =
-g^{-1}Vg^{-1}` for a matrix Lie group, which predicts exactly this result and is
consistent with it, but was not the thing computed — the computation used the
ordinary vector-field pushforward under the concrete linear coordinate map
`Phi`, ties directly to E9/round76's own frame conventions).

## Section C — connection swap, verified [VERIFIED-tool]

Script: `run_part_c`. This is the deepest new computation, directly answering the
task's step 3 ("does pulling back `Nabla^t` under this map give `Nabla^{1-t}`
exactly... checked directly on the frame/structure constants, not just asserted").

**The reduction used (documented here; each input is separately tool-verified, the
combination itself is direct algebra, not a new computation):**

1. `Nabla^t = Nabla^{LC} + (1/2)*T^t`, where `T^t(Zi^L,Zj^L) := (2t-1)*c0*eps(ijk)*Zk^L`
   is the torsion tensor. **Verified** (`torsion_formula_T_t_eq_2t_minus_1_c0_eps_verified
   = True`): computed directly from this project's own `Christoffel_left(t)(i,j,k) =
   t*c0*eps(ijk)` via `T^t(Zi,Zj) := Gamma(i,j,k) - Gamma(j,i,k) - c0*eps(ijk)`
   (the torsion-tensor definition applied to the frame) and confirmed it equals
   `(2t-1)*c0*eps(ijk)` exactly, for all `i,j,k`.
2. `iota^*(Nabla^{LC}) = Nabla^{LC}`: since the Levi-Civita connection is the
   UNIQUE metric+torsion-free connection for a given metric, and Section A shows
   `iota` pulls the metric back to itself, it pulls the (unique) LC connection back
   to itself too. (Not a separate symbolic computation — a direct logical
   consequence of Section A's isometry result plus the standard uniqueness
   theorem for the Levi-Civita connection; both premises are tool-verified.)
3. **The new computational ingredient**, needed to determine how `T^t` pulls back:
   `T^t(Zi^R,Zj^R)` (the SAME tensor `T^t`, now evaluated on the right-invariant
   frame, via the ONLY consistent way to do this — tensorial extension using the
   `b^j(x)` coefficients that express `Zi^R` in the `{Zj^L}` basis, generalizing
   round76 Part 3's single representative case `k=0` to all `k=0,1,2` here) reduces
   algebraically to checking:
   ```
   sum_{k,l} b_i^k(x) b_j^l(x) eps(k,l,m)  ==  sum_p eps(i,j,p) b_p^m(x)
   ```
   ("cross product of two SO(3)-rotated basis vectors is the rotation of their
   cross product," specialized to this project's own concrete `b(x)` functions).
   **Verified exactly** for all 27 combinations of `i,j,m in {1,2,3}`
   (`all_27_identity_checks_ok = True`) — including the 9 diagonal (`i=j`) cases,
   which come out trivially `0=0` on both sides and were checked anyway, per this
   project's own audit discipline, as a sign-error catch (an error that canceled
   only in the untested cases would not have been caught by checking `i!=j` alone).
   Also re-verified, for all `k=1,2,3` (not just round76's `k=1` representative):
   the `I2`-component of the scaled conjugation vanishes identically
   (`all_i2_zero = True`) and the reconstruction of `Zk^R` from the `b^k_j(x)`
   coefficients exactly reproduces Part B's independently-computed `X_k^R`
   (`all_reconstructions_ok = True`) — both are consistency controls on the `b(x)`
   functions themselves, not the main claim.
4. Combining 1-3 by direct algebra (not a further computation): this identity gives
   `T^t(Zi^R,Zj^R) = (2t-1)*c0*eps(ijl)*Zl^R` exactly (position-independent — the
   apparent position-dependence of the individual `b^j(x)` cancels exactly via the
   identity in step 3). Applying the pullback definition
   `(iota^*T^t)(Zi^L,Zj^L) := d(iota)^{-1}[T^t(d(iota)(Zi^L), d(iota)(Zj^L))]`, using
   Section B's `d(iota)(Zi^L)=-Zi^R` (so the two minus signs cancel inside `T^t`,
   which is bilinear over constants) and `d(iota)^{-1}(Zl^R) = -Zl^L` (the same
   relation, since `iota` is an involution):
   ```
   (iota^*T^t)(Zi^L,Zj^L) = -(2t-1)*c0*eps(ijl)*Zl^L = (1-2t)*c0*eps(ijl)*Zl^L
                          = (2(1-t)-1)*c0*eps(ijl)*Zl^L = T^{1-t}(Zi^L,Zj^L).
   ```
   **`iota^*(T^t) = T^{1-t}` exactly, for all `t`.** Combined with step 2
   (`iota^*(Nabla^{LC})=Nabla^{LC}`) and step 1's `Nabla^t = Nabla^{LC}+(1/2)T^t`:
   ```
   iota^*(Nabla^t) = Nabla^{LC} + (1/2)*iota^*(T^t) = Nabla^{LC} + (1/2)*T^{1-t}
                    = Nabla^{1-t}.
   ```

**This is the operator-level identity the task's step 3 asked for.** It is
strictly stronger than what was previously known: E7 (round72) showed the
CURVATURE (an algebraic consequence, `t(t-1)`) is symmetric under `t<->1-t`;
this experiment shows there is an actual, concrete, tool-verified DIFFEOMORPHISM
(`iota`, realized as `Phi`) that IMPLEMENTS this symmetry as a genuine geometric
map on the connection itself, for the whole family, not merely at the two
zero-mode-relevant values.

## Section D — search for existing use in this project [VERIFIED-tool, grep]

Grepped `preprint.tex` (full text) for "parity", "reflection", "involution",
"orientation-reversing", "inversion", "antipodal", "CPT" (case-insensitive):

- "parity"/"reflection"/"involution"/"orientation-reversing"/"antipodal": **0
  hits, anywhere in the paper.**
- "inversion": 1 hit (`preprint.tex:389`, "a formal one-loop inversion" — an
  unrelated renormalization-group concept, not a geometric map).
- "CPT": 1 hit (`preprint.tex:298`, "plus their CPT conjugates" — per E13
  (round79), this doubling is carried entirely by the S6 factor's B-L sign, not
  by any S3-side involution; E13 already ruled out identifying this with the
  S3-side doublet structure).

**No existing construction in this project invokes `iota`, or any analogous S3
involution, anywhere.** The only pre-existing discrete (`Z2`) choice in this
project's chirality mechanism is a DIFFERENT one: `preprint.tex:884-912` (Lemma
L5) fixes chirality "up to a single `Z2` choice: the orientation of `S^6`" — this
is a `Z2` acting on the S6 FACTOR's orientation, structurally unrelated to the
`iota` studied here (which acts on the S3 factor). The two `Z2`'s are not shown,
and not obviously expected, to be the same or linked.

## Section E — does this force BOTH t=0 and t=1 to be present? [interpretive, honest exploration, no forced verdict]

This is the hard part the task explicitly anticipated might not close. Three
readings were tried; none succeeds in supplying the hoped-for mechanism.

**Reading 1 — "same physics, different labels."** If `t=0` (torsion connection)
and `t=1` (its `iota`-image) describe the SAME physical configuration, merely in
two different, isometry-related coordinate descriptions, then there is no
"selection problem" at all (asking "why does nature pick `t=0` over `t=1`" would
be as physically empty as asking why it picks left-handed over right-handed
coordinates for the SAME object) — but this reading argues for **UNDER**-counting,
not doubling: the `ker(D^0)` (2-dim) and `ker(D^1)` (2-dim) would be the SAME
physical states described twice, giving 2 states total, not 4. This makes E12's
multiplicity gap WORSE relative to the `4` needed (per E13's G6 cross-check), not
better.

**Reading 2 — "gauge `iota` as an orbifold identification `S^3/<iota>`."** In
string/orbifold constructions, projecting by a geometric `Z2` and adding
"twisted sectors" is the standard mechanism for getting NEW states beyond the
naive quotient. Checked directly here (Section A + `run_part_d`): `iota` has
exactly 2 fixed points on `S^3` (`g=+-1`), so `S^3/<iota>` would be a genuine
orbifold with 2 singular points — a real candidate structure. **But**: for a
SINGLE torsion connection to descend consistently to this quotient (i.e. be
`iota`-invariant, `iota^*(Nabla^t)=Nabla^t`), Section C's result requires
`t = 1-t`, i.e. **`t=1/2` uniquely** (`run_part_d`: `t_star_is_one_half = True`).
`t=1/2` is exactly the Levi-Civita, TORSION-FREE connection — the one this
project's own Lichnerowicz-obstruction argument (KT-8, `preprint.tex`) already
shows has NO zero modes at all. **Gauging `iota` as an orbifold identification, if
anything, collapses the torsion family back to the value that KILLS the entire
escape-route mechanism, rather than doubling the surviving zero-mode count.** This
is a clean, decisive (if negative) finding: the most natural way to "require
invariance under this `Z2`" as an actual geometric identification is
incompatible with keeping `t != 1/2`.

**Reading 3 — "Left-Right-symmetric model building requires both doublets."**
Borrowing from Left-Right-symmetric extensions of the Standard Model (which this
project's own Pati-Salam framing is adjacent to, `preprint.tex:273-279`), one
might argue that DEMANDING the theory be invariant under a discrete `L<->R`
parity (which `iota` geometrically realizes for the S3 factor specifically)
motivates keeping BOTH `SU(2)_L`- and `SU(2)_R`-doublet content, exactly as
parity-symmetric model-building keeps both `L` and `R` fermion multiplets present
(until the parity is spontaneously broken). This is the reading CLOSEST to
supplying what E12/E13 need — but it is flagged here as a MODEL-BUILDING CHOICE
("build a parity-symmetric extension"), not something the geometry alone forces,
and it sits in direct, unreconciled tension with this project's OWN established
mechanism: Lemma L5 (`preprint.tex:884-912`) derives an explicitly ASYMMETRIC,
non-parity-symmetric chirality result for the S6 factor (`sign(ind)=+1` forces a
LEFT-HANDED EXCESS, fixed by the S6 orientation choice, not by any doubling). If
this project wanted to invoke "parity requires both sectors" for the S3 factor,
it would need to explain why the SAME logic does not apply to, or is somehow
different for, the S6 factor's own already-fixed, asymmetric chirality mechanism
— a reconciliation this experiment surfaces but does not attempt.

**Conclusion of Section E:** none of the three readings closes the gap in the
direction E12/E13 need. Readings 1 and 2 point toward under-counting or collapse
to the zero-mode-free value; Reading 3 is the only one pointing the right
direction, but is a phenomenological choice in tension with an already-established
part of this project's own construction, not a consequence of the geometry alone.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the possibility that "`t=0` and `t=1` are related
  only by an abstract algebraic symmetry of the eigenvalue/curvature formula, with
  no concrete geometric realization" — that specific, weaker claim is now false;
  a genuine isometry realizing the swap exists and is tool-verified, for the WHOLE
  family. It also kills, specifically, the naive "gauge `iota` as an orbifold"
  reading as a route to the needed doubling (Reading 2 above) — this is a genuine,
  decisive negative sub-result, not merely "unexplored."
- **What this result does NOT kill:** H1c (which of `t=0`/`t=1` is physically
  selected, if either) remains exactly as open as E7/E9/E10/E11 left it. KT-8 (no
  zero mode of the untwisted `D_full` exists at all) is untouched. E12/E13's
  6-vs-3 multiplicity gap is untouched — this experiment does not change the
  zero-mode COUNT at any fixed `t`, only how the `t`-family transforms under one
  specific discrete isometry.
- **What survives, confirmed stronger than before:** the `t<->1-t` symmetry is now
  known to be a genuine geometric fact (an actual isometry realizing it, verified
  on the connection/torsion level for the whole family), not merely an algebraic
  coincidence of the curvature eigenvalue formula. This is a real, if modest,
  strengthening of E7, independent of whether it ever supplies a physical
  selection or multiplicity mechanism.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Reconcile Reading 3 with Lemma L5's asymmetric S6 mechanism | Either find an independent reason parity-symmetric model-building applies to S3 but not S6, or abandon Reading 3 |
| Explicit spin-lift check | This experiment verified the AFFINE-connection-level (torsion/frame) pullback identity; a full spin-connection-level check (`Omega_i(t)` transforming to `Omega_i(1-t)` under the spin lift of `iota`) was NOT separately computed — flagged as [INFERRED] (standard consequence of the affine result via the canonical spin lift of SO(3) to Spin(3)=SU(2)), not independently verified here |
| A genuinely different candidate mechanism for the E12/E13 gap | Neither this experiment nor E12/E13 have found one; per E12's own Relaxation Map, the "reconcile 32-state vs zero-mode-kernel frameworks" question remains the recommended next-cheapest step, independent of this experiment's Z2 exploration |

## Assumptions carried, unresolved

- `SU(2)_L`=left-translation / `SU(2)_R`=right-translation convention (E11's
  import, `preprint.tex` never states this) is NOT needed for Sections A-C (which
  are convention-independent, symmetric statements about `iota`), but WOULD be
  needed if Reading 3 were pursued further (to say which doublet is "the" L one).
- The `c0=-2` vs abstract `c=+2` sign gap (round76) does not affect Sections A-C:
  the torsion-swap derivation used `c0` symbolically throughout (never substituted
  a specific numeric value beyond what `find_structure_constant` returns from the
  concrete realization itself), so the result holds regardless of which sign
  convention for the abstract physics-calibrated `c` this project ultimately
  adopts — this is a genuine robustness of the geometric result, not a coincidence
  of picking the "right" sign.
- Section E's three readings are not claimed to be exhaustive — a different,
  not-yet-conceived fourth reading might still succeed; this experiment reports
  what was tried, not a proof that no mechanism can exist.

## What this does NOT mean

1. Does **not** establish H1c (physical selection between `t=0` and `t=1`) —
   untouched.
2. Does **not** resolve KT-8 (whether ANY zero mode of the untwisted `D_full`
   exists) — untouched.
3. Does **not** resolve E12/E13's multiplicity gap (6 vs. 3 internal zero modes)
   — Section E's three readings all fail to supply the needed doubling mechanism;
   two of them argue in the OPPOSITE direction (under-counting, or collapse to
   `t=1/2`).
4. Does **not** claim this isometry is already used anywhere in `preprint.tex` —
   Section D confirms, by direct grep, that it is not.
5. Does **not** claim the general-`t` connection-pullback result (Section C) was
   previously known in this project — E7 established only the curvature-eigenvalue
   algebraic symmetry; this experiment is the first to realize it as an actual
   diffeomorphism-level operator identity, for the whole family.
6. Does **not** perform the full spin-connection-level pullback check (only the
   affine/torsion level) — flagged explicitly in the Relaxation Map above.

## Check (reproduces this decision)
`python e14_z2_left_right_symmetry.py` →
`verdict.core_a_pass==true`, `verdict.core_b_pass==true`,
`verdict.core_c_pass==true`,
`verdict.label=="PASS_GEOMETRIC_Z2_CONFIRMED__PHYSICAL_MECHANISM_STILL_OPEN"`.
