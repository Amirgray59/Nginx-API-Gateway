
import imghdr
from typing import BinaryIO

from fastapi import UploadFile


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_IMAGE_TYPES = {"png", "jpeg", "webp"}



class AssetSecurityError(Exception):
    pass


class FileTooLargeError(AssetSecurityError):
    pass


class InvalidImageError(AssetSecurityError):
    pass


def enforce_size_limit(file: UploadFile) -> None:
    total = 0
    chunk_size = 1024 * 1024  # 1MB chunks

    file.file.seek(0)

    while True:
        chunk = file.file.read(chunk_size)
        if not chunk:
            break
        total += len(chunk)
        if total > MAX_FILE_SIZE:
            raise FileTooLargeError("Uploaded file exceeds size limit")

    file.file.seek(0)


def detect_image_type(stream: BinaryIO) -> str:
    stream.seek(0)
    header = stream.read(512)
    stream.seek(0)
    return imghdr.what(None, header)


def validate_image(file: UploadFile) -> str:
    image_type = detect_image_type(file.file)

    if image_type not in ALLOWED_IMAGE_TYPES:
        raise InvalidImageError("File is not a valid or supported image")

    return image_type



def validate_upload(file: UploadFile) -> str:
    enforce_size_limit(file)
    return validate_image(file)
