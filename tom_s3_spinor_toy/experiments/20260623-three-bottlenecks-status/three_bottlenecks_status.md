# Three Bottlenecks Status

## Bottleneck 1 — Lambda origin

Status:

- `FREE_COUPLING_PARAMETER`
- Internal GeoSpectra geometry/spectral routes are exhausted.
- Standard gauge reduction, spectral/proper-time, Poisson/theta, saddle, dual-modulus, warp-factor, and dimensional lambda gates do not derive `lambda`.
- `lambda = 1/3` remains an external or phenomenological input inside the current framework.
- The strong no-free-parameter claim must be downgraded.

## Bottleneck 2 — Physical mass ratio

Status:

- `CONSTRAINED_PHYSICAL_RATIO` (updated 2026-06-24, G91)
- G88D: `CANONICAL_PROXY_ONLY`
- G88E: `FRAME_MAP_MISSING`
- G88F: `INSUFFICIENT_ACTION`
- **G91: `CONSTRAINED_PHYSICAL_RATIO` — 6/6 gates PASS** [VERIFIED-bash 2026-06-24]

G91 resolved three G88F gaps:
1. **Frame independence proved**: Ω² = ρ₆^12 cancels exactly in ratio; string frame = Einstein frame (diff = 0.0, machine precision)
2. **Verified KK spectrum used**: S³ λ₀ = 3/(2ρ₃), S⁶ λ₀ = 3/ρ₆ from G4/G73 [VERIFIED-pytest]
3. **2D potential written**: V(ρ₃,ρ₆) explicit; σ₃ runaway confirmed analytically (∂V/∂lnρ₃ = −3V)

Physical mass ratio:
- `m_mod/m_KK = 0.198%` (corrected from G88A proxy 0.252%; correction factor 0.786)
- Lightest KK from S³: m_KK = 3/(2ρ₆²) = 1.079 at ρ₆_min = 1.179
- S⁶ lightest: m_KK = 3/ρ₆ = 2.544 (not the lightest mode)

Remaining open in G91:
- Path constraint ρ₃ = ρ₆² is an **external assumption**, not derived from V(ρ₃,ρ₆)
- σ₃ (S³ radius) is a **runaway direction** — requires external stabilization mechanism

Include commits:

- `9752c93` — `test(audit): close physical mass ratio as insufficient action`
- `427c307` (feature/g91-full-4d-reduction) — `feat(g91): full 4D reduced action — frame independence + corrected KK spectrum`

## Bottleneck 3 — Right-handed neutrino Majorana mass

Status:

- `DIRAC_ONLY_CONFIRMED`
- G89A: `DIRAC_ONLY_ALLOWED`
- G89B: `DIRAC_ONLY_CONFIRMED`
- Exact `B-L` forbids a bare Majorana mass.
- No `B-L = +2` scalar/operator/sector was found.
- The current model predicts Dirac-only neutrinos unless external `B-L` breaking physics is added.

Include commit:

- `7792811` — `test(audit): close neutrino Majorana channel as Dirac-only`

## Overall conclusion

The current GeoSpectra framework remains useful as a phenomenological spectral compactification toy model, but it cannot currently support the stronger no-free-parameter first-principles claim.

Remaining options:

1. accept `lambda` as a phenomenological parameter;
2. add external non-perturbative physics for `lambda`;
3. add a full reduced 4D action for physical mass predictions;
4. add external `B-L` breaking physics if Majorana/seesaw neutrinos are desired;
5. otherwise state Dirac-only neutrinos as a prediction.
