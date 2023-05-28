###############################################################################
#
# 	STANDARD IMPORTS
#

from typing import List

from uuid import UUID

from fastapi import APIRouter


###############################################################################
#
# 	LOCAL IMPORTS
#

from .models import Task


###############################################################################
#
# 	GLOBAL VARIABLES
#

router = APIRouter(
    prefix="/tasks",
)


###############################################################################
#
# 	HELPER FUNCTIONS
#


@router.post("/")
async def create_task(task: Task) -> Task:
    return task


# @router.get("/{id}", status_code=200)
# async def list_tasks(*, task_id: UUID) -> List[Task]:
#     return {
#         "id": f"{id}",
#         "name": "hello world",
#     }
