"""Tests for the S3 parity formalization summary."""

from __future__ import annotations

from s3_kronecker_skeleton import s3_parity_formalization_summary


def test_parity_formalization_summary_preserves_s3_fence() -> None:
    """The parity formalization must stay within the S3 smoke fence."""

    summary = s3_parity_formalization_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["formalized_candidate"] == "P2 coordinate-swap smoke candidate"
    assert summary["formalized_verdict"] == "passed"
    assert summary["parity_summary"]["results"]["P2"].status == "passed"

