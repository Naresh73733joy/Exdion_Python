# app/domain/user.py
from random import randint
from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime

class UserOut(BaseModel):
    id: int = Field(default_factory=lambda: randint(1, 100))
    name: str
    creation_date: datetime = Field(default_factory=datetime.now)

class UserIn(BaseModel):
    name: Annotated[str, Field(example="my-username", min_length=3)]
    password: Annotated[str, Field(example="secret", min_length=5)]

    class Config:
        orm_mode = True  # Allow Pydantic models to read data from SQLAlchemy models