# Runtime Termination

Read [lifecycle artifact contracts](references/bundled/federated-workflow/LIFECYCLE-ARTIFACTS.md) before reconstructing a checkpoint.

Read [execution host liveness](references/bundled/federated-workflow/EXECUTION-HOST.md#liveness-and-termination) before judging termination. A termination source is valid only when its provider record identifies the interrupted Coordinator Activation through its execution reference and scope, reconstructed checkpoint, and termination outcome proven under that contract. Use runtime-reference evidence only for observability and liveness diagnosis. Indeterminate liveness enters the [human-boundary branch](HUMAN-BOUNDARY.md) before claim release.

For proven termination, reconstruct and validate the checkpoint from durable Work Tracker and Code Host state, retaining recorded execution choices and confirmed or pending merge operations. Check recorded child executions too. Coordinator termination proves a child stopped only when that child holds a `session` reference in the coordinator's hosting session. Settle any live or indeterminate child before releasing or reacquiring the claim. Neither a merged proposal nor runtime termination proves missing automatic merge permission. Return the ticket to unassigned `ready-for-agent`, reacquire the Workflow Identity claim, and return to the [Resume Gate](RECOVERY.md) with runtime termination qualified as the sole source. Local-only work remains excluded until human reconciliation establishes provenance.

**Complete when:** provider/runtime evidence proves termination and binds to the checkpoint, or one human boundary owns the unresolved liveness; elapsed time and live memory decide nothing.
