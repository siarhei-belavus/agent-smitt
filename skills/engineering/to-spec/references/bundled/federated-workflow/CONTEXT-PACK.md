# Context Pack consumption

A Context Pack is an immutable, runtime-local snapshot for one profile and permanent root. Its entry file identifies the result, sources, relationships, and any diagnostics. Full bodies and comments may be inline or in linked Markdown files within the same private directory. The entry path is the Authority input passed to consumers; every linked file travels with it.

## Acquire and reuse

Acquire a pack when the selected work needs authority. Use an explicitly supplied accepted pack for the same root when all its files remain readable and no known authority change makes it stale. Otherwise invoke [Context Assembly](WORK-TRACKER-CONTEXT-ASSEMBLY.md) once for that work. Accept only `Complete`. Inspect a non-complete result's diagnostics at the workflow's clarification or human boundary.

Keep packs outside worktrees. Parallel ticket coordinators may read an explicitly shared immutable pack, but each owns any new acquisition it starts. Independent invocations need no shared cache, directory search, or lock protocol. Acquire future tickets when they become eligible; their acquisition does not block already-ready independent work. A specification coordinator's scheduling reads do not require Delivery Context for every ticket.

Retain the directory until its last consumer finishes, including a paused coordinator that can still resume. The acquiring workflow owns cleanup; borrowers do not delete shared files. On another host, copy the complete directory without changing content and pass that host's entry path. A lost directory can be reacquired from permanent sources.

## Read for the current action

Read the entry and active artifact, including its applicable accepted decisions and execution feedback. Follow indexed local sources when a referenced decision supplies a needed condition, a requirement is missing or contradictory, or the current action reviews or changes that source. Material required by a repository instruction remains mandatory. Acquisition of a full source set does not require every consumer to read every source.

For a prepared ticket, publication owns source preservation and planning-contract validation. Execution consumes its self-contained scope, outcomes, criteria, settled decisions, and validation obligations. Check that these identify the next authorized action; return discovered gaps or conflicts to their owner. Execution does not repeat a source-to-ticket planning audit. Planning and Spec review still read the authority required by their selected coverage.

## Freshness

A pack supplies authority, not a live claim, dependency, routing, proposal, or merge state. Read current operational state at the action that depends on it. Known changed authority requires reconciliation and a new pack for affected work; never overwrite files already given to a consumer. Temporary tracker unavailability may leave independent local implementation usable, but does not waive an action's required live check.

On resume, first use durable execution state to identify the next action. Reacquire authority only when that action needs it and no usable pack remains. Terminal reporting and completion of missing handoff effects can use recorded authority and evidence when current observations prove their prerequisites unchanged. For reuse of review results across acquisitions, apply [Authority evidence](DELIVERY-RECORDS.md#authority-evidence).
