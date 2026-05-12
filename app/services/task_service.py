import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskResponse, TaskStats, TaskUpdate

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, db: Session):
        self.repo = TaskRepository(db)

    def create_task(self, data: TaskCreate) -> TaskResponse:
        task = self.repo.create(data)
        return TaskResponse.model_validate(task)

    def list_tasks(self) -> list[TaskResponse]:
        tasks = self.repo.get_all()
        return [TaskResponse.model_validate(t) for t in tasks]

    def get_task(self, task_id: int) -> TaskResponse:
        task = self._get_or_404(task_id)
        return TaskResponse.model_validate(task)

    def update_task(self, task_id: int, data: TaskUpdate) -> TaskResponse:
        task = self._get_or_404(task_id)
        updated = self.repo.update(task, data)
        return TaskResponse.model_validate(updated)

    def complete_task(self, task_id: int) -> TaskResponse:
        task = self._get_or_404(task_id)
        update = TaskUpdate(completed=True)
        updated = self.repo.update(task, update)
        return TaskResponse.model_validate(updated)

    def delete_task(self, task_id: int) -> None:
        task = self._get_or_404(task_id)
        self.repo.delete(task)

    def get_stats(self) -> TaskStats:
        total = self.repo.count_all()
        completed = self.repo.count_completed()
        pending = total - completed
        total_time = self.repo.sum_estimated_time()
        rate = round((completed / total * 100), 1) if total > 0 else 0.0
        return TaskStats(
            total=total,
            completed=completed,
            pending=pending,
            total_estimated_time=total_time,
            completion_rate=rate,
        )

    def _get_or_404(self, task_id: int) -> Task:
        task = self.repo.get_by_id(task_id)
        if not task:
            logger.warning(f"Task not found: id={task_id}")
            raise HTTPException(status_code=404, detail="Task not found")
        return task
