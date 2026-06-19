#!/usr/bin/env python3
"""Run HYP_01–HYP_03 toy experiments and write report."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cc_toy_lab.compactification.hypothesis_runner import (
    run_all_hypothesis_experiments,
    write_hypothesis_report,
)


def main() -> None:
    result = run_all_hypothesis_experiments()
    path = write_hypothesis_report(result)
    print(f"Wrote {path}")
    print(f"HYP_01 coupled: {result.coupled_hyp01.status}")
    print(f"HYP_01 falsifier: {result.falsifier_hyp01.status}")
    print(f"HYP_02: {result.hyp02_unit.status}")
    print(f"HYP_03: {result.hyp03.status}")


if __name__ == "__main__":
    main()
