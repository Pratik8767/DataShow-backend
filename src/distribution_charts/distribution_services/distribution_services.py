from fastapi import HTTPException
import pandas as pd
from src.file.services.service import FileManagement


class DistributionServices:
    """Class to provide distribution services"""

    @staticmethod
    def distribution_service() -> dict:
        try:
            if FileManagement.temp_file_path is None:
                raise ValueError("No file uploaded")

            df = pd.read_csv(FileManagement.temp_file_path)

            # Selecting numerical and categorical columns
            numerical_cols = df.select_dtypes(include=['number']).columns
            if len(numerical_cols) == 0:
                raise HTTPException(status_code=400, detail="No numerical columns found.")
            distribution_metrics = {"numerical": {}}
            chart_limits = {
                "max_range": 0,
                "max_variance": 0,
                "max_standard_deviation": 0,
                "max_interquartile_range": 0,
            }

            # Computing numerical data distribution
            for col in numerical_cols:
                min_val = int(df[col].min())
                max_val = int(df[col].max())
                range_val = max_val - min_val
                variance = float(df[col].var())
                std_dev = float(df[col].std())
                iqr = float(df[col].quantile(0.75) - df[col].quantile(0.25))

                distribution_metrics["numerical"][col] = {
                    "range": range_val,
                    "variance": variance,
                    "standard_deviation": std_dev,
                    "interquartile_range": iqr,
                }
                chart_limits["max_range"] = max(chart_limits["max_range"], max_val)
                chart_limits["max_variance"] = max(chart_limits["max_variance"], variance)
                chart_limits["max_standard_deviation"] = max(chart_limits["max_standard_deviation"], std_dev)
                chart_limits["max_interquartile_range"] = max(chart_limits["max_interquartile_range"], iqr)

          

            return {
                'message': 'Data distribution calculated',
                'distribution_metrics': distribution_metrics,
                'chart_limits': chart_limits
            }

        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error computing data distribution: {str(e)}")


    @staticmethod
    def picklist_distribution_service()->dict:
        try:
            if FileManagement.temp_file_path is None:
                raise ValueError("No file uploaded")

            df = pd.read_csv(FileManagement.temp_file_path)

            categorical_cols = df.select_dtypes(include=['object']).columns

            if len(categorical_cols) == 0:
                raise HTTPException(status_code=400, detail="No categorical columns found.")
            distribution_metrics ={ "categorical": {}}


            for col in categorical_cols:
                frequency_dict = df[col].value_counts().to_dict()
                frequency_dict = {k: int(v) for k, v in frequency_dict.items()}
                mode_values = df[col].mode().values
                mode = mode_values[0] if len(mode_values) > 0 else None
                distribution_metrics["categorical"][col] = {
                    "unique_values": int(df[col].nunique()),
                    "mode": mode,
                    "frequency": frequency_dict
                }

            return {
                'message': 'Picklist Data distribution calculated',
                'distribution_metrics': distribution_metrics
            }




        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error computing data distribution: {str(e)}")