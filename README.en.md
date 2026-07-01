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

## Included Skills

### mechanical-modeling-doc

Location: [`structural-design/mechanical-modeling-doc`](./structural-design/mechanical-modeling-doc/)

This Skill helps generate structured SolidWorks / CAD modeling manuals from mechanical design documents, CAD drawings, images, engineering screenshots, PDFs, DOCX files, and other project materials. It can produce modeling overviews, feasibility assessments, dimension conflict checks, assembly interference checks, part lists, part specifications, functional positions, assembly mates, motion simulation settings, and complete Markdown modeling documentation.

### vllm-ascend-contribution

Location: [`Code Assistance/vllm-ascend-contribution`](./Code%20Assistance/vllm-ascend-contribution/)

This Skill guides AI agents through the `vllm-project/vllm-ascend` contribution workflow. It covers change-scope triage, local lint/CI/test selection, DCO `Signed-off-by` commits, PR title and body conventions, documentation changes, multi-node test configuration, and E2E/nightly hardware CI trigger comments.

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

## Discussion and Improvements

Feedback, improvement ideas, new Skill suggestions, Issues, Discussions, and Pull Requests are welcome.

If a Skill is useful to you, feel free to adapt it into a version that better matches your own workflow.
