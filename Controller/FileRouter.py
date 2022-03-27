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
#asyc call (the call isn't blocked until you get the result)
async def create_upload_file(file: UploadFile):
    file.filename = f"{uuid.uuid4()}.jpg"
    #the read function is defined with async, call it with await
    contents = await file.read()
    IMAGEDIR = "files/"

    #save file to local path (db)
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)


    results = fileService.prediction_results( file.filename)
    return results

