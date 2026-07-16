# AI Agent Evaluation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Informed-0055A4?style=flat-square)](https://airc.nist.gov/home)

A practitioner framework for designing, recording, and reviewing agent evaluations without collapsing coverage, measurement validity, hard gates, and release judgment into one score.

The repository provides a human-readable report template, a machine-readable schema, a semantic validator, fictional examples, and guidance on evaluation validity. It is not a benchmark leaderboard or a source of universal pass thresholds.

## The central idea

An evaluation result is only useful when five things are explicit:

1. **the decision it supports** — prototype, compare, pilot, expand, hold, roll back, or retire;
2. **the operating population it represents** — users, tasks, languages, tools, permissions, and exclusions;
3. **the measurement instrument** — executable rule, expert review, user outcome, or model judge;
4. **the uncertainty and coverage limits** — sample size, evaluator error, slice gaps, version drift, and scenario bias;
5. **the decision semantics** — hard gate, quality threshold, required action, condition, blocker, or accepted residual risk.

Without those elements, a precise-looking score can be less informative than a small set of well-investigated failures.

## Start here

| Artifact | Use it for |
|---|---|
| [`docs/evaluation-validity.md`](docs/evaluation-validity.md) | Designing evidence that can support a stated decision |
| [`docs/decision-semantics.md`](docs/decision-semantics.md) | Keeping risk tier, finding severity, blockers, required actions, conditions, and release decisions distinct |
| [`templates/evaluation-report.md`](templates/evaluation-report.md) | Human review and sign-off discussion |
| [`schemas/evaluation-report.schema.json`](schemas/evaluation-report.schema.json) | Machine-readable evaluation records |
| [`examples/sample-evaluation-report.json`](examples/sample-evaluation-report.json) | Fictional structured example |
| [`tools/validate_evaluation_report.py`](tools/validate_evaluation_report.py) | Schema and decision-coherence validation |

## What the framework evaluates

The dimensions below are categories for designing measurements. They are not automatically valid metrics.

### Task and outcome performance

- end-to-end task completion;
- correctness against a defined reference or acceptance rule;
- user or workflow outcome;
- tool selection and parameter accuracy;
- correction and recovery behavior;
- unnecessary step or interaction cost.

### Safety, privacy, and policy behavior

- prohibited action or tool invocation;
- sensitive-data exposure or inappropriate retention;
- refusal, deferral, and escalation at defined boundaries;
- prompt-injection and untrusted-content handling;
- behavior under conflicting instructions;
- containment after a control or dependency failure.

### Operational reliability

- latency and timeout behavior under stated load;
- unhandled and handled failure rates;
- retry, fallback, and circuit-breaker behavior;
- dependency and tool degradation;
- cost and resource consumption;
- recovery time and state consistency.

### Governance and auditability

- decision and tool-call provenance;
- version and permission traceability;
- human override and stop mechanisms;
- evidence retention with privacy controls;
- owner, review, and residual-risk records;
- regression triggers after material change.

## Metrics need operational definitions

Terms such as “hallucination,” “helpfulness,” “safety,” “consistency,” and “quality” are not self-defining.

For each metric, record:

| Field | Example question |
|---|---|
| Construct | What property are we trying to understand? |
| Observable rule | What exactly counts as success or failure? |
| Unit | Response, task, conversation, tool call, user, or time window? |
| Denominator | Which attempts are included, excluded, or missing? |
| Evaluator | Rule, test, expert, user, or model judge? |
| Instrument error | How can the evaluator itself be wrong? |
| Decision use | Which action changes if the metric moves? |

Do not reuse a percentage target across systems unless the population, unit, evaluator, severity model, and decision context are comparable.

## Evaluation suite design

A credible suite usually separates several purposes:

| Suite | Primary purpose |
|---|---|
| Operating-distribution sample | Estimate routine performance under stated workload assumptions |
| Critical-risk suite | Oversample rare, high-consequence conditions and hard gates |
| Boundary suite | Test ambiguity, refusal, escalation, and policy transitions |
| Fault-injection suite | Exercise tool, retrieval, network, permission, and state failures |
| Regression suite | Preserve previously discovered failures and important invariants |
| Exploratory suite | Discover new slices and failure modes; not used alone for release claims |

A balanced challenge set may be good at finding failures but unsuitable for estimating production prevalence. Report coverage and prevalence-weighted performance separately.

## Evaluator hierarchy

Use the simplest evaluator capable of measuring the property.

1. **Executable checks** for directly observable invariants such as schema validity, unauthorized tool use, state mutation, citation presence, or timeout behavior.
2. **Qualified human review** for domain judgment, consequential ambiguity, and disputed failures.
3. **Model judges** for scalable rubric application only after calibration against representative human review and explicit testing for order, style, self-preference, and verbosity effects.

A model-judge result is an instrument reading, not ground truth. Record the judge model, prompt, configuration, version, agreement, and adjudication process.

## Repeated runs and uncertainty

For nondeterministic systems, report:

- attempts per scenario;
- run and seed policy where applicable;
- model, prompt, retrieval, tool, permission, and environment versions;
- missing or failed runs;
- scenario-level recurrence and variability;
- uncertainty intervals for estimated rates or means;
- coverage gaps and evaluator limitations that statistical intervals do not capture.

“Zero observed failures” must include the number of opportunities and a plain-language limit. Zero failures in a small sample is not evidence of zero risk.

## Slice analysis

Predefine decision-relevant slices such as:

- language or locale;
- task and user type;
- ambiguity level;
- tool authority and permission scope;
- data sensitivity;
- retrieval quality;
- accessibility need;
- dependency failure mode;
- safety or policy boundary.

Exploratory slicing can discover problems, but a post-hoc search across many slices should not be presented as confirmatory evidence without disclosure and follow-up testing.

## Threshold and gate design

This repository intentionally does not prescribe universal values such as a fixed hallucination rate, refusal rate, availability target, or latency objective.

A threshold should record:

- decision owner and intended decision;
- baseline or comparator;
- affected population and harm model;
- measurement method and uncertainty;
- minimum sample and slice coverage;
- non-compensable hard gates;
- quality or operational targets that may be optimized;
- exception and residual-risk process;
- expiry or review trigger.

A weighted aggregate must never hide a failed hard gate or an unresolved critical finding.

## Decision semantics

The schema and validator keep these concepts separate:

| Concept | Meaning |
|---|---|
| System risk tier | impact context for the evaluated system and use case |
| Scenario / finding severity | consequence of a specific failure |
| Blocker | unresolved condition that prevents the current decision |
| Required action | follow-up work accepted under a bounded conditional decision |
| Condition | explicit constraint attached to that decision |
| Residual risk | remaining uncertainty or harm accepted by a named authority |

See [`docs/decision-semantics.md`](docs/decision-semantics.md) for the validator rules.

## Validation

The validator checks schema conformance and selected decision coherence:

```bash
python tools/validate_evaluation_report.py \
  schemas/evaluation-report.schema.json \
  examples/sample-evaluation-report.json
```

It can catch contradictions such as an unconditional release with unresolved blockers. It cannot determine whether the benchmark is representative, the evaluator is valid, the threshold is justified, or the residual risk is acceptable.

## Failure review

Do not stop at the scorecard. For material failures, preserve:

- scenario and run identifiers;
- relevant input, context, and tool trace;
- evaluator result and disagreement;
- severity rationale;
- containment and remediation;
- root-cause hypothesis versus confirmed cause;
- regression test created;
- owner and disposition.

The failure corpus often becomes more valuable than the original aggregate score.

## Maturity and scope

This is a practitioner evaluation framework with working schema and semantic validation. It is useful for structured reviews, evaluation-plan design, fictional examples, and future automation. It is not a certified benchmark, safety case, regulatory assessment, or substitute for qualified domain, security, privacy, legal, compliance, or release authority.

References to NIST AI RMF or regulated-industry concerns are practitioner mappings. Verify official sources and adapt the framework to the actual system, population, jurisdiction, and failure tolerance.

## Related repositories

| Repository | Distinct role |
|---|---|
| [`agent-simulator`](https://github.com/simaba/agent-simulator) | runnable bounded-agent behavior and failure paths |
| [`agent-orchestration`](https://github.com/simaba/agent-orchestration) | control-flow patterns |
| [`multi-agent-governance`](https://github.com/simaba/multi-agent-governance) | authority, oversight, containment, and accountability |
| [`automotive-llm-eval-harness`](https://github.com/simaba/automotive-llm-eval-harness) | compact scorer for synthetic automotive evaluation artifacts |

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
