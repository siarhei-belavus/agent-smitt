# Delivery records

Read the [implementation contract](IMPLEMENTATION-CONTRACT.md) for repository deliveries, worktrees, references, authority inputs, settled seams, validation obligations, and writable scope. These records apply to every delivery assignment.

## Repository Store

A Repository Store is the validated Git checkout selected by Repository Resolution to supply Git storage without becoming a delivery workspace. Delivery preparation may fetch and register its own worktree while preserving the Store's checked-out branch, index, files, remotes, hooks, and configuration.

## Authority evidence

Before recording or reusing review evidence, read [Authority evidence](AUTHORITY-EVIDENCE.md).
