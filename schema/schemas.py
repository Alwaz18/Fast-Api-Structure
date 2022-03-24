from pydantic import BaseModel
from typing import Optional, List
from pydantic.main import BaseConfig


class OrderBase(BaseModel):
    title: str
    body: str


class Order(OrderBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    Orders: List[Order] = []

    class Config():
        orm_mode = True


class ShowOrder(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
