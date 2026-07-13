"""Round 52 (2026-07-13): narrow premise audit for the L4B "growing-gap"
claim, per the user's explicit scope: test ONLY whether the Casimir gap
underlying the Kostant-Parthasarathy (KP) mechanism grows (or stays
positive) as the G2 representation label rho grows -- do NOT build the
full Dirac-operator matrices for rho=27,64,77 (that would be the
expensive per-representation computation this audit exists to gate).

FROZEN CLAIM (decision.md:393-397, colloquially "Round 6", verified by
Prior Result Gate before this script was written): "Casimir gap grows
unboundedly while the torsion correction is a fixed, bounded fibre
operator." This is TWO separate sub-claims:
  (A) C_2(G2;rho) grows unboundedly as rho grows.
  (B) The torsion/algebraic correction operator stays BOUNDED (a fixed-
      size fibre operator) as rho grows.
Round 48's own shortlist flagged this whole premise as "unverified".
This script resolves (A) completely (elementary, provable, no new
matrices) and reports honestly that (B) has zero data anywhere in this
project and cannot be resolved at this audit's cheap tier.

REUSES (does not re-derive): g2_casimir, su3_casimir, g2_dim, su3_dim
from experiments/20260625-kp-zero-mode/kp_zero_mode.py (already
calibrated, cited in that file's own docstring against 2296 passing
project tests). The FIXED S+ tensor S- SU(3) fibre decomposition
(4 types: (0,0),(1,0),(0,1),(1,1), max Casimir 3, from (1,1)) is
likewise reused from that file's own run_kp_analysis(), not recomputed.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
KP_DIR = HERE.parent / "20260625-kp-zero-mode"
sys.path.insert(0, str(KP_DIR))

from kp_zero_mode import g2_casimir, g2_dim, su3_casimir  # noqa: E402

RESULTS_PATH = HERE / "results_round52.json"

# Fixed S+ (x) S- SU(3) fibre decomposition -- reused verbatim from
# kp_zero_mode.py's own run_kp_analysis() (already-calibrated, 2296 tests).
# S+|SU(3) = 3bar+1 = (0,1)+(0,0); S-|SU(3) = 3+1 = (1,0)+(0,0).
# S+(x)S- fibre types (SU(3) LR decomposition of the 16-dim tensor product):
FIBRE_SU3_TYPES = [(0, 0), (1, 0), (0, 1), (1, 1)]


def bare_casimir_gap(m: int, n: int, max_fibre_c2: Fraction) -> Fraction:
    """gap(m,n) = C_2(G2;m,n) - max_fibre_C2. This is the BARE (cubic
    Dirac operator) KP gap -- does NOT include the torsion correction
    needed for the physical Levi-Civita operator (see preprint.tex:699-708).
    """
    return g2_casimir(m, n) - max_fibre_c2


def main() -> None:
    print("=" * 70)
    print("STEP 0 (POSITIVE CONTROL): reproduce kp_zero_mode.py's own")
    print("already-published rho=7 gap result before trusting anything new")
    print("=" * 70)
    max_fibre_c2 = max(su3_casimir(*r) for r in FIBRE_SU3_TYPES)
    print(f"  Fixed fibre types: {FIBRE_SU3_TYPES}")
    print(f"  max C2(SU(3)) over fibre = {max_fibre_c2}  (kp_zero_mode.py states: 3, from (1,1))")
    assert max_fibre_c2 == 3, (
        "fibre max Casimir does not match kp_zero_mode.py's own stated value -- STOP"
    )
    c2_7 = g2_casimir(1, 0)
    gap_7 = bare_casimir_gap(1, 0, max_fibre_c2)
    print(f"  C2(G2; rho=7=(1,0)) = {c2_7}  (kp_zero_mode.py states: 4)")
    print(f"  bare gap at rho=7   = {gap_7}  (kp_zero_mode.py states: KP spectral gap = 4-3 = 1)")
    assert c2_7 == 4 and gap_7 == 1, (
        "does not match kp_zero_mode.py's own published rho=7 numbers -- STOP"
    )
    print("  PASS: matches kp_zero_mode.py's own published rho=7 result exactly")

    print()
    print("=" * 70)
    print("STEP 1: resolve the rho=27,64,77 labels used in Round 48's own")
    print("shortlist (never previously defined anywhere in this project)")
    print("=" * 70)
    candidates = [(2, 0), (1, 1), (0, 2), (3, 0), (2, 1), (1, 2), (0, 3), (4, 0), (0, 4)]
    dim_table = {}
    for m, n in candidates:
        d = g2_dim(m, n)
        dim_table.setdefault(d, []).append((m, n))
        print(f"  (m,n)=({m},{n}): dim={d}, C2(G2)={g2_casimir(m, n)}")
    print()
    for target_dim in (27, 64, 77):
        labels = dim_table.get(target_dim, [])
        if len(labels) == 1:
            print(f"  dim={target_dim} -> UNIQUE label {labels[0]}")
        else:
            print(
                f"  dim={target_dim} -> AMBIGUOUS, {len(labels)} distinct labels: {labels} "
                f"-- Round 48's shortlist never specified which one"
            )
    assert len(dim_table.get(77, [])) >= 2, (
        "expected the dim=77 ambiguity ((0,2) and (3,0) both have dim 77) -- "
        "if this assertion fails, the earlier gate-check's finding was wrong, STOP"
    )
    print()
    print("  CONFIRMED: 'rho=77' is genuinely ambiguous -- (0,2) [C2=20] and")
    print("  (3,0) [C2=16] are two INEQUIVALENT G2 irreps sharing dimension 77.")
    print("  Round 48's bare '(rho=27,64,77...)' list under-specifies the target.")

    print()
    print("=" * 70)
    print("STEP 2 (THE CORE RESULT): prove min C2(G2;m,n) over ALL nontrivial")
    print("(m,n) unconditionally -- elementary algebra, not a finite scan")
    print("=" * 70)
    print("""
  C2(m,n) = (2m^2 + 6mn + 6n^2 + 10m + 18n) / 3, for integers m,n >= 0.
  Every term is non-negative for m,n >= 0. Two cases for (m,n) != (0,0):

  Case m>=1 (any n>=0): C2 >= (2m^2+10m)/3 >= (2+10)/3 = 4   [at m=1,n=0]
    (dropping the non-negative 6mn+6n^2+18n terms only LOWERS the bound,
     so this is a valid lower bound for every n>=0, not just n=0)
  Case m=0, n>=1:       C2 = (6n^2+18n)/3 >= (6+18)/3 = 8    [at n=1]

  Therefore: min over (m,n) != (0,0) of C2(G2;m,n) = 4, achieved ONLY at
  (m,n)=(1,0) [rho=7]. This is a closed-form, unconditional bound valid
  for ALL (m,n), not limited to any scanned range.
""")
    # Computational confirmation of the hand proof, over a wide range
    # (this is a SANITY CHECK on the algebra above, not the proof itself --
    # the proof is the case analysis printed above, which holds for all m,n).
    scan_range = 60
    min_c2 = None
    min_at = None
    for m in range(scan_range):
        for n in range(scan_range):
            if m == 0 and n == 0:
                continue
            c2 = g2_casimir(m, n)
            if min_c2 is None or c2 < min_c2:
                min_c2 = c2
                min_at = (m, n)
    print(f"  Sanity scan over (m,n) in [0,{scan_range})^2 \\ (0,0): min C2 = {min_c2} at {min_at}")
    assert min_c2 == 4 and min_at == (1, 0), (
        f"Sanity scan contradicts the hand proof (found min={min_c2} at {min_at}, "
        "expected 4 at (1,0)) -- the algebra above has an error, STOP and do not trust it"
    )
    print("  PASS: scan confirms the hand proof over a wide range, no counterexample")

    print()
    print("=" * 70)
    print("STEP 3: bare gap is UNCONDITIONALLY positive for every nontrivial rho")
    print("=" * 70)
    unconditional_gap = min_c2 - max_fibre_c2
    print(f"  min C2(G2;rho) - max_fibre_C2(SU3) = {min_c2} - {max_fibre_c2} = {unconditional_gap}")
    print("  Since min C2(G2;rho)=4 is proven (Step 2, all rho, not just scanned),")
    print(f"  bare_gap(rho) >= {unconditional_gap} > 0 for EVERY nontrivial G2 irrep rho,")
    print(
        f"  including rho=27=(2,0) [C2={g2_casimir(2, 0)}], rho=64=(1,1) [C2={g2_casimir(1, 1)}],"
    )
    print(f"  rho=77 both labels [(0,2): C2={g2_casimir(0, 2)}, (3,0): C2={g2_casimir(3, 0)}],")
    print("  and every representation beyond, with NO exceptions and NO further scan needed.")

    print()
    print("=" * 70)
    print("STEP 4 (HONEST GAP -- NOT RESOLVED HERE): the torsion-correction")
    print("boundedness half of the premise")
    print("=" * 70)
    print("""
  Sub-claim (B) -- "the torsion correction is a fixed, bounded fibre
  operator [as rho grows]" -- is NOT addressed by Steps 0-3 above, which
  only concern the BARE (cubic Dirac operator) Casimir gap. The physical
  Levi-Civita operator needs an additional torsion-dependent correction
  term (preprint.tex:699-708), and this project's own explicit torsion
  computation (Round 22, decision.md:3317+) is a closed, one-off
  construction SPECIFIC to rho=7's own 448-dimensional multiplicity
  space -- it contains no formula or bound expressing how the torsion
  operator's norm scales with rho in general. No other file in this
  repo computes or bounds this for any rho beyond 7 and 14 (confirmed
  via Prior Result Gate: zero hits for 'growing-gap', 'monotonic', or
  any rho-scaling law anywhere in null_results/, parked/, or decision.md
  outside the rho=7/14-specific constructions).

  This cannot be resolved at this audit's cheap tier (by design -- doing
  so would require exactly the per-representation construction this
  premise audit exists to gate before committing to).
""")

    results = {
        "gate": "Round52-GrowingGap",
        "positive_control": {
            "c2_rho7": str(c2_7),
            "gap_rho7": str(gap_7),
            "max_fibre_c2": str(max_fibre_c2),
        },
        "dim_77_ambiguity": {str(k): v for k, v in dim_table.items() if k in (27, 64, 77)},
        "min_c2_nontrivial": {"value": str(min_c2), "achieved_at": list(min_at)},
        "unconditional_bare_gap": str(unconditional_gap),
        "sub_claim_A_bare_casimir_gap": "PROVEN unconditionally (elementary algebra, all (m,n))",
        "sub_claim_B_torsion_boundedness": "NOT RESOLVED -- zero data beyond rho=7,14, no scaling law exists anywhere in the repo",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"Results -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
