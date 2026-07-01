from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_evaluation_report.py"
SPEC = importlib.util.spec_from_file_location("validate_evaluation_report", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class EvaluationReportValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = json.loads(
            (ROOT / "examples" / "sample-evaluation-report.json").read_text(encoding="utf-8")
        )

    def test_sample_report_is_semantically_coherent(self) -> None:
        self.assertEqual(VALIDATOR.semantic_errors(self.report), [])

    def test_release_cannot_claim_not_approved_status(self) -> None:
        report = copy.deepcopy(self.report)
        report["recommendation"]["decision"] = "release"
        report["recommendation"].pop("blockers")
        report["decision"]["release_status"] = "not_approved"
        report["decision"]["conditions"] = []

        errors = VALIDATOR.semantic_errors(report)

        self.assertTrue(any("requires decision.release_status=approved" in error for error in errors))

    def test_release_with_conditions_requires_conditions_and_blockers(self) -> None:
        report = copy.deepcopy(self.report)
        report["recommendation"].pop("blockers")
        report["decision"]["conditions"] = []

        errors = VALIDATOR.semantic_errors(report)

        self.assertTrue(any("requires at least one stated blocker" in error for error in errors))
        self.assertTrue(any("requires at least one release condition" in error for error in errors))

    def test_release_cannot_ignore_high_severity_finding(self) -> None:
        report = copy.deepcopy(self.report)
        report["recommendation"]["decision"] = "release"
        report["recommendation"].pop("blockers")
        report["decision"]["release_status"] = "approved"
        report["decision"]["conditions"] = []

        errors = VALIDATOR.semantic_errors(report)

        self.assertTrue(any("high-severity findings" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
