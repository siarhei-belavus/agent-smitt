---
name: code-review
description: Review fixed Repository Targets. Use when the user asks to review a branch, PR, committed delivery, or worktree; asks for a multi-repository Delivery Bundle review; or asks for Standards-only or Spec-only review.
---

Review committed or worktree changes since fixed points without modifying the reviewed repositories or external collaboration state.

Read [implementation contract](references/bundled/federated-workflow/IMPLEMENTATION-CONTRACT.md) before resolving targets or review authority. For Work Tracker-backed authority, follow [Context Pack consumption](references/bundled/federated-workflow/CONTEXT-PACK.md).

## Public input

A Fixed point is the caller-selected revision used to anchor review bounds. A Repository Target is one repository's immutable review input, pinned to a Fixed point and exact Review head or WIP snapshot.

Accept one or more fixed Repository Targets. A single repository is the one-element case. Each target records:

- **Repository ID**;
- repository or worktree path;
- **Fixed point**;
- **Review head** as an exact commit SHA;
- **Authoritative sources**;
- an **Authority input** value for the authority under review, an accepted Context Pack file path when Work Tracker-backed;
- **Settled seams** and test approaches relevant to that target;
- repository validation evidence bound to the Review head for a committed target or bound to both the Review head and Worktree snapshot ID for WIP, when supplied.
- for explicit WIP review, a **Worktree snapshot ID** that identifies the captured uncommitted content.

For Work Tracker-backed authority, Authority input is the accepted Context Pack entry path for the authority under review. The entry identifies its profile, permanent root, `Complete` result, and full source payloads. Acquire or reuse it through the consumption contract and pass the entry and linked files to every selected reviewer. Reviewers apply its mandatory reading rules and read the sources required by their axis without invoking Context Assembly or querying the provider. Spec coverage includes every applicable requirement and accepted decision across the linked sources. Record the portable Authority evidence binding with the review result.

For authority that is not Work Tracker-backed, Authority input contains the supplied local specification, current user direction, or other non-provider authority. It has no invented Context Pack, profile, or result.

For the existing single-repository form, the user may supply only a fixed point; use the current repository and resolve the current `HEAD` as the exact Review head. When the single-repository worktree is dirty and the user did not select committed or WIP review, disclose the dirty state and ask whether those changes are in scope. Preserve explicit worktree/WIP review by identifying it with both the current exact `HEAD` and an immutable Git tree snapshot of the tracked, staged, and untracked content.

Select one review mode:

- **Standards only**;
- **Spec only**;
- **Both (the standalone default)**.

Do not silently add an unselected axis.

**Complete when:** every target has one Authority input accepted through its applicable authority gate and the selected axes are explicit.

## Process

### 1. Pin every target

Resolve every Fixed point and Review head once in its target repository. Compute `git merge-base <fixed-point> <review-head>` once and record the returned commit SHA as the exact **Comparison base** for that target. For committed review, use `<fixed-point>...<review-head>` and record `git log <comparison-base>..<review-head> --oneline`. Do not recompute the Comparison base from moving refs during freshness checks.

For explicit worktree review, follow [WIP review capture](WIP-REVIEW.md) before dispatch and again before reporting. Supply its immutable diff and snapshot identity to reviewers.

Confirm each target resolves and has a non-empty selected change set before starting reviewers. A bad ref or empty target fails here. Do not substitute a branch tip or later `HEAD` for the captured Review head.

Apply the complete Evidence freshness rule below before starting reviewers and again before reporting results.

### 2. Identify authoritative sources and seams

Use the Authority input and sources supplied with the Repository Targets first. Otherwise find non-Work-Tracker authority in this order:

1. a local specification or resolved decision path supplied by the user;
2. a matching file under `docs/`, `specs/`, or `.scratch/`;
3. ask the user only when the selected Spec axis has no authoritative source.

An issue reference found in a commit message is a provenance clue only and does not trigger provider lookup. Use an accepted Context Pack as the authoritative Work Tracker source set without replacing it with individual ticket reads, summaries, or newly discovered provider sources.

Start with supplied seam records, then validate every seam against current authoritative sources. Explicit current user direction, specifications, and resolved decisions take precedence over earlier sources and existing public interfaces. Record source conflicts as Spec findings. When no authoritative source settles a seam, mark it unsettled and assess its shape using the `codebase-design` baseline rather than choosing a design during review.

**Complete when:** every target still uses its accepted Authority input, every non-Work-Tracker target has the best available authority, and every seam is settled, explicitly conflicting, or marked unsettled.

### 3. Build repository-local Standards baselines

For each selected Standards target, discover and read its applicable repository instructions and documented standards. Include `CODING_STANDARDS.md` and relevant sections of `CONTRIBUTING.md` when present, together with directory-specific standards and linked rules governing the changed paths. Existing standards may live elsewhere; use the repository's navigation to find their authoritative home.

Record each source's path, applicability, and immutable revision or content fingerprint with the Authority evidence. Use accepted source versions from the supplied authority, falling back to the captured Comparison base for repository files. Changes to standards in the reviewed diff are proposals until authoritative input accepts them as governing this review. Pass the source list and exact contents or readable immutable references to the Standards Reviewer. A missing optional standards file leaves the other applicable sources and baseline in force; an unavailable required source leaves coverage incomplete.

When preparing Standards inputs, use the smell baseline in [Standards reviewer](STANDARDS-REVIEWER.md).
Determine per target whether the change introduces or reshapes a module, interface, seam, adapter, logical ownership, physical decomposition, or contract, or changes current-truth documentation. When it does, require the Standards Reviewer to read the `codebase-design` skill in full and apply its relevant deletion-test, proportional-design, and final-state rules.

Route requirement or settled-decision violations to Spec. Route structural and change-pressure findings to Standards.

Done when each selected Standards target has an attributable source set, applicable rules, and design trigger result ready for its reviewer.

### 4. Run the selected fresh reviews

Start each reviewer, including every repeat review, with a fresh context without the parent conversation. Supply its role file and readable source references, rather than the preparation and aggregation instructions in this skill.

For the Standards axis, start one fresh Standards Reviewer per selected Repository Target using [Standards reviewer](STANDARDS-REVIEWER.md). Supply only its captured target, commit list, repository-local standards, design trigger result, authoritative seam context, accepted Authority input, and validation claims.

For the Spec axis, start one fresh Bundle Spec Reviewer over the complete selected target set using [Spec reviewer](SPEC-REVIEWER.md). Supply all captured targets and diffs, accepted Authority inputs, authoritative sources, settled seams, and repository and cross-repository validation evidence.

Pass Work Tracker Authority inputs unchanged and allow no provider lookup. For WIP targets, include the snapshot ID and immutable materialized diff with its digest. The role files own the full-pass, coverage, finding, and severity requirements.

Run fresh reviewers concurrently where harness capacity permits; freshness and complete inputs matter, not a particular internal agent topology. If the selected Spec axis has no source after the user confirms none exists, skip that reviewer and report `no spec available`.

**Complete when:** every reviewer has returned one full-pass result whose Coverage receipt accounts for every changed file, applicable axis input, Settled Seam, named provider and consumer, and supplied validation claim.

### 5. Aggregate without merging axes

For each selected axis only, emit its result and counts. When Standards is selected, report it separately for every repository, using one section per target:

`## Standards — <Repository ID>`

When Spec is selected, report the whole-bundle result once:

`## Spec — selected targets`

Omit the unselected axis entirely. When both are selected, do not merge, reclassify, or rerank the axes. Include the Coverage receipt with each result. End with Blocking and Advisory counts and the highest-severity finding within each selected result when present.

Publish no branch, create or update no Review Proposal, and change no Work Tracker state. Report findings and evidence only.

## Evidence freshness

The calling workflow owns freshness checks before dispatch and before reporting. For mechanical dependency comparisons, use the optional [delivery validator](references/bundled/federated-workflow/MECHANICAL-VALIDATION.md) or the existing manual checks. Reviewers retain the full semantic coverage of their selected axis.

Every finding and pass result is bound to the captured exact Review heads, review bounds, [Authority evidence](references/bundled/federated-workflow/AUTHORITY-EVIDENCE.md), and, for WIP, the Worktree snapshot ID. Changed heads or snapshots invalidate affected repository validation and reviews. Changed review bounds or governing authority invalidate dependent reviews; changed obligation meaning also invalidates its validation. A relocated or reacquired pack with proven equivalent authority preserves results. Missing proof requires refreshed affected evidence and a new fixed target rather than an assumed pass.
