
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import database


app = FastAPI()


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=database.engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/todos", response_model=List[schemas.Task])
def get_todos(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks


@app.post("/task", response_model=schemas.Task, status_code=201)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.post("/toggle", response_model=schemas.Task)
def toggle_status(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.done = not task.done
    db.commit()
    db.refresh(task)
    return task


@app.post("/edit", response_model=schemas.Task)
def edit_task(request: schemas.EditTaskRequest, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(request.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if not request.edit_text:
        raise HTTPException(
            status_code=400, detail="Please enter text for your task"
        )
    task.content = request.edit_text
    db.commit()
    db.refresh(task)
    return task


@app.delete("/delete/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"result": "Task deleted", "id": task_id}


@app.post("/finished", response_model=List[schemas.Task])
def resolve_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    for task in tasks:
        if not task.done:
            task.done = True
    db.commit()
    return tasks
