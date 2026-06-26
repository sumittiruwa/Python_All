#!/usr/bin/env python3
"""
organize.py — Sort a messy folder into clean subfolders by file type.

A single-file utility with no external dependencies. Great for tidying up
folders like Downloads or Desktop.

Examples
--------
    # See what WOULD happen, without moving anything (safe preview):
    python organize.py ~/Downloads --dry-run

    # Actually organize the folder:
    python organize.py ~/Downloads

    # Organize, then undo the last run if you change your mind:
    python organize.py ~/Downloads
    python organize.py ~/Downloads --undo
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Map a category name -> the file extensions that belong in it.
CATEGORIES = {
    "Images":      {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic", ".tiff"},
    "Documents":   {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".tex"},
    "Spreadsheets":{".xls", ".xlsx", ".csv", ".tsv", ".ods"},
    "Slides":      {".ppt", ".pptx", ".odp", ".key"},
    "Audio":       {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "Video":       {".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv"},
    "Archives":    {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
    "Code":        {".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".go", ".rs", ".sh", ".json"},
    "Installers":  {".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage"},
}
OTHER = "Other"  # anything that doesn't match a known category

# Where the undo log is stored inside the target folder.
LOG_NAME = ".organize_log.json"


def category_for(extension: str) -> str:
    """Return the category name for a given file extension."""
    ext = extension.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return OTHER


def unique_destination(dest: Path) -> Path:
    """If dest already exists, append ' (1)', ' (2)', ... so nothing is overwritten."""
    if not dest.exists():
        return dest
    stem, suffix, parent = dest.stem, dest.suffix, dest.parent
    counter = 1
    while True:
        candidate = parent / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder: Path, dry_run: bool) -> None:
    """Move each top-level file in `folder` into a category subfolder."""
    if not folder.is_dir():
        sys.exit(f"Error: '{folder}' is not a folder.")

    moves = []  # records of (source, destination) for the undo log
    counts = {}

    # Only loop over files directly inside the folder (not subfolders).
    for item in sorted(folder.iterdir()):
        if item.is_dir() or item.name == LOG_NAME or item.name.startswith("."):
            continue

        category = category_for(item.suffix)
        target_dir = folder / category
        destination = unique_destination(target_dir / item.name)

        counts[category] = counts.get(category, 0) + 1

        if dry_run:
            print(f"  would move  {item.name}  ->  {category}/{destination.name}")
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            moves.append({"from": str(destination), "to": str(item)})
            print(f"  moved  {item.name}  ->  {category}/{destination.name}")

    if not counts:
        print("Nothing to organize — the folder has no loose files.")
        return

    print("\nSummary:")
    for category, n in sorted(counts.items()):
        print(f"  {category:<13} {n} file(s)")

    if dry_run:
        print("\nThis was a dry run. Re-run without --dry-run to actually move files.")
    else:
        # Save the undo log so the run can be reversed later.
        log = {"time": datetime.now().isoformat(timespec="seconds"), "moves": moves}
        (folder / LOG_NAME).write_text(json.dumps(log, indent=2))
        print(f"\nDone. Run with --undo to reverse this ({len(moves)} files).")


def undo(folder: Path) -> None:
    """Reverse the most recent organize run using the saved log."""
    log_path = folder / LOG_NAME
    if not log_path.exists():
        sys.exit("Nothing to undo — no organize log found in this folder.")

    log = json.loads(log_path.read_text())
    restored = 0
    for move in reversed(log["moves"]):
        src, dst = Path(move["from"]), Path(move["to"])
        if src.exists():
            dst = unique_destination(dst)
            shutil.move(str(src), str(dst))
            restored += 1

    # Clean up now-empty category folders and the log itself.
    for category in list(CATEGORIES) + [OTHER]:
        d = folder / category
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    log_path.unlink()
    print(f"Undo complete — restored {restored} file(s).")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort a folder into subfolders by file type."
    )
    parser.add_argument("folder", type=Path, help="The folder to organize.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without moving anything.")
    parser.add_argument("--undo", action="store_true",
                        help="Reverse the most recent organize run.")
    args = parser.parse_args()

    folder = args.folder.expanduser().resolve()

    if args.undo:
        undo(folder)
    else:
        print(f"Organizing: {folder}\n")
        organize(folder, dry_run=args.dry_run)


if __name__ == "__main__":
    main()