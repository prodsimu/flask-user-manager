from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CreateProjectBody(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)


class UpdateProjectBody(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class PaginationMeta(BaseModel):
    page: int
    per_page: int
    total: int
    pages: int


class ProjectListResponse(BaseModel):
    data: list[ProjectResponse]
    pagination: PaginationMeta
