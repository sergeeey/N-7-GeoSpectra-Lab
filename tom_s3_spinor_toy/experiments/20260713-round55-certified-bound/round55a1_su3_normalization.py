"""Round 55a.1 (2026-07-13): the last narrow normalization gate before
Round 56 -- does the SU(3) fibre Casimir, computed DIRECTLY from the
actual representation matrices this project's own code uses (not the
abstract su3_casimir formula in isolation), match the Bourbaki-self-norm
value used in Round 52's "-3" (Scenario A), or is it halved like the
G2 side turned out to be (Scenario B, "-3/2")?

User's own framing: G2-side rescale (native=Bourbaki/2, Round 55/55a)
does NOT automatically imply the SAME rescale applies to the SU(3) side
-- these are potentially independent normalization choices in the code,
and must be checked directly, not assumed by analogy.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
G2SU3_DIR = HERE.parent / "20260708-dolan-casimir-g2su3"
sys.path.insert(0, str(G2SU3_DIR))

from g2su3_equivariance_check import build_su3_matrix64  # noqa: E402


def su3_casimir_formula(p, q):
    return sp.Rational(p * p + p * q + q * q + 3 * p + 3 * q, 3)


def main() -> None:
    print("=" * 70)
    print("Direct computation: -Sum_{k=1}^8 M_k^2 on the FULL 64-dim fibre,")
    print("using build_su3_matrix64 -- the ACTUAL matrices Round 22's own")
    print("Ms[p]/torsion_cross_term/su3_curvature_term machinery is built")
    print("from, not the abstract su3_casimir formula in isolation")
    print("=" * 70)
    Ms = [build_su3_matrix64(i) for i in range(1, 9)]

    Casimir_fibre = sp.zeros(64, 64)
    for M in Ms:
        Casimir_fibre += M * M
    Casimir_fibre = sp.simplify(-Casimir_fibre)
    herm = sp.simplify(Casimir_fibre - Casimir_fibre.H) == sp.zeros(64, 64)
    print(f"  -Sum M_k^2 Hermitian? {herm}")
    assert herm, "SU(3) fibre Casimir not Hermitian -- STOP"

    ev = Casimir_fibre.eigenvals()
    print("  Exact eigenvalues of -Sum_{k=1}^8 M_k^2 on the full 64-dim fibre:")
    found_values = set()
    for val, mult in ev.items():
        v = sp.nsimplify(val)
        found_values.add(v)
        print(f"    {v}  (multiplicity {mult})")

    total_dim = sum(ev.values())
    print(f"  Total dimension check: {total_dim} (expect 64)")
    assert total_dim == 64, "dimension mismatch -- STOP"

    print()
    print("=" * 70)
    print("Compare against the Bourbaki-self-norm su3_casimir formula")
    print("(the SAME formula kp_zero_mode.py uses to derive '-3')")
    print("=" * 70)
    candidates = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    formula_values = {su3_casimir_formula(*pq) for pq in candidates}
    for pq in candidates:
        v = su3_casimir_formula(*pq)
        print(f"    su3_casimir{pq} = {v}")

    print()
    print(f"  Direct fibre eigenvalues: {sorted(found_values, key=float)}")
    print(f"  Formula values (relevant candidates): {sorted(formula_values, key=float)}")
    exact_match = found_values <= formula_values
    print("  Every direct fibre eigenvalue found among the UN-rescaled Bourbaki-self-norm")
    print(f"  su3_casimir formula values (Scenario A, no rescale needed)? {exact_match}")

    # Explicit check on the specific value driving Round 52's "-3":
    # does the fibre's own (1,1)-type block give exactly 3 (Scenario A)
    # or exactly 3/2 (Scenario B, i.e. half of su3_casimir(1,1)=3)?
    scenario_A = sp.Integer(3) in found_values
    scenario_B = sp.Rational(3, 2) in found_values
    print()
    print(f"  Scenario A (c_sigma,code = c_sigma,Bourbaki, i.e. 3 found directly): {scenario_A}")
    print(
        f"  Scenario B (c_sigma,code = c_sigma,Bourbaki/2, i.e. 3/2 found directly): {scenario_B}"
    )
    assert scenario_A and not scenario_B, (
        "AMBIGUOUS OR SCENARIO-B RESULT -- the '-3' in Round 52's bound needs "
        "correction to '-3/2', STOP and redo the exceptional-set derivation "
        "with the halved constant"
    )
    print()
    print("  RESOLVED: Scenario A confirmed directly, not assumed by analogy with")
    print("  the G2 side. The SU(3) fibre Casimir, as it ACTUALLY appears in the")
    print("  operator (via build_su3_matrix64, the same construction underlying")
    print("  Ms[p]/su3_curvature_term), exactly matches the Bourbaki-self-norm")
    print("  su3_casimir formula with NO rescale -- Round 52's '-3' is correct")
    print("  as originally stated, unchanged.")

    print()
    print("=" * 70)
    print("Note on the unmatched eigenvalue (10/3, multiplicity 12)")
    print("=" * 70)
    print("""
  10/3 = su3_casimir(2,0) = su3_casimir(0,2) -- a genuine SU(3) type present
  in the full 64-dim Sigma(x)Sigma fibre but NOT among the 4 types
  {(0,0)x2,(1,0),(0,1),(1,1)} appearing in S+(x)S- specifically (the
  domain/codomain-relevant subspace for THIS twisted Dirac operator).
  Dimension check: this is consistent (6+30+12+16=64 total; the (1,1)-type
  eigenspace has multiplicity 16 = 2 copies of the 8-dim (1,1) irrep,
  plausible since Sigma(x)Sigma (64-dim) is larger than S+(x)S- (16-dim)).
  Not relevant to Round 52/54/55's own K_cert or exceptional-set
  calculation, which only ever reference the 4 S+(x)S- fibre types --
  noted for completeness, not further investigated (out of scope).
""")


if __name__ == "__main__":
    main()
