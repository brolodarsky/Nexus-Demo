"""
index_manifest.py — Tracks file modification times for incremental indexing.

Stores a JSON manifest mapping {relative_path: mtime_epoch} so that
ingest_vault.py can skip files that haven't changed since the last run.
The manifest file (.rag_index_manifest.json) lives at the project root
alongside .chroma_db/ and is gitignored.
"""

import json
from pathlib import Path
from core.constants import PROJECT_ROOT

MANIFEST_PATH = PROJECT_ROOT / ".rag_index_manifest.json"


def load_manifest() -> dict[str, float]:
    """Load the manifest from disk. Returns empty dict if not found."""
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_manifest(manifest: dict[str, float]) -> None:
    """Write the manifest to disk."""
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def get_changed_files(
    md_files: list[Path], vault_path: Path
) -> tuple[list[Path], dict[str, float]]:
    """
    Compare current file mtimes against the manifest.

    Returns:
        changed_files: list of Path objects that are new or modified.
        new_manifest:  updated manifest dict (to be saved after successful ingestion).
    """
    old_manifest = load_manifest()
    new_manifest = {}
    changed_files = []

    for md_file in md_files:
        relative_path = str(md_file.relative_to(vault_path))
        current_mtime = md_file.stat().st_mtime

        new_manifest[relative_path] = current_mtime

        old_mtime = old_manifest.get(relative_path)
        if old_mtime is None or current_mtime > old_mtime:
            changed_files.append(md_file)

    return changed_files, new_manifest
