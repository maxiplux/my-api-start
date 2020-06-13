from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.db import MongoDBUserDatabase

from app.apps.controllers import example
from app.auth.Users import on_after_register, on_after_forgot_password, UserDB, UserCreate, User, \
    UserUpdate
from app.auth.security import fastapi_users
from app.settings.auth import JWT_AUTHENTICATION, SECRET
from app.settings.database import users_collections

app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}




app.include_router(fastapi_users.get_auth_router(JWT_AUTHENTICATION), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(SECRET, after_forgot_password=on_after_forgot_password),
                   prefix="/auth", tags=["auth"], )
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

app.include_router(example.router, prefix="/example")
