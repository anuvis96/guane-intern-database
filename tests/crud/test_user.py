import asyncio
from typing import Union

from app.CRUD.user import create_user as userCRUD_create
from app.schemas.user_schema import In_User_Schema, Out_User_Schema


user_default: In_User_Schema = In_User_Schema(
    name="Daniel",
    last_name="Torres",
    email="dan@mail.com",
    password="hola",
    create_date="2021-11-22 23:59:59"
)


def test_create_user(event_loop: asyncio.AbstractEventLoop):
    created_user = create_user(event_loop, user_default)
    assert created_user.name == "Daniel"
    assert created_user.last_name == "Torres"
    #assert created_user.__dict__.items() >= user_default.__dict__.items()  
    # Se recibe la data se convierte a un dic, luego a una lista con el items() para operarlo (>=) 
    # Ver que lo que me retorna es congruente con lo que envie



def create_user(event_loop: asyncio.AbstractEventLoop, user_default: In_User_Schema):
    create_user_test = event_loop.run_until_complete(
        userCRUD_create(user_default))
    return create_user_test 
    
