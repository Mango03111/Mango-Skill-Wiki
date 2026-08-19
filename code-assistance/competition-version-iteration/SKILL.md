---
name: competition-version-iteration
description: Safely maintain Git project version history. Use when Codex needs to initialize a project's release branch, publish a new version with a commit and annotated Git tag, or add user-supplied post-release results to the version record without changing a tag.
---

# Version Iteration

Manage a small, durable version record for one Git project. Keep the workflow minimal: initialize once, then either publish a version or record a result.

## Initialize once

On the first request for a project, ask for only:

1. Project directory.
2. Formal release branch.
3. Remote name, if it is not `origin`.

Use `README.md` as the record file unless the user specifies another tracked Markdown file. Confirm that the directory is a Git repository and that its current branch is the release branch. Save the choices in `.codex/version-iteration.json` in the project:

```json
{
  "branch": "dev",
  "remote": "origin",
  "record_file": "README.md"
}
```

If the configuration is absent, invalid, or the user asks to change it, ask again. Do not guess a release branch or rewrite the configuration silently.

## Common rules

- Treat `发布新版本` (or an equally explicit instruction to publish a version) as the only authorization to commit, tag, and push source changes.
- Treat user-supplied post-release results as authorization only for a record-only commit. Never create, move, or delete a tag for that action.
- Before a write, inspect the repository root, configured remote URL, current branch, upstream divergence, status, index, conflicts, relevant tags, and complete diff.
- Stop and report rather than force-push, amend, rebase, switch branches with a dirty worktree, resolve conflicts automatically, or rewrite published history.
- Do not run project tests or submit to external systems unless the user separately asks. A publish instruction confirms that any required release tests are acceptable to the user.
- Report the version, full commit SHA, tag (if any), included files, and push result after every successful write.

## Publish a new version

Require an explicit publish instruction. Before committing, ensure all of the following:

- The current branch equals the configured release branch and tracks the configured remote branch.
- No unresolved conflicts, staged changes, or remote divergence exist.
- The requested version tag does not already exist locally or remotely.
- The record file exists and its planned change is consistent with existing version tags and history.

Use an explicitly named version if the user supplies one. Otherwise, derive the next version from tags matching `v<major>.<minor>`: keep the highest major and increment its minor. If no matching tag exists, ask the user to name the first version.

Maintain a concise section near the top of the record file:

```markdown
## Version History

| Version | Date | Summary | Status |
| --- | --- | --- | --- |
| `v1.2` | YYYY-MM-DD | User-provided summary | Published |
```

Add the new row first. Review the complete change set with the user-visible summary, then stage all non-ignored repository changes with `git add -A`. Create one commit with this shape:

```text
[v1.2] <type>: <summary>

Version: v1.2
Previous-Version: v1.1
Summary: <summary>
Release-Test: user-confirmed
```

Create an annotated tag named exactly after the version. Push the release branch and tag atomically when the remote supports it; otherwise stop and explain before performing separate pushes.

## Record post-release results

Require an exact published version and the user-supplied result text. Verify its tag exists, the index is empty, the release branch is current, and the complete record-file diff contains only this result update. Keep unspecified values absent rather than inferring them.

Add the result in the existing version row or in a short adjacent subsection, preserving the user's wording and units. Stage only the record file, commit with:

```text
[records] docs: record v1.2 results

Version: v1.2
Source-Tag: v1.2
Data-Source: user-supplied
```

Push only the configured release branch. Do not stage source changes or create a tag.

## Fixes and rollbacks

Keep every published commit and tag unchanged. Implement a fix or rollback as ordinary local changes, then publish it later under a new, incremented version after another explicit publish instruction.
