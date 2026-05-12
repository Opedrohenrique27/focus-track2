import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskStats, TaskUpdate
from app.services.task_service import TaskService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, service: TaskService = Depends(get_task_service)):
    """Create a new task."""
    return service.create_task(data)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)):
    """List all tasks."""
    return service.list_tasks()


@router.get("/stats", response_model=TaskStats)
def get_stats(service: TaskService = Depends(get_task_service)):
    """Get task statistics for the dashboard."""
    return service.get_stats()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    """Get a specific task by ID."""
    return service.get_task(task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    """Update a task."""
    return service.update_task(task_id, data)


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    """Mark a task as completed."""
    return service.complete_task(task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    """Delete a task."""
    service.delete_task(task_id)
