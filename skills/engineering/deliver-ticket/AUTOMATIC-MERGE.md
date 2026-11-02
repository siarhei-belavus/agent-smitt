# Automatic merge

## Prepare the current result

For every unmerged changed delivery, fetch and pin the current Target Branch tip. If it differs from the current Fixed Review Base, synchronize that tip into the delivery's isolated source branch while preserving concurrent work. Resolve only conflicts whose result follows from accepted requirements. Inspect both intents; a semantic conflict requiring new authority stops at the human boundary with the unresolved state preserved.

Keep the original launch commit. Record the synchronized target commit as the new Fixed Review Base. Apply [the evidence validity rules](RECOVERY.md#evidence-validity), rerun invalidated repository validation, and resume [the delivery workflow](SKILL.md) at the earliest remaining prerequisite. Refresh evidence through that workflow before continuing here. Review the current target-to-source diff so unrelated target changes are not attributed to this ticket.

Apply [the confirmed-result preservation rules](RECOVERY.md#evidence-validity) to already merged deliveries throughout preparation and merge.

**Complete when:** one current bundle has all required evidence and reviews for its recorded source revisions, review bases, and validation sources, with no unresolved blocker. Textual mergeability alone does not meet this criterion.

## Merge and verify

Honor the declared merge order. If none is required, process repositories in stable Repository ID order. Before each operation:

1. Re-read the current claim, permission, requests, source revision, target tip, host checks, approvals, and blocking feedback. Any drift returns to its earliest invalidated prerequisite. Mark the verified open proposal ready and re-read it.
2. Publish and re-read an Execution Checkpoint containing the complete execution choices, current evidence, exact proposal/source/target pair, prior confirmed results, and this merge as the next permissible operation.
3. Submit the verified source/target pair through the binding's revision-safe merge operation and repository-selected strategy. Every prerequisite from Prepare the current result, including Standards, Bundle Spec, and applicable manual evidence, must pass before merge. If a queue changes the combination, hold it and repeat preparation and that readiness gate before permitting merge. Use the binding's verified guard or hold mechanism; unavailable guarantees enter the human boundary.
4. [Reconcile the outcome](#reconcile-the-outcome). A confirmed non-merge returns to preparation for an authorized retry; proceed to the next repository only after a confirmed merge.
5. Append and re-read the updated checkpoint before proceeding to the next repository.

A moved target before a guarded merge returns to preparation and evidence refresh.

**Complete when:** every changed delivery has a provider-confirmed merge into its selected target, with recorded source/result revisions and applicable evidence. Unchanged deliveries require no merge. An unresolved operation enters the existing human boundary instead of final handoff.

## Reconcile the outcome

Re-read authoritative provider state for the recorded proposal and operation. A queued operation, timeout, or lost response remains unconfirmed until provider truth establishes its outcome. Use bounded diagnosis for a persistent unknown or failed state, then enter the human boundary with the operation reference and remaining work preserved. Outcome lookup grants no permission to submit another operation.

For a confirmed merge, verify that its source and target match the recorded pair and obtain the exact result revision. For merge, squash, or rebase, prove the resulting tree matches the combination whose validation and review prerequisites passed before merge. Post-merge retrieval verifies that evidence; it never supplies a missing pre-merge check or review. Record discrepancies as a human boundary and preserve any merge that already occurred.

**Complete when:** the operation is confirmed merged with its revisions and evidence, or confirmed not merged with no pending operation. Only the latter may return to preparation for a separately authorized retry. An indeterminate outcome remains at the human boundary.
