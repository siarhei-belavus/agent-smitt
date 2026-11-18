# Diagnose selected work

Use the supplied evidence to identify a concrete problem or knowledge worth retaining. Compare actions with the instructions and information available at the time. Distinguish errors, restored scope, clarified preferences, new requirements, and changed decisions. A direct correction can justify a proposal, but preserve its intended scope.

Return proposals and their supporting evidence. The coordinator owns application of accepted remedies; the instructions below describe what to recommend and inspect.

## Navigation

When the selected work spent substantial effort finding information, examine how the agent found the relevant files and whether dependencies between files were hidden. Identify the missing connection and the document the agent already reads at that point. Propose a navigation pointer to the authoritative source, with the condition for following it. Check that the pointer would have helped at the point of confusion.

## Automated checks

When the agent made a mistake that automation could catch, consider linting, type checking, tests, and filesystem checks. Read the repository's own check commands first, including `package.json` or build-tool `lint` and `check` scripts, pre-commit hooks, and CI workflows. An existing check that is unwired or silently broken is the finding. Prefer a proposal to repair or connect it over a duplicate.

Inspect whether a pre-commit hook or CI job runs the repository's applicable lint, typecheck, or test commands. If neither does, record the missing automated guardrail as a finding even when the selected work contains no observed failure. Label it as an inspected repository condition, separately from an error in the work. Explain what the check could catch and where it would run. Its absence establishes a gap in automated enforcement; an expected reduction in errors still needs later evidence.

## Coding standards

When a reviewer missed a mistake, decide whether to add, remove, or clarify a rule. Classify the violation before choosing its owner.

A mechanical violation, such as a fixed syntactic pattern, banned API, import shape, or file-location rule, belongs in a deterministic check. Default to proposing the check rather than a prose rule. Choose the cheapest effective integration for the repository's language and existing tooling, such as a custom linter rule, pre-commit hook, or CI job.

Reserve `CODING_STANDARDS.md` or the project's existing standards document for judgment calls, such as cross-file consistency or whether a change matches the surrounding design. Propose removal or clarification of an existing rule when that is the smaller remedy. Keep mechanically enforceable rules in the automated checks.

### Implementation and review

Implementation carries the context of exploration, code changes, and debugging. A reviewer starts with a bounded change set and can focus on standards without retaining that implementation history. In proposed workflow changes, assign responsibility for checking judgment-based coding standards to review. Specify the applicable standards and context that the reviewer needs to assess the change.

Keep `CODING_STANDARDS.md` as a review input instead of adding its full contents to every implementation context. Follow repository instructions that require particular standards during implementation. A reviewer may still need to explore relevant code and documentation; a diff alone does not establish all the facts needed for review.

If a standards file grows beyond 1,000 lines, propose moving detailed guidance into appropriate documentation and adding navigation pointers for the reviewer. Keep the applicable rules discoverable from the standards entry point.

## Global and project steering

When a project or global `AGENTS.md` is particularly large, identify steering that belongs in coding standards or automated checks instead. Keep project and global writable scopes separate when proposing the move.

`AGENTS.md` and `CLAUDE.md` enter the context of agents working in their scope. Use that space sparingly, primarily for navigation pointers to the documentation needed for a particular task. Keep detailed reference material in its authoritative document and state when to read it.

## Ineffective instructions

When steering files are large or unwieldy, look for instructions that do not change the agent's behavior. Use the selected work and the relevant instruction version to explain why an instruction appears ineffective. Propose deletion, consolidation, or clarification when supported. Keep uncertainty explicit when the evidence cannot distinguish an ineffective instruction from one the agent never received.

## Tool economy

When the agent made expensive tool calls, inspect the calls, their inputs, and the output it actually needed. Check custom CLIs and MCP tools for excessive token use. Consider narrower queries, fewer repeated reads, smaller outputs, or a change to the tool itself. Connect the remedy to the observed cost and preserve information required for correct work.

## Information access

When crucial information was unavailable, identify the source and the point where the agent needed it. Consider exposing or saving development-server logs, read-only access to third-party services, or another project information source. A runbook can explain how to obtain and interpret that information. Keep proposed access within the relevant authorization scope.

## Project documentation

Identify knowledge from user corrections, discoveries, or successful approaches that future work should retain. Consider all project documentation, including README files, `docs/`, runbooks, how-to guides, setup and troubleshooting guides, `CONTEXT.md`, domain records, ADRs, coding standards, and local skills. Verify project facts against authoritative sources and keep temporary workarounds provisional.

Inspect the existing documentation structure and nearby examples before choosing an owning file. Propose additions, corrections, consolidation, or removal as the evidence requires. Look for an existing home before adding a document. When no suitable home exists, propose a new file using the project's naming, location, language, terminology, and structure, and explain why it is needed. If conventions are absent, state the smallest structure proposed. Apply the same placement and format rules to new runbooks, how-to guides, and project-local skills.

Keep one authoritative home for each fact or procedure. Use documentation as reference material reached through conditional navigation pointers. For domain language or architecture decisions, use `domain-modeling` to prepare a documentation delta within this proposal scope.

## Project-local skills

Failures in workflow sequencing, responsibility, context selection, delegation, validation, or handoff can justify changes to a local skill or its supporting references. A skill can hold a reusable procedure or reference discovered through its description, or provide an explicitly user-invoked command. Follow the project's skill conventions and intended invocation mode when choosing that form.

Identify the actual source and ownership before proposing edits. A copied, project-owned skill can be the canonical local adaptation. Follow symlinks; a project-local link to an external checkout does not make that checkout project-owned or add it to the authorized writable scope. Keep an external or upstream proposal distinct from a local remedy.

Target a skill's maintained source rather than a generated bundle or disposable installation cache. Identify its repository's generation and validation procedures and the project applicability for the coordinator's implementation and journal record. A local correction does not automatically become a rule for every user of the upstream pack.

Installing a skill or identifying its source does not supply approval to apply a proposal.

## Return candidates

For each candidate, give the originating correction, episode, or inspected condition; its consequence; knowledge to retain; smallest concrete remedy; owning project and file or check; applicability; expected behavior; and uncertainty. Include the examined scope and coverage gaps. Reference an existing journal change when the candidate revises it. Order candidates by severity, based on demonstrated consequences.

Include the expected upkeep and attention cost when they affect whether the remedy is worthwhile. Report no candidate when no change is justified. Do not invent recommendations to fill a quota.

Include a compact coverage receipt for the diagnostic categories above: examined with or without a finding, not applicable with a reason, or an evidence gap. Account for the automated-check setup inspection even when no failure was observed.

Done when every category has an applicability decision, each applicable category and the required check-setup inspection has been examined or has a named evidence gap, and each candidate has evidence, an owning source, a scoped remedy, and a reason it is worth retaining.
