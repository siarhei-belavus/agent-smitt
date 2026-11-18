# Context Pack consumption

When consuming authority, read [Context reading](CONTEXT-READING.md) for the pack structure, required sources, and handling of changed or unavailable authority.

## Acquire and reuse

Acquire a pack when the selected work needs authority. Use an explicitly supplied accepted pack for the same root when all its files remain readable and no known authority change makes it stale. Otherwise invoke [Context Assembly](WORK-TRACKER-CONTEXT-ASSEMBLY.md) once for that work. Accept only `Complete`. Inspect a non-complete result's diagnostics at the workflow's clarification or human boundary.

Keep packs outside worktrees. Parallel ticket coordinators may read an explicitly shared immutable pack, but each owns any new acquisition it starts. Independent invocations need no shared cache, directory search, or lock protocol. Acquire future tickets when they become eligible; their acquisition does not block already-ready independent work. A specification coordinator's scheduling reads do not require Delivery Context for every ticket.

Retain the directory until its last consumer finishes, including a paused coordinator that can still resume. The acquiring workflow owns cleanup; borrowers do not delete shared files. On another host, copy the complete directory without changing content and pass that host's entry path. A lost directory can be reacquired from permanent sources.

## Read for the current action

Before implementation, validation, or review, apply [Context reading](CONTEXT-READING.md) in full. Supply that contract to delegated consumers; acquisition, retention, and cleanup remain with the owning workflow.

## Freshness

A pack supplies authority, not a live claim, dependency, routing, proposal, or merge state. Read current operational state at the action that depends on it. Known changed authority requires reconciliation and a new pack for affected work; never overwrite files already given to a consumer. Temporary tracker unavailability may leave independent local implementation usable, but does not waive an action's required live check.

On resume, first use durable execution state to identify the next action. Continuing implementation, validation, or review requires the full active contract and applicable decisions and feedback under the reading rules above. Reacquire authority only when that action needs it and no usable pack remains. Terminal reporting and completion of missing handoff effects can use recorded authority and evidence when current observations prove their prerequisites unchanged. For reuse of review results across acquisitions, apply [Authority evidence](AUTHORITY-EVIDENCE.md).
