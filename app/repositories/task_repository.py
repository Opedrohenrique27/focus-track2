import logging

from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

logger = logging.getLogger(__name__)


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        logger.info(f"Task created: id={task.id}")
        return task

    def get_all(self) -> list[Task]:
        return self.db.query(Task).order_by(Task.created_at.desc()).all()

    def get_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update(self, task: Task, data: TaskUpdate) -> Task:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        logger.info(f"Task updated: id={task.id}")
        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()
        logger.info(f"Task deleted: id={task.id}")

    def count_all(self) -> int:
        return self.db.query(Task).count()

    def count_completed(self) -> int:
        return self.db.query(Task).filter(Task.completed == True).count()  # noqa: E712

    def sum_estimated_time(self) -> int:
        result = self.db.query(Task.estimated_time).all()
        return sum(r[0] for r in result if r[0])
