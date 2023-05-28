###############################################################################
#
# 	STANDARD IMPORTS
#

import os

import enum
from typing import Optional, Union

from pydantic import BaseSettings

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


###############################################################################
#
# 	CLASS DEFINITIONS
#


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # Current environment
    environment: str = os.environ.get("ENVIRONMENT", "local")

    application_name: str = os.environ.get(
        "APPLICATION_NAME", f"[{environment}] Generic Fast API Application."
    )
    application_description: str = os.environ.get(
        "APPLICATION_DESCRIPTION",
        f"[{environment}] Boilerplate for building the Fast API.",
    )

    host: str = "127.0.0.1"
    port: int = 5000

    origins = [
        f"http://{host}:{port}",
        f"https://{host}:{port}"
        # local
        "http://127.0.0.1",
        "http://localhost:5000",
        # add the deployed URL
    ]

    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Log

    #   override log level
    #       by using local envionment
    log_level: Union[int, str] = LogLevel.INFO.value

    # Monitoring & Error Tracking

    #   Sentry
    sentry_dsn: Optional[str] = os.environ.get("SENTRY_DSN", None)
    sentry_sample_rate: float = 0.1


settings = Settings()
