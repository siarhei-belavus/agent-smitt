# Automatic merge

Read this branch when Automatic merge is explicitly allowed, or when recovery must reconcile a recorded merge operation. It removes only the final wait for human review and merge. All implementation, review, validation, manual verification, claim, and human-boundary requirements still apply.

## Validate the binding

Before implementation, verify each writable repository's Code Host binding against the [conditional merge capability](references/bundled/federated-workflow/PROVIDER-BINDINGS.md#conditional-merge-capability). Confirm that the selected target is readable and the binding describes the required operations and permissions. Recheck actual merge readiness before the operation. A missing or prohibitive binding is an Environment Preparation Blocker; preserve work and request a compatible binding through the existing human boundary. Do not rewrite repository bindings implicitly or treat this mode as host approval.

**Complete when:** every writable repository can support the authorized path, or the existing human boundary records the precise missing capability.

## Prepare the current result

Re-read the ticket, current claim, execution choices, active human requests, proposals, source revisions, target tips, host checks, and actionable feedback. Require the current verified claim and all bundle prerequisites from steps 6 and 8. Resolve in-scope feedback through the existing correction/review loop; a required human decision or approval remains a human boundary.

For every unmerged changed delivery, fetch and pin the current Target Branch tip. If it differs from the current Fixed Review Base, synchronize that tip into the delivery's isolated source branch while preserving concurrent work. Resolve only conflicts whose result follows from accepted requirements. Inspect both intents; a semantic conflict requiring new authority stops at the human boundary with the unresolved state preserved.

Keep the original launch commit. Record the synchronized target commit as the new Fixed Review Base and return the resulting source head through repository validation, fresh Standards review, publication to the same proposal, dependent cross-repository validation, and fresh Bundle Spec review. Review the current target-to-source diff so unrelated target changes are not attributed to this ticket. A changed review base invalidates its Standards result and Bundle Spec even if the source head stays unchanged; affected validation must account for the combined result. Keep unchanged-dependency evidence under [recovery's evidence rule](RECOVERY.md).

Keep already merged deliveries fixed at their recorded source and confirmed result. They can participate in read-only review and validation. If new work would require changing one, preserve the partial result and enter the human boundary for an explicit follow-up plan instead of reopening or reusing its merged proposal.

**Complete when:** one current bundle has all required evidence and reviews for its recorded source revisions, review bases, and validation sources, with no unresolved blocker. Textual mergeability alone does not meet this criterion.

## Merge and verify

Honor the declared merge order. If none is required, process repositories in stable Repository ID order. Before each operation:

1. Re-read the current claim, permission, requests, source revision, target tip, host checks, approvals, and blocking feedback. Any drift returns to its earliest invalidated prerequisite. Mark the verified open proposal ready and re-read it.
2. Publish and re-read an Execution Checkpoint containing the complete execution choices, current evidence, exact proposal/source/target pair, prior confirmed results, and this merge as the next permissible operation.
3. Submit the verified source/target pair through the binding's revision-safe merge operation and repository-selected strategy. Every prerequisite from Prepare the current result, including Standards, Bundle Spec, and applicable manual evidence, must pass before merge. If a queue changes the combination, hold it and repeat that readiness gate before permitting merge. Use the binding's verified guard or hold mechanism; unavailable guarantees enter the human boundary.
4. Re-read authoritative provider state. Confirm the proposal merged into the selected target from the recorded source revision and obtain the exact result revision. For merge, squash, or rebase, prove the resulting tree matches the combination whose validation and review prerequisites passed before merge. Post-merge retrieval verifies that evidence; it never supplies a missing pre-merge check or review. Record discrepancies as a human boundary and preserve any merge that already occurred.
5. Append and re-read the updated checkpoint before proceeding to the next repository. Preserve delivery branches and worktrees for explicit closeout.

A moved target before a guarded merge returns to preparation and evidence refresh. A rejected operation is not success. A queued operation, timeout, or lost response remains unconfirmed until provider truth establishes its outcome. Re-read an existing pending operation before any retry; never enqueue or merge twice. Use bounded diagnosis for a persistent unknown or failed state, then enter the human boundary with the operation reference and remaining work preserved.

Merges across repositories are not atomic. Preserve confirmed results and finish only the remaining authorized work after recovery. A later failure does not authorize rollback, ticket closure, or reporting the bundle as merged.

**Complete when:** every changed delivery has a provider-confirmed merge into its selected target, with recorded source/result revisions and applicable evidence; otherwise one existing human boundary owns the unresolved state. Unchanged deliveries require no merge. Continue to final handoff only after this condition passes.
