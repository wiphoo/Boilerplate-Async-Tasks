###############################################################################
#
# 	STANDARD IMPORTS
#

from fastapi import APIRouter

###############################################################################
#
# 	LOCAL IMPORTS
#


###############################################################################
#
# 	GLOBAL VARIABLES
#

router = APIRouter(
    tags=["monitoring"],
)


###############################################################################
#
# 	HELPER FUNCTIONS
#


###############################################################################
#
# 	CLASS DEFINITIONS
#


@router.get("/health", status_code=200, dependencies=[])
def health_check() -> None:
    """
    Checks the health of a project.
    It returns 200 if the project is healthy.
    """
    pass
