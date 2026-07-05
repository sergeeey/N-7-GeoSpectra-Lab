# G104 Claim — H1 vs H2 lambda-origin hypotheses, forward-tested on S2xS6

**Question type:** descriptive (mathematical/structural; no physical data)

**Prior-art acknowledgment (Adaptive Iteration Branch Rule):** the Excel snapshot (2026-06-24)
recorded "G91: lambda dimensional hypothesis H1 vs H2 -- OPEN, need S2xS6 experiment" as
[VERIFIED-inline; not yet committed] -- no script or experiment folder was ever created; the
gate number G91 was independently reused the same day for an unrelated full-4D-reduction gate
(experiments/20260624-g91-full-4d-reduction/). This experiment is the first actual implementation,
under a new gate number to avoid collision, and corrects the originally-proposed methodology
(see "Rejected approach" below).

**Background:** on S3xS6 (a=3, N=6), two dimensional-counting formulas coincide:
- H1: lambda = 1/dim(S3) = 1/a = 1/3
- H2: lambda = dim(S3)/dim(S3xS6) = a/(a+N) = 3/9 = 1/3

They diverge on other products: S2xS6 (a=2,N=6) gives H1=0.500, H2=0.250.

**Rejected approach (found during design, source-traced to G61 decision.md):** the "natural"
generalization -- repeat G61's backward-solve lambda_exact = rho6*^2 * ln(A_np/V_FLUX) on
S2xS6 -- is CIRCULAR. G60's own pearl defines A_np = V_FLUX*exp(lambda/rho6*^2) "[given
lambda]" -- the same equation G61 inverts to solve for lambda. Any A_np choice reproduces
whatever lambda we want; this cannot discriminate H1 from H2 and is not implemented here.

**This experiment instead runs FORWARD:** treat lambda itself as the free input (as G62/GA1/
G103 already do), plug in lambda=H1 and lambda=H2 as two separate runs on the generalized
(a,N) potential (equal-radii trajectory rho_a=rho_N=rho -- the no-extra-assumption default,
since the SM-coupling-calibrated rho3=rho6^2 path has no independent justification for a
non-physical a=2 product), and compare each run against G66's already-VERIFIED, lambda-
independent analytic prediction kappa^2=(N+1)/N=7/6 (a genuine, non-circular cross-check,
since G66's derivation depends only on N=dim(second sphere), not on a or lambda).

**Falsifiable predicate:** if the (a,N)-generalized machinery is implemented correctly, it
must reproduce the ALREADY-VERIFIED (a,N)=(3,6) numbers as a positive control (kappa^2=7/6,
G62/G103's V_min sign and rho_min order of magnitude) before touching (a,N)=(2,6) at all.

**Measurable outcome (results_g104.json):**

| Check | Predicted | Kill if |
|---|---|---|
| C1 positive control: (a,N)=(3,6), equal-radii, lambda=1/3 gives kappa^2 | 7/6 (G66, exact) | \|kappa^2-7/6\|>1e-3 |
| C2 (a,N)=(2,6): AdS minimum exists for BOTH lambda=H1(0.5) and lambda=H2(0.25) | yes, both | either fails to exist -> that hypothesis is disfavored, not the test |
| C3 kappa^2(a=2,N=6) matches G66's N-only prediction 7/6 for BOTH lambda choices | yes (kappa depends on N only, per G66) | if kappa^2 differs between H1-run and H2-run -> kappa is NOT lambda-blind here, contradicts the established H1-pearl (2026-06-21) -- report loudly, do not paper over |
| C4 ratio of predicted V_min / m_mod between the two runs | computable, no target (descriptive) | n/a -- this is the actual differentiating number, reported not pre-judged |

**Claim:** this experiment does NOT expect to "discover which of H1/H2 is true" -- per C3's own
prediction, kappa (and by the H1-pearl, rho_min) should be near-identical for both lambda
choices, meaning the (a,N)-generalized geometry is likely ALSO lambda-blind at the level of
rho_min/kappa, same as G103 found for the S3xS6 case. The actual test is whether this blindness
still holds off the originally-scanned (a,N)=(3,6) point, and whether V_min/m_mod (the two
lambda-SENSITIVE observables per G103) differ enough between H1 and H2 to be a real future
discriminator IF an independent physical target for either becomes available.

**Kill criterion:**
- If C1 (positive control) fails -> generalized machinery is wrong, no conclusion possible, fix before reading C2-C4.
- If C2 fails for one hypothesis but not the other -> that hypothesis is geometrically disfavored (existence, not preference, but still informative).
- If C3 shows kappa differs materially between H1/H2 runs -> the H1-pearl's "near-universal across Sa x Sb family" claim needs re-examination; flag immediately, do not suppress.

**What this does NOT mean:**
1. Does NOT re-open lambda=FREE_COUPLING_PARAMETER -- G103 (today) already closed the UV-derivation
   question independent of H1/H2; this experiment is about a narrower historical curiosity (why
   did two formulas coincide at 1/3), not about deriving lambda's physical value.
2. Does NOT use the SM-calibrated V_FLUX/C_SM constants for the S2xS6 case -- S2xS6 is not
   claimed to be a physical compactification, only a mathematical probe of the (a,N) family.
3. Does NOT resolve which formula (if either) is "correct" -- only whether the geometry can
   distinguish them at all along the observables already known to be lambda-sensitive.
