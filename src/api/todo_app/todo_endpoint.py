from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from src.utils.db_utils import create_database_session
from src.models.todo_models import Todo
from src.utils.db_utils import CRUD

todo = APIRouter()

# Create new Todo List
@todo.post("/todos", response_model=Todo)
def create_new_todo():
    return CRUD.create_todo(Todo)

# Get Todo List
@todo.get("/todos", response_model=List[Todo])
def get_todo_list():
    return CRUD.list_todos()

# Update Todo List
@todo.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: UUID, todo_update: Todo):
    return CRUD.update_todo(todo_id, todo_update)

# Delete Todo List
@todo.delete("/todos/{todo_id}")
def delete_todo(todo_id: UUID):
    check = CRUD.delete_todo(todo_id)
    if not check:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
