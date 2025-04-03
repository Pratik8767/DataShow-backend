
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from src.cleanup.cleanup_services.cleanup_services import CleanUpService
from src.file.services.service import FileManagement


class OutliersService:

    def outliers_service()->dict:
        try:
            if FileManagement.temp_file_path is None:
                raise Exception('No file Uploaded!')
            file_path = CleanUpService.cleaned_file_path if CleanUpService.cleaned_file_path else FileManagement.temp_file_path
            print(f"🔹 File Path Used: {file_path}")
            df=pd.read_csv(file_path)

            x_column='Feature1' #independent variable!
            y_column='Feature2' #dependent variable!

            if x_column not in df.columns or y_column not in df.columns:
                raise Exception(f"Missing column(s) in data. Expected: {x_column}, {y_column}, Found: {df.columns.tolist()}")


            x=df[[x_column]]
            y=df[y_column] 

            
            print(f"📊 X (Feature1) Sample: \n{x.head()}")
            print(f"📊 Y (Feature2) Sample: \n{y.head()}")


            model=LinearRegression()
            model.fit(x,y)
            y_predict=model.predict(x)

            print(f"✅ Linear Regression Model Trained Successfully!")
            print(f"📈 Predicted Y Sample: \n{y_predict[:5]}")

            df['residuals'] = df[y_column] - y_predict.flatten()
            std_dev=np.std(df['residuals'])  
            threshold=2*std_dev
            df['is_outlier']=df['residuals'].abs()>threshold

            outliers=df[df['is_outlier']]

            print(f"⚠️ Number of Outliers Detected: {outliers.shape[0]}")
            print(f"🚨 Outliers Sample: \n{outliers[[x_column, y_column, 'residuals']].head()}")


            sorted_df = df.sort_values(by=x_column)
            regression_line = list(zip(sorted_df[x_column].tolist(), y_predict.tolist()))
            outlier_points = list(zip(outliers[x_column].tolist(), outliers[y_column].tolist()))


            output={'regression_line':regression_line,'outliers':outlier_points}
            print(f"✅ Output JSON Ready!")

            return output



        except Exception as e:
            raise Exception(f'error generating outliers:{e}')




