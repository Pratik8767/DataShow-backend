 



from typing import Optional
from fastapi import APIRouter, Query

from src.outliers.outliers_services.outliers_services import OutliersService


class Outliers:
    router=APIRouter()

    @router.get('/data/outliers')
    async def get_outliers(
          x_column_name: Optional[str] = Query(None, description="Name of the X column"),
          y_column_name: Optional[str] = Query(None, description="Name of the Y column")
    ):
        try:
            response=OutliersService.outliers_service(x_column_name,y_column_name)
            return response
        except Exception as e:
            raise Exception(status_code=500,detail=str(e))