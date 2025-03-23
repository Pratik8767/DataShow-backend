import os
import uvicorn
from src.distribution_charts.distribution_api.distribution_api import Distribution
from fastapi import FastAPI
from src.cleanup.cleanup_api.cleanup_api import router as cleanup_router
from src.file.api.api import FileRouter
# app = FastAPI()

app = FastAPI(
    title="Datashow API",
    description="These are the API's for Datashow Backend",
    # openapi_url="/management/openapi.json",
    docs_url="/datashow/docs",
)
# Include the router 
app.include_router(cleanup_router)
app.include_router(FileRouter.router)
app.include_router(Distribution.router)

# Run with: uvicorn main:app --reload

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use PORT from environment variables
    uvicorn.run(app, host="0.0.0.0", port=port)