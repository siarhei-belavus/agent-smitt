# Context reading

A Context Pack is an immutable, runtime-local snapshot for one profile and permanent root. Its entry file identifies the result, sources, relationships, and any diagnostics. Full bodies and comments may be inline or in linked Markdown files within the same private directory. The entry path is the Authority input passed to consumers; every linked file travels with it.

Before using a supplied pack, require its `Complete` result for the exact active root and readable entry and linked files. Keep that immutable source set intact. A delegated consumer returns missing or conflicting authority to the assigning workflow; it performs no Context Assembly or provider lookup.

## Read for the current action

For implementation, validation, or review, read the entry and active artifact in full, including its requirements, constraints, acceptance criteria, and validation obligations. Read applicable accepted decisions and execution feedback in full even when they are in linked files. Material required by a repository instruction remains mandatory. Defer supporting history and rationale until needed to interpret a decision, resolve a gap or contradiction, or inspect the source itself. Indexed reading changes when supporting material is opened; every applicable requirement and accepted decision remains part of the work and its Spec review coverage.

For a prepared ticket, publication owns source preservation and planning-contract validation. Execution consumes its self-contained scope, outcomes, criteria, settled decisions, and validation obligations. Check that these identify the next authorized action; return discovered gaps or conflicts to their owner. Execution does not repeat a source-to-ticket planning audit. Planning and Spec review still read the authority required by their selected coverage.

## Changed or unavailable authority

A pack supplies authority, not current claim, dependency, routing, proposal, or merge state. Known changed authority requires reconciliation by the owning workflow and a new pack for affected work. Never overwrite files already given to a consumer. Report discovered conflicts and unavailable required sources before dependent work continues.
