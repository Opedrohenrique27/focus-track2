from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: str | None = Field(None, description="Task description")
    estimated_time: int = Field(
        0, ge=0, le=1440, description="Estimated time in minutes (max 24h)"
    )

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title must not be blank")
        return v.strip()


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    estimated_time: int | None = Field(None, ge=0, le=1440)
    completed: bool | None = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError("Title must not be blank")
        return v.strip() if v else v


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    estimated_time: int
    completed: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class TaskStats(BaseModel):
    total: int
    completed: int
    pending: int
    total_estimated_time: int
    completion_rate: float
