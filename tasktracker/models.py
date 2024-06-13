from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from tasktracker.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    position = Column(String)

    tasks = relationship("Task", back_populates="employee")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_task_id = Column(Integer, ForeignKey('tasks.id'), nullable=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    due_date = Column(Date)
    status = Column(Enum('not_started', 'in_progress', 'completed', name='status'))

    parent_task = relationship("Task", remote_side=[id])
    employee = relationship("Employee", back_populates="tasks")
