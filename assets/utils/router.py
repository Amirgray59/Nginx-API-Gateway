from __future__ import annotations

from fastapi import APIRouter, File, UploadFile, Response, status, HTTPException
from fastapi.responses import JSONResponse

from utils.service import save_image, delete_image as delete_image_service
from utils.security import validate_image
from utils.metadata import add_image_metadata,  list_image_ids   
from utils.service import AssetNotFoundError, AssetWriteError 

from pathlib import Path

router = APIRouter(prefix="/images")


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Image uploaded"},
        413: {"description": "Payload too large"},
        415: {"description": "Unsupported media type"},
        500: {"description": "Internal server error"},
    },
)
async def upload_image(file: UploadFile = File(...)):
    validate_image(file)
    saved = save_image(file)

    entry = add_image_metadata(
        asset_id=saved.asset_id,
        relative_path=saved.relative_path,
        mime=saved.mime,
        size=saved.size,
    )

    headers = {"Location": saved.relative_path}
    return JSONResponse(status_code=201, content=entry, headers=headers)

@router.get("/", status_code=200, responses={
    200: {"description": "List image asset IDs"}
})
async def list_images() : 
    return {"images": list_image_ids()}

@router.delete(
    "/{asset_id}",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_image_route(asset_id: str) -> None:
    try:
        delete_image_service(asset_id)
    except AssetNotFoundError:
        raise HTTPException(status_code=404, detail="Not found")
    except AssetWriteError:
        raise HTTPException(status_code=400, detail="Invalid asset id")

    return Response(status_code=status.HTTP_204_NO_CONTENT) 

    
