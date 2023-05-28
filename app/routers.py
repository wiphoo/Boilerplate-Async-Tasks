##############################################################################
#
# 	STANDARD IMPORTS
#

from fastapi.routing import APIRouter

###############################################################################
#
# 	LOCAL IMPORTS
#

from .api.monitoring.health import (
    router as health_router,
)  # noqa # pylint: disable=unused-import

from .api.v1 import router as api_v1_router


###############################################################################
#
# 	GLOBAL VARIABLES
#

api_router = APIRouter()

api_router.include_router(api_v1_router, prefix="/v1", tags=["v1"])


###############################################################################
#
# 	HELPER FUNCTIONS
#


###############################################################################
#
# 	CLASS DEFINITIONS
#
