from fastapi import APIRouter, UploadFile, File, HTTPException
from src.file.services.service import FileManagement

class FileRouter:
    router = APIRouter()

    @router.post("/file/upload/")
    async def upload_csv(file: UploadFile = File(...)):
        """Uploads a CSV file and processes it."""
        try:
            if not file.filename.endswith(".csv"):
                raise HTTPException(status_code=400, detail="Only CSV files are allowed")

            result = FileManagement.upload_csv(await file.read(), file.filename)
            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @router.get("/file/info")
    async def get_file_info():
        """Retrieves file metadata such as row count, column count, and missing values."""
        try:
            file_info = FileManagement.get_file_status()
            return {"file_details": file_info}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))




# from flask import Blueprint, request, jsonify
# from db_session import get_db
# from src.file.services.service import FileManagement

# file_api = Blueprint('file_api', __name__)

# @file_api.route("/file/upload/", methods=["POST"])
# def upload_csv():
#     db = next(get_db())  # Get DB session
#     try:
#         file = request.files.get("file")
#         if not file:
#             return jsonify({"error": "No file provided"}), 400
#         if not file.filename.endswith(".csv"):
#             return jsonify({"error": "Only CSV files are allowed"}), 400
        
#         result = FileManagement.upload_csv(file)
#         return jsonify(result), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         db.close()


# @file_api.route("/file/info",methods=["GET"])
# def get_file_info():
#     try:
#         file_info=FileManagement.get_file_status()
#         return jsonify({"file_details": file_info}), 200



#     except Exception as e:
#                 return jsonify({"error": str(e)}), 400


