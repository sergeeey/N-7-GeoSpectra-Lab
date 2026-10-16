r"""
Negative control -- a mandatory companion to any check whose PASS is going to
be quoted as evidence, added 2026-09-07 after the C179-C182 round sequence
produced FIVE checks that could not fail by construction (pearl_registry
2026-09-07, impact 7). In every one of the five the underlying physics was
correct; what failed was the machinery built to establish it. Three were found
by external context-blind skeptics AFTER the round had declared itself done,
one by a control deliberately placed in the script, one by a corrupted-input
replay. Self-review caught none of the five.

THE RULE, restated as code instead of prose so it cannot be silently skipped:

    for every check whose PASS you intend to quote --
        run the SAME check on an input for which it MUST report failure.
        control also passes?  ->  the check discriminates NOTHING. Not evidence.
        control fails as it must ->  the check has falsifying power. Quote it.

The control's outcome is written into the results JSON as a BOOLEAN, not
eyeballed in stdout. `scripts/check_negative_control.py` reads that boolean;
a round whose results carry no such record is flagged before the round closes,
which is the whole point -- the defects above surfaced too late precisely
because nothing mechanical asked the question.

USAGE

    from negative_control import negative_control

    def check(spectrum):                     # your own check, returns bool
        return solve(spectrum) == expected

    nc = negative_control(
        check,
        real=observed_spectrum,
        controls={
            "every eigenvalue shifted by +1": shift(observed_spectrum, 1.0),
            "one multiplicity broken":        break_multiplicity(observed_spectrum),
        },
        label="connection-constant solve",
    )
    print(nc.report())
    res["negative_control"] = nc.as_dict()   # <- the boolean the checker reads
    # ... and do not quote the check as evidence unless nc.discriminates ...

CHOOSING THE CONTROL INPUT -- the part that is easy to get wrong

The control must break the SPECIFIC property the check claims to be sensitive
to, not merely be "different data". Two failure shapes seen in this project:

  * TOO WEAK -- C180's multiplicity check was fed only genuine su(2) data. The
    pattern (k+1)(k+2)/k(k+1) is forced by ANY su(2) generator set, so no
    su(2)-derived control could ever have exposed it; the control had to come
    from outside that family.
  * SAME OBJECT TWICE -- C181's discrimination test ranked the same matrix
    twice and called the two ranks different objects. A control that is a
    relabelling of the real input is not a control.

A control the check passes is a RESULT, not a bug in the control: it means the
check does not discriminate. Record it (`discriminates: false`) and withdraw
the check as evidence -- do not tune the control until the check looks good.

SCOPE -- what this helper does NOT do

It cannot tell whether the control input you chose is genuinely adversarial;
that stays a human/skeptic judgement. It makes the question unskippable and
the answer machine-readable. See `docs/negative_control_pattern.md`.
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from typing import Any


@dataclass
class NegativeControlResult:
    label: str
    passed_on_real: bool
    control_outcomes: dict[str, bool]
    deterministic_on_rerun: bool = True
    discriminates: bool = field(init=False)
    surviving_controls: list[str] = field(init=False)

    def __post_init__(self) -> None:
        self.surviving_controls = sorted(
            name for name, passed in self.control_outcomes.items() if passed
        )
        self.discriminates = bool(
            self.passed_on_real
            and self.control_outcomes
            and not self.surviving_controls
            and self.deterministic_on_rerun
        )

    def as_dict(self) -> dict[str, Any]:
        """The canonical block to store under `results[...]['negative_control']`."""
        return {
            "check": self.label,
            "passed_on_real": bool(self.passed_on_real),
            "control_inputs": {k: bool(v) for k, v in self.control_outcomes.items()},
            "controls_that_also_passed": list(self.surviving_controls),
            "deterministic_on_rerun": bool(self.deterministic_on_rerun),
            "discriminates": bool(self.discriminates),
        }

    def report(self) -> str:
        if not self.control_outcomes:
            return (
                f"*** NO CONTROL RUN -- {self.label}: `controls` was empty. ***\n"
                f"  A check with no negative control is not evidence. Supply at\n"
                f"  least one input for which the check MUST report failure."
            )
        if not self.deterministic_on_rerun:
            return (
                f"*** CHECK IS NOT A FUNCTION OF ITS INPUT -- NOT EVIDENCE. ***\n"
                f"  {self.label} gave two different answers on the SAME real input,\n"
                f"  so the control results below say nothing about the input at all:\n"
                f"  a check driven by call order or hidden state produces a clean\n"
                f"  pass/fail split without ever inspecting what it was given.\n"
                f"  Fix the check (seed any RNG, remove the state), then re-run."
            )
        if not self.passed_on_real:
            return (
                f"CHECK FAILED ON THE REAL INPUT -- {self.label}.\n"
                f"  The negative control is moot: report the failure itself."
            )
        if self.surviving_controls:
            survivors = ", ".join(repr(s) for s in self.surviving_controls)
            return (
                f"*** CANNOT-FAIL CHECK -- NOT EVIDENCE. ***\n"
                f"  {self.label} passed on the real input AND on {survivors}.\n"
                f"  It therefore discriminates nothing and must not be quoted in\n"
                f"  support of any claim. Record discriminates: false and withdraw\n"
                f"  the check -- do not weaken the control until the check passes."
            )
        n = len(self.control_outcomes)
        return (
            f"NEGATIVE CONTROL PASSED -- {self.label}: check holds on the real "
            f"input and fails on all {n} control input(s). It has falsifying power."
        )


def negative_control(
    check: Callable[[Any], bool],
    *,
    real: Any,
    controls: Mapping[str, Any],
    label: str = "check",
) -> NegativeControlResult:
    """Run `check` on the real input and on each deliberately-broken input.

    `check` must be the SAME callable used for the real verdict -- re-implementing
    it for the control tests what the re-implementation does, not what the check
    does, and is how C181's discrimination test ended up ranking one matrix twice.

    `controls` maps a human-readable description of the corruption to the
    corrupted input. Describe what was BROKEN ("one multiplicity broken"), not
    what the input is ("case 2"); the description is what a later reader uses to
    judge whether the control was adversarial enough.

    `check` is called on the real input TWICE -- once before the controls and
    once after -- and the two answers must agree.

    WHY: without the re-run, a check that ignores its argument entirely and
    answers from call order or hidden state (`return self.n == 1`) produces
    exactly the pattern this helper reads as success -- pass on the real input,
    fail on every control -- and would be certified as having falsifying power.
    Found by an independent context-blind review of this file and reproduced
    before the fix. A stochastic check will also trip the re-run: that is
    correct, not a false alarm. Seed it, or its control results are not
    trustworthy either.
    """
    passed_first = bool(check(real))
    outcomes = {name: bool(check(inp)) for name, inp in controls.items()}
    passed_again = bool(check(real))
    return NegativeControlResult(
        label=label,
        passed_on_real=passed_first,
        control_outcomes=outcomes,
        deterministic_on_rerun=(passed_again == passed_first),
    )
