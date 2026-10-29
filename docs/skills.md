# Skill catalog

The pack contains 30 stable skills. Install the complete pack for the composed workflow. Individual skills include their linked reference files, but the Skills CLI does not automatically install other skills they invoke by name.

Skills marked Explicit declare `disable-model-invocation: true`. Invoke them by name. Skills marked Agent or explicit allow agent selection as well as direct invocation. Agents differ in how they honor this metadata.

## Planning and setup

| Skill | Invocation | Use it to |
| --- | --- | --- |
| [setup-federated-workflow](../skills/engineering/setup-federated-workflow/SKILL.md) | Agent or explicit | Configure one repository, establish a federation, or join an existing one. |
| [ask-smitt](../skills/engineering/ask-smitt/SKILL.md) | Explicit | Choose the skill or flow for the current situation. |
| [grill-with-docs](../skills/engineering/grill-with-docs/SKILL.md) | Explicit | Sharpen an idea with domain modeling against an existing codebase. |
| [wayfinder](../skills/engineering/wayfinder/SKILL.md) | Explicit | Map a large uncertain effort into decision tickets. |
| [to-spec](../skills/engineering/to-spec/SKILL.md) | Explicit | Turn settled planning authority into a specification. |
| [to-tickets](../skills/engineering/to-tickets/SKILL.md) | Explicit | Split accepted authority into self-contained tracer-bullet tickets. |
| [triage](../skills/engineering/triage/SKILL.md) | Explicit | Move incoming requests toward complete executable Agent Briefs. |
| [prototype](../skills/engineering/prototype/SKILL.md) | Agent or explicit | Answer a design question with a throwaway implementation. |
| [research](../skills/engineering/research/SKILL.md) | Agent or explicit | Investigate a question against primary sources and save cited findings. |

## Design and implementation

| Skill | Invocation | Use it to |
| --- | --- | --- |
| [domain-modeling](../skills/engineering/domain-modeling/SKILL.md) | Agent or explicit | Clarify domain language and capture or route Domain Model Deltas. |
| [codebase-design](../skills/engineering/codebase-design/SKILL.md) | Agent or explicit | Design module interfaces, ownership, private decomposition, and test seams. |
| [improve-codebase-architecture](../skills/engineering/improve-codebase-architecture/SKILL.md) | Explicit | Survey a codebase for deepening opportunities before choosing a design. |
| [implement](../skills/engineering/implement/SKILL.md) | Agent or explicit | Implement standalone deliveries or one coordinator-assigned repository scope. |
| [tdd](../skills/engineering/tdd/SKILL.md) | Agent or explicit | Build one vertical slice at a time through public-interface tests. |
| [diagnosing-bugs](../skills/engineering/diagnosing-bugs/SKILL.md) | Agent or explicit | Reproduce, isolate, instrument, and fix a failure with regression evidence. |
| [resolving-merge-conflicts](../skills/engineering/resolving-merge-conflicts/SKILL.md) | Agent or explicit | Resolve an in-progress merge or rebase by understanding both sides. |

## Review and delivery

| Skill | Invocation | Use it to |
| --- | --- | --- |
| [coordinate-delivery](../skills/engineering/coordinate-delivery/SKILL.md) | Explicit | Coordinate one ready ticket through implementation, publication, validation, and human handoff. |
| [code-review](../skills/engineering/code-review/SKILL.md) | Agent or explicit | Review fixed repository targets in Standards, Spec, or combined modes. |
| [review-feedback](../skills/engineering/review-feedback/SKILL.md) | Agent or explicit | Draft or publish human feedback and explicitly return a ticket for correction. |
| [change-walkthrough](../skills/engineering/change-walkthrough/SKILL.md) | Explicit | Explore changes one scenario and logical step at a time. |
| [pr](../skills/engineering/pr/SKILL.md) | Agent or explicit | Write a PR or MR description using repository templates and evidence. |
| [closeout](../skills/engineering/closeout/SKILL.md) | Explicit | Close an accepted delivery and clean up its verified disposable resources. |
| [wizard](../skills/engineering/wizard/SKILL.md) | Agent or explicit | Guide a human through provisioning, credentials, or other manual steps. |

## Thinking and communication

| Skill | Invocation | Use it to |
| --- | --- | --- |
| [grill-me](../skills/productivity/grill-me/SKILL.md) | Explicit | Interview a plan or design without a codebase. |
| [grilling](../skills/productivity/grilling/SKILL.md) | Agent or explicit | Apply the shared questioning discipline directly or through another skill. |
| [handoff](../skills/productivity/handoff/SKILL.md) | Explicit | Transfer decisions and remaining work to another conversation or repository. |
| [teach](../skills/productivity/teach/SKILL.md) | Explicit | Learn over several sessions with local learning records. |
| [to-questionnaire](../skills/productivity/to-questionnaire/SKILL.md) | Explicit | Turn unresolved decisions into questions for the person who can answer. |
| [wait-what](../skills/productivity/wait-what/SKILL.md) | Explicit | Re-explain an answer in simpler language with its missing context. |
| [writing-for-agents](../skills/productivity/writing-for-agents/SKILL.md) | Agent or explicit | Write instructions and reference documents agents can follow. |

## Scope of the public pack

The public pack excludes experimental skills, one-off setup and migration tools, and personal maintenance skills. `ask-smitt` routes through the public collection.

See [credits](credits.md) for the upstream lineage and [the workflow guide](workflow.md) for the complete planning and delivery route.
