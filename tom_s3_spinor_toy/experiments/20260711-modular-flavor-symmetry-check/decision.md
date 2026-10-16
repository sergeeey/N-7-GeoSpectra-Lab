# Modular-flavor-symmetry decision — REJECT (precondition not met, by construction)

**Date:** 2026-07-11
**Verdict:** REJECT. Neither the (a,N) family nor rho6's actual built potential
has the discrete-duality structure the modular-flavor-symmetry mechanism needs.

## Evidence

1. Grepped whole repo for axion/T-duality/duality/modular/SL(2 -- zero hits
   in any .py file. This ground was never explored (novelty confirmed, not
   itself evidence for or against).

2. (a,N) type mismatch: `a`, `N` are fixed integers (sphere dimensions,
   e.g. a=3, N=6 for our headline case); lambda=a/(a+N) is a DERIVED
   rational number from them. The mechanism requires a continuous field
   that can be tuned arbitrarily close to a critical point -- (a,N) cannot
   be "tuned near" anything, they are discrete choices of which spheres to
   compactify on.

3. rho6's actual potential, read directly from
   `experiments/20260622-g84c-functional-form-degeneracy/g84c_functional_form_degeneracy.py`
   (already-built, already-tested code, no new computation needed):
   `f_inv(rho) = exp(-b*(1/rho**2 - 1/rho0**2))`, rho0=1.090=rho6*.
   Checked directly: under rho -> c/rho for any constant c, the exponent
   1/rho^2 maps to rho^2/c^2 -- NOT the same functional form. No inversion
   symmetry present in this piece of the potential.

## Kill Analysis (mandatory per Anti-Overfitting Gate)

**What this kills:** the specific hope that our EXISTING (a,N)/rho6
construction already carries a hidden SL(2,Z)-like symmetry we simply hadn't
noticed. It does not, by direct inspection of the actual objects involved.

**What this does NOT kill:** the general principle from the literature
(hierarchy via proximity to an enhanced-symmetry point) as a candidate
DIRECTION for a future, deliberately-designed extension. That would require
introducing a genuinely new field (an axion-like partner to rho6, giving a
complex tau = theta + i*rho6) and checking whether ANY natural potential in
our compactification is duality-invariant under a nontrivial discrete group
acting on that tau -- a substantial new construction project, not a
quick follow-up.

**Relaxation map (for a future round, not started):** would require (a)
identifying whether S6=G2/SU(3) or S3 admits a natural axion (e.g. from a
p-form flux Chern-Simons-type coupling), (b) checking what discrete group (if
any) acts on the resulting complex modulus, (c) checking whether our
potential is covariant under it. Each step independently falsifiable;
none attempted here.

**Sub-check on (a), same day:** is either cycle's "flux slot" free for a new
field? S6: NO (H^2=H^4=0, already established by G33/G38/G50's chi-lemma --
the only nontrivial cycle is the top form, already used for the Freund-Rubin
flux, G54-A). S3: also NO -- read directly from
`experiments/20260626-g93-flux-quantization-path/g93_flux_path.py` (existing,
already-tested code): S3's top cycle already carries a quantized flux N3=1,
which IS the source of the existing V_flux_S3 term used since G91. Both
naive "find an empty cycle" routes are closed.

**What survives:** not a free cycle, but a more specific (and harder) question
-- does the EXISTING flux quantum N3 have an associated phase/Wilson-line
degree of freedom (its natural axionic partner in most flux compactifications)
that is a genuine dynamical modulus in our EFT, rather than frozen/eaten? This
is qualitatively different from "find new real estate" and has not been
checked. Flagged for a possible future round, not started here.

## Cost

~25 minutes: grep + read one already-existing, already-tested file. No new
computation, no new tests.

## Relation to GAP-4

Independent question -- GAP-4 (S3-S6 mode mixing, closed 2026-07-11 same day)
concerned whether EXISTING structure could split masses; this concerns whether
a DIFFERENT kind of mechanism (modular symmetry) is already latent in what we
have. Both close NULL, for different structural reasons. Together they narrow
the live options for solving the Yukawa hierarchy: neither "more mixing in the
existing geometry" nor "hidden modular symmetry already present" -- any future
progress needs genuinely new structure, not extensions of what exists.
