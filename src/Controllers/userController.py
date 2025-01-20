from datetime import datetime
from random import randint
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from src.Core.auth import validate_token
from src.Models.userModel import UserOut, UserIn 

user_router = APIRouter()

@user_router.get("/api/User/GetUserDetailsByName/{name}", response_model=UserOut, tags=["Users"], dependencies=[Depends(validate_token)])
def get_user(name: Annotated[str, Path(min_length=3)]) -> UserOut:
    try:
        return UserOut(id=10, name=name, creation_date=datetime.now())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.post("/api/User/CreateNewUser", response_model=UserOut, tags=["Users"], dependencies=[Depends(validate_token)])
def create_user(user: UserIn) -> UserOut:
    return UserOut(id=randint(1, 100), name=user.name, creation_date=datetime.now())
