import logging
from functools import lru_cache
from pydantic import BaseSettings, Field


log = logging.getLogger(__name__)

class Settings(BaseSettings):
    DB_URL: str = Field(...)
    CELERY_BROKER: str = 'localhots:5672//rabbitmq'
    CELERY_BACKEND = 'redis://localhost:6379'


class Auxiliar():
    NOMBRE: str


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()