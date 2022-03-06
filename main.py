from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile

from Controller import FileRouter
from Controller.FileRouter import router

app = FastAPI()
app.include_router(router)
if __name__=="__main__":
    uvicorn.run(app)    
