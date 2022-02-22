import motor.motor_asyncio

from config.db_config import database_config
from schemas.model import Todo

# connection to mongodb
# TODO : compose env variables :  DONE
client = motor.motor_asyncio.AsyncIOMotorClient(database_config.URL, uuidRepresentation="standard")
# Access Database
database = client.TodoList
# Access Collection of the database
collection = database.todo


async def fetch_one_todo(title: str) -> dict:
    """

    :param title: Any existent title you wanna seek for
    :return: the todo searched for
    """
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    """

    :return: return all assigned todos
    """
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo: dict) -> dict:
    """

    :param:  write both title and description of the vaunted todo
    :return: created todo
    """
    document = todo
    # result = await collection.insert_one(document)
    return document


async def update_todo(title: str, desc: str) -> dict:
    """

    :param title: insert the title you want to update
    :param desc: same for des
    :return:
    """
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title: str) -> bool:
    """

    :param title: put the title you wanna delete
    :return: todo deleted
    """
    await collection.delete_one({"title": title})
    return True
