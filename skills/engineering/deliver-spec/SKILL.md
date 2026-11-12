---
name: deliver-spec
description: Deliver a prepared specification through its tickets, shared repository branches, and final human review. Resume its delivery or address final-review feedback.
disable-model-invocation: true
---

Coordinate one published Specification and its prepared delivery tickets. Accept its permanent reference in its Ticket Origin Repository. This invocation authorizes specification branches and proposals, ticket execution with automatic merge into those branches, and ticket closeout when each ticket's own completion criteria pass. Final specification merge and closeout remain human-controlled.

Use `deliver-ticket` for each ticket, `closeout` for completed tickets, Standalone `implement` for specification corrections, and `code-review` for independent review. These skills must be available as invokable skills. Their bundled instructions are reference material, not installed entry points.

Use repository-owned bindings for provider operations. Preserve host protections, unrelated work, and intermediate human decisions. Keep specification progress on the Specification and detailed ticket execution in its existing checkpoints.

## 1. Establish authority and composition

Read the Ticket Origin Repository's instructions and applicable Work Tracker and routing bindings. On an existing execution, use [recovery](RECOVERY.md) to determine the next action before acquiring context. For specification scheduling or validation, follow [Context Pack consumption](references/bundled/federated-workflow/CONTEXT-PACK.md) to obtain or reuse `Complete` Decision Context for the exact Specification reference. Read the Specification and applicable accepted changes; retain its entry path for consumers. Publication owns planning validation. A discovered gap or changed authority requires reconciliation before affected work continues.

Discover the complete explicitly related delivery-ticket set through the configured relationship procedure, including every page. Decision Context supplies authority, not a complete scheduler snapshot. For Local Markdown, enumerate a declared ticket index or explicitly supplied relationship directory when available. Otherwise enumerate the established `.scratch/*/issues/*.md` layout in the Ticket Origin Repository. Read ticket relationship fields and select exact permanent Parent or Authority Sources references to this Specification; directory proximity alone establishes no relationship. Resolve repository-relative references and enumerate the chosen set completely. This uses ticket-side relationships and requires no reverse index on the Specification. Missing relationships or an unavailable provider procedure require clarification, not guessed tickets.

Read each related ticket's published relationship fields, Repository References and writable Repository Scope, plus current dependency, claim, routing, and completion state. Use these records for the complete scheduling set and writable repository union. This is scheduling discovery, not per-ticket Context Assembly or a planning audit. Acquire each ticket's Delivery Context in its `deliver-ticket` execution when selected for launch. A Specification's Repository References alone grant no writes. Missing or contradictory scheduling records stop affected scheduling and return to their owner; this skill does not create substitute tickets.

Record the agreed permanent ticket set, effective authority references, writable repository union, and supplied execution directions in a [specification checkpoint](RECOVERY.md#specification-checkpoint). On any existing execution, apply [recovery](RECOVERY.md) before mutation. New tickets or changed requirements require explicit reconciliation. Pause affected work while valid independent work may continue. Preserve completed history; record approved changes and their authority before rebuilding affected packs.

**Complete when:** accepted authority and the exhaustive agreed scheduling set are available, every writable repository has attributable authorization, and existing execution or changed composition has been reconciled.

## 2. Prepare shared branches and execution contexts

Prepare shared targets for eligible tickets as capacity becomes available. Resolve the needed repositories against their Repository IDs, declared remotes, selected final targets, Git identities, and Code Host bindings. Read instructions needed for branch preparation. Domain implementation reading belongs to ticket executors; final validation preparation belongs to step 4. Use a matching known checkout as a Git store while preserving its checked-out branch, index, files, and configuration. Unresolved identity or access stops affected preparation without blocking independent tickets whose prerequisites are ready.

Record one specification integration branch and final Target Branch per writable repository, normally using the configured Base Branch as final target. For each repository needed by the next launch, pin the final target's current exact commit. Create the integration branch from that commit only after verifying the intended name is unused and the target exists. Publish through the binding and verify the remote revision before dispatching its ticket. A colliding branch requires ownership proof or reconciliation, never overwrite. Persist branch choices before creation and verified revisions afterward; future repository preparation remains explicitly pending.

Reuse attributable branches and suitable isolated specification worktrees. Create a worktree only when validation or corrections need writable local state; obey the execution host's location policy and repository bootstrap instructions. Record ownership separately from ticket worktrees. Durable records use repository, branch, revisions, and provenance; local paths remain host state. Keep read-only repositories outside the writable union and isolate mutable validation outputs from their stores.

Reconcile adopted results and active deliveries through [recovery](RECOVERY.md#reconcile-observed-state). A completed ticket must be represented in the assembled result. An active delivery on another target needs explicit reconciliation before reuse; never silently retarget it.

Select a context mechanism that can start, observe, continue, and recover ticket coordinators which themselves delegate implementation and review. Follow user preferences and actual runtime capabilities. When the user selects separate chats in the same project, use those chats for ticket coordinators and their subagents for repository work. Verify that capability before dispatch. If unavailable, report the limitation and obtain an authorized alternative rather than flattening context isolation.

Budget capacity across the delegation tree. Independent tickets may run in parallel, including two tickets writing the same repository through separate ticket worktrees. Shared repository identity is not a scheduling dependency. Retain execution references for reuse; runtime preferences belong to the user and execution host, not repository setup.

**Complete when:** the next eligible ticket's shared targets are durable and remotely readable, its adopted prerequisites are accounted for, and the context mechanism supports the required isolation and recovery within actual capacity. Dispatch it while preparing other independent eligible work.

## 3. Execute and close eligible tickets

Start each new ticket coordinator in a fresh context without the specification coordinator's conversation, whether it runs as a subagent or a separate chat. Supply the complete ticket assignment and required source references. On resume, continue the recorded execution instead of creating a new coordinator.

Use current tracker dependency rules to select only eligible tickets in the agreed set. Recheck state before dispatch. Record launch intent and its ticket before starting a coordinator; record and re-read the returned execution reference afterward. Use the runtime's available lookup to reconcile an uncertain launch before any retry.

Give each coordinator an explicit ticket reference, Ticket Origin Repository, and `Automatic merge: allowed`. Supply `Target Branch` entries only for repositories in that ticket's published Repository Scope, using each repository's recorded specification branch. Include relevant orchestration decisions and resource ownership. An already accepted matching ticket pack may be passed explicitly with its complete directory; do not acquire one merely to dispatch. Invoke `deliver-ticket` in that separate context. It owns live eligibility and claim verification, its Delivery Context, target synchronization, conflicts, validation, review, merges, handoff, and ticket recovery. Its isolated ticket source branches and per-ticket proposals remain part of delivery. Scheduling state does not replace its pre-claim check.

Observe or continue existing executions through their recorded references. For a ticket human-action checkpoint, retain the ticket's request as the response location and link it from the Specification. Surface the required action and pause affected and dependent work. Continue independent work only when its authority and prerequisites remain valid. A response resumes through `deliver-ticket`'s gate. A specification-level question belongs on the Specification with the affected work, required decision, owner, response location, and completion condition.

After a successful ticket handoff with confirmed merges or valid no-change results, check that ticket's actual completion criteria. Invoke `closeout` with exact revision evidence only when they pass. Explicitly scope cleanup to that ticket's disposable resources and identify specification branches and worktrees as retained shared resources. Merge alone supplies neither missing acceptance nor required deployment evidence. Preserve the human boundary until those conditions are met.

After confirmed tracker closure, reconsider dependents without waiting for final specification merge. Distinguish closure from cleanup; incomplete cleanup need not undo proven closure. Recover missing effects through their existing owner and update the specification checkpoint.

**Complete when:** every agreed ticket has confirmed completion, or remaining tickets have attributable active executions, dependency waits, or human boundaries. Continue eligible work while capacity permits; otherwise return the current checkpoint and required next actions.

## 4. Validate the assembled result

Once all agreed tickets are complete, pin the complete repository head set, current final target commits and review bounds, and every influencing Validation Source revision. Verify the assembled result includes all adopted ticket outcomes. Freeze coordinator writes while validating; observed external movement follows [evidence freshness](RECOVERY.md#evidence-freshness).

For each unmerged changed repository, synchronize the current final target into the isolated specification branch if it advanced. Preserve concurrent work. Resolve only conflicts determined by accepted requirements; a semantic conflict requiring new authority enters the specification human boundary. Record the new review base and resulting head before validation.

Run repository validation and all specification acceptance criteria and declared Validation Obligations against that exact combined result. Assign each obligation one evidence owner and its declared method, prerequisites, expected result, and exact influencing revisions. Reuse ticket evidence only when those complete dependencies still match. A clean set of ticket checks does not prove the combined result. Planned human verification remains a visible requirement with its declared procedure and evidence.

Use `code-review` in **Both** mode on fixed Repository Targets for changed repositories. Supply the accepted Specification Decision Context unchanged, exact review bases and heads, settled seams, repository evidence, and whole-specification validation. Include unchanged and confirmed merged repositories as exact read-only authority or Validation Sources where they influence acceptance. An empty diff requires no empty review target or proposal, but still requires the applicable acceptance evidence.

Record Advisory findings. When an attributable combined-result failure or Blocking review finding requires an in-scope correction, read and follow [corrections](CORRECTIONS.md), then refresh affected validation and independent reviews. Requirement or scope changes require the human boundary.

**Complete when:** all specification criteria and obligations have current passing evidence for one fixed combined result, and independent review has no Blocking finding. Otherwise preserve the result with its exact failed or pending conditions.

## 5. Publish the final human handoff

For each unmerged changed repository, publish the specification branch through its binding and create or update its one final Review Proposal to the recorded final target. Reconcile existing proposals before creation. Re-read source, target, remote head, draft/readiness state, feedback, and host checks. Any drift returns to the earliest invalidated prerequisite before claiming readiness. Mark verified proposals ready for human review. Never merge them automatically or bypass host policy.

Preserve confirmed merged proposals with their exact source/result revisions. Repositories with no resulting changes need no proposal. Record a current handoff checkpoint containing final proposals, validation and independent-review results, limitations, and remaining human review, merge, rollout, acceptance, and explicit closeout actions. Reuse an equivalent verified handoff on repeat invocation.

Keep the Specification open and retain its branches and worktrees for feedback and recovery. Do not invoke specification closeout. When actionable final-review feedback or a later correction request arrives, read and follow [recovery](RECOVERY.md), then [corrections](CORRECTIONS.md), for this same Specification.

**Complete when:** every changed repository has a verified final proposal or preserved confirmed merge, the durable handoff matches current evidence, and the human has the remaining actions with recoverable working state.
