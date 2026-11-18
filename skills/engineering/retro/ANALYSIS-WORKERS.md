# Analysis worker coordination

## Choose a proportional plan

The coordinator keeps the scope, source index, incident map, prior-change inventory, assignment status, concise result receipts, and unresolved questions. Store detailed evidence and assessments in private files under `journal-directory/retrospectives/<run-id>/` when persistent artifacts are needed. Keep each worker's output path exclusive. If private artifact storage is unavailable, use bounded structured results with source references and report the limitation.

For a small case, one worker or the coordinator can collect and analyze its bounded sources. For several changes with disjoint short histories, a worker may combine extraction and evaluation for its assigned change.

When branches share histories, or selected work contains many related chats, separate extraction from analysis. Readers cover disjoint incidents or source segments once for both branches. Diagnosis and prior-change workers then use the shared evidence. A large incident may have several readers with disjoint segments, but all keep the same incident ID.

Run ready independent jobs in parallel within host capacity. Start an analysis job when its required evidence is complete or its gaps are explicit; unrelated readers need not finish first. Avoid a worker per chat or per change when that would duplicate history reads.

## Give self-contained assignments

Start every new worker with a fresh context without the parent conversation. Give it:

- Role, bounded question, observation cutoff, and allowed scope.
- Incident and change IDs, relevant accepted expectations, and effective policy.
- Readable source references, assigned segments, and the role guide. Include the journal contract for prior-change evaluation.
- Required output fields, exclusive artifact destination, and completion condition.
- Read-only authority over histories, project files, skills, and journal records.

Workers write only their assigned private artifacts. They do not spawn other agents, expand scope on their own, apply remedies, or update the journal. The coordinator owns all dispatch and final writes.

## Evidence readers

Read each assigned segment for both branches' questions. Preserve direct user corrections, their preceding assumptions or actions, expected behavior, decisions, later revisions, and observed consequences. Also capture evidence relevant to prior changes and consequential surprises without turning extraction into a new retrospective.

Return evidence items with:

- Incident ID, source locator, segment coverage, and event time with known precision.
- Relevant change IDs and applicability as yes, no, or unknown, with reasons.
- Effective version or availability evidence, separately from actual use.
- Observed action, outcome, added work, and the correction or question it supports.
- Unknowns, unread or inaccessible segments, contradictory evidence, and newly discovered source references.

Include applicable opportunities where no failure occurred. Silence or missing evidence must not become a negative finding. Give the coordinator a short receipt with artifact paths, coverage, material observations, and open questions rather than a raw-log dump.

## Analysis workers

Diagnosis workers receive the evidence relevant to a coherent piece of work and the diagnosis guide. They propose scoped remedies with concrete owners and source references. Prior-change workers receive one change or a tightly related group, its applicable evidence, and the evaluation guide. They return proposed observations and a bounded assessment for each change.

Provide prior-change workers with earlier comparable journal observations and their incident IDs so they can assess accumulated evidence under the evaluation guide.

Use evidence artifacts as the initial input, with original locators available for checking. A worker may reread a specific source segment to resolve a material gap or contradiction. It identifies the question and segment in its receipt. Recollecting whole histories needs a revised coordinator assignment.

## Reconcile without accumulating histories

The coordinator retains source coverage and concise result receipts for the main skill's reconciliation step. Worker artifacts keep the detailed evidence available for that step.

Reuse a worker for a bounded clarification within its assignment. Give unrelated analysis or work exceeding its context budget a fresh context with a compact brief. Checkpoints preserve completed assignments, artifact paths, incident identities, pending writes, and remaining questions.

Only the coordinator applies authorized changes and writes journal observations. When writing records, follow the journal's [safe update procedure](references/JOURNAL.md#identity-and-safe-updates), including when another retrospective may write concurrently.

Done when every planned branch has a reconciled result or named gap and every final claim has a traceable source without requiring the coordinator to retain the raw histories.
