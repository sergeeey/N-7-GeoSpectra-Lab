# Invalidation — Cross-Domain SVD Phantom-Factor Test (2026-06-04)

**Status:** PRIOR TEST INVALIDATED — verdict must NOT be used
**Affected files:**
- `scripts/cross_domain_svd_phantom_test.py` — script ran successfully but tests an invalid quantity
- `reports/CROSS_DOMAIN_SVD_PHANTOM_TEST_2026-06-04.md` — verdict from this report is INVALID by construction
- `reports/CROSS_DOMAIN_SVD_PHANTOM_TEST_2026-06-04.json` — same

---

## What happened

1. Bridge C from the cross-domain audit proposed an SVD-based test for "phantom S³ axis":
   compute mode-1 and mode-2 unfolding of the operator, compare σ_max/σ_min ratios.
2. The smoke run executed cleanly in ~3 seconds across 6 cases.
3. Every single case produced `S3_ratio == S1_ratio` exactly.

## Why this is invalid (mathematical reason)

In the implemented `unfold_kron_axis(H, s3_dim, s1_dim, axis)`:

```
M_1 = T.transpose(0, 2, 1, 3).reshape(s3² , s1²)    # supposedly "S³ axis"
M_2 = T.transpose(1, 3, 0, 2).reshape(s1² , s3²)    # supposedly "S¹ axis"
```

But `T.transpose(1, 3, 0, 2)` is the **transpose** of `T.transpose(0, 2, 1, 3)`:

```
M_2 = M_1.T
```

And singular values are invariant under transpose:

```
SVD(M_1) ≡ SVD(M_1.T) ≡ SVD(M_2)
```

So the test by construction reports the same ratio for both axes — it is not a test that can distinguish S³-axis behaviour from S¹-axis behaviour. The verdict it produces is an artefact of the construction, not a property of the data.

## What the prior verdict claimed (and why it is unusable)

The prior aggregate verdict said:
> "BRIDGE_C_FALSIFIED — S³ shows heterogeneity (overturns 'passive' claim)"

This statement is **not supported by the test**. The test cannot distinguish "S³ heterogeneous" from "S¹ heterogeneous" — it reports both with the same number. No conclusion about the passivity or activity of either axis can be drawn from this script's output.

## Rules going forward

- The verdict in `CROSS_DOMAIN_SVD_PHANTOM_TEST_2026-06-04.md` must not be cited.
- The script `cross_domain_svd_phantom_test.py` must not be reused as-is — its design is invalid.
- No external claim (Tom, vault, repo, social) may rely on this script's output.
- The "passive S³ axis" question remains open. A replacement audit using static (no-eigensolve) checks is being prepared:
  `scripts/audit_s3_passive_axis_structure.py` → `reports/S3_PASSIVE_AXIS_STRUCTURAL_AUDIT_SMOKE_2026-06-04.md`.

## Cost / damage

- Compute wasted: ~3 seconds laptop.
- Files written: 2 (markdown + json).
- Commits made: 0.
- External claims made: 0.
- Risk to project: zero — the bug was caught on smoke, before any escalation.

## Lesson recorded

Cross-domain bridges that *look* like a clean SVD trick must be checked for trivial symmetries (transpose invariance, permutation invariance) before the actual experiment runs. A 30-second algebraic sanity check would have caught this before any code was written.

---

**Generated:** 2026-06-04 (after smoke run revealed S3_ratio == S1_ratio across all 6 cases).
