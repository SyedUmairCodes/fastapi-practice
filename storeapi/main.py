# Imports
from fastapi import FastAPI

from storeapi.routers.post import router as post_router

# Main app and routers
app = FastAPI()
app.include_router(post_router)
