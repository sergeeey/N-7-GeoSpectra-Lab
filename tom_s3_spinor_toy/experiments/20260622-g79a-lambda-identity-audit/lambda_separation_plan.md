# λ Separation Plan (G79A Action Item)

**Status:** DEFERRED — code rename requires Tom Part 4/5 input  
**Date:** 2026-06-26  
**Postmortem:** λ = FREE_COUPLING_PARAMETER (2026-06-22)

---

## Current State

The parameter_registry.json already defines two distinct symbols:
- `lambda_v_operator` — V-operator coupling; G4 non-identifiable from S³ observables
- `lambda_np` — non-perturbative exponent; candidates 1/3 (1.2% off) and π/9 (3.5% off)

G79A audit found **1977 occurrences** of `lambda` in the codebase. None are
explicitly typed. The audit verdict is `OPEN_IDENTITY_UNPROVEN`: no derivation
proves `lambda_v_operator = lambda_np` and no derivation proves them distinct.

---

## Why Not Renamed Now

Renaming 1977 occurrences requires knowing which `λ` each occurrence refers to.
This determination requires:
1. Tom's Part 4/5 — spinor field content and V-operator coupling in 4D EFT
2. Understanding whether the NP exponent appears in the same sector as the V-coupling

Without Tom's input, a rename risks silently misclassifying occurrences.

---

## Interim Convention (effective immediately)

Any NEW code or claim.md written after 2026-06-26 MUST use:
- `lambda_v` or `lambda_v_operator` — for the V-operator sector
- `lambda_np` — for the non-perturbative instanton exponent
- `lambda` (bare) — FORBIDDEN in new code; triggers ruff lint warning if added

**For existing code:** leave as-is until Tom Part 4/5 clarifies which sector
each occurrence belongs to. Do NOT bulk-rename.

---

## Trigger for Resolution

This plan activates into full rename when:
- Tom publishes Part 4/5 (spinor content + 4D EFT couplings)
- OR a derivation proves `lambda_v_operator = lambda_np` (BRIDGE_DERIVED)
- OR a derivation proves `lambda_v_operator ≠ lambda_np` (BRIDGE_REFUTED)

Tracking: `experiments/20260622-g79b-lambda-bridge-feasibility/`
