###############################################################################
#
# 	STANDARD IMPORTS
#

from datetime import datetime

from pydantic.fields import Field

# from beanie import Document
from pydantic import BaseModel, Field


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


class BaseDocument(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
