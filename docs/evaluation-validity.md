# Evaluation Validity and Evidence Design

An evaluation can be internally consistent and still support the wrong conclusion. This guide describes the evidence questions that should be answered before a score is treated as a product, safety, or release signal.

## Start from the decision

Define the decision the evaluation is intended to support:

- continue prototyping;
- compare two configurations;
- enter a bounded pilot;
- expand a pilot population;
- approve a particular tool permission;
- hold or roll back a release;
- retire a model, prompt, tool, or workflow.

A benchmark without a decision context often accumulates convenient metrics rather than decision-relevant evidence.

## Define the unit of analysis

State exactly what one observation represents:

- one model response;
- one end-to-end task attempt;
- one user journey;
- one tool invocation;
- one conversation;
- one incident window;
- one repeated run of a fixed scenario.

Do not mix units in one denominator. For example, “failure rate” is ambiguous when some records are messages, others are tasks, and others are conversations.

## Specify the target population

A scenario set is a sample from an intended operating environment. Document:

- user groups and languages;
- task categories and frequency assumptions;
- tool and data-access conditions;
- normal, ambiguous, adversarial, failure, and out-of-distribution cases;
- exclusions;
- known differences between the evaluation sample and expected use.

A balanced benchmark can be useful for finding failures but may not estimate production frequency. A production-shaped sample can estimate prevalence but may underrepresent rare critical cases. Use separate suites when those purposes conflict.

## Separate coverage from prevalence

Report both:

1. **coverage:** which risk, task, and failure classes were exercised;
2. **prevalence-weighted performance:** results under an explicit operating-distribution assumption.

Do not average a rare catastrophic scenario with routine tasks and call the result “overall safety.” Hard gates, scenario-level reporting, and residual-risk review are more appropriate for non-compensable harms.

## Operationalize each metric

For every metric, record:

| Field | Question |
|---|---|
| Construct | What property are we trying to understand? |
| Operational definition | What observable event counts as success or failure? |
| Unit | Response, task, conversation, user, run, or time window? |
| Denominator | Which attempted cases are included or excluded? |
| Evaluator | Rule, test, expert, user, or model judge? |
| Error modes | How can the measurement itself be wrong? |
| Decision use | Which decision changes if the metric moves? |

Labels such as “hallucination,” “quality,” “helpfulness,” and “safety” are not measurements until their decision rules are specified.

## Evaluator validity

### Deterministic checks

Use executable checks for properties that can be observed directly: schema validity, prohibited tool calls, citation presence, exact constraints, timeout behavior, or unauthorized state changes.

A deterministic check can be precise and still be incomplete. Passing it does not imply semantic correctness.

### Human review

Define reviewer qualifications, instructions, adjudication, and blinding where relevant. Measure agreement on a representative sample before interpreting reviewer labels as stable ground truth.

Raw agreement alone can be misleading when one label dominates. Report the confusion pattern and adjudication rate, not only a single coefficient.

### Model judges

A model judge is a measurement instrument, not an authority. Before using it for consequential conclusions:

- define the rubric independently of the judged outputs;
- test order, verbosity, style, and self-preference effects;
- compare against qualified human review on representative and difficult cases;
- record judge model, prompt, configuration, and version;
- preserve disagreement and adjudication rather than silently averaging it away;
- avoid using the same model family as generator and sole judge when correlated errors matter.

Do not describe an LLM-judge score as objective or ground truth.

## Repeated runs and dependence

Agent behavior can vary across repeated attempts, but repeated outputs from the same scenario are not automatically independent observations.

Record:

- run count per scenario;
- sampling and seed policy where applicable;
- model, prompt, retrieval, tools, permissions, and environment versions;
- cache and state behavior;
- whether failures cluster by scenario, user journey, or dependency.

Report scenario-level variability and worst-case recurrence, not only the mean across all attempts.

## Uncertainty

Use confidence intervals or other uncertainty summaries when estimating a rate or mean from a sample. Also report sources of uncertainty that statistical intervals do not capture:

- scenario-selection bias;
- incomplete coverage;
- evaluator error;
- distribution shift;
- version drift;
- hidden tool or retrieval state;
- small counts for critical slices.

A narrow interval around a biased benchmark is still misleading.

For a zero-observed-failure result, report the sample count and an upper bound or plain-language limitation. “0 observed in 50 cases” is not evidence of zero risk.

## Threshold design

Thresholds should come from the decision context, not from a generic table.

A threshold record should include:

- decision and owner;
- affected population and harm model;
- baseline or comparator;
- measurement method and uncertainty;
- hard gates that cannot be traded off;
- quality or operational thresholds that can be optimized;
- minimum sample and slice requirements;
- exception and residual-risk process;
- expiry or review trigger.

Avoid universal targets such as “hallucination below 2%” without defining the task distribution, severity, evaluator, and confidence required.

## Slice analysis

Predefine slices that can reveal concentrated failure:

- language or locale;
- user or task type;
- ambiguity level;
- tool permission;
- data sensitivity;
- retrieval quality;
- input length;
- dependency failure mode;
- safety or policy boundary;
- accessibility need.

Do not search hundreds of slices after the fact and report only the worst or best without disclosing the search. Exploratory slice discovery should lead to a versioned confirmatory test set.

## Comparison design

For model, prompt, or harness comparisons:

- keep task, tools, permissions, and evaluator conditions equivalent;
- use paired analysis when the same scenarios are attempted by both systems;
- randomize presentation order for subjective judging;
- report missing and failed runs rather than dropping them;
- distinguish statistical difference from operational significance;
- account for multiple comparisons when many variants are tested;
- preserve version and cost context.

A leaderboard number is not meaningful when the systems received different authority, context, or recovery paths.

## Failure review

Aggregate scores are navigation aids. Review failures as evidence.

For material failures, preserve:

- scenario and run identifiers;
- input and relevant context;
- tool trace and system state;
- evaluator result and disagreement;
- failure taxonomy and severity rationale;
- containment or remediation;
- regression test created;
- owner and disposition.

Separate root-cause hypotheses from confirmed causes.

## Release evidence package

A defensible evaluation package should make it possible for another reviewer to answer:

1. What system and version were tested?
2. What decision was being supported?
3. What operating population did the scenarios represent?
4. Which critical conditions were intentionally oversampled?
5. How were outcomes measured and how reliable were the evaluators?
6. What uncertainty and exclusions remain?
7. Which hard gates failed or passed?
8. Which residual risks were accepted, by whom, and under what conditions?
9. What changes invalidate the result and trigger regression testing?

The package supports accountable judgment. It does not automate release authority or prove safety.
