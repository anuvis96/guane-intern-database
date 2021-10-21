import asyncio
import os

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.core.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(
        TESTING=1, DEBUGGER=False, DATABASE_TEST_URL="sqlite://:memory"
    )


@pytest.fixture(scope="function", autouse=True)
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings]