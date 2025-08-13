from typing import Dict, List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from src.models.todo_models import Todo

todos_db: Dict[str, Todo] = {}

class CRUD:
    @staticmethod
    def create_todo(todo_create: Todo) -> Todo:
        todo_id = uuid4()
        todo = Todo(
            id=todo_id,
            title=todo_create.title,
            completed=todo_create.completed or False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        todos_db[str(todo_id)] = todo
        return todo

    @staticmethod
    def list_todos() -> List[Todo]:
        return list(todos_db.values())

    @staticmethod
    def update_todo(todo_id: UUID, todo_update: Todo) -> Optional[Todo]:
        key = str(todo_id)
        if key not in todos_db:
            return None

        todo = todos_db[key]
        update_data = todo_update.model_dump(exclude_unset=True)
        updated_todo = todo.model_copy(update={**update_data, "updated_at": datetime.now()})
        todos_db[key] = updated_todo
        return updated_todo

    @staticmethod
    def delete_todo(todo_id: UUID) -> bool:
        return todos_db.pop(str(todo_id), None) is not None
