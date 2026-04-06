from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CreateTaskBody(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    priority: Optional[str] = "medium"


class UpdateTaskBody(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    status: Optional[str] = None
    priority: Optional[str] = None


class MoveTaskBody(BaseModel):
    status: str
    position: int = Field(default=0, ge=0)


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    position: int
    created_at: datetime

    model_config = {"from_attributes": True}


class TaskHistoryResponse(BaseModel):
    id: int
    field: str
    old_value: Optional[str]
    new_value: Optional[str]
    changed_by: int
    changed_at: datetime

    model_config = {"from_attributes": True}


class PaginationMeta(BaseModel):
    page: int
    per_page: int
    total: int
    pages: int


class TaskListResponse(BaseModel):
    data: list[TaskResponse]
    pagination: PaginationMeta
