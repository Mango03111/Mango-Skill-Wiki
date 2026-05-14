# Input File Handling Guide

Use this guide when the task includes mixed engineering materials such as CAD, images, drawings, PDFs, DOCX files, spreadsheets, or Markdown notes.

## 1. Source Priority

Use this priority order when values disagree:

1. Explicit dimensions in drawings or CAD geometry.
2. Explicit dimensions in source calculation manuals or design reports.
3. Values derived by formula from source values.
4. Values visible in images, when scale or labels are readable.
5. Modeling supplements added only to make CAD assembly possible.
6. Engineering assumptions, only when clearly labeled and necessary.

## 2. Documents

For DOCX/PDF/Markdown/TXT materials:

- Extract core technical parameters, design requirements, part dimensions, formulas, and materials.
- Preserve formulas and substitutions when they justify a modeling dimension.
- Watch for OCR or formula-object extraction gaps. If formulas appear blank in text, inspect the original document or use document-specific tools when available.
- Quote or cite source files when the environment supports citations.

## 3. CAD Files

Common extensions: `.step`, `.stp`, `.iges`, `.igs`, `.stl`, `.obj`, `.sldprt`, `.sldasm`, `.dwg`, `.dxf`.

Recommended handling:

- Use direct CAD-aware tooling if available.
- Otherwise run `scripts/analyze_inputs.py` for metadata and simple geometry inspection.
- For STL/OBJ mesh files, use bounding boxes as approximate geometry references unless the mesh has known units.
- For STEP/STP files, extract header, entity counts, and any readable product names. Do not assume complete dimensions without a CAD parser.
- For SolidWorks native files (`.sldprt`, `.sldasm`), if the environment cannot parse them, report that only metadata is available and ask for STEP/STL exports when precise geometry is needed.
- For DWG/DXF drawings, extract text labels and visible dimensions when possible. If native parsing is unavailable, ask for PDF screenshots or DXF export.

## 4. Images and Drawings

For screenshots, photos, scanned drawings, and diagrams:

- Use visual inspection first.
- Extract visible labels, dimension callouts, axis directions, part names, and spatial relationships.
- Do not measure exact dimensions from pixels unless a scale is provided.
- If a drawing includes a title block, note drawing name, scale, material, and revision if readable.
- Identify likely parts and motion links, but label uncertain findings as inferred.

## 5. Spreadsheets

For spreadsheets:

- Use spreadsheet tools when the user asks to analyze or generate spreadsheet artifacts.
- Extract parameter tables, bill of materials, formulas, and named ranges when relevant.
- Avoid editing source spreadsheets unless explicitly asked.

## 6. Missing Data Handling

When a model cannot be built directly from source materials, classify missing data:

- `必须补充`: impossible to assemble or define motion without it.
- `建议补充`: needed for cleaner or more realistic modeling.
- `可简化`: can be omitted or approximated for teaching/展示用途.

Always provide reasonable modeling supplement values when the user needs a practical CAD model and exact manufacturing precision is not required.
