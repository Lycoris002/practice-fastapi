from fastapi import APIRouter
from src.api.todo_app.todo_endpoint import todo as todo_app

router = APIRouter()

router.include_router(todo_app)