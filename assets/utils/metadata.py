from __future__ import annotations

import json
import os
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import fcntl

# Base paths
BASE_STATIC_DIR = Path("app/static/img")
METADATA_PATH = BASE_STATIC_DIR / "metadata.json"


class MetadataError(Exception):
    """Base class for metadata errors."""


class MetadataLockError(MetadataError):
    pass


class MetadataWriteError(MetadataError):
    pass


@contextmanager
def _locked_metadata_file(path: Path):
    """Open metadata file with an exclusive lock."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_RDWR | os.O_CREAT, 0o644)
        with os.fdopen(fd, "r+") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            yield f
    except OSError as exc:
        raise MetadataLockError(str(exc)) from exc
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        except Exception:
            pass


def _load_metadata(file_obj) -> Dict:
    try:
        file_obj.seek(0)
        content = file_obj.read().strip()
        if not content:
            return {"images": []}
        return json.loads(content)
    except json.JSONDecodeError:
        raise MetadataWriteError("Invalid metadata.json format")

def list_image_ids() -> List[str] : 
    if not METADATA_PATH.exists() : 
        return [] 
    with METADATA_PATH.open("r", encoding="utf-8") as f : 
        data = json.load(f) 
    return [img.get("id") for img in data.get("images", []) if "id" in img]

def _atomic_write_json(target: Path, data: Dict) -> None:
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            dir=str(target.parent),
            delete=False,
            encoding="utf-8",
        ) as tmp:
            json.dump(data, tmp, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
            tmp_path = Path(tmp.name)
        os.replace(tmp_path, target)
    except OSError as exc:
        raise MetadataWriteError(str(exc)) from exc


def add_image_metadata(
    *,
    asset_id: str,
    relative_path: str,
    mime: str,
    size: int,
) -> Dict:
    entry = {
        "id": asset_id,
        "path": relative_path,
        "mime": mime,
        "size": size,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    with _locked_metadata_file(METADATA_PATH) as f:
        metadata = _load_metadata(f)
        images: List[Dict] = metadata.setdefault("images", [])

        if any(img.get("id") == asset_id for img in images):
            raise MetadataWriteError("Duplicate asset id")

        images.append(entry)
        _atomic_write_json(METADATA_PATH, metadata)

    return entry


def remove_image_metadata(asset_id: str) -> None:
    """Remove image entry from metadata.json."""
    with _locked_metadata_file(METADATA_PATH) as f:
        metadata = _load_metadata(f)
        images: List[Dict] = metadata.get("images", [])

        new_images = [img for img in images if img.get("id") != asset_id]
        metadata["images"] = new_images

        _atomic_write_json(METADATA_PATH, metadata)
