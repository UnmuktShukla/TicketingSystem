from fastapi import  Depends, FastAPI 
from contextlib import asynccontextmanager
from Auth.routes.auth import authRouter
from db.utils.protectedRoutes import getCurrentUser
from models.Auth_Entities import User


@asynccontextmanager
async def lifespan(app : FastAPI):
    yield

app = FastAPI(lifespan= lifespan)
app.include_router(router=authRouter , tags=["auth"] , prefix="/auth")

@app.get("/health")
async def get_index():
    return {
        "status" : "running"
    }

@app.get("/me")
async def get_user(user : User = Depends(getCurrentUser)):
    return {
        "user" : user
    }