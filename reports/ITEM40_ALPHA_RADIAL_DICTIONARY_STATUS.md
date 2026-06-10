# Item 40 — Consolidated Status: tom_ansatz / α-Radial Dictionary

**Date:** 2026-06-10
**Commits:** 7fa4360 (AV-1), e5576d7 (AV-1c′) — pushed to origin/main
**Tests:** suite 102/102

---

## One-line status

```
Item 40 = RADIAL + DICTIONARY_ROBUST
Promotion: NO
Full angular identification: PENDING (AV-2)
```

## Ladder of results (chronological)

| Step | Check | Verdict | Evidence |
|---|---|---|---|
| E1 (legacy) | tom_ansatz → φ₁₁, l=1 sector only | cos² = 0.9204 | [VT] regression-tested |
| AV-1a | global argmax over 49-mode dictionary | **PASS** — (1,1), convention-robust | [VT] 2 measures, 2 grids |
| AV-1b | 5-term linear approximation | **PASS** — residual 2.9% | [VT] |
| AV-1c | diagonal bilinear sparse model | **FAIL** — 12.38% > 10% | [VT] pre-registered |
| AV-1c′ | sparse cross-bilinear model (D2 primary) | **KILLED** — 13.0% > 10% | [VT] null_results/20260610-ht1-sparse-bilinear.md |
| P1 | boundary cos-exponent obstruction | **VERIFIED** — residual peak at α/π = 0.500 | [VT] pre-registered prediction |
| P2 | f^(φ) constant term required | **VERIFIED** — 37.9% → 13.0% | [VT] pre-registered prediction |

## What is established (approved phrasing)

> *The radial layer suggests a φ_ll boundary-family structure, with φ₁₁
> dominant at the linear level, while the eq. 49 bilinear layer requires
> f^(φ) plus a dense bilinear expansion.*

Supporting facts:
- Linear layer: tom_ansatz = √(2√||g||) is φ₁₁-dominated (cos = 0.9594);
  top-5 of 49 modes is exactly the n=l boundary family (92.4% of norm).
- Quadratic / eq. 49 layer: sparse bilinear models fail for a STRUCTURAL
  boundary-exponent reason (cos¹ target vs cos² bilinears), not bad fitting.
- f^(φ) is structurally necessary, not cosmetic (greedy picks it first;
  3× residual drop).
- The extended bilinear span DOES contain the target (full-LS ≈ 5e-4,
  ill-conditioning caveat) — the expansion exists but is dense.

## Forbidden phrasings (do not use)

```
"Tom's ansatz solved"          — NO
"eq. 49 derived"               — NO
"φ₁₁ identified as full mode"  — NO (radial layer only)
"H-T1 confirmed"               — NO (sparse form KILLED)
```

## Next

AV-2 (pre-registration: claim_av2_angular.md). Central estimand:
*does the full angular/spinor structure (half-integer Hopf weights, spin
connection) change the boundary exponents enough to explain eq. 49 without
an artificial dense radial fit?*
