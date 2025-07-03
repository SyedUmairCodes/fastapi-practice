# Imports
import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

# Change working environment to test mode
os.environ["ENV_STATE"] = "test"

from storeapi.database import database
from storeapi.main import app


# Configuring the async test runner
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# Test client
@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


# DB Connecter
@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    yield
    await database.disconnect()


# Test client
@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
