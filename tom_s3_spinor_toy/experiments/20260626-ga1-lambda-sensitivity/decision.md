# GA1 Decision — Lambda Sensitivity

**Verdict: ROBUST**

## Key numbers

| lambda | rho6_min | ratio% | KK source |
|--------|----------|--------|-----------|
| 0.15   | 1.1781   | 0.133% | S3        |
| 0.20   | 1.1784   | 0.154% | S3        |
| 0.25   | 1.1786   | 0.172% | S3        |
| **1/3** | **1.1791** | **0.198%** | **S3** |
| 0.40   | 1.1794   | 0.217% | S3        |
| 0.50   | 1.1800   | 0.242% | S3        |
| 0.60   | 1.1805   | 0.264% | S3        |

- Spread: 0.133% — 0.264%  (factor **1.99x** across [0.15, 0.60])
- Sensitivity: **0.30 %/unit-lambda** (central finite difference at 1/3)
- rho6_min shift: only 1.1781 → 1.1805 (< 0.3% change) — minimum position is ultra-stable
- KK lightest mode: **always S3** across entire range

## Implications

1. **Bottleneck 1 is not blocking order-of-magnitude physics.** Even without fixing lambda,
   the ratio is pinned to 0.1–0.3% range. This is a qualitatively robust prediction.

2. **rho6_min is essentially lambda-independent.** The geometry of the compactification
   (where the minimum sits) is set by the NP structure, not by the precise value of lambda.

3. **KK hierarchy is structural, not fine-tuned.** S3 always gives the lightest KK mode;
   this is a consequence of rho3 = rho6^2 and the 3/2 vs 3 prefactor, independent of lambda.

4. **Sensitivity 0.30 %/unit-lambda:** a 30% change in lambda (e.g. 1/3 → 0.43) changes
   ratio by only ~0.03 percentage points. Lambda must change by a factor of ~2 to shift
   ratio by a factor of ~2.

## Status
- Claim: PASS (spread factor 1.99x < threshold 3.0x)
- Promotes G91 result from "lambda-dependent number" to "robust order-of-magnitude prediction"
- Bottleneck 1 (lambda origin) remains open but is now classified as sub-leading for phenomenology
