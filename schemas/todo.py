from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    user_id: str
    title: str
    description: str
    is_completed: Optional[bool] = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: str
