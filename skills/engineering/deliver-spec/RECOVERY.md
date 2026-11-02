# Specification recovery

## Specification checkpoint

Store checkpoints in the Specification's configured coordination log. With Local Markdown, declare an append-only coordination section or linked comment file on the Specification and keep it outside disposable worktrees. Re-read every write. Use the shared [comment presentation](references/bundled/federated-workflow/LIFECYCLE-ARTIFACTS.md#comment-presentation) with a human-readable result and recovery details.

A specification checkpoint is an orchestration snapshot, not a ticket Execution Checkpoint. Include these groups, with explicit pending values for facts not yet established:

| Group | Contents |
| --- | --- |
| Authority and ownership | Permanent Specification reference, checkpoint identity and predecessor, agreed ticket references, effective authority references and accepted changes, writable repository union, current coordinator runtime reference and ownership evidence. |
| Repositories | Repository References, specification branch and final target, immutable launch commits, current review bases and exact source heads, attributable adopted results, preserved worktree ownership, and confirmed merge source/result revisions. |
| Ticket execution | Ticket-to-runtime references, observed liveness, latest ticket checkpoint or human request references, confirmed completion and outstanding closeout or cleanup actions. Detailed delivery state remains in the ticket. |
| Overall result | Final proposals, correction assignments and their feedback references, validation and review evidence with exact revision and authority dependencies, invalidated or pending evidence. |
| Continuation | Pending operations and their lookup references, next permissible actions and prerequisites, affected and independent work, open specification decisions and responses, retained resources and limitations. |

Keep credentials, local worktree paths, and runtime-local Context Pack paths out of durable records. Record authority by public profile and permanent source references. Append successors without erasing history. Re-read before appending; reuse an equivalent existing snapshot when nothing material changed. An uncertain write must be reconciled before retry.

## Reconcile observed state

On every resumed invocation, read the complete current specification coordination state and reconcile it with tracker, Code Host, and authoritative runtime observations before mutation. Reestablish accepted authority through step 1 of `deliver-spec`. A saved checkpoint identifies what to inspect; it does not override current external evidence.

Establish whether an existing specification coordinator is still active before starting another writer. Observe or continue a live coordinator. Silence, an old timestamp, or a missing local process is not proof that a remote execution terminated. If liveness or ownership is indeterminate, preserve state and request reconciliation. Use confirmed termination and current external state to recover only missing orchestration actions. Ticket claim and recovery authority remain with `deliver-ticket`.

| Observed state | Authorized continuation |
| --- | --- |
| Branch or worktree already exists | Verify repository identity, ownership, branch, exact head, and recorded provenance. Reuse suitable state. Preserve unknown dirty work or a collision for reconciliation. Reconstruct a missing local worktree from the attributable published revision; a former local path is not required. |
| Completed ticket, including one merged to the final target before this run | Verify acceptance and source/result provenance and prove its outcome is represented in the specification result through Git or equivalent content evidence. Do not rerun or reopen it. Missing representation requires explicit integration reconciliation. |
| Active ticket on the selected specification target | Reuse its runtime reference and observe or continue it. An interrupted ticket resumes through `deliver-ticket`, which decides its next valid step. |
| Active ticket on another target, or conflicting execution choices | Pause affected scheduling and reconcile the live execution and intended result with the human. Any changed ticket choices go through its existing recovery gate. Do not start a replacement or silently retarget. |
| Launch response lost or runtime liveness unknown | Look up the recorded launch intent through authoritative runtime state. Reuse the found execution. Retry only after proving no launch occurred or the earlier execution terminated and recovery permits it. An unavailable lookup requires a human boundary. |
| Ticket merge confirmed but handoff absent | Resume `deliver-ticket` for missing handoff effects. A merge does not itself authorize bypassing its Resume Gate. |
| Ticket handoff complete, closure pending | Invoke `closeout` only after its completion conditions pass. Retain missing acceptance or deployment as a human boundary. |
| Tracker closure confirmed, cleanup or spec checkpoint absent | Preserve closure and dependent eligibility. Use `closeout` for remaining safe ticket cleanup, retain specification resources, and record observed completion without duplicating records. |
| Final proposal or checkpoint response lost | Read actual proposal or coordination-log state before retry. Reuse the matching result, or perform only the proven missing authorized effect. |
| Some final proposals merged | Preserve exact source/result revisions and current open proposals. Correct only affected repositories through the correction branch; a historical target tip is not today's tip. |
| Repeated matching handoff or unchanged human boundary | Report the existing state and next human action without another launch, proposal, request, or equivalent checkpoint. |

Confirm partial success per repository. No multi-repository operation is atomic; failure elsewhere authorizes neither rollback nor replay of a completed effect. Reconcile changed composition or requirements before affected mutation, preserving valid independent progress. Persist the reconciled snapshot and next action before resuming side effects.

**Complete when:** every pending action has an attributable observed state, no live or indeterminate writer will be duplicated, and only missing authorized effects remain scheduled through their owning skill.

## Evidence freshness

Evidence records its exact influencing repository heads, review bounds, Validation Sources, and accepted authority. A changed head invalidates its validation and Standards result and every combined result it influences. Changed target or review bounds require renewed integration/readiness assessment and affected reviews. Changed influencing Validation Sources invalidate dependent validation and Spec review. Preserve unrelated evidence whose complete dependencies remain unchanged.

A new Context Pack invalidates reviews bound to the previous Authority input. Reassemble when accepted requirements change or the live pack is unavailable; refresh affected criteria and validation as required by the actual authority change. Reassembly alone does not invalidate execution checks whose authority and revision dependencies remain valid.

For confirmed merges, retain the historical validated source and provider-confirmed result relationship. Squash or rebase commit IDs alone do not prove changed content; prove the accepted combination is represented. Unrelated later target advancement does not reopen a completed ticket. A missing relationship or a semantic conflict enters the human boundary.

Recheck the full evidence set and actual proposal source/target/head state before reporting final readiness. A stale result is pending refresh, never a current pass.
