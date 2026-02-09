from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from utils.security import FileTooLargeError, InvalidImageError
from utils.service import AssetNotFoundError, AssetWriteError, AssetCollisionError, PathTraversalError
from utils.metadata import MetadataError


def problem_details(
    *,
    status_code: int,
    title: str,
    detail: str,
    type_: str,
    instance: str,
):
    return JSONResponse(
        status_code=status_code,
        media_type="application/problem+json",
        content={
            "type": type_,
            "title": title,
            "status": status_code,
            "detail": detail,
            "instance": instance,
        },
    )



def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(FileTooLargeError)
    async def file_too_large_handler(request: Request, exc: FileTooLargeError):
        return problem_details(
            status_code=413,
            title="Payload Too Large",
            detail=str(exc),
            type_="https://example.com/problems/payload-too-large",
            instance=str(request.url.path),
        )

    @app.exception_handler(InvalidImageError)
    async def invalid_image_handler(request: Request, exc: InvalidImageError):
        return problem_details(
            status_code=400,
            title="Unsupported Media Type",
            detail=str(exc),
            type_="https://example.com/problems/invalid-image",
            instance=str(request.url.path),
        )

    @app.exception_handler(AssetNotFoundError)
    async def asset_not_found_handler(request: Request, exc: AssetNotFoundError):
        return problem_details(
            status_code=404,
            title="Asset Not Found",
            detail=str(exc),
            type_="https://example.com/problems/not-found",
            instance=str(request.url.path),
        )

    @app.exception_handler(AssetCollisionError)
    async def asset_collision_handler(request: Request, exc: AssetCollisionError):
        return problem_details(
            status_code=409,
            title="Asset Already Exists",
            detail=str(exc),
            type_="https://example.com/problems/asset-collision-error",
            instance=str(request.url.path),
        )

    @app.exception_handler(PathTraversalError)
    async def path_traversal_handler(request: Request, exc: PathTraversalError):
        return problem_details(
            status_code=403,
            title="Invalid Path",
            detail=str(exc),
            type_="https://example.com/problems/asset-traversal-error",
            instance=str(request.url.path),
        )
    
    @app.exception_handler(AssetWriteError)
    async def asset_write_handler(request: Request, exc: AssetWriteError):
        return problem_details(
            status_code=403,
            title="Asset Write Failed",
            detail=str(exc),
            type_="https://example.com/problems/asset-write-error",
            instance=str(request.url.path),
        )

    @app.exception_handler(MetadataError)
    async def metadata_error_handler(request: Request, exc: MetadataError):
        return problem_details(
            status_code=500,
            title="Metadata Error",
            detail=str(exc),
            type_="https://example.com/problems/metadata-error",
            instance=str(request.url.path),
        )
