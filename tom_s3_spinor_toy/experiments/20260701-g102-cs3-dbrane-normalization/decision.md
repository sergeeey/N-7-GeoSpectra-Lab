# Decision — G102: does c_S3 (G94) reduce to a prediction for g_s?

**Date:** 2026-07-01
**Verdict:** STRUCTURAL_RELATION_CONFIRMED — c_S3 = 1/(2*g_s), implied g_s in [1.344, 2.016]
**Go/no-go:** GO on documenting this as a real constraint; caveat required on exact prefactor

## Result (5/5 script checks + 6/6 pytest, all PASS)

Substituting the standard Euclidean Dp-brane tension formula
T_2 = 1/((2*pi)^2 * alpha'^(3/2) * g_s) into G94's ansatz
S_inst = T_2 * Vol(S3), using this repo's own rho3-to-string-length
convention (GA2: physical radius = rho3 * l_s, string units M_s=1):

```
S_inst = rho3^3 / (2*g_s)
=> c_S3 = 1/(2*g_s)   [VERIFIED-sympy, symbolic, l_s cancels exactly]
```

G94's empirically-scanned valid window c_S3 in (0.248, 0.372) therefore
corresponds to **g_s in (1.344, 2.016)** -- a STRONGLY COUPLED string
regime (g_s > 1).

## Skeptic review outcome (agent aec83a030a24f6af4)

Pre-implementation review resolved the main worried risk (GA2's dropped
2*pi convention) as a red herring: GA2's simplification lives strictly in
the M_Pl^2=M_s^7*V_9 Planck-mass relation, a kinetic-term normalization
independent of the brane-tension-to-instanton-action formula used here.
Confirmed by direct read of 2 files (g94_s3_np_instanton.py:55,
ga2_m4_ms_units.py:28-29) plus the T4 control in the script itself
(c_S3's derivation never references M_Pl or V_9 at all).

One real blocker remained: source-trace confidence on the exact numeric
prefactor. WebSearch cross-confirmed the STRUCTURAL tension formula
(2 independent queries, Polchinski convention), but a direct PDF fetch of
a specific paper (arXiv:2310.20559) failed to parse cleanly (produced a
self-inconsistent double-1/g_s artifact) and was discarded. A follow-up
search for the Euclidean-instanton-specific normalization (Wick rotation /
RR-coupling subtleties that could add an extra O(1) factor) did not
cleanly resolve. This residual uncertainty is carried in the code's own
output and this document, not hidden: the coefficient 1/2 is [WEAK-MEDIUM]
confidence; the proportionality c_S3 ~ 1/g_s is more robust.

## What this does NOT mean

1. Does NOT measure g_s independently -- this shows what G94's empirical
   window IMPLIES under the source-traced tension formula, not a
   measurement of the actual string coupling.
2. Does NOT mean the strongly-coupled result is wrong or a red flag by
   itself -- per skeptic review, T_p is a BPS-protected quantity valid
   at any coupling; g_s>1 signals a physically interesting tension
   (perturbative DBI/instanton pictures are usually built assuming g_s<<1)
   worth flagging prominently, not silently accepting or panicking over.
3. Does NOT resolve lambda_np (the S6-side NP exponent, candidates 1/3 or
   pi/9, separately established in G60/G61) -- c_S3 is the S3-side
   analog, addressed independently here.
4. Does NOT change lambda_v_operator=FREE_COUPLING_PARAMETER,
   sm_derivation_claimed=False, or safe_for_runtime=False.
5. The exact prefactor (1/2, hence the exact g_s window [1.344, 2.016])
   should be treated as [WEAK-MEDIUM] pending a cleaner primary-source
   confirmation of the Euclidean-instanton normalization specifically --
   future work item, not blocking this result's structural content.

## Lesson

Fourth pre-implementation skeptic review this session (after G98, G99,
G101 all being killed pre-code) -- this is the first to get a mostly
green light, and the reason was concrete: the identified risk (GA2
convention mismatch) was checked directly against source files rather
than assumed, and it turned out to be genuinely irrelevant to this
specific derivation. Not every red flag is real; verifying which ones are
is exactly what the review step is for.
