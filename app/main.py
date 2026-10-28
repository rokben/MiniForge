from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database.database import init_db


from .routes.auth import router_auth

@asynccontextmanager
async def lifespan(app: FastAPI): 
    # Init the miniforge database
    init_db()
    yield
    
app = FastAPI(
    title = "MiniForge",
    description= "A lightweight Git forge", 
    lifespan=lifespan
)

app.include_router(router_auth)