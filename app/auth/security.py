from fastapi_users import FastAPIUsers
from fastapi_users.db import MongoDBUserDatabase

from app.auth.Users import UserDB, User, UserCreate, UserUpdate
from app.settings.auth import JWT_AUTHENTICATION
from app.settings.database import users_collections

fastapi_users = FastAPIUsers(MongoDBUserDatabase(UserDB, users_collections), [JWT_AUTHENTICATION], User, UserCreate,UserUpdate, UserDB)
