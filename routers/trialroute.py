import http

from fastapi import APIRouter
from fastapi import HTTPException


from schemas.model import Todo
from services.database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)

router = APIRouter(prefix="/trialroute")


@router.get("/api/todo")
async def get_todo():
    """

    :return: returns todos
    """
    response = await fetch_all_todos()
    return response


@router.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title) -> dict:
    """

    :param title: put the title you seek for
    :return: the todo
    """

    response = await fetch_one_todo(title)

    if response:
        return response
    raise HTTPException(http.HTTPStatus.NOT_FOUND, f"there is no todo item with this title{title}")


@router.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo) -> dict:
    """

    :param todo: new todo
    :return: NEW !
    """
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong / bad request")


@router.put("/api/todo/{title}", response_description="Update a todo",  response_model=Todo)
async def put_todo(title: str, desc: str) -> dict:
    """

    :param title: UPDATE the latest title
    :param desc: UPDATE the latest description
    :return: UPDATED content
    """
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(http.HTTPStatus.NOT_FOUND, f"there is no todo item with this title{title}")


@router.delete("/api/todo/{title}")
async def delete_todo(title) -> str:
    """

    :param title: The title you wanna delete
    :return: DELETED TODO
    """
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo item"
    raise HTTPException(http.HTTPStatus.NOT_FOUND, f"there is no todo item with this title{title}")
