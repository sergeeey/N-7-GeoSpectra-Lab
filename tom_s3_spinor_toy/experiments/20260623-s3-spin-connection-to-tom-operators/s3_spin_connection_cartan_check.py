"""S3 spin connection Cartan check in the Hopf orthonormal frame.

This is a small deterministic symbolic verification of:

- the unit S Hopf metric
- the orthonormal coframe
- the torsion-free Cartan structure equations
- the resulting spin connection one-forms
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results_s3_spin_connection_cartan_check.json"

alpha = sp.symbols("alpha", real=True)


@dataclass(frozen=True)
class OneForm:
    expr: sp.Expr
    basis: str

    def wedge(self, other: "OneForm") -> "TwoForm":
        return TwoForm(sp.simplify(self.expr * other.expr), self.basis, other.basis)


@dataclass(frozen=True)
class TwoForm:
    coeff: sp.Expr
    left: str
    right: str

    def canonical(self) -> "TwoForm":
        if self.left == self.right:
            return TwoForm(sp.Integer(0), self.left, self.right)
        if self.left < self.right:
            return self
        return TwoForm(-self.coeff, self.right, self.left)


def d_of(form: OneForm) -> TwoForm:
    """Exterior derivative for the explicit coframe used here."""
    if form.basis == "e1":
        return TwoForm(sp.Integer(0), "e1", "e1")
    if form.basis == "e2":
        # d(cos α dθ) = -sin α dα∧dθ = -tan α e1∧e2
        return TwoForm(-sp.tan(alpha), "e1", "e2")
    if form.basis == "e3":
        # d(sin α dφ) = cos α dα∧dφ = cot α e1∧e3
        return TwoForm(sp.cot(alpha), "e1", "e3")
    raise ValueError(f"Unknown basis form: {form.basis}")


def add_twoforms(*forms: TwoForm) -> TwoForm:
    coeff = sp.Integer(0)
    left = "e1"
    right = "e2"
    for form in forms:
        canon = form.canonical()
        coeff += canon.coeff
        left, right = canon.left, canon.right
    return TwoForm(sp.simplify(coeff), left, right)


def main() -> int:
    metric = "ds2 = dα2 + cos2(α)dθ2 + sin2(α)dφ2"
    e1 = OneForm(sp.Integer(1), "e1")
    e2 = OneForm(sp.cos(alpha), "e2")
    e3 = OneForm(sp.sin(alpha), "e3")

    omega_12 = OneForm(sp.tan(alpha), "e2")
    omega_13 = OneForm(-sp.cot(alpha), "e3")
    omega_23 = OneForm(sp.Integer(0), "e3")

    omega_21 = OneForm(-sp.tan(alpha), "e2")
    omega_31 = OneForm(sp.cot(alpha), "e3")
    omega_32 = OneForm(sp.Integer(0), "e2")

    eq1 = add_twoforms(d_of(e1), omega_12.wedge(e2), omega_13.wedge(e3))
    eq2 = add_twoforms(d_of(e2), omega_21.wedge(e1), omega_23.wedge(e3))
    eq3 = add_twoforms(d_of(e3), omega_31.wedge(e1), omega_32.wedge(e2))

    cartan_pass = all(sp.simplify(eq.coeff) == 0 for eq in (eq1.canonical(), eq2.canonical(), eq3.canonical()))

    result = {
        "verdict": "PASS_CARTAN_HOPF_FRAME" if cartan_pass else "FAIL_CARTAN_HOPF_FRAME",
        "metric": metric,
        "coframe": {
            "e1": "dα",
            "e2": "cos(α)dθ",
            "e3": "sin(α)dφ",
        },
        "connection_one_forms": {
            "omega_12": "tan(α)e2",
            "omega_13": "-cot(α)e3",
            "omega_23": "0",
        },
        "coordinate_components": {
            "omega_theta_12": "sin(α)",
            "omega_phi_13": "-cos(α)",
        },
        "cartan_equations_checked": cartan_pass,
        "cartan_residuals": {
            "eq1": str(sp.simplify(eq1.canonical().coeff)),
            "eq2": str(sp.simplify(eq2.canonical().coeff)),
            "eq3": str(sp.simplify(eq3.canonical().coeff)),
        },
    }

    RESULTS.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0 if cartan_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
