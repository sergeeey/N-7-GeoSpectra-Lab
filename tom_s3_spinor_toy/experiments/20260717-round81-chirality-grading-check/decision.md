# E15 (round81) — Decision

**Date:** 2026-07-17
**Verdict:** `NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE`
**Go/no-go:** This is a **clean, decisive NEGATIVE result** for one specific,
concretely-nameable candidate mechanism from E12's own Relaxation Map ("new
projection specific to the S3 factor"). It is reported as found, exactly as
the task anticipated might happen (the Pauli identity `sigma_x sigma_y
sigma_z = i*I` was flagged in advance as a real possible outcome) — no
resolution is forced. E12/E13's multiplicity-2 excess remains open.

## Bottom line, stated plainly first

The natural S3 Clifford volume element `omega := Z1.Z2.Z3` (this project's
own `Z_i = i*sigma_i` convention, used throughout E2/E9/E10/E12) is **exactly
the 2x2 identity matrix** — `omega = I2`, `scalar_value = 1` — confirmed by
independent re-derivation in this experiment (not by citing E2's own,
differently-motivated computation of the same object). It is central
(commutes with `Z1`, `Z2`, `Z3` individually), has a **single** eigenvalue
(`+1`, algebraic multiplicity 2, eigenvectors spanning the whole of `C^2`),
and consequently acts as `lambda=1` on **every** vector in the E12 kernel —
both the fully generic `(a,b)` at `t=0` and the fully generic
`gbar(x)*(a_,b_)` family at `t=1` — with no exception, no splitting, and no
`x`- or frame-dependence. **This specific candidate mechanism for reducing
the doublet to a single physical state is ruled out, cleanly, for a specific,
understood structural reason** (Section C below), not by a computational
accident.

## Result, section by section

### Section A — independent re-derivation of omega [VERIFIED-tool]

Script: `e15_chirality_grading_check.py`. Rebuilt `Z_i = i*sigma_i` from
scratch (Pauli matrices, same convention as E2/E9/E10/E12 but not imported
from any of their modules), re-verified `{Z_i,Z_j} = -2*delta_ij*I2` exactly
for all 6 pairs (`step1_clifford_relations.all_ok = true`), then computed
`omega = Z1.Z2.Z3` independently:

```
omega = Matrix([[1, 0], [0, 1]])          (exactly I2, scalar_value = 1)
omega commutes with Z1, Z2, Z3            (all_central = true)
omega^2 = I2                              (omega_squared_equals_identity = true)
```

This reproduces E2's own finding (`compute_omega_and_check_scalar`,
`experiments/20260717-round67-e2-s3-torsion-deformation/e2_s3_torsion_
deformation.py`) — but E2 computed this for a completely different purpose
(calibrating Kostant's cubic element `H=(3c/2)*omega` inside Agricola's
`D^t` formula, never framing `omega` as a chirality/grading candidate, and
written before the E12 kernel-splitting question existed). Re-deriving it
here, independently, under the explicit new framing "is this a
chirality/grading operator," is the non-trivial contribution of this
section — the two computations agreeing exactly (`scalar_value=1` both
times) is itself a real, falsifiable cross-check (had E9/E10's later frame
conventions introduced any sign or normalization drift relative to E2, this
recomputation would have caught it).

### Section B — exact eigenstructure [VERIFIED-tool]

`sympy .eigenvects()` on `omega` directly, not merely the binary
"proportional-to-identity" flag:

```
n_distinct_eigenvalues = 1
eigenvalue = 1, algebraic multiplicity = 2, eigenvectors = {(1,0), (0,1)}
```

One eigenvalue, full multiplicity 2 — the entire `C^2` is a single
eigenspace. There is no way to select a proper 1-dimensional subspace as
"the omega=+1 sector" versus "the omega=-1 sector," because there is no
`omega=-1` sector: every vector in `C^2` already satisfies `omega*v = v`.

### Section C — action on the actual E12 kernel, both t=0 and t=1 [VERIFIED-tool]

At `t=0`: applied `omega` to the fully generic (symbolic `a,b`, not
spot-checked at `(1,0)`/`(0,1)` alone — same rigor standard E12 itself used)
kernel vector `psi=(a,b)`. Result: `omega*psi = (a,b) = psi` exactly, i.e.
`lambda=1` solves `omega*psi=lambda*psi` identically in `a,b`
(`verdict_kernel_is_single_eigenspace_at_t0 = true`).

At `t=1`: applied `omega` to E10/E12's own right-invariant-frame kernel
family `psi(x) = gbar(x)*(a_,b_)` (fully generic in both the S3 coordinates
`x0..x3` and the spinor components `a_,b_`). Result: the SAME single
`lambda=1` solves `omega*psi_t1(x) = lambda*psi_t1(x)` identically for all
`x` and all `(a_,b_)` simultaneously
(`verdict_kernel_is_single_eigenspace_at_t1 = true`). This is not a
coincidence requiring a separate check — `omega` is a fixed, position- and
frame-independent 2x2 matrix (Section A), so once it is shown to act as the
identity on all of `C^2` (Section B), it necessarily acts as the identity on
**any** subset or twisted image of `C^2`, including both t=0 and t=1's
kernel families and, for that matter, any other spinor field on S3 whatsoever
that this project's Clifford conventions could produce. The t=1 check was
still run explicitly (not skipped as "obviously implied") to catch any
convention mismatch in how `gbar(x)` interacts with `omega` — none was
found.

### Section D — why this outcome is forced, not accidental [DOCS/derivation]

This is not a numerical coincidence specific to this project's normalization
choice. For a real or complex Clifford algebra `Cl(n)`, the volume element
`e_1...e_n` is **central** (commutes with every degree-1 generator) if and
only if `n` is **odd** — a standard structural fact of Clifford algebras
(cited, e.g., in Lawson-Michelsohn "Spin Geometry," already the source this
project's own E9/E10 scripts cite for the spin-connection formula). `n=3`
(S3's own dimension) is odd, so `omega=Z1.Z2.Z3` is guaranteed central by
this general fact — Section A's `all_central=true` computation is the
concrete instance of this. Once an operator is central, and the
representation it acts on (the 2-dimensional Pauli/spinor representation
used throughout this project) is **irreducible** (E11/E14 already
established this doublet is an irreducible SU(2) multiplet, not two
unrelated states), **Schur's lemma forces the central operator to act as a
scalar** on that representation — there is no freedom left for it to do
anything else. This means the NULL result found here was, in a precise
sense, **guaranteed in advance** by (a) S3 being odd-dimensional and (b) the
doublet being irreducible (E14's own finding) — the computation in Sections
A-C confirms this expectation concretely rather than merely asserting it,
and additionally pins down the exact scalar value (`+1`, not merely "some
scalar"), which was not knowable from the abstract argument alone.

This also directly explains why the task's own anticipated possibility (the
Pauli identity `sigma_x sigma_y sigma_z = i*I`) is not a special/lucky
feature of the Pauli representation specifically, but an instance of a
general odd-Clifford-dimension fact that would recur under any 2-dimensional
irreducible realization of `Cl(3)`.

### Section E — side-note: degree-1 (vector-type) elements DO split C^2, but this is not a valid mechanism [VERIFIED-tool, interpretive]

For completeness (not because the task asked about this specifically): a
generic degree-1 Clifford element `alpha*Z1+beta*Z2+gamma*Z3` (e.g. at
`alpha=beta=gamma=1`) has **2 distinct eigenvalues** on `C^2`
(`n_distinct_eigenvalues_at_111 = 2`, `splits_generically = true`). This is
unsurprising — these are ordinary Pauli-type Hermitian traceless matrices,
which always have two distinct eigenvalues for a generic direction.
**This is explicitly NOT a valid chirality/grading candidate**, for a
structural reason, not a matter of taste: a degree-1 Clifford element
transforms as a **vector** under the `SU(2)` action E14 (round80) already
showed acts **irreducibly** on this exact `C^2` doublet — "splitting" via
such an element is basis-dependent (rotate the `SU(2)` frame and the
eigenspaces rotate with it; there is no `SU(2)`-invariant way to prefer one
direction `(alpha,beta,gamma)` over any other), unlike a genuine central
grading operator, whose eigenspaces are basis-independent by construction.
This reproduces, from a completely different angle (Clifford grading rather
than direct representation theory), exactly the obstruction E14/round80
Section E already identified: any attempt to carve a 1-dimensional subspace
out of this doublet either breaks the manifest continuous `SU(2)` symmetry
(this section) or has no natural discrete-grading candidate to do it with
(Sections A-D). Both routes converge on the same wall.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the specific candidate mechanism "the natural
  Cl(3) volume element / chirality-type grading operator built from the
  tensor-product Dirac operator's own Clifford structure splits the E12
  doublet." This is now closed with a structural (not merely computational)
  reason: odd-dimensional Clifford volume elements are central, and Schur's
  lemma forces a central operator to be scalar on an irreducible
  representation — E14 already established the doublet is irreducible.
- **What this result does NOT kill:** E12's own multiplicity-2 finding
  (untouched, independently re-confirmed here as a byproduct of applying
  `omega` to the actual kernel), E14's Z2 isometry result (untouched;
  Section E here in fact reproduces E14's own obstruction from an
  independent angle, strengthening rather than weakening it), and G74A/G74B's
  S6-side results (this experiment does not touch the S6 factor at all — see
  "What this does NOT mean" below on why the Cl(6) volume element is a
  structurally different case, not addressed here).
- **What survives, confirmed stronger than before:** E14's finding that "no
  natural 1-dim invariant subspace exists under the manifest SU(2) symmetry"
  now has independent corroboration from a totally different mathematical
  angle — not merely "the continuous symmetry forbids it" (E14) but also
  "the most natural discrete/Clifford-grading candidate is trivial and
  forbids it too, for a structural reason" (this experiment). Two
  independent obstructions pointing the same direction is stronger evidence
  that the doublet-splitting approach in general (not just this one
  mechanism) is unlikely to succeed than either result alone.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Look outside Cl(3) entirely for a splitting operator | Any operator that splits the doublet must NOT be built solely from the S3 factor's own Clifford algebra (Section D shows this is structurally impossible); it would have to come from elsewhere — e.g. genuinely coupling to the S6 factor's own chirality data (G74B), not merely tensoring with it as `I_{S3} (x) gamma_{S6}` (which, per Section C, reduces to acting purely on the S6 factor and cannot touch the S3-side doublet at all) |
| Revisit whether "1 doublet = 1 generation slot" (E12 Section E.2) is itself the right resolution | Independent of any splitting mechanism — this remains E12's own top recommended next step, untouched by this experiment |
| A genuinely new physical input (reality condition, orbifold projection specific to S3) | No candidate exists yet in this project (E12 Section E.1, E.3); this experiment does not supply one |

## Assumptions carried, unresolved

- This experiment assumes the D_full tensor-product-Dirac-operator form and
  the E12/E14 kernel bases exactly as those experiments established them; it
  does not re-derive or re-examine the `D_full^2 = D_{S3,t}^2 (x) I +
  I (x) D_{S6,twisted}^2` decoupling assumption (carried as E12's own
  unresolved `[INFERRED, NOT independently literature-verified]` caveat).
- The Schur's-lemma argument (Section D) assumes the doublet's irreducibility
  as established by E11/E14; if a future experiment found the doublet is
  NOT actually irreducible under some other reading, Section D's forced-NULL
  argument would need re-examination (though Sections A-C's direct
  computation would stand regardless, since it does not use irreducibility
  as an input — only as an explanation for WHY the direct computation came
  out this way).

## What this does NOT mean

1. Does **not** prove no chirality/grading mechanism whatsoever can split
   the E12 doublet — only that the S3 factor's OWN Clifford volume element
   cannot, for a specific, general, structural reason (odd-dimensional
   centrality + Schur's lemma). A mechanism that genuinely couples to the
   S6 factor's chirality data (not merely tensoring trivially) is not ruled
   out by this experiment and was not attempted here.
2. Does **not** resolve E12/E13's multiplicity-2 excess (6 vs. 3 internal
   zero modes) — this remains exactly as open as E12/E14 left it.
3. Does **not** touch G74A/G74B's S6-side results — those live on a
   genuinely 6-real-dimensional (even) factor, where `Cl(6)`'s volume
   element is NOT automatically central (odd-vs-even Clifford dimension is
   the whole point of Section D's argument) and can behave very differently
   (indeed, G74B's own chirality operator is exactly this kind of
   S6-side-specific grading, already doing real work there) — nothing in
   this experiment implies or suggests G74B's mechanism is similarly
   trivial; the two cases are structurally different by the dimension
   parity argument itself.
4. Does **not** claim omega's triviality was previously unknown in this
   project — E2 already computed `omega=Z1.Z2.Z3=I2` for a different
   purpose (Kostant cubic element calibration); this experiment's
   contribution is applying that already-known fact to a NEW question (does
   it split the E12 kernel) that did not exist when E2 was written, and
   independently re-deriving it under that new framing rather than merely
   citing E2.
5. Does **not** claim the side-note on vector-type elements (Section E) is
   part of the main claim or kill criterion — it is reported for
   completeness and interpretive value only, not as a tested hypothesis.

## Check (reproduces this decision)
`python e15_chirality_grading_check.py` →
`verdict.omega_is_scalar_times_identity==true`,
`verdict.omega_all_central==true`,
`verdict.omega_single_eigenspace==true`,
`verdict.kernel_splits_at_t0_or_t1==false`,
`verdict.omega_is_trivial_grading_on_C2==true`,
`verdict.label=="NULL_OMEGA_PROPORTIONAL_TO_IDENTITY__NO_SPLITTING_POSSIBLE"`.
