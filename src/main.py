from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from src.api.api import File


app = FastAPI(
    title="CSV Analyzer API",
    description="These are the API's for CSV Analyzer Backend",
    # openapi_url="/management/openapi.json",
    docs_url="/csv/docs",
)

app.include_router(File.router, tags=["File API"])