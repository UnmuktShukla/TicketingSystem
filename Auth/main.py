from fastapi import  FastAPI 
from contextlib import asynccontextmanager
from db.utils.init_db import create_tables 
from Auth.routes.auth import authRouter


@asynccontextmanager
async def lifespan(app : FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan= lifespan)
app.include_router(router=authRouter , tags=["auth"] , prefix="/auth")

@app.get("/health")
async def get_index():
    return {
        "status" : "running"
    }