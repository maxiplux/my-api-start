from fastapi import APIRouter, HTTPException
from fastapi.params import Depends


from app.auth.Users import User
from app.auth.security import fastapi_users

router = APIRouter()

@router.get("/not_timed")
async def not_timed():
    return {"message": "Not timed"}


@router.get("/timed")
async def timed():
    return {"message": "It's the time of my life"}


@router.get("/optional-user-route")
def optional_user_route(user: User = Depends(fastapi_users.get_optional_current_active_user)):
    if user:
        return f"Hello, {user.email}"

    raise HTTPException(status_code=403, detail="Not Autorized")