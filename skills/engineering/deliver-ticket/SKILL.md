---
name: deliver-ticket
description: "Deliver or resume one prepared ticket through implementation, review, optional automatic merge, and human handoff. Use directly or for a ticket assigned by deliver-spec."
---

Read [Context Pack consumption](references/bundled/federated-workflow/CONTEXT-PACK.md) before accepting ticket authority. The same execution path applies to direct calls and assignments from a specification coordinator.

A Coordinator Activation is one invocation that selects or resumes at most one ticket and owns only a claim it acquires and verifies.

Coordinate `/deliver-ticket [<ticket reference>]` fail closed. A supplied reference selects that ticket only. Without a reference, select and claim at most one ticket from the configured Delivery frontier. An empty frontier is a successful no-op.

Accept optional execution instructions naming a Target Branch per writable Repository ID and Automatic merge permission, either `allowed` or `disabled`. On a new delivery, omitted targets use the configured Base Branch and omitted permission is `disabled`. These options are independent and belong to this ticket's execution. Permission replaces only the final wait for human review and merge; intermediate human boundaries and host policy still apply. On an existing delivery, restore the options through [recovery](RECOVERY.md) before applying defaults. They change neither planning artifacts nor Repository Scope, and add no dependency checks beyond the existing tracker eligibility rules.

Use repository-owned bindings for every provider operation. Persist no provider commands, credentials, or account identity. Preserve recoverable work. Merge only through the explicitly authorized [automatic merge branch](AUTOMATIC-MERGE.md). Never push a protected branch directly, close the ticket, invoke closeout, or remove delivery worktrees or branches.

## 1. Establish activation authority

Resolve tickets only through the configured Ticket Origin Repository. Read its `AGENTS.md`, Work Tracker, and Routing Label bindings before selecting a ticket. Load repository preparation, domain, and Code Host instructions when the next action needs them.

Choose one activation ticket. With a supplied reference, resolve exactly that ticket and never substitute another. Without a reference, read the Work Tracker's ordinary Markdown `## Delivery frontier` instructions and query the configured tracker. Authoritatively re-read every candidate's ticket, Routing Labels, assignees, and dependencies before deciding eligibility. Keep open, unblocked, unassigned tickets carrying exactly `ready-for-agent`, then order them as the binding says. If no eligible ticket remains, finish successfully without creating a bundle or changing provider state.

Read the selected ticket's dependencies, routing, assignee, coordination notes, Review Feedback, and Code Host state needed to classify eligibility and recovery. Read complete comment pagination only when the binding offers no narrower coordination-log operation. Leave the ticket body and delivery authority to Context Assembly in step 2. A ticketless candidate that becomes ineligible before mutation returns to selection against current provider state. A named ticket that is ineligible or assigned elsewhere stops at the applicable runtime-termination or human boundary and never falls back to frontier selection.

Classify the claim before recovery. Only a claim acquired and provider-verified during this activation is current. Any assignment already present on a named ticket is foreign or interrupted, including an assignment to the Workflow Identity, so read [runtime termination](RUNTIME-TERMINATION.md) before mutation.

When any prior checkpoint, request, response, Resumption Record, existing Review Proposal, or handoff exists, read [recovery](RECOVERY.md) before mutation. Otherwise resolve the Workflow Identity and re-read the selected ticket's Routing Labels, assignees, and dependencies immediately before claiming it. Require it to remain open, unblocked, unassigned, and exactly `ready-for-agent`. Assign only the Workflow Identity, then authoritatively re-read the same state and proceed only when that identity is the sole assignee and every eligibility condition still holds.

For a ticketless activation, any pre-claim change or failed post-claim verification recomputes the ordered frontier from current provider state. Repeat the selection and recovery checks, then attempt another claim. Stop after the first verified claim, so the activation claims at most one ticket. For a named ticket, the same race enters the applicable human boundary instead of selecting another ticket.

**Complete when:** the ticketless frontier is empty; recovery has produced and verified its terminal or resumable durable result; or one open, unblocked, exactly `ready-for-agent` ticket is solely assigned to the Workflow Identity through a claim verified in this Coordinator Activation.

## 2. Accept the prepared ticket

After the claim is verified, acquire or reuse `Complete` Delivery Context for the claimed ticket through the consumption contract. Retain its entry path as **Authority input** for this execution and pass it to consumers. Read the active ticket and applicable accepted changes; use indexed sources when the current action needs them. For `Incomplete` or `Ambiguous`, enter the [human-boundary branch](HUMAN-BOUNDARY.md) with the claim and safe state preserved.

Consume the published Repository References, non-empty writable Repository Scope, outcomes, acceptance criteria, Context Scope, settled decisions, and Validation Obligations. Publication owns their planning validation. Confirm that these records identify the authorized implementation assignments and report a discovered gap or contradiction through the human boundary. Do not reconstruct planning history to prove readiness again.

A Delivery Bundle is one ticket's complete delivery state: its Repository Deliveries; any Published Delivery Heads, Review Proposals, and lifecycle records; current validation and review evidence; and handoff state.

Resolve execution options against the complete writable Repository Scope. Require each override to name exactly one writable Repository ID and one target branch on its declared remote; verify branch existence after repository resolution. Reject ambiguous or out-of-scope instructions through the human boundary. Read [lifecycle artifact contracts](references/bundled/federated-workflow/LIFECYCLE-ARTIFACTS.md) and publish and re-read an initial Execution Checkpoint carrying the resolved choices and their invocation authority before preparing repository work. Record unprepared delivery fields as pending, never as invented revisions.

**Complete when:** the claimed ticket has accepted authority and executable assignments, and the resolved execution choices have a verified durable checkpoint; otherwise the delivery has entered the [human-boundary branch](HUMAN-BOUNDARY.md) before repository mutation.

Run steps 3 through 5 for each independent Repository Delivery as its prerequisites become available. Start a prepared delivery while other independent preparation continues. A shared seam or required source that affects its implementation is a prerequisite; a repository used only for later validation is not. Preserve the complete bundle scope and pending entries in checkpoints.

## 3. Resolve repository references

Before preparing a delivery, read [execution preparation](EXECUTION-PREPARATION.md).

Repository Resolution binds each Repository Reference to one validated Repository Store.

Resolve the delivery's writable repository and any read-only source required to begin that implementation. Validate and reuse a matching current checkout, explicitly supplied checkout, known worktree, execution-host checkout, or bounded nearby Repository Store. Otherwise prepare a checkout from the reference's declared remote at an execution-host location. Folder proximity neither grants relevance nor proves repository identity. Use no repository registry or broad filesystem scan. Resolve validation-only references in step 8 before their checks run.

Validate each candidate against its Repository ID, remote, Git and worktree identity, and repository-local Code Host binding. Record a material inferred or prepared binding by its portable repository identity and validation evidence, without its local path. Read the repository instructions and setup sources needed for preparation. Pass domain routing and Context Scope pointers to `implement`, which owns reading applicable canonical context, ADRs, and prior art before its implementation decisions. Preserve each Repository Store's checkout state and use it only as a Git source for worktree creation, never as a delivery workspace.

Verify the selected Target Branch exists and is readable through its binding. When automatic merge is allowed, read the binding's declared [conditional merge capability](references/bundled/federated-workflow/PROVIDER-BINDINGS.md#conditional-merge-capability). A missing, unverified, or prohibitive capability is a known Environment Preparation Blocker; request explicit binding reconciliation without changing choices or repository settings. Read live proposal checks, approvals, mergeability, and source/target guards at publication or merge, when those operations need them.

**Complete when:** this delivery's repository and immediate sources resolve, its target is readable, and its preparation instructions and declared capabilities permit the next action; otherwise the affected work has entered the [human-boundary branch](HUMAN-BOUNDARY.md).

## 4. Prepare repository deliveries

Apply the execution-preparation rules to the resolved delivery. Fetch its selected Target Branch without switching the Repository Store and pin its fresh exact launch commit and initial Fixed Review Base. Prepare or reuse one clean isolated Execution Worktree and unique delivery branch. Keep deliveries later classified as no-change at their pins and read-only repositories outside writable scope. Keep the Repository ID-to-worktree mapping in execution-host state; portable records identify the delivery, target, branch, launch commit, current Fixed Review Base, and exact head without a local path. Publish and re-read the bundle snapshot with this delivery prepared and other entries accurately pending before dispatch.

**Complete when:** this delivery has a provenance-verified persistent worktree at its intended branch and fixed base, immediate mandatory bootstrap has succeeded, and existing user checkout state is unchanged; otherwise preserve safe work at the [human-boundary branch](HUMAN-BOUNDARY.md).

## 5. Execute one flat attempt

Start exactly one direct-child Implementation Agent for each prepared delivery requiring changes. Give it one complete textual narrowing assignment for its Repository Scope entry and run `implement`. Include the Repository ID and Reference, Execution Worktree, branch, fixed base, accepted Context Pack entry path, repository-specific outcome, Settled Seams and test approaches, Validation Obligations, and repository instruction and validation-source pointers. `implement` resolves repository validation commands through those sources. For corrections, include actionable feedback by permanent provider ID and require an attributable disposition for every item. Require its one Repository Delivery result. Record validation-only and no-change deliveries directly. The Implementation Agent reads the accepted pack selectively and performs no Context Assembly or provider read.

Verify every result against its assigned worktree and base; classify an expected change with no diff as unchanged.

**Complete when:** every changed assignment preserves the Authority input from step 2, every scope entry has exactly one attributable result, every changed worktree is clean at its exact local head, all repository validation is bound to that head, and any discovered contradiction or material design decision has entered the [human-boundary branch](HUMAN-BOUNDARY.md) with affected and dependent work paused.

## 6. Review exact heads

For each changed delivery, verify its fixed-base diff and exact-head validation, then use the `code-review` skill in **Standards only** mode. Its fixed Repository Target includes the unchanged accepted Context Pack path from step 2, together with seams and evidence. Record Advisory findings. Route each attributable in-scope Blocking finding to the affected Implementation Agent. After a correction, refresh repository validation and launch another fresh Standards review against the new exact head with the same path. Reviewers reuse the file and perform no Context Assembly or provider read. Repeat until the result has no Blocking finding or a Specification Contradiction, Material Design Opportunity, or another genuine authority boundary applies.

**Complete when:** every changed exact head has current repository validation and a fresh Standards result bound to the Authority input from step 2, with no Blocking finding; a persistent or authority-changing finding has entered the [human-boundary branch](HUMAN-BOUNDARY.md).

## 7. Publish Review Proposals

Using each changed repository's Code Host binding, publish its delivery branch and verify its remote exact head. Create or update its single Draft Review Proposal to the selected Target Branch; re-read its source, target, draft state, and head. Publish nothing for unchanged deliveries. On resumed or partially merged work, preserve confirmed merged proposals and their recorded source/result revisions; publish updates only for still-open proposals.

**Complete when:** each pending changed delivery has one verified Draft Review Proposal at its exact Published Delivery Head, confirmed merged deliveries remain preserved, and this publication step has changed no Target Branch.

## 8. Validate the bundle

Ad hoc validation is allowed. Keep one-off validation code outside the committed delivery. If a check belongs in the MR or PR, implement it as a regular test following the repository's existing test conventions. Do not commit ad hoc runners or their supporting configuration and documentation.

Resolve deferred repository-backed Validation Sources through step 3's repository identity rules, read their validation instructions, and record exact commits before validation dispatch. Prepare or reuse isolated working state at each unchanged source commit outside Repository Scope, applying execution preparation before any local mutation. Run validation there so mutable outputs cannot pollute the configured Repository Store. Launch fresh direct-child Validation Agents against the stable exact Published Delivery Head set and declared Validation Sources. Each assignment and its resulting cross-repository evidence bind every repository-backed Validation Source it uses to that recorded exact commit. Assign every mandatory cross-repository Validation Obligation to exactly one agent. Compatible obligations may share one Validation Agent only when they execute through the same compatible Validation Source, with one recorded exact source commit and coherent setup and evidence ownership. Each agent follows the declared prerequisites, method, scenario, expected result, and evidence format. It produces evidence, changes no product code, and makes no whole-ticket Spec judgment.

After every mandatory obligation has current passing evidence, use the `code-review` skill in **Spec only** mode over the complete changed target set. Every Repository Target carries the unchanged accepted Context Pack path from step 2, together with all seams, evidence, and proposals. Record Advisory findings. Route attributable in-scope Blocking findings to the affected Implementation Agents. After a changed influencing delivery head, refresh its repository validation and fresh Standards review using that same path. Reviewers reuse the file and perform no Context Assembly or provider read. A changed influencing delivery head or exact Validation Source commit invalidates only dependent cross-repository evidence and the Bundle Spec result. Rerun every invalidated obligation with fresh Validation Agents before another fresh full-bundle Spec review. Repeat until the result has no Blocking finding or a Specification Contradiction, Material Design Opportunity, or another genuine authority boundary applies.

**Complete when:** every declared obligation and fresh Bundle Spec result passes against one current exact delivery-head and Validation Source commit set and accepted authority; evidence made stale by changed influencing revisions or governing authority has been refreshed while unchanged-dependency evidence remains current, or planned human verification has entered the [human-boundary branch](HUMAN-BOUNDARY.md).

## 9. Hand off idempotently

Re-read the ticket, claim, Published Delivery Heads, proposals, feedback, and current evidence. Return any drift to its earliest invalidated prerequisite. When Automatic merge is allowed, execute [automatic merge](AUTOMATIC-MERGE.md) before final handoff; otherwise mark every verified open proposal ready and re-read it. Preserve already merged proposals. Build `deliver-ticket:<canonical ticket reference>:<SHA-256 of sorted Repository ID=exact head lines>`. A matching key also requires matching execution choices and proposal states; the key alone is not completion proof.

Read [lifecycle artifact contracts](references/bundled/federated-workflow/LIFECYCLE-ARTIFACTS.md) completely before writing the final handoff. Reuse a matching handoff; otherwise append one complete Execution Checkpoint under that contract. Include Advisory findings and the remaining human actions in merge, rollout, and acceptance order. The handoff is the final checkpoint, so create no duplicate note. Apply only missing final effects in order: replace `ready-for-agent` with exactly `ready-for-human`, release the Workflow Identity claim, re-read both effects, and leave the ticket open.

**Complete when:** exactly one matching handoff exists and the ticket is open, unassigned, and carries exactly `ready-for-human` among Routing Labels. With automatic merge disabled, every proposal is ready at its recorded head or independently confirmed merged. With automatic merge allowed, every changed delivery has a confirmed merge result. No-change deliveries require no proposal or merge.

Report the ticket, host-local worktree disposition, fixed bases and heads, validation, proposals, review outcomes, and final Work Tracker state.
