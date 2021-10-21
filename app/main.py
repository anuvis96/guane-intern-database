from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from .debugger import initialize_fastapi_server_debugger_if_needed
from app.models import *
from app.routes.dog_routes import dog_router
from app.routes.user_routes import user_router
from app.config import Settings

application = FastAPI() 

def create_application() -> FastAPI:
    initialize_fastapi_server_debugger_if_needed()
    application = FastAPI()
    application.include_router(dog_router)
    application.include_router(user_router)
    return application

setting = Settings()

register_tortoise(application, db_url=setting.DB_URL, modules={"models": ["app.models"]}, generate_schemas=True, add_exception_handlers=True)
