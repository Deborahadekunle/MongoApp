from fastapi import APIRouter, HTTPException
from crud.todo import todo_crud  # ✅ Use absolute import
from schemas.todo import TodoCreate

router = APIRouter()

@router.post("/todos/")
def create_todo(todo: TodoCreate):
    return todo_crud.create_todo(todo)

@router.get("/todos/")
def get_todos():
    return todo_crud.get_todos()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    todo = todo_crud.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: TodoCreate):
    return todo_crud.update_todo(todo_id, todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    return todo_crud.delete_todo(todo_id)
