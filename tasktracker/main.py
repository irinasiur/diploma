from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from tasktracker.database import SessionLocal
import tasktracker.crud as crud
import tasktracker.models as models
import tasktracker.schemas as schemas
from tasktracker.database import engine
from tasktracker.routers import employees, tasks

from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем роутеры
app.include_router(employees.router)
app.include_router(tasks.router)


# Добавляем корневой эндпоинт для проверки
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Tracker API"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.get("/busy_employees/")
def read_busy_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()
    employees = sorted(employees, key=lambda e: len([t for t in e.tasks if t.status == 'in_progress']), reverse=True)
    return employees


@app.get("/important_tasks/")
def read_important_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.status == 'not_started').all()
    important_tasks = []
    for task in tasks:
        dependent_tasks = db.query(models.Task).filter(models.Task.parent_task_id == task.id,
                                                       models.Task.status == 'in_progress').all()
        if dependent_tasks:
            important_tasks.append(task)
    employees = db.query(models.Employee).all()
    least_loaded_employee = min(employees, key=lambda e: len([t for t in e.tasks if t.status == 'in_progress']))
    result = []
    for task in important_tasks:
        candidate_employees = [least_loaded_employee]
        parent_task = task.parent_task
        if parent_task and parent_task.employee:
            parent_employee = parent_task.employee
            if len([t for t in parent_employee.tasks if t.status == 'in_progress']) <= len([t for t in least_loaded_employee.tasks if t.status == 'in_progress']) + 2:
                candidate_employees.append(parent_employee)
        result.append({
            "important_task": task,
            "due_date": task.due_date,
            "candidate_employees": candidate_employees
        })
    return result
