# Discovery opportunities — 2026-10-21

Sorted by expected significance / cost. Each is a falsifiable hypothesis with a minimal decisive test. None is a result.

1. **The Track A discretisation contrast may be a 3-point artefact (highest priority, cheap).**
   - H: the spectral_circle "WEAKENING" slope is a df=1 fit artefact; with ≥5 sizes and per-seed errors the slope is consistent with 0 or with the ring family.
   - Decisive test: refit the existing spectral_circle IPR data with N = 16…256 (or 512), per-seed errors, report slope ± SE and a bootstrap CI. Refutes H if the slope stays near −0.35 to −0.48 with CI excluding 0.
   - Cost: one analysis pass over existing or one Gate-5-style run.

2. **Stored C78 spectrum is not the committed script's output.**
   - H: the committed JSON came from an uncommitted variant of the bridge or D. Decisive test: find the variant via reflog or the C70 bridge parameters; if none, regenerate and treat the old file as stale.
   - Value: low for physics, high for reproducibility hygiene.

3. **Commutant dimension 8 of D equals su(3) — a possible exact theorem at fiber level.**
   - H: for any D built from the S³ × S⁶ product ansatz with this bridge, c_so8(D) = su(3). Decisive test: vary the bridge (another intertwiner from the C68 search) and see if dim changes. Refutes H if a second valid bridge gives a different commutant.
   - Cost: moderate; requires bridge variants.

4. **Fiber centraliser vs global symmetry (structural gap).**
   - H: a global symmetry of the full operator exists that acts on base or sections and is invisible to the fiber centraliser test. Decisive test: act with a candidate base isometry on sections and check commutation with the full D numerically on a truncated mode basis.
   - Cost: high; needs a truncated full-operator model.

5. **Structural Twin candidate (requires item 1 first).** Pair: spectral_circle vs ring with matched N, W, seeds, and basis. Property: IPR slope. Only usable after item 1 resolves the slope.

Ordering rationale: item 1 is the only one that touches a headline number and is cheap; items 3 and 4 are the scientifically larger payoff but need new code.
