#!/usr/bin/env python3
"""Validate an AI-agent evaluation report beyond its JSON Schema shape.

The JSON Schema checks field types and allowed values. This utility adds the
cross-field rules needed to keep a recommendation, release status, conditions,
required actions, decision blockers, and material findings internally coherent.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


RECOMMENDATION_TO_RELEASE_STATUS = {
    "release": "approved",
    "release_with_conditions": "approved_with_conditions",
    "do_not_release": "not_approved",
}


def load_json(path: str | Path) -> dict[str, Any]:
    """Load one JSON object with a useful user-facing error."""
    source = Path(path)
    try:
        payload = json.loads(source.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"could not read {source}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {source}: {exc.msg}") from exc

    if not isinstance(payload, dict):
        raise ValueError(f"{source} must contain a JSON object")
    return payload


def schema_errors(schema: dict[str, Any], report: dict[str, Any]) -> list[str]:
    """Return readable Draft 2020-12 schema and date-format validation errors."""
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(report), key=lambda error: list(error.path))
    messages = []
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "<root>"
        messages.append(f"{location}: {error.message}")
    return messages


def semantic_errors(report: dict[str, Any]) -> list[str]:
    """Return cross-field consistency errors after schema validation succeeds.

    A *severity* states the consequence of a finding. A *blocker* is a decision
    status: unresolved blockers prevent the current release decision. Required
    actions may exist on a conditional approval, but they are not blockers once
    the accountable owners have accepted the bounded conditions.
    """
    recommendation = report["recommendation"]
    decision = report["decision"]
    recommendation_decision = recommendation["decision"]
    release_status = decision["release_status"]
    expected_status = RECOMMENDATION_TO_RELEASE_STATUS[recommendation_decision]
    errors: list[str] = []

    if release_status != expected_status:
        errors.append(
            "recommendation.decision={} requires decision.release_status={}".format(
                recommendation_decision,
                expected_status,
            )
        )

    blockers = recommendation.get("blockers", [])
    required_actions = recommendation.get("required_actions", [])
    conditions = decision["conditions"]
    severities = [failure["severity"] for failure in report["findings"]["failures"]]
    has_high = "high" in severities
    has_critical = "critical" in severities

    if recommendation_decision == "release":
        if blockers:
            errors.append("recommendation.decision=release must not include unresolved blockers")
        if required_actions:
            errors.append("recommendation.decision=release must not include unresolved required_actions")
        if conditions:
            errors.append("decision.release_status=approved must not include release conditions")

    if recommendation_decision == "release_with_conditions":
        if blockers:
            errors.append(
                "release_with_conditions is incompatible with unresolved blockers; "
                "use required_actions and decision.conditions for bounded follow-up"
            )
        if not required_actions and not conditions:
            errors.append(
                "release_with_conditions requires at least one stated required_action or release condition"
            )
        if not conditions:
            errors.append("approved_with_conditions requires at least one release condition")

    if recommendation_decision == "do_not_release" and not blockers and not has_critical:
        errors.append("do_not_release requires at least one stated blocker or critical finding")

    if has_high and recommendation_decision == "release":
        errors.append("recommendation.decision=release is incompatible with unresolved high-severity findings")
    if has_critical and recommendation_decision != "do_not_release":
        errors.append("critical findings require recommendation.decision=do_not_release")

    return errors


def validate(schema_path: str | Path, report_path: str | Path) -> list[str]:
    """Validate a report schema, formats, and semantic decision coherence."""
    schema = load_json(schema_path)
    report = load_json(report_path)
    errors = schema_errors(schema, report)
    if errors:
        return errors
    return semantic_errors(report)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 2:
        print(
            "Usage: python tools/validate_evaluation_report.py <schema.json> <report.json>",
            file=sys.stderr,
        )
        return 2

    try:
        errors = validate(args[0], args[1])
    except ValueError as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        return 2

    if errors:
        print("Evaluation report is invalid:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Evaluation report is schema-valid, date-valid, and semantically coherent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
