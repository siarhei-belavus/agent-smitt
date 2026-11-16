---
name: retro
description: Review selected work, evaluate prior changes, and propose scoped improvements.
disable-model-invocation: true
---

# Retrospective

Review the work selected by the user. Find new improvements and check how earlier accepted changes affected this work. You may update any project documentation, including project-local skills. Improvements may also target checks and tools.

One coordinator owns scope, incident identity, reconciliation, and journal writes. Evidence readers and analysis workers use fresh contexts and report bounded results. Review and delivery skills do not invoke this skill. Reading a delivery grants no authority to resume it or change its external state.

## 1. Fix the work scope and prior-change set

Accept the current chat, named chats, Review Proposals, or a delivery reference with its coordinator chat. The user chooses when to invoke this skill, including during ongoing work. Default to the current chat and record the observation cutoff.

Before starting any subagent, read [analysis worker coordination](ANALYSIS-WORKERS.md). Also read it before full-trace collection when work spans multiple histories, several applicable changes, or a history too large for bounded reading. Use it to choose a proportional execution plan. A small bounded case can perform the roles directly.

When selected work spans chats or contains delegation, delivery, ticket, review, or recovery references, follow [work scope discovery](WORK-SCOPE.md). Establish membership through recorded relationships and account for inaccessible or archived histories. For supplied or linked Review Proposals, use [Review Feedback](REVIEW-FEEDBACK.md) to collect the user's comments as primary evidence.

Read the [private change journal contract](references/JOURNAL.md) to locate existing records and select earlier implemented changes that may apply to this work. An absent journal leaves the prior-change branch empty; continue diagnosis. Freeze the selected change IDs, their expectations, and relevant source versions before analysis or edits. New proposals from this incident are outside that set.

If the private journal contains `retro-policy.md`, read its context-management and reporting settings. When that file is absent or omits a setting, use compatible settings from legacy `audit-policy.md` when available. Invocation instructions take precedence, then the new policy, then legacy settings, then host defaults. Record the effective policy sources. History scope comes from the selected work; policy observation windows do not authorize unrelated-history searches.

Completion criterion: scope, cutoff, member sources, prior-change IDs, policy sources, and coverage gaps are explicit.

## 2. Collect evidence once

Keep a compact source and incident index. Read the user's messages across the available selected histories and collected Review Feedback. For each correction, recover the preceding assumption or action, the user's expectation, and the resulting decision from the original surrounding messages and actions. Collect decisions effective at the time, observed consequences, and evidence needed for the selected prior changes. Distinguish factual errors and scope corrections from clarified preferences and changed requirements. Check later messages for revisions or withdrawals. One direct correction can justify a proposal. Preserve its task, project, or broader scope before generalizing it.

Use the selected execution plan. Assign each source segment to one collector for both analysis branches. With delegated collection, keep raw histories out of coordinator context.

Group reports of the same event into one incident. Count applicable opportunities with no observed failure as well as failures. Preserve source locators, event times, version evidence, unread segments, and uncertainty. Summaries point to evidence; missing evidence is not a successful outcome.

Completion criterion: every assigned source has evidence or a named coverage gap, and both branches can trace their inputs to the same incident index.

## 3. Run the analysis branches

When the execution plan uses subagents, run independent branches in parallel as their required evidence becomes ready. Keep all workers as direct children of the coordinator.

For new improvements, give a diagnosis worker the [diagnosis guide](DIAGNOSIS.md), relevant evidence, and project conventions. Read the guide yourself when performing that role.

When earlier implemented changes may apply, give prior-change workers the [evaluation guide](PRIOR-CHANGES.md), selected journal records, and their relevant evidence. Assign one change or a tightly related group per worker. Read the guide yourself when performing that role. This branch records observations about selected work and can combine them with existing journal observations; it does not search unrelated histories.

When delegation is unavailable, perform the roles sequentially with the same bounded inputs and outputs. Checkpoint scope, coverage, assignments, and unresolved comparisons before exceeding the applicable context policy. Use the host's supported continuation mechanism without inventing token counts.

Completion criterion: diagnosis candidates have source evidence and an owner; every selected prior change has an observation, a non-applicability result, or an explicit evidence gap.

## 4. Reconcile and present the result

Check source support, coverage, incident identity, applicability, and exposure across the results. Request a bounded source reread when a material conclusion lacks context. When findings overlap or disagree about facts, causes, or remedies, follow [reconciliation](RECONCILIATION.md), including when both branches concern the same earlier change.

Present observed effects of prior changes separately from new proposals. For each proposal, give its source correction, episode, or inspected repository condition, its consequence, knowledge to retain, owning file or check, scope, and concrete change. Rank by demonstrated consequence. Include coverage gaps and uncertainty. Report when no new change is justified.

The coordinator saves a reconciled observation for every selected prior change under the journal contract, including harmful, unsupported, non-applicable, and insufficient-evidence results. Report an explicit write gap for anything not saved.

Completion criterion: conclusions and proposals have distinct purposes, overlapping findings form one issue with its remedy options, each material disagreement has an evidence-backed resolution or explicit alternatives and the missing evidence or decision, and journal observation writes are verified or reported as pending.

## 5. Apply accepted changes and record them

For accepted changes, including authorization supplied with the invocation, follow the journal contract for recording, implementation evidence, and reporting. Apply only authorized changes within their scope using the owning project's editing and validation procedures. Project-local installation alone does not authorize a remedy.

Report applied changes, validation results, journal record IDs, pending proposals, and recording gaps. Keep secrets and private chat details out of shared artifacts.

End at the selected observation cutoff. Changes made during this retrospective await later independent work for evaluation.

Completion criterion: every accepted change has an implementation result or explicit deferral, and the journal's recording requirements are met or gaps reported.
