from fastapi import APIRouter, HTTPException
from crud.user import user_crud
from schemas.user import UserCreate

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate):
    return user_crud.create_user(user)

@router.get("/users/")
def get_users():
    return user_crud.get_users()

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = user_crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
def update_user(user_id: str, user: UserCreate):
    return user_crud.update_user(user_id, user)

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return user_crud.delete_user(user_id)
