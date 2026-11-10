---
name: retro
description: "Conduct a retrospective on a coding session."
disable-model-invocation: true
---

The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.

Accept the current chat, named chats, or a delivery reference and coordinator chat. The user chooses when to invoke `retro`, including during ongoing work. Review and delivery skills do not invoke it. Record the selected scope and observation cutoff. Reading a delivery grants no authority to resume it or change its external state.

## Steps

1. Call the Skill tool with `writing-for-agents` for the writing style guide.

2. Read the primary sources for the session the user specifies. This may mean searching through session logs on this machine. If the user doesn't specify a session, default to the current one.

   For work spanning sessions, follow coordinator checkpoints, ticket relationships, and execution references to implementation, validation, review, correction, and recovery sessions. Include attributable archived sessions and previous attempts. Use the host's available session tools and the project's configured records, following pagination. Establish membership from recorded relationships. Account for each discovered session and report inaccessible histories or evidence lost during cleanup. Ask for a missing reference only when the intended work cannot be identified, and continue with independently available evidence.

   Read the user's messages across the available selected histories. For each correction, recover the preceding assumption or action, the user's expectation, and the resulting decision from the original surrounding messages and actions. Distinguish errors and scope corrections from clarified preferences or changed requirements. Check later messages for revisions or withdrawals. One direct correction can justify a proposal. Preserve its task, project, or broader scope before generalizing it.

   Group reports of the same event across sessions into one incident. Compare actions with the instructions and evidence available at that time. Treat summaries as pointers to evidence and identify uncertainty when original records are unavailable.

3. Look for candidates for improvement in these categories.

- **Navigation**: how easy was it for the agent to find the right files? Are there hidden dependencies between files? Would a **navigation pointer** make it easier? _Use when_ the session took a long time to find a piece of information.
- **Automated checks**: are there automated checks that could catch errors the agent made? Linting, typing, tests, filesystem linters? Read the repo's own check command first (its `package.json`/build-tool `lint`/`check` scripts, its CI workflow), so a check that already exists but sits unwired or silently broken is the finding, not a reinvention. A repo with no **guardrail** (no pre-commit hook and no CI job running its lint/typecheck/test command) is itself a finding: an un-linted repo is a standing missed opportunity, not a neutral default. _Use when_ the agent made a mistake an automated check could have caught, or the repo has no guardrail at all.
- **Coding standards**: should the **reviewer agent** be given a new rule to enforce? Should an existing rule be removed or clarified? Classify the violation first: a **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full stop: a custom rule in the repo's own linter, a new pre-commit hook, or a new CI job, whichever the repo's language and existing guardrail make cheapest. Default to building the check over writing the rule. Reserve `CODING_STANDARDS.md` for genuine **judgement calls** (cross-file consistency, "matches the surrounding style," anything no guardrail could ever substitute for). _Use when_ the reviewer agent failed to catch a mistake.
- **Global AGENTS.md**: are there any steering instructions that should be moved to coding standards (or automated checks) instead? _Use when_ the AGENTS.md file is particularly large - in the repo OR the user's global scope.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is there any custom tooling (CLI's, MCP's) that is particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **No-ops**: look for instructions in steering files that don't modify the agent's behavior. _Use when_ the steering files are large and unwieldy.
- **Information access**: look for opportunities to increase the agent's access to information. Teeing dev server logs, readonly access to third-party services. _Use when_ a crucial piece of information was not available to the agent.

- **Project documentation**: what knowledge from user corrections, discoveries, or successful approaches should future work retain? Consider all project documentation, including README files, `docs/`, runbooks, setup and troubleshooting guides, domain records, and ADRs alongside the files above. Verify project facts against authoritative sources and keep temporary workarounds provisional. Inspect the existing documentation structure and nearby examples before choosing an owning file. Propose additions, corrections, consolidation, or removal. When no suitable home exists, propose a new file using the project's naming, location, language, terminology, and structure, and explain why it is needed. If conventions are absent, state the smallest structure proposed. Keep one authoritative home with conditional navigation pointers. For domain language or architecture decisions, use `domain-modeling` to prepare a documentation delta within this proposal scope.

  This includes proposing new runbooks, how-to guides, and project-local skills. Choose a runbook for an operational procedure, a how-to guide for a specific task, or a local skill for a repeatable agent workflow. Follow the project's existing placement and format, and use `writing-for-agents` when proposing a local skill.

4. Present these candidates to the user, in order of severity.

   For each candidate, give the source correction, episode, or inspected repository condition, its consequence, the knowledge to retain, and a concrete change to the owning repository's file or check. Include the examined scope, coverage gaps, and uncertainty. Report when no change is justified.

5. If the user has authorized changes, apply them within that scope using the project's editing and validation procedures. Reuse authorization supplied with the invocation. Report applied changes, validation results, and proposals awaiting a decision. Keep secrets and private chat details out of shared artifacts.

## Reference

### Implementation vs Review

Remember that all work goes through two stages: implementation and review. The implementation agent has the most **context pressure**. They are responsible for exploration, writing code, and debugging failures.

The review agent has the least context pressure - it receives a diff, so no exploration needed. It often does not need to write code or debug.

This means that the review agent should be responsible for imposing coding standards, not the implementation agent.

### Files

You have access to several files in the repo:

- `CLAUDE.md`/`AGENTS.md`: these files are pushed to the context window of any agent working in this repo. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.
- `CODING_STANDARDS.md`: this file is read during review, not implementation. Add **navigation pointers** to docs folders if the standards file gets more than 1,000 lines long.
- Docs: use docs as references files, pointed to by other files. Look for existing docs before writing new ones.
- Skills: use skills for docs (since their description goes into the agent's context window), or for user-invoked commands. Follow the advice in the `writing-for-agents` skill.
