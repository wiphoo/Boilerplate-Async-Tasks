###############################################################################
#
# 	STANDARD IMPORTS
#

import logging

import uvicorn

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import UJSONResponse

from fastapi.security import HTTPBearer

from fastapi.middleware.cors import CORSMiddleware

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

###############################################################################
#
# 	LOCAL IMPORTS
#

from .settings import settings

from .utils.lifetime import register_startup_event, register_shutdown_event

from .routers import health_router
from .routers import api_router


###############################################################################
#
# 	GLOBAL VARIABLES
#


###############################################################################
#
# 	HELPER FUNCTIONS
#


def app() -> FastAPI:
    ###############################################################################
    #   Application object                                                        #
    ###############################################################################

    ###############################################################################
    #   Logging configuration                                                     #
    ###############################################################################

    ###############################################################################
    #   Trace configuration                                                     #
    ###############################################################################

    if (
        settings.sentry_dsn
        and settings.environment
        and settings.environment.lower() != "local"
    ):
        # Enables sentry integration.
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            traces_sample_rate=settings.sentry_sample_rate,
            environment=settings.environment,
            integrations=[
                FastApiIntegration(transaction_style="endpoint"),
                LoggingIntegration(
                    level=logging.INFO,
                    event_level=logging.ERROR,
                ),
            ],
        )

    app = FastAPI(
        title=settings.application_name,
        description=settings.application_description,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    ###############################################################################
    #   startup/shutdown configuration                                            #
    ###############################################################################

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    ###############################################################################
    #   Error handlers configuration                                              #
    ###############################################################################

    ###############################################################################
    #   Middlewares configuration                                                 #
    ###############################################################################

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ###############################################################################
    #   Routers configuration                                                     #
    ###############################################################################

    # Main router for the API.

    #   Monitoring
    app.include_router(
        router=health_router,
        prefix="/api/monitoring",
    )

    #   APIs
    app.include_router(
        router=api_router,
        prefix="/api",
    )

    ###############################################################################
    #   Handler                                                                   #
    ###############################################################################

    # handler = Mangum(app)

    return app


###############################################################################
#
# 	CLASS DEFINITIONS
#


###############################################################################
#
# 	Main
#


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        app(),
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level,
        factory=True,
    )


###############################################################################
#   Run the self contained application                                        #
###############################################################################

if __name__ == "__main__":
    main()
