# Workflow guide

Use the amount of process the work needs. A settled, small change can go straight to `implement`. A feature with several deliverable slices benefits from a specification and tickets. A large effort with unresolved decisions starts in `wayfinder`.

The skill files define the workflow rules. This guide explains how to use them together.

## Configure the repositories

Install the pack and make sure your agent can access the code host, tracker, and project tools. Then invoke `setup-federated-workflow` in the repository you want to configure:

```text
Use setup-federated-workflow to configure this repository.
Use GitHub for code reviews and our existing issue tracker for delivery tickets.
Inspect the project and propose the provider and domain bindings.
```

Setup supports three operations:

| Operation | Use it when |
| --- | --- |
| Configure one repository | The repository needs provider bindings and domain documentation routing. |
| Establish Domain Federation | Several repositories share domain responsibilities and need one canonical context map. |
| Join Domain Federation | One repository needs to join an existing federation. |

The Code Host owns revisions and PRs or MRs. The Work Tracker owns planning artifacts, tickets, dependencies, claims, and workflow state. They can be different services. A Ticket Origin Repository owns the tracker binding for its tickets. Setup asks you to confirm that role rather than inferring it from Git remotes.

Setup researches existing code, documentation, provider capabilities, and configuration. It presents the proposed mappings for confirmation, then drafts the complete file changes for a second confirmation before applying them. It validates the result and leaves the changes uncommitted.

| File | Purpose |
| --- | --- |
| `docs/agents/code-host.md` | Repository identity, base branch, publication, review operations, and provider validation. |
| `docs/agents/issue-tracker.md` | Tracker operations, artifact mapping, context acquisition, claims, and delivery selection. Only Ticket Origins own this binding. |
| `docs/agents/triage-labels.md` | Mapping of workflow roles such as `ready-for-agent` to provider labels. Only Ticket Origins own this binding. |
| `docs/agents/domain.md` | Routes domain sources and architecture decisions. Contains the federation binding when applicable. |
| `AGENTS.md` or `CLAUDE.md` | Points the agent to the bindings that this repository owns. |

For a federation, one Home repository owns the Federated Context Map and federation-wide architecture decisions. Each context has exactly one owner. Other repositories can participate in that context without copying its glossary. Members and Home record the same portable Home identity. Local checkout paths stay out of durable configuration.

```text
Use setup-federated-workflow to establish a federation for our API,
web application, and contract-test repositories. Research ownership
and propose the Home, members, Ticket Origins, and context map.
```

Review and accept setup changes into every participating repository's configured base branch before treating the configuration as authoritative. Changing an existing federation's Home is a normal planned delivery, outside setup's Establish and Join operations.

## Sharpen the idea

Use `grill-with-docs` when there is a codebase. It combines an interview with domain modeling. It returns accepted decisions and Domain Model Deltas, records that preserve confirmed language or architecture changes and their eventual documentation owner.

```text
Use grill-with-docs to work through team invitations.
We need expiring invitations and must preserve existing membership rules.
```

Use `grill-me` for a plan without a codebase. If a question needs runnable evidence, use `prototype`. When the prototype needs a separate conversation or repository, use `handoff` to carry the question out and the findings back.

Keep refinement, specification, and ticket breakdown in one conversation so each stage can use the accepted reasoning. Automatic context compaction continues that conversation. It does not require a handoff.

Planning keeps future domain changes in its outputs. It does not rewrite canonical documentation to describe a system that has not been built. A delivery later applies each accepted documentation change to its recorded owner.

## Prepare the specification

When the decisions are settled, invoke `to-spec` in the same conversation:

```text
Use to-spec to turn the accepted invitation design into a specification.
Include every affected repository and the verification decisions we agreed on.
```

The specification captures the problem, solution, user stories, acceptance criteria, repository references, context scope, implementation decisions, testing decisions, and exclusions. Acceptance criteria use stable identifiers such as `AC-1`.

Agree on how the behavior will be tested before publishing. Testing Decisions own the Settled Seams, the agreed interfaces and observable behavior through which the feature will be verified. They include the test approach, ownership, prerequisites, and required evidence. Cross-repository verification belongs here too.

A specification names relevant repositories without granting permission to edit them. The later delivery tickets establish writable Repository Scope. Unresolved design decisions return to planning rather than being invented during ticket generation.

With configured providers, `to-spec` publishes through the Work Tracker mapping and reads the result back through Context Assembly. That operation acquires the required sources into a Context Pack and classifies it as `Complete`, `Incomplete`, or `Ambiguous`. Its entry points to complete local source files, so consumers can read the active artifact first and open supporting material when needed. Publication validates planning completeness and source preservation; execution consumes the prepared contract and reports discovered gaps rather than repeating that audit.

## Split the specification into tickets

```text
Use to-tickets to split this specification into tracer-bullet deliveries.
Show the proposed slices and blocking relationships before publishing.
```

Each ticket delivers a narrow, complete behavior. Prefer a slice that crosses the necessary layers and can be demonstrated independently. One ticket may change several repositories.

The ticket carries its relevant source decisions and acceptance criteria, repository references, writable scope, context scope, cross-repository seams, and blockers. It narrows settled authority without inventing another architecture or test strategy. You review the granularity and dependencies before publication.

Configured trackers store the tickets using their established artifact mapping. Standalone Local Markdown tickets go under `.scratch/<feature>/issues/`. Readiness requires a complete Delivery Context. Tickets produced by `to-tickets` do not need to go through `triage` again.

`triage` is the other entry point for incoming bugs and requests. It clarifies raw reports and prepares executable Agent Briefs before marking them ready.

## Deliver a specification

For a published specification with prepared tickets, invoke:

```text
Use deliver-spec for <specification reference>.
```

The coordinator reads the complete related-ticket set, published writable scopes, and current scheduling state. It records one integration branch per writable repository and prepares the branches needed for the next eligible tickets. It runs them through `deliver-ticket` with automatic merge allowed, supplying targets only for repositories in that ticket's writable scope. Each ticket acquires its own context when launched and keeps its worktrees, source branches, review proposals, and human checkpoints. Independent tickets can run in parallel even when they change the same repository. Future ticket context and repository preparation do not delay a ready launch.

The runtime must support ticket coordinators that can delegate their own implementation and review. Follow the user's context preference, such as separate chats in the same project, and reuse existing execution references on resume. A missing runtime capability is an explicit blocker, not a reason to silently flatten the workflow.

After each ticket meets its own completion criteria, the coordinator invokes `closeout` for that ticket. Confirmed closure releases its dependents before final specification merge. Required acceptance or deployment evidence still applies. Shared specification branches and worktrees survive ticket cleanup.

When the agreed tickets are complete, `deliver-spec` validates and independently reviews the assembled result, then publishes one final proposal per changed repository to its recorded final target. You review and merge those proposals. The Specification stays open for explicit closeout.

Resume with the same specification reference for interruptions or final-review feedback. Overall checkpoints live on the Specification; ticket recovery stays in ticket checkpoints. In-scope corrections use Standalone `implement` and update the existing open proposals without requiring another ticket. Changes to requirements, writable repositories, or active execution choices require reconciliation. If an affected final proposal already merged, agree on a follow-up proposal while preserving its historical result.

## Deliver a ticket

Invoke the coordinator from the Ticket Origin Repository with an exact ticket reference:

```text
Use deliver-ticket for <ticket reference>.
```

Or omit the reference to select one eligible ticket from the configured Delivery frontier:

```text
Use deliver-ticket to take the next eligible ticket.
```

One invocation owns at most one ticket. An empty frontier finishes successfully. A supplied reference selects that ticket only.

For a new delivery, the configured Base Branch and human merge are the defaults. Invocation instructions can select an existing target per writable repository, such as `Target Branch: api=spec/catalog`, and independently allow `Automatic merge: allowed`. See [deliver-ticket](../skills/engineering/deliver-ticket/SKILL.md) for execution options and their contract.

The coordinator:

1. Rechecks eligibility and dependencies, acquires and verifies its claim, and acquires or reuses the selected ticket's complete authority.
2. Consumes the published executable contract and records the chosen targets and merge permission.
3. Resolves the repositories needed for the next implementation, pins selected-target commits, and prepares their isolated worktrees. Read-only sources needed only for later validation are resolved at that stage.
4. Starts `implement` for each ready repository delivery while independent preparation continues. Each receives the accepted Context Pack entry and linked sources, its own scope, and instruction pointers. The implementer reads applicable domain context and ADRs before decisions that depend on them.
5. Runs fresh Standards reviews against the exact changed heads and corrects in-scope blocking findings.
6. Publishes one draft PR or MR per changed repository and verifies the remote revisions.
7. Runs the declared cross-repository validation and a Spec review of the complete bundle. A changed input invalidates the evidence that depends on it.
8. Hands verified proposals to the human or completes authorized merges, records the result and remaining actions, changes the ticket to `ready-for-human`, and releases its claim.

The ticket stays open for acceptance and explicit `closeout`. All required checks and intermediate human checkpoints apply to both merge modes. Repositories used only for context or validation stay outside product write scope.

The same startup applies to direct calls and specification assignments. Keep context snapshots outside worktrees and immutable while consumers use them. Reuse explicitly passed matching packs; independent runs need no shared cache. Acquisition can preserve the full related source set without placing every body in every agent's context. Read current tracker and Code Host state before claims, publication, and merge; a local snapshot does not replace those checks.

### Example across repositories

Suppose an invitation feature changes an API and a web application, and uses a third repository for contract tests.

| Repository | Role in this ticket |
| --- | --- |
| API | Writable delivery for issuing and accepting invitations. |
| Web application | Writable delivery for creating and accepting invitations in the UI. |
| Contract tests | Validation Source at an exact commit. Read-only product scope unless the ticket also authorizes test changes there. |

The ticket's Repository References include all required repositories. Repository Scope authorizes the API and web application changes. Testing Decisions define how those versions will be checked together. The coordinator produces separate review proposals and one combined acceptance result.

Federation describes durable domain ownership. A Delivery Bundle describes the repositories participating in one ticket. They answer different questions. Merely placing checkouts next to each other establishes neither identity nor write permission.

## Handle review and interruptions

Use `change-walkthrough` to explore a change through end-to-end scenarios. Use `review-feedback` to draft actionable feedback and publish it when authorized. Returning a ticket for correction is an explicit review-feedback operation.

Resume an interrupted delivery by invoking `deliver-ticket` with the same ticket reference. It inspects existing claims, checkpoints, proposals, feedback, and revision-bound evidence before deciding which work remains valid. An old assignment does not automatically count as a newly acquired claim.

Resume first identifies the next action from durable execution state, restores recorded choices, and reconciles progress, including partial merges. It reacquires context only when that action needs unavailable authority. Review evidence records governing source content identity, so a new context-file path does not force another review. Changed or unverifiable dependencies require affected checks again. Matching terminal handoffs and missing final effects do not restart implementation. Conflicting instructions or feedback requiring changes to merged code need explicit reconciliation.

Missing authority, a material design contradiction, or a persistent environment failure produces a recorded human action request. Safe work remains available. Planned manual verification also has an explicit request and evidence path. Resolve the stated boundary before resuming dependent work.

## Accept and close out

After review, merge any proposals still awaiting human merge and verify any required deployment. Automatic merge does not supply acceptance or deployment evidence. Once the result meets its completion criteria and you have accepted it:

```text
Use closeout for this delivery.
```

That invocation authorizes the scoped completion record, tracker transition, and cleanup of disposable worktrees and local and remote branches. `closeout` verifies ownership and final revisions, preserves unexplained edits and unrelated resources, and reports anything it retained. It does not supply missing acceptance or deployment evidence.

## Use a shorter route when appropriate

For a small, settled task, invoke `implement` directly with clear authority, writable scope, expected behavior, and verification decisions. It implements and validates the authorized deliveries. Standalone publication and tracker changes require separate authority.

Use `diagnosing-bugs` for investigation, `codebase-design` for module boundaries and test interfaces, and `improve-codebase-architecture` to find candidates for future design work. For a large uncertain effort, `wayfinder` creates a map of decision tickets. Once decisions settle, return to `to-spec` and `to-tickets` before delivery.
