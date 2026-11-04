# Delivery records

Read [repository identity](REPOSITORY-IDENTITY.md) and [module vocabulary](../codebase-design/MODULE-VOCABULARY.md) before applying these records.

## Repository Delivery

A Repository Delivery is one repository's authorized unit of work from fixed base to attributable exact-head result, including its repository-owned validation evidence.

A **Target Branch** is the existing remote branch selected for that delivery's execution, defaulting to the Repository Reference's configured Base Branch. It supplies the initial launch commit and receives the Review Proposal. Selecting it neither rewrites the Repository Reference nor expands Repository Scope.

The exact launch commit records where execution began and remains immutable. The **Fixed Review Base** is the exact commit bounding the current delivery diff, initially the launch commit. A target synchronization may advance the review base while preserving launch provenance and refreshing evidence for the new review bounds.

## Repository Store

A Repository Store is the validated Git checkout selected by Repository Resolution to supply Git storage without becoming a delivery workspace. Delivery preparation may fetch and register its own worktree while preserving the Store's checked-out branch, index, files, remotes, hooks, and configuration.

## Execution Worktree

An Execution Worktree is an isolated writable Git worktree assigned to one Repository Delivery across its Execution Attempts. Its host-local path is neither its identity nor portable delivery state. It persists until explicit safe cleanup. The Repository Scope entry, not the worktree, grants write authority.

## Repository Reference

A Repository Reference makes one repository resolvable without granting write authority or creating a Repository Delivery. It contains:

- Repository ID;
- remote;
- Base Branch.

## Authority input

For Work Tracker-backed delivery, Authority input is the entry path to one accepted runtime-local `Complete` Context Pack. Apply [Context Pack consumption](CONTEXT-PACK.md) when acquiring, sharing, or reading it. Coordinator-narrowed implementation and review agents use that pack without provider reads. The path locates the snapshot; it is not the identity of its requirements.

### Authority evidence

Bind review evidence to the profile, permanent root, governing source and effective Resolution set, and the content of those sources. Record immutable source revisions when available; otherwise record SHA-256 fingerprints of the exact UTF-8 authoritative bodies and recognized decision text, identified by permanent references. Include applicable accepted human directions and repository instruction, canonical-context, and ADR revisions used by the result. Keep this binding with the existing evidence record, not in a separate registry.

Compare these dependencies when reusing evidence. A different local path or acquisition timestamp does not change authority. Routing, claim state, and operational checkpoint comments are not requirements. Inspect new or edited comments for accepted authority or actionable feedback before excluding them; a matching old source set alone cannot prove that no governing decision was added. Changed governing content or membership invalidates dependent reviews and any validation obligation whose meaning changed. Unchanged dependencies preserve their results. If an earlier record lacks enough content identity to establish equivalence, refresh the affected review instead of assuming it still passes.

## Settled Seam

A Settled Seam is an accepted caller-visible Interface contract at a Seam. Execution preserves it unless authoritative input explicitly changes it. It records:

- owning module and Repository ID;
- providers and consumers by Repository ID;
- caller/test-visible interface;
- location;
- status: `new`, `changed`, or `unchanged`;
- observable behavior;
- selected repository-native test approach;
- nearest prior art; and
- each applicable Validation Obligation.

A cross-repository seam uses the same record with providers or consumers in different repositories. Its Validation Obligations stay with the seam rather than moving to a separate validation section.

## Validation Obligation

A Validation Obligation is an authority-backed behavior claim that one named owner must prove with reproducible evidence. It records the behavior to prove, its owner, affected Repository Deliveries, Validation Source, prerequisites, method, scenario, expected result, and required evidence.

When proving acceptance criteria, identify their source and criterion identifiers where assigned. Keep the obligation's required fields explicit and consistent with those criteria; a reference does not replace the behavior claim, scenario, or expected result.

A Validation Source is the exact repository revision or identified external harness or environment used to produce that evidence. An unchanged repository may be a read-only Validation Source. Creating or changing its validation entrypoint, assertions, or setup requires a Repository Scope entry for that repository.

A cross-repository Validation Obligation uses the same record when its affected Repository Deliveries or Validation Source span repositories.

## Repository Scope entry

A Repository Scope entry authorizes writes to exactly one referenced Repository ID and produces one Repository Delivery. It records:

- required repository-owned outcome;
- applicable repository-local Settled Seams; and
- repository-owned Validation Obligations.

Repository Scope is a non-empty writable subset of Repository References in every executable delivery artifact. Read-only context, validation, and decision sources remain references outside the scope. A required canonical documentation change places its owning repository in scope, including a documentation-only Repository Delivery when no code change belongs there.
