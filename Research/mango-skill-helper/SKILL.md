---
name: mango-skill-helper
description: Add Skills to the Mango Skill Wiki repository by placing source folders and .skill.zip packages into a user-selected category folder, creating or updating category README files, and synchronizing the root Chinese and English README indexes. Use when the user asks to add a skill package, organize a skill folder, or update this repository's skill catalog. The user must choose an existing top-level category folder or explicitly ask to create a new one before file edits begin.
---

# Mango Skill Helper

## Purpose

Use this skill when maintaining the Mango Skill Wiki repository itself, especially when the user asks to add a new ChatGPT Skill package and update the catalog documentation.

The goal is to reproduce the repository's established pattern:

```text
<category-folder>/
  README.md
  #skillPackage/
    <skill-name>.skill.zip
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    ...
```

Then synchronize:

- the category `README.md`;
- the root Chinese `README.md`;
- the root English `README.en.md`.

## Mandatory Category Rule

Before making file edits, the user must explicitly choose where the new skill should be stored.

Accepted target choices:

- an existing top-level category folder, such as `Research`, `Code Assistance`, or `structural-design`;
- a new top-level category folder to create.

If the user does not specify the target category folder, stop and ask them to choose one. Do not infer the folder from the skill topic, filename, or description.

Use a concise prompt such as:

```text
请先指定这个 skill 要放进哪个分类文件夹：使用现有文件夹，还是新建一个根目录分类文件夹？
```

If the user names a new folder, create that folder in the repository root and create its `README.md` in the same pattern as the existing category README files.

## Required Inputs

Collect or discover:

- the skill zip path or source folder path;
- the target category folder selected by the user;
- the skill name from `SKILL.md` frontmatter;
- the skill description from `SKILL.md` frontmatter;
- optional user wording for category name or README text.

If the zip contains multiple skill folders, ask which one to add unless the user clearly requested all of them.

## Standard Workflow

Follow this sequence.

1. Inspect the current repository.
   - Check `git status --short --branch`.
   - List root folders.
   - Read root `README.md`, root `README.en.md`, and the target category `README.md` if it exists.
   - Preserve unrelated user changes. Do not revert or overwrite existing work.

2. Inspect the incoming skill.
   - List the zip contents before extraction.
   - Verify that it contains a `SKILL.md`.
   - Read `SKILL.md` and `agents/openai.yaml` when present.
   - Extract the canonical skill name from frontmatter `name:`.

3. Place source and package files.
   - Ensure the target category folder exists.
   - Ensure `<category-folder>/#skillPackage/` exists.
   - Extract or copy the source folder to `<category-folder>/<skill-name>/`.
   - Copy or create the package at `<category-folder>/#skillPackage/<skill-name>.skill.zip`.
   - The `.skill.zip` should contain `<skill-name>/SKILL.md` and related files, not the whole category folder.

4. Create or update the category `README.md`.
   - Keep the same structure as existing category README files:
     - title;
     - one-paragraph category purpose;
     - `## Skills` table;
     - `## 使用方式`;
     - a short invocation example.
   - Add a row for the new skill:

```markdown
| [`<skill-name>`](./<skill-name>/) | <中文说明> | [`<skill-name>.skill.zip`](./%23skillPackage/<skill-name>.skill.zip) |
```

5. Update root `README.md`.
   - If the category is new, add it to `## 当前分类`.
   - Add a `### <skill-name>` section under `## 已收录 Skill`.
   - Include the location link and a concise Chinese explanation.
   - Add one Chinese invocation example under `## 使用方式`.

6. Update root `README.en.md`.
   - If the category is new, add it to `## Current Categories`.
   - Add a `### <skill-name>` section under `## Included Skills`.
   - Include the location link and a concise English explanation.
   - Add one English invocation example under `## How to Use`.

7. Validate.
   - Confirm the folder tree contains source, package, and README.
   - Run `tar -tf "<category-folder>/#skillPackage/<skill-name>.skill.zip"`.
   - If the source came from a zip, compare hashes between the original zip and copied `.skill.zip` when possible.
   - Read the changed README files with UTF-8.
   - Check `git diff --stat` and `git status --short`.

8. Report clearly.
   - List created files.
   - List updated README files.
   - State whether the copied package matches the original.
   - State whether changes are committed or only local. Do not commit, push, or create a release unless the user asks.

## README Writing Rules

Use Chinese by default in category README files and root `README.md`.

Use English in root `README.en.md`.

Keep descriptions short, practical, and matched to the skill's actual `SKILL.md` content. Do not overstate capabilities. Prefer describing the workflow rather than marketing it.

When linking folders with spaces in root README files, use URL-encoded paths such as:

```markdown
[`Code Assistance`](./Code%20Assistance/)
```

When linking `#skillPackage`, use `%23` to avoid broken Markdown anchors:

```markdown
[`<skill-name>.skill.zip`](./%23skillPackage/<skill-name>.skill.zip)
```

## Packaging Rules

If the user provides a `.zip` that already has the correct skill folder at its root, copy it directly and rename it to `<skill-name>.skill.zip`.

If the user provides a source folder, create the package so the zip root contains the skill folder:

```text
<skill-name>/SKILL.md
<skill-name>/agents/openai.yaml
...
```

Do not put `README.md`, root repository files, or category folders inside the skill package unless the skill source itself intentionally contains them.

## Safety Rules

- Never overwrite an existing skill folder or package with the same name without checking whether it is an update or a conflict.
- Never assume a category from topic alone. Ask for the folder if missing.
- Keep edits scoped to the new skill, its category README, and root README files.
- Preserve user edits and unrelated uncommitted changes.
- Do not create release notes, commits, pushes, or tags unless explicitly asked.
