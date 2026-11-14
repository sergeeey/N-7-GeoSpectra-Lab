# Morphism audit protocol (v2)

**Added:** 2026-09-19, after C200. **Status:** ACTIVE, OPTIONAL pre-check (not a gate,
not a promotion criterion). Used once so far (C200); treat as n=1.
**Source:** a user-pasted "Phase 2 — morphism mapping audit" prompt (five outcomes:
`EXACT_ISOMORPHISM / PARTIAL_ISOMORPHISM / HOMOMORPHISM / QUOTIENT_RELATION /
NO_STRUCTURAL_BRIDGE`), run on nine target pairs; see
`experiments/20260919-c200-morphism-mapping-audit/decision.md` for evidence and the
skeptic response.

Sibling of the 6-field Mechanism Transfer Gate (which asks WHICH correspondence
dimension fails: formula / object / role / generator / sector / observable). This
protocol asks WHAT KIND of map holds between two explicit objects. They are
complementary; neither replaces the other.

## When to use it

Only when BOTH sides are computed objects: explicit representations (matrices,
Hom spaces, invariant vectors), weight diagrams, spectra, block structures. There the
verdict is checkable against an independent computation. For prose analogies between
papers the verdict is mostly the author's encoding (C200: two of four hand-encoded
targets were tautological or convention-dependent, a third was uncalibrated and circular);
do not cite such a run as evidence.

## The protocol

```
0. SIGNATURE first: which nodes, which edge/operation types, which symmetry group may be
   used to identify objects. The verdict is a function of the signature; when the choice is
   ambiguous, output a table "signature -> verdict", not one word.
   (C200: {8_v,8_s,8_c} are EXACT under g2, split 1+2 under each so(7), NO_BRIDGE under so(8),
   twisted-isomorphic under so(8) up to the outer automorphism S3.)
1. PROVENANCE: were G_A and G_B built independently? If G_B was derived from G_A's
   vocabulary, mark [CIRCULAR]: the node correspondence is by construction.
2. LAYERS: classify each layer (magnitude / sign / structure) separately; report the set.
3. OUTCOMES: EXACT; TWISTED_ISOMORPHISM (equal after an automorphism of the label
   alphabet or algebra, lossless); QUOTIENT_COARSENING (equal after coarsening attributes;
   MUST list what was forgotten); PARTIAL (core threshold taken from the null, never "50%");
   HOMOMORPHISM (only if |A| > |B|, otherwise n/a); NO_STRUCTURAL_BRIDGE; UNCALIBRATED.
4. NULL: for every positive verdict, the rate at which same-size random graphs with the
   same per-label edge counts reach the same level. >= 5%, or too few trials, or an aborted
   search => VACUOUS / UNCALIBRATED. On <= 4 nodes no positive bridge can be calibrated.
5. CONTROLS with known answers (positive and negative) BEFORE the target pair, at every
   outcome level you intend to report.
6. Where objects are computable, compute (Hom dimensions, invariant-vector counts, 1-WL
   signatures) instead of encoding in prose.
```

## Known weaknesses of the five-word vocabulary (why v2 differs)

- The literal PARTIAL rule (core >= max(3, 50%)) fires on chance graphs at rate 1.000
  for 8-node graphs (300 random trials).
- `QUOTIENT_RELATION` covers two relations: twisted isomorphism (same size) and
  coarsening (lossy).
- No layered verdict (round89's `PARTIAL_OPPOSITE_SIGN_STRUCTURAL` cannot be expressed).
- Blind to circularity; small symmetric structures match by chance at rate 1.0.

## Reusable code

`experiments/20260919-c200-morphism-mapping-audit/c200_morphism_audit.py`: labelled-graph
isomorphism, induced common core, surjective-homomorphism search, module-level `Hom`
classifier (imports `g102_spin8_fiber.py`), same-size null, 19 controls.
`verify_c200_bruteforce.py` checks the graph routines against exhaustive enumeration.
