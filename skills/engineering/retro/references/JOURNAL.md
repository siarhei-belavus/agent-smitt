# Private change journal

Journal format: 1

This contract records accepted changes to an agent's working process and later evidence of their effects. It works for one project or several, without provider bindings or a configured federation. The journal is private user state. The instructions, checks, and documentation changed by a decision remain in their owning files.

## Location and initialization

Use the absolute directory in `AGENT_WORKFLOW_JOURNAL` when set. Otherwise use `$XDG_STATE_HOME/agent-workflow/journal` when `XDG_STATE_HOME` is an absolute path, or `$HOME/.local/state/agent-workflow/journal`. Use the same resolved directory across projects and chats. Report an invalid override instead of silently choosing another journal.

The directory contains `README.md`, with storage metadata, and `changes/`, with one Markdown file per accepted change. Store records outside repositories, installed skills, and shared or synchronized folders. Use owner-only access through the host's file permissions or equivalent access controls. Keep secrets and copied private conversations out of records; retain source references and the smallest useful paraphrase.

Read this contract from the consuming skill's packaged references. On the first accepted change, create the directory and the following `README.md` without replacing an existing file:

```markdown
# Private workflow change journal

Journal format: 1

Records live in changes/. This directory contains private user data.
Recording and evaluation tools provide the journal contract with their skills.
```

When the journal exists, verify the format in `README.md` and the records being read or updated. Legacy format-1 README files may contain a full contract copy; use their format marker as metadata and this packaged contract for instructions. The legacy prose can be replaced with the metadata above while preserving every record. A format mismatch, inaccessible journal, or records without storage metadata is a reporting gap, not permission to reset them. Continue independently authorized work and report any unrecorded changes. Changing the record format requires an explicit migration that preserves records.

## Ownership

The coordinator creates or resumes a record for each accepted change, including acceptance supplied with an invocation. Before implementation, capture the decision source, applicability, expected behavior and outcome, and observation criteria using the record format below. Keep deferred changes accepted until implementation is evidenced. Unaccepted ideas remain in their source reports.

After implementation, update the same record with the effective date, changed paths, version evidence, and validation result. An authorized implementation can supply this evidence later. Report the journal location, record IDs, and any failed or deferred writes. Recording is complete when every accepted change has a saved record or an explicit recording gap, and every applied change has implementation evidence. Implementation alone does not establish an effect.

The coordinator appends reconciled observations from subsequent independent work and updates the assessment, using worker results or its own direct analysis. Reading a record grants no authority to apply, revert, or broaden its change. It also grants no authority to invoke another skill or start a scheduled task.

Keep the accepted decision and original expectation intact. Add dated corrections with their sources. A material change to the mechanism or applicability gets a new accepted record linked through `Supersedes`. A revised assessment alone stays in the same record. Preserve withdrawn and superseded records.

## Identity and safe updates

Before creating a record, search existing records by decision reference, target files, and change description. Reuse the record for the same accepted change across chats. When identity is uncertain, report the uncertainty instead of merging unrelated changes. Use a date plus a UUID for new filenames and IDs, such as `<YYYY-MM-DD>-<uuid>.md`. Dates describe the actual decision and implementation; record unknown dates as `Unknown`.

Serialize writes using atomic creation of a `.write-lock` directory inside the journal. Only the process that created the lock owns it. Record its operation reference inside it. If another writer owns the lock, defer the write and report it; leave an unfamiliar lock intact. After acquiring the lock, reread the affected record and repeat the duplicate check. Write the full updated record to a temporary file in the same directory, then replace its destination atomically. Read the saved record back and release only the lock this operation created. Preserve unrelated records and previous observations.

Give observations stable IDs based on evaluator reference, change ID, and observation cutoff. Repeating an evaluation updates the same observation. Later evaluations may cite earlier incidents, but count each independent incident once in cumulative exposure.

## Event time and version

Record the effective implementation time with its timezone and precision when available. Preserve date-only evidence as date-only; keep unknown times unknown. Approval time, a commit timestamp, and a file's modification time do not by themselves prove when a change became effective for an observed agent.

Observations identify the relevant event time, the version available under the runtime's loading rules, and the evidence for that availability. Record whether the agent actually loaded or followed it separately. Classify comparison evidence as before, after, mixed, or unknown. Keep ambiguous ordering and mixed exposure separate from clean comparisons. A chat's creation or last-update time only locates evidence; it does not determine the comparison group.

Preserve the originating incident ID. Implementation, retry, review, or recovery of that incident cannot become independent validation of its own remedy. Recorded observations from subsequent independent work can accumulate across retrospectives without recounting the same incident.

## Record

Use the following sections. Record missing evidence as `Unknown` with the reason. A proposed observation criterion is the recorder's expectation, not a new user requirement.

```markdown
# <change ID>: <short title>

- Journal format: 1
- Change ID: <date-UUID>
- Change state: accepted | implemented | withdrawn | superseded
- Evaluation state: pending | insufficient-evidence | supported | unsupported | harmful
- Accepted at: <timestamp with timezone, date-only evidence, or Unknown>
- Decision source: <chat, review, or delivery reference>
- Implemented at: <effective timestamp with timezone, date-only evidence, or Unknown>
- Supersedes: <change ID or None>

## Decision

- Problem and consequence: <observed event and its source>
- Basis: <observed failure, user preference, or inspected condition>
- Accepted change: <mechanism and owning files or checks>
- Applicability: <projects, task conditions, and limits>

## Expected effect

- Behavior: <what the agent should do differently>
- Outcome: <quality or recurrence result that would justify the change>
- Baseline: <known independent incidents and applicable denominator, or Unknown>
- Observation plan: <eligible opportunities, observation window or exposure target>
- Success criterion: <observable support for the expected outcome>
- Reconsideration criterion: <ineffectiveness, added work, or harm worth reviewing>

## Implementation

- Evidence: <changed paths, effective date, commit or content digest>
- Validation: <checks of the implementation, separate from later effect>
- History: <dated implementation updates or decision corrections with sources>

## Observations

<Dated entries with stable IDs, evaluator references, observation cutoffs,
independent incident references, event times and their precision, version
availability, applicable exposure, behavior and outcomes, costs, comparison
conditions, competing explanations, and coverage gaps.>

## Assessment

- As of: <observation cutoff or Not evaluated>
- Evidence: <observation IDs and deduplicated exposure>
- Conclusion: <supported, unsupported, harmful, or insufficient evidence, and why>
- Next observation: <remaining evidence needed, or None>
```

`accepted` records a decision; `implemented` requires evidence that the intended change is effective. For uncommitted files, record a content digest and describe them as local edits. A successful edit or passing test does not establish a beneficial effect.

## Evaluation

Start evaluation at `pending`. Use `insufficient-evidence` when suitable later work, access, or comparable evidence is missing. Zero applicable opportunities never proves success. One new case can add evidence or reveal harm without establishing general benefit. Use `supported` or `unsupported` only when the recorded criterion and evidence justify that conclusion. Use `harmful` for evidenced adverse effects. Scope every conclusion to the observed conditions and record competing explanations. These states describe evidence, not permission to keep or remove a rule.

The assessment reflects accumulated comparable observations. A new window with no applicable opportunities adds no evidence; keep any earlier supported conclusion at its original scope and cutoff. Mark the new observation's evidence gap without treating it as proof against earlier observations.

Separate the opportunity for a problem, whether it occurred, whether the agent loaded the instruction or ran the check, whether behavior changed, and the outcome. Compare quality and recurrence as well as extra work. Fewer tool calls alone do not establish better quality. An explicit user preference remains authoritative; evaluate how well the implementation follows it, rather than whether to retain the preference.
