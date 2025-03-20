

from fastapi import APIRouter, HTTPException

from src.distribution_charts.distribution_services.distribution_services import DistributionServices

class Distribution:

    router=APIRouter()

    @router.get('/data/distribution')
    async def get_data_distribution():
        try:
            response = DistributionServices.distribution_service()
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    @router.get('/data/picklist/distribution')
    async def get_picklist_data_distribution():
        try:
            response = DistributionServices.picklist_distribution_service()
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
