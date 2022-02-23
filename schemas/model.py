from bson import ObjectId
from pydantic import BaseModel, Field


class Todo(BaseModel):
    title: str = Field(description='to do title', default='clean code')
    description: str = Field(alias='to d description', default='clean fast api code')

    # class Config:
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}
    #     schema_extra = {
    #         "example": {
    #             "title": "Task n1",
    #             "description": "Shower the cat",
    #
    #         }
    #     }
