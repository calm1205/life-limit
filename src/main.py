from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import birth, health, root, limit

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(root.router)
app.include_router(health.router, prefix="/health")
app.include_router(birth.router, prefix="/birth")
app.include_router(limit.router, prefix="/limit")