from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate):
    return {
        "message": "User received",
        "user": user
    }
