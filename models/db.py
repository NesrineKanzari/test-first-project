from lib2to3.pytree import Base
from pymongo import MongoClient


class DBModel(Base):
    # __tablename__ = "TodoList"

    client = MongoClient(host='localhost', port=27017)
    db = client['TodoList']
    collection = db.collection
