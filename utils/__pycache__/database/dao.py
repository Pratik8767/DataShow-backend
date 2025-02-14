# import datetime
# from uuid import uuid4
# import uuid

# from src.model.model import FileTable
# from src.utils.logs import CustomLogger

# logger_instance = CustomLogger(log_level='DEBUG', log_file_name='file.log', log_path='logs')
# logger = logger_instance.get_logger()


# class FileDAO:
 
#     async def upload_csv(data,db):
#         # Upload the file to the database
#         try:
#              # Save the analysis data into the database.
#             data["id"] = str(uuid.uuid4())  # Generate a unique ID for the file.
#             data["uploaded_at"] = datetime.datetime.now()  # Use current timestamp.
#             data["row_count"] = int(data["row_count"])  # Convert numpy.int64 to int
#             data["column_count"] = int(data["column_count"])  # Convert numpy.int64 to int
#             data["empty_cells"] = int(data["empty_cells"])  # Convert numpy.int64 to int
#             create_file_record = FileTable(**data)
#             db.add(create_file_record)
#             db.commit()
#             db.refresh(create_file_record)
#             return create_file_record
#         except Exception as e:
#             logger.error(str(e))
#             db.rollback()
#             raise Exception("Error uploading file: " + str(e))


# import datetime
# import uuid
# from db_session import get_db
# from src.model.model import FileTable

# class FileDAO:
#     @staticmethod
#     def upload_csv(data, db):
#         try:
#             data["id"] = str(uuid.uuid4())
#             data["uploaded_at"] = datetime.datetime.now()
#             data["row_count"] = int(data["row_count"])
#             data["column_count"] = int(data["column_count"])
#             data["empty_cells"] = int(data["empty_cells"])

#             create_file_record = FileTable(**data)
#             db.add(create_file_record)
#             db.commit()
#             db.refresh(create_file_record)

#             return create_file_record
#         except Exception as e:
#             db.rollback()
#             raise Exception(f"Error uploading file: {str(e)}")
