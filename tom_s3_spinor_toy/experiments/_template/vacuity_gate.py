r"""
Vacuity gate — a mandatory FIRST check before reporting any prediction-test
verdict, added 2026-09-04 after C151 Stage 2b printed "PREDICTION CONFIRMED"
over a quantity that was identically zero (0 = i*0 satisfied the check
perfectly, at the wrong-sign 4.9e-16 "deviation" — the closer to vacuous, the
better the score looked). The script's own non-vacuity check had been
computed but never wired into the verdict branch.

THE RULE, restated as code instead of prose so it cannot be silently skipped:

    observable non-zero / non-degenerate?
        NO  -> STOP. Print VACUOUS. Do not evaluate the prediction at all.
        YES -> proceed to test the actual prediction, and only THEN verdict.

Never the other order. A prediction test run before this gate can pass
"perfectly" on a vacuum (see C151), which is textbook validation theater —
this project's own skeptic-triggers.md names exactly this failure mode.

USAGE

    from vacuity_gate import vacuity_gate

    values = [max(abs(x)) for x in observable_samples]   # your own metric
    gate = vacuity_gate(values, floor=1e-8, label="c on the 6 family basis vectors")
    if not gate.nonvacuous:
        print(gate.report())
        raise SystemExit(0)   # or: return / continue -- STOP before the verdict
    # ... only now compute and print the actual prediction verdict ...

`floor` should be chosen relative to the SAME numerical process's own noise
floor (e.g. 1e-8 for float64 chains of moderate depth), not tuned after
seeing whether it lets the current data through — that is the self-serving
threshold this project's own rules (falsification-ladder.md) forbid.
"""

from dataclasses import dataclass, field


@dataclass
class VacuityGateResult:
    nonvacuous: bool
    values: list[float]
    floor: float
    label: str
    worst: float = field(init=False)

    def __post_init__(self) -> None:
        self.worst = max(self.values) if self.values else 0.0

    def report(self) -> str:
        if self.nonvacuous:
            return (
                f"VACUITY GATE PASSED -- {self.label}: "
                f"max = {self.worst:.3e} > floor {self.floor:.0e}. "
                f"Proceeding to test the actual prediction."
            )
        return (
            f"*** VACUOUS -- NOT A CONFIRMATION. STOP. ***\n"
            f"  {self.label}: max = {self.worst:.3e}, at or below floor {self.floor:.0e}.\n"
            f"  Any prediction test run on this observable would be satisfied\n"
            f"  trivially (0 = i*0, or equivalent) and carries no information.\n"
            f"  Do not evaluate the prediction. Report VACUOUS and stop here."
        )


def vacuity_gate(
    values: list[float], *, floor: float = 1e-8, label: str = "observable"
) -> VacuityGateResult:
    """First and dominant check: is every value in `values` above `floor`?

    `values` should be magnitudes (already abs'd) of the SAME observable the
    prediction test is about to use — e.g. max|c(v)| over each basis vector
    of an admissible family, NOT a summary statistic of the prediction's own
    deviation (that would test the wrong thing and could pass vacuously for
    the same reason this gate exists to prevent).
    """
    nonvacuous = bool(values) and min(values) > floor
    return VacuityGateResult(nonvacuous=nonvacuous, values=list(values), floor=floor, label=label)
