# AI Agent Evaluation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-0055A4?style=flat-square)](https://airc.nist.gov/home)
[![Discussions](https://img.shields.io/badge/Discussions-Join-7289da?style=flat-square&logo=github)](https://github.com/simaba/agent-eval/discussions)

A structured framework for evaluating AI agents across task performance, safety, reliability, and governance dimensions, designed for regulated-industry deployment.

---

## Choose this repo when

Use this repository when you need **measurement and pass/fail logic** for AI agents:

- what to measure
- which scenarios to test
- how to score performance, safety, and reliability
- what should appear in an evaluation report

Do **not** start here if you need the oversight model. Use [`multi-agent-governance`](https://github.com/simaba/multi-agent-governance).

Do **not** start here if you need orchestration patterns. Use [`agent-orchestration`](https://github.com/simaba/agent-orchestration).

Do **not** start here if you want runnable behavior. Use [`agent-simulator`](https://github.com/simaba/agent-simulator).

---

## Evaluation dimensions

### 1. Task performance

| Metric | Description | Measurement Method |
|---|---|---|
| **Task Completion Rate** | % of tasks completed without error | automated test suite against benchmark scenarios |
| **Goal Achievement Rate** | % of tasks where the final goal was met | human or LLM-judge evaluation |
| **Step Efficiency** | average steps taken vs. optimal path | comparison to expert baseline |
| **Tool Use Accuracy** | correct tool selection and parameter passing | automated verification |
| **Output Quality** | correctness and usefulness of agent outputs | rubric-based judging |

### 2. Safety and reliability

| Metric | Description | Target |
|---|---|---|
| **Hallucination Rate** | factually incorrect statements in outputs | < 2% on factual tasks |
| **Harmful Output Rate** | outputs violating safety guidelines | 0% hard limit |
| **Refusal Appropriateness** | correct refusal of inappropriate requests | > 95% |
| **Prompt Injection Resistance** | resistance to adversarial inputs | tested via red-team suite |
| **Consistency** | same input produces the same output class | > 90% across repeated runs |

### 3. Operational reliability

| Metric | Description | Target |
|---|---|---|
| **Availability** | uptime under normal and peak load | ≥ 99.5% |
| **P99 Latency** | 99th-percentile response time | ≤ configured SLA |
| **Error Rate** | % of requests ending in unhandled errors | < 0.1% |
| **Cost per Task** | token cost per successful task | tracked against budget |
| **Graceful Degradation** | behavior when tools or dependencies fail | tested via fault injection |

### 4. Governance and auditability

| Metric | Description | Pass Criterion |
|---|---|---|
| **Decision Traceability** | can every output be traced to inputs and reasoning? | full trace available |
| **Tool Call Logging** | all external tool calls logged with parameters | 100% logged |
| **Human Escalation Rate** | % of tasks escalated to human review | tracked with threshold defined |
| **Sensitive Data Handling** | PII or sensitive data not leaked in outputs or logs | 0 violations |
| **Override Capability** | operator can halt or override agent behavior | verified in testing |

---

## Evaluation scenarios

### Standard benchmark suite

| Scenario | Description | Difficulty |
|---|---|---|
| Single-step task | straightforward, well-defined task | Basic |
| Multi-step task | sequence of actions with intermediate dependencies | Intermediate |
| Ambiguous instruction | underspecified request requiring clarification | Intermediate |
| Tool failure | dependent tool returns an error | Intermediate |
| Adversarial input | prompt injection or manipulation attempt | Advanced |
| Novel situation | task outside the usual distribution | Advanced |
| Cascading failure | multiple dependencies fail in sequence | Advanced |
| Human escalation | agent should recognize the need to escalate | Advanced |

### Regulated-industry scenarios

| Industry | Scenario | Key Evaluation Criteria |
|---|---|---|
| Healthcare | clinical documentation assistant | factual accuracy, refusal quality, low hallucination |
| Finance | transaction-analysis agent | compliance, auditability, no PII leakage |
| Insurance | claims-assessment agent | fairness, traceability, escalation quality |
| Legal | contract-review agent | citation accuracy, scope awareness, human escalation |

---

## Evaluation report template

```markdown
## AI Agent Evaluation Report

**Agent:** [Agent Name and Version]
**Evaluation Date:** [Date]
**Evaluator:** [Name / Team]
**Environment:** [Staging / Production]

### Summary
| Dimension | Score | Pass/Fail |
|---|---|---|
| Task Performance | X% | ✅ / ❌ |
| Safety & Reliability | X% | ✅ / ❌ |
| Operational Reliability | Xms P99 | ✅ / ❌ |
| Governance & Auditability | X/4 criteria | ✅ / ❌ |

### Findings
[Describe key findings, failures, and anomalies]

### Recommendations
[List specific actions required before production deployment]

### Sign-Off
- [ ] Technical Owner: _________________
- [ ] AI Governance Lead: _________________
- [ ] Legal/Compliance (if high-risk): _________________
```

---

## NIST AI RMF alignment

Full mapping: [docs/nist-rmf-mapping.md](docs/nist-rmf-mapping.md)

Key alignment:

- **MS.1**: AI risk identification through safety and adversarial scenarios
- **MS.3**: structured evaluation techniques and benchmark design
- **MS.5**: subgroup and fairness measurement
- **GV.4**: human oversight via escalation and override checks

---

## Related repositories

| Repository | What it adds |
|---|---|
| [`multi-agent-governance`](https://github.com/simaba/multi-agent-governance) | oversight model, trust structure, accountability controls |
| [`agent-orchestration`](https://github.com/simaba/agent-orchestration) | control-flow patterns and orchestration logic |
| [`agent-simulator`](https://github.com/simaba/agent-simulator) | runnable execution and failure-mode examples |
| [`nist-rmf-guide`](https://github.com/simaba/nist-rmf-guide) | practitioner guide for broader RMF implementation |
| [`governance-playbook`](https://github.com/simaba/governance-playbook) | enterprise operating model beyond agent evaluation |

*Maintained by [Sima Bagheri](https://github.com/simaba) · Connect on [LinkedIn](https://www.linkedin.com/in/simaba/)*
