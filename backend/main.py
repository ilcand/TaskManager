from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Task, Base
from pydantic import BaseModel
from typing import List

DATABASE_URL = "postgresql://postgres:postgres@db:5432/tasks_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskSchema(BaseModel):
    title: str
    description: str = ""
    status: bool = False

@app.get("/tasks", response_model=List[TaskSchema])
def get_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()

    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks available")

    return tasks

@app.post("/tasks")
def create_task(task: TaskSchema):
    session = SessionLocal()
    db_task = Task(**task.dict())
    session.add(db_task)
    session.commit()
    session.close()
    return {"message": "Task created"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = not task.status
    session.commit()
    session.close()
    return {"message": "Task updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    session.close()
    return {"message": "Task deleted"}