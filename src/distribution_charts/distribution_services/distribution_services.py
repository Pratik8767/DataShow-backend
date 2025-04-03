from fastapi import HTTPException
import pandas as pd
from src.cleanup.cleanup_services.cleanup_services import CleanUpService
from src.file.services.service import FileManagement


class DistributionServices:
    """Class to provide distribution services"""

    @staticmethod
    def distribution_service() -> dict:
        try:
            # Check if a file is uploaded
            if FileManagement.temp_file_path is None:
                raise ValueError("No file uploaded")

            # Determine which file to use (cleaned or original)
            file_path = CleanUpService.cleaned_file_path if CleanUpService.cleaned_file_path else FileManagement.temp_file_path
            df = pd.read_csv(file_path)

            # Selecting numerical columns
            numerical_cols = df.select_dtypes(include=['number']).columns
            if len(numerical_cols) == 0:
                raise HTTPException(status_code=400, detail="No numerical columns found.")

            distribution_metrics = {"numerical": []}
            chart_limits = {
                "max_range": 0,
                "max_variance": 0,
                "max_standard_deviation": 0,
                "max_interquartile_range": 0,
            }

            # Computing numerical data distribution
            for col in numerical_cols:
                min_val = df[col].min()
                max_val = df[col].max()
                range_val = max_val - min_val
                variance = df[col].var()
                std_dev = df[col].std()
                iqr = df[col].quantile(0.75) - df[col].quantile(0.25)

                # Append to the numerical metrics list
                distribution_metrics["numerical"].append({
                    "column_name": col,
                    "range": float(range_val),
                    "variance": float(variance),
                    "standard_deviation": float(std_dev),
                    "interquartile_range": float(iqr),
                })

                # Update chart limits
                chart_limits["max_range"] = max(chart_limits["max_range"], float(max_val))
                chart_limits["max_variance"] = max(chart_limits["max_variance"], float(variance))
                chart_limits["max_standard_deviation"] = max(chart_limits["max_standard_deviation"], float(std_dev))
                chart_limits["max_interquartile_range"] = max(chart_limits["max_interquartile_range"], float(iqr))

            return {
                "message": "Data distribution calculated",
                "distribution_metrics": distribution_metrics,
                "chart_limits": chart_limits
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

            if CleanUpService.cleaned_file_path:
                            df = pd.read_csv(CleanUpService.cleaned_file_path)
                            # print('clened file')
            else:
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






            