from sqlalchemy.orm import Session
from sqlalchemy import select, Row
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.sql.expression import delete

from sql_app import database
from . import models, schemas

def get_tasks(db: Session):
    list_tasks = []
    for row in db.execute(select(models.Tasks)):
        task = {
            "id" : row.Tasks.id,
            "title" : row.Tasks.title,
            "description" : row.Tasks.description,
            "status" : row.Tasks.status
        }
        list_tasks.append(task)
    return list_tasks

def get_task(db: Session, tasks_id: int):
    # result = db.execute(select(models.Tasks).where(models.Tasks.id == tasks_id))
    # print(result[0])
    return db.query(models.Tasks).filter(models.Tasks.id == tasks_id).first()

def get_task_by_title(db: Session, tasks_title: str):
    return db.query(models.Tasks).filter(models.Tasks.title == tasks_title)

def create_task(db: Session, task: schemas.TasksBase):
    db_task = models.Tasks(title = task.title, description = task.description, status = task.status)
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task_status(db: Session, id: int, status: str):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == id).update({"status" : status},synchronize_session="fetch")
    db.commit()
    # db.refresh(db_task)
    
def delete_task(db: Session, tasks_id: int):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == tasks_id).first()
    db.delete(db_task)
    db.commit()
    return db_task