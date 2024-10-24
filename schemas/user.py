from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str


class Token(BaseModel):
    access_token: str


class SignInRequest(BaseModel):
    email: str
    password: str
