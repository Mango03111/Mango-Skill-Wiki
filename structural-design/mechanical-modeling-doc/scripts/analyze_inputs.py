#!/usr/bin/env python3
"""Basic engineering input inspector for mechanical-modeling-doc.

This script intentionally performs lightweight, dependency-tolerant inspection.
It reports metadata and simple readable geometry hints for common project files.
It does not replace a full CAD kernel.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import struct
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def file_record(path: Path) -> Dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path),
        "name": path.name,
        "suffix": path.suffix.lower(),
        "size_bytes": stat.st_size,
    }


def image_info(path: Path) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "image"}
    try:
        from PIL import Image  # type: ignore
        with Image.open(path) as im:
            info.update({
                "width_px": im.width,
                "height_px": im.height,
                "mode": im.mode,
                "format": im.format,
            })
    except Exception as exc:
        info["warning"] = f"image metadata unavailable: {exc}"
    return info


def text_preview(path: Path, max_chars: int = 4000) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "text"}
    try:
        data = path.read_text(encoding="utf-8", errors="replace")
        info["line_count"] = data.count("\n") + 1
        info["preview"] = data[:max_chars]
    except Exception as exc:
        info["warning"] = f"text preview unavailable: {exc}"
    return info


def docx_preview(path: Path, max_chars: int = 4000) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "docx"}
    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
            info["zip_entries"] = len(names)
            xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
            # Very lightweight text extraction.
            text = re.sub(r"<[^>]+>", " ", xml)
            text = re.sub(r"\s+", " ", text).strip()
            info["text_preview"] = text[:max_chars]
            info["approx_text_chars"] = len(text)
    except Exception as exc:
        info["warning"] = f"docx preview unavailable: {exc}"
    return info


def step_info(path: Path, max_chars: int = 2500) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "step_or_iges"}
    try:
        data = path.read_text(encoding="utf-8", errors="replace")
        upper = data.upper()
        info["entity_count"] = len(re.findall(r"#[0-9]+\s*=", data))
        for key in ["FILE_DESCRIPTION", "FILE_NAME", "FILE_SCHEMA"]:
            m = re.search(key + r"\s*\((.*?)\);", data, flags=re.I | re.S)
            if m:
                info[key.lower()] = re.sub(r"\s+", " ", m.group(1)).strip()[:500]
        products = re.findall(r"PRODUCT\s*\((.*?)\);", data, flags=re.I | re.S)
        if products:
            info["product_records"] = [re.sub(r"\s+", " ", p).strip()[:300] for p in products[:10]]
        info["preview"] = data[:max_chars]
        if "CARTESIAN_POINT" in upper:
            info["has_cartesian_points"] = True
    except Exception as exc:
        info["warning"] = f"step/iges text inspection unavailable: {exc}"
    return info


def obj_bounds(path: Path) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "obj_mesh"}
    mins = [math.inf, math.inf, math.inf]
    maxs = [-math.inf, -math.inf, -math.inf]
    count = 0
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if line.startswith("v "):
                    parts = line.split()
                    if len(parts) >= 4:
                        vals = [float(parts[1]), float(parts[2]), float(parts[3])]
                        for i, v in enumerate(vals):
                            mins[i] = min(mins[i], v)
                            maxs[i] = max(maxs[i], v)
                        count += 1
        info["vertex_count"] = count
        if count:
            info["bounds_min"] = mins
            info["bounds_max"] = maxs
            info["dimensions"] = [maxs[i] - mins[i] for i in range(3)]
    except Exception as exc:
        info["warning"] = f"obj bounds unavailable: {exc}"
    return info


def ascii_stl_bounds(text: str) -> Optional[Dict[str, Any]]:
    mins = [math.inf, math.inf, math.inf]
    maxs = [-math.inf, -math.inf, -math.inf]
    count = 0
    for m in re.finditer(r"vertex\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)", text):
        vals = [float(m.group(1)), float(m.group(2)), float(m.group(3))]
        for i, v in enumerate(vals):
            mins[i] = min(mins[i], v)
            maxs[i] = max(maxs[i], v)
        count += 1
    if not count:
        return None
    return {"vertex_count": count, "bounds_min": mins, "bounds_max": maxs, "dimensions": [maxs[i] - mins[i] for i in range(3)]}


def binary_stl_bounds(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with path.open("rb") as fh:
            header = fh.read(80)
            raw_count = fh.read(4)
            if len(raw_count) != 4:
                return None
            tri_count = struct.unpack("<I", raw_count)[0]
            mins = [math.inf, math.inf, math.inf]
            maxs = [-math.inf, -math.inf, -math.inf]
            read_tri = 0
            for _ in range(tri_count):
                chunk = fh.read(50)
                if len(chunk) != 50:
                    break
                vals = struct.unpack("<12fH", chunk)
                coords = vals[3:12]
                for j in range(0, 9, 3):
                    p = [coords[j], coords[j + 1], coords[j + 2]]
                    for i, v in enumerate(p):
                        mins[i] = min(mins[i], v)
                        maxs[i] = max(maxs[i], v)
                read_tri += 1
            if not read_tri:
                return None
            return {
                "triangle_count": read_tri,
                "bounds_min": mins,
                "bounds_max": maxs,
                "dimensions": [maxs[i] - mins[i] for i in range(3)],
            }
    except Exception:
        return None


def stl_info(path: Path) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "stl_mesh"}
    try:
        head = path.read_bytes()[:2048]
        maybe_text = head.decode("utf-8", errors="ignore")
        if maybe_text.lstrip().lower().startswith("solid"):
            full_text = path.read_text(encoding="utf-8", errors="replace")
            bounds = ascii_stl_bounds(full_text)
            if bounds:
                info.update({"format": "ascii", **bounds})
                return info
        bounds = binary_stl_bounds(path)
        if bounds:
            info.update({"format": "binary", **bounds})
        else:
            info["warning"] = "could not determine stl bounds"
    except Exception as exc:
        info["warning"] = f"stl inspection unavailable: {exc}"
    return info


def dxf_info(path: Path, max_chars: int = 3000) -> Dict[str, Any]:
    info: Dict[str, Any] = {"kind": "dxf_or_dwg_text"}
    try:
        data = path.read_text(encoding="utf-8", errors="replace")
        info["line_count"] = data.count("\n") + 1
        for token in ["DIMENSION", "LINE", "CIRCLE", "ARC", "TEXT", "MTEXT"]:
            info[f"count_{token.lower()}"] = data.upper().count(token)
        # Dimension-like text snippets.
        snippets = re.findall(r"(?i)(?:\b\d+(?:\.\d+)?\s*(?:mm|cm|m|deg|°)|[røφ]\s*\d+(?:\.\d+)?)", data)
        info["dimension_like_text"] = snippets[:50]
        info["preview"] = data[:max_chars]
    except Exception as exc:
        info["warning"] = f"dxf text inspection unavailable: {exc}"
    return info


def inspect_path(path: Path) -> Dict[str, Any]:
    rec = file_record(path)
    suffix = path.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".webp"}:
        rec.update(image_info(path))
    elif suffix in {".txt", ".md", ".csv", ".json", ".yaml", ".yml"}:
        rec.update(text_preview(path))
    elif suffix == ".docx":
        rec.update(docx_preview(path))
    elif suffix in {".step", ".stp", ".iges", ".igs"}:
        rec.update(step_info(path))
    elif suffix == ".stl":
        rec.update(stl_info(path))
    elif suffix == ".obj":
        rec.update(obj_bounds(path))
    elif suffix in {".dxf", ".dwg"}:
        rec.update(dxf_info(path))
    else:
        rec["kind"] = "unknown_or_binary"
        rec["note"] = "only file metadata inspected"
    return rec


def expand_inputs(paths: Iterable[str]) -> List[Path]:
    out: List[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            out.extend([q for q in path.rglob("*") if q.is_file()])
        elif path.exists():
            out.append(path)
        else:
            out.append(path)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect mixed mechanical modeling input files.")
    parser.add_argument("paths", nargs="+", help="files or folders to inspect")
    parser.add_argument("--pretty", action="store_true", help="pretty-print json")
    args = parser.parse_args()

    records = []
    for path in expand_inputs(args.paths):
        if not path.exists():
            records.append({"path": str(path), "error": "not found"})
            continue
        try:
            records.append(inspect_path(path))
        except Exception as exc:
            records.append({"path": str(path), "error": str(exc)})

    print(json.dumps(records, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
