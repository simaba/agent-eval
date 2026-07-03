# Evaluation Decision Semantics

This framework keeps three concepts separate:

| Concept | Meaning | Where it is recorded |
|---|---|---|
| System risk tier | Overall impact context for the evaluated system and use case | `metadata.risk_tier` (`low`, `medium`, `high`) |
| Scenario or finding severity | Consequence if one specific scenario or failure occurs | `scenarios[].risk` and `findings.failures[].severity` (`low`, `medium`, `high`, `critical`) |
| Decision blocker | An unresolved condition that prevents the current release decision | `recommendation.blockers` |

A high- or critical-severity scenario does not automatically define the whole system's risk tier. Conversely, a high-tier system may include routine lower-severity test scenarios.

## Recommendation fields

- Use `recommendation.blockers` only for unresolved items that prevent the current decision.
- Use `recommendation.required_actions` for follow-up work accepted as part of a bounded conditional approval.
- Use `decision.conditions` for the named, accountable constraints of that conditional approval.

A report with `release_with_conditions` must not claim unresolved blockers. It must instead state the required actions and release conditions that named owners have accepted.

## Validator rules

- A plain `release` cannot include blockers, required actions, or conditions.
- A high-severity finding prevents an unconditional `release`.
- A critical finding requires `do_not_release`.
- `do_not_release` requires either a stated blocker or at least one critical finding.

These rules make report logic internally coherent. They are practitioner controls, not a substitute for organization-specific release authority, legal review, safety analysis, or compliance decisions.
