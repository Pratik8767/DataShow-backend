import datetime
from uuid import uuid4
from fastapi import FastAPI, Depends, Form, HTTPException,APIRouter, UploadFile,File
from db_session import get_db
from sqlalchemy.orm import Session
from src.services.service import FileManagement
from src.utils.logs import CustomLogger

logger_instance = CustomLogger(log_level='DEBUG', log_file_name='file.log', log_path='logs')
logger = logger_instance.get_logger()

class File:
    
    router = APIRouter()

    @router.post("/file/upload/")
    async def upload_csv(file: UploadFile,db:Session=Depends(get_db)):
        try :
            if not file.filename.endswith(".csv"):
                raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
            result = await FileManagement.upload_csv(file,db)
            logger.info(f"File uploaded successfully {file.filename}")
            return {"message": "File uploaded successfully"}
        except Exception as e:
            logger.error(f"Error : {e}")
            raise HTTPException(status_code=400, detail="Error while uploading file")
        