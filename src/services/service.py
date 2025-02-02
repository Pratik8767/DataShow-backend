from sys import exc_info
import pandas as pd

from src.database.dao import FileDAO
from src.utils.logs import CustomLogger

logger_instance = CustomLogger(log_level='DEBUG', log_file_name='file.log', log_path='logs')
logger = logger_instance.get_logger()

class FileManagement:

    async def upload_csv(file,db):
        # Upload the CSV file to the server
        try:
            # Analyze the uploaded CSV file.
            # Read the CSV file into a pandas DataFrame.
            df = pd.read_csv(file.file)
            
            # Get the total rows, columns, and empty cells in the DataFrame.
            row_count = df.shape[0]
            column_count = df.shape[1]
            empty_cells = df.isnull().sum().sum()

            # Collect metadata about each column.
            columns_info = []
            for col in df.columns:
                col_data = {
                    "name": col,  # Column name
                    "type": str(df[col].dtypes),  # Data type of the column
                    "empty_count": df[col].isnull().sum()  # Number of empty cells
                }
                columns_info.append(col_data)

            # Calculate the distribution of data types in the DataFrame.
            type_dist = df.dtypes.value_counts().to_dict()
            type_distribution_info = [{"type": str(k), "count": int(v)} for k, v in type_dist.items()]

            data = {
                "row_count": row_count,
                "column_count": column_count,
                "empty_cells": empty_cells,
                "file_name":file.filename,
                # "columns_info": columns_info,
                # "type_distribution": type_distribution_info
            }
            result = await FileDAO.upload_csv(data,db)
            logger.info(f"Save file : {data}")
            return {"message":"File Upload Successfully"}
        except Exception as e:
            logger.error(f"Error : {str(e)}")
            raise Exception("Error uploading CSV file: " + str(e))