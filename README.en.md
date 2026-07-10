# Mango Skill Wiki

## Overview

This repository is used to store and share useful ChatGPT Skills that I create and refine through real production practice, study, and project work. Each Skill represents a reusable workflow for a specific task, especially tasks that are repetitive, multi-step, detail-heavy, or easy to standardize.

My goal is to gradually organize practical Skills that have proven useful in real projects, so they can be reused, shared, discussed, and improved by others. Contributions, suggestions, and discussions are welcome.

## Purpose

This repository is intended to:

- collect practical Skills created from real production and project experience;
- document each Skill's use cases, expected inputs, and output formats;
- share reusable workflows, document templates, and analysis conventions;
- make it easier for others to download, learn from, modify, and extend these Skills;
- serve as a personal Skill knowledge base and case library.

## Current Categories

| Category | Folder | Description |
|---|---|---|
| Structural Design | [`structural-design`](./structural-design/) | Skills for mechanical structure design, CAD/SolidWorks modeling manuals, assembly analysis, and dimension conflict checks |
| Code Assistance | [`Code Assistance`](./Code%20Assistance/) | Skills for open-source contribution, code review, commit conventions, PR workflows, CI triggers, and engineering collaboration |
| Research | [`Research`](./Research/) | Skills for academic paper reading, research workflows, structured notes, real Q&A records, and Skill knowledge-base maintenance |

## Included Skills

### mechanical-modeling-doc

Location: [`structural-design/mechanical-modeling-doc`](./structural-design/mechanical-modeling-doc/)

This Skill helps generate structured SolidWorks / CAD modeling manuals from mechanical design documents, CAD drawings, images, engineering screenshots, PDFs, DOCX files, and other project materials. It can produce modeling overviews, feasibility assessments, dimension conflict checks, assembly interference checks, part lists, part specifications, functional positions, assembly mates, motion simulation settings, and complete Markdown modeling documentation.

### vllm-ascend-contribution

Location: [`Code Assistance/vllm-ascend-contribution`](./Code%20Assistance/vllm-ascend-contribution/)

This Skill guides AI agents through the `vllm-project/vllm-ascend` contribution workflow. It covers change-scope triage, local lint/CI/test selection, DCO `Signed-off-by` commits, PR title and body conventions, documentation changes, multi-node test configuration, and E2E/nightly hardware CI trigger comments.

### read-paper-with-notes

Location: [`Research/read-paper-with-notes`](./Research/read-paper-with-notes/)

This Skill guides section-by-section academic paper reading while maintaining a concise Markdown reading archive. It focuses on understanding the paper's problem, method, evidence, and limitations before presentation work, explains key paragraphs, terms, figures, tables, and mechanisms, and records only the user's actual questions with brief answers.

### mango-skill-helper

Location: [`Research/mango-skill-helper`](./Research/mango-skill-helper/)

This Skill adds new ChatGPT Skills to Mango Skill Wiki in the repository's standard format. It requires the user to choose an existing category folder or request a new top-level category folder first, then organizes the source folder, `.skill.zip` package, category README, and root Chinese and English README entries.

## How to Use

1. Download the Skill folder or the `.skill.zip` file;
2. Upload and install it in a ChatGPT environment that supports Skills;
3. Upload the related project materials in a chat;
4. Invoke it with a prompt like:

```text
Use the mechanical-modeling-doc skill to organize these materials into a complete SolidWorks modeling manual.
```

```text
Use the vllm-ascend-contribution skill to prepare a compliant vllm-ascend commit and PR.
```

```text
Use the read-paper-with-notes skill to guide me through this paper section by section and maintain concise reading notes.
```

```text
Use the mango-skill-helper skill to add this skill to a chosen category and update the README files.
```

## Discussion and Improvements

Feedback, improvement ideas, new Skill suggestions, Issues, Discussions, and Pull Requests are welcome.

If a Skill is useful to you, feel free to adapt it into a version that better matches your own workflow.
