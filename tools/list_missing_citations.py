#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def analyze_paragraphs(root_dir: Path) -> list[dict]:
    """Flags paragraphs with claim verbs but no citations (heuristic, non-failing)."""
    claim_verbs = [
        "shows", "show", "proves", "prove", "implies", "imply",
        "therefore", "establishes", "establish", "demonstrates",
        "demonstrate", "confirms", "confirm"
    ]
    verb_pattern = re.compile(r"\b(" + "|".join(claim_verbs) + r")\b", re.IGNORECASE)

    # Treat citations as [KEY] but ignore markdown links/images ([text](...) / ![alt](...))
    cite_pattern = re.compile(r"(?<!\!)\[[A-Za-z0-9_-]+\](?!\()")

    warnings: list[dict] = []
    for md_file in root_dir.rglob("*.md"):
        posix = md_file.as_posix()
        if posix.endswith("references/bibliography.md") or md_file.name == "LICENSE":
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
            paragraphs = re.split(r"\n\s*\n", content)
            for i, para in enumerate(paragraphs, 1):
                clean_para = para.strip().replace("\n", " ")
                if not clean_para:
                    continue
                if verb_pattern.search(clean_para) and not cite_pattern.search(clean_para):
                    snippet = clean_para[:160] + ("…" if len(clean_para) > 160 else "")
                    warnings.append({"file": posix, "paragraph": i, "snippet": snippet})
        except Exception as e:
            print(f"Error processing {posix}: {e}")

    return warnings


def main() -> int:
    root = Path(".")
    warnings = analyze_paragraphs(root)

    if warnings:
        print(f"HEURISTIC AUDIT: Found {len(warnings)} potential missing citations.")
        for w in warnings:
            print(f"FILE: {w['file']} [Para {w['paragraph']}] Snippet: \"{w['snippet']}\"")
    else:
        print("HEURISTIC AUDIT: No obvious missing citations detected.")

    # Do not fail CI on heuristics.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
