from fastapi import FastAPI
from src.api.todo_app.todo_endpoint import todo as todo_app
router = FastAPI()
router.include_router(todo_app)
