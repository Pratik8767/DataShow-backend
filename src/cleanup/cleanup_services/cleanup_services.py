import tempfile
import pandas as pd
from src.file.services.service import FileManagement

class CleanUpService:
    cleaned_file_path = None

    @staticmethod
    def cleanup_methods(cleanup_actions: list) -> dict:
        """Performs cleanup actions on the uploaded file and saves the cleaned data into a new file."""
        try:
            if FileManagement.temp_file_path is None:
                raise ValueError("No file uploaded")

            df = pd.read_csv(FileManagement.temp_file_path)
            applied_operations = []

            for action in cleanup_actions:
                if action == "remove_duplicates":
                    df = CleanUpService.remove_duplicates(df)
                elif action == "fill_missing_values":
                    df = CleanUpService.fill_missing_values(df) 
                elif action == "convert_data_types":
                    df = CleanUpService.convert_data_types(df)
                else:
                    raise ValueError(f"Invalid cleanup option: {action}")
                
                applied_operations.append(action) 

            with tempfile.NamedTemporaryFile(delete=False, suffix="_cleaned.csv") as cleaned_temp_file:
                df.to_csv(cleaned_temp_file.name, index=False)
                CleanUpService.cleaned_file_path = cleaned_temp_file.name


            return {
                "message": "Cleanup operations completed",
                "applied_operations": applied_operations,
                "cleaned_file_path": CleanUpService.cleaned_file_path,
                "new_row_count": df.shape[0],
                "new_column_count": df.shape[1],
                "empty_cells": int(df.isnull().sum().sum()),

            }
        except Exception as e:
            raise Exception(f"Cleanup failed: {str(e)}")

    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        """Removes duplicate rows."""
        return df.drop_duplicates()

    @staticmethod
    def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
        """Fills missing values based on column type."""
        for col in df.columns:
             if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
             else:
                  df[col] = df[col].fillna(df[col].mean())
  
        return df

    @staticmethod
    def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
        """Converts columns to appropriate data types."""
        df = df.convert_dtypes()
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        return df




# import tempfile
# import pandas as pd
# from src.file.services.service import FileManagement

# class CleanUpService:
#     cleaned_file_path=None
#     @staticmethod
#     def cleanup_methods(cleanup_actions):
#         '''
#         Performs cleanup actions on the uploaded file and saves the cleaned data into a new file.

#         Returns:
#         A dictionary with details of the cleanup operation.
#         '''
#         try:
#             if FileManagement.temp_file_path is None:
#                 raise Exception("No file uploaded")

#             df = pd.read_csv(FileManagement.temp_file_path)
#             applied_operations = []

#             for action in cleanup_actions:
#                 if action == "remove_duplicates":
#                     df = CleanUpService.remove_duplicates(df)
#                 elif action == "fill_missing_values":
#                     df = CleanUpService.fill_missing_values(df)
#                 elif action == "convert_data_types":
#                     df = CleanUpService.convert_data_types(df)
#                 else:
#                     raise Exception(f"Invalid cleanup option: {action}")
                
#                 applied_operations.append(action)

#             with tempfile.NamedTemporaryFile(delete=False, suffix="_cleaned.csv") as cleaned_temp_file:
#                 df.to_csv(cleaned_temp_file.name, index=False)
#                 CleanUpService.cleaned_file_path = cleaned_temp_file.name


#             return {
#                 "message": "Cleanup operations completed",
#                 "applied_operations": applied_operations,
#                 "cleaned_file_path": CleanUpService.cleaned_file_path,
#                 "new_row_count": df.shape[0],
#                 "new_column_count": df.shape[1],
#             }
#         except Exception as e:
#             raise Exception(f"Cleanup failed: {str(e)}")

#     @staticmethod
#     def remove_duplicates(df):
#         """Removes duplicate rows."""
#         return df.drop_duplicates()

#     @staticmethod
#     def fill_missing_values(df):
#         """Fills missing values based on column type."""
#         for col in df.columns:
#             if df[col].dtype == "object":
#                 df[col].fillna("Unknown", inplace=True)
#             else:
#                 df[col].fillna(df[col].mean(), inplace=True)  
#         return df

#     @staticmethod
#     def convert_data_types(df):
#         """Converts columns to appropriate data types."""
#         df = df.convert_dtypes()
#         if "Subscription Date" in df.columns:
#             df["Subscription Date"] = pd.to_datetime(df["Subscription Date"], errors="coerce")
#         return df
