---
name: mechanical-modeling-doc
description: mechanical modeling documentation workflow for uploaded cad files, images, drawings, calculation reports, design manuals, markdown, pdf, docx, spreadsheets, or mixed project materials. use when the user wants modeling overview, solidworks or cad modeling guidance, feasibility or interference checks, part lists, dimensions, assembly mates, motion simulation notes, or a complete modeling manual generated from source materials.
---

# Mechanical Modeling Documentation

## Purpose

Use this skill to turn mechanical project materials into clear modeling documentation. It supports mixed inputs such as CAD files, screenshots, engineering drawings, design manuals, calculation reports, images, PDFs, DOCX files, spreadsheets, and previously drafted notes.

Primary outputs:
1. 建模概述：设备对象、建模目标、主要输入资料、关键参数。
2. 建模可行性与冲突检查：尺寸矛盾、装配干涉、缺失定位尺寸、运动约束风险。
3. 完整建模说明书：零件清单、零件尺寸规格、功能位置、建模方法、装配配合、运动仿真、干涉检查、数据来源与计算依据。

## Standard Workflow

Follow this sequence unless the user asks for only one section.

1. Inventory the inputs.
   - Identify each uploaded file type: CAD, image, drawing, PDF, DOCX, spreadsheet, markdown, or text.
   - For work-related internal docs or user-uploaded files, use file search or the relevant document-reading tool when available.
   - For images and drawings, inspect visually and extract visible dimensions, labels, part relationships, and geometry.
   - For CAD files, inspect metadata and simple geometry when possible. Use `scripts/analyze_inputs.py` via the container for file metadata, image sizes, simple STL/OBJ bounds, STEP entity counts, DOCX text preview, and text/markdown previews.

2. Extract source data.
   - Separate explicit source dimensions from inferred or modeling-supplement dimensions.
   - Track the source for every important dimension.
   - Preserve formulas and calculation logic when the source material contains them.
   - If formulas are missing or ambiguous, state that the value is a modeling supplement, not a source value.

3. Build the modeling overview.
   - State the design object, modeling scope, expected CAD platform, simplified vs detailed modeling boundary, and core motion chain.
   - Mention what the final assembly must demonstrate.

4. Run feasibility and conflict checks.
   - Check geometry consistency, assembly clearance, motion range, shaft/hole compatibility, center distances, belt/chain alignment, and likely over-defined mates.
   - Distinguish three statuses: usable directly, usable after adjustment, and missing/needs supplement.
   - Never claim manufacturing-level feasibility unless manufacturing drawings, tolerances, and standards are available.

5. Generate the complete modeling document.
   - Use the structure in `references/document_outline.md`.
   - Use the templates in `references/output_templates.md` for tables and section language.
   - Include a final “数据来源与计算依据” section that identifies which data came from source documents, formulas, CAD/drawing inspection, or modeling supplements.

6. Produce deliverables.
   - If the user asks for a Markdown file, create a `.md` document and provide a sandbox download link.
   - If the user asks for Word/PDF, follow the relevant docx/pdf skill instructions.
   - In chat summaries, keep the result concise and link the generated artifact.

## Input Handling Rules

Consult `references/input_file_handling.md` when files are mixed or ambiguous.

Key rules:
- Treat uploaded source materials as the authority for project-specific values.
- Do not invent exact dimensions when drawings or calculations do not provide them. Use clearly labeled modeling supplements.
- For CAD files, distinguish between exact geometry extracted from the file and approximate values inferred from metadata or screenshots.
- For images, identify dimensions only when visually readable or when the user provides scale.
- For formulas, restate variables and substitutions so the user can verify where dimensions came from.
- If a file cannot be parsed, still use filename, extension, visible context, and any user-provided descriptions; be transparent about the limitation.

## Output Style

Use Chinese by default when the user asks in Chinese. Be direct, practical, and oriented toward the person who will build the CAD model.

Formatting requirements:
- Use clear numbered headings.
- Use tables for dimensions, part lists, mates, and checks.
- Mark each dimension type as one of: `原文`, `公式计算`, `CAD/图纸读取`, `图片识别`, `建模补充`, or `待确认`.
- Use “注意” paragraphs for collision-prone or over-constraint-prone points.
- End complete manuals with a source-and-calculation section.

## Quality Checklist

Before finalizing, verify that the document includes:
- overall technical parameters;
- coordinate and assembly direction rules;
- complete part list;
- each major part’s function, dimensions, material, position, and modeling method;
- assembly mates and allowed degrees of freedom;
- motion simulation setup when relevant;
- interference and conflict checklist;
- source data and calculation basis;
- a clear statement of which dimensions are directly sourced and which are modeling supplements.
