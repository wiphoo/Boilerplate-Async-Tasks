###############################################################################
#
# 	STANDARD IMPORTS
#

from typing import Awaitable, Callable

from fastapi import FastAPI


###############################################################################
#
# 	LOCAL IMPORTS
#


###############################################################################
#
# 	GLOBAL VARIABLES
#


###############################################################################
#
# 	HELPER FUNCTIONS
#


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.
    This function uses fastAPI app to store data
    inthe state, such as db_engine.
    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _on_startup() -> None:
        """Initialize services on startup."""
        pass

    return _on_startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.
    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _on_shutdown() -> None:  # noqa: WPS430
        pass

    return _on_shutdown
