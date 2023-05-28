###############################################################################
#
# 	STANDARD IMPORTS
#

from typing import Any, AsyncGenerator

import pytest

from httpx import AsyncClient

from fastapi import FastAPI


###############################################################################
#
# 	LOCAL IMPORTS
#

from ..app import app


###############################################################################
#
# 	GLOBAL VARIABLES
#


###############################################################################
#
# 	HELPER FUNCTIONS
#


###############################################################################
#
# 	TEST DEFINITIONS
#


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.
    :return: backend name.
    """
    return "asyncio"


@pytest.fixture
def fastapi_app() -> FastAPI:
    """
    Fixture for creating FastAPI app.
    :return: fastapi app with mocked dependencies.
    """
    application = app()
    return application  # noqa: WPS331


@pytest.fixture
async def client(
    fastapi_app: FastAPI, anyio_backend: Any
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.
    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with (AsyncClient(app=fastapi_app, base_url="http://test") as ac,):
        yield ac


@pytest.fixture
async def request_header() -> dict:
    return {
        "Content-Type": "application/json",
        "accept": "application/json",
        "Authorization": "Bearer abcd1234",
    }
