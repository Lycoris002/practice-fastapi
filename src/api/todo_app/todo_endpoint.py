from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from src.utils.db_utils import create_database_session
from src.models.todo_models import Todo


router = APIRouter()

# Create new Todo List
@app.post("/create_new_todo_list", response_model=TodoResponse)
async def create_todo_list(
    todo: TodoCreate,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    new_todo = Todo(
        id=uuid.uuid4(),
        title=todo.title,
        description=todo.description
    )
    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)
    return new_todo
# Get Todo List
@app.get("/todo_list", response_model=List[Todo])
async def get_todo_list(session: Annotated[AsyncSession, Depends(create_database_session)]):
    result = await session.execute(select(Todo))
    todos = result.scalars().all()
    return todos

# Update Todo List
@app.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(
        todo_id: str,
        todo_update: TodoUpdate,
        session: Annotated[AsyncSession, Depends(create_database_session)]
):
    result = await session.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    if todo_update.title is not None:
        todo.title = todo_update.title
    if todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.completed is not None:
        todo.completed = todo_update.completed

    await session.commit()
    await session.refresh(todo)
    return todo


# Delete Todo List
@app.delete("/todos/{todo_id}")
async def delete_todo(
        todo_id: str,
        session: Annotated[AsyncSession, Depends(create_database_session)]
):
    result = await session.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    await session.delete(todo)
    await session.commit()
    return {"message": "Todo deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
