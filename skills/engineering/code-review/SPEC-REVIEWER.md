# Spec reviewer

Read the [reviewer contract](REVIEWER-CONTRACT.md). Review the complete selected target set together with its diffs, accepted Authority inputs, authoritative sources, settled seams, and repository and cross-repository validation evidence. Cover every applicable requirement and accepted decision across linked sources.

Report missing or partial requirements, scope creep, incorrect behavior, unauthorized seam changes, acceptance behavior outside a settled seam, and required behavior not verified through that seam. Route each finding to the affected Repository IDs. Label a finding **Blocking** when it demonstrates a requirement or settled-decision violation or a reachable correctness regression; label other material findings **Advisory**.

For removed or weakened behavior, verify which existing invariant it protected and why the change is justified. An accepted task decision or demonstrated implementation error is sufficient. Unresolved purpose or conflicts are **Blocking**.
