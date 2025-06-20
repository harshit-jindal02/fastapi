from pydantic import BaseModel


class TaskBase(BaseModel):
    content: str


class TaskCreate(TaskBase):
    pass


class EditTaskRequest(BaseModel):
    task_id: int
    edit_text: str


class Task(TaskBase):
    id: int
    done: bool

    class Config:
        orm_mode = True
