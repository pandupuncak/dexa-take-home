from pydantic import BaseModel

class TasksBase(BaseModel):
    title: str
    description: str
    status: str

class Tasks(TasksBase):
    id: int
    class Config:
        orm_mode = True