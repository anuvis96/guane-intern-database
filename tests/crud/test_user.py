import asyncio
from typing import Union

from app.CRUD.user import create_user
from app.schemas.user_schema import In_User_Schema, Out_User_Schema


user_default: In_User_Schema = In_User_Schema(
    name = "Daniel", 
    last_name = "Torres",
    email = "dan@mail.com",
    password = "hola",
)

def test_create_user(event_loop: asyncio.AbstractEventLoop):
    created_user = create_user(user_default)
    assert created_user.id is not None