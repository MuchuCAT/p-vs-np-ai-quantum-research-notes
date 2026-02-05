#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def get_defined_keys(bib_path: Path) -> set[str]:
    """
    Extract keys defined in references/bibliography.md.

    Supported formats (start of line):
      **[KEY]**
      - **[KEY]**
      * **[KEY]**
    """
    if not bib_path.exists():
        return set()

    content = bib_path.read_text(encoding="utf-8")
    pattern = re.compile(r'^\s*(?:[-*]\s+)?\*\*\[([A-Za-z0-9_-]+)\]\*\*', re.MULTILINE)
    return set(pattern.findall(content))


def check_notes(root_dir: Path, defined_keys: set[str]) -> list[dict]:
    """
    Scan .md files for citation keys [KEY], ignoring:
      - markdown links [text](...)
      - markdown images ![alt](...)
    """
    errors: list[dict] = []
    cite_pattern = re.compile(r'(?<!\!)\[([A-Za-z0-9_-]+)\](?!\()')

    for md_file in root_dir.rglob("*.md"):
        posix = md_file.as_posix()
        if posix.endswith("references/bibliography.md") or md_file.name == "LICENSE":
            continue

        try:
            with open(md_file, "r", encoding="utf-8", newline=None) as f:
                for line_num, line in enumerate(f, 1):
                    for key in cite_pattern.findall(line):
                        if key not in defined_keys:
                            errors.append({"file": posix, "line": line_num, "key": key})
        except Exception as e:
            print(f"Error reading {posix}: {e}")
            return [{"file": posix, "line": 0, "key": "READ_ERROR"}]

    return errors


def main() -> int:
    root = Path(".")
    bib_file = root / "references" / "bibliography.md"

    defined_keys = get_defined_keys(bib_file)
    if not defined_keys:
        print("FAIL: No bibliography keys detected. Check references/bibliography.md formatting.")
        return 1

    citation_errors = check_notes(root, defined_keys)
    if citation_errors:
        print(f"FAIL: Found {len(citation_errors)} undefined citations.")
        for err in citation_errors:
            print(f"{err['file']}:{err['line']}: error: Undefined key '[{err['key']}]'")
        return 1

    print("SUCCESS: All citations valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
