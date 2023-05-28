###############################################################################
#
# 	STANDARD IMPORTS
#

from typing import Union, List

from enum import Enum

from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pydantic import EmailStr

# from beanie import Indexed

###############################################################################
#
# 	LOCAL IMPORTS
#

from ..models import BaseDocument

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


class Status(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class Task(BaseDocument):
    uuid: Union[UUID, None] = Field(default_factory=uuid4)
    description: str = Field(...)
    status: Status = Status.PENDING

    class Settings:
        name = "tasks"
        use_state_management = True

    class Config:
        schema_extra = {
            "example": {
                "uuid": "1e9896b5-e791-4b25-848b-f0afb792a8b7",
                "description": "counting characters task",
                "status": "RUNNING",
            }
        }


# Task.update_forward_refs()
