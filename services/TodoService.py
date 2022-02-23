from typing import Any

from schemas.model import Todo
from services.service import AppCRUD, AppService
from utils.app_exceptions import AppException
from utils.service_result import ServiceResult


class TodoService(AppService):
    def create_item(self, item: Todo) -> ServiceResult:
        todo_item = TodoCRUD(self.db).create_item(item)
        if not todo_item:
            return ServiceResult(AppException.TodoCreateItem())
        return ServiceResult(todo_item)

    def get_item(self, item_id: int) -> ServiceResult:
        todo_item = TodoCRUD(self.db).get_item(item_id)
        if not todo_item:
            return ServiceResult(AppException.TodoGetItem({"item_id": item_id}))
        return ServiceResult(todo_item)


class TodoCRUD(AppCRUD):
    def create_item(self, item: Todo) -> Todo:
        todo_item = Todo()
        self.db.add(todo_item)
        self.db.commit()
        self.db.refresh(todo_item)
        return todo_item

    def get_item(self, item_id: int) -> Any | None:
        foo_item = self.db.query(Todo).filter(Todo.id == item_id).first()
        if foo_item:
            return foo_item
        return None
