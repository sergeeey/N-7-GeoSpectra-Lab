# OB11 (condition i) Decision — internal block structure verified

## Verdict

`PASS_CONDITION_I_SU3_PART_VERIFIED` (OB11 overall status: still OPEN)

## Scope note (read first)

OB11 has three unverified sufficiency conditions for the WEAK reading of
`H_physical=H_matter⊗H_generation`: (i) identical internal block
structure across channels, (ii) no channel-mixing in the Dirac operator,
(iii) triality acting purely as `1⊗t`. **This round only attempts (i).**
A grounding pass (Explore agent) confirmed the 2026-07-19 substrate-check
was right: (ii) requires assembling a genuinely new channel-decomposed
differential Dirac operator, entangled with the still-open OB1 — not a
cheap extraction from existing data, and not attempted here. (iii) would
need triality expressed as an explicit operator on a combined space and
is a separate, also-unattempted construction.

## What was checked and how

**Key scope-clarifying finding (changes how condition (i) should even be
read):** `SU(2)_L×SU(2)_R` lives entirely on the S³ factor of `H_matter`
(`preprint.tex:292-310`, round90) and **never acts on the S⁶-side
octonion fiber** where `8_v/8_s/8_c` are constructed at all — round119
(`decision.md:37-42`) explicitly corrected an earlier false claim that
`SU(3)×SU(2)×SU(2)` embeds inside `SO(6)`. Consequence: condition (i)'s
`SU(2)_L×SU(2)_R` part is **vacuous** — the S³-side 4-dim spinor factor
of `H_matter` is identical across all three channels by construction,
since the channel label attaches only to the S⁶ side. The only
substantive content of condition (i) is whether `SU(3)_c`'s
representation content on `8_v`, `8_s`, `8_c` is identical.

**Reused, without modification:** G102's own already-verified `su(3)`
construction (`stabilizer_basis(derivation_basis())`, dim 8, matching
G2/SU(3) holonomy) and `restrict_to_subalgebra` machinery
(`experiments/20260705-g102-spin8-fiber-obstruction/g102_spin8_fiber.py`).
G102 S7 already established `Hom_su3(a,b)=6` for all 9 ordered pairs
`a,b∈{v,s,c}` (a dimension count); round127's `decision.md:72-83` argued
algebraically that `Hom(V,V)=4+a²+b²=6⟹a=b=1` implies a `1⊕1⊕3⊕3̄`
decomposition — but neither round ever ran an explicit per-channel
diagonalization to confirm it.

**New computation (`ob11_internal_block_structure.py`)
[VERIFIED-numpy]:** for each channel, computed the quadratic Casimir
`C₂=Σ_a T_a²` using the SAME 8 `su(3)` generators fed into
`restrict_to_subalgebra` for all three channels (making the cross-channel
comparison basis-independent even though the absolute eigenvalue depends
on the arbitrary normalization of the `su(3)` basis returned by G102's
own `stabilizer_basis`). Result, all three channels:

```
channel 8_v: 2 zero eigenvalues + 6 eigenvalues at -1.333333...
channel 8_s: 2 zero eigenvalues + 6 eigenvalues at -1.333333...
channel 8_c: 2 zero eigenvalues + 6 eigenvalues at -1.333333...
```

Exact match, all three channels, to numerical precision (residuals
~1e-17, eigenvalue agreement to ~1e-6 tolerance used deliberately loose
for clustering, actual agreement far tighter). This directly confirms
the predicted `1⊕1⊕3⊕3̄` pattern (2 singlets + 6-dim block at one shared
nonzero Casimir value, consistent with `3` and `3̄` sharing the same
quadratic Casimir) for EACH channel individually, and that all three
channels' patterns are IDENTICAL to each other.

## Interpretation

Condition (i) of OB11's WEAK-reading sufficiency test is now genuinely
verified for its only non-trivial part (`SU(3)_c`): the internal gauge
representation content of `H_matter`'s S⁶-side factor is identical
across all three triality channels, and the S³-side factor is trivially
identical by construction (the channel label never touches it). This
strengthens the WEAK reading's live-candidate status (one more of three
sufficiency conditions now checked, none yet falsified) without
completing it — (ii) and (iii) remain open and are the harder,
not-yet-costed parts of the hypothesis.

## What this does NOT mean

1. Does NOT resolve OB11 overall — (ii) and (iii) untouched, and (ii) in
   particular is known (2026-07-19 substrate-check) to require a new
   differential-operator construction entangled with OB1.
2. Does NOT distinguish `3` from `3̄` within a channel (Casimir can't);
   only the aggregate multiplicity pattern is confirmed. round128's own
   explicit intertwiner already did the finer match for `8_v` alone
   (`iso_residual~1e-15`); the same fine-grained check for `8_s`/`8_c`
   is not attempted here.
3. Does NOT re-derive G102's `su(3)` construction, `Hom`-dimension
   counts, or round127's algebraic argument — all reused by citation.
4. Does NOT touch `N_gen=3`, `λ=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.

## Next gate (optional follow-up, not required by this claim)

If OB11 is picked up again: (ii) needs an explicit channel-decomposed
Dirac operator (new construction, scope it as its own SMALL–LARGE round,
entangled with OB1); (iii) needs triality expressed as an explicit
operator on a combined space with an admixture check into the matter
factor. Neither is cheap; this round deliberately did not force them.

## Check (reproduces this derivation)

```
cd experiments/20260803-ob11-internal-block-structure-check
python ob11_internal_block_structure.py
```
Expect: su(3) generator count 8; each channel's Casimir gives 2 zero +
6 equal-nonzero eigenvalues; all three channels' nonzero eigenvalue
identical; VERDICT: VERIFIED.
