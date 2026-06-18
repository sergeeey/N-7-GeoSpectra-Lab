#!/usr/bin/env python
"""Scaffold a new HAI-OS v0.3 task instance from templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "docs" / "hai-os" / "templates"
INSTANCES = ROOT / "docs" / "hai-os" / "instances"

TEMPLATE_FILES = (
    "task_passport.yaml",
    "context_map.yaml",
    "strategy_card.yaml",
    "work_log.yaml",
    "verification_report.yaml",
    "decision_record.yaml",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create HAI-OS v0.3 instance folder")
    parser.add_argument("instance_id", help="e.g. gate5_planning")
    args = parser.parse_args()

    target = INSTANCES / args.instance_id
    if target.exists():
        print(f"Already exists: {target}")
        return 1

    target.mkdir(parents=True)
    for name in TEMPLATE_FILES:
        shutil.copy2(TEMPLATES / name, target / name)

    readme = target / "README.txt"
    readme.write_text(
        f"HAI-OS instance: {args.instance_id}\n"
        "Fill templates in order: task_passport -> context_map -> strategy_card -> "
        "work_log -> verification_report -> decision_record\n",
        encoding="utf-8",
    )
    print(f"Created: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
