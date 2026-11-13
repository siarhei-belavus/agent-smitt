# Mechanical delivery validation

Use the bundled [Python validator](scripts/validate_delivery.py) to check local delivery results or compare declared evidence dependencies. It needs Python 3.10 or later and Git for local inspection. It uses the standard library, works with native paths on macOS, Linux, and Windows, and runs without shell commands or provider access.

Run `python3 <path-to-validate_delivery.py> <input.json>`, or pass `-` to read UTF-8 JSON from stdin. Resolve the script from this document's link in the installed skill. Keep input and output outside delivery worktrees and durable records. Host-local paths belong only to this invocation.

## Owner responsibilities

The calling workflow owns the accepted scope, Repository ID resolution, complete set of required results, and complete dependency sets. Inspect accepted requirements, new decisions, and feedback before constructing the input. Derive facts from the assigned result, recorded evidence, and current observations independently. Copying an evidence dependency into the observations does not establish freshness.

The validator checks declared facts mechanically. It does not interpret requirements, establish source membership, inspect test logs, prove a test passed, or authorize a claim, publication, merge, or resume. A `consistent` report is not a delivery pass. Apply every semantic, provider, review, and lifecycle gate in the calling workflow afterward.

This helper is optional. When Python, Git, or the helper is unavailable, perform the same checks through the workflow's existing manual procedure. Investigate a reported mismatch or missing fact; switching to manual checks does not waive it.

## Input contract

Supply exactly these fields with `schema_version: 1`:

| Field | Contents |
| --- | --- |
| `deliveries` | Array of local results to inspect. Each has `repository_id`, absolute native `path`, expected `remote`, `branch`, `base`, and `head`. Revisions are full lowercase 40- or 64-character Git object IDs. The path must name the worktree root. The remote is the resolved `origin` fetch URL. |
| `observations` | Object mapping dependency keys to current immutable identities. A missing key or `null` means unknown. Other values must be nonempty strings. |
| `required_evidence` | Unique IDs of all evidence required at the current gate. Missing records prevent a consistent result. |
| `evidence` | Records with unique `id`, `result` of `pass`, `fail`, or `pending`, and a nonempty `dependencies` object mapping keys to the immutable identities recorded when the evidence was produced. |

Unknown fields, duplicate JSON keys or IDs, malformed records, abbreviated revisions, and a request with no deliveries, required evidence, or evidence are invalid. Empty arrays are otherwise allowed, including for validation after losing a local checkout.

For each local delivery, the helper observes its root, HEAD, branch, remote, base commit availability, and cleanliness for supported worktrees. It supplies `head:<repository_id>` itself; callers cannot also supply that key. An identity mismatch, dirty worktree, unavailable Git state, or observed HEAD movement makes that dependency unknown. A stable changed HEAD is available for comparison and also reports a delivery mismatch. Git subprocesses clear inherited repository, index, object, and injected configuration overrides. They retain the caller's `GIT_CONFIG_GLOBAL`, `GIT_CONFIG_SYSTEM`, and `GIT_CONFIG_NOSYSTEM` configuration-file selectors. They disable optional locks, filesystem monitors, lazy object fetching, and all transport protocols. They write no files and perform no network operations. Missing objects in a partial clone remain unavailable.

Before checking cleanliness, the helper detects tracked submodules and any configured clean or process filter, including global filter configuration. Either produces `attention` with `submodules_require_manual_check` or `filters_require_manual_check`, leaves `clean` unknown, and makes the local head dependency unusable. It does not enter submodules or run filters. Use the existing repository-native manual validation path for these cases; declaring them clean or disabling their transformations would weaken the check. This conservative limitation also applies when a configured filter is unused by the current paths.

Other keys are caller-owned. Include every dependency required by the governing evidence contract: review bases, influencing delivery heads, Validation Source commits, governing source content and membership, and dependent evidence identities where applicable. Before recording or reusing review evidence, apply [Authority evidence](AUTHORITY-EVIDENCE.md). Compare stable content identities, never Context Pack paths or acquisition timestamps. Unknown or incomplete dependency coverage requires refresh even when all supplied values match.

For already merged deliveries or missing local worktrees, leave those repositories out of `deliveries` and obtain their historical published source identities through the configured provider. Supply those observations explicitly. Preserve the source/result relationship and partial-merge rules in the calling workflow; a current target tip cannot replace a historical validated source.

Example of an evidence-only comparison, with illustrative identities:

```json
{
  "schema_version": 1,
  "deliveries": [],
  "observations": {
    "head:api": "1111111111111111111111111111111111111111",
    "authority:ticket": "sha256:accepted-content-and-membership"
  },
  "required_evidence": ["api-tests"],
  "evidence": [{
    "id": "api-tests",
    "result": "pass",
    "dependencies": {
      "head:api": "1111111111111111111111111111111111111111",
      "authority:ticket": "sha256:accepted-content-and-membership"
    }
  }]
}
```

## Results and continuation

The helper emits one JSON object with `schema_version`, `status`, `issues`, observed `deliveries`, and classified `evidence`:

- Exit `0`, `consistent`: all declared local checks match, required evidence is present, and every supplied evidence record is current and passing.
- Exit `1`, `attention`: at least one local check or required result failed, or evidence is stale, unknown, or not passing.
- Exit `2`, `invalid`: input is unavailable, malformed, incomplete, or ambiguous. No delivery result is accepted.

Each evidence result includes its `id`, `status`, and sorted `changed` and `missing` dependency keys. `not_passed` takes precedence for failed or pending evidence; otherwise missing observations produce `unknown`, differing known identities produce `stale`, and matching identities produce `current`. Both diagnostic lists remain available. Issues contain a code and subject without echoing Git stderr or input values. Ordinary argument errors use argparse's help and exit `2`.

The observation is a point-in-time check, not a lock or a durable claim. External writes can race it. Repeat the required live checks at publication, merge, and resume boundaries. Changed influencing inputs invalidate the results that depend on them; unchanged independent results remain reusable only under the full workflow contract.
