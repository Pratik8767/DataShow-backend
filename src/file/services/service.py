import pandas as pd
import tempfile

class FileManagement:
    temp_file_path = None 
    file_name=None
    
    @staticmethod
    def upload_csv(file):
        try:
            # Store file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                temp_file.write(file.read())
                FileManagement.temp_file_path = temp_file.name
            
            # Read CSV into pandas
            df = pd.read_csv(FileManagement.temp_file_path)
            row_count = df.shape[0]
            column_count = df.shape[1]
            empty_cells = df.isnull().sum().sum()
            FileManagement.file_name=file.filename

            # Convert numpy int64 to Python int
            data = {
                "row_count": int(row_count),  # Convert to standard int
                "column_count": int(column_count),
                "empty_cells": int(empty_cells),
                "file_name": file.filename,
            }

            return {"message": "File Uploaded Successfully", "file_details": data}
        
        except Exception as e:
            raise Exception(f"Error uploading CSV file: {str(e)}")


    @staticmethod
    def get_file_status():
        try:
            if FileManagement.temp_file_path is None:
                raise Exception ("No file uploaded")
            df=pd.read_csv(FileManagement.temp_file_path)
            row_count = df.shape[0]
            column_count = df.shape[1]
            empty_cells = df.isnull().sum().sum()
            duplicates=df.duplicated().sum()
            file_name=FileManagement.file_name
            column_data_types = {col: str(df[col].dtype) for col in df.columns}


            data={
                "file_name":file_name,
                "row_count":   int(  row_count),
                "column_count": int(   column_count),
                "empty_cells": int(  empty_cells),
                "duplicates":   int(  duplicates),
                "columns_datatypes":column_data_types
            }

            return data

        except Exception as e:
            raise Exception(f"Error in getting file status",str(e))    