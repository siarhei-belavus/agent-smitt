# Execution host

The Execution Host is the agent runtime running a workflow activation. It supplies delegated contexts, the activation's local filesystem, and references to running executions. Workflows depend on the capabilities below, not on a runtime's tool names or agent topology.

## Capabilities

| Capability | Meaning |
| --- | --- |
| Fresh delegation | Start a context without the parent conversation, give it a self-contained assignment, and let it read and write the activation's local filesystem. |
| Delegation depth | How many levels of delegated contexts may start their own delegated contexts. A separate top-level session started by the activation delegates from depth zero. |
| Continuation | Send further input to a delegated context while its execution remains available. |
| Execution reference | An identifier that lets an activation find, observe, continue, or stop an execution. Its **scope** is `session` when the reference and its executions end with the hosting session, or `durable` when they survive it, such as a resumable session ID or a task URL. |
| Liveness evidence | An authoritative host observation that an execution is running or terminal. |

Take capabilities stated by the runtime's agent instructions or the user as given. Learn delegation depth by use, without a probe run: start delegated contexts through the host's ordinary delegation, and let each context that must delegate confirm its own capability as its first action.

## Delegated contexts

A delegated context is any fresh context the host can start: a subagent, a separate chat or session, or a headless runtime process. Each one satisfies a workflow's freshness requirement when it starts without the parent conversation and receives a self-contained assignment.

A context whose assignment requires delegation inspects its own tools before any provider mutation, claim, or repository change. When it has no tool that starts a delegated context, it returns a **Capability Blocker** naming the missing capability and stops with nothing changed. A Capability Blocker is a terminal result, so the same assignment may be relaunched safely through another mechanism.

On a Capability Blocker, the parent starts that assignment as a separate top-level session through a mechanism the host and user preferences support, preferring one with a durable execution reference. When no such mechanism exists, report the missing capability and obtain an authorized alternative. Each role keeps its own context: one context performing a coordinator's and its workers' assignments together is not an alternative.

## Liveness and termination

Record every started execution's reference and scope before relying on it.

- For a `durable` reference, prove termination through host-reported terminal state for that reference.
- For a `session` reference, an execution ends with its hosting session. Proven termination of the hosting session therefore proves termination of every execution it started. Prove it through host session state or a human response that confirms it, recorded with the checkpoint it unblocks.
- Inside the current activation, a returned final result or a host-reported terminal state proves termination. Otherwise request a stop through the host and wait for its terminal report.

Silence, elapsed time, an old timestamp, or a missing local process proves nothing. A `session` reference from an earlier session supports diagnosis only; it cannot be observed or continued.
