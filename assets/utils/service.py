
import os
import uuid
from pathlib import Path
from  typing import Tuple, List

from fastapi import UploadFile

from utils.security import validate_upload
from dataclasses import dataclass

from utils.paths import BASE_STATIC_DIR

BASE_DIR = BASE_STATIC_DIR 
TMP_SUFFIX = ".tmp"



class AssetServiceError(Exception):
    pass


class AssetWriteError(AssetServiceError):
    pass


class AssetNotFoundError(AssetServiceError):
    pass

class AssetCollisionError(AssetServiceError) : 
    pass 

class PathTraversalError(AssetServiceError) : 
    pass 


import utils.metadata as metadata 
import json

def _get_image_metadata(asset_id: str) -> dict:
    if not metadata.METADATA_PATH.exists():
        raise AssetNotFoundError("Asset not found")

    with metadata.METADATA_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    for img in data.get("images", []):
        if img.get("id") == asset_id:
            return img

    raise AssetNotFoundError("Asset not found")



@dataclass(frozen=True)
class SavedImage: 
    asset_id: str 
    relative_path: str 
    mime: str 
    size:int

def _ensure_base_dir() -> None:
    """Ensure base directory exists and is a directory."""
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    if not BASE_DIR.is_dir():
        raise AssetWriteError("Asset base directory is not a directory")



def _generate_filename(ext: str) -> str:
    return f"{uuid.uuid4()}.{ext}"


def save_image(file: UploadFile) -> SavedImage:
    _ensure_base_dir()

    image_type = validate_upload(file)

    filename = _generate_filename(image_type)
    final_path = (BASE_DIR / filename).resolve()
    
    if final_path.exists():
        raise AssetCollisionError("File already exists")

    if BASE_DIR not in final_path.parents:
        raise PathTraversalError("Resolved path escapes asset directory")

    tmp_path = final_path.with_suffix(final_path.suffix + TMP_SUFFIX)
    size = 0

    try:
        with open(tmp_path, "xb") as tmp:
            while True:
                chunk = file.file.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                tmp.write(chunk)
            tmp.flush()
            os.fsync(tmp.fileno())

        os.replace(tmp_path, final_path)

    except FileExistsError:
        raise AssetCollisionError("File already exists")

    except OSError as exc:
        raise AssetWriteError("Failed to write asset") from exc

    finally:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass

    return SavedImage(
        asset_id=final_path.stem,
        relative_path=final_path.name,
        mime=f"image/{image_type}",
        size=size,
    )



def delete_image(asset_id: str) -> None:
    _ensure_base_dir()

    if "/" in asset_id or "\\" in asset_id:
        raise AssetWriteError("Invalid asset id")

    img = _get_image_metadata(asset_id)

    target = (BASE_DIR / img["path"]).resolve()

    if BASE_DIR not in target.parents:
        raise PathTraversalError("Resolved path escapes asset directory")

    if not target.exists():
        raise AssetNotFoundError("Asset not found")

    try:
        target.unlink()
    except OSError as exc:
        raise AssetWriteError("Failed to delete asset") from exc

    metadata.remove_image_metadata(asset_id)
