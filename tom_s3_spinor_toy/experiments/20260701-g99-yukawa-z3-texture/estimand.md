# Estimand — G99: Z3-triality texture of inter-generation Yukawa couplings

**Date:** 2026-07-01
**FL tier:** Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

## Background

G25 (2026-06-19) proves the Yukawa operator within ONE generation (the
32-state object of G6) has exactly 4 free parameters (Y_nu, Y_e, Y_u, Y_d).
This construction has NO generation/channel index at all -- it is entirely
internal to a single 32-state block.

G73+G74A+G74B+G75 (2026-06-21/22) prove N_gen=3 via three independent Z3
triality zero-mode channels (8_v, 8_s, 8_c) of the twisted Dirac operator
on S6, with an explicit unitary Z3 action (eigenvalues 1, omega, omega^2)
established and verified orthogonal (G75).

**These two constructions have never been connected in this repo.** There
is currently no artifact defining what "generation index" means for a
Yukawa coupling, nor any check of what the Z3 symmetry implies for
inter-generation structure. This estimand formalizes that missing link,
not the full mass hierarchy (which is out of scope -- see "what this does
NOT mean").

## Estimand

**Population:** the abelian Z3 triality symmetry (G67/G75) extended to act
on 3 independent copies of the G25 32-state single-generation Yukawa
object, one copy per zero-mode channel (v,s,c), via phase omega^k on
channel k (k=0,1,2) -- exactly the representation already verified unitary
and orthogonal in G75.

**Intervention:** for each of the 4 Yukawa species (Y_nu, Y_e, Y_u, Y_d),
treat the coupling as a 3x3 matrix M_species[i,j] connecting channel i to
channel j (i,j in {0,1,2}), and ask which entries survive the requirement
that the Yukawa TERM be invariant under the Z3 action.

**Comparator:** (a) fully unconstrained 3x3 matrix (no Z3 relation checked)
vs (b) Z3-invariance-derived texture.

**Endpoint:** the pattern of allowed nonzero entries in M_species under
Z3-invariance, for a Yukawa term of the standard bilinear form (mass-like,
requiring total Z3 charge = 0 mod 3).

**Summary measure:** the texture class -- one of {PURE_DIAGONAL (i=j only,
i.e. exact degeneracy forced), OFF_DIAGONAL_ALLOWED (some i != j entries
survive), FULLY_UNCONSTRAINED (Z3 imposes no constraint at all, meaning the
triality label was never actually attached to the Yukawa sector)}.

**MCID:** any texture other than PURE_DIAGONAL is sufficient to show this
toy model does not structurally force generation-degenerate masses -- the
smallest informative distinction is PURE_DIAGONAL vs anything richer.

## Intercurrent events (ICE)

None -- pure symbolic/representation-theoretic computation, no missing
data, no stochastic sampling.

## Natural language statement

We estimate the texture class (diagonal / off-diagonal-allowed /
unconstrained) of the Z3-invariant inter-generation Yukawa coupling matrix
for each of the 4 SM particle species, comparing full Z3-invariance against
no constraint, with no ICE (deterministic algebra).

## What this result does NOT mean

1. Does NOT derive the observed Yukawa hierarchy (e.g. m_top/m_electron)
   -- at most it shows whether hierarchy is EXCLUDED or PERMITTED by the
   existing triality structure, not its actual numerical values.
2. Does NOT mean the 3 generations differ in any other observable if the
   texture allows off-diagonal terms -- off-diagonal Yukawa entries would
   need a separate diagonalization/mixing-angle analysis (CKM/PMNS), not
   attempted here.
3. Does NOT change N_gen=3 (G73-75) -- that result concerns the COUNT and
   ORTHOGONALITY of zero modes, independent of what this experiment finds
   about their Yukawa couplings.
4. If PURE_DIAGONAL is found: does NOT mean the geometric framework is
   falsified -- it would mean an ADDITIONAL symmetry-breaking mechanism
   (outside pure S3xS6 isometry+triality) is required for realistic masses,
   consistent with lambda=FREE_COUPLING_PARAMETER already showing this
   framework does not fix all couplings from geometry alone.
