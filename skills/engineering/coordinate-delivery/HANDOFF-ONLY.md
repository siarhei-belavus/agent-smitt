# Handoff-Only Recovery

After [recovery](RECOVERY.md) has published the Resumption Record for this branch, start a normal Execution Attempt with zero Implementation Agents. Re-read execution choices, exact source/result revisions, evidence, proposal merge states, ticket claim, routing, and the deterministic handoff key. If recovery invalidated required evidence, return to its earliest prerequisite before final effects. Apply only the missing effects through [Hand off idempotently](SKILL.md#9-hand-off-idempotently) and reuse any matching note or proposal. Confirmed merges need only missing record and handoff effects; an outstanding or uncertain automatic merge returns to [automatic merge](AUTOMATIC-MERGE.md), never an unconditional retry.

**Complete when:** the Delivery Bundle handoff is complete and no implementation, duplicate handoff, duplicate proposal, or unrelated mutation occurred.
