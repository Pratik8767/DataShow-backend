


import tempfile
import pandas as pd
from file.services.service import FileManagement


class CleanUpService:


    @staticmethod
    def cleanup_methods(cleanup_actions):
        try:
            if FileManagement.temp_file_path is None:
                raise ("no file uploaded")
            df=pd.read_csv(FileManagement.temp_file_path)
            applied_operations=[]

            for action in cleanup_actions:
                if action=="remove_duplicates":
                    df=CleanUpService.remove_duplicates(df)
                elif action =="fill_missing_values":
                    df=CleanUpService.fill_missing_values(df)
                elif action=="convert_data_types":
                    df=CleanUpService.convert_data_types(df)

                else:raise(f"Invalid cleanup option:{action}")

                applied_operations.append(action)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as cleaned_temp_file:
                df.to_csv(cleaned_temp_file.name, index=False)
                FileManagement.temp_file_path = cleaned_temp_file.name

            return {
                "message": "Cleanup operations completed",
                "applied_operations": applied_operations,
                "file_name": FileManagement.temp_file_path,
                "new_row_count": df.shape[0],
                "new_column_count": df.shape[1],
            }

        except Exception as e:
            raise Exception(f"Cleanup failed: {str(e)}")





    @staticmethod
    def remove_duplicates(df):
        """Removes duplicate rows."""
        return df.drop_duplicates()

    @staticmethod
    def fill_missing_values(df):
        """Fills missing values based on column type."""
        for col in df.columns:
            if df[col].dtype == "object":
                df[col].fillna("Unknown", inplace=True)
            else:
                df[col].fillna(df[col].mean(), inplace=True)  
        return df

    @staticmethod
    def convert_data_types(df):
        """Converts columns to appropriate data types."""
        df = df.convert_dtypes()
        if "Subscription Date" in df.columns:
            df["Subscription Date"] = pd.to_datetime(df["Subscription Date"], errors="coerce")
        return df