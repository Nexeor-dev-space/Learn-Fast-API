from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
async def read_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "fullname": current_user.fullname}
