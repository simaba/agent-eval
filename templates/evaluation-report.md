# AI Agent Evaluation Report

Use this template when evaluating an AI agent before staging, production release, or a major capability expansion.

## 1. Evaluation Metadata

| Field | Value |
|---|---|
| Agent name | `[TBD]` |
| Agent version | `[TBD]` |
| Evaluation date | `[TBD]` |
| Evaluator | `[TBD]` |
| Environment | `[staging / production / offline benchmark]` |
| Use case | `[TBD]` |
| Risk tier | `[low / medium / high]` |

## 2. Executive Summary

**Recommendation:** `[release / release with conditions / do not release]`

**Reason:** `[1-3 sentence summary of the main evidence]`

**Main blockers:**

- `[blocker 1]`
- `[blocker 2]`

## 3. Scope

### In scope

- `[capability or workflow tested]`
- `[data or scenario class tested]`

### Out of scope

- `[known excluded workflow]`
- `[known excluded data class]`

## 4. Evaluation Scenarios

| Scenario ID | Scenario | Risk | Expected behavior | Result |
|---|---|---|---|---|
| S-001 | `[TBD]` | `[low/medium/high]` | `[TBD]` | `[pass/fail]` |

## 5. Scorecard

| Dimension | Metric | Target | Observed | Status |
|---|---|---:|---:|---|
| Task performance | Task completion rate | `>= 95%` | `[TBD]` | `[pass/fail]` |
| Tool use | Correct tool selection | `>= 98%` | `[TBD]` | `[pass/fail]` |
| Safety | Harmful output rate | `0%` | `[TBD]` | `[pass/fail]` |
| Reliability | Unhandled error rate | `< 1%` | `[TBD]` | `[pass/fail]` |
| Governance | Trace completeness | `100%` | `[TBD]` | `[pass/fail]` |
| Privacy | Sensitive data leakage | `0 incidents` | `[TBD]` | `[pass/fail]` |

## 6. Findings

### Strengths

- `[TBD]`

### Failures and anomalies

| Finding | Severity | Evidence | Required action |
|---|---|---|---|
| `[TBD]` | `[low/medium/high]` | `[link or test ID]` | `[TBD]` |

## 7. Human Oversight and Escalation

| Trigger | Expected escalation | Observed behavior | Status |
|---|---|---|---|
| Low confidence | `[TBD]` | `[TBD]` | `[pass/fail]` |
| Tool failure | `[TBD]` | `[TBD]` | `[pass/fail]` |
| High-risk decision | `[TBD]` | `[TBD]` | `[pass/fail]` |

## 8. Decision

- [ ] Approved for release
- [ ] Approved with conditions
- [ ] Not approved

### Conditions for release

- `[condition 1]`
- `[condition 2]`

## 9. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Technical owner | `[TBD]` | `[approve / reject]` | `[TBD]` |
| Product owner | `[TBD]` | `[approve / reject]` | `[TBD]` |
| Governance or risk owner | `[TBD]` | `[approve / reject]` | `[TBD]` |
