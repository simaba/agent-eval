# AI Agent Evaluation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Aligned-0055A4?style=flat-square)](https://airc.nist.gov/home)
[![Discussions](https://img.shields.io/badge/Discussions-Join-7289da?style=flat-square&logo=github)](https://github.com/simaba/agent-eval/discussions)

A structured framework for evaluating AI agents across task performance, safety, reliability, and governance dimensions, designed for regulated industry deployment.

---

## Evaluation Dimensions

### 1. Task Performance

| Metric | Description | Measurement Method |
|---|---|---|
| **Task Completion Rate** | % of tasks completed without error | Automated test suite against benchmark scenarios |
| **Goal Achievement Rate** | % of tasks where the final goal was met | Human or LLM judge evaluation |
| **Step Efficiency** | Average steps taken vs. optimal path | Comparison to expert baseline |
| **Tool Use Accuracy** | Correct tool selection and parameter passing | Automated verification |
| **Output Quality** | Correctness and usefulness of agent outputs | Rubric-based LLM judge |

### 2. Safety and Reliability

| Metric | Description | Target |
|---|---|---|
| **Hallucination Rate** | Factually incorrect statements in outputs | < 2% on factual tasks |
| **Harmful Output Rate** | Outputs violating safety guidelines | 0% (hard limit) |
| **Refusal Appropriateness** | Correct refusal of inappropriate requests | > 95% |
| **Prompt Injection Resistance** | Resistance to adversarial user inputs | Tested via red team suite |
| **Consistency** | Same input → consistent output class | > 90% across N runs |

### 3. Operational Reliability

| Metric | Description | Target |
|---|---|---|
| **Availability** | Uptime under normal and peak load | ≥ 99.5% |
| **P99 Latency** | 99th percentile response time | ≤ configured SLA |
| **Error Rate** | % of requests resulting in unhandled errors | < 0.1% |
| **Cost per Task** | Token cost per successful task completion | Tracked against budget |
| **Graceful Degradation** | Behavior when tools or dependencies fail | Tested via fault injection |

### 4. Governance and Auditability

| Metric | Description | Pass Criterion |
|---|---|---|
| **Decision Traceability** | Can every output be traced to inputs and reasoning? | Full trace available |
| **Tool Call Logging** | All external tool calls logged with parameters | 100% logged |
| **Human Escalation Rate** | % of tasks escalated to human review | Tracked; threshold defined |
| **Sensitive Data Handling** | PII/sensitive data not leaked in outputs or logs | 0 violations |
| **Override Capability** | Operator can halt or override agent at any point | Verified in testing |

---

## Evaluation Scenarios

### Standard Benchmark Suite

| Scenario | Description | Difficulty |
|---|---|---|
| Single-step task | Agent completes a straightforward, well-defined task | Basic |
| Multi-step task | Agent plans and executes a sequence of actions | Intermediate |
| Ambiguous instruction | Agent clarifies or handles an underspecified request | Intermediate |
| Tool failure | Agent handles a tool returning an error | Intermediate |
| Adversarial input | Agent resists a prompt injection attempt | Advanced |
| Novel situation | Agent encounters a task outside its training distribution | Advanced |
| Cascading failure | Multiple tools fail in sequence | Advanced |
| Human escalation | Agent correctly identifies when to escalate | Advanced |

### Regulated Industry Scenarios

| Industry | Scenario | Key Evaluation Criteria |
|---|---|---|
| Healthcare | Clinical documentation assistant | Factual accuracy, no hallucination, appropriate refusal |
| Finance | Transaction analysis agent | Regulatory compliance, auditability, no PII leakage |
| Insurance | Claims assessment agent | Fairness across subgroups, decision traceability |
| Legal | Contract review agent | Citation accuracy, scope awareness, human escalation |

---

## Evaluation Report Template

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

## NIST AI RMF Alignment

Full mapping: [docs/nist-rmf-mapping.md](docs/nist-rmf-mapping.md)

Key alignment:
- **MS.1** — AI risk identification: safety and adversarial evaluation scenarios
- **MS.3** — Evaluation techniques: structured benchmark suite
- **MS.5** — Bias measurement: fairness evaluation across subgroups
- **GV.4** — Human oversight: escalation rate tracking and override testing

---

## Ecosystem

| Repository | Purpose |
|---|---|
| [agent-simulator](https://github.com/simaba/agent-simulator) | Simulate agent behavior for evaluation |
| [multi-agent-governance](https://github.com/simaba/multi-agent-governance) | Governance for multi-agent systems |
| [agent-orchestration](https://github.com/simaba/agent-orchestration) | Orchestration patterns and control flow design |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | NIST AI RMF practitioner guide |
| [governance-playbook](https://github.com/simaba/governance-playbook) | Broader enterprise governance operating model |

*Maintained by [Sima Bagheri](https://github.com/simaba) · Connect on [LinkedIn](https://www.linkedin.com/in/simaba/)*
