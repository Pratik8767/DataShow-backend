



from fastapi import APIRouter

from src.outliers.outliers_services.outliers_services import OutliersService


class Outliers:
    router=APIRouter()

    @router.get('/data/outliers')
    async def get_outliers():
        try:
            response=OutliersService.outliers_service()
            return response
        except Exception as e:
            raise Exception(status_code=500,detail=str(e))