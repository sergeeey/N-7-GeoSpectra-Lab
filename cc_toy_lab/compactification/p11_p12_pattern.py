"""P11/P12 frozen matrix-element pattern checks."""

from __future__ import annotations

from dataclasses import dataclass

from cc_toy_lab.compactification.registry_loader import load_registry


@dataclass(frozen=True)
class PatternExpectation:
    i: int
    j: int
    expected: str
    tolerance: float = 1e-10


def p11_expectation(i: int, j: int) -> PatternExpectation:
    data = load_registry("P11_robust_wigner_cg_pattern.yaml")
    for row in data["pattern_table"]:
        if int(row["i"]) == i and int(row["j"]) == j:
            return PatternExpectation(
                i=i,
                j=j,
                expected=str(row["expected"]),
                tolerance=1e-10,
            )
    raise KeyError(f"P11 pattern missing for ({i},{j})")


def p12_scale_class(i: int, j: int) -> str | None:
    data = load_registry("P12_matrix_element_pattern.yaml")
    for row in data["scale_rules"]:
        pair = row["pair"]
        if int(pair[0]) == i and int(pair[1]) == j:
            return str(row["absolute_scale"])
    return None


def pattern_compatible(i: int, j: int, value_abs: float, tol: float = 1e-8) -> bool:
    exp = p11_expectation(i, j)
    if exp.expected == "zero":
        return value_abs <= max(exp.tolerance, tol)
    if exp.expected == "nonzero_structure":
        return value_abs > tol
    return True
