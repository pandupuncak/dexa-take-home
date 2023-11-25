from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app = FastAPI(title="Dexa Take Home Test")

@app.get("/tasks", response_model = List, tags = ["getters"])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks/", response_model = schemas.Tasks, tags=["create"])
def create_task(task : schemas.TasksBase,db: Session = Depends(get_db)):
    
    db_task = crud.create_task(db, task)
    return db_task


@app.get("/tasks/{id_task}", response_model=schemas.Tasks, tags=["getters"])
def get_task(id_task: int, db: Session = Depends(get_db)):
    return crud.get_task(db,id_task)

@app.patch("/tasks/{id_task}", response_model = schemas.Tasks, tags=["update"])
def update_task(id_task: int, status : str, db: Session = Depends(get_db)):
    crud.update_task_status(db, id_task, status)# tambahin exception kalau salah
    task = crud.get_task(db, id_task)
    return task

@app.delete("/tasks/{id_task}", tags=["delete"])
def delete_task(id_task: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, id_task)
    delete_response = {
        "task_id" : db_task.id,
        "task_title" : db_task.title,
        "status" : "deleted"
    }
    return delete_response