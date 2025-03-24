import os
import uvicorn
from src.distribution_charts.distribution_api.distribution_api import Distribution
from fastapi import FastAPI
from src.cleanup.cleanup_api.cleanup_api import router as cleanup_router
from src.file.api.api import FileRouter
from fastapi.middleware.cors import CORSMiddleware 
# app = FastAPI()

app = FastAPI(
    title="Datashow API",
    description="These are the API's for Datashow Backend",
    # openapi_url="/management/openapi.json",
    docs_url="/datashow/docs",
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing); change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Include the router 
app.include_router(cleanup_router)
app.include_router(FileRouter.router)
app.include_router(Distribution.router)

# Run with: uvicorn main:app --reload

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use PORT from environment variables
    uvicorn.run(app, host="0.0.0.0", port=port)