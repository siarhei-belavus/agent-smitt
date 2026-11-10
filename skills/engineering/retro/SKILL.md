---
name: retro
description: Learn from selected work across its sessions and propose improvements to project documentation, checks, and agent tooling.
disable-model-invocation: true
---

# Retro

Run when the user explicitly requests a retrospective. Accept the current chat, named chats, or a delivery reference and coordinator chat. Default to the current chat when no scope is supplied. The user chooses the timing, including during ongoing work. Review and delivery skills do not invoke this skill.

Produce evidence-backed proposals. Apply selected changes only within the user's authorized scope, including authorization supplied with the invocation. Reading a delivery grants no authority to resume it or change its external state. Keep secrets and private chat details out of shared artifacts.

## 1. Establish the scope

Identify the selected work, repositories, and observation cutoff. For a delivery spanning sessions, follow the coordinator's checkpoints, ticket relationships, and recorded execution references to implementation, validation, review, correction, and recovery sessions. Include attributable archived sessions and previous attempts. Use the host's chat and session tools and the project's configured records. Establish membership from recorded relationships, rather than similar titles or shared directories.

Build a compact session inventory with each session's role, relationship, and availability. Follow paginated records through the selected scope. Report inaccessible histories and evidence lost during cleanup as coverage gaps. Ask for a missing reference only when the intended work cannot be identified, and continue with independently available evidence.

Done when each discovered session is accounted for and the scope, cutoff, and access gaps are explicit.

## 2. Recover lessons and corrections

Read the user's messages across the available selected histories, including corrections, redirections, and clarifications. Summaries and checkpoints locate evidence. Read the original surrounding messages and actions before drawing a conclusion about an episode.

For each correction, recover what the agent assumed or did, what the user expected, and the resulting decision. Distinguish an error or scope correction from a clarified preference or changed requirement. Check later messages for revisions or withdrawals. One direct correction can justify a proposal. Preserve its task, project, or broader scope before generalizing it.

Also examine repeated discovery work, failed checks, missed review findings, successful approaches worth documenting, unavailable information, and costly tool use. Group reports of the same event across coordinator and worker sessions into one incident. Compare actions with the instructions and evidence available at that time.

Record the source reference, observation, consequence, knowledge worth retaining, and any inferred cause or uncertainty. Verify project facts against current authoritative sources. Treat a temporary workaround as provisional until evidence supports a lasting procedure.

Done when the available user corrections have been accounted for and each candidate lesson has attributable evidence or an explicit uncertainty.

## 3. Find the documentation owner

Inspect the affected project's documentation structure, entry points, and nearby examples before choosing a destination. Any project documentation can be relevant, including `AGENTS.md`, README files, `docs/`, runbooks, setup and troubleshooting guides, architecture and domain records, ADRs, and coding standards.

Prefer an existing authoritative home. Propose additions, corrections, consolidation, or removal where evidence warrants them. Create a file when the knowledge has no suitable home, using the project's naming, location, language, terminology, and document structure. If the project has no convention, propose the smallest suitable structure and state that choice. Keep facts and procedures in one owning document, with conditional navigation pointers where readers need them.

For agent-consumed documentation, use `writing-for-agents` to shape proposed instructions and pointers. For domain language or architecture decisions, use `domain-modeling` to prepare the corresponding documentation delta. These uses retain this retrospective's proposal scope.

For mechanical failures, inspect existing check commands and CI wiring before proposing a deterministic check. Put rules requiring reviewer judgment in the project's standards. Consider changes to tooling or information access when documentation would not address the observed cause.

Done when every retained candidate has an owning repository and destination, follows local documentation conventions, and addresses the evidenced problem without duplicating an existing source or check.

## 4. Present and apply authorized changes

Present candidates in order of demonstrated consequence. For each, give the source correction or episode, its consequence, the lesson, the target file or check, and a concrete proposed change with the expected benefit. Explain why a new file is needed when proposing one. Include the examined scope and coverage gaps. Report when no change is justified.

When the user has authorized particular changes, apply them within that scope using the project's editing and validation procedures. Reuse prior authorization. Report which proposals were applied and which remain for a decision, with validation results. Keep broader changes as proposals for their respective owners.

Done when the user has a reviewable result and every authorized change has an attributable outcome.
