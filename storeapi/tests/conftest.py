# Imports
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

# Manage table states
from storeapi.main import app
from storeapi.routers.post import comment_table, post_table


# Configuring the async test runner
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# Test client
@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


# DB Cleaner
@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield


# Test client
@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
