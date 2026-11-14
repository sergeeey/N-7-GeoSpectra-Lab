"""C173 (items23-scoping): direct Hom_{SU(3)} computation between round59's
real, certified Sigma (an SU(3)-module under its own ADNU generators) and EACH
of G102's three actual Cl(0,8) triality channels {v,s,c}, restricted to the
same SU(3) holonomy.

This goes one step beyond C65 (which only matched Casimir eigenvalue -4/3,
i.e. module TYPE) and one step beyond G102's own S7 (which only compared the
three channels PAIRWISE to each other, never against round59's own Sigma).
Reuses round59's ADNU/spin_lift (round59_route_a_independent.py), G102's own
derivation_basis/stabilizer_basis/restrict_to_subalgebra
(g102_spin8_fiber.py), and G102's own hom_dim (Sylvester/Kronecker nullspace)
unmodified, by direct import -- no re-transcription.

Prediction (frozen before running, per this round's claim.md kill criterion):
if G44/G102's degeneracy genuinely extends to round59's own object, then
Hom_su3(Sigma, channel_x) = 6 for ALL THREE x in {v,s,c} -- i.e. round59's Sigma
is equally, maximally isomorphic to all three channels, with no SU(3)-level
fact able to prefer one over another.

**POST-HOC CORRECTION, found by re-deriving the result rather than trusting
the first run (self-caught before being written into decision.md as a
finding):** the actual output is Hom_su3(Sigma, channel_x) = 4 for all three
x, NOT 6, while Hom_su3(channel_x, channel_y) = 6 for all NINE ordered pairs
(correctly regressing G102's own committed S7 result). The Sigma-vs-channel
number is NOT trustworthy as computed: `hom_dim(rep_a, rep_b)` (reused
unmodified from G102) pairs generator k of rep_a with generator k of rep_b
via `zip()` -- a valid Hom_su(3) computation ONLY if generator k of round59's
own `ADNU` basis and generator k of G102's `stabilizer_basis` are already
known to be the SAME abstract su(3) Lie-algebra element (up to the
representation map). That correspondence is exactly what
`ob11ii_explicit_isomorphism.py` (C66) tried to build and reported
BLOCKED-SUBSTRATE on (real/complex reality-type mismatch: round59's ADNU is
complex anti-Hermitian, G102's stabilizer_basis is real antisymmetric) --
i.e. no validated index correspondence between the two bases exists yet
anywhere in this project. Comparing su3_r59[k] against channel[k] index-by-
index therefore computes something basis-dependent and not meaningful as a
representation-theoretic Hom-space; the "4" is very likely an artifact of an
arbitrary, uncorrelated pairing between two unrelated concrete bases of the
same abstract algebra, not a real representation-theoretic fact. This
function's Sigma-vs-channel output is RETAINED in the results file for
transparency but is explicitly NOT used as evidence in decision.md -- see
decision.md Section on this self-caught methodological error. The
channel-vs-channel regression (matching G102's own committed S7 exactly) IS
valid, because both channels there are images of the SAME G102 su3 basis
under the SAME restrict_to_subalgebra map (index k always means the same
abstract element throughout that computation).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c173_hom_su3.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module(
    "round59_route_a_independent",
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py",
)
G102 = load_module(
    "g102_spin8_fiber",
    HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py",
)


def su3_round59() -> list[np.ndarray]:
    clifford = R59.build_clifford()
    return [
        np.array(R59.spin_lift(R59.ADNU[i], clifford).evalf(), dtype=complex) for i in range(1, 9)
    ]


def main() -> None:
    su3_r59 = su3_round59()

    der = G102.derivation_basis()
    su3_g102 = G102.stabilizer_basis(der)
    v_out, s_out, c_out = G102.restrict_to_subalgebra(su3_g102)
    channels = {"v": v_out, "s": s_out, "c": c_out}

    # --- sanity: round59's su(3) closes (regression of C65's own P1) ---
    max_closure = 0.0
    su3_flat = np.array([m.flatten() for m in su3_r59]).T
    q, _ = np.linalg.qr(su3_flat)
    for a in range(8):
        for b in range(a + 1, 8):
            comm = su3_r59[a] @ su3_r59[b] - su3_r59[b] @ su3_r59[a]
            coeffs = q.conj().T @ comm.flatten()
            recon = q @ coeffs
            max_closure = max(max_closure, float(np.max(np.abs(recon - comm.flatten()))))

    # --- Casimir spectrum of round59's Sigma (regression of C65's own P2) ---
    c2 = sum(a @ a for a in su3_r59)
    c2_herm = (c2 + c2.conj().T) / 2
    eigs = np.sort(np.linalg.eigvalsh(c2_herm))
    n_zero = int(np.sum(np.abs(eigs) < 1e-6))
    nonzero = eigs[np.abs(eigs) >= 1e-6]

    # --- the new computation: Hom_su3(Sigma, channel_x) for each x, AND
    #     Hom_su3(channel_x, channel_y) for all pairs as an in-session
    #     regression check of G102's own S7 (independent of its committed
    #     results_g102.json) ---
    hom_r59_to_channel = {label: G102.hom_dim(su3_r59, chan) for label, chan in channels.items()}
    hom_channel_pairs = {
        f"{la}-{lb}": G102.hom_dim(channels[la], channels[lb]) for la in channels for lb in channels
    }

    all_six = all(v == 6 for v in hom_r59_to_channel.values())
    channels_pairwise_six = all(v == 6 for v in hom_channel_pairs.values())
    hom_r59_uniform_across_channels = len(set(hom_r59_to_channel.values())) == 1

    if not channels_pairwise_six:
        verdict = "REGRESSION_FAILURE_G102_S7_NOT_REPRODUCED"
    elif not hom_r59_uniform_across_channels:
        # This WOULD be meaningful even without a validated basis correspondence,
        # since a genuine asymmetry across v/s/c under the identical (even if
        # arbitrary) index pairing would be a real discriminating signal.
        # It did not occur (see below): the number is uniform (4,4,4).
        verdict = "ROUND59_SIGMA_HOM_ASYMMETRIC_ACROSS_CHANNELS_NEEDS_FOLLOWUP"
    else:
        # hom_r59_to_channel is uniform across v/s/c (4,4,4 as actually observed)
        # but NOT independently meaningful as a Hom-space value per the docstring
        # correction above (unvalidated index correspondence). The UNIFORMITY
        # across channels is itself weak corroborating evidence for
        # non-discrimination (an arbitrary/spurious pairing being asymmetric
        # would have been a red flag; it is not), but is NOT treated as the
        # decisive argument -- see decision.md, which relies on G102's own
        # basis-INDEPENDENT S3/S4 centralizer-vanishing result instead.
        verdict = "HOM_COMPUTATION_INCONCLUSIVE_BY_CONSTRUCTION_SEE_DECISION_MD"

    results = {
        "experiment": "c173_hom_su3_round59_vs_channels",
        "su3_r59_closure_residual": max_closure,
        "casimir_n_zero": n_zero,
        "casimir_nonzero_values": sorted(set(np.round(nonzero, 6).tolist())),
        "hom_su3_round59_sigma_to_channel": hom_r59_to_channel,
        "hom_su3_channel_pairs_regression_of_g102_s7": hom_channel_pairs,
        "all_round59_to_channel_homs_equal_6": all_six,
        "g102_s7_regression_reproduced": channels_pairwise_six,
        "verdict": verdict,
    }

    print("=" * 96)
    print("C173 items23-scoping: Hom_su3(round59 Sigma, G102 channel_x) for x in {v,s,c}")
    print("=" * 96)
    print(f"su(3) closure residual (round59) = {max_closure:.2e}")
    print(f"Casimir: n_zero={n_zero}, nonzero={sorted(set(np.round(nonzero, 6).tolist()))}")
    print(f"Hom_su3(Sigma, channel_x) = {hom_r59_to_channel}  (predict all 6)")
    print(f"Hom_su3(channel_x, channel_y) [G102 S7 regression] = {hom_channel_pairs}")
    print(f"\nVERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
