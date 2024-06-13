from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum


class Status(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed = "completed"


class TaskBase(BaseModel):
    name: str
    parent_task_id: Optional[int] = None
    employee_id: Optional[int] = None
    due_date: date
    status: Status


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    full_name: str
    position: str


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True
