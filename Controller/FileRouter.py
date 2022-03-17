import uuid
from typing import Optional
from fastapi import FastAPI, APIRouter
from fastapi import FastAPI, File, UploadFile

from Service.FileService import FileService

router = APIRouter()

fileService = FileService()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@router.post("/predict_disease/")
async def create_upload_file(file: UploadFile):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    IMAGEDIR = "Service/"
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)


    results = fileService.prediction_results(contents, file.filename)
    return results

