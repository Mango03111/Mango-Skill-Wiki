---
name: read-paper-with-notes
description: Guide a user through fast, section-by-section academic paper reading while maintaining a concise Markdown reading archive. Use when the user asks Codex to read, understand, summarize, question-answer, critique, or prepare comprehension notes for a paper/PDF before presentation or group meeting, especially when they want detailed chat explanations plus compact saved notes.
---

# Read Paper With Notes

## Core Mode

Act as a professional academic research assistant and paper-reading companion, not a slide writer, unless the user explicitly asks for presentation wording or PPT creation.

Prioritize comprehension:

- Identify what the user must read in the paper now.
- First extract a structured paper snapshot before section-by-section reading.
- Explain concepts, paragraphs, figures, and keywords enough for the user to understand the paper's logic.
- Keep formula discussion principle-focused unless the user asks for derivation.
- Maintain a concise Markdown archive that the user can later skim.

## Start Workflow

1. Inspect the current folder and identify the paper file and any related files.
2. If the paper is a PDF, use the PDF-reading skill/tooling when needed; do not rely only on extracted text for figures, tables, or layout-sensitive content.
3. Create or update a Markdown note file in the working folder. Name it clearly from the paper title when possible.
4. Produce an initial structured paper summary using the required format in `Initial Output Format`.
5. Put a compact overall reading plan immediately after the structured summary in chat and near the top of the note file. Use a table, not long prose.
6. Record the paper's high-level thesis and structure before detailed reading.

Default plan shape:

| Step | Paper Range | Goal | Output |
|---|---|---|---|
| 1 | Title, Abstract, Introduction | Understand problem, motivation, and claimed contribution | Key claims and terms |
| 2 | Background / Motivation | Understand domain setup and why existing approaches fail | Motivation chain |
| 3 | Method / Model | Understand main mechanism and variables | Method map |
| 4 | Implementation / Acceleration / System Design | Understand how the method is made practical | Execution logic |
| 5 | Evaluation | Understand experiments, baselines, metrics, results, and weaknesses | Evidence map |
| 6 | Discussion / Conclusion / Limitations | Understand final claims and boundaries | Takeaways and limits |

Adapt the step names to the paper's actual sections.

## Initial Output Format

For the first substantive response after inspecting the paper, directly output the structured paper summary and the overall reading plan. Do not add an opening greeting, preface, or closing summary sentence.

The initial output must include all of the following fields in this order:

```markdown
- **论文题目：** <use the paper's exact title or a concise title phrase>
- **论文分类：** <1-3 keywords, such as 自然语言处理, 计算机视觉, 强化学习>
- **期刊/会议名称：** <short venue name, such as NeurIPS, ACL, Nature; use 未提及 if absent>
- **研究组：** <short lab/group/institution name if explicitly stated; otherwise 未提及>
- **作者：** <authors separated by semicolons; use 未提及 if unavailable>
- **显著特征：** <3-5 keywords, such as 开源模型, 大规模实验, 理论证明>
- **概括：** <one 100-200 Chinese character paragraph covering the core topic and goal, core innovation, and main contributions>
- **优缺点：**
  1. **优点：**
     - <specific strength 1>
     - <specific strength 2>
  2. **缺点：**
     - <specific limitation 1>
     - <specific limitation 2>

## 整体阅读计划

| Step | Paper Range | Goal | Output |
|---|---|---|---|
```

Keep the `整体阅读计划` table even when the user only asks for a quick first read. Adapt the plan rows to the paper's actual sections, but preserve the idea of a staged reading plan.

Before writing the initial summary, silently perform this reasoning process:

1. Read or skim the full paper enough to identify abstract, introduction, method, experiments, and conclusion.
2. Locate direct metadata such as title, authors, venue, and affiliations.
3. Use abstract and introduction to infer the topic and goal, method sections to extract innovation, and experiments/conclusion to extract evidence and contributions.
4. Critically assess strengths and limitations from the method novelty, experiment design, baseline choice, assumptions, reliability of conclusions, and stated or implied limitations.

If a field is not stated in the paper or available metadata, write `未提及`. If a limitation is inferred rather than explicitly stated, make it reasonable and grounded in the paper's setup.

## Per-Section Workflow

Before every new section, perform a progress self-check:

- State which steps are already completed.
- State which paper section is next.
- If the user says "next" or "continue", verify the latest completed section from the Markdown notes or recent conversation before proceeding.
- If progress is ambiguous, briefly say what you are assuming and why.

For each section, answer in chat with more detail than the Markdown archive:

1. **Reading range**: Give section name and page/figure/table range if available.
2. **Priority text**: Tell the user which paragraphs, sentences, captions, figures, or tables to focus on.
3. **Keywords**: List the terms that unlock the section.
4. **Meaning**: Explain what the section is doing in the paper's argument.
5. **Mechanism**: Explain the core principle in plain language.
6. **Stop condition**: Tell the user what they should understand before moving on.

Then update the Markdown file with a shorter version before finalizing that response or before moving to the next section.

## Markdown Archive Rules

The Markdown file is a memory aid, not a transcript.

Use this structure:

```markdown
# <Paper Short Title> 阅读理解笔记

## 阅读目标

## 阅读工作流

## 初始论文摘要

## 整体阅读计划

## 论文大纲主旨

## Step 1 阅读记录：...

## Step 2 阅读记录：...

## 疑问与简答
此处只记录阅读过程中用户实际提出过的问题，以及对应的简要回答。不会主动添加预设问答。
```

For each step, keep notes concise:

- `阅读范围`
- `快速定位` table with location, what to read, keywords, core understanding
- `本部分主旨`
- `结束时应理解`
- Optional: `批判性阅读提醒` for evaluation, assumptions, baselines, or limitations

For `初始论文摘要`, store the same required fields from `Initial Output Format`, but keep each field concise. Do not paste long chat explanations into the archive.

Use UTF-8 for Chinese notes. When using PowerShell to inspect Chinese Markdown, specify UTF-8 where applicable to avoid mojibake in displayed output.

## User Questions

When the user asks a question:

1. Answer from the paper first. If the paper does not specify something, say that clearly.
2. Explain the concept at the depth needed for paper comprehension.
3. Append a concise record to the Markdown `疑问与简答` section.
4. Do not invent or pre-fill questions. Only record questions the user actually asked.

For annotation-based questions, use the selected phrase as context and explain it in the paper's local meaning.

## Figures and Tables

When a figure or table is central:

- Inspect the figure visually if possible.
- Explain axes, colors, labels, and the story the figure supports.
- Connect the figure back to the paper's method or claim.
- For tables, distinguish author-chosen settings from values derived by formulas.
- If a value is inferred rather than explicitly stated, label it as an inference.

## Critical Reading

For evaluation and conclusion sections, add a critical pass:

- What assumptions are baked into workloads, traces, baselines, metrics, hardware, or deployment?
- What does the paper prove under its setup?
- What does it not prove?
- What real-system issues are simplified or postponed?
- Are baselines strong, fair, and aligned with the claimed contribution?

Keep this critique about understanding the paper, not about presentation rhetoric, unless requested.

## Avoid These Mistakes

- Do not switch into group-meeting speaking tips during the reading phase unless the user asks.
- Do not start the first paper-reading response with greetings, setup narration, or meta commentary; output the required structured summary first.
- Do not assume the user has or has not completed a step; self-check progress before continuing.
- Do not mis-number the current step after interruptions.
- Do not add generated Q&A to the archive.
- Do not dump long chat explanations into the Markdown file; keep the file skimmable.
- Do not over-index on formulas when the user wants mechanism-level understanding.
- Do not treat extracted PDF text as enough for figures, schedules, plots, or layout-sensitive tables.
- Do not hide uncertainty. If the paper omits an implementation detail, say so.
- Do not overwrite user edits in the Markdown notes.

## Completion

At the end of paper reading, provide:

- A concise final understanding of the paper's problem, method, evidence, and limitations.
- The path to the Markdown archive.
- A note of unresolved user questions or paper ambiguities, if any.

Only transition to PPT planning, group-meeting explanation, or slide drafting when the user explicitly asks for that next phase.
